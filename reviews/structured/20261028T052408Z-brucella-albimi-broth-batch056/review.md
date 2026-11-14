# Scientific review of brucella_albimi_broth

- Review: 20261028T052408Z-brucella-albimi-broth-batch056
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T05:12:01.085097Z
- Finished UTC: 2026-10-28T05:24:08.140657Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact ATCC 1115 product branch supports the maintained water and autoclave repairs; the generated target is stale. Remaining owner work is limited to pH, claim evidence and honest batch-volume annotation. The optional scratch recipe is not substituted for the named commercial product.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch056 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008874 | data/merge_yaml/merged/Brucella_albimi_Broth.yaml | generated | brucella_albimi_broth |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008874 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:008874 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:008874 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:008874 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### ATCC 1115 and exact TOGO M2288 product branch

identity: supported. Targets: CultureMech:008874.

ATCC 1115 and M2288 identify Brucella albimi Broth and the same BD 211088 powder. The generated target has one exact normalized contributor. Complex undefined liquid classification is appropriate. The optional scratch recipe is a distinct source branch; decomposing the named product is not required.

### Organism and performance boundaries

scope: supported. Targets: CultureMech:008874.

The complete selected target and owner and the exact recipe sources name no strain or organism-specific growth experiment. Generic Microbial cultivation is a use category, not empirical growth support. No organism, incubation atmosphere, growth rate or performance claim is inferred from a medium name.

### Historical reports and current writers

provenance: concern. Targets: CultureMech:008874.

The September narrative is independently reassessed; the October target/owner concentration reports explicitly deferred source lookup rather than authenticating the quantities. Current TOGO code separates primary rows and stocks, maps mg/ml distinctly and retains comments. It still maps bare mass units to per-litre enums; _extract_ph reads a root ph key whereas these captured payloads put pH in meta. These inspected behaviors require explicit source-basis and pH review, but do not prove how the old imports ran. The current merger preserves scientific content and rejects incompatible formulations; stale generated data are not evidence that its present logic still discards these fields.

### Water identity and proprietary product

grounding: supported. Targets: CultureMech:008874.

The owner water primary and secondary CHEBI:15377 labels match current OLS and exact packaged MIM rows. The generated target lacks these already correct links. A complex commercial powder is not forced to a pure-chemical identifier. Selected documents contain no attached claim excerpts or numeric legacy MIM identifiers.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:008874.

All 4 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:008874", "selected_concentration_field_count": 4, "selected_concentration_fields_covered": 4, "decisions": [{"decision_id": "q1", "subject": "Generated water mass artifact", "local_fields": [{"record_path": "data/merge_yaml/merged/Brucella_albimi_Broth.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1000", "unit": "G_PER_L"}}], "decision": "correct", "stage": "commercial-base preparation water", "interpretation": "Current ATCC and TOGO state 1000 ml water. The generated 1000 G_PER_L is a mass-rate artifact, not an authenticated density conversion. Preserve the already repaired owner 1.0 L and regenerate.", "sources": [{"locator": "$.components[0].items[0]", "source_key": "togoM2288", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2288", "source_raw_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352", "source_text_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352", "accessed_at": "2026-10-28T05:12:24.953380Z", "exact_source_quote": "{\n          \"component_name\": \"DI Water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001695\",\n          \"gmo_id\": \"GMO_001695\",\n          \"label\": \"Deionized water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx", "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889", "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b", "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "DI Water………………………………………………..….1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject": "Maintained water volume repair", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/brucella_albimi_broth.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1.0", "unit": "L"}}, {"record_path": "data/normalized_yaml/bacterial/brucella_albimi_broth.yaml", "field_path": "ingredients[0].notes", "original": "TOGO M2288 lists 1000 ml deionized water."}], "decision": "evidence_only", "stage": "commercial-base preparation water", "interpretation": "Retain the source-faithful 1000 ml = 1 L batch-water amount. This is not proof of a measured final medium volume.", "sources": [{"locator": "$.components[0].items[0]", "source_key": "togoM2288", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2288", "source_raw_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352", "source_text_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352", "accessed_at": "2026-10-28T05:12:24.953380Z", "exact_source_quote": "{\n          \"component_name\": \"DI Water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001695\",\n          \"gmo_id\": \"GMO_001695\",\n          \"label\": \"Deionized water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx", "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889", "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b", "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "DI Water………………………………………………..….1000 ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject": "Commercial broth quantity and denominator", "local_fields": [{"record_path": "data/merge_yaml/merged/Brucella_albimi_Broth.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "28", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/brucella_albimi_broth.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "28", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/brucella_albimi_broth.yaml", "field_path": "ingredients[1].notes", "original": "TOGO M2288 lists 28 g Brucella Broth (BD 211088) per liter."}], "decision": "unsupported", "stage": "commercial-powder batch", "interpretation": "Both sources support 28 g BD 211088 with 1000 ml water. They do not explicitly make up to a measured final litre. Retain the powder identity and 28 g amount; qualify the local G_PER_L and owner per-liter note as an adopted water-batch convention rather than verified final concentration.", "sources": [{"locator": "$.components[0].items[1]", "source_key": "togoM2288", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2288", "source_raw_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352", "source_text_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352", "accessed_at": "2026-10-28T05:12:24.953380Z", "exact_source_quote": "{\n          \"component_name\": \"Brucella Broth (BD 211088)\",\n          \"volume\": 28,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002023\",\n          \"gmo_id\": \"GMO_002023\",\n          \"label\": \"BBL &amp;trade; Brucella broth (BD)\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            },\n            {\n              \"id\": \"GMO_000050\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\": \"Complex component\"\n            }\n          ],\n          \"roles\": []\n        }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx", "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889", "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b", "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Brucella Broth (BD 211088)…………………….……….28.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject": "Maintained autoclave instruction", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/brucella_albimi_broth.yaml", "field_path": "preparation_steps[0].description", "original": "Autoclave the dissolved medium at 121 C."}, {"record_path": "data/normalized_yaml/bacterial/brucella_albimi_broth.yaml", "field_path": "sterilization", "original": {"method": "AUTOCLAVE"}}], "decision": "evidence_only", "stage": "commercial broth preparation", "interpretation": "The owner correctly retains the explicit 121 °C autoclave instruction; regenerate it into the target. No holding time, pressure or incubation temperature is supplied or invented.", "sources": [{"locator": "extracted-text lines 7-7", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx", "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889", "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b", "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Autoclave at 121ºC.", "quote_representation": "captured extracted text"}, {"locator": "$.comments[3]", "source_key": "togoM2288", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2288", "source_raw_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352", "source_text_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352", "accessed_at": "2026-10-28T05:12:24.953380Z", "exact_source_quote": "{\n      \"paragraph_index\": 5,\n      \"comment\": \"Autoclave at 121ºC.\"\n    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q5", "subject": "pH metadata and scratch-branch qualification", "local_fields": [], "decision": "evidence_only", "stage": "source pH scope", "interpretation": "TOGO explicitly reports 6.8–7.2 for M2288. ATCC prints 7.0 ±0.2 beneath the optional scratch table. Add the TOGO-supported medium pH with this branch qualification; do not claim a separate manufacturer product specification was recovered.", "sources": [{"locator": "$.meta", "source_key": "togoM2288", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2288", "source_raw_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352", "source_text_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352", "accessed_at": "2026-10-28T05:12:24.953380Z", "exact_source_quote": "{\n    \"gm\": \"http://togomedium.org/medium/M2288\",\n    \"name\": \"Brucella albimi Broth\",\n    \"src_url\": \"https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx\",\n    \"ph\": \"6.8 - 7.2\"\n  }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 20-20", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx", "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889", "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b", "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "pH 7.0 +/- 0.2", "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject": "Optional scratch branch: Tryptone", "local_fields": [], "decision": "evidence_only", "stage": "alternative scratch formulation, not product decomposition", "interpretation": "Retain this printed batch amount only as an explicitly separate optional source formulation. It is not an extra ingredient of the selected commercial-powder branch and not independently verified as the current proprietary BD composition. Listed water does not establish a measured final volume.", "sources": [{"locator": "extracted-text lines 12-12", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx", "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889", "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b", "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Tryptone (Trypticase)………………………………..10.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject": "Optional scratch branch: Peptamin", "local_fields": [], "decision": "evidence_only", "stage": "alternative scratch formulation, not product decomposition", "interpretation": "Retain this printed batch amount only as an explicitly separate optional source formulation. It is not an extra ingredient of the selected commercial-powder branch and not independently verified as the current proprietary BD composition. Listed water does not establish a measured final volume.", "sources": [{"locator": "extracted-text lines 13-13", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx", "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889", "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b", "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Peptamin *(Peptone)………………………………..10.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q8", "subject": "Optional scratch branch: Dextrose", "local_fields": [], "decision": "evidence_only", "stage": "alternative scratch formulation, not product decomposition", "interpretation": "Retain this printed batch amount only as an explicitly separate optional source formulation. It is not an extra ingredient of the selected commercial-powder branch and not independently verified as the current proprietary BD composition. Listed water does not establish a measured final volume.", "sources": [{"locator": "extracted-text lines 14-14", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx", "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889", "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b", "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Dextrose……………………………………………....1.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject": "Optional scratch branch: Yeast Extract", "local_fields": [], "decision": "evidence_only", "stage": "alternative scratch formulation, not product decomposition", "interpretation": "Retain this printed batch amount only as an explicitly separate optional source formulation. It is not an extra ingredient of the selected commercial-powder branch and not independently verified as the current proprietary BD composition. Listed water does not establish a measured final volume.", "sources": [{"locator": "extracted-text lines 15-15", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx", "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889", "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b", "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Yeast Extract………………………………………….2.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject": "Optional scratch branch: NaCl", "local_fields": [], "decision": "evidence_only", "stage": "alternative scratch formulation, not product decomposition", "interpretation": "Retain this printed batch amount only as an explicitly separate optional source formulation. It is not an extra ingredient of the selected commercial-powder branch and not independently verified as the current proprietary BD composition. Listed water does not establish a measured final volume.", "sources": [{"locator": "extracted-text lines 16-16", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx", "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889", "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b", "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "NaCl…………………………………………………...5.0 g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject": "Optional scratch branch: Na2S2O5", "local_fields": [], "decision": "evidence_only", "stage": "alternative scratch formulation, not product decomposition", "interpretation": "Retain this printed batch amount only as an explicitly separate optional source formulation. It is not an extra ingredient of the selected commercial-powder branch and not independently verified as the current proprietary BD composition. Listed water does not establish a measured final volume.", "sources": [{"locator": "extracted-text lines 17-17", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx", "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889", "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b", "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Na2S2O5...…………………………………………....0.1 g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject": "Optional scratch water", "local_fields": [], "decision": "evidence_only", "stage": "alternative scratch batch", "interpretation": "The scratch branch independently lists 1000 ml water. Do not add a second litre to the commercial branch or infer volume additivity.", "sources": [{"locator": "extracted-text lines 12-22", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx", "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889", "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b", "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Tryptone (Trypticase)………………………………..10.0 g\nPeptamin *(Peptone)………………………………..10.0 g\nDextrose……………………………………………....1.0 g\nYeast Extract………………………………………….2.0 g\nNaCl…………………………………………………...5.0 g\nNa2S2O5...…………………………………………....0.1 g\nDI Water……………………………………………….1000 ml\n\npH 7.0 +/- 0.2\n\n*Peptic Digest of Animal Tissue", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch056/record04/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: supported. Targets: CultureMech:008874.

data/merge_yaml/merged/Brucella_albimi_Broth.yaml: primary 0/2, secondary 0/2; data/normalized_yaml/bacterial/brucella_albimi_broth.yaml: primary 1/2, secondary 1/2. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI/UBERON term is joined to its exact current OLS object and packaged MIM CSV rows. Zero numeric legacy MediaIngredientMech identifiers occur in the full selected documents; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Native structural checks

schema: supported. Targets: CultureMech:008874.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Generated record omits the owner’s source-backed water and preparation repairs

major / open / confirmed; issue key: culturemech-008874-stale-water-preparation.

The target retains water as 1000 G_PER_L and omits the owner’s 1.0 L water interpretation, water grounding, autoclave instruction, sterilization and source references. These maintained repairs are supported by current TOGO and ATCC; preserve them before regeneration.

### f2: The powder amount is supported but its final-volume normalization is not explicit

minor / open / confirmed; issue key: culturemech-008874-powder-batch-basis.

The source recipe specifies 28 g commercial powder and 1000 ml water. Local G_PER_L and the owner per-liter note do not distinguish this water-batch convention from a measured final litre.

### f3: Source pH metadata is missing

minor / open / confirmed; issue key: culturemech-008874-missing-ph.

TOGO M2288 reports pH 6.8–7.2; ATCC places 7.0±0.2 after the optional scratch recipe. Preserve the metadata and its source branch precisely rather than claiming an independently inspected BD specification.

### f4: Useful owner references lack claim-scoped excerpts

minor / open / confirmed; issue key: culturemech-008874-claim-evidence.

The owner already has TOGO and ATCC references, which should be retained. Neither selected layer has attached formulation or preparation claim evidence; source URLs and curation flags alone do not validate every rate. Preparation claims belong in root evidence explicitly scoped to preparation_steps[0] and its temperature; PreparationStep has no evidence slot.

## Recommended Actions And Acceptance Checks

### action1

Regenerate from the maintained owner after the remaining bounded source-basis and pH work. Preserve its existing correct water and preparation repairs.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Preserve 28 g and explicitly record the listed water-batch basis; do not silently claim a measured final volume.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Add the supported pH range with exact TOGO evidence and an explicit note about the ATCC scratch-branch placement.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Attach exact current water, powder, pH and preparation excerpts, keeping product and scratch branches separate.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/Brucella_albimi_Broth.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/brucella_albimi_broth.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch056/record04/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch056/record04/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch056/record04/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch056/record04/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| togoM2288 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2288; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current source read, including exact identity, all formulation rows, units and preparation. It establishes a formulation, not strain-specific growth. |
| atccOld | https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current source read, including exact identity, all formulation rows, units and preparation. It establishes a formulation, not strain-specific growth. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O']; mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch056/record04/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/yaml_record_review/20260922T003547Z-Brucella_albimi_Broth.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/brucella_albimi_broth.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Brucella_albimi_Broth.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| writer13 | src/culturemech/import/togo_importer.py; relevant functions named in summary | context_only | Current _extract_primary_components/_solution_from_item preserve main versus nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps retains comments. Bare units mapped to per-litre enums still require source-basis review. Current fixed code is not proof of historical execution. |
| writer14 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer15 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer16 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| quantity-inventory | REVIEW_WORK/batch056/record04/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- The primary lists water rather than an explicit measured final volume; 28 g is supported but a final-litre denominator is not independently measured.
- The ATCC pH statement follows the scratch table; TOGO separately supplies medium-level pH metadata. Product identity does not establish a manufacturer formulation or strain-specific growth.
- An ignored-inclusive filename search across the owned checkout and content search of scripts/src/tests did not locate repair_togo_literal_products_score40.py named in owner history. Current writer code is inspected context, not historical-execution proof.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T052408Z-brucella-albimi-broth-batch056
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of brucella_albimi_broth
started_at: '2026-10-28T05:12:01.085097Z'
finished_at: '2026-10-28T05:24:08.140657Z'
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
summary: The exact ATCC 1115 product branch supports the maintained water and autoclave
  repairs; the generated target is stale. Remaining owner work is limited to pH, claim
  evidence and honest batch-volume annotation. The optional scratch recipe is not
  substituted for the named commercial product.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
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
  - path: data/merge_yaml/merged/Brucella_albimi_Broth.yaml
    sha256: e716595f72c7260b503bb01fd6633926a636a0f4fc1c9b417ab78b4a7c17fcaa
    role: target
  - path: data/normalized_yaml/bacterial/brucella_albimi_broth.yaml
    sha256: 2e8e0b3e14186f298392bdb9c3f6ff874911000a6520164f34603d7120263b64
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Brucella_albimi_Broth.md
    sha256: 2e7cc8bb204b8ad77321f373fc14abe2a09859b6b2414af0d59ca50d07df8e71
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/brucella_albimi_broth.md
    sha256: bb33935678aac033237009a00b796b6ee67ab7c6e5e8fd24fc56776301a858bf
    role: context
  - path: reports/yaml_record_review/20260922T003547Z-Brucella_albimi_Broth.md
    sha256: bd4953323533321b8806114b546139cea1882b1b4c9134ef39492ec8fc05e241
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
  description: Full selected target and maintained owners, every quantity and unchanged
    claim; separately scoped source dependencies and current writers.
  selection: Authoritative batch056 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008874
targets:
- target_id: CultureMech:008874
  path: data/merge_yaml/merged/Brucella_albimi_Broth.yaml
  label: brucella_albimi_broth
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_albimi_broth.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:008874
  command: just validate-schema data/merge_yaml/merged/Brucella_albimi_Broth.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:008874
  command: just validate-strict data/merge_yaml/merged/Brucella_albimi_Broth.yaml
    --workers 1 --out REVIEW_WORK/batch056/record04/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:008874
  command: just validate-terms data/merge_yaml/merged/Brucella_albimi_Broth.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:008874
  command: just validate-references data/merge_yaml/merged/Brucella_albimi_Broth.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/Brucella_albimi_Broth.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T05:18:10.849553Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: e716595f72c7260b503bb01fd6633926a636a0f4fc1c9b417ab78b4a7c17fcaa
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/brucella_albimi_broth.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T05:18:10.849718Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 2e8e0b3e14186f298392bdb9c3f6ff874911000a6520164f34603d7120263b64
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch056/record04/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T05:12:02.330269Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 7f8c0e1749e27d9473e52dc52ca635c696f94fc41e78d1fe5391a3565bb2f8d2
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch056/record04/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T05:12:03.383939Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 115fcbcaba0174316504241cc23d328246e73770e47609d1bdfe397e5077cf34
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch056/record04/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T05:12:04.554095Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 12175e3126d008779c9e808875f386085edb8364fd9eb5b3d3d7228cfaad16c1
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch056/record04/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T05:12:05.259248Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: dd6206eb74973daf7b65f0a27c65b30caa057a78d3c3f20fb073a4566559ac85
- evidence_id: togoM2288
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2288
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T05:12:24.953380Z'
  support: supports
  summary: Complete current source read, including exact identity, all formulation
    rows, units and preparation. It establishes a formulation, not strain-specific
    growth.
  snapshot_sha256: e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352
- evidence_id: atccOld
  kind: primary_source
  reference: https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T05:12:24.953692Z'
  support: supports
  summary: Complete current source read, including exact identity, all formulation
    rows, units and preparation. It establishes a formulation, not strain-specific
    growth.
  snapshot_sha256: bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:24.953786Z'
  support: supports
  summary: OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting
    of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O'];
    mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch056/record04/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T05:18:10.851496Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: eabd980c9cb1a23b25f8de287fa7d9a32182e14a869b9918aeb4f0f51f2def82
- evidence_id: history0
  kind: prior_review
  reference: reports/yaml_record_review/20260922T003547Z-Brucella_albimi_Broth.md
  locator: entire report
  accessed_at: '2026-10-28T05:18:10.851525Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: bd4953323533321b8806114b546139cea1882b1b4c9134ef39492ec8fc05e241
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/brucella_albimi_broth.md
  locator: entire report
  accessed_at: '2026-10-28T05:18:10.851551Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: bb33935678aac033237009a00b796b6ee67ab7c6e5e8fd24fc56776301a858bf
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Brucella_albimi_Broth.md
  locator: entire report
  accessed_at: '2026-10-28T05:18:10.851571Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: 2e7cc8bb204b8ad77321f373fc14abe2a09859b6b2414af0d59ca50d07df8e71
- evidence_id: writer13
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T05:18:10.851606Z'
  support: context_only
  summary: Current _extract_primary_components/_solution_from_item preserve main versus
    nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps
    retains comments. Bare units mapped to per-litre enums still require source-basis
    review. Current fixed code is not proof of historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer14
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T05:18:10.851627Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer15
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T05:18:10.851647Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer16
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T05:18:10.851672Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch056/record04/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T05:18:10.870672Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: a30a869637bee6389ff8f72f78a01db072fcd8099271c23df70f96f65e89b3c7
assessments:
- assessment_id: a1
  area: identity
  topic: ATCC 1115 and exact TOGO M2288 product branch
  outcome: supported
  summary: ATCC 1115 and M2288 identify Brucella albimi Broth and the same BD 211088
    powder. The generated target has one exact normalized contributor. Complex undefined
    liquid classification is appropriate. The optional scratch recipe is a distinct
    source branch; decomposing the named product is not required.
  target_ids:
  - CultureMech:008874
  evidence_ids:
  - atccOld
  - togoM2288
  - local0
  - local1
- assessment_id: a2
  area: scope
  topic: Organism and performance boundaries
  outcome: supported
  summary: The complete selected target and owner and the exact recipe sources name
    no strain or organism-specific growth experiment. Generic Microbial cultivation
    is a use category, not empirical growth support. No organism, incubation atmosphere,
    growth rate or performance claim is inferred from a medium name.
  target_ids:
  - CultureMech:008874
  evidence_ids:
  - atccOld
  - togoM2288
  - local0
  - local1
- assessment_id: a3
  area: provenance
  topic: Historical reports and current writers
  outcome: concern
  summary: The September narrative is independently reassessed; the October target/owner
    concentration reports explicitly deferred source lookup rather than authenticating
    the quantities. Current TOGO code separates primary rows and stocks, maps mg/ml
    distinctly and retains comments. It still maps bare mass units to per-litre enums;
    _extract_ph reads a root ph key whereas these captured payloads put pH in meta.
    These inspected behaviors require explicit source-basis and pH review, but do
    not prove how the old imports ran. The current merger preserves scientific content
    and rejects incompatible formulations; stale generated data are not evidence that
    its present logic still discards these fields.
  target_ids:
  - CultureMech:008874
  evidence_ids:
  - local0
  - local1
  - history0
  - history1
  - history2
  - writer13
  - writer14
  - writer15
  - writer16
- assessment_id: a4
  area: grounding
  topic: Water identity and proprietary product
  outcome: supported
  summary: The owner water primary and secondary CHEBI:15377 labels match current
    OLS and exact packaged MIM rows. The generated target lacks these already correct
    links. A complex commercial powder is not forced to a pure-chemical identifier.
    Selected documents contain no attached claim excerpts or numeric legacy MIM identifiers.
  target_ids:
  - CultureMech:008874
  evidence_ids:
  - grounding
  - chebi15377
  - local0
  - local1
- assessment_id: a5
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 4 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:008874
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:008874",
    "selected_concentration_field_count": 4, "selected_concentration_fields_covered":
    4, "decisions": [{"decision_id": "q1", "subject": "Generated water mass artifact",
    "local_fields": [{"record_path": "data/merge_yaml/merged/Brucella_albimi_Broth.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "1000", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "commercial-base preparation water",
    "interpretation": "Current ATCC and TOGO state 1000 ml water. The generated 1000
    G_PER_L is a mass-rate artifact, not an authenticated density conversion. Preserve
    the already repaired owner 1.0 L and regenerate.", "sources": [{"locator": "$.components[0].items[0]",
    "source_key": "togoM2288", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2288",
    "source_raw_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352",
    "source_text_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352",
    "accessed_at": "2026-10-28T05:12:24.953380Z", "exact_source_quote": "{\n          \"component_name\":
    \"DI Water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001695\",\n          \"gmo_id\": \"GMO_001695\",\n          \"label\":
    \"Deionized water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "atccOld",
    "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx",
    "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889",
    "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b",
    "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "DI Water………………………………………………..….1000
    ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2",
    "subject": "Maintained water volume repair", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/brucella_albimi_broth.yaml", "field_path": "ingredients[0].concentration",
    "original": {"value": "1.0", "unit": "L"}}, {"record_path": "data/normalized_yaml/bacterial/brucella_albimi_broth.yaml",
    "field_path": "ingredients[0].notes", "original": "TOGO M2288 lists 1000 ml deionized
    water."}], "decision": "evidence_only", "stage": "commercial-base preparation
    water", "interpretation": "Retain the source-faithful 1000 ml = 1 L batch-water
    amount. This is not proof of a measured final medium volume.", "sources": [{"locator":
    "$.components[0].items[0]", "source_key": "togoM2288", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2288",
    "source_raw_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352",
    "source_text_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352",
    "accessed_at": "2026-10-28T05:12:24.953380Z", "exact_source_quote": "{\n          \"component_name\":
    \"DI Water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001695\",\n          \"gmo_id\": \"GMO_001695\",\n          \"label\":
    \"Deionized water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }", "quote_representation": "raw
    JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "atccOld",
    "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx",
    "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889",
    "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b",
    "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "DI Water………………………………………………..….1000
    ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3",
    "subject": "Commercial broth quantity and denominator", "local_fields": [{"record_path":
    "data/merge_yaml/merged/Brucella_albimi_Broth.yaml", "field_path": "ingredients[1].concentration",
    "original": {"value": "28", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/brucella_albimi_broth.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "28", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/brucella_albimi_broth.yaml",
    "field_path": "ingredients[1].notes", "original": "TOGO M2288 lists 28 g Brucella
    Broth (BD 211088) per liter."}], "decision": "unsupported", "stage": "commercial-powder
    batch", "interpretation": "Both sources support 28 g BD 211088 with 1000 ml water.
    They do not explicitly make up to a measured final litre. Retain the powder identity
    and 28 g amount; qualify the local G_PER_L and owner per-liter note as an adopted
    water-batch convention rather than verified final concentration.", "sources":
    [{"locator": "$.components[0].items[1]", "source_key": "togoM2288", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2288", "source_raw_sha256":
    "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352", "source_text_sha256":
    "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352", "accessed_at":
    "2026-10-28T05:12:24.953380Z", "exact_source_quote": "{\n          \"component_name\":
    \"Brucella Broth (BD 211088)\",\n          \"volume\": 28,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002023\",\n          \"gmo_id\":
    \"GMO_002023\",\n          \"label\": \"BBL &trade; Brucella broth (BD)\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            },\n            {\n              \"id\": \"GMO_000050\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\": \"Complex
    component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines
    4-4", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx",
    "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889",
    "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b",
    "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Brucella
    Broth (BD 211088)…………………….……….28.0 g", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q4", "subject": "Maintained autoclave instruction",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/brucella_albimi_broth.yaml",
    "field_path": "preparation_steps[0].description", "original": "Autoclave the dissolved
    medium at 121 C."}, {"record_path": "data/normalized_yaml/bacterial/brucella_albimi_broth.yaml",
    "field_path": "sterilization", "original": {"method": "AUTOCLAVE"}}], "decision":
    "evidence_only", "stage": "commercial broth preparation", "interpretation": "The
    owner correctly retains the explicit 121 °C autoclave instruction; regenerate
    it into the target. No holding time, pressure or incubation temperature is supplied
    or invented.", "sources": [{"locator": "extracted-text lines 7-7", "source_key":
    "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx",
    "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889",
    "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b",
    "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Autoclave
    at 121ºC.", "quote_representation": "captured extracted text"}, {"locator": "$.comments[3]",
    "source_key": "togoM2288", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2288",
    "source_raw_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352",
    "source_text_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352",
    "accessed_at": "2026-10-28T05:12:24.953380Z", "exact_source_quote": "{\n      \"paragraph_index\":
    5,\n      \"comment\": \"Autoclave at 121ºC.\"\n    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q5", "subject": "pH metadata and scratch-branch
    qualification", "local_fields": [], "decision": "evidence_only", "stage": "source
    pH scope", "interpretation": "TOGO explicitly reports 6.8–7.2 for M2288. ATCC
    prints 7.0 ±0.2 beneath the optional scratch table. Add the TOGO-supported medium
    pH with this branch qualification; do not claim a separate manufacturer product
    specification was recovered.", "sources": [{"locator": "$.meta", "source_key":
    "togoM2288", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2288",
    "source_raw_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352",
    "source_text_sha256": "e16b82cc75b97a1f65b5c9c61967a30da5afe0cc23cadefa4d657435814c7352",
    "accessed_at": "2026-10-28T05:12:24.953380Z", "exact_source_quote": "{\n    \"gm\":
    \"http://togomedium.org/medium/M2288\",\n    \"name\": \"Brucella albimi Broth\",\n    \"src_url\":
    \"https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx\",\n    \"ph\":
    \"6.8 - 7.2\"\n  }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text
    lines 20-20", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx",
    "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889",
    "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b",
    "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "pH 7.0 +/-
    0.2", "quote_representation": "captured extracted text"}]}, {"decision_id": "q6",
    "subject": "Optional scratch branch: Tryptone", "local_fields": [], "decision":
    "evidence_only", "stage": "alternative scratch formulation, not product decomposition",
    "interpretation": "Retain this printed batch amount only as an explicitly separate
    optional source formulation. It is not an extra ingredient of the selected commercial-powder
    branch and not independently verified as the current proprietary BD composition.
    Listed water does not establish a measured final volume.", "sources": [{"locator":
    "extracted-text lines 12-12", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx",
    "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889",
    "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b",
    "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Tryptone
    (Trypticase)………………………………..10.0 g", "quote_representation": "captured extracted
    text"}]}, {"decision_id": "q7", "subject": "Optional scratch branch: Peptamin",
    "local_fields": [], "decision": "evidence_only", "stage": "alternative scratch
    formulation, not product decomposition", "interpretation": "Retain this printed
    batch amount only as an explicitly separate optional source formulation. It is
    not an extra ingredient of the selected commercial-powder branch and not independently
    verified as the current proprietary BD composition. Listed water does not establish
    a measured final volume.", "sources": [{"locator": "extracted-text lines 13-13",
    "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx",
    "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889",
    "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b",
    "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Peptamin
    *(Peptone)………………………………..10.0 g", "quote_representation": "captured extracted text"}]},
    {"decision_id": "q8", "subject": "Optional scratch branch: Dextrose", "local_fields":
    [], "decision": "evidence_only", "stage": "alternative scratch formulation, not
    product decomposition", "interpretation": "Retain this printed batch amount only
    as an explicitly separate optional source formulation. It is not an extra ingredient
    of the selected commercial-powder branch and not independently verified as the
    current proprietary BD composition. Listed water does not establish a measured
    final volume.", "sources": [{"locator": "extracted-text lines 14-14", "source_key":
    "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx",
    "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889",
    "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b",
    "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Dextrose……………………………………………....1.0
    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q9",
    "subject": "Optional scratch branch: Yeast Extract", "local_fields": [], "decision":
    "evidence_only", "stage": "alternative scratch formulation, not product decomposition",
    "interpretation": "Retain this printed batch amount only as an explicitly separate
    optional source formulation. It is not an extra ingredient of the selected commercial-powder
    branch and not independently verified as the current proprietary BD composition.
    Listed water does not establish a measured final volume.", "sources": [{"locator":
    "extracted-text lines 15-15", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx",
    "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889",
    "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b",
    "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Yeast Extract………………………………………….2.0
    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q10",
    "subject": "Optional scratch branch: NaCl", "local_fields": [], "decision": "evidence_only",
    "stage": "alternative scratch formulation, not product decomposition", "interpretation":
    "Retain this printed batch amount only as an explicitly separate optional source
    formulation. It is not an extra ingredient of the selected commercial-powder branch
    and not independently verified as the current proprietary BD composition. Listed
    water does not establish a measured final volume.", "sources": [{"locator": "extracted-text
    lines 16-16", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx",
    "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889",
    "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b",
    "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "NaCl…………………………………………………...5.0
    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q11",
    "subject": "Optional scratch branch: Na2S2O5", "local_fields": [], "decision":
    "evidence_only", "stage": "alternative scratch formulation, not product decomposition",
    "interpretation": "Retain this printed batch amount only as an explicitly separate
    optional source formulation. It is not an extra ingredient of the selected commercial-powder
    branch and not independently verified as the current proprietary BD composition.
    Listed water does not establish a measured final volume.", "sources": [{"locator":
    "extracted-text lines 17-17", "source_key": "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx",
    "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889",
    "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b",
    "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Na2S2O5...…………………………………………....0.1
    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q12",
    "subject": "Optional scratch water", "local_fields": [], "decision": "evidence_only",
    "stage": "alternative scratch batch", "interpretation": "The scratch branch independently
    lists 1000 ml water. Do not add a second litre to the commercial branch or infer
    volume additivity.", "sources": [{"locator": "extracted-text lines 12-22", "source_key":
    "atccOld", "reference": "https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx",
    "source_raw_sha256": "bb1acbfa71a7323025acdf641d830e7016e10e878aecd3e4ede77cacacc5e889",
    "source_text_sha256": "94a883d5b14c66596935213ca4970248e443617dee0ea3c4ec31f7347b97309b",
    "accessed_at": "2026-10-28T05:12:24.953692Z", "exact_source_quote": "Tryptone
    (Trypticase)………………………………..10.0 g\nPeptamin *(Peptone)………………………………..10.0 g\nDextrose……………………………………………....1.0
    g\nYeast Extract………………………………………….2.0 g\nNaCl…………………………………………………...5.0 g\nNa2S2O5...…………………………………………....0.1
    g\nDI Water……………………………………………….1000 ml\n\npH 7.0 +/- 0.2\n\n*Peptic Digest of Animal
    Tissue", "quote_representation": "captured extracted text"}]}], "local_field_census_reference":
    "REVIEW_WORK/batch056/record04/grounding-inventory.json", "source_only_gaps_are_explicit":
    true, "note": "Batch amounts, provider normalization, stock composition, working
    dose and preparation controls are separate. No source edits or automatic curation
    performed."}'
- assessment_id: a6
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: supported
  summary: 'data/merge_yaml/merged/Brucella_albimi_Broth.yaml: primary 0/2, secondary
    0/2; data/normalized_yaml/bacterial/brucella_albimi_broth.yaml: primary 1/2, secondary
    1/2. These are ingredient-instance linkage fractions, not accuracy scores. Solution
    terms are audited separately. Every actually asserted CHEBI/UBERON term is joined
    to its exact current OLS object and packaged MIM CSV rows. Zero numeric legacy
    MediaIngredientMech identifiers occur in the full selected documents; NNNNNN is
    a historical placeholder, not an ID. Complex commercial/product components are
    not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:008874
  evidence_ids:
  - grounding
- assessment_id: a7
  area: schema
  topic: Native structural checks
  outcome: supported
  summary: All four canonical commands passed once; strict schema TSV contains only
    its header and reference validation checked zero references on the generated target.
    This does not certify quantities or chemical forms.
  target_ids:
  - CultureMech:008874
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-008874-stale-water-preparation
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Generated record omits the owner’s source-backed water and preparation repairs
  description: The target retains water as 1000 G_PER_L and omits the owner’s 1.0
    L water interpretation, water grounding, autoclave instruction, sterilization
    and source references. These maintained repairs are supported by current TOGO
    and ATCC; preserve them before regeneration.
  target_ids:
  - CultureMech:008874
  field_paths:
  - ingredients[0].concentration
  - ingredients[0].term
  - preparation_steps
  - sterilization
  - references
  evidence_ids:
  - local0
  - local1
  - atccOld
  - togoM2288
  rule_id: generated-record-freshness
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_albimi_broth.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-008874-powder-batch-basis
  category: quantity
  severity: minor
  status: open
  certainty: confirmed
  title: The powder amount is supported but its final-volume normalization is not
    explicit
  description: The source recipe specifies 28 g commercial powder and 1000 ml water.
    Local G_PER_L and the owner per-liter note do not distinguish this water-batch
    convention from a measured final litre.
  target_ids:
  - CultureMech:008874
  field_paths:
  - ingredients[1].concentration
  - data/normalized_yaml/bacterial/brucella_albimi_broth.yaml::ingredients[1].notes
  evidence_ids:
  - atccOld
  - togoM2288
  rule_id: source-quantity-basis
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_albimi_broth.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-008874-missing-ph
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Source pH metadata is missing
  description: TOGO M2288 reports pH 6.8–7.2; ATCC places 7.0±0.2 after the optional
    scratch recipe. Preserve the metadata and its source branch precisely rather than
    claiming an independently inspected BD specification.
  target_ids:
  - CultureMech:008874
  field_paths:
  - ph_range
  - ph_value
  evidence_ids:
  - atccOld
  - togoM2288
  rule_id: source-preparation-completeness
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_albimi_broth.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-008874-claim-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Useful owner references lack claim-scoped excerpts
  description: The owner already has TOGO and ATCC references, which should be retained.
    Neither selected layer has attached formulation or preparation claim evidence;
    source URLs and curation flags alone do not validate every rate. Preparation claims
    belong in root evidence explicitly scoped to preparation_steps[0] and its temperature;
    PreparationStep has no evidence slot.
  target_ids:
  - CultureMech:008874
  field_paths:
  - ingredients[*].evidence
  - evidence
  - references
  evidence_ids:
  - grounding
  - local1
  - atccOld
  - togoM2288
  rule_id: source-specific-formulation-fidelity
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_albimi_broth.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Regenerate from the maintained owner after the remaining bounded source-basis
    and pH work. Preserve its existing correct water and preparation repairs.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008874
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_albimi_broth.yaml
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
  description: Preserve 28 g and explicitly record the listed water-batch basis; do
    not silently claim a measured final volume.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008874
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_albimi_broth.yaml
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
  description: Add the supported pH range with exact TOGO evidence and an explicit
    note about the ATCC scratch-branch placement.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008874
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_albimi_broth.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action4
  description: Attach exact current water, powder, pH and preparation excerpts, keeping
    product and scratch branches separate.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008874
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brucella_albimi_broth.yaml
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
- The primary lists water rather than an explicit measured final volume; 28 g is supported
  but a final-litre denominator is not independently measured.
- The ATCC pH statement follows the scratch table; TOGO separately supplies medium-level
  pH metadata. Product identity does not establish a manufacturer formulation or strain-specific
  growth.
- An ignored-inclusive filename search across the owned checkout and content search
  of scripts/src/tests did not locate repair_togo_literal_products_score40.py named
  in owner history. Current writer code is inspected context, not historical-execution
  proof.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
