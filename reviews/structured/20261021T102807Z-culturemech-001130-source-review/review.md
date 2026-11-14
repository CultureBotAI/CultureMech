# Source and formulation review: acetobacteroides_medium (CultureMech:001130)

- Review: 20261021T102807Z-culturemech-001130-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T10:23:10Z
- Finished UTC: 2026-10-21T10:28:07Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 1647 is correctly identified, but the local formulation collapses three separately dosed stocks into main-medium concentrations, adds calcium across incompatible stages, and retains a provider trace composition that differs from the primary modified stock. The ammonium-chloride mass conversion lacks source support; nickel hydrate grounding and stock preparation/evidence need curation.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 152; batch 016 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding fifteen task batches contain 150 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 152 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001130 | data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml | generated | acetobacteroides_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001130 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001130 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-016/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch016/152/strict.tsv |
| validate-terms | passed | True | CultureMech:001130 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001130 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001130 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001130.

The four documented recipes completed; interpret the scope of each separately.

### Exact primary labels and current secondary linkage coverage

grounding: supported. Targets: CultureMech:001130.

33 unique asserted CHEBI identifiers resolve with exact labels. Primary linkage 33/34 (97.06%); verified current secondary linkage 33/34 (97.06%). This is a 0–100 ingredient-instance linkage scale, not scientific correctness. Missing current secondary keys: []. Legacy links and chemical-form correctness are assessed separately.

### Full history and timezone audit

provenance: supported. Targets: CultureMech:001130.

History event counts: [('target', 9), ('data/normalized_yaml/bacterial/acetobacteroides_medium.yaml', 8)]. Explicit timestamp defects: []. Historical bytes are assessed as observed; no inferred timezone or retroactive replacement timestamp is supplied.

### Every direct, stock, stock-addition and preparation quantity

quantity: concern. Targets: CultureMech:001130.

All 42 provider recipe rows are reconciled against the primary main and three stock tables, including three explicit trace-composition conflicts; five further decisions cover existing and missing scoped preparation. Every value is attributed to its own stage and source. No unsupported claim is marked verified.

[{"field_path": "ingredients[0].concentration", "decision": "evidence_only", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Yeast extract 0.20 g", "source_locator": "DSMZ 1647; Main sol. 1647; exact Yeast extract entry", "explanation": "The stored value matches provider g/L under its declared 1000 ml normalization. Preserve the primary batch amount and unit, attach narrow evidence and qualify the volume basis; there is no existing claim-level evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine specificity is explicit there but not in the primary unspecific cysteine wording.", "owner_decision": "evidence_only", "local_value": {"value": "0.2", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[0].recipe[0] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"optional\": 0\n                    }", "source_amount": 0.2, "source_unit": "g", "provider_g_l": 0.2, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[1].concentration", "decision": "evidence_only", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Glucose 0.18 g", "source_locator": "DSMZ 1647; Main sol. 1647; exact Glucose entry", "explanation": "The stored value matches provider g/L under its declared 1000 ml normalization. Preserve the primary batch amount and unit, attach narrow evidence and qualify the volume basis; there is no existing claim-level evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine specificity is explicit there but not in the primary unspecific cysteine wording.", "owner_decision": "evidence_only", "local_value": {"value": "0.18", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[0].recipe[1] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.999112,\n                        \"optional\": 0\n                    }", "source_amount": 0.18, "source_unit": "g", "provider_g_l": 0.18, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[2].concentration", "decision": "evidence_only", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "KH\n2PO4 0.14 g", "source_locator": "DSMZ 1647; Main sol. 1647; exact KH2PO4 entry", "explanation": "The stored value matches provider g/L under its declared 1000 ml normalization. Preserve the primary batch amount and unit, attach narrow evidence and qualify the volume basis; there is no existing claim-level evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine specificity is explicit there but not in the primary unspecific cysteine wording.", "owner_decision": "evidence_only", "local_value": {"value": "0.14", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[0].recipe[2] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.14,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.14,\n                        \"mmol_l\": 1.02877,\n                        \"optional\": 0\n                    }", "source_amount": 0.14, "source_unit": "g", "provider_g_l": 0.14, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[3].concentration", "decision": "evidence_only", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "MgCl2 x 6 H2O 0.20 g", "source_locator": "DSMZ 1647; Main sol. 1647; exact MgCl2 x 6 H2O entry", "explanation": "The stored value matches provider g/L under its declared 1000 ml normalization. Preserve the primary batch amount and unit, attach narrow evidence and qualify the volume basis; there is no existing claim-level evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine specificity is explicit there but not in the primary unspecific cysteine wording.", "owner_decision": "evidence_only", "local_value": {"value": "0.2", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[0].recipe[3] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.983753,\n                        \"optional\": 0\n                    }", "source_amount": 0.2, "source_unit": "g", "provider_g_l": 0.2, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[4].concentration", "decision": "correct", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "CaCl2 x 2 H2O 0.15 g", "source_locator": "DSMZ 1647; Main sol. 1647; exact CaCl2 x 2 H2O entry", "explanation": "The local 0.25 g/L is the numerical sum of 0.15 g in the main batch and 0.10 g in a separate litre of trace stock. Restore the separate stages. The stock dose of 1 ml transfers 0.0001 g calcium chloride dihydrate; 0.1501 g is a conditional combined batch mass, not a verified final-volume concentration.", "owner_decision": "correct", "local_value": {"value": "0.25", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[0].recipe[4] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.15,\n                        \"mmol_l\": 1.0203,\n                        \"optional\": 0\n                    }", "source_amount": 0.15, "source_unit": "g", "provider_g_l": 0.15, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[5].concentration", "decision": "unsupported", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "NH4Cl 0.54 ml", "source_locator": "DSMZ 1647; Main sol. 1647; exact NH4Cl entry", "explanation": "Both primary image and provider amount state 0.54 ml, but no strength or density supports provider g_l=0.824796. Preserve the literal source unit and unresolved mass conversion; do not silently replace ml with g.", "owner_decision": "unsupported", "local_value": {"value": "0.824796", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[0].recipe[5] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.54,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.824796,\n                        \"mmol_l\": 15.4196,\n                        \"optional\": 0\n                    }", "source_amount": 0.54, "source_unit": "ml", "provider_g_l": 0.824796, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[6].concentration", "decision": "evidence_only", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Cysteine-HCl x H2O 0.30 g", "source_locator": "DSMZ 1647; Main sol. 1647; exact L-Cysteine HCl x H2O entry", "explanation": "The stored value matches provider g/L under its declared 1000 ml normalization. Preserve the primary batch amount and unit, attach narrow evidence and qualify the volume basis; there is no existing claim-level evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine specificity is explicit there but not in the primary unspecific cysteine wording.", "owner_decision": "evidence_only", "local_value": {"value": "0.3", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[0].recipe[6] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.70808,\n                        \"optional\": 0\n                    }", "source_amount": 0.3, "source_unit": "g", "provider_g_l": 0.3, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[7].concentration", "decision": "evidence_only", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "NaHCO3 2.50 g", "source_locator": "DSMZ 1647; Main sol. 1647; exact NaHCO3 entry", "explanation": "The stored value matches provider g/L under its declared 1000 ml normalization. Preserve the primary batch amount and unit, attach narrow evidence and qualify the volume basis; there is no existing claim-level evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine specificity is explicit there but not in the primary unspecific cysteine wording.", "owner_decision": "evidence_only", "local_value": {"value": "2.5", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[0].recipe[7] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 29.7594,\n                        \"optional\": 0\n                    }", "source_amount": 2.5, "source_unit": "g", "provider_g_l": 2.5, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[8].concentration", "decision": "evidence_only", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Na2S x 9 H2O 0.30 g", "source_locator": "DSMZ 1647; Main sol. 1647; exact Na2S x 9 H2O entry", "explanation": "The stored value matches provider g/L under its declared 1000 ml normalization. Preserve the primary batch amount and unit, attach narrow evidence and qualify the volume basis; there is no existing claim-level evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine specificity is explicit there but not in the primary unspecific cysteine wording.", "owner_decision": "evidence_only", "local_value": {"value": "0.3", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[0].recipe[8] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.24905,\n                        \"optional\": 0\n                    }", "source_amount": 0.3, "source_unit": "g", "provider_g_l": 0.3, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[9].concentration", "decision": "evidence_only", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Resazurin 1.00 mg", "source_locator": "DSMZ 1647; Main sol. 1647; exact Resazurin entry", "explanation": "The stored value matches provider g/L under its declared 1000 ml normalization. Preserve the primary batch amount and unit, attach narrow evidence and qualify the volume basis; there is no existing claim-level evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine specificity is explicit there but not in the primary unspecific cysteine wording.", "owner_decision": "evidence_only", "local_value": {"value": "0.001", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[0].recipe[9] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00436319,\n                        \"optional\": 0\n                    }", "source_amount": 1, "source_unit": "mg", "provider_g_l": 0.001, "provider_declared_volume_ml": 1000}, {"field_path": "solutions (missing additions)", "decision": "add", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Vitamin solution (see below) 1 ml", "source_locator": "DSMZ 1647; Main sol. 1647; exact Vitamin solution entry", "explanation": "The exact 1 ml stock addition is absent as a structured solution. Preserve this dose and the corresponding stock recipe separately; a stock concentration is not a final-medium concentration.", "owner_decision": "add", "local_value": null, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[0].recipe[10] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\": 11,\n                        \"solution\": \"Vitamin solution\",\n                        \"solution_id\": 5769,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_amount": 1, "source_unit": "ml", "provider_g_l": null, "provider_declared_volume_ml": 1000}, {"field_path": "solutions (missing additions)", "decision": "add", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Trace element solution (see below) 1.00 ml", "source_locator": "DSMZ 1647; Main sol. 1647; exact Trace element solution entry", "explanation": "The exact 1 ml stock addition is absent as a structured solution. Preserve this dose and the corresponding stock recipe separately; a stock concentration is not a final-medium concentration.", "owner_decision": "add", "local_value": null, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[0].recipe[11] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 5770,\n                        \"attribute\": \"\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_amount": 1, "source_unit": "ml", "provider_g_l": null, "provider_declared_volume_ml": 1000}, {"field_path": "solutions (missing additions)", "decision": "add", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Se/W solution (see below) 1.00 ml", "source_locator": "DSMZ 1647; Main sol. 1647; exact Se/W solution entry", "explanation": "The exact 1 ml stock addition is absent as a structured solution. Preserve this dose and the corresponding stock recipe separately; a stock concentration is not a final-medium concentration.", "owner_decision": "add", "local_value": null, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[0].recipe[12] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Se/W solution\",\n                        \"solution_id\": 3409,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_amount": 1, "source_unit": "ml", "provider_g_l": null, "provider_declared_volume_ml": 1000}, {"field_path": "preparation_steps (missing scoped solvent)", "decision": "add", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Distilled water 1000.00 ml", "source_locator": "DSMZ 1647; Main sol. 1647; exact Distilled water entry", "explanation": "Preserve 1000 ml main water as solvent/batch context. Provider volume is declared as 1000 ml, but source water plus additions is not an independently measured final volume.", "owner_decision": "add", "local_value": null, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[0].recipe[13] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_amount": 1000, "source_unit": "ml", "provider_g_l": null, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[10].concentration", "decision": "correct", "stage": "Se/W solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Na\n2SeO3 4.0 mg", "source_locator": "DSMZ 1647; Se/W solution; exact Na2SeO3 entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.004", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[1].recipe[0] (solution_id 3409)", "provider_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2SeO3\",\n                        \"compound_id\": 699,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0231297,\n                        \"optional\": 0\n                    }", "source_amount": 4, "source_unit": "mg", "provider_g_l": 0.004, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[11].concentration", "decision": "correct", "stage": "Se/W solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Na2WO4 4.0 mg", "source_locator": "DSMZ 1647; Se/W solution; exact Na2WO4 entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.004", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[1].recipe[1] (solution_id 3409)", "provider_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2WO4\",\n                        \"compound_id\": 550,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0136138,\n                        \"optional\": 0\n                    }", "source_amount": 4, "source_unit": "mg", "provider_g_l": 0.004, "provider_declared_volume_ml": 1000}, {"field_path": "preparation_steps (missing scoped solvent)", "decision": "add", "stage": "Se/W solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Distilled water 1000.00 ml", "source_locator": "DSMZ 1647; Se/W solution; exact Distilled water entry", "explanation": "Retain the separate stock solvent quantity of 1000 ml. This is not another direct main-medium water addition.", "owner_decision": "add", "local_value": null, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[1].recipe[2] (solution_id 3409)", "provider_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_amount": 1000, "source_unit": "ml", "provider_g_l": null, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[12].concentration", "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Biotin 2.00 mg", "source_locator": "DSMZ 1647; Vitamin solution; exact Biotin entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.002", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[2].recipe[0] (solution_id 5769)", "provider_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00818632,\n                        \"optional\": 0\n                    }", "source_amount": 2, "source_unit": "mg", "provider_g_l": 0.002, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[13].concentration", "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Folic acid 2.00 mg", "source_locator": "DSMZ 1647; Vitamin solution; exact Folic acid entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.002", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[2].recipe[1] (solution_id 5769)", "provider_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00453104,\n                        \"optional\": 0\n                    }", "source_amount": 2, "source_unit": "mg", "provider_g_l": 0.002, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[14].concentration", "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Pyridoxine-HCl 10.00 mg", "source_locator": "DSMZ 1647; Vitamin solution; exact Pyridoxine hydrochloride entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.01", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[2].recipe[2] (solution_id 5769)", "provider_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0486287,\n                        \"optional\": 0\n                    }", "source_amount": 10, "source_unit": "mg", "provider_g_l": 0.01, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[15].concentration", "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Thiamine-HCl x 2 H2O 5.00 mg", "source_locator": "DSMZ 1647; Vitamin solution; exact Thiamine-HCl x 2 H2O entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.005", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[2].recipe[3] (solution_id 5769)", "provider_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.013394,\n                        \"optional\": 0\n                    }", "source_amount": 5, "source_unit": "mg", "provider_g_l": 0.005, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[16].concentration", "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Riboflavin 5.00 mg", "source_locator": "DSMZ 1647; Vitamin solution; exact Riboflavin entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.005", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[2].recipe[4] (solution_id 5769)", "provider_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0132837,\n                        \"optional\": 0\n                    }", "source_amount": 5, "source_unit": "mg", "provider_g_l": 0.005, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[17].concentration", "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Nicotinic acid 5.00 mg", "source_locator": "DSMZ 1647; Vitamin solution; exact Nicotinic acid entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.005", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[2].recipe[5] (solution_id 5769)", "provider_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0406141,\n                        \"optional\": 0\n                    }", "source_amount": 5, "source_unit": "mg", "provider_g_l": 0.005, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[18].concentration", "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "D-Ca-pantothenate 5.00 mg", "source_locator": "DSMZ 1647; Vitamin solution; exact D-Calcium pantothenate entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.005", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[2].recipe[6] (solution_id 5769)", "provider_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"D-Calcium pantothenate\",\n                        \"compound_id\": 1807,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"optional\": 0\n                    }", "source_amount": 5, "source_unit": "mg", "provider_g_l": 0.005, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[19].concentration", "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Vitamin B\n12 0.10 mg", "source_locator": "DSMZ 1647; Vitamin solution; exact Vitamin B12 entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.0001", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[2].recipe[7] (solution_id 5769)", "provider_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\": 7.3779e-5,\n                        \"optional\": 0\n                    }", "source_amount": 0.1, "source_unit": "mg", "provider_g_l": 0.0001, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[20].concentration", "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "p-Aminobenzoic acid 5.00 mg", "source_locator": "DSMZ 1647; Vitamin solution; exact p-Aminobenzoic acid entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.005", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[2].recipe[8] (solution_id 5769)", "provider_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0364591,\n                        \"optional\": 0\n                    }", "source_amount": 5, "source_unit": "mg", "provider_g_l": 0.005, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[21].concentration", "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Lipoic acid 5.00 mg", "source_locator": "DSMZ 1647; Vitamin solution; exact Lipoic acid entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.005", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[2].recipe[9] (solution_id 5769)", "provider_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Lipoic acid\",\n                        \"compound_id\": 368,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.024233,\n                        \"optional\": 0\n                    }", "source_amount": 5, "source_unit": "mg", "provider_g_l": 0.005, "provider_declared_volume_ml": 1000}, {"field_path": "preparation_steps (missing scoped solvent)", "decision": "add", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Distilled water 1000.00 ml", "source_locator": "DSMZ 1647; Vitamin solution; exact Distilled water entry", "explanation": "Retain the separate stock solvent quantity of 1000 ml. This is not another direct main-medium water addition.", "owner_decision": "add", "local_value": null, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[2].recipe[10] (solution_id 5769)", "provider_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_amount": 1000, "source_unit": "ml", "provider_g_l": null, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[22].concentration", "decision": "correct", "stage": "Trace element solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Nitrilotriacetic acid (NTA) 12.80 g", "source_locator": "DSMZ 1647; modified Trace element solution; exact Nitrilotriacetic acid entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "12.8", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[3].recipe[0] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"attribute\": \"NTA\",\n                        \"amount\": 12.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 12.8,\n                        \"mmol_l\": 66.9666,\n                        \"optional\": 0\n                    }", "source_amount": 12.8, "source_unit": "g", "provider_g_l": 12.8, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[23].concentration", "decision": "correct", "stage": "Trace element solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "FeCl\n2 x 4 H2O 1.00 g", "source_locator": "DSMZ 1647; modified Trace element solution; exact FeCl2 x 4 H2O entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "1", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[3].recipe[1] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.02988,\n                        \"optional\": 0\n                    }", "source_amount": 1, "source_unit": "g", "provider_g_l": 1, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[24].concentration", "decision": "correct", "stage": "Trace element solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "MnCl2 x 4 H2O 0.10 g", "source_locator": "DSMZ 1647; modified Trace element solution; exact MnCl2 x 4 H2O entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.1", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[3].recipe[2] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "source_amount": 0.1, "source_unit": "g", "provider_g_l": 0.1, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[25].concentration", "decision": "correct", "stage": "Trace element solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "CoCl2 x 6 H2O 0.03 g", "source_locator": "DSMZ 1647; modified Trace element solution; exact CoCl2 x 6 H2O entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.03", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[3].recipe[3] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.231055,\n                        \"optional\": 0\n                    }", "source_amount": 0.03, "source_unit": "g", "provider_g_l": 0.03, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[4].concentration", "decision": "correct", "stage": "Trace element solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "CaCl2 x 2 H2O 0.10 g", "source_locator": "DSMZ 1647; modified Trace element solution; exact CaCl2 x 2 H2O entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.25", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[3].recipe[4] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }", "source_amount": 0.1, "source_unit": "g", "provider_g_l": 0.1, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[26].concentration", "decision": "correct", "stage": "Trace element solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "ZnCl2 0.10 g", "source_locator": "DSMZ 1647; modified Trace element solution; exact ZnCl2 entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.1", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[3].recipe[5] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.733676,\n                        \"optional\": 0\n                    }", "source_amount": 0.1, "source_unit": "g", "provider_g_l": 0.1, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[27].concentration", "decision": "correct", "stage": "Trace element solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "CuCl2 0.02 g", "source_locator": "DSMZ 1647; modified Trace element solution; exact CuCl2 entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.02", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[3].recipe[6] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2\",\n                        \"compound_id\": 261,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.148754,\n                        \"optional\": 0\n                    }", "source_amount": 0.02, "source_unit": "g", "provider_g_l": 0.02, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[28].concentration", "decision": "correct", "stage": "Trace element solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "H3BO3 0.01 g", "source_locator": "DSMZ 1647; modified Trace element solution; exact H3BO3 entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.01", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[3].recipe[7] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }", "source_amount": 0.01, "source_unit": "g", "provider_g_l": 0.01, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[29].concentration", "decision": "correct", "stage": "Trace element solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Na2MoO4 x 2 H2O 0.03 g", "source_locator": "DSMZ 1647; modified Trace element solution; exact Na2MoO4 x 2 H2O entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.03", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[3].recipe[8] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.123993,\n                        \"optional\": 0\n                    }", "source_amount": 0.03, "source_unit": "g", "provider_g_l": 0.03, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[30].concentration", "decision": "correct", "stage": "Trace element solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "NiCl2 x 6 H2O 0.10 g", "source_locator": "DSMZ 1647; modified Trace element solution; exact NiCl2 x 6 H2O entry", "explanation": "This amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L is stock strength incorrectly placed among direct medium ingredients. Amount times 1/1000 is the transferred mass; division by actual final medium volume requires a supported volume basis. Preserve exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value": {"value": "0.1", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[3].recipe[9] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.771611,\n                        \"optional\": 0\n                    }", "source_amount": 0.1, "source_unit": "g", "provider_g_l": 0.1, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[31].concentration", "decision": "conflict", "stage": "Trace element solution", "source_reference": "https://mediadive.dsmz.de/rest/medium/1647", "source_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[10] (solution_id 5770)", "explanation": "This provider trace-stock salt and amount occur in current DSMZ 318, but are absent from the complete modified trace table in DSMZ 1647. The reference to 318 is explicitly for preparation. Preserve the source-version conflict and do not silently promote this extra stock constituent into the 1647 main recipe.", "owner_decision": "conflict", "local_value": {"value": "1", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[3].recipe[10] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }", "source_amount": 1, "source_unit": "g", "provider_g_l": 1, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[32].concentration", "decision": "conflict", "stage": "Trace element solution", "source_reference": "https://mediadive.dsmz.de/rest/medium/1647", "source_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.114062,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[11] (solution_id 5770)", "explanation": "This provider trace-stock salt and amount occur in current DSMZ 318, but are absent from the complete modified trace table in DSMZ 1647. The reference to 318 is explicitly for preparation. Preserve the source-version conflict and do not silently promote this extra stock constituent into the 1647 main recipe.", "owner_decision": "conflict", "local_value": {"value": "0.03", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[3].recipe[11] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.114062,\n                        \"optional\": 0\n                    }", "source_amount": 0.03, "source_unit": "g", "provider_g_l": 0.03, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[33].concentration", "decision": "conflict", "stage": "Trace element solution", "source_reference": "https://mediadive.dsmz.de/rest/medium/1647", "source_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.04,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.04,\n                        \"mmol_l\": 0.121267,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[12] (solution_id 5770)", "explanation": "This provider trace-stock salt and amount occur in current DSMZ 318, but are absent from the complete modified trace table in DSMZ 1647. The reference to 318 is explicitly for preparation. Preserve the source-version conflict and do not silently promote this extra stock constituent into the 1647 main recipe.", "owner_decision": "conflict", "local_value": {"value": "0.04", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[3].recipe[12] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.04,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.04,\n                        \"mmol_l\": 0.121267,\n                        \"optional\": 0\n                    }", "source_amount": 0.04, "source_unit": "g", "provider_g_l": 0.04, "provider_declared_volume_ml": 1000}, {"field_path": "preparation_steps (missing scoped solvent)", "decision": "add", "stage": "Trace element solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "Distilled water 1000.00 ml", "source_locator": "DSMZ 1647; modified Trace element solution; exact Distilled water entry", "explanation": "Retain the separate stock solvent quantity of 1000 ml. This is not another direct main-medium water addition.", "owner_decision": "add", "local_value": null, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator": "$.data.solutions[3].recipe[13] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_amount": 1000, "source_unit": "ml", "provider_g_l": null, "provider_declared_volume_ml": 1000}, {"field_path": "preparation_steps[0]", "decision": "evidence_only", "stage": "main sterilization and subsequent additions", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote": "NaHCO3 are added after the medium has been autoclaved.", "source_locator": "Named preparation sentence at the stated stage", "explanation": "The complete preceding sentence names vitamins, trace, Se/W, cysteine, glucose, sulfide and bicarbonate. The sequence is retained, but claim evidence is absent; no autoclave temperature or duration is specified.", "owner_decision": "evidence_only"}, {"field_path": "preparation_steps[2]", "decision": "correct", "stage": "trace stock initial dissolution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318.pdf", "source_sha256": "8ca3cb45479ba00e11f9574bf3b315e365e9c98c92bbc5323d4cd5dc4b862f29", "source_quote": "First dissolve NTA in 200 ml of distilled water and adjust pH to 6.5 with KOH, then dissolve", "source_locator": "Named preparation sentence at the stated stage", "explanation": "The 200 ml and initial pH 6.5 belong exclusively to trace-stock preparation, not the main medium. Retain the existing literal values while restoring their stock scope.", "owner_decision": "correct"}, {"field_path": "preparation_steps[2]", "decision": "correct", "stage": "trace stock final make-up", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318.pdf", "source_sha256": "8ca3cb45479ba00e11f9574bf3b315e365e9c98c92bbc5323d4cd5dc4b862f29", "source_quote": "mineral salts. Finally adjust pH to 6.5 with KOH and make up to 1000.00 ml.", "source_locator": "Named preparation sentence at the stated stage", "explanation": "Final stock pH 6.5 and 1000 ml volume are retained but flattened into main preparation. They do not establish main-medium pH.", "owner_decision": "correct"}, {"field_path": "solutions (trace KOH adjustment)", "decision": "not_quantified", "stage": "trace stock titration", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318.pdf", "source_sha256": "8ca3cb45479ba00e11f9574bf3b315e365e9c98c92bbc5323d4cd5dc4b862f29", "source_quote": "adjust pH to 6.5 with KOH", "source_locator": "Named preparation sentence at the stated stage", "explanation": "Neither KOH amount nor stock strength is specified; do not invent either.", "owner_decision": "not_quantified"}, {"field_path": "solutions (vitamin preparation)", "decision": "add", "stage": "vitamin stock only", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf", "source_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8", "source_quote": "Vitamins are prepared under 100% N2 gas\natmosphere and sterilized by filtration.", "source_locator": "Named preparation sentence at the stated stage", "explanation": "Resolve the explicit preparation cross-reference with its named vitamin instruction: 100% nitrogen and filtration. Do not import 141 basal gases, pH, pressure, or different vitamin composition.", "owner_decision": "add"}]

### Exact source and one maintained owner

identity: supported. Targets: CultureMech:001130.

CultureMech:001130 and media_term mediadive.medium:1647 resolve to the exact primary and provider title. The single normalized contributor has the same ingredients/preparation as the target; generated provenance adds the August merge event. No KG match, internal solution ID, paper citation or asserted organism-growth claim occurs in the complete target.

### Main recipe, stocks and conflicts

consistency: concern. Targets: CultureMech:001130.

Local 34 direct ingredients replace 10 main solutes and three separately dosed stocks. The primary trace table has ten solutes, while provider stock 5770 adds NaCl, sodium selenite pentahydrate and sodium tungstate dihydrate. Main calcium and trace calcium are wrongly summed. The exact source ammonium volume is unresolved as mass.

### Supplied hydrates and source specificity

grounding: concern. Targets: CultureMech:001130.

Nickel chloride hexahydrate is linked to CHEBI:34887, whose formula Cl2Ni lacks water. Other inspected asserted salt/hydrate forms match their source labels; the dihydrate thiamine term is positively supported by 1647, and D-calcium pantothenate is explicit. Neutral resazurin and the anhydrous Se/W salts are stated by the primary. The provider specifically says L-cysteine while the primary does not specify stereochemistry; retain that attribution without inventing a primary L claim.

### Source preparation scope

completeness: concern. Targets: CultureMech:001130.

Post-autoclave additions are retained. Trace 200 ml/pH 6.5/1000 ml instructions are present but unscoped. Vitamin preparation is only an unresolved textual reference, despite a named nitrogen/filtration instruction in the referenced source. Main pH, incubation temperature/time, autoclave settings and stock strengths not supplied by 1647 are not inferred.

### Mixture classification and biological scope

scope: supported. Targets: CultureMech:001130.

COMPLEX with SEMI_DEFINED composition is consistent with yeast extract plus specified salts/vitamins; LIQUID is consistent with the no-solidifier recipe. Microbial cultivation is a generic application, not strain-specific experimental evidence. No taxon, optimal condition or organism-growth assertion is inferred from the title or adjacent cross-referenced media.

### Evidence, history and maintained-input ownership

provenance: concern. Targets: CultureMech:001130.

All ingredient evidence is absent in both local layers, notwithstanding the resolvable source URL. All observed history timestamps are timezone-aware; the March duplicate-merge note supports the observed calcium sum but does not identify a replayed implementation. Maintain the normalized source and regenerate only after stage/source reconciliation.

## Findings

### f1: Three stock formulations are encoded as main-medium ingredients

blocker / open / confirmed; issue key: CM001130-stock-flattening.

All stock solutes are represented at their stock strengths among direct ingredients, with no three 1 ml additions. Calcium 0.25 g/L adds distinct 0.15 g main and 0.10 g stock stages. The representation denotes a different formulation.

### f2: Ammonium mass concentration lacks a valid conversion

major / open / confirmed; issue key: CM001130-ammonium-unit.

The visually confirmed primary and provider amount are 0.54 ml. Stored 0.824796 g/L copies provider g_l without a specified stock strength or density; 0.54 g is also unsupported.

### f3: Provider trace composition differs from the modified primary stock

major / open / confirmed; issue key: CM001130-trace-version.

The provider includes three additional salts absent from the complete modified 1647 trace table. A preparation-only cross-reference to current 318 does not establish composition equivalence.

### f4: Nickel hexahydrate is linked to anhydrous nickel dichloride

major / open / confirmed; issue key: CM001130-nickel-hydrate.

The supplied source material is NiCl2 x 6 H2O; CHEBI:34887 encodes Cl2Ni. Exact canonical labeling does not validate the hydrate.

### f5: Stock preparation stages are incomplete or flattened

major / open / confirmed; issue key: CM001130-stock-preparation.

Trace pH and solvent instructions appear in main preparation; vitamin preparation is a bare reference and omits the named stock nitrogen/filtration context.

### f6: Even source-consistent quantities lack attached claim evidence

minor / open / confirmed; issue key: CM001130-quantity-evidence.

The source link alone does not attach literal snippets, original units, stock stages or volume basis to individual local quantities. No quantity is currently verified under the native evidence definition.

## Recommended Actions And Acceptance Checks

### a1

Restore separate main/trace/vitamin/Se-W formulations and source doses; reconcile calcium by stage before any final-volume calculation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain the exact ml claim and unresolved conversion until exact source evidence supplies the missing basis; do not guess a mass.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the explicit primary/provider conflict and establish the intended exact formulation/version before retaining or removing the extra salts.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Resolve the stated hydrate using verified evidence, or explicitly leave the exact form unresolved; preserve any secondary linkage only if its pinned identity also matches.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Scope all stock instructions to their exact stock, resolve the vitamin preparation-only reference, and keep unrelated referenced basal recipes and variants excluded.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Attach exact claim-level source evidence while preserving source version, original units and unresolved conflicts; retain append-only history.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/acetobacteroides_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch016/152/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-016/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch016/152/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml:1:id: CultureMech:001130<br>./data/normalized_yaml/bacterial/acetobacteroides_medium.yaml:1:id: CultureMech:001130<br> |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:131361 resolves to disodium selenite pentahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["5H2O.2Na.O3Se"], "inchi_string": ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"], "mass": ["263.012"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]} |
| chebi132751 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:132751 resolves to thiamine hydrochloride dihydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C12H18N4OS.2Cl.2H2O"], "inchi_string": ["InChI=1S/C12H17N4OS.2ClH.2H2O/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H;2*1H2/q+1;;;;/p-1"], "mass": ["373.306"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c([NH3+])n1.O.O.[Cl-].[Cl-]"]} |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:15940 resolves to nicotinic acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C6H5NO2"], "inchi_string": ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"], "mass": ["123.111"], "smiles_string": ["O=C(O)c1cccnc1"]} |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:15956 resolves to biotin; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C10H16N2O3S"], "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"], "mass": ["244.316"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]} |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:16494 resolves to lipoic acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C8H14O2S2"], "inchi_string": ["InChI=1S/C8H14O2S2/c9-8(10)4-2-1-3-7-5-6-11-12-7/h7H,1-6H2,(H,9,10)"], "mass": ["206.332"], "smiles_string": ["O=C(O)CCCCC1CCSS1"]} |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:17015 resolves to riboflavin; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C17H20N4O6"], "inchi_string": ["InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23)14(25)12(24)6-22)15-13(18-9)16(26)20-17(27)19-15/h3-4,11-12,14,22-25H,5-6H2,1-2H3,(H,20,26,27)/t11-,12+,14-/m0/s1"], "mass": ["376.369"], "smiles_string": ["Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)CO)c2cc1C"]} |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:17234 resolves to glucose; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C6H12O6"], "mass": ["180.156"]} |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:176843 resolves to vitamin B12; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {} |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:26710 resolves to sodium chloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["Cl.Na"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "smiles_string": ["[Cl-].[Na+]"]} |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:27470 resolves to folic acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C19H19N7O6"], "inchi_string": ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"], "mass": ["441.404"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]} |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:30753 resolves to 4-aminobenzoic acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C7H7NO2"], "inchi_string": ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"], "mass": ["137.138"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]} |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:30961 resolves to pyridoxine hydrochloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C8H11NO3.HCl"], "inchi_string": ["InChI=1S/C8H11NO3.ClH/c1-5-8(12)7(4-11)6(3-10)2-9-5;/h2,10-12H,3-4H2,1H3;1H"], "mass": ["205.641"], "smiles_string": ["Cc1ncc(CO)c(CO)c1O.Cl"]} |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:31206 resolves to ammonium chloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["Cl.H4N"], "inchi_string": ["InChI=1S/ClH.H3N/h1H;1H3"], "mass": ["53.492"], "smiles_string": ["[Cl-].[H][N+]([H])([H])[H]"]} |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:31345 resolves to Calcium pantothenate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["2C9H16NO5.Ca"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"], "mass": ["476.536"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]} |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:32139 resolves to sodium hydrogencarbonate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["CHO3.Na"], "inchi_string": ["InChI=1S/CH2O3.Na/c2-1(3)4;/h(H2,2,3,4);/q;+1/p-1"], "mass": ["84.006"], "smiles_string": ["O=C([O-])O.[Na+]"]} |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:33118 resolves to boric acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["H3BO3"], "inchi_string": ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"], "mass": ["61.833"], "smiles_string": ["[H]OB(O[H])O[H]"]} |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:34887 resolves to nickel dichloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["Cl2Ni"], "inchi_string": ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"], "mass": ["129.599"], "smiles_string": ["[Cl][Ni][Cl]"]} |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:44557 resolves to nitrilotriacetic acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C6H9NO6"], "inchi_string": ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"], "mass": ["191.139"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]} |
| chebi48843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_48843; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:48843 resolves to disodium selenite; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["2Na.O3Se"], "inchi_string": ["InChI=1S/2Na.H2O3Se/c;;1-4(2)3/h;;(H2,1,2,3)/q2*+1;/p-2"], "mass": ["172.937"], "smiles_string": ["O=[Se]([O-])[O-].[Na+].[Na+]"]} |
| chebi49553 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49553; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:49553 resolves to copper(II) chloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["Cl2Cu"], "inchi_string": ["InChI=1S/2ClH.Cu/h2*1H;/q;;+2/p-2"], "mass": ["134.452"], "smiles_string": ["[Cl][Cu][Cl]"]} |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:49976 resolves to zinc dichloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["2Cl.Zn"], "inchi_string": ["InChI=1S/2ClH.Zn/h2*1H;/q;;+2/p-2"], "mass": ["136.296"], "smiles_string": ["[Cl-].[Cl-].[Zn+2]"]} |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["2Cl.Co.6H2O"], "inchi_string": ["InChI=1S/2ClH.Co.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass": ["237.929"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Co+2]"]} |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["H2O4P.K"], "inchi_string": ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"], "smiles_string": ["O=P([O-])(O)O.[K+]"]} |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:63939 resolves to sodium tungstate dihydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["2H2O.2Na.O4W"], "inchi_string": ["InChI=1S/2Na.2H2O.4O.W/h;;2*1H2;;;;;/q2*+1;;;;;2*-1;"], "mass": ["329.846"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]} |
| chebi63940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63940; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:63940 resolves to sodium tungstate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["2Na.O4W"], "inchi_string": ["InChI=1S/2Na.4O.W/q2*+1;;;2*-1;"], "mass": ["293.816"], "smiles_string": ["[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]} |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:75213 resolves to sodium molybdate dihydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["2H2O.MoO4.2Na"], "inchi_string": ["InChI=1S/Mo.2Na.2H2O.4O/h;;;2*1H2;;;;/q;2*+1;;;;;2*-1"], "mass": ["241.946"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]} |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["9H2O.2Na.S"], "inchi_string": ["InChI=1S/2Na.9H2O.S/h;;9*1H2;/q2*+1;;;;;;;;;;-2"], "mass": ["240.182"], "smiles_string": ["O.O.O.O.O.O.O.O.O.[Na+].[Na+].[S-2]"]} |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:86158 resolves to calcium chloride dihydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["Ca.2Cl.2H2O"], "inchi_string": ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]} |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["Cl2Fe.4H2O"], "inchi_string": ["InChI=1S/2ClH.Fe.4H2O/h2*1H;;4*1H2/q;;+2;;;;/p-2"], "mass": ["198.811"], "smiles_string": ["O.O.O.O.[Cl][Fe][Cl]"]} |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["2Cl.6H2O.Mg"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass": ["203.301"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]} |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["Cl2Mn.4H2O"], "inchi_string": ["InChI=1S/2ClH.Mn.4H2O/h2*1H;;4*1H2/q;;+2;;;;/p-2"], "mass": ["197.904"], "smiles_string": ["O.O.O.O.[Cl][Mn][Cl]"]} |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:8806 resolves to Resazurin; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C12H7NO4"], "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"], "mass": ["229.191"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]} |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"], "mass": ["175.637"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]} |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned CSV; preferred-term MAPPED rows for every asserted secondary CHEBI key | supports | {"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:48843": [{"label": "Na2SeO3", "match_type": "preferred_term", "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63940": [{"label": "Na2WO4", "match_type": "preferred_term", "identifier": "CHEBI:63940", "preferred_term": "Na2WO4", "ontology_id": "CHEBI:63940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:132751": [{"label": "Thiamine-HCl x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:132751", "preferred_term": "Thiamine-HCl x 2 H2O", "ontology_id": "CHEBI:132751", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31345": [{"label": "Calcium pantothenate", "match_type": "preferred_term", "identifier": "CHEBI:31345", "preferred_term": "Calcium pantothenate", "ontology_id": "CHEBI:31345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49553": [{"label": "CuCl2", "match_type": "preferred_term", "identifier": "CHEBI:49553", "preferred_term": "CuCl2", "ontology_id": "CHEBI:49553", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| api | https://mediadive.dsmz.de/rest/medium/1647; Complete data.medium and all four data.solutions, IDs 3408, 3409, 5769, 5770 | supports | The provider declares 1000 ml for each separate solution. All 42 recipe rows, stock links, amounts, units and steps were compared with the exact primary and local layers. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf; Both pages; main table, three stock tables and post-autoclave sentence; page 1 also visually inspected | supports | The exact primary specifies three 1 ml stock additions, distinct main and trace calcium, NH4Cl 0.54 ml, and a modified trace stock with ten solutes. The vitamin table explicitly specifies thiamine hydrochloride dihydrate. |
| trace-prep | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318.pdf; Page 2 trace-element preparation, with page 1 trace table read for comparison only | supports | Trace preparation starts with NTA in 200 ml water, adjusts pH to 6.5, then makes up to 1000 ml at pH 6.5. Its table has three additional salts absent from the modified 1647 table; its basal medium and 10x vitamins are excluded. |
| vit-prep | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf; Page 1 named vitamin preparation sentence; pages 2–3 vitamin table as comparison only | supports | The explicitly named vitamin preparation uses 100% N2 and filtration. The current 141 thiamine HCl table does not override the dihydrate explicitly specified in 1647. Other 141 ingredients, gases and organism-specific conditions are excluded. |
| quantities | /private/tmp/culturemech-review-work-batch016/152/quantity-inventory.json; Complete source-linked quantity decision inventory | context_only | All 42 provider recipe rows are reconciled against the primary main and three stock tables, including three explicit trace-composition conflicts; five further decisions cover existing and missing scoped preparation. Every value is attributed to its own stage and source. No unsupported claim is marked verified. |
| writer | src/culturemech/import/mediadive_importer.py; scripts/cleanup_media_quality.py; src/culturemech/merge/formulation.py; _parse_api_composition/_is_api_stock_addition/_parse_api_solutions/_normalize_unit; _merge_ingredient_group; merge_formulation_evidence | context_only | Current importer selects main solution, retains stock references and prefers provider g_l; it still cannot independently justify this NH4Cl conversion. Current cleanup does not sum conflicting duplicates. Current formulation merge preserves evidence only for compatible inputs. These current functions are context, not a historical replay of the recorded import or calcium sum. |

## Limits And Additional Notes

- The inspected DSMZ 1647 PDF prints NH4Cl 0.54 ml, confirmed visually on page 1. Its strength or density is unspecified; no mass replacement is inferred.
- Current DSMZ 318 and 141 are used only for the preparations explicitly cross-referenced by DSMZ 1647. Their complete basal recipes, organism-specific variants and different stock compositions do not replace the exact 1647 tables. Source chronology or intent is not inferred from copyright years.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T102807Z-culturemech-001130-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acetobacteroides_medium (CultureMech:001130)'
started_at: '2026-10-21T10:23:10Z'
finished_at: '2026-10-21T10:28:07Z'
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
summary: DSMZ 1647 is correctly identified, but the local formulation collapses three
  separately dosed stocks into main-medium concentrations, adds calcium across incompatible
  stages, and retains a provider trace composition that differs from the primary modified
  stock. The ammonium-chloride mass conversion lacks source support; nickel hydrate
  grounding and stock preparation/evidence need curation.
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
  - path: data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml
    sha256: cd9f098546b757567ac790928dbf0ed267c4cd4b9497fa6872d7ca428eefe7b8
    role: target
  - path: data/normalized_yaml/bacterial/acetobacteroides_medium.yaml
    sha256: 2b0c4a5a8c917276d41c6487a0ec6e1b2af2fb3b6169b6978497749fa8675b26
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
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/komodo_web_raw_yaml.py
    sha256: a1a37015b4e6bac657e49f375b39a319815cc6b02a02135674a858a8b6eab03a
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
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/fetch/komodo_web_fetcher.py
    sha256: 89c510caa08d989b7ec6cee9ac17cc2f0faab606fe8a29ca435df476e52ff004
    role: context
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
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
  selection: Task review 152; batch 016 item 2 of 10, selected in Python lexicographic
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
  - CultureMech:001130
targets:
- target_id: CultureMech:001130
  path: data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml
  label: acetobacteroides_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacteroides_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001130
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch016/152/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-016/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch016/152/strict.tsv"
  target_ids:
  - CultureMech:001130
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001130
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001130
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
  - CultureMech:001130
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T10:28:06Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/acetobacteroides_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:28:06Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:23:48.068284Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch016/152/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T10:23:49.705561Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-016/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch016/152/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:23:51.633703Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:23:52.833331Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T10:28:06Z'
  support: supports
  summary: './data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml:1:id: CultureMech:001130

    ./data/normalized_yaml/bacterial/acetobacteroides_medium.yaml:1:id: CultureMech:001130

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: chebi131361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T07:33:27.980786Z'
  support: supports
  summary: 'CHEBI:131361 resolves to disodium selenite pentahydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"generalized_empirical_formula": ["5H2O.2Na.O3Se"],
    "inchi_string": ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"],
    "mass": ["263.012"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]}'
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi132751
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T09:49:54.818359Z'
  support: supports
  summary: 'CHEBI:132751 resolves to thiamine hydrochloride dihydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"generalized_empirical_formula": ["C12H18N4OS.2Cl.2H2O"],
    "inchi_string": ["InChI=1S/C12H17N4OS.2ClH.2H2O/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H;2*1H2/q+1;;;;/p-1"],
    "mass": ["373.306"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c([NH3+])n1.O.O.[Cl-].[Cl-]"]}'
  snapshot_sha256: 509a9cc0fafffbbccf4801dc30121b1cf3d5d176746d0003356be395faf625e9
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: 'CHEBI:15940 resolves to nicotinic acid; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"generalized_empirical_formula": ["C6H5NO2"], "inchi_string":
    ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"], "mass": ["123.111"],
    "smiles_string": ["O=C(O)c1cccnc1"]}'
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: 'CHEBI:15956 resolves to biotin; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"generalized_empirical_formula": ["C10H16N2O3S"], "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"],
    "mass": ["244.316"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]}'
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16494
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:13.001958Z'
  support: supports
  summary: 'CHEBI:16494 resolves to lipoic acid; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"generalized_empirical_formula": ["C8H14O2S2"], "inchi_string": ["InChI=1S/C8H14O2S2/c9-8(10)4-2-1-3-7-5-6-11-12-7/h7H,1-6H2,(H,9,10)"],
    "mass": ["206.332"], "smiles_string": ["O=C(O)CCCCC1CCSS1"]}'
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: 'CHEBI:17015 resolves to riboflavin; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"generalized_empirical_formula": ["C17H20N4O6"], "inchi_string": ["InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23)14(25)12(24)6-22)15-13(18-9)16(26)20-17(27)19-15/h3-4,11-12,14,22-25H,5-6H2,1-2H3,(H,20,26,27)/t11-,12+,14-/m0/s1"],
    "mass": ["376.369"], "smiles_string": ["Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)CO)c2cc1C"]}'
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:26.738243Z'
  support: supports
  summary: 'CHEBI:17234 resolves to glucose; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"generalized_empirical_formula": ["C6H12O6"], "mass": ["180.156"]}'
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: 'CHEBI:176843 resolves to vitamin B12; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {}'
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: 'CHEBI:26710 resolves to sodium chloride; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"generalized_empirical_formula": ["Cl.Na"], "inchi_string":
    ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "smiles_string": ["[Cl-].[Na+]"]}'
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: 'CHEBI:27470 resolves to folic acid; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"generalized_empirical_formula": ["C19H19N7O6"], "inchi_string": ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"],
    "mass": ["441.404"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]}'
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: 'CHEBI:30753 resolves to 4-aminobenzoic acid; canonical label and live
    status alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"generalized_empirical_formula": ["C7H7NO2"], "inchi_string":
    ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"], "mass": ["137.138"],
    "smiles_string": ["Nc1ccc(C(=O)O)cc1"]}'
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: 'CHEBI:30961 resolves to pyridoxine hydrochloride; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"generalized_empirical_formula": ["C8H11NO3.HCl"],
    "inchi_string": ["InChI=1S/C8H11NO3.ClH/c1-5-8(12)7(4-11)6(3-10)2-9-5;/h2,10-12H,3-4H2,1H3;1H"],
    "mass": ["205.641"], "smiles_string": ["Cc1ncc(CO)c(CO)c1O.Cl"]}'
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: 'CHEBI:31206 resolves to ammonium chloride; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"generalized_empirical_formula": ["Cl.H4N"], "inchi_string":
    ["InChI=1S/ClH.H3N/h1H;1H3"], "mass": ["53.492"], "smiles_string": ["[Cl-].[H][N+]([H])([H])[H]"]}'
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: 'CHEBI:31345 resolves to Calcium pantothenate; canonical label and live
    status alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"generalized_empirical_formula": ["2C9H16NO5.Ca"], "inchi_string":
    ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"],
    "mass": ["476.536"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]}'
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: 'CHEBI:32139 resolves to sodium hydrogencarbonate; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"generalized_empirical_formula": ["CHO3.Na"], "inchi_string":
    ["InChI=1S/CH2O3.Na/c2-1(3)4;/h(H2,2,3,4);/q;+1/p-1"], "mass": ["84.006"], "smiles_string":
    ["O=C([O-])O.[Na+]"]}'
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: 'CHEBI:33118 resolves to boric acid; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"generalized_empirical_formula": ["H3BO3"], "inchi_string": ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"],
    "mass": ["61.833"], "smiles_string": ["[H]OB(O[H])O[H]"]}'
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: 'CHEBI:34887 resolves to nickel dichloride; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"generalized_empirical_formula": ["Cl2Ni"], "inchi_string":
    ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"], "mass": ["129.599"], "smiles_string": ["[Cl][Ni][Cl]"]}'
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi44557
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:46:15.250117Z'
  support: supports
  summary: 'CHEBI:44557 resolves to nitrilotriacetic acid; canonical label and live
    status alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"generalized_empirical_formula": ["C6H9NO6"], "inchi_string":
    ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"],
    "mass": ["191.139"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]}'
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
- evidence_id: chebi48843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_48843
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T10:07:16.976958Z'
  support: supports
  summary: 'CHEBI:48843 resolves to disodium selenite; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"generalized_empirical_formula": ["2Na.O3Se"], "inchi_string":
    ["InChI=1S/2Na.H2O3Se/c;;1-4(2)3/h;;(H2,1,2,3)/q2*+1;/p-2"], "mass": ["172.937"],
    "smiles_string": ["O=[Se]([O-])[O-].[Na+].[Na+]"]}'
  snapshot_sha256: f8b54c90292c3ea1c215cbb96e7b9302304ba97f07c586c66f09b6689b9f2d91
- evidence_id: chebi49553
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49553
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T10:07:17.608864Z'
  support: supports
  summary: 'CHEBI:49553 resolves to copper(II) chloride; canonical label and live
    status alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"generalized_empirical_formula": ["Cl2Cu"], "inchi_string":
    ["InChI=1S/2ClH.Cu/h2*1H;/q;;+2/p-2"], "mass": ["134.452"], "smiles_string": ["[Cl][Cu][Cl]"]}'
  snapshot_sha256: 55d84961ae8c483bc2364cb9c5f159267161b61a3c77c93632021c6f4ea1810d
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: 'CHEBI:49976 resolves to zinc dichloride; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"generalized_empirical_formula": ["2Cl.Zn"], "inchi_string":
    ["InChI=1S/2ClH.Zn/h2*1H;/q;;+2/p-2"], "mass": ["136.296"], "smiles_string": ["[Cl-].[Cl-].[Zn+2]"]}'
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: 'CHEBI:53503 resolves to cobalt chloride hexahydrate; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"generalized_empirical_formula": ["2Cl.Co.6H2O"],
    "inchi_string": ["InChI=1S/2ClH.Co.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass":
    ["237.929"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Co+2]"]}'
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: 'CHEBI:63036 resolves to potassium dihydrogen phosphate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"generalized_empirical_formula": ["H2O4P.K"],
    "inchi_string": ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass":
    ["136.084"], "smiles_string": ["O=P([O-])(O)O.[K+]"]}'
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: 'CHEBI:63939 resolves to sodium tungstate dihydrate; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"generalized_empirical_formula": ["2H2O.2Na.O4W"],
    "inchi_string": ["InChI=1S/2Na.2H2O.4O.W/h;;2*1H2;;;;;/q2*+1;;;;;2*-1;"], "mass":
    ["329.846"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]}'
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi63940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63940
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T10:07:18.442988Z'
  support: supports
  summary: 'CHEBI:63940 resolves to sodium tungstate; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"generalized_empirical_formula": ["2Na.O4W"], "inchi_string":
    ["InChI=1S/2Na.4O.W/q2*+1;;;2*-1;"], "mass": ["293.816"], "smiles_string": ["[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]}'
  snapshot_sha256: c40f4b9c14d073989f58af77af0f1ffe969948e21d2bbe05a08c919f776aaf5c
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: 'CHEBI:75213 resolves to sodium molybdate dihydrate; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"generalized_empirical_formula": ["2H2O.MoO4.2Na"],
    "inchi_string": ["InChI=1S/Mo.2Na.2H2O.4O/h;;;2*1H2;;;;/q;2*+1;;;;;2*-1"], "mass":
    ["241.946"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]}'
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: 'CHEBI:76209 resolves to sodium sulfide nonahydrate; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"generalized_empirical_formula": ["9H2O.2Na.S"],
    "inchi_string": ["InChI=1S/2Na.9H2O.S/h;;9*1H2;/q2*+1;;;;;;;;;;-2"], "mass": ["240.182"],
    "smiles_string": ["O.O.O.O.O.O.O.O.O.[Na+].[Na+].[S-2]"]}'
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: 'CHEBI:86158 resolves to calcium chloride dihydrate; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"generalized_empirical_formula": ["Ca.2Cl.2H2O"],
    "inchi_string": ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"],
    "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}'
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T09:49:55.693358Z'
  support: supports
  summary: 'CHEBI:86249 resolves to iron dichloride tetrahydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"generalized_empirical_formula": ["Cl2Fe.4H2O"],
    "inchi_string": ["InChI=1S/2ClH.Fe.4H2O/h2*1H;;4*1H2/q;;+2;;;;/p-2"], "mass":
    ["198.811"], "smiles_string": ["O.O.O.O.[Cl][Fe][Cl]"]}'
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: 'CHEBI:86345 resolves to magnesium dichloride hexahydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"generalized_empirical_formula": ["2Cl.6H2O.Mg"],
    "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass":
    ["203.301"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}'
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: 'CHEBI:86368 resolves to manganese(II) chloride tetrahydrate; canonical
    label and live status alone do not verify source grade, hydration, stereochemistry
    or stock identity. Formula/structure: {"generalized_empirical_formula": ["Cl2Mn.4H2O"],
    "inchi_string": ["InChI=1S/2ClH.Mn.4H2O/h2*1H;;4*1H2/q;;+2;;;;/p-2"], "mass":
    ["197.904"], "smiles_string": ["O.O.O.O.[Cl][Mn][Cl]"]}'
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: 'CHEBI:8806 resolves to Resazurin; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"generalized_empirical_formula": ["C12H7NO4"], "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"],
    "mass": ["229.191"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]}'
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi91248
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:42:32.136441Z'
  support: supports
  summary: 'CHEBI:91248 resolves to L-cysteine hydrochloride hydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"],
    "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"],
    "mass": ["175.637"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]}'
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned CSV; preferred-term MAPPED rows for every asserted secondary
    CHEBI key
  accessed_at: '2026-10-21T10:28:06Z'
  support: supports
  summary: '{"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl
    x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term",
    "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label":
    "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term":
    "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term",
    "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:48843": [{"label":
    "Na2SeO3", "match_type": "preferred_term", "identifier": "CHEBI:48843", "preferred_term":
    "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63940": [{"label": "Na2WO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63940", "preferred_term": "Na2WO4", "ontology_id": "CHEBI:63940",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label":
    "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term":
    "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label":
    "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961",
    "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:132751": [{"label": "Thiamine-HCl x
    2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:132751", "preferred_term":
    "Thiamine-HCl x 2 H2O", "ontology_id": "CHEBI:132751", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type":
    "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31345": [{"label":
    "Calcium pantothenate", "match_type": "preferred_term", "identifier": "CHEBI:31345",
    "preferred_term": "Calcium pantothenate", "ontology_id": "CHEBI:31345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}],
    "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494":
    [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label":
    "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557",
    "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term":
    "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503":
    [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier":
    "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id":
    "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976":
    [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976",
    "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:49553": [{"label": "CuCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:49553", "preferred_term": "CuCl2", "ontology_id": "CHEBI:49553",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label":
    "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term":
    "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887":
    [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887",
    "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131361": [{"label":
    "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term":
    "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1647
  locator: Complete data.medium and all four data.solutions, IDs 3408, 3409, 5769,
    5770
  accessed_at: '2026-10-21T10:07:15.156451Z'
  support: supports
  summary: The provider declares 1000 ml for each separate solution. All 42 recipe
    rows, stock links, amounts, units and steps were compared with the exact primary
    and local layers.
  snapshot_sha256: dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf
  locator: Both pages; main table, three stock tables and post-autoclave sentence;
    page 1 also visually inspected
  accessed_at: '2026-10-21T10:07:16.042056Z'
  support: supports
  summary: The exact primary specifies three 1 ml stock additions, distinct main and
    trace calcium, NH4Cl 0.54 ml, and a modified trace stock with ten solutes. The
    vitamin table explicitly specifies thiamine hydrochloride dihydrate.
  snapshot_sha256: 8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad
- evidence_id: trace-prep
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318.pdf
  locator: Page 2 trace-element preparation, with page 1 trace table read for comparison
    only
  accessed_at: '2026-10-21T10:08:09.386964Z'
  support: supports
  summary: Trace preparation starts with NTA in 200 ml water, adjusts pH to 6.5, then
    makes up to 1000 ml at pH 6.5. Its table has three additional salts absent from
    the modified 1647 table; its basal medium and 10x vitamins are excluded.
  snapshot_sha256: 8ca3cb45479ba00e11f9574bf3b315e365e9c98c92bbc5323d4cd5dc4b862f29
- evidence_id: vit-prep
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf
  locator: Page 1 named vitamin preparation sentence; pages 2–3 vitamin table as comparison
    only
  accessed_at: '2026-10-21T10:08:11.018847Z'
  support: supports
  summary: The explicitly named vitamin preparation uses 100% N2 and filtration. The
    current 141 thiamine HCl table does not override the dihydrate explicitly specified
    in 1647. Other 141 ingredients, gases and organism-specific conditions are excluded.
  snapshot_sha256: 8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8
- evidence_id: quantities
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch016/152/quantity-inventory.json
  locator: Complete source-linked quantity decision inventory
  accessed_at: '2026-10-21T10:28:06Z'
  support: context_only
  summary: All 42 provider recipe rows are reconciled against the primary main and
    three stock tables, including three explicit trace-composition conflicts; five
    further decisions cover existing and missing scoped preparation. Every value is
    attributed to its own stage and source. No unsupported claim is marked verified.
  snapshot_sha256: 27a095b4ff6e3b9b2adbbc44bf40d5e6f3b50d89e4810b58aece4f564f506737
- evidence_id: writer
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py; scripts/cleanup_media_quality.py;
    src/culturemech/merge/formulation.py
  locator: _parse_api_composition/_is_api_stock_addition/_parse_api_solutions/_normalize_unit;
    _merge_ingredient_group; merge_formulation_evidence
  accessed_at: '2026-10-21T10:28:06Z'
  support: context_only
  summary: Current importer selects main solution, retains stock references and prefers
    provider g_l; it still cannot independently justify this NH4Cl conversion. Current
    cleanup does not sum conflicting duplicates. Current formulation merge preserves
    evidence only for compatible inputs. These current functions are context, not
    a historical replay of the recorded import or calcium sum.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001130
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding-coverage
  area: grounding
  topic: Exact primary labels and current secondary linkage coverage
  outcome: supported
  summary: '33 unique asserted CHEBI identifiers resolve with exact labels. Primary
    linkage 33/34 (97.06%); verified current secondary linkage 33/34 (97.06%). This
    is a 0–100 ingredient-instance linkage scale, not scientific correctness. Missing
    current secondary keys: []. Legacy links and chemical-form correctness are assessed
    separately.'
  target_ids:
  - CultureMech:001130
  evidence_ids:
  - record
  - mim
  - chebi131361
  - chebi132751
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi17234
  - chebi176843
  - chebi26710
  - chebi27470
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi32139
  - chebi33118
  - chebi34887
  - chebi44557
  - chebi48843
  - chebi49553
  - chebi49976
  - chebi53503
  - chebi63036
  - chebi63939
  - chebi63940
  - chebi75213
  - chebi76209
  - chebi86158
  - chebi86249
  - chebi86345
  - chebi86368
  - chebi8806
  - chebi91248
- assessment_id: history-time
  area: provenance
  topic: Full history and timezone audit
  outcome: supported
  summary: 'History event counts: [(''target'', 9), (''data/normalized_yaml/bacterial/acetobacteroides_medium.yaml'',
    8)]. Explicit timestamp defects: []. Historical bytes are assessed as observed;
    no inferred timezone or retroactive replacement timestamp is supplied.'
  target_ids:
  - CultureMech:001130
  evidence_ids:
  - record
  - owner-0
- assessment_id: quantities
  area: quantity
  topic: Every direct, stock, stock-addition and preparation quantity
  outcome: concern
  summary: All 42 provider recipe rows are reconciled against the primary main and
    three stock tables, including three explicit trace-composition conflicts; five
    further decisions cover existing and missing scoped preparation. Every value is
    attributed to its own stage and source. No unsupported claim is marked verified.
  target_ids:
  - CultureMech:001130
  evidence_ids:
  - record
  - quantities
  - owner-0
  details: '[{"field_path": "ingredients[0].concentration", "decision": "evidence_only",
    "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Yeast extract 0.20 g", "source_locator": "DSMZ 1647; Main sol.
    1647; exact Yeast extract entry", "explanation": "The stored value matches provider
    g/L under its declared 1000 ml normalization. Preserve the primary batch amount
    and unit, attach narrow evidence and qualify the volume basis; there is no existing
    claim-level evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine specificity
    is explicit there but not in the primary unspecific cysteine wording.", "owner_decision":
    "evidence_only", "local_value": {"value": "0.2", "unit": "G_PER_L"}, "provider_reference":
    "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[0].recipe[0] (solution_id 3408)", "provider_quote":
    "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    0.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.2,\n                        \"optional\": 0\n                    }", "source_amount":
    0.2, "source_unit": "g", "provider_g_l": 0.2, "provider_declared_volume_ml": 1000},
    {"field_path": "ingredients[1].concentration", "decision": "evidence_only", "stage":
    "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Glucose 0.18 g", "source_locator": "DSMZ 1647; Main sol. 1647;
    exact Glucose entry", "explanation": "The stored value matches provider g/L under
    its declared 1000 ml normalization. Preserve the primary batch amount and unit,
    attach narrow evidence and qualify the volume basis; there is no existing claim-level
    evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine specificity is explicit
    there but not in the primary unspecific cysteine wording.", "owner_decision":
    "evidence_only", "local_value": {"value": "0.18", "unit": "G_PER_L"}, "provider_reference":
    "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[0].recipe[1] (solution_id 3408)", "provider_quote":
    "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\":
    0.18,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.18,\n                        \"mmol_l\": 0.999112,\n                        \"optional\":
    0\n                    }", "source_amount": 0.18, "source_unit": "g", "provider_g_l":
    0.18, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[2].concentration",
    "decision": "evidence_only", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "KH\n2PO4 0.14 g", "source_locator": "DSMZ 1647; Main sol. 1647;
    exact KH2PO4 entry", "explanation": "The stored value matches provider g/L under
    its declared 1000 ml normalization. Preserve the primary batch amount and unit,
    attach narrow evidence and qualify the volume basis; there is no existing claim-level
    evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine specificity is explicit
    there but not in the primary unspecific cysteine wording.", "owner_decision":
    "evidence_only", "local_value": {"value": "0.14", "unit": "G_PER_L"}, "provider_reference":
    "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[0].recipe[2] (solution_id 3408)", "provider_quote":
    "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\":
    0.14,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.14,\n                        \"mmol_l\": 1.02877,\n                        \"optional\":
    0\n                    }", "source_amount": 0.14, "source_unit": "g", "provider_g_l":
    0.14, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[3].concentration",
    "decision": "evidence_only", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "MgCl2 x 6 H2O 0.20 g", "source_locator": "DSMZ 1647; Main sol.
    1647; exact MgCl2 x 6 H2O entry", "explanation": "The stored value matches provider
    g/L under its declared 1000 ml normalization. Preserve the primary batch amount
    and unit, attach narrow evidence and qualify the volume basis; there is no existing
    claim-level evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine specificity
    is explicit there but not in the primary unspecific cysteine wording.", "owner_decision":
    "evidence_only", "local_value": {"value": "0.2", "unit": "G_PER_L"}, "provider_reference":
    "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[0].recipe[3] (solution_id 3408)", "provider_quote":
    "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\":
    0.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.2,\n                        \"mmol_l\": 0.983753,\n                        \"optional\":
    0\n                    }", "source_amount": 0.2, "source_unit": "g", "provider_g_l":
    0.2, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[4].concentration",
    "decision": "correct", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "CaCl2 x 2 H2O 0.15 g", "source_locator": "DSMZ 1647; Main sol.
    1647; exact CaCl2 x 2 H2O entry", "explanation": "The local 0.25 g/L is the numerical
    sum of 0.15 g in the main batch and 0.10 g in a separate litre of trace stock.
    Restore the separate stages. The stock dose of 1 ml transfers 0.0001 g calcium
    chloride dihydrate; 0.1501 g is a conditional combined batch mass, not a verified
    final-volume concentration.", "owner_decision": "correct", "local_value": {"value":
    "0.25", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[0].recipe[4] (solution_id 3408)", "provider_quote":
    "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\":
    0.15,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.15,\n                        \"mmol_l\": 1.0203,\n                        \"optional\":
    0\n                    }", "source_amount": 0.15, "source_unit": "g", "provider_g_l":
    0.15, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[5].concentration",
    "decision": "unsupported", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "NH4Cl 0.54 ml", "source_locator": "DSMZ 1647; Main sol. 1647;
    exact NH4Cl entry", "explanation": "Both primary image and provider amount state
    0.54 ml, but no strength or density supports provider g_l=0.824796. Preserve the
    literal source unit and unresolved mass conversion; do not silently replace ml
    with g.", "owner_decision": "unsupported", "local_value": {"value": "0.824796",
    "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[0].recipe[5] (solution_id 3408)", "provider_quote":
    "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\":
    0.54,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.824796,\n                        \"mmol_l\": 15.4196,\n                        \"optional\":
    0\n                    }", "source_amount": 0.54, "source_unit": "ml", "provider_g_l":
    0.824796, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[6].concentration",
    "decision": "evidence_only", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Cysteine-HCl x H2O 0.30 g", "source_locator": "DSMZ 1647; Main
    sol. 1647; exact L-Cysteine HCl x H2O entry", "explanation": "The stored value
    matches provider g/L under its declared 1000 ml normalization. Preserve the primary
    batch amount and unit, attach narrow evidence and qualify the volume basis; there
    is no existing claim-level evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine
    specificity is explicit there but not in the primary unspecific cysteine wording.",
    "owner_decision": "evidence_only", "local_value": {"value": "0.3", "unit": "G_PER_L"},
    "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256":
    "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator":
    "$.data.solutions[0].recipe[6] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\":
    770,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    1.70808,\n                        \"optional\": 0\n                    }", "source_amount":
    0.3, "source_unit": "g", "provider_g_l": 0.3, "provider_declared_volume_ml": 1000},
    {"field_path": "ingredients[7].concentration", "decision": "evidence_only", "stage":
    "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "NaHCO3 2.50 g", "source_locator": "DSMZ 1647; Main sol. 1647;
    exact NaHCO3 entry", "explanation": "The stored value matches provider g/L under
    its declared 1000 ml normalization. Preserve the primary batch amount and unit,
    attach narrow evidence and qualify the volume basis; there is no existing claim-level
    evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine specificity is explicit
    there but not in the primary unspecific cysteine wording.", "owner_decision":
    "evidence_only", "local_value": {"value": "2.5", "unit": "G_PER_L"}, "provider_reference":
    "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[0].recipe[7] (solution_id 3408)", "provider_quote":
    "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\":
    2.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 29.7594,\n                        \"optional\":
    0\n                    }", "source_amount": 2.5, "source_unit": "g", "provider_g_l":
    2.5, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[8].concentration",
    "decision": "evidence_only", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Na2S x 9 H2O 0.30 g", "source_locator": "DSMZ 1647; Main sol.
    1647; exact Na2S x 9 H2O entry", "explanation": "The stored value matches provider
    g/L under its declared 1000 ml normalization. Preserve the primary batch amount
    and unit, attach narrow evidence and qualify the volume basis; there is no existing
    claim-level evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine specificity
    is explicit there but not in the primary unspecific cysteine wording.", "owner_decision":
    "evidence_only", "local_value": {"value": "0.3", "unit": "G_PER_L"}, "provider_reference":
    "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[0].recipe[8] (solution_id 3408)", "provider_quote":
    "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\":
    0.3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.3,\n                        \"mmol_l\": 1.24905,\n                        \"optional\":
    0\n                    }", "source_amount": 0.3, "source_unit": "g", "provider_g_l":
    0.3, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[9].concentration",
    "decision": "evidence_only", "stage": "Main sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Resazurin 1.00 mg", "source_locator": "DSMZ 1647; Main sol. 1647;
    exact Resazurin entry", "explanation": "The stored value matches provider g/L
    under its declared 1000 ml normalization. Preserve the primary batch amount and
    unit, attach narrow evidence and qualify the volume basis; there is no existing
    claim-level evidence. For resazurin 1 mg is 0.001 g. Provider L-cysteine specificity
    is explicit there but not in the primary unspecific cysteine wording.", "owner_decision":
    "evidence_only", "local_value": {"value": "0.001", "unit": "G_PER_L"}, "provider_reference":
    "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[0].recipe[9] (solution_id 3408)", "provider_quote":
    "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\":
    1,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.001,\n                        \"mmol_l\": 0.00436319,\n                        \"optional\":
    0\n                    }", "source_amount": 1, "source_unit": "mg", "provider_g_l":
    0.001, "provider_declared_volume_ml": 1000}, {"field_path": "solutions (missing
    additions)", "decision": "add", "stage": "Main sol. 1647", "source_reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256":
    "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote":
    "Vitamin solution (see below) 1 ml", "source_locator": "DSMZ 1647; Main sol. 1647;
    exact Vitamin solution entry", "explanation": "The exact 1 ml stock addition is
    absent as a structured solution. Preserve this dose and the corresponding stock
    recipe separately; a stock concentration is not a final-medium concentration.",
    "owner_decision": "add", "local_value": null, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[0].recipe[10] (solution_id 3408)", "provider_quote":
    "{\n                        \"recipe_order\": 11,\n                        \"solution\":
    \"Vitamin solution\",\n                        \"solution_id\": 5769,\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_amount": 1, "source_unit": "ml", "provider_g_l":
    null, "provider_declared_volume_ml": 1000}, {"field_path": "solutions (missing
    additions)", "decision": "add", "stage": "Main sol. 1647", "source_reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256":
    "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote":
    "Trace element solution (see below) 1.00 ml", "source_locator": "DSMZ 1647; Main
    sol. 1647; exact Trace element solution entry", "explanation": "The exact 1 ml
    stock addition is absent as a structured solution. Preserve this dose and the
    corresponding stock recipe separately; a stock concentration is not a final-medium
    concentration.", "owner_decision": "add", "local_value": null, "provider_reference":
    "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[0].recipe[11] (solution_id 3408)", "provider_quote":
    "{\n                        \"recipe_order\": 12,\n                        \"solution\":
    \"Trace element solution\",\n                        \"solution_id\": 5770,\n                        \"attribute\":
    \"\",\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_amount":
    1, "source_unit": "ml", "provider_g_l": null, "provider_declared_volume_ml": 1000},
    {"field_path": "solutions (missing additions)", "decision": "add", "stage": "Main
    sol. 1647", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Se/W solution (see below) 1.00 ml", "source_locator": "DSMZ 1647;
    Main sol. 1647; exact Se/W solution entry", "explanation": "The exact 1 ml stock
    addition is absent as a structured solution. Preserve this dose and the corresponding
    stock recipe separately; a stock concentration is not a final-medium concentration.",
    "owner_decision": "add", "local_value": null, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[0].recipe[12] (solution_id 3408)", "provider_quote":
    "{\n                        \"recipe_order\": 13,\n                        \"solution\":
    \"Se/W solution\",\n                        \"solution_id\": 3409,\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_amount": 1, "source_unit": "ml", "provider_g_l":
    null, "provider_declared_volume_ml": 1000}, {"field_path": "preparation_steps
    (missing scoped solvent)", "decision": "add", "stage": "Main sol. 1647", "source_reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256":
    "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote":
    "Distilled water 1000.00 ml", "source_locator": "DSMZ 1647; Main sol. 1647; exact
    Distilled water entry", "explanation": "Preserve 1000 ml main water as solvent/batch
    context. Provider volume is declared as 1000 ml, but source water plus additions
    is not an independently measured final volume.", "owner_decision": "add", "local_value":
    null, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256":
    "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator":
    "$.data.solutions[0].recipe[13] (solution_id 3408)", "provider_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_amount":
    1000, "source_unit": "ml", "provider_g_l": null, "provider_declared_volume_ml":
    1000}, {"field_path": "ingredients[10].concentration", "decision": "correct",
    "stage": "Se/W solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Na\n2SeO3 4.0 mg", "source_locator": "DSMZ 1647; Se/W solution;
    exact Na2SeO3 entry", "explanation": "This amount belongs to a separately prepared
    1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L
    is stock strength incorrectly placed among direct medium ingredients. Amount times
    1/1000 is the transferred mass; division by actual final medium volume requires
    a supported volume basis. Preserve exact supplied form and original mg/g unit.",
    "owner_decision": "correct", "local_value": {"value": "0.004", "unit": "G_PER_L"},
    "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256":
    "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator":
    "$.data.solutions[1].recipe[0] (solution_id 3409)", "provider_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2SeO3\",\n                        \"compound_id\":
    699,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0231297,\n                        \"optional\": 0\n                    }", "source_amount":
    4, "source_unit": "mg", "provider_g_l": 0.004, "provider_declared_volume_ml":
    1000}, {"field_path": "ingredients[11].concentration", "decision": "correct",
    "stage": "Se/W solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Na2WO4 4.0 mg", "source_locator": "DSMZ 1647; Se/W solution;
    exact Na2WO4 entry", "explanation": "This amount belongs to a separately prepared
    1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L
    is stock strength incorrectly placed among direct medium ingredients. Amount times
    1/1000 is the transferred mass; division by actual final medium volume requires
    a supported volume basis. Preserve exact supplied form and original mg/g unit.",
    "owner_decision": "correct", "local_value": {"value": "0.004", "unit": "G_PER_L"},
    "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256":
    "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator":
    "$.data.solutions[1].recipe[1] (solution_id 3409)", "provider_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2WO4\",\n                        \"compound_id\":
    550,\n                        \"amount\": 4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\":
    0.0136138,\n                        \"optional\": 0\n                    }", "source_amount":
    4, "source_unit": "mg", "provider_g_l": 0.004, "provider_declared_volume_ml":
    1000}, {"field_path": "preparation_steps (missing scoped solvent)", "decision":
    "add", "stage": "Se/W solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Distilled water 1000.00 ml", "source_locator": "DSMZ 1647; Se/W
    solution; exact Distilled water entry", "explanation": "Retain the separate stock
    solvent quantity of 1000 ml. This is not another direct main-medium water addition.",
    "owner_decision": "add", "local_value": null, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[1].recipe[2] (solution_id 3409)", "provider_quote":
    "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_amount": 1000, "source_unit": "ml", "provider_g_l":
    null, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[12].concentration",
    "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Biotin 2.00 mg", "source_locator": "DSMZ 1647; Vitamin solution;
    exact Biotin entry", "explanation": "This amount belongs to a separately prepared
    1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L
    is stock strength incorrectly placed among direct medium ingredients. Amount times
    1/1000 is the transferred mass; division by actual final medium volume requires
    a supported volume basis. Preserve exact supplied form and original mg/g unit.",
    "owner_decision": "correct", "local_value": {"value": "0.002", "unit": "G_PER_L"},
    "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256":
    "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator":
    "$.data.solutions[2].recipe[0] (solution_id 5769)", "provider_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.00818632,\n                        \"optional\": 0\n                    }",
    "source_amount": 2, "source_unit": "mg", "provider_g_l": 0.002, "provider_declared_volume_ml":
    1000}, {"field_path": "ingredients[13].concentration", "decision": "correct",
    "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Folic acid 2.00 mg", "source_locator": "DSMZ 1647; Vitamin solution;
    exact Folic acid entry", "explanation": "This amount belongs to a separately prepared
    1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L
    is stock strength incorrectly placed among direct medium ingredients. Amount times
    1/1000 is the transferred mass; division by actual final medium volume requires
    a supported volume basis. Preserve exact supplied form and original mg/g unit.",
    "owner_decision": "correct", "local_value": {"value": "0.002", "unit": "G_PER_L"},
    "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256":
    "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator":
    "$.data.solutions[2].recipe[1] (solution_id 5769)", "provider_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.00453104,\n                        \"optional\": 0\n                    }",
    "source_amount": 2, "source_unit": "mg", "provider_g_l": 0.002, "provider_declared_volume_ml":
    1000}, {"field_path": "ingredients[14].concentration", "decision": "correct",
    "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Pyridoxine-HCl 10.00 mg", "source_locator": "DSMZ 1647; Vitamin
    solution; exact Pyridoxine hydrochloride entry", "explanation": "This amount belongs
    to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main
    recipe. The local G_PER_L is stock strength incorrectly placed among direct medium
    ingredients. Amount times 1/1000 is the transferred mass; division by actual final
    medium volume requires a supported volume basis. Preserve exact supplied form
    and original mg/g unit.", "owner_decision": "correct", "local_value": {"value":
    "0.01", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[2].recipe[2] (solution_id 5769)", "provider_quote":
    "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\":
    10,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.0486287,\n                        \"optional\":
    0\n                    }", "source_amount": 10, "source_unit": "mg", "provider_g_l":
    0.01, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[15].concentration",
    "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Thiamine-HCl x 2 H2O 5.00 mg", "source_locator": "DSMZ 1647;
    Vitamin solution; exact Thiamine-HCl x 2 H2O entry", "explanation": "This amount
    belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into
    the main recipe. The local G_PER_L is stock strength incorrectly placed among
    direct medium ingredients. Amount times 1/1000 is the transferred mass; division
    by actual final medium volume requires a supported volume basis. Preserve exact
    supplied form and original mg/g unit.", "owner_decision": "correct", "local_value":
    {"value": "0.005", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[2].recipe[3] (solution_id 5769)", "provider_quote":
    "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.013394,\n                        \"optional\":
    0\n                    }", "source_amount": 5, "source_unit": "mg", "provider_g_l":
    0.005, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[16].concentration",
    "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Riboflavin 5.00 mg", "source_locator": "DSMZ 1647; Vitamin solution;
    exact Riboflavin entry", "explanation": "This amount belongs to a separately prepared
    1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L
    is stock strength incorrectly placed among direct medium ingredients. Amount times
    1/1000 is the transferred mass; division by actual final medium volume requires
    a supported volume basis. Preserve exact supplied form and original mg/g unit.",
    "owner_decision": "correct", "local_value": {"value": "0.005", "unit": "G_PER_L"},
    "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256":
    "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator":
    "$.data.solutions[2].recipe[4] (solution_id 5769)", "provider_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0132837,\n                        \"optional\": 0\n                    }", "source_amount":
    5, "source_unit": "mg", "provider_g_l": 0.005, "provider_declared_volume_ml":
    1000}, {"field_path": "ingredients[17].concentration", "decision": "correct",
    "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Nicotinic acid 5.00 mg", "source_locator": "DSMZ 1647; Vitamin
    solution; exact Nicotinic acid entry", "explanation": "This amount belongs to
    a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main
    recipe. The local G_PER_L is stock strength incorrectly placed among direct medium
    ingredients. Amount times 1/1000 is the transferred mass; division by actual final
    medium volume requires a supported volume basis. Preserve exact supplied form
    and original mg/g unit.", "owner_decision": "correct", "local_value": {"value":
    "0.005", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[2].recipe[5] (solution_id 5769)", "provider_quote":
    "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0406141,\n                        \"optional\":
    0\n                    }", "source_amount": 5, "source_unit": "mg", "provider_g_l":
    0.005, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[18].concentration",
    "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "D-Ca-pantothenate 5.00 mg", "source_locator": "DSMZ 1647; Vitamin
    solution; exact D-Calcium pantothenate entry", "explanation": "This amount belongs
    to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main
    recipe. The local G_PER_L is stock strength incorrectly placed among direct medium
    ingredients. Amount times 1/1000 is the transferred mass; division by actual final
    medium volume requires a supported volume basis. Preserve exact supplied form
    and original mg/g unit.", "owner_decision": "correct", "local_value": {"value":
    "0.005", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[2].recipe[6] (solution_id 5769)", "provider_quote":
    "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"D-Calcium pantothenate\",\n                        \"compound_id\": 1807,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"optional\": 0\n                    }", "source_amount":
    5, "source_unit": "mg", "provider_g_l": 0.005, "provider_declared_volume_ml":
    1000}, {"field_path": "ingredients[19].concentration", "decision": "correct",
    "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Vitamin B\n12 0.10 mg", "source_locator": "DSMZ 1647; Vitamin
    solution; exact Vitamin B12 entry", "explanation": "This amount belongs to a separately
    prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local
    G_PER_L is stock strength incorrectly placed among direct medium ingredients.
    Amount times 1/1000 is the transferred mass; division by actual final medium volume
    requires a supported volume basis. Preserve exact supplied form and original mg/g
    unit.", "owner_decision": "correct", "local_value": {"value": "0.0001", "unit":
    "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[2].recipe[7] (solution_id 5769)", "provider_quote":
    "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\":
    0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.0001,\n                        \"mmol_l\": 7.3779e-5,\n                        \"optional\":
    0\n                    }", "source_amount": 0.1, "source_unit": "mg", "provider_g_l":
    0.0001, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[20].concentration",
    "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "p-Aminobenzoic acid 5.00 mg", "source_locator": "DSMZ 1647; Vitamin
    solution; exact p-Aminobenzoic acid entry", "explanation": "This amount belongs
    to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into the main
    recipe. The local G_PER_L is stock strength incorrectly placed among direct medium
    ingredients. Amount times 1/1000 is the transferred mass; division by actual final
    medium volume requires a supported volume basis. Preserve exact supplied form
    and original mg/g unit.", "owner_decision": "correct", "local_value": {"value":
    "0.005", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[2].recipe[8] (solution_id 5769)", "provider_quote":
    "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0364591,\n                        \"optional\":
    0\n                    }", "source_amount": 5, "source_unit": "mg", "provider_g_l":
    0.005, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[21].concentration",
    "decision": "correct", "stage": "Vitamin solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Lipoic acid 5.00 mg", "source_locator": "DSMZ 1647; Vitamin solution;
    exact Lipoic acid entry", "explanation": "This amount belongs to a separately
    prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local
    G_PER_L is stock strength incorrectly placed among direct medium ingredients.
    Amount times 1/1000 is the transferred mass; division by actual final medium volume
    requires a supported volume basis. Preserve exact supplied form and original mg/g
    unit.", "owner_decision": "correct", "local_value": {"value": "0.005", "unit":
    "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[2].recipe[9] (solution_id 5769)", "provider_quote":
    "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Lipoic acid\",\n                        \"compound_id\": 368,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.024233,\n                        \"optional\":
    0\n                    }", "source_amount": 5, "source_unit": "mg", "provider_g_l":
    0.005, "provider_declared_volume_ml": 1000}, {"field_path": "preparation_steps
    (missing scoped solvent)", "decision": "add", "stage": "Vitamin solution", "source_reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256":
    "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote":
    "Distilled water 1000.00 ml", "source_locator": "DSMZ 1647; Vitamin solution;
    exact Distilled water entry", "explanation": "Retain the separate stock solvent
    quantity of 1000 ml. This is not another direct main-medium water addition.",
    "owner_decision": "add", "local_value": null, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[2].recipe[10] (solution_id 5769)", "provider_quote":
    "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_amount": 1000, "source_unit": "ml", "provider_g_l":
    null, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[22].concentration",
    "decision": "correct", "stage": "Trace element solution", "source_reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256":
    "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote":
    "Nitrilotriacetic acid (NTA) 12.80 g", "source_locator": "DSMZ 1647; modified
    Trace element solution; exact Nitrilotriacetic acid entry", "explanation": "This
    amount belongs to a separately prepared 1000 ml stock, subsequently dosed at 1
    ml into the main recipe. The local G_PER_L is stock strength incorrectly placed
    among direct medium ingredients. Amount times 1/1000 is the transferred mass;
    division by actual final medium volume requires a supported volume basis. Preserve
    exact supplied form and original mg/g unit.", "owner_decision": "correct", "local_value":
    {"value": "12.8", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[3].recipe[0] (solution_id 5770)", "provider_quote":
    "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"attribute\":
    \"NTA\",\n                        \"amount\": 12.8,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 12.8,\n                        \"mmol_l\":
    66.9666,\n                        \"optional\": 0\n                    }", "source_amount":
    12.8, "source_unit": "g", "provider_g_l": 12.8, "provider_declared_volume_ml":
    1000}, {"field_path": "ingredients[23].concentration", "decision": "correct",
    "stage": "Trace element solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "FeCl\n2 x 4 H2O 1.00 g", "source_locator": "DSMZ 1647; modified
    Trace element solution; exact FeCl2 x 4 H2O entry", "explanation": "This amount
    belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into
    the main recipe. The local G_PER_L is stock strength incorrectly placed among
    direct medium ingredients. Amount times 1/1000 is the transferred mass; division
    by actual final medium volume requires a supported volume basis. Preserve exact
    supplied form and original mg/g unit.", "owner_decision": "correct", "local_value":
    {"value": "1", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[3].recipe[1] (solution_id 5770)", "provider_quote":
    "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 5.02988,\n                        \"optional\":
    0\n                    }", "source_amount": 1, "source_unit": "g", "provider_g_l":
    1, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[24].concentration",
    "decision": "correct", "stage": "Trace element solution", "source_reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256":
    "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote":
    "MnCl2 x 4 H2O 0.10 g", "source_locator": "DSMZ 1647; modified Trace element solution;
    exact MnCl2 x 4 H2O entry", "explanation": "This amount belongs to a separately
    prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local
    G_PER_L is stock strength incorrectly placed among direct medium ingredients.
    Amount times 1/1000 is the transferred mass; division by actual final medium volume
    requires a supported volume basis. Preserve exact supplied form and original mg/g
    unit.", "owner_decision": "correct", "local_value": {"value": "0.1", "unit": "G_PER_L"},
    "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256":
    "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator":
    "$.data.solutions[3].recipe[2] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }", "source_amount":
    0.1, "source_unit": "g", "provider_g_l": 0.1, "provider_declared_volume_ml": 1000},
    {"field_path": "ingredients[25].concentration", "decision": "correct", "stage":
    "Trace element solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "CoCl2 x 6 H2O 0.03 g", "source_locator": "DSMZ 1647; modified
    Trace element solution; exact CoCl2 x 6 H2O entry", "explanation": "This amount
    belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into
    the main recipe. The local G_PER_L is stock strength incorrectly placed among
    direct medium ingredients. Amount times 1/1000 is the transferred mass; division
    by actual final medium volume requires a supported volume basis. Preserve exact
    supplied form and original mg/g unit.", "owner_decision": "correct", "local_value":
    {"value": "0.03", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[3].recipe[3] (solution_id 5770)", "provider_quote":
    "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\":
    0.03,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.03,\n                        \"mmol_l\": 0.231055,\n                        \"optional\":
    0\n                    }", "source_amount": 0.03, "source_unit": "g", "provider_g_l":
    0.03, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[4].concentration",
    "decision": "correct", "stage": "Trace element solution", "source_reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256":
    "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote":
    "CaCl2 x 2 H2O 0.10 g", "source_locator": "DSMZ 1647; modified Trace element solution;
    exact CaCl2 x 2 H2O entry", "explanation": "This amount belongs to a separately
    prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local
    G_PER_L is stock strength incorrectly placed among direct medium ingredients.
    Amount times 1/1000 is the transferred mass; division by actual final medium volume
    requires a supported volume basis. Preserve exact supplied form and original mg/g
    unit.", "owner_decision": "correct", "local_value": {"value": "0.25", "unit":
    "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[3].recipe[4] (solution_id 5770)", "provider_quote":
    "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\":
    0.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\":
    0\n                    }", "source_amount": 0.1, "source_unit": "g", "provider_g_l":
    0.1, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[26].concentration",
    "decision": "correct", "stage": "Trace element solution", "source_reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256":
    "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote":
    "ZnCl2 0.10 g", "source_locator": "DSMZ 1647; modified Trace element solution;
    exact ZnCl2 entry", "explanation": "This amount belongs to a separately prepared
    1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L
    is stock strength incorrectly placed among direct medium ingredients. Amount times
    1/1000 is the transferred mass; division by actual final medium volume requires
    a supported volume basis. Preserve exact supplied form and original mg/g unit.",
    "owner_decision": "correct", "local_value": {"value": "0.1", "unit": "G_PER_L"},
    "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256":
    "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator":
    "$.data.solutions[3].recipe[5] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.733676,\n                        \"optional\": 0\n                    }", "source_amount":
    0.1, "source_unit": "g", "provider_g_l": 0.1, "provider_declared_volume_ml": 1000},
    {"field_path": "ingredients[27].concentration", "decision": "correct", "stage":
    "Trace element solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "CuCl2 0.02 g", "source_locator": "DSMZ 1647; modified Trace element
    solution; exact CuCl2 entry", "explanation": "This amount belongs to a separately
    prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local
    G_PER_L is stock strength incorrectly placed among direct medium ingredients.
    Amount times 1/1000 is the transferred mass; division by actual final medium volume
    requires a supported volume basis. Preserve exact supplied form and original mg/g
    unit.", "owner_decision": "correct", "local_value": {"value": "0.02", "unit":
    "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[3].recipe[6] (solution_id 5770)", "provider_quote":
    "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"CuCl2\",\n                        \"compound_id\": 261,\n                        \"amount\":
    0.02,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.148754,\n                        \"optional\":
    0\n                    }", "source_amount": 0.02, "source_unit": "g", "provider_g_l":
    0.02, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[28].concentration",
    "decision": "correct", "stage": "Trace element solution", "source_reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256":
    "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote":
    "H3BO3 0.01 g", "source_locator": "DSMZ 1647; modified Trace element solution;
    exact H3BO3 entry", "explanation": "This amount belongs to a separately prepared
    1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local G_PER_L
    is stock strength incorrectly placed among direct medium ingredients. Amount times
    1/1000 is the transferred mass; division by actual final medium volume requires
    a supported volume basis. Preserve exact supplied form and original mg/g unit.",
    "owner_decision": "correct", "local_value": {"value": "0.01", "unit": "G_PER_L"},
    "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256":
    "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator":
    "$.data.solutions[3].recipe[7] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.161708,\n                        \"optional\": 0\n                    }", "source_amount":
    0.01, "source_unit": "g", "provider_g_l": 0.01, "provider_declared_volume_ml":
    1000}, {"field_path": "ingredients[29].concentration", "decision": "correct",
    "stage": "Trace element solution", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Na2MoO4 x 2 H2O 0.03 g", "source_locator": "DSMZ 1647; modified
    Trace element solution; exact Na2MoO4 x 2 H2O entry", "explanation": "This amount
    belongs to a separately prepared 1000 ml stock, subsequently dosed at 1 ml into
    the main recipe. The local G_PER_L is stock strength incorrectly placed among
    direct medium ingredients. Amount times 1/1000 is the transferred mass; division
    by actual final medium volume requires a supported volume basis. Preserve exact
    supplied form and original mg/g unit.", "owner_decision": "correct", "local_value":
    {"value": "0.03", "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[3].recipe[8] (solution_id 5770)", "provider_quote":
    "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    0.03,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.03,\n                        \"mmol_l\": 0.123993,\n                        \"optional\":
    0\n                    }", "source_amount": 0.03, "source_unit": "g", "provider_g_l":
    0.03, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[30].concentration",
    "decision": "correct", "stage": "Trace element solution", "source_reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf", "source_sha256":
    "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad", "source_quote":
    "NiCl2 x 6 H2O 0.10 g", "source_locator": "DSMZ 1647; modified Trace element solution;
    exact NiCl2 x 6 H2O entry", "explanation": "This amount belongs to a separately
    prepared 1000 ml stock, subsequently dosed at 1 ml into the main recipe. The local
    G_PER_L is stock strength incorrectly placed among direct medium ingredients.
    Amount times 1/1000 is the transferred mass; division by actual final medium volume
    requires a supported volume basis. Preserve exact supplied form and original mg/g
    unit.", "owner_decision": "correct", "local_value": {"value": "0.1", "unit": "G_PER_L"},
    "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256":
    "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8", "provider_locator":
    "$.data.solutions[3].recipe[9] (solution_id 5770)", "provider_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.771611,\n                        \"optional\": 0\n                    }", "source_amount":
    0.1, "source_unit": "g", "provider_g_l": 0.1, "provider_declared_volume_ml": 1000},
    {"field_path": "ingredients[31].concentration", "decision": "conflict", "stage":
    "Trace element solution", "source_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "source_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[3].recipe[10] (solution_id
    5770)", "explanation": "This provider trace-stock salt and amount occur in current
    DSMZ 318, but are absent from the complete modified trace table in DSMZ 1647.
    The reference to 318 is explicitly for preparation. Preserve the source-version
    conflict and do not silently promote this extra stock constituent into the 1647
    main recipe.", "owner_decision": "conflict", "local_value": {"value": "1", "unit":
    "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[3].recipe[10] (solution_id 5770)", "provider_quote":
    "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\":
    0\n                    }", "source_amount": 1, "source_unit": "g", "provider_g_l":
    1, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[32].concentration",
    "decision": "conflict", "stage": "Trace element solution", "source_reference":
    "https://mediadive.dsmz.de/rest/medium/1647", "source_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\":
    \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\":
    0.03,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.03,\n                        \"mmol_l\": 0.114062,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[3].recipe[11] (solution_id
    5770)", "explanation": "This provider trace-stock salt and amount occur in current
    DSMZ 318, but are absent from the complete modified trace table in DSMZ 1647.
    The reference to 318 is explicitly for preparation. Preserve the source-version
    conflict and do not silently promote this extra stock constituent into the 1647
    main recipe.", "owner_decision": "conflict", "local_value": {"value": "0.03",
    "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[3].recipe[11] (solution_id 5770)", "provider_quote":
    "{\n                        \"recipe_order\": 12,\n                        \"compound\":
    \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\":
    0.03,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.03,\n                        \"mmol_l\": 0.114062,\n                        \"optional\":
    0\n                    }", "source_amount": 0.03, "source_unit": "g", "provider_g_l":
    0.03, "provider_declared_volume_ml": 1000}, {"field_path": "ingredients[33].concentration",
    "decision": "conflict", "stage": "Trace element solution", "source_reference":
    "https://mediadive.dsmz.de/rest/medium/1647", "source_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\":
    \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\":
    0.04,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.04,\n                        \"mmol_l\": 0.121267,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[3].recipe[12] (solution_id
    5770)", "explanation": "This provider trace-stock salt and amount occur in current
    DSMZ 318, but are absent from the complete modified trace table in DSMZ 1647.
    The reference to 318 is explicitly for preparation. Preserve the source-version
    conflict and do not silently promote this extra stock constituent into the 1647
    main recipe.", "owner_decision": "conflict", "local_value": {"value": "0.04",
    "unit": "G_PER_L"}, "provider_reference": "https://mediadive.dsmz.de/rest/medium/1647",
    "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[3].recipe[12] (solution_id 5770)", "provider_quote":
    "{\n                        \"recipe_order\": 13,\n                        \"compound\":
    \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\":
    0.04,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.04,\n                        \"mmol_l\": 0.121267,\n                        \"optional\":
    0\n                    }", "source_amount": 0.04, "source_unit": "g", "provider_g_l":
    0.04, "provider_declared_volume_ml": 1000}, {"field_path": "preparation_steps
    (missing scoped solvent)", "decision": "add", "stage": "Trace element solution",
    "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "Distilled water 1000.00 ml", "source_locator": "DSMZ 1647; modified
    Trace element solution; exact Distilled water entry", "explanation": "Retain the
    separate stock solvent quantity of 1000 ml. This is not another direct main-medium
    water addition.", "owner_decision": "add", "local_value": null, "provider_reference":
    "https://mediadive.dsmz.de/rest/medium/1647", "provider_sha256": "dc7039fc8af317273b4fd793c5bce7e5c927a8dca93738bcc310fda3050769a8",
    "provider_locator": "$.data.solutions[3].recipe[13] (solution_id 5770)", "provider_quote":
    "{\n                        \"recipe_order\": 14,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_amount": 1000, "source_unit": "ml", "provider_g_l":
    null, "provider_declared_volume_ml": 1000}, {"field_path": "preparation_steps[0]",
    "decision": "evidence_only", "stage": "main sterilization and subsequent additions",
    "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1647.pdf",
    "source_sha256": "8271c7a1e5956b1f4b8a3cece29ee18741ebcedf18570c97db829c1892ce36ad",
    "source_quote": "NaHCO3 are added after the medium has been autoclaved.", "source_locator":
    "Named preparation sentence at the stated stage", "explanation": "The complete
    preceding sentence names vitamins, trace, Se/W, cysteine, glucose, sulfide and
    bicarbonate. The sequence is retained, but claim evidence is absent; no autoclave
    temperature or duration is specified.", "owner_decision": "evidence_only"}, {"field_path":
    "preparation_steps[2]", "decision": "correct", "stage": "trace stock initial dissolution",
    "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318.pdf",
    "source_sha256": "8ca3cb45479ba00e11f9574bf3b315e365e9c98c92bbc5323d4cd5dc4b862f29",
    "source_quote": "First dissolve NTA in 200 ml of distilled water and adjust pH
    to 6.5 with KOH, then dissolve", "source_locator": "Named preparation sentence
    at the stated stage", "explanation": "The 200 ml and initial pH 6.5 belong exclusively
    to trace-stock preparation, not the main medium. Retain the existing literal values
    while restoring their stock scope.", "owner_decision": "correct"}, {"field_path":
    "preparation_steps[2]", "decision": "correct", "stage": "trace stock final make-up",
    "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318.pdf",
    "source_sha256": "8ca3cb45479ba00e11f9574bf3b315e365e9c98c92bbc5323d4cd5dc4b862f29",
    "source_quote": "mineral salts. Finally adjust pH to 6.5 with KOH and make up
    to 1000.00 ml.", "source_locator": "Named preparation sentence at the stated stage",
    "explanation": "Final stock pH 6.5 and 1000 ml volume are retained but flattened
    into main preparation. They do not establish main-medium pH.", "owner_decision":
    "correct"}, {"field_path": "solutions (trace KOH adjustment)", "decision": "not_quantified",
    "stage": "trace stock titration", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318.pdf",
    "source_sha256": "8ca3cb45479ba00e11f9574bf3b315e365e9c98c92bbc5323d4cd5dc4b862f29",
    "source_quote": "adjust pH to 6.5 with KOH", "source_locator": "Named preparation
    sentence at the stated stage", "explanation": "Neither KOH amount nor stock strength
    is specified; do not invent either.", "owner_decision": "not_quantified"}, {"field_path":
    "solutions (vitamin preparation)", "decision": "add", "stage": "vitamin stock
    only", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
    "source_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
    "source_quote": "Vitamins are prepared under 100% N2 gas\natmosphere and sterilized
    by filtration.", "source_locator": "Named preparation sentence at the stated stage",
    "explanation": "Resolve the explicit preparation cross-reference with its named
    vitamin instruction: 100% nitrogen and filtration. Do not import 141 basal gases,
    pH, pressure, or different vitamin composition.", "owner_decision": "add"}]'
- assessment_id: identity
  area: identity
  topic: Exact source and one maintained owner
  outcome: supported
  summary: CultureMech:001130 and media_term mediadive.medium:1647 resolve to the
    exact primary and provider title. The single normalized contributor has the same
    ingredients/preparation as the target; generated provenance adds the August merge
    event. No KG match, internal solution ID, paper citation or asserted organism-growth
    claim occurs in the complete target.
  target_ids:
  - CultureMech:001130
  evidence_ids:
  - record
  - owner-0
  - primary
  - api
  - id-search
- assessment_id: formulation
  area: consistency
  topic: Main recipe, stocks and conflicts
  outcome: concern
  summary: Local 34 direct ingredients replace 10 main solutes and three separately
    dosed stocks. The primary trace table has ten solutes, while provider stock 5770
    adds NaCl, sodium selenite pentahydrate and sodium tungstate dihydrate. Main calcium
    and trace calcium are wrongly summed. The exact source ammonium volume is unresolved
    as mass.
  target_ids:
  - CultureMech:001130
  evidence_ids:
  - record
  - owner-0
  - primary
  - api
  - trace-prep
  - quantities
- assessment_id: forms
  area: grounding
  topic: Supplied hydrates and source specificity
  outcome: concern
  summary: Nickel chloride hexahydrate is linked to CHEBI:34887, whose formula Cl2Ni
    lacks water. Other inspected asserted salt/hydrate forms match their source labels;
    the dihydrate thiamine term is positively supported by 1647, and D-calcium pantothenate
    is explicit. Neutral resazurin and the anhydrous Se/W salts are stated by the
    primary. The provider specifically says L-cysteine while the primary does not
    specify stereochemistry; retain that attribution without inventing a primary L
    claim.
  target_ids:
  - CultureMech:001130
  evidence_ids:
  - record
  - owner-0
  - primary
  - api
  - chebi34887
  - chebi132751
  - chebi31345
  - chebi8806
  - mim
- assessment_id: preparation
  area: completeness
  topic: Source preparation scope
  outcome: concern
  summary: Post-autoclave additions are retained. Trace 200 ml/pH 6.5/1000 ml instructions
    are present but unscoped. Vitamin preparation is only an unresolved textual reference,
    despite a named nitrogen/filtration instruction in the referenced source. Main
    pH, incubation temperature/time, autoclave settings and stock strengths not supplied
    by 1647 are not inferred.
  target_ids:
  - CultureMech:001130
  evidence_ids:
  - record
  - owner-0
  - primary
  - trace-prep
  - vit-prep
  - quantities
- assessment_id: classification
  area: scope
  topic: Mixture classification and biological scope
  outcome: supported
  summary: COMPLEX with SEMI_DEFINED composition is consistent with yeast extract
    plus specified salts/vitamins; LIQUID is consistent with the no-solidifier recipe.
    Microbial cultivation is a generic application, not strain-specific experimental
    evidence. No taxon, optimal condition or organism-growth assertion is inferred
    from the title or adjacent cross-referenced media.
  target_ids:
  - CultureMech:001130
  evidence_ids:
  - record
  - owner-0
  - primary
- assessment_id: provenance
  area: provenance
  topic: Evidence, history and maintained-input ownership
  outcome: concern
  summary: All ingredient evidence is absent in both local layers, notwithstanding
    the resolvable source URL. All observed history timestamps are timezone-aware;
    the March duplicate-merge note supports the observed calcium sum but does not
    identify a replayed implementation. Maintain the normalized source and regenerate
    only after stage/source reconciliation.
  target_ids:
  - CultureMech:001130
  evidence_ids:
  - record
  - owner-0
  - writer
  - primary
  - api
  - quantities
findings:
- finding_id: f1
  issue_key: CM001130-stock-flattening
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Three stock formulations are encoded as main-medium ingredients
  description: All stock solutes are represented at their stock strengths among direct
    ingredients, with no three 1 ml additions. Calcium 0.25 g/L adds distinct 0.15
    g main and 0.10 g stock stages. The representation denotes a different formulation.
  target_ids:
  - CultureMech:001130
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - api
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacteroides_medium.yaml
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
  issue_key: CM001130-ammonium-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Ammonium mass concentration lacks a valid conversion
  description: The visually confirmed primary and provider amount are 0.54 ml. Stored
    0.824796 g/L copies provider g_l without a specified stock strength or density;
    0.54 g is also unsupported.
  target_ids:
  - CultureMech:001130
  field_paths:
  - ingredients[5].concentration
  evidence_ids:
  - record
  - owner-0
  - primary
  - api
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacteroides_medium.yaml
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
  issue_key: CM001130-trace-version
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Provider trace composition differs from the modified primary stock
  description: The provider includes three additional salts absent from the complete
    modified 1647 trace table. A preparation-only cross-reference to current 318 does
    not establish composition equivalence.
  target_ids:
  - CultureMech:001130
  field_paths:
  - ingredients[31]
  - ingredients[32]
  - ingredients[33]
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - api
  - trace-prep
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacteroides_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: CM001130-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is linked to anhydrous nickel dichloride
  description: The supplied source material is NiCl2 x 6 H2O; CHEBI:34887 encodes
    Cl2Ni. Exact canonical labeling does not validate the hydrate.
  target_ids:
  - CultureMech:001130
  field_paths:
  - ingredients[30].term
  - ingredients[30].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - primary
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacteroides_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: CM001130-stock-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Stock preparation stages are incomplete or flattened
  description: Trace pH and solvent instructions appear in main preparation; vitamin
    preparation is a bare reference and omits the named stock nitrogen/filtration
    context.
  target_ids:
  - CultureMech:001130
  field_paths:
  - preparation_steps
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - trace-prep
  - vit-prep
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacteroides_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: CM001130-quantity-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Even source-consistent quantities lack attached claim evidence
  description: The source link alone does not attach literal snippets, original units,
    stock stages or volume basis to individual local quantities. No quantity is currently
    verified under the native evidence definition.
  target_ids:
  - CultureMech:001130
  field_paths:
  - ingredients[*].evidence
  - references
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - primary
  - api
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacteroides_medium.yaml
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
  description: Restore separate main/trace/vitamin/Se-W formulations and source doses;
    reconcile calcium by stage before any final-volume calculation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001130
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacteroides_medium.yaml
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
  description: Retain the exact ml claim and unresolved conversion until exact source
    evidence supplies the missing basis; do not guess a mass.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001130
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacteroides_medium.yaml
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
  description: Preserve the explicit primary/provider conflict and establish the intended
    exact formulation/version before retaining or removing the extra salts.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001130
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacteroides_medium.yaml
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
  description: Resolve the stated hydrate using verified evidence, or explicitly leave
    the exact form unresolved; preserve any secondary linkage only if its pinned identity
    also matches.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001130
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacteroides_medium.yaml
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
  description: Scope all stock instructions to their exact stock, resolve the vitamin
    preparation-only reference, and keep unrelated referenced basal recipes and variants
    excluded.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:001130
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacteroides_medium.yaml
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
  description: Attach exact claim-level source evidence while preserving source version,
    original units and unresolved conflicts; retain append-only history.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:001130
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacteroides_medium.yaml
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
- The inspected DSMZ 1647 PDF prints NH4Cl 0.54 ml, confirmed visually on page 1.
  Its strength or density is unspecified; no mass replacement is inferred.
- Current DSMZ 318 and 141 are used only for the preparations explicitly cross-referenced
  by DSMZ 1647. Their complete basal recipes, organism-specific variants and different
  stock compositions do not replace the exact 1647 tables. Source chronology or intent
  is not inferred from copyright years.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-016
- generated-medium
```
