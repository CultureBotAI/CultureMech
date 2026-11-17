# Source and formulation review: acidaminobacter_medium (CultureMech:004754)

- Review: 20261021T103523Z-culturemech-004754-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T10:23:16Z
- Finished UTC: 2026-10-21T10:35:23Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact DSMZ 292 and both normalized owners resolve. The generated recipe and both owners flatten 22 stock constituents into direct medium ingredients, omit stock additions and solvent context, and retain two supplied-form mismatches. Main provider concentrations agree on its declared basis, but source preparation and conflicting aerobic metadata require scoped recovery.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 158; batch 016 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding fifteen task batches contain 150 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 152 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:004754 | data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml | generated | acidaminobacter_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:004754 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:004754 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-016/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch016/158/strict.tsv |
| validate-terms | passed | True | CultureMech:004754 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:004754 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:004754 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Original KOMODO detail availability | unavailable | False | CultureMech:004754 | The captured detail request returned HTTP 403 once. This is not needed to substitute for the available exact DSMZ formulation and verified accession mapping. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:004754.

The four documented recipes completed; interpret the scope of each separately.

### Source accession, generated ownership and source-duplicate relationship

identity: supported. Targets: CultureMech:004754.

KOMODO 292 maps to DSMZ 292; both complete normalized owners and the generated target have identical local ingredient quantities. Their stable IDs and reciprocal SOURCE_DUPLICATE links are retained. Local signature equality does not validate stock stages or source amounts.

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:004754.

32 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 32/33 primary and 30/33 secondary instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 33: primary 96.97%; secondary 90.91%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Every main amount, stock constituent, addition, solvent and preparation quantity

quantity: concern. Targets: CultureMech:004754.

The 46-row inventory covers all 33 local ingredients, three missing stock additions, four missing solvent contexts and six preparation contexts. Eleven unchanged main values need claim-level evidence; 22 stock-strength values require correct stage representation. HCl percent basis and physical final volumes remain explicitly unresolved.

[{"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Glycine\",\n                        \"compound_id\": 358,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.49551,\n                        \"mmol_l\": 19.9216,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount": 1.5, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path": "ingredients[0].concentration", "decision": "evidence_only", "current": {"value": "1.49551", "unit": "G_PER_L"}, "source_form": "Glycine", "explanation": "Current number exactly matches provider g_l on its declared main basis, but no attached amount evidence exists in any local layer. Retain that provider scope, original source amount and stage; do not assert measured final volume. Arithmetic on the provider-declared basis: 1.5 g / 1003 ml gives 1.495513459621136590229312064 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[1]", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.99103,\n                        \"mmol_l\": 21.0576,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount": 3, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path": "ingredients[1].concentration", "decision": "evidence_only", "current": {"value": "2.99103", "unit": "G_PER_L"}, "source_form": "Na2SO4", "explanation": "Current number exactly matches provider g_l on its declared main basis, but no attached amount evidence exists in any local layer. Retain that provider scope, original source amount and stage; do not assert measured final volume. Arithmetic on the provider-declared basis: 3 g / 1003 ml gives 2.991026919242273180458624128 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199402,\n                        \"mmol_l\": 1.46527,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount": 0.2, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path": "ingredients[2].concentration", "decision": "evidence_only", "current": {"value": "0.199402", "unit": "G_PER_L"}, "source_form": "KH2PO4", "explanation": "Current number exactly matches provider g_l on its declared main basis, but no attached amount evidence exists in any local layer. Retain that provider scope, original source amount and stage; do not assert measured final volume. Arithmetic on the provider-declared basis: 0.2 g / 1003 ml gives 0.1994017946161515453639082752 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[3]", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\": 1.96162,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount": 0.4, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path": "ingredients[3].concentration", "decision": "evidence_only", "current": {"value": "0.398804", "unit": "G_PER_L"}, "source_form": "MgCl2 x 6 H2O", "explanation": "Current number exactly matches provider g_l on its declared main basis, but no attached amount evidence exists in any local layer. Retain that provider scope, original source amount and stage; do not assert measured final volume. Arithmetic on the provider-declared basis: 0.4 g / 1003 ml gives 0.3988035892323030907278165503 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[4]", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.19641,\n                        \"mmol_l\": 20.4725,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount": 1.2, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path": "ingredients[4].concentration", "decision": "evidence_only", "current": {"value": "1.19641", "unit": "G_PER_L"}, "source_form": "NaCl", "explanation": "Current number exactly matches provider g_l on its declared main basis, but no attached amount evidence exists in any local layer. Retain that provider scope, original source amount and stage; do not assert measured final volume. Arithmetic on the provider-declared basis: 1.2 g / 1003 ml gives 1.196410767696909272183449651 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[5]", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.149551,\n                        \"mmol_l\": 1.01725,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount": 0.15, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path": "ingredients[5].concentration", "decision": "evidence_only", "current": {"value": "0.149551", "unit": "G_PER_L"}, "source_form": "CaCl2 x 2 H2O", "explanation": "Current number exactly matches provider g_l on its declared main basis, but no attached amount evidence exists in any local layer. Retain that provider scope, original source amount and stage; do not assert measured final volume. Arithmetic on the provider-declared basis: 0.15 g / 1003 ml gives 0.1495513459621136590229312064 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[6]", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\": 5.34948,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount": 0.4, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path": "ingredients[6].concentration", "decision": "evidence_only", "current": {"value": "0.398804", "unit": "G_PER_L"}, "source_form": "KCl", "explanation": "Current number exactly matches provider g_l on its declared main basis, but no attached amount evidence exists in any local layer. Retain that provider scope, original source amount and stage; do not assert measured final volume. Arithmetic on the provider-declared basis: 0.4 g / 1003 ml gives 0.3988035892323030907278165503 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[7]", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199402,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount": 0.2, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path": "ingredients[7].concentration", "decision": "evidence_only", "current": {"value": "0.199402", "unit": "G_PER_L"}, "source_form": "Yeast extract", "explanation": "Current number exactly matches provider g_l on its declared main basis, but no attached amount evidence exists in any local layer. Retain that provider scope, original source amount and stage; do not assert measured final volume. Arithmetic on the provider-declared basis: 0.2 g / 1003 ml gives 0.1994017946161515453639082752 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[8]", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount": 1, "source_original_unit": "ml", "provider_declared_volume_ml": 1003, "field_path": "solutions (missing Trace element solution SL-10)", "decision": "add", "current": null, "explanation": "Preserve this exact 1 ml addition to the stated receiving batch separately from stock composition. Do not encode an unqualified 1 ml/L assertion or expand stock concentrations as direct medium amounts. Root evidence must name the exact solution path."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[9]", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount": 1, "source_original_unit": "ml", "provider_declared_volume_ml": 1003, "field_path": "solutions (missing Selenite-tungstate solution)", "decision": "add", "current": null, "explanation": "Preserve this exact 1 ml addition to the stated receiving batch separately from stock composition. Do not encode an unqualified 1 ml/L assertion or expand stock concentrations as direct medium amounts. Root evidence must name the exact solution path."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[10]", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}, {"source_key": "dsmz292", "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf", "source_locator": "PDF page 1 main table", "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml", "snapshot_sha256": "47a522dcda71f9f25bb9a362d5b3917b897198f5b3f106580f4b7dd165823974", "parsed_text_sha256": "4de2c8b21ac40e3418caed5d6e81f6bceaf2c6ae8ae0a1fb3e6e924108cd8d10"}], "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount": 0.5, "source_original_unit": "ml", "provider_declared_volume_ml": 1003, "field_path": "ingredients[8].concentration", "decision": "evidence_only", "current": {"value": "0.000498504", "unit": "G_PER_L"}, "source_form": "Sodium resazurin", "explanation": "Current number exactly matches provider g_l on its declared main basis, but no attached amount evidence exists in any local layer. Retain that provider scope, original source amount and stage; do not assert measured final volume. Source 0.1% w/v means 1 mg/ml; 0.50 ml supplies 0.5 mg. Dividing by provider 1.003 L gives 0.000498504 g/L after rounding. The stock label/dose must remain explicit; this arithmetic does not validate the neutral-resazurin term."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[11]", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.99402,\n                        \"mmol_l\": 23.7363,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount": 2, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path": "ingredients[9].concentration", "decision": "evidence_only", "current": {"value": "1.99402", "unit": "G_PER_L"}, "source_form": "NaHCO3", "explanation": "Current number exactly matches provider g_l on its declared main basis, but no attached amount evidence exists in any local layer. Retain that provider scope, original source amount and stage; do not assert measured final volume. Arithmetic on the provider-declared basis: 2 g / 1003 ml gives 1.994017946161515453639082752 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[12]", "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount": 1, "source_original_unit": "ml", "provider_declared_volume_ml": 1003, "field_path": "solutions (missing Wolin's vitamin solution (10x))", "decision": "add", "current": null, "explanation": "Preserve this exact 1 ml addition to the stated receiving batch separately from stock composition. Do not encode an unqualified 1 ml/L assertion or expand stock concentrations as direct medium amounts. Root evidence must name the exact solution path."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[13]", "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\": 1.24532,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount": 0.3, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path": "ingredients[10].concentration", "decision": "evidence_only", "current": {"value": "0.299103", "unit": "G_PER_L"}, "source_form": "Na2S x 9 H2O", "explanation": "Current number exactly matches provider g_l on its declared main basis, but no attached amount evidence exists in any local layer. Retain that provider scope, original source amount and stage; do not assert measured final volume. Arithmetic on the provider-declared basis: 0.3 g / 1003 ml gives 0.2991026919242273180458624128 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[14]", "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount": 1000, "source_original_unit": "ml", "provider_declared_volume_ml": 1003, "field_path": "preparation_steps (missing solvent for Main sol. 292)", "decision": "add", "current": null, "explanation": "Preserve the source solvent amount at this stage, not as a G_PER_L ingredient. Water alone does not prove final volume; SL-10 has a separately quoted explicit final make-up instruction."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount": 10, "source_original_unit": "ml", "provider_declared_volume_ml": 1000, "field_path": "ingredients[11].concentration", "decision": "correct", "current": {"value": "2.5", "unit": "G_PER_L"}, "source_form": "HCl", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. The primary supplies 10 ml of HCl labelled 25%, without a percent basis. Provider g_l=2.5 cannot validate a mass conversion without that basis/density. Preserve the liquid amount and ambiguity; no replacement mass or molarity is proposed."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[1]", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount": 1.5, "source_original_unit": "g", "provider_declared_volume_ml": 1000, "field_path": "ingredients[12].concentration", "decision": "correct", "current": {"value": "1.5", "unit": "G_PER_L"}, "source_form": "FeCl2 x 4 H2O", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 1.5 g / 1000 ml gives 1.5 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount": 70, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[13].concentration", "decision": "correct", "current": {"value": "0.07", "unit": "G_PER_L"}, "source_form": "ZnCl2", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 70 mg / 1000 ml gives 0.070 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[3]", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount": 100, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[14].concentration", "decision": "correct", "current": {"value": "0.1", "unit": "G_PER_L"}, "source_form": "MnCl2 x 4 H2O", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 100 mg / 1000 ml gives 0.100 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[4]", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount": 6, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[15].concentration", "decision": "correct", "current": {"value": "0.006", "unit": "G_PER_L"}, "source_form": "H3BO3", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 6 mg / 1000 ml gives 0.006 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[5]", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount": 190, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[16].concentration", "decision": "correct", "current": {"value": "0.19", "unit": "G_PER_L"}, "source_form": "CoCl2 x 6 H2O", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 190 mg / 1000 ml gives 0.190 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[6]", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount": 2, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[17].concentration", "decision": "correct", "current": {"value": "0.002", "unit": "G_PER_L"}, "source_form": "CuCl2 x 2 H2O", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 2 mg / 1000 ml gives 0.002 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[7]", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount": 24, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[18].concentration", "decision": "correct", "current": {"value": "0.024", "unit": "G_PER_L"}, "source_form": "NiCl2 x 6 H2O", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 24 mg / 1000 ml gives 0.024 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[8]", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount": 36, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[19].concentration", "decision": "correct", "current": {"value": "0.036", "unit": "G_PER_L"}, "source_form": "Na2MoO4 x 2 H2O", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 36 mg / 1000 ml gives 0.036 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[9]", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount": 990, "source_original_unit": "ml", "provider_declared_volume_ml": 1000, "field_path": "preparation_steps (missing solvent for Trace element solution SL-10)", "decision": "add", "current": null, "explanation": "Preserve the source solvent amount at this stage, not as a G_PER_L ingredient. Water alone does not prove final volume; SL-10 has a separately quoted explicit final make-up instruction."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[2].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Selenite-tungstate solution", "source_solution_id": 777, "source_original_amount": 0.5, "source_original_unit": "g", "provider_declared_volume_ml": 1000, "field_path": "ingredients[20].concentration", "decision": "correct", "current": {"value": "0.5", "unit": "G_PER_L"}, "source_form": "NaOH", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 0.5 g / 1000 ml gives 0.5 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[2].recipe[1]", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Selenite-tungstate solution", "source_solution_id": 777, "source_original_amount": 3, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[21].concentration", "decision": "correct", "current": {"value": "0.003", "unit": "G_PER_L"}, "source_form": "Na2SeO3 x 5 H2O", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 3 mg / 1000 ml gives 0.003 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[2].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Selenite-tungstate solution", "source_solution_id": 777, "source_original_amount": 4, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[22].concentration", "decision": "correct", "current": {"value": "0.004", "unit": "G_PER_L"}, "source_form": "Na2WO4 x 2 H2O", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 4 mg / 1000 ml gives 0.004 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[2].recipe[3]", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Selenite-tungstate solution", "source_solution_id": 777, "source_original_amount": 1000, "source_original_unit": "ml", "provider_declared_volume_ml": 1000, "field_path": "preparation_steps (missing solvent for Selenite-tungstate solution)", "decision": "add", "current": null, "explanation": "Preserve the source solvent amount at this stage, not as a G_PER_L ingredient. Water alone does not prove final volume; SL-10 has a separately quoted explicit final make-up instruction."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[3].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Wolin's vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount": 20, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[23].concentration", "decision": "correct", "current": {"value": "0.02", "unit": "G_PER_L"}, "source_form": "Biotin", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 20 mg / 1000 ml gives 0.020 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[3].recipe[1]", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Wolin's vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount": 20, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[24].concentration", "decision": "correct", "current": {"value": "0.02", "unit": "G_PER_L"}, "source_form": "Folic acid", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 20 mg / 1000 ml gives 0.020 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[3].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Wolin's vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount": 100, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[25].concentration", "decision": "correct", "current": {"value": "0.1", "unit": "G_PER_L"}, "source_form": "Pyridoxine hydrochloride", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 100 mg / 1000 ml gives 0.100 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[3].recipe[3]", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Wolin's vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount": 50, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[26].concentration", "decision": "correct", "current": {"value": "0.05", "unit": "G_PER_L"}, "source_form": "Thiamine HCl", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 50 mg / 1000 ml gives 0.050 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[3].recipe[4]", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Wolin's vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount": 50, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[27].concentration", "decision": "correct", "current": {"value": "0.05", "unit": "G_PER_L"}, "source_form": "Riboflavin", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 50 mg / 1000 ml gives 0.050 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[3].recipe[5]", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Wolin's vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount": 50, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[28].concentration", "decision": "correct", "current": {"value": "0.05", "unit": "G_PER_L"}, "source_form": "Nicotinic acid", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 50 mg / 1000 ml gives 0.050 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[3].recipe[6]", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Wolin's vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount": 50, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[29].concentration", "decision": "correct", "current": {"value": "0.05", "unit": "G_PER_L"}, "source_form": "Calcium D-(+)-pantothenate", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 50 mg / 1000 ml gives 0.050 g/L before provider rounding. The source explicitly supplies the D form; the generic-label concern from other pantothenate recipes is not applicable here."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[3].recipe[7]", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Wolin's vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount": 1, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[30].concentration", "decision": "correct", "current": {"value": "0.001", "unit": "G_PER_L"}, "source_form": "Vitamin B12", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 1 mg / 1000 ml gives 0.001 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[3].recipe[8]", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Wolin's vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount": 50, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[31].concentration", "decision": "correct", "current": {"value": "0.05", "unit": "G_PER_L"}, "source_form": "p-Aminobenzoic acid", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 50 mg / 1000 ml gives 0.050 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[3].recipe[9]", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Wolin's vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount": 50, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path": "ingredients[32].concentration", "decision": "correct", "current": {"value": "0.05", "unit": "G_PER_L"}, "source_form": "(DL)-alpha-Lipoic acid", "explanation": "Current direct-medium value is the provider stock concentration. Restore the named stock composition and its separate receiving dose, with source-original units and explicit stock basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium concentration. Arithmetic on the provider-declared basis: 50 mg / 1000 ml gives 0.050 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[3].recipe[10]", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage": "Wolin's vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount": 1000, "source_original_unit": "ml", "provider_declared_volume_ml": 1000, "field_path": "preparation_steps (missing solvent for Wolin's vitamin solution (10x))", "decision": "add", "current": null, "explanation": "Preserve the source solvent amount at this stage, not as a G_PER_L ingredient. Water alone does not prove final volume; SL-10 has a separately quoted explicit final make-up instruction."}, {"field_path": "preparation_steps (initial pH)", "decision": "add", "current": null, "owner_decisions": {"data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml": "add", "data/normalized_yaml/bacterial/acidaminobacter_medium.yaml": "evidence_only"}, "source_stage": "main or exact named stock preparation as located", "source_snippets": [{"source_key": "dsmz292", "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf", "source_locator": "PDF page 1 main preparation; initial pH", "exact_source_quote": "adjust pH to 6.5", "snapshot_sha256": "47a522dcda71f9f25bb9a362d5b3917b897198f5b3f106580f4b7dd165823974", "parsed_text_sha256": "4de2c8b21ac40e3418caed5d6e81f6bceaf2c6ae8ae0a1fb3e6e924108cd8d10"}], "explanation": "Initial pH belongs before sparging and is distinct from the already stored final range. The DSMZ owner retains corresponding prose; the target and KOMODO owner omit it."}, {"field_path": "preparation_steps (initial gas and sparging duration)", "decision": "add", "current": null, "owner_decisions": {"data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml": "add", "data/normalized_yaml/bacterial/acidaminobacter_medium.yaml": "evidence_only"}, "source_stage": "main or exact named stock preparation as located", "source_snippets": [{"source_key": "dsmz292", "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf", "source_locator": "PDF page 1 main preparation; initial gas and duration", "exact_source_quote": "sparge with 100% N2 gas for 30 - 45 min", "snapshot_sha256": "47a522dcda71f9f25bb9a362d5b3917b897198f5b3f106580f4b7dd165823974", "parsed_text_sha256": "4de2c8b21ac40e3418caed5d6e81f6bceaf2c6ae8ae0a1fb3e6e924108cd8d10"}], "explanation": "Retain the exact gas and time range; the source does not state a replacement midpoint. The DSMZ owner retains corresponding prose; the target and KOMODO owner omit it."}, {"field_path": "preparation_steps (vitamin and sulfide stock gas)", "decision": "add", "current": null, "owner_decisions": {"data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml": "add", "data/normalized_yaml/bacterial/acidaminobacter_medium.yaml": "evidence_only"}, "source_stage": "main or exact named stock preparation as located", "source_snippets": [{"source_key": "dsmz292", "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf", "source_locator": "PDF page 1 main preparation; vitamin/sulfide stocks", "exact_source_quote": "stock solutions prepared under\n100% N2 gas", "snapshot_sha256": "47a522dcda71f9f25bb9a362d5b3917b897198f5b3f106580f4b7dd165823974", "parsed_text_sha256": "4de2c8b21ac40e3418caed5d6e81f6bceaf2c6ae8ae0a1fb3e6e924108cd8d10"}], "explanation": "This second gas context applies to the anoxic vitamin and sulfide stocks after the stated autoclaving stage. The DSMZ owner retains corresponding prose; the target and KOMODO owner omit it."}, {"field_path": "preparation_steps (bicarbonate stock gas)", "decision": "add", "current": null, "owner_decisions": {"data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml": "add", "data/normalized_yaml/bacterial/acidaminobacter_medium.yaml": "evidence_only"}, "source_stage": "main or exact named stock preparation as located", "source_snippets": [{"source_key": "dsmz292", "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf", "source_locator": "PDF page 1 main preparation; bicarbonate stock", "exact_source_quote": "80% N2\nand 20% CO2 gas mixture", "snapshot_sha256": "47a522dcda71f9f25bb9a362d5b3917b897198f5b3f106580f4b7dd165823974", "parsed_text_sha256": "4de2c8b21ac40e3418caed5d6e81f6bceaf2c6ae8ae0a1fb3e6e924108cd8d10"}], "explanation": "Keep this distinct stock gas mixture and do not silently apply it to the main-medium sparging stage. The DSMZ owner retains corresponding prose; the target and KOMODO owner omit it."}, {"field_path": "ph_range", "decision": "evidence_only", "current": {"min": 7.4, "max": 7.5}, "owner_decisions": {"data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml": "evidence_only", "data/normalized_yaml/bacterial/acidaminobacter_medium.yaml": "evidence_only"}, "source_stage": "main or exact named stock preparation as located", "source_snippets": [{"source_key": "dsmz292", "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf", "source_locator": "PDF page 1 final pH instruction", "exact_source_quote": "7.4 - 7.5, if necessary.", "snapshot_sha256": "47a522dcda71f9f25bb9a362d5b3917b897198f5b3f106580f4b7dd165823974", "parsed_text_sha256": "4de2c8b21ac40e3418caed5d6e81f6bceaf2c6ae8ae0a1fb3e6e924108cd8d10"}], "explanation": "The final range is already stored in all layers; attach source evidence and retain the conditional adjustment wording."}, {"field_path": "preparation_steps (SL-10 final make-up)", "decision": "add", "current": null, "owner_decisions": {"data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml": "add", "data/normalized_yaml/bacterial/acidaminobacter_medium.yaml": "correct"}, "source_stage": "main or exact named stock preparation as located", "source_snippets": [{"source_key": "dsmz292", "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf", "source_locator": "PDF page 1 SL-10 preparation paragraph", "exact_source_quote": "Finally\nmake up to 1000.00 ml.", "snapshot_sha256": "47a522dcda71f9f25bb9a362d5b3917b897198f5b3f106580f4b7dd165823974", "parsed_text_sha256": "4de2c8b21ac40e3418caed5d6e81f6bceaf2c6ae8ae0a1fb3e6e924108cd8d10"}], "explanation": "Explicit final volume belongs to SL-10, not the receiving medium or other stocks. Relocate the DSMZ owner root step to stock scope while preserving its sequence. The DSMZ owner retains corresponding prose; the target and KOMODO owner omit it."}]

### Exact supplied chemical forms

grounding: concern. Targets: CultureMech:004754.

Nickel chloride hexahydrate is linked in both primary and secondary slots to anhydrous nickel dichloride CHEBI:34887. Sodium resazurin is linked to neutral CHEBI:8806. Other explicitly named hydrates match the captured formulas. D-pantothenate is source-explicit and consistent with CHEBI:31345 D synonyms/structure; DL-lipoic acid retains its source label without an invented stereospecific ID.

### Preparation stages, sterilization and conflicting aerobic metadata

completeness: concern. Targets: CultureMech:004754.

The DSMZ owner preserves the main anoxic preparation and an SL-10 paragraph, but places both at root; the target and KOMODO owner omit them. Preserve initial/final pH, gas/duration and distinct stock gas contexts, vitamin filtration, delayed additions and SL-10 dissolution sequence. The exact DSMZ source does not specify an autoclave temperature/time; none is supplied here. Catalogue aerobic metadata conflicts with this preparation scope without a demonstrated source chronology.

### Medium classification, physical state and organism assertions

scope: supported. Targets: CultureMech:004754.

COMPLEX/SEMI_DEFINED is consistent with named salts, glycine and undefined yeast extract; LIQUID is compatible with the supplied formulation. The bacterial category is catalogue organization, not a strain-specific growth assertion. No target_organisms, taxonomy ID, temperature or growth evidence is invented from the title; the aerobic note is separately disputed.

### Quantity evidence and citation placement

evidence: concern. Targets: CultureMech:004754.

Source URLs in notes do not support all ingredient claims. Each retained main amount and restored stock constituent needs evidence on the appropriate ingredient descriptor; stock doses require root evidence with exact solution paths, and root references need collection/provider metadata. No SolutionDescriptor evidence slot is invented.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:004754.

28 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

## Findings

### f1: Stock concentrations are asserted as direct medium composition

blocker / open / confirmed; issue key: dsmz292-stock-stage-and-basis.

All three local layers list 22 constituents of SL-10, selenite-tungstate and 10x vitamins as direct medium concentrations while losing the three stock doses and four solvent contexts. This changes the represented formulation. HCl 2.5 G_PER_L also assumes an unsupported conversion from a bare 25% liquid stock. Eleven main g_l transcriptions match the provider but lack local scoped evidence.

### f2: Two asserted chemical identities do not preserve the supplied form

major / open / confirmed; issue key: dsmz292-supplied-form-grounding.

Source nickel chloride hexahydrate maps to an anhydrous structure in both CHEBI slots; sodium resazurin maps to the neutral compound. Existing live canonical IDs and pinned MIM rows do not validate those correspondences.

### f3: Source preparation is missing or assigned to the wrong stage

major / open / confirmed; issue key: dsmz292-preparation-oxygen-scope.

Target and KOMODO owner omit the exact source preparation. DSMZ owner retains an SL-10 step at medium root. The inherited Aerobic: Yes catalogue note conflicts with the explicitly anoxic main preparation. Lost stage distinctions materially alter interpretation despite an already present final pH range.

### f4: Import history contains malformed and timezone-naive timestamps

minor / open / confirmed; issue key: dsmz292-history-timestamp-shape.

Target and KOMODO owner each preserve one literal .fZ timestamp and one timezone-naive enrichment timestamp. The DSMZ owner timestamps are timezone-aware. This limits auditability; it does not negate the independently captured formulation evidence.

## Recommended Actions And Acceptance Checks

### a1

Restore exact stock structures, original units and source-scoped addition/batch evidence in both maintained owners, retaining unqualified HCl percent basis as unresolved. Preserve main provider quantities only with their declared basis; do not double-count stock constituents or infer measured final volume. Regenerate only after owner verification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve exact source-form groundings in both owners, preserving salt/hydrate notation and existing quantity evidence scope. Verify replacement identity independently or leave the unsupported assertion unassigned; do not infer new IDs or perform hydrate-based mass conversions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Recover and cite the source preparation in both owners with main/stock scope, conditional final pH and sterilization method. Preserve the conflicting aerobic catalogue assertion with explicit source scope pending resolution; do not assert a new chronology or invent a cycle. Place the SL-10 dissolution/final-volume paragraph under that stock.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Keep historical events append-only. Add a documented clarification if a later curation is authorized, and correct current writer timestamp generation before future imports without guessing the missing historical timezone.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/acidaminobacter_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch016/158/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-016/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch016/158/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml:1:id: CultureMech:004754<br>./data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml:1:id: CultureMech:004754<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch016/source-preflight-bound/158/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 36 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf; Both PDF pages: main medium, SL-10, selenite-tungstate and 10x Wolin vitamin tables and preparation paragraphs | supports | The exact receiving-medium document prints all three stock definitions. Parent media 320, 385 and 120 are subsection provenance, not substitute basal formulations. Source copyright year is 2022; it is not an independently established recipe publication date. |
| provider | https://mediadive.dsmz.de/rest/medium/292; $.data.medium and all four solutions/recipe/steps arrays | supports | Exact DSMZ 292 metadata and solution IDs resolve. Main declared volume is 1003 ml; each stock is declared 1000 ml. These are provider bases, not independently measured final volumes. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Full table header and exact ID 292 row | supports | Header and row: {"header": ["ID", "Name", "PH Info", "Is Complex", "Is Aerobic", "Is SubMedium", "Instructions"], "row": ["292", "ACIDAMINOBACTER medium", "7.4 - 7.5", "true", "true", "false", "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf"]}. Catalogue IsAerobic=true is the origin of the inherited Yes note; the primary preparation is explicitly anoxic. Identity and metadata only, not concentration or broad growth evidence. |
| unavailable-komodo292 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=292; Exact recorded access attempt | unknown | HTTP 403 prevented exact KOMODO detail access. Collection primary, provider and accession mapping remain available; no unavailable detail is claimed to have been inspected. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15428 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15428; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15428 resolves to glycine. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32149 resolves to sodium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15428": [{"label": "Glycine", "match_type": "preferred_term", "identifier": "CHEBI:15428", "preferred_term": "Glycine", "ontology_id": "CHEBI:15428", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| quantity-inventory | /private/tmp/culturemech-review-work-batch016/158/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive composition parsing uses the first solution and preserves stock references separately; historical flattened bytes must not be blamed on that updated path. Its unit normalizer still maps bare amounts to per-liter enums and its preparation parser traverses all solutions. DSMZ resolution copies ingredients/solutions but not preparation; KOMODO writes aerobic metadata and a platform-incompatible fractional-time format. Current merge logic compares formulation content and unions scoped evidence rather than proving source correctness. Correct owners first and review current generator behavior before regeneration; none was executed. |
| writer-1 | src/culturemech/enrich/dsmz_resolver.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive composition parsing uses the first solution and preserves stock references separately; historical flattened bytes must not be blamed on that updated path. Its unit normalizer still maps bare amounts to per-liter enums and its preparation parser traverses all solutions. DSMZ resolution copies ingredients/solutions but not preparation; KOMODO writes aerobic metadata and a platform-incompatible fractional-time format. Current merge logic compares formulation content and unions scoped evidence rather than proving source correctness. Correct owners first and review current generator behavior before regeneration; none was executed. |
| writer-2 | src/culturemech/import/komodo_web_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive composition parsing uses the first solution and preserves stock references separately; historical flattened bytes must not be blamed on that updated path. Its unit normalizer still maps bare amounts to per-liter enums and its preparation parser traverses all solutions. DSMZ resolution copies ingredients/solutions but not preparation; KOMODO writes aerobic metadata and a platform-incompatible fractional-time format. Current merge logic compares formulation content and unions scoped evidence rather than proving source correctness. Correct owners first and review current generator behavior before regeneration; none was executed. |
| writer-3 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive composition parsing uses the first solution and preserves stock references separately; historical flattened bytes must not be blamed on that updated path. Its unit normalizer still maps bare amounts to per-liter enums and its preparation parser traverses all solutions. DSMZ resolution copies ingredients/solutions but not preparation; KOMODO writes aerobic metadata and a platform-incompatible fractional-time format. Current merge logic compares formulation content and unions scoped evidence rather than proving source correctness. Correct owners first and review current generator behavior before regeneration; none was executed. |
| writer-4 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive composition parsing uses the first solution and preserves stock references separately; historical flattened bytes must not be blamed on that updated path. Its unit normalizer still maps bare amounts to per-liter enums and its preparation parser traverses all solutions. DSMZ resolution copies ingredients/solutions but not preparation; KOMODO writes aerobic metadata and a platform-incompatible fractional-time format. Current merge logic compares formulation content and unions scoped evidence rather than proving source correctness. Correct owners first and review current generator behavior before regeneration; none was executed. |
| history-metadata | data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml; data/normalized_yaml/bacterial/acidaminobacter_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 11, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:10.545821"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:10.545821"}]}, {"input": "data/normalized_yaml/bacterial/acidaminobacter_medium.yaml", "events": 8, "timestamp_issues": []}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No required source identity/formulation check is unavailable: the exact primary includes all three stocks. The optional KOMODO detail 403 is explicitly retained.
- Source water amounts and provider volumes are separately reported; this review does not validate a physical final volume or infer HCl percent basis/density.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T103523Z-culturemech-004754-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acidaminobacter_medium (CultureMech:004754)'
started_at: '2026-10-21T10:23:16Z'
finished_at: '2026-10-21T10:35:23Z'
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
summary: Exact DSMZ 292 and both normalized owners resolve. The generated recipe and
  both owners flatten 22 stock constituents into direct medium ingredients, omit stock
  additions and solvent context, and retain two supplied-form mismatches. Main provider
  concentrations agree on its declared basis, but source preparation and conflicting
  aerobic metadata require scoped recovery.
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
  - path: data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml
    sha256: 796a6ed4fb8632612279e88783750f56a8d3a98366b3540d01b17ca14d4cc086
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml
    sha256: 1c1adfd9225b0d9368bb7090c5bd05428e4c99ec49786d159df55009c8d1b32d
    role: context
  - path: data/normalized_yaml/bacterial/acidaminobacter_medium.yaml
    sha256: 5ad3417222e35509459feba012329c86879829e151bf9e14f3fb6b5951f07da8
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
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
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
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/import/komodo_importer.py
    sha256: 702733bd580e4ba28f77e183e1e8268f17ea2c1041cf7b3addd92919624f2706
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
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
  selection: Task review 158; batch 016 item 8 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding fifteen task batches
    contain 150 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 152 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:004754
targets:
- target_id: CultureMech:004754
  path: data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml
  label: acidaminobacter_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidaminobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:004754
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch016/158/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-016/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch016/158/strict.tsv"
  target_ids:
  - CultureMech:004754
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:004754
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:004754
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
  - CultureMech:004754
- check_id: optional-komodo-detail
  name: Original KOMODO detail availability
  required: false
  status: unavailable
  summary: The captured detail request returned HTTP 403 once. This is not needed
    to substitute for the available exact DSMZ formulation and verified accession
    mapping.
  target_ids:
  - CultureMech:004754
  evidence_ids:
  - unavailable-komodo292
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T10:35:20Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:35:20Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/acidaminobacter_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:35:20Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:24:00.286403Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch016/158/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T10:24:03.554477Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-016/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch016/158/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:24:07.541728Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:24:08.698920Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T10:35:20Z'
  support: supports
  summary: './data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml:1:id: CultureMech:004754

    ./data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml:1:id:
    CultureMech:004754

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch016/source-preflight-bound/158/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T10:35:20Z'
  support: supports
  summary: 36 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 98f362c93c58a4f4ed7439652f99e6a40c7cff78c081d341aefe4a62c943861e
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf
  locator: 'Both PDF pages: main medium, SL-10, selenite-tungstate and 10x Wolin vitamin
    tables and preparation paragraphs'
  accessed_at: '2026-10-21T10:12:24.624029Z'
  support: supports
  summary: The exact receiving-medium document prints all three stock definitions.
    Parent media 320, 385 and 120 are subsection provenance, not substitute basal
    formulations. Source copyright year is 2022; it is not an independently established
    recipe publication date.
  snapshot_sha256: 47a522dcda71f9f25bb9a362d5b3917b897198f5b3f106580f4b7dd165823974
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/292
  locator: $.data.medium and all four solutions/recipe/steps arrays
  accessed_at: '2026-10-21T10:12:23.961012Z'
  support: supports
  summary: Exact DSMZ 292 metadata and solution IDs resolve. Main declared volume
    is 1003 ml; each stock is declared 1000 ml. These are provider bases, not independently
    measured final volumes.
  snapshot_sha256: 438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Full table header and exact ID 292 row
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: 'Header and row: {"header": ["ID", "Name", "PH Info", "Is Complex", "Is
    Aerobic", "Is SubMedium", "Instructions"], "row": ["292", "ACIDAMINOBACTER medium",
    "7.4 - 7.5", "true", "true", "false", "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf"]}.
    Catalogue IsAerobic=true is the origin of the inherited Yes note; the primary
    preparation is explicitly anoxic. Identity and metadata only, not concentration
    or broad growth evidence.'
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: unavailable-komodo292
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=292
  locator: Exact recorded access attempt
  accessed_at: '2026-10-21T10:13:11.727524Z'
  support: unknown
  summary: HTTP 403 prevented exact KOMODO detail access. Collection primary, provider
    and accession mapping remain available; no unavailable detail is claimed to have
    been inspected.
  snapshot_sha256: e037f89a7693bd0d2daa422ee7270ce6b724c5afb4cab1d8570d75337d54db8e
- evidence_id: chebi131361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:27.980786Z'
  support: supports
  summary: CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi15428
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15428
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T10:12:25.545400Z'
  support: supports
  summary: CHEBI:15428 resolves to glycine. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: fe15e67af15eb83fc8824f11d1ba2dec039cb13dee005535e9acc71c1a2dd9d2
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: CHEBI:15940 resolves to nicotinic acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: CHEBI:15956 resolves to biotin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16494
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:13.001958Z'
  support: supports
  summary: CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi17883
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:37:25.439020Z'
  support: supports
  summary: CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: CHEBI:27470 resolves to folic acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32145
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:28.263004Z'
  support: supports
  summary: CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi32149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:18:34.792120Z'
  support: supports
  summary: CHEBI:32149 resolves to sodium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
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
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: CHEBI:34887 resolves to nickel dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: CHEBI:49976 resolves to zinc dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:49:55.693358Z'
  support: supports
  summary: CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T10:35:20Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15428": [{"label": "Glycine", "match_type":
    "preferred_term", "identifier": "CHEBI:15428", "preferred_term": "Glycine", "ontology_id":
    "CHEBI:15428", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940":
    [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940",
    "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type":
    "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id":
    "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494":
    [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label":
    "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term":
    "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term",
    "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id":
    "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883":
    [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883",
    "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label":
    "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961":
    [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier":
    "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label":
    "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term":
    "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term",
    "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label":
    "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term":
    "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type":
    "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887":
    [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887",
    "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type":
    "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl",
    "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier":
    "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride
    hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term":
    "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939":
    [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term":
    "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345":
    [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier":
    "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch016/158/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T10:35:20Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 6d0b9b4004ce60e1d21520c682ddcf1d86675b1814c77710d2e850a61f3ad8a4
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:35:20Z'
  support: context_only
  summary: Current MediaDive composition parsing uses the first solution and preserves
    stock references separately; historical flattened bytes must not be blamed on
    that updated path. Its unit normalizer still maps bare amounts to per-liter enums
    and its preparation parser traverses all solutions. DSMZ resolution copies ingredients/solutions
    but not preparation; KOMODO writes aerobic metadata and a platform-incompatible
    fractional-time format. Current merge logic compares formulation content and unions
    scoped evidence rather than proving source correctness. Correct owners first and
    review current generator behavior before regeneration; none was executed.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:35:20Z'
  support: context_only
  summary: Current MediaDive composition parsing uses the first solution and preserves
    stock references separately; historical flattened bytes must not be blamed on
    that updated path. Its unit normalizer still maps bare amounts to per-liter enums
    and its preparation parser traverses all solutions. DSMZ resolution copies ingredients/solutions
    but not preparation; KOMODO writes aerobic metadata and a platform-incompatible
    fractional-time format. Current merge logic compares formulation content and unions
    scoped evidence rather than proving source correctness. Correct owners first and
    review current generator behavior before regeneration; none was executed.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:35:20Z'
  support: context_only
  summary: Current MediaDive composition parsing uses the first solution and preserves
    stock references separately; historical flattened bytes must not be blamed on
    that updated path. Its unit normalizer still maps bare amounts to per-liter enums
    and its preparation parser traverses all solutions. DSMZ resolution copies ingredients/solutions
    but not preparation; KOMODO writes aerobic metadata and a platform-incompatible
    fractional-time format. Current merge logic compares formulation content and unions
    scoped evidence rather than proving source correctness. Correct owners first and
    review current generator behavior before regeneration; none was executed.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:35:20Z'
  support: context_only
  summary: Current MediaDive composition parsing uses the first solution and preserves
    stock references separately; historical flattened bytes must not be blamed on
    that updated path. Its unit normalizer still maps bare amounts to per-liter enums
    and its preparation parser traverses all solutions. DSMZ resolution copies ingredients/solutions
    but not preparation; KOMODO writes aerobic metadata and a platform-incompatible
    fractional-time format. Current merge logic compares formulation content and unions
    scoped evidence rather than proving source correctness. Correct owners first and
    review current generator behavior before regeneration; none was executed.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-4
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T10:35:20Z'
  support: context_only
  summary: Current MediaDive composition parsing uses the first solution and preserves
    stock references separately; historical flattened bytes must not be blamed on
    that updated path. Its unit normalizer still maps bare amounts to per-liter enums
    and its preparation parser traverses all solutions. DSMZ resolution copies ingredients/solutions
    but not preparation; KOMODO writes aerobic metadata and a platform-incompatible
    fractional-time format. Current merge logic compares formulation content and unions
    scoped evidence rather than proving source correctness. Correct owners first and
    review current generator behavior before regeneration; none was executed.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml;
    data/normalized_yaml/bacterial/acidaminobacter_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T10:35:20Z'
  support: context_only
  summary: '[{"input": "target", "events": 11, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:10.545821"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml",
    "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:10.545821"}]}, {"input": "data/normalized_yaml/bacterial/acidaminobacter_medium.yaml",
    "events": 8, "timestamp_issues": []}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:004754
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Source accession, generated ownership and source-duplicate relationship
  outcome: supported
  summary: KOMODO 292 maps to DSMZ 292; both complete normalized owners and the generated
    target have identical local ingredient quantities. Their stable IDs and reciprocal
    SOURCE_DUPLICATE links are retained. Local signature equality does not validate
    stock stages or source amounts.
  target_ids:
  - CultureMech:004754
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - provider
  - catalog
  - id-search
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '32 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 32/33 primary and 30/33 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form
    mismatch is addressed separately; valid IDs and labels do not establish correct
    source grounding.'
  target_ids:
  - CultureMech:004754
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi131361
  - chebi15428
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi176843
  - chebi17883
  - chebi26710
  - chebi27470
  - chebi30753
  - chebi30961
  - chebi31345
  - chebi32139
  - chebi32145
  - chebi32149
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi49105
  - chebi49976
  - chebi53503
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi76209
  - chebi86158
  - chebi86249
  - chebi86318
  - chebi86345
  - chebi86368
  - chebi8806
  details: 'Instance coverage on a 0–100 percent scale, denominator 33: primary 96.97%;
    secondary 90.91%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: quantities
  area: quantity
  topic: Every main amount, stock constituent, addition, solvent and preparation quantity
  outcome: concern
  summary: The 46-row inventory covers all 33 local ingredients, three missing stock
    additions, four missing solvent contexts and six preparation contexts. Eleven
    unchanged main values need claim-level evidence; 22 stock-strength values require
    correct stage representation. HCl percent basis and physical final volumes remain
    explicitly unresolved.
  target_ids:
  - CultureMech:004754
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - provider
  - quantity-inventory
  details: '[{"source_snippets": [{"source_key": "mediadive292api", "source_url":
    "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[0]",
    "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Glycine\",\n                        \"compound_id\": 358,\n                        \"amount\":
    1.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.49551,\n                        \"mmol_l\": 19.9216,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount":
    1.5, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path":
    "ingredients[0].concentration", "decision": "evidence_only", "current": {"value":
    "1.49551", "unit": "G_PER_L"}, "source_form": "Glycine", "explanation": "Current
    number exactly matches provider g_l on its declared main basis, but no attached
    amount evidence exists in any local layer. Retain that provider scope, original
    source amount and stage; do not assert measured final volume. Arithmetic on the
    provider-declared basis: 1.5 g / 1003 ml gives 1.495513459621136590229312064 g/L
    before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[1]",
    "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\":
    3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    2.99103,\n                        \"mmol_l\": 21.0576,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount":
    3, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path":
    "ingredients[1].concentration", "decision": "evidence_only", "current": {"value":
    "2.99103", "unit": "G_PER_L"}, "source_form": "Na2SO4", "explanation": "Current
    number exactly matches provider g_l on its declared main basis, but no attached
    amount evidence exists in any local layer. Retain that provider scope, original
    source amount and stage; do not assert measured final volume. Arithmetic on the
    provider-declared basis: 3 g / 1003 ml gives 2.991026919242273180458624128 g/L
    before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[2]",
    "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\":
    0.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.199402,\n                        \"mmol_l\": 1.46527,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount":
    0.2, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path":
    "ingredients[2].concentration", "decision": "evidence_only", "current": {"value":
    "0.199402", "unit": "G_PER_L"}, "source_form": "KH2PO4", "explanation": "Current
    number exactly matches provider g_l on its declared main basis, but no attached
    amount evidence exists in any local layer. Retain that provider scope, original
    source amount and stage; do not assert measured final volume. Arithmetic on the
    provider-declared basis: 0.2 g / 1003 ml gives 0.1994017946161515453639082752
    g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[3]",
    "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\":
    0.4,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.398804,\n                        \"mmol_l\": 1.96162,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount":
    0.4, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path":
    "ingredients[3].concentration", "decision": "evidence_only", "current": {"value":
    "0.398804", "unit": "G_PER_L"}, "source_form": "MgCl2 x 6 H2O", "explanation":
    "Current number exactly matches provider g_l on its declared main basis, but no
    attached amount evidence exists in any local layer. Retain that provider scope,
    original source amount and stage; do not assert measured final volume. Arithmetic
    on the provider-declared basis: 0.4 g / 1003 ml gives 0.3988035892323030907278165503
    g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[4]",
    "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\":
    1.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.19641,\n                        \"mmol_l\": 20.4725,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount":
    1.2, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path":
    "ingredients[4].concentration", "decision": "evidence_only", "current": {"value":
    "1.19641", "unit": "G_PER_L"}, "source_form": "NaCl", "explanation": "Current
    number exactly matches provider g_l on its declared main basis, but no attached
    amount evidence exists in any local layer. Retain that provider scope, original
    source amount and stage; do not assert measured final volume. Arithmetic on the
    provider-declared basis: 1.2 g / 1003 ml gives 1.196410767696909272183449651 g/L
    before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[5]",
    "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\":
    0.15,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.149551,\n                        \"mmol_l\": 1.01725,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount":
    0.15, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path":
    "ingredients[5].concentration", "decision": "evidence_only", "current": {"value":
    "0.149551", "unit": "G_PER_L"}, "source_form": "CaCl2 x 2 H2O", "explanation":
    "Current number exactly matches provider g_l on its declared main basis, but no
    attached amount evidence exists in any local layer. Retain that provider scope,
    original source amount and stage; do not assert measured final volume. Arithmetic
    on the provider-declared basis: 0.15 g / 1003 ml gives 0.1495513459621136590229312064
    g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[6]",
    "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\":
    0.4,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.398804,\n                        \"mmol_l\": 5.34948,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount":
    0.4, "source_original_unit": "g", "provider_declared_volume_ml": 1003, "field_path":
    "ingredients[6].concentration", "decision": "evidence_only", "current": {"value":
    "0.398804", "unit": "G_PER_L"}, "source_form": "KCl", "explanation": "Current
    number exactly matches provider g_l on its declared main basis, but no attached
    amount evidence exists in any local layer. Retain that provider scope, original
    source amount and stage; do not assert measured final volume. Arithmetic on the
    provider-declared basis: 0.4 g / 1003 ml gives 0.3988035892323030907278165503
    g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[0].recipe[7]",
    "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    0.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.199402,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Main sol. 292", "source_solution_id": 559, "source_original_amount": 0.2, "source_original_unit":
    "g", "provider_declared_volume_ml": 1003, "field_path": "ingredients[7].concentration",
    "decision": "evidence_only", "current": {"value": "0.199402", "unit": "G_PER_L"},
    "source_form": "Yeast extract", "explanation": "Current number exactly matches
    provider g_l on its declared main basis, but no attached amount evidence exists
    in any local layer. Retain that provider scope, original source amount and stage;
    do not assert measured final volume. Arithmetic on the provider-declared basis:
    0.2 g / 1003 ml gives 0.1994017946161515453639082752 g/L before provider rounding."},
    {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[0].recipe[8]", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Main sol. 292", "source_solution_id": 559, "source_original_amount": 1, "source_original_unit":
    "ml", "provider_declared_volume_ml": 1003, "field_path": "solutions (missing Trace
    element solution SL-10)", "decision": "add", "current": null, "explanation": "Preserve
    this exact 1 ml addition to the stated receiving batch separately from stock composition.
    Do not encode an unqualified 1 ml/L assertion or expand stock concentrations as
    direct medium amounts. Root evidence must name the exact solution path."}, {"source_snippets":
    [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[0].recipe[9]", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\":
    777,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Main sol. 292", "source_solution_id": 559, "source_original_amount": 1, "source_original_unit":
    "ml", "provider_declared_volume_ml": 1003, "field_path": "solutions (missing Selenite-tungstate
    solution)", "decision": "add", "current": null, "explanation": "Preserve this
    exact 1 ml addition to the stated receiving batch separately from stock composition.
    Do not encode an unqualified 1 ml/L assertion or expand stock concentrations as
    direct medium amounts. Root evidence must name the exact solution path."}, {"source_snippets":
    [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[0].recipe[10]", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"},
    {"source_key": "dsmz292", "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf",
    "source_locator": "PDF page 1 main table", "exact_source_quote": "Sodium resazurin
    (0.1% w/v) 0.50 ml", "snapshot_sha256": "47a522dcda71f9f25bb9a362d5b3917b897198f5b3f106580f4b7dd165823974",
    "parsed_text_sha256": "4de2c8b21ac40e3418caed5d6e81f6bceaf2c6ae8ae0a1fb3e6e924108cd8d10"}],
    "source_stage": "Main sol. 292", "source_solution_id": 559, "source_original_amount":
    0.5, "source_original_unit": "ml", "provider_declared_volume_ml": 1003, "field_path":
    "ingredients[8].concentration", "decision": "evidence_only", "current": {"value":
    "0.000498504", "unit": "G_PER_L"}, "source_form": "Sodium resazurin", "explanation":
    "Current number exactly matches provider g_l on its declared main basis, but no
    attached amount evidence exists in any local layer. Retain that provider scope,
    original source amount and stage; do not assert measured final volume. Source
    0.1% w/v means 1 mg/ml; 0.50 ml supplies 0.5 mg. Dividing by provider 1.003 L
    gives 0.000498504 g/L after rounding. The stock label/dose must remain explicit;
    this arithmetic does not validate the neutral-resazurin term."}, {"source_snippets":
    [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[0].recipe[11]", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.99402,\n                        \"mmol_l\":
    23.7363,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Main sol. 292", "source_solution_id": 559, "source_original_amount": 2, "source_original_unit":
    "g", "provider_declared_volume_ml": 1003, "field_path": "ingredients[9].concentration",
    "decision": "evidence_only", "current": {"value": "1.99402", "unit": "G_PER_L"},
    "source_form": "NaHCO3", "explanation": "Current number exactly matches provider
    g_l on its declared main basis, but no attached amount evidence exists in any
    local layer. Retain that provider scope, original source amount and stage; do
    not assert measured final volume. Arithmetic on the provider-declared basis: 2
    g / 1003 ml gives 1.994017946161515453639082752 g/L before provider rounding."},
    {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[0].recipe[12]", "exact_source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Main sol. 292", "source_solution_id": 559, "source_original_amount": 1, "source_original_unit":
    "ml", "provider_declared_volume_ml": 1003, "field_path": "solutions (missing Wolin''s
    vitamin solution (10x))", "decision": "add", "current": null, "explanation": "Preserve
    this exact 1 ml addition to the stated receiving batch separately from stock composition.
    Do not encode an unqualified 1 ml/L assertion or expand stock concentrations as
    direct medium amounts. Root evidence must name the exact solution path."}, {"source_snippets":
    [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[0].recipe[13]", "exact_source_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\":
    1.24532,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Main sol. 292", "source_solution_id": 559, "source_original_amount": 0.3, "source_original_unit":
    "g", "provider_declared_volume_ml": 1003, "field_path": "ingredients[10].concentration",
    "decision": "evidence_only", "current": {"value": "0.299103", "unit": "G_PER_L"},
    "source_form": "Na2S x 9 H2O", "explanation": "Current number exactly matches
    provider g_l on its declared main basis, but no attached amount evidence exists
    in any local layer. Retain that provider scope, original source amount and stage;
    do not assert measured final volume. Arithmetic on the provider-declared basis:
    0.3 g / 1003 ml gives 0.2991026919242273180458624128 g/L before provider rounding."},
    {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[0].recipe[14]", "exact_source_quote": "{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Main sol. 292", "source_solution_id": 559, "source_original_amount": 1000, "source_original_unit":
    "ml", "provider_declared_volume_ml": 1003, "field_path": "preparation_steps (missing
    solvent for Main sol. 292)", "decision": "add", "current": null, "explanation":
    "Preserve the source solvent amount at this stage, not as a G_PER_L ingredient.
    Water alone does not prove final volume; SL-10 has a separately quoted explicit
    final make-up instruction."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[0]",
    "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\":
    \"25%\",\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\":
    68.5683,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount":
    10, "source_original_unit": "ml", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[11].concentration", "decision": "correct", "current": {"value": "2.5",
    "unit": "G_PER_L"}, "source_form": "HCl", "explanation": "Current direct-medium
    value is the provider stock concentration. Restore the named stock composition
    and its separate receiving dose, with source-original units and explicit stock
    basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium
    concentration. The primary supplies 10 ml of HCl labelled 25%, without a percent
    basis. Provider g_l=2.5 cannot validate a mass conversion without that basis/density.
    Preserve the liquid amount and ambiguity; no replacement mass or molarity is proposed."},
    {"source_snippets": [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[1].recipe[1]", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount":
    1.5, "source_original_unit": "g", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[12].concentration", "decision": "correct", "current": {"value": "1.5",
    "unit": "G_PER_L"}, "source_form": "FeCl2 x 4 H2O", "explanation": "Current direct-medium
    value is the provider stock concentration. Restore the named stock composition
    and its separate receiving dose, with source-original units and explicit stock
    basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium
    concentration. Arithmetic on the provider-declared basis: 1.5 g / 1000 ml gives
    1.5 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[2]",
    "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\":
    70,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount":
    70, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[13].concentration", "decision": "correct", "current": {"value": "0.07",
    "unit": "G_PER_L"}, "source_form": "ZnCl2", "explanation": "Current direct-medium
    value is the provider stock concentration. Restore the named stock composition
    and its separate receiving dose, with source-original units and explicit stock
    basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium
    concentration. Arithmetic on the provider-declared basis: 70 mg / 1000 ml gives
    0.070 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[3]",
    "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\":
    100,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount":
    100, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[14].concentration", "decision": "correct", "current": {"value": "0.1",
    "unit": "G_PER_L"}, "source_form": "MnCl2 x 4 H2O", "explanation": "Current direct-medium
    value is the provider stock concentration. Restore the named stock composition
    and its separate receiving dose, with source-original units and explicit stock
    basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium
    concentration. Arithmetic on the provider-declared basis: 100 mg / 1000 ml gives
    0.100 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[4]",
    "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\":
    6,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount":
    6, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[15].concentration", "decision": "correct", "current": {"value": "0.006",
    "unit": "G_PER_L"}, "source_form": "H3BO3", "explanation": "Current direct-medium
    value is the provider stock concentration. Restore the named stock composition
    and its separate receiving dose, with source-original units and explicit stock
    basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium
    concentration. Arithmetic on the provider-declared basis: 6 mg / 1000 ml gives
    0.006 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[5]",
    "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\":
    190,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount":
    190, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[16].concentration", "decision": "correct", "current": {"value": "0.19",
    "unit": "G_PER_L"}, "source_form": "CoCl2 x 6 H2O", "explanation": "Current direct-medium
    value is the provider stock concentration. Restore the named stock composition
    and its separate receiving dose, with source-original units and explicit stock
    basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium
    concentration. Arithmetic on the provider-declared basis: 190 mg / 1000 ml gives
    0.190 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[6]",
    "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount":
    2, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[17].concentration", "decision": "correct", "current": {"value": "0.002",
    "unit": "G_PER_L"}, "source_form": "CuCl2 x 2 H2O", "explanation": "Current direct-medium
    value is the provider stock concentration. Restore the named stock composition
    and its separate receiving dose, with source-original units and explicit stock
    basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium
    concentration. Arithmetic on the provider-declared basis: 2 mg / 1000 ml gives
    0.002 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[7]",
    "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\":
    24,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount":
    24, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[18].concentration", "decision": "correct", "current": {"value": "0.024",
    "unit": "G_PER_L"}, "source_form": "NiCl2 x 6 H2O", "explanation": "Current direct-medium
    value is the provider stock concentration. Restore the named stock composition
    and its separate receiving dose, with source-original units and explicit stock
    basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium
    concentration. Arithmetic on the provider-declared basis: 24 mg / 1000 ml gives
    0.024 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[1].recipe[8]",
    "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    36,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount":
    36, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[19].concentration", "decision": "correct", "current": {"value": "0.036",
    "unit": "G_PER_L"}, "source_form": "Na2MoO4 x 2 H2O", "explanation": "Current
    direct-medium value is the provider stock concentration. Restore the named stock
    composition and its separate receiving dose, with source-original units and explicit
    stock basis. Do not retain it simultaneously as a direct ingredient or infer the
    final-medium concentration. Arithmetic on the provider-declared basis: 36 mg /
    1000 ml gives 0.036 g/L before provider rounding."}, {"source_snippets": [{"source_key":
    "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[1].recipe[9]", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Trace element solution SL-10", "source_solution_id": 595, "source_original_amount":
    990, "source_original_unit": "ml", "provider_declared_volume_ml": 1000, "field_path":
    "preparation_steps (missing solvent for Trace element solution SL-10)", "decision":
    "add", "current": null, "explanation": "Preserve the source solvent amount at
    this stage, not as a G_PER_L ingredient. Water alone does not prove final volume;
    SL-10 has a separately quoted explicit final make-up instruction."}, {"source_snippets":
    [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[2].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    12.5009,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Selenite-tungstate solution", "source_solution_id": 777, "source_original_amount":
    0.5, "source_original_unit": "g", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[20].concentration", "decision": "correct", "current": {"value": "0.5",
    "unit": "G_PER_L"}, "source_form": "NaOH", "explanation": "Current direct-medium
    value is the provider stock concentration. Restore the named stock composition
    and its separate receiving dose, with source-original units and explicit stock
    basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium
    concentration. Arithmetic on the provider-declared basis: 0.5 g / 1000 ml gives
    0.5 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[2].recipe[1]",
    "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\":
    3,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Selenite-tungstate solution", "source_solution_id": 777, "source_original_amount":
    3, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[21].concentration", "decision": "correct", "current": {"value": "0.003",
    "unit": "G_PER_L"}, "source_form": "Na2SeO3 x 5 H2O", "explanation": "Current
    direct-medium value is the provider stock concentration. Restore the named stock
    composition and its separate receiving dose, with source-original units and explicit
    stock basis. Do not retain it simultaneously as a direct ingredient or infer the
    final-medium concentration. Arithmetic on the provider-declared basis: 3 mg /
    1000 ml gives 0.003 g/L before provider rounding."}, {"source_snippets": [{"source_key":
    "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[2].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0121267,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Selenite-tungstate solution", "source_solution_id": 777, "source_original_amount":
    4, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[22].concentration", "decision": "correct", "current": {"value": "0.004",
    "unit": "G_PER_L"}, "source_form": "Na2WO4 x 2 H2O", "explanation": "Current direct-medium
    value is the provider stock concentration. Restore the named stock composition
    and its separate receiving dose, with source-original units and explicit stock
    basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium
    concentration. Arithmetic on the provider-declared basis: 4 mg / 1000 ml gives
    0.004 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[2].recipe[3]",
    "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Selenite-tungstate solution", "source_solution_id": 777, "source_original_amount":
    1000, "source_original_unit": "ml", "provider_declared_volume_ml": 1000, "field_path":
    "preparation_steps (missing solvent for Selenite-tungstate solution)", "decision":
    "add", "current": null, "explanation": "Preserve the source solvent amount at
    this stage, not as a G_PER_L ingredient. Water alone does not prove final volume;
    SL-10 has a separately quoted explicit final make-up instruction."}, {"source_snippets":
    [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[3].recipe[0]", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Wolin''s vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount":
    20, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[23].concentration", "decision": "correct", "current": {"value": "0.02",
    "unit": "G_PER_L"}, "source_form": "Biotin", "explanation": "Current direct-medium
    value is the provider stock concentration. Restore the named stock composition
    and its separate receiving dose, with source-original units and explicit stock
    basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium
    concentration. Arithmetic on the provider-declared basis: 20 mg / 1000 ml gives
    0.020 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[3].recipe[1]",
    "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\":
    20,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Wolin''s vitamin solution (10x)", "source_solution_id": 5980,
    "source_original_amount": 20, "source_original_unit": "mg", "provider_declared_volume_ml":
    1000, "field_path": "ingredients[24].concentration", "decision": "correct", "current":
    {"value": "0.02", "unit": "G_PER_L"}, "source_form": "Folic acid", "explanation":
    "Current direct-medium value is the provider stock concentration. Restore the
    named stock composition and its separate receiving dose, with source-original
    units and explicit stock basis. Do not retain it simultaneously as a direct ingredient
    or infer the final-medium concentration. Arithmetic on the provider-declared basis:
    20 mg / 1000 ml gives 0.020 g/L before provider rounding."}, {"source_snippets":
    [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[3].recipe[2]", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Wolin''s vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount":
    100, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[25].concentration", "decision": "correct", "current": {"value": "0.1",
    "unit": "G_PER_L"}, "source_form": "Pyridoxine hydrochloride", "explanation":
    "Current direct-medium value is the provider stock concentration. Restore the
    named stock composition and its separate receiving dose, with source-original
    units and explicit stock basis. Do not retain it simultaneously as a direct ingredient
    or infer the final-medium concentration. Arithmetic on the provider-declared basis:
    100 mg / 1000 ml gives 0.100 g/L before provider rounding."}, {"source_snippets":
    [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[3].recipe[3]", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Wolin''s vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount":
    50, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[26].concentration", "decision": "correct", "current": {"value": "0.05",
    "unit": "G_PER_L"}, "source_form": "Thiamine HCl", "explanation": "Current direct-medium
    value is the provider stock concentration. Restore the named stock composition
    and its separate receiving dose, with source-original units and explicit stock
    basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium
    concentration. Arithmetic on the provider-declared basis: 50 mg / 1000 ml gives
    0.050 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[3].recipe[4]",
    "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Wolin''s vitamin solution (10x)", "source_solution_id": 5980,
    "source_original_amount": 50, "source_original_unit": "mg", "provider_declared_volume_ml":
    1000, "field_path": "ingredients[27].concentration", "decision": "correct", "current":
    {"value": "0.05", "unit": "G_PER_L"}, "source_form": "Riboflavin", "explanation":
    "Current direct-medium value is the provider stock concentration. Restore the
    named stock composition and its separate receiving dose, with source-original
    units and explicit stock basis. Do not retain it simultaneously as a direct ingredient
    or infer the final-medium concentration. Arithmetic on the provider-declared basis:
    50 mg / 1000 ml gives 0.050 g/L before provider rounding."}, {"source_snippets":
    [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[3].recipe[5]", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Wolin''s vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount":
    50, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[28].concentration", "decision": "correct", "current": {"value": "0.05",
    "unit": "G_PER_L"}, "source_form": "Nicotinic acid", "explanation": "Current direct-medium
    value is the provider stock concentration. Restore the named stock composition
    and its separate receiving dose, with source-original units and explicit stock
    basis. Do not retain it simultaneously as a direct ingredient or infer the final-medium
    concentration. Arithmetic on the provider-declared basis: 50 mg / 1000 ml gives
    0.050 g/L before provider rounding."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[3].recipe[6]",
    "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Wolin''s vitamin solution (10x)", "source_solution_id": 5980,
    "source_original_amount": 50, "source_original_unit": "mg", "provider_declared_volume_ml":
    1000, "field_path": "ingredients[29].concentration", "decision": "correct", "current":
    {"value": "0.05", "unit": "G_PER_L"}, "source_form": "Calcium D-(+)-pantothenate",
    "explanation": "Current direct-medium value is the provider stock concentration.
    Restore the named stock composition and its separate receiving dose, with source-original
    units and explicit stock basis. Do not retain it simultaneously as a direct ingredient
    or infer the final-medium concentration. Arithmetic on the provider-declared basis:
    50 mg / 1000 ml gives 0.050 g/L before provider rounding. The source explicitly
    supplies the D form; the generic-label concern from other pantothenate recipes
    is not applicable here."}, {"source_snippets": [{"source_key": "mediadive292api",
    "source_url": "https://mediadive.dsmz.de/rest/medium/292", "source_locator": "$.data.solutions[3].recipe[7]",
    "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\":
    1,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\":
    0\n                    }", "snapshot_sha256": "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}],
    "source_stage": "Wolin''s vitamin solution (10x)", "source_solution_id": 5980,
    "source_original_amount": 1, "source_original_unit": "mg", "provider_declared_volume_ml":
    1000, "field_path": "ingredients[30].concentration", "decision": "correct", "current":
    {"value": "0.001", "unit": "G_PER_L"}, "source_form": "Vitamin B12", "explanation":
    "Current direct-medium value is the provider stock concentration. Restore the
    named stock composition and its separate receiving dose, with source-original
    units and explicit stock basis. Do not retain it simultaneously as a direct ingredient
    or infer the final-medium concentration. Arithmetic on the provider-declared basis:
    1 mg / 1000 ml gives 0.001 g/L before provider rounding."}, {"source_snippets":
    [{"source_key": "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[3].recipe[8]", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Wolin''s vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount":
    50, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[31].concentration", "decision": "correct", "current": {"value": "0.05",
    "unit": "G_PER_L"}, "source_form": "p-Aminobenzoic acid", "explanation": "Current
    direct-medium value is the provider stock concentration. Restore the named stock
    composition and its separate receiving dose, with source-original units and explicit
    stock basis. Do not retain it simultaneously as a direct ingredient or infer the
    final-medium concentration. Arithmetic on the provider-declared basis: 50 mg /
    1000 ml gives 0.050 g/L before provider rounding."}, {"source_snippets": [{"source_key":
    "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[3].recipe[9]", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Wolin''s vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount":
    50, "source_original_unit": "mg", "provider_declared_volume_ml": 1000, "field_path":
    "ingredients[32].concentration", "decision": "correct", "current": {"value": "0.05",
    "unit": "G_PER_L"}, "source_form": "(DL)-alpha-Lipoic acid", "explanation": "Current
    direct-medium value is the provider stock concentration. Restore the named stock
    composition and its separate receiving dose, with source-original units and explicit
    stock basis. Do not retain it simultaneously as a direct ingredient or infer the
    final-medium concentration. Arithmetic on the provider-declared basis: 50 mg /
    1000 ml gives 0.050 g/L before provider rounding."}, {"source_snippets": [{"source_key":
    "mediadive292api", "source_url": "https://mediadive.dsmz.de/rest/medium/292",
    "source_locator": "$.data.solutions[3].recipe[10]", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "snapshot_sha256":
    "438b3e89d0efb5fa8ee25a49c4e2fb072ef8c001bff61e19504b8d0b8f166aad"}], "source_stage":
    "Wolin''s vitamin solution (10x)", "source_solution_id": 5980, "source_original_amount":
    1000, "source_original_unit": "ml", "provider_declared_volume_ml": 1000, "field_path":
    "preparation_steps (missing solvent for Wolin''s vitamin solution (10x))", "decision":
    "add", "current": null, "explanation": "Preserve the source solvent amount at
    this stage, not as a G_PER_L ingredient. Water alone does not prove final volume;
    SL-10 has a separately quoted explicit final make-up instruction."}, {"field_path":
    "preparation_steps (initial pH)", "decision": "add", "current": null, "owner_decisions":
    {"data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml": "add",
    "data/normalized_yaml/bacterial/acidaminobacter_medium.yaml": "evidence_only"},
    "source_stage": "main or exact named stock preparation as located", "source_snippets":
    [{"source_key": "dsmz292", "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf",
    "source_locator": "PDF page 1 main preparation; initial pH", "exact_source_quote":
    "adjust pH to 6.5", "snapshot_sha256": "47a522dcda71f9f25bb9a362d5b3917b897198f5b3f106580f4b7dd165823974",
    "parsed_text_sha256": "4de2c8b21ac40e3418caed5d6e81f6bceaf2c6ae8ae0a1fb3e6e924108cd8d10"}],
    "explanation": "Initial pH belongs before sparging and is distinct from the already
    stored final range. The DSMZ owner retains corresponding prose; the target and
    KOMODO owner omit it."}, {"field_path": "preparation_steps (initial gas and sparging
    duration)", "decision": "add", "current": null, "owner_decisions": {"data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml":
    "add", "data/normalized_yaml/bacterial/acidaminobacter_medium.yaml": "evidence_only"},
    "source_stage": "main or exact named stock preparation as located", "source_snippets":
    [{"source_key": "dsmz292", "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf",
    "source_locator": "PDF page 1 main preparation; initial gas and duration", "exact_source_quote":
    "sparge with 100% N2 gas for 30 - 45 min", "snapshot_sha256": "47a522dcda71f9f25bb9a362d5b3917b897198f5b3f106580f4b7dd165823974",
    "parsed_text_sha256": "4de2c8b21ac40e3418caed5d6e81f6bceaf2c6ae8ae0a1fb3e6e924108cd8d10"}],
    "explanation": "Retain the exact gas and time range; the source does not state
    a replacement midpoint. The DSMZ owner retains corresponding prose; the target
    and KOMODO owner omit it."}, {"field_path": "preparation_steps (vitamin and sulfide
    stock gas)", "decision": "add", "current": null, "owner_decisions": {"data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml":
    "add", "data/normalized_yaml/bacterial/acidaminobacter_medium.yaml": "evidence_only"},
    "source_stage": "main or exact named stock preparation as located", "source_snippets":
    [{"source_key": "dsmz292", "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf",
    "source_locator": "PDF page 1 main preparation; vitamin/sulfide stocks", "exact_source_quote":
    "stock solutions prepared under\n100% N2 gas", "snapshot_sha256": "47a522dcda71f9f25bb9a362d5b3917b897198f5b3f106580f4b7dd165823974",
    "parsed_text_sha256": "4de2c8b21ac40e3418caed5d6e81f6bceaf2c6ae8ae0a1fb3e6e924108cd8d10"}],
    "explanation": "This second gas context applies to the anoxic vitamin and sulfide
    stocks after the stated autoclaving stage. The DSMZ owner retains corresponding
    prose; the target and KOMODO owner omit it."}, {"field_path": "preparation_steps
    (bicarbonate stock gas)", "decision": "add", "current": null, "owner_decisions":
    {"data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml": "add",
    "data/normalized_yaml/bacterial/acidaminobacter_medium.yaml": "evidence_only"},
    "source_stage": "main or exact named stock preparation as located", "source_snippets":
    [{"source_key": "dsmz292", "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf",
    "source_locator": "PDF page 1 main preparation; bicarbonate stock", "exact_source_quote":
    "80% N2\nand 20% CO2 gas mixture", "snapshot_sha256": "47a522dcda71f9f25bb9a362d5b3917b897198f5b3f106580f4b7dd165823974",
    "parsed_text_sha256": "4de2c8b21ac40e3418caed5d6e81f6bceaf2c6ae8ae0a1fb3e6e924108cd8d10"}],
    "explanation": "Keep this distinct stock gas mixture and do not silently apply
    it to the main-medium sparging stage. The DSMZ owner retains corresponding prose;
    the target and KOMODO owner omit it."}, {"field_path": "ph_range", "decision":
    "evidence_only", "current": {"min": 7.4, "max": 7.5}, "owner_decisions": {"data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml":
    "evidence_only", "data/normalized_yaml/bacterial/acidaminobacter_medium.yaml":
    "evidence_only"}, "source_stage": "main or exact named stock preparation as located",
    "source_snippets": [{"source_key": "dsmz292", "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf",
    "source_locator": "PDF page 1 final pH instruction", "exact_source_quote": "7.4
    - 7.5, if necessary.", "snapshot_sha256": "47a522dcda71f9f25bb9a362d5b3917b897198f5b3f106580f4b7dd165823974",
    "parsed_text_sha256": "4de2c8b21ac40e3418caed5d6e81f6bceaf2c6ae8ae0a1fb3e6e924108cd8d10"}],
    "explanation": "The final range is already stored in all layers; attach source
    evidence and retain the conditional adjustment wording."}, {"field_path": "preparation_steps
    (SL-10 final make-up)", "decision": "add", "current": null, "owner_decisions":
    {"data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml": "add",
    "data/normalized_yaml/bacterial/acidaminobacter_medium.yaml": "correct"}, "source_stage":
    "main or exact named stock preparation as located", "source_snippets": [{"source_key":
    "dsmz292", "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium292.pdf",
    "source_locator": "PDF page 1 SL-10 preparation paragraph", "exact_source_quote":
    "Finally\nmake up to 1000.00 ml.", "snapshot_sha256": "47a522dcda71f9f25bb9a362d5b3917b897198f5b3f106580f4b7dd165823974",
    "parsed_text_sha256": "4de2c8b21ac40e3418caed5d6e81f6bceaf2c6ae8ae0a1fb3e6e924108cd8d10"}],
    "explanation": "Explicit final volume belongs to SL-10, not the receiving medium
    or other stocks. Relocate the DSMZ owner root step to stock scope while preserving
    its sequence. The DSMZ owner retains corresponding prose; the target and KOMODO
    owner omit it."}]'
- assessment_id: forms
  area: grounding
  topic: Exact supplied chemical forms
  outcome: concern
  summary: Nickel chloride hexahydrate is linked in both primary and secondary slots
    to anhydrous nickel dichloride CHEBI:34887. Sodium resazurin is linked to neutral
    CHEBI:8806. Other explicitly named hydrates match the captured formulas. D-pantothenate
    is source-explicit and consistent with CHEBI:31345 D synonyms/structure; DL-lipoic
    acid retains its source label without an invented stereospecific ID.
  target_ids:
  - CultureMech:004754
  evidence_ids:
  - primary
  - provider
  - chebi34887
  - chebi8806
  - chebi31345
  - chebi16494
- assessment_id: preparation
  area: completeness
  topic: Preparation stages, sterilization and conflicting aerobic metadata
  outcome: concern
  summary: The DSMZ owner preserves the main anoxic preparation and an SL-10 paragraph,
    but places both at root; the target and KOMODO owner omit them. Preserve initial/final
    pH, gas/duration and distinct stock gas contexts, vitamin filtration, delayed
    additions and SL-10 dissolution sequence. The exact DSMZ source does not specify
    an autoclave temperature/time; none is supplied here. Catalogue aerobic metadata
    conflicts with this preparation scope without a demonstrated source chronology.
  target_ids:
  - CultureMech:004754
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - provider
  - catalog
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Medium classification, physical state and organism assertions
  outcome: supported
  summary: COMPLEX/SEMI_DEFINED is consistent with named salts, glycine and undefined
    yeast extract; LIQUID is compatible with the supplied formulation. The bacterial
    category is catalogue organization, not a strain-specific growth assertion. No
    target_organisms, taxonomy ID, temperature or growth evidence is invented from
    the title; the aerobic note is separately disputed.
  target_ids:
  - CultureMech:004754
  evidence_ids:
  - record
  - primary
  - provider
- assessment_id: evidence-placement
  area: evidence
  topic: Quantity evidence and citation placement
  outcome: concern
  summary: Source URLs in notes do not support all ingredient claims. Each retained
    main amount and restored stock constituent needs evidence on the appropriate ingredient
    descriptor; stock doses require root evidence with exact solution paths, and root
    references need collection/provider metadata. No SolutionDescriptor evidence slot
    is invented.
  target_ids:
  - CultureMech:004754
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - provider
  - quantity-inventory
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 28 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:004754
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
findings:
- finding_id: f1
  issue_key: dsmz292-stock-stage-and-basis
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock concentrations are asserted as direct medium composition
  description: All three local layers list 22 constituents of SL-10, selenite-tungstate
    and 10x vitamins as direct medium concentrations while losing the three stock
    doses and four solvent contexts. This changes the represented formulation. HCl
    2.5 G_PER_L also assumes an unsupported conversion from a bare 25% liquid stock.
    Eleven main g_l transcriptions match the provider but lack local scoped evidence.
  target_ids:
  - CultureMech:004754
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidaminobacter_medium.yaml
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
  issue_key: dsmz292-supplied-form-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two asserted chemical identities do not preserve the supplied form
  description: Source nickel chloride hexahydrate maps to an anhydrous structure in
    both CHEBI slots; sodium resazurin maps to the neutral compound. Existing live
    canonical IDs and pinned MIM rows do not validate those correspondences.
  target_ids:
  - CultureMech:004754
  field_paths:
  - ingredients[8].term
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  evidence_ids:
  - primary
  - provider
  - chebi8806
  - chebi34887
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidaminobacter_medium.yaml
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
  issue_key: dsmz292-preparation-oxygen-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation is missing or assigned to the wrong stage
  description: 'Target and KOMODO owner omit the exact source preparation. DSMZ owner
    retains an SL-10 step at medium root. The inherited Aerobic: Yes catalogue note
    conflicts with the explicitly anoxic main preparation. Lost stage distinctions
    materially alter interpretation despite an already present final pH range.'
  target_ids:
  - CultureMech:004754
  field_paths:
  - preparation_steps
  - notes
  - ph_range
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - provider
  - catalog
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidaminobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3
  normalization_reason: P3.4 is normally minor; major is justified because the omitted
    anoxic stages and incorrect placement of a stock-specific step, together with
    the conflicting aerobic note, materially change this formulation rather than merely
    omitting optional prose.
- finding_id: f4
  issue_key: dsmz292-history-timestamp-shape
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Import history contains malformed and timezone-naive timestamps
  description: Target and KOMODO owner each preserve one literal .fZ timestamp and
    one timezone-naive enrichment timestamp. The DSMZ owner timestamps are timezone-aware.
    This limits auditability; it does not negate the independently captured formulation
    evidence.
  target_ids:
  - CultureMech:004754
  field_paths:
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidaminobacter_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Restore exact stock structures, original units and source-scoped addition/batch
    evidence in both maintained owners, retaining unqualified HCl percent basis as
    unresolved. Preserve main provider quantities only with their declared basis;
    do not double-count stock constituents or infer measured final volume. Regenerate
    only after owner verification.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:004754
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidaminobacter_medium.yaml
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
  description: Resolve exact source-form groundings in both owners, preserving salt/hydrate
    notation and existing quantity evidence scope. Verify replacement identity independently
    or leave the unsupported assertion unassigned; do not infer new IDs or perform
    hydrate-based mass conversions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:004754
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidaminobacter_medium.yaml
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
  description: Recover and cite the source preparation in both owners with main/stock
    scope, conditional final pH and sterilization method. Preserve the conflicting
    aerobic catalogue assertion with explicit source scope pending resolution; do
    not assert a new chronology or invent a cycle. Place the SL-10 dissolution/final-volume
    paragraph under that stock.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:004754
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidaminobacter_medium.yaml
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
  description: Keep historical events append-only. Add a documented clarification
    if a later curation is authorized, and correct current writer timestamp generation
    before future imports without guessing the missing historical timezone.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:004754
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidaminobacter_medium.yaml
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
- 'No required source identity/formulation check is unavailable: the exact primary
  includes all three stocks. The optional KOMODO detail 403 is explicitly retained.'
- Source water amounts and provider volumes are separately reported; this review does
  not validate a physical final volume or infer HCl percent basis/density.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-016
- generated-medium
```
