# Source and formulation review: acetomicrobium_faecale_medium (CultureMech:007645)

- Review: 20261021T103231Z-culturemech-007645-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T10:23:12Z
- Finished UTC: 2026-10-21T10:32:31Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated M1124/JCM 1057 record predates a substantial evidence-backed owner repair: it retains wrong water/stock units, a resazurin mg-to-g error, flattened trace constituents and missing nested composition/preparation. The owner now preserves source batch quantities and nested mineral stocks, but its vitamin stock remains empty and two hydrate mappings remain wrong. The review distinguishes verified owner claims from the stale generated target.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 155; batch 016 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding fifteen task batches contain 150 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 152 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007645 | data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml | generated | acetomicrobium_faecale_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007645 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007645 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-016/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch016/155/strict.tsv |
| validate-terms | passed | True | CultureMech:007645 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007645 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007645 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007645.

The four documented recipes completed; interpret the scope of each separately.

### Exact primary labels and current secondary linkage coverage

grounding: supported. Targets: CultureMech:007645.

16 unique asserted CHEBI identifiers resolve with exact labels. Primary linkage 16/18 (88.89%); verified current secondary linkage 8/18 (44.44%). This is a 0–100 ingredient-instance linkage scale, not scientific correctness. Missing current secondary keys: []. Legacy links and chemical-form correctness are assessed separately.

### Full history and timezone audit

provenance: supported. Targets: CultureMech:007645.

History event counts: [('target', 14), ('data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml', 14)]. Explicit timestamp defects: []. Historical bytes are assessed as observed; no inferred timezone or retroactive replacement timestamp is supplied.

### Every direct, stock, stock-addition and preparation quantity

quantity: concern. Targets: CultureMech:007645.

Fifty-five exact-source decisions cover all 23 M1124 items, fourteen nested M142 trace items, eleven M190 vitamin items and seven preparation claims. Owner batch quantities/evidence are separately verified; the stale generated target is never marked verified by inheritance. Gas and KOH quantities remain explicitly unquantified.

[{"field_path": "ingredients[0].concentration", "decision": "correct", "stage": "main batch before later bicarbonate/cysteine additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "Distilled water 1.0 L", "source_locator": "JCM 1057 main table; exact Distilled water 1.0 L", "explanation": "Source 1.0 L water is correctly represented in the owner with exact evidence and batch basis; target 1 G_PER_L is a dimensional error, not an equivalent solvent quantity.", "source_amount": 1, "source_unit": "L", "owner_field_path": "ingredients[0].concentration", "owner_decision": "verified", "owner_existing_value": {"value": "1", "unit": "L"}, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[0].items[0]", "provider_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\""}, {"field_path": "ingredients[1].concentration", "decision": "correct", "stage": "main batch before later bicarbonate/cysteine additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "MgSO 4 ·7H 2 O 0.1 g", "source_locator": "JCM 1057 main table; exact MgSO 4 ·7H 2 O 0.1 g", "explanation": "The target still asserts an unsupported final-medium concentration. The owner preserves this exact original amount and unit as an evidence-backed batch claim, withdrawing unsupported g/L. Its verified batch claim does not certify the target.", "source_amount": 0.1, "source_unit": "g", "owner_field_path": "ingredients[1].notes", "owner_decision": "verified", "owner_existing_value": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[0].items[1]", "provider_quote": "{\n          \"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\""}, {"field_path": "ingredients[2].concentration", "decision": "correct", "stage": "main batch before later bicarbonate/cysteine additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "Yeast extract 2.0 g", "source_locator": "JCM 1057 main table; exact Yeast extract 2.0 g", "explanation": "The target still asserts an unsupported final-medium concentration. The owner preserves this exact original amount and unit as an evidence-backed batch claim, withdrawing unsupported g/L. Its verified batch claim does not certify the target.", "source_amount": 2, "source_unit": "g", "owner_field_path": "ingredients[2].notes", "owner_decision": "verified", "owner_existing_value": "Role: Nutrient source; Properties: Undefined component\n\nSource batch input: 2 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[0].items[2]", "provider_quote": "{\n          \"component_name\": \"Yeast extract\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\""}, {"field_path": "ingredients[3].concentration", "decision": "correct", "stage": "main batch before later bicarbonate/cysteine additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "NaCl 0.5 g", "source_locator": "JCM 1057 main table; exact NaCl 0.5 g", "explanation": "The target still asserts an unsupported final-medium concentration. The owner preserves this exact original amount and unit as an evidence-backed batch claim, withdrawing unsupported g/L. Its verified batch claim does not certify the target.", "source_amount": 0.5, "source_unit": "g", "owner_field_path": "ingredients[3].notes", "owner_decision": "verified", "owner_existing_value": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[0].items[3]", "provider_quote": "{\n          \"component_name\": \"NaCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\""}, {"field_path": "ingredients[4].concentration", "decision": "correct", "stage": "main batch before later bicarbonate/cysteine additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "CaCl 2 ·2H 2 O 0.07 g", "source_locator": "JCM 1057 main table; exact CaCl 2 ·2H 2 O 0.07 g", "explanation": "The target still asserts an unsupported final-medium concentration. The owner preserves this exact original amount and unit as an evidence-backed batch claim, withdrawing unsupported g/L. Its verified batch claim does not certify the target.", "source_amount": 0.07, "source_unit": "g", "owner_field_path": "ingredients[4].notes", "owner_decision": "verified", "owner_existing_value": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.07 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[0].items[4]", "provider_quote": "{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.07,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\""}, {"field_path": "ingredients[5].concentration", "decision": "correct", "stage": "main batch before later bicarbonate/cysteine additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "KH 2 PO 4 0.225 g", "source_locator": "JCM 1057 main table; exact KH 2 PO 4 0.225 g", "explanation": "The target still asserts an unsupported final-medium concentration. The owner preserves this exact original amount and unit as an evidence-backed batch claim, withdrawing unsupported g/L. Its verified batch claim does not certify the target.", "source_amount": 0.225, "source_unit": "g", "owner_field_path": "ingredients[5].notes", "owner_decision": "verified", "owner_existing_value": "Role: Buffer; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.225 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[0].items[5]", "provider_quote": "{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.225,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\""}, {"field_path": "ingredients[6].concentration", "decision": "correct", "stage": "main batch before later bicarbonate/cysteine additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "K 2 HPO 4 0.255 g", "source_locator": "JCM 1057 main table; exact K 2 HPO 4 0.255 g", "explanation": "The target still asserts an unsupported final-medium concentration. The owner preserves this exact original amount and unit as an evidence-backed batch claim, withdrawing unsupported g/L. Its verified batch claim does not certify the target.", "source_amount": 0.255, "source_unit": "g", "owner_field_path": "ingredients[6].notes", "owner_decision": "verified", "owner_existing_value": "Role: Buffer; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.255 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[0].items[6]", "provider_quote": "{\n          \"component_name\": \"K2HPO4\",\n          \"volume\": 0.255,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001009\""}, {"field_path": "ingredients[7].concentration", "decision": "correct", "stage": "main batch before later bicarbonate/cysteine additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "Resazurin 1.0 mg", "source_locator": "JCM 1057 main table; exact Resazurin 1.0 mg", "explanation": "Source 1 mg equals 0.001 g for the batch, not target 1 g/L. The owner correctly preserves 1 mg in an evidence-backed batch note without inventing final volume.", "source_amount": 1, "source_unit": "mg", "owner_field_path": "ingredients[7].notes", "owner_decision": "verified", "owner_existing_value": "Role: pH dependent redox indicator; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[0].items[7]", "provider_quote": "{\n          \"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001012\""}, {"field_path": "ingredients[8].concentration", "decision": "correct", "stage": "main batch before later bicarbonate/cysteine additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "(NH 4 ) 2 SO 4 0.255 g", "source_locator": "JCM 1057 main table; exact (NH 4 ) 2 SO 4 0.255 g", "explanation": "The target still asserts an unsupported final-medium concentration. The owner preserves this exact original amount and unit as an evidence-backed batch claim, withdrawing unsupported g/L. Its verified batch claim does not certify the target.", "source_amount": 0.255, "source_unit": "g", "owner_field_path": "ingredients[8].notes", "owner_decision": "verified", "owner_existing_value": "Role: Nitrogen source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.255 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[0].items[8]", "provider_quote": "{\n          \"component_name\": \"(NH4)2SO4\",\n          \"volume\": 0.255,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001030\""}, {"field_path": "ingredients[9].concentration", "decision": "correct", "stage": "main batch before later bicarbonate/cysteine additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "Sodium acetate·3H 2 O 5.0 g", "source_locator": "JCM 1057 main table; exact Sodium acetate·3H 2 O 5.0 g", "explanation": "The target still asserts an unsupported final-medium concentration. The owner preserves this exact original amount and unit as an evidence-backed batch claim, withdrawing unsupported g/L. Its verified batch claim does not certify the target.", "source_amount": 5, "source_unit": "g", "owner_field_path": "ingredients[9].notes", "owner_decision": "verified", "owner_existing_value": "Role: Buffer; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[0].items[9]", "provider_quote": "{\n          \"component_name\": \"Sodium acetate・3H2O\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001396\""}, {"field_path": "ingredients[10].concentration", "decision": "correct", "stage": "main batch before later bicarbonate/cysteine additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "Glucose 4.0 g", "source_locator": "JCM 1057 main table; exact Glucose 4.0 g", "explanation": "The target still asserts an unsupported final-medium concentration. The owner preserves this exact original amount and unit as an evidence-backed batch claim, withdrawing unsupported g/L. Its verified batch claim does not certify the target.", "source_amount": 4, "source_unit": "g", "owner_field_path": "ingredients[10].notes", "owner_decision": "verified", "owner_existing_value": "Role: Carbon source; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 4 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[0].items[10]", "provider_quote": "{\n          \"component_name\": \"Glucose\",\n          \"volume\": 4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001815\""}, {"field_path": "ingredients[11].concentration", "decision": "correct", "stage": "main batch before later bicarbonate/cysteine additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "Trypticase peptone (BD-BBL) 2.0 g", "source_locator": "JCM 1057 main table; exact Trypticase peptone (BD-BBL) 2.0 g", "explanation": "The target still asserts an unsupported final-medium concentration. The owner preserves this exact original amount and unit as an evidence-backed batch claim, withdrawing unsupported g/L. Its verified batch claim does not certify the target.", "source_amount": 2, "source_unit": "g", "owner_field_path": "ingredients[11].notes", "owner_decision": "verified", "owner_existing_value": "Properties: Undefined component\n\nSource batch input: 2 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[0].items[11]", "provider_quote": "{\n          \"component_name\": \"Trypticase peptone (BD-BBL)\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001097\""}, {"field_path": "solutions[0].concentration", "decision": "correct", "stage": "main batch before later bicarbonate/cysteine additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "Trace vitamins (see Medium No. 197 ) 10.0 ml", "source_locator": "JCM 1057 main table; exact Trace vitamins (see Medium No. 197 ) 10.0 ml", "explanation": "Source 10 ml equals 0.01 L per receiving batch. The owner has that exact dose with field-specific root evidence; target 10 G_PER_L has the wrong physical dimension. Keep vitamin and custom-mineral formulations separate.", "source_amount": 10, "source_unit": "ml", "owner_field_path": "solutions[0].concentration", "owner_decision": "verified", "owner_existing_value": {"value": "0.01", "unit": "L"}, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[0].items[12]", "provider_quote": "{\n          \"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\""}, {"field_path": "solutions[1].concentration", "decision": "correct", "stage": "main batch before later bicarbonate/cysteine additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "Trace minerals solution (see below) 10.0 ml", "source_locator": "JCM 1057 main table; exact Trace minerals solution (see below) 10.0 ml", "explanation": "Source 10 ml equals 0.01 L per receiving batch. The owner has that exact dose with field-specific root evidence; target 10 G_PER_L has the wrong physical dimension. Keep vitamin and custom-mineral formulations separate.", "source_amount": 10, "source_unit": "ml", "owner_field_path": "solutions[1].concentration", "owner_decision": "verified", "owner_existing_value": {"value": "0.01", "unit": "L"}, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[0].items[13]", "provider_quote": "{\n          \"component_name\": \"Trace minerals solution (see below)\",\n          \"volume\": 10,\n          \"unit\": \"ml\""}, {"field_path": "ingredients[12].concentration", "decision": "not_quantified", "stage": "main source section 0; gas context", "source_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "source_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "source_quote": "{\n          \"component_name\": \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\"", "source_locator": "$.components[0].items[14]", "explanation": "The source item has no fixed gas volume, flow or dissolved concentration. The legacy VARIABLE placeholder is not a verified concentration. Separate preparation decisions retain the explicit mixture ratio and bottle pressure; repeated mentions do not authorize summing gas doses.", "owner_field_path": "ingredients[12].concentration", "owner_decision": "not_quantified"}, {"field_path": "ingredients[13].concentration", "decision": "not_quantified", "stage": "main source section 0; gas context", "source_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "source_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "source_quote": "{\n          \"component_name\": \"Nitrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\"", "source_locator": "$.components[0].items[15]", "explanation": "The source item has no fixed gas volume, flow or dissolved concentration. The legacy VARIABLE placeholder is not a verified concentration. Separate preparation decisions retain the explicit mixture ratio and bottle pressure; repeated mentions do not authorize summing gas doses.", "owner_field_path": "ingredients[13].concentration", "owner_decision": "not_quantified"}, {"field_path": "ingredients[12].concentration", "decision": "not_quantified", "stage": "main source section 1; gas context", "source_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "source_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "source_quote": "{\n          \"component_name\": \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\"", "source_locator": "$.components[1].items[2]", "explanation": "The source item has no fixed gas volume, flow or dissolved concentration. The legacy VARIABLE placeholder is not a verified concentration. Separate preparation decisions retain the explicit mixture ratio and bottle pressure; repeated mentions do not authorize summing gas doses.", "owner_field_path": "ingredients[12].concentration", "owner_decision": "not_quantified"}, {"field_path": "ingredients[13].concentration", "decision": "not_quantified", "stage": "main source section 1; gas context", "source_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "source_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "source_quote": "{\n          \"component_name\": \"Nitrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\"", "source_locator": "$.components[1].items[3]", "explanation": "The source item has no fixed gas volume, flow or dissolved concentration. The legacy VARIABLE placeholder is not a verified concentration. Separate preparation decisions retain the explicit mixture ratio and bottle pressure; repeated mentions do not authorize summing gas doses.", "owner_field_path": "ingredients[13].concentration", "owner_decision": "not_quantified"}, {"field_path": "ingredients[14].concentration", "decision": "correct", "stage": "post-boiling main additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "NaHCO 3 6.0 g", "source_locator": "JCM 1057 second table, following boiling/cooling", "explanation": "Target g/L assumes final volume. The owner correctly keeps this exact batch mass with attached evidence in notes, after boiling/cooling and before sealing/autoclaving.", "source_amount": 6, "source_unit": "g", "owner_field_path": "ingredients[14].notes", "owner_decision": "verified", "owner_existing_value": "Role: Buffer; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 6 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[1].items[0]", "provider_quote": "{\n          \"component_name\": \"NaHCO3\",\n          \"volume\": 6,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001019\""}, {"field_path": "ingredients[15].concentration", "decision": "correct", "stage": "post-boiling main additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "L-Cysteine·HCl·H 2 O 0.5 g", "source_locator": "JCM 1057 second table, following boiling/cooling", "explanation": "Target g/L assumes final volume. The owner correctly keeps this exact batch mass with attached evidence in notes, after boiling/cooling and before sealing/autoclaving.", "source_amount": 0.5, "source_unit": "g", "owner_field_path": "ingredients[15].notes", "owner_decision": "verified", "owner_existing_value": "Properties: Defined component, Simple component, Organic compound\n\nSource batch input: 0.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[1].items[1]", "provider_quote": "{\n          \"component_name\": \"L--Cysteine・HCl・H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001205\""}, {"field_path": "ingredients[16].concentration", "decision": "correct", "stage": "custom trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "NiCl 2 ·6H 2 O 0.03 g", "source_locator": "JCM 1057 Trace minerals solution subsection; exact NiCl 2 ·6H 2 O 0.03 g", "explanation": "This is a custom trace-stock batch constituent, not a direct main ingredient. The owner has the exact batch quantity and attached evidence in the correct nested scope. The 10 ml custom-stock addition must remain distinct from its 1 L M142 input; actual final volumes are not established.", "source_amount": 0.03, "source_unit": "g", "owner_field_path": "solutions[1].composition[0].notes", "owner_decision": "verified", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[2].items[0]", "provider_quote": "{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 0.03,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\""}, {"field_path": "ingredients[17].concentration", "decision": "correct", "stage": "custom trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "Na 2 SeO 3 ·5H 2 O 0.3 mg", "source_locator": "JCM 1057 Trace minerals solution subsection; exact Na 2 SeO 3 ·5H 2 O 0.3 mg", "explanation": "This is a custom trace-stock batch constituent, not a direct main ingredient. The owner has the exact batch quantity and attached evidence in the correct nested scope. The 10 ml custom-stock addition must remain distinct from its 1 L M142 input; actual final volumes are not established. The source 0.3 mg is 0.0003 g in the stock batch, not target 0.3 g/L.", "source_amount": 0.3, "source_unit": "mg", "owner_field_path": "solutions[1].composition[1].notes", "owner_decision": "verified", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[2].items[1]", "provider_quote": "{\n          \"component_name\": \"Na2SeO3・5H2O\",\n          \"volume\": 0.3,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001046\""}, {"field_path": "solutions[2].concentration", "decision": "correct", "stage": "custom trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "Trace minerals (see Medium No. 151 ) 1.0 L", "source_locator": "JCM 1057 Trace minerals solution subsection; exact Trace minerals (see Medium No. 151 ) 1.0 L", "explanation": "This is a custom trace-stock batch constituent, not a direct main ingredient. The owner has the exact batch quantity and attached evidence in the correct nested scope. The 10 ml custom-stock addition must remain distinct from its 1 L M142 input; actual final volumes are not established.", "source_amount": 1, "source_unit": "L", "owner_field_path": "solutions[1].solutions[0].concentration", "owner_decision": "verified", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator": "$.components[2].items[2]", "provider_quote": "{\n          \"component_name\": \"Trace minerals (see Medium [M142])\",\n          \"volume\": 1,\n          \"unit\": \"L\""}, {"field_path": "solutions[2].composition (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "Distilled water 1.0 L", "source_locator": "JCM 151 Trace minerals subsection; exact Distilled water 1.0 L", "explanation": "The owner already preserves this exact source batch amount and unit with attached evidence. Restore its scope and evidence in derived output. Do not equate stock water with final volume, or replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.", "source_amount": 1, "source_unit": "L", "owner_field_path": "solutions[1].solutions[0].composition[0].concentration", "owner_decision": "verified", "owner_existing_value": {"value": "1", "unit": "L"}, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "provider_locator": "$.components[2].items[0]", "provider_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\""}, {"field_path": "solutions[2].composition (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "MgSO 4 ·7H 2 O 3.0 g", "source_locator": "JCM 151 Trace minerals subsection; exact MgSO 4 ·7H 2 O 3.0 g", "explanation": "The owner already preserves this exact source batch amount and unit with attached evidence. Restore its scope and evidence in derived output. Do not equate stock water with final volume, or replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.", "source_amount": 3, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[1].notes", "owner_decision": "verified", "owner_existing_value": "Source batch input: 3 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "provider_locator": "$.components[2].items[1]", "provider_quote": "{\n          \"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\""}, {"field_path": "solutions[2].composition (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "NaCl 1.0 g", "source_locator": "JCM 151 Trace minerals subsection; exact NaCl 1.0 g", "explanation": "The owner already preserves this exact source batch amount and unit with attached evidence. Restore its scope and evidence in derived output. Do not equate stock water with final volume, or replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.", "source_amount": 1, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[2].notes", "owner_decision": "verified", "owner_existing_value": "Source batch input: 1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "provider_locator": "$.components[2].items[2]", "provider_quote": "{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\""}, {"field_path": "solutions[2].composition (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "CaCl 2 ·2H 2 O 0.1 g", "source_locator": "JCM 151 Trace minerals subsection; exact CaCl 2 ·2H 2 O 0.1 g", "explanation": "The owner already preserves this exact source batch amount and unit with attached evidence. Restore its scope and evidence in derived output. Do not equate stock water with final volume, or replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.", "source_amount": 0.1, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[3].notes", "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "provider_locator": "$.components[2].items[3]", "provider_quote": "{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\""}, {"field_path": "solutions[2].composition (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "Na 2 MoO 4 ·2H 2 O 0.01 g", "source_locator": "JCM 151 Trace minerals subsection; exact Na 2 MoO 4 ·2H 2 O 0.01 g", "explanation": "The owner already preserves this exact source batch amount and unit with attached evidence. Restore its scope and evidence in derived output. Do not equate stock water with final volume, or replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.", "source_amount": 0.01, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[4].notes", "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "provider_locator": "$.components[2].items[4]", "provider_quote": "{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\""}, {"field_path": "solutions[2].composition (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "H 3 BO 3 0.01 g", "source_locator": "JCM 151 Trace minerals subsection; exact H 3 BO 3 0.01 g", "explanation": "The owner already preserves this exact source batch amount and unit with attached evidence. Restore its scope and evidence in derived output. Do not equate stock water with final volume, or replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.", "source_amount": 0.01, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[5].notes", "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "provider_locator": "$.components[2].items[5]", "provider_quote": "{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\""}, {"field_path": "solutions[2].composition (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "FeSO 4 ·7H 2 O 0.1 g", "source_locator": "JCM 151 Trace minerals subsection; exact FeSO 4 ·7H 2 O 0.1 g", "explanation": "The owner already preserves this exact source batch amount and unit with attached evidence. Restore its scope and evidence in derived output. Do not equate stock water with final volume, or replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.", "source_amount": 0.1, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[6].notes", "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "provider_locator": "$.components[2].items[6]", "provider_quote": "{\n          \"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001016\""}, {"field_path": "solutions[2].composition (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "ZnSO 4 ·7H 2 O 0.1 g", "source_locator": "JCM 151 Trace minerals subsection; exact ZnSO 4 ·7H 2 O 0.1 g", "explanation": "The owner already preserves this exact source batch amount and unit with attached evidence. Restore its scope and evidence in derived output. Do not equate stock water with final volume, or replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.", "source_amount": 0.1, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[7].notes", "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "provider_locator": "$.components[2].items[7]", "provider_quote": "{\n          \"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001023\""}, {"field_path": "solutions[2].composition (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "CuSO 4 ·5H 2 O 0.01 g", "source_locator": "JCM 151 Trace minerals subsection; exact CuSO 4 ·5H 2 O 0.01 g", "explanation": "The owner already preserves this exact source batch amount and unit with attached evidence. Restore its scope and evidence in derived output. Do not equate stock water with final volume, or replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.", "source_amount": 0.01, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[8].notes", "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "provider_locator": "$.components[2].items[8]", "provider_quote": "{\n          \"component_name\": \"CuSO4・5H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001039\""}, {"field_path": "solutions[2].composition (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "CoSO 4 ·7H 2 O 0.1 g", "source_locator": "JCM 151 Trace minerals subsection; exact CoSO 4 ·7H 2 O 0.1 g", "explanation": "The owner already preserves this exact source batch amount and unit with attached evidence. Restore its scope and evidence in derived output. Do not equate stock water with final volume, or replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.", "source_amount": 0.1, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[9].notes", "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "provider_locator": "$.components[2].items[9]", "provider_quote": "{\n          \"component_name\": \"CoSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001050\""}, {"field_path": "solutions[2].composition (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "Nitrilotriacetic acid 1.5 g", "source_locator": "JCM 151 Trace minerals subsection; exact Nitrilotriacetic acid 1.5 g", "explanation": "The owner already preserves this exact source batch amount and unit with attached evidence. Restore its scope and evidence in derived output. Do not equate stock water with final volume, or replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.", "source_amount": 1.5, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[10].notes", "owner_decision": "verified", "owner_existing_value": "Source batch input: 1.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "provider_locator": "$.components[2].items[10]", "provider_quote": "{\n          \"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001053\""}, {"field_path": "solutions[2].composition (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "MnSO 4 · x H 2 O 0.5 g", "source_locator": "JCM 151 Trace minerals subsection; exact MnSO 4 · x H 2 O 0.5 g", "explanation": "The owner already preserves this exact source batch amount and unit with attached evidence. Restore its scope and evidence in derived output. Do not equate stock water with final volume, or replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.", "source_amount": 0.5, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[11].notes", "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "provider_locator": "$.components[2].items[11]", "provider_quote": "{\n          \"component_name\": \"MnSO4・xH2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001065\""}, {"field_path": "solutions[2].composition (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "AlK(SO 4 ) 2 0.01 g", "source_locator": "JCM 151 Trace minerals subsection; exact AlK(SO 4 ) 2 0.01 g", "explanation": "The owner already preserves this exact source batch amount and unit with attached evidence. Restore its scope and evidence in derived output. Do not equate stock water with final volume, or replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.", "source_amount": 0.01, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[12].notes", "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "provider_locator": "$.components[2].items[12]", "provider_quote": "{\n          \"component_name\": \"AlK(SO4)2\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001088\""}, {"field_path": "solutions[2].composition (missing KOH context)", "decision": "not_quantified", "stage": "innermost trace-stock titration", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "adjust pH to 6.5 with KOH solution.", "source_locator": "JCM 151 final Trace minerals preparation sentence", "explanation": "KOH amount and strength are unspecified. Owner preserves an empty KOH adjustment node with root evidence; it is intentionally unquantified, unlike the incomplete vitamin stock.", "owner_field_path": "solutions[1].solutions[0].solutions[0]", "owner_decision": "not_quantified", "provider_quote": "{\n          \"component_name\": \"KOH solution\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001903\"", "provider_locator": "$.components[2].items[13]", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"}, {"field_path": "solutions[0].composition (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532", "source_quote": "Distilled water 1.0 L", "source_locator": "JCM 197 Trace vitamins subsection; exact Distilled water 1.0 L", "explanation": "Both target and owner vitamin compositions are empty despite a resolvable exact eleven-row source stock. Add original amounts/units and solvent context with narrow evidence; do not transfer the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving dose is a separate claim.", "source_amount": 1, "source_unit": "L", "owner_field_path": "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "provider_locator": "$.components[1].items[0]", "provider_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\""}, {"field_path": "solutions[0].composition (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532", "source_quote": "Biotin 2.0 mg", "source_locator": "JCM 197 Trace vitamins subsection; exact Biotin 2.0 mg", "explanation": "Both target and owner vitamin compositions are empty despite a resolvable exact eleven-row source stock. Add original amounts/units and solvent context with narrow evidence; do not transfer the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving dose is a separate claim.", "source_amount": 2, "source_unit": "mg", "owner_field_path": "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "provider_locator": "$.components[1].items[1]", "provider_quote": "{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\""}, {"field_path": "solutions[0].composition (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532", "source_quote": "p -Aminobenzoic acid 5.0 mg", "source_locator": "JCM 197 Trace vitamins subsection; exact p -Aminobenzoic acid 5.0 mg", "explanation": "Both target and owner vitamin compositions are empty despite a resolvable exact eleven-row source stock. Add original amounts/units and solvent context with narrow evidence; do not transfer the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving dose is a separate claim.", "source_amount": 5, "source_unit": "mg", "owner_field_path": "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "provider_locator": "$.components[1].items[2]", "provider_quote": "{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\""}, {"field_path": "solutions[0].composition (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532", "source_quote": "Thiamine·HCl 5.0 mg", "source_locator": "JCM 197 Trace vitamins subsection; exact Thiamine·HCl 5.0 mg", "explanation": "Both target and owner vitamin compositions are empty despite a resolvable exact eleven-row source stock. Add original amounts/units and solvent context with narrow evidence; do not transfer the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving dose is a separate claim.", "source_amount": 5, "source_unit": "mg", "owner_field_path": "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "provider_locator": "$.components[1].items[3]", "provider_quote": "{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\""}, {"field_path": "solutions[0].composition (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532", "source_quote": "Calcium pantothenate 5.0 mg", "source_locator": "JCM 197 Trace vitamins subsection; exact Calcium pantothenate 5.0 mg", "explanation": "Both target and owner vitamin compositions are empty despite a resolvable exact eleven-row source stock. Add original amounts/units and solvent context with narrow evidence; do not transfer the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving dose is a separate claim.", "source_amount": 5, "source_unit": "mg", "owner_field_path": "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "provider_locator": "$.components[1].items[4]", "provider_quote": "{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\""}, {"field_path": "solutions[0].composition (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532", "source_quote": "Pyridoxine·HCl 10.0 mg", "source_locator": "JCM 197 Trace vitamins subsection; exact Pyridoxine·HCl 10.0 mg", "explanation": "Both target and owner vitamin compositions are empty despite a resolvable exact eleven-row source stock. Add original amounts/units and solvent context with narrow evidence; do not transfer the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving dose is a separate claim.", "source_amount": 10, "source_unit": "mg", "owner_field_path": "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "provider_locator": "$.components[1].items[5]", "provider_quote": "{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\""}, {"field_path": "solutions[0].composition (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532", "source_quote": "Folic acid 2.0 mg", "source_locator": "JCM 197 Trace vitamins subsection; exact Folic acid 2.0 mg", "explanation": "Both target and owner vitamin compositions are empty despite a resolvable exact eleven-row source stock. Add original amounts/units and solvent context with narrow evidence; do not transfer the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving dose is a separate claim.", "source_amount": 2, "source_unit": "mg", "owner_field_path": "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "provider_locator": "$.components[1].items[6]", "provider_quote": "{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\""}, {"field_path": "solutions[0].composition (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532", "source_quote": "Vitamin B 1 2 0.1 mg", "source_locator": "JCM 197 Trace vitamins subsection; exact Vitamin B 1 2 0.1 mg", "explanation": "Both target and owner vitamin compositions are empty despite a resolvable exact eleven-row source stock. Add original amounts/units and solvent context with narrow evidence; do not transfer the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving dose is a separate claim.", "source_amount": 0.1, "source_unit": "mg", "owner_field_path": "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "provider_locator": "$.components[1].items[7]", "provider_quote": "{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\""}, {"field_path": "solutions[0].composition (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532", "source_quote": "Riboflavin 5.0 mg", "source_locator": "JCM 197 Trace vitamins subsection; exact Riboflavin 5.0 mg", "explanation": "Both target and owner vitamin compositions are empty despite a resolvable exact eleven-row source stock. Add original amounts/units and solvent context with narrow evidence; do not transfer the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving dose is a separate claim.", "source_amount": 5, "source_unit": "mg", "owner_field_path": "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "provider_locator": "$.components[1].items[8]", "provider_quote": "{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\""}, {"field_path": "solutions[0].composition (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532", "source_quote": "Nicotinic acid 5.0 mg", "source_locator": "JCM 197 Trace vitamins subsection; exact Nicotinic acid 5.0 mg", "explanation": "Both target and owner vitamin compositions are empty despite a resolvable exact eleven-row source stock. Add original amounts/units and solvent context with narrow evidence; do not transfer the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving dose is a separate claim.", "source_amount": 5, "source_unit": "mg", "owner_field_path": "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "provider_locator": "$.components[1].items[9]", "provider_quote": "{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\""}, {"field_path": "solutions[0].composition (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532", "source_quote": "Lipoic acid 5.0 mg", "source_locator": "JCM 197 Trace vitamins subsection; exact Lipoic acid 5.0 mg", "explanation": "Both target and owner vitamin compositions are empty despite a resolvable exact eleven-row source stock. Add original amounts/units and solvent context with narrow evidence; do not transfer the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving dose is a separate claim.", "source_amount": 5, "source_unit": "mg", "owner_field_path": "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "provider_locator": "$.components[1].items[10]", "provider_quote": "{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\""}, {"field_path": "preparation_steps (missing)", "decision": "not_quantified", "stage": "main boiling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "Bring to a boil for seconds", "source_locator": "main preparation, before cooling", "explanation": "The source specifies seconds but no numeric duration. The owner retains this wording; do not invent a boil duration.", "owner_field_path": "preparation_steps[0]", "owner_decision": "not_quantified"}, {"field_path": "preparation_steps (missing)", "decision": "add", "stage": "main cooling before bicarbonate/cysteine", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture", "source_locator": "main cooling sentence", "explanation": "Source ratio is 4:1 v/v (80:20), not separate ingredient concentrations. The owner already retains the ratio and matching source excerpt.", "owner_field_path": "preparation_steps[0]", "owner_decision": "verified"}, {"field_path": "preparation_steps (missing)", "decision": "add", "stage": "after inoculation", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "pressurize the inoculated bottles to 200 kPa with a N 2 -CO 2 (4:1, v/v) gas mixture.", "source_locator": "after-inoculation sentence", "explanation": "Both 200 kPa and 4:1 v/v belong to the stated bottle stage. The owner preserves them with exact evidence; gauge versus absolute pressure is not specified and is not invented.", "owner_field_path": "preparation_steps[1]", "owner_decision": "verified"}, {"field_path": "preparation_steps (missing)", "decision": "add", "stage": "main sterilization", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897", "source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.", "source_locator": "page-level default together with recipe-specific autoclave sentence", "explanation": "The exact JCM 1057 page states this default and its main recipe calls for autoclaving without an alternate setting. Neither local layer spells out the numeric settings. Do not apply the default to the separately filter-sterilized vitamin stock.", "owner_field_path": "preparation_steps[1]", "owner_decision": "add"}, {"field_path": "solutions[2].preparation_notes (missing)", "decision": "add", "stage": "innermost trace before mineral additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "adjust pH to 6.5 with KOH solution.", "source_locator": "Trace minerals preparation", "explanation": "The owner already preserves initial stock pH 6.5 and exact root evidence. This is not main-medium pH.", "owner_field_path": "solutions[1].solutions[0].preparation_notes", "owner_decision": "verified"}, {"field_path": "solutions[2].preparation_notes (missing)", "decision": "add", "stage": "innermost trace final adjustment", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7", "source_quote": "Adjust final pH to 7.0.", "source_locator": "Trace minerals preparation final sentence", "explanation": "Final stock pH 7.0 is already correctly retained in the owner with exact evidence. No main pH is inferred.", "owner_field_path": "solutions[1].solutions[0].preparation_notes", "owner_decision": "verified"}, {"field_path": "solutions[0].preparation_notes (missing)", "decision": "add", "stage": "vitamin stock sterilization only", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532", "source_quote": "and Trace vitamins while gassing       with N 2 .", "source_locator": "main paragraph, named trace-vitamin filtration clause", "explanation": "The immediately preceding filter-sterilize instruction explicitly applies to Trace vitamins under nitrogen. No gas fraction, filtration pore size, basal gas mixture or unrelated 8% bicarbonate/5% reagent stock is transferred.", "owner_field_path": "solutions[0].preparation_notes (missing)", "owner_decision": "add"}]

### Exact main and stock identities

identity: supported. Targets: CultureMech:007645.

TOGO M1124 explicitly identifies JCM 1057. Its vitamin reference M190 maps to JCM 197 and its nested mineral reference M142 maps to JCM 151. These are subsection dependencies, not whole-medium equivalences. One maintained owner is explicitly named by the merge history.

### Existing owner evidence and batch representation

evidence: supported. Targets: CultureMech:007645.

The owner has 31 evidence objects, with additional exact excerpts specifying all three stock doses and main/stock preparation. Literal snippets and historical response hashes match current captures. These verify existing owner batch amounts, units and stage explanations; they do not verify removed final g/L or correct chemical grounding. The target has none of this evidence.

### Every direct, inline and nested-stock quantity

consistency: concern. Targets: CultureMech:007645.

Target water, stock doses and resazurin have wrong units; nickel and selenite remain flattened at wrong stages and the latter also carries a mg-to-g error. The owner correctly withdrew unsupported final concentrations, preserving batch mass evidence. Its custom trace and nested M142 composition are restored, while its vitamin composition remains empty. No numeric final medium concentration is inferred from one litre of input water.

### Exact supplied forms and bounded stock identities

grounding: concern. Targets: CultureMech:007645.

Sodium acetate trihydrate maps to CHEBI:32954, formula C2H3NaO2, and nickel chloride hexahydrate maps to CHEBI:34887, formula Cl2Ni. These terms omit the stated hydrate. The owner retained both unresolved groundings during quantity repair. Other asserted direct forms agree with source wording; nested M142 ingredients have no newly invented ontology links. Unspecified manganese hydration, aluminum-potassium sulfate hydration and vitamin pantothenate stereochemistry remain unresolved.

### Main preparation and stock-specific processing

completeness: concern. Targets: CultureMech:007645.

Generated preparation is absent; the owner correctly retains main boiling/cooling, staged additions, bottle pressure and trace-stock pH. Both layers omit the numerical JCM sterilization default and explicit vitamin preparation. The intentionally unquantified KOH node is not a missing fixed formulation. Main pH and incubation duration/temperature are not asserted by these sources and are not inferred.

### Mixture class and biological scope

scope: supported. Targets: CultureMech:007645.

COMPLEX/UNDEFINED and LIQUID are consistent with yeast extract/trypticase and no solidifier. Imported roles and property notes are recognizable provider annotations, not independent experimental mechanisms; no structured target-organism, incubation, KG, or strain-variant claim is made. The title alone does not establish growth.

### Derived-output lag and append-only repair history

provenance: concern. Targets: CultureMech:007645.

The August generated target predates the October RESTORED_NESTED_M142_TRACE_STOCKS_WITH_EVIDENCE owner event. All timestamps are timezone-aware. The full serialized repair changes and source excerpts distinguish corrected units, withheld final concentrations, nested stock restoration and intentionally unresolved gases/grounding. Current merge code is not blamed for an unexecuted regeneration.

## Findings

### f1: Generated recipe retains superseded units and flattened stock stages

blocker / open / confirmed; issue key: CM007645-stale-formulation.

The target stores water as 1 g/L, resazurin as 1 g/L rather than source 1 mg per batch, stock additions as g/L, and nickel/selenite as direct ingredients. Its empty mineral stubs omit the nested composition already repaired with evidence in the owner.

### f2: Resolvable trace-vitamin stock remains empty

major / open / confirmed; issue key: CM007645-vitamin-composition.

Both layers leave the M190/JCM 197 trace-vitamin composition empty despite its exact ten-vitamin and water recipe and the stated 10 ml dose. This differs from the intentionally unquantified KOH adjustment node.

### f3: Two retained ontology terms omit source hydrate identities

major / open / confirmed; issue key: CM007645-hydrate-grounding.

Sodium acetate trihydrate is linked to anhydrous sodium acetate and nickel hexahydrate to anhydrous nickel dichloride. October quantity evidence explicitly did not recertify chemical grounding.

### f4: Preparation and stock processing are incomplete in derived output

major / open / confirmed; issue key: CM007645-preparation-scope.

The generated recipe omits all preparation; the owner preserves main and nested-trace stages but leaves vitamin preparation and the explicit main JCM sterilization default unrepresented.

### f5: Generated output omits the repaired owner evidence and references

minor / open / confirmed; issue key: CM007645-evidence-lineage.

The target has no October source excerpts, narrow stock-dose explanations or appended repair event. The current owner already has verifiable source content; this is derived lag rather than absent owner provenance.

## Recommended Actions And Acceptance Checks

### a1

Preserve the verified owner repair, reconcile remaining issues, then regenerate and confirm exact batch units, nested scopes and evidence survive. Do not reintroduce unsupported final g/L.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore only the named vitamin subsection with its original amounts, forms and dose; give the stock an informative source-supported name. Exclude JCM 197 basal/mineral formulation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Verify exact hydrate representations or leave their grounding explicitly unresolved; preserve supported quantities without substituting anhydrous forms.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Retain verified owner stages, add exact missing stock/default context with source scope, and keep trace pH separate from unspecified main pH. Preserve unquantified gas flow and KOH.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Carry existing source evidence, original timestamps and history through an authorized regeneration after source reconciliation; do not invent historical provenance or rewrite prior events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch016/155/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-016/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch016/155/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml:1:id: CultureMech:007645<br>./data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml:1:id: CultureMech:007645<br> |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:131361 resolves to disodium selenite pentahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["5H2O.2Na.O3Se"], "inchi_string": ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"], "mass": ["263.012"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]} |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["HO4P.2K"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]} |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:15377 resolves to water; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "smiles_string": ["[H]O[H]"]} |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:16526 resolves to carbon dioxide; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["CO2"], "inchi_string": ["InChI=1S/CO2/c2-1-3"], "mass": ["44.009"], "smiles_string": ["O=C=O"]} |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:17234 resolves to glucose; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C6H12O6"], "mass": ["180.156"]} |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:17997 resolves to dinitrogen; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["N2"], "inchi_string": ["InChI=1S/N2/c1-2"], "mass": ["28.014"], "smiles_string": ["N#N"]} |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:26710 resolves to sodium chloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["Cl.Na"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "smiles_string": ["[Cl-].[Na+]"]} |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["7H2O.Mg.O4S"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]} |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:32139 resolves to sodium hydrogencarbonate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["CHO3.Na"], "inchi_string": ["InChI=1S/CH2O3.Na/c2-1(3)4;/h(H2,2,3,4);/q;+1/p-1"], "mass": ["84.006"], "smiles_string": ["O=C([O-])O.[Na+]"]} |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:32954 resolves to sodium acetate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C2H3O2.Na"], "inchi_string": ["InChI=1S/C2H4O2.Na/c1-2(3)4;/h1H3,(H,3,4);/q;+1/p-1"], "mass": ["82.034"], "smiles_string": ["CC(=O)[O-].[Na+]"]} |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:34887 resolves to nickel dichloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["Cl2Ni"], "inchi_string": ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"], "mass": ["129.599"], "smiles_string": ["[Cl][Ni][Cl]"]} |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:62946 resolves to ammonium sulfate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["2H4N.O4S"], "inchi_string": ["InChI=1S/2H3N.H2O4S/c;;1-5(2,3)4/h2*1H3;(H2,1,2,3,4)"], "mass": ["132.141"], "smiles_string": ["O=S(=O)([O-])[O-].[NH4+].[NH4+]"]} |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["H2O4P.K"], "inchi_string": ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"], "smiles_string": ["O=P([O-])(O)O.[K+]"]} |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:86158 resolves to calcium chloride dihydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["Ca.2Cl.2H2O"], "inchi_string": ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]} |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:8806 resolves to Resazurin; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C12H7NO4"], "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"], "mass": ["229.191"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]} |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"], "mass": ["175.637"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]} |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned CSV; preferred-term MAPPED rows for every asserted secondary CHEBI key | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057; Entire JCM 1057 page, main/post-boiling/custom-trace tables and preparation | supports | Exact original source for M1124; distinguishes main mixture, later bicarbonate/cysteine additions and the custom trace solution. Site-default sterilization is explicitly printed. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124; meta; all components[0:3] and both comments | supports | Exact JCM 1057 correspondence; three sections contain 16, 4 and 3 items. Repeated gas mentions are stage context, not duplicate numeric doses. |
| vit-api | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; meta and components[1] Trace vitamins only; comments[0] named vitamin instruction | supports | This record corresponds to JCM 197. Its eleven-row vitamin stock is the dependency; its own basal medium, mineral stock and pH are excluded. |
| trace-api | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; meta; components[2] Trace minerals and comments[1] only | supports | This record corresponds to JCM 151. Only fourteen trace items including unquantified KOH are used, not its salt-base or Pyrococcus basal medium. |
| vit-primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Trace vitamins subsection and explicitly named filter-sterilization instruction | supports | Ten vitamin quantities and one litre of stock water support the missing vitamin composition; unspecified pantothenate stereochemistry is not broadened to a D-specific claim. |
| trace-primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151; Trace minerals subsection and its final pH-adjustment sentence only | supports | Twelve mineral/chelating constituents plus one litre water; initial stock pH 6.5 and final stock pH 7.0 with unquantified KOH. No Pyrococcus basal conditions are transferred. |
| owner-evidence | /private/tmp/culturemech-review-work-batch016/155/owner-evidence-audit.json; All 31 owner evidence objects and five additional exact excerpts in root evidence explanations | supports | Every snippet is literal in the exact current TOGO body and every historical response hash equals the captured current hash. Original historical access times remain as recorded. Values/units/basis were separately reconciled with the owner nodes and primary; no generated claim inherits verification from the owner. |
| quantities | /private/tmp/culturemech-review-work-batch016/155/quantity-inventory.json; Complete source-linked quantity decision inventory | context_only | Fifty-five exact-source decisions cover all 23 M1124 items, fourteen nested M142 trace items, eleven M190 vitamin items and seven preparation claims. Owner batch quantities/evidence are separately verified; the stale generated target is never marked verified by inheritance. Gas and KOH quantities remain explicitly unquantified. |
| writer | scripts/repair_m142_nested_traces.py; scripts/repair_jcm_stock_preparations.py; scripts/repair_methanogen_stock_boundaries.py; src/culturemech/import/togo_importer.py; src/culturemech/merge/formulation.py; SIZES/M1124, MAIN/M1124=2, LINKS[(0,13)]=2; leaf/stock/comment_claim; current source importer; merge_formulation_evidence | context_only | The scoped repair retains batch input notes, nested M142 stocks and exact source excerpts while explicitly leaving gas placeholders and chemical grounding unresolved. The current formulation-aware merger requires compatibility and preserves evidence. The existing August output predates the October repair; no script or merge was executed in this review. |

## Limits And Additional Notes

- Main water and stock input volumes are not independently measured final volumes. Batch masses are retained without assuming final g/L.
- Only the named JCM 197 trace-vitamin subsection and JCM 151 trace-mineral subsection are dependencies; their basal media, other stocks and organism conditions are excluded. MnSO4 xH2O and aluminum-potassium sulfate hydrate state remain as stated, without inventing a hydrate count.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T103231Z-culturemech-007645-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acetomicrobium_faecale_medium (CultureMech:007645)'
started_at: '2026-10-21T10:23:12Z'
finished_at: '2026-10-21T10:32:31Z'
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
summary: 'The generated M1124/JCM 1057 record predates a substantial evidence-backed
  owner repair: it retains wrong water/stock units, a resazurin mg-to-g error, flattened
  trace constituents and missing nested composition/preparation. The owner now preserves
  source batch quantities and nested mineral stocks, but its vitamin stock remains
  empty and two hydrate mappings remain wrong. The review distinguishes verified owner
  claims from the stale generated target.'
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
  - path: data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml
    sha256: cb216d07f1f3f3c87b585b5f741a2d02ebca94af7b51ed8f75b58ab1d2764eb3
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml
    sha256: e69f71edb54e312fc0148c9217224e0ba3320fdca3dfe272d34264477966491e
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
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_jcm_stock_preparations.py
    sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
    role: context
  - path: scripts/repair_m142_nested_traces.py
    sha256: d015c2df13aadb722e2ada9cd45fbd0e86e4cd48390edae78dab78d5df5ce80f
    role: context
  - path: scripts/repair_methanogen_stock_boundaries.py
    sha256: 8d4d32c7dc3cb2586242a188f958087482df3aff553d1dbc468c422eddb037ba
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/togo_raw_yaml.py
    sha256: ce5e73545c9ecde54724259d2fd475676c0f3cb44dcfd283950e89fd49c10993
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
  - path: src/culturemech/fetch/togo_fetcher.py
    sha256: 7aac40fe1d47e30810ae0be02f6e369ddb9bf657d630072595c62f46fb0bf339
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
  selection: Task review 155; batch 016 item 5 of 10, selected in Python lexicographic
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
  - CultureMech:007645
targets:
- target_id: CultureMech:007645
  path: data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml
  label: acetomicrobium_faecale_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007645
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch016/155/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-016/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch016/155/strict.tsv"
  target_ids:
  - CultureMech:007645
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007645
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007645
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
  - CultureMech:007645
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T10:32:30Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:32:30Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:24:09.515648Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch016/155/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T10:24:11.161732Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-016/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch016/155/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:24:13.150790Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:24:14.305618Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T10:32:30Z'
  support: supports
  summary: './data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml:1:id: CultureMech:007645

    ./data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml:1:id:
    CultureMech:007645

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
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: 'CHEBI:131527 resolves to dipotassium hydrogen phosphate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"generalized_empirical_formula": ["HO4P.2K"],
    "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"],
    "mass": ["174.174"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}'
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: 'CHEBI:15377 resolves to water; canonical label and live status alone do
    not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"generalized_empirical_formula": ["H2O"], "inchi_string": ["InChI=1S/H2O/h1H2"],
    "mass": ["18.015"], "smiles_string": ["[H]O[H]"]}'
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi16526
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:26.337128Z'
  support: supports
  summary: 'CHEBI:16526 resolves to carbon dioxide; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"generalized_empirical_formula": ["CO2"], "inchi_string":
    ["InChI=1S/CO2/c2-1-3"], "mass": ["44.009"], "smiles_string": ["O=C=O"]}'
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
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
- evidence_id: chebi17997
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:27.385647Z'
  support: supports
  summary: 'CHEBI:17997 resolves to dinitrogen; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"generalized_empirical_formula": ["N2"], "inchi_string": ["InChI=1S/N2/c1-2"],
    "mass": ["28.014"], "smiles_string": ["N#N"]}'
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
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
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: 'CHEBI:31795 resolves to magnesium sulfate heptahydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"generalized_empirical_formula": ["7H2O.Mg.O4S"],
    "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}'
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
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
- evidence_id: chebi32954
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:00:48.206583Z'
  support: supports
  summary: 'CHEBI:32954 resolves to sodium acetate; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"generalized_empirical_formula": ["C2H3O2.Na"], "inchi_string":
    ["InChI=1S/C2H4O2.Na/c1-2(3)4;/h1H3,(H,3,4);/q;+1/p-1"], "mass": ["82.034"], "smiles_string":
    ["CC(=O)[O-].[Na+]"]}'
  snapshot_sha256: 573cba85f57c363463610a20b17be618893d6432ba239604fbd8aa562f98161b
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
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: 'CHEBI:62946 resolves to ammonium sulfate; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"generalized_empirical_formula": ["2H4N.O4S"], "inchi_string":
    ["InChI=1S/2H3N.H2O4S/c;;1-5(2,3)4/h2*1H3;(H2,1,2,3,4)"], "mass": ["132.141"],
    "smiles_string": ["O=S(=O)([O-])[O-].[NH4+].[NH4+]"]}'
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
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
  accessed_at: '2026-10-21T10:32:30Z'
  support: supports
  summary: '{"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label":
    "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term":
    "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term",
    "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label":
    "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term":
    "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label":
    "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term":
    "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057
  locator: Entire JCM 1057 page, main/post-boiling/custom-trace tables and preparation
  accessed_at: '2026-10-21T10:07:19.042717Z'
  support: supports
  summary: Exact original source for M1124; distinguishes main mixture, later bicarbonate/cysteine
    additions and the custom trace solution. Site-default sterilization is explicitly
    printed.
  snapshot_sha256: 572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124
  locator: meta; all components[0:3] and both comments
  accessed_at: '2026-10-21T10:07:15.884548Z'
  support: supports
  summary: Exact JCM 1057 correspondence; three sections contain 16, 4 and 3 items.
    Repeated gas mentions are stage context, not duplicate numeric doses.
  snapshot_sha256: b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a
- evidence_id: vit-api
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  locator: meta and components[1] Trace vitamins only; comments[0] named vitamin instruction
  accessed_at: '2026-10-21T09:28:25.418127Z'
  support: supports
  summary: This record corresponds to JCM 197. Its eleven-row vitamin stock is the
    dependency; its own basal medium, mineral stock and pH are excluded.
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: trace-api
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  locator: meta; components[2] Trace minerals and comments[1] only
  accessed_at: '2026-10-21T09:28:25.414106Z'
  support: supports
  summary: This record corresponds to JCM 151. Only fourteen trace items including
    unquantified KOH are used, not its salt-base or Pyrococcus basal medium.
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
- evidence_id: vit-primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: Trace vitamins subsection and explicitly named filter-sterilization instruction
  accessed_at: '2026-10-20T06:58:05.867253Z'
  support: supports
  summary: Ten vitamin quantities and one litre of stock water support the missing
    vitamin composition; unspecified pantothenate stereochemistry is not broadened
    to a D-specific claim.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: trace-primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151
  locator: Trace minerals subsection and its final pH-adjustment sentence only
  accessed_at: '2026-10-21T09:01:28.851101Z'
  support: supports
  summary: Twelve mineral/chelating constituents plus one litre water; initial stock
    pH 6.5 and final stock pH 7.0 with unquantified KOH. No Pyrococcus basal conditions
    are transferred.
  snapshot_sha256: 6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7
- evidence_id: owner-evidence
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch016/155/owner-evidence-audit.json
  locator: All 31 owner evidence objects and five additional exact excerpts in root
    evidence explanations
  accessed_at: '2026-10-21T10:32:30Z'
  support: supports
  summary: Every snippet is literal in the exact current TOGO body and every historical
    response hash equals the captured current hash. Original historical access times
    remain as recorded. Values/units/basis were separately reconciled with the owner
    nodes and primary; no generated claim inherits verification from the owner.
  snapshot_sha256: 56e37b04bfd9ed5d2a63b1df2e5942f8d1ec79af233f0be3f756c7a75a3df0f7
- evidence_id: quantities
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch016/155/quantity-inventory.json
  locator: Complete source-linked quantity decision inventory
  accessed_at: '2026-10-21T10:32:30Z'
  support: context_only
  summary: Fifty-five exact-source decisions cover all 23 M1124 items, fourteen nested
    M142 trace items, eleven M190 vitamin items and seven preparation claims. Owner
    batch quantities/evidence are separately verified; the stale generated target
    is never marked verified by inheritance. Gas and KOH quantities remain explicitly
    unquantified.
  snapshot_sha256: 21169ffe47d2d03902c147d188a1a0609d5b3b7b7be82f7e5d6af1c05a1c0dde
- evidence_id: writer
  kind: record_content
  reference: scripts/repair_m142_nested_traces.py; scripts/repair_jcm_stock_preparations.py;
    scripts/repair_methanogen_stock_boundaries.py; src/culturemech/import/togo_importer.py;
    src/culturemech/merge/formulation.py
  locator: SIZES/M1124, MAIN/M1124=2, LINKS[(0,13)]=2; leaf/stock/comment_claim; current
    source importer; merge_formulation_evidence
  accessed_at: '2026-10-21T10:32:30Z'
  support: context_only
  summary: The scoped repair retains batch input notes, nested M142 stocks and exact
    source excerpts while explicitly leaving gas placeholders and chemical grounding
    unresolved. The current formulation-aware merger requires compatibility and preserves
    evidence. The existing August output predates the October repair; no script or
    merge was executed in this review.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007645
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding-coverage
  area: grounding
  topic: Exact primary labels and current secondary linkage coverage
  outcome: supported
  summary: '16 unique asserted CHEBI identifiers resolve with exact labels. Primary
    linkage 16/18 (88.89%); verified current secondary linkage 8/18 (44.44%). This
    is a 0–100 ingredient-instance linkage scale, not scientific correctness. Missing
    current secondary keys: []. Legacy links and chemical-form correctness are assessed
    separately.'
  target_ids:
  - CultureMech:007645
  evidence_ids:
  - record
  - mim
  - chebi131361
  - chebi131527
  - chebi15377
  - chebi16526
  - chebi17234
  - chebi17997
  - chebi26710
  - chebi31795
  - chebi32139
  - chebi32954
  - chebi34887
  - chebi62946
  - chebi63036
  - chebi86158
  - chebi8806
  - chebi91248
- assessment_id: history-time
  area: provenance
  topic: Full history and timezone audit
  outcome: supported
  summary: 'History event counts: [(''target'', 14), (''data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml'',
    14)]. Explicit timestamp defects: []. Historical bytes are assessed as observed;
    no inferred timezone or retroactive replacement timestamp is supplied.'
  target_ids:
  - CultureMech:007645
  evidence_ids:
  - record
  - owner-0
- assessment_id: quantities
  area: quantity
  topic: Every direct, stock, stock-addition and preparation quantity
  outcome: concern
  summary: Fifty-five exact-source decisions cover all 23 M1124 items, fourteen nested
    M142 trace items, eleven M190 vitamin items and seven preparation claims. Owner
    batch quantities/evidence are separately verified; the stale generated target
    is never marked verified by inheritance. Gas and KOH quantities remain explicitly
    unquantified.
  target_ids:
  - CultureMech:007645
  evidence_ids:
  - record
  - quantities
  - owner-0
  details: '[{"field_path": "ingredients[0].concentration", "decision": "correct",
    "stage": "main batch before later bicarbonate/cysteine additions", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "Distilled water 1.0 L", "source_locator": "JCM 1057 main table;
    exact Distilled water 1.0 L", "explanation": "Source 1.0 L water is correctly
    represented in the owner with exact evidence and batch basis; target 1 G_PER_L
    is a dimensional error, not an equivalent solvent quantity.", "source_amount":
    1, "source_unit": "L", "owner_field_path": "ingredients[0].concentration", "owner_decision":
    "verified", "owner_existing_value": {"value": "1", "unit": "L"}, "provider_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256":
    "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator":
    "$.components[0].items[0]", "provider_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\""}, {"field_path": "ingredients[1].concentration",
    "decision": "correct", "stage": "main batch before later bicarbonate/cysteine
    additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "MgSO 4 ·7H 2 O 0.1 g", "source_locator": "JCM 1057 main table;
    exact MgSO 4 ·7H 2 O 0.1 g", "explanation": "The target still asserts an unsupported
    final-medium concentration. The owner preserves this exact original amount and
    unit as an evidence-backed batch claim, withdrawing unsupported g/L. Its verified
    batch claim does not certify the target.", "source_amount": 0.1, "source_unit":
    "g", "owner_field_path": "ingredients[1].notes", "owner_decision": "verified",
    "owner_existing_value": "Role: Mineral source; Properties: Inorganic compound,
    Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation
    volume is not independently established; the unsupported g/L assertion is withdrawn,
    not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "provider_locator": "$.components[0].items[1]", "provider_quote": "{\n          \"component_name\":
    \"MgSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001002\""}, {"field_path": "ingredients[2].concentration",
    "decision": "correct", "stage": "main batch before later bicarbonate/cysteine
    additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "Yeast extract 2.0 g", "source_locator": "JCM 1057 main table;
    exact Yeast extract 2.0 g", "explanation": "The target still asserts an unsupported
    final-medium concentration. The owner preserves this exact original amount and
    unit as an evidence-backed batch claim, withdrawing unsupported g/L. Its verified
    batch claim does not certify the target.", "source_amount": 2, "source_unit":
    "g", "owner_field_path": "ingredients[2].notes", "owner_decision": "verified",
    "owner_existing_value": "Role: Nutrient source; Properties: Undefined component\n\nSource
    batch input: 2 g. Final preparation volume is not independently established; the
    unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "provider_locator": "$.components[0].items[2]", "provider_quote": "{\n          \"component_name\":
    \"Yeast extract\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001003\""}, {"field_path": "ingredients[3].concentration",
    "decision": "correct", "stage": "main batch before later bicarbonate/cysteine
    additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "NaCl 0.5 g", "source_locator": "JCM 1057 main table; exact NaCl
    0.5 g", "explanation": "The target still asserts an unsupported final-medium concentration.
    The owner preserves this exact original amount and unit as an evidence-backed
    batch claim, withdrawing unsupported g/L. Its verified batch claim does not certify
    the target.", "source_amount": 0.5, "source_unit": "g", "owner_field_path": "ingredients[3].notes",
    "owner_decision": "verified", "owner_existing_value": "Role: Mineral source; Properties:
    Inorganic compound, Defined component, Simple component\n\nSource batch input:
    0.5 g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "provider_locator": "$.components[0].items[3]", "provider_quote": "{\n          \"component_name\":
    \"NaCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001004\""}, {"field_path": "ingredients[4].concentration",
    "decision": "correct", "stage": "main batch before later bicarbonate/cysteine
    additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "CaCl 2 ·2H 2 O 0.07 g", "source_locator": "JCM 1057 main table;
    exact CaCl 2 ·2H 2 O 0.07 g", "explanation": "The target still asserts an unsupported
    final-medium concentration. The owner preserves this exact original amount and
    unit as an evidence-backed batch claim, withdrawing unsupported g/L. Its verified
    batch claim does not certify the target.", "source_amount": 0.07, "source_unit":
    "g", "owner_field_path": "ingredients[4].notes", "owner_decision": "verified",
    "owner_existing_value": "Role: Mineral source; Properties: Inorganic compound,
    Defined component, Simple component\n\nSource batch input: 0.07 g. Final preparation
    volume is not independently established; the unsupported g/L assertion is withdrawn,
    not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "provider_locator": "$.components[0].items[4]", "provider_quote": "{\n          \"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 0.07,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\""}, {"field_path": "ingredients[5].concentration",
    "decision": "correct", "stage": "main batch before later bicarbonate/cysteine
    additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "KH 2 PO 4 0.225 g", "source_locator": "JCM 1057 main table; exact
    KH 2 PO 4 0.225 g", "explanation": "The target still asserts an unsupported final-medium
    concentration. The owner preserves this exact original amount and unit as an evidence-backed
    batch claim, withdrawing unsupported g/L. Its verified batch claim does not certify
    the target.", "source_amount": 0.225, "source_unit": "g", "owner_field_path":
    "ingredients[5].notes", "owner_decision": "verified", "owner_existing_value":
    "Role: Buffer; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.225 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "provider_locator": "$.components[0].items[5]", "provider_quote": "{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 0.225,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\""}, {"field_path": "ingredients[6].concentration",
    "decision": "correct", "stage": "main batch before later bicarbonate/cysteine
    additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "K 2 HPO 4 0.255 g", "source_locator": "JCM 1057 main table; exact
    K 2 HPO 4 0.255 g", "explanation": "The target still asserts an unsupported final-medium
    concentration. The owner preserves this exact original amount and unit as an evidence-backed
    batch claim, withdrawing unsupported g/L. Its verified batch claim does not certify
    the target.", "source_amount": 0.255, "source_unit": "g", "owner_field_path":
    "ingredients[6].notes", "owner_decision": "verified", "owner_existing_value":
    "Role: Buffer; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.255 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "provider_locator": "$.components[0].items[6]", "provider_quote": "{\n          \"component_name\":
    \"K2HPO4\",\n          \"volume\": 0.255,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001009\""}, {"field_path": "ingredients[7].concentration",
    "decision": "correct", "stage": "main batch before later bicarbonate/cysteine
    additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "Resazurin 1.0 mg", "source_locator": "JCM 1057 main table; exact
    Resazurin 1.0 mg", "explanation": "Source 1 mg equals 0.001 g for the batch, not
    target 1 g/L. The owner correctly preserves 1 mg in an evidence-backed batch note
    without inventing final volume.", "source_amount": 1, "source_unit": "mg", "owner_field_path":
    "ingredients[7].notes", "owner_decision": "verified", "owner_existing_value":
    "Role: pH dependent redox indicator; Properties: Organic compound, Defined component,
    Simple component\n\nSource batch input: 1 mg. Final preparation volume is not
    independently established; the unsupported g/L assertion is withdrawn, not replaced
    by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "provider_locator": "$.components[0].items[7]", "provider_quote": "{\n          \"component_name\":
    \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001012\""}, {"field_path": "ingredients[8].concentration",
    "decision": "correct", "stage": "main batch before later bicarbonate/cysteine
    additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "(NH 4 ) 2 SO 4 0.255 g", "source_locator": "JCM 1057 main table;
    exact (NH 4 ) 2 SO 4 0.255 g", "explanation": "The target still asserts an unsupported
    final-medium concentration. The owner preserves this exact original amount and
    unit as an evidence-backed batch claim, withdrawing unsupported g/L. Its verified
    batch claim does not certify the target.", "source_amount": 0.255, "source_unit":
    "g", "owner_field_path": "ingredients[8].notes", "owner_decision": "verified",
    "owner_existing_value": "Role: Nitrogen source; Properties: Inorganic compound,
    Defined component, Simple component\n\nSource batch input: 0.255 g. Final preparation
    volume is not independently established; the unsupported g/L assertion is withdrawn,
    not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "provider_locator": "$.components[0].items[8]", "provider_quote": "{\n          \"component_name\":
    \"(NH4)2SO4\",\n          \"volume\": 0.255,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001030\""}, {"field_path": "ingredients[9].concentration",
    "decision": "correct", "stage": "main batch before later bicarbonate/cysteine
    additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "Sodium acetate·3H 2 O 5.0 g", "source_locator": "JCM 1057 main
    table; exact Sodium acetate·3H 2 O 5.0 g", "explanation": "The target still asserts
    an unsupported final-medium concentration. The owner preserves this exact original
    amount and unit as an evidence-backed batch claim, withdrawing unsupported g/L.
    Its verified batch claim does not certify the target.", "source_amount": 5, "source_unit":
    "g", "owner_field_path": "ingredients[9].notes", "owner_decision": "verified",
    "owner_existing_value": "Role: Buffer; Properties: Organic compound, Defined component,
    Simple component\n\nSource batch input: 5 g. Final preparation volume is not independently
    established; the unsupported g/L assertion is withdrawn, not replaced by an assumed
    one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "provider_locator": "$.components[0].items[9]", "provider_quote": "{\n          \"component_name\":
    \"Sodium acetate・3H2O\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001396\""}, {"field_path": "ingredients[10].concentration",
    "decision": "correct", "stage": "main batch before later bicarbonate/cysteine
    additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "Glucose 4.0 g", "source_locator": "JCM 1057 main table; exact
    Glucose 4.0 g", "explanation": "The target still asserts an unsupported final-medium
    concentration. The owner preserves this exact original amount and unit as an evidence-backed
    batch claim, withdrawing unsupported g/L. Its verified batch claim does not certify
    the target.", "source_amount": 4, "source_unit": "g", "owner_field_path": "ingredients[10].notes",
    "owner_decision": "verified", "owner_existing_value": "Role: Carbon source; Properties:
    Organic compound, Defined component, Simple component\n\nSource batch input: 4
    g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "provider_locator": "$.components[0].items[10]", "provider_quote": "{\n          \"component_name\":
    \"Glucose\",\n          \"volume\": 4,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001815\""}, {"field_path": "ingredients[11].concentration",
    "decision": "correct", "stage": "main batch before later bicarbonate/cysteine
    additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "Trypticase peptone (BD-BBL) 2.0 g", "source_locator": "JCM 1057
    main table; exact Trypticase peptone (BD-BBL) 2.0 g", "explanation": "The target
    still asserts an unsupported final-medium concentration. The owner preserves this
    exact original amount and unit as an evidence-backed batch claim, withdrawing
    unsupported g/L. Its verified batch claim does not certify the target.", "source_amount":
    2, "source_unit": "g", "owner_field_path": "ingredients[11].notes", "owner_decision":
    "verified", "owner_existing_value": "Properties: Undefined component\n\nSource
    batch input: 2 g. Final preparation volume is not independently established; the
    unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "provider_locator": "$.components[0].items[11]", "provider_quote": "{\n          \"component_name\":
    \"Trypticase peptone (BD-BBL)\",\n          \"volume\": 2,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001097\""}, {"field_path":
    "solutions[0].concentration", "decision": "correct", "stage": "main batch before
    later bicarbonate/cysteine additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "Trace vitamins (see Medium No. 197 ) 10.0 ml", "source_locator":
    "JCM 1057 main table; exact Trace vitamins (see Medium No. 197 ) 10.0 ml", "explanation":
    "Source 10 ml equals 0.01 L per receiving batch. The owner has that exact dose
    with field-specific root evidence; target 10 G_PER_L has the wrong physical dimension.
    Keep vitamin and custom-mineral formulations separate.", "source_amount": 10,
    "source_unit": "ml", "owner_field_path": "solutions[0].concentration", "owner_decision":
    "verified", "owner_existing_value": {"value": "0.01", "unit": "L"}, "provider_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256":
    "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator":
    "$.components[0].items[12]", "provider_quote": "{\n          \"component_name\":
    \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\":
    \"ml\""}, {"field_path": "solutions[1].concentration", "decision": "correct",
    "stage": "main batch before later bicarbonate/cysteine additions", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "Trace minerals solution (see below) 10.0 ml", "source_locator":
    "JCM 1057 main table; exact Trace minerals solution (see below) 10.0 ml", "explanation":
    "Source 10 ml equals 0.01 L per receiving batch. The owner has that exact dose
    with field-specific root evidence; target 10 G_PER_L has the wrong physical dimension.
    Keep vitamin and custom-mineral formulations separate.", "source_amount": 10,
    "source_unit": "ml", "owner_field_path": "solutions[1].concentration", "owner_decision":
    "verified", "owner_existing_value": {"value": "0.01", "unit": "L"}, "provider_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256":
    "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator":
    "$.components[0].items[13]", "provider_quote": "{\n          \"component_name\":
    \"Trace minerals solution (see below)\",\n          \"volume\": 10,\n          \"unit\":
    \"ml\""}, {"field_path": "ingredients[12].concentration", "decision": "not_quantified",
    "stage": "main source section 0; gas context", "source_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "source_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "source_quote": "{\n          \"component_name\": \"Carbon dioxide gas\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_002260\"", "source_locator": "$.components[0].items[14]",
    "explanation": "The source item has no fixed gas volume, flow or dissolved concentration.
    The legacy VARIABLE placeholder is not a verified concentration. Separate preparation
    decisions retain the explicit mixture ratio and bottle pressure; repeated mentions
    do not authorize summing gas doses.", "owner_field_path": "ingredients[12].concentration",
    "owner_decision": "not_quantified"}, {"field_path": "ingredients[13].concentration",
    "decision": "not_quantified", "stage": "main source section 0; gas context", "source_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "source_sha256":
    "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "source_quote":
    "{\n          \"component_name\": \"Nitrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\"",
    "source_locator": "$.components[0].items[15]", "explanation": "The source item
    has no fixed gas volume, flow or dissolved concentration. The legacy VARIABLE
    placeholder is not a verified concentration. Separate preparation decisions retain
    the explicit mixture ratio and bottle pressure; repeated mentions do not authorize
    summing gas doses.", "owner_field_path": "ingredients[13].concentration", "owner_decision":
    "not_quantified"}, {"field_path": "ingredients[12].concentration", "decision":
    "not_quantified", "stage": "main source section 1; gas context", "source_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "source_sha256":
    "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "source_quote":
    "{\n          \"component_name\": \"Carbon dioxide gas\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_002260\"", "source_locator": "$.components[1].items[2]",
    "explanation": "The source item has no fixed gas volume, flow or dissolved concentration.
    The legacy VARIABLE placeholder is not a verified concentration. Separate preparation
    decisions retain the explicit mixture ratio and bottle pressure; repeated mentions
    do not authorize summing gas doses.", "owner_field_path": "ingredients[12].concentration",
    "owner_decision": "not_quantified"}, {"field_path": "ingredients[13].concentration",
    "decision": "not_quantified", "stage": "main source section 1; gas context", "source_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "source_sha256":
    "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "source_quote":
    "{\n          \"component_name\": \"Nitrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\"",
    "source_locator": "$.components[1].items[3]", "explanation": "The source item
    has no fixed gas volume, flow or dissolved concentration. The legacy VARIABLE
    placeholder is not a verified concentration. Separate preparation decisions retain
    the explicit mixture ratio and bottle pressure; repeated mentions do not authorize
    summing gas doses.", "owner_field_path": "ingredients[13].concentration", "owner_decision":
    "not_quantified"}, {"field_path": "ingredients[14].concentration", "decision":
    "correct", "stage": "post-boiling main additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "NaHCO 3 6.0 g", "source_locator": "JCM 1057 second table, following
    boiling/cooling", "explanation": "Target g/L assumes final volume. The owner correctly
    keeps this exact batch mass with attached evidence in notes, after boiling/cooling
    and before sealing/autoclaving.", "source_amount": 6, "source_unit": "g", "owner_field_path":
    "ingredients[14].notes", "owner_decision": "verified", "owner_existing_value":
    "Role: Buffer; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 6 g. Final preparation volume is not independently established; the
    unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "provider_locator": "$.components[1].items[0]", "provider_quote": "{\n          \"component_name\":
    \"NaHCO3\",\n          \"volume\": 6,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001019\""}, {"field_path": "ingredients[15].concentration",
    "decision": "correct", "stage": "post-boiling main additions", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "L-Cysteine·HCl·H 2 O 0.5 g", "source_locator": "JCM 1057 second
    table, following boiling/cooling", "explanation": "Target g/L assumes final volume.
    The owner correctly keeps this exact batch mass with attached evidence in notes,
    after boiling/cooling and before sealing/autoclaving.", "source_amount": 0.5,
    "source_unit": "g", "owner_field_path": "ingredients[15].notes", "owner_decision":
    "verified", "owner_existing_value": "Properties: Defined component, Simple component,
    Organic compound\n\nSource batch input: 0.5 g. Final preparation volume is not
    independently established; the unsupported g/L assertion is withdrawn, not replaced
    by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "provider_locator": "$.components[1].items[1]", "provider_quote": "{\n          \"component_name\":
    \"L--Cysteine・HCl・H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001205\""}, {"field_path": "ingredients[16].concentration",
    "decision": "correct", "stage": "custom trace-stock batch", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "NiCl 2 ·6H 2 O 0.03 g", "source_locator": "JCM 1057 Trace minerals
    solution subsection; exact NiCl 2 ·6H 2 O 0.03 g", "explanation": "This is a custom
    trace-stock batch constituent, not a direct main ingredient. The owner has the
    exact batch quantity and attached evidence in the correct nested scope. The 10
    ml custom-stock addition must remain distinct from its 1 L M142 input; actual
    final volumes are not established.", "source_amount": 0.03, "source_unit": "g",
    "owner_field_path": "solutions[1].composition[0].notes", "owner_decision": "verified",
    "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "provider_locator": "$.components[2].items[0]", "provider_quote": "{\n          \"component_name\":
    \"NiCl2・6H2O\",\n          \"volume\": 0.03,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001022\""}, {"field_path": "ingredients[17].concentration",
    "decision": "correct", "stage": "custom trace-stock batch", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "Na 2 SeO 3 ·5H 2 O 0.3 mg", "source_locator": "JCM 1057 Trace
    minerals solution subsection; exact Na 2 SeO 3 ·5H 2 O 0.3 mg", "explanation":
    "This is a custom trace-stock batch constituent, not a direct main ingredient.
    The owner has the exact batch quantity and attached evidence in the correct nested
    scope. The 10 ml custom-stock addition must remain distinct from its 1 L M142
    input; actual final volumes are not established. The source 0.3 mg is 0.0003 g
    in the stock batch, not target 0.3 g/L.", "source_amount": 0.3, "source_unit":
    "mg", "owner_field_path": "solutions[1].composition[1].notes", "owner_decision":
    "verified", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124",
    "provider_sha256": "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a",
    "provider_locator": "$.components[2].items[1]", "provider_quote": "{\n          \"component_name\":
    \"Na2SeO3・5H2O\",\n          \"volume\": 0.3,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001046\""}, {"field_path": "solutions[2].concentration",
    "decision": "correct", "stage": "custom trace-stock batch", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "Trace minerals (see Medium No. 151 ) 1.0 L", "source_locator":
    "JCM 1057 Trace minerals solution subsection; exact Trace minerals (see Medium
    No. 151 ) 1.0 L", "explanation": "This is a custom trace-stock batch constituent,
    not a direct main ingredient. The owner has the exact batch quantity and attached
    evidence in the correct nested scope. The 10 ml custom-stock addition must remain
    distinct from its 1 L M142 input; actual final volumes are not established.",
    "source_amount": 1, "source_unit": "L", "owner_field_path": "solutions[1].solutions[0].concentration",
    "owner_decision": "verified", "owner_existing_value": null, "provider_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124", "provider_sha256":
    "b6df18d591ddeb0cea1d65784017ee54fad6fc0376c5b629db12b305ae15631a", "provider_locator":
    "$.components[2].items[2]", "provider_quote": "{\n          \"component_name\":
    \"Trace minerals (see Medium [M142])\",\n          \"volume\": 1,\n          \"unit\":
    \"L\""}, {"field_path": "solutions[2].composition (empty target)", "decision":
    "add", "stage": "innermost M142/JCM 151 trace-stock batch", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "Distilled water 1.0 L", "source_locator": "JCM 151 Trace minerals
    subsection; exact Distilled water 1.0 L", "explanation": "The owner already preserves
    this exact source batch amount and unit with attached evidence. Restore its scope
    and evidence in derived output. Do not equate stock water with final volume, or
    replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.",
    "source_amount": 1, "source_unit": "L", "owner_field_path": "solutions[1].solutions[0].composition[0].concentration",
    "owner_decision": "verified", "owner_existing_value": {"value": "1", "unit": "L"},
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "provider_locator": "$.components[2].items[0]", "provider_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\""}, {"field_path": "solutions[2].composition
    (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock
    batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
    "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "MgSO 4 ·7H 2 O 3.0 g", "source_locator": "JCM 151 Trace minerals
    subsection; exact MgSO 4 ·7H 2 O 3.0 g", "explanation": "The owner already preserves
    this exact source batch amount and unit with attached evidence. Restore its scope
    and evidence in derived output. Do not equate stock water with final volume, or
    replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.",
    "source_amount": 3, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[1].notes",
    "owner_decision": "verified", "owner_existing_value": "Source batch input: 3 g.
    Final preparation volume is not independently established; the unsupported g/L
    assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "provider_locator": "$.components[2].items[1]", "provider_quote": "{\n          \"component_name\":
    \"MgSO4・7H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001002\""}, {"field_path": "solutions[2].composition
    (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock
    batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
    "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "NaCl 1.0 g", "source_locator": "JCM 151 Trace minerals subsection;
    exact NaCl 1.0 g", "explanation": "The owner already preserves this exact source
    batch amount and unit with attached evidence. Restore its scope and evidence in
    derived output. Do not equate stock water with final volume, or replace MnSO4
    xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.", "source_amount":
    1, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[2].notes",
    "owner_decision": "verified", "owner_existing_value": "Source batch input: 1 g.
    Final preparation volume is not independently established; the unsupported g/L
    assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "provider_locator": "$.components[2].items[2]", "provider_quote": "{\n          \"component_name\":
    \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001004\""}, {"field_path": "solutions[2].composition
    (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock
    batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
    "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "CaCl 2 ·2H 2 O 0.1 g", "source_locator": "JCM 151 Trace minerals
    subsection; exact CaCl 2 ·2H 2 O 0.1 g", "explanation": "The owner already preserves
    this exact source batch amount and unit with attached evidence. Restore its scope
    and evidence in derived output. Do not equate stock water with final volume, or
    replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.",
    "source_amount": 0.1, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[3].notes",
    "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.1
    g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "provider_locator": "$.components[2].items[3]", "provider_quote": "{\n          \"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\""}, {"field_path": "solutions[2].composition
    (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock
    batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
    "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "Na 2 MoO 4 ·2H 2 O 0.01 g", "source_locator": "JCM 151 Trace
    minerals subsection; exact Na 2 MoO 4 ·2H 2 O 0.01 g", "explanation": "The owner
    already preserves this exact source batch amount and unit with attached evidence.
    Restore its scope and evidence in derived output. Do not equate stock water with
    final volume, or replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with
    an unstated hydrate.", "source_amount": 0.01, "source_unit": "g", "owner_field_path":
    "solutions[1].solutions[0].composition[4].notes", "owner_decision": "verified",
    "owner_existing_value": "Source batch input: 0.01 g. Final preparation volume
    is not independently established; the unsupported g/L assertion is withdrawn,
    not replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "provider_locator": "$.components[2].items[4]", "provider_quote": "{\n          \"component_name\":
    \"Na2MoO4・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001011\""}, {"field_path": "solutions[2].composition
    (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock
    batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
    "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "H 3 BO 3 0.01 g", "source_locator": "JCM 151 Trace minerals subsection;
    exact H 3 BO 3 0.01 g", "explanation": "The owner already preserves this exact
    source batch amount and unit with attached evidence. Restore its scope and evidence
    in derived output. Do not equate stock water with final volume, or replace MnSO4
    xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.", "source_amount":
    0.01, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[5].notes",
    "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.01
    g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "provider_locator": "$.components[2].items[5]", "provider_quote": "{\n          \"component_name\":
    \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001015\""}, {"field_path": "solutions[2].composition
    (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock
    batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
    "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "FeSO 4 ·7H 2 O 0.1 g", "source_locator": "JCM 151 Trace minerals
    subsection; exact FeSO 4 ·7H 2 O 0.1 g", "explanation": "The owner already preserves
    this exact source batch amount and unit with attached evidence. Restore its scope
    and evidence in derived output. Do not equate stock water with final volume, or
    replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.",
    "source_amount": 0.1, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[6].notes",
    "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.1
    g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "provider_locator": "$.components[2].items[6]", "provider_quote": "{\n          \"component_name\":
    \"FeSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001016\""}, {"field_path": "solutions[2].composition
    (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock
    batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
    "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "ZnSO 4 ·7H 2 O 0.1 g", "source_locator": "JCM 151 Trace minerals
    subsection; exact ZnSO 4 ·7H 2 O 0.1 g", "explanation": "The owner already preserves
    this exact source batch amount and unit with attached evidence. Restore its scope
    and evidence in derived output. Do not equate stock water with final volume, or
    replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.",
    "source_amount": 0.1, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[7].notes",
    "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.1
    g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "provider_locator": "$.components[2].items[7]", "provider_quote": "{\n          \"component_name\":
    \"ZnSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001023\""}, {"field_path": "solutions[2].composition
    (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock
    batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
    "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "CuSO 4 ·5H 2 O 0.01 g", "source_locator": "JCM 151 Trace minerals
    subsection; exact CuSO 4 ·5H 2 O 0.01 g", "explanation": "The owner already preserves
    this exact source batch amount and unit with attached evidence. Restore its scope
    and evidence in derived output. Do not equate stock water with final volume, or
    replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.",
    "source_amount": 0.01, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[8].notes",
    "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.01
    g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "provider_locator": "$.components[2].items[8]", "provider_quote": "{\n          \"component_name\":
    \"CuSO4・5H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001039\""}, {"field_path": "solutions[2].composition
    (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock
    batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
    "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "CoSO 4 ·7H 2 O 0.1 g", "source_locator": "JCM 151 Trace minerals
    subsection; exact CoSO 4 ·7H 2 O 0.1 g", "explanation": "The owner already preserves
    this exact source batch amount and unit with attached evidence. Restore its scope
    and evidence in derived output. Do not equate stock water with final volume, or
    replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.",
    "source_amount": 0.1, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[9].notes",
    "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.1
    g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "provider_locator": "$.components[2].items[9]", "provider_quote": "{\n          \"component_name\":
    \"CoSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001050\""}, {"field_path": "solutions[2].composition
    (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock
    batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
    "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "Nitrilotriacetic acid 1.5 g", "source_locator": "JCM 151 Trace
    minerals subsection; exact Nitrilotriacetic acid 1.5 g", "explanation": "The owner
    already preserves this exact source batch amount and unit with attached evidence.
    Restore its scope and evidence in derived output. Do not equate stock water with
    final volume, or replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with
    an unstated hydrate.", "source_amount": 1.5, "source_unit": "g", "owner_field_path":
    "solutions[1].solutions[0].composition[10].notes", "owner_decision": "verified",
    "owner_existing_value": "Source batch input: 1.5 g. Final preparation volume is
    not independently established; the unsupported g/L assertion is withdrawn, not
    replaced by an assumed one-liter concentration.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "provider_locator": "$.components[2].items[10]", "provider_quote": "{\n          \"component_name\":
    \"Nitrilotriacetic acid\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001053\""}, {"field_path": "solutions[2].composition
    (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock
    batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
    "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "MnSO 4 · x H 2 O 0.5 g", "source_locator": "JCM 151 Trace minerals
    subsection; exact MnSO 4 · x H 2 O 0.5 g", "explanation": "The owner already preserves
    this exact source batch amount and unit with attached evidence. Restore its scope
    and evidence in derived output. Do not equate stock water with final volume, or
    replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.",
    "source_amount": 0.5, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[11].notes",
    "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.5
    g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "provider_locator": "$.components[2].items[11]", "provider_quote": "{\n          \"component_name\":
    \"MnSO4・xH2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001065\""}, {"field_path": "solutions[2].composition
    (empty target)", "decision": "add", "stage": "innermost M142/JCM 151 trace-stock
    batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
    "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "AlK(SO 4 ) 2 0.01 g", "source_locator": "JCM 151 Trace minerals
    subsection; exact AlK(SO 4 ) 2 0.01 g", "explanation": "The owner already preserves
    this exact source batch amount and unit with attached evidence. Restore its scope
    and evidence in derived output. Do not equate stock water with final volume, or
    replace MnSO4 xH2O with a chosen hydrate count or AlK(SO4)2 with an unstated hydrate.",
    "source_amount": 0.01, "source_unit": "g", "owner_field_path": "solutions[1].solutions[0].composition[12].notes",
    "owner_decision": "verified", "owner_existing_value": "Source batch input: 0.01
    g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "provider_locator": "$.components[2].items[12]", "provider_quote": "{\n          \"component_name\":
    \"AlK(SO4)2\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001088\""}, {"field_path": "solutions[2].composition
    (missing KOH context)", "decision": "not_quantified", "stage": "innermost trace-stock
    titration", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
    "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "adjust pH to 6.5 with KOH solution.", "source_locator": "JCM
    151 final Trace minerals preparation sentence", "explanation": "KOH amount and
    strength are unspecified. Owner preserves an empty KOH adjustment node with root
    evidence; it is intentionally unquantified, unlike the incomplete vitamin stock.",
    "owner_field_path": "solutions[1].solutions[0].solutions[0]", "owner_decision":
    "not_quantified", "provider_quote": "{\n          \"component_name\": \"KOH solution\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001903\"", "provider_locator": "$.components[2].items[13]",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "provider_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"},
    {"field_path": "solutions[0].composition (empty)", "decision": "add", "stage":
    "separate trace-vitamin stock batch", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
    "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
    "source_quote": "Distilled water 1.0 L", "source_locator": "JCM 197 Trace vitamins
    subsection; exact Distilled water 1.0 L", "explanation": "Both target and owner
    vitamin compositions are empty despite a resolvable exact eleven-row source stock.
    Add original amounts/units and solvent context with narrow evidence; do not transfer
    the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving
    dose is a separate claim.", "source_amount": 1, "source_unit": "L", "owner_field_path":
    "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value":
    null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "provider_locator": "$.components[1].items[0]", "provider_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\""}, {"field_path": "solutions[0].composition
    (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
    "source_quote": "Biotin 2.0 mg", "source_locator": "JCM 197 Trace vitamins subsection;
    exact Biotin 2.0 mg", "explanation": "Both target and owner vitamin compositions
    are empty despite a resolvable exact eleven-row source stock. Add original amounts/units
    and solvent context with narrow evidence; do not transfer the JCM 197 basal mixture
    or infer pantothenate stereochemistry. Its 10 ml receiving dose is a separate
    claim.", "source_amount": 2, "source_unit": "mg", "owner_field_path": "solutions[0].composition
    (empty)", "owner_decision": "add", "owner_existing_value": null, "provider_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "provider_sha256":
    "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "provider_locator":
    "$.components[1].items[1]", "provider_quote": "{\n          \"component_name\":
    \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001025\""}, {"field_path": "solutions[0].composition
    (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
    "source_quote": "p -Aminobenzoic acid 5.0 mg", "source_locator": "JCM 197 Trace
    vitamins subsection; exact p -Aminobenzoic acid 5.0 mg", "explanation": "Both
    target and owner vitamin compositions are empty despite a resolvable exact eleven-row
    source stock. Add original amounts/units and solvent context with narrow evidence;
    do not transfer the JCM 197 basal mixture or infer pantothenate stereochemistry.
    Its 10 ml receiving dose is a separate claim.", "source_amount": 5, "source_unit":
    "mg", "owner_field_path": "solutions[0].composition (empty)", "owner_decision":
    "add", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "provider_locator": "$.components[1].items[2]", "provider_quote": "{\n          \"component_name\":
    \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001026\""}, {"field_path": "solutions[0].composition
    (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
    "source_quote": "Thiamine·HCl 5.0 mg", "source_locator": "JCM 197 Trace vitamins
    subsection; exact Thiamine·HCl 5.0 mg", "explanation": "Both target and owner
    vitamin compositions are empty despite a resolvable exact eleven-row source stock.
    Add original amounts/units and solvent context with narrow evidence; do not transfer
    the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving
    dose is a separate claim.", "source_amount": 5, "source_unit": "mg", "owner_field_path":
    "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value":
    null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "provider_locator": "$.components[1].items[3]", "provider_quote": "{\n          \"component_name\":
    \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001027\""}, {"field_path": "solutions[0].composition
    (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
    "source_quote": "Calcium pantothenate 5.0 mg", "source_locator": "JCM 197 Trace
    vitamins subsection; exact Calcium pantothenate 5.0 mg", "explanation": "Both
    target and owner vitamin compositions are empty despite a resolvable exact eleven-row
    source stock. Add original amounts/units and solvent context with narrow evidence;
    do not transfer the JCM 197 basal mixture or infer pantothenate stereochemistry.
    Its 10 ml receiving dose is a separate claim.", "source_amount": 5, "source_unit":
    "mg", "owner_field_path": "solutions[0].composition (empty)", "owner_decision":
    "add", "owner_existing_value": null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "provider_locator": "$.components[1].items[4]", "provider_quote": "{\n          \"component_name\":
    \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001028\""}, {"field_path": "solutions[0].composition
    (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
    "source_quote": "Pyridoxine·HCl 10.0 mg", "source_locator": "JCM 197 Trace vitamins
    subsection; exact Pyridoxine·HCl 10.0 mg", "explanation": "Both target and owner
    vitamin compositions are empty despite a resolvable exact eleven-row source stock.
    Add original amounts/units and solvent context with narrow evidence; do not transfer
    the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving
    dose is a separate claim.", "source_amount": 10, "source_unit": "mg", "owner_field_path":
    "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value":
    null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "provider_locator": "$.components[1].items[5]", "provider_quote": "{\n          \"component_name\":
    \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001029\""}, {"field_path": "solutions[0].composition
    (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
    "source_quote": "Folic acid 2.0 mg", "source_locator": "JCM 197 Trace vitamins
    subsection; exact Folic acid 2.0 mg", "explanation": "Both target and owner vitamin
    compositions are empty despite a resolvable exact eleven-row source stock. Add
    original amounts/units and solvent context with narrow evidence; do not transfer
    the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving
    dose is a separate claim.", "source_amount": 2, "source_unit": "mg", "owner_field_path":
    "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value":
    null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "provider_locator": "$.components[1].items[6]", "provider_quote": "{\n          \"component_name\":
    \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001033\""}, {"field_path": "solutions[0].composition
    (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
    "source_quote": "Vitamin B 1 2 0.1 mg", "source_locator": "JCM 197 Trace vitamins
    subsection; exact Vitamin B 1 2 0.1 mg", "explanation": "Both target and owner
    vitamin compositions are empty despite a resolvable exact eleven-row source stock.
    Add original amounts/units and solvent context with narrow evidence; do not transfer
    the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving
    dose is a separate claim.", "source_amount": 0.1, "source_unit": "mg", "owner_field_path":
    "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value":
    null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "provider_locator": "$.components[1].items[7]", "provider_quote": "{\n          \"component_name\":
    \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001034\""}, {"field_path": "solutions[0].composition
    (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
    "source_quote": "Riboflavin 5.0 mg", "source_locator": "JCM 197 Trace vitamins
    subsection; exact Riboflavin 5.0 mg", "explanation": "Both target and owner vitamin
    compositions are empty despite a resolvable exact eleven-row source stock. Add
    original amounts/units and solvent context with narrow evidence; do not transfer
    the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving
    dose is a separate claim.", "source_amount": 5, "source_unit": "mg", "owner_field_path":
    "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value":
    null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "provider_locator": "$.components[1].items[8]", "provider_quote": "{\n          \"component_name\":
    \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001037\""}, {"field_path": "solutions[0].composition
    (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
    "source_quote": "Nicotinic acid 5.0 mg", "source_locator": "JCM 197 Trace vitamins
    subsection; exact Nicotinic acid 5.0 mg", "explanation": "Both target and owner
    vitamin compositions are empty despite a resolvable exact eleven-row source stock.
    Add original amounts/units and solvent context with narrow evidence; do not transfer
    the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving
    dose is a separate claim.", "source_amount": 5, "source_unit": "mg", "owner_field_path":
    "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value":
    null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "provider_locator": "$.components[1].items[9]", "provider_quote": "{\n          \"component_name\":
    \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001038\""}, {"field_path": "solutions[0].composition
    (empty)", "decision": "add", "stage": "separate trace-vitamin stock batch", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
    "source_quote": "Lipoic acid 5.0 mg", "source_locator": "JCM 197 Trace vitamins
    subsection; exact Lipoic acid 5.0 mg", "explanation": "Both target and owner vitamin
    compositions are empty despite a resolvable exact eleven-row source stock. Add
    original amounts/units and solvent context with narrow evidence; do not transfer
    the JCM 197 basal mixture or infer pantothenate stereochemistry. Its 10 ml receiving
    dose is a separate claim.", "source_amount": 5, "source_unit": "mg", "owner_field_path":
    "solutions[0].composition (empty)", "owner_decision": "add", "owner_existing_value":
    null, "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "provider_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "provider_locator": "$.components[1].items[10]", "provider_quote": "{\n          \"component_name\":
    \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001699\""}, {"field_path": "preparation_steps
    (missing)", "decision": "not_quantified", "stage": "main boiling", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057", "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "Bring to a boil for seconds", "source_locator": "main preparation,
    before cooling", "explanation": "The source specifies seconds but no numeric duration.
    The owner retains this wording; do not invent a boil duration.", "owner_field_path":
    "preparation_steps[0]", "owner_decision": "not_quantified"}, {"field_path": "preparation_steps
    (missing)", "decision": "add", "stage": "main cooling before bicarbonate/cysteine",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture", "source_locator": "main cooling
    sentence", "explanation": "Source ratio is 4:1 v/v (80:20), not separate ingredient
    concentrations. The owner already retains the ratio and matching source excerpt.",
    "owner_field_path": "preparation_steps[0]", "owner_decision": "verified"}, {"field_path":
    "preparation_steps (missing)", "decision": "add", "stage": "after inoculation",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "pressurize the inoculated bottles to 200 kPa with a N 2 -CO 2
    (4:1, v/v) gas mixture.", "source_locator": "after-inoculation sentence", "explanation":
    "Both 200 kPa and 4:1 v/v belong to the stated bottle stage. The owner preserves
    them with exact evidence; gauge versus absolute pressure is not specified and
    is not invented.", "owner_field_path": "preparation_steps[1]", "owner_decision":
    "verified"}, {"field_path": "preparation_steps (missing)", "decision": "add",
    "stage": "main sterilization", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1057",
    "source_sha256": "572017c9f4e1f79091b3c14d07c3a38f58e705c7e7ff084391980e4f2af92897",
    "source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C
    for 15 min.", "source_locator": "page-level default together with recipe-specific
    autoclave sentence", "explanation": "The exact JCM 1057 page states this default
    and its main recipe calls for autoclaving without an alternate setting. Neither
    local layer spells out the numeric settings. Do not apply the default to the separately
    filter-sterilized vitamin stock.", "owner_field_path": "preparation_steps[1]",
    "owner_decision": "add"}, {"field_path": "solutions[2].preparation_notes (missing)",
    "decision": "add", "stage": "innermost trace before mineral additions", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151", "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "adjust pH to 6.5 with KOH solution.", "source_locator": "Trace
    minerals preparation", "explanation": "The owner already preserves initial stock
    pH 6.5 and exact root evidence. This is not main-medium pH.", "owner_field_path":
    "solutions[1].solutions[0].preparation_notes", "owner_decision": "verified"},
    {"field_path": "solutions[2].preparation_notes (missing)", "decision": "add",
    "stage": "innermost trace final adjustment", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
    "source_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
    "source_quote": "Adjust final pH to 7.0.", "source_locator": "Trace minerals preparation
    final sentence", "explanation": "Final stock pH 7.0 is already correctly retained
    in the owner with exact evidence. No main pH is inferred.", "owner_field_path":
    "solutions[1].solutions[0].preparation_notes", "owner_decision": "verified"},
    {"field_path": "solutions[0].preparation_notes (missing)", "decision": "add",
    "stage": "vitamin stock sterilization only", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
    "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
    "source_quote": "and Trace vitamins while gassing       with N 2 .", "source_locator":
    "main paragraph, named trace-vitamin filtration clause", "explanation": "The immediately
    preceding filter-sterilize instruction explicitly applies to Trace vitamins under
    nitrogen. No gas fraction, filtration pore size, basal gas mixture or unrelated
    8% bicarbonate/5% reagent stock is transferred.", "owner_field_path": "solutions[0].preparation_notes
    (missing)", "owner_decision": "add"}]'
- assessment_id: identity
  area: identity
  topic: Exact main and stock identities
  outcome: supported
  summary: TOGO M1124 explicitly identifies JCM 1057. Its vitamin reference M190 maps
    to JCM 197 and its nested mineral reference M142 maps to JCM 151. These are subsection
    dependencies, not whole-medium equivalences. One maintained owner is explicitly
    named by the merge history.
  target_ids:
  - CultureMech:007645
  evidence_ids:
  - record
  - owner-0
  - primary
  - togo
  - vit-api
  - vit-primary
  - trace-api
  - trace-primary
  - id-search
- assessment_id: owner-evidence
  area: evidence
  topic: Existing owner evidence and batch representation
  outcome: supported
  summary: The owner has 31 evidence objects, with additional exact excerpts specifying
    all three stock doses and main/stock preparation. Literal snippets and historical
    response hashes match current captures. These verify existing owner batch amounts,
    units and stage explanations; they do not verify removed final g/L or correct
    chemical grounding. The target has none of this evidence.
  target_ids:
  - CultureMech:007645
  evidence_ids:
  - owner-0
  - owner-evidence
  - togo
  - trace-api
  - quantities
- assessment_id: formulation
  area: consistency
  topic: Every direct, inline and nested-stock quantity
  outcome: concern
  summary: Target water, stock doses and resazurin have wrong units; nickel and selenite
    remain flattened at wrong stages and the latter also carries a mg-to-g error.
    The owner correctly withdrew unsupported final concentrations, preserving batch
    mass evidence. Its custom trace and nested M142 composition are restored, while
    its vitamin composition remains empty. No numeric final medium concentration is
    inferred from one litre of input water.
  target_ids:
  - CultureMech:007645
  evidence_ids:
  - record
  - owner-0
  - primary
  - togo
  - vit-primary
  - trace-primary
  - quantities
- assessment_id: forms
  area: grounding
  topic: Exact supplied forms and bounded stock identities
  outcome: concern
  summary: Sodium acetate trihydrate maps to CHEBI:32954, formula C2H3NaO2, and nickel
    chloride hexahydrate maps to CHEBI:34887, formula Cl2Ni. These terms omit the
    stated hydrate. The owner retained both unresolved groundings during quantity
    repair. Other asserted direct forms agree with source wording; nested M142 ingredients
    have no newly invented ontology links. Unspecified manganese hydration, aluminum-potassium
    sulfate hydration and vitamin pantothenate stereochemistry remain unresolved.
  target_ids:
  - CultureMech:007645
  evidence_ids:
  - record
  - owner-0
  - primary
  - trace-primary
  - vit-primary
  - chebi32954
  - chebi34887
  - mim
- assessment_id: preparation
  area: completeness
  topic: Main preparation and stock-specific processing
  outcome: concern
  summary: Generated preparation is absent; the owner correctly retains main boiling/cooling,
    staged additions, bottle pressure and trace-stock pH. Both layers omit the numerical
    JCM sterilization default and explicit vitamin preparation. The intentionally
    unquantified KOH node is not a missing fixed formulation. Main pH and incubation
    duration/temperature are not asserted by these sources and are not inferred.
  target_ids:
  - CultureMech:007645
  evidence_ids:
  - record
  - owner-0
  - primary
  - vit-primary
  - trace-primary
  - quantities
- assessment_id: classification
  area: scope
  topic: Mixture class and biological scope
  outcome: supported
  summary: COMPLEX/UNDEFINED and LIQUID are consistent with yeast extract/trypticase
    and no solidifier. Imported roles and property notes are recognizable provider
    annotations, not independent experimental mechanisms; no structured target-organism,
    incubation, KG, or strain-variant claim is made. The title alone does not establish
    growth.
  target_ids:
  - CultureMech:007645
  evidence_ids:
  - record
  - owner-0
  - primary
  - togo
- assessment_id: history
  area: provenance
  topic: Derived-output lag and append-only repair history
  outcome: concern
  summary: The August generated target predates the October RESTORED_NESTED_M142_TRACE_STOCKS_WITH_EVIDENCE
    owner event. All timestamps are timezone-aware. The full serialized repair changes
    and source excerpts distinguish corrected units, withheld final concentrations,
    nested stock restoration and intentionally unresolved gases/grounding. Current
    merge code is not blamed for an unexecuted regeneration.
  target_ids:
  - CultureMech:007645
  evidence_ids:
  - record
  - owner-0
  - owner-evidence
  - writer
  - quantities
findings:
- finding_id: f1
  issue_key: CM007645-stale-formulation
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated recipe retains superseded units and flattened stock stages
  description: The target stores water as 1 g/L, resazurin as 1 g/L rather than source
    1 mg per batch, stock additions as g/L, and nickel/selenite as direct ingredients.
    Its empty mineral stubs omit the nested composition already repaired with evidence
    in the owner.
  target_ids:
  - CultureMech:007645
  field_paths:
  - ingredients
  - solutions
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - primary
  - togo
  - trace-primary
  - owner-evidence
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml
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
  issue_key: CM007645-vitamin-composition
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Resolvable trace-vitamin stock remains empty
  description: Both layers leave the M190/JCM 197 trace-vitamin composition empty
    despite its exact ten-vitamin and water recipe and the stated 10 ml dose. This
    differs from the intentionally unquantified KOH adjustment node.
  target_ids:
  - CultureMech:007645
  field_paths:
  - solutions[0].composition
  - solutions[0].name
  evidence_ids:
  - record
  - owner-0
  - primary
  - vit-primary
  - vit-api
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml
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
  issue_key: CM007645-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two retained ontology terms omit source hydrate identities
  description: Sodium acetate trihydrate is linked to anhydrous sodium acetate and
    nickel hexahydrate to anhydrous nickel dichloride. October quantity evidence explicitly
    did not recertify chemical grounding.
  target_ids:
  - CultureMech:007645
  field_paths:
  - ingredients[9].term
  - ingredients[16].term
  - solutions (owner custom-trace nickel term)
  evidence_ids:
  - record
  - owner-0
  - primary
  - chebi32954
  - chebi34887
  - owner-evidence
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml
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
  issue_key: CM007645-preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation and stock processing are incomplete in derived output
  description: The generated recipe omits all preparation; the owner preserves main
    and nested-trace stages but leaves vitamin preparation and the explicit main JCM
    sterilization default unrepresented.
  target_ids:
  - CultureMech:007645
  field_paths:
  - preparation_steps
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - vit-primary
  - trace-primary
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml
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
  issue_key: CM007645-evidence-lineage
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated output omits the repaired owner evidence and references
  description: The target has no October source excerpts, narrow stock-dose explanations
    or appended repair event. The current owner already has verifiable source content;
    this is derived lag rather than absent owner provenance.
  target_ids:
  - CultureMech:007645
  field_paths:
  - evidence
  - references
  - ingredients[*].evidence
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - owner-evidence
  - writer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml
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
  description: Preserve the verified owner repair, reconcile remaining issues, then
    regenerate and confirm exact batch units, nested scopes and evidence survive.
    Do not reintroduce unsupported final g/L.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007645
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml
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
  description: Restore only the named vitamin subsection with its original amounts,
    forms and dose; give the stock an informative source-supported name. Exclude JCM
    197 basal/mineral formulation.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007645
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml
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
  description: Verify exact hydrate representations or leave their grounding explicitly
    unresolved; preserve supported quantities without substituting anhydrous forms.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007645
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml
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
  description: Retain verified owner stages, add exact missing stock/default context
    with source scope, and keep trace pH separate from unspecified main pH. Preserve
    unquantified gas flow and KOH.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007645
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml
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
  description: Carry existing source evidence, original timestamps and history through
    an authorized regeneration after source reconciliation; do not invent historical
    provenance or rewrite prior events.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:007645
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml
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
- Main water and stock input volumes are not independently measured final volumes.
  Batch masses are retained without assuming final g/L.
- Only the named JCM 197 trace-vitamin subsection and JCM 151 trace-mineral subsection
  are dependencies; their basal media, other stocks and organism conditions are excluded.
  MnSO4 xH2O and aluminum-potassium sulfate hydrate state remain as stated, without
  inventing a hydrate count.
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
