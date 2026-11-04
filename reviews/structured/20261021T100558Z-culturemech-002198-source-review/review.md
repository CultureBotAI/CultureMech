# Source and formulation review: acetivibrio_medium (CultureMech:002198)

- Review: 20261021T100558Z-culturemech-002198-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T09:56:46Z
- Finished UTC: 2026-10-21T10:05:58Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The JCM 1013 identity resolves, but the record conflates basal and trace-stock strengths with receiving-medium concentrations and links a different vitamin mixture. Exact stock sources, liquid doses, chemical forms and primary/provider disagreements are separately documented. No record or stock was changed.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 144; batch 015 item 4 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding fourteen task batches contain 140 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 142 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002198 | data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml | generated | acetivibrio_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002198 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002198 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch015/144/strict.tsv |
| validate-terms | passed | True | CultureMech:002198 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002198 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002198 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Scoped history timestamp syntax and timezone check | failed | False | CultureMech:002198 | 26 timestamp instances inspected; 2 malformed or timezone-naive instances. Existing provenance is preserved; no timestamps were rewritten. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002198.

The four documented recipes completed; interpret the scope of each separately.

### Exact accession, owner and asserted dependency

identity: supported. Targets: CultureMech:002198.

JCM 1013, MediaDive J1013 and the complete normalized owner agree on the medium identity. The owner and target differ only by merge metadata/history. Stock 6241 resolves to CultureMech:014933; source-specific equivalence is separately refuted below.

### Every direct concentration and separate stock stage

quantity: concern. Targets: CultureMech:002198.

The 49 decisions distinguish eight main additions, six basal rows, ten SL-10 rows, four selenite-tungstate rows, eleven vitamin rows, four dependency rows and six preparation/volume contexts. Main percentage-stock doses were mislabeled as mass, 17 stock constituents were flattened, and the vitamin dose is dimensionally wrong. Two direct provider mass rates are supported on its declared volume basis.

[{"field_path": "solutions (missing source stock descriptor)", "name": "Basal medium", "decision": "add", "stage": "Main recipe stock addition", "stored": null, "explanation": "Preserve the source volume dose and its referenced stock definition separately. Constituent stock strengths are currently flattened into direct ingredient concentrations; do not treat the listed mL dose as g/L.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "Basal medium (see below) 950.0 ml", "source_locator": "JCM 1013 main table row 1", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Basal medium\",\n                        \"solution_id\": 5056,\n                        \"amount\": 950,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[0]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]}, {"field_path": "solutions (missing source stock descriptor)", "name": "Trace element solution SL-10", "decision": "add", "stage": "Main recipe stock addition", "stored": null, "explanation": "Preserve the source volume dose and its referenced stock definition separately. Constituent stock strengths are currently flattened into direct ingredient concentrations; do not treat the listed mL dose as g/L.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "Trace element solution SL-10 (see Medium No. 433 ) 1.0 ml", "source_locator": "JCM 1013 main table row 2", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 4178,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[1]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]}, {"field_path": "solutions (missing source stock descriptor)", "name": "Selenite-tungstate solution", "decision": "add", "stage": "Main recipe stock addition", "stored": null, "explanation": "Preserve the source volume dose and its referenced stock definition separately. Constituent stock strengths are currently flattened into direct ingredient concentrations; do not treat the listed mL dose as g/L.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "Selenite-tungstate solution(see Medium No. 554 ) 1.0 ml", "source_locator": "JCM 1013 main table row 3", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[2]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]}, {"field_path": "solutions[0]", "name": "Vitamin solution", "decision": "correct", "stage": "Main recipe vitamin stock addition", "stored": {"preferred_term": "Vitamin solution", "term": {"id": "mediadive.solution:6241", "label": "Vitamin solution"}, "concentration": {"value": "10", "unit": "G_PER_L"}, "notes": "See mediadive_6241_Vitamin_solution.yaml for composition", "name": "Unknown solution"}, "explanation": "The source specifies 10 mL of the JCM 197 Trace vitamins stock. Local 10 G_PER_L is dimensionally wrong, and asserted 6241 is a different three-vitamin mixture. Resolve exact stock identity before any dilution calculation.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "Vitamin solution (see Medium No. 197 ) 10.0 ml", "source_locator": "JCM 1013 main table row 4", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Vitamin solution\",\n                        \"compound_id\": 154,\n                        \"attribute\": \"see Medium No. 197\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[3]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]}, {"field_path": "ingredients[0].concentration", "name": "NaHCO3", "decision": "correct", "stage": "Main recipe percentage-stock addition", "stored": {"value": "30", "unit": "G_PER_L"}, "explanation": "The literal source is a volume of an explicitly w/v stock, not a neat-compound mass concentration. Preserve stock strength and addition volume. Derived batch mass is separate from any final concentration.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "NaHCO 3 (5%, w/v) 30.0 ml", "source_locator": "JCM 1013 main table row 5", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"attribute\": \"5%, w/v\",\n                        \"amount\": 30,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[4]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"calculation": "5 g/100 mL × 30 mL = 1.5 g per listed batch", "batch_mass_g": "1.5", "receiving_final_volume": "not measured by this source; provider separately declares 1002 mL"}}, {"field_path": "ingredients[1].concentration", "name": "Sucrose", "decision": "correct", "stage": "Main recipe percentage-stock addition", "stored": {"value": "10", "unit": "G_PER_L"}, "explanation": "The literal source is a volume of an explicitly w/v stock, not a neat-compound mass concentration. Preserve stock strength and addition volume. Derived batch mass is separate from any final concentration.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "Sucrose (20%, w/v) 10.0 ml", "source_locator": "JCM 1013 main table row 6", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Sucrose\",\n                        \"compound_id\": 108,\n                        \"attribute\": \"20%, w/v\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[5]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"calculation": "20 g/100 mL × 10 mL = 2 g per listed batch", "batch_mass_g": "2", "receiving_final_volume": "not measured by this source; provider separately declares 1002 mL"}}, {"field_path": "ingredients[2].concentration", "name": "Yeast extract", "decision": "evidence_only", "stage": "Main recipe direct mass addition", "stored": {"value": "0.0499002", "unit": "G_PER_L"}, "explanation": "The stored value agrees with provider g_l and its declared 1002 mL normalization. Add narrow source evidence; do not call this an independently measured final-medium concentration.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "Yeast extract 50.0 mg", "source_locator": "JCM 1013 main table row 7", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0499002,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[6]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"calculation": "50 mg × 0.001 g/mg / 1.002 L = 0.04990019960079840319361277445 g/L", "basis": "provider-declared volume only", "reported_g_per_l": 0.0499002}}, {"field_path": "ingredients[3].concentration", "name": "Na2S x 9 H2O", "decision": "evidence_only", "stage": "Main recipe direct mass addition", "stored": {"value": "0.249501", "unit": "G_PER_L"}, "explanation": "The stored value agrees with provider g_l and its declared 1002 mL normalization. Add narrow source evidence; do not call this an independently measured final-medium concentration.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "Na 2 S·9H 2 O 0.25 g", "source_locator": "JCM 1013 main table row 8", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.249501,\n                        \"mmol_l\": 1.0388,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[7]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"calculation": "0.25 g × 1 g/g / 1.002 L = 0.2495009980039920159680638723 g/L", "basis": "provider-declared volume only", "reported_g_per_l": 0.249501}}, {"field_path": "ingredients[4].concentration", "name": "KH2PO4", "decision": "correct", "stage": "Basal medium", "stored": {"value": "1.47368", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "KH 2 PO 4 1.4 g", "source_locator": "Basal medium subsection, literal row 1", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.47368,\n                        \"mmol_l\": 10.8291,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[0]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 950, "provider_stock_g_l": 1.47368, "receiving_dose_ml": 950, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[5].concentration", "name": "NH4Cl", "decision": "correct", "stage": "Basal medium", "stored": {"value": "0.526316", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "NH 4 Cl 0.5 g", "source_locator": "Basal medium subsection, literal row 2", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.526316,\n                        \"mmol_l\": 9.83952,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[1]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 950, "provider_stock_g_l": 0.526316, "receiving_dose_ml": 950, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[6].concentration", "name": "MgCl2 x 6 H2O", "decision": "correct", "stage": "Basal medium", "stored": {"value": "0.210526", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "MgCl 2 ·6H 2 O 0.2 g", "source_locator": "Basal medium subsection, literal row 3", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.210526,\n                        \"mmol_l\": 1.03553,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[2]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 950, "provider_stock_g_l": 0.210526, "receiving_dose_ml": 950, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[7].concentration", "name": "CaCl2 x 2 H2O", "decision": "correct", "stage": "Basal medium", "stored": {"value": "0.157895", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "CaCl 2 ·2H 2 O 0.15 g", "source_locator": "Basal medium subsection, literal row 4", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.157895,\n                        \"mmol_l\": 1.074,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[3]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 950, "provider_stock_g_l": 0.157895, "receiving_dose_ml": 950, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[8].concentration", "name": "Resazurin", "decision": "correct", "stage": "Basal medium", "stored": {"value": "0.00105263", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "Resazurin 1.0 mg", "source_locator": "Basal medium subsection, literal row 5", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00105263,\n                        \"mmol_l\": 0.00459283,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[4]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 950, "provider_stock_g_l": 0.00105263, "receiving_dose_ml": 950, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "stock preparation solvent context", "name": "Distilled water", "decision": "add", "stage": "Basal medium", "stored": null, "explanation": "Preserve this solvent amount within its own source stock batch; never add separate stock water amounts into a final-medium water mass or infer measured final volume.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "Distilled water 950.0 ml", "source_locator": "Basal medium subsection, literal row 6", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 950,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[5]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]}, {"field_path": "ingredients[9].concentration", "name": "HCl", "decision": "conflict", "stage": "Trace element solution SL-10", "stored": {"value": "2.5", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic. The source HCl strength 7.7 M implies a different mass from provider 2.5 g/L on the provider one-liter stock basis. The source bare 25% does not specify w/v or justify overriding its explicit molarity.", "source_snippets": [{"source_key": "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_quote": "HCl (25%, 7.7 M) 10.0 ml", "source_locator": "Trace element solution SL-10 subsection, literal row 1", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%, 7.7 M\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[0]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 2.5, "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted", "conditional_stock_mass_g": "2.8074970", "calculation": "7.7 mol/L × 0.010 L × 36.461 g/mol = 2.807497 g; dividing by the provider-declared 1 L stock gives 2.807497 g/L, versus reported 2.5 g/L"}}, {"field_path": "ingredients[10].concentration", "name": "FeCl2 x 4 H2O", "decision": "correct", "stage": "Trace element solution SL-10", "stored": {"value": "1.5", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_quote": "FeCl 2 ·4H 2 O 1.5 g", "source_locator": "Trace element solution SL-10 subsection, literal row 2", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[1]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 1.5, "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[11].concentration", "name": "ZnCl2", "decision": "correct", "stage": "Trace element solution SL-10", "stored": {"value": "0.07", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_quote": "ZnCl 2 70.0 mg", "source_locator": "Trace element solution SL-10 subsection, literal row 3", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[2]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.07, "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[12].concentration", "name": "MnCl2 x 4 H2O", "decision": "correct", "stage": "Trace element solution SL-10", "stored": {"value": "0.1", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_quote": "MnCl 2 ·4H 2 O 100.0 mg", "source_locator": "Trace element solution SL-10 subsection, literal row 4", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[3]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.1, "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[13].concentration", "name": "H3BO3", "decision": "correct", "stage": "Trace element solution SL-10", "stored": {"value": "0.006", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_quote": "H 3 BO 3 6.0 mg", "source_locator": "Trace element solution SL-10 subsection, literal row 5", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[4]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.006, "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[14].concentration", "name": "CoCl2 x 6 H2O", "decision": "correct", "stage": "Trace element solution SL-10", "stored": {"value": "0.19", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_quote": "CoCl 2 ·6H 2 O 190.0 mg", "source_locator": "Trace element solution SL-10 subsection, literal row 6", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[5]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.19, "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[15].concentration", "name": "CuCl2 x 2 H2O", "decision": "correct", "stage": "Trace element solution SL-10", "stored": {"value": "0.002", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_quote": "CuCl 2 ·2H 2 O 2.0 mg", "source_locator": "Trace element solution SL-10 subsection, literal row 7", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[6]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.002, "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[16].concentration", "name": "NiCl2 x 6 H2O", "decision": "correct", "stage": "Trace element solution SL-10", "stored": {"value": "0.024", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_quote": "NiCl 2 ·6H 2 O 24.0 mg", "source_locator": "Trace element solution SL-10 subsection, literal row 8", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[7]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.024, "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[17].concentration", "name": "Na2MoO4 x 2 H2O", "decision": "correct", "stage": "Trace element solution SL-10", "stored": {"value": "0.036", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_quote": "Na 2 MoO 4 ·2H 2 O 36.0 mg", "source_locator": "Trace element solution SL-10 subsection, literal row 9", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[8]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.036, "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "stock preparation solvent context", "name": "Distilled water", "decision": "add", "stage": "Trace element solution SL-10", "stored": null, "explanation": "Preserve this solvent amount within its own source stock batch; never add separate stock water amounts into a final-medium water mass or infer measured final volume.", "source_snippets": [{"source_key": "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_quote": "Distilled water 990.0 ml", "source_locator": "Trace element solution SL-10 subsection, literal row 10", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[9]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]}, {"field_path": "ingredients[18].concentration", "name": "NaOH", "decision": "correct", "stage": "Selenite-tungstate solution", "stored": {"value": "0.5", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm554", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=554", "source_quote": "NaOH 0.5 g", "source_locator": "Selenite-tungstate solution subsection, literal row 1", "source_sha256": "f37922162077d3f497dd07baa484a66a223e3225eadd1dee22fad2aebf794694"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[0]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.5, "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[19].concentration", "name": "Na2SeO3 x 5 H2O", "decision": "correct", "stage": "Selenite-tungstate solution", "stored": {"value": "0.003", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm554", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=554", "source_quote": "Na 2 SeO 3 ·5H 2 O 0.003 g", "source_locator": "Selenite-tungstate solution subsection, literal row 2", "source_sha256": "f37922162077d3f497dd07baa484a66a223e3225eadd1dee22fad2aebf794694"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[1]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.003, "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[20].concentration", "name": "Na2WO4 x 2 H2O", "decision": "correct", "stage": "Selenite-tungstate solution", "stored": {"value": "0.004", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider stock-strength value, incorrectly placed as a direct receiving-medium ingredient. Preserve the original stock batch and its separately documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm554", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=554", "source_quote": "Na 2 WO 4 ·2H 2 O 0.004 g", "source_locator": "Selenite-tungstate solution subsection, literal row 3", "source_sha256": "f37922162077d3f497dd07baa484a66a223e3225eadd1dee22fad2aebf794694"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[2]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}], "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.004, "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002 mL; no measured final volume asserted"}}, {"field_path": "stock preparation solvent context", "name": "Distilled water", "decision": "add", "stage": "Selenite-tungstate solution", "stored": null, "explanation": "Preserve this solvent amount within its own source stock batch; never add separate stock water amounts into a final-medium water mass or infer measured final volume.", "source_snippets": [{"source_key": "jcm554", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=554", "source_quote": "Distilled water 1.0 L", "source_locator": "Selenite-tungstate solution subsection, literal row 4", "source_sha256": "f37922162077d3f497dd07baa484a66a223e3225eadd1dee22fad2aebf794694"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[3]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]}, {"field_path": "solutions[0].source-specific composition", "name": "Biotin", "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null, "explanation": "Recover this exact stock constituent or solvent context, keeping its one-liter source batch separate from the 10 mL receiving dose. This is not evidence for a parent-medium ingredient, replacement ontology ID or growth claim.", "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_quote": "Biotin 2.0 mg", "source_locator": "Trace vitamins subsection row 1", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"}, {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00818632,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[0]", "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]}, {"field_path": "solutions[0].source-specific composition", "name": "Folic acid", "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null, "explanation": "Recover this exact stock constituent or solvent context, keeping its one-liter source batch separate from the 10 mL receiving dose. This is not evidence for a parent-medium ingredient, replacement ontology ID or growth claim.", "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_quote": "Folic acid 2.0 mg", "source_locator": "Trace vitamins subsection row 2", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"}, {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00453104,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[1]", "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]}, {"field_path": "solutions[0].source-specific composition", "name": "Pyridoxine hydrochloride", "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null, "explanation": "Recover this exact stock constituent or solvent context, keeping its one-liter source batch separate from the 10 mL receiving dose. This is not evidence for a parent-medium ingredient, replacement ontology ID or growth claim.", "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_quote": "Pyridoxine·HCl 10.0 mg", "source_locator": "Trace vitamins subsection row 3", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"}, {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0486287,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[2]", "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]}, {"field_path": "solutions[0].source-specific composition", "name": "Thiamine HCl", "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null, "explanation": "Recover this exact stock constituent or solvent context, keeping its one-liter source batch separate from the 10 mL receiving dose. This is not evidence for a parent-medium ingredient, replacement ontology ID or growth claim.", "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_quote": "Thiamine·HCl 5.0 mg", "source_locator": "Trace vitamins subsection row 4", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"}, {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197", "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0148236,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[3]", "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]}, {"field_path": "solutions[0].source-specific composition", "name": "Riboflavin", "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null, "explanation": "Recover this exact stock constituent or solvent context, keeping its one-liter source batch separate from the 10 mL receiving dose. This is not evidence for a parent-medium ingredient, replacement ontology ID or growth claim.", "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_quote": "Riboflavin 5.0 mg", "source_locator": "Trace vitamins subsection row 5", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"}, {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197", "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0132837,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[4]", "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]}, {"field_path": "solutions[0].source-specific composition", "name": "Nicotinic acid", "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null, "explanation": "Recover this exact stock constituent or solvent context, keeping its one-liter source batch separate from the 10 mL receiving dose. This is not evidence for a parent-medium ingredient, replacement ontology ID or growth claim.", "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_quote": "Nicotinic acid 5.0 mg", "source_locator": "Trace vitamins subsection row 6", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"}, {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197", "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0406141,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[5]", "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]}, {"field_path": "solutions[0].source-specific composition", "name": "Calcium pantothenate", "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null, "explanation": "Recover this exact stock constituent or solvent context, keeping its one-liter source batch separate from the 10 mL receiving dose. This is not evidence for a parent-medium ingredient, replacement ontology ID or growth claim.", "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_quote": "Calcium pantothenate 5.0 mg", "source_locator": "Trace vitamins subsection row 7", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"}, {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197", "source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0104925,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[6]", "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]}, {"field_path": "solutions[0].source-specific composition", "name": "Vitamin B12", "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null, "explanation": "Recover this exact stock constituent or solvent context, keeping its one-liter source batch separate from the 10 mL receiving dose. This is not evidence for a parent-medium ingredient, replacement ontology ID or growth claim.", "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_quote": "Vitamin B 1 2 0.1 mg", "source_locator": "Trace vitamins subsection row 8", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"}, {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197", "source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\": 7.3779e-5,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[7]", "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]}, {"field_path": "solutions[0].source-specific composition", "name": "p-Aminobenzoic acid", "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null, "explanation": "Recover this exact stock constituent or solvent context, keeping its one-liter source batch separate from the 10 mL receiving dose. This is not evidence for a parent-medium ingredient, replacement ontology ID or growth claim.", "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_quote": "p -Aminobenzoic acid 5.0 mg", "source_locator": "Trace vitamins subsection row 9", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"}, {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197", "source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0364591,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[8]", "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]}, {"field_path": "solutions[0].source-specific composition", "name": "Lipoic acid", "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null, "explanation": "Recover this exact stock constituent or solvent context, keeping its one-liter source batch separate from the 10 mL receiving dose. This is not evidence for a parent-medium ingredient, replacement ontology ID or growth claim.", "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_quote": "Lipoic acid 5.0 mg", "source_locator": "Trace vitamins subsection row 10", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"}, {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197", "source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Lipoic acid\",\n                        \"compound_id\": 368,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.024233,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[9]", "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]}, {"field_path": "solutions[0].source-specific composition", "name": "Distilled water", "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null, "explanation": "Recover this exact stock constituent or solvent context, keeping its one-liter source batch separate from the 10 mL receiving dose. This is not evidence for a parent-medium ingredient, replacement ontology ID or growth claim.", "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_quote": "Distilled water 1.0 L", "source_locator": "Trace vitamins subsection row 11", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"}, {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197", "source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[10]", "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]}, {"field_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml:composition[0].concentration", "name": "Cyanocobalamine", "decision": "verified", "stage": "Asserted wrong-stock dependency 6241 only", "stored": {"value": "0.1", "unit": "G_PER_L"}, "explanation": "The local concentration and existing literal excerpt match this 100 mL stock. That supports stock 6241 only, not its substitution for JCM 197.", "source_snippets": [{"source_key": "solution6241", "source_reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            }", "source_locator": "$.data.recipe[0]", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"}, {"source_key": "solution6241", "source_reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_quote": "\"Make up to 100 ml with distilled water.\"", "source_locator": "$.data.steps[0].step", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"}]}, {"field_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml:composition[1].concentration", "name": "Thiamine HCl", "decision": "verified", "stage": "Asserted wrong-stock dependency 6241 only", "stored": {"value": "0.1", "unit": "G_PER_L"}, "explanation": "The local concentration and existing literal excerpt match this 100 mL stock. That supports stock 6241 only, not its substitution for JCM 197.", "source_snippets": [{"source_key": "solution6241", "source_reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\": 0\n            }", "source_locator": "$.data.recipe[1]", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"}, {"source_key": "solution6241", "source_reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_quote": "\"Make up to 100 ml with distilled water.\"", "source_locator": "$.data.steps[0].step", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"}]}, {"field_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml:composition[2].concentration", "name": "Biotin", "decision": "correct", "stage": "Asserted wrong-stock dependency 6241 only", "stored": {"value": "2000.0", "unit": "G_PER_L"}, "explanation": "200 micrograms / 100 mL = 0.002 g/L on the explicit make-up-to-volume basis, whereas the dependency stores 2000 g/L. This dependency error is not a proposed receiving-medium concentration.", "source_snippets": [{"source_key": "solution6241", "source_reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "source_locator": "$.data.recipe[2]", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"}, {"source_key": "solution6241", "source_reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_quote": "\"Make up to 100 ml with distilled water.\"", "source_locator": "$.data.steps[0].step", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"}]}, {"field_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml:composition[3].concentration", "name": "Distilled water", "decision": "correct", "stage": "Asserted wrong-stock dependency 6241 only", "stored": {"value": "1000.0", "unit": "PERCENT_V_V"}, "explanation": "The source makes the stock up to 100 mL with water; local 1000 PERCENT_V_V is not supported. Preserve solvent volume context, not a water concentration.", "source_snippets": [{"source_key": "solution6241", "source_reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }", "source_locator": "$.data.recipe[3]", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"}, {"source_key": "solution6241", "source_reference": "https://mediadive.dsmz.de/rest/solution/6241", "source_quote": "\"Make up to 100 ml with distilled water.\"", "source_locator": "$.data.steps[0].step", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"}]}, {"field_path": "ph_value; preparation_steps[0]", "name": "Source pH range", "decision": "evidence_only", "stage": "JCM 1013 main preparation", "stored": null, "explanation": "Local 7.8 equals provider min/max and lies within the primary range; local prose retains the range. Preserve that range and its conditional adjustment scope instead of declaring 7.8 wrong or an optimum.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "Readjust pH to 7.7 - 7.9, if necessary.", "source_locator": "Default-cycle header or exact main preparation sentence", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}]}, {"field_path": "preparation_steps", "name": "Default source sterilization cycle", "decision": "add", "stage": "JCM 1013 main preparation", "stored": null, "explanation": "The primary default cycle is absent from local prose. Preserve it with the explicit filtering and separate-autoclaving exceptions; it does not authorize autoclaving every stock together.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.", "source_locator": "Default-cycle header or exact main preparation sentence", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}]}, {"field_path": "preparation_steps[0]", "name": "Atmosphere", "decision": "evidence_only", "stage": "JCM 1013 main preparation", "stored": null, "explanation": "The exact atmosphere is retained in local prose. This is preparation context, not evidence of strain-specific growth.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "under 100% N 2 gas", "source_locator": "Default-cycle header or exact main preparation sentence", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}]}, {"field_path": "preparation_steps[0]", "name": "Sulfide stock strength", "decision": "not_quantified", "stage": "JCM 1013 main preparation", "stored": null, "explanation": "Preserve the literal 5% solution and separate preparation context. The sentence does not specify percentage basis or dosing volume; do not infer a w/v conversion or receiving final volume from it.", "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "5% Na 2 S·9H 2 O solution (autoclaved under N 2 gas)", "source_locator": "Default-cycle header or exact main preparation sentence", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}]}, {"field_path": "preparation_steps[1]", "name": "SL-10 stock preparation", "decision": "correct", "stage": "JCM 433 SL-10 stock only", "stored": null, "explanation": "The literal sequence is retained locally but detached into the main recipe preparation array. Keep it scoped to the trace stock rather than interpreted as a whole-medium operation.", "source_snippets": [{"source_key": "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_quote": "Dissolve FeCl 2 ·4H 2 O first in HCl. Then dilute in distilled water and add the remaining salts.", "source_locator": "SL-10 subsection paragraph immediately following its table", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "\"Dissolve FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining salts.\"", "source_locator": "$.data.solutions[2].steps[0].step", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]}, {"field_path": "source volume context", "name": "Provider volume declarations", "decision": "evidence_only", "stage": "Each independently declared solution volume", "stored": null, "explanation": "Preserve the separate volume bases: main 1002 mL, basal 950 mL, SL-10 1000 mL and selenite-tungstate 1000 mL. They are not interchangeable or measured receiving volumes. No addition volume for the separate sulfide solution is inferred.", "source_snippets": [{"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "1002", "source_locator": "$.data.solutions[0].volume", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "950", "source_locator": "$.data.solutions[1].volume", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "1000", "source_locator": "$.data.solutions[2].volume", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}, {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "1000", "source_locator": "$.data.solutions[3].volume", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]}]

### Identifiers, labels and exact source forms

grounding: concern. Targets: CultureMech:002198.

Both target and owner have 20/21 primary and 20/21 secondary ingredient links (95.24% linkage coverage, not a correctness score); all asserted labels and current MIM keys resolve. Explicit nickel chloride hexahydrate is mapped to CHEBI:34887, whose structure has no waters. The other explicit hydrate formulas correspond. The source says generic Resazurin here, so no sodium-salt discrepancy is inferred. Linked-stock provider compound IDs and CHEBI metadata resolve; cyanocob(III)alamin identifies one B12 form, not all vitamin stocks. Yeast extract remains an undefined mixture.

### JCM 197 versus asserted solution 6241

identity: concern. Targets: CultureMech:002198.

The named source stock has ten vitamins in a one-liter batch, while 6241 contains three vitamins made up to 100 mL with different amounts. Two verified dependency excerpts do not establish equivalence. The source-specific 3861 provider object corroborates JCM 197 but is not an automatically minted or substituted local ID. The 6241 biotin and water quantities also conflict with its own provider.

### Main preparation, source defaults and stock-only instructions

completeness: concern. Targets: CultureMech:002198.

Main prose preserves gas, separate sterilization, filtration, reducing-agent and conditional pH contexts. It omits the printed source default cycle and attaches the SL-10 dissolution instruction to the main array without stock scope. Keep all source exceptions and the primary pH range; 7.8 is within that range and is not itself a wrong value. No incubation, storage or new growth claim is inferred.

### Liquid complex medium and biological limits

scope: supported. Targets: CultureMech:002198.

The exact source has yeast extract and defined salts, consistent with COMPLEX/SEMI_DEFINED and LIQUID. No target organism, strain, taxonomic ID, experimental variant or KG match is asserted. The title and generic cultivation application do not establish growth evidence. The auxiliary stock is contextual, not an additional reviewed medium.

### Exact maintained input and current transforms

ownership: concern. Targets: CultureMech:002198.

The target and main owner share all scientific fields. Corrections belong first in the exact JCM owner, with separate dependency follow-up if authorized, then merge regeneration. Current importer and name-based migration mechanisms can explain classes of representation errors but do not replay historical execution. No generated file was edited.

### Narrow support and existing dependency excerpts

evidence: concern. Targets: CultureMech:002198.

Target and main owner lack claim-level source excerpts. The target reference check examines zero excerpts. The two dependency quantity snippets match current identical provider bytes and retain their historical hash/time, but support only their own 6241 quantities. All primary/provider disputes and stages remain explicit.

### Append-only event history and timestamp interpretation

provenance: concern. Targets: CultureMech:002198.

All 26 scoped timestamps were checked for ISO syntax and timezone. 2 instances are malformed or lack timezone, as itemized. Curation events are process provenance rather than independent confirmation of recipe correctness.

[{"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-14T21:09:46.292785", "valid_ISO_datetime": true, "timezone_aware": false, "problem": "Timezone absent; local time cannot be asserted as UTC"}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml", "field": "curation_history[3].timestamp", "value": "2026-04-04T17:50:16.857966", "valid_ISO_datetime": true, "timezone_aware": false, "problem": "Timezone absent; local time cannot be asserted as UTC"}]

## Findings

### f1: Stock definitions and liquid additions are represented as direct medium concentrations

blocker / open / confirmed; issue key: cm002198-stock-stage-collapse.

The main record stores 30 and 10 G_PER_L for 30 mL of 5% w/v bicarbonate and 10 mL of 20% w/v sucrose; their source batch masses are 1.5 and 2 g. Five basal constituents and twelve trace-stock constituents retain their own stock-strength values as direct medium concentrations. Three source stock doses are missing and the vitamin dose is 10 G_PER_L instead of 10 mL. The represented formulation therefore differs materially from the source.

### f2: The vitamin link resolves to a different source stock

major / open / confirmed; issue key: cm002198-wrong-vitamin-stock.

The local mediadive.solution:6241 link resolves, but JCM 1013 explicitly cites JCM 197 Trace vitamins. The source ten-vitamin one-liter stock differs from the three-vitamin 100 mL dependency. Existing 6241 evidence verifies only two of its own quantities and cannot establish this cross-reference. Its own biotin and solvent values also conflict with its source.

### f3: Explicit nickel hexahydrate is assigned an anhydrous identity

major / open / confirmed; issue key: cm002198-nickel-hydrate-grounding.

Both primary and provider SL-10 sources specify NiCl2 hexahydrate. Target and owner assign CHEBI:34887 to both primary and secondary fields, while that term has formula Cl2Ni and no hydrate waters. Correct labels and current MIM rows do not establish source-form correspondence.

### f4: The SL-10 HCl source molarity conflicts with provider mass normalization

major / open / confirmed; issue key: cm002198-hcl-source-discrepancy.

The primary and provider attribute specify 10 mL HCl at 7.7 M, while provider g_l and the flattened target store 2.5. Conditional on the provider one-liter stock volume and captured hydrogen chloride mass 36.461 g/mol, explicit molarity yields 2.807497 g/L. This source discrepancy remains after separating the stock stage; bare 25% does not establish w/v.

### f5: Preparation omits the source default cycle and detaches stock instructions

major / open / confirmed; issue key: cm002198-preparation-stock-scope.

The main prose retains important source exceptions, but omits the JCM default 121°C/15 min cycle. The SL-10 FeCl2/HCl dissolution sequence is stored as a main preparation step without naming the stock. Quantitative gas, pH and separate sulfide contexts must remain attached to the correct stage.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct source stock boundaries and their exact receiving doses in the maintained JCM owner. Preserve original stock batch amounts, explicit percentage bases and the provider volume convention. Derive receiving concentrations only with an explicit supported denominator and separate arithmetic; do not flatten stock strengths or silently use 1 L.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve the exact source-specific JCM 197 stock and its 10 mL dose before changing the main reference. Preserve the existing dependency as a distinct record; any correction of its biotin or solvent amounts needs its own maintained-input scope. Do not substitute by shared name or apply a 6241 dilution to this medium.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Retain the literal hexahydrate source material and verify a matching ontology identity before changing either primary or secondary grounding. Do not convert its source mass using the anhydrous molecular weight or guess a replacement ID.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve both reported stock-strength representations with their exact sources. Verify the source stock convention before choosing a mass rate, and keep this conflict separate from the receiving dose and final-medium volume. Do not silently reinterpret the percent label.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Preserve the source default cycle with explicit filtration and separate-autoclaving exceptions. Attach the SL-10 dissolution sequence to that stock and retain the conditional pH range and unquantified sulfide percentage/dose scope. Do not introduce additional incubation or culture-performance claims.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch015/144/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch015/144/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| source-catalog | /private/tmp/culturemech-review-work-batch015/source-preflight-bound/144/source-catalog.json; All bound per-record source metadata, successful captures and retained failed attempts | context_only | [{"key": "jcm1013", "url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "status": 200, "accessed_at": "2026-10-21T09:46:51.540618Z", "sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293", "metadata_sha256": "ca50a0be08f4f8371d21ff505b2eccb7cf7824f78c182843be30667f696d4736", "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "mediadiveJ1013api", "url": "https://mediadive.dsmz.de/rest/medium/J1013", "status": 200, "accessed_at": "2026-10-21T09:46:49.455372Z", "sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757", "metadata_sha256": "80d979623d024af7218b06b0f73575932ed8a2ebb35651f17f918062dcecc3d5", "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "solution6241", "url": "https://mediadive.dsmz.de/rest/solution/6241", "status": 200, "accessed_at": "2026-10-21T09:46:49.463537Z", "sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1", "metadata_sha256": "5bef66b98c346817862c93534b9a1cb2dd1e19fa11d34ea4bbf25653ebd8fee4", "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "chebi131361", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361", "status": 200, "accessed_at": "2026-10-21T07:33:27.980786Z", "sha256": "643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10", "metadata_sha256": "233e3bc6eec19f0b2d4910629113871f0f801ec9fad02cbf5d9beba9507302cf", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi131361.json", "content_limit": null, "error": null}, {"key": "chebi15377", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377", "status": 200, "accessed_at": "2026-10-21T08:17:26.097802Z", "sha256": "de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b", "metadata_sha256": "72dd5a7deb860db3666b4e829f29bf7024f17f0e63ff1f513dc3298b07fecb6b", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15377.json", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "error": null}, {"key": "chebi15956", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956", "status": 200, "accessed_at": "2026-10-21T08:42:30.425993Z", "sha256": "d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd", "metadata_sha256": "580492ca7f33dc5a24e7534276bba41e9c94e43c82de73c014d431170af9cf84", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15956.json", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "error": null}, {"key": "chebi17439", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439", "status": 200, "accessed_at": "2026-10-21T07:16:23.574834Z", "sha256": "210a9fbc1db1c75e6053f4e23d098851ad5c63f087c736061f7664d9a393dbdd", "metadata_sha256": "cf2048fac20fa7ff48555c580295fe7ba2f32f9e61fbfd97a4e9b2c390ced0c2", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch010-tail/098/chebi17439.json", "content_limit": null, "error": null}, {"key": "chebi17883", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883", "status": 200, "accessed_at": "2026-10-20T07:37:25.439020Z", "sha256": "1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a", "metadata_sha256": "5756fc4c41d9b29d189fa931f5ba8a1a091e6b3e02abbcb06ae21c5634481def", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/132/chebi17883.json", "content_limit": null, "error": null}, {"key": "chebi17992", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17992", "status": 200, "accessed_at": "2026-10-21T08:42:31.913996Z", "sha256": "509f9cbc014a0211d3a8e536a2c68048a090719ce68ee80550c8bbf532f150aa", "metadata_sha256": "caeb0150bec3f5c620c0d988ce0b93a50ddef9771ee2d6d64500a0b52b78bd40", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/139/chebi17992.json", "content_limit": "Identity/provenance and exact identifier metadata only; no operational formulation or culture-procedure assessment.", "error": null}, {"key": "chebi31206", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206", "status": 200, "accessed_at": "2026-10-21T08:17:28.439407Z", "sha256": "ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76", "metadata_sha256": "df2a292a870613733f0555365eb5e9768259b400982522ff486094a3fa3beb4f", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi31206.json", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "error": null}, {"key": "chebi32139", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139", "status": 200, "accessed_at": "2026-10-21T07:16:24.226823Z", "sha256": "2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe", "metadata_sha256": "e22c2cf978a7ec315cf2c3110ef5b9434dbc17430f3bbb3db5efa02824fbbd1a", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/135/chebi32139.json", "content_limit": null, "error": null}, {"key": "chebi32145", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145", "status": 200, "accessed_at": "2026-10-21T07:33:28.263004Z", "sha256": "db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1", "metadata_sha256": "b20c9d330e1362a45042e189276604a8d16c160bd063fb27e66dad34ccc517fd", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch009-tail/087/chebi32145.json", "content_limit": null, "error": null}, {"key": "chebi33118", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118", "status": 200, "accessed_at": "2026-10-21T08:17:29.364390Z", "sha256": "f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87", "metadata_sha256": "18bce3130b0d0e05a5be03c9efe512ec5ff67bfbbb05b0756a980dffdc42f0f1", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi33118.json", "content_limit": null, "error": null}, {"key": "chebi34887", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887", "status": 200, "accessed_at": "2026-10-21T08:04:44.093348Z", "sha256": "f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc", "metadata_sha256": "c196058e819dd3ceca902ee8cde45f83b9116e94432ec3d92bf8e03de3450238", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi34887.json", "content_limit": null, "error": null}, {"key": "chebi49105", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105", "status": 200, "accessed_at": "2026-10-20T06:55:10.911379Z", "sha256": "0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4", "metadata_sha256": "723b9751feb8ab66f48f87ac82446583bccad1e02c682bf47891a937283af0b1", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi49105.json", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "error": null}, {"key": "chebi49976", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976", "status": 200, "accessed_at": "2026-10-21T08:04:44.168295Z", "sha256": "d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321", "metadata_sha256": "82c37b47478a7a0bdf0c84ee66521938920b2318352268bda11acf60b11c9d10", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/136/chebi49976.json", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "error": null}, {"key": "chebi53503", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503", "status": 200, "accessed_at": "2026-10-21T08:04:44.349630Z", "sha256": "c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d", "metadata_sha256": "1da3e479c9ca2e858e4d07f89b48b11326e3bfdff9418cc9f9520f85ae1901c5", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/136/chebi53503.json", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "error": null}, {"key": "chebi63036", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036", "status": 200, "accessed_at": "2026-10-21T08:17:29.666916Z", "sha256": "48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3", "metadata_sha256": "1ef7480d2ea5bdb5518ad6d5f9a94584384ec48f560ea50a588b29ed366261d4", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/139/chebi63036.json", "content_limit": "Identity/provenance and exact identifier metadata only; no operational formulation or culture-procedure assessment.", "error": null}, {"key": "chebi63939", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939", "status": 200, "accessed_at": "2026-10-20T06:55:09.796192Z", "sha256": "987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a", "metadata_sha256": "1d2cb0b600169daf3922336c8c36707c01ef86d4e6ae6779343c137c93723dc1", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi63939.json", "content_limit": null, "error": null}, {"key": "chebi75213", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213", "status": 200, "accessed_at": "2026-10-21T08:17:29.756647Z", "sha256": "b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083", "metadata_sha256": "1dfd34dea2370cb22006a48279806974a7f52be9b6e115656a108ec2d42554eb", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/136/chebi75213.json", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "error": null}, {"key": "chebi76209", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209", "status": 200, "accessed_at": "2026-10-20T06:55:04.847843Z", "sha256": "f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c", "metadata_sha256": "a27755ce099dd73bdfec1edb24c56a0af540fdeae1c989965ee30e8efb4a0495", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi76209.json", "content_limit": null, "error": null}, {"key": "chebi86158", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158", "status": 200, "accessed_at": "2026-10-21T08:17:30.011607Z", "sha256": "b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61", "metadata_sha256": "43dd1a06fa3c2b5a0bf314b7e7c0fb221d2fb1c6a40bac37548659587cb8a131", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi86158.json", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "error": null}, {"key": "chebi86249", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249", "status": 200, "accessed_at": "2026-10-21T09:46:51.536553Z", "sha256": "63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683", "metadata_sha256": "f241b487470e01e594cf7c82f32a80202526c2c30d9503d7bd5cef7d3228990c", "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "chebi86318", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318", "status": 200, "accessed_at": "2026-10-21T08:43:12.592415Z", "sha256": "9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae", "metadata_sha256": "601d2aa4c49a0c817e8843451d1b7bf043620ea3fd35c5bbfffac4adad3fcb1e", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi86318.json", "content_limit": null, "error": null}, {"key": "chebi86345", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345", "status": 200, "accessed_at": "2026-10-21T08:17:30.382026Z", "sha256": "08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133", "metadata_sha256": "73c55da23f961dac1480e9586e97c0ab02edcf1bb2a09aca9fc1096e629804c5", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi86345.json", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "error": null}, {"key": "chebi86368", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368", "status": 200, "accessed_at": "2026-10-21T08:17:30.657545Z", "sha256": "286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f", "metadata_sha256": "b61427450f992c84099cd291eba6f029aa247d3cef76a6657daa9ac91003aba4", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/136/chebi86368.json", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "error": null}, {"key": "chebi8806", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806", "status": 200, "accessed_at": "2026-10-21T08:17:30.774007Z", "sha256": "e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5", "metadata_sha256": "702243aa23112f8cb9b894281c15988bbea59c02a49404b25ad9ead450f72e95", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi8806.json", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "error": null}, {"key": "jcm433", "url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "status": 200, "accessed_at": "2026-10-21T09:49:11.794269Z", "sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b", "metadata_sha256": "47dc533bf0ec6f6b006880c70306c4a38b24cb278056c5a755a3c818420f5f81", "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "jcm554", "url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=554", "status": 200, "accessed_at": "2026-10-21T09:49:11.794199Z", "sha256": "f37922162077d3f497dd07baa484a66a223e3225eadd1dee22fad2aebf794694", "metadata_sha256": "0ba24d6b872c396d9daa2ba3a2b6f6c2080355fe202709d21f4041f8db40ddf0", "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "jcm197", "url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "status": 200, "accessed_at": "2026-10-20T06:58:05.867253Z", "sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532", "metadata_sha256": "251b36cd6d2c9001683a3035facf9937641aa017f71cfec38be523a5bbd0c4d1", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/jcm197.json", "content_limit": "Trace vitamins subsection only; unrelated parent basal medium excluded.", "error": null}, {"key": "mediadiveJ197api", "url": "https://mediadive.dsmz.de/rest/medium/J197", "status": 200, "accessed_at": "2026-10-21T09:49:11.793511Z", "sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb", "metadata_sha256": "d63c2e386ea604ce8d011033bda0c36c3b4c2b34e9b915d9721ed4d3aba21702", "reused_capture_from": null, "content_limit": null, "error": null}] |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml:1:id: CultureMech:002198<br>./data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml:1:id: CultureMech:002198<br> |
| linked-stock | data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml; Entire exact asserted solution 6241 YAML, including composition, preparation notes, evidence and history | context_only | The asserted ID resolves to this local stock. Its source and composition are compared with the cited JCM 197 stock; file existence does not establish equivalence. |
| jcm1013 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013; Complete primary recipe, basal subsection, default-cycle line and preparation paragraph | supports | Complete primary recipe, basal subsection, default-cycle line and preparation paragraph inspected with stock and receiving-medium boundaries retained. |
| mediadiveJ1013api | https://mediadive.dsmz.de/rest/medium/J1013; Exact medium J1013 and all four solution objects | supports | Exact medium J1013 and all four solution objects inspected with stock and receiving-medium boundaries retained. |
| jcm433 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433; Trace element solution SL-10 subsection only | supports | Trace element solution SL-10 subsection only inspected with stock and receiving-medium boundaries retained. |
| jcm554 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=554; Selenite-tungstate solution subsection only | supports | Selenite-tungstate solution subsection only inspected with stock and receiving-medium boundaries retained. |
| jcm197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Trace vitamins subsection only | supports | Trace vitamins subsection only inspected with stock and receiving-medium boundaries retained. |
| mediadiveJ197api | https://mediadive.dsmz.de/rest/medium/J197; Exact J197 metadata and solution 3861 Trace vitamins only | supports | Exact J197 metadata and solution 3861 Trace vitamins only inspected with stock and receiving-medium boundaries retained. |
| solution6241 | https://mediadive.dsmz.de/rest/solution/6241; Exact solution 6241 metadata, all four rows and make-up-volume instruction | supports | Exact solution 6241 metadata, all four rows and make-up-volume instruction inspected with stock and receiving-medium boundaries retained. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch015/144/quantity-inventory.json; All 49 source-linked decisions, including original units, stages and separate arithmetic | context_only | Covers every target ingredient/stock amount, every cited stock row, the exact contextual dependency and all quantitative preparation contexts. Every quote is checked against the captured raw response or parsed primary text. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:131361, canonical label disodium selenite pentahydrate, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:15377, canonical label water, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:15956, canonical label biotin, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi17439 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:17439, canonical label cyanocob(III)alamin, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:17883, canonical label hydrogen chloride, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi17992 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17992; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:17992, canonical label sucrose, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:31206, canonical label ammonium chloride, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:32139, canonical label sodium hydrogencarbonate, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:32145, canonical label sodium hydroxide, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:33118, canonical label boric acid, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:34887, canonical label nickel dichloride, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:49105, canonical label thiamine hydrochloride, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:49976, canonical label zinc dichloride, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:53503, canonical label cobalt chloride hexahydrate, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:63036, canonical label potassium dihydrogen phosphate, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:63939, canonical label sodium tungstate dihydrate, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:75213, canonical label sodium molybdate dihydrate, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:76209, canonical label sodium sulfide nonahydrate, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:86158, canonical label calcium chloride dihydrate, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:86249, canonical label iron dichloride tetrahydrate, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:86318, canonical label copper(II) chloride dihydrate, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:86345, canonical label magnesium dichloride hexahydrate, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:86368, canonical label manganese(II) chloride tetrahydrate, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; $._embedded.terms[0] | supports | Exact nonobsolete identifier CHEBI:8806, canonical label Resazurin, definitions, synonyms and structural annotations inspected; source-form correspondence assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact live preferred-term rows for all asserted secondary keys; pinned metadata in source inputs | supports | {"CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17992": [{"label": "Sucrose", "match_type": "preferred_term", "identifier": "CHEBI:17992", "preferred_term": "Sucrose", "ontology_id": "CHEBI:17992", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| importer | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _normalize_unit | context_only | Current code separates solution_id and percentage-labelled liquid stocks from the main recipe; a compound called Vitamin solution with a cross-reference attribute is not recognized by that predicate. The mL unit fallback alone does not establish a receiving-volume denominator. Current code was inspected, not executed or historically replayed. |
| migrator | scripts/migrate_solutions_from_ingredients.py; SolutionMigrator.__init__; _resolve_solution | context_only | Current global lowercase name index retains the last same-name entry and resolves by name without comparing source-specific compositions, copying the existing concentration. This is contextual mechanism evidence, not proof of the exact historical run. |
| stock-importer | scripts/import_mediadive_solutions.py; UNIT_MAP and stock concentration construction | context_only | The pinned stock writer maps mL forms to PERCENT_V_V. Current writer behavior is not source validation and was not run. |
| history | data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml; Every timestamp in target, owner and explicitly listed contextual dependencies | refutes | [{"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[0].timestamp", "value": "2026-01-26T17:53:18.319549Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[1].timestamp", "value": "2026-03-09T08:05:09.947926+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-13T06:19:11.173341Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[4].timestamp", "value": "2026-03-17T06:30:54.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[5].timestamp", "value": "2026-03-17T19:45:23.932651+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[6].timestamp", "value": "2026-05-16T09:02:58.616469+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[7].timestamp", "value": "2026-06-05T07:40:16.419330+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[8].timestamp", "value": "2026-06-10T07:46:42.697805+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[9].timestamp", "value": "2026-08-06T03:04:35.042478+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[0].timestamp", "value": "2026-01-26T17:53:18.319549Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[1].timestamp", "value": "2026-03-09T08:05:09.947926+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-13T06:19:11.173341Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[4].timestamp", "value": "2026-03-17T06:30:54.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[5].timestamp", "value": "2026-03-17T19:45:23.932651+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[6].timestamp", "value": "2026-05-16T09:02:58.616469+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[7].timestamp", "value": "2026-06-05T07:40:16.419330+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[8].timestamp", "value": "2026-06-10T07:46:42.697805+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml", "field": "curation_history[0].timestamp", "value": "2026-03-13T06:20:40.072854Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml", "field": "curation_history[1].timestamp", "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-14T21:09:46.292785", "valid_ISO_datetime": true, "timezone_aware": false, "problem": "Timezone absent; local time cannot be asserted as UTC"}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml", "field": "curation_history[3].timestamp", "value": "2026-04-04T17:50:16.857966", "valid_ISO_datetime": true, "timezone_aware": false, "problem": "Timezone absent; local time cannot be asserted as UTC"}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml", "field": "curation_history[4].timestamp", "value": "2026-05-16T09:04:08.292076+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml", "field": "curation_history[5].timestamp", "value": "2026-06-10T06:38:41.446646+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml", "field": "curation_history[6].timestamp", "value": "2026-10-07T10:04:07.640757+00:00", "valid_ISO_datetime": true, "timezone_aware": true}] |

## Limits And Additional Notes

- MediaDive declares 1002 mL for its main solution; this is a provider normalization basis, not a measured final volume. The separate sulfide preparation is not used to infer an additional liquid volume or percentage basis.
- JCM 433 is used only for SL-10, JCM 554 only for selenite-tungstate, and JCM 197 only for Trace vitamins. Their parent recipes, other stocks, biological claims and preparation are not transferred.
- The asserted stock 6241 is inspected as a contextual dependency, not a second reviewed target. Its valid accession and two supported quantities do not make it the JCM 197 vitamin stock.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- All 19 main-target/owner timestamps are timezone-aware; two of seven contextual stock timestamps are timezone-naive. Preserve those original dependency events and uncertainty; no historical timezone is invented.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T100558Z-culturemech-002198-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acetivibrio_medium (CultureMech:002198)'
started_at: '2026-10-21T09:56:46Z'
finished_at: '2026-10-21T10:05:58Z'
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
summary: The JCM 1013 identity resolves, but the record conflates basal and trace-stock
  strengths with receiving-medium concentrations and links a different vitamin mixture.
  Exact stock sources, liquid doses, chemical forms and primary/provider disagreements
  are separately documented. No record or stock was changed.
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
  - path: data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml
    sha256: 5220ad9c5dac31532b07a36cb240aeadea8f05a3d42a17a7bddc5060194244cd
    role: target
  - path: data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml
    sha256: e14d642862c12a57ca1e6c9239cb8b9147cd9e8a6bd517481116fd36f9b0af89
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    sha256: 993f6c076ae708ef824e3637f0b5a8eb9afb742877a80f5c6dc445c376efc43f
    role: context
  - path: data/normalized_yaml/solutions/mediadive_solution_index.json
    sha256: 2e43ed2391d0113480837e0756120d71a8dad8a4490010054e67bfb90c66d381
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
  - path: scripts/fetch_medium_concentration_sources.py
    sha256: 746c2828863e6ee409d88409a540ea0a8d01ffad3e38be4a4a47f47bec5bbeb5
    role: context
  - path: scripts/import_mediadive_solutions.py
    sha256: f97db7607d76c46b75d2d2428e8a425a5735e52beb3a9c28fd0af03ab5b31aa8
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
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: scripts/review_solution_concentration_evidence.py
    sha256: 40a5bb439caf0791caff746a1eac8d5069525f381c7f3b52556c26937741f65a
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
  selection: Task review 144; batch 015 item 4 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding fourteen task batches
    contain 140 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 142 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002198
targets:
- target_id: CultureMech:002198
  path: data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml
  label: acetivibrio_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002198
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch015/144/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch015/144/strict.tsv"
  target_ids:
  - CultureMech:002198
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002198
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002198
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
  - CultureMech:002198
- check_id: scoped-history-timestamps
  name: Scoped history timestamp syntax and timezone check
  required: false
  status: failed
  summary: 26 timestamp instances inspected; 2 malformed or timezone-naive instances.
    Existing provenance is preserved; no timestamps were rewritten.
  target_ids:
  - CultureMech:002198
  evidence_ids:
  - history
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T10:05:57Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:05:57Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:58:07.902961Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch015/144/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T09:58:11.068620Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch015/144/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:58:14.623515Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:58:17.342155Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: source-catalog
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch015/source-preflight-bound/144/source-catalog.json
  locator: All bound per-record source metadata, successful captures and retained
    failed attempts
  accessed_at: '2026-10-21T10:05:57Z'
  support: context_only
  summary: '[{"key": "jcm1013", "url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "status": 200, "accessed_at": "2026-10-21T09:46:51.540618Z", "sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293",
    "metadata_sha256": "ca50a0be08f4f8371d21ff505b2eccb7cf7824f78c182843be30667f696d4736",
    "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "mediadiveJ1013api",
    "url": "https://mediadive.dsmz.de/rest/medium/J1013", "status": 200, "accessed_at":
    "2026-10-21T09:46:49.455372Z", "sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757",
    "metadata_sha256": "80d979623d024af7218b06b0f73575932ed8a2ebb35651f17f918062dcecc3d5",
    "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "solution6241",
    "url": "https://mediadive.dsmz.de/rest/solution/6241", "status": 200, "accessed_at":
    "2026-10-21T09:46:49.463537Z", "sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1",
    "metadata_sha256": "5bef66b98c346817862c93534b9a1cb2dd1e19fa11d34ea4bbf25653ebd8fee4",
    "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "chebi131361",
    "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361",
    "status": 200, "accessed_at": "2026-10-21T07:33:27.980786Z", "sha256": "643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10",
    "metadata_sha256": "233e3bc6eec19f0b2d4910629113871f0f801ec9fad02cbf5d9beba9507302cf",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi131361.json",
    "content_limit": null, "error": null}, {"key": "chebi15377", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377",
    "status": 200, "accessed_at": "2026-10-21T08:17:26.097802Z", "sha256": "de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b",
    "metadata_sha256": "72dd5a7deb860db3666b4e829f29bf7024f17f0e63ff1f513dc3298b07fecb6b",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15377.json",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "error": null}, {"key": "chebi15956", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956",
    "status": 200, "accessed_at": "2026-10-21T08:42:30.425993Z", "sha256": "d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd",
    "metadata_sha256": "580492ca7f33dc5a24e7534276bba41e9c94e43c82de73c014d431170af9cf84",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15956.json",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "error": null}, {"key": "chebi17439", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439",
    "status": 200, "accessed_at": "2026-10-21T07:16:23.574834Z", "sha256": "210a9fbc1db1c75e6053f4e23d098851ad5c63f087c736061f7664d9a393dbdd",
    "metadata_sha256": "cf2048fac20fa7ff48555c580295fe7ba2f32f9e61fbfd97a4e9b2c390ced0c2",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch010-tail/098/chebi17439.json",
    "content_limit": null, "error": null}, {"key": "chebi17883", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883",
    "status": 200, "accessed_at": "2026-10-20T07:37:25.439020Z", "sha256": "1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a",
    "metadata_sha256": "5756fc4c41d9b29d189fa931f5ba8a1a091e6b3e02abbcb06ae21c5634481def",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/132/chebi17883.json",
    "content_limit": null, "error": null}, {"key": "chebi17992", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17992",
    "status": 200, "accessed_at": "2026-10-21T08:42:31.913996Z", "sha256": "509f9cbc014a0211d3a8e536a2c68048a090719ce68ee80550c8bbf532f150aa",
    "metadata_sha256": "caeb0150bec3f5c620c0d988ce0b93a50ddef9771ee2d6d64500a0b52b78bd40",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/139/chebi17992.json",
    "content_limit": "Identity/provenance and exact identifier metadata only; no operational
    formulation or culture-procedure assessment.", "error": null}, {"key": "chebi31206",
    "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206",
    "status": 200, "accessed_at": "2026-10-21T08:17:28.439407Z", "sha256": "ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76",
    "metadata_sha256": "df2a292a870613733f0555365eb5e9768259b400982522ff486094a3fa3beb4f",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi31206.json",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "error": null}, {"key": "chebi32139", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139",
    "status": 200, "accessed_at": "2026-10-21T07:16:24.226823Z", "sha256": "2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe",
    "metadata_sha256": "e22c2cf978a7ec315cf2c3110ef5b9434dbc17430f3bbb3db5efa02824fbbd1a",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/135/chebi32139.json",
    "content_limit": null, "error": null}, {"key": "chebi32145", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145",
    "status": 200, "accessed_at": "2026-10-21T07:33:28.263004Z", "sha256": "db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1",
    "metadata_sha256": "b20c9d330e1362a45042e189276604a8d16c160bd063fb27e66dad34ccc517fd",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch009-tail/087/chebi32145.json",
    "content_limit": null, "error": null}, {"key": "chebi33118", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118",
    "status": 200, "accessed_at": "2026-10-21T08:17:29.364390Z", "sha256": "f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87",
    "metadata_sha256": "18bce3130b0d0e05a5be03c9efe512ec5ff67bfbbb05b0756a980dffdc42f0f1",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi33118.json",
    "content_limit": null, "error": null}, {"key": "chebi34887", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887",
    "status": 200, "accessed_at": "2026-10-21T08:04:44.093348Z", "sha256": "f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc",
    "metadata_sha256": "c196058e819dd3ceca902ee8cde45f83b9116e94432ec3d92bf8e03de3450238",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi34887.json",
    "content_limit": null, "error": null}, {"key": "chebi49105", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105",
    "status": 200, "accessed_at": "2026-10-20T06:55:10.911379Z", "sha256": "0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4",
    "metadata_sha256": "723b9751feb8ab66f48f87ac82446583bccad1e02c682bf47891a937283af0b1",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi49105.json",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "error": null}, {"key": "chebi49976", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976",
    "status": 200, "accessed_at": "2026-10-21T08:04:44.168295Z", "sha256": "d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321",
    "metadata_sha256": "82c37b47478a7a0bdf0c84ee66521938920b2318352268bda11acf60b11c9d10",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/136/chebi49976.json",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "error": null}, {"key": "chebi53503", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503",
    "status": 200, "accessed_at": "2026-10-21T08:04:44.349630Z", "sha256": "c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d",
    "metadata_sha256": "1da3e479c9ca2e858e4d07f89b48b11326e3bfdff9418cc9f9520f85ae1901c5",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/136/chebi53503.json",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "error": null}, {"key": "chebi63036", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036",
    "status": 200, "accessed_at": "2026-10-21T08:17:29.666916Z", "sha256": "48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3",
    "metadata_sha256": "1ef7480d2ea5bdb5518ad6d5f9a94584384ec48f560ea50a588b29ed366261d4",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/139/chebi63036.json",
    "content_limit": "Identity/provenance and exact identifier metadata only; no operational
    formulation or culture-procedure assessment.", "error": null}, {"key": "chebi63939",
    "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939",
    "status": 200, "accessed_at": "2026-10-20T06:55:09.796192Z", "sha256": "987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a",
    "metadata_sha256": "1d2cb0b600169daf3922336c8c36707c01ef86d4e6ae6779343c137c93723dc1",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi63939.json",
    "content_limit": null, "error": null}, {"key": "chebi75213", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213",
    "status": 200, "accessed_at": "2026-10-21T08:17:29.756647Z", "sha256": "b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083",
    "metadata_sha256": "1dfd34dea2370cb22006a48279806974a7f52be9b6e115656a108ec2d42554eb",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/136/chebi75213.json",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "error": null}, {"key": "chebi76209", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209",
    "status": 200, "accessed_at": "2026-10-20T06:55:04.847843Z", "sha256": "f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c",
    "metadata_sha256": "a27755ce099dd73bdfec1edb24c56a0af540fdeae1c989965ee30e8efb4a0495",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi76209.json",
    "content_limit": null, "error": null}, {"key": "chebi86158", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158",
    "status": 200, "accessed_at": "2026-10-21T08:17:30.011607Z", "sha256": "b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61",
    "metadata_sha256": "43dd1a06fa3c2b5a0bf314b7e7c0fb221d2fb1c6a40bac37548659587cb8a131",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi86158.json",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "error": null}, {"key": "chebi86249", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249",
    "status": 200, "accessed_at": "2026-10-21T09:46:51.536553Z", "sha256": "63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683",
    "metadata_sha256": "f241b487470e01e594cf7c82f32a80202526c2c30d9503d7bd5cef7d3228990c",
    "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "chebi86318",
    "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318",
    "status": 200, "accessed_at": "2026-10-21T08:43:12.592415Z", "sha256": "9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae",
    "metadata_sha256": "601d2aa4c49a0c817e8843451d1b7bf043620ea3fd35c5bbfffac4adad3fcb1e",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi86318.json",
    "content_limit": null, "error": null}, {"key": "chebi86345", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345",
    "status": 200, "accessed_at": "2026-10-21T08:17:30.382026Z", "sha256": "08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133",
    "metadata_sha256": "73c55da23f961dac1480e9586e97c0ab02edcf1bb2a09aca9fc1096e629804c5",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi86345.json",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "error": null}, {"key": "chebi86368", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368",
    "status": 200, "accessed_at": "2026-10-21T08:17:30.657545Z", "sha256": "286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f",
    "metadata_sha256": "b61427450f992c84099cd291eba6f029aa247d3cef76a6657daa9ac91003aba4",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/136/chebi86368.json",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "error": null}, {"key": "chebi8806", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806",
    "status": 200, "accessed_at": "2026-10-21T08:17:30.774007Z", "sha256": "e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5",
    "metadata_sha256": "702243aa23112f8cb9b894281c15988bbea59c02a49404b25ad9ead450f72e95",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi8806.json",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "error": null}, {"key": "jcm433", "url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433",
    "status": 200, "accessed_at": "2026-10-21T09:49:11.794269Z", "sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b",
    "metadata_sha256": "47dc533bf0ec6f6b006880c70306c4a38b24cb278056c5a755a3c818420f5f81",
    "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "jcm554",
    "url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=554", "status": 200,
    "accessed_at": "2026-10-21T09:49:11.794199Z", "sha256": "f37922162077d3f497dd07baa484a66a223e3225eadd1dee22fad2aebf794694",
    "metadata_sha256": "0ba24d6b872c396d9daa2ba3a2b6f6c2080355fe202709d21f4041f8db40ddf0",
    "reused_capture_from": null, "content_limit": null, "error": null}, {"key": "jcm197",
    "url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "status": 200,
    "accessed_at": "2026-10-20T06:58:05.867253Z", "sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
    "metadata_sha256": "251b36cd6d2c9001683a3035facf9937641aa017f71cfec38be523a5bbd0c4d1",
    "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/jcm197.json",
    "content_limit": "Trace vitamins subsection only; unrelated parent basal medium
    excluded.", "error": null}, {"key": "mediadiveJ197api", "url": "https://mediadive.dsmz.de/rest/medium/J197",
    "status": 200, "accessed_at": "2026-10-21T09:49:11.793511Z", "sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb",
    "metadata_sha256": "d63c2e386ea604ce8d011033bda0c36c3b4c2b34e9b915d9721ed4d3aba21702",
    "reused_capture_from": null, "content_limit": null, "error": null}]'
  snapshot_sha256: c7b80f1a3f5eb644a376d8f3f0082dfe4952269036f57b961947d4707613de6c
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T10:05:57Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml:1:id:
    CultureMech:002198

    ./data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml:1:id: CultureMech:002198

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: linked-stock
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
  locator: Entire exact asserted solution 6241 YAML, including composition, preparation
    notes, evidence and history
  accessed_at: '2026-10-21T10:05:57Z'
  support: context_only
  summary: The asserted ID resolves to this local stock. Its source and composition
    are compared with the cited JCM 197 stock; file existence does not establish equivalence.
- evidence_id: jcm1013
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013
  locator: Complete primary recipe, basal subsection, default-cycle line and preparation
    paragraph
  accessed_at: '2026-10-21T09:46:51.540618Z'
  support: supports
  summary: Complete primary recipe, basal subsection, default-cycle line and preparation
    paragraph inspected with stock and receiving-medium boundaries retained.
  snapshot_sha256: b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293
- evidence_id: mediadiveJ1013api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1013
  locator: Exact medium J1013 and all four solution objects
  accessed_at: '2026-10-21T09:46:49.455372Z'
  support: supports
  summary: Exact medium J1013 and all four solution objects inspected with stock and
    receiving-medium boundaries retained.
  snapshot_sha256: 21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757
- evidence_id: jcm433
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433
  locator: Trace element solution SL-10 subsection only
  accessed_at: '2026-10-21T09:49:11.794269Z'
  support: supports
  summary: Trace element solution SL-10 subsection only inspected with stock and receiving-medium
    boundaries retained.
  snapshot_sha256: bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b
- evidence_id: jcm554
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=554
  locator: Selenite-tungstate solution subsection only
  accessed_at: '2026-10-21T09:49:11.794199Z'
  support: supports
  summary: Selenite-tungstate solution subsection only inspected with stock and receiving-medium
    boundaries retained.
  snapshot_sha256: f37922162077d3f497dd07baa484a66a223e3225eadd1dee22fad2aebf794694
- evidence_id: jcm197
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: Trace vitamins subsection only
  accessed_at: '2026-10-20T06:58:05.867253Z'
  support: supports
  summary: Trace vitamins subsection only inspected with stock and receiving-medium
    boundaries retained.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: mediadiveJ197api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J197
  locator: Exact J197 metadata and solution 3861 Trace vitamins only
  accessed_at: '2026-10-21T09:49:11.793511Z'
  support: supports
  summary: Exact J197 metadata and solution 3861 Trace vitamins only inspected with
    stock and receiving-medium boundaries retained.
  snapshot_sha256: 779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb
- evidence_id: solution6241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6241
  locator: Exact solution 6241 metadata, all four rows and make-up-volume instruction
  accessed_at: '2026-10-21T09:46:49.463537Z'
  support: supports
  summary: Exact solution 6241 metadata, all four rows and make-up-volume instruction
    inspected with stock and receiving-medium boundaries retained.
  snapshot_sha256: d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch015/144/quantity-inventory.json
  locator: All 49 source-linked decisions, including original units, stages and separate
    arithmetic
  accessed_at: '2026-10-21T10:05:57Z'
  support: context_only
  summary: Covers every target ingredient/stock amount, every cited stock row, the
    exact contextual dependency and all quantitative preparation contexts. Every quote
    is checked against the captured raw response or parsed primary text.
  snapshot_sha256: f7805d7b6565c98602003b21d0eaec6bc44768b1a84932ed4b76b4d76b72b6fc
- evidence_id: chebi131361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T07:33:27.980786Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:131361, canonical label disodium selenite
    pentahydrate, definitions, synonyms and structural annotations inspected; source-form
    correspondence assessed separately.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:15377, canonical label water, definitions,
    synonyms and structural annotations inspected; source-form correspondence assessed
    separately.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:15956, canonical label biotin, definitions,
    synonyms and structural annotations inspected; source-form correspondence assessed
    separately.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi17439
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T07:16:23.574834Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:17439, canonical label cyanocob(III)alamin,
    definitions, synonyms and structural annotations inspected; source-form correspondence
    assessed separately.
  snapshot_sha256: 210a9fbc1db1c75e6053f4e23d098851ad5c63f087c736061f7664d9a393dbdd
- evidence_id: chebi17883
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T07:37:25.439020Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:17883, canonical label hydrogen chloride,
    definitions, synonyms and structural annotations inspected; source-form correspondence
    assessed separately.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: chebi17992
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17992
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:42:31.913996Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:17992, canonical label sucrose, definitions,
    synonyms and structural annotations inspected; source-form correspondence assessed
    separately.
  snapshot_sha256: 509f9cbc014a0211d3a8e536a2c68048a090719ce68ee80550c8bbf532f150aa
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:31206, canonical label ammonium chloride,
    definitions, synonyms and structural annotations inspected; source-form correspondence
    assessed separately.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:32139, canonical label sodium hydrogencarbonate,
    definitions, synonyms and structural annotations inspected; source-form correspondence
    assessed separately.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32145
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T07:33:28.263004Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:32145, canonical label sodium hydroxide,
    definitions, synonyms and structural annotations inspected; source-form correspondence
    assessed separately.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:33118, canonical label boric acid, definitions,
    synonyms and structural annotations inspected; source-form correspondence assessed
    separately.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:34887, canonical label nickel dichloride,
    definitions, synonyms and structural annotations inspected; source-form correspondence
    assessed separately.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:49105, canonical label thiamine hydrochloride,
    definitions, synonyms and structural annotations inspected; source-form correspondence
    assessed separately.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:49976, canonical label zinc dichloride,
    definitions, synonyms and structural annotations inspected; source-form correspondence
    assessed separately.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:53503, canonical label cobalt chloride
    hexahydrate, definitions, synonyms and structural annotations inspected; source-form
    correspondence assessed separately.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:63036, canonical label potassium dihydrogen
    phosphate, definitions, synonyms and structural annotations inspected; source-form
    correspondence assessed separately.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:63939, canonical label sodium tungstate
    dihydrate, definitions, synonyms and structural annotations inspected; source-form
    correspondence assessed separately.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:75213, canonical label sodium molybdate
    dihydrate, definitions, synonyms and structural annotations inspected; source-form
    correspondence assessed separately.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:76209, canonical label sodium sulfide
    nonahydrate, definitions, synonyms and structural annotations inspected; source-form
    correspondence assessed separately.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:86158, canonical label calcium chloride
    dihydrate, definitions, synonyms and structural annotations inspected; source-form
    correspondence assessed separately.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T09:46:51.536553Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:86249, canonical label iron dichloride
    tetrahydrate, definitions, synonyms and structural annotations inspected; source-form
    correspondence assessed separately.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:86318, canonical label copper(II) chloride
    dihydrate, definitions, synonyms and structural annotations inspected; source-form
    correspondence assessed separately.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:86345, canonical label magnesium dichloride
    hexahydrate, definitions, synonyms and structural annotations inspected; source-form
    correspondence assessed separately.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:86368, canonical label manganese(II)
    chloride tetrahydrate, definitions, synonyms and structural annotations inspected;
    source-form correspondence assessed separately.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: Exact nonobsolete identifier CHEBI:8806, canonical label Resazurin, definitions,
    synonyms and structural annotations inspected; source-form correspondence assessed
    separately.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact live preferred-term rows for all asserted secondary keys; pinned
    metadata in source inputs
  accessed_at: '2026-10-21T10:05:57Z'
  support: supports
  summary: '{"CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier":
    "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17992": [{"label": "Sucrose", "match_type":
    "preferred_term", "identifier": "CHEBI:17992", "preferred_term": "Sucrose", "ontology_id":
    "CHEBI:17992", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209":
    [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type":
    "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride",
    "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term",
    "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17883": [{"label":
    "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term":
    "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id":
    "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976":
    [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976",
    "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O",
    "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier":
    "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride
    hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term":
    "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term":
    "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label":
    "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type":
    "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id":
    "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term":
    "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _normalize_unit
  accessed_at: '2026-10-21T10:05:57Z'
  support: context_only
  summary: Current code separates solution_id and percentage-labelled liquid stocks
    from the main recipe; a compound called Vitamin solution with a cross-reference
    attribute is not recognized by that predicate. The mL unit fallback alone does
    not establish a receiving-volume denominator. Current code was inspected, not
    executed or historically replayed.
- evidence_id: migrator
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: SolutionMigrator.__init__; _resolve_solution
  accessed_at: '2026-10-21T10:05:57Z'
  support: context_only
  summary: Current global lowercase name index retains the last same-name entry and
    resolves by name without comparing source-specific compositions, copying the existing
    concentration. This is contextual mechanism evidence, not proof of the exact historical
    run.
- evidence_id: stock-importer
  kind: record_content
  reference: scripts/import_mediadive_solutions.py
  locator: UNIT_MAP and stock concentration construction
  accessed_at: '2026-10-21T10:05:57Z'
  support: context_only
  summary: The pinned stock writer maps mL forms to PERCENT_V_V. Current writer behavior
    is not source validation and was not run.
- evidence_id: history
  kind: record_content
  reference: data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml
  locator: Every timestamp in target, owner and explicitly listed contextual dependencies
  accessed_at: '2026-10-21T10:05:57Z'
  support: refutes
  summary: '[{"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[0].timestamp",
    "value": "2026-01-26T17:53:18.319549Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[1].timestamp",
    "value": "2026-03-09T08:05:09.947926+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[2].timestamp",
    "value": "2026-03-13T06:19:11.173341Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[3].timestamp",
    "value": "2026-03-14T00:00:00+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[4].timestamp",
    "value": "2026-03-17T06:30:54.000000Z", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[5].timestamp",
    "value": "2026-03-17T19:45:23.932651+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[6].timestamp",
    "value": "2026-05-16T09:02:58.616469+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[7].timestamp",
    "value": "2026-06-05T07:40:16.419330+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[8].timestamp",
    "value": "2026-06-10T07:46:42.697805+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml", "field": "curation_history[9].timestamp",
    "value": "2026-08-06T03:04:35.042478+00:00", "valid_ISO_datetime": true, "timezone_aware":
    true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml",
    "field": "curation_history[0].timestamp", "value": "2026-01-26T17:53:18.319549Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml",
    "field": "curation_history[1].timestamp", "value": "2026-03-09T08:05:09.947926+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml",
    "field": "curation_history[2].timestamp", "value": "2026-03-13T06:19:11.173341Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml",
    "field": "curation_history[3].timestamp", "value": "2026-03-14T00:00:00+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml",
    "field": "curation_history[4].timestamp", "value": "2026-03-17T06:30:54.000000Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml",
    "field": "curation_history[5].timestamp", "value": "2026-03-17T19:45:23.932651+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml",
    "field": "curation_history[6].timestamp", "value": "2026-05-16T09:02:58.616469+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml",
    "field": "curation_history[7].timestamp", "value": "2026-06-05T07:40:16.419330+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml",
    "field": "curation_history[8].timestamp", "value": "2026-06-10T07:46:42.697805+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
    "field": "curation_history[0].timestamp", "value": "2026-03-13T06:20:40.072854Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
    "field": "curation_history[1].timestamp", "value": "2026-03-14T00:00:00+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
    "field": "curation_history[2].timestamp", "value": "2026-03-14T21:09:46.292785",
    "valid_ISO_datetime": true, "timezone_aware": false, "problem": "Timezone absent;
    local time cannot be asserted as UTC"}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
    "field": "curation_history[3].timestamp", "value": "2026-04-04T17:50:16.857966",
    "valid_ISO_datetime": true, "timezone_aware": false, "problem": "Timezone absent;
    local time cannot be asserted as UTC"}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
    "field": "curation_history[4].timestamp", "value": "2026-05-16T09:04:08.292076+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
    "field": "curation_history[5].timestamp", "value": "2026-06-10T06:38:41.446646+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
    "field": "curation_history[6].timestamp", "value": "2026-10-07T10:04:07.640757+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002198
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact accession, owner and asserted dependency
  outcome: supported
  summary: JCM 1013, MediaDive J1013 and the complete normalized owner agree on the
    medium identity. The owner and target differ only by merge metadata/history. Stock
    6241 resolves to CultureMech:014933; source-specific equivalence is separately
    refuted below.
  target_ids:
  - CultureMech:002198
  evidence_ids:
  - record
  - owner-0
  - linked-stock
  - id-search
  - jcm1013
  - mediadiveJ1013api
  - solution6241
- assessment_id: quantities
  area: quantity
  topic: Every direct concentration and separate stock stage
  outcome: concern
  summary: The 49 decisions distinguish eight main additions, six basal rows, ten
    SL-10 rows, four selenite-tungstate rows, eleven vitamin rows, four dependency
    rows and six preparation/volume contexts. Main percentage-stock doses were mislabeled
    as mass, 17 stock constituents were flattened, and the vitamin dose is dimensionally
    wrong. Two direct provider mass rates are supported on its declared volume basis.
  target_ids:
  - CultureMech:002198
  evidence_ids:
  - record
  - owner-0
  - jcm1013
  - mediadiveJ1013api
  - jcm433
  - jcm554
  - jcm197
  - mediadiveJ197api
  - solution6241
  - quantity-inventory
  details: '[{"field_path": "solutions (missing source stock descriptor)", "name":
    "Basal medium", "decision": "add", "stage": "Main recipe stock addition", "stored":
    null, "explanation": "Preserve the source volume dose and its referenced stock
    definition separately. Constituent stock strengths are currently flattened into
    direct ingredient concentrations; do not treat the listed mL dose as g/L.", "source_snippets":
    [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "source_quote": "Basal medium (see below) 950.0 ml", "source_locator": "JCM 1013
    main table row 1", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\":
    \"Basal medium\",\n                        \"solution_id\": 5056,\n                        \"amount\":
    950,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[0].recipe[0]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]},
    {"field_path": "solutions (missing source stock descriptor)", "name": "Trace element
    solution SL-10", "decision": "add", "stage": "Main recipe stock addition", "stored":
    null, "explanation": "Preserve the source volume dose and its referenced stock
    definition separately. Constituent stock strengths are currently flattened into
    direct ingredient concentrations; do not treat the listed mL dose as g/L.", "source_snippets":
    [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "source_quote": "Trace element solution SL-10 (see Medium No. 433 ) 1.0 ml", "source_locator":
    "JCM 1013 main table row 2", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\":
    \"Trace element solution SL-10\",\n                        \"solution_id\": 4178,\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[0].recipe[1]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]},
    {"field_path": "solutions (missing source stock descriptor)", "name": "Selenite-tungstate
    solution", "decision": "add", "stage": "Main recipe stock addition", "stored":
    null, "explanation": "Preserve the source volume dose and its referenced stock
    definition separately. Constituent stock strengths are currently flattened into
    direct ingredient concentrations; do not treat the listed mL dose as g/L.", "source_snippets":
    [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "source_quote": "Selenite-tungstate solution(see Medium No. 554 ) 1.0 ml", "source_locator":
    "JCM 1013 main table row 3", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\":
    \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[0].recipe[2]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]},
    {"field_path": "solutions[0]", "name": "Vitamin solution", "decision": "correct",
    "stage": "Main recipe vitamin stock addition", "stored": {"preferred_term": "Vitamin
    solution", "term": {"id": "mediadive.solution:6241", "label": "Vitamin solution"},
    "concentration": {"value": "10", "unit": "G_PER_L"}, "notes": "See mediadive_6241_Vitamin_solution.yaml
    for composition", "name": "Unknown solution"}, "explanation": "The source specifies
    10 mL of the JCM 197 Trace vitamins stock. Local 10 G_PER_L is dimensionally wrong,
    and asserted 6241 is a different three-vitamin mixture. Resolve exact stock identity
    before any dilution calculation.", "source_snippets": [{"source_key": "jcm1013",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "source_quote": "Vitamin solution (see Medium No. 197 ) 10.0 ml", "source_locator":
    "JCM 1013 main table row 4", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Vitamin solution\",\n                        \"compound_id\": 154,\n                        \"attribute\":
    \"see Medium No. 197\",\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[3]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]},
    {"field_path": "ingredients[0].concentration", "name": "NaHCO3", "decision": "correct",
    "stage": "Main recipe percentage-stock addition", "stored": {"value": "30", "unit":
    "G_PER_L"}, "explanation": "The literal source is a volume of an explicitly w/v
    stock, not a neat-compound mass concentration. Preserve stock strength and addition
    volume. Derived batch mass is separate from any final concentration.", "source_snippets":
    [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "source_quote": "NaHCO 3 (5%, w/v) 30.0 ml", "source_locator": "JCM 1013 main
    table row 5", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"attribute\":
    \"5%, w/v\",\n                        \"amount\": 30,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[4]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"calculation": "5 g/100 mL × 30 mL = 1.5 g per listed batch", "batch_mass_g":
    "1.5", "receiving_final_volume": "not measured by this source; provider separately
    declares 1002 mL"}}, {"field_path": "ingredients[1].concentration", "name": "Sucrose",
    "decision": "correct", "stage": "Main recipe percentage-stock addition", "stored":
    {"value": "10", "unit": "G_PER_L"}, "explanation": "The literal source is a volume
    of an explicitly w/v stock, not a neat-compound mass concentration. Preserve stock
    strength and addition volume. Derived batch mass is separate from any final concentration.",
    "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "source_quote": "Sucrose (20%, w/v) 10.0 ml", "source_locator": "JCM 1013 main
    table row 6", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Sucrose\",\n                        \"compound_id\": 108,\n                        \"attribute\":
    \"20%, w/v\",\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[5]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"calculation": "20 g/100 mL × 10 mL = 2 g per listed batch", "batch_mass_g":
    "2", "receiving_final_volume": "not measured by this source; provider separately
    declares 1002 mL"}}, {"field_path": "ingredients[2].concentration", "name": "Yeast
    extract", "decision": "evidence_only", "stage": "Main recipe direct mass addition",
    "stored": {"value": "0.0499002", "unit": "G_PER_L"}, "explanation": "The stored
    value agrees with provider g_l and its declared 1002 mL normalization. Add narrow
    source evidence; do not call this an independently measured final-medium concentration.",
    "source_snippets": [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "source_quote": "Yeast extract 50.0 mg", "source_locator": "JCM 1013 main table
    row 7", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.0499002,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[6]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"calculation": "50 mg × 0.001 g/mg / 1.002 L = 0.04990019960079840319361277445
    g/L", "basis": "provider-declared volume only", "reported_g_per_l": 0.0499002}},
    {"field_path": "ingredients[3].concentration", "name": "Na2S x 9 H2O", "decision":
    "evidence_only", "stage": "Main recipe direct mass addition", "stored": {"value":
    "0.249501", "unit": "G_PER_L"}, "explanation": "The stored value agrees with provider
    g_l and its declared 1002 mL normalization. Add narrow source evidence; do not
    call this an independently measured final-medium concentration.", "source_snippets":
    [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "source_quote": "Na 2 S·9H 2 O 0.25 g", "source_locator": "JCM 1013 main table
    row 8", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\":
    0.25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.249501,\n                        \"mmol_l\": 1.0388,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[0].recipe[7]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"calculation": "0.25 g × 1 g/g / 1.002 L = 0.2495009980039920159680638723
    g/L", "basis": "provider-declared volume only", "reported_g_per_l": 0.249501}},
    {"field_path": "ingredients[4].concentration", "name": "KH2PO4", "decision": "correct",
    "stage": "Basal medium", "stored": {"value": "1.47368", "unit": "G_PER_L"}, "explanation":
    "The stored g/L value is the provider stock-strength value, incorrectly placed
    as a direct receiving-medium ingredient. Preserve the original stock batch and
    its separately documented dose before any final-medium arithmetic.", "source_snippets":
    [{"source_key": "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "source_quote": "KH 2 PO 4 1.4 g", "source_locator": "Basal medium subsection,
    literal row 1", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\":
    1.4,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.47368,\n                        \"mmol_l\": 10.8291,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[0]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 950, "provider_stock_g_l": 1.47368,
    "receiving_dose_ml": 950, "receiving_basis": "provider main solution declares
    1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[5].concentration",
    "name": "NH4Cl", "decision": "correct", "stage": "Basal medium", "stored": {"value":
    "0.526316", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider
    stock-strength value, incorrectly placed as a direct receiving-medium ingredient.
    Preserve the original stock batch and its separately documented dose before any
    final-medium arithmetic.", "source_snippets": [{"source_key": "jcm1013", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "NH
    4 Cl 0.5 g", "source_locator": "Basal medium subsection, literal row 2", "source_sha256":
    "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}, {"source_key":
    "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.526316,\n                        \"mmol_l\": 9.83952,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[1]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 950, "provider_stock_g_l": 0.526316,
    "receiving_dose_ml": 950, "receiving_basis": "provider main solution declares
    1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[6].concentration",
    "name": "MgCl2 x 6 H2O", "decision": "correct", "stage": "Basal medium", "stored":
    {"value": "0.210526", "unit": "G_PER_L"}, "explanation": "The stored g/L value
    is the provider stock-strength value, incorrectly placed as a direct receiving-medium
    ingredient. Preserve the original stock batch and its separately documented dose
    before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm1013",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "source_quote": "MgCl 2 ·6H 2 O 0.2 g", "source_locator": "Basal medium subsection,
    literal row 3", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\":
    0.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.210526,\n                        \"mmol_l\": 1.03553,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[2]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 950, "provider_stock_g_l": 0.210526,
    "receiving_dose_ml": 950, "receiving_basis": "provider main solution declares
    1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[7].concentration",
    "name": "CaCl2 x 2 H2O", "decision": "correct", "stage": "Basal medium", "stored":
    {"value": "0.157895", "unit": "G_PER_L"}, "explanation": "The stored g/L value
    is the provider stock-strength value, incorrectly placed as a direct receiving-medium
    ingredient. Preserve the original stock batch and its separately documented dose
    before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm1013",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "source_quote": "CaCl 2 ·2H 2 O 0.15 g", "source_locator": "Basal medium subsection,
    literal row 4", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\":
    0.15,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.157895,\n                        \"mmol_l\": 1.074,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[3]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 950, "provider_stock_g_l": 0.157895,
    "receiving_dose_ml": 950, "receiving_basis": "provider main solution declares
    1002 mL; no measured final volume asserted"}}, {"field_path": "ingredients[8].concentration",
    "name": "Resazurin", "decision": "correct", "stage": "Basal medium", "stored":
    {"value": "0.00105263", "unit": "G_PER_L"}, "explanation": "The stored g/L value
    is the provider stock-strength value, incorrectly placed as a direct receiving-medium
    ingredient. Preserve the original stock batch and its separately documented dose
    before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm1013",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "source_quote": "Resazurin 1.0 mg", "source_locator": "Basal medium subsection,
    literal row 5", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\":
    1,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.00105263,\n                        \"mmol_l\": 0.00459283,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[4]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 950, "provider_stock_g_l": 0.00105263,
    "receiving_dose_ml": 950, "receiving_basis": "provider main solution declares
    1002 mL; no measured final volume asserted"}}, {"field_path": "stock preparation
    solvent context", "name": "Distilled water", "decision": "add", "stage": "Basal
    medium", "stored": null, "explanation": "Preserve this solvent amount within its
    own source stock batch; never add separate stock water amounts into a final-medium
    water mass or infer measured final volume.", "source_snippets": [{"source_key":
    "jcm1013", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "source_quote": "Distilled water 950.0 ml", "source_locator": "Basal medium subsection,
    literal row 6", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    950,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[5]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]},
    {"field_path": "ingredients[9].concentration", "name": "HCl", "decision": "conflict",
    "stage": "Trace element solution SL-10", "stored": {"value": "2.5", "unit": "G_PER_L"},
    "explanation": "The stored g/L value is the provider stock-strength value, incorrectly
    placed as a direct receiving-medium ingredient. Preserve the original stock batch
    and its separately documented dose before any final-medium arithmetic. The source
    HCl strength 7.7 M implies a different mass from provider 2.5 g/L on the provider
    one-liter stock basis. The source bare 25% does not specify w/v or justify overriding
    its explicit molarity.", "source_snippets": [{"source_key": "jcm433", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_quote": "HCl
    (25%, 7.7 M) 10.0 ml", "source_locator": "Trace element solution SL-10 subsection,
    literal row 1", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\":
    \"25%, 7.7 M\",\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\":
    68.5683,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[0]", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 2.5, "receiving_dose_ml":
    1, "receiving_basis": "provider main solution declares 1002 mL; no measured final
    volume asserted", "conditional_stock_mass_g": "2.8074970", "calculation": "7.7
    mol/L × 0.010 L × 36.461 g/mol = 2.807497 g; dividing by the provider-declared
    1 L stock gives 2.807497 g/L, versus reported 2.5 g/L"}}, {"field_path": "ingredients[10].concentration",
    "name": "FeCl2 x 4 H2O", "decision": "correct", "stage": "Trace element solution
    SL-10", "stored": {"value": "1.5", "unit": "G_PER_L"}, "explanation": "The stored
    g/L value is the provider stock-strength value, incorrectly placed as a direct
    receiving-medium ingredient. Preserve the original stock batch and its separately
    documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key":
    "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433",
    "source_quote": "FeCl 2 ·4H 2 O 1.5 g", "source_locator": "Trace element solution
    SL-10 subsection, literal row 2", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\":
    1.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[2].recipe[1]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 1.5, "receiving_dose_ml":
    1, "receiving_basis": "provider main solution declares 1002 mL; no measured final
    volume asserted"}}, {"field_path": "ingredients[11].concentration", "name": "ZnCl2",
    "decision": "correct", "stage": "Trace element solution SL-10", "stored": {"value":
    "0.07", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider
    stock-strength value, incorrectly placed as a direct receiving-medium ingredient.
    Preserve the original stock batch and its separately documented dose before any
    final-medium arithmetic.", "source_snippets": [{"source_key": "jcm433", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_quote": "ZnCl
    2 70.0 mg", "source_locator": "Trace element solution SL-10 subsection, literal
    row 3", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\":
    70,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[2].recipe[2]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.07, "receiving_dose_ml":
    1, "receiving_basis": "provider main solution declares 1002 mL; no measured final
    volume asserted"}}, {"field_path": "ingredients[12].concentration", "name": "MnCl2
    x 4 H2O", "decision": "correct", "stage": "Trace element solution SL-10", "stored":
    {"value": "0.1", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the
    provider stock-strength value, incorrectly placed as a direct receiving-medium
    ingredient. Preserve the original stock batch and its separately documented dose
    before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm433",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433",
    "source_quote": "MnCl 2 ·4H 2 O 100.0 mg", "source_locator": "Trace element solution
    SL-10 subsection, literal row 4", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\":
    100,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[2].recipe[3]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.1, "receiving_dose_ml":
    1, "receiving_basis": "provider main solution declares 1002 mL; no measured final
    volume asserted"}}, {"field_path": "ingredients[13].concentration", "name": "H3BO3",
    "decision": "correct", "stage": "Trace element solution SL-10", "stored": {"value":
    "0.006", "unit": "G_PER_L"}, "explanation": "The stored g/L value is the provider
    stock-strength value, incorrectly placed as a direct receiving-medium ingredient.
    Preserve the original stock batch and its separately documented dose before any
    final-medium arithmetic.", "source_snippets": [{"source_key": "jcm433", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_quote": "H 3
    BO 3 6.0 mg", "source_locator": "Trace element solution SL-10 subsection, literal
    row 5", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\":
    6,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[2].recipe[4]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.006,
    "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002
    mL; no measured final volume asserted"}}, {"field_path": "ingredients[14].concentration",
    "name": "CoCl2 x 6 H2O", "decision": "correct", "stage": "Trace element solution
    SL-10", "stored": {"value": "0.19", "unit": "G_PER_L"}, "explanation": "The stored
    g/L value is the provider stock-strength value, incorrectly placed as a direct
    receiving-medium ingredient. Preserve the original stock batch and its separately
    documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key":
    "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433",
    "source_quote": "CoCl 2 ·6H 2 O 190.0 mg", "source_locator": "Trace element solution
    SL-10 subsection, literal row 6", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\":
    190,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[2].recipe[5]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.19, "receiving_dose_ml":
    1, "receiving_basis": "provider main solution declares 1002 mL; no measured final
    volume asserted"}}, {"field_path": "ingredients[15].concentration", "name": "CuCl2
    x 2 H2O", "decision": "correct", "stage": "Trace element solution SL-10", "stored":
    {"value": "0.002", "unit": "G_PER_L"}, "explanation": "The stored g/L value is
    the provider stock-strength value, incorrectly placed as a direct receiving-medium
    ingredient. Preserve the original stock batch and its separately documented dose
    before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm433",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433",
    "source_quote": "CuCl 2 ·2H 2 O 2.0 mg", "source_locator": "Trace element solution
    SL-10 subsection, literal row 7", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[2].recipe[6]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.002,
    "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002
    mL; no measured final volume asserted"}}, {"field_path": "ingredients[16].concentration",
    "name": "NiCl2 x 6 H2O", "decision": "correct", "stage": "Trace element solution
    SL-10", "stored": {"value": "0.024", "unit": "G_PER_L"}, "explanation": "The stored
    g/L value is the provider stock-strength value, incorrectly placed as a direct
    receiving-medium ingredient. Preserve the original stock batch and its separately
    documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key":
    "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433",
    "source_quote": "NiCl 2 ·6H 2 O 24.0 mg", "source_locator": "Trace element solution
    SL-10 subsection, literal row 8", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\":
    24,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[2].recipe[7]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.024,
    "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002
    mL; no measured final volume asserted"}}, {"field_path": "ingredients[17].concentration",
    "name": "Na2MoO4 x 2 H2O", "decision": "correct", "stage": "Trace element solution
    SL-10", "stored": {"value": "0.036", "unit": "G_PER_L"}, "explanation": "The stored
    g/L value is the provider stock-strength value, incorrectly placed as a direct
    receiving-medium ingredient. Preserve the original stock batch and its separately
    documented dose before any final-medium arithmetic.", "source_snippets": [{"source_key":
    "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433",
    "source_quote": "Na 2 MoO 4 ·2H 2 O 36.0 mg", "source_locator": "Trace element
    solution SL-10 subsection, literal row 9", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    36,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[2].recipe[8]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.036,
    "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002
    mL; no measured final volume asserted"}}, {"field_path": "stock preparation solvent
    context", "name": "Distilled water", "decision": "add", "stage": "Trace element
    solution SL-10", "stored": null, "explanation": "Preserve this solvent amount
    within its own source stock batch; never add separate stock water amounts into
    a final-medium water mass or infer measured final volume.", "source_snippets":
    [{"source_key": "jcm433", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433",
    "source_quote": "Distilled water 990.0 ml", "source_locator": "Trace element solution
    SL-10 subsection, literal row 10", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    990,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[2].recipe[9]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]},
    {"field_path": "ingredients[18].concentration", "name": "NaOH", "decision": "correct",
    "stage": "Selenite-tungstate solution", "stored": {"value": "0.5", "unit": "G_PER_L"},
    "explanation": "The stored g/L value is the provider stock-strength value, incorrectly
    placed as a direct receiving-medium ingredient. Preserve the original stock batch
    and its separately documented dose before any final-medium arithmetic.", "source_snippets":
    [{"source_key": "jcm554", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=554",
    "source_quote": "NaOH 0.5 g", "source_locator": "Selenite-tungstate solution subsection,
    literal row 1", "source_sha256": "f37922162077d3f497dd07baa484a66a223e3225eadd1dee22fad2aebf794694"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[3].recipe[0]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.5, "receiving_dose_ml":
    1, "receiving_basis": "provider main solution declares 1002 mL; no measured final
    volume asserted"}}, {"field_path": "ingredients[19].concentration", "name": "Na2SeO3
    x 5 H2O", "decision": "correct", "stage": "Selenite-tungstate solution", "stored":
    {"value": "0.003", "unit": "G_PER_L"}, "explanation": "The stored g/L value is
    the provider stock-strength value, incorrectly placed as a direct receiving-medium
    ingredient. Preserve the original stock batch and its separately documented dose
    before any final-medium arithmetic.", "source_snippets": [{"source_key": "jcm554",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=554",
    "source_quote": "Na 2 SeO 3 ·5H 2 O 0.003 g", "source_locator": "Selenite-tungstate
    solution subsection, literal row 2", "source_sha256": "f37922162077d3f497dd07baa484a66a223e3225eadd1dee22fad2aebf794694"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\":
    3,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[3].recipe[1]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.003,
    "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002
    mL; no measured final volume asserted"}}, {"field_path": "ingredients[20].concentration",
    "name": "Na2WO4 x 2 H2O", "decision": "correct", "stage": "Selenite-tungstate
    solution", "stored": {"value": "0.004", "unit": "G_PER_L"}, "explanation": "The
    stored g/L value is the provider stock-strength value, incorrectly placed as a
    direct receiving-medium ingredient. Preserve the original stock batch and its
    separately documented dose before any final-medium arithmetic.", "source_snippets":
    [{"source_key": "jcm554", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=554",
    "source_quote": "Na 2 WO 4 ·2H 2 O 0.004 g", "source_locator": "Selenite-tungstate
    solution subsection, literal row 3", "source_sha256": "f37922162077d3f497dd07baa484a66a223e3225eadd1dee22fad2aebf794694"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\":
    4,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[3].recipe[2]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}],
    "arithmetic": {"provider_stock_volume_ml": 1000, "provider_stock_g_l": 0.004,
    "receiving_dose_ml": 1, "receiving_basis": "provider main solution declares 1002
    mL; no measured final volume asserted"}}, {"field_path": "stock preparation solvent
    context", "name": "Distilled water", "decision": "add", "stage": "Selenite-tungstate
    solution", "stored": null, "explanation": "Preserve this solvent amount within
    its own source stock batch; never add separate stock water amounts into a final-medium
    water mass or infer measured final volume.", "source_snippets": [{"source_key":
    "jcm554", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=554",
    "source_quote": "Distilled water 1.0 L", "source_locator": "Selenite-tungstate
    solution subsection, literal row 4", "source_sha256": "f37922162077d3f497dd07baa484a66a223e3225eadd1dee22fad2aebf794694"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[3].recipe[3]",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]},
    {"field_path": "solutions[0].source-specific composition", "name": "Biotin", "decision":
    "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null, "explanation":
    "Recover this exact stock constituent or solvent context, keeping its one-liter
    source batch separate from the 10 mL receiving dose. This is not evidence for
    a parent-medium ingredient, replacement ontology ID or growth claim.", "source_snippets":
    [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
    "source_quote": "Biotin 2.0 mg", "source_locator": "Trace vitamins subsection
    row 1", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"},
    {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197",
    "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.002,\n                        \"mmol_l\": 0.00818632,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[0]",
    "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]},
    {"field_path": "solutions[0].source-specific composition", "name": "Folic acid",
    "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null,
    "explanation": "Recover this exact stock constituent or solvent context, keeping
    its one-liter source batch separate from the 10 mL receiving dose. This is not
    evidence for a parent-medium ingredient, replacement ontology ID or growth claim.",
    "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
    "source_quote": "Folic acid 2.0 mg", "source_locator": "Trace vitamins subsection
    row 2", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"},
    {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197",
    "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.002,\n                        \"mmol_l\": 0.00453104,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[1]",
    "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]},
    {"field_path": "solutions[0].source-specific composition", "name": "Pyridoxine
    hydrochloride", "decision": "add", "stage": "JCM 197 Trace vitamins stock only",
    "stored": null, "explanation": "Recover this exact stock constituent or solvent
    context, keeping its one-liter source batch separate from the 10 mL receiving
    dose. This is not evidence for a parent-medium ingredient, replacement ontology
    ID or growth claim.", "source_snippets": [{"source_key": "jcm197", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197", "source_quote": "Pyridoxine·HCl
    10.0 mg", "source_locator": "Trace vitamins subsection row 3", "source_sha256":
    "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"}, {"source_key":
    "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197",
    "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\":
    10,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.0486287,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[2]",
    "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]},
    {"field_path": "solutions[0].source-specific composition", "name": "Thiamine HCl",
    "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null,
    "explanation": "Recover this exact stock constituent or solvent context, keeping
    its one-liter source batch separate from the 10 mL receiving dose. This is not
    evidence for a parent-medium ingredient, replacement ontology ID or growth claim.",
    "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
    "source_quote": "Thiamine·HCl 5.0 mg", "source_locator": "Trace vitamins subsection
    row 4", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"},
    {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197",
    "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0148236,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[3]",
    "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]},
    {"field_path": "solutions[0].source-specific composition", "name": "Riboflavin",
    "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null,
    "explanation": "Recover this exact stock constituent or solvent context, keeping
    its one-liter source batch separate from the 10 mL receiving dose. This is not
    evidence for a parent-medium ingredient, replacement ontology ID or growth claim.",
    "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
    "source_quote": "Riboflavin 5.0 mg", "source_locator": "Trace vitamins subsection
    row 5", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"},
    {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197",
    "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0132837,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[4]",
    "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]},
    {"field_path": "solutions[0].source-specific composition", "name": "Nicotinic
    acid", "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored":
    null, "explanation": "Recover this exact stock constituent or solvent context,
    keeping its one-liter source batch separate from the 10 mL receiving dose. This
    is not evidence for a parent-medium ingredient, replacement ontology ID or growth
    claim.", "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
    "source_quote": "Nicotinic acid 5.0 mg", "source_locator": "Trace vitamins subsection
    row 6", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"},
    {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197",
    "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0406141,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[5]",
    "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]},
    {"field_path": "solutions[0].source-specific composition", "name": "Calcium pantothenate",
    "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null,
    "explanation": "Recover this exact stock constituent or solvent context, keeping
    its one-liter source batch separate from the 10 mL receiving dose. This is not
    evidence for a parent-medium ingredient, replacement ontology ID or growth claim.",
    "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
    "source_quote": "Calcium pantothenate 5.0 mg", "source_locator": "Trace vitamins
    subsection row 7", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"},
    {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197",
    "source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0104925,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[6]",
    "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]},
    {"field_path": "solutions[0].source-specific composition", "name": "Vitamin B12",
    "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null,
    "explanation": "Recover this exact stock constituent or solvent context, keeping
    its one-liter source batch separate from the 10 mL receiving dose. This is not
    evidence for a parent-medium ingredient, replacement ontology ID or growth claim.",
    "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
    "source_quote": "Vitamin B 1 2 0.1 mg", "source_locator": "Trace vitamins subsection
    row 8", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"},
    {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197",
    "source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\":
    0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.0001,\n                        \"mmol_l\": 7.3779e-5,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[7]",
    "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]},
    {"field_path": "solutions[0].source-specific composition", "name": "p-Aminobenzoic
    acid", "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored":
    null, "explanation": "Recover this exact stock constituent or solvent context,
    keeping its one-liter source batch separate from the 10 mL receiving dose. This
    is not evidence for a parent-medium ingredient, replacement ontology ID or growth
    claim.", "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
    "source_quote": "p -Aminobenzoic acid 5.0 mg", "source_locator": "Trace vitamins
    subsection row 9", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"},
    {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197",
    "source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0364591,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[8]",
    "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]},
    {"field_path": "solutions[0].source-specific composition", "name": "Lipoic acid",
    "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored": null,
    "explanation": "Recover this exact stock constituent or solvent context, keeping
    its one-liter source batch separate from the 10 mL receiving dose. This is not
    evidence for a parent-medium ingredient, replacement ontology ID or growth claim.",
    "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
    "source_quote": "Lipoic acid 5.0 mg", "source_locator": "Trace vitamins subsection
    row 10", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"},
    {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197",
    "source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Lipoic acid\",\n                        \"compound_id\": 368,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.024233,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[9]",
    "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]},
    {"field_path": "solutions[0].source-specific composition", "name": "Distilled
    water", "decision": "add", "stage": "JCM 197 Trace vitamins stock only", "stored":
    null, "explanation": "Recover this exact stock constituent or solvent context,
    keeping its one-liter source batch separate from the 10 mL receiving dose. This
    is not evidence for a parent-medium ingredient, replacement ontology ID or growth
    claim.", "source_snippets": [{"source_key": "jcm197", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
    "source_quote": "Distilled water 1.0 L", "source_locator": "Trace vitamins subsection
    row 11", "source_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"},
    {"source_key": "mediadiveJ197api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J197",
    "source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[10]",
    "source_sha256": "779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb"}]},
    {"field_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml:composition[0].concentration",
    "name": "Cyanocobalamine", "decision": "verified", "stage": "Asserted wrong-stock
    dependency 6241 only", "stored": {"value": "0.1", "unit": "G_PER_L"}, "explanation":
    "The local concentration and existing literal excerpt match this 100 mL stock.
    That supports stock 6241 only, not its substitution for JCM 197.", "source_snippets":
    [{"source_key": "solution6241", "source_reference": "https://mediadive.dsmz.de/rest/solution/6241",
    "source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\":
    \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\":
    0\n            }", "source_locator": "$.data.recipe[0]", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"},
    {"source_key": "solution6241", "source_reference": "https://mediadive.dsmz.de/rest/solution/6241",
    "source_quote": "\"Make up to 100 ml with distilled water.\"", "source_locator":
    "$.data.steps[0].step", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"}]},
    {"field_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml:composition[1].concentration",
    "name": "Thiamine HCl", "decision": "verified", "stage": "Asserted wrong-stock
    dependency 6241 only", "stored": {"value": "0.1", "unit": "G_PER_L"}, "explanation":
    "The local concentration and existing literal excerpt match this 100 mL stock.
    That supports stock 6241 only, not its substitution for JCM 197.", "source_snippets":
    [{"source_key": "solution6241", "source_reference": "https://mediadive.dsmz.de/rest/solution/6241",
    "source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\":
    \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\":
    0\n            }", "source_locator": "$.data.recipe[1]", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"},
    {"source_key": "solution6241", "source_reference": "https://mediadive.dsmz.de/rest/solution/6241",
    "source_quote": "\"Make up to 100 ml with distilled water.\"", "source_locator":
    "$.data.steps[0].step", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"}]},
    {"field_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml:composition[2].concentration",
    "name": "Biotin", "decision": "correct", "stage": "Asserted wrong-stock dependency
    6241 only", "stored": {"value": "2000.0", "unit": "G_PER_L"}, "explanation": "200
    micrograms / 100 mL = 0.002 g/L on the explicit make-up-to-volume basis, whereas
    the dependency stores 2000 g/L. This dependency error is not a proposed receiving-medium
    concentration.", "source_snippets": [{"source_key": "solution6241", "source_reference":
    "https://mediadive.dsmz.de/rest/solution/6241", "source_quote": "{\n                \"recipe_order\":
    4,\n                \"compound\": \"Biotin\",\n                \"compound_id\":
    46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\":
    \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "source_locator": "$.data.recipe[2]", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"},
    {"source_key": "solution6241", "source_reference": "https://mediadive.dsmz.de/rest/solution/6241",
    "source_quote": "\"Make up to 100 ml with distilled water.\"", "source_locator":
    "$.data.steps[0].step", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"}]},
    {"field_path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml:composition[3].concentration",
    "name": "Distilled water", "decision": "correct", "stage": "Asserted wrong-stock
    dependency 6241 only", "stored": {"value": "1000.0", "unit": "PERCENT_V_V"}, "explanation":
    "The source makes the stock up to 100 mL with water; local 1000 PERCENT_V_V is
    not supported. Preserve solvent volume context, not a water concentration.", "source_snippets":
    [{"source_key": "solution6241", "source_reference": "https://mediadive.dsmz.de/rest/solution/6241",
    "source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\":
    \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }", "source_locator": "$.data.recipe[3]", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"},
    {"source_key": "solution6241", "source_reference": "https://mediadive.dsmz.de/rest/solution/6241",
    "source_quote": "\"Make up to 100 ml with distilled water.\"", "source_locator":
    "$.data.steps[0].step", "source_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"}]},
    {"field_path": "ph_value; preparation_steps[0]", "name": "Source pH range", "decision":
    "evidence_only", "stage": "JCM 1013 main preparation", "stored": null, "explanation":
    "Local 7.8 equals provider min/max and lies within the primary range; local prose
    retains the range. Preserve that range and its conditional adjustment scope instead
    of declaring 7.8 wrong or an optimum.", "source_snippets": [{"source_key": "jcm1013",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "source_quote": "Readjust pH to 7.7 - 7.9, if necessary.", "source_locator": "Default-cycle
    header or exact main preparation sentence", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}]},
    {"field_path": "preparation_steps", "name": "Default source sterilization cycle",
    "decision": "add", "stage": "JCM 1013 main preparation", "stored": null, "explanation":
    "The primary default cycle is absent from local prose. Preserve it with the explicit
    filtering and separate-autoclaving exceptions; it does not authorize autoclaving
    every stock together.", "source_snippets": [{"source_key": "jcm1013", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "Unless
    otherwise stated, sterilize media by autoclaving at 121°C for 15 min.", "source_locator":
    "Default-cycle header or exact main preparation sentence", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}]},
    {"field_path": "preparation_steps[0]", "name": "Atmosphere", "decision": "evidence_only",
    "stage": "JCM 1013 main preparation", "stored": null, "explanation": "The exact
    atmosphere is retained in local prose. This is preparation context, not evidence
    of strain-specific growth.", "source_snippets": [{"source_key": "jcm1013", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013", "source_quote": "under
    100% N 2 gas", "source_locator": "Default-cycle header or exact main preparation
    sentence", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}]},
    {"field_path": "preparation_steps[0]", "name": "Sulfide stock strength", "decision":
    "not_quantified", "stage": "JCM 1013 main preparation", "stored": null, "explanation":
    "Preserve the literal 5% solution and separate preparation context. The sentence
    does not specify percentage basis or dosing volume; do not infer a w/v conversion
    or receiving final volume from it.", "source_snippets": [{"source_key": "jcm1013",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1013",
    "source_quote": "5% Na 2 S·9H 2 O solution (autoclaved under N 2 gas)", "source_locator":
    "Default-cycle header or exact main preparation sentence", "source_sha256": "b9b385330b7f0698f8ff8df64258015a64b605a711f74ad206e0799fa411e293"}]},
    {"field_path": "preparation_steps[1]", "name": "SL-10 stock preparation", "decision":
    "correct", "stage": "JCM 433 SL-10 stock only", "stored": null, "explanation":
    "The literal sequence is retained locally but detached into the main recipe preparation
    array. Keep it scoped to the trace stock rather than interpreted as a whole-medium
    operation.", "source_snippets": [{"source_key": "jcm433", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433", "source_quote": "Dissolve
    FeCl 2 ·4H 2 O first in HCl. Then dilute in distilled water and add the remaining
    salts.", "source_locator": "SL-10 subsection paragraph immediately following its
    table", "source_sha256": "bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "\"Dissolve FeCl2 x 4H2O first in HCl. Then dilute in distilled
    water and add the remaining salts.\"", "source_locator": "$.data.solutions[2].steps[0].step",
    "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]},
    {"field_path": "source volume context", "name": "Provider volume declarations",
    "decision": "evidence_only", "stage": "Each independently declared solution volume",
    "stored": null, "explanation": "Preserve the separate volume bases: main 1002
    mL, basal 950 mL, SL-10 1000 mL and selenite-tungstate 1000 mL. They are not interchangeable
    or measured receiving volumes. No addition volume for the separate sulfide solution
    is inferred.", "source_snippets": [{"source_key": "mediadiveJ1013api", "source_reference":
    "https://mediadive.dsmz.de/rest/medium/J1013", "source_quote": "1002", "source_locator":
    "$.data.solutions[0].volume", "source_sha256": "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"},
    {"source_key": "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "950", "source_locator": "$.data.solutions[1].volume", "source_sha256":
    "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}, {"source_key":
    "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "1000", "source_locator": "$.data.solutions[2].volume", "source_sha256":
    "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}, {"source_key":
    "mediadiveJ1013api", "source_reference": "https://mediadive.dsmz.de/rest/medium/J1013",
    "source_quote": "1000", "source_locator": "$.data.solutions[3].volume", "source_sha256":
    "21086ddc5ece5c67a5ebde2e12890b63c50a32eb33d67aa26afa7d52c4a11757"}]}]'
- assessment_id: grounding
  area: grounding
  topic: Identifiers, labels and exact source forms
  outcome: concern
  summary: Both target and owner have 20/21 primary and 20/21 secondary ingredient
    links (95.24% linkage coverage, not a correctness score); all asserted labels
    and current MIM keys resolve. Explicit nickel chloride hexahydrate is mapped to
    CHEBI:34887, whose structure has no waters. The other explicit hydrate formulas
    correspond. The source says generic Resazurin here, so no sodium-salt discrepancy
    is inferred. Linked-stock provider compound IDs and CHEBI metadata resolve; cyanocob(III)alamin
    identifies one B12 form, not all vitamin stocks. Yeast extract remains an undefined
    mixture.
  target_ids:
  - CultureMech:002198
  evidence_ids:
  - record
  - owner-0
  - linked-stock
  - mim
  - chebi131361
  - chebi15377
  - chebi15956
  - chebi17439
  - chebi17883
  - chebi17992
  - chebi31206
  - chebi32139
  - chebi32145
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
- assessment_id: stock-identity
  area: identity
  topic: JCM 197 versus asserted solution 6241
  outcome: concern
  summary: The named source stock has ten vitamins in a one-liter batch, while 6241
    contains three vitamins made up to 100 mL with different amounts. Two verified
    dependency excerpts do not establish equivalence. The source-specific 3861 provider
    object corroborates JCM 197 but is not an automatically minted or substituted
    local ID. The 6241 biotin and water quantities also conflict with its own provider.
  target_ids:
  - CultureMech:002198
  evidence_ids:
  - record
  - owner-0
  - linked-stock
  - jcm1013
  - jcm197
  - mediadiveJ197api
  - solution6241
  - quantity-inventory
- assessment_id: preparation
  area: completeness
  topic: Main preparation, source defaults and stock-only instructions
  outcome: concern
  summary: Main prose preserves gas, separate sterilization, filtration, reducing-agent
    and conditional pH contexts. It omits the printed source default cycle and attaches
    the SL-10 dissolution instruction to the main array without stock scope. Keep
    all source exceptions and the primary pH range; 7.8 is within that range and is
    not itself a wrong value. No incubation, storage or new growth claim is inferred.
  target_ids:
  - CultureMech:002198
  evidence_ids:
  - record
  - owner-0
  - jcm1013
  - jcm433
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Liquid complex medium and biological limits
  outcome: supported
  summary: The exact source has yeast extract and defined salts, consistent with COMPLEX/SEMI_DEFINED
    and LIQUID. No target organism, strain, taxonomic ID, experimental variant or
    KG match is asserted. The title and generic cultivation application do not establish
    growth evidence. The auxiliary stock is contextual, not an additional reviewed
    medium.
  target_ids:
  - CultureMech:002198
  evidence_ids:
  - record
  - owner-0
  - jcm1013
  - mediadiveJ1013api
- assessment_id: ownership
  area: ownership
  topic: Exact maintained input and current transforms
  outcome: concern
  summary: The target and main owner share all scientific fields. Corrections belong
    first in the exact JCM owner, with separate dependency follow-up if authorized,
    then merge regeneration. Current importer and name-based migration mechanisms
    can explain classes of representation errors but do not replay historical execution.
    No generated file was edited.
  target_ids:
  - CultureMech:002198
  evidence_ids:
  - record
  - owner-0
  - linked-stock
  - importer
  - migrator
  - stock-importer
- assessment_id: evidence
  area: evidence
  topic: Narrow support and existing dependency excerpts
  outcome: concern
  summary: Target and main owner lack claim-level source excerpts. The target reference
    check examines zero excerpts. The two dependency quantity snippets match current
    identical provider bytes and retain their historical hash/time, but support only
    their own 6241 quantities. All primary/provider disputes and stages remain explicit.
  target_ids:
  - CultureMech:002198
  evidence_ids:
  - record
  - owner-0
  - linked-stock
  - solution6241
  - quantity-inventory
  - validate-references
- assessment_id: history
  area: provenance
  topic: Append-only event history and timestamp interpretation
  outcome: concern
  summary: All 26 scoped timestamps were checked for ISO syntax and timezone. 2 instances
    are malformed or lack timezone, as itemized. Curation events are process provenance
    rather than independent confirmation of recipe correctness.
  target_ids:
  - CultureMech:002198
  evidence_ids:
  - record
  - owner-0
  - history
  details: '[{"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
    "field": "curation_history[2].timestamp", "value": "2026-03-14T21:09:46.292785",
    "valid_ISO_datetime": true, "timezone_aware": false, "problem": "Timezone absent;
    local time cannot be asserted as UTC"}, {"path": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
    "field": "curation_history[3].timestamp", "value": "2026-04-04T17:50:16.857966",
    "valid_ISO_datetime": true, "timezone_aware": false, "problem": "Timezone absent;
    local time cannot be asserted as UTC"}]'
findings:
- finding_id: f1
  issue_key: cm002198-stock-stage-collapse
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock definitions and liquid additions are represented as direct medium concentrations
  description: The main record stores 30 and 10 G_PER_L for 30 mL of 5% w/v bicarbonate
    and 10 mL of 20% w/v sucrose; their source batch masses are 1.5 and 2 g. Five
    basal constituents and twelve trace-stock constituents retain their own stock-strength
    values as direct medium concentrations. Three source stock doses are missing and
    the vitamin dose is 10 G_PER_L instead of 10 mL. The represented formulation therefore
    differs materially from the source.
  target_ids:
  - CultureMech:002198
  field_paths:
  - ingredients[*].concentration
  - solutions
  evidence_ids:
  - record
  - owner-0
  - jcm1013
  - mediadiveJ1013api
  - quantity-inventory
  - importer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P1
  normalization_reason: 'Native P1 scientific formulation blocker normalized to blocker:
    the encoded recipe changes stock doses and strengths. This is not a schema P1.1
    failure; all mechanical target checks pass.'
  rule_id: P1
- finding_id: f2
  issue_key: cm002198-wrong-vitamin-stock
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The vitamin link resolves to a different source stock
  description: The local mediadive.solution:6241 link resolves, but JCM 1013 explicitly
    cites JCM 197 Trace vitamins. The source ten-vitamin one-liter stock differs from
    the three-vitamin 100 mL dependency. Existing 6241 evidence verifies only two
    of its own quantities and cannot establish this cross-reference. Its own biotin
    and solvent values also conflict with its source.
  target_ids:
  - CultureMech:002198
  field_paths:
  - solutions[0].term
  - solutions[0].name
  - solutions[0].concentration
  evidence_ids:
  - record
  - owner-0
  - linked-stock
  - jcm1013
  - jcm197
  - mediadiveJ197api
  - solution6241
  - quantity-inventory
  - migrator
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
  rule_id: P2
- finding_id: f3
  issue_key: cm002198-nickel-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Explicit nickel hexahydrate is assigned an anhydrous identity
  description: Both primary and provider SL-10 sources specify NiCl2 hexahydrate.
    Target and owner assign CHEBI:34887 to both primary and secondary fields, while
    that term has formula Cl2Ni and no hydrate waters. Correct labels and current
    MIM rows do not establish source-form correspondence.
  target_ids:
  - CultureMech:002198
  field_paths:
  - ingredients[16].term
  - ingredients[16].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - jcm433
  - mediadiveJ1013api
  - chebi34887
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
  rule_id: P2
- finding_id: f4
  issue_key: cm002198-hcl-source-discrepancy
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: The SL-10 HCl source molarity conflicts with provider mass normalization
  description: The primary and provider attribute specify 10 mL HCl at 7.7 M, while
    provider g_l and the flattened target store 2.5. Conditional on the provider one-liter
    stock volume and captured hydrogen chloride mass 36.461 g/mol, explicit molarity
    yields 2.807497 g/L. This source discrepancy remains after separating the stock
    stage; bare 25% does not establish w/v.
  target_ids:
  - CultureMech:002198
  field_paths:
  - ingredients[9].concentration
  evidence_ids:
  - record
  - owner-0
  - jcm433
  - mediadiveJ1013api
  - chebi17883
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
  rule_id: P2
- finding_id: f5
  issue_key: cm002198-preparation-stock-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation omits the source default cycle and detaches stock instructions
  description: The main prose retains important source exceptions, but omits the JCM
    default 121°C/15 min cycle. The SL-10 FeCl2/HCl dissolution sequence is stored
    as a main preparation step without naming the stock. Quantitative gas, pH and
    separate sulfide contexts must remain attached to the correct stage.
  target_ids:
  - CultureMech:002198
  field_paths:
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm1013
  - jcm433
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P3
  normalization_reason: Native P3.5 preparation incompleteness normalized to major
    because missing cycle context and an unscoped stock dissolution instruction impair
    reproducible interpretation of this multi-stock recipe.
  rule_id: P3.5
actions:
- action_id: a1
  description: Reconstruct source stock boundaries and their exact receiving doses
    in the maintained JCM owner. Preserve original stock batch amounts, explicit percentage
    bases and the provider volume convention. Derive receiving concentrations only
    with an explicit supported denominator and separate arithmetic; do not flatten
    stock strengths or silently use 1 L.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002198
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml
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
  description: Resolve the exact source-specific JCM 197 stock and its 10 mL dose
    before changing the main reference. Preserve the existing dependency as a distinct
    record; any correction of its biotin or solvent amounts needs its own maintained-input
    scope. Do not substitute by shared name or apply a 6241 dilution to this medium.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002198
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml
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
  description: Retain the literal hexahydrate source material and verify a matching
    ontology identity before changing either primary or secondary grounding. Do not
    convert its source mass using the anhydrous molecular weight or guess a replacement
    ID.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002198
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml
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
  description: Preserve both reported stock-strength representations with their exact
    sources. Verify the source stock convention before choosing a mass rate, and keep
    this conflict separate from the receiving dose and final-medium volume. Do not
    silently reinterpret the percent label.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002198
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml
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
  description: Preserve the source default cycle with explicit filtration and separate-autoclaving
    exceptions. Attach the SL-10 dissolution sequence to that stock and retain the
    conditional pH range and unquantified sulfide percentage/dose scope. Do not introduce
    additional incubation or culture-performance claims.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:002198
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml
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
- MediaDive declares 1002 mL for its main solution; this is a provider normalization
  basis, not a measured final volume. The separate sulfide preparation is not used
  to infer an additional liquid volume or percentage basis.
- JCM 433 is used only for SL-10, JCM 554 only for selenite-tungstate, and JCM 197
  only for Trace vitamins. Their parent recipes, other stocks, biological claims and
  preparation are not transferred.
- The asserted stock 6241 is inspected as a contextual dependency, not a second reviewed
  target. Its valid accession and two supported quantities do not make it the JCM
  197 vitamin stock.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- All 19 main-target/owner timestamps are timezone-aware; two of seven contextual
  stock timestamps are timezone-naive. Preserve those original dependency events and
  uncertainty; no historical timezone is invented.
tags:
- unreviewed-records
- batch-015
- generated-medium
```
