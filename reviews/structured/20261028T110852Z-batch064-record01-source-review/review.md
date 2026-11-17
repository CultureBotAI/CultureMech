# Source and stage review of Clostridium thermosulfurogenes medium

- Review: 20261028T110852Z-batch064-record01-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T10:58:48.916559Z
- Finished UTC: 2026-10-28T11:08:52.785113Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The sole TOGO M768 contributor resolves to JCM743. All canonical diagnostics pass, but trace-stock contents are flattened, mass/volume units are conflated, stock stubs and preparation are incomplete, and three hydrate identities are mismatched. The later owner water repair is credited separately from the stale generated record. JCM743 currently returns Nothing found; usable TOGO/MediaDive evidence supports a partial review.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch064 native selection index 01.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010175 | data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml | generated | clostridium_thermosulfurogenes_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010175 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:010175 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:010175 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:010175 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact record and lineage

identity: supported. Targets: CultureMech:010175.

Generated CM010175 has one exact owner TOGO M768, whose source metadata identifies JCM743. No nearby DSM211/KOMODO211 or similarly named branch is used as owner.

### Classification and source stages

representation: concern. Targets: CultureMech:010175.

Liquid complex/undefined classification is consistent with yeast extract and no agar in this exact source. Main and trace-stock ingredients are wrongly combined; source role notes are descriptive imported annotations, not independent mechanistic evidence.

### Available primary and provider sources

evidence: unknown. Targets: CultureMech:010175.

Exact JCM743 endpoint supplies Nothing found. Two provider representations independently expose the same source identity and stage graph, but cannot replace an unavailable direct primary formulation. JCM197 corroborates only the referenced vitamin stock.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:010175.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Distilled water", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[0].items[0]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo": "http://purl.jp/bio/10/gmo/GMO_001001", "gmo_id": "GMO_001001", "label": "Distilled water", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044", "label": "Solvating media"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Main recipe and trace-stock recipe each list separate 1 L water inputs. Target 2.0 G_PER_L sums different stages; owner 1.0 G_PER_L removes a numerical duplicate but still conflates stages and uses a mass unit. Preserve separate water inputs without treating either as measured final volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "2.0", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Main recipe and trace-stock recipe each list separate 1 L water inputs. Target 2.0 G_PER_L sums different stages; owner 1.0 G_PER_L removes a numerical duplicate but still conflates stages and uses a mass unit. Preserve separate water inputs without treating either as measured final volume."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1.0", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Main recipe and trace-stock recipe each list separate 1 L water inputs. Target 2.0 G_PER_L sums different stages; owner 1.0 G_PER_L removes a numerical duplicate but still conflates stages and uses a mass unit. Preserve separate water inputs without treating either as measured final volume."}], "corroboration": [{"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[1].items[0]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo": "http://purl.jp/bio/10/gmo/GMO_001001", "gmo_id": "GMO_001001", "label": "Distilled water", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044", "label": "Solvating media"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}]}, {"quantity_id": "q2", "topic": "Yeast extract", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[0].items[1]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"Yeast extract\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Yeast extract", "volume": 1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001003", "gmo_id": "GMO_001003", "label": "Yeast extract", "properties": [{"id": "GMO_000047", "uri": "http://purl.jp/bio/10/gmo/GMO_000047", "label": "Undefined component"}], "roles": [{"id": "GMO_000042", "uri": "http://purl.jp/bio/10/gmo/GMO_000042", "label": "Nutrient source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "Source main-batch mass 1 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 1 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 1 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately."}]}, {"quantity_id": "q3", "topic": "KH2PO4", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[0].items[2]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "KH2PO4", "volume": 0.3, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001006", "gmo_id": "GMO_001006", "label": "Potassium phosphate monobasic", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038", "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "Source main-batch mass 0.3 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 0.3 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 0.3 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately."}]}, {"quantity_id": "q4", "topic": "NH4Cl", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[0].items[3]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "NH4Cl", "volume": 1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001008", "gmo_id": "GMO_001008", "label": "Ammonium chloride", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000062", "uri": "http://purl.jp/bio/10/gmo/GMO_000062", "label": "Nitrogen source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "Source main-batch mass 1 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 1 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 1 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately."}]}, {"quantity_id": "q5", "topic": "Resazurin", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[0].items[4]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\": \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Resazurin", "volume": 1, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001012", "gmo_id": "GMO_001012", "label": "Resazurin", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000055", "uri": "http://purl.jp/bio/10/gmo/GMO_000055", "label": "pH dependent redox indicator"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source main-batch input is 1 mg; stored same numeral G_PER_L has wrong mass unit and unsupported final-volume basis. Preserve explicit mass without assuming one final liter.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source main-batch input is 1 mg; stored same numeral G_PER_L has wrong mass unit and unsupported final-volume basis. Preserve explicit mass without assuming one final liter."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source main-batch input is 1 mg; stored same numeral G_PER_L has wrong mass unit and unsupported final-volume basis. Preserve explicit mass without assuming one final liter."}]}, {"quantity_id": "q6", "topic": "MgCl2・6H2O", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[0].items[5]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "MgCl2・6H2O", "volume": 0.2, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001013", "gmo_id": "GMO_001013", "label": "Magnesium chloride hexahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "Source main-batch mass 0.2 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 0.2 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 0.2 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately."}]}, {"quantity_id": "q7", "topic": "Na2S・9H2O", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[0].items[6]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"Na2S・9H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\": \"GMO_001014\",\n          \"label\": \"Sodium sulfide nonahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Na2S・9H2O", "volume": 0.5, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001014", "gmo_id": "GMO_001014", "label": "Sodium sulfide nonahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000064", "uri": "http://purl.jp/bio/10/gmo/GMO_000064", "label": "Reducing agent"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "Source main-batch mass 0.5 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 0.5 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 0.5 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately."}]}, {"quantity_id": "q8", "topic": "FeSO4・7H2O", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[0].items[7]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\": \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "FeSO4・7H2O", "volume": 1.5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001016", "gmo_id": "GMO_001016", "label": "Iron(II) sulfate heptahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source main-batch input is 1.5 mg; stored same numeral G_PER_L has wrong mass unit and unsupported final-volume basis. Preserve explicit mass without assuming one final liter.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source main-batch input is 1.5 mg; stored same numeral G_PER_L has wrong mass unit and unsupported final-volume basis. Preserve explicit mass without assuming one final liter."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source main-batch input is 1.5 mg; stored same numeral G_PER_L has wrong mass unit and unsupported final-volume basis. Preserve explicit mass without assuming one final liter."}]}, {"quantity_id": "q9", "topic": "Na2HPO4・12H2O", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[0].items[8]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"Na2HPO4・12H2O\",\n          \"volume\": 5.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001115\",\n          \"gmo_id\": \"GMO_001115\",\n          \"label\": \"Disodium phosphate dodecahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Na2HPO4・12H2O", "volume": 5.3, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001115", "gmo_id": "GMO_001115", "label": "Disodium phosphate dodecahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038", "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "Source main-batch mass 5.3 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "5.3", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 5.3 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "5.3", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 5.3 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately."}]}, {"quantity_id": "q10", "topic": "Glucose", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[0].items[9]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"Glucose\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001815\",\n          \"gmo_id\": \"GMO_001815\",\n          \"label\": \"Glucose\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Glucose", "volume": 5, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001815", "gmo_id": "GMO_001815", "label": "Glucose", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000063", "uri": "http://purl.jp/bio/10/gmo/GMO_000063", "label": "Carbon source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "unsupported", "rationale": "Source main-batch mass 5 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 5 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 5 g agrees numerically, but a water input of 1 L does not establish final volume. Current G_PER_L is not independently verified; MediaDive declares a different g_l using nominal volume 1015. Preserve the batch mass and qualify any provider rate separately."}]}, {"quantity_id": "q11", "topic": "HCl", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[0].items[12]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"HCl\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"N\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "HCl", "conc_value": 1, "conc_unit": "N", "gmo": "http://purl.jp/bio/10/gmo/GMO_001499", "gmo_id": "GMO_001499", "label": "Hydrochloric acid solution", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051", "label": "Solution"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044", "label": "Solvating media"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "not_quantified", "rationale": "No fixed titrant amount is specified, so VARIABLE remains an unquantified placeholder; HCl 1 N is reagent strength for separately prepared sulfide, not a fixed final-medium dose.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "No fixed titrant amount is specified, so VARIABLE remains an unquantified placeholder; HCl 1 N is reagent strength for separately prepared sulfide, not a fixed final-medium dose."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "No fixed titrant amount is specified, so VARIABLE remains an unquantified placeholder; HCl 1 N is reagent strength for separately prepared sulfide, not a fixed final-medium dose."}]}, {"quantity_id": "q12", "topic": "NaCl", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[1].items[1]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "NaCl", "volume": 1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001004", "gmo_id": "GMO_001004", "label": "Sodium chloride", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source trace-stock input is 1 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 1 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 1 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}]}, {"quantity_id": "q13", "topic": "CaCl2・2H2O", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[1].items[2]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "CaCl2・2H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001005", "gmo_id": "GMO_001005", "label": "Calcium chloride dihydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source trace-stock input is 0.1 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 0.1 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 0.1 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}]}, {"quantity_id": "q14", "topic": "Na2MoO4・2H2O", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[1].items[3]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Na2MoO4・2H2O", "volume": 10, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001011", "gmo_id": "GMO_001011", "label": "Sodium molybdate dihydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source trace-stock input is 10 mg; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 10 mg; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 10 mg; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}]}, {"quantity_id": "q15", "topic": "H3BO3", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[1].items[4]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "H3BO3", "volume": 10, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001015", "gmo_id": "GMO_001015", "label": "Boric acid", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source trace-stock input is 10 mg; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 10 mg; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 10 mg; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}]}, {"quantity_id": "q16", "topic": "MnCl2・4H2O", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[1].items[5]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "MnCl2・4H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001020", "gmo_id": "GMO_001020", "label": "Manganese chloride tetrahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source trace-stock input is 0.1 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 0.1 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 0.1 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}]}, {"quantity_id": "q17", "topic": "CoCl2・6H2O", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[1].items[6]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 0.17,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "CoCl2・6H2O", "volume": 0.17, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001021", "gmo_id": "GMO_001021", "label": "Cobalt dichloride hexahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source trace-stock input is 0.17 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.17", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 0.17 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.17", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 0.17 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}]}, {"quantity_id": "q18", "topic": "NiCl2・6H2O", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[1].items[7]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 26,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "NiCl2・6H2O", "volume": 26, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001022", "gmo_id": "GMO_001022", "label": "Nickel chloride hexahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source trace-stock input is 26 mg; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "26", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 26 mg; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "26", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 26 mg; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}]}, {"quantity_id": "q19", "topic": "ZnCl2", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[1].items[8]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "ZnCl2", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001035", "gmo_id": "GMO_001035", "label": "Zinc chloride", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source trace-stock input is 0.1 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 0.1 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 0.1 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}]}, {"quantity_id": "q20", "topic": "Na2SeO3・5H2O", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[1].items[9]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"Na2SeO3・5H2O\",\n          \"volume\": 20,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001046\",\n          \"gmo_id\": \"GMO_001046\",\n          \"label\": \"Sodium selenite pentahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Na2SeO3・5H2O", "volume": 20, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001046", "gmo_id": "GMO_001046", "label": "Sodium selenite pentahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source trace-stock input is 20 mg; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "20", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 20 mg; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "20", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 20 mg; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}]}, {"quantity_id": "q21", "topic": "Nitrilotriacetic acid", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[1].items[10]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\": 12.8,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001053\",\n          \"gmo_id\": \"GMO_001053\",\n          \"label\": \"Nitrilotriacetic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Nitrilotriacetic acid", "volume": 12.8, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001053", "gmo_id": "GMO_001053", "label": "Nitrilotriacetic acid", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source trace-stock input is 12.8 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "12.8", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 12.8 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "12.8", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 12.8 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}]}, {"quantity_id": "q22", "topic": "CuCl2", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[1].items[11]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"CuCl2\",\n          \"volume\": 20,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001542\",\n          \"gmo_id\": \"GMO_001542\",\n          \"label\": \"Copper(II) chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "CuCl2", "volume": 20, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001542", "gmo_id": "GMO_001542", "label": "Copper(II) chloride", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source trace-stock input is 20 mg; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "20", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 20 mg; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "20", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 20 mg; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}]}, {"quantity_id": "q23", "topic": "FeCl2・4H2O", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[1].items[12]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"FeCl2・4H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\": \"GMO_001548\",\n          \"label\": \"Iron(II) chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "FeCl2・4H2O", "volume": 0.2, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001548", "gmo_id": "GMO_001548", "label": "Iron(II) chloride tetrahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source trace-stock input is 0.2 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 0.2 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input is 0.2 g; it is not a direct final-medium rate. Preserve stock stage and explicit unit, with water input distinguished from final volume. MediaDive stock g_l is only a provider-declared stock rate."}]}, {"quantity_id": "q24", "topic": "KOH", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[1].items[13]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"KOH\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\": \"GMO_001903\",\n          \"label\": \"Potassium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "KOH", "gmo": "http://purl.jp/bio/10/gmo/GMO_001903", "gmo_id": "GMO_001903", "label": "Potassium hydroxide solution", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051", "label": "Solution"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "not_quantified", "rationale": "No KOH dose is specified. VARIABLE is compatible with an unquantified adjustment reagent, but its parent placement must be changed to trace-stock preparation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "No KOH dose is specified. VARIABLE is compatible with an unquantified adjustment reagent, but its parent placement must be changed to trace-stock preparation."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "No KOH dose is specified. VARIABLE is compatible with an unquantified adjustment reagent, but its parent placement must be changed to trace-stock preparation."}]}, {"quantity_id": "q25", "topic": "Receiving stock addition 1", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[0].items[10]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"Trace element solution (see below)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M768\",\n          \"properties\": [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Trace element solution (see below)", "volume": 10, "unit": "ml", "reference_media_id": "M768", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source addition is 10 ml per listed receiving batch, not grams per liter; do not infer a final-volume denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "solutions[0].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source addition is 10 ml per listed receiving batch, not grams per liter; do not infer a final-volume denominator."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "solutions[0].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source addition is 10 ml per listed receiving batch, not grams per liter; do not infer a final-volume denominator."}]}, {"quantity_id": "q26", "topic": "Receiving stock addition 2", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.components[0].items[11]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n          \"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 5,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\": [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Trace vitamins (see Medium [M190])", "volume": 5, "unit": "ml", "reference_media_id": "M190", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "Source addition is 5 ml per listed receiving batch, not grams per liter; do not infer a final-volume denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "solutions[1].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source addition is 5 ml per listed receiving batch, not grams per liter; do not infer a final-volume denominator."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "solutions[1].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source addition is 5 ml per listed receiving batch, not grams per liter; do not infer a final-volume denominator."}]}, {"quantity_id": "q27", "topic": "M190 referenced vitamin: Distilled water", "source": {"evidence_id": "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[0]", "accessed_at": "2026-10-28T10:59:55.487110Z", "quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo": "http://purl.jp/bio/10/gmo/GMO_001001", "gmo_id": "GMO_001001", "label": "Distilled water", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044", "label": "Solvating media"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "verified", "rationale": "Existing 1 L water is verified as stock-batch input only, not measured final volume.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[0].concentration", "stored_value": {"value": "1", "unit": "L"}, "decision": "verified", "rationale": "Existing 1 L water is verified as stock-batch input only, not measured final volume."}]}, {"quantity_id": "q28", "topic": "M190 referenced vitamin: Biotin", "source": {"evidence_id": "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[1]", "accessed_at": "2026-10-28T10:59:55.487110Z", "quote": "{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Biotin", "volume": 2, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001025", "gmo_id": "GMO_001025", "label": "Biotin", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "verified", "rationale": "Existing note correctly retains 2 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[1].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "Existing note correctly retains 2 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q29", "topic": "M190 referenced vitamin: p--Aminobenzoic acid", "source": {"evidence_id": "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[2]", "accessed_at": "2026-10-28T10:59:55.487110Z", "quote": "{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "p--Aminobenzoic acid", "volume": 5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001026", "gmo_id": "GMO_001026", "label": "4-Aminobenzoic acid", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "verified", "rationale": "Existing note correctly retains 5 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[2].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "Existing note correctly retains 5 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q30", "topic": "M190 referenced vitamin: Thiamine・HCl", "source": {"evidence_id": "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[3]", "accessed_at": "2026-10-28T10:59:55.487110Z", "quote": "{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Thiamine・HCl", "volume": 5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001027", "gmo_id": "GMO_001027", "label": "Thiamine hydrochloride", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "verified", "rationale": "Existing note correctly retains 5 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[3].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "Existing note correctly retains 5 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q31", "topic": "M190 referenced vitamin: Calcium pantothenate", "source": {"evidence_id": "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[4]", "accessed_at": "2026-10-28T10:59:55.487110Z", "quote": "{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\": \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Calcium pantothenate", "volume": 5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001028", "gmo_id": "GMO_001028", "label": "Calcium pantothenate", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "verified", "rationale": "Existing note correctly retains 5 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[4].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "Existing note correctly retains 5 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q32", "topic": "M190 referenced vitamin: Pyridoxine・HCl", "source": {"evidence_id": "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[5]", "accessed_at": "2026-10-28T10:59:55.487110Z", "quote": "{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Pyridoxine・HCl", "volume": 10, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001029", "gmo_id": "GMO_001029", "label": "Pyridoxine hydrochloride", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "verified", "rationale": "Existing note correctly retains 10 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[5].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "Existing note correctly retains 10 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q33", "topic": "M190 referenced vitamin: Folic acid", "source": {"evidence_id": "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[6]", "accessed_at": "2026-10-28T10:59:55.487110Z", "quote": "{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Folic acid", "volume": 2, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001033", "gmo_id": "GMO_001033", "label": "Folic acid", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "verified", "rationale": "Existing note correctly retains 2 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[6].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "Existing note correctly retains 2 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q34", "topic": "M190 referenced vitamin: Vitamin B12", "source": {"evidence_id": "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[7]", "accessed_at": "2026-10-28T10:59:55.487110Z", "quote": "{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Vitamin B12", "volume": 0.1, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001034", "gmo_id": "GMO_001034", "label": "Cobalamin", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "verified", "rationale": "Existing note correctly retains 0.1 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[7].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "Existing note correctly retains 0.1 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q35", "topic": "M190 referenced vitamin: Riboflavin", "source": {"evidence_id": "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[8]", "accessed_at": "2026-10-28T10:59:55.487110Z", "quote": "{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Riboflavin", "volume": 5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001037", "gmo_id": "GMO_001037", "label": "Riboflavin", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "verified", "rationale": "Existing note correctly retains 5 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[8].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "Existing note correctly retains 5 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q36", "topic": "M190 referenced vitamin: Nicotinic acid", "source": {"evidence_id": "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[9]", "accessed_at": "2026-10-28T10:59:55.487110Z", "quote": "{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Nicotinic acid", "volume": 5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001038", "gmo_id": "GMO_001038", "label": "Nicotinic acid", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "verified", "rationale": "Existing note correctly retains 5 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[9].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "Existing note correctly retains 5 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q37", "topic": "M190 referenced vitamin: Lipoic acid", "source": {"evidence_id": "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[10]", "accessed_at": "2026-10-28T10:59:55.487110Z", "quote": "{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\": \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Lipoic acid", "volume": 5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001699", "gmo_id": "GMO_001699", "label": "Lipoic acid", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000067", "uri": "http://purl.jp/bio/10/gmo/GMO_000067", "label": "Growth factor"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "verified", "rationale": "Existing note correctly retains 5 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[10].notes", "stored_value": "Role: Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "Existing note correctly retains 5 mg batch mass and withdraws unsupported final concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q38", "topic": "Missing source preparation 1", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.comments[0]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Adjust pH to 6.0 -- 6.5.\"\n    }", "exact_decoded_object": {"paragraph_index": 2, "comment": "Adjust pH to 6.0 -- 6.5."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "evidence_only", "rationale": "Main preparation states pH 6.0–6.5; TOGO meta.ph 7.0 and API medium.min_pH/max_pH 6.5 are scoped conflicting metadata, not reasons to discard the explicit step.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "evidence_only", "rationale": "Main preparation states pH 6.0–6.5; TOGO meta.ph 7.0 and API medium.min_pH/max_pH 6.5 are scoped conflicting metadata, not reasons to discard the explicit step.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "evidence_only", "rationale": "Main preparation states pH 6.0–6.5; TOGO meta.ph 7.0 and API medium.min_pH/max_pH 6.5 are scoped conflicting metadata, not reasons to discard the explicit step.", "missing": true}]}, {"quantity_id": "q39", "topic": "Missing source preparation 2", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.comments[1]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n      \"paragraph_index\": 3,\n      \"comment\": \"Prepare sodium sulfide separately as 5% (w/v) solution, autoclave under a nitrogen atmosphere and neutralize with 1 N HCl before use. Sterilize glucose separately.\"\n    }", "exact_decoded_object": {"paragraph_index": 3, "comment": "Prepare sodium sulfide separately as 5% (w/v) solution, autoclave under a nitrogen atmosphere and neutralize with 1 N HCl before use. Sterilize glucose separately."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "evidence_only", "rationale": "Separate sulfide 5% w/v stock, nitrogen autoclave, 1 N HCl neutralization and separate glucose sterilization are absent locally. These specify preparation, not stock volume or incubation conditions.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "evidence_only", "rationale": "Separate sulfide 5% w/v stock, nitrogen autoclave, 1 N HCl neutralization and separate glucose sterilization are absent locally. These specify preparation, not stock volume or incubation conditions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "evidence_only", "rationale": "Separate sulfide 5% w/v stock, nitrogen autoclave, 1 N HCl neutralization and separate glucose sterilization are absent locally. These specify preparation, not stock volume or incubation conditions.", "missing": true}]}, {"quantity_id": "q40", "topic": "Missing source preparation 3", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.comments[2]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n      \"paragraph_index\": 5,\n      \"comment\": \"First, dissolve nitrilotriacetic acid and adjust to pH 6.5 with KOH.\"\n    }", "exact_decoded_object": {"paragraph_index": 5, "comment": "First, dissolve nitrilotriacetic acid and adjust to pH 6.5 with KOH."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "evidence_only", "rationale": "Trace-stock NTA dissolution and pH 6.5 KOH adjustment are separate from main-medium pH.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "evidence_only", "rationale": "Trace-stock NTA dissolution and pH 6.5 KOH adjustment are separate from main-medium pH.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "evidence_only", "rationale": "Trace-stock NTA dissolution and pH 6.5 KOH adjustment are separate from main-medium pH.", "missing": true}]}, {"quantity_id": "q41", "topic": "Conflicting source pH metadata", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528", "locator": "$.meta", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n    \"gm\": \"http://togomedium.org/medium/M768\",\n    \"name\": \"Clostridium Thermosulfurogenes Medium\",\n    \"original_media_id\": \"JCM_M743\",\n    \"src_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=743\",\n    \"ph\": \"7.0\"\n  }", "exact_decoded_object": {"gm": "http://togomedium.org/medium/M768", "name": "Clostridium Thermosulfurogenes Medium", "original_media_id": "JCM_M743", "src_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=743", "ph": "7.0"}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "conflict", "rationale": "TOGO meta.ph 7.0 disagrees with its comments[0] range6.0–6.5. API medium.min_pH/max_pH 6.5 is a scalar within the range. No current local pH is asserted. Preserve each source locus and favor no invented reconciliation.", "layer_assessments": [], "corroboration": [{"evidence_id": "apiJ743", "reference": "https://mediadive.dsmz.de/rest/medium/J743", "raw_path": "REVIEW_WORK/batch064/source01/apiJ743.bin", "raw_sha256": "f32986f3cb333c4fdba212746030a76076f39ac33090109ad3e4727f34a14b8a", "locator": "$.data.medium", "accessed_at": "2026-10-28T10:59:54.900568Z", "quote": "{\n            \"id\": \"J743\",\n            \"name\": \"CLOSTRIDIUM THERMOSULFUROGENES MEDIUM\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\": 6.5,\n            \"max_pH\": 6.5,\n            \"source\": \"JCM\",\n            \"link\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=743\"\n        }", "exact_decoded_object": {"id": "J743", "name": "CLOSTRIDIUM THERMOSULFUROGENES MEDIUM", "complex_medium": "yes", "min_pH": 6.5, "max_pH": 6.5, "source": "JCM", "link": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=743"}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}]}]

### Current ontology and MIM correspondence

grounding: concern. Targets: CultureMech:010175.

All current target/owner and scoped vitamin identifier slots are inventoried; ingredient ontology terms are checked against fresh OLS and the packaged MIM catalog. Three source-explicit hydrates map to anhydrous forms. Generic calcium pantothenate source text does not establish the D-specific structure in CHEBI:31345; specificity remains unresolved, not an assertion of the opposite enantiomer. Catalog presence and labels do not authenticate source chemical form.

### History and evidence scope

provenance: concern. Targets: CultureMech:010175.

Complete selected target and owner histories, references and all eleven vitamin claims were read. Four exact historical reports are mechanical source-incomplete context; the current dependency repair is credited. Matching old/current TOGO190 and JCM197 raw hashes authenticate bytes, not historical access events. Existing history remains append-only.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:010175.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:010175.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Stock stages and source units are conflated

major / open / confirmed; issue key: culturemech-010175-stock-stages-and-source-units-are-conflated.

Main and trace-stock water inputs were combined; the generated record retains 2.0 G_PER_L while the maintained owner reduced it to 1.0 G_PER_L. Both remain wrong as stage-specific water quantities. Resazurin and ferrous sulfate use source mg as g/L; trace-stock contents are direct ingredients, with several mg values likewise read as g/L. Both receiving stock doses use G_PER_L although source additions are volumes. Main g values remain batch inputs without an independently established final volume. Correct the maintained representation with exact source units and nested stages, preserving the owner repair as historical context.

### f2: Referenced stock compositions remain unresolved

major / open / confirmed; issue key: culturemech-010175-referenced-stock-compositions-remain-unresolved.

Trace element contents belong inside solutions[0], whose composition is empty. The vitamin stub refers to M190 as a whole; only its repaired solutions[1].composition is the relevant dependency. Retain the 11 supported vitamin claims and target-specific addition; do not import M190 receiving dose or parent conditions. Give each stock its source name and a scoped, resolvable reference or inline composition.

### f3: Hydrate identities do not match explicit source forms

major / open / confirmed; issue key: culturemech-010175-hydrate-identities-do-not-match-explicit-source-forms.

Na2HPO4·12H2O is mapped to CHEBI:34683 whose formula lacks twelve waters; CoCl2·6H2O and NiCl2·6H2O map to anhydrous CHEBI:35696 and CHEBI:34887. Fresh OLS CHEBI:53503/CHEBI:53542 confirm cobalt/nickel hexahydrate candidates. Verify a source-exact sodium phosphate hydrate before proposing its identifier. Neutral Resazurin is not a sodium salt assertion. Preserve explicit hydrate mass basis.

### f4: Preparation boundaries and pH evidence are missing

major / open / confirmed; issue key: culturemech-010175-preparation-boundaries-and-ph-evidence-are-missing.

Source comments specify separate sulfide preparation/neutralization and glucose sterilization, main pH range and separate trace-stock adjustment. Current target and owner omit preparation_steps. Preserve stock strength versus receiving contribution and main versus stock pH; keep TOGO scalar pH conflict explicit. Do not invent stock volume, incubation atmosphere, temperature or sterilization time.

### f5: Source claims lack field-level evidence

minor / open / confirmed; issue key: culturemech-010175-source-claims-lack-field-level-evidence.

The selected target and owner retain source URLs but no attached quantity/preparation evidence. Add narrowly scoped evidence for each repaired claim, retain unavailable JCM743 status and append history rather than rewriting earlier events. M190 vitamin evidence already exists and is verified separately.

## Recommended Actions And Acceptance Checks

### action1

Main and trace-stock water inputs were combined; the generated record retains 2.0 G_PER_L while the maintained owner reduced it to 1.0 G_PER_L. Both remain wrong as stage-specific water quantities. Resazurin and ferrous sulfate use source mg as g/L; trace-stock contents are direct ingredients, with several mg values likewise read as g/L. Both receiving stock doses use G_PER_L although source additions are volumes. Main g values remain batch inputs without an independently established final volume. Correct the maintained representation with exact source units and nested stages, preserving the owner repair as historical context.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Trace element contents belong inside solutions[0], whose composition is empty. The vitamin stub refers to M190 as a whole; only its repaired solutions[1].composition is the relevant dependency. Retain the 11 supported vitamin claims and target-specific addition; do not import M190 receiving dose or parent conditions. Give each stock its source name and a scoped, resolvable reference or inline composition.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Na2HPO4·12H2O is mapped to CHEBI:34683 whose formula lacks twelve waters; CoCl2·6H2O and NiCl2·6H2O map to anhydrous CHEBI:35696 and CHEBI:34887. Fresh OLS CHEBI:53503/CHEBI:53542 confirm cobalt/nickel hexahydrate candidates. Verify a source-exact sodium phosphate hydrate before proposing its identifier. Neutral Resazurin is not a sodium salt assertion. Preserve explicit hydrate mass basis.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Source comments specify separate sulfide preparation/neutralization and glucose sterilization, main pH range and separate trace-stock adjustment. Current target and owner omit preparation_steps. Preserve stock strength versus receiving contribution and main versus stock pH; keep TOGO scalar pH conflict explicit. Do not invent stock volume, incubation atmosphere, temperature or sterilization time.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action5

The selected target and owner retain source URLs but no attached quantity/preparation evidence. Add narrowly scoped evidence for each repaired claim, retain unavailable JCM743 status and append history rather than rewriting earlier events. M190 vitamin evidence already exists and is verified separately.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch064/record01/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| dependency-vitamin | data/normalized_yaml/bacterial/togo_medium_m190.yaml; solutions[1].composition; media_term; notes; references; curation_history | context_only | Only solutions[1].composition, source identity, references and complete append-only history inspected. Other parent ingredients, stocks, receiving dose and preparation are excluded from target evidence. |
| jcm743 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=743; Exact source identity and scoped formulation/preparation | context_only | Exact JCM743 endpoint returned HTTP 200 with Nothing found; no primary formulation text was available at this endpoint. |
| togo768 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768; Exact source identity and scoped formulation/preparation | supports | Full exact TOGO M768 metadata, main and trace stock components and comments read. M768 identifies JCM743. Main/stock pH and material stages remain distinct. |
| apiJ743 | https://mediadive.dsmz.de/rest/medium/J743; Exact source identity and scoped formulation/preparation | supports | Full exact MediaDive J743 medium metadata, all three solutions, recipes and steps read. Provider g_l and nominal volume are distinct from measured final volume. |
| jcm197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Exact source identity and scoped formulation/preparation | supports | JCM197 source identity and Trace vitamins section read; only the referenced vitamin stock is used, not parent cultivation instructions or dose. |
| togo190 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; Exact source identity and scoped formulation/preparation | supports | Only source metadata and components[1] Trace vitamins are scientific evidence here. The full raw hash matches the historical attached capture; this authenticates bytes, not the old access event. |
| apiJ197 | https://mediadive.dsmz.de/rest/medium/J197; Exact source identity and scoped formulation/preparation | supports | Only medium source identity and data.solutions[1] Trace vitamins (id3861) read for scientific corroboration; parent formulation, conditions and dose excluded. |
| dependency-provenance | REVIEW_WORK/batch064/record01/dependency-provenance.json | context_only | Complete dependency identity/references/history read; only vitamin composition is assessed as target scientific evidence. No parent receiving dose or unrelated stock is transferred. |
| attached-evidence-joins | REVIEW_WORK/batch064/record01/attached-evidence-joins.json | supports | All eleven existing vitamin-stock snippets match fresh raw TOGO190 bytes and exact source item locators; historical full raw digest also matches. Historical access events are not reauthenticated. |
| historical-1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md; Complete document | context_only | Complete report text read, with exact generated-counterpart differences checked. Historical source-incomplete mechanical inventory with zero source-checked claims; no scientific conclusion imported. Current October8 dependency repair postdates it. |
| historical-2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.md; Complete document | context_only | Complete report text read, with exact generated-counterpart differences checked. Historical source-incomplete mechanical inventory with zero source-checked claims; no scientific conclusion imported. Current October8 dependency repair postdates it. |
| historical-3 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.md; Complete document | context_only | Complete report text read, with exact generated-counterpart differences checked. Historical source-incomplete mechanical inventory with zero source-checked claims; no scientific conclusion imported. Current October8 dependency repair postdates it. |
| historical-4 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md; Complete document | context_only | Complete report text read, with exact generated-counterpart differences checked. Historical source-incomplete mechanical inventory with zero source-checked claims; no scientific conclusion imported. Current October8 dependency repair postdates it. |
| writer-togo | src/culturemech/import/togo_importer.py; _ingredient_from_item; _extract_primary_components; _local_batch_volume_ml; _solution_from_item; _extract_preparation_steps; _parse_unit; _extract_ph; _convert_to_culturemech | context_only | Current primary extraction separates local stock sections and fixes mg/ml/L mappings. A 10 ml addition does not establish the 1 L local stock final basis, so the local composition remains empty under the guarded path. All comments still become root preparation_steps; _extract_ph reads top-level ph rather than meta.ph. These improvements do not repair stored data or certify inferred final-volume denominators. |
| writer-migrate | scripts/migrate_solutions_from_ingredients.py; _extract_medium_reference; _resolve_solution | context_only | Cross-reference M190 returns an empty composition and preserves old concentration; the reference names a parent medium, not a resolved vitamin composition. Numeric receiving doses must remain target-specific. |
| writer-cleanup | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current same-unit identical duplicates collapse to the first value; unequal values retain first with warning. It does not restore preparation stages or source units and does not prove historical summation execution. |
| writer-repair | scripts/repair_merged_duplicates.py; repair_ingredient; repair_record | context_only | Current repair changes duplicate-derived numeric value and note, recursively. The owner has this later repair; neither this operation nor its history establishes that separate source stages were duplicates. |
| writer-jcm-stock | scripts/repair_jcm_stock_preparations.py; Review.leaf; Review.stock; Review.fill; Review.stages; build; process | context_only | Scoped JCM/TOGO repair stores water and stock volumes in L, retains TOGO masses in notes where final volume is unknown, and qualifies provider stock rates. M190 vitamin repair is retained. No rerun is requested; its fixed source context and shared guard are outside any new execution authorization. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Single-source merge copies the contributor and adds merge metadata; regenerate after owner curation rather than hand-editing generated target. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current multi-source compatibility preserves substantive formulation fields, not just ingredient fingerprints. It does no stock expansion or source authentication. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503; Exact obo_id, preferred label and formula/InChI/SMILES | supports | Fresh OLS exact candidate confirms a hexahydrate chemical identity; candidate is not installed in any recipe. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53542; Exact obo_id, preferred label and formula/InChI/SMILES | supports | Fresh OLS exact candidate confirms a hexahydrate chemical identity; candidate is not installed in any recipe. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15377; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63036; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86345; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76209; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34683; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17234; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17883; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86368; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_35696; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49976; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131361; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_44557; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi49553 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49553; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
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
| quantities | REVIEW_WORK/batch064/record01/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch064/record01/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch064/record01/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch064/record01/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch064/record01/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch064/record01/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch064/record01/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch064/record01/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch064/record01/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- Exact JCM743 endpoint returned HTTP 200 with Nothing found. Source-dependent findings use inspected TOGO M768 and MediaDive J743; primary verification of the full selected formulation remains unavailable.
- M190 scientific dependency scope is only solutions[1].composition and exact corresponding source vitamin tables. Parent dose, parent recipe, other stocks and parent growth/preparation conditions are excluded.
- No independently established final volume is inferred from water input or provider nominal volume. MediaDive g_l values remain provider declarations, not measured concentrations.
- Generic calcium pantothenate does not resolve stereochemical specificity. No exact sodium phosphate dodecahydrate replacement identifier is proposed in this review.
- No strain-level growth evidence or taxonomic assertion is inferred from a medium name or general application. iModulonDB is not applicable to this medium identity review.
- Canonical reference validation ran zero reference checks. History/provenance and source reference resolution were assessed separately; whole-corpus product, ID and merge gates were not rerun for an unchanged-recipe review.
- Current writer code does not authenticate historical execution. No record, generated product, scientific status or curation history was modified.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T110852Z-batch064-record01-source-review
kind: record
repository: CultureBotAI/CultureMech
title: Source and stage review of Clostridium thermosulfurogenes medium
started_at: '2026-10-28T10:58:48.916559Z'
finished_at: '2026-10-28T11:08:52.785113Z'
reviewer:
  identity: Codex independent source reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh assessment of the inspected checkout and newly captured
    primary/provider/ontology evidence; no reconstruction of lost reviews and no record
    edits.
skill: .claude/skills/review-yaml-record/SKILL.md; .claude/skills/review-ingredient-concentrations/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The sole TOGO M768 contributor resolves to JCM743. All canonical diagnostics
  pass, but trace-stock contents are flattened, mass/volume units are conflated, stock
  stubs and preparation are incomplete, and three hydrate identities are mismatched.
  The later owner water repair is credited separately from the stale generated record.
  JCM743 currently returns Nothing found; usable TOGO/MediaDive evidence supports
  a partial review.
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
  - path: data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml
    sha256: 70861ff226ab358702a1d1eb513e7416b01bfd96046a41e0834cee98c70da9ea
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml
    sha256: 9ce05e87f7bb24ebd8f79ffbeeec8455d4a90b6eab39833a587f5079d36558c8
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.md
    sha256: 21893d9ba45732604e050205cacca9fbbfba3f952d5a031fc944dd1998e6b3bb
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md
    sha256: 4ee172b59b8f9a19921c300ecf394dc632e301c0f375a6e86adfade6ec86a619
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.md
    sha256: 4aaa265ccaa154e3cb7447b19402ef9fdad51e7eb57d8a18ec858a4339eb4d01
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
    sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
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
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
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
  - path: scripts/repair_jcm_stock_preparations.py
    sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
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
  selection: Actual batch064 native selection index 01.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010175
targets:
- target_id: CultureMech:010175
  path: data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml
  label: clostridium_thermosulfurogenes_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:010175
  command: just validate-schema data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml
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
  - CultureMech:010175
  command: just validate-strict data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml
    --out REVIEW_WORK/batch064/record01/strict.tsv --workers 1
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
  - CultureMech:010175
  command: just validate-terms data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml
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
  - CultureMech:010175
  command: just validate-references data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T11:07:47.516340Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 70861ff226ab358702a1d1eb513e7416b01bfd96046a41e0834cee98c70da9ea
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T11:07:47.516340Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 9ce05e87f7bb24ebd8f79ffbeeec8455d4a90b6eab39833a587f5079d36558c8
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch064/record01/identity-search.json
  accessed_at: '2026-10-28T11:07:47.567488Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    excluded namesakes are retained in the census. Similar names and source accessions
    are not promoted to owners.
  snapshot_sha256: e8aee3c3c33e74f3aa60c1a0f643a619149f57fdc5adaa172990a301e6b13ae6
- evidence_id: dependency-vitamin
  kind: record_content
  reference: data/normalized_yaml/bacterial/togo_medium_m190.yaml
  locator: solutions[1].composition; media_term; notes; references; curation_history
  accessed_at: '2026-10-28T11:07:47.516340Z'
  support: context_only
  summary: Only solutions[1].composition, source identity, references and complete
    append-only history inspected. Other parent ingredients, stocks, receiving dose
    and preparation are excluded from target evidence.
  snapshot_sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
- evidence_id: jcm743
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=743
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:59:54.801822Z'
  support: context_only
  summary: Exact JCM743 endpoint returned HTTP 200 with Nothing found; no primary
    formulation text was available at this endpoint.
  snapshot_sha256: b03545e995c8f93ec2a6ea5460506294c910dfbe9912e3e5a3028bde5e834782
- evidence_id: togo768
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:59:54.946565Z'
  support: supports
  summary: Full exact TOGO M768 metadata, main and trace stock components and comments
    read. M768 identifies JCM743. Main/stock pH and material stages remain distinct.
  snapshot_sha256: 38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528
- evidence_id: apiJ743
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J743
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:59:54.900568Z'
  support: supports
  summary: Full exact MediaDive J743 medium metadata, all three solutions, recipes
    and steps read. Provider g_l and nominal volume are distinct from measured final
    volume.
  snapshot_sha256: f32986f3cb333c4fdba212746030a76076f39ac33090109ad3e4727f34a14b8a
- evidence_id: jcm197
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:59:54.793901Z'
  support: supports
  summary: JCM197 source identity and Trace vitamins section read; only the referenced
    vitamin stock is used, not parent cultivation instructions or dose.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: togo190
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:59:55.487110Z'
  support: supports
  summary: Only source metadata and components[1] Trace vitamins are scientific evidence
    here. The full raw hash matches the historical attached capture; this authenticates
    bytes, not the old access event.
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: apiJ197
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J197
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:59:55.329448Z'
  support: supports
  summary: Only medium source identity and data.solutions[1] Trace vitamins (id3861)
    read for scientific corroboration; parent formulation, conditions and dose excluded.
  snapshot_sha256: 779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb
- evidence_id: dependency-provenance
  kind: record_content
  reference: REVIEW_WORK/batch064/record01/dependency-provenance.json
  accessed_at: '2026-10-28T11:07:47.609226Z'
  support: context_only
  summary: Complete dependency identity/references/history read; only vitamin composition
    is assessed as target scientific evidence. No parent receiving dose or unrelated
    stock is transferred.
  snapshot_sha256: ec36b916dbc47cdf9ac8d55d7af026a6b70fb29694d2d74e8dac727b38dcc9c1
- evidence_id: attached-evidence-joins
  kind: record_content
  reference: REVIEW_WORK/batch064/record01/attached-evidence-joins.json
  accessed_at: '2026-10-28T11:07:47.609372Z'
  support: supports
  summary: All eleven existing vitamin-stock snippets match fresh raw TOGO190 bytes
    and exact source item locators; historical full raw digest also matches. Historical
    access events are not reauthenticated.
  snapshot_sha256: c0500686a6886e3f71884af0203d4b4d24ffd2892162703a98267bc3f23f266d
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
  locator: Complete document
  accessed_at: '2026-10-28T11:07:47.516340Z'
  support: context_only
  summary: Complete report text read, with exact generated-counterpart differences
    checked. Historical source-incomplete mechanical inventory with zero source-checked
    claims; no scientific conclusion imported. Current October8 dependency repair
    postdates it.
  snapshot_sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.md
  locator: Complete document
  accessed_at: '2026-10-28T11:07:47.516340Z'
  support: context_only
  summary: Complete report text read, with exact generated-counterpart differences
    checked. Historical source-incomplete mechanical inventory with zero source-checked
    claims; no scientific conclusion imported. Current October8 dependency repair
    postdates it.
  snapshot_sha256: 4aaa265ccaa154e3cb7447b19402ef9fdad51e7eb57d8a18ec858a4339eb4d01
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.md
  locator: Complete document
  accessed_at: '2026-10-28T11:07:47.516340Z'
  support: context_only
  summary: Complete report text read, with exact generated-counterpart differences
    checked. Historical source-incomplete mechanical inventory with zero source-checked
    claims; no scientific conclusion imported. Current October8 dependency repair
    postdates it.
  snapshot_sha256: 21893d9ba45732604e050205cacca9fbbfba3f952d5a031fc944dd1998e6b3bb
- evidence_id: historical-4
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md
  locator: Complete document
  accessed_at: '2026-10-28T11:07:47.516340Z'
  support: context_only
  summary: Complete report text read, with exact generated-counterpart differences
    checked. Historical source-incomplete mechanical inventory with zero source-checked
    claims; no scientific conclusion imported. Current October8 dependency repair
    postdates it.
  snapshot_sha256: 4ee172b59b8f9a19921c300ecf394dc632e301c0f375a6e86adfade6ec86a619
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item; _extract_primary_components; _local_batch_volume_ml;
    _solution_from_item; _extract_preparation_steps; _parse_unit; _extract_ph; _convert_to_culturemech
  accessed_at: '2026-10-28T11:07:47.516340Z'
  support: context_only
  summary: Current primary extraction separates local stock sections and fixes mg/ml/L
    mappings. A 10 ml addition does not establish the 1 L local stock final basis,
    so the local composition remains empty under the guarded path. All comments still
    become root preparation_steps; _extract_ph reads top-level ph rather than meta.ph.
    These improvements do not repair stored data or certify inferred final-volume
    denominators.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-migrate
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: _extract_medium_reference; _resolve_solution
  accessed_at: '2026-10-28T11:07:47.516340Z'
  support: context_only
  summary: Cross-reference M190 returns an empty composition and preserves old concentration;
    the reference names a parent medium, not a resolved vitamin composition. Numeric
    receiving doses must remain target-specific.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T11:07:47.516340Z'
  support: context_only
  summary: Current same-unit identical duplicates collapse to the first value; unequal
    values retain first with warning. It does not restore preparation stages or source
    units and does not prove historical summation execution.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-repair
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_ingredient; repair_record
  accessed_at: '2026-10-28T11:07:47.516340Z'
  support: context_only
  summary: Current repair changes duplicate-derived numeric value and note, recursively.
    The owner has this later repair; neither this operation nor its history establishes
    that separate source stages were duplicates.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer-jcm-stock
  kind: record_content
  reference: scripts/repair_jcm_stock_preparations.py
  locator: Review.leaf; Review.stock; Review.fill; Review.stages; build; process
  accessed_at: '2026-10-28T11:07:47.516340Z'
  support: context_only
  summary: Scoped JCM/TOGO repair stores water and stock volumes in L, retains TOGO
    masses in notes where final volume is unknown, and qualifies provider stock rates.
    M190 vitamin repair is retained. No rerun is requested; its fixed source context
    and shared guard are outside any new execution authorization.
  snapshot_sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T11:07:47.516340Z'
  support: context_only
  summary: Single-source merge copies the contributor and adds merge metadata; regenerate
    after owner curation rather than hand-editing generated target.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T11:07:47.516340Z'
  support: context_only
  summary: Current multi-source compatibility preserves substantive formulation fields,
    not just ingredient fingerprints. It does no stock expansion or source authentication.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503
  locator: Exact obo_id, preferred label and formula/InChI/SMILES
  accessed_at: '2026-10-28T10:59:59.297579Z'
  support: supports
  summary: Fresh OLS exact candidate confirms a hexahydrate chemical identity; candidate
    is not installed in any recipe.
  snapshot_sha256: 31dc996638b0cc1341ed24fcb38ec344af726c99d376ac94e952210fcb9ed583
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53542
  locator: Exact obo_id, preferred label and formula/InChI/SMILES
  accessed_at: '2026-10-28T10:59:59.577083Z'
  support: supports
  summary: Fresh OLS exact candidate confirms a hexahydrate chemical identity; candidate
    is not installed in any recipe.
  snapshot_sha256: 1e444345efd33c02d5050deadd66637cc6dae004c55e6962c62abd172291e526
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15377
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:55.638114Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 42561686e12ba0831d99216248ea8c0b3338b461b0b77dd988f3096ad8678e59
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63036
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:59.814062Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 913baf38abc38dd61f05c5d636fd6532b70a668673a1f5762f290d2b67270164
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:57.640656Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: c70055293606f21dcdfb72325a4677661b51efb723ba9357efab43f8ec9b03f7
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:00:01.038033Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: ceb05e9dd7fba3802d28b34c50bbb604ded87951e4ea3a812739824a84648d72
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:00:00.539370Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 015a33a158257cc5cba8a8e62de382053399be060366af5d95074883bb22b86e
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76209
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:00:00.174115Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 3eece7d96d2433ff020ece90db55323d138c5c828b78198f91d26b3eafa91f9f
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:59.911294Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: e12b865122aab78645385260e1e83ff28f3c45365cb67c9181166628f68974b3
- evidence_id: chebi34683
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34683
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:58.247113Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b8fc153769cf791f5e08680678fe7df66be98486bbfbb734518f3de625596efe
- evidence_id: chebi17234
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17234
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:56.669213Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2d78d31a7829da999c31ae102da842c5b5c37a5d334be6389539d92ecd786de7
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17883
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:56.826228Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 5f7b2f292559b9033f3c62c8403ed552842a28535010d6af5daa018a0977c28d
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:57.035728Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b145f4ff9b90ebb993ff576d9ab35a6c10b7c42a3b99e18feffcc8d75c0e1e50
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:00:00.443771Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: df8f702eb5b9d3e50209bfa2b0c4b6f1db30c116e56a58e348cbd4bf3bc0ebc1
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:59.880121Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0271a149a298ff837ad8f690ce8cb0acf111f5d25c5efaf6fa828401ab951d56
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:58.051077Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f23e1405347fa9d8a0826d4dd1279b7cdec8361390d20e439154dcbbd386a2d4
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86368
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:00:00.885708Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2bb4588e6734285b5536bdac78701f9800fdb8d17236d12cf5a1c30490f1614d
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_35696
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:58.641048Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b0671d570f256f8479ecacea745d00f94a953ac336192c6b41bd8a6dcd527e57
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:58.585041Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a43b8268f70ae50c4cfbc53e12bbd195618c521619cfab8f71d3704b338af95b
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49976
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:59.242106Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2d2305ca671adbbd3b0cc07b2331373a768bb44d41f32f61ba894594ae470eff
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131361
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:55.508091Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 345cb9c46670b2812cacd12098169f03ea94fe064710e06a7aa545a2717706b0
- evidence_id: chebi44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_44557
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:58.704892Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 371aa3b809db6c5d1ec8f8b8be40011e6b1132b1c0be40e70fb927788728d65a
- evidence_id: chebi49553
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49553
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:59.207799Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: fb38cbec0d8e8f422fbf3992bc1076af9213b2fec1cd371223b249795e9d7d07
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86249
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T11:00:00.475876Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 69797bf2582679b3f621fa4f982077ed90f48f3a5e1293c7444a3aaacbb25ba2
- evidence_id: chebi32035
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32035
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:58.022465Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: beb9265e17aebd20539ab8a464558e2820b9155c520635a44f77fa3e48f51ad4
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15956
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:56.211253Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0d2e75e0bd98dbffff14d85a41dfd0af8aae2a8d65a945d34a4126a17091c2b8
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30753
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:57.413713Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 42ea4022bd68e8fa28962bc496ca757174da7bbd18ce06b7f3d521885609a50c
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49105
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:58.890865Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: fc6b8e9d8657914ed8fd568c69d8a5b2cf41b26767bd6361a5e2d258883be97d
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:57.921744Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: d2a04309eb6976fd395f9684ec4c3f5192362e2b6b75464b0af128a28e188d25
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30961
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:57.436762Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 491af523ba70d13857fcb828561d0556e46382fa0591011a06693d7db24ad91f
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_27470
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:57.323036Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: dcee85bb585d3a73341ab66eff772dc6361330b3c899c4daecbda49d5e84e590
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_176843
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:56.759649Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 5c42e2236866d0314bc8d45947ddf9eb2fdf6364d08e802b0fb271011cbfe563
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17015
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:56.410147Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f8bec809c7ba5a36faea58b8fe1b5110f0d75dbd4ac1929a121cd352bce63309
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15940
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:56.070348Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2890ef915cd546e70c1e638af285a3cc19b8299ae7722d00b43a40170a57ab8a
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16494
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:59:56.133111Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: db6824ffab0d71efc11d1e64b505ae583949e9d5837086a4b0e7b364b2933a22
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch064/record01/quantity-inventory.json
  accessed_at: '2026-10-28T11:07:47.635049Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: b59e1748b9c4c77370230488d141fce45e3b01ab0343bf89684c596052a9e4c6
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch064/record01/grounding-inventory.json
  accessed_at: '2026-10-28T11:07:47.635133Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: b06fb4fc135caab7626c128ac1ec6ec8df864d659daa6921e9a03ba1e3e58bdf
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch064/record01/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T11:07:47.635245Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: dca3e37c4998732b5e46e683c937b2a7be753777eb1c198ca40ac7d6e1f850fe
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch064/record01/scalar-census.json
  accessed_at: '2026-10-28T11:07:47.635274Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: b20fe6934accd92b268494d341ec108105d2585a56d1262c95315ca0cd651a23
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch064/record01/validate-schema.json
  accessed_at: '2026-10-28T10:58:49.931507Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: 12d7e049db6b388f5f9c3faf29b77ef3bdacb14d8a5f8bbdec41c2334ca12e44
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch064/record01/validate-strict.json
  accessed_at: '2026-10-28T10:58:50.854273Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch064/record01/strict.tsv\n"
  snapshot_sha256: 9af6a1e92ef314d0e4a821be1bd65cb08eb184108854a73d8de04732b13e5f91
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch064/record01/validate-terms.json
  accessed_at: '2026-10-28T10:58:51.864183Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: 231a92bff80e0908d0e0c638447f92b42cf052fec93e6cd6150f5b546d480ec4
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch064/record01/validate-references.json
  accessed_at: '2026-10-28T10:58:52.567572Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 719addf2d2fe3a5ce22661f62fab2d0c5c23e60010814edf4097c33b294c895f
assessments:
- assessment_id: a1
  area: identity
  topic: Exact record and lineage
  outcome: supported
  summary: Generated CM010175 has one exact owner TOGO M768, whose source metadata
    identifies JCM743. No nearby DSM211/KOMODO211 or similarly named branch is used
    as owner.
  target_ids:
  - CultureMech:010175
  evidence_ids:
  - local-target
  - owner-1
  - identity-search
  - togo768
  - apiJ743
- assessment_id: a2
  area: representation
  topic: Classification and source stages
  outcome: concern
  summary: Liquid complex/undefined classification is consistent with yeast extract
    and no agar in this exact source. Main and trace-stock ingredients are wrongly
    combined; source role notes are descriptive imported annotations, not independent
    mechanistic evidence.
  target_ids:
  - CultureMech:010175
  evidence_ids:
  - local-target
  - togo768
- assessment_id: a3
  area: evidence
  topic: Available primary and provider sources
  outcome: unknown
  summary: Exact JCM743 endpoint supplies Nothing found. Two provider representations
    independently expose the same source identity and stage graph, but cannot replace
    an unavailable direct primary formulation. JCM197 corroborates only the referenced
    vitamin stock.
  target_ids:
  - CultureMech:010175
  evidence_ids:
  - jcm743
  - togo768
  - apiJ743
  - jcm197
- assessment_id: a4
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:010175
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Distilled water", "source": {"evidence_id":
    "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[0].items[0]", "accessed_at": "2026-10-28T10:59:54.946565Z",
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
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "Main recipe and trace-stock recipe each list separate 1 L water
    inputs. Target 2.0 G_PER_L sums different stages; owner 1.0 G_PER_L removes a
    numerical duplicate but still conflates stages and uses a mass unit. Preserve
    separate water inputs without treating either as measured final volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "2.0",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Main recipe and trace-stock
    recipe each list separate 1 L water inputs. Target 2.0 G_PER_L sums different
    stages; owner 1.0 G_PER_L removes a numerical duplicate but still conflates stages
    and uses a mass unit. Preserve separate water inputs without treating either as
    measured final volume."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "1.0",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Main recipe and trace-stock
    recipe each list separate 1 L water inputs. Target 2.0 G_PER_L sums different
    stages; owner 1.0 G_PER_L removes a numerical duplicate but still conflates stages
    and uses a mass unit. Preserve separate water inputs without treating either as
    measured final volume."}], "corroboration": [{"evidence_id": "togo768", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path":
    "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[1].items[0]", "accessed_at": "2026-10-28T10:59:54.946565Z",
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
    decoded object independently equals exact JSON locator."}]}, {"quantity_id": "q2",
    "topic": "Yeast extract", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[0].items[1]", "accessed_at": "2026-10-28T10:59:54.946565Z",
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
    "rationale": "Source main-batch mass 1 g agrees numerically, but a water input
    of 1 L does not establish final volume. Current G_PER_L is not independently verified;
    MediaDive declares a different g_l using nominal volume 1015. Preserve the batch
    mass and qualify any provider rate separately.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path":
    "ingredients[1].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "Source main-batch mass 1 g agrees numerically,
    but a water input of 1 L does not establish final volume. Current G_PER_L is not
    independently verified; MediaDive declares a different g_l using nominal volume
    1015. Preserve the batch mass and qualify any provider rate separately."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 1
    g agrees numerically, but a water input of 1 L does not establish final volume.
    Current G_PER_L is not independently verified; MediaDive declares a different
    g_l using nominal volume 1015. Preserve the batch mass and qualify any provider
    rate separately."}]}, {"quantity_id": "q3", "topic": "KH2PO4", "source": {"evidence_id":
    "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[0].items[2]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"KH2PO4\",\n          \"volume\":
    0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\":
    \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "KH2PO4", "volume": 0.3, "unit": "g",
    "gmo": "http://purl.jp/bio/10/gmo/GMO_001006", "gmo_id": "GMO_001006", "label":
    "Potassium phosphate monobasic", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040",
    "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038",
    "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, "decision": "unsupported",
    "rationale": "Source main-batch mass 0.3 g agrees numerically, but a water input
    of 1 L does not establish final volume. Current G_PER_L is not independently verified;
    MediaDive declares a different g_l using nominal volume 1015. Preserve the batch
    mass and qualify any provider rate separately.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path":
    "ingredients[2].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "Source main-batch mass 0.3 g agrees numerically,
    but a water input of 1 L does not establish final volume. Current G_PER_L is not
    independently verified; MediaDive declares a different g_l using nominal volume
    1015. Preserve the batch mass and qualify any provider rate separately."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch
    mass 0.3 g agrees numerically, but a water input of 1 L does not establish final
    volume. Current G_PER_L is not independently verified; MediaDive declares a different
    g_l using nominal volume 1015. Preserve the batch mass and qualify any provider
    rate separately."}]}, {"quantity_id": "q4", "topic": "NH4Cl", "source": {"evidence_id":
    "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[0].items[3]", "accessed_at": "2026-10-28T10:59:54.946565Z",
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
    "rationale": "Source main-batch mass 1 g agrees numerically, but a water input
    of 1 L does not establish final volume. Current G_PER_L is not independently verified;
    MediaDive declares a different g_l using nominal volume 1015. Preserve the batch
    mass and qualify any provider rate separately.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path":
    "ingredients[3].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "Source main-batch mass 1 g agrees numerically,
    but a water input of 1 L does not establish final volume. Current G_PER_L is not
    independently verified; MediaDive declares a different g_l using nominal volume
    1015. Preserve the batch mass and qualify any provider rate separately."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 1
    g agrees numerically, but a water input of 1 L does not establish final volume.
    Current G_PER_L is not independently verified; MediaDive declares a different
    g_l using nominal volume 1015. Preserve the batch mass and qualify any provider
    rate separately."}]}, {"quantity_id": "q5", "topic": "Resazurin", "source": {"evidence_id":
    "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[0].items[4]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"Resazurin\",\n          \"volume\":
    1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\":
    \"GMO_001012\",\n          \"label\": \"Resazurin\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent
    redox indicator\"\n            }\n          ]\n        }", "exact_decoded_object":
    {"component_name": "Resazurin", "volume": 1, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001012",
    "gmo_id": "GMO_001012", "label": "Resazurin", "properties": [{"id": "GMO_000041",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id":
    "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined
    component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000055", "uri": "http://purl.jp/bio/10/gmo/GMO_000055",
    "label": "pH dependent redox indicator"}]}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "Source main-batch input is 1 mg; stored same numeral
    G_PER_L has wrong mass unit and unsupported final-volume basis. Preserve explicit
    mass without assuming one final liter.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Source main-batch input is 1
    mg; stored same numeral G_PER_L has wrong mass unit and unsupported final-volume
    basis. Preserve explicit mass without assuming one final liter."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Source main-batch input is 1
    mg; stored same numeral G_PER_L has wrong mass unit and unsupported final-volume
    basis. Preserve explicit mass without assuming one final liter."}]}, {"quantity_id":
    "q6", "topic": "MgCl2・6H2O", "source": {"evidence_id": "togo768", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path":
    "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[0].items[5]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"MgCl2・6H2O\",\n          \"volume\":
    0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\":
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
    "MgCl2・6H2O", "volume": 0.2, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001013",
    "gmo_id": "GMO_001013", "label": "Magnesium chloride hexahydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "unsupported",
    "rationale": "Source main-batch mass 0.2 g agrees numerically, but a water input
    of 1 L does not establish final volume. Current G_PER_L is not independently verified;
    MediaDive declares a different g_l using nominal volume 1015. Preserve the batch
    mass and qualify any provider rate separately.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path":
    "ingredients[5].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "Source main-batch mass 0.2 g agrees numerically,
    but a water input of 1 L does not establish final volume. Current G_PER_L is not
    independently verified; MediaDive declares a different g_l using nominal volume
    1015. Preserve the batch mass and qualify any provider rate separately."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch
    mass 0.2 g agrees numerically, but a water input of 1 L does not establish final
    volume. Current G_PER_L is not independently verified; MediaDive declares a different
    g_l using nominal volume 1015. Preserve the batch mass and qualify any provider
    rate separately."}]}, {"quantity_id": "q7", "topic": "Na2S・9H2O", "source": {"evidence_id":
    "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[0].items[6]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"Na2S・9H2O\",\n          \"volume\":
    0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\":
    \"GMO_001014\",\n          \"label\": \"Sodium sulfide nonahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing
    agent\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "Na2S・9H2O", "volume": 0.5, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001014",
    "gmo_id": "GMO_001014", "label": "Sodium sulfide nonahydrate", "properties": [{"id":
    "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic
    compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000064", "uri": "http://purl.jp/bio/10/gmo/GMO_000064",
    "label": "Reducing agent"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "unsupported",
    "rationale": "Source main-batch mass 0.5 g agrees numerically, but a water input
    of 1 L does not establish final volume. Current G_PER_L is not independently verified;
    MediaDive declares a different g_l using nominal volume 1015. Preserve the batch
    mass and qualify any provider rate separately.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path":
    "ingredients[6].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "Source main-batch mass 0.5 g agrees numerically,
    but a water input of 1 L does not establish final volume. Current G_PER_L is not
    independently verified; MediaDive declares a different g_l using nominal volume
    1015. Preserve the batch mass and qualify any provider rate separately."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch
    mass 0.5 g agrees numerically, but a water input of 1 L does not establish final
    volume. Current G_PER_L is not independently verified; MediaDive declares a different
    g_l using nominal volume 1015. Preserve the batch mass and qualify any provider
    rate separately."}]}, {"quantity_id": "q8", "topic": "FeSO4・7H2O", "source": {"evidence_id":
    "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[0].items[7]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"FeSO4・7H2O\",\n          \"volume\":
    1.5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\":
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
    "FeSO4・7H2O", "volume": 1.5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001016",
    "gmo_id": "GMO_001016", "label": "Iron(II) sulfate heptahydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "Source main-batch input is 1.5 mg; stored same numeral G_PER_L has
    wrong mass unit and unsupported final-volume basis. Preserve explicit mass without
    assuming one final liter.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source main-batch input
    is 1.5 mg; stored same numeral G_PER_L has wrong mass unit and unsupported final-volume
    basis. Preserve explicit mass without assuming one final liter."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source main-batch input
    is 1.5 mg; stored same numeral G_PER_L has wrong mass unit and unsupported final-volume
    basis. Preserve explicit mass without assuming one final liter."}]}, {"quantity_id":
    "q9", "topic": "Na2HPO4・12H2O", "source": {"evidence_id": "togo768", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768", "raw_path":
    "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[0].items[8]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"Na2HPO4・12H2O\",\n          \"volume\":
    5.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001115\",\n          \"gmo_id\":
    \"GMO_001115\",\n          \"label\": \"Disodium phosphate dodecahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "Na2HPO4・12H2O", "volume": 5.3, "unit":
    "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001115", "gmo_id": "GMO_001115", "label":
    "Disodium phosphate dodecahydrate", "properties": [{"id": "GMO_000040", "uri":
    "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id":
    "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined
    component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038",
    "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, "decision": "unsupported",
    "rationale": "Source main-batch mass 5.3 g agrees numerically, but a water input
    of 1 L does not establish final volume. Current G_PER_L is not independently verified;
    MediaDive declares a different g_l using nominal volume 1015. Preserve the batch
    mass and qualify any provider rate separately.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path":
    "ingredients[8].concentration", "stored_value": {"value": "5.3", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "Source main-batch mass 5.3 g agrees numerically,
    but a water input of 1 L does not establish final volume. Current G_PER_L is not
    independently verified; MediaDive declares a different g_l using nominal volume
    1015. Preserve the batch mass and qualify any provider rate separately."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "5.3",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch
    mass 5.3 g agrees numerically, but a water input of 1 L does not establish final
    volume. Current G_PER_L is not independently verified; MediaDive declares a different
    g_l using nominal volume 1015. Preserve the batch mass and qualify any provider
    rate separately."}]}, {"quantity_id": "q10", "topic": "Glucose", "source": {"evidence_id":
    "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[0].items[9]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"Glucose\",\n          \"volume\":
    5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001815\",\n          \"gmo_id\":
    \"GMO_001815\",\n          \"label\": \"Glucose\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "Glucose", "volume": 5, "unit": "g",
    "gmo": "http://purl.jp/bio/10/gmo/GMO_001815", "gmo_id": "GMO_001815", "label":
    "Glucose", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041",
    "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000063", "uri": "http://purl.jp/bio/10/gmo/GMO_000063",
    "label": "Carbon source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "unsupported",
    "rationale": "Source main-batch mass 5 g agrees numerically, but a water input
    of 1 L does not establish final volume. Current G_PER_L is not independently verified;
    MediaDive declares a different g_l using nominal volume 1015. Preserve the batch
    mass and qualify any provider rate separately.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml", "field_path":
    "ingredients[9].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "Source main-batch mass 5 g agrees numerically,
    but a water input of 1 L does not establish final volume. Current G_PER_L is not
    independently verified; MediaDive declares a different g_l using nominal volume
    1015. Preserve the batch mass and qualify any provider rate separately."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "Source main-batch mass 5
    g agrees numerically, but a water input of 1 L does not establish final volume.
    Current G_PER_L is not independently verified; MediaDive declares a different
    g_l using nominal volume 1015. Preserve the batch mass and qualify any provider
    rate separately."}]}, {"quantity_id": "q11", "topic": "HCl", "source": {"evidence_id":
    "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[0].items[12]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"HCl\",\n          \"conc_value\":
    1,\n          \"conc_unit\": \"N\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\":
    \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "HCl", "conc_value": 1, "conc_unit": "N", "gmo": "http://purl.jp/bio/10/gmo/GMO_001499",
    "gmo_id": "GMO_001499", "label": "Hydrochloric acid solution", "properties": [{"id":
    "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined
    component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040",
    "label": "Inorganic compound"}, {"id": "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051",
    "label": "Solution"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044",
    "label": "Solvating media"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "not_quantified",
    "rationale": "No fixed titrant amount is specified, so VARIABLE remains an unquantified
    placeholder; HCl 1 N is reagent strength for separately prepared sulfide, not
    a fixed final-medium dose.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "No fixed titrant
    amount is specified, so VARIABLE remains an unquantified placeholder; HCl 1 N
    is reagent strength for separately prepared sulfide, not a fixed final-medium
    dose."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "No fixed titrant
    amount is specified, so VARIABLE remains an unquantified placeholder; HCl 1 N
    is reagent strength for separately prepared sulfide, not a fixed final-medium
    dose."}]}, {"quantity_id": "q12", "topic": "NaCl", "source": {"evidence_id": "togo768",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[1].items[1]", "accessed_at": "2026-10-28T10:59:54.946565Z",
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
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "Source trace-stock input is 1 g; it is not a direct final-medium
    rate. Preserve stock stage and explicit unit, with water input distinguished from
    final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 1 g; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 1 g; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}]}, {"quantity_id": "q13", "topic": "CaCl2・2H2O",
    "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[1].items[2]", "accessed_at": "2026-10-28T10:59:54.946565Z",
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
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "Source trace-stock input is 0.1 g; it is not a direct final-medium
    rate. Preserve stock stage and explicit unit, with water input distinguished from
    final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 0.1 g; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 0.1 g; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}]}, {"quantity_id": "q14", "topic": "Na2MoO4・2H2O",
    "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[1].items[3]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\":
    10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\":
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
    "Na2MoO4・2H2O", "volume": 10, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001011",
    "gmo_id": "GMO_001011", "label": "Sodium molybdate dihydrate", "properties": [{"id":
    "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic
    compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "Source trace-stock input is 10 mg; it is not a direct final-medium
    rate. Preserve stock stage and explicit unit, with water input distinguished from
    final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 10 mg; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 10 mg; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}]}, {"quantity_id": "q15", "topic": "H3BO3",
    "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[1].items[4]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 10,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\":
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
    "H3BO3", "volume": 10, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001015",
    "gmo_id": "GMO_001015", "label": "Boric acid", "properties": [{"id": "GMO_000040",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"},
    {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined
    component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "Source trace-stock input is 10 mg; it is not a direct final-medium
    rate. Preserve stock stage and explicit unit, with water input distinguished from
    final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 10 mg; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 10 mg; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}]}, {"quantity_id": "q16", "topic": "MnCl2・4H2O",
    "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[1].items[5]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"MnCl2・4H2O\",\n          \"volume\":
    0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\":
    \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "MnCl2・4H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001020",
    "gmo_id": "GMO_001020", "label": "Manganese chloride tetrahydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "Source trace-stock input is 0.1 g; it is not a direct final-medium
    rate. Preserve stock stage and explicit unit, with water input distinguished from
    final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 0.1 g; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 0.1 g; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}]}, {"quantity_id": "q17", "topic": "CoCl2・6H2O",
    "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[1].items[6]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"CoCl2・6H2O\",\n          \"volume\":
    0.17,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\":
    \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "CoCl2・6H2O", "volume": 0.17, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001021",
    "gmo_id": "GMO_001021", "label": "Cobalt dichloride hexahydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "Source trace-stock input is 0.17 g; it is not a direct final-medium
    rate. Preserve stock stage and explicit unit, with water input distinguished from
    final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.17",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 0.17 g; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.17",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 0.17 g; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}]}, {"quantity_id": "q18", "topic": "NiCl2・6H2O",
    "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[1].items[7]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\":
    26,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\":
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
    "NiCl2・6H2O", "volume": 26, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001022",
    "gmo_id": "GMO_001022", "label": "Nickel chloride hexahydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "Source trace-stock input is 26 mg; it is not a direct final-medium
    rate. Preserve stock stage and explicit unit, with water input distinguished from
    final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "26",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 26 mg; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "26",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 26 mg; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}]}, {"quantity_id": "q19", "topic": "ZnCl2",
    "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[1].items[8]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 0.1,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\":
    \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "ZnCl2", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001035",
    "gmo_id": "GMO_001035", "label": "Zinc chloride", "properties": [{"id": "GMO_000040",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"},
    {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined
    component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "Source trace-stock input is 0.1 g; it is not a direct final-medium
    rate. Preserve stock stage and explicit unit, with water input distinguished from
    final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 0.1 g; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 0.1 g; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}]}, {"quantity_id": "q20", "topic": "Na2SeO3・5H2O",
    "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[1].items[9]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"Na2SeO3・5H2O\",\n          \"volume\":
    20,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001046\",\n          \"gmo_id\":
    \"GMO_001046\",\n          \"label\": \"Sodium selenite pentahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "Na2SeO3・5H2O", "volume": 20, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001046",
    "gmo_id": "GMO_001046", "label": "Sodium selenite pentahydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "Source trace-stock input is 20 mg; it is not a direct final-medium
    rate. Preserve stock stage and explicit unit, with water input distinguished from
    final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "20",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 20 mg; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "20",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 20 mg; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}]}, {"quantity_id": "q21", "topic": "Nitrilotriacetic
    acid", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[1].items[10]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\":
    12.8,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001053\",\n          \"gmo_id\":
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
    "Nitrilotriacetic acid", "volume": 12.8, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001053",
    "gmo_id": "GMO_001053", "label": "Nitrilotriacetic acid", "properties": [{"id":
    "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic
    compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "Source trace-stock input is 12.8 g; it is not a direct final-medium
    rate. Preserve stock stage and explicit unit, with water input distinguished from
    final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "12.8",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 12.8 g; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "12.8",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 12.8 g; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}]}, {"quantity_id": "q22", "topic": "CuCl2",
    "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[1].items[11]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"CuCl2\",\n          \"volume\": 20,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001542\",\n          \"gmo_id\":
    \"GMO_001542\",\n          \"label\": \"Copper(II) chloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "CuCl2", "volume": 20, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001542",
    "gmo_id": "GMO_001542", "label": "Copper(II) chloride", "properties": [{"id":
    "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic
    compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "Source trace-stock input is 20 mg; it is not a direct final-medium
    rate. Preserve stock stage and explicit unit, with water input distinguished from
    final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "20",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 20 mg; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "20",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 20 mg; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}]}, {"quantity_id": "q23", "topic": "FeCl2・4H2O",
    "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[1].items[12]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"FeCl2・4H2O\",\n          \"volume\":
    0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\":
    \"GMO_001548\",\n          \"label\": \"Iron(II) chloride tetrahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "FeCl2・4H2O", "volume": 0.2, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001548",
    "gmo_id": "GMO_001548", "label": "Iron(II) chloride tetrahydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "Source trace-stock input is 0.2 g; it is not a direct final-medium
    rate. Preserve stock stage and explicit unit, with water input distinguished from
    final volume. MediaDive stock g_l is only a provider-declared stock rate.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 0.2 g; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source trace-stock input
    is 0.2 g; it is not a direct final-medium rate. Preserve stock stage and explicit
    unit, with water input distinguished from final volume. MediaDive stock g_l is
    only a provider-declared stock rate."}]}, {"quantity_id": "q24", "topic": "KOH",
    "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[1].items[13]", "accessed_at": "2026-10-28T10:59:54.946565Z",
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
    decoded object independently equals exact JSON locator."}, "decision": "not_quantified",
    "rationale": "No KOH dose is specified. VARIABLE is compatible with an unquantified
    adjustment reagent, but its parent placement must be changed to trace-stock preparation.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "ingredients[23].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "No KOH dose is
    specified. VARIABLE is compatible with an unquantified adjustment reagent, but
    its parent placement must be changed to trace-stock preparation."}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "ingredients[23].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "not_quantified", "rationale": "No KOH dose is
    specified. VARIABLE is compatible with an unquantified adjustment reagent, but
    its parent placement must be changed to trace-stock preparation."}]}, {"quantity_id":
    "q25", "topic": "Receiving stock addition 1", "source": {"evidence_id": "togo768",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[0].items[10]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"Trace element solution (see below)\",\n          \"volume\":
    10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M768\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name":
    "Trace element solution (see below)", "volume": 10, "unit": "ml", "reference_media_id":
    "M768", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "Source addition is 10 ml per listed receiving batch,
    not grams per liter; do not infer a final-volume denominator.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "solutions[0].concentration", "stored_value": {"value": "10", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Source addition is 10 ml per
    listed receiving batch, not grams per liter; do not infer a final-volume denominator."},
    {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "solutions[0].concentration", "stored_value": {"value": "10", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Source addition is 10 ml per
    listed receiving batch, not grams per liter; do not infer a final-volume denominator."}]},
    {"quantity_id": "q26", "topic": "Receiving stock addition 2", "source": {"evidence_id":
    "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.components[0].items[11]", "accessed_at": "2026-10-28T10:59:54.946565Z",
    "quote": "{\n          \"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\":
    5,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name":
    "Trace vitamins (see Medium [M190])", "volume": 5, "unit": "ml", "reference_media_id":
    "M190", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "Source addition is 5 ml per listed receiving batch, not
    grams per liter; do not infer a final-volume denominator.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "solutions[1].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Source addition is 5 ml per listed
    receiving batch, not grams per liter; do not infer a final-volume denominator."},
    {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "solutions[1].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Source addition is 5 ml per listed
    receiving batch, not grams per liter; do not infer a final-volume denominator."}]},
    {"quantity_id": "q27", "topic": "M190 referenced vitamin: Distilled water", "source":
    {"evidence_id": "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[0]", "accessed_at": "2026-10-28T10:59:55.487110Z",
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
    decoded object independently equals exact JSON locator."}, "decision": "verified",
    "rationale": "Existing 1 L water is verified as stock-batch input only, not measured
    final volume.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "solutions[1].composition[0].concentration", "stored_value": {"value":
    "1", "unit": "L"}, "decision": "verified", "rationale": "Existing 1 L water is
    verified as stock-batch input only, not measured final volume."}]}, {"quantity_id":
    "q28", "topic": "M190 referenced vitamin: Biotin", "source": {"evidence_id": "togo190",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[1]", "accessed_at": "2026-10-28T10:59:55.487110Z",
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
    object independently equals exact JSON locator."}, "decision": "verified", "rationale":
    "Existing note correctly retains 2 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[1].notes",
    "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component,
    Simple component\n\nSource batch input: 2 mg. Final preparation volume is not
    independently established; the unsupported g/L assertion is withdrawn, not replaced
    by an assumed one-liter concentration.", "decision": "verified", "rationale":
    "Existing note correctly retains 2 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q29",
    "topic": "M190 referenced vitamin: p--Aminobenzoic acid", "source": {"evidence_id":
    "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[2]", "accessed_at": "2026-10-28T10:59:55.487110Z",
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
    object independently equals exact JSON locator."}, "decision": "verified", "rationale":
    "Existing note correctly retains 5 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[2].notes",
    "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component,
    Simple component\n\nSource batch input: 5 mg. Final preparation volume is not
    independently established; the unsupported g/L assertion is withdrawn, not replaced
    by an assumed one-liter concentration.", "decision": "verified", "rationale":
    "Existing note correctly retains 5 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q30",
    "topic": "M190 referenced vitamin: Thiamine・HCl", "source": {"evidence_id": "togo190",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[3]", "accessed_at": "2026-10-28T10:59:55.487110Z",
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
    object independently equals exact JSON locator."}, "decision": "verified", "rationale":
    "Existing note correctly retains 5 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[3].notes",
    "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component,
    Simple component\n\nSource batch input: 5 mg. Final preparation volume is not
    independently established; the unsupported g/L assertion is withdrawn, not replaced
    by an assumed one-liter concentration.", "decision": "verified", "rationale":
    "Existing note correctly retains 5 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q31",
    "topic": "M190 referenced vitamin: Calcium pantothenate", "source": {"evidence_id":
    "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[4]", "accessed_at": "2026-10-28T10:59:55.487110Z",
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
    object independently equals exact JSON locator."}, "decision": "verified", "rationale":
    "Existing note correctly retains 5 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[4].notes",
    "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component,
    Simple component\n\nSource batch input: 5 mg. Final preparation volume is not
    independently established; the unsupported g/L assertion is withdrawn, not replaced
    by an assumed one-liter concentration.", "decision": "verified", "rationale":
    "Existing note correctly retains 5 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q32",
    "topic": "M190 referenced vitamin: Pyridoxine・HCl", "source": {"evidence_id":
    "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[5]", "accessed_at": "2026-10-28T10:59:55.487110Z",
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
    object independently equals exact JSON locator."}, "decision": "verified", "rationale":
    "Existing note correctly retains 10 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[5].notes",
    "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component,
    Simple component\n\nSource batch input: 10 mg. Final preparation volume is not
    independently established; the unsupported g/L assertion is withdrawn, not replaced
    by an assumed one-liter concentration.", "decision": "verified", "rationale":
    "Existing note correctly retains 10 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q33",
    "topic": "M190 referenced vitamin: Folic acid", "source": {"evidence_id": "togo190",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[6]", "accessed_at": "2026-10-28T10:59:55.487110Z",
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
    object independently equals exact JSON locator."}, "decision": "verified", "rationale":
    "Existing note correctly retains 2 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[6].notes",
    "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component,
    Simple component\n\nSource batch input: 2 mg. Final preparation volume is not
    independently established; the unsupported g/L assertion is withdrawn, not replaced
    by an assumed one-liter concentration.", "decision": "verified", "rationale":
    "Existing note correctly retains 2 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q34",
    "topic": "M190 referenced vitamin: Vitamin B12", "source": {"evidence_id": "togo190",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[7]", "accessed_at": "2026-10-28T10:59:55.487110Z",
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
    object independently equals exact JSON locator."}, "decision": "verified", "rationale":
    "Existing note correctly retains 0.1 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[7].notes",
    "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component,
    Simple component\n\nSource batch input: 0.1 mg. Final preparation volume is not
    independently established; the unsupported g/L assertion is withdrawn, not replaced
    by an assumed one-liter concentration.", "decision": "verified", "rationale":
    "Existing note correctly retains 0.1 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q35",
    "topic": "M190 referenced vitamin: Riboflavin", "source": {"evidence_id": "togo190",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[8]", "accessed_at": "2026-10-28T10:59:55.487110Z",
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
    object independently equals exact JSON locator."}, "decision": "verified", "rationale":
    "Existing note correctly retains 5 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[8].notes",
    "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component,
    Simple component\n\nSource batch input: 5 mg. Final preparation volume is not
    independently established; the unsupported g/L assertion is withdrawn, not replaced
    by an assumed one-liter concentration.", "decision": "verified", "rationale":
    "Existing note correctly retains 5 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q36",
    "topic": "M190 referenced vitamin: Nicotinic acid", "source": {"evidence_id":
    "togo190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[9]", "accessed_at": "2026-10-28T10:59:55.487110Z",
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
    object independently equals exact JSON locator."}, "decision": "verified", "rationale":
    "Existing note correctly retains 5 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[9].notes",
    "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component,
    Simple component\n\nSource batch input: 5 mg. Final preparation volume is not
    independently established; the unsupported g/L assertion is withdrawn, not replaced
    by an assumed one-liter concentration.", "decision": "verified", "rationale":
    "Existing note correctly retains 5 mg batch mass and withdraws unsupported final
    concentration; preserve this repair and its evidence."}]}, {"quantity_id": "q37",
    "topic": "M190 referenced vitamin: Lipoic acid", "source": {"evidence_id": "togo190",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch064/source01/togo190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[10]", "accessed_at": "2026-10-28T10:59:55.487110Z",
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
    decoded object independently equals exact JSON locator."}, "decision": "verified",
    "rationale": "Existing note correctly retains 5 mg batch mass and withdraws unsupported
    final concentration; preserve this repair and its evidence.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "solutions[1].composition[10].notes", "stored_value": "Role: Growth factor; Properties:
    Organic compound, Defined component, Simple component\n\nSource batch input: 5
    mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "verified", "rationale": "Existing note correctly retains 5 mg batch
    mass and withdraws unsupported final concentration; preserve this repair and its
    evidence."}]}, {"quantity_id": "q38", "topic": "Missing source preparation 1",
    "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.comments[0]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote":
    "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Adjust pH to 6.0 -- 6.5.\"\n    }",
    "exact_decoded_object": {"paragraph_index": 2, "comment": "Adjust pH to 6.0 --
    6.5."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, "decision": "evidence_only", "rationale": "Main
    preparation states pH 6.0–6.5; TOGO meta.ph 7.0 and API medium.min_pH/max_pH 6.5
    are scoped conflicting metadata, not reasons to discard the explicit step.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "evidence_only",
    "rationale": "Main preparation states pH 6.0–6.5; TOGO meta.ph 7.0 and API medium.min_pH/max_pH
    6.5 are scoped conflicting metadata, not reasons to discard the explicit step.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "evidence_only",
    "rationale": "Main preparation states pH 6.0–6.5; TOGO meta.ph 7.0 and API medium.min_pH/max_pH
    6.5 are scoped conflicting metadata, not reasons to discard the explicit step.",
    "missing": true}]}, {"quantity_id": "q39", "topic": "Missing source preparation
    2", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.comments[1]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote":
    "{\n      \"paragraph_index\": 3,\n      \"comment\": \"Prepare sodium sulfide
    separately as 5% (w/v) solution, autoclave under a nitrogen atmosphere and neutralize
    with 1 N HCl before use. Sterilize glucose separately.\"\n    }", "exact_decoded_object":
    {"paragraph_index": 3, "comment": "Prepare sodium sulfide separately as 5% (w/v)
    solution, autoclave under a nitrogen atmosphere and neutralize with 1 N HCl before
    use. Sterilize glucose separately."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "evidence_only", "rationale": "Separate sulfide 5% w/v stock, nitrogen autoclave,
    1 N HCl neutralization and separate glucose sterilization are absent locally.
    These specify preparation, not stock volume or incubation conditions.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "evidence_only",
    "rationale": "Separate sulfide 5% w/v stock, nitrogen autoclave, 1 N HCl neutralization
    and separate glucose sterilization are absent locally. These specify preparation,
    not stock volume or incubation conditions.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "evidence_only",
    "rationale": "Separate sulfide 5% w/v stock, nitrogen autoclave, 1 N HCl neutralization
    and separate glucose sterilization are absent locally. These specify preparation,
    not stock volume or incubation conditions.", "missing": true}]}, {"quantity_id":
    "q40", "topic": "Missing source preparation 3", "source": {"evidence_id": "togo768",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.comments[2]", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote":
    "{\n      \"paragraph_index\": 5,\n      \"comment\": \"First, dissolve nitrilotriacetic
    acid and adjust to pH 6.5 with KOH.\"\n    }", "exact_decoded_object": {"paragraph_index":
    5, "comment": "First, dissolve nitrilotriacetic acid and adjust to pH 6.5 with
    KOH."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, "decision": "evidence_only", "rationale": "Trace-stock
    NTA dissolution and pH 6.5 KOH adjustment are separate from main-medium pH.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_THERMOSULFUROGENES_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "evidence_only",
    "rationale": "Trace-stock NTA dissolution and pH 6.5 KOH adjustment are separate
    from main-medium pH.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "evidence_only",
    "rationale": "Trace-stock NTA dissolution and pH 6.5 KOH adjustment are separate
    from main-medium pH.", "missing": true}]}, {"quantity_id": "q41", "topic": "Conflicting
    source pH metadata", "source": {"evidence_id": "togo768", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M768",
    "raw_path": "REVIEW_WORK/batch064/source01/togo768.bin", "raw_sha256": "38477fe39edb680fdd163b3161c157c755bc610cfbbd34e7de674355514e2528",
    "locator": "$.meta", "accessed_at": "2026-10-28T10:59:54.946565Z", "quote": "{\n    \"gm\":
    \"http://togomedium.org/medium/M768\",\n    \"name\": \"Clostridium Thermosulfurogenes
    Medium\",\n    \"original_media_id\": \"JCM_M743\",\n    \"src_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=743\",\n    \"ph\":
    \"7.0\"\n  }", "exact_decoded_object": {"gm": "http://togomedium.org/medium/M768",
    "name": "Clostridium Thermosulfurogenes Medium", "original_media_id": "JCM_M743",
    "src_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=743", "ph": "7.0"},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, "decision": "conflict", "rationale": "TOGO meta.ph
    7.0 disagrees with its comments[0] range6.0–6.5. API medium.min_pH/max_pH 6.5
    is a scalar within the range. No current local pH is asserted. Preserve each source
    locus and favor no invented reconciliation.", "layer_assessments": [], "corroboration":
    [{"evidence_id": "apiJ743", "reference": "https://mediadive.dsmz.de/rest/medium/J743",
    "raw_path": "REVIEW_WORK/batch064/source01/apiJ743.bin", "raw_sha256": "f32986f3cb333c4fdba212746030a76076f39ac33090109ad3e4727f34a14b8a",
    "locator": "$.data.medium", "accessed_at": "2026-10-28T10:59:54.900568Z", "quote":
    "{\n            \"id\": \"J743\",\n            \"name\": \"CLOSTRIDIUM THERMOSULFUROGENES
    MEDIUM\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\": 6.5,\n            \"max_pH\":
    6.5,\n            \"source\": \"JCM\",\n            \"link\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=743\"\n        }",
    "exact_decoded_object": {"id": "J743", "name": "CLOSTRIDIUM THERMOSULFUROGENES
    MEDIUM", "complex_medium": "yes", "min_pH": 6.5, "max_pH": 6.5, "source": "JCM",
    "link": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=743"}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}]}]'
- assessment_id: a5
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: concern
  summary: All current target/owner and scoped vitamin identifier slots are inventoried;
    ingredient ontology terms are checked against fresh OLS and the packaged MIM catalog.
    Three source-explicit hydrates map to anhydrous forms. Generic calcium pantothenate
    source text does not establish the D-specific structure in CHEBI:31345; specificity
    remains unresolved, not an assertion of the opposite enantiomer. Catalog presence
    and labels do not authenticate source chemical form.
  target_ids:
  - CultureMech:010175
  evidence_ids:
  - grounding
- assessment_id: a6
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Complete selected target and owner histories, references and all eleven
    vitamin claims were read. Four exact historical reports are mechanical source-incomplete
    context; the current dependency repair is credited. Matching old/current TOGO190
    and JCM197 raw hashes authenticate bytes, not historical access events. Existing
    history remains append-only.
  target_ids:
  - CultureMech:010175
  evidence_ids:
  - history
  - scalars
  - dependency-provenance
  - attached-evidence-joins
- assessment_id: a7
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:010175
  evidence_ids:
  - local-target
- assessment_id: a8
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:010175
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-010175-stock-stages-and-source-units-are-conflated
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Stock stages and source units are conflated
  description: Main and trace-stock water inputs were combined; the generated record
    retains 2.0 G_PER_L while the maintained owner reduced it to 1.0 G_PER_L. Both
    remain wrong as stage-specific water quantities. Resazurin and ferrous sulfate
    use source mg as g/L; trace-stock contents are direct ingredients, with several
    mg values likewise read as g/L. Both receiving stock doses use G_PER_L although
    source additions are volumes. Main g values remain batch inputs without an independently
    established final volume. Correct the maintained representation with exact source
    units and nested stages, preserving the owner repair as historical context.
  target_ids:
  - CultureMech:010175
  field_paths:
  - ingredients
  - solutions[0].concentration
  - solutions[1].concentration
  evidence_ids:
  - quantities
  - togo768
  - apiJ743
  - writer-togo
  - writer-cleanup
  - writer-repair
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-010175-referenced-stock-compositions-remain-unresolved
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Referenced stock compositions remain unresolved
  description: Trace element contents belong inside solutions[0], whose composition
    is empty. The vitamin stub refers to M190 as a whole; only its repaired solutions[1].composition
    is the relevant dependency. Retain the 11 supported vitamin claims and target-specific
    addition; do not import M190 receiving dose or parent conditions. Give each stock
    its source name and a scoped, resolvable reference or inline composition.
  target_ids:
  - CultureMech:010175
  field_paths:
  - solutions[0]
  - solutions[1]
  evidence_ids:
  - togo768
  - apiJ743
  - dependency-vitamin
  - attached-evidence-joins
  - writer-migrate
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-010175-hydrate-identities-do-not-match-explicit-source-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Hydrate identities do not match explicit source forms
  description: Na2HPO4·12H2O is mapped to CHEBI:34683 whose formula lacks twelve waters;
    CoCl2·6H2O and NiCl2·6H2O map to anhydrous CHEBI:35696 and CHEBI:34887. Fresh
    OLS CHEBI:53503/CHEBI:53542 confirm cobalt/nickel hexahydrate candidates. Verify
    a source-exact sodium phosphate hydrate before proposing its identifier. Neutral
    Resazurin is not a sodium salt assertion. Preserve explicit hydrate mass basis.
  target_ids:
  - CultureMech:010175
  field_paths:
  - ingredients[8].term
  - ingredients[16].term
  - ingredients[17].term
  evidence_ids:
  - togo768
  - grounding
  - chebi34683
  - chebi35696
  - chebi34887
  - chebi53503
  - chebi53542
  rule_id: source-chemical-form-mismatch
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-010175-preparation-boundaries-and-ph-evidence-are-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation boundaries and pH evidence are missing
  description: Source comments specify separate sulfide preparation/neutralization
    and glucose sterilization, main pH range and separate trace-stock adjustment.
    Current target and owner omit preparation_steps. Preserve stock strength versus
    receiving contribution and main versus stock pH; keep TOGO scalar pH conflict
    explicit. Do not invent stock volume, incubation atmosphere, temperature or sterilization
    time.
  target_ids:
  - CultureMech:010175
  field_paths:
  - preparation_steps
  - ph_value
  - ingredients[10]
  - ingredients[23]
  evidence_ids:
  - quantities
  - togo768
  - apiJ743
  - writer-togo
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f5
  issue_key: culturemech-010175-source-claims-lack-field-level-evidence
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Source claims lack field-level evidence
  description: The selected target and owner retain source URLs but no attached quantity/preparation
    evidence. Add narrowly scoped evidence for each repaired claim, retain unavailable
    JCM743 status and append history rather than rewriting earlier events. M190 vitamin
    evidence already exists and is verified separately.
  target_ids:
  - CultureMech:010175
  field_paths:
  - notes
  - ingredients
  - solutions
  - curation_history
  evidence_ids:
  - local-target
  - owner-1
  - attached-evidence-joins
  - dependency-provenance
  rule_id: source-stage-or-identity
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Main and trace-stock water inputs were combined; the generated record
    retains 2.0 G_PER_L while the maintained owner reduced it to 1.0 G_PER_L. Both
    remain wrong as stage-specific water quantities. Resazurin and ferrous sulfate
    use source mg as g/L; trace-stock contents are direct ingredients, with several
    mg values likewise read as g/L. Both receiving stock doses use G_PER_L although
    source additions are volumes. Main g values remain batch inputs without an independently
    established final volume. Correct the maintained representation with exact source
    units and nested stages, preserving the owner repair as historical context.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010175
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Trace element contents belong inside solutions[0], whose composition
    is empty. The vitamin stub refers to M190 as a whole; only its repaired solutions[1].composition
    is the relevant dependency. Retain the 11 supported vitamin claims and target-specific
    addition; do not import M190 receiving dose or parent conditions. Give each stock
    its source name and a scoped, resolvable reference or inline composition.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010175
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Na2HPO4·12H2O is mapped to CHEBI:34683 whose formula lacks twelve waters;
    CoCl2·6H2O and NiCl2·6H2O map to anhydrous CHEBI:35696 and CHEBI:34887. Fresh
    OLS CHEBI:53503/CHEBI:53542 confirm cobalt/nickel hexahydrate candidates. Verify
    a source-exact sodium phosphate hydrate before proposing its identifier. Neutral
    Resazurin is not a sodium salt assertion. Preserve explicit hydrate mass basis.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010175
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: Source comments specify separate sulfide preparation/neutralization
    and glucose sterilization, main pH range and separate trace-stock adjustment.
    Current target and owner omit preparation_steps. Preserve stock strength versus
    receiving contribution and main versus stock pH; keep TOGO scalar pH conflict
    explicit. Do not invent stock volume, incubation atmosphere, temperature or sterilization
    time.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010175
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action5
  description: The selected target and owner retain source URLs but no attached quantity/preparation
    evidence. Add narrowly scoped evidence for each repaired claim, retain unavailable
    JCM743 status and append history rather than rewriting earlier events. M190 vitamin
    evidence already exists and is verified separately.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:010175
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M768_Clostridium_Thermosulfurogenes_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- Exact JCM743 endpoint returned HTTP 200 with Nothing found. Source-dependent findings
  use inspected TOGO M768 and MediaDive J743; primary verification of the full selected
  formulation remains unavailable.
- M190 scientific dependency scope is only solutions[1].composition and exact corresponding
  source vitamin tables. Parent dose, parent recipe, other stocks and parent growth/preparation
  conditions are excluded.
- No independently established final volume is inferred from water input or provider
  nominal volume. MediaDive g_l values remain provider declarations, not measured
  concentrations.
- Generic calcium pantothenate does not resolve stereochemical specificity. No exact
  sodium phosphate dodecahydrate replacement identifier is proposed in this review.
- No strain-level growth evidence or taxonomic assertion is inferred from a medium
  name or general application. iModulonDB is not applicable to this medium identity
  review.
- Canonical reference validation ran zero reference checks. History/provenance and
  source reference resolution were assessed separately; whole-corpus product, ID and
  merge gates were not rerun for an unchanged-recipe review.
- Current writer code does not authenticate historical execution. No record, generated
  product, scientific status or curation history was modified.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
