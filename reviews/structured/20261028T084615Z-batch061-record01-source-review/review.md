# CH: retain repaired stock formulation and correct generated scope

- Review: 20261028T084615Z-batch061-record01-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T08:33:25.534370Z
- Finished UTC: 2026-10-28T08:46:15.835993Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The maintained CCAP C22 owner already restores all three stocks and their 5 ml/L additions. The generated record remains stale and misstates each stock addition as 5 g/L. Clarify water as final-volume makeup, retain the supported preparation, link exact evidence and distinguish the primary freshwater-protozoan scope from the bacterial filing and separate algae namesake.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch061 native selection index 01.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000330 | data/merge_yaml/merged/CH.yaml | generated | ch |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000330 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:000330 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:000330 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:000330 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact C22 owner and separate namesake

identity: supported. Targets: CultureMech:000330.

The target ID000330 and MediaDive C22 identify the bacterial maintained contributor. The separate algae/ch record has ID000059 and is a comparison, not a second target owner. The current primary title and provider identity agree; defined composition and liquid state are supported.

### Repair already present in maintained owner

completeness: concern. Targets: CultureMech:000330.

The owner already preserves all stock strengths, doses and preparation. The generated composition and stock structure are stale. Water needs a local final-makeup qualifier, and source evidence must accompany retained claims.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:000330.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "NaCl stock strength and receiving dose", "source": [{"evidence_id": "apiC22", "reference": "https://mediadive.dsmz.de/rest/medium/C22", "raw_path": "REVIEW_WORK/batch061/source01-03/apiC22.bin", "raw_sha256": "7cd273abdec2f90fe874700767054331de29b27b72fd7e013208dbbb14ce5f3b", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T08:34:39.657498Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"attribute\": \"2 g/100 ml stock solution\",\n                        \"amount\": 5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "NaCl", "compound_id": 43, "attribute": "2 g/100 ml stock solution", "amount": 5, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "ccapCH", "reference": "https://www.ccap.ac.uk/wp-content/uploads/MR_CH.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/ccapCH.bin", "raw_sha256": "44b2cf7784d6842d2c6b1c8e182a3406f64ccc18069ddf60283ce236f7dff8e0", "locator": "Page1 Stocks and Medium table", "accessed_at": "2026-10-28T08:34:40.049277Z", "quote": "Stock solutions 1-3                                           5.0 ml each"}], "decision": "mixed", "rationale": "The source stock is 2.0 g per 100 ml (20 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage error; the owner already has the correct stock strength and dose. Preserve those repairs rather than adding direct salts on top of the stocks.", "layer_assessments": [{"path": "data/merge_yaml/merged/CH.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source stock is 2.0 g per 100 ml (20 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage error; the owner already has the correct stock strength and dose. Preserve those repairs rather than adding direct salts on top of the stocks."}, {"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path": "solutions[0].concentration", "stored_value": {"value": "5.0", "unit": "ML_PER_L"}, "decision": "evidence_only", "rationale": "The source stock is 2.0 g per 100 ml (20 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage error; the owner already has the correct stock strength and dose. Preserve those repairs rather than adding direct salts on top of the stocks."}, {"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path": "solutions[0].composition[0].concentration", "stored_value": {"value": "20", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The source stock is 2.0 g per 100 ml (20 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage error; the owner already has the correct stock strength and dose. Preserve those repairs rather than adding direct salts on top of the stocks."}]}, {"quantity_id": "q2", "topic": "KCl stock strength and receiving dose", "source": [{"evidence_id": "apiC22", "reference": "https://mediadive.dsmz.de/rest/medium/C22", "raw_path": "REVIEW_WORK/batch061/source01-03/apiC22.bin", "raw_sha256": "7cd273abdec2f90fe874700767054331de29b27b72fd7e013208dbbb14ce5f3b", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T08:34:39.657498Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"attribute\": \"0.08 g/100 ml stock solution\",\n                        \"amount\": 5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "KCl", "compound_id": 61, "attribute": "0.08 g/100 ml stock solution", "amount": 5, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "ccapCH", "reference": "https://www.ccap.ac.uk/wp-content/uploads/MR_CH.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/ccapCH.bin", "raw_sha256": "44b2cf7784d6842d2c6b1c8e182a3406f64ccc18069ddf60283ce236f7dff8e0", "locator": "Page1 Stocks and Medium table", "accessed_at": "2026-10-28T08:34:40.049277Z", "quote": "Stock solutions 1-3                                           5.0 ml each"}], "decision": "mixed", "rationale": "The source stock is 0.08 g per 100 ml (0.8 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage error; the owner already has the correct stock strength and dose. Preserve those repairs rather than adding direct salts on top of the stocks.", "layer_assessments": [{"path": "data/merge_yaml/merged/CH.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source stock is 0.08 g per 100 ml (0.8 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage error; the owner already has the correct stock strength and dose. Preserve those repairs rather than adding direct salts on top of the stocks."}, {"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path": "solutions[1].concentration", "stored_value": {"value": "5.0", "unit": "ML_PER_L"}, "decision": "evidence_only", "rationale": "The source stock is 0.08 g per 100 ml (0.8 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage error; the owner already has the correct stock strength and dose. Preserve those repairs rather than adding direct salts on top of the stocks."}, {"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path": "solutions[1].composition[0].concentration", "stored_value": {"value": "0.8", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The source stock is 0.08 g per 100 ml (0.8 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage error; the owner already has the correct stock strength and dose. Preserve those repairs rather than adding direct salts on top of the stocks."}]}, {"quantity_id": "q3", "topic": "CaCl2 stock strength and receiving dose", "source": [{"evidence_id": "apiC22", "reference": "https://mediadive.dsmz.de/rest/medium/C22", "raw_path": "REVIEW_WORK/batch061/source01-03/apiC22.bin", "raw_sha256": "7cd273abdec2f90fe874700767054331de29b27b72fd7e013208dbbb14ce5f3b", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T08:34:39.657498Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2\",\n                        \"compound_id\": 81,\n                        \"attribute\": \"0.12 g/100 ml stock solution\",\n                        \"amount\": 5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "CaCl2", "compound_id": 81, "attribute": "0.12 g/100 ml stock solution", "amount": 5, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "ccapCH", "reference": "https://www.ccap.ac.uk/wp-content/uploads/MR_CH.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/ccapCH.bin", "raw_sha256": "44b2cf7784d6842d2c6b1c8e182a3406f64ccc18069ddf60283ce236f7dff8e0", "locator": "Page1 Stocks and Medium table", "accessed_at": "2026-10-28T08:34:40.049277Z", "quote": "Stock solutions 1-3                                           5.0 ml each"}], "decision": "mixed", "rationale": "The source stock is 0.12 g per 100 ml (1.2 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage error; the owner already has the correct stock strength and dose. Preserve those repairs rather than adding direct salts on top of the stocks.", "layer_assessments": [{"path": "data/merge_yaml/merged/CH.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source stock is 0.12 g per 100 ml (1.2 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage error; the owner already has the correct stock strength and dose. Preserve those repairs rather than adding direct salts on top of the stocks."}, {"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path": "solutions[2].concentration", "stored_value": {"value": "5.0", "unit": "ML_PER_L"}, "decision": "evidence_only", "rationale": "The source stock is 0.12 g per 100 ml (1.2 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage error; the owner already has the correct stock strength and dose. Preserve those repairs rather than adding direct salts on top of the stocks."}, {"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path": "solutions[2].composition[0].concentration", "stored_value": {"value": "1.2", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The source stock is 0.12 g per 100 ml (1.2 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage error; the owner already has the correct stock strength and dose. Preserve those repairs rather than adding direct salts on top of the stocks."}]}, {"quantity_id": "q4", "topic": "Final-volume makeup and water context", "source": [{"evidence_id": "apiC22", "reference": "https://mediadive.dsmz.de/rest/medium/C22", "raw_path": "REVIEW_WORK/batch061/source01-03/apiC22.bin", "raw_sha256": "7cd273abdec2f90fe874700767054331de29b27b72fd7e013208dbbb14ce5f3b", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T08:34:39.657498Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Deionized water\",\n                        \"compound_id\": 418,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "Deionized water", "compound_id": 418, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "ccapCH", "reference": "https://www.ccap.ac.uk/wp-content/uploads/MR_CH.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/ccapCH.bin", "raw_sha256": "44b2cf7784d6842d2c6b1c8e182a3406f64ccc18069ddf60283ce236f7dff8e0", "locator": "Page1 preparation", "accessed_at": "2026-10-28T08:34:40.049277Z", "quote": "Make up to 1 litre with deionised water. Autoclave at 15 psi for 15 minutes."}], "decision": "mixed", "rationale": "The PDF and retained preparation explicitly make the medium up to 1 litre after the stock additions. The owner water 1 L must be identified as final-volume makeup, not a fixed additional litre of solvent. Keep the supported 1 L endpoint and add a field-local qualifier; do not calculate an exact standalone water volume from assumed volume additivity.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "L"}, "decision": "correct", "rationale": "The PDF and retained preparation explicitly make the medium up to 1 litre after the stock additions. The owner water 1 L must be identified as final-volume makeup, not a fixed additional litre of solvent. Keep the supported 1 L endpoint and add a field-local qualifier; do not calculate an exact standalone water volume from assumed volume additivity."}, {"path": "data/merge_yaml/merged/CH.yaml", "field_path": "notes", "stored_value": "Source: CCAP &#124; Link: https://www.ccap.ac.uk/wp-content/uploads/MR_CH.pdf", "decision": "add", "rationale": "The PDF and retained preparation explicitly make the medium up to 1 litre after the stock additions. The owner water 1 L must be identified as final-volume makeup, not a fixed additional litre of solvent. Keep the supported 1 L endpoint and add a field-local qualifier; do not calculate an exact standalone water volume from assumed volume additivity."}]}, {"quantity_id": "q5", "topic": "Preparation, all numeric instructions and sterilization", "source": [{"evidence_id": "apiC22", "reference": "https://mediadive.dsmz.de/rest/medium/C22", "raw_path": "REVIEW_WORK/batch061/source01-03/apiC22.bin", "raw_sha256": "7cd273abdec2f90fe874700767054331de29b27b72fd7e013208dbbb14ce5f3b", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T08:34:39.657498Z", "quote": "{\n                        \"step\": \"Make up to 1 litre with deionised water. Autoclave at 15 psi for 15 minutes.\"\n                    }", "exact_decoded_object": {"step": "Make up to 1 litre with deionised water. Autoclave at 15 psi for 15 minutes."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "ccapCH", "reference": "https://www.ccap.ac.uk/wp-content/uploads/MR_CH.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/ccapCH.bin", "raw_sha256": "44b2cf7784d6842d2c6b1c8e182a3406f64ccc18069ddf60283ce236f7dff8e0", "locator": "Page1 preparation", "accessed_at": "2026-10-28T08:34:40.049277Z", "quote": "Make up to 1 litre with deionised water. Autoclave at 15 psi for 15 minutes."}], "decision": "evidence_only", "rationale": "The target already retains the 1 litre makeup and 15 psi / 15 minute autoclave instruction. The owner correctly adds the missing 5 ml of each stock and separates mixing from autoclaving. All these stated numbers are supported; no temperature, incubation period or organism-specific condition is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CH.yaml", "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action": "AUTOCLAVE", "description": "Make up to 1 litre with deionised water. Autoclave at 15 psi for 15 minutes."}, "decision": "evidence_only", "rationale": "The target already retains the 1 litre makeup and 15 psi / 15 minute autoclave instruction. The owner correctly adds the missing 5 ml of each stock and separates mixing from autoclaving. All these stated numbers are supported; no temperature, incubation period or organism-specific condition is inferred."}, {"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action": "MIX", "description": "Add 5 ml of each stock solution and make up to 1 L with deionized water."}, "decision": "evidence_only", "rationale": "The target already retains the 1 litre makeup and 15 psi / 15 minute autoclave instruction. The owner correctly adds the missing 5 ml of each stock and separates mixing from autoclaving. All these stated numbers are supported; no temperature, incubation period or organism-specific condition is inferred."}, {"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path": "preparation_steps[1]", "stored_value": {"step_number": 2, "action": "AUTOCLAVE", "description": "Autoclave at 15 psi for 15 minutes."}, "decision": "evidence_only", "rationale": "The target already retains the 1 litre makeup and 15 psi / 15 minute autoclave instruction. The owner correctly adds the missing 5 ml of each stock and separates mixing from autoclaving. All these stated numbers are supported; no temperature, incubation period or organism-specific condition is inferred."}, {"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path": "sterilization.method", "stored_value": "AUTOCLAVE", "decision": "evidence_only", "rationale": "The target already retains the 1 litre makeup and 15 psi / 15 minute autoclave instruction. The owner correctly adds the missing 5 ml of each stock and separates mixing from autoclaving. All these stated numbers are supported; no temperature, incubation period or organism-specific condition is inferred."}]}]

### Current ontology and MIM correspondence

grounding: supported. Targets: CultureMech:000330.

All 14 current chemical term slots agree with the four fresh OLS objects and exact current packaged catalog rows: sodium chloride, potassium chloride, calcium dichloride and water. Medium accession C22 is separately scoped and is not tested as a chemical-catalog identifier. No unsupported hydrate or alternate chemical form is introduced.

### History and evidence scope

provenance: concern. Targets: CultureMech:000330.

Complete target and owner histories plus all four exact historical reports were read. Five October source objects and its raw digest match the fresh API capture, but missing attached evidence remains. The historical API failure and repair-event access assertions are retained as historical claims; new context is append-only.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:000330.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:000330.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Regenerate from repaired stocks and qualify final water makeup

major / open / confirmed; issue key: culturemech-000330-regenerate-from-repaired-stocks-and-qualify-final-water-makeup.

Each target ingredient is 5 G_PER_L, although both current sources describe 5 ml additions from three different stocks. The maintained owner already has 20, 0.8 and 1.2 g/L stock concentrations and 5 ml/L doses. Preserve those owner repairs and regenerate; do not apply the stale error to the owner. Qualify the owner water 1 L as makeup to the final litre, rather than a fixed additional solvent dose. Target preparation already retains the autoclave instruction.

### f2: Align categorical use with primary freshwater protozoan scope

minor / open / confirmed; issue key: culturemech-000330-align-categorical-use-with-primary-freshwater-protozoan-scope.

CCAP explicitly calls CH a Freshwater Protozoa medium. The bacterial category is a source-scope mismatch; generic Microbial cultivation does not establish bacterial growth. The separate algae owner and current importer defaults likewise do not establish algae-specific light, temperature or strain claims.

### f3: Attach exact stock and preparation evidence append only

minor / open / confirmed; issue key: culturemech-000330-attach-exact-stock-and-preparation-evidence-append-only.

The owner has a source URL, a repair note and retained history but lacks attached claim-level evidence. Fresh API bytes exactly authenticate the cited October raw response and five literal objects, not the historical retrieval event or its blanket conflict labels. September recommendations remain derivative; its reported old API failure is superseded only by this separately dated successful capture.

## Recommended Actions And Acceptance Checks

### action1

Preserve the three repaired owner stock objects and doses; add explicit water-makeup scope at the water field, attach exact primary evidence and regenerate the target from that owner. Confirm no direct 5 g/L salt row and no duplicated stock contribution remains.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Represent the stated freshwater-protozoan source scope in supported schema fields and explanatory text, resolving categorical placement without inferring a taxon-specific growth claim or copying generic algae defaults. Keep the distinct stable IDs and source identity explicit.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Attach exact stock-composition evidence at supported ingredient slots and root evidence with precise stock/dose/preparation locators. Preserve every original history event unchanged and append new verified context; do not rewrite earlier access claims or force a cross-category merge.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/CH.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/ch.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch061/record01/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition parser restricts ingredients to the primary solution, excludes solvent and recognized stock additions, and retains explicit g_l. The solution parser preserves referenced or percent-defined stocks and source attributes. Preparation parsing still concatenates all solution steps into root preparation_steps; source-stage annotation remains important. These present functions do not prove the historical execution that produced this record. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. Current behavior does not establish the historical cause of an existing discrepancy. |
| historical-1 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/ch.yaml.md; Entire exact Record-header report, every claim row and narrative | context_only | Current independently captured API response has exactly the cited historical raw SHA256; all 5 literal JSON snippets and locators match. This authenticates those response bytes, not the historical access time or recommendations. |
| historical-2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CH.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/ch.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-4 | reports/yaml_record_review/20260922T065304Z-CH.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-reader | REVIEW_WORK/batch061/record01/historical-reader.json | context_only | All exact target/owner historical report texts and current raw/literal/locator joins; historical recommendations remain subject to current stage and volume evidence. |
| comparison-algae | data/normalized_yaml/algae/ch.yaml; Complete document, source identity and importer-derived defaults | context_only | Complete same-name record read only as a comparison. Its distinct CultureMech:000059 ID does not make it a maintained contributor to this target. Generic algae light and temperature defaults are not adopted. |
| writer-ccap | src/culturemech/import/ccap_importer.py; convert_recipe, _extract_ingredients_from_text, _extract_preparation_from_text | context_only | Current convert_recipe hardcodes algae/category/applications and generic light/temperature prose. These defaults do not authenticate use of this CH recipe. The simple text parser is not proof of this historical import. |
| writer-ch-repair | scripts/repair_ccap_duplicate_compositions.py; water, stock, ch_recipe | context_only | Current ch_recipe explicitly constructs three stock strengths/doses and final-volume preparation. Its water() ingredient has 1 L without a field-local makeup qualifier; retain the explicit preparation context. Code supports the current structure, not independent proof that a past event ran. |
| writer-source-repair | scripts/repair_ccap_sources_score10.py; _require_target, _ensure_source, _ensure_event, repair_record | context_only | Current source repair requires matching CCAP reference and ccap-import event, adds structured sources and manages its own event. That precondition is not satisfied merely by a MediaDive C22 identity; do not blindly apply it to the bacterial owner or rewrite historical events. |
| ccapCH | https://www.ccap.ac.uk/wp-content/uploads/MR_CH.pdf; Page 1, Stocks / Medium / preparation / reference; revision002 May2026 | supports | Complete one-page primary PDF read textually and visually. Stock table has an explicit per-100-ml basis, each stock is added at 5 ml per litre, and the medium is made up to 1 litre. Freshwater Protozoa is the stated application. |
| apiC22 | https://mediadive.dsmz.de/rest/medium/C22; $.data.medium; $.data.solutions[0].recipe and steps | supports | Complete current C22 response independently confirms the three 5 ml stock additions with explicit strength attributes. It declares no g_l for these additions; the 1000 ml water recipe row must be read with the explicit make-up step. Raw digest exactly matches the October report. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32588; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi3312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_3312; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15377; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch061/record01/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch061/record01/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch061/record01/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch061/record01/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch061/record01/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch061/record01/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch061/record01/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch061/record01/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch061/record01/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- The CCAP reference to Chalkley (1930) is read as the PDF bibliography; the original paper was not acquired and no DOI or paper-derived formulation is asserted.
- Freshwater Protozoa is a general source application, not strain-level growth evidence. Same-name algae metadata and generic importer conditions are excluded from transfer.
- The primary specifies final makeup to 1 litre; the exact water addition before adjustment is not specified. No fixed 985 ml solvent inference is made.
- Current source agreement and historical raw-byte equality do not authenticate historical execution, retrieval time or every derivative recommendation.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T084615Z-batch061-record01-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'CH: retain repaired stock formulation and correct generated scope'
started_at: '2026-10-28T08:33:25.534370Z'
finished_at: '2026-10-28T08:46:15.835993Z'
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
summary: The maintained CCAP C22 owner already restores all three stocks and their
  5 ml/L additions. The generated record remains stale and misstates each stock addition
  as 5 g/L. Clarify water as final-volume makeup, retain the supported preparation,
  link exact evidence and distinguish the primary freshwater-protozoan scope from
  the bacterial filing and separate algae namesake.
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
  - path: data/merge_yaml/merged/CH.yaml
    sha256: 1f37093e0996c86a2b9b86657d7ad933ea297a696abc5161916da2967088cd5b
    role: target
  - path: data/normalized_yaml/algae/ch.yaml
    sha256: fb2fc53cd34d7ca82b06d9a98810d42ac4ddec57b74e65d311574b880d4593c1
    role: context
  - path: data/normalized_yaml/bacterial/ch.yaml
    sha256: 1896b05f38c642ca9bf2c9cbb7e79aaa4e390218aedeaaf7bbace273fd76176d
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/ch.yaml.md
    sha256: 399197d052f869d5c8a7b4c6b41ac2d1d52ff85574522a520f0bb36e1309998a
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CH.md
    sha256: 19c86ca850fb57ab34640ecf73e401a3d6c48b4f47ab21b7a0c6c8d4536bb748
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/ch.md
    sha256: ebdc3c937b179dd9afa041eb4f3aeba39f6cceb66ee17b09457ec0a185297ac3
    role: context
  - path: reports/yaml_record_review/20260922T065304Z-CH.md
    sha256: 0969047f8c4724289d955d3ae339c2dd876af188e92d64fd7d792c5225a67091
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/repair_ccap_duplicate_compositions.py
    sha256: d6ce21d516f227305d30631f8b04af781946cb40bb87aa8fd0fc47aa5a8caa0c
    role: context
  - path: scripts/repair_ccap_sources_score10.py
    sha256: f518688ae99e154f490af337dab30b9038657a814db72861e0b53658a2541ae6
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
  - path: src/culturemech/import/ccap_importer.py
    sha256: c579c1d8fb62b96e739e5ee5c963453753ebca0bbf50996fb0f0d6eedd75c9ac
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
  selection: Actual batch061 native selection index 01.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000330
targets:
- target_id: CultureMech:000330
  path: data/merge_yaml/merged/CH.yaml
  label: ch
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ch.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:000330
  command: just validate-schema data/merge_yaml/merged/CH.yaml
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
  - CultureMech:000330
  command: just validate-strict data/merge_yaml/merged/CH.yaml --out REVIEW_WORK/batch061/record01/strict.tsv
    --workers 1
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
  - CultureMech:000330
  command: just validate-terms data/merge_yaml/merged/CH.yaml
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
  - CultureMech:000330
  command: just validate-references data/merge_yaml/merged/CH.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CH.yaml
  locator: Complete document
  accessed_at: '2026-10-28T08:42:05.303376Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 1f37093e0996c86a2b9b86657d7ad933ea297a696abc5161916da2967088cd5b
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/ch.yaml
  locator: Complete document
  accessed_at: '2026-10-28T08:42:05.303376Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 1896b05f38c642ca9bf2c9cbb7e79aaa4e390218aedeaaf7bbace273fd76176d
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch061/record01/identity-search.json
  accessed_at: '2026-10-28T08:42:05.349494Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    excluded namesakes are retained in the census. Similar names and source accessions
    are not promoted to owners.
  snapshot_sha256: 5ac5691f9d033c13875cd7d8a71344e82b3d345e342e7356cf6a48f84a5f523a
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T08:42:05.303376Z'
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
  accessed_at: '2026-10-28T08:42:05.303376Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T08:42:05.303376Z'
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
  accessed_at: '2026-10-28T08:42:05.303376Z'
  support: context_only
  summary: Current cleanup groups identical normalized names, keeps the first entry
    as a base, flags differing concentrations and combines a warning note; it does
    not sum concentrations. It can still discard distinctions when names repeat, so
    source stage must be retained. Current behavior does not establish the historical
    cause of an existing discrepancy.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/ch.yaml.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:42:05.303376Z'
  support: context_only
  summary: Current independently captured API response has exactly the cited historical
    raw SHA256; all 5 literal JSON snippets and locators match. This authenticates
    those response bytes, not the historical access time or recommendations.
  snapshot_sha256: 399197d052f869d5c8a7b4c6b41ac2d1d52ff85574522a520f0bb36e1309998a
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CH.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:42:05.303376Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 19c86ca850fb57ab34640ecf73e401a3d6c48b4f47ab21b7a0c6c8d4536bb748
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/ch.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:42:05.303376Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: ebdc3c937b179dd9afa041eb4f3aeba39f6cceb66ee17b09457ec0a185297ac3
- evidence_id: historical-4
  kind: record_content
  reference: reports/yaml_record_review/20260922T065304Z-CH.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:42:05.303376Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 0969047f8c4724289d955d3ae339c2dd876af188e92d64fd7d792c5225a67091
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch061/record01/historical-reader.json
  accessed_at: '2026-10-28T08:42:05.351575Z'
  support: context_only
  summary: All exact target/owner historical report texts and current raw/literal/locator
    joins; historical recommendations remain subject to current stage and volume evidence.
  snapshot_sha256: c9b88063e1eb77cd86fecad61d29dc2ac3aebafb109012612fcaa7b2c52d4676
- evidence_id: comparison-algae
  kind: record_content
  reference: data/normalized_yaml/algae/ch.yaml
  locator: Complete document, source identity and importer-derived defaults
  accessed_at: '2026-10-28T08:42:05.303376Z'
  support: context_only
  summary: Complete same-name record read only as a comparison. Its distinct CultureMech:000059
    ID does not make it a maintained contributor to this target. Generic algae light
    and temperature defaults are not adopted.
  snapshot_sha256: fb2fc53cd34d7ca82b06d9a98810d42ac4ddec57b74e65d311574b880d4593c1
- evidence_id: writer-ccap
  kind: record_content
  reference: src/culturemech/import/ccap_importer.py
  locator: convert_recipe, _extract_ingredients_from_text, _extract_preparation_from_text
  accessed_at: '2026-10-28T08:42:05.303376Z'
  support: context_only
  summary: Current convert_recipe hardcodes algae/category/applications and generic
    light/temperature prose. These defaults do not authenticate use of this CH recipe.
    The simple text parser is not proof of this historical import.
  snapshot_sha256: c579c1d8fb62b96e739e5ee5c963453753ebca0bbf50996fb0f0d6eedd75c9ac
- evidence_id: writer-ch-repair
  kind: record_content
  reference: scripts/repair_ccap_duplicate_compositions.py
  locator: water, stock, ch_recipe
  accessed_at: '2026-10-28T08:42:05.303376Z'
  support: context_only
  summary: Current ch_recipe explicitly constructs three stock strengths/doses and
    final-volume preparation. Its water() ingredient has 1 L without a field-local
    makeup qualifier; retain the explicit preparation context. Code supports the current
    structure, not independent proof that a past event ran.
  snapshot_sha256: d6ce21d516f227305d30631f8b04af781946cb40bb87aa8fd0fc47aa5a8caa0c
- evidence_id: writer-source-repair
  kind: record_content
  reference: scripts/repair_ccap_sources_score10.py
  locator: _require_target, _ensure_source, _ensure_event, repair_record
  accessed_at: '2026-10-28T08:42:05.303376Z'
  support: context_only
  summary: Current source repair requires matching CCAP reference and ccap-import
    event, adds structured sources and manages its own event. That precondition is
    not satisfied merely by a MediaDive C22 identity; do not blindly apply it to the
    bacterial owner or rewrite historical events.
  snapshot_sha256: f518688ae99e154f490af337dab30b9038657a814db72861e0b53658a2541ae6
- evidence_id: ccapCH
  kind: primary_source
  reference: https://www.ccap.ac.uk/wp-content/uploads/MR_CH.pdf
  locator: Page 1, Stocks / Medium / preparation / reference; revision002 May2026
  accessed_at: '2026-10-28T08:34:40.049277Z'
  support: supports
  summary: Complete one-page primary PDF read textually and visually. Stock table
    has an explicit per-100-ml basis, each stock is added at 5 ml per litre, and the
    medium is made up to 1 litre. Freshwater Protozoa is the stated application.
  snapshot_sha256: 44b2cf7784d6842d2c6b1c8e182a3406f64ccc18069ddf60283ce236f7dff8e0
- evidence_id: apiC22
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/C22
  locator: $.data.medium; $.data.solutions[0].recipe and steps
  accessed_at: '2026-10-28T08:34:39.657498Z'
  support: supports
  summary: Complete current C22 response independently confirms the three 5 ml stock
    additions with explicit strength attributes. It declares no g_l for these additions;
    the 1000 ml water recipe row must be read with the explicit make-up step. Raw
    digest exactly matches the October report.
  snapshot_sha256: 7cd273abdec2f90fe874700767054331de29b27b72fd7e013208dbbb14ce5f3b
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:42.769919Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b145f4ff9b90ebb993ff576d9ab35a6c10b7c42a3b99e18feffcc8d75c0e1e50
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32588
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:44.217978Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 8fc333e98ee953346b5c291b9e5765e77d03cc46740a1282af3e5f4ad355de1a
- evidence_id: chebi3312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_3312
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:44.572008Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 76bdc025d30f15d533c0352d0584f76ec02f6904ab57a13277a2d87ae1189a47
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15377
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T08:34:41.398621Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 42561686e12ba0831d99216248ea8c0b3338b461b0b77dd988f3096ad8678e59
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch061/record01/quantity-inventory.json
  accessed_at: '2026-10-28T08:42:05.356786Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 0ecc7dfedfdf2e0f72b26e9bc6a557acf997f155020246e7b6546097de3f744a
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch061/record01/grounding-inventory.json
  accessed_at: '2026-10-28T08:42:05.356818Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: f930afcb1fce6ed63638f74b6911ea8d99bbbf64f20cb35113e6551a210cfe74
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch061/record01/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T08:42:05.356850Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 31ec62494addbce47af709e536fc288745fd02224af26ee9cc1e853472bbd320
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch061/record01/scalar-census.json
  accessed_at: '2026-10-28T08:42:05.356870Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: d1213dbf37a9e300dd682e38813d8b61b9a7d31038552552c74f1f29097a9ef1
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch061/record01/validate-schema.json
  accessed_at: '2026-10-28T08:33:26.533699Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: 1a908e632e313f49cf64bff19bee421ac86f48301e52c61022009615f52c5b56
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch061/record01/validate-strict.json
  accessed_at: '2026-10-28T08:33:27.451428Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch061/record01/strict.tsv\n"
  snapshot_sha256: 100fb886301c5a4863847c0b47618981523c22c0e6b3b66b972b1a7af316558c
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch061/record01/validate-terms.json
  accessed_at: '2026-10-28T08:33:28.440047Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: 65b4fab455941e6cae38e016e3c063cbedee271db15d486fa3fdbddb2f32c412
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch061/record01/validate-references.json
  accessed_at: '2026-10-28T08:33:29.067341Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 0fad44c22a006754a114670da3102a7235bf57491d8c41f5e3120d73becb2755
assessments:
- assessment_id: a1
  area: identity
  topic: Exact C22 owner and separate namesake
  outcome: supported
  summary: The target ID000330 and MediaDive C22 identify the bacterial maintained
    contributor. The separate algae/ch record has ID000059 and is a comparison, not
    a second target owner. The current primary title and provider identity agree;
    defined composition and liquid state are supported.
  target_ids:
  - CultureMech:000330
  evidence_ids:
  - local-target
  - owner-1
  - identity-search
  - comparison-algae
  - ccapCH
  - apiC22
- assessment_id: a2
  area: completeness
  topic: Repair already present in maintained owner
  outcome: concern
  summary: The owner already preserves all stock strengths, doses and preparation.
    The generated composition and stock structure are stale. Water needs a local final-makeup
    qualifier, and source evidence must accompany retained claims.
  target_ids:
  - CultureMech:000330
  evidence_ids:
  - ccapCH
  - apiC22
  - writer-ch-repair
  - writer-merge
  - writer-mediadive
- assessment_id: a3
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:000330
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "NaCl stock strength and receiving dose",
    "source": [{"evidence_id": "apiC22", "reference": "https://mediadive.dsmz.de/rest/medium/C22",
    "raw_path": "REVIEW_WORK/batch061/source01-03/apiC22.bin", "raw_sha256": "7cd273abdec2f90fe874700767054331de29b27b72fd7e013208dbbb14ce5f3b",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T08:34:39.657498Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"NaCl\",\n                        \"compound_id\": 43,\n                        \"attribute\":
    \"2 g/100 ml stock solution\",\n                        \"amount\": 5,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 2, "compound": "NaCl", "compound_id": 43, "attribute": "2 g/100
    ml stock solution", "amount": 5, "unit": "ml", "optional": 0}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}, {"evidence_id": "ccapCH", "reference": "https://www.ccap.ac.uk/wp-content/uploads/MR_CH.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/ccapCH.bin", "raw_sha256": "44b2cf7784d6842d2c6b1c8e182a3406f64ccc18069ddf60283ce236f7dff8e0",
    "locator": "Page1 Stocks and Medium table", "accessed_at": "2026-10-28T08:34:40.049277Z",
    "quote": "Stock solutions 1-3                                           5.0 ml
    each"}], "decision": "mixed", "rationale": "The source stock is 2.0 g per 100
    ml (20 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage
    error; the owner already has the correct stock strength and dose. Preserve those
    repairs rather than adding direct salts on top of the stocks.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CH.yaml", "field_path": "ingredients[0].concentration",
    "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "The source stock is 2.0 g per 100 ml (20 g/L stock), added at 5 ml per final
    litre. The target 5 G_PER_L is a volume-to-mass/stage error; the owner already
    has the correct stock strength and dose. Preserve those repairs rather than adding
    direct salts on top of the stocks."}, {"path": "data/normalized_yaml/bacterial/ch.yaml",
    "field_path": "solutions[0].concentration", "stored_value": {"value": "5.0", "unit":
    "ML_PER_L"}, "decision": "evidence_only", "rationale": "The source stock is 2.0
    g per 100 ml (20 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L
    is a volume-to-mass/stage error; the owner already has the correct stock strength
    and dose. Preserve those repairs rather than adding direct salts on top of the
    stocks."}, {"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path": "solutions[0].composition[0].concentration",
    "stored_value": {"value": "20", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The source stock is 2.0 g per 100 ml (20 g/L stock), added at 5
    ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage error; the
    owner already has the correct stock strength and dose. Preserve those repairs
    rather than adding direct salts on top of the stocks."}]}, {"quantity_id": "q2",
    "topic": "KCl stock strength and receiving dose", "source": [{"evidence_id": "apiC22",
    "reference": "https://mediadive.dsmz.de/rest/medium/C22", "raw_path": "REVIEW_WORK/batch061/source01-03/apiC22.bin",
    "raw_sha256": "7cd273abdec2f90fe874700767054331de29b27b72fd7e013208dbbb14ce5f3b",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T08:34:39.657498Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"KCl\",\n                        \"compound_id\": 61,\n                        \"attribute\":
    \"0.08 g/100 ml stock solution\",\n                        \"amount\": 5,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 3, "compound": "KCl", "compound_id": 61, "attribute": "0.08 g/100
    ml stock solution", "amount": 5, "unit": "ml", "optional": 0}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}, {"evidence_id": "ccapCH", "reference": "https://www.ccap.ac.uk/wp-content/uploads/MR_CH.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/ccapCH.bin", "raw_sha256": "44b2cf7784d6842d2c6b1c8e182a3406f64ccc18069ddf60283ce236f7dff8e0",
    "locator": "Page1 Stocks and Medium table", "accessed_at": "2026-10-28T08:34:40.049277Z",
    "quote": "Stock solutions 1-3                                           5.0 ml
    each"}], "decision": "mixed", "rationale": "The source stock is 0.08 g per 100
    ml (0.8 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage
    error; the owner already has the correct stock strength and dose. Preserve those
    repairs rather than adding direct salts on top of the stocks.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CH.yaml", "field_path": "ingredients[1].concentration",
    "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "The source stock is 0.08 g per 100 ml (0.8 g/L stock), added at 5 ml per final
    litre. The target 5 G_PER_L is a volume-to-mass/stage error; the owner already
    has the correct stock strength and dose. Preserve those repairs rather than adding
    direct salts on top of the stocks."}, {"path": "data/normalized_yaml/bacterial/ch.yaml",
    "field_path": "solutions[1].concentration", "stored_value": {"value": "5.0", "unit":
    "ML_PER_L"}, "decision": "evidence_only", "rationale": "The source stock is 0.08
    g per 100 ml (0.8 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L
    is a volume-to-mass/stage error; the owner already has the correct stock strength
    and dose. Preserve those repairs rather than adding direct salts on top of the
    stocks."}, {"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path": "solutions[1].composition[0].concentration",
    "stored_value": {"value": "0.8", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The source stock is 0.08 g per 100 ml (0.8 g/L stock), added at
    5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage error; the
    owner already has the correct stock strength and dose. Preserve those repairs
    rather than adding direct salts on top of the stocks."}]}, {"quantity_id": "q3",
    "topic": "CaCl2 stock strength and receiving dose", "source": [{"evidence_id":
    "apiC22", "reference": "https://mediadive.dsmz.de/rest/medium/C22", "raw_path":
    "REVIEW_WORK/batch061/source01-03/apiC22.bin", "raw_sha256": "7cd273abdec2f90fe874700767054331de29b27b72fd7e013208dbbb14ce5f3b",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T08:34:39.657498Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"CaCl2\",\n                        \"compound_id\": 81,\n                        \"attribute\":
    \"0.12 g/100 ml stock solution\",\n                        \"amount\": 5,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 4, "compound": "CaCl2", "compound_id": 81, "attribute": "0.12
    g/100 ml stock solution", "amount": 5, "unit": "ml", "optional": 0}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}, {"evidence_id": "ccapCH", "reference": "https://www.ccap.ac.uk/wp-content/uploads/MR_CH.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/ccapCH.bin", "raw_sha256": "44b2cf7784d6842d2c6b1c8e182a3406f64ccc18069ddf60283ce236f7dff8e0",
    "locator": "Page1 Stocks and Medium table", "accessed_at": "2026-10-28T08:34:40.049277Z",
    "quote": "Stock solutions 1-3                                           5.0 ml
    each"}], "decision": "mixed", "rationale": "The source stock is 0.12 g per 100
    ml (1.2 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage
    error; the owner already has the correct stock strength and dose. Preserve those
    repairs rather than adding direct salts on top of the stocks.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CH.yaml", "field_path": "ingredients[2].concentration",
    "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "The source stock is 0.12 g per 100 ml (1.2 g/L stock), added at 5 ml per final
    litre. The target 5 G_PER_L is a volume-to-mass/stage error; the owner already
    has the correct stock strength and dose. Preserve those repairs rather than adding
    direct salts on top of the stocks."}, {"path": "data/normalized_yaml/bacterial/ch.yaml",
    "field_path": "solutions[2].concentration", "stored_value": {"value": "5.0", "unit":
    "ML_PER_L"}, "decision": "evidence_only", "rationale": "The source stock is 0.12
    g per 100 ml (1.2 g/L stock), added at 5 ml per final litre. The target 5 G_PER_L
    is a volume-to-mass/stage error; the owner already has the correct stock strength
    and dose. Preserve those repairs rather than adding direct salts on top of the
    stocks."}, {"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path": "solutions[2].composition[0].concentration",
    "stored_value": {"value": "1.2", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The source stock is 0.12 g per 100 ml (1.2 g/L stock), added at
    5 ml per final litre. The target 5 G_PER_L is a volume-to-mass/stage error; the
    owner already has the correct stock strength and dose. Preserve those repairs
    rather than adding direct salts on top of the stocks."}]}, {"quantity_id": "q4",
    "topic": "Final-volume makeup and water context", "source": [{"evidence_id": "apiC22",
    "reference": "https://mediadive.dsmz.de/rest/medium/C22", "raw_path": "REVIEW_WORK/batch061/source01-03/apiC22.bin",
    "raw_sha256": "7cd273abdec2f90fe874700767054331de29b27b72fd7e013208dbbb14ce5f3b",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T08:34:39.657498Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Deionized water\",\n                        \"compound_id\": 418,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "Deionized water", "compound_id": 418, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "ccapCH", "reference": "https://www.ccap.ac.uk/wp-content/uploads/MR_CH.pdf",
    "raw_path": "REVIEW_WORK/batch061/source01-03/ccapCH.bin", "raw_sha256": "44b2cf7784d6842d2c6b1c8e182a3406f64ccc18069ddf60283ce236f7dff8e0",
    "locator": "Page1 preparation", "accessed_at": "2026-10-28T08:34:40.049277Z",
    "quote": "Make up to 1 litre with deionised water. Autoclave at 15 psi for 15
    minutes."}], "decision": "mixed", "rationale": "The PDF and retained preparation
    explicitly make the medium up to 1 litre after the stock additions. The owner
    water 1 L must be identified as final-volume makeup, not a fixed additional litre
    of solvent. Keep the supported 1 L endpoint and add a field-local qualifier; do
    not calculate an exact standalone water volume from assumed volume additivity.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path":
    "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "L"}, "decision":
    "correct", "rationale": "The PDF and retained preparation explicitly make the
    medium up to 1 litre after the stock additions. The owner water 1 L must be identified
    as final-volume makeup, not a fixed additional litre of solvent. Keep the supported
    1 L endpoint and add a field-local qualifier; do not calculate an exact standalone
    water volume from assumed volume additivity."}, {"path": "data/merge_yaml/merged/CH.yaml",
    "field_path": "notes", "stored_value": "Source: CCAP | Link: https://www.ccap.ac.uk/wp-content/uploads/MR_CH.pdf",
    "decision": "add", "rationale": "The PDF and retained preparation explicitly make
    the medium up to 1 litre after the stock additions. The owner water 1 L must be
    identified as final-volume makeup, not a fixed additional litre of solvent. Keep
    the supported 1 L endpoint and add a field-local qualifier; do not calculate an
    exact standalone water volume from assumed volume additivity."}]}, {"quantity_id":
    "q5", "topic": "Preparation, all numeric instructions and sterilization", "source":
    [{"evidence_id": "apiC22", "reference": "https://mediadive.dsmz.de/rest/medium/C22",
    "raw_path": "REVIEW_WORK/batch061/source01-03/apiC22.bin", "raw_sha256": "7cd273abdec2f90fe874700767054331de29b27b72fd7e013208dbbb14ce5f3b",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T08:34:39.657498Z",
    "quote": "{\n                        \"step\": \"Make up to 1 litre with deionised
    water. Autoclave at 15 psi for 15 minutes.\"\n                    }", "exact_decoded_object":
    {"step": "Make up to 1 litre with deionised water. Autoclave at 15 psi for 15
    minutes."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object
    independently equals exact JSON locator."}, {"evidence_id": "ccapCH", "reference":
    "https://www.ccap.ac.uk/wp-content/uploads/MR_CH.pdf", "raw_path": "REVIEW_WORK/batch061/source01-03/ccapCH.bin",
    "raw_sha256": "44b2cf7784d6842d2c6b1c8e182a3406f64ccc18069ddf60283ce236f7dff8e0",
    "locator": "Page1 preparation", "accessed_at": "2026-10-28T08:34:40.049277Z",
    "quote": "Make up to 1 litre with deionised water. Autoclave at 15 psi for 15
    minutes."}], "decision": "evidence_only", "rationale": "The target already retains
    the 1 litre makeup and 15 psi / 15 minute autoclave instruction. The owner correctly
    adds the missing 5 ml of each stock and separates mixing from autoclaving. All
    these stated numbers are supported; no temperature, incubation period or organism-specific
    condition is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CH.yaml",
    "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action":
    "AUTOCLAVE", "description": "Make up to 1 litre with deionised water. Autoclave
    at 15 psi for 15 minutes."}, "decision": "evidence_only", "rationale": "The target
    already retains the 1 litre makeup and 15 psi / 15 minute autoclave instruction.
    The owner correctly adds the missing 5 ml of each stock and separates mixing from
    autoclaving. All these stated numbers are supported; no temperature, incubation
    period or organism-specific condition is inferred."}, {"path": "data/normalized_yaml/bacterial/ch.yaml",
    "field_path": "preparation_steps[0]", "stored_value": {"step_number": 1, "action":
    "MIX", "description": "Add 5 ml of each stock solution and make up to 1 L with
    deionized water."}, "decision": "evidence_only", "rationale": "The target already
    retains the 1 litre makeup and 15 psi / 15 minute autoclave instruction. The owner
    correctly adds the missing 5 ml of each stock and separates mixing from autoclaving.
    All these stated numbers are supported; no temperature, incubation period or organism-specific
    condition is inferred."}, {"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path":
    "preparation_steps[1]", "stored_value": {"step_number": 2, "action": "AUTOCLAVE",
    "description": "Autoclave at 15 psi for 15 minutes."}, "decision": "evidence_only",
    "rationale": "The target already retains the 1 litre makeup and 15 psi / 15 minute
    autoclave instruction. The owner correctly adds the missing 5 ml of each stock
    and separates mixing from autoclaving. All these stated numbers are supported;
    no temperature, incubation period or organism-specific condition is inferred."},
    {"path": "data/normalized_yaml/bacterial/ch.yaml", "field_path": "sterilization.method",
    "stored_value": "AUTOCLAVE", "decision": "evidence_only", "rationale": "The target
    already retains the 1 litre makeup and 15 psi / 15 minute autoclave instruction.
    The owner correctly adds the missing 5 ml of each stock and separates mixing from
    autoclaving. All these stated numbers are supported; no temperature, incubation
    period or organism-specific condition is inferred."}]}]'
- assessment_id: a4
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: supported
  summary: 'All 14 current chemical term slots agree with the four fresh OLS objects
    and exact current packaged catalog rows: sodium chloride, potassium chloride,
    calcium dichloride and water. Medium accession C22 is separately scoped and is
    not tested as a chemical-catalog identifier. No unsupported hydrate or alternate
    chemical form is introduced.'
  target_ids:
  - CultureMech:000330
  evidence_ids:
  - grounding
- assessment_id: a5
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Complete target and owner histories plus all four exact historical reports
    were read. Five October source objects and its raw digest match the fresh API
    capture, but missing attached evidence remains. The historical API failure and
    repair-event access assertions are retained as historical claims; new context
    is append-only.
  target_ids:
  - CultureMech:000330
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
  - CultureMech:000330
  evidence_ids:
  - local-target
- assessment_id: a7
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:000330
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-000330-regenerate-from-repaired-stocks-and-qualify-final-water-makeup
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Regenerate from repaired stocks and qualify final water makeup
  description: Each target ingredient is 5 G_PER_L, although both current sources
    describe 5 ml additions from three different stocks. The maintained owner already
    has 20, 0.8 and 1.2 g/L stock concentrations and 5 ml/L doses. Preserve those
    owner repairs and regenerate; do not apply the stale error to the owner. Qualify
    the owner water 1 L as makeup to the final litre, rather than a fixed additional
    solvent dose. Target preparation already retains the autoclave instruction.
  target_ids:
  - CultureMech:000330
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  - data/normalized_yaml/bacterial/ch.yaml::ingredients[0].concentration
  evidence_ids:
  - ccapCH
  - apiC22
  - quantities
  - writer-ch-repair
  - writer-merge
  rule_id: P2.3
  native_severity: P2
  normalization_reason: 'Major: P2.3 concentration-interpretation concern is generalized
    here to a documented volume-to-mass and solution-stage mismatch; this is not an
    assertion that G_PER_L is intrinsically invalid for this physical state.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ch.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-000330-align-categorical-use-with-primary-freshwater-protozoan-scope
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Align categorical use with primary freshwater protozoan scope
  description: CCAP explicitly calls CH a Freshwater Protozoa medium. The bacterial
    category is a source-scope mismatch; generic Microbial cultivation does not establish
    bacterial growth. The separate algae owner and current importer defaults likewise
    do not establish algae-specific light, temperature or strain claims.
  target_ids:
  - CultureMech:000330
  field_paths:
  - category
  - applications
  evidence_ids:
  - ccapCH
  - comparison-algae
  - writer-ccap
  rule_id: P2.4
  native_severity: P2
  normalization_reason: 'Minor: category mismatch is supported by the primary general
    application, but no strain-specific growth claim or chemical formulation is changed;
    the organizational scope can be clarified without guessing a new taxon.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ch.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-000330-attach-exact-stock-and-preparation-evidence-append-only
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attach exact stock and preparation evidence append only
  description: The owner has a source URL, a repair note and retained history but
    lacks attached claim-level evidence. Fresh API bytes exactly authenticate the
    cited October raw response and five literal objects, not the historical retrieval
    event or its blanket conflict labels. September recommendations remain derivative;
    its reported old API failure is superseded only by this separately dated successful
    capture.
  target_ids:
  - CultureMech:000330
  field_paths:
  - ingredients
  - solutions
  - evidence
  - curation_history
  evidence_ids:
  - apiC22
  - ccapCH
  - historical-reader
  - history
  - writer-source-repair
  rule_id: P4.3
  native_severity: P4
  normalization_reason: 'Minor: source URL is retained in notes, but claim-level stock/preparation
    linkage and explicit reference placement are missing; source bytes are available
    and no new formulation is inferred.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ch.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Preserve the three repaired owner stock objects and doses; add explicit
    water-makeup scope at the water field, attach exact primary evidence and regenerate
    the target from that owner. Confirm no direct 5 g/L salt row and no duplicated
    stock contribution remains.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000330
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ch.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Represent the stated freshwater-protozoan source scope in supported
    schema fields and explanatory text, resolving categorical placement without inferring
    a taxon-specific growth claim or copying generic algae defaults. Keep the distinct
    stable IDs and source identity explicit.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000330
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ch.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Attach exact stock-composition evidence at supported ingredient slots
    and root evidence with precise stock/dose/preparation locators. Preserve every
    original history event unchanged and append new verified context; do not rewrite
    earlier access claims or force a cross-category merge.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000330
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ch.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- The CCAP reference to Chalkley (1930) is read as the PDF bibliography; the original
  paper was not acquired and no DOI or paper-derived formulation is asserted.
- Freshwater Protozoa is a general source application, not strain-level growth evidence.
  Same-name algae metadata and generic importer conditions are excluded from transfer.
- The primary specifies final makeup to 1 litre; the exact water addition before adjustment
  is not specified. No fixed 985 ml solvent inference is made.
- Current source agreement and historical raw-byte equality do not authenticate historical
  execution, retrieval time or every derivative recommendation.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
