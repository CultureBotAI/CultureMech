# Source and formulation review: acidimicrobium_medium (CultureMech:003043)

- Review: 20261021T110527Z-culturemech-003043-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T10:48:48Z
- Finished UTC: 2026-10-21T11:05:27Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated JCM 698 record contains the six amounts from JCM 283 while retaining JCM 698 identity and preparation; three distinct normalized formulations were conflated. The JCM 698 owner misrepresents a liquid yeast-stock dose, pH and variant notes lose source scope, and one child path is broken. All exact source documents are available; six DSMZ-owner amount-evidence claims remain valid within their own provider scope.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 170; batch 017 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding sixteen task batches contain 160 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 162 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003043 | data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml | generated | acidimicrobium_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003043 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003043 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch017/170/strict.tsv |
| validate-terms | passed | True | CultureMech:003043 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003043 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003043 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003043.

The four documented recipes completed; interpret the scope of each separately.

### Source identities, exact contributors and merged formulation

identity: concern. Targets: CultureMech:003043.

All three sources and normalized owners resolve by stable IDs and explicit merge provenance. The target ingredient list exactly equals JCM 283, while its ID/media_term and preparation come from JCM 698. Shared ingredient names do not establish formulation equivalence. DSMZ 709 is separately represented and retains its own existing amount evidence.

### Asserted ontology and pinned secondary identifier metadata

grounding: supported. Targets: CultureMech:003043.

5 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 5/6 primary and 5/6 secondary instances; all asserted secondary keys have exact pinned MIM rows. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 6: primary 83.33%; secondary 83.33%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### All generated and owner amounts, source-only water and preparation/variant quantities

quantity: concern. Targets: CultureMech:003043.

The 41-row inventory covers six conflicted generated amounts, every row of all three provider main tables, twelve preparation contexts, including four explicit unquantified source-only contexts and two variant-note comparisons. Six DSMZ owner amounts are verified against existing attached exact evidence; other unchanged owner amounts are evidence_only. JCM 698 yeast dose and source-volume disagreement remain explicit.

[{"field_path": "ingredients[0].concentration", "input": "target", "current": {"value": "0.4", "unit": "G_PER_L"}, "decision": "conflict", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\": 1.62288,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}, {"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\": 2.02455,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation": "This value/order matches JCM 283, but the target identifies JCM 698 and retains its preparation. Resolve source identity and split formulations before selecting a replacement amount. Numerical coincidence for one component does not establish whole-medium equivalence."}, {"field_path": "ingredients[1].concentration", "input": "target", "current": {"value": "0.2", "unit": "G_PER_L"}, "decision": "conflict", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].recipe[1]", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.51355,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}, {"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].recipe[1]", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.399202,\n                        \"mmol_l\": 3.02105,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation": "This value/order matches JCM 283, but the target identifies JCM 698 and retains its preparation. Resolve source identity and split formulations before selecting a replacement amount. Numerical coincidence for one component does not establish whole-medium equivalence."}, {"field_path": "ingredients[2].concentration", "input": "target", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "conflict", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.34138,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}, {"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].recipe[3]", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\": 1.3387,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation": "This value/order matches JCM 283, but the target identifies JCM 698 and retains its preparation. Resolve source identity and split formulations before selecting a replacement amount. Numerical coincidence for one component does not establish whole-medium equivalence."}, {"field_path": "ingredients[3].concentration", "input": "target", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "conflict", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].recipe[3]", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.574132,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}, {"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\": 1.14597,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation": "This value/order matches JCM 283, but the target identifies JCM 698 and retains its preparation. Resolve source identity and split formulations before selecting a replacement amount. Numerical coincidence for one component does not establish whole-medium equivalence."}, {"field_path": "ingredients[4].concentration", "input": "target", "current": {"value": "25", "unit": "G_PER_L"}, "decision": "conflict", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].recipe[4]", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 25,\n                        \"unit\": \"g\",\n                        \"g_l\": 25,\n                        \"mmol_l\": 89.9232,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}, {"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].recipe[4]", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00998004,\n                        \"mmol_l\": 0.0358975,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation": "This value/order matches JCM 283, but the target identifies JCM 698 and retains its preparation. Resolve source identity and split formulations before selecting a replacement amount. Numerical coincidence for one component does not establish whole-medium equivalence."}, {"field_path": "ingredients[5].concentration", "input": "target", "current": {"value": "0.16", "unit": "G_PER_L"}, "decision": "conflict", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].recipe[5]", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 0.16,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.16,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}, {"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].recipe[6]", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"10%, BD-Difco\",\n                        \"amount\": 2.5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation": "This value/order matches JCM 283, but the target identifies JCM 698 and retains its preparation. Resolve source identity and split formulations before selecting a replacement amount. Numerical coincidence for one component does not establish whole-medium equivalence."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "current": {"value": "0.499002", "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J698", "provider_declared_volume_ml": 1002, "source_original_amount": 0.5, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\": 2.02455,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation": "The owner value matches provider g_l on its own declared basis, but lacks attached local amount evidence. Original source mass and stage must remain explicit; this does not establish physical final volume. Provider-basis arithmetic: 0.5 g / 1002 ml gives 0.4990019960079840319361277445 g/L before rounding."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "current": {"value": "0.399202", "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J698", "provider_declared_volume_ml": 1002, "source_original_amount": 0.4, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].recipe[1]", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.399202,\n                        \"mmol_l\": 3.02105,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation": "The owner value matches provider g_l on its own declared basis, but lacks attached local amount evidence. Original source mass and stage must remain explicit; this does not establish physical final volume. Provider-basis arithmetic: 0.4 g / 1002 ml gives 0.3992015968063872255489021956 g/L before rounding."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "current": {"value": "0.199601", "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J698", "provider_declared_volume_ml": 1002, "source_original_amount": 0.2, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\": 1.14597,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation": "The owner value matches provider g_l on its own declared basis, but lacks attached local amount evidence. Original source mass and stage must remain explicit; this does not establish physical final volume. Provider-basis arithmetic: 0.2 g / 1002 ml gives 0.1996007984031936127744510978 g/L before rounding."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "current": {"value": "0.0998004", "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J698", "provider_declared_volume_ml": 1002, "source_original_amount": 0.1, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].recipe[3]", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\": 1.3387,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation": "The owner value matches provider g_l on its own declared basis, but lacks attached local amount evidence. Original source mass and stage must remain explicit; this does not establish physical final volume. Provider-basis arithmetic: 0.1 g / 1002 ml gives 0.09980039920159680638722554890 g/L before rounding."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "current": {"value": "0.00998004", "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J698", "provider_declared_volume_ml": 1002, "source_original_amount": 10, "source_original_unit": "mg", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].recipe[4]", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00998004,\n                        \"mmol_l\": 0.0358975,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation": "The owner value matches provider g_l on its own declared basis, but lacks attached local amount evidence. Original source mass and stage must remain explicit; this does not establish physical final volume. Provider-basis arithmetic: 10 mg / 1002 ml gives 0.009980039920159680638722554890 g/L before rounding."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml", "field_path": "preparation_steps (source water omitted)", "current": null, "decision": "add", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].recipe[5]", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "source_original_amount": 1000, "source_original_unit": "ml", "explanation": "Retain this source-specific solvent amount, not a mass concentration or assumed measured final volume. Keep the three owner recipes distinct."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "current": {"value": "2.5", "unit": "G_PER_L"}, "decision": "correct", "source_stage": "Main sol. J698", "provider_declared_volume_ml": 1002, "source_original_amount": 2.5, "source_original_unit": "ml", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].recipe[6]", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"10%, BD-Difco\",\n                        \"amount\": 2.5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation": "The owner stores 2.5 G_PER_L, but the source supplies 2.5 ml of a stock labelled 10% (BD-Difco), without a percent basis. Preserve liquid addition and stock label; do not infer 2.5 g/L, a mass/volume basis, or equivalence to DSMZ 709 yeast 0.25 g. Provider volume 1002 ml differs from the nominal 1002.5 ml sum and is not a measured final volume."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "current": {"value": "0.4", "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J283", "provider_declared_volume_ml": 1000, "source_original_amount": 0.4, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\": 1.62288,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation": "The owner value matches provider g_l on its own declared basis, but lacks attached local amount evidence. Original source mass and stage must remain explicit; this does not establish physical final volume. Provider-basis arithmetic: 0.4 g / 1000 ml gives 0.4 g/L before rounding."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "current": {"value": "0.2", "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J283", "provider_declared_volume_ml": 1000, "source_original_amount": 0.2, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].recipe[1]", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.51355,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation": "The owner value matches provider g_l on its own declared basis, but lacks attached local amount evidence. Original source mass and stage must remain explicit; this does not establish physical final volume. Provider-basis arithmetic: 0.2 g / 1000 ml gives 0.2 g/L before rounding."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J283", "provider_declared_volume_ml": 1000, "source_original_amount": 0.1, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.34138,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation": "The owner value matches provider g_l on its own declared basis, but lacks attached local amount evidence. Original source mass and stage must remain explicit; this does not establish physical final volume. Provider-basis arithmetic: 0.1 g / 1000 ml gives 0.1 g/L before rounding."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J283", "provider_declared_volume_ml": 1000, "source_original_amount": 0.1, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].recipe[3]", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.574132,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation": "The owner value matches provider g_l on its own declared basis, but lacks attached local amount evidence. Original source mass and stage must remain explicit; this does not establish physical final volume. Provider-basis arithmetic: 0.1 g / 1000 ml gives 0.1 g/L before rounding."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "current": {"value": "25", "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J283", "provider_declared_volume_ml": 1000, "source_original_amount": 25, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].recipe[4]", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 25,\n                        \"unit\": \"g\",\n                        \"g_l\": 25,\n                        \"mmol_l\": 89.9232,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation": "The owner value matches provider g_l on its own declared basis, but lacks attached local amount evidence. Original source mass and stage must remain explicit; this does not establish physical final volume. Provider-basis arithmetic: 25 g / 1000 ml gives 25 g/L before rounding."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "current": {"value": "0.16", "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J283", "provider_declared_volume_ml": 1000, "source_original_amount": 0.16, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].recipe[5]", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 0.16,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.16,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation": "The owner value matches provider g_l on its own declared basis, but lacks attached local amount evidence. Original source mass and stage must remain explicit; this does not establish physical final volume. Provider-basis arithmetic: 0.16 g / 1000 ml gives 0.16 g/L before rounding."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml", "field_path": "preparation_steps (source water omitted)", "current": null, "decision": "add", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].recipe[6]", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "source_original_amount": 1000, "source_original_unit": "ml", "explanation": "Retain this source-specific solvent amount, not a mass concentration or assumed measured final volume. Keep the three owner recipes distinct."}, {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "field_path": "ingredients[0].concentration", "current": {"value": "0.5", "unit": "G_PER_L"}, "decision": "verified", "source_stage": "Main sol. 709", "provider_declared_volume_ml": 1000, "source_original_amount": 0.5, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "explanation": "Existing attached exact provider evidence supports this unchanged owner amount at its declared basis. Preserve original mass and stage, and the evidence in this owner; do not transfer it to the generated mixed record. 0.5 g / 1000 ml = 0.5 g/L on the provider basis; water alone does not prove final volume."}, {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "field_path": "ingredients[1].concentration", "current": {"value": "0.4", "unit": "G_PER_L"}, "decision": "verified", "source_stage": "Main sol. 709", "provider_declared_volume_ml": 1000, "source_original_amount": 0.4, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].recipe[1]", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\": 3.02709,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "explanation": "Existing attached exact provider evidence supports this unchanged owner amount at its declared basis. Preserve original mass and stage, and the evidence in this owner; do not transfer it to the generated mixed record. 0.4 g / 1000 ml = 0.4 g/L on the provider basis; water alone does not prove final volume."}, {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "field_path": "ingredients[2].concentration", "current": {"value": "0.2", "unit": "G_PER_L"}, "decision": "verified", "source_stage": "Main sol. 709", "provider_declared_volume_ml": 1000, "source_original_amount": 0.2, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.14826,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "explanation": "Existing attached exact provider evidence supports this unchanged owner amount at its declared basis. Preserve original mass and stage, and the evidence in this owner; do not transfer it to the generated mixed record. 0.2 g / 1000 ml = 0.2 g/L on the provider basis; water alone does not prove final volume."}, {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "field_path": "ingredients[3].concentration", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "verified", "source_stage": "Main sol. 709", "provider_declared_volume_ml": 1000, "source_original_amount": 0.1, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].recipe[3]", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.34138,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "explanation": "Existing attached exact provider evidence supports this unchanged owner amount at its declared basis. Preserve original mass and stage, and the evidence in this owner; do not transfer it to the generated mixed record. 0.1 g / 1000 ml = 0.1 g/L on the provider basis; water alone does not prove final volume."}, {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "field_path": "ingredients[4].concentration", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision": "verified", "source_stage": "Main sol. 709", "provider_declared_volume_ml": 1000, "source_original_amount": 0.01, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].recipe[4]", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0359693,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "explanation": "Existing attached exact provider evidence supports this unchanged owner amount at its declared basis. Preserve original mass and stage, and the evidence in this owner; do not transfer it to the generated mixed record. 0.01 g / 1000 ml = 0.01 g/L on the provider basis; water alone does not prove final volume."}, {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "field_path": "ingredients[5].concentration", "current": {"value": "0.25", "unit": "G_PER_L"}, "decision": "verified", "source_stage": "Main sol. 709", "provider_declared_volume_ml": 1000, "source_original_amount": 0.25, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].recipe[5]", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.25,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "explanation": "Existing attached exact provider evidence supports this unchanged owner amount at its declared basis. Preserve original mass and stage, and the evidence in this owner; do not transfer it to the generated mixed record. 0.25 g / 1000 ml = 0.25 g/L on the provider basis; water alone does not prove final volume."}, {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "field_path": "preparation_steps (source water omitted)", "current": null, "decision": "add", "source_snippets": [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].recipe[6]", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "source_original_amount": 1000, "source_original_unit": "ml", "explanation": "Retain this source-specific solvent amount, not a mass concentration or assumed measured final volume. Keep the three owner recipes distinct."}, {"field_path": "ph_value (target and JCM 698 owner)", "current": "existing scalar/prose as specified", "decision": "correct", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].steps[0].step", "exact_source_quote": "pH to 2.0", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation": "Existing scalar 1.7 is the conditional branch pH; restore base pH 2.0 while retaining 1.7 only with the yeast-free branch. Existing base preparation prose already says 2.0."}, {"field_path": "ph_value (JCM 283 owner)", "current": "existing scalar/prose as specified", "decision": "correct", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].steps[0].step", "exact_source_quote": "pH to 1.6-1.8", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation": "Provider scalar 1.7 loses the primary range. Preserve the full range already present in owner prose, without asserting that 1.7 is a false possible value."}, {"field_path": "ph_value (DSMZ 709 owner)", "current": "existing scalar/prose as specified", "decision": "evidence_only", "source_snippets": [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].steps[0].step", "exact_source_quote": "pH to 2.0", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "explanation": "The owner scalar and base prose are consistent with source base pH. Attach scoped evidence without borrowing the JCM branch as a universal condition."}, {"field_path": "preparation_steps[1] (target and JCM 698 owner conditional branch)", "current": "existing scalar/prose as specified", "decision": "evidence_only", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].steps[1].step", "exact_source_quote": "13.9 g/L (final) FeSO4 x 7H2O and adjust pH to 1.7", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation": "Retain both existing source quantities only with the explicit yeast-free conditional formulation. Do not sum this final concentration with the basal iron amount or assert growth for an unspecified organism."}, {"field_path": "preparation_steps[1] (DSMZ 709 owner conditional branch)", "current": "existing scalar/prose as specified", "decision": "evidence_only", "source_snippets": [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].steps[1].step", "exact_source_quote": "13.90 g/l FeSO4 x 7 H2O. Adjust medium pH to 1.7", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "explanation": "Keep the owner-specific conditional wording, omission of yeast and pH adjustment before autoclaving. Do not silently resolve whether its iron wording means addition versus replacement by borrowing the JCM final qualifier."}, {"field_path": "preparation_steps[0] (JCM 283 yeast stock strength)", "current": "existing scalar/prose as specified", "decision": "evidence_only", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].steps[0].step", "exact_source_quote": "autoclaved 10% solution", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation": "This existing stock label has no stated percent basis; do not recast as PERCENT_W_V or derive a liquid dose. Main filtration remains distinct from stock autoclaving."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml", "field_path": "preparation_steps (missing qualified JCM cycle)", "current": null, "decision": "add", "source_snippets": [{"source_key": "jcm698", "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=698", "source_locator": "Global JCM qualifier before medium heading", "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.", "snapshot_sha256": "4154e76475d6acd8a7bb6ec012d35c2322c3a5edfd6bf62706c532bb1a92310b", "parsed_text_sha256": "310fed215efc9448d394ab1ee38290c139a00527185cdd82d79efcf2e917e648"}], "explanation": "Preserve the source exception qualifier. Apply to explicit autoclave stages only, not JCM 283 main filtration, and do not transfer to DSMZ 709 where no cycle is supplied. For JCM 698 this is also missing from the generated target."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml", "field_path": "preparation_steps (missing qualified JCM cycle)", "current": null, "decision": "add", "source_snippets": [{"source_key": "jcm283", "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=283", "source_locator": "Global JCM qualifier before medium heading", "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.", "snapshot_sha256": "c88ce0723ed9fc471190c0bdbecf2236a8aa10b09e17f14155df03e2db6cb20e", "parsed_text_sha256": "dec625300e0fb56c6abfda28b096a8be75a4b46aa90fcbe67189a6a24724c84d"}], "explanation": "Preserve the source exception qualifier. Apply to explicit autoclave stages only, not JCM 283 main filtration, and do not transfer to DSMZ 709 where no cycle is supplied. For JCM 698 this is also missing from the generated target."}, {"field_path": "variant_children[0].notes; reciprocal child variant_modifications", "current": "Reviewed same-name Acidimicrobium medium records; child rounds the inorganic salts to the same effective levels but lowers yeast extract from 2.5 g/L to 0.25 g/L and changes pH from 1.7 to 2.0.", "decision": "correct", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].recipe[6]", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"10%, BD-Difco\",\n                        \"amount\": 2.5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}, {"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].recipe[5]", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.25,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "explanation": "The asserted parent 2.5 g/L yeast basis is actually a 2.5 ml stock addition with unspecified percent basis. Rewrite both ends of the relationship only after owner/source reconciliation; preserve source-specific pH/base/conditional scope and avoid a false tenfold mass comparison."}, {"field_path": "variant_children[1].notes; reciprocal child variant_modifications", "current": "Reviewed JCM Acidimicrobium/Ferroplasma pair; child keeps acidic pH 1.7 and same component set but changes sulfate/phosphate salts, raises FeSO4 from 0.00998004 to 25 g/L, and lowers yeast extract from 2.5 to 0.16 g/L.", "decision": "correct", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].recipe[6]", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"10%, BD-Difco\",\n                        \"amount\": 2.5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}, {"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].recipe[5]", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 0.16,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.16,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation": "The asserted parent 2.5 g/L yeast basis is actually a 2.5 ml stock addition with unspecified percent basis. Rewrite both ends of the relationship only after owner/source reconciliation; preserve source-specific pH/base/conditional scope and avoid a false tenfold mass comparison."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml", "field_path": "preparation_steps (H2SO4 titrant quantity)", "current": "Sulfuric acid named in the source-specific pH-adjustment prose; no fixed strength or dose is supplied.", "decision": "not_quantified", "source_stage": "Each exact base/conditional adjustment stage remains separate; no condition is transferred between formulations.", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].steps[0].step", "exact_source_quote": "Adjust pH to 2.0 with H2SO4.", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}, {"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator": "$.data.solutions[0].steps[1].step", "exact_source_quote": "adjust pH to 1.7 with H2SO4.", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation": "The source specifies sulfuric acid for pH adjustment but neither a fixed titrant volume nor acid strength. Preserve the exact source pH/stage and leave these quantities unquantified. The JCM 698 preparation retained in the mixed generated target has the same limitation; resolving formulation identity comes first."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml", "field_path": "preparation_steps (H2SO4 titrant quantity)", "current": "Sulfuric acid named in the source-specific pH-adjustment prose; no fixed strength or dose is supplied.", "decision": "not_quantified", "source_stage": "Each exact base/conditional adjustment stage remains separate; no condition is transferred between formulations.", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283", "source_locator": "$.data.solutions[0].steps[0].step", "exact_source_quote": "adjust pH to 1.6-1.8 with H2SO4,", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation": "The source specifies sulfuric acid for pH adjustment but neither a fixed titrant volume nor acid strength. Preserve the exact source pH/stage and leave these quantities unquantified; do not infer them from another formulation."}, {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "field_path": "preparation_steps (H2SO4 titrant quantity)", "current": "Sulfuric acid named in the source-specific pH-adjustment prose; no fixed strength or dose is supplied.", "decision": "not_quantified", "source_stage": "Each exact base/conditional adjustment stage remains separate; no condition is transferred between formulations.", "source_snippets": [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].steps[0].step", "exact_source_quote": "adjust pH to 2.0 with H2SO4.", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}, {"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].steps[1].step", "exact_source_quote": "Adjust medium pH to 1.7 with H2SO4 prior to autoclaving.", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "explanation": "The source specifies sulfuric acid for pH adjustment but neither a fixed titrant volume nor acid strength. Preserve the exact source pH/stage and leave these quantities unquantified; do not infer them from another formulation."}, {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "field_path": "preparation_steps[0] (yeast-stock strength and addition volume)", "current": "A sterile yeast-extract stock is named, without its strength or addition volume.", "decision": "not_quantified", "source_stage": "DSMZ 709 base formulation, post-autoclave addition only", "source_snippets": [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].steps[0].step", "exact_source_quote": "After autoclaving add yeast extract from a sterile stock solution.", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "explanation": "Keep the independently verified main-recipe yeast mass 0.25 g and provider-declared 0.25 g/L unchanged. The stock strength and liquid addition volume are not supplied. Do not borrow the JCM 10% stock label, infer a percent basis, or derive a liquid dose."}]

### Exact chemical forms and undefined yeast products

grounding: supported. Targets: CultureMech:003043.

The five asserted CHEBI primary/secondary identities are live and preserve supplied inorganic forms, including the magnesium and iron heptahydrates. Exact pinned MIM keys do not establish recipe equivalence. Yeast extract remains an undefined mixture; JCM identifies BD-Difco, whereas the DSMZ table does not establish the same product identity. No replacement chemical or product mapping is inferred.

### Base versus conditional pH and sterilization stages

completeness: concern. Targets: CultureMech:003043.

The generated ingredients and retained preparation belong to different formulations. JCM 698 base pH is 2.0 with a separate yeast-stock addition; 1.7 belongs to its conditional branch. JCM 283 supplies range 1.6–1.8 and main filtration, yet its owner action is AUTOCLAVE because the same prose also mentions yeast-stock autoclaving. DSMZ 709 preparation is separately retained. Keep each branch, range, stock and qualified cycle at its exact source scope.

### Variant links and reciprocal source relationships

graph: concern. Targets: CultureMech:003043.

The target and JCM 698 owner point to a nonexistent bacterial-path JCM 283 child. The exact stable-ID contributor exists under archaea and its parent path resolves. The other child and both reciprocal parent paths resolve exactly. Correct the link after verifying the source-specific relationship; a matching stable ID does not make the stored path valid.

### Composition class, source labels and organism scope

scope: concern. Targets: CultureMech:003043.

The defined inorganic salts plus undefined yeast support COMPLEX/SEMI_DEFINED for each base formulation, as already stored in the JCM 283 and DSMZ owners. UNDEFINED in the target/JCM 698 owner overstates the unknown fraction. The combined categories and Ferroplasma synonym are merge provenance, not evidence of cross-organism applicability or source equivalence. No phenotype, taxonomic assertion or growth result is inferred from medium titles or conditional comments.

### Existing DSMZ evidence and missing evidence in other layers

evidence: concern. Targets: CultureMech:003043.

All six DSMZ owner amount snippets remain literal and hash-consistent with the captured response; their explanations distinguish provider normalization from measured volume. Preserve them. The target and JCM owners lack comparable amount evidence, and exact per-owner evidence must survive a future split/regeneration without reassignment to different formulations.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:003043.

27 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

## Findings

### f1: The generated identity and formulation come from different sources

blocker / open / confirmed; issue key: acidimicrobium-source-formulation-conflation.

JCM 698 is the retained accession, but every generated ingredient amount and order matches JCM 283; preparation retains JCM 698. DSMZ 709 is a third distinct contributor. Shared ingredient membership and historical merge fingerprints cannot support this synthetic combination.

### f2: A liquid yeast-stock dose is asserted as a mass concentration

major / open / confirmed; issue key: jcm698-yeast-stock-and-variant-prose.

JCM 698 owner ingredients[5] stores 2.5 G_PER_L although the primary and provider give 2.5 ml of a 10% stock without percent basis. Target and owner variant_children notes, plus reciprocal child variant_modifications, repeat that unsupported parent mass and misleading comparisons. The target ingredient value itself is 0.16 from JCM 283, not 2.5.

### f3: The JCM 283 child link points to a nonexistent category path

blocker / open / confirmed; issue key: jcm283-dangling-child-path.

Target and JCM 698 owner variant_children[1].path name the bacterial directory, while the exact CultureMech:002641 contributor is under archaea. The ignored-inclusive path inventory finds only the latter. A successful reference command reporting zero checked references did not assess this defect.

### f4: Base pH, conditional branches and sterilization stages are conflated

major / open / confirmed; issue key: acidimicrobium-source-preparation-scope.

JCM 698 scalar pH 1.7 represents its conditional branch despite base prose at 2.0. JCM 283 scalar 1.7 loses its source range and its AUTOCLAVE action conflates main filtration with yeast-stock autoclaving. Source water and qualified JCM cycles are absent. The generated record combines these source contexts rather than representing one branch faithfully.

### f5: The retained UNDEFINED composition class loses specified chemistry

major / open / confirmed; issue key: acidimicrobium-composition-class.

The target/JCM 698 owner classify the base as UNDEFINED despite individually specified salts plus undefined yeast extract. The other owners already use SEMI_DEFINED. This is a composition classification issue, not evidence about phenotype or taxonomic suitability.

## Recommended Actions And Acceptance Checks

### a1

Keep the three exact maintained formulations separate, resolve owner-specific source issues, and regenerate using current lossless formulation boundaries. Preserve stable IDs and valid variant relationships; do not promote source-specific synonyms/categories or evidence into equivalence claims. Preserve historical merge events append-only with later clarification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Correct the JCM 698 normalized owner to preserve liquid stock dose, supplied stock label and unresolved percent basis/final volume. Reconcile both child relationship notes using source-specific quantities and pH branches. Do not infer the DSMZ 709 mass or a tenfold difference from the stock-volume number.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Correct the maintained JCM 698 child path after exact ID/content verification, retain its reciprocal parent link, and verify all relationship paths independently before regeneration. Do not silently treat basename similarity as existing-path resolution.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Recover exact owner-specific base and conditional pH, original solvent amounts, stock stages and preparation actions. Preserve ranges and JCM exception-qualified cycles without importing them into DSMZ 709. Keep conditional source language bounded and do not add growth assertions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Reassess the maintained JCM 698 composition class against the explicit inorganic ingredients and undefined yeast mixture, using SEMI_DEFINED where that exact base is retained. Keep any yeast-free conditional formulation separately classified; regenerate after source separation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-2 | data/normalized_yaml/bacterial/acidimicrobium_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch017/170/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch017/170/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml:1:id: CultureMech:003043<br>./data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml:1:id: CultureMech:003043<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch017/source-preflight-bound/170/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 11 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary-698 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=698; JCM 698 heading, main table, post-autoclave yeast-stock row, conditional comment and global cycle qualifier | supports | The base formulation is distinct from its explicitly conditional yeast-free/iron-enriched branch. Its yeast row is a liquid volume of a stock labelled 10%, with no stated percent basis. |
| primary-283 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=283; JCM 283 heading, entire main table, preparation and global cycle qualifier | supports | This distinct formulation specifies different salts/iron/yeast amounts and a pH range. Main filtration and yeast-stock autoclaving are separate. |
| primary-709 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium709.pdf; PDF page 1, main table and both numbered preparation paragraphs | supports | DSMZ 709 has its own direct yeast mass and base pH, with a separate conditional branch. No exact autoclave cycle is specified in this PDF; the JCM default must not be imported into this source. |
| provider-698 | https://mediadive.dsmz.de/rest/medium/J698; $.data.medium and solutions[0] ID 4607, recipe and steps | supports | Provider volume is 1002 ml; this differs from the nominal sum of its 1000 ml water and 2.5 ml yeast addition (1002.5 ml). Neither is established as measured final volume. Its pH metadata 1.7 must be distinguished from the base preparation at pH 2.0. |
| provider-283 | https://mediadive.dsmz.de/rest/medium/J283; $.data.medium and solutions[0] ID 3975, recipe and steps | supports | The provider declares 1000 ml and scalar pH 1.7; the primary gives pH 1.6–1.8. These scope differences are preserved, with no chronological claim. |
| provider-709 | https://mediadive.dsmz.de/rest/medium/709; $.data.medium and solutions[0] ID 1459, recipe and steps | supports | The provider declares 1000 ml and pH 2.0. All six existing DSMZ owner amount snippets exactly match this captured response and remain scoped to this formulation. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| variant-paths | /private/tmp/culturemech-review-work-batch017/170/variant-path-audit.json; Target and JCM 698 owner variant_children[1]; both child parent_media references | refutes | {"argv": ["rg", "--files", "--no-ignore", "--hidden", "data/normalized_yaml"], "exit_code": 0, "ignored_hidden_included": true, "broken_asserted_path": "data/normalized_yaml/bacterial/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml", "exact_existing_contributor_path": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml", "exact_contributor_id": "CultureMech:002641", "existing_contributor_sha256": "7604d1a843116fe4dd8bdd968a0bedcecc55977a3cc8eaa0591a8436e41811ed", "same_basename_candidates": ["data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml"], "reciprocal_parent_paths_resolve": true} |
| preflight-correction | /private/tmp/culturemech-review-work-batch017/batch017-tail-independent-audit.json; material_context_corrections for ordinal 170 | context_only | The independent preflight audit corrects the frozen summary overstatement that both sibling paths resolve. Frozen capture bytes remain unchanged; the current review explicitly assesses the broken bacterial path. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch017/170/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive ingestion recognizes percent-labelled liquid rows as stocks and separates them from compounds, but normalizes bare ml to per-liter units and classifies mixed preparation prose by one keyword action. Current formulation merge requires scientific-field equality and rejects incompatible sources. Do not attribute this historical mixed generated record to current equality-guarded behavior; owner repair and separately authorized regeneration are required. |
| writer-1 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive ingestion recognizes percent-labelled liquid rows as stocks and separates them from compounds, but normalizes bare ml to per-liter units and classifies mixed preparation prose by one keyword action. Current formulation merge requires scientific-field equality and rejects incompatible sources. Do not attribute this historical mixed generated record to current equality-guarded behavior; owner repair and separately authorized regeneration are required. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive ingestion recognizes percent-labelled liquid rows as stocks and separates them from compounds, but normalizes bare ml to per-liter units and classifies mixed preparation prose by one keyword action. Current formulation merge requires scientific-field equality and rejects incompatible sources. Do not attribute this historical mixed generated record to current equality-guarded behavior; owner repair and separately authorized regeneration are required. |
| history-metadata | data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml; data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml; data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml; data/normalized_yaml/bacterial/acidimicrobium_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "events": 7, "timestamp_issues": []}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- All required primary, provider, ontology and exact owner identity sources are available. Percent basis and physical final volume are unstated quantities, not assumed values.
- The source conditional comments are preserved as formulation branches, not independent evidence of organism growth or current phenotype. No source chronology is inferred from the differing provider and primary metadata.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T110527Z-culturemech-003043-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acidimicrobium_medium (CultureMech:003043)'
started_at: '2026-10-21T10:48:48Z'
finished_at: '2026-10-21T11:05:27Z'
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
summary: The generated JCM 698 record contains the six amounts from JCM 283 while
  retaining JCM 698 identity and preparation; three distinct normalized formulations
  were conflated. The JCM 698 owner misrepresents a liquid yeast-stock dose, pH and
  variant notes lose source scope, and one child path is broken. All exact source
  documents are available; six DSMZ-owner amount-evidence claims remain valid within
  their own provider scope.
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
  - path: data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml
    sha256: bcbc0cfaa1f1051913222f30e78b3a8c90309af82e60f9b73fa4f2f9e0227fae
    role: target
  - path: data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml
    sha256: 7604d1a843116fe4dd8bdd968a0bedcecc55977a3cc8eaa0591a8436e41811ed
    role: context
  - path: data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml
    sha256: b4fa1082521b0198ec1f63df3d5f03c1bc8c2e14e8f1251a6b3cf82b728b01e7
    role: context
  - path: data/normalized_yaml/bacterial/acidimicrobium_medium.yaml
    sha256: 4708a81c364961e8bc04983afb5b413d1c9b6ffe44bfb145bec2c36f3094246b
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
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
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
  - path: scripts/propose_media_variant_links.py
    sha256: bd5b0b86c9457e42ca52ba2b253e5842c7f414093ba15aaeb4f9f0d682b5f4c2
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: scripts/validate_media_variant_links.py
    sha256: d18ef71320a0c50abe085e151d0d0d4d963007d1e1c9afbefab97581a983e31e
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
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
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
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
  selection: Task review 170; batch 017 item 10 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding sixteen task batches
    contain 160 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 162 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003043
targets:
- target_id: CultureMech:003043
  path: data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml
  label: acidimicrobium_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidimicrobium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003043
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch017/170/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch017/170/strict.tsv"
  target_ids:
  - CultureMech:003043
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003043
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003043
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
  - CultureMech:003043
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T11:05:26Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:05:26Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:05:26Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/acidimicrobium_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:05:26Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:51.321714Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch017/170/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:53.941710Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch017/170/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:55.672577Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:56.588630Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T11:05:26Z'
  support: supports
  summary: './data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml:1:id: CultureMech:003043

    ./data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml:1:id: CultureMech:003043

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/source-preflight-bound/170/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T11:05:26Z'
  support: supports
  summary: 11 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 138107c5e40c065ffb93a7cd25570b9b62a45441ac0150b4b2ef27c4d12d41d4
- evidence_id: primary-698
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=698
  locator: JCM 698 heading, main table, post-autoclave yeast-stock row, conditional
    comment and global cycle qualifier
  accessed_at: '2026-10-21T10:35:30.536142Z'
  support: supports
  summary: The base formulation is distinct from its explicitly conditional yeast-free/iron-enriched
    branch. Its yeast row is a liquid volume of a stock labelled 10%, with no stated
    percent basis.
  snapshot_sha256: 4154e76475d6acd8a7bb6ec012d35c2322c3a5edfd6bf62706c532bb1a92310b
- evidence_id: primary-283
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=283
  locator: JCM 283 heading, entire main table, preparation and global cycle qualifier
  accessed_at: '2026-10-21T10:35:30.401904Z'
  support: supports
  summary: This distinct formulation specifies different salts/iron/yeast amounts
    and a pH range. Main filtration and yeast-stock autoclaving are separate.
  snapshot_sha256: c88ce0723ed9fc471190c0bdbecf2236a8aa10b09e17f14155df03e2db6cb20e
- evidence_id: primary-709
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium709.pdf
  locator: PDF page 1, main table and both numbered preparation paragraphs
  accessed_at: '2026-10-21T10:35:28.817020Z'
  support: supports
  summary: DSMZ 709 has its own direct yeast mass and base pH, with a separate conditional
    branch. No exact autoclave cycle is specified in this PDF; the JCM default must
    not be imported into this source.
  snapshot_sha256: 97742970076af5b6148ef3241d878bebf581a27a65506b3b3a09a5fa0790d77d
- evidence_id: provider-698
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J698
  locator: $.data.medium and solutions[0] ID 4607, recipe and steps
  accessed_at: '2026-10-21T10:35:27.450505Z'
  support: supports
  summary: Provider volume is 1002 ml; this differs from the nominal sum of its 1000
    ml water and 2.5 ml yeast addition (1002.5 ml). Neither is established as measured
    final volume. Its pH metadata 1.7 must be distinguished from the base preparation
    at pH 2.0.
  snapshot_sha256: 74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6
- evidence_id: provider-283
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J283
  locator: $.data.medium and solutions[0] ID 3975, recipe and steps
  accessed_at: '2026-10-21T10:35:27.442568Z'
  support: supports
  summary: The provider declares 1000 ml and scalar pH 1.7; the primary gives pH 1.6–1.8.
    These scope differences are preserved, with no chronological claim.
  snapshot_sha256: 4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad
- evidence_id: provider-709
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/709
  locator: $.data.medium and solutions[0] ID 1459, recipe and steps
  accessed_at: '2026-10-21T10:35:26.813174Z'
  support: supports
  summary: The provider declares 1000 ml and pH 2.0. All six existing DSMZ owner amount
    snippets exactly match this captured response and remain scoped to this formulation.
  snapshot_sha256: 9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: CHEBI:32588 resolves to potassium chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T11:05:26Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type":
    "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id":
    "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946":
    [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946",
    "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term":
    "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: variant-paths
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/170/variant-path-audit.json
  locator: Target and JCM 698 owner variant_children[1]; both child parent_media references
  accessed_at: '2026-10-21T11:05:26Z'
  support: refutes
  summary: '{"argv": ["rg", "--files", "--no-ignore", "--hidden", "data/normalized_yaml"],
    "exit_code": 0, "ignored_hidden_included": true, "broken_asserted_path": "data/normalized_yaml/bacterial/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml",
    "exact_existing_contributor_path": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml",
    "exact_contributor_id": "CultureMech:002641", "existing_contributor_sha256": "7604d1a843116fe4dd8bdd968a0bedcecc55977a3cc8eaa0591a8436e41811ed",
    "same_basename_candidates": ["data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml"],
    "reciprocal_parent_paths_resolve": true}'
  snapshot_sha256: 41547f30471fcdaeedba9fb150d394e8080fe95470d2f36022e2120c11c27229
  search_scope: rg --files --no-ignore --hidden across normalized corpus; exact asserted
    paths checked directly.
- evidence_id: preflight-correction
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/batch017-tail-independent-audit.json
  locator: material_context_corrections for ordinal 170
  accessed_at: '2026-10-21T11:05:26Z'
  support: context_only
  summary: The independent preflight audit corrects the frozen summary overstatement
    that both sibling paths resolve. Frozen capture bytes remain unchanged; the current
    review explicitly assesses the broken bacterial path.
  snapshot_sha256: 7da2f26264fe11c5ebb5e8ebb48df18260667aef2a4c4599bd5f3648478c1e1d
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/170/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T11:05:26Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: ca65120263f3a5f0268b20dca12e9fb5dffed545098a3ce56a94c09d48402ddf
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:05:26Z'
  support: context_only
  summary: Current MediaDive ingestion recognizes percent-labelled liquid rows as
    stocks and separates them from compounds, but normalizes bare ml to per-liter
    units and classifies mixed preparation prose by one keyword action. Current formulation
    merge requires scientific-field equality and rejects incompatible sources. Do
    not attribute this historical mixed generated record to current equality-guarded
    behavior; owner repair and separately authorized regeneration are required.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:05:26Z'
  support: context_only
  summary: Current MediaDive ingestion recognizes percent-labelled liquid rows as
    stocks and separates them from compounds, but normalizes bare ml to per-liter
    units and classifies mixed preparation prose by one keyword action. Current formulation
    merge requires scientific-field equality and rejects incompatible sources. Do
    not attribute this historical mixed generated record to current equality-guarded
    behavior; owner repair and separately authorized regeneration are required.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:05:26Z'
  support: context_only
  summary: Current MediaDive ingestion recognizes percent-labelled liquid rows as
    stocks and separates them from compounds, but normalizes bare ml to per-liter
    units and classifies mixed preparation prose by one keyword action. Current formulation
    merge requires scientific-field equality and rejects incompatible sources. Do
    not attribute this historical mixed generated record to current equality-guarded
    behavior; owner repair and separately authorized regeneration are required.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml; data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml;
    data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml; data/normalized_yaml/bacterial/acidimicrobium_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T11:05:26Z'
  support: context_only
  summary: '[{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml",
    "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml",
    "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003043
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Source identities, exact contributors and merged formulation
  outcome: concern
  summary: All three sources and normalized owners resolve by stable IDs and explicit
    merge provenance. The target ingredient list exactly equals JCM 283, while its
    ID/media_term and preparation come from JCM 698. Shared ingredient names do not
    establish formulation equivalence. DSMZ 709 is separately represented and retains
    its own existing amount evidence.
  target_ids:
  - CultureMech:003043
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - id-search
  - primary-698
  - primary-283
  - primary-709
  - provider-698
  - provider-283
  - provider-709
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: supported
  summary: '5 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 5/6 primary and 5/6 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Source forms
    are assessed separately.'
  target_ids:
  - CultureMech:003043
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - owner-2
  - chebi131527
  - chebi31795
  - chebi32588
  - chebi62946
  - chebi75836
  details: 'Instance coverage on a 0–100 percent scale, denominator 6: primary 83.33%;
    secondary 83.33%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: quantities
  area: quantity
  topic: All generated and owner amounts, source-only water and preparation/variant
    quantities
  outcome: concern
  summary: The 41-row inventory covers six conflicted generated amounts, every row
    of all three provider main tables, twelve preparation contexts, including four
    explicit unquantified source-only contexts and two variant-note comparisons. Six
    DSMZ owner amounts are verified against existing attached exact evidence; other
    unchanged owner amounts are evidence_only. JCM 698 yeast dose and source-volume
    disagreement remain explicit.
  target_ids:
  - CultureMech:003043
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - primary-698
  - primary-283
  - primary-709
  - provider-698
  - provider-283
  - provider-709
  - quantity-inventory
  details: '[{"field_path": "ingredients[0].concentration", "input": "target", "current":
    {"value": "0.4", "unit": "G_PER_L"}, "decision": "conflict", "source_snippets":
    [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\":
    1.62288,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}, {"source_key":
    "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\":
    2.02455,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation":
    "This value/order matches JCM 283, but the target identifies JCM 698 and retains
    its preparation. Resolve source identity and split formulations before selecting
    a replacement amount. Numerical coincidence for one component does not establish
    whole-medium equivalence."}, {"field_path": "ingredients[1].concentration", "input":
    "target", "current": {"value": "0.2", "unit": "G_PER_L"}, "decision": "conflict",
    "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].recipe[1]", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\":
    27,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.51355,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}, {"source_key":
    "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].recipe[1]", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\":
    27,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.399202,\n                        \"mmol_l\":
    3.02105,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation":
    "This value/order matches JCM 283, but the target identifies JCM 698 and retains
    its preparation. Resolve source identity and split formulations before selecting
    a replacement amount. Numerical coincidence for one component does not establish
    whole-medium equivalence."}, {"field_path": "ingredients[2].concentration", "input":
    "target", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "conflict",
    "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    1.34138,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}, {"source_key":
    "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].recipe[3]", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\":
    1.3387,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation":
    "This value/order matches JCM 283, but the target identifies JCM 698 and retains
    its preparation. Resolve source identity and split formulations before selecting
    a replacement amount. Numerical coincidence for one component does not establish
    whole-medium equivalence."}, {"field_path": "ingredients[3].concentration", "input":
    "target", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "conflict",
    "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].recipe[3]", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.574132,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}, {"source_key":
    "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\":
    1.14597,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation":
    "This value/order matches JCM 283, but the target identifies JCM 698 and retains
    its preparation. Resolve source identity and split formulations before selecting
    a replacement amount. Numerical coincidence for one component does not establish
    whole-medium equivalence."}, {"field_path": "ingredients[4].concentration", "input":
    "target", "current": {"value": "25", "unit": "G_PER_L"}, "decision": "conflict",
    "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].recipe[4]", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 25,\n                        \"mmol_l\":
    89.9232,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}, {"source_key":
    "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].recipe[4]", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 10,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.00998004,\n                        \"mmol_l\":
    0.0358975,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation":
    "This value/order matches JCM 283, but the target identifies JCM 698 and retains
    its preparation. Resolve source identity and split formulations before selecting
    a replacement amount. Numerical coincidence for one component does not establish
    whole-medium equivalence."}, {"field_path": "ingredients[5].concentration", "input":
    "target", "current": {"value": "0.16", "unit": "G_PER_L"}, "decision": "conflict",
    "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].recipe[5]", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\":
    0.16,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.16,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}, {"source_key":
    "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].recipe[6]", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"10%, BD-Difco\",\n                        \"amount\":
    2.5,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}],
    "explanation": "This value/order matches JCM 283, but the target identifies JCM
    698 and retains its preparation. Resolve source identity and split formulations
    before selecting a replacement amount. Numerical coincidence for one component
    does not establish whole-medium equivalence."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "current": {"value": "0.499002",
    "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J698",
    "provider_declared_volume_ml": 1002, "source_original_amount": 0.5, "source_original_unit":
    "g", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\":
    2.02455,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation":
    "The owner value matches provider g_l on its own declared basis, but lacks attached
    local amount evidence. Original source mass and stage must remain explicit; this
    does not establish physical final volume. Provider-basis arithmetic: 0.5 g / 1002
    ml gives 0.4990019960079840319361277445 g/L before rounding."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "current": {"value": "0.399202",
    "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J698",
    "provider_declared_volume_ml": 1002, "source_original_amount": 0.4, "source_original_unit":
    "g", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].recipe[1]", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\":
    27,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.399202,\n                        \"mmol_l\":
    3.02105,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation":
    "The owner value matches provider g_l on its own declared basis, but lacks attached
    local amount evidence. Original source mass and stage must remain explicit; this
    does not establish physical final volume. Provider-basis arithmetic: 0.4 g / 1002
    ml gives 0.3992015968063872255489021956 g/L before rounding."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "current": {"value": "0.199601",
    "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J698",
    "provider_declared_volume_ml": 1002, "source_original_amount": 0.2, "source_original_unit":
    "g", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\":
    1.14597,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation":
    "The owner value matches provider g_l on its own declared basis, but lacks attached
    local amount evidence. Original source mass and stage must remain explicit; this
    does not establish physical final volume. Provider-basis arithmetic: 0.2 g / 1002
    ml gives 0.1996007984031936127744510978 g/L before rounding."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "current": {"value": "0.0998004",
    "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J698",
    "provider_declared_volume_ml": 1002, "source_original_amount": 0.1, "source_original_unit":
    "g", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].recipe[3]", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\":
    1.3387,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation":
    "The owner value matches provider g_l on its own declared basis, but lacks attached
    local amount evidence. Original source mass and stage must remain explicit; this
    does not establish physical final volume. Provider-basis arithmetic: 0.1 g / 1002
    ml gives 0.09980039920159680638722554890 g/L before rounding."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "current": {"value": "0.00998004",
    "unit": "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J698",
    "provider_declared_volume_ml": 1002, "source_original_amount": 10, "source_original_unit":
    "mg", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].recipe[4]", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 10,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.00998004,\n                        \"mmol_l\":
    0.0358975,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "explanation":
    "The owner value matches provider g_l on its own declared basis, but lacks attached
    local amount evidence. Original source mass and stage must remain explicit; this
    does not establish physical final volume. Provider-basis arithmetic: 10 mg / 1002
    ml gives 0.009980039920159680638722554890 g/L before rounding."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml",
    "field_path": "preparation_steps (source water omitted)", "current": null, "decision":
    "add", "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].recipe[5]", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}], "source_original_amount":
    1000, "source_original_unit": "ml", "explanation": "Retain this source-specific
    solvent amount, not a mass concentration or assumed measured final volume. Keep
    the three owner recipes distinct."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "current": {"value": "2.5", "unit":
    "G_PER_L"}, "decision": "correct", "source_stage": "Main sol. J698", "provider_declared_volume_ml":
    1002, "source_original_amount": 2.5, "source_original_unit": "ml", "source_snippets":
    [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].recipe[6]", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"10%, BD-Difco\",\n                        \"amount\":
    2.5,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}],
    "explanation": "The owner stores 2.5 G_PER_L, but the source supplies 2.5 ml of
    a stock labelled 10% (BD-Difco), without a percent basis. Preserve liquid addition
    and stock label; do not infer 2.5 g/L, a mass/volume basis, or equivalence to
    DSMZ 709 yeast 0.25 g. Provider volume 1002 ml differs from the nominal 1002.5
    ml sum and is not a measured final volume."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "current": {"value": "0.4", "unit":
    "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J283", "provider_declared_volume_ml":
    1000, "source_original_amount": 0.4, "source_original_unit": "g", "source_snippets":
    [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\":
    1.62288,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation":
    "The owner value matches provider g_l on its own declared basis, but lacks attached
    local amount evidence. Original source mass and stage must remain explicit; this
    does not establish physical final volume. Provider-basis arithmetic: 0.4 g / 1000
    ml gives 0.4 g/L before rounding."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "current": {"value": "0.2", "unit":
    "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J283", "provider_declared_volume_ml":
    1000, "source_original_amount": 0.2, "source_original_unit": "g", "source_snippets":
    [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].recipe[1]", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\":
    27,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.51355,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation":
    "The owner value matches provider g_l on its own declared basis, but lacks attached
    local amount evidence. Original source mass and stage must remain explicit; this
    does not establish physical final volume. Provider-basis arithmetic: 0.2 g / 1000
    ml gives 0.2 g/L before rounding."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "current": {"value": "0.1", "unit":
    "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J283", "provider_declared_volume_ml":
    1000, "source_original_amount": 0.1, "source_original_unit": "g", "source_snippets":
    [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    1.34138,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation":
    "The owner value matches provider g_l on its own declared basis, but lacks attached
    local amount evidence. Original source mass and stage must remain explicit; this
    does not establish physical final volume. Provider-basis arithmetic: 0.1 g / 1000
    ml gives 0.1 g/L before rounding."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "current": {"value": "0.1", "unit":
    "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J283", "provider_declared_volume_ml":
    1000, "source_original_amount": 0.1, "source_original_unit": "g", "source_snippets":
    [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].recipe[3]", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.574132,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation":
    "The owner value matches provider g_l on its own declared basis, but lacks attached
    local amount evidence. Original source mass and stage must remain explicit; this
    does not establish physical final volume. Provider-basis arithmetic: 0.1 g / 1000
    ml gives 0.1 g/L before rounding."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "current": {"value": "25", "unit":
    "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J283", "provider_declared_volume_ml":
    1000, "source_original_amount": 25, "source_original_unit": "g", "source_snippets":
    [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].recipe[4]", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 25,\n                        \"mmol_l\":
    89.9232,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation":
    "The owner value matches provider g_l on its own declared basis, but lacks attached
    local amount evidence. Original source mass and stage must remain explicit; this
    does not establish physical final volume. Provider-basis arithmetic: 25 g / 1000
    ml gives 25 g/L before rounding."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "current": {"value": "0.16", "unit":
    "G_PER_L"}, "decision": "evidence_only", "source_stage": "Main sol. J283", "provider_declared_volume_ml":
    1000, "source_original_amount": 0.16, "source_original_unit": "g", "source_snippets":
    [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].recipe[5]", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\":
    0.16,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.16,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation":
    "The owner value matches provider g_l on its own declared basis, but lacks attached
    local amount evidence. Original source mass and stage must remain explicit; this
    does not establish physical final volume. Provider-basis arithmetic: 0.16 g /
    1000 ml gives 0.16 g/L before rounding."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml",
    "field_path": "preparation_steps (source water omitted)", "current": null, "decision":
    "add", "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].recipe[6]", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "source_original_amount":
    1000, "source_original_unit": "ml", "explanation": "Retain this source-specific
    solvent amount, not a mass concentration or assumed measured final volume. Keep
    the three owner recipes distinct."}, {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml",
    "field_path": "ingredients[0].concentration", "current": {"value": "0.5", "unit":
    "G_PER_L"}, "decision": "verified", "source_stage": "Main sol. 709", "provider_declared_volume_ml":
    1000, "source_original_amount": 0.5, "source_original_unit": "g", "source_snippets":
    [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709",
    "source_locator": "$.data.solutions[0].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.02859,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "explanation":
    "Existing attached exact provider evidence supports this unchanged owner amount
    at its declared basis. Preserve original mass and stage, and the evidence in this
    owner; do not transfer it to the generated mixed record. 0.5 g / 1000 ml = 0.5
    g/L on the provider basis; water alone does not prove final volume."}, {"input":
    "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "field_path": "ingredients[1].concentration",
    "current": {"value": "0.4", "unit": "G_PER_L"}, "decision": "verified", "source_stage":
    "Main sol. 709", "provider_declared_volume_ml": 1000, "source_original_amount":
    0.4, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadive709api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].recipe[1]",
    "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\":
    0.4,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.4,\n                        \"mmol_l\": 3.02709,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}],
    "explanation": "Existing attached exact provider evidence supports this unchanged
    owner amount at its declared basis. Preserve original mass and stage, and the
    evidence in this owner; do not transfer it to the generated mixed record. 0.4
    g / 1000 ml = 0.4 g/L on the provider basis; water alone does not prove final
    volume."}, {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml",
    "field_path": "ingredients[2].concentration", "current": {"value": "0.2", "unit":
    "G_PER_L"}, "decision": "verified", "source_stage": "Main sol. 709", "provider_declared_volume_ml":
    1000, "source_original_amount": 0.2, "source_original_unit": "g", "source_snippets":
    [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709",
    "source_locator": "$.data.solutions[0].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.14826,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "explanation":
    "Existing attached exact provider evidence supports this unchanged owner amount
    at its declared basis. Preserve original mass and stage, and the evidence in this
    owner; do not transfer it to the generated mixed record. 0.2 g / 1000 ml = 0.2
    g/L on the provider basis; water alone does not prove final volume."}, {"input":
    "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "field_path": "ingredients[3].concentration",
    "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "verified", "source_stage":
    "Main sol. 709", "provider_declared_volume_ml": 1000, "source_original_amount":
    0.1, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadive709api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].recipe[3]",
    "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\":
    0.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 1.34138,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}],
    "explanation": "Existing attached exact provider evidence supports this unchanged
    owner amount at its declared basis. Preserve original mass and stage, and the
    evidence in this owner; do not transfer it to the generated mixed record. 0.1
    g / 1000 ml = 0.1 g/L on the provider basis; water alone does not prove final
    volume."}, {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml",
    "field_path": "ingredients[4].concentration", "current": {"value": "0.01", "unit":
    "G_PER_L"}, "decision": "verified", "source_stage": "Main sol. 709", "provider_declared_volume_ml":
    1000, "source_original_amount": 0.01, "source_original_unit": "g", "source_snippets":
    [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709",
    "source_locator": "$.data.solutions[0].recipe[4]", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0359693,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "explanation":
    "Existing attached exact provider evidence supports this unchanged owner amount
    at its declared basis. Preserve original mass and stage, and the evidence in this
    owner; do not transfer it to the generated mixed record. 0.01 g / 1000 ml = 0.01
    g/L on the provider basis; water alone does not prove final volume."}, {"input":
    "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "field_path": "ingredients[5].concentration",
    "current": {"value": "0.25", "unit": "G_PER_L"}, "decision": "verified", "source_stage":
    "Main sol. 709", "provider_declared_volume_ml": 1000, "source_original_amount":
    0.25, "source_original_unit": "g", "source_snippets": [{"source_key": "mediadive709api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].recipe[5]",
    "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    0.25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.25,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "explanation":
    "Existing attached exact provider evidence supports this unchanged owner amount
    at its declared basis. Preserve original mass and stage, and the evidence in this
    owner; do not transfer it to the generated mixed record. 0.25 g / 1000 ml = 0.25
    g/L on the provider basis; water alone does not prove final volume."}, {"input":
    "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "field_path": "preparation_steps
    (source water omitted)", "current": null, "decision": "add", "source_snippets":
    [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709",
    "source_locator": "$.data.solutions[0].recipe[6]", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}], "source_original_amount":
    1000, "source_original_unit": "ml", "explanation": "Retain this source-specific
    solvent amount, not a mass concentration or assumed measured final volume. Keep
    the three owner recipes distinct."}, {"field_path": "ph_value (target and JCM
    698 owner)", "current": "existing scalar/prose as specified", "decision": "correct",
    "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].steps[0].step", "exact_source_quote": "pH
    to 2.0", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}],
    "explanation": "Existing scalar 1.7 is the conditional branch pH; restore base
    pH 2.0 while retaining 1.7 only with the yeast-free branch. Existing base preparation
    prose already says 2.0."}, {"field_path": "ph_value (JCM 283 owner)", "current":
    "existing scalar/prose as specified", "decision": "correct", "source_snippets":
    [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].steps[0].step", "exact_source_quote": "pH
    to 1.6-1.8", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}],
    "explanation": "Provider scalar 1.7 loses the primary range. Preserve the full
    range already present in owner prose, without asserting that 1.7 is a false possible
    value."}, {"field_path": "ph_value (DSMZ 709 owner)", "current": "existing scalar/prose
    as specified", "decision": "evidence_only", "source_snippets": [{"source_key":
    "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709",
    "source_locator": "$.data.solutions[0].steps[0].step", "exact_source_quote": "pH
    to 2.0", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}],
    "explanation": "The owner scalar and base prose are consistent with source base
    pH. Attach scoped evidence without borrowing the JCM branch as a universal condition."},
    {"field_path": "preparation_steps[1] (target and JCM 698 owner conditional branch)",
    "current": "existing scalar/prose as specified", "decision": "evidence_only",
    "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].steps[1].step", "exact_source_quote": "13.9
    g/L (final) FeSO4 x 7H2O and adjust pH to 1.7", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}],
    "explanation": "Retain both existing source quantities only with the explicit
    yeast-free conditional formulation. Do not sum this final concentration with the
    basal iron amount or assert growth for an unspecified organism."}, {"field_path":
    "preparation_steps[1] (DSMZ 709 owner conditional branch)", "current": "existing
    scalar/prose as specified", "decision": "evidence_only", "source_snippets": [{"source_key":
    "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709",
    "source_locator": "$.data.solutions[0].steps[1].step", "exact_source_quote": "13.90
    g/l FeSO4 x 7 H2O. Adjust medium pH to 1.7", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}],
    "explanation": "Keep the owner-specific conditional wording, omission of yeast
    and pH adjustment before autoclaving. Do not silently resolve whether its iron
    wording means addition versus replacement by borrowing the JCM final qualifier."},
    {"field_path": "preparation_steps[0] (JCM 283 yeast stock strength)", "current":
    "existing scalar/prose as specified", "decision": "evidence_only", "source_snippets":
    [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].steps[0].step", "exact_source_quote": "autoclaved
    10% solution", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}],
    "explanation": "This existing stock label has no stated percent basis; do not
    recast as PERCENT_W_V or derive a liquid dose. Main filtration remains distinct
    from stock autoclaving."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml",
    "field_path": "preparation_steps (missing qualified JCM cycle)", "current": null,
    "decision": "add", "source_snippets": [{"source_key": "jcm698", "source_url":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=698", "source_locator": "Global
    JCM qualifier before medium heading", "exact_source_quote": "Unless otherwise
    stated, sterilize media by autoclaving at 121°C for 15 min.", "snapshot_sha256":
    "4154e76475d6acd8a7bb6ec012d35c2322c3a5edfd6bf62706c532bb1a92310b", "parsed_text_sha256":
    "310fed215efc9448d394ab1ee38290c139a00527185cdd82d79efcf2e917e648"}], "explanation":
    "Preserve the source exception qualifier. Apply to explicit autoclave stages only,
    not JCM 283 main filtration, and do not transfer to DSMZ 709 where no cycle is
    supplied. For JCM 698 this is also missing from the generated target."}, {"input":
    "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml", "field_path":
    "preparation_steps (missing qualified JCM cycle)", "current": null, "decision":
    "add", "source_snippets": [{"source_key": "jcm283", "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=283",
    "source_locator": "Global JCM qualifier before medium heading", "exact_source_quote":
    "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
    "snapshot_sha256": "c88ce0723ed9fc471190c0bdbecf2236a8aa10b09e17f14155df03e2db6cb20e",
    "parsed_text_sha256": "dec625300e0fb56c6abfda28b096a8be75a4b46aa90fcbe67189a6a24724c84d"}],
    "explanation": "Preserve the source exception qualifier. Apply to explicit autoclave
    stages only, not JCM 283 main filtration, and do not transfer to DSMZ 709 where
    no cycle is supplied. For JCM 698 this is also missing from the generated target."},
    {"field_path": "variant_children[0].notes; reciprocal child variant_modifications",
    "current": "Reviewed same-name Acidimicrobium medium records; child rounds the
    inorganic salts to the same effective levels but lowers yeast extract from 2.5
    g/L to 0.25 g/L and changes pH from 1.7 to 2.0.", "decision": "correct", "source_snippets":
    [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].recipe[6]", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"10%, BD-Difco\",\n                        \"amount\":
    2.5,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"},
    {"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709",
    "source_locator": "$.data.solutions[0].recipe[5]", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.25,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}],
    "explanation": "The asserted parent 2.5 g/L yeast basis is actually a 2.5 ml stock
    addition with unspecified percent basis. Rewrite both ends of the relationship
    only after owner/source reconciliation; preserve source-specific pH/base/conditional
    scope and avoid a false tenfold mass comparison."}, {"field_path": "variant_children[1].notes;
    reciprocal child variant_modifications", "current": "Reviewed JCM Acidimicrobium/Ferroplasma
    pair; child keeps acidic pH 1.7 and same component set but changes sulfate/phosphate
    salts, raises FeSO4 from 0.00998004 to 25 g/L, and lowers yeast extract from 2.5
    to 0.16 g/L.", "decision": "correct", "source_snippets": [{"source_key": "mediadiveJ698api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/J698", "source_locator":
    "$.data.solutions[0].recipe[6]", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"10%, BD-Difco\",\n                        \"amount\":
    2.5,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"},
    {"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].recipe[5]", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\":
    0.16,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.16,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}], "explanation":
    "The asserted parent 2.5 g/L yeast basis is actually a 2.5 ml stock addition with
    unspecified percent basis. Rewrite both ends of the relationship only after owner/source
    reconciliation; preserve source-specific pH/base/conditional scope and avoid a
    false tenfold mass comparison."}, {"input": "data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml",
    "field_path": "preparation_steps (H2SO4 titrant quantity)", "current": "Sulfuric
    acid named in the source-specific pH-adjustment prose; no fixed strength or dose
    is supplied.", "decision": "not_quantified", "source_stage": "Each exact base/conditional
    adjustment stage remains separate; no condition is transferred between formulations.",
    "source_snippets": [{"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].steps[0].step", "exact_source_quote": "Adjust
    pH to 2.0 with H2SO4.", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"},
    {"source_key": "mediadiveJ698api", "source_url": "https://mediadive.dsmz.de/rest/medium/J698",
    "source_locator": "$.data.solutions[0].steps[1].step", "exact_source_quote": "adjust
    pH to 1.7 with H2SO4.", "snapshot_sha256": "74e40c762215f871e378fd4f712ca547f478843973a12d0362966029674facb6"}],
    "explanation": "The source specifies sulfuric acid for pH adjustment but neither
    a fixed titrant volume nor acid strength. Preserve the exact source pH/stage and
    leave these quantities unquantified. The JCM 698 preparation retained in the mixed
    generated target has the same limitation; resolving formulation identity comes
    first."}, {"input": "data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml",
    "field_path": "preparation_steps (H2SO4 titrant quantity)", "current": "Sulfuric
    acid named in the source-specific pH-adjustment prose; no fixed strength or dose
    is supplied.", "decision": "not_quantified", "source_stage": "Each exact base/conditional
    adjustment stage remains separate; no condition is transferred between formulations.",
    "source_snippets": [{"source_key": "mediadiveJ283api", "source_url": "https://mediadive.dsmz.de/rest/medium/J283",
    "source_locator": "$.data.solutions[0].steps[0].step", "exact_source_quote": "adjust
    pH to 1.6-1.8 with H2SO4,", "snapshot_sha256": "4195a8c6ca8fe27f1f7adc3ac328244c182a0750100e3c1ad1f5bc7b667973ad"}],
    "explanation": "The source specifies sulfuric acid for pH adjustment but neither
    a fixed titrant volume nor acid strength. Preserve the exact source pH/stage and
    leave these quantities unquantified; do not infer them from another formulation."},
    {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "field_path":
    "preparation_steps (H2SO4 titrant quantity)", "current": "Sulfuric acid named
    in the source-specific pH-adjustment prose; no fixed strength or dose is supplied.",
    "decision": "not_quantified", "source_stage": "Each exact base/conditional adjustment
    stage remains separate; no condition is transferred between formulations.", "source_snippets":
    [{"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709",
    "source_locator": "$.data.solutions[0].steps[0].step", "exact_source_quote": "adjust
    pH to 2.0 with H2SO4.", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"},
    {"source_key": "mediadive709api", "source_url": "https://mediadive.dsmz.de/rest/medium/709",
    "source_locator": "$.data.solutions[0].steps[1].step", "exact_source_quote": "Adjust
    medium pH to 1.7 with H2SO4 prior to autoclaving.", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}],
    "explanation": "The source specifies sulfuric acid for pH adjustment but neither
    a fixed titrant volume nor acid strength. Preserve the exact source pH/stage and
    leave these quantities unquantified; do not infer them from another formulation."},
    {"input": "data/normalized_yaml/bacterial/acidimicrobium_medium.yaml", "field_path":
    "preparation_steps[0] (yeast-stock strength and addition volume)", "current":
    "A sterile yeast-extract stock is named, without its strength or addition volume.",
    "decision": "not_quantified", "source_stage": "DSMZ 709 base formulation, post-autoclave
    addition only", "source_snippets": [{"source_key": "mediadive709api", "source_url":
    "https://mediadive.dsmz.de/rest/medium/709", "source_locator": "$.data.solutions[0].steps[0].step",
    "exact_source_quote": "After autoclaving add yeast extract from a sterile stock
    solution.", "snapshot_sha256": "9307b0a9265a74999e61f39b9c439a5f87a6c1b50653e74d7efb087be60bd9bc"}],
    "explanation": "Keep the independently verified main-recipe yeast mass 0.25 g
    and provider-declared 0.25 g/L unchanged. The stock strength and liquid addition
    volume are not supplied. Do not borrow the JCM 10% stock label, infer a percent
    basis, or derive a liquid dose."}]'
- assessment_id: forms
  area: grounding
  topic: Exact chemical forms and undefined yeast products
  outcome: supported
  summary: The five asserted CHEBI primary/secondary identities are live and preserve
    supplied inorganic forms, including the magnesium and iron heptahydrates. Exact
    pinned MIM keys do not establish recipe equivalence. Yeast extract remains an
    undefined mixture; JCM identifies BD-Difco, whereas the DSMZ table does not establish
    the same product identity. No replacement chemical or product mapping is inferred.
  target_ids:
  - CultureMech:003043
  evidence_ids:
  - record
  - primary-698
  - primary-283
  - primary-709
  - mim
  - chebi31795
  - chebi75836
  - chebi62946
  - chebi32588
  - chebi131527
- assessment_id: preparation
  area: completeness
  topic: Base versus conditional pH and sterilization stages
  outcome: concern
  summary: The generated ingredients and retained preparation belong to different
    formulations. JCM 698 base pH is 2.0 with a separate yeast-stock addition; 1.7
    belongs to its conditional branch. JCM 283 supplies range 1.6–1.8 and main filtration,
    yet its owner action is AUTOCLAVE because the same prose also mentions yeast-stock
    autoclaving. DSMZ 709 preparation is separately retained. Keep each branch, range,
    stock and qualified cycle at its exact source scope.
  target_ids:
  - CultureMech:003043
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - primary-698
  - primary-283
  - primary-709
  - quantity-inventory
- assessment_id: graph
  area: graph
  topic: Variant links and reciprocal source relationships
  outcome: concern
  summary: The target and JCM 698 owner point to a nonexistent bacterial-path JCM
    283 child. The exact stable-ID contributor exists under archaea and its parent
    path resolves. The other child and both reciprocal parent paths resolve exactly.
    Correct the link after verifying the source-specific relationship; a matching
    stable ID does not make the stored path valid.
  target_ids:
  - CultureMech:003043
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - variant-paths
  - preflight-correction
- assessment_id: classification
  area: scope
  topic: Composition class, source labels and organism scope
  outcome: concern
  summary: The defined inorganic salts plus undefined yeast support COMPLEX/SEMI_DEFINED
    for each base formulation, as already stored in the JCM 283 and DSMZ owners. UNDEFINED
    in the target/JCM 698 owner overstates the unknown fraction. The combined categories
    and Ferroplasma synonym are merge provenance, not evidence of cross-organism applicability
    or source equivalence. No phenotype, taxonomic assertion or growth result is inferred
    from medium titles or conditional comments.
  target_ids:
  - CultureMech:003043
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - primary-698
  - primary-283
  - primary-709
- assessment_id: evidence-placement
  area: evidence
  topic: Existing DSMZ evidence and missing evidence in other layers
  outcome: concern
  summary: All six DSMZ owner amount snippets remain literal and hash-consistent with
    the captured response; their explanations distinguish provider normalization from
    measured volume. Preserve them. The target and JCM owners lack comparable amount
    evidence, and exact per-owner evidence must survive a future split/regeneration
    without reassignment to different formulations.
  target_ids:
  - CultureMech:003043
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - provider-709
  - quantity-inventory
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 27 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:003043
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
  - owner-2
findings:
- finding_id: f1
  issue_key: acidimicrobium-source-formulation-conflation
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The generated identity and formulation come from different sources
  description: JCM 698 is the retained accession, but every generated ingredient amount
    and order matches JCM 283; preparation retains JCM 698. DSMZ 709 is a third distinct
    contributor. Shared ingredient membership and historical merge fingerprints cannot
    support this synthetic combination.
  target_ids:
  - CultureMech:003043
  field_paths:
  - media_term
  - ingredients
  - preparation_steps
  - synonyms
  - merged_from
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - primary-698
  - primary-283
  - primary-709
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidimicrobium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P1
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: jcm698-yeast-stock-and-variant-prose
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: A liquid yeast-stock dose is asserted as a mass concentration
  description: JCM 698 owner ingredients[5] stores 2.5 G_PER_L although the primary
    and provider give 2.5 ml of a 10% stock without percent basis. Target and owner
    variant_children notes, plus reciprocal child variant_modifications, repeat that
    unsupported parent mass and misleading comparisons. The target ingredient value
    itself is 0.16 from JCM 283, not 2.5.
  target_ids:
  - CultureMech:003043
  field_paths:
  - variant_children
  - ingredients[5].concentration
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - primary-698
  - provider-698
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidimicrobium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: jcm283-dangling-child-path
  category: graph
  severity: blocker
  status: open
  certainty: confirmed
  title: The JCM 283 child link points to a nonexistent category path
  description: Target and JCM 698 owner variant_children[1].path name the bacterial
    directory, while the exact CultureMech:002641 contributor is under archaea. The
    ignored-inclusive path inventory finds only the latter. A successful reference
    command reporting zero checked references did not assess this defect.
  target_ids:
  - CultureMech:003043
  field_paths:
  - variant_children[1].path
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - variant-paths
  - preflight-correction
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidimicrobium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P1
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: acidimicrobium-source-preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Base pH, conditional branches and sterilization stages are conflated
  description: JCM 698 scalar pH 1.7 represents its conditional branch despite base
    prose at 2.0. JCM 283 scalar 1.7 loses its source range and its AUTOCLAVE action
    conflates main filtration with yeast-stock autoclaving. Source water and qualified
    JCM cycles are absent. The generated record combines these source contexts rather
    than representing one branch faithfully.
  target_ids:
  - CultureMech:003043
  field_paths:
  - ph_value
  - preparation_steps
  - variant_children
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - primary-698
  - primary-283
  - primary-709
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidimicrobium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 is normally minor; major is justified because base/conditional
    pH and filtration/autoclaving boundaries materially alter source formulation interpretation.
- finding_id: f5
  issue_key: acidimicrobium-composition-class
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: The retained UNDEFINED composition class loses specified chemistry
  description: The target/JCM 698 owner classify the base as UNDEFINED despite individually
    specified salts plus undefined yeast extract. The other owners already use SEMI_DEFINED.
    This is a composition classification issue, not evidence about phenotype or taxonomic
    suitability.
  target_ids:
  - CultureMech:003043
  field_paths:
  - composition_type
  evidence_ids:
  - record
  - owner-0
  - primary-698
  - primary-283
  - primary-709
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidimicrobium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Keep the three exact maintained formulations separate, resolve owner-specific
    source issues, and regenerate using current lossless formulation boundaries. Preserve
    stable IDs and valid variant relationships; do not promote source-specific synonyms/categories
    or evidence into equivalence claims. Preserve historical merge events append-only
    with later clarification.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003043
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidimicrobium_medium.yaml
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
  description: Correct the JCM 698 normalized owner to preserve liquid stock dose,
    supplied stock label and unresolved percent basis/final volume. Reconcile both
    child relationship notes using source-specific quantities and pH branches. Do
    not infer the DSMZ 709 mass or a tenfold difference from the stock-volume number.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003043
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidimicrobium_medium.yaml
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
  description: Correct the maintained JCM 698 child path after exact ID/content verification,
    retain its reciprocal parent link, and verify all relationship paths independently
    before regeneration. Do not silently treat basename similarity as existing-path
    resolution.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003043
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidimicrobium_medium.yaml
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
  description: Recover exact owner-specific base and conditional pH, original solvent
    amounts, stock stages and preparation actions. Preserve ranges and JCM exception-qualified
    cycles without importing them into DSMZ 709. Keep conditional source language
    bounded and do not add growth assertions.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003043
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidimicrobium_medium.yaml
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
  description: Reassess the maintained JCM 698 composition class against the explicit
    inorganic ingredients and undefined yeast mixture, using SEMI_DEFINED where that
    exact base is retained. Keep any yeast-free conditional formulation separately
    classified; regenerate after source separation.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:003043
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J283_FERROPLASMA_ACIDIPHILUM_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidimicrobium_medium.yaml
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
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- All required primary, provider, ontology and exact owner identity sources are available.
  Percent basis and physical final volume are unstated quantities, not assumed values.
- The source conditional comments are preserved as formulation branches, not independent
  evidence of organism growth or current phenotype. No source chronology is inferred
  from the differing provider and primary metadata.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-017
- generated-medium
```
