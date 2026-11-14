# Scientific review of complete_medium

- Review: 20261028T153314Z-complete-medium-batch071
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T15:21:37.128657Z
- Finished UTC: 2026-10-28T15:33:14.354900Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact NBRC1627 and TOGO M3059 sources support the retained batch ingredients and current magnesium heptahydrate mapping. The local water and iron-stock units conflict with the sources, seven matching masses lack a verified final-volume basis, and source pH is missing. Existing optional-agar wording and the solid branch classification are retained.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch071 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009573 | data/merge_yaml/merged/Complete_Medium.yaml | generated | complete_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009573 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:009573 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:009573 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:009573 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact source and classification

identity: supported. Targets: CultureMech:009573.

The source identity is TOGO M3059 / NBRC1627 Complete Medium, with the same nine batch ingredients. Casein and yeast extract support the existing COMPLEX/UNDEFINED classification. SOLID_AGAR is valid for the optional agar branch, whose qualifier is already retained. No organism is named by the exact formulation sources.

### Preparation and biological evidence

evidence: unknown. Targets: CultureMech:009573.

The official source has no preparation or incubation protocol beyond its composition and pH. No generic autoclaving, atmosphere, strain or growth result is supplied or inferred. Existing general cultivation applications do not constitute experimental growth evidence.

### Current supplied forms and retained repairs

grounding: supported. Targets: CultureMech:009573.

Both current primary and secondary magnesium slots correctly assert heptahydrate CHEBI:31795, matching the explicit source form; the historical primary repair is credited. All asserted CHEBI labels match current OLS. Generic sodium citrate does not establish hydration, and the bare FeSO4 stock designation does not establish a hydrate. Casein, yeast extract, agar and the stock remain without forced pure-compound mappings. Exact CSV aliases can contain differing hydrate labels; their presence does not override the source and current authority.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:009573.

The complete current history retains import, grounding, naming and heptahydrate-repair events. Both October reports checked zero external source references and do not authenticate historical retrieval. Current TOGO parsing and source metadata explain possible unit/basis and pH loss risks without proving the historical execution path. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:009573.

All 18 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:009573", "selected_concentration_field_count": 18, "selected_concentration_fields_covered": 18, "decisions": [{"decision_id": "q1", "subject": "Distilled water", "local_fields": [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "NBRC1627 batch input and TOGO M3059 counterpart", "interpretation": "Both exact sources specify 1 L of distilled water, whereas both local layers encode 1 G_PER_L. Retain the explicit solvent input as volume. Listed water is not a measured final batch volume; neither density conversion nor 1000 g/L is inferred.", "sources": [{"locator": "HTML tr[11]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627", "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0", "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6", "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "Distilled water\n1\nL", "quote_representation": "HTML tr[11] DOM text"}, {"locator": "$.components[0].items[0]", "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059", "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject": "MgSO4·7H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC1627 batch input and TOGO M3059 counterpart", "interpretation": "The source explicitly gives 10 g for this batch input, and the local numeric value matches. The stored G_PER_L denominator is not established: 1 L is a water input, with a separate liquid stock addition and no make-up-to-final-volume instruction. Preserve the source batch mass rather than asserting a final concentration.", "sources": [{"locator": "HTML tr[7]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627", "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0", "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6", "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "MgSO\n4\n·7H\n2\nO\n10\ng", "quote_representation": "HTML tr[7] DOM text"}, {"locator": "$.components[0].items[1]", "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059", "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\": \"MgSO4·7H2O\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\": \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "10", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "10", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC1627 batch input and TOGO M3059 counterpart", "interpretation": "The source explicitly gives 10 g for this batch input, and the local numeric value matches. The stored G_PER_L denominator is not established: 1 L is a water input, with a separate liquid stock addition and no make-up-to-final-volume instruction. Preserve the source batch mass rather than asserting a final concentration.", "sources": [{"locator": "HTML tr[5]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627", "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0", "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6", "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "Yeast extract\n10\ng", "quote_representation": "HTML tr[5] DOM text"}, {"locator": "$.components[0].items[2]", "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059", "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\": \"Yeast extract\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "150", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "150", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC1627 batch input and TOGO M3059 counterpart", "interpretation": "The source explicitly gives 150 g for this batch input, and the local numeric value matches. The stored G_PER_L denominator is not established: 1 L is a water input, with a separate liquid stock addition and no make-up-to-final-volume instruction. Preserve the source batch mass rather than asserting a final concentration.", "sources": [{"locator": "HTML tr[10]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627", "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0", "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6", "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "NaCl\n150\ng", "quote_representation": "HTML tr[10] DOM text"}, {"locator": "$.components[0].items[3]", "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059", "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\": \"NaCl\",\n          \"volume\": 150,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "KCl", "local_fields": [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "2", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC1627 batch input and TOGO M3059 counterpart", "interpretation": "The source explicitly gives 2 g for this batch input, and the local numeric value matches. The stored G_PER_L denominator is not established: 1 L is a water input, with a separate liquid stock addition and no make-up-to-final-volume instruction. Preserve the source batch mass rather than asserting a final concentration.", "sources": [{"locator": "HTML tr[8]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627", "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0", "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6", "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "KCl\n2\ng", "quote_representation": "HTML tr[8] DOM text"}, {"locator": "$.components[0].items[4]", "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059", "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\": \"KCl\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\": \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject": "Sodium citrate", "local_fields": [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "3", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "3", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC1627 batch input and TOGO M3059 counterpart", "interpretation": "The source explicitly gives 3 g for this batch input, and the local numeric value matches. The stored G_PER_L denominator is not established: 1 L is a water input, with a separate liquid stock addition and no make-up-to-final-volume instruction. Preserve the source batch mass rather than asserting a final concentration.", "sources": [{"locator": "HTML tr[6]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627", "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0", "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6", "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "Sodium citrate\n3\ng", "quote_representation": "HTML tr[6] DOM text"}, {"locator": "$.components[0].items[5]", "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059", "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\": \"Sodium citrate\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001109\",\n          \"gmo_id\": \"GMO_001109\",\n          \"label\": \"Sodium citrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject": "4.98% FeSO4", "local_fields": [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "NBRC1627 batch input and TOGO M3059 counterpart", "interpretation": "Both sources specify 1 ml of the separately named 4.98% FeSO4 solution. Local 1 G_PER_L confuses the liquid receiving dose with solute mass concentration. Preserve the source stock identity and explicit aliquot; percentage basis, stock preparation, hydrate and final medium denominator remain unspecified.", "sources": [{"locator": "HTML tr[9]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627", "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0", "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6", "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "4.98% FeSO\n4\n1\nml", "quote_representation": "HTML tr[9] DOM text"}, {"locator": "$.components[0].items[6]", "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059", "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\": \"4.98% FeSO4\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001393\",\n          \"gmo_id\": \"GMO_001393\",\n          \"label\": \"Iron(II) sulfate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject": "Casein", "local_fields": [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "7.5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "7.5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC1627 batch input and TOGO M3059 counterpart", "interpretation": "The source explicitly gives 7.5 g for this batch input, and the local numeric value matches. The stored G_PER_L denominator is not established: 1 L is a water input, with a separate liquid stock addition and no make-up-to-final-volume instruction. Preserve the source batch mass rather than asserting a final concentration.", "sources": [{"locator": "HTML tr[4]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627", "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0", "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6", "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "Casein\n7.5\ng", "quote_representation": "HTML tr[4] DOM text"}, {"locator": "$.components[0].items[7]", "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059", "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\": \"Casein\",\n          \"volume\": 7.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001531\",\n          \"gmo_id\": \"GMO_001531\",\n          \"label\": \"Casein\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q9", "subject": "Agar (if needed)", "local_fields": [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "15", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "15", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC1627 batch input and TOGO M3059 counterpart", "interpretation": "The source explicitly gives 15 g for this batch input, and the local numeric value matches. The stored G_PER_L denominator is not established: 1 L is a water input, with a separate liquid stock addition and no make-up-to-final-volume instruction. Preserve the source batch mass rather than asserting a final concentration. Agar is optional in both sources; SOLID_AGAR is valid for the selected solid branch, and the retained preferred_term already preserves if needed.", "sources": [{"locator": "HTML tr[12]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627", "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0", "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6", "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "Agar (if needed)\n15\ng", "quote_representation": "HTML tr[12] DOM text"}, {"locator": "$.components[0].items[8]", "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059", "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\": \"Agar (if needed)\",\n          \"volume\": 15,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001007\",\n          \"gmo_id\": \"GMO_001007\",\n          \"label\": \"Agar\",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000048\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000048\",\n              \"label\": \"Solidifying component\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q10", "subject": "4.98% stock identity", "local_fields": [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path": "ingredients[6].preferred_term", "original": "4.98% FeSO4"}, {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path": "ingredients[6].preferred_term", "original": "4.98% FeSO4"}], "decision": "evidence_only", "stage": "Undetermined percentage basis of the separate iron stock", "interpretation": "The existing stock label retains the literal 4.98% FeSO4 designation. Neither source specifies w/v, w/w, a hydrate, stock final volume or density. Retain this identity without deriving solute mass or final-medium molarity.", "sources": [{"locator": "HTML tr[9]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627", "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0", "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6", "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "4.98% FeSO\n4\n1\nml", "quote_representation": "HTML tr[9] DOM text"}, {"locator": "$.components[0].items[6]", "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059", "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\": \"4.98% FeSO4\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001393\",\n          \"gmo_id\": \"GMO_001393\",\n          \"label\": \"Iron(II) sulfate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q11", "subject": "Source pH", "local_fields": [], "decision": "add", "stage": "Medium pH stated by the exact source", "interpretation": "Both NBRC1627 and TOGO M3059 state pH 7.0. Neither local layer records it. This is source pH, without an inferred adjustment reagent, temperature, timing or sterilization protocol.", "sources": [{"locator": "HTML tr[13]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627", "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0", "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6", "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "pH 7.0", "quote_representation": "HTML tr[13] DOM text"}, {"locator": "$.comments[0]", "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059", "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"pH 7.0\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q12", "subject": "Optional solid branch", "local_fields": [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path": "ingredients[8].preferred_term", "original": "Agar (if needed)"}, {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path": "ingredients[8].preferred_term", "original": "Agar (if needed)"}, {"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path": "physical_state", "original": "SOLID_AGAR"}, {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path": "physical_state", "original": "SOLID_AGAR"}], "decision": "evidence_only", "stage": "Optional agar branch", "interpretation": "The retained if needed wording is correct. SOLID_AGAR describes the agar-containing branch; do not call it a classification error. Preserve the optional liquid alternative without transferring an unrelated formula or claiming a growth result.", "sources": [{"locator": "HTML tr[12]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627", "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0", "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6", "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "Agar (if needed)\n15\ng", "quote_representation": "HTML tr[12] DOM text"}, {"locator": "$.components[0].items[8]", "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059", "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1", "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\": \"Agar (if needed)\",\n          \"volume\": 15,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001007\",\n          \"gmo_id\": \"GMO_001007\",\n          \"label\": \"Agar\",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000048\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000048\",\n              \"label\": \"Solidifying component\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch071/record06/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: supported. Targets: CultureMech:009573.

data/merge_yaml/merged/Complete_Medium.yaml: primary 5/9, secondary 5/9; data/normalized_yaml/bacterial/complete_medium.yaml: primary 5/9, secondary 5/9. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:009573.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:009573.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Water and iron-stock aliquot use mass-rate units

major / open / confirmed; issue key: culturemech-009573-liquid-inputs-misrepresented-as-mass.

Both layers encode the water input and the iron-stock aliquot as G_PER_L, contradicting the explicit L and ml units in both exact sources. The stock percentage and its receiving aliquot are different quantities, and the source does not establish a final-medium solute concentration.

### f2: Matching batch masses have unsupported per-litre denominators

major / open / confirmed; issue key: culturemech-009573-unsupported-final-volume-denominator.

Seven retained numeric masses match the source batch inputs, but the exact sources list water and a separate liquid addition without an explicit final-volume instruction. Therefore the local G_PER_L basis is unverified even where the digits agree; it is not a demonstrated error in the source masses. No claim-level evidence currently records these stage boundaries.

### f3: Source pH is absent from both current layers

minor / open / confirmed; issue key: culturemech-009573-source-ph-missing.

NBRC1627 and TOGO M3059 both state pH 7.0, while the selected target and maintained owner have no pH field. The source does not give a preparation or adjustment procedure.

## Recommended Actions And Acceptance Checks

### action1

Restore explicit source solvent volume and liquid-stock dose with source-scoped evidence. Keep the iron-stock percentage basis and chemical form unresolved unless separately verified; do not substitute water density or infer final-medium iron mass.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Preserve all explicit batch masses and optional agar context. Withdraw or qualify unsupported final-volume normalization, and attach exact source excerpts at the represented quantity/stage. Do not calculate a replacement final denominator from nominal water plus stock volume.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Add the exact source pH with a claim-scoped excerpt and preserve its limited context. Do not infer an adjustment reagent or add an unsupported preparation protocol.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/Complete_Medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/complete_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch071/record06/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch071/record06/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch071/record06/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch071/record06/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O']; mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S']; mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53258 = sodium citrate; definition ['The trisodium salt of citric acid.']; formula ['C6H5O7.3Na']; mass ['258.069']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| nbrc1627 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| togo3059 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Current TOGO source identity, complete component paragraphs, units, stock references and comments read; exact primary collection source checked independently. Batch inputs and bare percentages are not silently normalized. |
| grounding | REVIEW_WORK/batch071/record06/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/complete_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Complete_Medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch071/record06/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer18 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer19 | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients; merge_ingredient_group | context_only | Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group retains the first concentration, flags differing values and selects the first CHEBI. It cannot establish source stages or justify collapsing independent supplemental and product-contained components. |
| writer20 | scripts/import_from_culturebotht.py; CultureBotHTImporter.transform_medium; infer_category; import_file | context_only | Current CultureBotHTImporter.transform_medium shallow-copies input data, maps medium types, uses infer_category only when category is missing, appends a generic repository source URL and an actual timestamped import event, and flags missing primary terms. It does not independently verify ingredient identity or source quantities. import_file serializes the transformed record; historical execution is not established by this read. |
| writer21 | scripts/migrate_solutions_from_ingredients.py; _is_solution; _resolve_solution; _migrate_media_file | context_only | Current _is_solution uses name patterns, _resolve_solution keeps concentrations while creating empty reference stubs or matching a name-indexed solution, and _migrate_media_file appends those solutions and history. It does not reconstruct nested source batches or authenticate copied unit/basis. |
| writer22 | scripts/repair_merged_duplicates.py; repair_ingredient; repair_record | context_only | Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS duplicate notes. This bounded repair is not a general solution for product decomposition, stock flattening or differing source formulations. |
| writer23 | src/culturemech/import/togo_importer.py; _extract_primary_components; _solution_from_item; _extract_assembled_solutions; _parse_unit; _extract_preparation_steps; _convert_to_culturemech; _extract_ph | context_only | Current _extract_primary_components, _solution_from_item and _extract_assembled_solutions distinguish primary sections, nested stocks and assembled solutions. _parse_unit maps bare g/mg/ml to per-litre enum labels, while L remains L; those enum choices still require a verified source basis. _extract_preparation_steps retains comments. _convert_to_culturemech sets COMPLEX by default, and _extract_ph reads its supplied object. These present behaviors neither authenticate historical execution nor prove that all source metadata survived the old import. |
| writer24 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer25 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer26 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| quantity-inventory | REVIEW_WORK/batch071/record06/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- The sources provide no explicit final-volume instruction, stock percentage basis, iron hydrate, density or stock preparation; no final-medium conversion is inferred.
- The source recipe is not an experimental growth claim. No incubation or generic sterilization procedure is added.
- Historical report narratives and current writer behavior do not reconstruct historical source access or execution. Preserve all original history and append newly verified context using the actual current curation date.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T153314Z-complete-medium-batch071
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of complete_medium
started_at: '2026-10-28T15:21:37.128657Z'
finished_at: '2026-10-28T15:33:14.354900Z'
reviewer:
  identity: Codex independent record reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh review of existing unchanged repository records; this
    reviewer did not author or curate the selected target/owners. Historical reports
    were independently reassessed against current exact sources.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The exact NBRC1627 and TOGO M3059 sources support the retained batch ingredients
  and current magnesium heptahydrate mapping. The local water and iron-stock units
  conflict with the sources, seven matching masses lack a verified final-volume basis,
  and source pH is missing. Existing optional-agar wording and the solid branch classification
  are retained.
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
  - path: data/merge_yaml/merged/Complete_Medium.yaml
    sha256: 7041018f59ca28ce4a6912185f5f33cd62039122503a6d19669b740fb667484c
    role: target
  - path: data/normalized_yaml/bacterial/complete_medium.yaml
    sha256: f91c479b5e7bdeeb350de3a98e4425ca9a37400b0fb7bc002d85f9c6fe521448
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Complete_Medium.md
    sha256: 77d861487fc08aaee4e9484bb325656456737500441d5c2a9d1f3d747a64718b
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/complete_medium.md
    sha256: bb7f819d0b276b117c5cb048c912b532543363c9f374cc5cfd9449c31e9885f5
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
  - path: scripts/fetch_mediadive_solution_volumes.py
    sha256: 408cdfa3f5c446e8f9c32ac98d7ea8a3a36553b23c032f3b7551f6a1661fd39a
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
    role: context
  - path: scripts/import_mediadive_solutions.py
    sha256: f97db7607d76c46b75d2d2428e8a425a5735e52beb3a9c28fd0af03ab5b31aa8
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/review_komodo_concentration_evidence.py
    sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
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
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
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
  - path: src/culturemech/match/kg_media_matcher.py
    sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
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
  description: Full selected target and maintained owners, every quantity and unchanged
    claim; separately scoped source dependencies and current writers.
  selection: Authoritative batch071 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009573
targets:
- target_id: CultureMech:009573
  path: data/merge_yaml/merged/Complete_Medium.yaml
  label: complete_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/complete_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:009573
  command: just validate-schema data/merge_yaml/merged/Complete_Medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:009573
  command: just validate-strict data/merge_yaml/merged/Complete_Medium.yaml --workers
    1 --out REVIEW_WORK/batch071/record06/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:009573
  command: just validate-terms data/merge_yaml/merged/Complete_Medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:009573
  command: just validate-references data/merge_yaml/merged/Complete_Medium.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/Complete_Medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T15:33:14.348438Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 7041018f59ca28ce4a6912185f5f33cd62039122503a6d19669b740fb667484c
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/complete_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T15:33:14.348574Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: f91c479b5e7bdeeb350de3a98e4425ca9a37400b0fb7bc002d85f9c6fe521448
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch071/record06/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T15:21:38.276510Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: d4edfb0f9e58cdac2a9daf1b74e5527b42ed0355b2165d0bd3f5bc1238736cfb
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch071/record06/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T15:21:39.218194Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: b21ac17a6db49169673246e63795183579c1d257450caada5bc4773a89c42b47
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch071/record06/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T15:21:40.266346Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 6083496365431138de913bb70dd540256e14c10934f021b83f270cb7e2f5b4c1
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch071/record06/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T15:21:40.935174Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 15a4c1122a5909d429d88fba3e4bfbb6c36a129dde6e4d07aad7c298dfa8a314
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:19.100152Z'
  support: supports
  summary: OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting
    of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O'];
    mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:18.976452Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:18.205543Z'
  support: supports
  summary: OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S'];
    mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:18.205501Z'
  support: supports
  summary: OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal
    chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi32599
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:18.205445Z'
  support: supports
  summary: OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium
    salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: chebi53258
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:18.205381Z'
  support: supports
  summary: OLS current exact CHEBI:53258 = sodium citrate; definition ['The trisodium
    salt of citric acid.']; formula ['C6H5O7.3Na']; mass ['258.069']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2a35c6dc3532c2276c6b19aef0992260e14b1fc36423fa3eb812bb94f63c4371
- evidence_id: nbrc1627
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T15:24:18.205290Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0
- evidence_id: togo3059
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T15:22:09.157025Z'
  support: supports
  summary: Current TOGO source identity, complete component paragraphs, units, stock
    references and comments read; exact primary collection source checked independently.
    Batch inputs and bare percentages are not silently normalized.
  snapshot_sha256: c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch071/record06/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T15:33:14.351630Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: df08f59115e6aae08b0eb3da89eb87d35b2263b996987c6359d308738ef65a30
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/complete_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T15:33:14.351905Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: bb7f819d0b276b117c5cb048c912b532543363c9f374cc5cfd9449c31e9885f5
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Complete_Medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T15:33:14.351926Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: 77d861487fc08aaee4e9484bb325656456737500441d5c2a9d1f3d747a64718b
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch071/record06/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T15:33:14.351944Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: 58d23992b2b10732c01c7cef5f3fe6574c753b831fd0247390ff5e8e60c2ed68
- evidence_id: writer18
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T15:33:14.351996Z'
  support: context_only
  summary: Current _merge_ingredient_group collapses equal duplicate values without
    summing them and retains the first conflicting value with a flag. This behavior
    is distinct from historical summed-amount artifacts and does not authenticate
    source-specific stock or product structure.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer19
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients; merge_ingredient_group
  accessed_at: '2026-10-28T15:33:14.352018Z'
  support: context_only
  summary: Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group
    retains the first concentration, flags differing values and selects the first
    CHEBI. It cannot establish source stages or justify collapsing independent supplemental
    and product-contained components.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer20
  kind: record_content
  reference: scripts/import_from_culturebotht.py
  locator: CultureBotHTImporter.transform_medium; infer_category; import_file
  accessed_at: '2026-10-28T15:33:14.352041Z'
  support: context_only
  summary: Current CultureBotHTImporter.transform_medium shallow-copies input data,
    maps medium types, uses infer_category only when category is missing, appends
    a generic repository source URL and an actual timestamped import event, and flags
    missing primary terms. It does not independently verify ingredient identity or
    source quantities. import_file serializes the transformed record; historical execution
    is not established by this read.
  snapshot_sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
- evidence_id: writer21
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: _is_solution; _resolve_solution; _migrate_media_file
  accessed_at: '2026-10-28T15:33:14.352066Z'
  support: context_only
  summary: Current _is_solution uses name patterns, _resolve_solution keeps concentrations
    while creating empty reference stubs or matching a name-indexed solution, and
    _migrate_media_file appends those solutions and history. It does not reconstruct
    nested source batches or authenticate copied unit/basis.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer22
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_ingredient; repair_record
  accessed_at: '2026-10-28T15:33:14.352087Z'
  support: context_only
  summary: Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS
    duplicate notes. This bounded repair is not a general solution for product decomposition,
    stock flattening or differing source formulations.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer23
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components; _solution_from_item; _extract_assembled_solutions;
    _parse_unit; _extract_preparation_steps; _convert_to_culturemech; _extract_ph
  accessed_at: '2026-10-28T15:33:14.352127Z'
  support: context_only
  summary: Current _extract_primary_components, _solution_from_item and _extract_assembled_solutions
    distinguish primary sections, nested stocks and assembled solutions. _parse_unit
    maps bare g/mg/ml to per-litre enum labels, while L remains L; those enum choices
    still require a verified source basis. _extract_preparation_steps retains comments.
    _convert_to_culturemech sets COMPLEX by default, and _extract_ph reads its supplied
    object. These present behaviors neither authenticate historical execution nor
    prove that all source metadata survived the old import.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer24
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T15:33:14.352148Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer25
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T15:33:14.352167Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer26
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T15:33:14.352187Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch071/record06/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T15:33:14.354829Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: a8983b3605c7d54fd9c92a3b35bf9823bc619d5a9de21f9282c34cc724ae0f9f
assessments:
- assessment_id: a1
  area: identity
  topic: Exact source and classification
  outcome: supported
  summary: The source identity is TOGO M3059 / NBRC1627 Complete Medium, with the
    same nine batch ingredients. Casein and yeast extract support the existing COMPLEX/UNDEFINED
    classification. SOLID_AGAR is valid for the optional agar branch, whose qualifier
    is already retained. No organism is named by the exact formulation sources.
  target_ids:
  - CultureMech:009573
  evidence_ids:
  - nbrc1627
  - togo3059
  - local0
  - local1
- assessment_id: a2
  area: evidence
  topic: Preparation and biological evidence
  outcome: unknown
  summary: The official source has no preparation or incubation protocol beyond its
    composition and pH. No generic autoclaving, atmosphere, strain or growth result
    is supplied or inferred. Existing general cultivation applications do not constitute
    experimental growth evidence.
  target_ids:
  - CultureMech:009573
  evidence_ids:
  - nbrc1627
  - togo3059
- assessment_id: a3
  area: grounding
  topic: Current supplied forms and retained repairs
  outcome: supported
  summary: Both current primary and secondary magnesium slots correctly assert heptahydrate
    CHEBI:31795, matching the explicit source form; the historical primary repair
    is credited. All asserted CHEBI labels match current OLS. Generic sodium citrate
    does not establish hydration, and the bare FeSO4 stock designation does not establish
    a hydrate. Casein, yeast extract, agar and the stock remain without forced pure-compound
    mappings. Exact CSV aliases can contain differing hydrate labels; their presence
    does not override the source and current authority.
  target_ids:
  - CultureMech:009573
  evidence_ids:
  - chebi31795
  - chebi53258
  - grounding
  - nbrc1627
- assessment_id: a4
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: The complete current history retains import, grounding, naming and heptahydrate-repair
    events. Both October reports checked zero external source references and do not
    authenticate historical retrieval. Current TOGO parsing and source metadata explain
    possible unit/basis and pH loss risks without proving the historical execution
    path. Current conservative merging preserves scientific fields and rejects incompatible
    formulations. Inspected writer behavior is described separately by exact file
    and function; it does not prove historical execution.
  target_ids:
  - CultureMech:009573
  evidence_ids:
  - history-auth
  - writer18
  - writer19
  - writer20
  - writer21
  - writer22
  - writer23
  - writer24
  - writer25
  - writer26
- assessment_id: a5
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 18 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:009573
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:009573",
    "selected_concentration_field_count": 18, "selected_concentration_fields_covered":
    18, "decisions": [{"decision_id": "q1", "subject": "Distilled water", "local_fields":
    [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path":
    "ingredients[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path":
    "ingredients[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "NBRC1627 batch input and TOGO M3059 counterpart",
    "interpretation": "Both exact sources specify 1 L of distilled water, whereas
    both local layers encode 1 G_PER_L. Retain the explicit solvent input as volume.
    Listed water is not a measured final batch volume; neither density conversion
    nor 1000 g/L is inferred.", "sources": [{"locator": "HTML tr[11]", "source_key":
    "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627",
    "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0",
    "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6",
    "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "Distilled
    water\n1\nL", "quote_representation": "HTML tr[11] DOM text"}, {"locator": "$.components[0].items[0]",
    "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059",
    "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\":
    \"Solvating media\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q2", "subject": "MgSO4·7H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path":
    "ingredients[1].concentration", "original": {"value": "10", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path":
    "ingredients[1].concentration", "original": {"value": "10", "unit": "G_PER_L"}}],
    "decision": "unsupported", "stage": "NBRC1627 batch input and TOGO M3059 counterpart",
    "interpretation": "The source explicitly gives 10 g for this batch input, and
    the local numeric value matches. The stored G_PER_L denominator is not established:
    1 L is a water input, with a separate liquid stock addition and no make-up-to-final-volume
    instruction. Preserve the source batch mass rather than asserting a final concentration.",
    "sources": [{"locator": "HTML tr[7]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627",
    "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0",
    "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6",
    "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "MgSO\n4\n·7H\n2\nO\n10\ng",
    "quote_representation": "HTML tr[7] DOM text"}, {"locator": "$.components[0].items[1]",
    "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059",
    "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\":
    \"MgSO4·7H2O\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\":
    \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q3", "subject": "Yeast extract", "local_fields":
    [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path":
    "ingredients[2].concentration", "original": {"value": "10", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path":
    "ingredients[2].concentration", "original": {"value": "10", "unit": "G_PER_L"}}],
    "decision": "unsupported", "stage": "NBRC1627 batch input and TOGO M3059 counterpart",
    "interpretation": "The source explicitly gives 10 g for this batch input, and
    the local numeric value matches. The stored G_PER_L denominator is not established:
    1 L is a water input, with a separate liquid stock addition and no make-up-to-final-volume
    instruction. Preserve the source batch mass rather than asserting a final concentration.",
    "sources": [{"locator": "HTML tr[5]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627",
    "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0",
    "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6",
    "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "Yeast extract\n10\ng",
    "quote_representation": "HTML tr[5] DOM text"}, {"locator": "$.components[0].items[2]",
    "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059",
    "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\":
    \"Yeast extract\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\":
    \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q4", "subject": "NaCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path":
    "ingredients[3].concentration", "original": {"value": "150", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path":
    "ingredients[3].concentration", "original": {"value": "150", "unit": "G_PER_L"}}],
    "decision": "unsupported", "stage": "NBRC1627 batch input and TOGO M3059 counterpart",
    "interpretation": "The source explicitly gives 150 g for this batch input, and
    the local numeric value matches. The stored G_PER_L denominator is not established:
    1 L is a water input, with a separate liquid stock addition and no make-up-to-final-volume
    instruction. Preserve the source batch mass rather than asserting a final concentration.",
    "sources": [{"locator": "HTML tr[10]", "source_key": "nbrc1627", "reference":
    "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627", "source_raw_sha256":
    "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0", "source_text_sha256":
    "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6", "accessed_at":
    "2026-10-28T15:24:18.205290Z", "exact_source_quote": "NaCl\n150\ng", "quote_representation":
    "HTML tr[10] DOM text"}, {"locator": "$.components[0].items[3]", "source_key":
    "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059",
    "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\":
    \"NaCl\",\n          \"volume\": 150,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\":
    \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q5", "subject": "KCl", "local_fields": [{"record_path":
    "data/merge_yaml/merged/Complete_Medium.yaml", "field_path": "ingredients[4].concentration",
    "original": {"value": "2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC1627 batch input and TOGO
    M3059 counterpart", "interpretation": "The source explicitly gives 2 g for this
    batch input, and the local numeric value matches. The stored G_PER_L denominator
    is not established: 1 L is a water input, with a separate liquid stock addition
    and no make-up-to-final-volume instruction. Preserve the source batch mass rather
    than asserting a final concentration.", "sources": [{"locator": "HTML tr[8]",
    "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627",
    "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0",
    "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6",
    "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "KCl\n2\ng",
    "quote_representation": "HTML tr[8] DOM text"}, {"locator": "$.components[0].items[4]",
    "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059",
    "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\":
    \"KCl\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\":
    \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q6", "subject": "Sodium citrate", "local_fields":
    [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path":
    "ingredients[5].concentration", "original": {"value": "3", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path":
    "ingredients[5].concentration", "original": {"value": "3", "unit": "G_PER_L"}}],
    "decision": "unsupported", "stage": "NBRC1627 batch input and TOGO M3059 counterpart",
    "interpretation": "The source explicitly gives 3 g for this batch input, and the
    local numeric value matches. The stored G_PER_L denominator is not established:
    1 L is a water input, with a separate liquid stock addition and no make-up-to-final-volume
    instruction. Preserve the source batch mass rather than asserting a final concentration.",
    "sources": [{"locator": "HTML tr[6]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627",
    "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0",
    "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6",
    "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "Sodium citrate\n3\ng",
    "quote_representation": "HTML tr[6] DOM text"}, {"locator": "$.components[0].items[5]",
    "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059",
    "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\":
    \"Sodium citrate\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001109\",\n          \"gmo_id\": \"GMO_001109\",\n          \"label\":
    \"Sodium citrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q7", "subject": "4.98% FeSO4", "local_fields":
    [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path":
    "ingredients[6].concentration", "original": {"value": "1", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path":
    "ingredients[6].concentration", "original": {"value": "1", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "NBRC1627 batch input and TOGO M3059 counterpart",
    "interpretation": "Both sources specify 1 ml of the separately named 4.98% FeSO4
    solution. Local 1 G_PER_L confuses the liquid receiving dose with solute mass
    concentration. Preserve the source stock identity and explicit aliquot; percentage
    basis, stock preparation, hydrate and final medium denominator remain unspecified.",
    "sources": [{"locator": "HTML tr[9]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627",
    "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0",
    "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6",
    "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "4.98% FeSO\n4\n1\nml",
    "quote_representation": "HTML tr[9] DOM text"}, {"locator": "$.components[0].items[6]",
    "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059",
    "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\":
    \"4.98% FeSO4\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001393\",\n          \"gmo_id\": \"GMO_001393\",\n          \"label\":
    \"Iron(II) sulfate solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\":
    \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q8", "subject": "Casein", "local_fields":
    [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path":
    "ingredients[7].concentration", "original": {"value": "7.5", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path":
    "ingredients[7].concentration", "original": {"value": "7.5", "unit": "G_PER_L"}}],
    "decision": "unsupported", "stage": "NBRC1627 batch input and TOGO M3059 counterpart",
    "interpretation": "The source explicitly gives 7.5 g for this batch input, and
    the local numeric value matches. The stored G_PER_L denominator is not established:
    1 L is a water input, with a separate liquid stock addition and no make-up-to-final-volume
    instruction. Preserve the source batch mass rather than asserting a final concentration.",
    "sources": [{"locator": "HTML tr[4]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627",
    "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0",
    "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6",
    "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "Casein\n7.5\ng",
    "quote_representation": "HTML tr[4] DOM text"}, {"locator": "$.components[0].items[7]",
    "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059",
    "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\":
    \"Casein\",\n          \"volume\": 7.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001531\",\n          \"gmo_id\": \"GMO_001531\",\n          \"label\":
    \"Casein\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\":
    \"Nitrogen source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q9", "subject": "Agar (if needed)", "local_fields":
    [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path":
    "ingredients[8].concentration", "original": {"value": "15", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path":
    "ingredients[8].concentration", "original": {"value": "15", "unit": "G_PER_L"}}],
    "decision": "unsupported", "stage": "NBRC1627 batch input and TOGO M3059 counterpart",
    "interpretation": "The source explicitly gives 15 g for this batch input, and
    the local numeric value matches. The stored G_PER_L denominator is not established:
    1 L is a water input, with a separate liquid stock addition and no make-up-to-final-volume
    instruction. Preserve the source batch mass rather than asserting a final concentration.
    Agar is optional in both sources; SOLID_AGAR is valid for the selected solid branch,
    and the retained preferred_term already preserves if needed.", "sources": [{"locator":
    "HTML tr[12]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627",
    "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0",
    "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6",
    "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "Agar (if
    needed)\n15\ng", "quote_representation": "HTML tr[12] DOM text"}, {"locator":
    "$.components[0].items[8]", "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059",
    "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\":
    \"Agar (if needed)\",\n          \"volume\": 15,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001007\",\n          \"gmo_id\": \"GMO_001007\",\n          \"label\":
    \"Agar\",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000048\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000048\",\n              \"label\":
    \"Solidifying component\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q10", "subject": "4.98% stock identity",
    "local_fields": [{"record_path": "data/merge_yaml/merged/Complete_Medium.yaml",
    "field_path": "ingredients[6].preferred_term", "original": "4.98% FeSO4"}, {"record_path":
    "data/normalized_yaml/bacterial/complete_medium.yaml", "field_path": "ingredients[6].preferred_term",
    "original": "4.98% FeSO4"}], "decision": "evidence_only", "stage": "Undetermined
    percentage basis of the separate iron stock", "interpretation": "The existing
    stock label retains the literal 4.98% FeSO4 designation. Neither source specifies
    w/v, w/w, a hydrate, stock final volume or density. Retain this identity without
    deriving solute mass or final-medium molarity.", "sources": [{"locator": "HTML
    tr[9]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627",
    "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0",
    "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6",
    "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "4.98% FeSO\n4\n1\nml",
    "quote_representation": "HTML tr[9] DOM text"}, {"locator": "$.components[0].items[6]",
    "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059",
    "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\":
    \"4.98% FeSO4\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001393\",\n          \"gmo_id\": \"GMO_001393\",\n          \"label\":
    \"Iron(II) sulfate solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\":
    \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q11", "subject": "Source pH", "local_fields":
    [], "decision": "add", "stage": "Medium pH stated by the exact source", "interpretation":
    "Both NBRC1627 and TOGO M3059 state pH 7.0. Neither local layer records it. This
    is source pH, without an inferred adjustment reagent, temperature, timing or sterilization
    protocol.", "sources": [{"locator": "HTML tr[13]", "source_key": "nbrc1627", "reference":
    "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627", "source_raw_sha256":
    "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0", "source_text_sha256":
    "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6", "accessed_at":
    "2026-10-28T15:24:18.205290Z", "exact_source_quote": "pH 7.0", "quote_representation":
    "HTML tr[13] DOM text"}, {"locator": "$.comments[0]", "source_key": "togo3059",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059",
    "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n      \"paragraph_index\":
    2,\n      \"comment\": \"pH 7.0\"\n    }", "quote_representation": "raw JSON object"}]},
    {"decision_id": "q12", "subject": "Optional solid branch", "local_fields": [{"record_path":
    "data/merge_yaml/merged/Complete_Medium.yaml", "field_path": "ingredients[8].preferred_term",
    "original": "Agar (if needed)"}, {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml",
    "field_path": "ingredients[8].preferred_term", "original": "Agar (if needed)"},
    {"record_path": "data/merge_yaml/merged/Complete_Medium.yaml", "field_path": "physical_state",
    "original": "SOLID_AGAR"}, {"record_path": "data/normalized_yaml/bacterial/complete_medium.yaml",
    "field_path": "physical_state", "original": "SOLID_AGAR"}], "decision": "evidence_only",
    "stage": "Optional agar branch", "interpretation": "The retained if needed wording
    is correct. SOLID_AGAR describes the agar-containing branch; do not call it a
    classification error. Preserve the optional liquid alternative without transferring
    an unrelated formula or claiming a growth result.", "sources": [{"locator": "HTML
    tr[12]", "source_key": "nbrc1627", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1627",
    "source_raw_sha256": "e896741e1070d27f56a2f806f1cea5b734d925385cbfbe4958730344293a58c0",
    "source_text_sha256": "776bad9c03c40d0f6d53b9e23071a74ddd399668c409ef7492011bbcd43b01c6",
    "accessed_at": "2026-10-28T15:24:18.205290Z", "exact_source_quote": "Agar (if
    needed)\n15\ng", "quote_representation": "HTML tr[12] DOM text"}, {"locator":
    "$.components[0].items[8]", "source_key": "togo3059", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3059",
    "source_raw_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "source_text_sha256": "c7c8d3b73b353caaeebb95b5bbec480674567eb42408158b7a16dc0f8c17a8d1",
    "accessed_at": "2026-10-28T15:22:09.157025Z", "exact_source_quote": "{\n          \"component_name\":
    \"Agar (if needed)\",\n          \"volume\": 15,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001007\",\n          \"gmo_id\": \"GMO_001007\",\n          \"label\":
    \"Agar\",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000048\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000048\",\n              \"label\":
    \"Solidifying component\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch071/record06/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a6
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: supported
  summary: 'data/merge_yaml/merged/Complete_Medium.yaml: primary 5/9, secondary 5/9;
    data/normalized_yaml/bacterial/complete_medium.yaml: primary 5/9, secondary 5/9.
    These are ingredient-instance linkage fractions, not accuracy scores. Solution
    terms are audited separately. Every actually asserted CHEBI term is joined to
    its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech
    mentions occur across the complete selected documents, with exact locators in
    the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product
    components are not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:009573
  evidence_ids:
  - grounding
- assessment_id: a7
  area: scope
  topic: Scope and source limits
  outcome: supported
  summary: Complete selected target and exact maintained owners reviewed. Dependencies
    transfer only their explicitly named stock subsection; unrelated parent media
    and source prescriptions are not growth evidence.
  target_ids:
  - CultureMech:009573
  evidence_ids:
  - local0
- assessment_id: a8
  area: schema
  topic: Native structural checks
  outcome: supported
  summary: All four canonical commands passed once; strict schema TSV contains only
    its header and reference validation checked zero references on the generated target.
    This does not certify quantities or chemical forms.
  target_ids:
  - CultureMech:009573
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-009573-liquid-inputs-misrepresented-as-mass
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water and iron-stock aliquot use mass-rate units
  description: Both layers encode the water input and the iron-stock aliquot as G_PER_L,
    contradicting the explicit L and ml units in both exact sources. The stock percentage
    and its receiving aliquot are different quantities, and the source does not establish
    a final-medium solute concentration.
  target_ids:
  - CultureMech:009573
  field_paths:
  - ingredients[0].concentration
  - ingredients[6].concentration
  - ingredients[6].preferred_term
  evidence_ids:
  - nbrc1627
  - togo3059
  rule_id: review-yaml-record/source-quantity-unit-and-stage
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/complete_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-009573-unsupported-final-volume-denominator
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Matching batch masses have unsupported per-litre denominators
  description: Seven retained numeric masses match the source batch inputs, but the
    exact sources list water and a separate liquid addition without an explicit final-volume
    instruction. Therefore the local G_PER_L basis is unverified even where the digits
    agree; it is not a demonstrated error in the source masses. No claim-level evidence
    currently records these stage boundaries.
  target_ids:
  - CultureMech:009573
  field_paths:
  - ingredients[1].concentration
  - ingredients[2].concentration
  - ingredients[3].concentration
  - ingredients[4].concentration
  - ingredients[5].concentration
  - ingredients[7].concentration
  - ingredients[8].concentration
  - evidence
  evidence_ids:
  - nbrc1627
  - togo3059
  rule_id: review-yaml-record/explicit-volume-basis
  native_severity: P2
  normalization_reason: Custom P2 quantity-basis concern normalized to major because
    seven fields assert an unsupported final-volume denominator. The matching source
    batch masses are expressly credited; this is not native P2.3 physical-state attribution.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/complete_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-009573-source-ph-missing
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Source pH is absent from both current layers
  description: NBRC1627 and TOGO M3059 both state pH 7.0, while the selected target
    and maintained owner have no pH field. The source does not give a preparation
    or adjustment procedure.
  target_ids:
  - CultureMech:009573
  field_paths:
  - ph_value
  - evidence
  evidence_ids:
  - nbrc1627
  - togo3059
  rule_id: review-yaml-record/source-completeness
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/complete_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Restore explicit source solvent volume and liquid-stock dose with source-scoped
    evidence. Keep the iron-stock percentage basis and chemical form unresolved unless
    separately verified; do not substitute water density or infer final-medium iron
    mass.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009573
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/complete_medium.yaml
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
  description: Preserve all explicit batch masses and optional agar context. Withdraw
    or qualify unsupported final-volume normalization, and attach exact source excerpts
    at the represented quantity/stage. Do not calculate a replacement final denominator
    from nominal water plus stock volume.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009573
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/complete_medium.yaml
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
  description: Add the exact source pH with a claim-scoped excerpt and preserve its
    limited context. Do not infer an adjustment reagent or add an unsupported preparation
    protocol.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009573
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/complete_medium.yaml
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
- The sources provide no explicit final-volume instruction, stock percentage basis,
  iron hydrate, density or stock preparation; no final-medium conversion is inferred.
- The source recipe is not an experimental growth claim. No incubation or generic
  sterilization procedure is added.
- Historical report narratives and current writer behavior do not reconstruct historical
  source access or execution. Preserve all original history and append newly verified
  context using the actual current curation date.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
