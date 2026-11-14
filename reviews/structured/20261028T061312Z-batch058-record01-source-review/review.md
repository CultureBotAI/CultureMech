# Caldinitratiruptor microaerophilus: preserve JCM782 batch and stock bases

- Review: 20261028T061312Z-batch058-record01-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T06:08:52.425624Z
- Finished UTC: 2026-10-28T06:13:12.341166Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The selected TOGO M812 import has water and three stock additions represented in mass-per-liter units, unsupported main-batch rate assertions, empty stock shells and missing JCM preparation. Exact source quantities and a repaired trace-mineral dependency are credited separately. A current legacy potassium-nitrate linkage remains unresolved.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch058 native selection index 01.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010224 | data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml | generated | caldinitratiruptor_microaerophilus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010224 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:010224 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:010224 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:010224 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact source lineage

identity: supported. Targets: CultureMech:010224.

The generated record has one exact TOGO M812 maintained contributor. Current TOGO identifies original JCM782 and both sources name the same recipe. Historical reports mention another JCM-generated record; it is comparison context, not an additional selected owner or authority to merge unequal formulations.

### Classification and source roles

scope: supported. Targets: CultureMech:010224.

COMPLEX/UNDEFINED and LIQUID agree with yeast extract and a liquid recipe. Ingredient role annotations are retained as imported TOGO assertions, not independently proved mechanisms. No strain-level growth is inferred from the medium name.

### Source form and current catalog

grounding: supported. Targets: CultureMech:010224.

The current source-compatible primary salt/hydrate IDs are retained. Potassium nitrate CHEBI:63043 agrees chemically; its legacy MediaIngredientMech:000170 slot is absent from the current catalog. Yeast extract remains an undefined mixture without a fabricated CHEBI identity. Scoped MnSO4·xH2O in M142 has an unresolved hydration count: CHEBI:86360 describes manganese sulfate without specifying that hydrate; no exact-hydrate claim or conversion is made.

### Current writers and historical evidence

provenance: supported. Targets: CultureMech:010224.

The current TOGO importer separates primary stocks and captures comments but bare-unit normalization still does not prove a final-liter basis. The current merger copies a sole contributor and preserves exact formulation assertions when merging multiple inputs. Historical reviews are derivative; their recommendation to treat every stock as mL/L or merge related records is not automatically adopted.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:010224.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Distilled water", "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[0].items[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo": "http://purl.jp/bio/10/gmo/GMO_001001", "gmo_id": "GMO_001001", "label": "Distilled water", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044", "label": "Solvating media"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The source supplies 1 L distilled water as a batch solvent input, not 1 g/L water. Retain the liquid volume and do not use it as an explicit final-medium volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source supplies 1 L distilled water as a batch solvent input, not 1 g/L water. Retain the liquid volume and do not use it as an explicit final-medium volume."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source supplies 1 L distilled water as a batch solvent input, not 1 g/L water. Retain the liquid volume and do not use it as an explicit final-medium volume."}]}, {"quantity_id": "q2", "topic": "Yeast extract", "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[0].items[1]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"Yeast extract\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Yeast extract", "volume": 1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001003", "gmo_id": "GMO_001003", "label": "Yeast extract", "properties": [{"id": "GMO_000047", "uri": "http://purl.jp/bio/10/gmo/GMO_000047", "label": "Undefined component"}], "roles": [{"id": "GMO_000042", "uri": "http://purl.jp/bio/10/gmo/GMO_000042", "label": "Nutrient source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "The source directly supports 1 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 1 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 1 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}]}, {"quantity_id": "q3", "topic": "NaCl", "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[0].items[2]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "NaCl", "volume": 1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001004", "gmo_id": "GMO_001004", "label": "Sodium chloride", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "The source directly supports 1 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 1 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 1 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}]}, {"quantity_id": "q4", "topic": "CaCl2・2H2O", "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[0].items[3]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "CaCl2・2H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001005", "gmo_id": "GMO_001005", "label": "Calcium chloride dihydrate", "properties": [{"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "The source directly supports 0.1 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 0.1 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 0.1 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}]}, {"quantity_id": "q5", "topic": "KH2PO4", "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[0].items[4]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "KH2PO4", "volume": 0.3, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001006", "gmo_id": "GMO_001006", "label": "Potassium phosphate monobasic", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038", "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "The source directly supports 0.3 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 0.3 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 0.3 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}]}, {"quantity_id": "q6", "topic": "NH4Cl", "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[0].items[5]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "NH4Cl", "volume": 1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001008", "gmo_id": "GMO_001008", "label": "Ammonium chloride", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000062", "uri": "http://purl.jp/bio/10/gmo/GMO_000062", "label": "Nitrogen source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "The source directly supports 1 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 1 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 1 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}]}, {"quantity_id": "q7", "topic": "K2HPO4", "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[0].items[6]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"K2HPO4\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\": \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "K2HPO4", "volume": 0.3, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001009", "gmo_id": "GMO_001009", "label": "Potassium phosphate dibasic", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038", "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "The source directly supports 0.3 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 0.3 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 0.3 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}]}, {"quantity_id": "q8", "topic": "MgCl2・6H2O", "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[0].items[7]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.25,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "MgCl2・6H2O", "volume": 0.25, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001013", "gmo_id": "GMO_001013", "label": "Magnesium chloride hexahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "The source directly supports 0.25 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 0.25 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 0.25 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}]}, {"quantity_id": "q9", "topic": "KCl", "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[0].items[8]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"KCl\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\": \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "KCl", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001017", "gmo_id": "GMO_001017", "label": "Potassium chloride", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "The source directly supports 0.1 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 0.1 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 0.1 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}]}, {"quantity_id": "q10", "topic": "KNO3", "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[0].items[9]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"KNO3\",\n          \"volume\": 1.7,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001056\",\n          \"gmo_id\": \"GMO_001056\",\n          \"label\": \"Potassium nitrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "KNO3", "volume": 1.7, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001056", "gmo_id": "GMO_001056", "label": "Potassium nitrate", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "The source directly supports 1.7 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "1.7", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 1.7 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "1.7", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports 1.7 g of this exact component per initial recipe batch, but does not state a final medium volume. The local unchanged number in G_PER_L is therefore unsupported as a final-medium rate. The provider separately reports g_l on volume1055 mL; preserve that declared comparison without replacing the original batch basis or inventing a final concentration."}]}, {"quantity_id": "q11", "topic": "KOH", "source": {"sources": [{"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[0].items[11]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"KOH\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\": \"GMO_001903\",\n          \"label\": \"Potassium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "KOH", "gmo": "http://purl.jp/bio/10/gmo/GMO_001903", "gmo_id": "GMO_001903", "label": "Potassium hydroxide solution", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051", "label": "Solution"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.comments[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }", "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix components thoroughly, adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):"}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}]}, "decision": "not_quantified", "rationale": "KOH is the source-explicit pH-adjustment reagent; no fixed dose or stock strength is given. VARIABLE is not a measured concentration. Retain the reagent as scoped preparation with pH7.2, rather than a nominal nutrient rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "KOH is the source-explicit pH-adjustment reagent; no fixed dose or stock strength is given. VARIABLE is not a measured concentration. Retain the reagent as scoped preparation with pH7.2, rather than a nominal nutrient rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "KOH is the source-explicit pH-adjustment reagent; no fixed dose or stock strength is given. VARIABLE is not a measured concentration. Retain the reagent as scoped preparation with pH7.2, rather than a nominal nutrient rate."}]}, {"quantity_id": "q12", "topic": "Carbon dioxide gas", "source": {"sources": [{"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[0].items[12]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\": \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Carbon dioxide gas", "gmo": "http://purl.jp/bio/10/gmo/GMO_002260", "gmo_id": "GMO_002260", "label": "Carbon dioxide gas", "properties": [{"id": "GMO_000077", "uri": "http://purl.jp/bio/10/gmo/GMO_000077", "label": "ガス"}], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.comments[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }", "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix components thoroughly, adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):"}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}]}, "decision": "not_quantified", "rationale": "This source gas is part of the explicit N2–CO2 4:1 v/v atmosphere, not a measured dissolved ingredient concentration. The gas mixture is quantified, but neither gas delivery volume nor dissolved concentration is supplied; retain the atmospheric role and ratio.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "This source gas is part of the explicit N2–CO2 4:1 v/v atmosphere, not a measured dissolved ingredient concentration. The gas mixture is quantified, but neither gas delivery volume nor dissolved concentration is supplied; retain the atmospheric role and ratio."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "This source gas is part of the explicit N2–CO2 4:1 v/v atmosphere, not a measured dissolved ingredient concentration. The gas mixture is quantified, but neither gas delivery volume nor dissolved concentration is supplied; retain the atmospheric role and ratio."}]}, {"quantity_id": "q13", "topic": "Nitrogen gas", "source": {"sources": [{"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[0].items[13]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"Nitrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Nitrogen gas", "gmo": "http://purl.jp/bio/10/gmo/GMO_002261", "gmo_id": "GMO_002261", "label": "Nitrogen gas", "properties": [{"id": "GMO_000077", "uri": "http://purl.jp/bio/10/gmo/GMO_000077", "label": "ガス"}], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.comments[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }", "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix components thoroughly, adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):"}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}]}, "decision": "not_quantified", "rationale": "This source gas is part of the explicit N2–CO2 4:1 v/v atmosphere, not a measured dissolved ingredient concentration. The gas mixture is quantified, but neither gas delivery volume nor dissolved concentration is supplied; retain the atmospheric role and ratio.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "This source gas is part of the explicit N2–CO2 4:1 v/v atmosphere, not a measured dissolved ingredient concentration. The gas mixture is quantified, but neither gas delivery volume nor dissolved concentration is supplied; retain the atmospheric role and ratio."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "This source gas is part of the explicit N2–CO2 4:1 v/v atmosphere, not a measured dissolved ingredient concentration. The gas mixture is quantified, but neither gas delivery volume nor dissolved concentration is supplied; retain the atmospheric role and ratio."}]}, {"quantity_id": "q14", "topic": "Trace minerals (see Medium [M142]) receiving dose", "source": {"sources": [{"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[0].items[10]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"Trace minerals (see Medium [M142])\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M142\",\n          \"properties\": [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Trace minerals (see Medium [M142])", "volume": 10, "unit": "ml", "reference_media_id": "M142", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.comments[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }", "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix components thoroughly, adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):"}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}]}, "decision": "correct", "rationale": "Trace minerals are added as10 mL per initial batch; no final-liter dose is stated for this earlier table row.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Trace minerals are added as10 mL per initial batch; no final-liter dose is stated for this earlier table row."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Trace minerals are added as10 mL per initial batch; no final-liter dose is stated for this earlier table row."}]}, {"quantity_id": "q15", "topic": "Trace minerals (see Medium [M142]) stock descriptor", "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[0].items[10]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"Trace minerals (see Medium [M142])\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M142\",\n          \"properties\": [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Trace minerals (see Medium [M142])", "volume": 10, "unit": "ml", "reference_media_id": "M142", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The referenced stock is the trace-mineral subsection of M142/JCM151, not the whole Pyrococcus medium.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].name", "stored_value": "Unknown solution", "decision": "correct", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The referenced stock is the trace-mineral subsection of M142/JCM151, not the whole Pyrococcus medium."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].name", "stored_value": "Unknown solution", "decision": "correct", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The referenced stock is the trace-mineral subsection of M142/JCM151, not the whole Pyrococcus medium."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The referenced stock is the trace-mineral subsection of M142/JCM151, not the whole Pyrococcus medium."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The referenced stock is the trace-mineral subsection of M142/JCM151, not the whole Pyrococcus medium."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].preferred_term", "stored_value": "Trace minerals (see Medium [M142])", "decision": "evidence_only", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The referenced stock is the trace-mineral subsection of M142/JCM151, not the whole Pyrococcus medium."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].preferred_term", "stored_value": "Trace minerals (see Medium [M142])", "decision": "evidence_only", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The referenced stock is the trace-mineral subsection of M142/JCM151, not the whole Pyrococcus medium."}]}, {"quantity_id": "q16", "topic": "8% NaHCO3 solution* receiving dose", "source": {"sources": [{"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[1].items[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"8% NaHCO3 solution*\",\n          \"volume\": 25,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001119\",\n          \"gmo_id\": \"GMO_001119\",\n          \"label\": \"Sodium bicarbonate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "8% NaHCO3 solution*", "volume": 25, "unit": "ml", "conc_value": 8, "conc_unit": "%", "gmo": "http://purl.jp/bio/10/gmo/GMO_001119", "gmo_id": "GMO_001119", "label": "Sodium bicarbonate solution", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051", "label": "Solution"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038", "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.comments[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }", "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix components thoroughly, adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):"}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}]}, "decision": "correct", "rationale": "The post-cooling instruction explicitly says add per liter; 25 mL/L is supported for this addition, not 25 g/L. Preserve the receiving-liter instruction without treating it as a measured final volume after both additions.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[1].concentration", "stored_value": {"value": "25", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The post-cooling instruction explicitly says add per liter; 25 mL/L is supported for this addition, not 25 g/L. Preserve the receiving-liter instruction without treating it as a measured final volume after both additions."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[1].concentration", "stored_value": {"value": "25", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The post-cooling instruction explicitly says add per liter; 25 mL/L is supported for this addition, not 25 g/L. Preserve the receiving-liter instruction without treating it as a measured final volume after both additions."}]}, {"quantity_id": "q17", "topic": "8% NaHCO3 solution* stock descriptor", "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[1].items[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"8% NaHCO3 solution*\",\n          \"volume\": 25,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001119\",\n          \"gmo_id\": \"GMO_001119\",\n          \"label\": \"Sodium bicarbonate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "8% NaHCO3 solution*", "volume": 25, "unit": "ml", "conc_value": 8, "conc_unit": "%", "gmo": "http://purl.jp/bio/10/gmo/GMO_001119", "gmo_id": "GMO_001119", "label": "Sodium bicarbonate solution", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051", "label": "Solution"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038", "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The bicarbonate 8% label has no stated w/v/w/w/v/v basis; preserve it verbatim without converting to a mass or molar concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[1].name", "stored_value": "Unknown solution", "decision": "correct", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The bicarbonate 8% label has no stated w/v/w/w/v/v basis; preserve it verbatim without converting to a mass or molar concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[1].name", "stored_value": "Unknown solution", "decision": "correct", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The bicarbonate 8% label has no stated w/v/w/w/v/v basis; preserve it verbatim without converting to a mass or molar concentration."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[1].composition", "stored_value": [], "decision": "add", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The bicarbonate 8% label has no stated w/v/w/w/v/v basis; preserve it verbatim without converting to a mass or molar concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[1].composition", "stored_value": [], "decision": "add", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The bicarbonate 8% label has no stated w/v/w/w/v/v basis; preserve it verbatim without converting to a mass or molar concentration."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[1].preferred_term", "stored_value": "8% NaHCO3 solution*", "decision": "evidence_only", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The bicarbonate 8% label has no stated w/v/w/w/v/v basis; preserve it verbatim without converting to a mass or molar concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[1].preferred_term", "stored_value": "8% NaHCO3 solution*", "decision": "evidence_only", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The bicarbonate 8% label has no stated w/v/w/w/v/v basis; preserve it verbatim without converting to a mass or molar concentration."}]}, {"quantity_id": "q18", "topic": "1 M Glucose solution receiving dose", "source": {"sources": [{"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[1].items[1]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"1 M Glucose solution\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001465\",\n          \"gmo_id\": \"GMO_001465\",\n          \"label\": \"Glucose solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "1 M Glucose solution", "volume": 20, "unit": "ml", "conc_value": 1, "conc_unit": "M", "gmo": "http://purl.jp/bio/10/gmo/GMO_001465", "gmo_id": "GMO_001465", "label": "Glucose solution", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051", "label": "Solution"}, {"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}], "roles": [{"id": "GMO_000063", "uri": "http://purl.jp/bio/10/gmo/GMO_000063", "label": "Carbon source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.comments[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }", "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix components thoroughly, adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):"}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}]}, "decision": "correct", "rationale": "The post-cooling instruction explicitly says add per liter; 20 mL/L is supported for this addition, not 20 g/L. Preserve the receiving-liter instruction without treating it as a measured final volume after both additions.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[2].concentration", "stored_value": {"value": "20", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The post-cooling instruction explicitly says add per liter; 20 mL/L is supported for this addition, not 20 g/L. Preserve the receiving-liter instruction without treating it as a measured final volume after both additions."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[2].concentration", "stored_value": {"value": "20", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The post-cooling instruction explicitly says add per liter; 20 mL/L is supported for this addition, not 20 g/L. Preserve the receiving-liter instruction without treating it as a measured final volume after both additions."}]}, {"quantity_id": "q19", "topic": "1 M Glucose solution stock descriptor", "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.components[1].items[1]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n          \"component_name\": \"1 M Glucose solution\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001465\",\n          \"gmo_id\": \"GMO_001465\",\n          \"label\": \"Glucose solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "1 M Glucose solution", "volume": 20, "unit": "ml", "conc_value": 1, "conc_unit": "M", "gmo": "http://purl.jp/bio/10/gmo/GMO_001465", "gmo_id": "GMO_001465", "label": "Glucose solution", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051", "label": "Solution"}, {"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}], "roles": [{"id": "GMO_000063", "uri": "http://purl.jp/bio/10/gmo/GMO_000063", "label": "Carbon source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The glucose stock is explicitly1 M. Its species is generic glucose; no D/L, anomer or hydrate is inferred, and the receiving-medium final molarity is not independently calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[2].name", "stored_value": "Unknown solution", "decision": "correct", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The glucose stock is explicitly1 M. Its species is generic glucose; no D/L, anomer or hydrate is inferred, and the receiving-medium final molarity is not independently calculated."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[2].name", "stored_value": "Unknown solution", "decision": "correct", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The glucose stock is explicitly1 M. Its species is generic glucose; no D/L, anomer or hydrate is inferred, and the receiving-medium final molarity is not independently calculated."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[2].composition", "stored_value": [], "decision": "add", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The glucose stock is explicitly1 M. Its species is generic glucose; no D/L, anomer or hydrate is inferred, and the receiving-medium final molarity is not independently calculated."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[2].composition", "stored_value": [], "decision": "add", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The glucose stock is explicitly1 M. Its species is generic glucose; no D/L, anomer or hydrate is inferred, and the receiving-medium final molarity is not independently calculated."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[2].preferred_term", "stored_value": "1 M Glucose solution", "decision": "evidence_only", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The glucose stock is explicitly1 M. Its species is generic glucose; no D/L, anomer or hydrate is inferred, and the receiving-medium final molarity is not independently calculated."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[2].preferred_term", "stored_value": "1 M Glucose solution", "decision": "evidence_only", "rationale": "Retain the existing specific preferred_term; replace the placeholder name and populate only supported stock identity/composition. The glucose stock is explicitly1 M. Its species is generic glucose; no D/L, anomer or hydrate is inferred, and the receiving-medium final molarity is not independently calculated."}]}, {"quantity_id": "q20", "topic": "Trace stock: Distilled water", "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "locator": "$.components[2].items[0]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo": "http://purl.jp/bio/10/gmo/GMO_001001", "gmo_id": "GMO_001001", "label": "Distilled water", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044", "label": "Solvating media"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "The current dependency correctly retains the 1 L stock water input as volume, not final makeup.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "solutions[1].composition[0].concentration", "stored_value": {"value": "1", "unit": "L"}, "decision": "evidence_only", "rationale": "The current dependency correctly retains the 1 L stock water input as volume, not final makeup."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}]}, {"quantity_id": "q21", "topic": "Trace stock: MgSO4・7H2O", "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "locator": "$.components[2].items[1]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote": "{\n          \"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\": \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "MgSO4・7H2O", "volume": 3, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001002", "gmo_id": "GMO_001002", "label": "Magnesium sulfate heptahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "The current dependency already preserves the exact 3 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "solutions[1].composition[1].notes", "stored_value": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component [Merged 2 duplicates: 3.5, 3.0]\n\nSource batch input: 3 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "evidence_only", "rationale": "The current dependency already preserves the exact 3 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}]}, {"quantity_id": "q22", "topic": "Trace stock: NaCl", "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "locator": "$.components[2].items[2]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote": "{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "NaCl", "volume": 1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001004", "gmo_id": "GMO_001004", "label": "Sodium chloride", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "The current dependency already preserves the exact 1 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "solutions[1].composition[2].notes", "stored_value": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component [Merged 2 duplicates: 13.85, 1.0]\n\nSource batch input: 1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "evidence_only", "rationale": "The current dependency already preserves the exact 1 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}]}, {"quantity_id": "q23", "topic": "Trace stock: CaCl2・2H2O", "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "locator": "$.components[2].items[3]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote": "{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "CaCl2・2H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001005", "gmo_id": "GMO_001005", "label": "Calcium chloride dihydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "The current dependency already preserves the exact 0.1 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "solutions[1].composition[3].notes", "stored_value": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "evidence_only", "rationale": "The current dependency already preserves the exact 0.1 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}]}, {"quantity_id": "q24", "topic": "Trace stock: Na2MoO4・2H2O", "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "locator": "$.components[2].items[4]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote": "{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Na2MoO4・2H2O", "volume": 0.01, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001011", "gmo_id": "GMO_001011", "label": "Sodium molybdate dihydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "The current dependency already preserves the exact 0.01 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "solutions[1].composition[4].notes", "stored_value": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "evidence_only", "rationale": "The current dependency already preserves the exact 0.01 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}]}, {"quantity_id": "q25", "topic": "Trace stock: H3BO3", "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "locator": "$.components[2].items[5]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote": "{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "H3BO3", "volume": 0.01, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001015", "gmo_id": "GMO_001015", "label": "Boric acid", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "The current dependency already preserves the exact 0.01 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "solutions[1].composition[5].notes", "stored_value": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component [Merged 2 duplicates: 15.0, 0.01]\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "evidence_only", "rationale": "The current dependency already preserves the exact 0.01 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}]}, {"quantity_id": "q26", "topic": "Trace stock: FeSO4・7H2O", "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "locator": "$.components[2].items[6]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote": "{\n          \"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\": \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "FeSO4・7H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001016", "gmo_id": "GMO_001016", "label": "Iron(II) sulfate heptahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "The current dependency already preserves the exact 0.1 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "solutions[1].composition[6].notes", "stored_value": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "evidence_only", "rationale": "The current dependency already preserves the exact 0.1 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}]}, {"quantity_id": "q27", "topic": "Trace stock: ZnSO4・7H2O", "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "locator": "$.components[2].items[7]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote": "{\n          \"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\": \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "ZnSO4・7H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001023", "gmo_id": "GMO_001023", "label": "Zinc sulfate heptahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "The current dependency already preserves the exact 0.1 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "solutions[1].composition[7].notes", "stored_value": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "evidence_only", "rationale": "The current dependency already preserves the exact 0.1 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}]}, {"quantity_id": "q28", "topic": "Trace stock: CuSO4・5H2O", "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "locator": "$.components[2].items[8]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote": "{\n          \"component_name\": \"CuSO4・5H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001039\",\n          \"gmo_id\": \"GMO_001039\",\n          \"label\": \"Copper(II) sulfate pentahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "CuSO4・5H2O", "volume": 0.01, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001039", "gmo_id": "GMO_001039", "label": "Copper(II) sulfate pentahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "The current dependency already preserves the exact 0.01 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "solutions[1].composition[8].notes", "stored_value": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "evidence_only", "rationale": "The current dependency already preserves the exact 0.01 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}]}, {"quantity_id": "q29", "topic": "Trace stock: CoSO4・7H2O", "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "locator": "$.components[2].items[9]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote": "{\n          \"component_name\": \"CoSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001050\",\n          \"gmo_id\": \"GMO_001050\",\n          \"label\": \"Cobalt(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "CoSO4・7H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001050", "gmo_id": "GMO_001050", "label": "Cobalt(II) sulfate heptahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "The current dependency already preserves the exact 0.1 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "solutions[1].composition[9].notes", "stored_value": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "evidence_only", "rationale": "The current dependency already preserves the exact 0.1 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}]}, {"quantity_id": "q30", "topic": "Trace stock: Nitrilotriacetic acid", "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "locator": "$.components[2].items[10]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote": "{\n          \"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001053\",\n          \"gmo_id\": \"GMO_001053\",\n          \"label\": \"Nitrilotriacetic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Nitrilotriacetic acid", "volume": 1.5, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001053", "gmo_id": "GMO_001053", "label": "Nitrilotriacetic acid", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "The current dependency already preserves the exact 1.5 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "solutions[1].composition[10].notes", "stored_value": "Role: Mineral source; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 1.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "evidence_only", "rationale": "The current dependency already preserves the exact 1.5 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}]}, {"quantity_id": "q31", "topic": "Trace stock: MnSO4・xH2O", "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "locator": "$.components[2].items[11]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote": "{\n          \"component_name\": \"MnSO4・xH2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001065\",\n          \"gmo_id\": \"GMO_001065\",\n          \"label\": \"Manganese sulfate n-hydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "MnSO4・xH2O", "volume": 0.5, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001065", "gmo_id": "GMO_001065", "label": "Manganese sulfate n-hydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "The current dependency already preserves the exact 0.5 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "solutions[1].composition[11].notes", "stored_value": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "evidence_only", "rationale": "The current dependency already preserves the exact 0.5 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}]}, {"quantity_id": "q32", "topic": "Trace stock: AlK(SO4)2", "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "locator": "$.components[2].items[12]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote": "{\n          \"component_name\": \"AlK(SO4)2\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001088\",\n          \"gmo_id\": \"GMO_001088\",\n          \"label\": \"Aluminum potassium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "AlK(SO4)2", "volume": 0.01, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001088", "gmo_id": "GMO_001088", "label": "Aluminum potassium sulfate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "The current dependency already preserves the exact 0.01 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "solutions[1].composition[12].notes", "stored_value": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "evidence_only", "rationale": "The current dependency already preserves the exact 0.01 g batch amount in notes and withdraws unsupported final-volume concentration. Credit this repair. JCM151 provides a water input, while provider J782 separately declares stock g_l; do not overwrite this conservative source-batch representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Link or represent only this exact trace-stock component with its source amount and unresolved primary final volume; preserve the existing repaired dependency."}]}, {"quantity_id": "q33", "topic": "Trace-stock KOH and pH", "source": {"sources": [{"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "locator": "$.components[2].items[13]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote": "{\n          \"component_name\": \"KOH solution\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\": \"GMO_001903\",\n          \"label\": \"Potassium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "KOH solution", "gmo": "http://purl.jp/bio/10/gmo/GMO_001903", "gmo_id": "GMO_001903", "label": "Potassium hydroxide solution", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051", "label": "Solution"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "locator": "$.comments[1]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote": "{\n      \"paragraph_index\": 5,\n      \"comment\": \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0.\"\n    }", "exact_decoded_object": {"paragraph_index": 5, "comment": "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}]}, "decision": "evidence_only", "rationale": "The trace-stock KOH adjustment has no fixed dose/strength. The existing dependency records that limitation; the primary trace process specifies pH6.5 then7.0. The parent receiving dose is not transferred.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "solutions[1].solutions[0].notes", "stored_value": "Role: Mineral source; Properties: Defined component, Solution\n\npH-adjustment reagent; no fixed dose is specified. Normality is not converted to molarity.", "decision": "evidence_only", "rationale": "The trace-stock KOH adjustment has no fixed dose/strength. The existing dependency records that limitation; the primary trace process specifies pH6.5 then7.0. The parent receiving dose is not transferred."}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "solutions[1].preparation_notes", "stored_value": "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0.", "decision": "evidence_only", "rationale": "The trace-stock KOH adjustment has no fixed dose/strength. The existing dependency records that limitation; the primary trace process specifies pH6.5 then7.0. The parent receiving dose is not transferred."}]}, {"quantity_id": "q34", "topic": "Main preparation and numeric process scope", "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14", "locator": "$.comments[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }", "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix components thoroughly, adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter--sterilized):"}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "add", "rationale": "Add the exact source process with pH7.2, the example5 mL vessel fill (an example, not a universal prescription), 4:1 v/v N2–CO2, closure/autoclaving and the post-cooling per-liter additions. The trace-stock pH6.5 then7.0 must remain separate from the main-medium pH.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Add the exact source process with pH7.2, the example5 mL vessel fill (an example, not a universal prescription), 4:1 v/v N2–CO2, closure/autoclaving and the post-cooling per-liter additions. The trace-stock pH6.5 then7.0 must remain separate from the main-medium pH.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Add the exact source process with pH7.2, the example5 mL vessel fill (an example, not a universal prescription), 4:1 v/v N2–CO2, closure/autoclaving and the post-cooling per-liter additions. The trace-stock pH6.5 then7.0 must remain separate from the main-medium pH.", "missing": true}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "ph_value", "stored_value": null, "decision": "add", "rationale": "Add the exact source process with pH7.2, the example5 mL vessel fill (an example, not a universal prescription), 4:1 v/v N2–CO2, closure/autoclaving and the post-cooling per-liter additions. The trace-stock pH6.5 then7.0 must remain separate from the main-medium pH.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "ph_value", "stored_value": null, "decision": "add", "rationale": "Add the exact source process with pH7.2, the example5 mL vessel fill (an example, not a universal prescription), 4:1 v/v N2–CO2, closure/autoclaving and the post-cooling per-liter additions. The trace-stock pH6.5 then7.0 must remain separate from the main-medium pH.", "missing": true}]}, {"quantity_id": "q35", "topic": "JCM default sterilization and explicit exception", "source": {"evidence_id": "jcm782", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=782", "raw_path": "REVIEW_WORK/batch058/source01-03/jcm782.bin", "raw_sha256": "61323f3bfd79a7fb32371ed2713b6ad4d03ddea38f9975a465b727e98cf801ee", "locator": "Default header and starred post-cooling addition", "accessed_at": "2026-10-28T06:09:02.690012Z", "quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min."}, "decision": "add", "rationale": "JCM782 explicitly supplies the global default121°C for15 min unless otherwise stated; apply only to the stated autoclaving step. The starred bicarbonate is explicitly filter-sterilized instead. Do not invent a filtration pore size or a separate glucose autoclaving exception.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "JCM782 explicitly supplies the global default121°C for15 min unless otherwise stated; apply only to the stated autoclaving step. The starred bicarbonate is explicitly filter-sterilized instead. Do not invent a filtration pore size or a separate glucose autoclaving exception.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "JCM782 explicitly supplies the global default121°C for15 min unless otherwise stated; apply only to the stated autoclaving step. The starred bicarbonate is explicitly filter-sterilized instead. Do not invent a filtration pore size or a separate glucose autoclaving exception.", "missing": true}]}]

### Current ontology and MIM correspondence

grounding: supported. Targets: CultureMech:010224.

The grounding inventory enumerates every asserted identifier and exact preferred label. Exact identifier rows and ontology-linked rows are recorded separately, including mapping_status. Present catalog membership does not validate supplied hydrate form or historical identity; specific limits are assessed separately.

### History and evidence scope

provenance: supported. Targets: CultureMech:010224.

Complete owner and target histories were read. Current source bytes and inspected code are independent evidence; historical timestamps remain historical claims unless an exact cited raw digest is recovered.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:010224.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:010224.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Liquid solvent and stock additions have mass units

major / open / confirmed; issue key: culturemech-010224-liquid-solvent-and-stock-additions-have-mass-units.

The target and TOGO owner store1 L water as1 G_PER_L and the10,25,20 mL stock additions as10,25,20 G_PER_L. Restore water volume and distinguish the initial trace-mineral batch addition from the two explicitly per-liter late additions. No density or final-medium volume is inferred.

### f2: Main batch masses are unsupported as unchanged final-medium rates

major / open / confirmed; issue key: culturemech-010224-main-batch-masses-are-unsupported-as-unchanged-final-medium-rates.

Nine non-solvent main ingredients use the literal source batch gram numbers as G_PER_L. JCM782 supplies1 L water and further stock additions without an explicit final-volume makeup. Provider J782 reports different g_l rates on declared1055 mL. Keep both source assertions distinct and preserve the batch masses; neither source permits silently endorsing the local unchanged values as measured final concentrations.

### f3: Named stocks remain empty placeholder shells

major / open / confirmed; issue key: culturemech-010224-named-stocks-remain-empty-placeholder-shells.

All three solutions retain informative preferred_term text but have Unknown solution names and empty composition. The trace stock is scoped to the JCM151/M142 trace subsection; the bicarbonate stock has a bare8% label and glucose is1 M. Credit the already repaired M142 composition notes; do not transfer its Pyrococcus main recipe, salt base or receiving dose.

### f4: Source preparation and pH are missing

major / open / confirmed; issue key: culturemech-010224-source-preparation-and-ph-are-missing.

The target and owner lack preparation_steps and ph_value despite exact JCM/TOGO instructions. KOH and gases appear only as VARIABLE ingredients, which does not encode the pH adjustment,4:1 atmosphere, vessel example, sterilization or late-addition stages.

### f5: Potassium nitrate retains an unresolved legacy catalog link

minor / open / confirmed; issue key: culturemech-010224-potassium-nitrate-retains-an-unresolved-legacy-catalog-link.

The current primary CHEBI:63043 correctly identifies potassium nitrate, but the separate MediaIngredientMech:000170 identifier has no exact current packaged catalog row. This is a current resolution limitation, not a claim that its historical identity was invalid.

## Recommended Actions And Acceptance Checks

### action1

Preserve the source1 L water input as a solvent/preparation volume; represent10 mL trace stock per initial batch and25/20 mL per receiving liter for the post-cooling stocks. Retain exact source evidence at the root for solution/preparation claims; regenerate after owner curation.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Retain each exact source batch amount with scoped evidence and mark the final-medium basis unresolved. If adopting provider-reported rates, identify that provider stage explicitly and reconcile it with the primary per-liter addition instructions rather than inventing a common denominator.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Replace placeholder names and resolve or link the exact stock contents. Preserve the M142 trace repairs and source-supported1 M glucose stock; keep bicarbonate percentage basis unresolved. Record each dose separately with root evidence and no double-counted components.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Add only the exact source process and pH with stage-qualified root evidence. Preserve the5 mL example as an example, gas ratio as atmosphere rather than dissolved concentration, and starred filtration exception. Keep unquantified titrant and gas volumes unspecified.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action5

Resolve the legacy slot against the pinned current catalog while preserving source potassium nitrate identity and append-only historical provenance. Do not fabricate a replacement from a label-only match.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| jcm782 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=782; Exact source identity and scoped formulation/preparation | supports | Complete original JCM782 source read: main batch, explicit per-liter post-cooling stock additions, pH/gas/distribution and default sterilization header. |
| togo812 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812; Exact source identity and scoped formulation/preparation | supports | Complete current TOGO M812 response read, preserving the original JCM782 accession and all two-section rows and comment. |
| apiJ782 | https://mediadive.dsmz.de/rest/medium/J782; Exact source identity and scoped formulation/preparation | supports | Complete current official provider J782 payload: declared main volume1055 mL, explicit lower g_l rates, distinct trace stock and literal late additions. This is a source comparison, not an automatic replacement of the JCM/TOGO basis. |
| jcm151 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151; Exact source identity and scoped formulation/preparation | supports | Only the Trace minerals subsection and its preparation are used; the Pyrococcus basal recipe and its receiving dose/process are excluded. |
| togo142 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; Exact source identity and scoped formulation/preparation | supports | Only components[2] trace-mineral rows and comments[1] trace preparation are used; other parent constituents, receiving dose and variants are outside scope. |
| identity-search | REVIEW_WORK/batch058/record01/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition parser restricts ingredients to the primary solution, excludes solvent and recognized stock additions, and retains explicit g_l. The solution parser preserves referenced or percent-defined stocks and source attributes. Preparation parsing still concatenates all solution steps into root preparation_steps; source-stage annotation remains important. These present functions do not prove the historical execution that produced this record. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. The current code is not proof of the earlier summed value. |
| historical-1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-3 | reports/yaml_record_review/20260922T022222Z-CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-reader | REVIEW_WORK/batch058/record01/historical-reader.json | context_only | All exact target/owner historical report texts and current raw/literal/locator joins; historical recommendations remain subject to current stage and volume evidence. |
| writer-togo | src/culturemech/import/togo_importer.py; _ingredient_from_item, _solution_from_item, _extract_primary_components, _extract_preparation_steps, _parse_unit | context_only | Current primary-section parser separates referenced stocks, retains unknown stock composition, represents gas entries as VARIABLE and captures source comments. _parse_unit still maps bare g/ml to per-liter enums and defaults unknown units to G_PER_L; such mechanical unit mapping does not establish a denominator. No historical execution is inferred. |
| trace-dependency | data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml; solutions[1].composition, solutions[1].solutions, solutions[1].preparation_notes | context_only | Exact trace-mineral composition, batch notes, evidence and preparation only. Parent receiving concentration, other stocks, main formulation, whole-parent process and variants are excluded. |
| source-rows | REVIEW_WORK/batch058/record01/source-row-inventory.json | context_only | All M812 source rows and only the M142 trace-stock rows, with exact literal objects and locators. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15377; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63036; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86345; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32588; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63043 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63043; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32035 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32035; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16526; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17997; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91244; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_44557; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86360; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86463 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86463; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch058/record01/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch058/record01/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch058/record01/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch058/record01/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch058/record01/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch058/record01/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch058/record01/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch058/record01/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch058/record01/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- The JCM main table gives a water input, not an explicit final-medium makeup; provider1055 mL and explicit g_l remain separately attributed. The two late stock additions alone have an explicit per-liter instruction.
- The bicarbonate8% basis is unspecified; no density, molecular-weight, final-medium molarity or gas dissolution calculation was used. M142 MnSO4 hydration is unspecified; no exact hydrate conversion is justified.
- Only the M142/JCM151 trace-mineral subsection is in dependency scope. Parent main medium, salt-base formulation, receiving dose, organism claims and variants are excluded.
- Current source-byte matches do not prove historical access events or scientific correctness of older report recommendations. Same-source neighboring JCM imports were not promoted to selected owners.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T061312Z-batch058-record01-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Caldinitratiruptor microaerophilus: preserve JCM782 batch and stock bases'
started_at: '2026-10-28T06:08:52.425624Z'
finished_at: '2026-10-28T06:13:12.341166Z'
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
summary: The selected TOGO M812 import has water and three stock additions represented
  in mass-per-liter units, unsupported main-batch rate assertions, empty stock shells
  and missing JCM preparation. Exact source quantities and a repaired trace-mineral
  dependency are credited separately. A current legacy potassium-nitrate linkage remains
  unresolved.
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
  - path: data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml
    sha256: a7537e8f4406c43a5bd0622b4f4e632dc4f00b1b84fc37a64e6e1626d5ba4e2e
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml
    sha256: 290433e6204999b98296f516fb77589d6df2c07e922d780683ae0ed53353844d
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml
    sha256: 7c6e65acbb7439af7edd74a48681202447d724fe12ea2d0554fa3efe00dc6039
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.md
    sha256: 73742f12e8e161f0e6206327fb0bd3f8ebbeb5c6041b3cbcfdf7a414087a5c45
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/caldinitratiruptor_microaerophilus_medium__a882ad30.md
    sha256: bddaaa85a1f0b9ec33b4d8b3936c4edd20cc2a47a1c064302c704bb4b7d95792
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.md
    sha256: 1f705caee7f14ef05c7f1bc65c7dc7996cbe39deac3b3a76f6e9fca433df66c4
    role: context
  - path: reports/yaml_record_review/20260922T022222Z-CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.md
    sha256: 34df87c8c6e775006f5ad1a3e145dbedf1e7f30a6f72850198a38f2b407e6914
    role: context
  - path: reports/yaml_record_review/20260922T022352Z-caldinitratiruptor_microaerophilus_medium__a882ad30.md
    sha256: 16e9a27deb55e3ffb4fb4f1f2f86c1cb8c5463d9d2454bb1c36437405b63ce6f
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
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
scope:
  description: Full selected record and exact maintained contributors; explicitly
    scoped dependency and external-source limits retained.
  selection: Actual batch058 native selection index 01.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010224
targets:
- target_id: CultureMech:010224
  path: data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml
  label: caldinitratiruptor_microaerophilus_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:010224
  command: just validate-schema data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml
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
  - CultureMech:010224
  command: just validate-strict data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml
    --out REVIEW_WORK/batch058/record01/strict.tsv --workers 1
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
  - CultureMech:010224
  command: just validate-terms data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml
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
  - CultureMech:010224
  command: just validate-references data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T06:13:12.235871Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: a7537e8f4406c43a5bd0622b4f4e632dc4f00b1b84fc37a64e6e1626d5ba4e2e
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T06:13:12.235871Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 7c6e65acbb7439af7edd74a48681202447d724fe12ea2d0554fa3efe00dc6039
- evidence_id: jcm782
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=782
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T06:09:02.690012Z'
  support: supports
  summary: 'Complete original JCM782 source read: main batch, explicit per-liter post-cooling
    stock additions, pH/gas/distribution and default sterilization header.'
  snapshot_sha256: 61323f3bfd79a7fb32371ed2713b6ad4d03ddea38f9975a465b727e98cf801ee
- evidence_id: togo812
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T06:09:02.638524Z'
  support: supports
  summary: Complete current TOGO M812 response read, preserving the original JCM782
    accession and all two-section rows and comment.
  snapshot_sha256: a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14
- evidence_id: apiJ782
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J782
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T06:09:03.148827Z'
  support: supports
  summary: 'Complete current official provider J782 payload: declared main volume1055
    mL, explicit lower g_l rates, distinct trace stock and literal late additions.
    This is a source comparison, not an automatic replacement of the JCM/TOGO basis.'
  snapshot_sha256: ebec4b4ba0faa1446d7e5091babb72e2b7e084ba9ba7749d756bb298a21ce6bf
- evidence_id: jcm151
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T06:09:02.752166Z'
  support: supports
  summary: Only the Trace minerals subsection and its preparation are used; the Pyrococcus
    basal recipe and its receiving dose/process are excluded.
  snapshot_sha256: 6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7
- evidence_id: togo142
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T06:09:02.797070Z'
  support: supports
  summary: Only components[2] trace-mineral rows and comments[1] trace preparation
    are used; other parent constituents, receiving dose and variants are outside scope.
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch058/record01/identity-search.json
  accessed_at: '2026-10-28T06:13:12.283607Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems resolved uniquely. Similar names and
    source accessions are not promoted to owners.
  snapshot_sha256: 7ec1a204ab8971214c7ddb44c8340c7321d41b672d7d904a8e448813c2ddd16c
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T06:13:12.235871Z'
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
  accessed_at: '2026-10-28T06:13:12.235871Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T06:13:12.235871Z'
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
  accessed_at: '2026-10-28T06:13:12.235871Z'
  support: context_only
  summary: Current cleanup groups identical normalized names, keeps the first entry
    as a base, flags differing concentrations and combines a warning note; it does
    not sum concentrations. It can still discard distinctions when names repeat, so
    source stage must be retained. The current code is not proof of the earlier summed
    value.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T06:13:12.235871Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 73742f12e8e161f0e6206327fb0bd3f8ebbeb5c6041b3cbcfdf7a414087a5c45
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T06:13:12.235871Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 1f705caee7f14ef05c7f1bc65c7dc7996cbe39deac3b3a76f6e9fca433df66c4
- evidence_id: historical-3
  kind: record_content
  reference: reports/yaml_record_review/20260922T022222Z-CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T06:13:12.235871Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 34df87c8c6e775006f5ad1a3e145dbedf1e7f30a6f72850198a38f2b407e6914
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch058/record01/historical-reader.json
  accessed_at: '2026-10-28T06:13:12.286886Z'
  support: context_only
  summary: All exact target/owner historical report texts and current raw/literal/locator
    joins; historical recommendations remain subject to current stage and volume evidence.
  snapshot_sha256: a35de55e4b12c6964a98d13796cf3070ba68e28cb3e5cc0e8fb9c204f1a2817d
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item, _solution_from_item, _extract_primary_components,
    _extract_preparation_steps, _parse_unit
  accessed_at: '2026-10-28T06:13:12.235871Z'
  support: context_only
  summary: Current primary-section parser separates referenced stocks, retains unknown
    stock composition, represents gas entries as VARIABLE and captures source comments.
    _parse_unit still maps bare g/ml to per-liter enums and defaults unknown units
    to G_PER_L; such mechanical unit mapping does not establish a denominator. No
    historical execution is inferred.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: trace-dependency
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml
  locator: solutions[1].composition, solutions[1].solutions, solutions[1].preparation_notes
  accessed_at: '2026-10-28T06:13:12.235871Z'
  support: context_only
  summary: Exact trace-mineral composition, batch notes, evidence and preparation
    only. Parent receiving concentration, other stocks, main formulation, whole-parent
    process and variants are excluded.
  snapshot_sha256: 290433e6204999b98296f516fb77589d6df2c07e922d780683ae0ed53353844d
- evidence_id: source-rows
  kind: record_content
  reference: REVIEW_WORK/batch058/record01/source-row-inventory.json
  accessed_at: '2026-10-28T06:13:12.324063Z'
  support: context_only
  summary: All M812 source rows and only the M142 trace-stock rows, with exact literal
    objects and locators.
  snapshot_sha256: 9293f959d6817b5554518dca87e3f0b7da24776175a2aff4e34e8875cfb14006
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15377
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:03.408915Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 42561686e12ba0831d99216248ea8c0b3338b461b0b77dd988f3096ad8678e59
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:05.236641Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b145f4ff9b90ebb993ff576d9ab35a6c10b7c42a3b99e18feffcc8d75c0e1e50
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:09.947533Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: df8f702eb5b9d3e50209bfa2b0c4b6f1db30c116e56a58e348cbd4bf3bc0ebc1
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63036
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:08.868167Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 913baf38abc38dd61f05c5d636fd6532b70a668673a1f5762f290d2b67270164
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:05.827954Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: c70055293606f21dcdfb72325a4677661b51efb723ba9357efab43f8ec9b03f7
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:03.365873Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 97e9c2b05f3937c5beeebb4e6338aa6730f9e422ee0e7570a6c622dda8d97a86
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:10.594154Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 015a33a158257cc5cba8a8e62de382053399be060366af5d95074883bb22b86e
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32588
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:07.129321Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 8fc333e98ee953346b5c291b9e5765e77d03cc46740a1282af3e5f4ad355de1a
- evidence_id: chebi63043
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63043
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:08.960793Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 27d2a6a8a75a261941f0290b29dab700e2a3dc13dbf882f1624793e18ea2fa62
- evidence_id: chebi32035
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32035
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:06.893179Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: beb9265e17aebd20539ab8a464558e2820b9155c520635a44f77fa3e48f51ad4
- evidence_id: chebi16526
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16526
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:04.043826Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a46d1979945f86fa259f0c40d36d152254b9b4a949a60bbfbb7ef7d01b247561
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17997
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:04.635414Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 3072b950418eb270c362b75526cb52e64d918480d57dcafd96d75961002f3d3e
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:06.435125Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1635f67d01e00cabdef4ed0d9ef6d5383787c56bd0447051deb90ad353b499a2
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:09.443282Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0271a149a298ff837ad8f690ce8cb0acf111f5d25c5efaf6fa828401ab951d56
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:07.629317Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f23e1405347fa9d8a0826d4dd1279b7cdec8361390d20e439154dcbbd386a2d4
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:09.464302Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: e12b865122aab78645385260e1e83ff28f3c45365cb67c9181166628f68974b3
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:07.064096Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 6bf1390236046f1cb7b21e2fc324fccba6e6eac2bc4e519f12d998f0edce671b
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:06.522708Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 453e496e1e59b82bb42cd3252d410b9dc77d0c11e49f3da70496a82978e80505
- evidence_id: chebi91244
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91244
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:11.213752Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 4b8d2689d3b68919586644a832e86d7a50b6b619c20295d55212660c7f794a55
- evidence_id: chebi44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_44557
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:07.739982Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 371aa3b809db6c5d1ec8f8b8be40011e6b1132b1c0be40e70fb927788728d65a
- evidence_id: chebi86360
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86360
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:10.552610Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: d7fa588a0312e9c257c235a7219db2e63b9d8a1ae7c8af0af9d549739f00aa6d
- evidence_id: chebi86463
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86463
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:09:10.759493Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 32e2141c0b853fd1737549b7420543d27f5f5b309ba9e54b34a19e2053eea69d
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch058/record01/quantity-inventory.json
  accessed_at: '2026-10-28T06:13:12.339908Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 5f42e4132d824524d3c6e8efbf1f116b50cdea91aa72d9789a37f26acad95632
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch058/record01/grounding-inventory.json
  accessed_at: '2026-10-28T06:13:12.339992Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 5e92603c817e8b5c47f2143f652e5015a15cc0c9e127ac79f435e796ad521d80
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch058/record01/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T06:13:12.340066Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 56fec0c9c33f7f75e5f67ecbdf742b66b91bcf6140c1b0e10455e40a4e62a4f2
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch058/record01/scalar-census.json
  accessed_at: '2026-10-28T06:13:12.340097Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: f41a2a5b67f7f4a806b738748e454a9eda75cb4107448708b053f918f6be1c3b
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch058/record01/validate-schema.json
  accessed_at: '2026-10-28T06:08:53.540905Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: 612931e9e184463b336511dfac3307a2ef1363c551f6ce91954776ca92b6e955
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch058/record01/validate-strict.json
  accessed_at: '2026-10-28T06:08:54.552062Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch058/record01/strict.tsv\n"
  snapshot_sha256: 02713cd33a0db95397038167623e951caa1afcd5eaf4f0aa8c5405dbc80d5a7f
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch058/record01/validate-terms.json
  accessed_at: '2026-10-28T06:08:55.660561Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: 30b30de080abea5bf401995a0fd3a1b9c335937f93144bf0c159046f91186d2b
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch058/record01/validate-references.json
  accessed_at: '2026-10-28T06:08:56.429717Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: c7f6cc7ff700161d8c895652b1710e75d38e640c07b1cf9208971cc1744f9c2f
assessments:
- assessment_id: a1
  area: identity
  topic: Exact source lineage
  outcome: supported
  summary: The generated record has one exact TOGO M812 maintained contributor. Current
    TOGO identifies original JCM782 and both sources name the same recipe. Historical
    reports mention another JCM-generated record; it is comparison context, not an
    additional selected owner or authority to merge unequal formulations.
  target_ids:
  - CultureMech:010224
  evidence_ids:
  - identity-search
  - togo812
  - jcm782
- assessment_id: a2
  area: scope
  topic: Classification and source roles
  outcome: supported
  summary: COMPLEX/UNDEFINED and LIQUID agree with yeast extract and a liquid recipe.
    Ingredient role annotations are retained as imported TOGO assertions, not independently
    proved mechanisms. No strain-level growth is inferred from the medium name.
  target_ids:
  - CultureMech:010224
  evidence_ids:
  - local-target
  - togo812
  - jcm782
- assessment_id: a3
  area: grounding
  topic: Source form and current catalog
  outcome: supported
  summary: 'The current source-compatible primary salt/hydrate IDs are retained. Potassium
    nitrate CHEBI:63043 agrees chemically; its legacy MediaIngredientMech:000170 slot
    is absent from the current catalog. Yeast extract remains an undefined mixture
    without a fabricated CHEBI identity. Scoped MnSO4·xH2O in M142 has an unresolved
    hydration count: CHEBI:86360 describes manganese sulfate without specifying that
    hydrate; no exact-hydrate claim or conversion is made.'
  target_ids:
  - CultureMech:010224
  evidence_ids:
  - grounding
  - chebi63043
  - chebi86360
  - trace-dependency
- assessment_id: a4
  area: provenance
  topic: Current writers and historical evidence
  outcome: supported
  summary: The current TOGO importer separates primary stocks and captures comments
    but bare-unit normalization still does not prove a final-liter basis. The current
    merger copies a sole contributor and preserves exact formulation assertions when
    merging multiple inputs. Historical reviews are derivative; their recommendation
    to treat every stock as mL/L or merge related records is not automatically adopted.
  target_ids:
  - CultureMech:010224
  evidence_ids:
  - writer-togo
  - writer-merge
  - writer-formulation
  - historical-reader
- assessment_id: a5
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:010224
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Distilled water", "source": {"evidence_id":
    "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[0].items[0]", "accessed_at": "2026-10-28T06:09:02.638524Z",
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
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "The source supplies 1 L distilled water as a batch solvent input,
    not 1 g/L water. Retain the liquid volume and do not use it as an explicit final-medium
    volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "The source supplies 1 L distilled
    water as a batch solvent input, not 1 g/L water. Retain the liquid volume and
    do not use it as an explicit final-medium volume."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "The source supplies 1 L distilled
    water as a batch solvent input, not 1 g/L water. Retain the liquid volume and
    do not use it as an explicit final-medium volume."}]}, {"quantity_id": "q2", "topic":
    "Yeast extract", "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[0].items[1]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"Yeast extract\",\n          \"volume\":
    1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\":
    \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }", "exact_decoded_object":
    {"component_name": "Yeast extract", "volume": 1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001003",
    "gmo_id": "GMO_001003", "label": "Yeast extract", "properties": [{"id": "GMO_000047",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000047", "label": "Undefined component"}],
    "roles": [{"id": "GMO_000042", "uri": "http://purl.jp/bio/10/gmo/GMO_000042",
    "label": "Nutrient source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "unsupported",
    "rationale": "The source directly supports 1 g of this exact component per initial
    recipe batch, but does not state a final medium volume. The local unchanged number
    in G_PER_L is therefore unsupported as a final-medium rate. The provider separately
    reports g_l on volume1055 mL; preserve that declared comparison without replacing
    the original batch basis or inventing a final concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports
    1 g of this exact component per initial recipe batch, but does not state a final
    medium volume. The local unchanged number in G_PER_L is therefore unsupported
    as a final-medium rate. The provider separately reports g_l on volume1055 mL;
    preserve that declared comparison without replacing the original batch basis or
    inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports
    1 g of this exact component per initial recipe batch, but does not state a final
    medium volume. The local unchanged number in G_PER_L is therefore unsupported
    as a final-medium rate. The provider separately reports g_l on volume1055 mL;
    preserve that declared comparison without replacing the original batch basis or
    inventing a final concentration."}]}, {"quantity_id": "q3", "topic": "NaCl", "source":
    {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[0].items[2]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\":
    \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object":
    {"component_name": "NaCl", "volume": 1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001004",
    "gmo_id": "GMO_001004", "label": "Sodium chloride", "properties": [{"id": "GMO_000040",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"},
    {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple
    component"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "unsupported",
    "rationale": "The source directly supports 1 g of this exact component per initial
    recipe batch, but does not state a final medium volume. The local unchanged number
    in G_PER_L is therefore unsupported as a final-medium rate. The provider separately
    reports g_l on volume1055 mL; preserve that declared comparison without replacing
    the original batch basis or inventing a final concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports
    1 g of this exact component per initial recipe batch, but does not state a final
    medium volume. The local unchanged number in G_PER_L is therefore unsupported
    as a final-medium rate. The provider separately reports g_l on volume1055 mL;
    preserve that declared comparison without replacing the original batch basis or
    inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports
    1 g of this exact component per initial recipe batch, but does not state a final
    medium volume. The local unchanged number in G_PER_L is therefore unsupported
    as a final-medium rate. The provider separately reports g_l on volume1055 mL;
    preserve that declared comparison without replacing the original batch basis or
    inventing a final concentration."}]}, {"quantity_id": "q4", "topic": "CaCl2・2H2O",
    "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[0].items[3]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\":
    0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\":
    \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object":
    {"component_name": "CaCl2・2H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001005",
    "gmo_id": "GMO_001005", "label": "Calcium chloride dihydrate", "properties": [{"id":
    "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple
    component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040",
    "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "unsupported",
    "rationale": "The source directly supports 0.1 g of this exact component per initial
    recipe batch, but does not state a final medium volume. The local unchanged number
    in G_PER_L is therefore unsupported as a final-medium rate. The provider separately
    reports g_l on volume1055 mL; preserve that declared comparison without replacing
    the original batch basis or inventing a final concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly
    supports 0.1 g of this exact component per initial recipe batch, but does not
    state a final medium volume. The local unchanged number in G_PER_L is therefore
    unsupported as a final-medium rate. The provider separately reports g_l on volume1055
    mL; preserve that declared comparison without replacing the original batch basis
    or inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly
    supports 0.1 g of this exact component per initial recipe batch, but does not
    state a final medium volume. The local unchanged number in G_PER_L is therefore
    unsupported as a final-medium rate. The provider separately reports g_l on volume1055
    mL; preserve that declared comparison without replacing the original batch basis
    or inventing a final concentration."}]}, {"quantity_id": "q5", "topic": "KH2PO4",
    "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[0].items[4]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"KH2PO4\",\n          \"volume\":
    0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\":
    \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "KH2PO4", "volume": 0.3, "unit": "g",
    "gmo": "http://purl.jp/bio/10/gmo/GMO_001006", "gmo_id": "GMO_001006", "label":
    "Potassium phosphate monobasic", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040",
    "label": "Inorganic compound"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038",
    "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, "decision": "unsupported",
    "rationale": "The source directly supports 0.3 g of this exact component per initial
    recipe batch, but does not state a final medium volume. The local unchanged number
    in G_PER_L is therefore unsupported as a final-medium rate. The provider separately
    reports g_l on volume1055 mL; preserve that declared comparison without replacing
    the original batch basis or inventing a final concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly
    supports 0.3 g of this exact component per initial recipe batch, but does not
    state a final medium volume. The local unchanged number in G_PER_L is therefore
    unsupported as a final-medium rate. The provider separately reports g_l on volume1055
    mL; preserve that declared comparison without replacing the original batch basis
    or inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly
    supports 0.3 g of this exact component per initial recipe batch, but does not
    state a final medium volume. The local unchanged number in G_PER_L is therefore
    unsupported as a final-medium rate. The provider separately reports g_l on volume1055
    mL; preserve that declared comparison without replacing the original batch basis
    or inventing a final concentration."}]}, {"quantity_id": "q6", "topic": "NH4Cl",
    "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[0].items[5]", "accessed_at": "2026-10-28T06:09:02.638524Z",
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
    decoded object independently equals exact JSON locator."}, "decision": "unsupported",
    "rationale": "The source directly supports 1 g of this exact component per initial
    recipe batch, but does not state a final medium volume. The local unchanged number
    in G_PER_L is therefore unsupported as a final-medium rate. The provider separately
    reports g_l on volume1055 mL; preserve that declared comparison without replacing
    the original batch basis or inventing a final concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports
    1 g of this exact component per initial recipe batch, but does not state a final
    medium volume. The local unchanged number in G_PER_L is therefore unsupported
    as a final-medium rate. The provider separately reports g_l on volume1055 mL;
    preserve that declared comparison without replacing the original batch basis or
    inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly supports
    1 g of this exact component per initial recipe batch, but does not state a final
    medium volume. The local unchanged number in G_PER_L is therefore unsupported
    as a final-medium rate. The provider separately reports g_l on volume1055 mL;
    preserve that declared comparison without replacing the original batch basis or
    inventing a final concentration."}]}, {"quantity_id": "q7", "topic": "K2HPO4",
    "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[0].items[6]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"K2HPO4\",\n          \"volume\":
    0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\":
    \"GMO_001009\",\n          \"label\": \"Potassium phosphate dibasic\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "K2HPO4", "volume": 0.3, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001009",
    "gmo_id": "GMO_001009", "label": "Potassium phosphate dibasic", "properties":
    [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label":
    "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040",
    "label": "Inorganic compound"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038",
    "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, "decision": "unsupported",
    "rationale": "The source directly supports 0.3 g of this exact component per initial
    recipe batch, but does not state a final medium volume. The local unchanged number
    in G_PER_L is therefore unsupported as a final-medium rate. The provider separately
    reports g_l on volume1055 mL; preserve that declared comparison without replacing
    the original batch basis or inventing a final concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly
    supports 0.3 g of this exact component per initial recipe batch, but does not
    state a final medium volume. The local unchanged number in G_PER_L is therefore
    unsupported as a final-medium rate. The provider separately reports g_l on volume1055
    mL; preserve that declared comparison without replacing the original batch basis
    or inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly
    supports 0.3 g of this exact component per initial recipe batch, but does not
    state a final medium volume. The local unchanged number in G_PER_L is therefore
    unsupported as a final-medium rate. The provider separately reports g_l on volume1055
    mL; preserve that declared comparison without replacing the original batch basis
    or inventing a final concentration."}]}, {"quantity_id": "q8", "topic": "MgCl2・6H2O",
    "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[0].items[7]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"MgCl2・6H2O\",\n          \"volume\":
    0.25,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\":
    \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "MgCl2・6H2O", "volume": 0.25, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001013",
    "gmo_id": "GMO_001013", "label": "Magnesium chloride hexahydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "unsupported",
    "rationale": "The source directly supports 0.25 g of this exact component per
    initial recipe batch, but does not state a final medium volume. The local unchanged
    number in G_PER_L is therefore unsupported as a final-medium rate. The provider
    separately reports g_l on volume1055 mL; preserve that declared comparison without
    replacing the original batch basis or inventing a final concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.25",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly
    supports 0.25 g of this exact component per initial recipe batch, but does not
    state a final medium volume. The local unchanged number in G_PER_L is therefore
    unsupported as a final-medium rate. The provider separately reports g_l on volume1055
    mL; preserve that declared comparison without replacing the original batch basis
    or inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.25",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly
    supports 0.25 g of this exact component per initial recipe batch, but does not
    state a final medium volume. The local unchanged number in G_PER_L is therefore
    unsupported as a final-medium rate. The provider separately reports g_l on volume1055
    mL; preserve that declared comparison without replacing the original batch basis
    or inventing a final concentration."}]}, {"quantity_id": "q9", "topic": "KCl",
    "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[0].items[8]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"KCl\",\n          \"volume\": 0.1,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\":
    \"GMO_001017\",\n          \"label\": \"Potassium chloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object":
    {"component_name": "KCl", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001017",
    "gmo_id": "GMO_001017", "label": "Potassium chloride", "properties": [{"id": "GMO_000046",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"},
    {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple
    component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040",
    "label": "Inorganic compound"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "unsupported",
    "rationale": "The source directly supports 0.1 g of this exact component per initial
    recipe batch, but does not state a final medium volume. The local unchanged number
    in G_PER_L is therefore unsupported as a final-medium rate. The provider separately
    reports g_l on volume1055 mL; preserve that declared comparison without replacing
    the original batch basis or inventing a final concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly
    supports 0.1 g of this exact component per initial recipe batch, but does not
    state a final medium volume. The local unchanged number in G_PER_L is therefore
    unsupported as a final-medium rate. The provider separately reports g_l on volume1055
    mL; preserve that declared comparison without replacing the original batch basis
    or inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly
    supports 0.1 g of this exact component per initial recipe batch, but does not
    state a final medium volume. The local unchanged number in G_PER_L is therefore
    unsupported as a final-medium rate. The provider separately reports g_l on volume1055
    mL; preserve that declared comparison without replacing the original batch basis
    or inventing a final concentration."}]}, {"quantity_id": "q10", "topic": "KNO3",
    "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[0].items[9]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"KNO3\",\n          \"volume\": 1.7,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001056\",\n          \"gmo_id\":
    \"GMO_001056\",\n          \"label\": \"Potassium nitrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object":
    {"component_name": "KNO3", "volume": 1.7, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001056",
    "gmo_id": "GMO_001056", "label": "Potassium nitrate", "properties": [{"id": "GMO_000046",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"},
    {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple
    component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040",
    "label": "Inorganic compound"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "unsupported",
    "rationale": "The source directly supports 1.7 g of this exact component per initial
    recipe batch, but does not state a final medium volume. The local unchanged number
    in G_PER_L is therefore unsupported as a final-medium rate. The provider separately
    reports g_l on volume1055 mL; preserve that declared comparison without replacing
    the original batch basis or inventing a final concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "1.7",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly
    supports 1.7 g of this exact component per initial recipe batch, but does not
    state a final medium volume. The local unchanged number in G_PER_L is therefore
    unsupported as a final-medium rate. The provider separately reports g_l on volume1055
    mL; preserve that declared comparison without replacing the original batch basis
    or inventing a final concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "1.7",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source directly
    supports 1.7 g of this exact component per initial recipe batch, but does not
    state a final medium volume. The local unchanged number in G_PER_L is therefore
    unsupported as a final-medium rate. The provider separately reports g_l on volume1055
    mL; preserve that declared comparison without replacing the original batch basis
    or inventing a final concentration."}]}, {"quantity_id": "q11", "topic": "KOH",
    "source": {"sources": [{"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[0].items[11]", "accessed_at": "2026-10-28T06:09:02.638524Z",
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
    decoded object independently equals exact JSON locator."}, {"evidence_id": "togo812",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.comments[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote":
    "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly,
    adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g.,
    5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per liter the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }",
    "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix components thoroughly,
    adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g.,
    5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per liter the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):"},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}]}, "decision": "not_quantified", "rationale": "KOH
    is the source-explicit pH-adjustment reagent; no fixed dose or stock strength
    is given. VARIABLE is not a measured concentration. Retain the reagent as scoped
    preparation with pH7.2, rather than a nominal nutrient rate.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "KOH is the source-explicit
    pH-adjustment reagent; no fixed dose or stock strength is given. VARIABLE is not
    a measured concentration. Retain the reagent as scoped preparation with pH7.2,
    rather than a nominal nutrient rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "KOH is the source-explicit
    pH-adjustment reagent; no fixed dose or stock strength is given. VARIABLE is not
    a measured concentration. Retain the reagent as scoped preparation with pH7.2,
    rather than a nominal nutrient rate."}]}, {"quantity_id": "q12", "topic": "Carbon
    dioxide gas", "source": {"sources": [{"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[0].items[12]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"Carbon dioxide gas\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\": \"GMO_002260\",\n          \"label\":
    \"Carbon dioxide gas\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\":
    \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }", "exact_decoded_object":
    {"component_name": "Carbon dioxide gas", "gmo": "http://purl.jp/bio/10/gmo/GMO_002260",
    "gmo_id": "GMO_002260", "label": "Carbon dioxide gas", "properties": [{"id": "GMO_000077",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000077", "label": "ガス"}], "roles": []},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.comments[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote":
    "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly,
    adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g.,
    5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per liter the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }",
    "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix components thoroughly,
    adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g.,
    5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per liter the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):"},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}]}, "decision": "not_quantified", "rationale": "This
    source gas is part of the explicit N2–CO2 4:1 v/v atmosphere, not a measured dissolved
    ingredient concentration. The gas mixture is quantified, but neither gas delivery
    volume nor dissolved concentration is supplied; retain the atmospheric role and
    ratio.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "This source gas
    is part of the explicit N2–CO2 4:1 v/v atmosphere, not a measured dissolved ingredient
    concentration. The gas mixture is quantified, but neither gas delivery volume
    nor dissolved concentration is supplied; retain the atmospheric role and ratio."},
    {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "This source gas
    is part of the explicit N2–CO2 4:1 v/v atmosphere, not a measured dissolved ingredient
    concentration. The gas mixture is quantified, but neither gas delivery volume
    nor dissolved concentration is supplied; retain the atmospheric role and ratio."}]},
    {"quantity_id": "q13", "topic": "Nitrogen gas", "source": {"sources": [{"evidence_id":
    "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[0].items[13]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"Nitrogen gas\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\":
    \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\":
    \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }", "exact_decoded_object":
    {"component_name": "Nitrogen gas", "gmo": "http://purl.jp/bio/10/gmo/GMO_002261",
    "gmo_id": "GMO_002261", "label": "Nitrogen gas", "properties": [{"id": "GMO_000077",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000077", "label": "ガス"}], "roles": []},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.comments[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote":
    "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly,
    adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g.,
    5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per liter the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }",
    "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix components thoroughly,
    adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g.,
    5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per liter the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):"},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}]}, "decision": "not_quantified", "rationale": "This
    source gas is part of the explicit N2–CO2 4:1 v/v atmosphere, not a measured dissolved
    ingredient concentration. The gas mixture is quantified, but neither gas delivery
    volume nor dissolved concentration is supplied; retain the atmospheric role and
    ratio.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "This source gas
    is part of the explicit N2–CO2 4:1 v/v atmosphere, not a measured dissolved ingredient
    concentration. The gas mixture is quantified, but neither gas delivery volume
    nor dissolved concentration is supplied; retain the atmospheric role and ratio."},
    {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "This source gas
    is part of the explicit N2–CO2 4:1 v/v atmosphere, not a measured dissolved ingredient
    concentration. The gas mixture is quantified, but neither gas delivery volume
    nor dissolved concentration is supplied; retain the atmospheric role and ratio."}]},
    {"quantity_id": "q14", "topic": "Trace minerals (see Medium [M142]) receiving
    dose", "source": {"sources": [{"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[0].items[10]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"Trace minerals (see Medium [M142])\",\n          \"volume\":
    10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M142\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name":
    "Trace minerals (see Medium [M142])", "volume": 10, "unit": "ml", "reference_media_id":
    "M142", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.comments[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote":
    "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly,
    adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g.,
    5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per liter the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }",
    "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix components thoroughly,
    adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g.,
    5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per liter the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):"},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}]}, "decision": "correct", "rationale": "Trace minerals
    are added as10 mL per initial batch; no final-liter dose is stated for this earlier
    table row.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].concentration", "stored_value": {"value": "10", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Trace minerals are added as10
    mL per initial batch; no final-liter dose is stated for this earlier table row."},
    {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].concentration", "stored_value": {"value": "10", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Trace minerals are added as10
    mL per initial batch; no final-liter dose is stated for this earlier table row."}]},
    {"quantity_id": "q15", "topic": "Trace minerals (see Medium [M142]) stock descriptor",
    "source": {"evidence_id": "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[0].items[10]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"Trace minerals (see Medium [M142])\",\n          \"volume\":
    10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M142\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name":
    "Trace minerals (see Medium [M142])", "volume": 10, "unit": "ml", "reference_media_id":
    "M142", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "mixed", "rationale": "Retain the existing specific preferred_term; replace the
    placeholder name and populate only supported stock identity/composition. The referenced
    stock is the trace-mineral subsection of M142/JCM151, not the whole Pyrococcus
    medium.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].name", "stored_value": "Unknown solution", "decision":
    "correct", "rationale": "Retain the existing specific preferred_term; replace
    the placeholder name and populate only supported stock identity/composition. The
    referenced stock is the trace-mineral subsection of M142/JCM151, not the whole
    Pyrococcus medium."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].name", "stored_value": "Unknown solution", "decision":
    "correct", "rationale": "Retain the existing specific preferred_term; replace
    the placeholder name and populate only supported stock identity/composition. The
    referenced stock is the trace-mineral subsection of M142/JCM151, not the whole
    Pyrococcus medium."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Retain the existing specific preferred_term; replace the placeholder
    name and populate only supported stock identity/composition. The referenced stock
    is the trace-mineral subsection of M142/JCM151, not the whole Pyrococcus medium."},
    {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Retain the existing specific preferred_term; replace the placeholder
    name and populate only supported stock identity/composition. The referenced stock
    is the trace-mineral subsection of M142/JCM151, not the whole Pyrococcus medium."},
    {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].preferred_term", "stored_value": "Trace minerals (see
    Medium [M142])", "decision": "evidence_only", "rationale": "Retain the existing
    specific preferred_term; replace the placeholder name and populate only supported
    stock identity/composition. The referenced stock is the trace-mineral subsection
    of M142/JCM151, not the whole Pyrococcus medium."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].preferred_term", "stored_value": "Trace minerals (see
    Medium [M142])", "decision": "evidence_only", "rationale": "Retain the existing
    specific preferred_term; replace the placeholder name and populate only supported
    stock identity/composition. The referenced stock is the trace-mineral subsection
    of M142/JCM151, not the whole Pyrococcus medium."}]}, {"quantity_id": "q16", "topic":
    "8% NaHCO3 solution* receiving dose", "source": {"sources": [{"evidence_id": "togo812",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[1].items[0]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"8% NaHCO3 solution*\",\n          \"volume\":
    25,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\":
    \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001119\",\n          \"gmo_id\":
    \"GMO_001119\",\n          \"label\": \"Sodium bicarbonate solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "8% NaHCO3 solution*", "volume": 25,
    "unit": "ml", "conc_value": 8, "conc_unit": "%", "gmo": "http://purl.jp/bio/10/gmo/GMO_001119",
    "gmo_id": "GMO_001119", "label": "Sodium bicarbonate solution", "properties":
    [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label":
    "Defined component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040",
    "label": "Inorganic compound"}, {"id": "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051",
    "label": "Solution"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038",
    "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "togo812",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.comments[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote":
    "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly,
    adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g.,
    5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per liter the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }",
    "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix components thoroughly,
    adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g.,
    5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per liter the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):"},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}]}, "decision": "correct", "rationale": "The post-cooling
    instruction explicitly says add per liter; 25 mL/L is supported for this addition,
    not 25 g/L. Preserve the receiving-liter instruction without treating it as a
    measured final volume after both additions.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[1].concentration", "stored_value": {"value": "25", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "The post-cooling instruction
    explicitly says add per liter; 25 mL/L is supported for this addition, not 25
    g/L. Preserve the receiving-liter instruction without treating it as a measured
    final volume after both additions."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[1].concentration", "stored_value": {"value": "25", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "The post-cooling instruction
    explicitly says add per liter; 25 mL/L is supported for this addition, not 25
    g/L. Preserve the receiving-liter instruction without treating it as a measured
    final volume after both additions."}]}, {"quantity_id": "q17", "topic": "8% NaHCO3
    solution* stock descriptor", "source": {"evidence_id": "togo812", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path":
    "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[1].items[0]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"8% NaHCO3 solution*\",\n          \"volume\":
    25,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\":
    \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001119\",\n          \"gmo_id\":
    \"GMO_001119\",\n          \"label\": \"Sodium bicarbonate solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "8% NaHCO3 solution*", "volume": 25,
    "unit": "ml", "conc_value": 8, "conc_unit": "%", "gmo": "http://purl.jp/bio/10/gmo/GMO_001119",
    "gmo_id": "GMO_001119", "label": "Sodium bicarbonate solution", "properties":
    [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label":
    "Defined component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040",
    "label": "Inorganic compound"}, {"id": "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051",
    "label": "Solution"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038",
    "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, "decision": "mixed", "rationale":
    "Retain the existing specific preferred_term; replace the placeholder name and
    populate only supported stock identity/composition. The bicarbonate 8% label has
    no stated w/v/w/w/v/v basis; preserve it verbatim without converting to a mass
    or molar concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[1].name", "stored_value": "Unknown solution", "decision":
    "correct", "rationale": "Retain the existing specific preferred_term; replace
    the placeholder name and populate only supported stock identity/composition. The
    bicarbonate 8% label has no stated w/v/w/w/v/v basis; preserve it verbatim without
    converting to a mass or molar concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[1].name", "stored_value": "Unknown solution", "decision":
    "correct", "rationale": "Retain the existing specific preferred_term; replace
    the placeholder name and populate only supported stock identity/composition. The
    bicarbonate 8% label has no stated w/v/w/w/v/v basis; preserve it verbatim without
    converting to a mass or molar concentration."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[1].composition", "stored_value": [], "decision": "add",
    "rationale": "Retain the existing specific preferred_term; replace the placeholder
    name and populate only supported stock identity/composition. The bicarbonate 8%
    label has no stated w/v/w/w/v/v basis; preserve it verbatim without converting
    to a mass or molar concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[1].composition", "stored_value": [], "decision": "add",
    "rationale": "Retain the existing specific preferred_term; replace the placeholder
    name and populate only supported stock identity/composition. The bicarbonate 8%
    label has no stated w/v/w/w/v/v basis; preserve it verbatim without converting
    to a mass or molar concentration."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[1].preferred_term", "stored_value": "8% NaHCO3 solution*",
    "decision": "evidence_only", "rationale": "Retain the existing specific preferred_term;
    replace the placeholder name and populate only supported stock identity/composition.
    The bicarbonate 8% label has no stated w/v/w/w/v/v basis; preserve it verbatim
    without converting to a mass or molar concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[1].preferred_term", "stored_value": "8% NaHCO3 solution*",
    "decision": "evidence_only", "rationale": "Retain the existing specific preferred_term;
    replace the placeholder name and populate only supported stock identity/composition.
    The bicarbonate 8% label has no stated w/v/w/w/v/v basis; preserve it verbatim
    without converting to a mass or molar concentration."}]}, {"quantity_id": "q18",
    "topic": "1 M Glucose solution receiving dose", "source": {"sources": [{"evidence_id":
    "togo812", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[1].items[1]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"1 M Glucose solution\",\n          \"volume\":
    20,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\":
    \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001465\",\n          \"gmo_id\":
    \"GMO_001465\",\n          \"label\": \"Glucose solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }", "exact_decoded_object":
    {"component_name": "1 M Glucose solution", "volume": 20, "unit": "ml", "conc_value":
    1, "conc_unit": "M", "gmo": "http://purl.jp/bio/10/gmo/GMO_001465", "gmo_id":
    "GMO_001465", "label": "Glucose solution", "properties": [{"id": "GMO_000046",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"},
    {"id": "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051", "label": "Solution"},
    {"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic
    compound"}], "roles": [{"id": "GMO_000063", "uri": "http://purl.jp/bio/10/gmo/GMO_000063",
    "label": "Carbon source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "togo812",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.comments[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote":
    "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly,
    adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g.,
    5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per liter the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }",
    "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix components thoroughly,
    adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g.,
    5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per liter the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):"},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}]}, "decision": "correct", "rationale": "The post-cooling
    instruction explicitly says add per liter; 20 mL/L is supported for this addition,
    not 20 g/L. Preserve the receiving-liter instruction without treating it as a
    measured final volume after both additions.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[2].concentration", "stored_value": {"value": "20", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "The post-cooling instruction
    explicitly says add per liter; 20 mL/L is supported for this addition, not 20
    g/L. Preserve the receiving-liter instruction without treating it as a measured
    final volume after both additions."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[2].concentration", "stored_value": {"value": "20", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "The post-cooling instruction
    explicitly says add per liter; 20 mL/L is supported for this addition, not 20
    g/L. Preserve the receiving-liter instruction without treating it as a measured
    final volume after both additions."}]}, {"quantity_id": "q19", "topic": "1 M Glucose
    solution stock descriptor", "source": {"evidence_id": "togo812", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path":
    "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.components[1].items[1]", "accessed_at": "2026-10-28T06:09:02.638524Z",
    "quote": "{\n          \"component_name\": \"1 M Glucose solution\",\n          \"volume\":
    20,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\":
    \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001465\",\n          \"gmo_id\":
    \"GMO_001465\",\n          \"label\": \"Glucose solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }", "exact_decoded_object":
    {"component_name": "1 M Glucose solution", "volume": 20, "unit": "ml", "conc_value":
    1, "conc_unit": "M", "gmo": "http://purl.jp/bio/10/gmo/GMO_001465", "gmo_id":
    "GMO_001465", "label": "Glucose solution", "properties": [{"id": "GMO_000046",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"},
    {"id": "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051", "label": "Solution"},
    {"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic
    compound"}], "roles": [{"id": "GMO_000063", "uri": "http://purl.jp/bio/10/gmo/GMO_000063",
    "label": "Carbon source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "Retain the existing specific preferred_term; replace the placeholder
    name and populate only supported stock identity/composition. The glucose stock
    is explicitly1 M. Its species is generic glucose; no D/L, anomer or hydrate is
    inferred, and the receiving-medium final molarity is not independently calculated.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[2].name", "stored_value": "Unknown solution", "decision":
    "correct", "rationale": "Retain the existing specific preferred_term; replace
    the placeholder name and populate only supported stock identity/composition. The
    glucose stock is explicitly1 M. Its species is generic glucose; no D/L, anomer
    or hydrate is inferred, and the receiving-medium final molarity is not independently
    calculated."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[2].name", "stored_value": "Unknown solution", "decision":
    "correct", "rationale": "Retain the existing specific preferred_term; replace
    the placeholder name and populate only supported stock identity/composition. The
    glucose stock is explicitly1 M. Its species is generic glucose; no D/L, anomer
    or hydrate is inferred, and the receiving-medium final molarity is not independently
    calculated."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[2].composition", "stored_value": [], "decision": "add",
    "rationale": "Retain the existing specific preferred_term; replace the placeholder
    name and populate only supported stock identity/composition. The glucose stock
    is explicitly1 M. Its species is generic glucose; no D/L, anomer or hydrate is
    inferred, and the receiving-medium final molarity is not independently calculated."},
    {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[2].composition", "stored_value": [], "decision": "add",
    "rationale": "Retain the existing specific preferred_term; replace the placeholder
    name and populate only supported stock identity/composition. The glucose stock
    is explicitly1 M. Its species is generic glucose; no D/L, anomer or hydrate is
    inferred, and the receiving-medium final molarity is not independently calculated."},
    {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[2].preferred_term", "stored_value": "1 M Glucose solution",
    "decision": "evidence_only", "rationale": "Retain the existing specific preferred_term;
    replace the placeholder name and populate only supported stock identity/composition.
    The glucose stock is explicitly1 M. Its species is generic glucose; no D/L, anomer
    or hydrate is inferred, and the receiving-medium final molarity is not independently
    calculated."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[2].preferred_term", "stored_value": "1 M Glucose solution",
    "decision": "evidence_only", "rationale": "Retain the existing specific preferred_term;
    replace the placeholder name and populate only supported stock identity/composition.
    The glucose stock is explicitly1 M. Its species is generic glucose; no D/L, anomer
    or hydrate is inferred, and the receiving-medium final molarity is not independently
    calculated."}]}, {"quantity_id": "q20", "topic": "Trace stock: Distilled water",
    "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "locator": "$.components[2].items[0]", "accessed_at": "2026-10-28T06:09:02.797070Z",
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
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "The current dependency correctly retains the 1 L stock water input
    as volume, not final makeup.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
    "field_path": "solutions[1].composition[0].concentration", "stored_value": {"value":
    "1", "unit": "L"}, "decision": "evidence_only", "rationale": "The current dependency
    correctly retains the 1 L stock water input as volume, not final makeup."}, {"path":
    "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml", "field_path":
    "solutions[0].composition", "stored_value": [], "decision": "add", "rationale":
    "Link or represent only this exact trace-stock component with its source amount
    and unresolved primary final volume; preserve the existing repaired dependency."},
    {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}]}, {"quantity_id": "q21", "topic": "Trace stock: MgSO4・7H2O", "source":
    {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "locator": "$.components[2].items[1]", "accessed_at": "2026-10-28T06:09:02.797070Z",
    "quote": "{\n          \"component_name\": \"MgSO4・7H2O\",\n          \"volume\":
    3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\":
    \"GMO_001002\",\n          \"label\": \"Magnesium sulfate heptahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "MgSO4・7H2O", "volume": 3, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001002",
    "gmo_id": "GMO_001002", "label": "Magnesium sulfate heptahydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "The current dependency already preserves the exact 3 g batch amount
    in notes and withdraws unsupported final-volume concentration. Credit this repair.
    JCM151 provides a water input, while provider J782 separately declares stock g_l;
    do not overwrite this conservative source-batch representation.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path":
    "solutions[1].composition[1].notes", "stored_value": "Role: Mineral source; Properties:
    Inorganic compound, Defined component, Simple component [Merged 2 duplicates:
    3.5, 3.0]\n\nSource batch input: 3 g. Final preparation volume is not independently
    established; the unsupported g/L assertion is withdrawn, not replaced by an assumed
    one-liter concentration.", "decision": "evidence_only", "rationale": "The current
    dependency already preserves the exact 3 g batch amount in notes and withdraws
    unsupported final-volume concentration. Credit this repair. JCM151 provides a
    water input, while provider J782 separately declares stock g_l; do not overwrite
    this conservative source-batch representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}]}, {"quantity_id": "q22", "topic": "Trace stock: NaCl", "source":
    {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "locator": "$.components[2].items[2]", "accessed_at": "2026-10-28T06:09:02.797070Z",
    "quote": "{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\":
    \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "NaCl", "volume": 1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001004",
    "gmo_id": "GMO_001004", "label": "Sodium chloride", "properties": [{"id": "GMO_000040",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"},
    {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined
    component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "The current dependency already preserves the exact 1 g batch amount
    in notes and withdraws unsupported final-volume concentration. Credit this repair.
    JCM151 provides a water input, while provider J782 separately declares stock g_l;
    do not overwrite this conservative source-batch representation.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path":
    "solutions[1].composition[2].notes", "stored_value": "Role: Mineral source; Properties:
    Inorganic compound, Defined component, Simple component [Merged 2 duplicates:
    13.85, 1.0]\n\nSource batch input: 1 g. Final preparation volume is not independently
    established; the unsupported g/L assertion is withdrawn, not replaced by an assumed
    one-liter concentration.", "decision": "evidence_only", "rationale": "The current
    dependency already preserves the exact 1 g batch amount in notes and withdraws
    unsupported final-volume concentration. Credit this repair. JCM151 provides a
    water input, while provider J782 separately declares stock g_l; do not overwrite
    this conservative source-batch representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}]}, {"quantity_id": "q23", "topic": "Trace stock: CaCl2・2H2O", "source":
    {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "locator": "$.components[2].items[3]", "accessed_at": "2026-10-28T06:09:02.797070Z",
    "quote": "{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\":
    0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\":
    \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "CaCl2・2H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001005",
    "gmo_id": "GMO_001005", "label": "Calcium chloride dihydrate", "properties": [{"id":
    "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic
    compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "The current dependency already preserves the exact 0.1 g batch amount
    in notes and withdraws unsupported final-volume concentration. Credit this repair.
    JCM151 provides a water input, while provider J782 separately declares stock g_l;
    do not overwrite this conservative source-batch representation.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path":
    "solutions[1].composition[3].notes", "stored_value": "Role: Mineral source; Properties:
    Inorganic compound, Defined component, Simple component\n\nSource batch input:
    0.1 g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "evidence_only", "rationale": "The current dependency already preserves
    the exact 0.1 g batch amount in notes and withdraws unsupported final-volume concentration.
    Credit this repair. JCM151 provides a water input, while provider J782 separately
    declares stock g_l; do not overwrite this conservative source-batch representation."},
    {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}]}, {"quantity_id": "q24", "topic": "Trace stock: Na2MoO4・2H2O",
    "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "locator": "$.components[2].items[4]", "accessed_at": "2026-10-28T06:09:02.797070Z",
    "quote": "{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\":
    0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\":
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
    "Na2MoO4・2H2O", "volume": 0.01, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001011",
    "gmo_id": "GMO_001011", "label": "Sodium molybdate dihydrate", "properties": [{"id":
    "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic
    compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "The current dependency already preserves the exact 0.01 g batch
    amount in notes and withdraws unsupported final-volume concentration. Credit this
    repair. JCM151 provides a water input, while provider J782 separately declares
    stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path":
    "solutions[1].composition[4].notes", "stored_value": "Role: Mineral source; Properties:
    Inorganic compound, Defined component, Simple component\n\nSource batch input:
    0.01 g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "evidence_only", "rationale": "The current dependency already preserves
    the exact 0.01 g batch amount in notes and withdraws unsupported final-volume
    concentration. Credit this repair. JCM151 provides a water input, while provider
    J782 separately declares stock g_l; do not overwrite this conservative source-batch
    representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}]}, {"quantity_id": "q25", "topic": "Trace stock: H3BO3", "source":
    {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "locator": "$.components[2].items[5]", "accessed_at": "2026-10-28T06:09:02.797070Z",
    "quote": "{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\":
    \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "H3BO3", "volume": 0.01, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001015",
    "gmo_id": "GMO_001015", "label": "Boric acid", "properties": [{"id": "GMO_000040",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"},
    {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined
    component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "The current dependency already preserves the exact 0.01 g batch
    amount in notes and withdraws unsupported final-volume concentration. Credit this
    repair. JCM151 provides a water input, while provider J782 separately declares
    stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path":
    "solutions[1].composition[5].notes", "stored_value": "Role: Mineral source; Properties:
    Inorganic compound, Defined component, Simple component [Merged 2 duplicates:
    15.0, 0.01]\n\nSource batch input: 0.01 g. Final preparation volume is not independently
    established; the unsupported g/L assertion is withdrawn, not replaced by an assumed
    one-liter concentration.", "decision": "evidence_only", "rationale": "The current
    dependency already preserves the exact 0.01 g batch amount in notes and withdraws
    unsupported final-volume concentration. Credit this repair. JCM151 provides a
    water input, while provider J782 separately declares stock g_l; do not overwrite
    this conservative source-batch representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}]}, {"quantity_id": "q26", "topic": "Trace stock: FeSO4・7H2O", "source":
    {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "locator": "$.components[2].items[6]", "accessed_at": "2026-10-28T06:09:02.797070Z",
    "quote": "{\n          \"component_name\": \"FeSO4・7H2O\",\n          \"volume\":
    0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\":
    \"GMO_001016\",\n          \"label\": \"Iron(II) sulfate heptahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "FeSO4・7H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001016",
    "gmo_id": "GMO_001016", "label": "Iron(II) sulfate heptahydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "The current dependency already preserves the exact 0.1 g batch amount
    in notes and withdraws unsupported final-volume concentration. Credit this repair.
    JCM151 provides a water input, while provider J782 separately declares stock g_l;
    do not overwrite this conservative source-batch representation.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path":
    "solutions[1].composition[6].notes", "stored_value": "Role: Mineral source; Properties:
    Inorganic compound, Defined component, Simple component\n\nSource batch input:
    0.1 g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "evidence_only", "rationale": "The current dependency already preserves
    the exact 0.1 g batch amount in notes and withdraws unsupported final-volume concentration.
    Credit this repair. JCM151 provides a water input, while provider J782 separately
    declares stock g_l; do not overwrite this conservative source-batch representation."},
    {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}]}, {"quantity_id": "q27", "topic": "Trace stock: ZnSO4・7H2O", "source":
    {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "locator": "$.components[2].items[7]", "accessed_at": "2026-10-28T06:09:02.797070Z",
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
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "The current dependency already preserves the exact 0.1 g batch amount
    in notes and withdraws unsupported final-volume concentration. Credit this repair.
    JCM151 provides a water input, while provider J782 separately declares stock g_l;
    do not overwrite this conservative source-batch representation.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path":
    "solutions[1].composition[7].notes", "stored_value": "Role: Mineral source; Properties:
    Inorganic compound, Defined component, Simple component\n\nSource batch input:
    0.1 g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "evidence_only", "rationale": "The current dependency already preserves
    the exact 0.1 g batch amount in notes and withdraws unsupported final-volume concentration.
    Credit this repair. JCM151 provides a water input, while provider J782 separately
    declares stock g_l; do not overwrite this conservative source-batch representation."},
    {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}]}, {"quantity_id": "q28", "topic": "Trace stock: CuSO4・5H2O", "source":
    {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "locator": "$.components[2].items[8]", "accessed_at": "2026-10-28T06:09:02.797070Z",
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
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "The current dependency already preserves the exact 0.01 g batch
    amount in notes and withdraws unsupported final-volume concentration. Credit this
    repair. JCM151 provides a water input, while provider J782 separately declares
    stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path":
    "solutions[1].composition[8].notes", "stored_value": "Role: Mineral source; Properties:
    Inorganic compound, Defined component, Simple component\n\nSource batch input:
    0.01 g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "evidence_only", "rationale": "The current dependency already preserves
    the exact 0.01 g batch amount in notes and withdraws unsupported final-volume
    concentration. Credit this repair. JCM151 provides a water input, while provider
    J782 separately declares stock g_l; do not overwrite this conservative source-batch
    representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}]}, {"quantity_id": "q29", "topic": "Trace stock: CoSO4・7H2O", "source":
    {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "locator": "$.components[2].items[9]", "accessed_at": "2026-10-28T06:09:02.797070Z",
    "quote": "{\n          \"component_name\": \"CoSO4・7H2O\",\n          \"volume\":
    0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001050\",\n          \"gmo_id\":
    \"GMO_001050\",\n          \"label\": \"Cobalt(II) sulfate heptahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "CoSO4・7H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001050",
    "gmo_id": "GMO_001050", "label": "Cobalt(II) sulfate heptahydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "The current dependency already preserves the exact 0.1 g batch amount
    in notes and withdraws unsupported final-volume concentration. Credit this repair.
    JCM151 provides a water input, while provider J782 separately declares stock g_l;
    do not overwrite this conservative source-batch representation.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path":
    "solutions[1].composition[9].notes", "stored_value": "Role: Mineral source; Properties:
    Inorganic compound, Defined component, Simple component\n\nSource batch input:
    0.1 g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "evidence_only", "rationale": "The current dependency already preserves
    the exact 0.1 g batch amount in notes and withdraws unsupported final-volume concentration.
    Credit this repair. JCM151 provides a water input, while provider J782 separately
    declares stock g_l; do not overwrite this conservative source-batch representation."},
    {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}]}, {"quantity_id": "q30", "topic": "Trace stock: Nitrilotriacetic
    acid", "source": {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "locator": "$.components[2].items[10]", "accessed_at": "2026-10-28T06:09:02.797070Z",
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
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "The current dependency already preserves the exact 1.5 g batch amount
    in notes and withdraws unsupported final-volume concentration. Credit this repair.
    JCM151 provides a water input, while provider J782 separately declares stock g_l;
    do not overwrite this conservative source-batch representation.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path":
    "solutions[1].composition[10].notes", "stored_value": "Role: Mineral source; Properties:
    Organic compound, Defined component, Simple component\n\nSource batch input: 1.5
    g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "evidence_only", "rationale": "The current dependency already preserves
    the exact 1.5 g batch amount in notes and withdraws unsupported final-volume concentration.
    Credit this repair. JCM151 provides a water input, while provider J782 separately
    declares stock g_l; do not overwrite this conservative source-batch representation."},
    {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}]}, {"quantity_id": "q31", "topic": "Trace stock: MnSO4・xH2O", "source":
    {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "locator": "$.components[2].items[11]", "accessed_at": "2026-10-28T06:09:02.797070Z",
    "quote": "{\n          \"component_name\": \"MnSO4・xH2O\",\n          \"volume\":
    0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001065\",\n          \"gmo_id\":
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
    "MnSO4・xH2O", "volume": 0.5, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001065",
    "gmo_id": "GMO_001065", "label": "Manganese sulfate n-hydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "The current dependency already preserves the exact 0.5 g batch amount
    in notes and withdraws unsupported final-volume concentration. Credit this repair.
    JCM151 provides a water input, while provider J782 separately declares stock g_l;
    do not overwrite this conservative source-batch representation.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path":
    "solutions[1].composition[11].notes", "stored_value": "Role: Mineral source; Properties:
    Inorganic compound, Defined component, Simple component\n\nSource batch input:
    0.5 g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "evidence_only", "rationale": "The current dependency already preserves
    the exact 0.5 g batch amount in notes and withdraws unsupported final-volume concentration.
    Credit this repair. JCM151 provides a water input, while provider J782 separately
    declares stock g_l; do not overwrite this conservative source-batch representation."},
    {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}]}, {"quantity_id": "q32", "topic": "Trace stock: AlK(SO4)2", "source":
    {"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "locator": "$.components[2].items[12]", "accessed_at": "2026-10-28T06:09:02.797070Z",
    "quote": "{\n          \"component_name\": \"AlK(SO4)2\",\n          \"volume\":
    0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001088\",\n          \"gmo_id\":
    \"GMO_001088\",\n          \"label\": \"Aluminum potassium sulfate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "AlK(SO4)2", "volume": 0.01, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001088",
    "gmo_id": "GMO_001088", "label": "Aluminum potassium sulfate", "properties": [{"id":
    "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic
    compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "The current dependency already preserves the exact 0.01 g batch
    amount in notes and withdraws unsupported final-volume concentration. Credit this
    repair. JCM151 provides a water input, while provider J782 separately declares
    stock g_l; do not overwrite this conservative source-batch representation.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path":
    "solutions[1].composition[12].notes", "stored_value": "Role: Mineral source; Properties:
    Inorganic compound, Defined component, Simple component\n\nSource batch input:
    0.01 g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "evidence_only", "rationale": "The current dependency already preserves
    the exact 0.01 g batch amount in notes and withdraws unsupported final-volume
    concentration. Credit this repair. JCM151 provides a water input, while provider
    J782 separately declares stock g_l; do not overwrite this conservative source-batch
    representation."}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Link or represent only this exact trace-stock component with its
    source amount and unresolved primary final volume; preserve the existing repaired
    dependency."}]}, {"quantity_id": "q33", "topic": "Trace-stock KOH and pH", "source":
    {"sources": [{"evidence_id": "togo142", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "locator": "$.components[2].items[13]", "accessed_at": "2026-10-28T06:09:02.797070Z",
    "quote": "{\n          \"component_name\": \"KOH solution\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\": \"GMO_001903\",\n          \"label\":
    \"Potassium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "KOH solution", "gmo": "http://purl.jp/bio/10/gmo/GMO_001903", "gmo_id": "GMO_001903",
    "label": "Potassium hydroxide solution", "properties": [{"id": "GMO_000046", "uri":
    "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id":
    "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051", "label": "Solution"}],
    "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "togo142",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "raw_path": "REVIEW_WORK/batch058/source01-03/togo142.bin", "raw_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "locator": "$.comments[1]", "accessed_at": "2026-10-28T06:09:02.797070Z", "quote":
    "{\n      \"paragraph_index\": 5,\n      \"comment\": \"Dissolve nitrilotriacetic
    acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust
    final pH to 7.0.\"\n    }", "exact_decoded_object": {"paragraph_index": 5, "comment":
    "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed
    to add minerals. Adjust final pH to 7.0."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}]}, "decision":
    "evidence_only", "rationale": "The trace-stock KOH adjustment has no fixed dose/strength.
    The existing dependency records that limitation; the primary trace process specifies
    pH6.5 then7.0. The parent receiving dose is not transferred.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path":
    "solutions[1].solutions[0].notes", "stored_value": "Role: Mineral source; Properties:
    Defined component, Solution\n\npH-adjustment reagent; no fixed dose is specified.
    Normality is not converted to molarity.", "decision": "evidence_only", "rationale":
    "The trace-stock KOH adjustment has no fixed dose/strength. The existing dependency
    records that limitation; the primary trace process specifies pH6.5 then7.0. The
    parent receiving dose is not transferred."}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
    "field_path": "solutions[1].preparation_notes", "stored_value": "Dissolve nitrilotriacetic
    acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust
    final pH to 7.0.", "decision": "evidence_only", "rationale": "The trace-stock
    KOH adjustment has no fixed dose/strength. The existing dependency records that
    limitation; the primary trace process specifies pH6.5 then7.0. The parent receiving
    dose is not transferred."}]}, {"quantity_id": "q34", "topic": "Main preparation
    and numeric process scope", "source": {"evidence_id": "togo812", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M812", "raw_path":
    "REVIEW_WORK/batch058/source01-03/togo812.bin", "raw_sha256": "a51d365cc30d7a4d2f747af760e537bf59acee8cf334bf65418802c424e75d14",
    "locator": "$.comments[0]", "accessed_at": "2026-10-28T06:09:02.638524Z", "quote":
    "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly,
    adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g.,
    5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per liter the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):\"\n    }",
    "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix components thoroughly,
    adjust pH to 7.2 with KOH and distribute the medium into culture vessels (e.g.,
    5 ml of the medium in the Hungate tubes) under a N2--CO2 (4:1, v/v) gas mixture,
    seal with butyl rubber stoppers and autoclave. After cooling, add per liter the
    following solutions from anaerobic stocks (autoclaved or *filter--sterilized):"},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, "decision": "add", "rationale": "Add the exact source
    process with pH7.2, the example5 mL vessel fill (an example, not a universal prescription),
    4:1 v/v N2–CO2, closure/autoclaving and the post-cooling per-liter additions.
    The trace-stock pH6.5 then7.0 must remain separate from the main-medium pH.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Add the exact source process with pH7.2, the example5 mL vessel fill (an example,
    not a universal prescription), 4:1 v/v N2–CO2, closure/autoclaving and the post-cooling
    per-liter additions. The trace-stock pH6.5 then7.0 must remain separate from the
    main-medium pH.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Add the exact source process with pH7.2, the example5 mL vessel fill (an example,
    not a universal prescription), 4:1 v/v N2–CO2, closure/autoclaving and the post-cooling
    per-liter additions. The trace-stock pH6.5 then7.0 must remain separate from the
    main-medium pH.", "missing": true}, {"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "ph_value", "stored_value": null, "decision": "add", "rationale":
    "Add the exact source process with pH7.2, the example5 mL vessel fill (an example,
    not a universal prescription), 4:1 v/v N2–CO2, closure/autoclaving and the post-cooling
    per-liter additions. The trace-stock pH6.5 then7.0 must remain separate from the
    main-medium pH.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "ph_value", "stored_value": null, "decision": "add", "rationale":
    "Add the exact source process with pH7.2, the example5 mL vessel fill (an example,
    not a universal prescription), 4:1 v/v N2–CO2, closure/autoclaving and the post-cooling
    per-liter additions. The trace-stock pH6.5 then7.0 must remain separate from the
    main-medium pH.", "missing": true}]}, {"quantity_id": "q35", "topic": "JCM default
    sterilization and explicit exception", "source": {"evidence_id": "jcm782", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=782", "raw_path": "REVIEW_WORK/batch058/source01-03/jcm782.bin",
    "raw_sha256": "61323f3bfd79a7fb32371ed2713b6ad4d03ddea38f9975a465b727e98cf801ee",
    "locator": "Default header and starred post-cooling addition", "accessed_at":
    "2026-10-28T06:09:02.690012Z", "quote": "Unless otherwise stated, sterilize media
    by autoclaving at 121°C for 15 min."}, "decision": "add", "rationale": "JCM782
    explicitly supplies the global default121°C for15 min unless otherwise stated;
    apply only to the stated autoclaving step. The starred bicarbonate is explicitly
    filter-sterilized instead. Do not invent a filtration pore size or a separate
    glucose autoclaving exception.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "JCM782 explicitly supplies the global default121°C for15 min unless otherwise
    stated; apply only to the stated autoclaving step. The starred bicarbonate is
    explicitly filter-sterilized instead. Do not invent a filtration pore size or
    a separate glucose autoclaving exception.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "JCM782 explicitly supplies the global default121°C for15 min unless otherwise
    stated; apply only to the stated autoclaving step. The starred bicarbonate is
    explicitly filter-sterilized instead. Do not invent a filtration pore size or
    a separate glucose autoclaving exception.", "missing": true}]}]'
- assessment_id: a6
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: supported
  summary: The grounding inventory enumerates every asserted identifier and exact
    preferred label. Exact identifier rows and ontology-linked rows are recorded separately,
    including mapping_status. Present catalog membership does not validate supplied
    hydrate form or historical identity; specific limits are assessed separately.
  target_ids:
  - CultureMech:010224
  evidence_ids:
  - grounding
- assessment_id: a7
  area: provenance
  topic: History and evidence scope
  outcome: supported
  summary: Complete owner and target histories were read. Current source bytes and
    inspected code are independent evidence; historical timestamps remain historical
    claims unless an exact cited raw digest is recovered.
  target_ids:
  - CultureMech:010224
  evidence_ids:
  - history
  - scalars
- assessment_id: a8
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:010224
  evidence_ids:
  - local-target
- assessment_id: a9
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:010224
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-010224-liquid-solvent-and-stock-additions-have-mass-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Liquid solvent and stock additions have mass units
  description: The target and TOGO owner store1 L water as1 G_PER_L and the10,25,20
    mL stock additions as10,25,20 G_PER_L. Restore water volume and distinguish the
    initial trace-mineral batch addition from the two explicitly per-liter late additions.
    No density or final-medium volume is inferred.
  target_ids:
  - CultureMech:010224
  field_paths:
  - ingredients[0].concentration
  - solutions[0].concentration
  - solutions[1].concentration
  - solutions[2].concentration
  evidence_ids:
  - jcm782
  - togo812
  - quantities
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-010224-main-batch-masses-are-unsupported-as-unchanged-final-medium-rates
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Main batch masses are unsupported as unchanged final-medium rates
  description: Nine non-solvent main ingredients use the literal source batch gram
    numbers as G_PER_L. JCM782 supplies1 L water and further stock additions without
    an explicit final-volume makeup. Provider J782 reports different g_l rates on
    declared1055 mL. Keep both source assertions distinct and preserve the batch masses;
    neither source permits silently endorsing the local unchanged values as measured
    final concentrations.
  target_ids:
  - CultureMech:010224
  field_paths:
  - ingredients[1].concentration
  - ingredients[2].concentration
  - ingredients[3].concentration
  - ingredients[4].concentration
  - ingredients[5].concentration
  - ingredients[6].concentration
  - ingredients[7].concentration
  - ingredients[8].concentration
  - ingredients[9].concentration
  evidence_ids:
  - jcm782
  - togo812
  - apiJ782
  - quantities
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-010224-named-stocks-remain-empty-placeholder-shells
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Named stocks remain empty placeholder shells
  description: All three solutions retain informative preferred_term text but have
    Unknown solution names and empty composition. The trace stock is scoped to the
    JCM151/M142 trace subsection; the bicarbonate stock has a bare8% label and glucose
    is1 M. Credit the already repaired M142 composition notes; do not transfer its
    Pyrococcus main recipe, salt base or receiving dose.
  target_ids:
  - CultureMech:010224
  field_paths:
  - solutions[0].name
  - solutions[0].composition
  - solutions[1].name
  - solutions[1].composition
  - solutions[2].name
  - solutions[2].composition
  evidence_ids:
  - jcm782
  - jcm151
  - togo142
  - trace-dependency
  - quantities
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-010224-source-preparation-and-ph-are-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation and pH are missing
  description: The target and owner lack preparation_steps and ph_value despite exact
    JCM/TOGO instructions. KOH and gases appear only as VARIABLE ingredients, which
    does not encode the pH adjustment,4:1 atmosphere, vessel example, sterilization
    or late-addition stages.
  target_ids:
  - CultureMech:010224
  field_paths:
  - preparation_steps
  - ph_value
  - ingredients[10].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  evidence_ids:
  - jcm782
  - togo812
  - quantities
  - writer-togo
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f5
  issue_key: culturemech-010224-potassium-nitrate-retains-an-unresolved-legacy-catalog-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Potassium nitrate retains an unresolved legacy catalog link
  description: The current primary CHEBI:63043 correctly identifies potassium nitrate,
    but the separate MediaIngredientMech:000170 identifier has no exact current packaged
    catalog row. This is a current resolution limitation, not a claim that its historical
    identity was invalid.
  target_ids:
  - CultureMech:010224
  field_paths:
  - ingredients[9].mediaingredientmech_term
  evidence_ids:
  - grounding
  - chebi63043
  rule_id: current-legacy-link-resolution
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Preserve the source1 L water input as a solvent/preparation volume;
    represent10 mL trace stock per initial batch and25/20 mL per receiving liter for
    the post-cooling stocks. Retain exact source evidence at the root for solution/preparation
    claims; regenerate after owner curation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010224
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Retain each exact source batch amount with scoped evidence and mark
    the final-medium basis unresolved. If adopting provider-reported rates, identify
    that provider stage explicitly and reconcile it with the primary per-liter addition
    instructions rather than inventing a common denominator.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010224
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Replace placeholder names and resolve or link the exact stock contents.
    Preserve the M142 trace repairs and source-supported1 M glucose stock; keep bicarbonate
    percentage basis unresolved. Record each dose separately with root evidence and
    no double-counted components.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010224
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: Add only the exact source process and pH with stage-qualified root
    evidence. Preserve the5 mL example as an example, gas ratio as atmosphere rather
    than dissolved concentration, and starred filtration exception. Keep unquantified
    titrant and gas volumes unspecified.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010224
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action5
  description: Resolve the legacy slot against the pinned current catalog while preserving
    source potassium nitrate identity and append-only historical provenance. Do not
    fabricate a replacement from a label-only match.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:010224
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M812_Caldinitratiruptor_Microaerophilus_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- The JCM main table gives a water input, not an explicit final-medium makeup; provider1055
  mL and explicit g_l remain separately attributed. The two late stock additions alone
  have an explicit per-liter instruction.
- The bicarbonate8% basis is unspecified; no density, molecular-weight, final-medium
  molarity or gas dissolution calculation was used. M142 MnSO4 hydration is unspecified;
  no exact hydrate conversion is justified.
- Only the M142/JCM151 trace-mineral subsection is in dependency scope. Parent main
  medium, salt-base formulation, receiving dose, organism claims and variants are
  excluded.
- Current source-byte matches do not prove historical access events or scientific
  correctness of older report recommendations. Same-source neighboring JCM imports
  were not promoted to selected owners.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
