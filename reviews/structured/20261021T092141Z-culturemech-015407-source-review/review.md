# Source and formulation review: a1_marine_medium (CultureMech:015407)

- Review: 20261021T092141Z-culturemech-015407-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T09:12:11Z
- Finished UTC: 2026-10-21T09:21:41Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

A1 MARINE MEDIUM retains JCM 425 identity but imports five basal g/L values from a provider denominator inconsistent with its own preparation prose, and imports thirteen stock concentrations as direct medium ingredients. The current JCM recipe differs materially from MediaDive in iron source and preparation. Both local layers require source-version reconciliation and restoration of stock/stage boundaries.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 129; batch 013 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twelve task batches contain 120 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 122 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:015407 | data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml | generated | a1_marine_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:015407 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:015407 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch013/129/strict.tsv |
| validate-terms | passed | True | CultureMech:015407 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:015407 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:015407 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:015407.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: concern. Targets: CultureMech:015407.

18 primary CHEBI identities resolve with matching labels; 18 of 18 current secondary keys have live pinned-index rows. Unresolved keys: []. Canonical labels and MIM keys resolve, but source support for calcium-pantothenate stereochemistry and sodium-acetate hydration is unresolved; see forms assessment.

18 direct ingredient instances; CHEBI-primary instance linkage 18/18 (100.00%), verified secondary coverage 18/18 (100.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Exact accession and generated-owner correspondence

identity: supported. Targets: CultureMech:015407.

The sole normalized owner shares stable ID015407 and explicit merge provenance with the generated target. Both identify JCM 425 via MediaDive J425. This establishes accession identity, while source-version differences remain a separate concern.

### Every direct concentration and original preparation stage

quantity: concern. Targets: CultureMech:015407.

All 18 direct concentrations were assessed. The first five copy provider g_l based on50 ml despite contradictory one-liter prose; thirteen others belong to acetate/APM/vitamin stocks. The stock dose and definition boundaries are absent. Six additional assembly decisions cover missing or conflicting source ingredients, doses and solvent; nine further decisions retain stock-procedure strengths and their applicability limits.

[{"field_path": "ingredients[0].concentration", "name": "NaCl", "stored": {"value": "400", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Main sol. J425", "original_amount": 20, "original_unit": "g", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[1] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 400,\n                        \"mmol_l\": 6844.63,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Basal mass 20 g. Provider g_l equals this mass divided by 0.05 L, but provider preparation says bring to 1.0 L before separate acetate/APM additions. Current primary agrees with the literal basal mass. Retain original quantities and stage; do not interpret the stored g/L as source-verified or infer an exact final concentration."}, {"field_path": "ingredients[1].concentration", "name": "KCl", "stored": {"value": "15.4", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Main sol. J425", "original_amount": 0.77, "original_unit": "g", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[2] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.77,\n                        \"unit\": \"g\",\n                        \"g_l\": 15.4,\n                        \"mmol_l\": 206.573,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Basal mass 0.77 g. Provider g_l equals this mass divided by 0.05 L, but provider preparation says bring to 1.0 L before separate acetate/APM additions. Current primary agrees with the literal basal mass. Retain original quantities and stage; do not interpret the stored g/L as source-verified or infer an exact final concentration."}, {"field_path": "ingredients[2].concentration", "name": "NH4Cl", "stored": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Main sol. J425", "original_amount": 0.25, "original_unit": "g", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[3] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 93.4754,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Basal mass 0.25 g. Provider g_l equals this mass divided by 0.05 L, but provider preparation says bring to 1.0 L before separate acetate/APM additions. Current primary agrees with the literal basal mass. Retain original quantities and stage; do not interpret the stored g/L as source-verified or infer an exact final concentration."}, {"field_path": "ingredients[3].concentration", "name": "KH2PO4", "stored": {"value": "2", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Main sol. J425", "original_amount": 0.1, "original_unit": "g", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[4] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 14.6966,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Basal mass 0.1 g. Provider g_l equals this mass divided by 0.05 L, but provider preparation says bring to 1.0 L before separate acetate/APM additions. Current primary agrees with the literal basal mass. Retain original quantities and stage; do not interpret the stored g/L as source-verified or infer an exact final concentration."}, {"field_path": "ingredients[4].concentration", "name": "MgSO4 x 7 H2O", "stored": {"value": "4", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Main sol. J425", "original_amount": 0.2, "original_unit": "g", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[5] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 4,\n                        \"mmol_l\": 16.2288,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Basal mass 0.2 g. Provider g_l equals this mass divided by 0.05 L, but provider preparation says bring to 1.0 L before separate acetate/APM additions. Current primary agrees with the literal basal mass. Retain original quantities and stage; do not interpret the stored g/L as source-verified or infer an exact final concentration."}, {"field_path": "ingredients[5].concentration", "name": "Sodium acetate", "stored": {"value": "41", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Acetate solution 41.0 g/L", "original_amount": 41, "original_unit": "g", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[1].recipe[0] (solution id 4162)", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Sodium acetate\",\n                        \"compound_id\": 731,\n                        \"amount\": 41,\n                        \"unit\": \"g\",\n                        \"g_l\": 41,\n                        \"mmol_l\": 499.817,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[8] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Acetate solution 41.0 g/L\",\n                        \"solution_id\": 4162,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[1].recipe[1] (solution id 4162)", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Provider acetate stock is41 g in 1000 ml water and is added as10 ml; current JCM 425 instead lists 0.41 g acetate directly. The flat 41 G_PER_L value is the stock concentration. The stock dose contains 0.41 g by 41 g/L x0.010 L; this arithmetic does not establish final-medium g/L. Source sodium-acetate hydration is unstated; the asserted CHEBI term represents the anhydrous salt. No hydrate or molar conversion is inferred."}, {"field_path": "ingredients[6].concentration", "name": "MgCl2 x 6 H2O", "stored": {"value": "21.2", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "APM salts solution", "original_amount": 21.2, "original_unit": "g", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[2].recipe[0] (solution id 4163)", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 21.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 21.2,\n                        \"mmol_l\": 104.278,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[9] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"solution\": \"APM salts solution\",\n                        \"solution_id\": 4163,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[2].recipe[2] (solution id 4163)", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "APM stock mass in 1000 ml water, with 20 ml added to the medium. Both source representations retain this stock/dose boundary. Stored g/L is the undiluted stock value; no final-volume concentration is inferred."}, {"field_path": "ingredients[7].concentration", "name": "CaCl2 x 2 H2O", "stored": {"value": "3.04", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "APM salts solution", "original_amount": 3.04, "original_unit": "g", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[2].recipe[1] (solution id 4163)", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 3.04,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.04,\n                        \"mmol_l\": 20.6782,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[9] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"solution\": \"APM salts solution\",\n                        \"solution_id\": 4163,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[2].recipe[2] (solution id 4163)", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "APM stock mass in 1000 ml water, with 20 ml added to the medium. Both source representations retain this stock/dose boundary. Stored g/L is the undiluted stock value; no final-volume concentration is inferred."}, {"field_path": "ingredients[8].concentration", "name": "Biotin", "stored": {"value": "0.002", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Trace vitamins", "original_amount": 2, "original_unit": "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[0] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00818632,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium. The stored g/L matches stock strength after mg-to-g conversion, not the final medium concentration."}, {"field_path": "ingredients[9].concentration", "name": "Folic acid", "stored": {"value": "0.002", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Trace vitamins", "original_amount": 2, "original_unit": "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[1] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00453104,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium. The stored g/L matches stock strength after mg-to-g conversion, not the final medium concentration."}, {"field_path": "ingredients[10].concentration", "name": "Pyridoxine hydrochloride", "stored": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Trace vitamins", "original_amount": 10, "original_unit": "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[2] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0486287,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium. The stored g/L matches stock strength after mg-to-g conversion, not the final medium concentration."}, {"field_path": "ingredients[11].concentration", "name": "Thiamine HCl", "stored": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Trace vitamins", "original_amount": 5, "original_unit": "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[3] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0148236,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium. The stored g/L matches stock strength after mg-to-g conversion, not the final medium concentration."}, {"field_path": "ingredients[12].concentration", "name": "Riboflavin", "stored": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Trace vitamins", "original_amount": 5, "original_unit": "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[4] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0132837,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium. The stored g/L matches stock strength after mg-to-g conversion, not the final medium concentration."}, {"field_path": "ingredients[13].concentration", "name": "Nicotinic acid", "stored": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Trace vitamins", "original_amount": 5, "original_unit": "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[5] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0406141,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium. The stored g/L matches stock strength after mg-to-g conversion, not the final medium concentration."}, {"field_path": "ingredients[14].concentration", "name": "Calcium pantothenate", "stored": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Trace vitamins", "original_amount": 5, "original_unit": "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[6] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0104925,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium. The stored g/L matches stock strength after mg-to-g conversion, not the final medium concentration. Source Calcium pantothenate does not specify the D stereochemistry encoded by CHEBI:31345. Exact source-form support remains unresolved."}, {"field_path": "ingredients[15].concentration", "name": "Vitamin B12", "stored": {"value": "0.0001", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Trace vitamins", "original_amount": 0.1, "original_unit": "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[7] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\": 7.3779e-5,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium. The stored g/L matches stock strength after mg-to-g conversion, not the final medium concentration."}, {"field_path": "ingredients[16].concentration", "name": "p-Aminobenzoic acid", "stored": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Trace vitamins", "original_amount": 5, "original_unit": "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[8] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0364591,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium. The stored g/L matches stock strength after mg-to-g conversion, not the final medium concentration."}, {"field_path": "ingredients[17].concentration", "name": "Lipoic acid", "stored": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Trace vitamins", "original_amount": 5, "original_unit": "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[9] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Lipoic acid\",\n                        \"compound_id\": 368,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.024233,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10] (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium. The stored g/L matches stock strength after mg-to-g conversion, not the final medium concentration."}, {"field_path": "solutions (missing iron source)", "name": "Iron assembly", "stored": "No structured descriptor in either local layer", "decision": "conflict", "source_snippets": [{"source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=425", "source_locator": "Main recipe, iron stock row", "exact_source_quote": "Iron(III)citrate solution (see Medium No. 1014 ) 50.0 ml", "snapshot_sha256": "d8f5facb349061ab14a980bf62847270322eb86e86ef4a66f5d2ae4c2f9ef9ee", "parsed_text_sha256": "12974af5f451d14fbe4d69e335251b4c926f477c2531d237b2e433062f36caac"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[0] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Poorly crystalline iron(III) oxide\",\n                        \"solution_id\": 4143,\n                        \"amount\": 100,\n                        \"unit\": \"mM\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Current primary 50 ml iron-citrate stock conflicts with provider 100 mM poorly crystalline iron(III) oxide. Do not silently identify the two species or derive an oxide volume from its assay-dependent suspension strength."}, {"field_path": "solutions (missing trace-mineral dose)", "name": "Trace minerals", "stored": "No structured descriptor in either local layer", "decision": "add", "source_snippets": [{"source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=425", "source_locator": "Main recipe, trace-mineral row", "exact_source_quote": "Trace mineral solution (see Medium No. 411 ) 10.0 ml", "snapshot_sha256": "d8f5facb349061ab14a980bf62847270322eb86e86ef4a66f5d2ae4c2f9ef9ee", "parsed_text_sha256": "12974af5f451d14fbe4d69e335251b4c926f477c2531d237b2e433062f36caac"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[7] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Trace mineral solution\",\n                        \"solution_id\": 4144,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Both sources specify 10 ml of the source-linked modified trace-mineral stock. Preserve JCM 411→151 definition and its final molybdate wording."}, {"field_path": "solutions (missing vitamin dose)", "name": "Trace vitamins", "stored": "No structured descriptor in either local layer", "decision": "add", "source_snippets": [{"source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=425", "source_locator": "Post-cooling addition table", "exact_source_quote": "Trace vitamins* (see Medium No. 197 ) 10.0 ml", "snapshot_sha256": "d8f5facb349061ab14a980bf62847270322eb86e86ef4a66f5d2ae4c2f9ef9ee", "parsed_text_sha256": "12974af5f451d14fbe4d69e335251b4c926f477c2531d237b2e433062f36caac"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Both specify 10 ml; the current primary marks this stock for filter sterilization. The ten vitamin ingredients belong to its stock definition."}, {"field_path": "solutions (missing APM dose)", "name": "APM salts", "stored": "No structured descriptor in either local layer", "decision": "add", "source_snippets": [{"source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=425", "source_locator": "Post-cooling addition table", "exact_source_quote": "APM salts solution (see below) 20.0 ml", "snapshot_sha256": "d8f5facb349061ab14a980bf62847270322eb86e86ef4a66f5d2ae4c2f9ef9ee", "parsed_text_sha256": "12974af5f451d14fbe4d69e335251b4c926f477c2531d237b2e433062f36caac"}, {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[9] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"solution\": \"APM salts solution\",\n                        \"solution_id\": 4163,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Both specify 20 ml of the defined APM stock. Do not keep its stock masses as medium g/L."}, {"field_path": "ingredients/solutions (missing bicarbonate)", "name": "Bicarbonate stock", "stored": "No structured descriptor in either local layer", "decision": "conflict", "source_snippets": [{"source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=425", "source_locator": "Post-cooling addition table", "exact_source_quote": "8%NaHCO 3 solution* 25.0 ml", "snapshot_sha256": "d8f5facb349061ab14a980bf62847270322eb86e86ef4a66f5d2ae4c2f9ef9ee", "parsed_text_sha256": "12974af5f451d14fbe4d69e335251b4c926f477c2531d237b2e433062f36caac"}], "assessment": "Current primary supplies 25 ml of an8% stock, absent from provider/local assembly. Percent basis is not explicitly stated here; do not infer a mass or replace the provider variant without source-version resolution."}, {"field_path": "preparation_steps (solvent basis)", "name": "Water", "stored": "No structured descriptor in either local layer", "decision": "conflict", "source_snippets": [{"source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=425", "source_locator": "Main recipe, solvent row", "exact_source_quote": "Distilled water 940.0 ml", "snapshot_sha256": "d8f5facb349061ab14a980bf62847270322eb86e86ef4a66f5d2ae4c2f9ef9ee", "parsed_text_sha256": "12974af5f451d14fbe4d69e335251b4c926f477c2531d237b2e433062f36caac"}], "assessment": "Current primary uses 940 ml water plus listed stocks before later additions; provider prose brings its main stage to 1.0 L before separate stocks. These bases must remain separate. No measured final volume or density conversion is claimed."}, {"field_path": "preparation_steps[1].description", "name": "Iron-stock precursor", "decision": "evidence_only", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[3].steps[0].step (solution id 4143)", "exact_source_quote": "Dissolve 108 g FeCl3 in 1.0 L distilled water.", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "This is the provider oxide-stock precursor step, not a final-medium iron dose; washing and resuspension prevent treating precursor mass as retained product mass."}, {"field_path": "preparation_steps[1].description", "name": "Stock pH adjuster", "decision": "not_quantified", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[3].steps[0].step (solution id 4143)", "exact_source_quote": "10 N NaOH", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Strength is given, but addition amount is not quantified; no dry-solute amount or normality-to-molarity conversion is inferred."}, {"field_path": "preparation_steps[1].description", "name": "Iron suspension strength", "decision": "evidence_only", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[3].steps[0].step (solution id 4143)", "exact_source_quote": "Use the Fe(III) suspension as 0.67 M solution.", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Retain the nominal source stock-strength statement alongside its assay instruction. It is not a measured result in this review and does not identify the current primary iron-citrate alternative."}, {"field_path": "preparation_steps[1].description", "name": "Chloride assay criterion", "decision": "evidence_only", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[3].steps[0].step (solution id 4143)", "exact_source_quote": "the concentration of Cl- to be less than 1 mM", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "This is an analytical criterion for the washed stock, not chloride added to the medium."}, {"field_path": "preparation_steps[2].description", "name": "Modified trace-stock molybdate", "decision": "evidence_only", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[5].steps[0].step (solution id 4144)", "exact_source_quote": "0.025 g (final) Na2MoO4 x 2H2O", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "The source explicitly says final in the per-liter trace stock. Do not add this amount again to the parent 0.01 g molybdate."}, {"field_path": "preparation_steps[2].description", "name": "Modified trace-stock nickel", "decision": "evidence_only", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[5].steps[0].step (solution id 4144)", "exact_source_quote": "0.024 g NiCl2 x 6H2O", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Per-liter modified trace-stock amount, not a final-medium concentration; its 10 ml addition remains separately represented."}, {"field_path": "preparation_steps[2].description", "name": "Modified trace-stock tungstate", "decision": "evidence_only", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[5].steps[0].step (solution id 4144)", "exact_source_quote": "0.025 g Na2WO4 x 2H2O (per liter)", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Per-liter modified trace-stock amount, not a final-medium concentration."}, {"field_path": "preparation_steps[0].description", "name": "Gas mixture", "decision": "not_quantified", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].steps[0].step (solution id 4161)", "exact_source_quote": "N2-CO2 (4:1, v/v)", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "Preparation gas ratio is explicit, but no fixed mass or final-medium concentration is supplied. Retain stage-specific nitrogen handling separately."}, {"field_path": "preparation_steps[3].description", "name": "Inherited strain-specific inoculum", "decision": "unsupported", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[5].steps[1].step (solution id 4144)", "exact_source_quote": "For strain JCM 12378, inoculate with a 10% inoculum.", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment": "The provider attaches this comment to trace stock 4144; its primary location is JCM 411. Target-specific applicability to JCM 425 is unsupported; no target growth or taxonomy assertion follows."}]

### Current collection recipe versus provider representation

provenance: concern. Targets: CultureMech:015407.

The primary lists iron citrate, direct acetate and later bicarbonate additions; MediaDive lists iron oxide and acetate stock without bicarbonate, with different preparation wording. Both share the basal salt masses, pH6.8, trace-mineral/vitamin stock doses and APM dose. Their access dates do not establish recipe chronology. Choose and cite an exact version before any scientific correction.

### All named source stocks and nested reference boundaries

quantity: concern. Targets: CultureMech:015407.

Both local layers lack structured stock descriptors. Provider 4162 acetate is41 g with 1000 ml water,4163 APM is21.2 g magnesium chloride hexahydrate and 3.04 g calcium chloride dihydrate with 1000 ml water, and 3861 vitamins is a separate one-liter stock. Provider 4143 iron oxide is defined in prose and 4144 trace minerals by an external reference. Current primary uses the different iron-citrate stock and a bicarbonate stock. Fully inspected linked pages supply only their named stock subsections; unrelated basal recipes are excluded.

JCM 197 vitamin stock: biotin 2 mg, folic acid 2 mg, pyridoxine HCl 10 mg, thiamine HCl 5 mg, riboflavin 5 mg, nicotinic acid 5 mg, calcium pantothenate 5 mg, vitamin B12 0.1 mg, p-aminobenzoic acid 5 mg and lipoic acid 5 mg with 1 L water. JCM 151 trace minerals: nitrilotriacetic acid 1.5 g, MgSO4·7H2O 3 g, MnSO4·xH2O 0.5 g, NaCl 1 g, FeSO4·7H2O 0.1 g, CoSO4·7H2O 0.1 g, CaCl2·2H2O 0.1 g, ZnSO4·7H2O 0.1 g, CuSO4·5H2O 0.01 g, AlK(SO4)2 0.01 g, H3BO3 0.01 g, Na2MoO4·2H2O 0.01 g with 1 L water. JCM 411 specifies Mo0.025 g(final), NiCl2·6H2O 0.024 g and Na2WO4·2H2O 0.025 g per liter. Do not treat final Mo as an additional 0.025 g or invent the unspecified manganese/alum hydration. JCM 1014 iron citrate is2.4 g filled to 100 ml after its separate dissolution/pH sequence. No quoted stock mass is an approved final-medium dose.

### All asserted chemical forms and linkage scope

grounding: concern. Targets: CultureMech:015407.

All 18 direct ingredient instances have primary CHEBI links and current secondary keys, with canonical metadata verified separately. The basal and APM hydrates match their respective source stock forms. CHEBI:31345 has D-calcium-pantothenate synonyms and stereospecific structural annotations, while the source says only Calcium pantothenate; exact stereochemical support is unresolved. CHEBI:32954 encodes anhydrous sodium acetate, while source hydration is unstated. Neither observation alone proves a wrong ID, and no mass-to-molar conversion is made. Vitamin B12 remains a broad class at the source specificity. Valid terms do not repair the preparation-stage errors. Omitted iron source and trace-stock constituents require separate source-specific grounding after version selection.

### Preparation stages, pH and imported strain comment

completeness: concern. Targets: CultureMech:015407.

Target and owner reproduce provider main preparation, oxide-stock preparation, trace-stock definition and a JCM 12378 comment as one sequential medium procedure. The latter occurs under provider trace stock 4144 and on parent JCM 411, without target-specific growth support. The current primary has a different staged assembly, source-default autoclaving and marked filter-sterilized additions. Keep each stock procedure and version separate; pH6.8 is common medium context, while oxide/trace/citrate pH values belong to their stocks.

### Physical state, composition and biological annotations

scope: supported. Targets: CultureMech:015407.

LIQUID and a defined chemical formulation agree with the listed sources; high_metal is consistent with their iron additions. These annotations do not make the incomplete quantitative assembly usable. No target_organisms, native variants, environment, gene or measured growth assertions occur. The imported JCM 12378 procedure comment must not be promoted into a target-specific organism association.

### History, evidence and present writer limitations

provenance: concern. Targets: CultureMech:015407.

All7 target and6 owner history timestamps parse with timezones. History records import, grounding and generation rather than scientific verification. Neither layer has claim-level formulation evidence; reference validation inspected zero excerpts. Current importer code now separates stock composition but still trusts supplied g_l and flattens preparation steps across solutions. This is current context, not proof of a historical run.

### Bibliographic locator embedded in oxide-stock procedure

provenance: concern. Targets: CultureMech:015407.

Author/year/pages match the registered paper but the source-inherited volume 54 differs from registered volume 52. The paper was checked for bibliographic identity only; its method was not independently assessed.

## Findings

### f1: Five basal concentrations use a conflicting provider denominator

blocker / open / confirmed; issue key: CM015407-basal-volume-normalization.

NaCl 400, KCl 15.4, NH4Cl 5, KH2PO4 2 and MgSO4·7H2O 4 G_PER_L reproduce MediaDive g_l calculated from its declared 50 ml volume. The same provider lists 20,0.77,0.25,0.1 and 0.2 g and specifies bringing the main stage to 1.0 L before later additions. Current JCM 425 agrees with those literal masses. Neither source supports the stored concentrations as final-medium values.

### f2: Thirteen stock concentrations appear as direct medium ingredients

blocker / open / confirmed; issue key: CM015407-stock-stage-collapse.

The acetate 41 G_PER_L, two APM values 21.2/3.04 G_PER_L and ten vitamin values are stock concentrations. Their 10/20/10 ml additions and separate stock definitions are absent from both local layers. Iron and trace-mineral assembly are not represented as structured ingredients or solutions. Correct chemical identifiers do not make the flattened quantities valid.

### f3: Primary and provider formulations differ materially

major / open / confirmed; issue key: CM015407-source-version-conflict.

Current JCM 425 uses iron(III)citrate and bicarbonate additions with a different acetate/preparation representation. MediaDive/local prose uses poorly crystalline iron(III)oxide and separate acetate stock. The sources share accession identity but are not interchangeable formulations, and capture timestamps establish no historical order.

### f4: Stock procedures and an unrelated strain comment became medium steps

major / open / confirmed; issue key: CM015407-preparation-scope-and-evidence.

Both local layers concatenate main preparation, oxide stock preparation, trace-stock wording and the JCM 12378 comment into one medium procedure. The strain comment is captured on JCM 411 and provider trace stock 4144 without JCM 425-specific support. Source-version-specific sterilization and additive stages require separate scope; claim-level formulation evidence is absent.

### f5: The embedded method citation has the wrong journal volume

minor / open / confirmed; issue key: CM015407-inherited-citation-volume.

The record and its provider/linked primary stock prose cite Lovley and Phillips, Appl. Environ. Microbiol.54,751–757,1986. Registration metadata for those authors/year/pages gives volume 52(4) and DOI 10.1128/aem.52.4.751-757.1986. This is an inherited bibliographic defect, not evidence that the analytical method itself is invalid.

### f6: Two ontology forms exceed explicit source detail

minor / open / confirmed; issue key: CM015407-source-chemical-form-specificity.

CHEBI:31345 includes D-calcium-pantothenate synonyms and stereospecific InChI/SMILES, but the vitamin source names only Calcium pantothenate. CHEBI:32954 represents anhydrous sodium acetate while the recipe name does not state hydration. The asserted labels and IDs are valid; exact source-form support remains unresolved and no alternative form is proved.

## Recommended Actions And Acceptance Checks

### a1

Retain exact masses and preparation basis, resolve the source version, and derive concentrations only from a justified final-volume convention. Audit the importer reliance on provider g_l when it conflicts with source prose.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore source-specific stock identities, complete definitions, original units and addition stages in the maintained owner. Preserve nested reference overrides and uncertain forms; do not flatten stock concentrations or treat every linked parent recipe as inherited.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Identify and document the intended recipe version with exact source evidence before rebuilding the assembly. Preserve the alternative as a version/variant conflict rather than silently combining ingredients from both.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Separate medium and stock procedures, retain the intended version-specific instructions, and exclude or explicitly qualify the inherited strain comment without creating a growth assertion. Attach narrow source excerpts to quantities, stock identity and preparation claims.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Correct the bibliographic locator with DOI-backed metadata and preserve the source-transcription distinction. Assess the paper method separately before treating the procedure citation as analytical validation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Verify source-specific reagent form or document the residual uncertainty before claiming exact chemical-form grounding or deriving molar values. Do not replace either ID solely from the generic source label or invent a hydrate/stereoisomer.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/specialized/a1_marine_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch013/129/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch013/129/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/specialized/a1_marine_medium.yaml:1:id: CultureMech:015407<br>./data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml:1:id: CultureMech:015407<br> |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15940 resolves to nicotinic acid and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15956 resolves to biotin and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:16494 resolves to lipoic acid and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17015 resolves to riboflavin and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:176843 resolves to vitamin B12 and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:27470 resolves to folic acid and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:30753 resolves to 4-aminobenzoic acid and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:30961 resolves to pyridoxine hydrochloride and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31206 resolves to ammonium chloride and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31345 resolves to Calcium pantothenate and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32588 resolves to potassium chloride and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32954 resolves to sodium acetate and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:49105 resolves to thiamine hydrochloride and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86158 resolves to calcium chloride dihydrate and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate and is not obsolete. This verifies term metadata; source chemical form and preparation stage are assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32954": [{"label": "Na-acetate", "match_type": "preferred_term", "identifier": "CHEBI:32954", "preferred_term": "Na-acetate", "ontology_id": "CHEBI:32954", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31345": [{"label": "Calcium pantothenate", "match_type": "preferred_term", "identifier": "CHEBI:31345", "preferred_term": "Calcium pantothenate", "ontology_id": "CHEBI:31345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| jcm425 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=425; Entire JCM 425 main recipe, post-sterilization additions, APM subsection and default sterilization statement | supports | The current exact primary lists five basal salts, sodium acetate, trace minerals, iron(III) citrate stock and water, followed by bicarbonate, trace vitamins and APM additions. It gives pH 6.8 and staged anaerobic preparation. APM has its own one-liter stock recipe. It does not reproduce the provider iron-oxide/acetate-stock assembly. |
| provider | https://mediadive.dsmz.de/rest/medium/J425; $.data.medium and all six $.data.solutions with their recipes, volume and steps | supports | MediaDive identifies J425 and the exact JCM URL. Main solution 4161 has volume 50 and five calculated g_l values that are twenty times the literal gram quantities, despite prose specifying a one-liter preparation before separate additions. Its subsequent entries define acetate 4162, APM4163, iron oxide 4143, trace vitamins 3861 and trace minerals 4144. These are stock definitions, not additional direct medium ingredients. |
| jcm411 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=411; Trace mineral solution subsection; separate final JCM 12378 comment location | supports | JCM 425 explicitly links the trace-mineral subsection, which in turn uses JCM 151 trace minerals with specified Mo/Ni/W supplementation. The final JCM 12378 inoculum comment occurs on the JCM 411 page. It is not evidence that this instruction applies to JCM 425. |
| jcm1014 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1014; Iron(III) citrate solution subsection only | supports | The explicitly linked stock mixes 2.4 g iron(III) citrate with 90 ml water, dissolves by boiling, adjusts pH6.0 with 10 N NaOH and fills to 100 ml. These quantities and pH belong to the stock; the unrelated basal recipe of1014 is outside this target scope. |
| jcm197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Trace vitamins subsection only | supports | The explicitly linked one-liter vitamin stock lists ten vitamin masses, matching the provider stock values. The unrelated basal medium and its reducers are not components of JCM 425. |
| jcm151 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151; Trace minerals subsection and its pH preparation only | supports | The trace stock contains twelve named solutes with one-liter water context. Its preparation dissolves nitrilotriacetic acid and adjusts pH6.5 before adding minerals, then final pH7.0. The sulfur-containing basal Pyrococcus medium is not inherited by JCM 425. JCM 411 modifies the trace stock; retain its stated final molybdate amount rather than silently adding it to the parent amount. |
| writer | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition code separates the first formulation from subsequent stock definitions, but still trusts supplied g_l. Current preparation code collects steps from every provider solution into one list. These inspected current behaviors explain relevant transformation risks; no historical importer execution was replayed and no regeneration was run. |
| quantities | /private/tmp/culturemech-review-work-batch013/129/quantity-inventory.json; 18 direct claims, 6 missing/source-conflicting assembly descriptors, and 9 stock/procedure claims | context_only | All 33 decisions retain exact source snippets and locators; unit conversion and stage interpretation are kept separate from quotes. |
| citation-metadata | https://api.crossref.org/works/10.1128%2Faem.52.4.751-757.1986; $.message DOI, authors, journal volume, pages and publication date | refutes | Registration metadata identifies Lovley and Phillips, 1986, volume 52(4), pages 751–757, DOI 10.1128/aem.52.4.751-757.1986. The local/provider/linked JCM 411 text says volume 54. This bibliographic check does not verify the described analytical method or growth. |

## Limits And Additional Notes

- The current primary and captured provider formulations are different representations of the same accession. Their chronological relationship is not established; no historical replacement sequence or approved reconstructed recipe is asserted.
- No measured final volume, percent-strength convention, unprovided chemical form, strain taxonomy, incubation optimum or experimental growth result is inferred. Completion means the defects and source conflict were assessed, not resolved by editing a recipe.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T092141Z-culturemech-015407-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: a1_marine_medium (CultureMech:015407)'
started_at: '2026-10-21T09:12:11Z'
finished_at: '2026-10-21T09:21:41Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify the assessed recipe bytes.
    This is an independent agent review of captured local inputs and inspected primary/database
    sources, not experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: A1 MARINE MEDIUM retains JCM 425 identity but imports five basal g/L values
  from a provider denominator inconsistent with its own preparation prose, and imports
  thirteen stock concentrations as direct medium ingredients. The current JCM recipe
  differs materially from MediaDive in iron source and preparation. Both local layers
  require source-version reconciliation and restoration of stock/stage boundaries.
source:
  git_revision: 24a1d277eb7f0437af53af0d178a30f9bfa6374c
  state: working_tree
  inputs:
  - path: .claude/skills/audit-schema-gaps/SKILL.md
    sha256: 86467f280ecdd2d60531d3b2a9249d7a38efa4cfeab714d55421b9a62cfabb7d
    role: context
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
  - path: .claude/skills/schema-gap-analysis/SKILL.md
    sha256: 09665fe53584559e776f75ab41dfabd997eff0cac10bafcca0a721b678ccee93
    role: context
  - path: AGENTS.md
    sha256: 72737a531548de8636bcf70b972e71a7630a0e579215b6ded392d88d1b51a4fc
    role: context
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/oak_config.yaml
    sha256: e35781d4fd66de4289411141b4c8a94189782d864ba6c45e49bf46537c46c5a1
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml
    sha256: 1264d14720521718dd4e6eefe614f263cd8c5dff0074261afbaf983f611ca59a
    role: target
  - path: data/normalized_yaml/specialized/a1_marine_medium.yaml
    sha256: cf7d100e61cbf498cfced469a32d8b1e533e7fcb173e80f7899cf8d4a37efd4a
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
    sha256: 3576f5ce2adee0179be4f2d3fd134841249eb9a54a7eed8b388c3b345883a5fe
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/mediadive_raw_yaml.py
    sha256: 70ba720001705c315f2c5bd40871e08f6f429b6229c78255e6c94dfdcc482432
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
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
  - path: src/culturemech/merge/merge_recipes.py
    sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 129; batch 013 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twelve task batches contain
    120 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 122 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:015407
targets:
- target_id: CultureMech:015407
  path: data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml
  label: a1_marine_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/a1_marine_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:015407
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch013/129/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch013/129/strict.tsv"
  target_ids:
  - CultureMech:015407
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:015407
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:015407
  evidence_ids:
  - validate-references
- check_id: structured-source-adapter
  name: iModulonDB applicability
  required: false
  status: not_applicable
  summary: The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic
    dataset requiring an iModulonDB cross-check; expression-module membership cannot
    establish this formulation.
  target_ids:
  - CultureMech:015407
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T09:21:39Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/specialized/a1_marine_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T09:21:39Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:13.599033Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch013/129/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:21.399754Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch013/129/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:26.678583Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:29.615387Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T09:21:39Z'
  support: supports
  summary: './data/normalized_yaml/specialized/a1_marine_medium.yaml:1:id: CultureMech:015407

    ./data/merge_yaml/merged/A1_MARINE_MEDIUM.yaml:1:id: CultureMech:015407

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: CHEBI:15940 resolves to nicotinic acid and is not obsolete. This verifies
    term metadata; source chemical form and preparation stage are assessed separately.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: CHEBI:15956 resolves to biotin and is not obsolete. This verifies term
    metadata; source chemical form and preparation stage are assessed separately.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16494
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:13.001958Z'
  support: supports
  summary: CHEBI:16494 resolves to lipoic acid and is not obsolete. This verifies
    term metadata; source chemical form and preparation stage are assessed separately.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: CHEBI:17015 resolves to riboflavin and is not obsolete. This verifies term
    metadata; source chemical form and preparation stage are assessed separately.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: CHEBI:176843 resolves to vitamin B12 and is not obsolete. This verifies
    term metadata; source chemical form and preparation stage are assessed separately.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies
    term metadata; source chemical form and preparation stage are assessed separately.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: CHEBI:27470 resolves to folic acid and is not obsolete. This verifies term
    metadata; source chemical form and preparation stage are assessed separately.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: CHEBI:30753 resolves to 4-aminobenzoic acid and is not obsolete. This verifies
    term metadata; source chemical form and preparation stage are assessed separately.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: CHEBI:30961 resolves to pyridoxine hydrochloride and is not obsolete. This
    verifies term metadata; source chemical form and preparation stage are assessed
    separately.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: CHEBI:31206 resolves to ammonium chloride and is not obsolete. This verifies
    term metadata; source chemical form and preparation stage are assessed separately.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: CHEBI:31345 resolves to Calcium pantothenate and is not obsolete. This
    verifies term metadata; source chemical form and preparation stage are assessed
    separately.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete.
    This verifies term metadata; source chemical form and preparation stage are assessed
    separately.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: CHEBI:32588 resolves to potassium chloride and is not obsolete. This verifies
    term metadata; source chemical form and preparation stage are assessed separately.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi32954
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:00:48.206583Z'
  support: supports
  summary: CHEBI:32954 resolves to sodium acetate and is not obsolete. This verifies
    term metadata; source chemical form and preparation stage are assessed separately.
  snapshot_sha256: 573cba85f57c363463610a20b17be618893d6432ba239604fbd8aa562f98161b
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: CHEBI:49105 resolves to thiamine hydrochloride and is not obsolete. This
    verifies term metadata; source chemical form and preparation stage are assessed
    separately.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete.
    This verifies term metadata; source chemical form and preparation stage are assessed
    separately.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate and is not obsolete.
    This verifies term metadata; source chemical form and preparation stage are assessed
    separately.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: CHEBI:86345 resolves to magnesium dichloride hexahydrate and is not obsolete.
    This verifies term metadata; source chemical form and preparation stage are assessed
    separately.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T09:21:39Z'
  support: supports
  summary: '{"CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier":
    "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type":
    "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id":
    "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label":
    "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32954":
    [{"label": "Na-acetate", "match_type": "preferred_term", "identifier": "CHEBI:32954",
    "preferred_term": "Na-acetate", "ontology_id": "CHEBI:32954", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type":
    "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id":
    "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470":
    [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470",
    "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride",
    "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term":
    "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type":
    "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl",
    "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier":
    "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid",
    "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term":
    "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31345": [{"label": "Calcium pantothenate", "match_type": "preferred_term",
    "identifier": "CHEBI:31345", "preferred_term": "Calcium pantothenate", "ontology_id":
    "CHEBI:31345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843":
    [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843",
    "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status":
    "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:30753": [{"label": "p-Aminobenzoic
    acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term":
    "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic
    acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}'
- evidence_id: jcm425
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=425
  locator: Entire JCM 425 main recipe, post-sterilization additions, APM subsection
    and default sterilization statement
  accessed_at: '2026-10-21T09:01:28.983880Z'
  support: supports
  summary: The current exact primary lists five basal salts, sodium acetate, trace
    minerals, iron(III) citrate stock and water, followed by bicarbonate, trace vitamins
    and APM additions. It gives pH 6.8 and staged anaerobic preparation. APM has its
    own one-liter stock recipe. It does not reproduce the provider iron-oxide/acetate-stock
    assembly.
  snapshot_sha256: d8f5facb349061ab14a980bf62847270322eb86e86ef4a66f5d2ae4c2f9ef9ee
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J425
  locator: $.data.medium and all six $.data.solutions with their recipes, volume and
    steps
  accessed_at: '2026-10-21T09:01:27.528885Z'
  support: supports
  summary: MediaDive identifies J425 and the exact JCM URL. Main solution 4161 has
    volume 50 and five calculated g_l values that are twenty times the literal gram
    quantities, despite prose specifying a one-liter preparation before separate additions.
    Its subsequent entries define acetate 4162, APM4163, iron oxide 4143, trace vitamins
    3861 and trace minerals 4144. These are stock definitions, not additional direct
    medium ingredients.
  snapshot_sha256: 908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee
- evidence_id: jcm411
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=411
  locator: Trace mineral solution subsection; separate final JCM 12378 comment location
  accessed_at: '2026-10-21T09:02:24.975436Z'
  support: supports
  summary: JCM 425 explicitly links the trace-mineral subsection, which in turn uses
    JCM 151 trace minerals with specified Mo/Ni/W supplementation. The final JCM 12378
    inoculum comment occurs on the JCM 411 page. It is not evidence that this instruction
    applies to JCM 425.
  snapshot_sha256: df41e941725d00c60920ded78ab026a04267371c171e2e691b8de2df8354b48f
- evidence_id: jcm1014
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1014
  locator: Iron(III) citrate solution subsection only
  accessed_at: '2026-10-21T09:02:24.974894Z'
  support: supports
  summary: The explicitly linked stock mixes 2.4 g iron(III) citrate with 90 ml water,
    dissolves by boiling, adjusts pH6.0 with 10 N NaOH and fills to 100 ml. These
    quantities and pH belong to the stock; the unrelated basal recipe of1014 is outside
    this target scope.
  snapshot_sha256: 00343a13344352b678e1e7c3d3dc5de970af9e4366f721c506b706505aa64f3c
- evidence_id: jcm197
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: Trace vitamins subsection only
  accessed_at: '2026-10-20T06:58:05.867253Z'
  support: supports
  summary: The explicitly linked one-liter vitamin stock lists ten vitamin masses,
    matching the provider stock values. The unrelated basal medium and its reducers
    are not components of JCM 425.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: jcm151
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151
  locator: Trace minerals subsection and its pH preparation only
  accessed_at: '2026-10-21T09:01:28.851101Z'
  support: supports
  summary: The trace stock contains twelve named solutes with one-liter water context.
    Its preparation dissolves nitrilotriacetic acid and adjusts pH6.5 before adding
    minerals, then final pH7.0. The sulfur-containing basal Pyrococcus medium is not
    inherited by JCM 425. JCM 411 modifies the trace stock; retain its stated final
    molybdate amount rather than silently adding it to the parent amount.
  snapshot_sha256: 6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7
- evidence_id: writer
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-21T09:21:39Z'
  support: context_only
  summary: Current composition code separates the first formulation from subsequent
    stock definitions, but still trusts supplied g_l. Current preparation code collects
    steps from every provider solution into one list. These inspected current behaviors
    explain relevant transformation risks; no historical importer execution was replayed
    and no regeneration was run.
- evidence_id: quantities
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch013/129/quantity-inventory.json
  locator: 18 direct claims, 6 missing/source-conflicting assembly descriptors, and
    9 stock/procedure claims
  accessed_at: '2026-10-21T09:21:39Z'
  support: context_only
  summary: All 33 decisions retain exact source snippets and locators; unit conversion
    and stage interpretation are kept separate from quotes.
  snapshot_sha256: 66733d2f1b7c031e3715c4c3fff345a87b3950791af739e6dbba12d3c31d760a
- evidence_id: citation-metadata
  kind: database
  reference: https://api.crossref.org/works/10.1128%2Faem.52.4.751-757.1986
  locator: $.message DOI, authors, journal volume, pages and publication date
  accessed_at: '2026-10-21T09:14:57.804624Z'
  support: refutes
  summary: Registration metadata identifies Lovley and Phillips, 1986, volume 52(4),
    pages 751–757, DOI 10.1128/aem.52.4.751-757.1986. The local/provider/linked JCM
    411 text says volume 54. This bibliographic check does not verify the described
    analytical method or growth.
  snapshot_sha256: 91e69377b95424ff4d8a91c693effc66dc141fc769fb19d17ae7dc06bbd9deef
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:015407
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: concern
  summary: '18 primary CHEBI identities resolve with matching labels; 18 of 18 current
    secondary keys have live pinned-index rows. Unresolved keys: []. Canonical labels
    and MIM keys resolve, but source support for calcium-pantothenate stereochemistry
    and sodium-acetate hydration is unresolved; see forms assessment.'
  target_ids:
  - CultureMech:015407
  evidence_ids:
  - record
  - mim
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi176843
  - chebi26710
  - chebi27470
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi31795
  - chebi32588
  - chebi32954
  - chebi49105
  - chebi63036
  - chebi86158
  - chebi86345
  - provider
  - jcm425
  - jcm197
  details: 18 direct ingredient instances; CHEBI-primary instance linkage 18/18 (100.00%),
    verified secondary coverage 18/18 (100.00%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Exact accession and generated-owner correspondence
  outcome: supported
  summary: The sole normalized owner shares stable ID015407 and explicit merge provenance
    with the generated target. Both identify JCM 425 via MediaDive J425. This establishes
    accession identity, while source-version differences remain a separate concern.
  target_ids:
  - CultureMech:015407
  evidence_ids:
  - record
  - owner-0
  - id-search
  - jcm425
  - provider
- assessment_id: quantities
  area: quantity
  topic: Every direct concentration and original preparation stage
  outcome: concern
  summary: All 18 direct concentrations were assessed. The first five copy provider
    g_l based on50 ml despite contradictory one-liter prose; thirteen others belong
    to acetate/APM/vitamin stocks. The stock dose and definition boundaries are absent.
    Six additional assembly decisions cover missing or conflicting source ingredients,
    doses and solvent; nine further decisions retain stock-procedure strengths and
    their applicability limits.
  target_ids:
  - CultureMech:015407
  evidence_ids:
  - record
  - owner-0
  - provider
  - jcm425
  - quantities
  details: '[{"field_path": "ingredients[0].concentration", "name": "NaCl", "stored":
    {"value": "400", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Main
    sol. J425", "original_amount": 20, "original_unit": "g", "source_snippets": [{"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[1]
    (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 400,\n                        \"mmol_l\":
    6844.63,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Basal mass 20 g. Provider g_l equals this mass divided by 0.05 L, but provider
    preparation says bring to 1.0 L before separate acetate/APM additions. Current
    primary agrees with the literal basal mass. Retain original quantities and stage;
    do not interpret the stored g/L as source-verified or infer an exact final concentration."},
    {"field_path": "ingredients[1].concentration", "name": "KCl", "stored": {"value":
    "15.4", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Main sol.
    J425", "original_amount": 0.77, "original_unit": "g", "source_snippets": [{"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[2]
    (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.77,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 15.4,\n                        \"mmol_l\":
    206.573,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Basal mass 0.77 g. Provider g_l equals this mass divided by 0.05 L, but provider
    preparation says bring to 1.0 L before separate acetate/APM additions. Current
    primary agrees with the literal basal mass. Retain original quantities and stage;
    do not interpret the stored g/L as source-verified or infer an exact final concentration."},
    {"field_path": "ingredients[2].concentration", "name": "NH4Cl", "stored": {"value":
    "5", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Main sol. J425",
    "original_amount": 0.25, "original_unit": "g", "source_snippets": [{"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[3]
    (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    93.4754,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Basal mass 0.25 g. Provider g_l equals this mass divided by 0.05 L, but provider
    preparation says bring to 1.0 L before separate acetate/APM additions. Current
    primary agrees with the literal basal mass. Retain original quantities and stage;
    do not interpret the stored g/L as source-verified or infer an exact final concentration."},
    {"field_path": "ingredients[3].concentration", "name": "KH2PO4", "stored": {"value":
    "2", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Main sol. J425",
    "original_amount": 0.1, "original_unit": "g", "source_snippets": [{"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[4]
    (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\":
    14.6966,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Basal mass 0.1 g. Provider g_l equals this mass divided by 0.05 L, but provider
    preparation says bring to 1.0 L before separate acetate/APM additions. Current
    primary agrees with the literal basal mass. Retain original quantities and stage;
    do not interpret the stored g/L as source-verified or infer an exact final concentration."},
    {"field_path": "ingredients[4].concentration", "name": "MgSO4 x 7 H2O", "stored":
    {"value": "4", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Main
    sol. J425", "original_amount": 0.2, "original_unit": "g", "source_snippets": [{"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[5]
    (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4,\n                        \"mmol_l\":
    16.2288,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Basal mass 0.2 g. Provider g_l equals this mass divided by 0.05 L, but provider
    preparation says bring to 1.0 L before separate acetate/APM additions. Current
    primary agrees with the literal basal mass. Retain original quantities and stage;
    do not interpret the stored g/L as source-verified or infer an exact final concentration."},
    {"field_path": "ingredients[5].concentration", "name": "Sodium acetate", "stored":
    {"value": "41", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Acetate
    solution 41.0 g/L", "original_amount": 41, "original_unit": "g", "source_snippets":
    [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[1].recipe[0] (solution id 4162)", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Sodium acetate\",\n                        \"compound_id\":
    731,\n                        \"amount\": 41,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 41,\n                        \"mmol_l\":
    499.817,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[0].recipe[8]
    (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Acetate solution 41.0 g/L\",\n                        \"solution_id\":
    4162,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[1].recipe[1]
    (solution id 4162)", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Provider acetate stock is41 g in 1000 ml water and is added as10 ml; current
    JCM 425 instead lists 0.41 g acetate directly. The flat 41 G_PER_L value is the
    stock concentration. The stock dose contains 0.41 g by 41 g/L x0.010 L; this arithmetic
    does not establish final-medium g/L. Source sodium-acetate hydration is unstated;
    the asserted CHEBI term represents the anhydrous salt. No hydrate or molar conversion
    is inferred."}, {"field_path": "ingredients[6].concentration", "name": "MgCl2
    x 6 H2O", "stored": {"value": "21.2", "unit": "G_PER_L"}, "decision": "correct",
    "source_stage": "APM salts solution", "original_amount": 21.2, "original_unit":
    "g", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[2].recipe[0] (solution id 4163)", "exact_source_quote":
    "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\":
    21.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    21.2,\n                        \"mmol_l\": 104.278,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[9] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"solution\": \"APM salts solution\",\n                        \"solution_id\":
    4163,\n                        \"amount\": 20,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[2].recipe[2]
    (solution id 4163)", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "APM stock mass in 1000 ml water, with 20 ml added to the medium. Both source
    representations retain this stock/dose boundary. Stored g/L is the undiluted stock
    value; no final-volume concentration is inferred."}, {"field_path": "ingredients[7].concentration",
    "name": "CaCl2 x 2 H2O", "stored": {"value": "3.04", "unit": "G_PER_L"}, "decision":
    "correct", "source_stage": "APM salts solution", "original_amount": 3.04, "original_unit":
    "g", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[2].recipe[1] (solution id 4163)", "exact_source_quote":
    "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\":
    3.04,\n                        \"unit\": \"g\",\n                        \"g_l\":
    3.04,\n                        \"mmol_l\": 20.6782,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[9] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"solution\": \"APM salts solution\",\n                        \"solution_id\":
    4163,\n                        \"amount\": 20,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[2].recipe[2]
    (solution id 4163)", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "APM stock mass in 1000 ml water, with 20 ml added to the medium. Both source
    representations retain this stock/dose boundary. Stored g/L is the undiluted stock
    value; no final-volume concentration is inferred."}, {"field_path": "ingredients[8].concentration",
    "name": "Biotin", "stored": {"value": "0.002", "unit": "G_PER_L"}, "decision":
    "correct", "source_stage": "Trace vitamins", "original_amount": 2, "original_unit":
    "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[4].recipe[0] (solution id 3861)", "exact_source_quote":
    "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.002,\n                        \"mmol_l\": 0.00818632,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\":
    3861,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10]
    (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium.
    The stored g/L matches stock strength after mg-to-g conversion, not the final
    medium concentration."}, {"field_path": "ingredients[9].concentration", "name":
    "Folic acid", "stored": {"value": "0.002", "unit": "G_PER_L"}, "decision": "correct",
    "source_stage": "Trace vitamins", "original_amount": 2, "original_unit": "mg",
    "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[4].recipe[1] (solution id 3861)", "exact_source_quote":
    "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.002,\n                        \"mmol_l\": 0.00453104,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\":
    3861,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10]
    (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium.
    The stored g/L matches stock strength after mg-to-g conversion, not the final
    medium concentration."}, {"field_path": "ingredients[10].concentration", "name":
    "Pyridoxine hydrochloride", "stored": {"value": "0.01", "unit": "G_PER_L"}, "decision":
    "correct", "source_stage": "Trace vitamins", "original_amount": 10, "original_unit":
    "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[4].recipe[2] (solution id 3861)", "exact_source_quote":
    "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\":
    10,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.0486287,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\":
    3861,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10]
    (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium.
    The stored g/L matches stock strength after mg-to-g conversion, not the final
    medium concentration."}, {"field_path": "ingredients[11].concentration", "name":
    "Thiamine HCl", "stored": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct",
    "source_stage": "Trace vitamins", "original_amount": 5, "original_unit": "mg",
    "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[4].recipe[3] (solution id 3861)", "exact_source_quote":
    "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0148236,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\":
    3861,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10]
    (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium.
    The stored g/L matches stock strength after mg-to-g conversion, not the final
    medium concentration."}, {"field_path": "ingredients[12].concentration", "name":
    "Riboflavin", "stored": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct",
    "source_stage": "Trace vitamins", "original_amount": 5, "original_unit": "mg",
    "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[4].recipe[4] (solution id 3861)", "exact_source_quote":
    "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0132837,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\":
    3861,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10]
    (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium.
    The stored g/L matches stock strength after mg-to-g conversion, not the final
    medium concentration."}, {"field_path": "ingredients[13].concentration", "name":
    "Nicotinic acid", "stored": {"value": "0.005", "unit": "G_PER_L"}, "decision":
    "correct", "source_stage": "Trace vitamins", "original_amount": 5, "original_unit":
    "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[4].recipe[5] (solution id 3861)", "exact_source_quote":
    "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0406141,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\":
    3861,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10]
    (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium.
    The stored g/L matches stock strength after mg-to-g conversion, not the final
    medium concentration."}, {"field_path": "ingredients[14].concentration", "name":
    "Calcium pantothenate", "stored": {"value": "0.005", "unit": "G_PER_L"}, "decision":
    "correct", "source_stage": "Trace vitamins", "original_amount": 5, "original_unit":
    "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[4].recipe[6] (solution id 3861)", "exact_source_quote":
    "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0104925,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\":
    3861,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10]
    (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium.
    The stored g/L matches stock strength after mg-to-g conversion, not the final
    medium concentration. Source Calcium pantothenate does not specify the D stereochemistry
    encoded by CHEBI:31345. Exact source-form support remains unresolved."}, {"field_path":
    "ingredients[15].concentration", "name": "Vitamin B12", "stored": {"value": "0.0001",
    "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Trace vitamins", "original_amount":
    0.1, "original_unit": "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[4].recipe[7] (solution id 3861)", "exact_source_quote":
    "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\":
    0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.0001,\n                        \"mmol_l\": 7.3779e-5,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\":
    3861,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10]
    (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium.
    The stored g/L matches stock strength after mg-to-g conversion, not the final
    medium concentration."}, {"field_path": "ingredients[16].concentration", "name":
    "p-Aminobenzoic acid", "stored": {"value": "0.005", "unit": "G_PER_L"}, "decision":
    "correct", "source_stage": "Trace vitamins", "original_amount": 5, "original_unit":
    "mg", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[4].recipe[8] (solution id 3861)", "exact_source_quote":
    "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0364591,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\":
    3861,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10]
    (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium.
    The stored g/L matches stock strength after mg-to-g conversion, not the final
    medium concentration."}, {"field_path": "ingredients[17].concentration", "name":
    "Lipoic acid", "stored": {"value": "0.005", "unit": "G_PER_L"}, "decision": "correct",
    "source_stage": "Trace vitamins", "original_amount": 5, "original_unit": "mg",
    "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[4].recipe[9] (solution id 3861)", "exact_source_quote":
    "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Lipoic acid\",\n                        \"compound_id\": 368,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.024233,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\":
    3861,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}, {"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[4].recipe[10]
    (solution id 3861)", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Trace-vitamin stock mass in 1000 ml water;10 ml stock is added to the medium.
    The stored g/L matches stock strength after mg-to-g conversion, not the final
    medium concentration."}, {"field_path": "solutions (missing iron source)", "name":
    "Iron assembly", "stored": "No structured descriptor in either local layer", "decision":
    "conflict", "source_snippets": [{"source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=425",
    "source_locator": "Main recipe, iron stock row", "exact_source_quote": "Iron(III)citrate
    solution (see Medium No. 1014 ) 50.0 ml", "snapshot_sha256": "d8f5facb349061ab14a980bf62847270322eb86e86ef4a66f5d2ae4c2f9ef9ee",
    "parsed_text_sha256": "12974af5f451d14fbe4d69e335251b4c926f477c2531d237b2e433062f36caac"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[0] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Poorly crystalline iron(III) oxide\",\n                        \"solution_id\":
    4143,\n                        \"amount\": 100,\n                        \"unit\":
    \"mM\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Current primary 50 ml iron-citrate stock conflicts with provider 100 mM poorly
    crystalline iron(III) oxide. Do not silently identify the two species or derive
    an oxide volume from its assay-dependent suspension strength."}, {"field_path":
    "solutions (missing trace-mineral dose)", "name": "Trace minerals", "stored":
    "No structured descriptor in either local layer", "decision": "add", "source_snippets":
    [{"source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=425", "source_locator":
    "Main recipe, trace-mineral row", "exact_source_quote": "Trace mineral solution
    (see Medium No. 411 ) 10.0 ml", "snapshot_sha256": "d8f5facb349061ab14a980bf62847270322eb86e86ef4a66f5d2ae4c2f9ef9ee",
    "parsed_text_sha256": "12974af5f451d14fbe4d69e335251b4c926f477c2531d237b2e433062f36caac"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[7] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Trace mineral solution\",\n                        \"solution_id\":
    4144,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Both sources specify 10 ml of the source-linked modified trace-mineral stock.
    Preserve JCM 411→151 definition and its final molybdate wording."}, {"field_path":
    "solutions (missing vitamin dose)", "name": "Trace vitamins", "stored": "No structured
    descriptor in either local layer", "decision": "add", "source_snippets": [{"source_url":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=425", "source_locator": "Post-cooling
    addition table", "exact_source_quote": "Trace vitamins* (see Medium No. 197 )
    10.0 ml", "snapshot_sha256": "d8f5facb349061ab14a980bf62847270322eb86e86ef4a66f5d2ae4c2f9ef9ee",
    "parsed_text_sha256": "12974af5f451d14fbe4d69e335251b4c926f477c2531d237b2e433062f36caac"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[6] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\":
    3861,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Both specify 10 ml; the current primary marks this stock for filter sterilization.
    The ten vitamin ingredients belong to its stock definition."}, {"field_path":
    "solutions (missing APM dose)", "name": "APM salts", "stored": "No structured
    descriptor in either local layer", "decision": "add", "source_snippets": [{"source_url":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=425", "source_locator": "Post-cooling
    addition table", "exact_source_quote": "APM salts solution (see below) 20.0 ml",
    "snapshot_sha256": "d8f5facb349061ab14a980bf62847270322eb86e86ef4a66f5d2ae4c2f9ef9ee",
    "parsed_text_sha256": "12974af5f451d14fbe4d69e335251b4c926f477c2531d237b2e433062f36caac"},
    {"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[0].recipe[9] (solution id 4161)", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"solution\": \"APM salts solution\",\n                        \"solution_id\":
    4163,\n                        \"amount\": 20,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}], "assessment":
    "Both specify 20 ml of the defined APM stock. Do not keep its stock masses as
    medium g/L."}, {"field_path": "ingredients/solutions (missing bicarbonate)", "name":
    "Bicarbonate stock", "stored": "No structured descriptor in either local layer",
    "decision": "conflict", "source_snippets": [{"source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=425",
    "source_locator": "Post-cooling addition table", "exact_source_quote": "8%NaHCO
    3 solution* 25.0 ml", "snapshot_sha256": "d8f5facb349061ab14a980bf62847270322eb86e86ef4a66f5d2ae4c2f9ef9ee",
    "parsed_text_sha256": "12974af5f451d14fbe4d69e335251b4c926f477c2531d237b2e433062f36caac"}],
    "assessment": "Current primary supplies 25 ml of an8% stock, absent from provider/local
    assembly. Percent basis is not explicitly stated here; do not infer a mass or
    replace the provider variant without source-version resolution."}, {"field_path":
    "preparation_steps (solvent basis)", "name": "Water", "stored": "No structured
    descriptor in either local layer", "decision": "conflict", "source_snippets":
    [{"source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=425", "source_locator":
    "Main recipe, solvent row", "exact_source_quote": "Distilled water 940.0 ml",
    "snapshot_sha256": "d8f5facb349061ab14a980bf62847270322eb86e86ef4a66f5d2ae4c2f9ef9ee",
    "parsed_text_sha256": "12974af5f451d14fbe4d69e335251b4c926f477c2531d237b2e433062f36caac"}],
    "assessment": "Current primary uses 940 ml water plus listed stocks before later
    additions; provider prose brings its main stage to 1.0 L before separate stocks.
    These bases must remain separate. No measured final volume or density conversion
    is claimed."}, {"field_path": "preparation_steps[1].description", "name": "Iron-stock
    precursor", "decision": "evidence_only", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[3].steps[0].step (solution id 4143)", "exact_source_quote":
    "Dissolve 108 g FeCl3 in 1.0 L distilled water.", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}],
    "assessment": "This is the provider oxide-stock precursor step, not a final-medium
    iron dose; washing and resuspension prevent treating precursor mass as retained
    product mass."}, {"field_path": "preparation_steps[1].description", "name": "Stock
    pH adjuster", "decision": "not_quantified", "source_snippets": [{"source_url":
    "https://mediadive.dsmz.de/rest/medium/J425", "source_locator": "$.data.solutions[3].steps[0].step
    (solution id 4143)", "exact_source_quote": "10 N NaOH", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}],
    "assessment": "Strength is given, but addition amount is not quantified; no dry-solute
    amount or normality-to-molarity conversion is inferred."}, {"field_path": "preparation_steps[1].description",
    "name": "Iron suspension strength", "decision": "evidence_only", "source_snippets":
    [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[3].steps[0].step (solution id 4143)", "exact_source_quote":
    "Use the Fe(III) suspension as 0.67 M solution.", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}],
    "assessment": "Retain the nominal source stock-strength statement alongside its
    assay instruction. It is not a measured result in this review and does not identify
    the current primary iron-citrate alternative."}, {"field_path": "preparation_steps[1].description",
    "name": "Chloride assay criterion", "decision": "evidence_only", "source_snippets":
    [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[3].steps[0].step (solution id 4143)", "exact_source_quote":
    "the concentration of Cl- to be less than 1 mM", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}],
    "assessment": "This is an analytical criterion for the washed stock, not chloride
    added to the medium."}, {"field_path": "preparation_steps[2].description", "name":
    "Modified trace-stock molybdate", "decision": "evidence_only", "source_snippets":
    [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[5].steps[0].step (solution id 4144)", "exact_source_quote":
    "0.025 g (final) Na2MoO4 x 2H2O", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}],
    "assessment": "The source explicitly says final in the per-liter trace stock.
    Do not add this amount again to the parent 0.01 g molybdate."}, {"field_path":
    "preparation_steps[2].description", "name": "Modified trace-stock nickel", "decision":
    "evidence_only", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[5].steps[0].step (solution id 4144)", "exact_source_quote":
    "0.024 g NiCl2 x 6H2O", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}],
    "assessment": "Per-liter modified trace-stock amount, not a final-medium concentration;
    its 10 ml addition remains separately represented."}, {"field_path": "preparation_steps[2].description",
    "name": "Modified trace-stock tungstate", "decision": "evidence_only", "source_snippets":
    [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425", "source_locator":
    "$.data.solutions[5].steps[0].step (solution id 4144)", "exact_source_quote":
    "0.025 g Na2WO4 x 2H2O (per liter)", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}],
    "assessment": "Per-liter modified trace-stock amount, not a final-medium concentration."},
    {"field_path": "preparation_steps[0].description", "name": "Gas mixture", "decision":
    "not_quantified", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[0].steps[0].step (solution id 4161)", "exact_source_quote":
    "N2-CO2 (4:1, v/v)", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}],
    "assessment": "Preparation gas ratio is explicit, but no fixed mass or final-medium
    concentration is supplied. Retain stage-specific nitrogen handling separately."},
    {"field_path": "preparation_steps[3].description", "name": "Inherited strain-specific
    inoculum", "decision": "unsupported", "source_snippets": [{"source_url": "https://mediadive.dsmz.de/rest/medium/J425",
    "source_locator": "$.data.solutions[5].steps[1].step (solution id 4144)", "exact_source_quote":
    "For strain JCM 12378, inoculate with a 10% inoculum.", "snapshot_sha256": "908e3499652e4d2855e1f2029bba5f602b231eea8f4b2740d7960b4c4a0cc8ee"}],
    "assessment": "The provider attaches this comment to trace stock 4144; its primary
    location is JCM 411. Target-specific applicability to JCM 425 is unsupported;
    no target growth or taxonomy assertion follows."}]'
- assessment_id: source-conflict
  area: provenance
  topic: Current collection recipe versus provider representation
  outcome: concern
  summary: The primary lists iron citrate, direct acetate and later bicarbonate additions;
    MediaDive lists iron oxide and acetate stock without bicarbonate, with different
    preparation wording. Both share the basal salt masses, pH6.8, trace-mineral/vitamin
    stock doses and APM dose. Their access dates do not establish recipe chronology.
    Choose and cite an exact version before any scientific correction.
  target_ids:
  - CultureMech:015407
  evidence_ids:
  - record
  - owner-0
  - provider
  - jcm425
  - jcm1014
- assessment_id: stocks
  area: quantity
  topic: All named source stocks and nested reference boundaries
  outcome: concern
  summary: Both local layers lack structured stock descriptors. Provider 4162 acetate
    is41 g with 1000 ml water,4163 APM is21.2 g magnesium chloride hexahydrate and
    3.04 g calcium chloride dihydrate with 1000 ml water, and 3861 vitamins is a separate
    one-liter stock. Provider 4143 iron oxide is defined in prose and 4144 trace minerals
    by an external reference. Current primary uses the different iron-citrate stock
    and a bicarbonate stock. Fully inspected linked pages supply only their named
    stock subsections; unrelated basal recipes are excluded.
  target_ids:
  - CultureMech:015407
  evidence_ids:
  - record
  - owner-0
  - provider
  - jcm425
  - jcm411
  - jcm151
  - jcm197
  - jcm1014
  details: 'JCM 197 vitamin stock: biotin 2 mg, folic acid 2 mg, pyridoxine HCl 10
    mg, thiamine HCl 5 mg, riboflavin 5 mg, nicotinic acid 5 mg, calcium pantothenate
    5 mg, vitamin B12 0.1 mg, p-aminobenzoic acid 5 mg and lipoic acid 5 mg with 1
    L water. JCM 151 trace minerals: nitrilotriacetic acid 1.5 g, MgSO4·7H2O 3 g,
    MnSO4·xH2O 0.5 g, NaCl 1 g, FeSO4·7H2O 0.1 g, CoSO4·7H2O 0.1 g, CaCl2·2H2O 0.1
    g, ZnSO4·7H2O 0.1 g, CuSO4·5H2O 0.01 g, AlK(SO4)2 0.01 g, H3BO3 0.01 g, Na2MoO4·2H2O
    0.01 g with 1 L water. JCM 411 specifies Mo0.025 g(final), NiCl2·6H2O 0.024 g
    and Na2WO4·2H2O 0.025 g per liter. Do not treat final Mo as an additional 0.025
    g or invent the unspecified manganese/alum hydration. JCM 1014 iron citrate is2.4
    g filled to 100 ml after its separate dissolution/pH sequence. No quoted stock
    mass is an approved final-medium dose.'
- assessment_id: forms
  area: grounding
  topic: All asserted chemical forms and linkage scope
  outcome: concern
  summary: All 18 direct ingredient instances have primary CHEBI links and current
    secondary keys, with canonical metadata verified separately. The basal and APM
    hydrates match their respective source stock forms. CHEBI:31345 has D-calcium-pantothenate
    synonyms and stereospecific structural annotations, while the source says only
    Calcium pantothenate; exact stereochemical support is unresolved. CHEBI:32954
    encodes anhydrous sodium acetate, while source hydration is unstated. Neither
    observation alone proves a wrong ID, and no mass-to-molar conversion is made.
    Vitamin B12 remains a broad class at the source specificity. Valid terms do not
    repair the preparation-stage errors. Omitted iron source and trace-stock constituents
    require separate source-specific grounding after version selection.
  target_ids:
  - CultureMech:015407
  evidence_ids:
  - record
  - provider
  - jcm425
  - jcm197
  - mim
  - chebi26710
  - chebi32588
  - chebi31206
  - chebi63036
  - chebi31795
  - chebi32954
  - chebi86345
  - chebi86158
  - chebi15956
  - chebi27470
  - chebi30961
  - chebi49105
  - chebi17015
  - chebi15940
  - chebi31345
  - chebi176843
  - chebi30753
  - chebi16494
- assessment_id: preparation
  area: completeness
  topic: Preparation stages, pH and imported strain comment
  outcome: concern
  summary: Target and owner reproduce provider main preparation, oxide-stock preparation,
    trace-stock definition and a JCM 12378 comment as one sequential medium procedure.
    The latter occurs under provider trace stock 4144 and on parent JCM 411, without
    target-specific growth support. The current primary has a different staged assembly,
    source-default autoclaving and marked filter-sterilized additions. Keep each stock
    procedure and version separate; pH6.8 is common medium context, while oxide/trace/citrate
    pH values belong to their stocks.
  target_ids:
  - CultureMech:015407
  evidence_ids:
  - record
  - owner-0
  - provider
  - jcm425
  - jcm411
  - jcm1014
  - jcm151
  - writer
- assessment_id: classification
  area: scope
  topic: Physical state, composition and biological annotations
  outcome: supported
  summary: LIQUID and a defined chemical formulation agree with the listed sources;
    high_metal is consistent with their iron additions. These annotations do not make
    the incomplete quantitative assembly usable. No target_organisms, native variants,
    environment, gene or measured growth assertions occur. The imported JCM 12378
    procedure comment must not be promoted into a target-specific organism association.
  target_ids:
  - CultureMech:015407
  evidence_ids:
  - record
  - owner-0
  - provider
  - jcm425
  - jcm411
- assessment_id: provenance
  area: provenance
  topic: History, evidence and present writer limitations
  outcome: concern
  summary: All7 target and6 owner history timestamps parse with timezones. History
    records import, grounding and generation rather than scientific verification.
    Neither layer has claim-level formulation evidence; reference validation inspected
    zero excerpts. Current importer code now separates stock composition but still
    trusts supplied g_l and flattens preparation steps across solutions. This is current
    context, not proof of a historical run.
  target_ids:
  - CultureMech:015407
  evidence_ids:
  - record
  - owner-0
  - validate-references
  - writer
- assessment_id: citation
  area: provenance
  topic: Bibliographic locator embedded in oxide-stock procedure
  outcome: concern
  summary: Author/year/pages match the registered paper but the source-inherited volume
    54 differs from registered volume 52. The paper was checked for bibliographic
    identity only; its method was not independently assessed.
  target_ids:
  - CultureMech:015407
  evidence_ids:
  - record
  - owner-0
  - provider
  - jcm411
  - citation-metadata
findings:
- finding_id: f1
  issue_key: CM015407-basal-volume-normalization
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Five basal concentrations use a conflicting provider denominator
  description: NaCl 400, KCl 15.4, NH4Cl 5, KH2PO4 2 and MgSO4·7H2O 4 G_PER_L reproduce
    MediaDive g_l calculated from its declared 50 ml volume. The same provider lists
    20,0.77,0.25,0.1 and 0.2 g and specifies bringing the main stage to 1.0 L before
    later additions. Current JCM 425 agrees with those literal masses. Neither source
    supports the stored concentrations as final-medium values.
  target_ids:
  - CultureMech:015407
  field_paths:
  - ingredients[0:5].concentration
  evidence_ids:
  - record
  - owner-0
  - provider
  - jcm425
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/a1_marine_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CM015407-stock-stage-collapse
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Thirteen stock concentrations appear as direct medium ingredients
  description: The acetate 41 G_PER_L, two APM values 21.2/3.04 G_PER_L and ten vitamin
    values are stock concentrations. Their 10/20/10 ml additions and separate stock
    definitions are absent from both local layers. Iron and trace-mineral assembly
    are not represented as structured ingredients or solutions. Correct chemical identifiers
    do not make the flattened quantities valid.
  target_ids:
  - CultureMech:015407
  field_paths:
  - ingredients[5:18].concentration
  - solutions
  evidence_ids:
  - record
  - owner-0
  - provider
  - jcm425
  - jcm411
  - jcm151
  - jcm197
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/a1_marine_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: CM015407-source-version-conflict
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Primary and provider formulations differ materially
  description: Current JCM 425 uses iron(III)citrate and bicarbonate additions with
    a different acetate/preparation representation. MediaDive/local prose uses poorly
    crystalline iron(III)oxide and separate acetate stock. The sources share accession
    identity but are not interchangeable formulations, and capture timestamps establish
    no historical order.
  target_ids:
  - CultureMech:015407
  field_paths:
  - notes
  - media_term
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm425
  - provider
  - jcm1014
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/a1_marine_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: CM015407-preparation-scope-and-evidence
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Stock procedures and an unrelated strain comment became medium steps
  description: Both local layers concatenate main preparation, oxide stock preparation,
    trace-stock wording and the JCM 12378 comment into one medium procedure. The strain
    comment is captured on JCM 411 and provider trace stock 4144 without JCM 425-specific
    support. Source-version-specific sterilization and additive stages require separate
    scope; claim-level formulation evidence is absent.
  target_ids:
  - CultureMech:015407
  field_paths:
  - preparation_steps
  - evidence
  - references
  evidence_ids:
  - record
  - owner-0
  - provider
  - jcm425
  - jcm411
  - writer
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/a1_marine_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: CM015407-inherited-citation-volume
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The embedded method citation has the wrong journal volume
  description: The record and its provider/linked primary stock prose cite Lovley
    and Phillips, Appl. Environ. Microbiol.54,751–757,1986. Registration metadata
    for those authors/year/pages gives volume 52(4) and DOI 10.1128/aem.52.4.751-757.1986.
    This is an inherited bibliographic defect, not evidence that the analytical method
    itself is invalid.
  target_ids:
  - CultureMech:015407
  field_paths:
  - preparation_steps[1].description
  - references
  evidence_ids:
  - record
  - owner-0
  - provider
  - jcm411
  - citation-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/a1_marine_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: CM015407-source-chemical-form-specificity
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Two ontology forms exceed explicit source detail
  description: CHEBI:31345 includes D-calcium-pantothenate synonyms and stereospecific
    InChI/SMILES, but the vitamin source names only Calcium pantothenate. CHEBI:32954
    represents anhydrous sodium acetate while the recipe name does not state hydration.
    The asserted labels and IDs are valid; exact source-form support remains unresolved
    and no alternative form is proved.
  target_ids:
  - CultureMech:015407
  field_paths:
  - ingredients[5].term
  - ingredients[14].term
  - ingredients[5].mediaingredientmech_chebi_term
  - ingredients[14].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - provider
  - jcm425
  - jcm197
  - chebi32954
  - chebi31345
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/a1_marine_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Retain exact masses and preparation basis, resolve the source version,
    and derive concentrations only from a justified final-volume convention. Audit
    the importer reliance on provider g_l when it conflicts with source prose.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:015407
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/a1_marine_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a2
  description: Restore source-specific stock identities, complete definitions, original
    units and addition stages in the maintained owner. Preserve nested reference overrides
    and uncertain forms; do not flatten stock concentrations or treat every linked
    parent recipe as inherited.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:015407
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/a1_marine_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a3
  description: Identify and document the intended recipe version with exact source
    evidence before rebuilding the assembly. Preserve the alternative as a version/variant
    conflict rather than silently combining ingredients from both.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:015407
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/a1_marine_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a4
  description: Separate medium and stock procedures, retain the intended version-specific
    instructions, and exclude or explicitly qualify the inherited strain comment without
    creating a growth assertion. Attach narrow source excerpts to quantities, stock
    identity and preparation claims.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:015407
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/a1_marine_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a5
  description: Correct the bibliographic locator with DOI-backed metadata and preserve
    the source-transcription distinction. Assess the paper method separately before
    treating the procedure citation as analytical validation.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:015407
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/a1_marine_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a6
  description: Verify source-specific reagent form or document the residual uncertainty
    before claiming exact chemical-form grounding or deriving molar values. Do not
    replace either ID solely from the generic source label or invent a hydrate/stereoisomer.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:015407
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/a1_marine_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
limitations:
- The current primary and captured provider formulations are different representations
  of the same accession. Their chronological relationship is not established; no historical
  replacement sequence or approved reconstructed recipe is asserted.
- No measured final volume, percent-strength convention, unprovided chemical form,
  strain taxonomy, incubation optimum or experimental growth result is inferred. Completion
  means the defects and source conflict were assessed, not resolved by editing a recipe.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-013
- generated-medium
```
