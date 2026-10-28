# Source and formulation review: a1_medium (CultureMech:002863)

- Review: 20261021T092835Z-culturemech-002863-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T09:12:13Z
- Finished UTC: 2026-10-21T09:28:35Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated record and its one maintained owner flatten five separately prepared stocks into 31 direct ingredients, including three sums across incompatible concentration bases. The complete JCM and MediaDive formulations support reconstruction of stock relationships, while material-form, stereochemical, preparation and secondary-linkage issues remain explicit.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 130; batch 013 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twelve task batches contain 120 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 122 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002863 | data/merge_yaml/merged/A1_MEDIUM.yaml | generated | a1_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002863 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002863 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch013/130/strict.tsv |
| validate-terms | passed | True | CultureMech:002863 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002863 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002863 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002863.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: concern. Targets: CultureMech:002863.

31 primary CHEBI identities resolve with matching labels; 29 of 30 current secondary keys have live pinned-index rows. Unresolved keys: ['CHEBI:30314'].

31 direct ingredient instances; CHEBI-primary instance linkage 31/31 (100.00%), verified secondary coverage 29/31 (93.55%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Exact JCM origin and MediaDive representation

identity: supported. Targets: CultureMech:002863.

CultureMech:002863 identifies JCM recipe 512, exposed by DSMZ MediaDive as J512. The source name, term and original link agree. One normalized owner supplies this generated record; matching names alone do not establish equivalence with unrelated A1 media.

### Complete stage-specific quantity reconciliation

quantity: concern. Targets: CultureMech:002863.

All 31 target/owner ingredient amounts are covered by 42 source recipe rows and eight preparation decisions. NaCl sums 19.6078 + 1.0; magnesium sulfate sums 0.196078 + 3.0; calcium chloride sums 0.1 + 30.4. Those operands come from different main/stock bases and cannot be added directly. Values such as 212, 40 and 90.1 g/L are stock concentrations, not final medium concentrations. Main-only KCl, NH4Cl, KH2PO4 and NaHCO3 values match provider normalization but retain its declared main-stage basis.

[{"source_row": "0:0", "field_paths": ["ingredients[0].concentration"], "target_index": 0, "record_value": {"value": "20.6078", "unit": "G_PER_L"}, "owner_value": {"value": "20.6078", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[0].concentration", "ingredient": "NaCl", "decision": "correct", "stage": "Main sol. J512", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 Main sol. J512 recipe row 1", "source_quote": "NaCl 20.0 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[0].recipe[0]", "provider_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 19.6078,\n                        \"mmol_l\": 335.521,\n                        \"optional\": 0\n                    }", "provider_original_amount": 20, "provider_original_unit": "g", "provider_g_l": 19.6078, "provider_volume_ml": 1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation": "This is a main-mixture amount. Preserve the literal primary mass and provider-declared 1020 ml basis separately from the later tube additions and measured final volume. The current value also sums entries from different source stages; undo that unsupported cross-stage sum before any downstream concentration calculation."}, {"source_row": "0:1", "field_paths": ["ingredients[1].concentration"], "target_index": 1, "record_value": {"value": "0.754902", "unit": "G_PER_L"}, "owner_value": {"value": "0.754902", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[1].concentration", "ingredient": "KCl", "decision": "evidence_only", "stage": "Main sol. J512", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 Main sol. J512 recipe row 2", "source_quote": "KCl 0.77 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[0].recipe[1]", "provider_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.77,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.754902,\n                        \"mmol_l\": 10.1261,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.77, "provider_original_unit": "g", "provider_g_l": 0.754902, "provider_volume_ml": 1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation": "This is a main-mixture amount. Preserve the literal primary mass and provider-declared 1020 ml basis separately from the later tube additions and measured final volume."}, {"source_row": "0:2", "field_paths": ["ingredients[2].concentration"], "target_index": 2, "record_value": {"value": "0.245098", "unit": "G_PER_L"}, "owner_value": {"value": "0.245098", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[2].concentration", "ingredient": "NH4Cl", "decision": "evidence_only", "stage": "Main sol. J512", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 Main sol. J512 recipe row 3", "source_quote": "NH 4 Cl 0.25 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[0].recipe[2]", "provider_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.245098,\n                        \"mmol_l\": 4.58213,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.25, "provider_original_unit": "g", "provider_g_l": 0.245098, "provider_volume_ml": 1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation": "This is a main-mixture amount. Preserve the literal primary mass and provider-declared 1020 ml basis separately from the later tube additions and measured final volume."}, {"source_row": "0:3", "field_paths": ["ingredients[3].concentration"], "target_index": 3, "record_value": {"value": "0.0980392", "unit": "G_PER_L"}, "owner_value": {"value": "0.0980392", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[3].concentration", "ingredient": "KH2PO4", "decision": "evidence_only", "stage": "Main sol. J512", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 Main sol. J512 recipe row 4", "source_quote": "KH 2 PO 4 0.1 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[0].recipe[3]", "provider_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0980392,\n                        \"mmol_l\": 0.720421,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.1, "provider_original_unit": "g", "provider_g_l": 0.0980392, "provider_volume_ml": 1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation": "This is a main-mixture amount. Preserve the literal primary mass and provider-declared 1020 ml basis separately from the later tube additions and measured final volume."}, {"source_row": "0:4", "field_paths": ["ingredients[4].concentration"], "target_index": 4, "record_value": {"value": "3.196078", "unit": "G_PER_L"}, "owner_value": {"value": "3.196078", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[4].concentration", "ingredient": "MgSO4 x 7 H2O", "decision": "correct", "stage": "Main sol. J512", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 Main sol. J512 recipe row 5", "source_quote": "MgSO 4 ·7H 2 O 0.2 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[0].recipe[4]", "provider_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.196078,\n                        \"mmol_l\": 0.795527,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.2, "provider_original_unit": "g", "provider_g_l": 0.196078, "provider_volume_ml": 1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation": "This is a main-mixture amount. Preserve the literal primary mass and provider-declared 1020 ml basis separately from the later tube additions and measured final volume. The current value also sums entries from different source stages; undo that unsupported cross-stage sum before any downstream concentration calculation."}, {"source_row": "0:5", "field_paths": ["solutions"], "ingredient": "DL vitamins (refrigerated)", "decision": "add", "stage": "Main sol. J512", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 Main sol. J512 recipe row 6", "source_quote": "DL vitamins (see below) 10.0 ml", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[0].recipe[5]", "provider_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"DL vitamins (refrigerated)\",\n                        \"solution_id\": 4294,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount": 10, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml": 1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation": "The source gives a stock addition missing as a structured solution relationship. Preserve its literal volume and source main-batch basis; do not silently convert this to an addition per measured final liter."}, {"source_row": "0:6", "field_paths": ["solutions"], "ingredient": "DL minerals (refrigerated)", "decision": "add", "stage": "Main sol. J512", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 Main sol. J512 recipe row 7", "source_quote": "DL minerals (see below) 10.0 ml", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[0].recipe[6]", "provider_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"DL minerals (refrigerated)\",\n                        \"solution_id\": 4293,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount": 10, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml": 1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation": "The source gives a stock addition missing as a structured solution relationship. Preserve its literal volume and source main-batch basis; do not silently convert this to an addition per measured final liter."}, {"source_row": "0:7", "field_paths": ["ingredients[5].concentration"], "target_index": 5, "record_value": {"value": "1.96078", "unit": "G_PER_L"}, "owner_value": {"value": "1.96078", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[5].concentration", "ingredient": "NaHCO3", "decision": "evidence_only", "stage": "Main sol. J512", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 Main sol. J512 recipe row 8", "source_quote": "NaHCO 3 2.0 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[0].recipe[7]", "provider_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.96078,\n                        \"mmol_l\": 23.3407,\n                        \"optional\": 0\n                    }", "provider_original_amount": 2, "provider_original_unit": "g", "provider_g_l": 1.96078, "provider_volume_ml": 1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation": "This is a main-mixture amount. Preserve the literal primary mass and provider-declared 1020 ml basis separately from the later tube additions and measured final volume."}, {"source_row": "0:8", "field_paths": ["preparation_steps"], "ingredient": "Distilled water", "decision": "add", "stage": "Main sol. J512", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 Main sol. J512 recipe row 9", "source_quote": "Distilled water 1.0 L", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[0].recipe[8]", "provider_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount": 1000, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml": 1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation": "This solvent amount belongs to the named preparation stage. Preserve it as solvent/batch context, without adding a second independent chemical ingredient edge or claiming measured final volume."}, {"source_row": "1:0", "field_paths": ["ingredients[6].concentration"], "target_index": 6, "record_value": {"value": "1.5", "unit": "G_PER_L"}, "owner_value": {"value": "1.5", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[6].concentration", "ingredient": "Nitrilotriacetic acid", "decision": "correct", "stage": "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 1", "source_quote": "Nitrilotriacetic acid, trisodium salt 1.5 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[1].recipe[0]", "provider_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"condition\": \" trisodium salt\",\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }", "provider_original_amount": 1.5, "provider_original_unit": "g", "provider_g_l": 1.5, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration."}, {"source_row": "1:1", "field_paths": ["ingredients[4].concentration"], "target_index": 4, "record_value": {"value": "3.196078", "unit": "G_PER_L"}, "owner_value": {"value": "3.196078", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[4].concentration", "ingredient": "MgSO4 x 7 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 2", "source_quote": "MgSO 4 ·7H 2 O 3.0 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[1].recipe[1]", "provider_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }", "provider_original_amount": 3, "provider_original_unit": "g", "provider_g_l": 3, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration. The current value also sums entries from different source stages; undo that unsupported cross-stage sum before any downstream concentration calculation."}, {"source_row": "1:2", "field_paths": ["ingredients[7].concentration"], "target_index": 7, "record_value": {"value": "0.5", "unit": "G_PER_L"}, "owner_value": {"value": "0.5", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[7].concentration", "ingredient": "MnSO4 x n H2O", "decision": "correct", "stage": "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 3", "source_quote": "MnSO 4 · x H 2 O 0.5 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[1].recipe[2]", "provider_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x n H2O\",\n                        \"compound_id\": 1000,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.5, "provider_original_unit": "g", "provider_g_l": 0.5, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration."}, {"source_row": "1:3", "field_paths": ["ingredients[0].concentration"], "target_index": 0, "record_value": {"value": "20.6078", "unit": "G_PER_L"}, "owner_value": {"value": "20.6078", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[0].concentration", "ingredient": "NaCl", "decision": "correct", "stage": "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 4", "source_quote": "NaCl 1.0 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[1].recipe[3]", "provider_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }", "provider_original_amount": 1, "provider_original_unit": "g", "provider_g_l": 1, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration. The current value also sums entries from different source stages; undo that unsupported cross-stage sum before any downstream concentration calculation."}, {"source_row": "1:4", "field_paths": ["ingredients[8].concentration"], "target_index": 8, "record_value": {"value": "0.1", "unit": "G_PER_L"}, "owner_value": {"value": "0.1", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[8].concentration", "ingredient": "FeSO4 x 7 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 5", "source_quote": "FeSO 4 ·7H 2 O 0.1 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[1].recipe[4]", "provider_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.1, "provider_original_unit": "g", "provider_g_l": 0.1, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration."}, {"source_row": "1:5", "field_paths": ["ingredients[9].concentration"], "target_index": 9, "record_value": {"value": "30.5", "unit": "G_PER_L"}, "owner_value": {"value": "30.5", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[9].concentration", "ingredient": "CaCl2 x 2 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 6", "source_quote": "CaCl 2 ·2H 2 O 0.1 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[1].recipe[5]", "provider_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.1, "provider_original_unit": "g", "provider_g_l": 0.1, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration. The current value also sums entries from different source stages; undo that unsupported cross-stage sum before any downstream concentration calculation."}, {"source_row": "1:6", "field_paths": ["ingredients[10].concentration"], "target_index": 10, "record_value": {"value": "0.1", "unit": "G_PER_L"}, "owner_value": {"value": "0.1", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[10].concentration", "ingredient": "CoCl2 x 6 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 7", "source_quote": "CoCl 2 ·6H 2 O 0.1 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[1].recipe[6]", "provider_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.770185,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.1, "provider_original_unit": "g", "provider_g_l": 0.1, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration."}, {"source_row": "1:7", "field_paths": ["ingredients[11].concentration"], "target_index": 11, "record_value": {"value": "0.13", "unit": "G_PER_L"}, "owner_value": {"value": "0.13", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[11].concentration", "ingredient": "ZnCl2", "decision": "correct", "stage": "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 8", "source_quote": "ZnCl 2 0.13 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[1].recipe[7]", "provider_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 0.13,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.13,\n                        \"mmol_l\": 0.953778,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.13, "provider_original_unit": "g", "provider_g_l": 0.13, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration."}, {"source_row": "1:8", "field_paths": ["ingredients[12].concentration"], "target_index": 12, "record_value": {"value": "0.01", "unit": "G_PER_L"}, "owner_value": {"value": "0.01", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[12].concentration", "ingredient": "CuSO4 x 5 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 9", "source_quote": "CuSO 4 ·5H 2 O 0.01 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[1].recipe[8]", "provider_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.01, "provider_original_unit": "g", "provider_g_l": 0.01, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration."}, {"source_row": "1:9", "field_paths": ["ingredients[13].concentration"], "target_index": 13, "record_value": {"value": "0.01", "unit": "G_PER_L"}, "owner_value": {"value": "0.01", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[13].concentration", "ingredient": "AlK(SO4)2 x 12 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 10", "source_quote": "AlK(SO 4 ) 2 ·12H 2 O 0.01 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[1].recipe[9]", "provider_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0210798,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.01, "provider_original_unit": "g", "provider_g_l": 0.01, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration."}, {"source_row": "1:10", "field_paths": ["ingredients[14].concentration"], "target_index": 14, "record_value": {"value": "0.01", "unit": "G_PER_L"}, "owner_value": {"value": "0.01", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[14].concentration", "ingredient": "H3BO3", "decision": "correct", "stage": "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 11", "source_quote": "H 3 BO 3 0.01 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[1].recipe[10]", "provider_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.01, "provider_original_unit": "g", "provider_g_l": 0.01, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration."}, {"source_row": "1:11", "field_paths": ["ingredients[15].concentration"], "target_index": 15, "record_value": {"value": "0.025", "unit": "G_PER_L"}, "owner_value": {"value": "0.025", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[15].concentration", "ingredient": "Na2MoO4 x 2 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 12", "source_quote": "Na 2 MoO 4 ·2H 2 O 0.025 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[1].recipe[11]", "provider_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.025,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.025,\n                        \"mmol_l\": 0.103327,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.025, "provider_original_unit": "g", "provider_g_l": 0.025, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration."}, {"source_row": "1:12", "field_paths": ["ingredients[16].concentration"], "target_index": 16, "record_value": {"value": "0.024", "unit": "G_PER_L"}, "owner_value": {"value": "0.024", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[16].concentration", "ingredient": "NiCl2 x 6 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 13", "source_quote": "NiCl 2 ·6H 2 O 0.024 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[1].recipe[12]", "provider_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.024,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.024, "provider_original_unit": "g", "provider_g_l": 0.024, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration."}, {"source_row": "1:13", "field_paths": ["ingredients[17].concentration"], "target_index": 17, "record_value": {"value": "0.025", "unit": "G_PER_L"}, "owner_value": {"value": "0.025", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[17].concentration", "ingredient": "Na2WO4 x 2 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 14", "source_quote": "Na 2 WO 4 ·2H 2 O 0.025 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[1].recipe[13]", "provider_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.025,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.025,\n                        \"mmol_l\": 0.075792,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.025, "provider_original_unit": "g", "provider_g_l": 0.025, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration."}, {"source_row": "1:14", "field_paths": ["preparation_steps"], "ingredient": "Distilled water", "decision": "add", "stage": "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 15", "source_quote": "Distilled water 1.0 L", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[1].recipe[14]", "provider_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount": 1000, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "This solvent amount belongs to the named preparation stage. Preserve it as solvent/batch context, without adding a second independent chemical ingredient edge or claiming measured final volume."}, {"source_row": "2:0", "field_paths": ["ingredients[18].concentration"], "target_index": 18, "record_value": {"value": "0.002", "unit": "G_PER_L"}, "owner_value": {"value": "0.002", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[18].concentration", "ingredient": "Biotin", "decision": "correct", "stage": "DL vitamins (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 1", "source_quote": "Biotin 0.002 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[2].recipe[0]", "provider_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00818632,\n                        \"optional\": 0\n                    }", "provider_original_amount": 2, "provider_original_unit": "mg", "provider_g_l": 0.002, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration. The provider uses mg while JCM states the equivalent mass in g; both original representations are retained."}, {"source_row": "2:1", "field_paths": ["ingredients[19].concentration"], "target_index": 19, "record_value": {"value": "0.005", "unit": "G_PER_L"}, "owner_value": {"value": "0.005", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[19].concentration", "ingredient": "Pantothenic acid", "decision": "correct", "stage": "DL vitamins (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 2", "source_quote": "Pantothenic acid 0.005 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[2].recipe[1]", "provider_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Pantothenic acid\",\n                        \"compound_id\": 135,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0228071,\n                        \"optional\": 0\n                    }", "provider_original_amount": 5, "provider_original_unit": "mg", "provider_g_l": 0.005, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration. The provider uses mg while JCM states the equivalent mass in g; both original representations are retained."}, {"source_row": "2:2", "field_paths": ["ingredients[20].concentration"], "target_index": 20, "record_value": {"value": "0.0001", "unit": "G_PER_L"}, "owner_value": {"value": "0.0001", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[20].concentration", "ingredient": "Vitamin B12", "decision": "correct", "stage": "DL vitamins (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 3", "source_quote": "Vitamin B 1 2 0.0001 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[2].recipe[2]", "provider_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\": 7.3779e-5,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.1, "provider_original_unit": "mg", "provider_g_l": 0.0001, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration. The provider uses mg while JCM states the equivalent mass in g; both original representations are retained."}, {"source_row": "2:3", "field_paths": ["ingredients[21].concentration"], "target_index": 21, "record_value": {"value": "0.005", "unit": "G_PER_L"}, "owner_value": {"value": "0.005", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[21].concentration", "ingredient": "p-Aminobenzoic acid", "decision": "correct", "stage": "DL vitamins (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 4", "source_quote": "p -Aminobenzoic acid 0.005 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[2].recipe[3]", "provider_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0364591,\n                        \"optional\": 0\n                    }", "provider_original_amount": 5, "provider_original_unit": "mg", "provider_g_l": 0.005, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration. The provider uses mg while JCM states the equivalent mass in g; both original representations are retained."}, {"source_row": "2:4", "field_paths": ["ingredients[22].concentration"], "target_index": 22, "record_value": {"value": "0.005", "unit": "G_PER_L"}, "owner_value": {"value": "0.005", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[22].concentration", "ingredient": "Thioctic acid", "decision": "correct", "stage": "DL vitamins (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 5", "source_quote": "Thioctic acid 0.005 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[2].recipe[4]", "provider_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Thioctic acid\",\n                        \"compound_id\": 535,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0242365,\n                        \"optional\": 0\n                    }", "provider_original_amount": 5, "provider_original_unit": "mg", "provider_g_l": 0.005, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration. The provider uses mg while JCM states the equivalent mass in g; both original representations are retained."}, {"source_row": "2:5", "field_paths": ["ingredients[23].concentration"], "target_index": 23, "record_value": {"value": "0.005", "unit": "G_PER_L"}, "owner_value": {"value": "0.005", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[23].concentration", "ingredient": "Nicotinic acid", "decision": "correct", "stage": "DL vitamins (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 6", "source_quote": "Nicotinic acid 0.005 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[2].recipe[5]", "provider_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0406141,\n                        \"optional\": 0\n                    }", "provider_original_amount": 5, "provider_original_unit": "mg", "provider_g_l": 0.005, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration. The provider uses mg while JCM states the equivalent mass in g; both original representations are retained."}, {"source_row": "2:6", "field_paths": ["ingredients[24].concentration"], "target_index": 24, "record_value": {"value": "0.005", "unit": "G_PER_L"}, "owner_value": {"value": "0.005", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[24].concentration", "ingredient": "Thiamine HCl", "decision": "correct", "stage": "DL vitamins (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 7", "source_quote": "Thiamine·HCl 0.005 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[2].recipe[6]", "provider_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"optional\": 0\n                    }", "provider_original_amount": 5, "provider_original_unit": "mg", "provider_g_l": 0.005, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration. The provider uses mg while JCM states the equivalent mass in g; both original representations are retained."}, {"source_row": "2:7", "field_paths": ["ingredients[25].concentration"], "target_index": 25, "record_value": {"value": "0.005", "unit": "G_PER_L"}, "owner_value": {"value": "0.005", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[25].concentration", "ingredient": "Riboflavin", "decision": "correct", "stage": "DL vitamins (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 8", "source_quote": "Riboflavin 0.005 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[2].recipe[7]", "provider_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0132837,\n                        \"optional\": 0\n                    }", "provider_original_amount": 5, "provider_original_unit": "mg", "provider_g_l": 0.005, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration. The provider uses mg while JCM states the equivalent mass in g; both original representations are retained."}, {"source_row": "2:8", "field_paths": ["ingredients[26].concentration"], "target_index": 26, "record_value": {"value": "0.01", "unit": "G_PER_L"}, "owner_value": {"value": "0.01", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[26].concentration", "ingredient": "Pyridoxine hydrochloride", "decision": "correct", "stage": "DL vitamins (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 9", "source_quote": "Pyridoxine·HCl 0.01 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[2].recipe[8]", "provider_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.01, "provider_original_unit": "g", "provider_g_l": 0.01, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration."}, {"source_row": "2:9", "field_paths": ["ingredients[27].concentration"], "target_index": 27, "record_value": {"value": "0.002", "unit": "G_PER_L"}, "owner_value": {"value": "0.002", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[27].concentration", "ingredient": "Folic acid", "decision": "correct", "stage": "DL vitamins (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 10", "source_quote": "Folic acid 0.002 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[2].recipe[9]", "provider_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00453104,\n                        \"optional\": 0\n                    }", "provider_original_amount": 2, "provider_original_unit": "mg", "provider_g_l": 0.002, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration. The provider uses mg while JCM states the equivalent mass in g; both original representations are retained."}, {"source_row": "2:10", "field_paths": ["preparation_steps"], "ingredient": "Distilled water", "decision": "add", "stage": "DL vitamins (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 11", "source_quote": "Distilled water 1.0 L", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[2].recipe[10]", "provider_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount": 1000, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation": "This solvent amount belongs to the named preparation stage. Preserve it as solvent/batch context, without adding a second independent chemical ingredient edge or claiming measured final volume."}, {"source_row": "3:0", "field_paths": ["ingredients[28].concentration"], "target_index": 28, "record_value": {"value": "212", "unit": "G_PER_L"}, "owner_value": {"value": "212", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[28].concentration", "ingredient": "MgCl2 x 6 H2O", "decision": "correct", "stage": "APM salts solution (autoclaved)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 APM salts solution (autoclaved) recipe row 1", "source_quote": "MgCl 2 ·6H 2 O 21.2 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[3].recipe[0]", "provider_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 21.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 212,\n                        \"mmol_l\": 1042.78,\n                        \"optional\": 0\n                    }", "provider_original_amount": 21.2, "provider_original_unit": "g", "provider_g_l": 212, "provider_volume_ml": 100, "provider_volume_locator": "$.data.solutions[3].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration."}, {"source_row": "3:1", "field_paths": ["ingredients[9].concentration"], "target_index": 9, "record_value": {"value": "30.5", "unit": "G_PER_L"}, "owner_value": {"value": "30.5", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[9].concentration", "ingredient": "CaCl2 x 2 H2O", "decision": "correct", "stage": "APM salts solution (autoclaved)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 APM salts solution (autoclaved) recipe row 2", "source_quote": "CaCl 2 ·2H 2 O 3.04 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[3].recipe[1]", "provider_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 3.04,\n                        \"unit\": \"g\",\n                        \"g_l\": 30.4,\n                        \"mmol_l\": 206.782,\n                        \"optional\": 0\n                    }", "provider_original_amount": 3.04, "provider_original_unit": "g", "provider_g_l": 30.4, "provider_volume_ml": 100, "provider_volume_locator": "$.data.solutions[3].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration. The current value also sums entries from different source stages; undo that unsupported cross-stage sum before any downstream concentration calculation."}, {"source_row": "3:2", "field_paths": ["preparation_steps"], "ingredient": "Distilled water", "decision": "add", "stage": "APM salts solution (autoclaved)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 APM salts solution (autoclaved) recipe row 3", "source_quote": "Distilled water 100.0 ml", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[3].recipe[2]", "provider_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount": 100, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml": 100, "provider_volume_locator": "$.data.solutions[3].volume", "explanation": "This solvent amount belongs to the named preparation stage. Preserve it as solvent/batch context, without adding a second independent chemical ingredient edge or claiming measured final volume."}, {"source_row": "4:0", "field_paths": ["ingredients[29].concentration"], "target_index": 29, "record_value": {"value": "40", "unit": "G_PER_L"}, "owner_value": {"value": "40", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[29].concentration", "ingredient": "Na2S x 9 H2O", "decision": "correct", "stage": "Sulfide stock solution (autoclaved)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 Sulfide stock solution (autoclaved) recipe row 1", "source_quote": "Na 2 S·9H 2 O 0.4 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[4].recipe[0]", "provider_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 40,\n                        \"mmol_l\": 166.54,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.4, "provider_original_unit": "g", "provider_g_l": 40, "provider_volume_ml": 10, "provider_volume_locator": "$.data.solutions[4].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration."}, {"source_row": "4:1", "field_paths": ["preparation_steps"], "ingredient": "Distilled water", "decision": "add", "stage": "Sulfide stock solution (autoclaved)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 Sulfide stock solution (autoclaved) recipe row 2", "source_quote": "Distilled water 10.0 ml", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[4].recipe[1]", "provider_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount": 10, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml": 10, "provider_volume_locator": "$.data.solutions[4].volume", "explanation": "This solvent amount belongs to the named preparation stage. Preserve it as solvent/batch context, without adding a second independent chemical ingredient edge or claiming measured final volume."}, {"source_row": "5:0", "field_paths": ["ingredients[30].concentration"], "target_index": 30, "record_value": {"value": "90.1", "unit": "G_PER_L"}, "owner_value": {"value": "90.1", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[30].concentration", "ingredient": "Galactose", "decision": "correct", "stage": "Galactose stock solution (filter-sterilized)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 Galactose stock solution (filter-sterilized) recipe row 1", "source_quote": "Galactose 0.901 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[5].recipe[0]", "provider_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Galactose\",\n                        \"compound_id\": 321,\n                        \"amount\": 0.901,\n                        \"unit\": \"g\",\n                        \"g_l\": 90.1,\n                        \"mmol_l\": 500.111,\n                        \"optional\": 0\n                    }", "provider_original_amount": 0.901, "provider_original_unit": "g", "provider_g_l": 90.1, "provider_volume_ml": 10, "provider_volume_locator": "$.data.solutions[5].volume", "explanation": "A stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve this stock basis and its separately stated addition; do not use undiluted stock strength as final medium concentration."}, {"source_row": "5:1", "field_paths": ["preparation_steps"], "ingredient": "Distilled water", "decision": "add", "stage": "Galactose stock solution (filter-sterilized)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 Galactose stock solution (filter-sterilized) recipe row 2", "source_quote": "Distilled water 10.0 ml", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator": "$.data.solutions[5].recipe[1]", "provider_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount": 10, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml": 10, "provider_volume_locator": "$.data.solutions[5].volume", "explanation": "This solvent amount belongs to the named preparation stage. Preserve it as solvent/batch context, without adding a second independent chemical ingredient edge or claiming measured final volume."}, {"field_paths": ["ph_value", "preparation_steps[0]"], "decision": "evidence_only", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 main preparation paragraph", "source_quote": "adjust pH to 6.8 and add NaHCO 3", "explanation": "The schema defines ph_value as a target pH. The recorded 6.8 target and the pre-bicarbonate adjustment stage already agree with the source in both layers. Preserve them and add exact claim-level support; no value removal or final-pH assertion is warranted."}, {"field_paths": ["preparation_steps[0]"], "decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 main preparation paragraph", "source_quote": "Dispense the medium (9 ml)", "explanation": "This is the main-mixture aliquot, not a final volume including the three later additions."}, {"field_paths": ["preparation_steps[0]"], "decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 main preparation paragraph", "source_quote": "26-ml anaerobic pressure tubes", "explanation": "This is vessel capacity, not medium volume or a concentration denominator."}, {"field_paths": ["preparation_steps[0]"], "decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 main preparation paragraph", "source_quote": "oxygen-free N 2 -CO 2 (80:20)", "explanation": "Preserve the stated gas ratio and atmosphere; this is not an incubation temperature or experimentally demonstrated optimum."}, {"field_paths": ["preparation_steps[0]", "solutions"], "decision": "evidence_only", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 main preparation paragraph", "source_quote": "0.2 ml APM salts solution", "explanation": "The addition is retained in prose but needs a resolvable relationship to the separately prepared APM stock; it is added after main-mixture autoclaving."}, {"field_paths": ["preparation_steps[0]", "solutions"], "decision": "evidence_only", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 main preparation paragraph", "source_quote": "0.1 ml Sulfide stock solution", "explanation": "The addition is retained in prose but needs its source stock recipe and separate autoclaving scope."}, {"field_paths": ["preparation_steps[0]", "solutions"], "decision": "evidence_only", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM 512 main preparation paragraph", "source_quote": "0.1 ml Galactose stock solution", "explanation": "The addition is retained in prose but needs its stock recipe and filter-sterilization exception."}, {"field_paths": ["sterilization", "preparation_steps"], "decision": "add", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674", "source_locator": "JCM page-wide default preceding recipe 512", "source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.", "explanation": "The primary page-wide default is absent; retain it only where no source exception applies. The galactose stock is explicitly filter-sterilized."}]

### Five stocks and both addition stages

representation: concern. Targets: CultureMech:002863.

The full sources define all five stock recipes. DL vitamins and DL minerals each enter the main mixture as 10 ml additions; APM, sulfide and galactose enter the dispensed aliquot later. The preparation prose preserves the three later doses but the record has no structured stock relationships or recipes. Removing stock-strength flat rows alone would lose source constituents unless the stock relationships are restored.

### Every asserted chemical form and secondary key

grounding: concern. Targets: CultureMech:002863.

All 31 primary canonical labels resolve, but neutral nitrilotriacetic acid is not the stated trisodium salt, nickel dichloride lacks the specified hexahydrate, and manganese sulfate has no water in its asserted formula despite source variable hydration. Thioctic acid is not specified as the R enantiomer. The generic vitamin B12 and galactose terms remain appropriately broad; no vitamer or stereoisomer is invented. Thirty secondary keys are asserted, with 29 live pinned-index matches and one absent lipoic key. The missing manganese secondary link remains unasserted, not fabricated.

### Solvents, storage, sterilization and pH stage

completeness: concern. Targets: CultureMech:002863.

The primary recipe supplies all six solvent quantities. Stock headings distinguish refrigerated DL solutions, autoclaved APM/sulfide stocks and filter-sterilized galactose. These scopes and page-default autoclave parameters are absent from the record. The main paragraph correctly retains anaerobic atmosphere, aliquot, vessel capacity and later addition order; The schema target pH 6.8 and its pre-bicarbonate adjustment stage are already correctly retained; they need claim-level evidence, not a value or stage correction.

### Defined mixture labels and growth boundaries

scope: concern. Targets: CultureMech:002863.

The record and provider classify this as defined, and the source has no complex extract or agar. LIQUID is consistent with the formulation. However, exact molecular composition is not completely resolved because manganese hydration and the B12 vitamer are unspecified; DEFINED must not be read as proof of fully specified chemistry. There is no asserted strain, native variant, parent, growth assay or external KG correspondence to validate.

### Append-only history and current-code boundaries

provenance: supported. Targets: CultureMech:002863.

All 8 target and 7 owner timestamps carry timezones. Owner history agrees with the target before its final merge event. The March cleanup reports three duplicate merges, consistent with three current merged-value notes, but no historical execution was reproduced. No source, owner, target or history bytes were edited.

### Exact source access and claim-level support

evidence: concern. Targets: CultureMech:002863.

The source URL is retained only in notes. Neither layer supplies native references or claim-level evidence for the stock hierarchy, quantities or chemical forms. Reference validation examined zero excerpts. Captured primary, provider and ontology versions and original access timestamps remain distinct; present source agreement is not retrospective proof of an earlier import.

## Findings

### f1: Five stock formulations are flattened and three cross-stage values are summed

blocker / open / confirmed; issue key: CM002863-stock-strength-flattening.

Both layers place all stock constituents in the direct ingredient list and add NaCl, magnesium sulfate and calcium chloride values across different volume bases. The source explicitly defines five stocks and separately timed additions. The flat values therefore misrepresent source quantities and make the stock preparation prose unresolved.

### f2: Three asserted chemical identities omit source salt or hydration

major / open / confirmed; issue key: CM002863-salt-hydrate-grounding.

The nitrilotriacetate material is explicitly trisodium salt, while CHEBI:44557 is neutral C6H9NO6. The nickel ingredient is a hexahydrate but CHEBI:34887 has formula Cl2Ni. The source manganese sulfate has variable hydration while CHEBI:86360 has no water in its formula. Canonical label passes and secondary MIM membership do not establish equivalence.

### f3: Generic thioctic acid is assigned a specific R enantiomer

major / open / confirmed; issue key: CM002863-thioctic-stereochemistry.

Both source versions say Thioctic acid without an enantiomer qualifier. The asserted primary and secondary CHEBI:30314 explicitly represent (R)-lipoic acid. The available source does not establish that stereochemical narrowing.

### f4: Solvent bases and stock-specific handling are incompletely retained

major / open / confirmed; issue key: CM002863-preparation-stock-context.

No solvent quantities or stock headings survive as structured preparation context. The DL stocks are refrigerated, APM and sulfide stocks are autoclaved, and galactose is filter-sterilized. The JCM page-default autoclave parameters are also absent. The existing main preparation paragraph and post-autoclave addition order should be retained.

### f5: The secondary lipoic key is absent from the pinned MIM index

minor / open / confirmed; issue key: CM002863-secondary-lipoic-link.

CHEBI:30314 is asserted as a secondary key but is absent from every row of the pinned index. Twenty-nine other secondary keys resolve in that snapshot. This linkage issue is separate from the source stereochemical overstatement.

### f6: Source notes do not provide claim-level stock and quantity support

minor / open / confirmed; issue key: CM002863-claim-evidence-gap.

Neither layer has native source references or evidence snippets for the quantities, stock recipes, material forms or handling conditions. The source link in notes and passing zero-excerpt reference check do not provide claim-level support. The already correct target pH and adjustment stage need only exact supporting evidence.

## Recommended Actions And Acceptance Checks

### a1

Restore all five source stock relationships and their individual recipes, solvent bases and addition stages in maintained inputs. Keep original masses and volumes with evidence, undo cross-stage sums, and derive any final concentration only after explicitly fixing the applicable volume basis. Preserve the three later additions that are present only in preparation text.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Reconcile each exact source material with verified ontology terms and preserve salt/hydrate qualifiers in both primary and secondary assertions. Leave the unspecified manganese hydration explicit; do not guess a particular hydrate or use an anhydrous molecular mass for the stated material.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the source generic material until source-specific stereochemistry is verified. Reconcile primary and secondary links against verified appropriately scoped terms, without guessing a replacement or changing canonical labels to hide the mismatch.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve the exact source solvent quantities, storage qualifiers and sterilization scopes for each stock and main mixture, with the galactose exception explicit. Retain source addition order and distinguish vessel capacity from liquid volume; do not invent storage temperatures or filter pore sizes.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Reconcile the secondary key against versioned authoritative MIM evidence after resolving source material scope. Preserve other verified links and leave unresolved correspondence explicit; do not infer a replacement from a similar name.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Add exact claim-level excerpts and locators to maintained source claims, distinguishing JCM origin from MediaDive hosting and preserving original capture versions/times. Confirm the evidence survives authorized regeneration without rewriting existing history.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/A1_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/A1_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/A1_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch013/130/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch013/130/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/A1_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/A1_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/A1_MEDIUM.yaml:1:id: CultureMech:002863<br>./data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:1:id: CultureMech:002863<br> |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15940 resolves to canonical label nicotinic acid; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15956 resolves to canonical label biotin; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17015 resolves to canonical label riboflavin; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:176843 resolves to canonical label vitamin B12; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to canonical label sodium chloride; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:27470 resolves to canonical label folic acid; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi28260 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28260; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:28260 resolves to canonical label galactose; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi30314 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30314; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:30314 resolves to canonical label (R)-lipoic acid; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:30753 resolves to canonical label 4-aminobenzoic acid; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:30961 resolves to canonical label pyridoxine hydrochloride; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31206 resolves to canonical label ammonium chloride; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31440 resolves to canonical label copper(II) sulfate pentahydrate; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31795 resolves to canonical label magnesium sulfate heptahydrate; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32139 resolves to canonical label sodium hydrogencarbonate; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32588 resolves to canonical label potassium chloride; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:33118 resolves to canonical label boric acid; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:34887 resolves to canonical label nickel dichloride; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:44557 resolves to canonical label nitrilotriacetic acid; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:49105 resolves to canonical label thiamine hydrochloride; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:49976 resolves to canonical label zinc dichloride; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:53503 resolves to canonical label cobalt chloride hexahydrate; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:63036 resolves to canonical label potassium dihydrogen phosphate; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:63939 resolves to canonical label sodium tungstate dihydrate; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:75213 resolves to canonical label sodium molybdate dihydrate; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:75836 resolves to canonical label iron(2+) sulfate heptahydrate; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:76209 resolves to canonical label sodium sulfide nonahydrate; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi7916 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_7916; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:7916 resolves to canonical label pantothenic acid; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86158 resolves to canonical label calcium chloride dihydrate; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86345 resolves to canonical label magnesium dichloride hexahydrate; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86360 resolves to canonical label manganese(II) sulfate; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86465 resolves to canonical label potassium aluminium sulfate dodecahydrate; the complete captured definition and formula annotations were inspected. Label agreement alone does not validate source salt, hydrate, stereochemistry or stock concentration. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | context_only | {"CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:7916": [{"label": "Pantothenic acid", "match_type": "preferred_term", "identifier": "CHEBI:7916", "preferred_term": "Pantothenic acid", "ontology_id": "CHEBI:7916", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30314": [], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:28260": [{"label": "Galactose", "match_type": "preferred_term", "identifier": "CHEBI:28260", "preferred_term": "Galactose", "ontology_id": "CHEBI:28260", "mapping_status": "MAPPED", "ambiguity": "unique"}]}; Unresolved current secondary keys: ['CHEBI:30314'] |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512; JCM 512 complete main formulation, preparation paragraph, five named stock subsections and page-wide default | supports | The primary source distinguishes a main mixture from DL minerals, DL vitamins, APM salts, sulfide and galactose stocks. Every stock has its own solvent basis and addition stage. Refrigeration and sterilization methods are stated in stock headings; the page-wide default is qualified by explicit exceptions. |
| provider | https://mediadive.dsmz.de/rest/medium/J512; $.data.medium; all six $.data.solutions entries, including every recipe row and main preparation step | supports | J512 identifies JCM 512. Main solution 4292 has volume 1020 ml; solutions 4293–4297 separately retain all five stock recipes. Only two stock additions occur as main recipe rows; the three later additions are specified in preparation text. Stock g/L values are not final-medium concentrations. |
| quantities | /private/tmp/culturemech-review-work-batch013/130/quantity-inventory.json; 42 complete source recipe rows plus eight preparation quantities; all 31 target/owner ingredient amounts covered | context_only | Every decision has an exact primary quote and locator. Each recipe row also retains a literal provider JSON object, original amount/unit, stock stage and declared volume. Multiple source rows map to the three improperly merged target ingredients; the denominator is 31 target amounts, not 42 unique target ingredients. |
| mim-lipoic-absence | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned CSV; all identifiers including non-preferred matching modes | refutes | All 9077 rows were read. No row carries CHEBI:30314. Twenty-nine other asserted secondary keys have live preferred-term rows; the manganese ingredient has no secondary assertion. Index membership is not independent validation of material form. |
| writer | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _parse_api_solutions; _parse_preparation_steps | context_only | The current importer restricts direct composition to the first solution, skips solvent rows and preserves main-recipe stock references. Its stock parser considers primary recipe rows, so the three stocks mentioned only in preparation text need explicit treatment. Current code is not proof of which historical version produced the January import or March cleanup. |

## Limits And Additional Notes

- The provider declares a 1020 ml main-solution basis while JCM lists 1 L water plus two 10 ml stock additions. This is a nominal addition-volume convention, not a measured final volume or permission to silently normalize everything to 1 L.
- The source leaves manganese sulfate hydration variable and vitamin B12 chemically generic. No particular hydrate, B12 vitamer, galactose stereoisomer, thioctic-acid enantiomer or organism-specific growth result is inferred. Provider mmol/L fields are retained only as captured data, not endorsed conversions.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T092835Z-culturemech-002863-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: a1_medium (CultureMech:002863)'
started_at: '2026-10-21T09:12:13Z'
finished_at: '2026-10-21T09:28:35Z'
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
summary: The generated record and its one maintained owner flatten five separately
  prepared stocks into 31 direct ingredients, including three sums across incompatible
  concentration bases. The complete JCM and MediaDive formulations support reconstruction
  of stock relationships, while material-form, stereochemical, preparation and secondary-linkage
  issues remain explicit.
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
  - path: data/merge_yaml/merged/A1_MEDIUM.yaml
    sha256: 7f37e3d746bdb0d5db53a70a76c16eb2714c7a7e56e4d8c35c9acb2d4fd0b516
    role: target
  - path: data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml
    sha256: dd2484d805eb867a58d3a6baaa3040d96a9ac9cde97eac90acf533416c332877
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
  selection: Task review 130; batch 013 item 10 of 10, selected in Python lexicographic
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
  - CultureMech:002863
targets:
- target_id: CultureMech:002863
  path: data/merge_yaml/merged/A1_MEDIUM.yaml
  label: a1_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/A1_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002863
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/A1_MEDIUM.yaml --workers 1
    --out /private/tmp/culturemech-review-work-batch013/130/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch013/130/strict.tsv"
  target_ids:
  - CultureMech:002863
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/A1_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002863
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/A1_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002863
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
  - CultureMech:002863
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/A1_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T09:28:33Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T09:28:33Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/A1_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:30.795856Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/A1_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch013/130/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:32.331950Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch013/130/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/A1_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:34.596098Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/A1_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:35.789978Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T09:28:33Z'
  support: supports
  summary: './data/merge_yaml/merged/A1_MEDIUM.yaml:1:id: CultureMech:002863

    ./data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:1:id: CultureMech:002863

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
  summary: CHEBI:15940 resolves to canonical label nicotinic acid; the complete captured
    definition and formula annotations were inspected. Label agreement alone does
    not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: CHEBI:15956 resolves to canonical label biotin; the complete captured definition
    and formula annotations were inspected. Label agreement alone does not validate
    source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: CHEBI:17015 resolves to canonical label riboflavin; the complete captured
    definition and formula annotations were inspected. Label agreement alone does
    not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: CHEBI:176843 resolves to canonical label vitamin B12; the complete captured
    definition and formula annotations were inspected. Label agreement alone does
    not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to canonical label sodium chloride; the complete captured
    definition and formula annotations were inspected. Label agreement alone does
    not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: CHEBI:27470 resolves to canonical label folic acid; the complete captured
    definition and formula annotations were inspected. Label agreement alone does
    not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi28260
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28260
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T09:01:28.331315Z'
  support: supports
  summary: CHEBI:28260 resolves to canonical label galactose; the complete captured
    definition and formula annotations were inspected. Label agreement alone does
    not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: f38a6988f3378a33765a0a763c586f0e92a474c936f1e05d3d251b13342d57c8
- evidence_id: chebi30314
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30314
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T09:01:28.379797Z'
  support: supports
  summary: CHEBI:30314 resolves to canonical label (R)-lipoic acid; the complete captured
    definition and formula annotations were inspected. Label agreement alone does
    not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: d162d6ba3d06179e12ab34153e28aafd1c3105891c075935538b9811111ffd93
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: CHEBI:30753 resolves to canonical label 4-aminobenzoic acid; the complete
    captured definition and formula annotations were inspected. Label agreement alone
    does not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: CHEBI:30961 resolves to canonical label pyridoxine hydrochloride; the complete
    captured definition and formula annotations were inspected. Label agreement alone
    does not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: CHEBI:31206 resolves to canonical label ammonium chloride; the complete
    captured definition and formula annotations were inspected. Label agreement alone
    does not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:28.489501Z'
  support: supports
  summary: CHEBI:31440 resolves to canonical label copper(II) sulfate pentahydrate;
    the complete captured definition and formula annotations were inspected. Label
    agreement alone does not validate source salt, hydrate, stereochemistry or stock
    concentration.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to canonical label magnesium sulfate heptahydrate;
    the complete captured definition and formula annotations were inspected. Label
    agreement alone does not validate source salt, hydrate, stereochemistry or stock
    concentration.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: CHEBI:32139 resolves to canonical label sodium hydrogencarbonate; the complete
    captured definition and formula annotations were inspected. Label agreement alone
    does not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: CHEBI:32588 resolves to canonical label potassium chloride; the complete
    captured definition and formula annotations were inspected. Label agreement alone
    does not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: CHEBI:33118 resolves to canonical label boric acid; the complete captured
    definition and formula annotations were inspected. Label agreement alone does
    not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: CHEBI:34887 resolves to canonical label nickel dichloride; the complete
    captured definition and formula annotations were inspected. Label agreement alone
    does not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi44557
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:46:15.250117Z'
  support: supports
  summary: CHEBI:44557 resolves to canonical label nitrilotriacetic acid; the complete
    captured definition and formula annotations were inspected. Label agreement alone
    does not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: CHEBI:49105 resolves to canonical label thiamine hydrochloride; the complete
    captured definition and formula annotations were inspected. Label agreement alone
    does not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: CHEBI:49976 resolves to canonical label zinc dichloride; the complete captured
    definition and formula annotations were inspected. Label agreement alone does
    not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: CHEBI:53503 resolves to canonical label cobalt chloride hexahydrate; the
    complete captured definition and formula annotations were inspected. Label agreement
    alone does not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: CHEBI:63036 resolves to canonical label potassium dihydrogen phosphate;
    the complete captured definition and formula annotations were inspected. Label
    agreement alone does not validate source salt, hydrate, stereochemistry or stock
    concentration.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: CHEBI:63939 resolves to canonical label sodium tungstate dihydrate; the
    complete captured definition and formula annotations were inspected. Label agreement
    alone does not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to canonical label sodium molybdate dihydrate; the
    complete captured definition and formula annotations were inspected. Label agreement
    alone does not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: CHEBI:75836 resolves to canonical label iron(2+) sulfate heptahydrate;
    the complete captured definition and formula annotations were inspected. Label
    agreement alone does not validate source salt, hydrate, stereochemistry or stock
    concentration.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: CHEBI:76209 resolves to canonical label sodium sulfide nonahydrate; the
    complete captured definition and formula annotations were inspected. Label agreement
    alone does not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi7916
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_7916
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T09:01:28.387666Z'
  support: supports
  summary: CHEBI:7916 resolves to canonical label pantothenic acid; the complete captured
    definition and formula annotations were inspected. Label agreement alone does
    not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: 7b057eb0f384350a666b22dce9bd0529405271e968b5fe5fb69c63d74cc14122
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 resolves to canonical label calcium chloride dihydrate; the
    complete captured definition and formula annotations were inspected. Label agreement
    alone does not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: CHEBI:86345 resolves to canonical label magnesium dichloride hexahydrate;
    the complete captured definition and formula annotations were inspected. Label
    agreement alone does not validate source salt, hydrate, stereochemistry or stock
    concentration.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86360
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:05.958063Z'
  support: supports
  summary: CHEBI:86360 resolves to canonical label manganese(II) sulfate; the complete
    captured definition and formula annotations were inspected. Label agreement alone
    does not validate source salt, hydrate, stereochemistry or stock concentration.
  snapshot_sha256: ee3b60385f389c4eeb301cfe59996112ffa9c3c135268559b79e91810a14932b
- evidence_id: chebi86465
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:08.054799Z'
  support: supports
  summary: CHEBI:86465 resolves to canonical label potassium aluminium sulfate dodecahydrate;
    the complete captured definition and formula annotations were inspected. Label
    agreement alone does not validate source salt, hydrate, stereochemistry or stock
    concentration.
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T09:28:33Z'
  support: context_only
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
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139":
    [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139",
    "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic
    acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride
    hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term":
    "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type":
    "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id":
    "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440":
    [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term":
    "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label":
    "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type":
    "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id":
    "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939":
    [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type":
    "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id":
    "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:7916":
    [{"label": "Pantothenic acid", "match_type": "preferred_term", "identifier": "CHEBI:7916",
    "preferred_term": "Pantothenic acid", "ontology_id": "CHEBI:7916", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}],
    "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30314":
    [], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id":
    "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105":
    [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105",
    "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type":
    "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term",
    "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id":
    "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470":
    [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470",
    "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209":
    [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:28260": [{"label": "Galactose", "match_type":
    "preferred_term", "identifier": "CHEBI:28260", "preferred_term": "Galactose",
    "ontology_id": "CHEBI:28260", "mapping_status": "MAPPED", "ambiguity": "unique"}]};
    Unresolved current secondary keys: [''CHEBI:30314'']'
- evidence_id: jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512
  locator: JCM 512 complete main formulation, preparation paragraph, five named stock
    subsections and page-wide default
  accessed_at: '2026-10-21T09:01:29.144368Z'
  support: supports
  summary: The primary source distinguishes a main mixture from DL minerals, DL vitamins,
    APM salts, sulfide and galactose stocks. Every stock has its own solvent basis
    and addition stage. Refrigeration and sterilization methods are stated in stock
    headings; the page-wide default is qualified by explicit exceptions.
  snapshot_sha256: e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J512
  locator: $.data.medium; all six $.data.solutions entries, including every recipe
    row and main preparation step
  accessed_at: '2026-10-21T09:01:27.529467Z'
  support: supports
  summary: J512 identifies JCM 512. Main solution 4292 has volume 1020 ml; solutions
    4293–4297 separately retain all five stock recipes. Only two stock additions occur
    as main recipe rows; the three later additions are specified in preparation text.
    Stock g/L values are not final-medium concentrations.
  snapshot_sha256: 526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e
- evidence_id: quantities
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch013/130/quantity-inventory.json
  locator: 42 complete source recipe rows plus eight preparation quantities; all 31
    target/owner ingredient amounts covered
  accessed_at: '2026-10-21T09:28:33Z'
  support: context_only
  summary: Every decision has an exact primary quote and locator. Each recipe row
    also retains a literal provider JSON object, original amount/unit, stock stage
    and declared volume. Multiple source rows map to the three improperly merged target
    ingredients; the denominator is 31 target amounts, not 42 unique target ingredients.
  snapshot_sha256: ea1e084ee6499b35e40a12cbe42cc8092e6f688c1fb478689a277e6df2585dff
- evidence_id: mim-lipoic-absence
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned CSV; all identifiers including non-preferred matching modes
  accessed_at: '2026-10-21T09:28:33Z'
  support: refutes
  summary: All 9077 rows were read. No row carries CHEBI:30314. Twenty-nine other
    asserted secondary keys have live preferred-term rows; the manganese ingredient
    has no secondary assertion. Index membership is not independent validation of
    material form.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: writer
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _parse_api_solutions; _parse_preparation_steps
  accessed_at: '2026-10-21T09:28:33Z'
  support: context_only
  summary: The current importer restricts direct composition to the first solution,
    skips solvent rows and preserves main-recipe stock references. Its stock parser
    considers primary recipe rows, so the three stocks mentioned only in preparation
    text need explicit treatment. Current code is not proof of which historical version
    produced the January import or March cleanup.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002863
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: concern
  summary: '31 primary CHEBI identities resolve with matching labels; 29 of 30 current
    secondary keys have live pinned-index rows. Unresolved keys: [''CHEBI:30314''].'
  target_ids:
  - CultureMech:002863
  evidence_ids:
  - record
  - mim
  - chebi15940
  - chebi15956
  - chebi17015
  - chebi176843
  - chebi26710
  - chebi27470
  - chebi28260
  - chebi30314
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31440
  - chebi31795
  - chebi32139
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi44557
  - chebi49105
  - chebi49976
  - chebi53503
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi75836
  - chebi76209
  - chebi7916
  - chebi86158
  - chebi86345
  - chebi86360
  - chebi86465
  details: 31 direct ingredient instances; CHEBI-primary instance linkage 31/31 (100.00%),
    verified secondary coverage 29/31 (93.55%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Exact JCM origin and MediaDive representation
  outcome: supported
  summary: CultureMech:002863 identifies JCM recipe 512, exposed by DSMZ MediaDive
    as J512. The source name, term and original link agree. One normalized owner supplies
    this generated record; matching names alone do not establish equivalence with
    unrelated A1 media.
  target_ids:
  - CultureMech:002863
  evidence_ids:
  - record
  - owner-0
  - id-search
  - jcm
  - provider
- assessment_id: amounts
  area: quantity
  topic: Complete stage-specific quantity reconciliation
  outcome: concern
  summary: All 31 target/owner ingredient amounts are covered by 42 source recipe
    rows and eight preparation decisions. NaCl sums 19.6078 + 1.0; magnesium sulfate
    sums 0.196078 + 3.0; calcium chloride sums 0.1 + 30.4. Those operands come from
    different main/stock bases and cannot be added directly. Values such as 212, 40
    and 90.1 g/L are stock concentrations, not final medium concentrations. Main-only
    KCl, NH4Cl, KH2PO4 and NaHCO3 values match provider normalization but retain its
    declared main-stage basis.
  target_ids:
  - CultureMech:002863
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - quantities
  details: '[{"source_row": "0:0", "field_paths": ["ingredients[0].concentration"],
    "target_index": 0, "record_value": {"value": "20.6078", "unit": "G_PER_L"}, "owner_value":
    {"value": "20.6078", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[0].concentration",
    "ingredient": "NaCl", "decision": "correct", "stage": "Main sol. J512", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 Main sol. J512 recipe row 1", "source_quote": "NaCl
    20.0 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256":
    "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator":
    "$.data.solutions[0].recipe[0]", "provider_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 20,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 19.6078,\n                        \"mmol_l\":
    335.521,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    20, "provider_original_unit": "g", "provider_g_l": 19.6078, "provider_volume_ml":
    1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation":
    "This is a main-mixture amount. Preserve the literal primary mass and provider-declared
    1020 ml basis separately from the later tube additions and measured final volume.
    The current value also sums entries from different source stages; undo that unsupported
    cross-stage sum before any downstream concentration calculation."}, {"source_row":
    "0:1", "field_paths": ["ingredients[1].concentration"], "target_index": 1, "record_value":
    {"value": "0.754902", "unit": "G_PER_L"}, "owner_value": {"value": "0.754902",
    "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[1].concentration",
    "ingredient": "KCl", "decision": "evidence_only", "stage": "Main sol. J512", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 Main sol. J512 recipe row 2", "source_quote": "KCl
    0.77 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512", "provider_sha256":
    "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e", "provider_locator":
    "$.data.solutions[0].recipe[1]", "provider_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.77,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.754902,\n                        \"mmol_l\":
    10.1261,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.77, "provider_original_unit": "g", "provider_g_l": 0.754902, "provider_volume_ml":
    1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation":
    "This is a main-mixture amount. Preserve the literal primary mass and provider-declared
    1020 ml basis separately from the later tube additions and measured final volume."},
    {"source_row": "0:2", "field_paths": ["ingredients[2].concentration"], "target_index":
    2, "record_value": {"value": "0.245098", "unit": "G_PER_L"}, "owner_value": {"value":
    "0.245098", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[2].concentration",
    "ingredient": "NH4Cl", "decision": "evidence_only", "stage": "Main sol. J512",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 Main sol. J512 recipe row 3", "source_quote": "NH 4
    Cl 0.25 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[0].recipe[2]", "provider_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.245098,\n                        \"mmol_l\":
    4.58213,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.25, "provider_original_unit": "g", "provider_g_l": 0.245098, "provider_volume_ml":
    1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation":
    "This is a main-mixture amount. Preserve the literal primary mass and provider-declared
    1020 ml basis separately from the later tube additions and measured final volume."},
    {"source_row": "0:3", "field_paths": ["ingredients[3].concentration"], "target_index":
    3, "record_value": {"value": "0.0980392", "unit": "G_PER_L"}, "owner_value": {"value":
    "0.0980392", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[3].concentration",
    "ingredient": "KH2PO4", "decision": "evidence_only", "stage": "Main sol. J512",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 Main sol. J512 recipe row 4", "source_quote": "KH 2
    PO 4 0.1 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[0].recipe[3]", "provider_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0980392,\n                        \"mmol_l\":
    0.720421,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.1, "provider_original_unit": "g", "provider_g_l": 0.0980392, "provider_volume_ml":
    1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation":
    "This is a main-mixture amount. Preserve the literal primary mass and provider-declared
    1020 ml basis separately from the later tube additions and measured final volume."},
    {"source_row": "0:4", "field_paths": ["ingredients[4].concentration"], "target_index":
    4, "record_value": {"value": "3.196078", "unit": "G_PER_L"}, "owner_value": {"value":
    "3.196078", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[4].concentration",
    "ingredient": "MgSO4 x 7 H2O", "decision": "correct", "stage": "Main sol. J512",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 Main sol. J512 recipe row 5", "source_quote": "MgSO
    4 ·7H 2 O 0.2 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[0].recipe[4]", "provider_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.196078,\n                        \"mmol_l\":
    0.795527,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.2, "provider_original_unit": "g", "provider_g_l": 0.196078, "provider_volume_ml":
    1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation":
    "This is a main-mixture amount. Preserve the literal primary mass and provider-declared
    1020 ml basis separately from the later tube additions and measured final volume.
    The current value also sums entries from different source stages; undo that unsupported
    cross-stage sum before any downstream concentration calculation."}, {"source_row":
    "0:5", "field_paths": ["solutions"], "ingredient": "DL vitamins (refrigerated)",
    "decision": "add", "stage": "Main sol. J512", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 Main sol. J512 recipe row 6", "source_quote": "DL vitamins
    (see below) 10.0 ml", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[0].recipe[5]", "provider_quote": "{\n                        \"recipe_order\":
    6,\n                        \"solution\": \"DL vitamins (refrigerated)\",\n                        \"solution_id\":
    4294,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount":
    10, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml":
    1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation":
    "The source gives a stock addition missing as a structured solution relationship.
    Preserve its literal volume and source main-batch basis; do not silently convert
    this to an addition per measured final liter."}, {"source_row": "0:6", "field_paths":
    ["solutions"], "ingredient": "DL minerals (refrigerated)", "decision": "add",
    "stage": "Main sol. J512", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 Main sol. J512 recipe row 7", "source_quote": "DL minerals
    (see below) 10.0 ml", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[0].recipe[6]", "provider_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"DL minerals (refrigerated)\",\n                        \"solution_id\":
    4293,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount":
    10, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml":
    1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation":
    "The source gives a stock addition missing as a structured solution relationship.
    Preserve its literal volume and source main-batch basis; do not silently convert
    this to an addition per measured final liter."}, {"source_row": "0:7", "field_paths":
    ["ingredients[5].concentration"], "target_index": 5, "record_value": {"value":
    "1.96078", "unit": "G_PER_L"}, "owner_value": {"value": "1.96078", "unit": "G_PER_L"},
    "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[5].concentration",
    "ingredient": "NaHCO3", "decision": "evidence_only", "stage": "Main sol. J512",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 Main sol. J512 recipe row 8", "source_quote": "NaHCO
    3 2.0 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[0].recipe[7]", "provider_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.96078,\n                        \"mmol_l\":
    23.3407,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    2, "provider_original_unit": "g", "provider_g_l": 1.96078, "provider_volume_ml":
    1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation":
    "This is a main-mixture amount. Preserve the literal primary mass and provider-declared
    1020 ml basis separately from the later tube additions and measured final volume."},
    {"source_row": "0:8", "field_paths": ["preparation_steps"], "ingredient": "Distilled
    water", "decision": "add", "stage": "Main sol. J512", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 Main sol. J512 recipe row 9", "source_quote": "Distilled
    water 1.0 L", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[0].recipe[8]", "provider_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount":
    1000, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml":
    1020, "provider_volume_locator": "$.data.solutions[0].volume", "explanation":
    "This solvent amount belongs to the named preparation stage. Preserve it as solvent/batch
    context, without adding a second independent chemical ingredient edge or claiming
    measured final volume."}, {"source_row": "1:0", "field_paths": ["ingredients[6].concentration"],
    "target_index": 6, "record_value": {"value": "1.5", "unit": "G_PER_L"}, "owner_value":
    {"value": "1.5", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[6].concentration",
    "ingredient": "Nitrilotriacetic acid", "decision": "correct", "stage": "DL minerals
    (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 1", "source_quote":
    "Nitrilotriacetic acid, trisodium salt 1.5 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[1].recipe[0]", "provider_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\":
    189,\n                        \"condition\": \" trisodium salt\",\n                        \"amount\":
    1.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\":
    0\n                    }", "provider_original_amount": 1.5, "provider_original_unit":
    "g", "provider_g_l": 1.5, "provider_volume_ml": 1000, "provider_volume_locator":
    "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock
    g/L were promoted to a direct medium amount. Preserve this stock basis and its
    separately stated addition; do not use undiluted stock strength as final medium
    concentration."}, {"source_row": "1:1", "field_paths": ["ingredients[4].concentration"],
    "target_index": 4, "record_value": {"value": "3.196078", "unit": "G_PER_L"}, "owner_value":
    {"value": "3.196078", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[4].concentration",
    "ingredient": "MgSO4 x 7 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 2", "source_quote":
    "MgSO 4 ·7H 2 O 3.0 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[1].recipe[1]", "provider_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    12.1716,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    3, "provider_original_unit": "g", "provider_g_l": 3, "provider_volume_ml": 1000,
    "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe
    amount and stock g/L were promoted to a direct medium amount. Preserve this stock
    basis and its separately stated addition; do not use undiluted stock strength
    as final medium concentration. The current value also sums entries from different
    source stages; undo that unsupported cross-stage sum before any downstream concentration
    calculation."}, {"source_row": "1:2", "field_paths": ["ingredients[7].concentration"],
    "target_index": 7, "record_value": {"value": "0.5", "unit": "G_PER_L"}, "owner_value":
    {"value": "0.5", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[7].concentration",
    "ingredient": "MnSO4 x n H2O", "decision": "correct", "stage": "DL minerals (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 3", "source_quote":
    "MnSO 4 · x H 2 O 0.5 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[1].recipe[2]", "provider_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MnSO4 x n H2O\",\n                        \"compound_id\":
    1000,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\":
    0\n                    }", "provider_original_amount": 0.5, "provider_original_unit":
    "g", "provider_g_l": 0.5, "provider_volume_ml": 1000, "provider_volume_locator":
    "$.data.solutions[1].volume", "explanation": "A stock-recipe amount and stock
    g/L were promoted to a direct medium amount. Preserve this stock basis and its
    separately stated addition; do not use undiluted stock strength as final medium
    concentration."}, {"source_row": "1:3", "field_paths": ["ingredients[0].concentration"],
    "target_index": 0, "record_value": {"value": "20.6078", "unit": "G_PER_L"}, "owner_value":
    {"value": "20.6078", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[0].concentration",
    "ingredient": "NaCl", "decision": "correct", "stage": "DL minerals (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 4", "source_quote":
    "NaCl 1.0 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[1].recipe[3]", "provider_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    17.1116,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    1, "provider_original_unit": "g", "provider_g_l": 1, "provider_volume_ml": 1000,
    "provider_volume_locator": "$.data.solutions[1].volume", "explanation": "A stock-recipe
    amount and stock g/L were promoted to a direct medium amount. Preserve this stock
    basis and its separately stated addition; do not use undiluted stock strength
    as final medium concentration. The current value also sums entries from different
    source stages; undo that unsupported cross-stage sum before any downstream concentration
    calculation."}, {"source_row": "1:4", "field_paths": ["ingredients[8].concentration"],
    "target_index": 8, "record_value": {"value": "0.1", "unit": "G_PER_L"}, "owner_value":
    {"value": "0.1", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[8].concentration",
    "ingredient": "FeSO4 x 7 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 5", "source_quote":
    "FeSO 4 ·7H 2 O 0.1 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[1].recipe[4]", "provider_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.359693,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.1, "provider_original_unit": "g", "provider_g_l": 0.1, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration."}, {"source_row": "1:5", "field_paths":
    ["ingredients[9].concentration"], "target_index": 9, "record_value": {"value":
    "30.5", "unit": "G_PER_L"}, "owner_value": {"value": "30.5", "unit": "G_PER_L"},
    "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[9].concentration",
    "ingredient": "CaCl2 x 2 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 6", "source_quote":
    "CaCl 2 ·2H 2 O 0.1 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[1].recipe[5]", "provider_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.680203,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.1, "provider_original_unit": "g", "provider_g_l": 0.1, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration. The current value also sums entries
    from different source stages; undo that unsupported cross-stage sum before any
    downstream concentration calculation."}, {"source_row": "1:6", "field_paths":
    ["ingredients[10].concentration"], "target_index": 10, "record_value": {"value":
    "0.1", "unit": "G_PER_L"}, "owner_value": {"value": "0.1", "unit": "G_PER_L"},
    "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[10].concentration",
    "ingredient": "CoCl2 x 6 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 7", "source_quote":
    "CoCl 2 ·6H 2 O 0.1 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[1].recipe[6]", "provider_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.770185,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.1, "provider_original_unit": "g", "provider_g_l": 0.1, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration."}, {"source_row": "1:7", "field_paths":
    ["ingredients[11].concentration"], "target_index": 11, "record_value": {"value":
    "0.13", "unit": "G_PER_L"}, "owner_value": {"value": "0.13", "unit": "G_PER_L"},
    "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[11].concentration",
    "ingredient": "ZnCl2", "decision": "correct", "stage": "DL minerals (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 8", "source_quote":
    "ZnCl 2 0.13 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[1].recipe[7]", "provider_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 0.13,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.13,\n                        \"mmol_l\":
    0.953778,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.13, "provider_original_unit": "g", "provider_g_l": 0.13, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration."}, {"source_row": "1:8", "field_paths":
    ["ingredients[12].concentration"], "target_index": 12, "record_value": {"value":
    "0.01", "unit": "G_PER_L"}, "owner_value": {"value": "0.01", "unit": "G_PER_L"},
    "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[12].concentration",
    "ingredient": "CuSO4 x 5 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 9", "source_quote":
    "CuSO 4 ·5H 2 O 0.01 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[1].recipe[8]", "provider_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\":
    121,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0400503,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.01, "provider_original_unit": "g", "provider_g_l": 0.01, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration."}, {"source_row": "1:9", "field_paths":
    ["ingredients[13].concentration"], "target_index": 13, "record_value": {"value":
    "0.01", "unit": "G_PER_L"}, "owner_value": {"value": "0.01", "unit": "G_PER_L"},
    "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[13].concentration",
    "ingredient": "AlK(SO4)2 x 12 H2O", "decision": "correct", "stage": "DL minerals
    (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 10", "source_quote":
    "AlK(SO 4 ) 2 ·12H 2 O 0.01 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[1].recipe[9]", "provider_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\":
    908,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0210798,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.01, "provider_original_unit": "g", "provider_g_l": 0.01, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration."}, {"source_row": "1:10", "field_paths":
    ["ingredients[14].concentration"], "target_index": 14, "record_value": {"value":
    "0.01", "unit": "G_PER_L"}, "owner_value": {"value": "0.01", "unit": "G_PER_L"},
    "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[14].concentration",
    "ingredient": "H3BO3", "decision": "correct", "stage": "DL minerals (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 11", "source_quote":
    "H 3 BO 3 0.01 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[1].recipe[10]", "provider_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.161708,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.01, "provider_original_unit": "g", "provider_g_l": 0.01, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration."}, {"source_row": "1:11", "field_paths":
    ["ingredients[15].concentration"], "target_index": 15, "record_value": {"value":
    "0.025", "unit": "G_PER_L"}, "owner_value": {"value": "0.025", "unit": "G_PER_L"},
    "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[15].concentration",
    "ingredient": "Na2MoO4 x 2 H2O", "decision": "correct", "stage": "DL minerals
    (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 12", "source_quote":
    "Na 2 MoO 4 ·2H 2 O 0.025 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[1].recipe[11]", "provider_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 0.025,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.025,\n                        \"mmol_l\":
    0.103327,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.025, "provider_original_unit": "g", "provider_g_l": 0.025, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration."}, {"source_row": "1:12", "field_paths":
    ["ingredients[16].concentration"], "target_index": 16, "record_value": {"value":
    "0.024", "unit": "G_PER_L"}, "owner_value": {"value": "0.024", "unit": "G_PER_L"},
    "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[16].concentration",
    "ingredient": "NiCl2 x 6 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 13", "source_quote":
    "NiCl 2 ·6H 2 O 0.024 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[1].recipe[12]", "provider_quote": "{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 0.024,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.024, "provider_original_unit": "g", "provider_g_l": 0.024, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration."}, {"source_row": "1:13", "field_paths":
    ["ingredients[17].concentration"], "target_index": 17, "record_value": {"value":
    "0.025", "unit": "G_PER_L"}, "owner_value": {"value": "0.025", "unit": "G_PER_L"},
    "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[17].concentration",
    "ingredient": "Na2WO4 x 2 H2O", "decision": "correct", "stage": "DL minerals (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 14", "source_quote":
    "Na 2 WO 4 ·2H 2 O 0.025 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[1].recipe[13]", "provider_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 0.025,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.025,\n                        \"mmol_l\":
    0.075792,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.025, "provider_original_unit": "g", "provider_g_l": 0.025, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration."}, {"source_row": "1:14", "field_paths":
    ["preparation_steps"], "ingredient": "Distilled water", "decision": "add", "stage":
    "DL minerals (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL minerals (refrigerated) recipe row 15", "source_quote":
    "Distilled water 1.0 L", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[1].recipe[14]", "provider_quote": "{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount":
    1000, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[1].volume", "explanation":
    "This solvent amount belongs to the named preparation stage. Preserve it as solvent/batch
    context, without adding a second independent chemical ingredient edge or claiming
    measured final volume."}, {"source_row": "2:0", "field_paths": ["ingredients[18].concentration"],
    "target_index": 18, "record_value": {"value": "0.002", "unit": "G_PER_L"}, "owner_value":
    {"value": "0.002", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[18].concentration",
    "ingredient": "Biotin", "decision": "correct", "stage": "DL vitamins (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 1", "source_quote":
    "Biotin 0.002 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[2].recipe[0]", "provider_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.00818632,\n                        \"optional\": 0\n                    }",
    "provider_original_amount": 2, "provider_original_unit": "mg", "provider_g_l":
    0.002, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[2].volume",
    "explanation": "A stock-recipe amount and stock g/L were promoted to a direct
    medium amount. Preserve this stock basis and its separately stated addition; do
    not use undiluted stock strength as final medium concentration. The provider uses
    mg while JCM states the equivalent mass in g; both original representations are
    retained."}, {"source_row": "2:1", "field_paths": ["ingredients[19].concentration"],
    "target_index": 19, "record_value": {"value": "0.005", "unit": "G_PER_L"}, "owner_value":
    {"value": "0.005", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[19].concentration",
    "ingredient": "Pantothenic acid", "decision": "correct", "stage": "DL vitamins
    (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 2", "source_quote":
    "Pantothenic acid 0.005 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[2].recipe[1]", "provider_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Pantothenic acid\",\n                        \"compound_id\":
    135,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0228071,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    5, "provider_original_unit": "mg", "provider_g_l": 0.005, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration. The provider uses mg while JCM states
    the equivalent mass in g; both original representations are retained."}, {"source_row":
    "2:2", "field_paths": ["ingredients[20].concentration"], "target_index": 20, "record_value":
    {"value": "0.0001", "unit": "G_PER_L"}, "owner_value": {"value": "0.0001", "unit":
    "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[20].concentration",
    "ingredient": "Vitamin B12", "decision": "correct", "stage": "DL vitamins (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 3", "source_quote":
    "Vitamin B 1 2 0.0001 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[2].recipe[2]", "provider_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\":
    7.3779e-5,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.1, "provider_original_unit": "mg", "provider_g_l": 0.0001, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration. The provider uses mg while JCM states
    the equivalent mass in g; both original representations are retained."}, {"source_row":
    "2:3", "field_paths": ["ingredients[21].concentration"], "target_index": 21, "record_value":
    {"value": "0.005", "unit": "G_PER_L"}, "owner_value": {"value": "0.005", "unit":
    "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[21].concentration",
    "ingredient": "p-Aminobenzoic acid", "decision": "correct", "stage": "DL vitamins
    (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 4", "source_quote":
    "p -Aminobenzoic acid 0.005 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[2].recipe[3]", "provider_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0364591,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    5, "provider_original_unit": "mg", "provider_g_l": 0.005, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration. The provider uses mg while JCM states
    the equivalent mass in g; both original representations are retained."}, {"source_row":
    "2:4", "field_paths": ["ingredients[22].concentration"], "target_index": 22, "record_value":
    {"value": "0.005", "unit": "G_PER_L"}, "owner_value": {"value": "0.005", "unit":
    "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[22].concentration",
    "ingredient": "Thioctic acid", "decision": "correct", "stage": "DL vitamins (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 5", "source_quote":
    "Thioctic acid 0.005 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[2].recipe[4]", "provider_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Thioctic acid\",\n                        \"compound_id\":
    535,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0242365,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    5, "provider_original_unit": "mg", "provider_g_l": 0.005, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration. The provider uses mg while JCM states
    the equivalent mass in g; both original representations are retained."}, {"source_row":
    "2:5", "field_paths": ["ingredients[23].concentration"], "target_index": 23, "record_value":
    {"value": "0.005", "unit": "G_PER_L"}, "owner_value": {"value": "0.005", "unit":
    "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[23].concentration",
    "ingredient": "Nicotinic acid", "decision": "correct", "stage": "DL vitamins (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 6", "source_quote":
    "Nicotinic acid 0.005 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[2].recipe[5]", "provider_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0406141,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    5, "provider_original_unit": "mg", "provider_g_l": 0.005, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration. The provider uses mg while JCM states
    the equivalent mass in g; both original representations are retained."}, {"source_row":
    "2:6", "field_paths": ["ingredients[24].concentration"], "target_index": 24, "record_value":
    {"value": "0.005", "unit": "G_PER_L"}, "owner_value": {"value": "0.005", "unit":
    "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[24].concentration",
    "ingredient": "Thiamine HCl", "decision": "correct", "stage": "DL vitamins (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 7", "source_quote":
    "Thiamine·HCl 0.005 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[2].recipe[6]", "provider_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"optional\":
    0\n                    }", "provider_original_amount": 5, "provider_original_unit":
    "mg", "provider_g_l": 0.005, "provider_volume_ml": 1000, "provider_volume_locator":
    "$.data.solutions[2].volume", "explanation": "A stock-recipe amount and stock
    g/L were promoted to a direct medium amount. Preserve this stock basis and its
    separately stated addition; do not use undiluted stock strength as final medium
    concentration. The provider uses mg while JCM states the equivalent mass in g;
    both original representations are retained."}, {"source_row": "2:7", "field_paths":
    ["ingredients[25].concentration"], "target_index": 25, "record_value": {"value":
    "0.005", "unit": "G_PER_L"}, "owner_value": {"value": "0.005", "unit": "G_PER_L"},
    "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[25].concentration",
    "ingredient": "Riboflavin", "decision": "correct", "stage": "DL vitamins (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 8", "source_quote":
    "Riboflavin 0.005 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[2].recipe[7]", "provider_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0132837,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    5, "provider_original_unit": "mg", "provider_g_l": 0.005, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation":
    "A stock-recipe amount and stock g/L were promoted to a direct medium amount.
    Preserve this stock basis and its separately stated addition; do not use undiluted
    stock strength as final medium concentration. The provider uses mg while JCM states
    the equivalent mass in g; both original representations are retained."}, {"source_row":
    "2:8", "field_paths": ["ingredients[26].concentration"], "target_index": 26, "record_value":
    {"value": "0.01", "unit": "G_PER_L"}, "owner_value": {"value": "0.01", "unit":
    "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[26].concentration",
    "ingredient": "Pyridoxine hydrochloride", "decision": "correct", "stage": "DL
    vitamins (refrigerated)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 9", "source_quote":
    "Pyridoxine·HCl 0.01 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[2].recipe[8]", "provider_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"optional\":
    0\n                    }", "provider_original_amount": 0.01, "provider_original_unit":
    "g", "provider_g_l": 0.01, "provider_volume_ml": 1000, "provider_volume_locator":
    "$.data.solutions[2].volume", "explanation": "A stock-recipe amount and stock
    g/L were promoted to a direct medium amount. Preserve this stock basis and its
    separately stated addition; do not use undiluted stock strength as final medium
    concentration."}, {"source_row": "2:9", "field_paths": ["ingredients[27].concentration"],
    "target_index": 27, "record_value": {"value": "0.002", "unit": "G_PER_L"}, "owner_value":
    {"value": "0.002", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[27].concentration",
    "ingredient": "Folic acid", "decision": "correct", "stage": "DL vitamins (refrigerated)",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 10", "source_quote":
    "Folic acid 0.002 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[2].recipe[9]", "provider_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.00453104,\n                        \"optional\": 0\n                    }",
    "provider_original_amount": 2, "provider_original_unit": "mg", "provider_g_l":
    0.002, "provider_volume_ml": 1000, "provider_volume_locator": "$.data.solutions[2].volume",
    "explanation": "A stock-recipe amount and stock g/L were promoted to a direct
    medium amount. Preserve this stock basis and its separately stated addition; do
    not use undiluted stock strength as final medium concentration. The provider uses
    mg while JCM states the equivalent mass in g; both original representations are
    retained."}, {"source_row": "2:10", "field_paths": ["preparation_steps"], "ingredient":
    "Distilled water", "decision": "add", "stage": "DL vitamins (refrigerated)", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 DL vitamins (refrigerated) recipe row 11", "source_quote":
    "Distilled water 1.0 L", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[2].recipe[10]", "provider_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount":
    1000, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml":
    1000, "provider_volume_locator": "$.data.solutions[2].volume", "explanation":
    "This solvent amount belongs to the named preparation stage. Preserve it as solvent/batch
    context, without adding a second independent chemical ingredient edge or claiming
    measured final volume."}, {"source_row": "3:0", "field_paths": ["ingredients[28].concentration"],
    "target_index": 28, "record_value": {"value": "212", "unit": "G_PER_L"}, "owner_value":
    {"value": "212", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[28].concentration",
    "ingredient": "MgCl2 x 6 H2O", "decision": "correct", "stage": "APM salts solution
    (autoclaved)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 APM salts solution (autoclaved) recipe row 1", "source_quote":
    "MgCl 2 ·6H 2 O 21.2 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[3].recipe[0]", "provider_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 21.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 212,\n                        \"mmol_l\":
    1042.78,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    21.2, "provider_original_unit": "g", "provider_g_l": 212, "provider_volume_ml":
    100, "provider_volume_locator": "$.data.solutions[3].volume", "explanation": "A
    stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve
    this stock basis and its separately stated addition; do not use undiluted stock
    strength as final medium concentration."}, {"source_row": "3:1", "field_paths":
    ["ingredients[9].concentration"], "target_index": 9, "record_value": {"value":
    "30.5", "unit": "G_PER_L"}, "owner_value": {"value": "30.5", "unit": "G_PER_L"},
    "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[9].concentration",
    "ingredient": "CaCl2 x 2 H2O", "decision": "correct", "stage": "APM salts solution
    (autoclaved)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 APM salts solution (autoclaved) recipe row 2", "source_quote":
    "CaCl 2 ·2H 2 O 3.04 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[3].recipe[1]", "provider_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 3.04,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 30.4,\n                        \"mmol_l\":
    206.782,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    3.04, "provider_original_unit": "g", "provider_g_l": 30.4, "provider_volume_ml":
    100, "provider_volume_locator": "$.data.solutions[3].volume", "explanation": "A
    stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve
    this stock basis and its separately stated addition; do not use undiluted stock
    strength as final medium concentration. The current value also sums entries from
    different source stages; undo that unsupported cross-stage sum before any downstream
    concentration calculation."}, {"source_row": "3:2", "field_paths": ["preparation_steps"],
    "ingredient": "Distilled water", "decision": "add", "stage": "APM salts solution
    (autoclaved)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 APM salts solution (autoclaved) recipe row 3", "source_quote":
    "Distilled water 100.0 ml", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[3].recipe[2]", "provider_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 100,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount":
    100, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml":
    100, "provider_volume_locator": "$.data.solutions[3].volume", "explanation": "This
    solvent amount belongs to the named preparation stage. Preserve it as solvent/batch
    context, without adding a second independent chemical ingredient edge or claiming
    measured final volume."}, {"source_row": "4:0", "field_paths": ["ingredients[29].concentration"],
    "target_index": 29, "record_value": {"value": "40", "unit": "G_PER_L"}, "owner_value":
    {"value": "40", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[29].concentration",
    "ingredient": "Na2S x 9 H2O", "decision": "correct", "stage": "Sulfide stock solution
    (autoclaved)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 Sulfide stock solution (autoclaved) recipe row 1",
    "source_quote": "Na 2 S·9H 2 O 0.4 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[4].recipe[0]", "provider_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 40,\n                        \"mmol_l\":
    166.54,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.4, "provider_original_unit": "g", "provider_g_l": 40, "provider_volume_ml":
    10, "provider_volume_locator": "$.data.solutions[4].volume", "explanation": "A
    stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve
    this stock basis and its separately stated addition; do not use undiluted stock
    strength as final medium concentration."}, {"source_row": "4:1", "field_paths":
    ["preparation_steps"], "ingredient": "Distilled water", "decision": "add", "stage":
    "Sulfide stock solution (autoclaved)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 Sulfide stock solution (autoclaved) recipe row 2",
    "source_quote": "Distilled water 10.0 ml", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[4].recipe[1]", "provider_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount":
    10, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml":
    10, "provider_volume_locator": "$.data.solutions[4].volume", "explanation": "This
    solvent amount belongs to the named preparation stage. Preserve it as solvent/batch
    context, without adding a second independent chemical ingredient edge or claiming
    measured final volume."}, {"source_row": "5:0", "field_paths": ["ingredients[30].concentration"],
    "target_index": 30, "record_value": {"value": "90.1", "unit": "G_PER_L"}, "owner_value":
    {"value": "90.1", "unit": "G_PER_L"}, "owner_field_path": "data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml:ingredients[30].concentration",
    "ingredient": "Galactose", "decision": "correct", "stage": "Galactose stock solution
    (filter-sterilized)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 Galactose stock solution (filter-sterilized) recipe
    row 1", "source_quote": "Galactose 0.901 g", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[5].recipe[0]", "provider_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Galactose\",\n                        \"compound_id\":
    321,\n                        \"amount\": 0.901,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 90.1,\n                        \"mmol_l\":
    500.111,\n                        \"optional\": 0\n                    }", "provider_original_amount":
    0.901, "provider_original_unit": "g", "provider_g_l": 90.1, "provider_volume_ml":
    10, "provider_volume_locator": "$.data.solutions[5].volume", "explanation": "A
    stock-recipe amount and stock g/L were promoted to a direct medium amount. Preserve
    this stock basis and its separately stated addition; do not use undiluted stock
    strength as final medium concentration."}, {"source_row": "5:1", "field_paths":
    ["preparation_steps"], "ingredient": "Distilled water", "decision": "add", "stage":
    "Galactose stock solution (filter-sterilized)", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 Galactose stock solution (filter-sterilized) recipe
    row 2", "source_quote": "Distilled water 10.0 ml", "provider_reference": "https://mediadive.dsmz.de/rest/medium/J512",
    "provider_sha256": "526620c5e060123d1bbaca83090ad15364a135c4c16844e322847ca4c556bf4e",
    "provider_locator": "$.data.solutions[5].recipe[1]", "provider_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "provider_original_amount":
    10, "provider_original_unit": "ml", "provider_g_l": null, "provider_volume_ml":
    10, "provider_volume_locator": "$.data.solutions[5].volume", "explanation": "This
    solvent amount belongs to the named preparation stage. Preserve it as solvent/batch
    context, without adding a second independent chemical ingredient edge or claiming
    measured final volume."}, {"field_paths": ["ph_value", "preparation_steps[0]"],
    "decision": "evidence_only", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 main preparation paragraph", "source_quote": "adjust
    pH to 6.8 and add NaHCO 3", "explanation": "The schema defines ph_value as a target
    pH. The recorded 6.8 target and the pre-bicarbonate adjustment stage already agree
    with the source in both layers. Preserve them and add exact claim-level support;
    no value removal or final-pH assertion is warranted."}, {"field_paths": ["preparation_steps[0]"],
    "decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 main preparation paragraph", "source_quote": "Dispense
    the medium (9 ml)", "explanation": "This is the main-mixture aliquot, not a final
    volume including the three later additions."}, {"field_paths": ["preparation_steps[0]"],
    "decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 main preparation paragraph", "source_quote": "26-ml
    anaerobic pressure tubes", "explanation": "This is vessel capacity, not medium
    volume or a concentration denominator."}, {"field_paths": ["preparation_steps[0]"],
    "decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 main preparation paragraph", "source_quote": "oxygen-free
    N 2 -CO 2 (80:20)", "explanation": "Preserve the stated gas ratio and atmosphere;
    this is not an incubation temperature or experimentally demonstrated optimum."},
    {"field_paths": ["preparation_steps[0]", "solutions"], "decision": "evidence_only",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 main preparation paragraph", "source_quote": "0.2 ml
    APM salts solution", "explanation": "The addition is retained in prose but needs
    a resolvable relationship to the separately prepared APM stock; it is added after
    main-mixture autoclaving."}, {"field_paths": ["preparation_steps[0]", "solutions"],
    "decision": "evidence_only", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512",
    "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 main preparation paragraph", "source_quote": "0.1 ml
    Sulfide stock solution", "explanation": "The addition is retained in prose but
    needs its source stock recipe and separate autoclaving scope."}, {"field_paths":
    ["preparation_steps[0]", "solutions"], "decision": "evidence_only", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM 512 main preparation paragraph", "source_quote": "0.1 ml
    Galactose stock solution", "explanation": "The addition is retained in prose but
    needs its stock recipe and filter-sterilization exception."}, {"field_paths":
    ["sterilization", "preparation_steps"], "decision": "add", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=512", "source_sha256": "e5b7df028a3fbf404a3e6e8555da3f28d759f69d0981b2b5e08ddfa802789674",
    "source_locator": "JCM page-wide default preceding recipe 512", "source_quote":
    "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
    "explanation": "The primary page-wide default is absent; retain it only where
    no source exception applies. The galactose stock is explicitly filter-sterilized."}]'
- assessment_id: stocks
  area: representation
  topic: Five stocks and both addition stages
  outcome: concern
  summary: The full sources define all five stock recipes. DL vitamins and DL minerals
    each enter the main mixture as 10 ml additions; APM, sulfide and galactose enter
    the dispensed aliquot later. The preparation prose preserves the three later doses
    but the record has no structured stock relationships or recipes. Removing stock-strength
    flat rows alone would lose source constituents unless the stock relationships
    are restored.
  target_ids:
  - CultureMech:002863
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - quantities
  - writer
- assessment_id: forms
  area: grounding
  topic: Every asserted chemical form and secondary key
  outcome: concern
  summary: All 31 primary canonical labels resolve, but neutral nitrilotriacetic acid
    is not the stated trisodium salt, nickel dichloride lacks the specified hexahydrate,
    and manganese sulfate has no water in its asserted formula despite source variable
    hydration. Thioctic acid is not specified as the R enantiomer. The generic vitamin
    B12 and galactose terms remain appropriately broad; no vitamer or stereoisomer
    is invented. Thirty secondary keys are asserted, with 29 live pinned-index matches
    and one absent lipoic key. The missing manganese secondary link remains unasserted,
    not fabricated.
  target_ids:
  - CultureMech:002863
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - mim
  - mim-lipoic-absence
  - chebi44557
  - chebi34887
  - chebi86360
  - chebi30314
  - chebi176843
  - chebi28260
- assessment_id: preparation
  area: completeness
  topic: Solvents, storage, sterilization and pH stage
  outcome: concern
  summary: The primary recipe supplies all six solvent quantities. Stock headings
    distinguish refrigerated DL solutions, autoclaved APM/sulfide stocks and filter-sterilized
    galactose. These scopes and page-default autoclave parameters are absent from
    the record. The main paragraph correctly retains anaerobic atmosphere, aliquot,
    vessel capacity and later addition order; The schema target pH 6.8 and its pre-bicarbonate
    adjustment stage are already correctly retained; they need claim-level evidence,
    not a value or stage correction.
  target_ids:
  - CultureMech:002863
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - quantities
- assessment_id: classification
  area: scope
  topic: Defined mixture labels and growth boundaries
  outcome: concern
  summary: The record and provider classify this as defined, and the source has no
    complex extract or agar. LIQUID is consistent with the formulation. However, exact
    molecular composition is not completely resolved because manganese hydration and
    the B12 vitamer are unspecified; DEFINED must not be read as proof of fully specified
    chemistry. There is no asserted strain, native variant, parent, growth assay or
    external KG correspondence to validate.
  target_ids:
  - CultureMech:002863
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - chebi176843
- assessment_id: history
  area: provenance
  topic: Append-only history and current-code boundaries
  outcome: supported
  summary: All 8 target and 7 owner timestamps carry timezones. Owner history agrees
    with the target before its final merge event. The March cleanup reports three
    duplicate merges, consistent with three current merged-value notes, but no historical
    execution was reproduced. No source, owner, target or history bytes were edited.
  target_ids:
  - CultureMech:002863
  evidence_ids:
  - record
  - owner-0
  - writer
- assessment_id: evidence
  area: evidence
  topic: Exact source access and claim-level support
  outcome: concern
  summary: The source URL is retained only in notes. Neither layer supplies native
    references or claim-level evidence for the stock hierarchy, quantities or chemical
    forms. Reference validation examined zero excerpts. Captured primary, provider
    and ontology versions and original access timestamps remain distinct; present
    source agreement is not retrospective proof of an earlier import.
  target_ids:
  - CultureMech:002863
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - validate-references
  - quantities
findings:
- finding_id: f1
  issue_key: CM002863-stock-strength-flattening
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Five stock formulations are flattened and three cross-stage values are summed
  description: Both layers place all stock constituents in the direct ingredient list
    and add NaCl, magnesium sulfate and calcium chloride values across different volume
    bases. The source explicitly defines five stocks and separately timed additions.
    The flat values therefore misrepresent source quantities and make the stock preparation
    prose unresolved.
  target_ids:
  - CultureMech:002863
  field_paths:
  - ingredients
  - solutions
  - preparation_steps[0]
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - quantities
  - writer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CM002863-salt-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Three asserted chemical identities omit source salt or hydration
  description: The nitrilotriacetate material is explicitly trisodium salt, while
    CHEBI:44557 is neutral C6H9NO6. The nickel ingredient is a hexahydrate but CHEBI:34887
    has formula Cl2Ni. The source manganese sulfate has variable hydration while CHEBI:86360
    has no water in its formula. Canonical label passes and secondary MIM membership
    do not establish equivalence.
  target_ids:
  - CultureMech:002863
  field_paths:
  - ingredients[6].term
  - ingredients[6].mediaingredientmech_chebi_term
  - ingredients[7].term
  - ingredients[16].term
  - ingredients[16].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - chebi44557
  - chebi34887
  - chebi86360
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: CM002863-thioctic-stereochemistry
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Generic thioctic acid is assigned a specific R enantiomer
  description: Both source versions say Thioctic acid without an enantiomer qualifier.
    The asserted primary and secondary CHEBI:30314 explicitly represent (R)-lipoic
    acid. The available source does not establish that stereochemical narrowing.
  target_ids:
  - CultureMech:002863
  field_paths:
  - ingredients[22].term
  - ingredients[22].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - chebi30314
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: CM002863-preparation-stock-context
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Solvent bases and stock-specific handling are incompletely retained
  description: No solvent quantities or stock headings survive as structured preparation
    context. The DL stocks are refrigerated, APM and sulfide stocks are autoclaved,
    and galactose is filter-sterilized. The JCM page-default autoclave parameters
    are also absent. The existing main preparation paragraph and post-autoclave addition
    order should be retained.
  target_ids:
  - CultureMech:002863
  field_paths:
  - solutions
  - preparation_steps
  - sterilization
  - notes
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: CM002863-secondary-lipoic-link
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: The secondary lipoic key is absent from the pinned MIM index
  description: CHEBI:30314 is asserted as a secondary key but is absent from every
    row of the pinned index. Twenty-nine other secondary keys resolve in that snapshot.
    This linkage issue is separate from the source stereochemical overstatement.
  target_ids:
  - CultureMech:002863
  field_paths:
  - ingredients[22].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - mim
  - mim-lipoic-absence
  - chebi30314
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: CM002863-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source notes do not provide claim-level stock and quantity support
  description: Neither layer has native source references or evidence snippets for
    the quantities, stock recipes, material forms or handling conditions. The source
    link in notes and passing zero-excerpt reference check do not provide claim-level
    support. The already correct target pH and adjustment stage need only exact supporting
    evidence.
  target_ids:
  - CultureMech:002863
  field_paths:
  - ingredients[*].evidence
  - solutions
  - references
  - evidence
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - quantities
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml
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
  description: Restore all five source stock relationships and their individual recipes,
    solvent bases and addition stages in maintained inputs. Keep original masses and
    volumes with evidence, undo cross-stage sums, and derive any final concentration
    only after explicitly fixing the applicable volume basis. Preserve the three later
    additions that are present only in preparation text.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002863
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml
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
  description: Reconcile each exact source material with verified ontology terms and
    preserve salt/hydrate qualifiers in both primary and secondary assertions. Leave
    the unspecified manganese hydration explicit; do not guess a particular hydrate
    or use an anhydrous molecular mass for the stated material.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002863
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml
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
  description: Preserve the source generic material until source-specific stereochemistry
    is verified. Reconcile primary and secondary links against verified appropriately
    scoped terms, without guessing a replacement or changing canonical labels to hide
    the mismatch.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002863
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml
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
  description: Preserve the exact source solvent quantities, storage qualifiers and
    sterilization scopes for each stock and main mixture, with the galactose exception
    explicit. Retain source addition order and distinguish vessel capacity from liquid
    volume; do not invent storage temperatures or filter pore sizes.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002863
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml
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
  description: Reconcile the secondary key against versioned authoritative MIM evidence
    after resolving source material scope. Preserve other verified links and leave
    unresolved correspondence explicit; do not infer a replacement from a similar
    name.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:002863
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml
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
  description: Add exact claim-level excerpts and locators to maintained source claims,
    distinguishing JCM origin from MediaDive hosting and preserving original capture
    versions/times. Confirm the evidence survives authorized regeneration without
    rewriting existing history.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:002863
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J512_A1_MEDIUM.yaml
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
- The provider declares a 1020 ml main-solution basis while JCM lists 1 L water plus
  two 10 ml stock additions. This is a nominal addition-volume convention, not a measured
  final volume or permission to silently normalize everything to 1 L.
- The source leaves manganese sulfate hydration variable and vitamin B12 chemically
  generic. No particular hydrate, B12 vitamer, galactose stereoisomer, thioctic-acid
  enantiomer or organism-specific growth result is inferred. Provider mmol/L fields
  are retained only as captured data, not endorsed conversions.
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
