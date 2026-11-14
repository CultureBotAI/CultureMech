# Scientific review of chryspyg

- Review: 20261028T143845Z-chryspyg-batch070
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T14:31:11.978065Z
- Finished UTC: 2026-10-28T14:38:45.862891Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

ChrysPYG matches NBRC907 in ingredient identity and batch numerals, but water has the wrong quantity kind and five per-litre denominators lack a final-volume instruction. Complex solid state is supported. Documented fungal use warrants a bounded category review; primary pH and preparation remain unknown.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch070 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008263 | data/merge_yaml/merged/ChrysPYG.yaml | generated | chryspyg |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008263 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:008263 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:008263 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:008263 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact source and maintained ownership

identity: supported. Targets: CultureMech:008263.

The generated target and sole maintained owner identify TOGO M1701, NBRC_M907 and the exact NBRC907 URL. Fresh TOGO metadata and official NBRC catalogue agree on ChrysPYG and all six batch components. All scientific fields of target and owner are equal; the target adds generated merge provenance.

### Source silence and retained complex composition

completeness: unknown. Targets: CultureMech:008263.

Chrysalis extract, proteose peptone and yeast extract are undefined mixtures, so COMPLEX and UNDEFINED are supported; agar supports SOLID_AGAR. The primary page does not disclose pH, stock preparation, incubation or sterilization. Their absence is a source limitation, not a demonstrated missing-source instruction.

### Growth and taxonomic scope

evidence: concern. Targets: CultureMech:008263.

No selected-record growth assertion or strain identifier is present. The official NBRC33274 page documents Ophiocordyceps odonatae, Fungi, associated with medium907. This establishes a fungal use context and challenges an unqualified bacterial category, but does not establish exclusive use, experimental growth or automatic transfer of its collection conditions.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:008263.

Both full October reports were read and explicitly report zero of six claims checked; current source verification supplies the missing assessment. Existing import, enrichment and ID events are retained, and current packaged MIM rows do not recertify historical execution. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:008263.

All 12 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:008263", "selected_concentration_field_count": 12, "selected_concentration_fields_covered": 12, "decisions": [{"decision_id": "q1", "subject": "Distilled water", "local_fields": [{"record_path": "data/merge_yaml/merged/ChrysPYG.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chryspyg.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "NBRC907 batch input", "interpretation": "Both sources specify 1 L distilled water, not 1 g/L. Retain the explicit batch solvent amount; neither source states make up to a measured final 1 L.", "sources": [{"locator": "HTML tr[8]", "source_key": "nbrc907", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907", "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e", "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0", "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Distilled water\n1\nL", "quote_representation": "HTML tr[8] DOM text"}, {"locator": "$.components[0].items[0]", "source_key": "togo1701", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1701", "source_raw_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0", "source_text_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0", "accessed_at": "2026-10-28T14:31:20.279394Z", "exact_source_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q2", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/ChrysPYG.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chryspyg.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC907 batch input", "interpretation": "The source mass is 1 g for this batch. Its numeral is retained correctly, but the stored G_PER_L denominator is not established by the listed 1 L water. Preserve the source mass and unresolved final-volume basis rather than inventing a replacement final concentration.", "sources": [{"locator": "HTML tr[6]", "source_key": "nbrc907", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907", "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e", "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0", "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Yeast extract\n1\ng", "quote_representation": "HTML tr[6] DOM text"}, {"locator": "$.components[0].items[1]", "source_key": "togo1701", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1701", "source_raw_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0", "source_text_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0", "accessed_at": "2026-10-28T14:31:20.279394Z", "exact_source_quote": "{\n          \"component_name\": \"Yeast extract\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q3", "subject": "Glucose", "local_fields": [{"record_path": "data/merge_yaml/merged/ChrysPYG.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chryspyg.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC907 batch input", "interpretation": "The source mass is 1 g for this batch. Its numeral is retained correctly, but the stored G_PER_L denominator is not established by the listed 1 L water. Preserve the source mass and unresolved final-volume basis rather than inventing a replacement final concentration.", "sources": [{"locator": "HTML tr[7]", "source_key": "nbrc907", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907", "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e", "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0", "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Glucose\n1\ng", "quote_representation": "HTML tr[7] DOM text"}, {"locator": "$.components[0].items[2]", "source_key": "togo1701", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1701", "source_raw_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0", "source_text_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0", "accessed_at": "2026-10-28T14:31:20.279394Z", "exact_source_quote": "{\n          \"component_name\": \"Glucose\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001815\",\n          \"gmo_id\": \"GMO_001815\",\n          \"label\": \"Glucose\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q4", "subject": "Agar", "local_fields": [{"record_path": "data/merge_yaml/merged/ChrysPYG.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "15", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chryspyg.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "15", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC907 batch input", "interpretation": "The source mass is 15 g for this batch. Its numeral is retained correctly, but the stored G_PER_L denominator is not established by the listed 1 L water. Preserve the source mass and unresolved final-volume basis rather than inventing a replacement final concentration.", "sources": [{"locator": "HTML tr[9]", "source_key": "nbrc907", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907", "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e", "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0", "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Agar\n15\ng", "quote_representation": "HTML tr[9] DOM text"}, {"locator": "$.components[0].items[3]", "source_key": "togo1701", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1701", "source_raw_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0", "source_text_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0", "accessed_at": "2026-10-28T14:31:20.279394Z", "exact_source_quote": "{\n          \"component_name\": \"Agar\",\n          \"volume\": 15,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001007\",\n          \"gmo_id\": \"GMO_001007\",\n          \"label\": \"Agar\",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000048\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000048\",\n              \"label\": \"Solidifying component\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "Proteose peptone", "local_fields": [{"record_path": "data/merge_yaml/merged/ChrysPYG.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chryspyg.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC907 batch input", "interpretation": "The source mass is 1 g for this batch. Its numeral is retained correctly, but the stored G_PER_L denominator is not established by the listed 1 L water. Preserve the source mass and unresolved final-volume basis rather than inventing a replacement final concentration.", "sources": [{"locator": "HTML tr[5]", "source_key": "nbrc907", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907", "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e", "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0", "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Proteose peptone\n1\ng", "quote_representation": "HTML tr[5] DOM text"}, {"locator": "$.components[0].items[4]", "source_key": "togo1701", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1701", "source_raw_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0", "source_text_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0", "accessed_at": "2026-10-28T14:31:20.279394Z", "exact_source_quote": "{\n          \"component_name\": \"Proteose peptone\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001185\",\n          \"gmo_id\": \"GMO_001185\",\n          \"label\": \"Proteose peptone\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject": "Chrysalis extract", "local_fields": [{"record_path": "data/merge_yaml/merged/ChrysPYG.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chryspyg.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC907 batch input", "interpretation": "The source mass is 1 g for this batch. Its numeral is retained correctly, but the stored G_PER_L denominator is not established by the listed 1 L water. Preserve the source mass and unresolved final-volume basis rather than inventing a replacement final concentration.", "sources": [{"locator": "HTML tr[4]", "source_key": "nbrc907", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907", "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e", "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0", "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Chrysalis extract\n1\ng", "quote_representation": "HTML tr[4] DOM text"}, {"locator": "$.components[0].items[5]", "source_key": "togo1701", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1701", "source_raw_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0", "source_text_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0", "accessed_at": "2026-10-28T14:31:20.279394Z", "exact_source_quote": "{\n          \"component_name\": \"Chrysalis extract\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001282\",\n          \"gmo_id\": \"GMO_001282\",\n          \"label\": \"Chrysalis extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject": "Unspecified pH, temperature and preparation", "local_fields": [], "decision": "unsupported", "stage": "Source-only limits", "interpretation": "The complete NBRC907 composition is followed by an empty Comment field and TOGO has no comments. Neither specifies medium pH, sterilization, order of addition or incubation. Do not add a conventional procedure or promote the separate NBRC33274 collection temperature to a universal medium condition.", "sources": [{"locator": "HTML tr[3]", "source_key": "nbrc907", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907", "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e", "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0", "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Chrysalis extract\n1\ng\nProteose peptone\n1\ng\nYeast extract\n1\ng\nGlucose\n1\ng\nDistilled water\n1\nL\nAgar\n15\ng", "quote_representation": "HTML tr[3] DOM text"}, {"locator": "HTML tr[10]", "source_key": "nbrc907", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907", "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e", "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0", "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Comment", "quote_representation": "HTML tr[10] DOM text"}]}], "local_field_census_reference": "REVIEW_WORK/batch070/record06/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: supported. Targets: CultureMech:008263.

data/merge_yaml/merged/ChrysPYG.yaml: primary 3/6, secondary 3/6; data/normalized_yaml/bacterial/chryspyg.yaml: primary 3/6, secondary 3/6. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:008263.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:008263.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Batch masses and water volume are represented as per-litre concentrations

major / open / confirmed; issue key: culturemech-008263-batch-volume-and-concentration-basis.

Water is 1 L in both current sources, while both local layers store 1 G_PER_L. The other five component numerals agree with the source masses, but their G_PER_L basis is unsupported because listed water is not an explicit final-volume instruction. This is a unit/basis representation problem, not evidence that the five source masses are wrong.

### f2: The bacterial category omits documented fungal use

minor / open / confirmed; issue key: culturemech-008263-documented-fungal-use-category.

Both layers use category bacterial, but the exact official medium907 collection association is for Ophiocordyceps odonatae NBRC33274, explicitly classified Fungi. The medium page itself is generic, so the evidence supports correcting the categorical scope rather than claiming exclusive fungal use or a growth experiment.

### f3: Source URLs have no attached claim-level support

minor / open / confirmed; issue key: culturemech-008263-claim-level-source-evidence.

Both layers retain source URLs and import/mapping history but no attached formulation evidence. The two October reports explicitly checked zero of six concentration claims. They cannot certify the unsupported denominators.

## Recommended Actions And Acceptance Checks

### action1

Restore the explicit 1 L solvent input and the five source batch masses with clear quantity kind and basis. Leave final-medium concentrations unresolved unless an exact final-volume instruction is independently verified. Preserve all six ingredient identities and attach stage-scoped evidence.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Reconcile the maintained category with documented fungal use under the current category contract. Preserve the medium identity and avoid inventing organism growth assertions or copying collection-specific incubation conditions.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Attach exact NBRC907 and TOGO source excerpts to the corrected quantity claims at their proper schema locations. Preserve old history unchanged and append any verified corrective event with its actual current date.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/ChrysPYG.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/chryspyg.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch070/record06/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch070/record06/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch070/record06/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch070/record06/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| nbrc907 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| togo1701 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1701; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Current TOGO source identity, complete component paragraphs, units, stock references and comments read; exact primary collection source checked independently. Batch inputs and bare percentages are not silently normalized. |
| nbrc33274 | https://www.nite.go.jp/nbrc/dbrp/dataview?dataId=STNB0000000033274; raw source; exact captured text/DOM/JSON locators in quantity inventory | context_only | Official NBRC33274/IFO33274 collection identity and medium907 association read in full. The page classifies Ophiocordyceps odonatae as Fungi and records an environmental insect-associated isolation. Its 25 C collection guidance is not an experimental growth measurement or a universal ChrysPYG prescription. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O']; mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17234 = glucose; definition ['An aldohexose used as a source of energy and metabolic intermediate.']; formula ['C6H12O6']; mass ['180.156']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:2509 = agar; definition ['A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties.']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch070/record06/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chryspyg.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/ChrysPYG.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch070/record06/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer16 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer17 | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients; merge_ingredient_group | context_only | Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group retains the first concentration, flags differing values and selects the first CHEBI. It cannot establish source stages or justify collapsing independent supplemental and product-contained components. |
| writer18 | scripts/migrate_solutions_from_ingredients.py; _is_solution; _resolve_solution; _migrate_media_file | context_only | Current _is_solution uses name patterns, _resolve_solution keeps concentrations while creating empty reference stubs or matching a name-indexed solution, and _migrate_media_file appends those solutions and history. It does not reconstruct nested source batches or authenticate copied unit/basis. |
| writer19 | scripts/repair_merged_duplicates.py; repair_ingredient; repair_record | context_only | Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS duplicate notes. This bounded repair is not a general solution for product decomposition, stock flattening or differing source formulations. |
| writer20 | src/culturemech/import/togo_importer.py; _extract_primary_components; _solution_from_item; _extract_assembled_solutions; _parse_unit; _extract_preparation_steps; _convert_to_culturemech; _extract_ph | context_only | Current _extract_primary_components, _solution_from_item and _extract_assembled_solutions distinguish primary sections, nested stocks and assembled solutions. _parse_unit maps bare g/mg/ml to per-litre enum labels, while L remains L; those enum choices still require a verified source basis. _extract_preparation_steps retains comments. _convert_to_culturemech sets COMPLEX by default, and _extract_ph reads its supplied object. These present behaviors neither authenticate historical execution nor prove that all source metadata survived the old import. |
| writer21 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer22 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer23 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| quantity-inventory | REVIEW_WORK/batch070/record06/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- No final mixture volume is stated. No solvent density or additive-volume arithmetic was used.
- NBRC33274 is collection metadata, not experimental growth evidence or an instruction to apply its temperature to every use of this medium.
- The three exact current CHEBI IDs and all primary/secondary slots match OLS labels; the three complex mixtures remain appropriately unmapped. Current MIM commit 6643131b0f12ab40b66f98135245fca04027e0e9 is a present snapshot, not historical validity proof.
- Historical reports are derivative zero-source-check assessments; no historical retrieval or missing raw payload has been reconstructed.
- All four native structural checks passed once, with zero reference checks; none independently authenticates scientific quantity bases.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T143845Z-chryspyg-batch070
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of chryspyg
started_at: '2026-10-28T14:31:11.978065Z'
finished_at: '2026-10-28T14:38:45.862891Z'
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
summary: ChrysPYG matches NBRC907 in ingredient identity and batch numerals, but water
  has the wrong quantity kind and five per-litre denominators lack a final-volume
  instruction. Complex solid state is supported. Documented fungal use warrants a
  bounded category review; primary pH and preparation remain unknown.
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
  - path: data/merge_yaml/merged/ChrysPYG.yaml
    sha256: 1d462e0d21d2ba1e819771e0597a11a8cf21d3a99243b12373a1240f707cf3d3
    role: target
  - path: data/normalized_yaml/bacterial/chryspyg.yaml
    sha256: 141bdb22c368a97f0f85cb7c88267d90960d4a0847fab1b2b7428ad7764d2634
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/ChrysPYG.md
    sha256: 9f93ff86551c980f95c1b545e8af3c2b5221b3fbf2e2111fc5653ce85bee68df
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chryspyg.md
    sha256: 46a3b5b0720ad83734b9bb7df0341463c404c6405050e55721b7fbd1554e6ee0
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
  - path: scripts/import_mediadive_solutions.py
    sha256: f97db7607d76c46b75d2d2428e8a425a5735e52beb3a9c28fd0af03ab5b31aa8
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
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
  selection: Authoritative batch070 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008263
targets:
- target_id: CultureMech:008263
  path: data/merge_yaml/merged/ChrysPYG.yaml
  label: chryspyg
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chryspyg.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:008263
  command: just validate-schema data/merge_yaml/merged/ChrysPYG.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:008263
  command: just validate-strict data/merge_yaml/merged/ChrysPYG.yaml --workers 1 --out
    REVIEW_WORK/batch070/record06/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:008263
  command: just validate-terms data/merge_yaml/merged/ChrysPYG.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:008263
  command: just validate-references data/merge_yaml/merged/ChrysPYG.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/ChrysPYG.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T14:38:45.857918Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 1d462e0d21d2ba1e819771e0597a11a8cf21d3a99243b12373a1240f707cf3d3
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/chryspyg.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T14:38:45.858065Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 141bdb22c368a97f0f85cb7c88267d90960d4a0847fab1b2b7428ad7764d2634
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch070/record06/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T14:31:12.994352Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: a7cffa16ca7ae87bfef3b63515e13e0cd9082ca6ace9637c4aa520911e34c53e
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch070/record06/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T14:31:13.927909Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 734fffe3093239c9b87c47965af5a020206c8087b7709d367b543280bf256380
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch070/record06/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T14:31:14.932169Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: eb6c410eca0f30a51d2564adcbab9a5eef18c702c8cb3761072e8ee907000bc1
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch070/record06/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T14:31:15.579085Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 1158397301227e68ff2f448985e8329e0326f4d5008595cdaea2206df3becbe4
- evidence_id: nbrc907
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T14:31:20.279434Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: 46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e
- evidence_id: togo1701
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1701
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T14:31:20.279394Z'
  support: supports
  summary: Current TOGO source identity, complete component paragraphs, units, stock
    references and comments read; exact primary collection source checked independently.
    Batch inputs and bare percentages are not silently normalized.
  snapshot_sha256: 07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0
- evidence_id: nbrc33274
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/dbrp/dataview?dataId=STNB0000000033274
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T14:31:20.279339Z'
  support: context_only
  summary: Official NBRC33274/IFO33274 collection identity and medium907 association
    read in full. The page classifies Ophiocordyceps odonatae as Fungi and records
    an environmental insect-associated isolation. Its 25 C collection guidance is
    not an experimental growth measurement or a universal ChrysPYG prescription.
  snapshot_sha256: 4fa27eb99794c1516274f3f62fc491466bcfa4224e68524b1895f253f6b0b25e
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T14:31:20.279273Z'
  support: supports
  summary: OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting
    of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O'];
    mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi17234
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T14:31:20.279178Z'
  support: supports
  summary: OLS current exact CHEBI:17234 = glucose; definition ['An aldohexose used
    as a source of energy and metabolic intermediate.']; formula ['C6H12O6']; mass
    ['180.156']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T14:31:20.278886Z'
  support: supports
  summary: OLS current exact CHEBI:2509 = agar; definition ['A complex mixture of
    polysaccharides extracted from species of red algae. Its two main components are
    agarose and agaropectin. Agarose is the component responsible for the high-strength
    gelling properties of agar, while agaropectin provides the viscous properties.'];
    formula None; mass None; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch070/record06/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T14:38:45.860770Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 470db57fc15906430a5dfea21d91bdc1007f5f4ee01909a0828f19c27550f06f
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chryspyg.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T14:38:45.861074Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: 46a3b5b0720ad83734b9bb7df0341463c404c6405050e55721b7fbd1554e6ee0
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/ChrysPYG.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T14:38:45.861096Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: 9f93ff86551c980f95c1b545e8af3c2b5221b3fbf2e2111fc5653ce85bee68df
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch070/record06/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T14:38:45.861116Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: 38ee87f45a44d5140ce4e021d6a1469f485457edb3c55857d8efc40c76636a32
- evidence_id: writer16
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T14:38:45.861180Z'
  support: context_only
  summary: Current _merge_ingredient_group collapses equal duplicate values without
    summing them and retains the first conflicting value with a flag. This behavior
    is distinct from historical summed-amount artifacts and does not authenticate
    source-specific stock or product structure.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer17
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients; merge_ingredient_group
  accessed_at: '2026-10-28T14:38:45.861206Z'
  support: context_only
  summary: Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group
    retains the first concentration, flags differing values and selects the first
    CHEBI. It cannot establish source stages or justify collapsing independent supplemental
    and product-contained components.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer18
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: _is_solution; _resolve_solution; _migrate_media_file
  accessed_at: '2026-10-28T14:38:45.861238Z'
  support: context_only
  summary: Current _is_solution uses name patterns, _resolve_solution keeps concentrations
    while creating empty reference stubs or matching a name-indexed solution, and
    _migrate_media_file appends those solutions and history. It does not reconstruct
    nested source batches or authenticate copied unit/basis.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer19
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_ingredient; repair_record
  accessed_at: '2026-10-28T14:38:45.861262Z'
  support: context_only
  summary: Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS
    duplicate notes. This bounded repair is not a general solution for product decomposition,
    stock flattening or differing source formulations.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer20
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components; _solution_from_item; _extract_assembled_solutions;
    _parse_unit; _extract_preparation_steps; _convert_to_culturemech; _extract_ph
  accessed_at: '2026-10-28T14:38:45.861306Z'
  support: context_only
  summary: Current _extract_primary_components, _solution_from_item and _extract_assembled_solutions
    distinguish primary sections, nested stocks and assembled solutions. _parse_unit
    maps bare g/mg/ml to per-litre enum labels, while L remains L; those enum choices
    still require a verified source basis. _extract_preparation_steps retains comments.
    _convert_to_culturemech sets COMPLEX by default, and _extract_ph reads its supplied
    object. These present behaviors neither authenticate historical execution nor
    prove that all source metadata survived the old import.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer21
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T14:38:45.861331Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer22
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T14:38:45.861352Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer23
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T14:38:45.861375Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch070/record06/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T14:38:45.862839Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 6d23231e7a7ec65dc8dfa0749e450f7444c814105f20868589d6d22c96019cce
assessments:
- assessment_id: a1
  area: identity
  topic: Exact source and maintained ownership
  outcome: supported
  summary: The generated target and sole maintained owner identify TOGO M1701, NBRC_M907
    and the exact NBRC907 URL. Fresh TOGO metadata and official NBRC catalogue agree
    on ChrysPYG and all six batch components. All scientific fields of target and
    owner are equal; the target adds generated merge provenance.
  target_ids:
  - CultureMech:008263
  evidence_ids:
  - local0
  - local1
  - nbrc907
  - togo1701
- assessment_id: a2
  area: completeness
  topic: Source silence and retained complex composition
  outcome: unknown
  summary: Chrysalis extract, proteose peptone and yeast extract are undefined mixtures,
    so COMPLEX and UNDEFINED are supported; agar supports SOLID_AGAR. The primary
    page does not disclose pH, stock preparation, incubation or sterilization. Their
    absence is a source limitation, not a demonstrated missing-source instruction.
  target_ids:
  - CultureMech:008263
  evidence_ids:
  - nbrc907
  - togo1701
- assessment_id: a3
  area: evidence
  topic: Growth and taxonomic scope
  outcome: concern
  summary: No selected-record growth assertion or strain identifier is present. The
    official NBRC33274 page documents Ophiocordyceps odonatae, Fungi, associated with
    medium907. This establishes a fungal use context and challenges an unqualified
    bacterial category, but does not establish exclusive use, experimental growth
    or automatic transfer of its collection conditions.
  target_ids:
  - CultureMech:008263
  evidence_ids:
  - nbrc33274
  - local0
  - local1
- assessment_id: a4
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: Both full October reports were read and explicitly report zero of six claims
    checked; current source verification supplies the missing assessment. Existing
    import, enrichment and ID events are retained, and current packaged MIM rows do
    not recertify historical execution. Current conservative merging preserves scientific
    fields and rejects incompatible formulations. Inspected writer behavior is described
    separately by exact file and function; it does not prove historical execution.
  target_ids:
  - CultureMech:008263
  evidence_ids:
  - history-auth
  - writer16
  - writer17
  - writer18
  - writer19
  - writer20
  - writer21
  - writer22
  - writer23
- assessment_id: a5
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 12 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:008263
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:008263",
    "selected_concentration_field_count": 12, "selected_concentration_fields_covered":
    12, "decisions": [{"decision_id": "q1", "subject": "Distilled water", "local_fields":
    [{"record_path": "data/merge_yaml/merged/ChrysPYG.yaml", "field_path": "ingredients[0].concentration",
    "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chryspyg.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "NBRC907 batch input", "interpretation":
    "Both sources specify 1 L distilled water, not 1 g/L. Retain the explicit batch
    solvent amount; neither source states make up to a measured final 1 L.", "sources":
    [{"locator": "HTML tr[8]", "source_key": "nbrc907", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907",
    "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e",
    "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0",
    "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Distilled
    water\n1\nL", "quote_representation": "HTML tr[8] DOM text"}, {"locator": "$.components[0].items[0]",
    "source_key": "togo1701", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1701",
    "source_raw_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0",
    "source_text_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0",
    "accessed_at": "2026-10-28T14:31:20.279394Z", "exact_source_quote": "{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}]}, {"decision_id": "q2", "subject": "Yeast extract", "local_fields":
    [{"record_path": "data/merge_yaml/merged/ChrysPYG.yaml", "field_path": "ingredients[1].concentration",
    "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chryspyg.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC907 batch input", "interpretation":
    "The source mass is 1 g for this batch. Its numeral is retained correctly, but
    the stored G_PER_L denominator is not established by the listed 1 L water. Preserve
    the source mass and unresolved final-volume basis rather than inventing a replacement
    final concentration.", "sources": [{"locator": "HTML tr[6]", "source_key": "nbrc907",
    "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907",
    "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e",
    "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0",
    "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Yeast extract\n1\ng",
    "quote_representation": "HTML tr[6] DOM text"}, {"locator": "$.components[0].items[1]",
    "source_key": "togo1701", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1701",
    "source_raw_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0",
    "source_text_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0",
    "accessed_at": "2026-10-28T14:31:20.279394Z", "exact_source_quote": "{\n          \"component_name\":
    \"Yeast extract\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\":
    \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q3", "subject": "Glucose", "local_fields":
    [{"record_path": "data/merge_yaml/merged/ChrysPYG.yaml", "field_path": "ingredients[2].concentration",
    "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chryspyg.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC907 batch input", "interpretation":
    "The source mass is 1 g for this batch. Its numeral is retained correctly, but
    the stored G_PER_L denominator is not established by the listed 1 L water. Preserve
    the source mass and unresolved final-volume basis rather than inventing a replacement
    final concentration.", "sources": [{"locator": "HTML tr[7]", "source_key": "nbrc907",
    "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907",
    "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e",
    "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0",
    "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Glucose\n1\ng",
    "quote_representation": "HTML tr[7] DOM text"}, {"locator": "$.components[0].items[2]",
    "source_key": "togo1701", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1701",
    "source_raw_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0",
    "source_text_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0",
    "accessed_at": "2026-10-28T14:31:20.279394Z", "exact_source_quote": "{\n          \"component_name\":
    \"Glucose\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001815\",\n          \"gmo_id\": \"GMO_001815\",\n          \"label\":
    \"Glucose\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q4", "subject": "Agar", "local_fields":
    [{"record_path": "data/merge_yaml/merged/ChrysPYG.yaml", "field_path": "ingredients[3].concentration",
    "original": {"value": "15", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chryspyg.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "15", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC907 batch input", "interpretation":
    "The source mass is 15 g for this batch. Its numeral is retained correctly, but
    the stored G_PER_L denominator is not established by the listed 1 L water. Preserve
    the source mass and unresolved final-volume basis rather than inventing a replacement
    final concentration.", "sources": [{"locator": "HTML tr[9]", "source_key": "nbrc907",
    "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907",
    "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e",
    "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0",
    "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Agar\n15\ng",
    "quote_representation": "HTML tr[9] DOM text"}, {"locator": "$.components[0].items[3]",
    "source_key": "togo1701", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1701",
    "source_raw_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0",
    "source_text_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0",
    "accessed_at": "2026-10-28T14:31:20.279394Z", "exact_source_quote": "{\n          \"component_name\":
    \"Agar\",\n          \"volume\": 15,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001007\",\n          \"gmo_id\": \"GMO_001007\",\n          \"label\":
    \"Agar\",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000048\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000048\",\n              \"label\":
    \"Solidifying component\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q5", "subject": "Proteose peptone", "local_fields":
    [{"record_path": "data/merge_yaml/merged/ChrysPYG.yaml", "field_path": "ingredients[4].concentration",
    "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chryspyg.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "NBRC907 batch input", "interpretation":
    "The source mass is 1 g for this batch. Its numeral is retained correctly, but
    the stored G_PER_L denominator is not established by the listed 1 L water. Preserve
    the source mass and unresolved final-volume basis rather than inventing a replacement
    final concentration.", "sources": [{"locator": "HTML tr[5]", "source_key": "nbrc907",
    "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907",
    "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e",
    "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0",
    "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Proteose
    peptone\n1\ng", "quote_representation": "HTML tr[5] DOM text"}, {"locator": "$.components[0].items[4]",
    "source_key": "togo1701", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1701",
    "source_raw_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0",
    "source_text_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0",
    "accessed_at": "2026-10-28T14:31:20.279394Z", "exact_source_quote": "{\n          \"component_name\":
    \"Proteose peptone\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001185\",\n          \"gmo_id\": \"GMO_001185\",\n          \"label\":
    \"Proteose peptone\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q6", "subject":
    "Chrysalis extract", "local_fields": [{"record_path": "data/merge_yaml/merged/ChrysPYG.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chryspyg.yaml", "field_path":
    "ingredients[5].concentration", "original": {"value": "1", "unit": "G_PER_L"}}],
    "decision": "unsupported", "stage": "NBRC907 batch input", "interpretation": "The
    source mass is 1 g for this batch. Its numeral is retained correctly, but the
    stored G_PER_L denominator is not established by the listed 1 L water. Preserve
    the source mass and unresolved final-volume basis rather than inventing a replacement
    final concentration.", "sources": [{"locator": "HTML tr[4]", "source_key": "nbrc907",
    "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907",
    "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e",
    "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0",
    "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Chrysalis
    extract\n1\ng", "quote_representation": "HTML tr[4] DOM text"}, {"locator": "$.components[0].items[5]",
    "source_key": "togo1701", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1701",
    "source_raw_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0",
    "source_text_sha256": "07f64d1e563d543148a2bf84fdf360dc997a79fe1e94e02620cbab0c49cb11c0",
    "accessed_at": "2026-10-28T14:31:20.279394Z", "exact_source_quote": "{\n          \"component_name\":
    \"Chrysalis extract\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001282\",\n          \"gmo_id\": \"GMO_001282\",\n          \"label\":
    \"Chrysalis extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q7", "subject":
    "Unspecified pH, temperature and preparation", "local_fields": [], "decision":
    "unsupported", "stage": "Source-only limits", "interpretation": "The complete
    NBRC907 composition is followed by an empty Comment field and TOGO has no comments.
    Neither specifies medium pH, sterilization, order of addition or incubation. Do
    not add a conventional procedure or promote the separate NBRC33274 collection
    temperature to a universal medium condition.", "sources": [{"locator": "HTML tr[3]",
    "source_key": "nbrc907", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907",
    "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e",
    "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0",
    "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Chrysalis
    extract\n1\ng\nProteose peptone\n1\ng\nYeast extract\n1\ng\nGlucose\n1\ng\nDistilled
    water\n1\nL\nAgar\n15\ng", "quote_representation": "HTML tr[3] DOM text"}, {"locator":
    "HTML tr[10]", "source_key": "nbrc907", "reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=907",
    "source_raw_sha256": "46c214d7e9a986053d3c4c1c16dd52fec9b7e4c92b0a0d933129bdd014190e5e",
    "source_text_sha256": "57a791f87020af8c8c17ce71ec3267c9860e33b3e02af410bf8bbf8a1e180bb0",
    "accessed_at": "2026-10-28T14:31:20.279434Z", "exact_source_quote": "Comment",
    "quote_representation": "HTML tr[10] DOM text"}]}], "local_field_census_reference":
    "REVIEW_WORK/batch070/record06/grounding-inventory.json", "source_only_gaps_are_explicit":
    true, "note": "Batch amounts, provider normalization, stock composition, working
    dose and preparation controls are separate. No source edits or automatic curation
    performed."}'
- assessment_id: a6
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: supported
  summary: 'data/merge_yaml/merged/ChrysPYG.yaml: primary 3/6, secondary 3/6; data/normalized_yaml/bacterial/chryspyg.yaml:
    primary 3/6, secondary 3/6. These are ingredient-instance linkage fractions, not
    accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    0 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:008263
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
  - CultureMech:008263
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
  - CultureMech:008263
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-008263-batch-volume-and-concentration-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Batch masses and water volume are represented as per-litre concentrations
  description: Water is 1 L in both current sources, while both local layers store
    1 G_PER_L. The other five component numerals agree with the source masses, but
    their G_PER_L basis is unsupported because listed water is not an explicit final-volume
    instruction. This is a unit/basis representation problem, not evidence that the
    five source masses are wrong.
  target_ids:
  - CultureMech:008263
  field_paths:
  - ingredients
  evidence_ids:
  - nbrc907
  - togo1701
  rule_id: review-ingredient-concentrations/explicit-quantity-kind-and-basis
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chryspyg.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-008263-documented-fungal-use-category
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: The bacterial category omits documented fungal use
  description: Both layers use category bacterial, but the exact official medium907
    collection association is for Ophiocordyceps odonatae NBRC33274, explicitly classified
    Fungi. The medium page itself is generic, so the evidence supports correcting
    the categorical scope rather than claiming exclusive fungal use or a growth experiment.
  target_ids:
  - CultureMech:008263
  field_paths:
  - category
  evidence_ids:
  - nbrc33274
  - nbrc907
  rule_id: review-yaml-record/source-supported-category
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded category-scope
    mismatch; the ingredients and supported solid complex state are unchanged.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chryspyg.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-008263-claim-level-source-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source URLs have no attached claim-level support
  description: Both layers retain source URLs and import/mapping history but no attached
    formulation evidence. The two October reports explicitly checked zero of six concentration
    claims. They cannot certify the unsupported denominators.
  target_ids:
  - CultureMech:008263
  field_paths:
  - evidence
  - ingredients
  evidence_ids:
  - local0
  - local1
  - history0
  - history1
  rule_id: review-ingredient-concentrations/claim-evidence-traceability
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chryspyg.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Restore the explicit 1 L solvent input and the five source batch masses
    with clear quantity kind and basis. Leave final-medium concentrations unresolved
    unless an exact final-volume instruction is independently verified. Preserve all
    six ingredient identities and attach stage-scoped evidence.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008263
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chryspyg.yaml
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
  description: Reconcile the maintained category with documented fungal use under
    the current category contract. Preserve the medium identity and avoid inventing
    organism growth assertions or copying collection-specific incubation conditions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008263
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chryspyg.yaml
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
  description: Attach exact NBRC907 and TOGO source excerpts to the corrected quantity
    claims at their proper schema locations. Preserve old history unchanged and append
    any verified corrective event with its actual current date.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008263
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chryspyg.yaml
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
- No final mixture volume is stated. No solvent density or additive-volume arithmetic
  was used.
- NBRC33274 is collection metadata, not experimental growth evidence or an instruction
  to apply its temperature to every use of this medium.
- The three exact current CHEBI IDs and all primary/secondary slots match OLS labels;
  the three complex mixtures remain appropriately unmapped. Current MIM commit 6643131b0f12ab40b66f98135245fca04027e0e9
  is a present snapshot, not historical validity proof.
- Historical reports are derivative zero-source-check assessments; no historical retrieval
  or missing raw payload has been reconstructed.
- All four native structural checks passed once, with zero reference checks; none
  independently authenticates scientific quantity bases.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
