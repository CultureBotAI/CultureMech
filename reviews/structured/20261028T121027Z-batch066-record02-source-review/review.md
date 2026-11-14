# COOKED MEAT JCM605/TOGO M612: preserve solvent units and source context

- Review: 20261028T121027Z-batch066-record02-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T12:01:24.589325Z
- Finished UTC: 2026-10-28T12:10:27.905773Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact current JCM605, TOGO M612 and provider J605 agree on the generic medium identity. Both local layers misrepresent the source water volume as a mass concentration and omit the source pH and JCM default preparation. The two non-solvent rates are explicitly supported by the current provider and should remain unchanged with precise evidence. No organism-specific claim or recipe edit is made.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch066 native selection index 02.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010012 | data/merge_yaml/merged/COOKED_MEAT_MEDIUM.yaml | generated | cooked_meat_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010012 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:010012 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:010012 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:010012 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### JCM605 and TOGO M612 identity

identity: supported. Targets: CultureMech:010012.

The exact current JCM heading, TOGO original_media_id/source URL and J605 provider link agree. Only the maintained TOGO contributor owns this target. The two historical reports for cooked_meat_medium__5c313447 concern a different generated identity and owner; they are comparison context, not authority to collapse current unequal records.

### Commercial premix and omitted source context

completeness: concern. Targets: CultureMech:010012.

Complex/undefined composition is appropriate for the named cooked-meat premix. The current source does not identify a specific organism or establish strain-level growth; generic bacterial/application labels remain generic. Source water units, pH and preparation need explicit representation, while glucose and premix rates retain provider support. No product-code-specific composition is inferred from the Oxoid label.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:010012.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Distilled-water input", "source": [{"evidence_id": "togo612", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M612", "raw_path": "REVIEW_WORK/batch066/source01-03/togo612.bin", "raw_sha256": "aa3d9543530f9ddc12cbf1d252c5702d747f7f1d92a93716317f85b724a1872a", "locator": "$.components[0].items[0]", "accessed_at": "2026-10-28T12:04:10.608522Z", "quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo": "http://purl.jp/bio/10/gmo/GMO_001001", "gmo_id": "GMO_001001", "label": "Distilled water", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044", "label": "Solvating media"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ605", "reference": "https://mediadive.dsmz.de/rest/medium/J605", "raw_path": "REVIEW_WORK/batch066/source01-03/apiJ605.bin", "raw_sha256": "aeb40b82f4a35c55ab17c19c28207f1e89e286a31d492be15c806416f800738d", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T12:04:10.791700Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "jcm605", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=605", "raw_path": "REVIEW_WORK/batch066/source01-03/jcm605.bin", "raw_sha256": "2bd152d41eff1f489cc77ab8dd23309aca0b737e9f444efc53635f70d830513e", "locator": "Exact recipe-table water row rendered as DOM text", "accessed_at": "2026-10-28T12:04:10.732503Z", "quote": "Distilled water\n1.0\nL"}], "decision": "correct", "rationale": "Correct the dimensional representation while retaining the printed source quantity. Water identity CHEBI:15377 is supported independently of this unit error.", "layer_assessments": [{"path": "data/merge_yaml/merged/COOKED_MEAT_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source specifies 1 L water (provider 1000 ml), not 1 g/L. Preserve as solvent-volume context; no density conversion or measured-final-volume inference is justified."}, {"path": "data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source specifies 1 L water (provider 1000 ml), not 1 g/L. Preserve as solvent-volume context; no density conversion or measured-final-volume inference is justified."}]}, {"quantity_id": "q2", "topic": "Glucose", "source": [{"evidence_id": "togo612", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M612", "raw_path": "REVIEW_WORK/batch066/source01-03/togo612.bin", "raw_sha256": "aa3d9543530f9ddc12cbf1d252c5702d747f7f1d92a93716317f85b724a1872a", "locator": "$.components[0].items[1]", "accessed_at": "2026-10-28T12:04:10.608522Z", "quote": "{\n          \"component_name\": \"Glucose\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001815\",\n          \"gmo_id\": \"GMO_001815\",\n          \"label\": \"Glucose\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Glucose", "volume": 10, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001815", "gmo_id": "GMO_001815", "label": "Glucose", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}, {"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}], "roles": [{"id": "GMO_000063", "uri": "http://purl.jp/bio/10/gmo/GMO_000063", "label": "Carbon source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ605", "reference": "https://mediadive.dsmz.de/rest/medium/J605", "raw_path": "REVIEW_WORK/batch066/source01-03/apiJ605.bin", "raw_sha256": "aeb40b82f4a35c55ab17c19c28207f1e89e286a31d492be15c806416f800738d", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T12:04:10.791700Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 55.5062,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Glucose", "compound_id": 5, "amount": 10, "unit": "g", "g_l": 10, "mmol_l": 55.5062, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "jcm605", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=605", "raw_path": "REVIEW_WORK/batch066/source01-03/jcm605.bin", "raw_sha256": "2bd152d41eff1f489cc77ab8dd23309aca0b737e9f444efc53635f70d830513e", "locator": "Exact JCM605 recipe-table row", "accessed_at": "2026-10-28T12:04:10.732503Z", "quote": "Glucose\n10.0\ng"}], "decision": "evidence_only", "rationale": "Keep the source-specific nominal rate. Oxoid names a commercial complex premix, not a single chemical or a license to substitute a different product formulation.", "layer_assessments": [{"path": "data/merge_yaml/merged/COOKED_MEAT_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Unchanged rate agrees with explicit current provider g_l. Primary JCM and TOGO supply the batch mass and water input; add exact provider basis and primary identity evidence without claiming a measured final volume."}, {"path": "data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Unchanged rate agrees with explicit current provider g_l. Primary JCM and TOGO supply the batch mass and water input; add exact provider basis and primary identity evidence without claiming a measured final volume."}]}, {"quantity_id": "q3", "topic": "Cooked meat medium (Oxoid)", "source": [{"evidence_id": "togo612", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M612", "raw_path": "REVIEW_WORK/batch066/source01-03/togo612.bin", "raw_sha256": "aa3d9543530f9ddc12cbf1d252c5702d747f7f1d92a93716317f85b724a1872a", "locator": "$.components[0].items[2]", "accessed_at": "2026-10-28T12:04:10.608522Z", "quote": "{\n          \"component_name\": \"Cooked meat medium (Oxoid)\",\n          \"volume\": 55,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001538\",\n          \"gmo_id\": \"GMO_001538\",\n          \"label\": \"Oxoid &amp;trade; Cooked meat medium\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            },\n            {\n              \"id\": \"GMO_000050\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\": \"Complex component\"\n            }\n          ],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Cooked meat medium (Oxoid)", "volume": 55, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001538", "gmo_id": "GMO_001538", "label": "Oxoid &amp;trade; Cooked meat medium", "properties": [{"id": "GMO_000047", "uri": "http://purl.jp/bio/10/gmo/GMO_000047", "label": "Undefined component"}, {"id": "GMO_000050", "uri": "http://purl.jp/bio/10/gmo/GMO_000050", "label": "Complex component"}], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ605", "reference": "https://mediadive.dsmz.de/rest/medium/J605", "raw_path": "REVIEW_WORK/batch066/source01-03/apiJ605.bin", "raw_sha256": "aeb40b82f4a35c55ab17c19c28207f1e89e286a31d492be15c806416f800738d", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T12:04:10.791700Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Cooked meat medium\",\n                        \"compound_id\": 1824,\n                        \"attribute\": \"Oxoid\",\n                        \"amount\": 55,\n                        \"unit\": \"g\",\n                        \"g_l\": 55,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Cooked meat medium", "compound_id": 1824, "attribute": "Oxoid", "amount": 55, "unit": "g", "g_l": 55, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "jcm605", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=605", "raw_path": "REVIEW_WORK/batch066/source01-03/jcm605.bin", "raw_sha256": "2bd152d41eff1f489cc77ab8dd23309aca0b737e9f444efc53635f70d830513e", "locator": "Exact JCM605 recipe-table row", "accessed_at": "2026-10-28T12:04:10.732503Z", "quote": "Cooked meat medium (Oxoid)\n55.0\ng"}], "decision": "evidence_only", "rationale": "Keep the source-specific nominal rate. Oxoid names a commercial complex premix, not a single chemical or a license to substitute a different product formulation.", "layer_assessments": [{"path": "data/merge_yaml/merged/COOKED_MEAT_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "55", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Unchanged rate agrees with explicit current provider g_l. Primary JCM and TOGO supply the batch mass and water input; add exact provider basis and primary identity evidence without claiming a measured final volume."}, {"path": "data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "55", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Unchanged rate agrees with explicit current provider g_l. Primary JCM and TOGO supply the batch mass and water input; add exact provider basis and primary identity evidence without claiming a measured final volume."}]}, {"quantity_id": "q4", "topic": "Missing final pH", "source": [{"evidence_id": "jcm605", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=605", "raw_path": "REVIEW_WORK/batch066/source01-03/jcm605.bin", "raw_sha256": "2bd152d41eff1f489cc77ab8dd23309aca0b737e9f444efc53635f70d830513e", "locator": "Exact sentence following JCM605 recipe", "accessed_at": "2026-10-28T12:04:10.732503Z", "quote": "Check the final pH to be around 7.2."}, {"evidence_id": "apiJ605", "reference": "https://mediadive.dsmz.de/rest/medium/J605", "raw_path": "REVIEW_WORK/batch066/source01-03/apiJ605.bin", "raw_sha256": "aeb40b82f4a35c55ab17c19c28207f1e89e286a31d492be15c806416f800738d", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T12:04:10.791700Z", "quote": "{\n                        \"step\": \"Check the final pH to be around 7.2.\"\n                    }", "exact_decoded_object": {"step": "Check the final pH to be around 7.2."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "togo612", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M612", "raw_path": "REVIEW_WORK/batch066/source01-03/togo612.bin", "raw_sha256": "aa3d9543530f9ddc12cbf1d252c5702d747f7f1d92a93716317f85b724a1872a", "locator": "$.comments[0]", "accessed_at": "2026-10-28T12:04:10.608522Z", "quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Check the final pH to be around 7.2.\"\n    }", "exact_decoded_object": {"paragraph_index": 2, "comment": "Check the final pH to be around 7.2."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Add source pH around 7.2 as approximate source context with root evidence; do not claim an exact measured pH, unspecified adjustment reagent or measurement temperature.", "layer_assessments": []}, {"quantity_id": "q5", "topic": "Missing JCM default preparation", "source": [{"evidence_id": "jcm605", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=605", "raw_path": "REVIEW_WORK/batch066/source01-03/jcm605.bin", "raw_sha256": "2bd152d41eff1f489cc77ab8dd23309aca0b737e9f444efc53635f70d830513e", "locator": "Page-wide default preceding exact JCM605 heading", "accessed_at": "2026-10-28T12:04:10.732503Z", "quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min."}], "decision": "add", "rationale": "The exact primary page applies this default unless overridden, and 605 supplies no override. Retain its conditional default scope and original 121°C/15 min in preparation with root evidence; it is not an organism-specific optimization.", "layer_assessments": []}]

### Current ontology and MIM correspondence

grounding: supported. Targets: CultureMech:010012.

Both primary and secondary water/glucose assertions resolve to fresh canonical CHEBI:15377 and CHEBI:17234 and current exact MIM rows. Generic glucose is not upgraded to an unstated stereochemical form. Commercial cooked-meat premix remains an ungrounded mixture; no invented pure-compound ID is assigned.

### History and evidence scope

provenance: supported. Targets: CultureMech:010012.

Complete selected histories and all four matching or neighboring reports were read. Selected October reports were source-unchecked screenings; September and the other October generated report refer to CM002953, not this CM010012 lineage. No old retrieval event or forced merge recommendation is authenticated by current captures.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:010012.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:010012.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Represent source water as solvent volume

major / open / confirmed; issue key: culturemech-010012-represent-source-water-as-solvent-volume.

Both layers encode distilled water as 1 G_PER_L, although JCM605 and TOGO specify 1.0 L and current J605 supplies 1000 ml. The water identifier is correct; the concentration dimension is not. Primary solvent volume does not establish a measured final volume for the non-solvent components.

### f2: Restore source pH and scoped default preparation

major / open / confirmed; issue key: culturemech-010012-restore-source-ph-and-scoped-default-preparation.

Both layers omit the primary final-pH statement around 7.2 and JCM page-wide 121°C/15 min default. Current TOGO retains the pH comment and meta.ph but does not carry the JCM page-wide default; the current pH extractor reads a different root key. These are exact source-context omissions, not evidence for a different medium or organism.

### f3: Link supported unchanged claims and preserve historical scope

minor / open / confirmed; issue key: culturemech-010012-link-supported-unchanged-claims-and-preserve-historical-scope.

Neither layer attaches exact formulation/preparation evidence. October 5 reports expressly performed no source checks. The September review discusses a different generated identity and recommends a forced source-duplicate collapse; current owner resolution and formulation-compatibility rules require separate reassessment before any such merge.

## Recommended Actions And Acceptance Checks

### action1

Preserve the exact 1 L water input in schema-supported solvent/preparation context and remove the false water mass concentration. Keep the two explicitly provider-supported non-solvent rates with their named basis; do not calculate an unreported final volume.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Add the approximate source pH and exact conditionally applicable JCM default preparation with schema-supported root evidence and precise source locators. Preserve absence of organism-specific claims; do not infer reagent, culture duration or growth temperature.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Attach exact current JCM/TOGO/provider claims to the supported ingredient and root slots. Preserve all original histories and neighboring reports, append only verified new context, and avoid automatically applying the old two-record-collapse recommendation.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/COOKED_MEAT_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| jcm605 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=605; h2 medium605; complete recipe table and adjacent pH sentence; preceding default sterilization notice | supports | Complete primary HTML document read, including exact medium605 heading, three formulation rows, final-pH sentence and site-wide default sterilization text. The page names no organism or pathogen; generic media-name associations are not transferred. |
| togo612 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M612; Exact source identity and scoped formulation/preparation | supports | Complete current TOGO M612 object: exact JCM_M605 identifier and source URL, three component objects, meta.ph and pH comment. No organism-specific growth claim is supplied. |
| apiJ605 | https://mediadive.dsmz.de/rest/medium/J605; Exact source identity and scoped formulation/preparation | supports | Complete current J605 provider object: explicit main-stage g_l rates for glucose and Oxoid cooked-meat premix, solvent volume and pH preparation. Provider rates do not prove a measured final litre. |
| identity-search | REVIEW_WORK/batch066/record02/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition parser restricts ingredients to the primary solution, excludes solvent and recognized stock additions, and retains explicit g_l. The solution parser preserves referenced or percent-defined stocks and source attributes. Preparation parsing still concatenates all solution steps into root preparation_steps; source-stage annotation remains important. These present functions do not prove the historical execution that produced this record. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. Current behavior does not establish the historical cause of an existing discrepancy. |
| historical-1 | reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md; Exact selected-owner matching rows, if present, plus report purpose/method and validation claims only; all other pair-specific conclusions outside scope. | context_only | Historical source-duplicate report: only exact selected-owner rows, where present, and its stated signature method are in scope. Similarity does not prove complete preparation identity; no assertion about absent exact pairs is inferred. |
| historical-2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COOKED_MEAT_MEDIUM.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-3 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/cooked_meat_medium__5c313447.md; Complete neighboring report read as comparison-only context; its exact Record header is not one of this review target or maintained contributors. No quantities or conclusions transferred. | context_only | Different-record historical report, comparison-only: exact header is outside this selected lineage. No source or quantity conclusion transferred. |
| historical-4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-5 | reports/yaml_record_review/20260922T113219Z-cooked_meat_medium__5c313447.md; Complete neighboring report read as comparison-only context; its exact Record header is not one of this review target or maintained contributors. No quantities or conclusions transferred. | context_only | Different-record historical report, comparison-only: exact header is outside this selected lineage. No source or quantity conclusion transferred. |
| historical-reader | REVIEW_WORK/batch066/record02/historical-reader.json | context_only | Full exact-header historical texts and scoped large report, with literal/decoded current-source joins and explicit mismatches. Historical access events are not reauthenticated. |
| historical-plan-rows | REVIEW_WORK/batch066/record02/historical-plan-rows.json | context_only | Exact scoped plan-row membership; full parent payload retained as an inspected pin without transferring neighboring records. |
| attached-evidence-joins | REVIEW_WORK/batch066/record02/attached-evidence-joins.json | context_only | Every existing attached evidence claim is preserved and compared to the exact freshly captured response. Matching snippets do not authenticate historical access times. |
| complete-source-rows | REVIEW_WORK/batch066/record02/complete-source-rows.json | context_only | Every source recipe row and preparation object, with exact raw substring and decoded JSON locator, kept in its own solution stage. No biological recommendation follows from provider equipment metadata. |
| writer-togo | src/culturemech/import/togo_importer.py; _ingredient_from_item, _parse_unit, _extract_primary_components, _extract_ph, _extract_preparation_steps, _convert_to_culturemech | context_only | Current _ingredient_from_item preserves the supplied scalar and maps units through _parse_unit; that function now maps l to L, while g is G_PER_L. Primary-section handling avoids unrelated stock sections. _extract_ph reads root ph, whereas this source stores meta.ph, and _extract_preparation_steps reads comments but cannot import the JCM page-wide default absent from TOGO. This current code does not authenticate the historical execution. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15377; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17234; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch066/record02/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch066/record02/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch066/record02/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch066/record02/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch066/record02/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch066/record02/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch066/record02/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch066/record02/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch066/record02/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- The source supplies water input, not explicit final volume; current provider g_l is retained as its declared main-stage basis.
- The exact current JCM605/TOGO M612 context contains no organism claim. No generic Cooked Meat product association is transferred into strain-specific growth or safety assertions. Oxoid product-code and premix composition remain unspecified.
- JCM default preparation is explicitly conditional; no missing reagent, measured pH or organism-specific culture condition is invented.
- Historical reports are derivative context, not a reconstructed review or verified historical retrieval. Native reference validation performed zero checks.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T121027Z-batch066-record02-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'COOKED MEAT JCM605/TOGO M612: preserve solvent units and source context'
started_at: '2026-10-28T12:01:24.589325Z'
finished_at: '2026-10-28T12:10:27.905773Z'
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
summary: Exact current JCM605, TOGO M612 and provider J605 agree on the generic medium
  identity. Both local layers misrepresent the source water volume as a mass concentration
  and omit the source pH and JCM default preparation. The two non-solvent rates are
  explicitly supported by the current provider and should remain unchanged with precise
  evidence. No organism-specific claim or recipe edit is made.
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
  - path: data/merge_yaml/merged/COOKED_MEAT_MEDIUM.yaml
    sha256: a7742e258d75f8a0555e5ccdbd8f6d247be1adb3a559811b5e99b4c79771930a
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml
    sha256: c3e718828059b7169695b662a657864f8a29d30f4180f5fb3c662529eb37e014
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
  - path: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
    sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COOKED_MEAT_MEDIUM.md
    sha256: 56abd6913e4e9f32ac835d0aaf5df3b26196f7bca46a4d96d1e9c89620094d03
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/cooked_meat_medium__5c313447.md
    sha256: 8770e48648b6fc14ec93fb5e1bfd520081b03ddddf18ad5cb54994ce9a38c8e8
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.md
    sha256: 654eaa7b80956d931391bdc486d8237d80f59686c64e704094b13df899e5ca2d
    role: context
  - path: reports/yaml_record_review/20260922T113219Z-cooked_meat_medium__5c313447.md
    sha256: 948cf65e24b37a6459bd62275b0097be26d712ddb66f3e8d1b02863bccd476e7
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/validate_media_variant_links.py
    sha256: d18ef71320a0c50abe085e151d0d0d4d963007d1e1c9afbefab97581a983e31e
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: Full selected record and exact maintained contributors; explicitly
    scoped dependency and external-source limits retained.
  selection: Actual batch066 native selection index 02.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010012
targets:
- target_id: CultureMech:010012
  path: data/merge_yaml/merged/COOKED_MEAT_MEDIUM.yaml
  label: cooked_meat_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:010012
  command: just validate-schema data/merge_yaml/merged/COOKED_MEAT_MEDIUM.yaml
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
  - CultureMech:010012
  command: just validate-strict data/merge_yaml/merged/COOKED_MEAT_MEDIUM.yaml --out
    REVIEW_WORK/batch066/record02/strict.tsv --workers 1 --quiet
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
  - CultureMech:010012
  command: just validate-terms data/merge_yaml/merged/COOKED_MEAT_MEDIUM.yaml
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
  - CultureMech:010012
  command: just validate-references data/merge_yaml/merged/COOKED_MEAT_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/COOKED_MEAT_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T12:10:06.509495Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: a7742e258d75f8a0555e5ccdbd8f6d247be1adb3a559811b5e99b4c79771930a
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T12:10:06.509495Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: c3e718828059b7169695b662a657864f8a29d30f4180f5fb3c662529eb37e014
- evidence_id: jcm605
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=605
  locator: h2 medium605; complete recipe table and adjacent pH sentence; preceding
    default sterilization notice
  accessed_at: '2026-10-28T12:04:10.732503Z'
  support: supports
  summary: Complete primary HTML document read, including exact medium605 heading,
    three formulation rows, final-pH sentence and site-wide default sterilization
    text. The page names no organism or pathogen; generic media-name associations
    are not transferred.
  snapshot_sha256: 2bd152d41eff1f489cc77ab8dd23309aca0b737e9f444efc53635f70d830513e
- evidence_id: togo612
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M612
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T12:04:10.608522Z'
  support: supports
  summary: 'Complete current TOGO M612 object: exact JCM_M605 identifier and source
    URL, three component objects, meta.ph and pH comment. No organism-specific growth
    claim is supplied.'
  snapshot_sha256: aa3d9543530f9ddc12cbf1d252c5702d747f7f1d92a93716317f85b724a1872a
- evidence_id: apiJ605
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J605
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T12:04:10.791700Z'
  support: supports
  summary: 'Complete current J605 provider object: explicit main-stage g_l rates for
    glucose and Oxoid cooked-meat premix, solvent volume and pH preparation. Provider
    rates do not prove a measured final litre.'
  snapshot_sha256: aeb40b82f4a35c55ab17c19c28207f1e89e286a31d492be15c806416f800738d
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch066/record02/identity-search.json
  accessed_at: '2026-10-28T12:10:06.553472Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    excluded namesakes are retained in the census. Similar names and source accessions
    are not promoted to owners.
  snapshot_sha256: cbb20a5c43ea32ee3dc085ce7fa85bcc6af24769a3d691dd78c891ed12f85568
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T12:10:06.509495Z'
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
  accessed_at: '2026-10-28T12:10:06.509495Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T12:10:06.509495Z'
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
  accessed_at: '2026-10-28T12:10:06.509495Z'
  support: context_only
  summary: Current cleanup groups identical normalized names, keeps the first entry
    as a base, flags differing concentrations and combines a warning note; it does
    not sum concentrations. It can still discard distinctions when names repeat, so
    source stage must be retained. Current behavior does not establish the historical
    cause of an existing discrepancy.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: historical-1
  kind: record_content
  reference: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
  locator: Exact selected-owner matching rows, if present, plus report purpose/method
    and validation claims only; all other pair-specific conclusions outside scope.
  accessed_at: '2026-10-28T12:10:06.509495Z'
  support: context_only
  summary: 'Historical source-duplicate report: only exact selected-owner rows, where
    present, and its stated signature method are in scope. Similarity does not prove
    complete preparation identity; no assertion about absent exact pairs is inferred.'
  snapshot_sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/COOKED_MEAT_MEDIUM.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T12:10:06.509495Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 56abd6913e4e9f32ac835d0aaf5df3b26196f7bca46a4d96d1e9c89620094d03
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/cooked_meat_medium__5c313447.md
  locator: Complete neighboring report read as comparison-only context; its exact
    Record header is not one of this review target or maintained contributors. No
    quantities or conclusions transferred.
  accessed_at: '2026-10-28T12:10:06.509495Z'
  support: context_only
  summary: 'Different-record historical report, comparison-only: exact header is outside
    this selected lineage. No source or quantity conclusion transferred.'
  snapshot_sha256: 8770e48648b6fc14ec93fb5e1bfd520081b03ddddf18ad5cb54994ce9a38c8e8
- evidence_id: historical-4
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T12:10:06.509495Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 654eaa7b80956d931391bdc486d8237d80f59686c64e704094b13df899e5ca2d
- evidence_id: historical-5
  kind: record_content
  reference: reports/yaml_record_review/20260922T113219Z-cooked_meat_medium__5c313447.md
  locator: Complete neighboring report read as comparison-only context; its exact
    Record header is not one of this review target or maintained contributors. No
    quantities or conclusions transferred.
  accessed_at: '2026-10-28T12:10:06.509495Z'
  support: context_only
  summary: 'Different-record historical report, comparison-only: exact header is outside
    this selected lineage. No source or quantity conclusion transferred.'
  snapshot_sha256: 948cf65e24b37a6459bd62275b0097be26d712ddb66f3e8d1b02863bccd476e7
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch066/record02/historical-reader.json
  accessed_at: '2026-10-28T12:10:06.557225Z'
  support: context_only
  summary: Full exact-header historical texts and scoped large report, with literal/decoded
    current-source joins and explicit mismatches. Historical access events are not
    reauthenticated.
  snapshot_sha256: 6475c6e68c902c9abd965f4b54877622f135ef69f772fcca0a77d10a1076aa69
- evidence_id: historical-plan-rows
  kind: record_content
  reference: REVIEW_WORK/batch066/record02/historical-plan-rows.json
  accessed_at: '2026-10-28T12:10:06.557402Z'
  support: context_only
  summary: Exact scoped plan-row membership; full parent payload retained as an inspected
    pin without transferring neighboring records.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: attached-evidence-joins
  kind: record_content
  reference: REVIEW_WORK/batch066/record02/attached-evidence-joins.json
  accessed_at: '2026-10-28T12:10:06.557642Z'
  support: context_only
  summary: Every existing attached evidence claim is preserved and compared to the
    exact freshly captured response. Matching snippets do not authenticate historical
    access times.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: complete-source-rows
  kind: record_content
  reference: REVIEW_WORK/batch066/record02/complete-source-rows.json
  accessed_at: '2026-10-28T12:10:06.558016Z'
  support: context_only
  summary: Every source recipe row and preparation object, with exact raw substring
    and decoded JSON locator, kept in its own solution stage. No biological recommendation
    follows from provider equipment metadata.
  snapshot_sha256: 68385e2a0d7f1c8d2b2284b09a506ab863e34b965f078042345c761bf29e63d8
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item, _parse_unit, _extract_primary_components, _extract_ph,
    _extract_preparation_steps, _convert_to_culturemech
  accessed_at: '2026-10-28T12:10:06.509495Z'
  support: context_only
  summary: Current _ingredient_from_item preserves the supplied scalar and maps units
    through _parse_unit; that function now maps l to L, while g is G_PER_L. Primary-section
    handling avoids unrelated stock sections. _extract_ph reads root ph, whereas this
    source stores meta.ph, and _extract_preparation_steps reads comments but cannot
    import the JCM page-wide default absent from TOGO. This current code does not
    authenticate the historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15377
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T12:04:11.293489Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 42561686e12ba0831d99216248ea8c0b3338b461b0b77dd988f3096ad8678e59
- evidence_id: chebi17234
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17234
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T12:04:12.101949Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2d78d31a7829da999c31ae102da842c5b5c37a5d334be6389539d92ecd786de7
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch066/record02/quantity-inventory.json
  accessed_at: '2026-10-28T12:10:06.562375Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 6f82dafc6a1faf41cd2a9c6ba2cf28c26862cbffc10b890f26bbbb25580aed9c
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch066/record02/grounding-inventory.json
  accessed_at: '2026-10-28T12:10:06.562408Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: d9524b9734a8e52550f294be295999b6bdab8d575bf2c3c11fe1fbd9ed7b710b
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch066/record02/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T12:10:06.562450Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: db79954deb0f2d7a6b5c8f65bfbfb0dd16440d6da93579110820b974e690c2a0
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch066/record02/scalar-census.json
  accessed_at: '2026-10-28T12:10:06.562471Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 740923511484d0510becd22cf9a983fd57ee9ec206695d8f48315037cb8c91a8
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch066/record02/validate-schema.json
  accessed_at: '2026-10-28T12:01:25.659849Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: 2a973cdb1c4749423983355c79176c08e6d7b0d2ea0e187aa70aa9e04f248233
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch066/record02/validate-strict.json
  accessed_at: '2026-10-28T12:01:26.592974Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch066/record02/strict.tsv\n"
  snapshot_sha256: 64eac25163ce525c9ad4d0f410bac0335df6aae0c3465ac279646ed0cfe65011
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch066/record02/validate-terms.json
  accessed_at: '2026-10-28T12:01:27.609095Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: 3836b7bf3b16aad127d7005617df3cb6978a21bad4c79f5f129f983ca5710ef4
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch066/record02/validate-references.json
  accessed_at: '2026-10-28T12:01:28.249181Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: b06e9f070a53477cc0431ade3025a5fd30feb630048bfaabd882a3ada2b62ac2
assessments:
- assessment_id: a1
  area: identity
  topic: JCM605 and TOGO M612 identity
  outcome: supported
  summary: The exact current JCM heading, TOGO original_media_id/source URL and J605
    provider link agree. Only the maintained TOGO contributor owns this target. The
    two historical reports for cooked_meat_medium__5c313447 concern a different generated
    identity and owner; they are comparison context, not authority to collapse current
    unequal records.
  target_ids:
  - CultureMech:010012
  evidence_ids:
  - identity-search
  - jcm605
  - togo612
  - apiJ605
  - historical-reader
- assessment_id: a2
  area: completeness
  topic: Commercial premix and omitted source context
  outcome: concern
  summary: Complex/undefined composition is appropriate for the named cooked-meat
    premix. The current source does not identify a specific organism or establish
    strain-level growth; generic bacterial/application labels remain generic. Source
    water units, pH and preparation need explicit representation, while glucose and
    premix rates retain provider support. No product-code-specific composition is
    inferred from the Oxoid label.
  target_ids:
  - CultureMech:010012
  evidence_ids:
  - jcm605
  - togo612
  - apiJ605
  - quantities
- assessment_id: a3
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:010012
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Distilled-water input", "source": [{"evidence_id":
    "togo612", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M612",
    "raw_path": "REVIEW_WORK/batch066/source01-03/togo612.bin", "raw_sha256": "aa3d9543530f9ddc12cbf1d252c5702d747f7f1d92a93716317f85b724a1872a",
    "locator": "$.components[0].items[0]", "accessed_at": "2026-10-28T12:04:10.608522Z",
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
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ605",
    "reference": "https://mediadive.dsmz.de/rest/medium/J605", "raw_path": "REVIEW_WORK/batch066/source01-03/apiJ605.bin",
    "raw_sha256": "aeb40b82f4a35c55ab17c19c28207f1e89e286a31d492be15c806416f800738d",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T12:04:10.791700Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "jcm605", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=605",
    "raw_path": "REVIEW_WORK/batch066/source01-03/jcm605.bin", "raw_sha256": "2bd152d41eff1f489cc77ab8dd23309aca0b737e9f444efc53635f70d830513e",
    "locator": "Exact recipe-table water row rendered as DOM text", "accessed_at":
    "2026-10-28T12:04:10.732503Z", "quote": "Distilled water\n1.0\nL"}], "decision":
    "correct", "rationale": "Correct the dimensional representation while retaining
    the printed source quantity. Water identity CHEBI:15377 is supported independently
    of this unit error.", "layer_assessments": [{"path": "data/merge_yaml/merged/COOKED_MEAT_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Source specifies 1 L water (provider
    1000 ml), not 1 g/L. Preserve as solvent-volume context; no density conversion
    or measured-final-volume inference is justified."}, {"path": "data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "Source specifies 1 L water (provider
    1000 ml), not 1 g/L. Preserve as solvent-volume context; no density conversion
    or measured-final-volume inference is justified."}]}, {"quantity_id": "q2", "topic":
    "Glucose", "source": [{"evidence_id": "togo612", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M612",
    "raw_path": "REVIEW_WORK/batch066/source01-03/togo612.bin", "raw_sha256": "aa3d9543530f9ddc12cbf1d252c5702d747f7f1d92a93716317f85b724a1872a",
    "locator": "$.components[0].items[1]", "accessed_at": "2026-10-28T12:04:10.608522Z",
    "quote": "{\n          \"component_name\": \"Glucose\",\n          \"volume\":
    10,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001815\",\n          \"gmo_id\":
    \"GMO_001815\",\n          \"label\": \"Glucose\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }", "exact_decoded_object":
    {"component_name": "Glucose", "volume": 10, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001815",
    "gmo_id": "GMO_001815", "label": "Glucose", "properties": [{"id": "GMO_000046",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"},
    {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple
    component"}, {"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041",
    "label": "Organic compound"}], "roles": [{"id": "GMO_000063", "uri": "http://purl.jp/bio/10/gmo/GMO_000063",
    "label": "Carbon source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ605",
    "reference": "https://mediadive.dsmz.de/rest/medium/J605", "raw_path": "REVIEW_WORK/batch066/source01-03/apiJ605.bin",
    "raw_sha256": "aeb40b82f4a35c55ab17c19c28207f1e89e286a31d492be15c806416f800738d",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T12:04:10.791700Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\":
    10,\n                        \"unit\": \"g\",\n                        \"g_l\":
    10,\n                        \"mmol_l\": 55.5062,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Glucose", "compound_id": 5, "amount": 10, "unit": "g", "g_l": 10, "mmol_l": 55.5062,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "jcm605", "reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=605", "raw_path": "REVIEW_WORK/batch066/source01-03/jcm605.bin",
    "raw_sha256": "2bd152d41eff1f489cc77ab8dd23309aca0b737e9f444efc53635f70d830513e",
    "locator": "Exact JCM605 recipe-table row", "accessed_at": "2026-10-28T12:04:10.732503Z",
    "quote": "Glucose\n10.0\ng"}], "decision": "evidence_only", "rationale": "Keep
    the source-specific nominal rate. Oxoid names a commercial complex premix, not
    a single chemical or a license to substitute a different product formulation.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/COOKED_MEAT_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Unchanged rate
    agrees with explicit current provider g_l. Primary JCM and TOGO supply the batch
    mass and water input; add exact provider basis and primary identity evidence without
    claiming a measured final volume."}, {"path": "data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Unchanged rate
    agrees with explicit current provider g_l. Primary JCM and TOGO supply the batch
    mass and water input; add exact provider basis and primary identity evidence without
    claiming a measured final volume."}]}, {"quantity_id": "q3", "topic": "Cooked
    meat medium (Oxoid)", "source": [{"evidence_id": "togo612", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M612",
    "raw_path": "REVIEW_WORK/batch066/source01-03/togo612.bin", "raw_sha256": "aa3d9543530f9ddc12cbf1d252c5702d747f7f1d92a93716317f85b724a1872a",
    "locator": "$.components[0].items[2]", "accessed_at": "2026-10-28T12:04:10.608522Z",
    "quote": "{\n          \"component_name\": \"Cooked meat medium (Oxoid)\",\n          \"volume\":
    55,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001538\",\n          \"gmo_id\":
    \"GMO_001538\",\n          \"label\": \"Oxoid &trade; Cooked meat medium\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            },\n            {\n              \"id\": \"GMO_000050\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000050\",\n              \"label\": \"Complex
    component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "exact_decoded_object": {"component_name": "Cooked meat medium (Oxoid)", "volume":
    55, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001538", "gmo_id": "GMO_001538",
    "label": "Oxoid &trade; Cooked meat medium", "properties": [{"id": "GMO_000047",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000047", "label": "Undefined component"},
    {"id": "GMO_000050", "uri": "http://purl.jp/bio/10/gmo/GMO_000050", "label": "Complex
    component"}], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ605",
    "reference": "https://mediadive.dsmz.de/rest/medium/J605", "raw_path": "REVIEW_WORK/batch066/source01-03/apiJ605.bin",
    "raw_sha256": "aeb40b82f4a35c55ab17c19c28207f1e89e286a31d492be15c806416f800738d",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T12:04:10.791700Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Cooked meat medium\",\n                        \"compound_id\": 1824,\n                        \"attribute\":
    \"Oxoid\",\n                        \"amount\": 55,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 55,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Cooked meat medium", "compound_id": 1824, "attribute": "Oxoid", "amount": 55,
    "unit": "g", "g_l": 55, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "jcm605", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=605",
    "raw_path": "REVIEW_WORK/batch066/source01-03/jcm605.bin", "raw_sha256": "2bd152d41eff1f489cc77ab8dd23309aca0b737e9f444efc53635f70d830513e",
    "locator": "Exact JCM605 recipe-table row", "accessed_at": "2026-10-28T12:04:10.732503Z",
    "quote": "Cooked meat medium (Oxoid)\n55.0\ng"}], "decision": "evidence_only",
    "rationale": "Keep the source-specific nominal rate. Oxoid names a commercial
    complex premix, not a single chemical or a license to substitute a different product
    formulation.", "layer_assessments": [{"path": "data/merge_yaml/merged/COOKED_MEAT_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "55",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Unchanged rate
    agrees with explicit current provider g_l. Primary JCM and TOGO supply the batch
    mass and water input; add exact provider basis and primary identity evidence without
    claiming a measured final volume."}, {"path": "data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "55",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Unchanged rate
    agrees with explicit current provider g_l. Primary JCM and TOGO supply the batch
    mass and water input; add exact provider basis and primary identity evidence without
    claiming a measured final volume."}]}, {"quantity_id": "q4", "topic": "Missing
    final pH", "source": [{"evidence_id": "jcm605", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=605",
    "raw_path": "REVIEW_WORK/batch066/source01-03/jcm605.bin", "raw_sha256": "2bd152d41eff1f489cc77ab8dd23309aca0b737e9f444efc53635f70d830513e",
    "locator": "Exact sentence following JCM605 recipe", "accessed_at": "2026-10-28T12:04:10.732503Z",
    "quote": "Check the final pH to be around 7.2."}, {"evidence_id": "apiJ605", "reference":
    "https://mediadive.dsmz.de/rest/medium/J605", "raw_path": "REVIEW_WORK/batch066/source01-03/apiJ605.bin",
    "raw_sha256": "aeb40b82f4a35c55ab17c19c28207f1e89e286a31d492be15c806416f800738d",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T12:04:10.791700Z",
    "quote": "{\n                        \"step\": \"Check the final pH to be around
    7.2.\"\n                    }", "exact_decoded_object": {"step": "Check the final
    pH to be around 7.2."}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "togo612",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M612",
    "raw_path": "REVIEW_WORK/batch066/source01-03/togo612.bin", "raw_sha256": "aa3d9543530f9ddc12cbf1d252c5702d747f7f1d92a93716317f85b724a1872a",
    "locator": "$.comments[0]", "accessed_at": "2026-10-28T12:04:10.608522Z", "quote":
    "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Check the final pH to
    be around 7.2.\"\n    }", "exact_decoded_object": {"paragraph_index": 2, "comment":
    "Check the final pH to be around 7.2."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "add", "rationale": "Add source pH around 7.2 as approximate source context with
    root evidence; do not claim an exact measured pH, unspecified adjustment reagent
    or measurement temperature.", "layer_assessments": []}, {"quantity_id": "q5",
    "topic": "Missing JCM default preparation", "source": [{"evidence_id": "jcm605",
    "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=605", "raw_path":
    "REVIEW_WORK/batch066/source01-03/jcm605.bin", "raw_sha256": "2bd152d41eff1f489cc77ab8dd23309aca0b737e9f444efc53635f70d830513e",
    "locator": "Page-wide default preceding exact JCM605 heading", "accessed_at":
    "2026-10-28T12:04:10.732503Z", "quote": "Unless otherwise stated, sterilize media
    by autoclaving at 121°C for 15 min."}], "decision": "add", "rationale": "The exact
    primary page applies this default unless overridden, and 605 supplies no override.
    Retain its conditional default scope and original 121°C/15 min in preparation
    with root evidence; it is not an organism-specific optimization.", "layer_assessments":
    []}]'
- assessment_id: a4
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: supported
  summary: Both primary and secondary water/glucose assertions resolve to fresh canonical
    CHEBI:15377 and CHEBI:17234 and current exact MIM rows. Generic glucose is not
    upgraded to an unstated stereochemical form. Commercial cooked-meat premix remains
    an ungrounded mixture; no invented pure-compound ID is assigned.
  target_ids:
  - CultureMech:010012
  evidence_ids:
  - grounding
- assessment_id: a5
  area: provenance
  topic: History and evidence scope
  outcome: supported
  summary: Complete selected histories and all four matching or neighboring reports
    were read. Selected October reports were source-unchecked screenings; September
    and the other October generated report refer to CM002953, not this CM010012 lineage.
    No old retrieval event or forced merge recommendation is authenticated by current
    captures.
  target_ids:
  - CultureMech:010012
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
  - CultureMech:010012
  evidence_ids:
  - local-target
- assessment_id: a7
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:010012
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-010012-represent-source-water-as-solvent-volume
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Represent source water as solvent volume
  description: Both layers encode distilled water as 1 G_PER_L, although JCM605 and
    TOGO specify 1.0 L and current J605 supplies 1000 ml. The water identifier is
    correct; the concentration dimension is not. Primary solvent volume does not establish
    a measured final volume for the non-solvent components.
  target_ids:
  - CultureMech:010012
  field_paths:
  - ingredients[0].concentration
  - preparation_steps
  evidence_ids:
  - jcm605
  - togo612
  - apiJ605
  - quantities
  - writer-togo
  rule_id: P2.3
  native_severity: P2
  normalization_reason: 'Major: native P2.3 unit consistency applies directly because
    a source volume is encoded as mass per volume. This is not an ingredient-identity
    correction.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-010012-restore-source-ph-and-scoped-default-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Restore source pH and scoped default preparation
  description: Both layers omit the primary final-pH statement around 7.2 and JCM
    page-wide 121°C/15 min default. Current TOGO retains the pH comment and meta.ph
    but does not carry the JCM page-wide default; the current pH extractor reads a
    different root key. These are exact source-context omissions, not evidence for
    a different medium or organism.
  target_ids:
  - CultureMech:010012
  field_paths:
  - ph_value
  - preparation_steps
  - evidence
  evidence_ids:
  - jcm605
  - togo612
  - apiJ605
  - quantities
  - writer-togo
  rule_id: custom-source-process-completeness
  native_severity: P3
  normalization_reason: 'Major normalized from preparation-completeness concern: both
    the entire source preparation and pH context are absent. The substantive omission
    is documented explicitly rather than treated as a minor formatting defect.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-010012-link-supported-unchanged-claims-and-preserve-historical-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Link supported unchanged claims and preserve historical scope
  description: Neither layer attaches exact formulation/preparation evidence. October
    5 reports expressly performed no source checks. The September review discusses
    a different generated identity and recommends a forced source-duplicate collapse;
    current owner resolution and formulation-compatibility rules require separate
    reassessment before any such merge.
  target_ids:
  - CultureMech:010012
  field_paths:
  - evidence
  - references
  - ingredients[1].evidence
  - ingredients[2].evidence
  evidence_ids:
  - jcm605
  - togo612
  - apiJ605
  - historical-reader
  - writer-merge
  - writer-formulation
  rule_id: P4.3
  native_severity: P4
  normalization_reason: 'Minor normalized from native P4.3 missing source citation:
    exact source routes are present and freshly checked, but current field-level claims
    lack durable supporting evidence.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Preserve the exact 1 L water input in schema-supported solvent/preparation
    context and remove the false water mass concentration. Keep the two explicitly
    provider-supported non-solvent rates with their named basis; do not calculate
    an unreported final volume.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010012
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Add the approximate source pH and exact conditionally applicable JCM
    default preparation with schema-supported root evidence and precise source locators.
    Preserve absence of organism-specific claims; do not infer reagent, culture duration
    or growth temperature.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010012
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Attach exact current JCM/TOGO/provider claims to the supported ingredient
    and root slots. Preserve all original histories and neighboring reports, append
    only verified new context, and avoid automatically applying the old two-record-collapse
    recommendation.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010012
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M612_Cooked_Meat_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- The source supplies water input, not explicit final volume; current provider g_l
  is retained as its declared main-stage basis.
- The exact current JCM605/TOGO M612 context contains no organism claim. No generic
  Cooked Meat product association is transferred into strain-specific growth or safety
  assertions. Oxoid product-code and premix composition remain unspecified.
- JCM default preparation is explicitly conditional; no missing reagent, measured
  pH or organism-specific culture condition is invented.
- Historical reports are derivative context, not a reconstructed review or verified
  historical retrieval. Native reference validation performed zero checks.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
