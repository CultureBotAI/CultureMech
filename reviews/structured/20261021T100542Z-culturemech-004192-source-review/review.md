# Source and formulation review: acetivibrio_cellulolyticus_medium (CultureMech:004192)

- Review: 20261021T100542Z-culturemech-004192-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T09:56:43Z
- Finished UTC: 2026-10-21T10:05:42Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

KOMODO 165 and the exact DSMZ 165 recipe identify the medium, but the generated target and both owners flatten five stocks and sum amounts from distinct stages. Sulfuric acid is especially misrepresented: 1000 mL of 0.1 N acid used in a ferrous stock becomes 1000 g/L in the medium. The generated/KOMODO representations also lose the DSMZ owner preparation and the cellulose-for-cellobiose alternative. Nickel hydrate and sodium-resazurin mappings disagree with the supplied forms. All four diagnostics pass; four inherited timestamps remain malformed or timezone-naive.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 143; batch 015 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding fourteen task batches contain 140 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 142 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:004192 | data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml | generated | acetivibrio_cellulolyticus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:004192 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:004192 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch015/143/strict.tsv |
| validate-terms | passed | True | CultureMech:004192 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:004192 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:004192 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Scoped timestamp syntax and timezone inspection | failed | False | CultureMech:004192 | 29 timestamps inspected, 4 invalid or timezone-naive; old provenance remains unchanged. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:004192.

The four documented recipes completed; interpret the scope of each separately.

### Stable source identity and exact contributors

identity: supported. Targets: CultureMech:004192.

The target CM004192 derives from the KOMODO 165 owner and DSMZ owner CM001142, both explicitly named in merge metadata. The exact KOMODO accession link and current DSMZ title agree. The owners have the same 35 ingredient values but differ in preparation, pH representation and notes; the old ingredient fingerprint does not erase those differences. All inspected input hashes match.

### Source contributors and bounded carbon-source alternatives

scope: concern. Targets: CultureMech:004192.

There is no explicit parent_media or variant_children relationship in these three records. The two source contributors are identified by the actual merge event. The exact primary treats cellulose as an alternative to cellobiose; the target/KOMODO owner encode only Optional ingredient beside a simultaneous cellobiose row. That does not document a selected branch or preserve the mutual substitution stated in the DSMZ owner preparation.

### Primary labels/forms and pinned secondary correspondence

grounding: supported. Targets: CultureMech:004192.

Layer-specific counts are {"target": {"ingredient_instances": 35, "primary_CHEBI_instances": 35, "secondary_current_asserted_instances": 33, "secondary_current_verified_instances": 33, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 100.0, "secondary_verified_percent": 94.29}, "owner-0": {"ingredient_instances": 35, "primary_CHEBI_instances": 35, "secondary_current_asserted_instances": 33, "secondary_current_verified_instances": 33, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 100.0, "secondary_verified_percent": 94.29}, "owner-1": {"ingredient_instances": 35, "primary_CHEBI_instances": 35, "secondary_current_asserted_instances": 33, "secondary_current_verified_instances": 33, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 100.0, "secondary_verified_percent": 94.29}}. Percentages are 0–100 linkage coverage over direct ingredient instances, not scientific accuracy. The 0 legacy link instances across reviewed layers are unverified by the current CHEBI-keyed snapshot; absence here does not prove historical invalidity. Current secondary keys without a live preferred-term row are []. No secondary linked-set percentage is invented for an empty set.

{"label_drift": [], "legacy": [], "missing_current_secondary": []}

### Supplied hydrates, redox indicator and carbon-source materials

grounding: concern. Targets: CultureMech:004192.

All 35 asserted primary CHEBI instances resolve with canonical labels, and all 33 asserted current secondary keys have live pinned-index rows. Nevertheless NiCl2 x 6 H2O maps to CHEBI:34887 with no waters, and sodium resazurin maps to neutral CHEBI:8806 with no sodium. D-(+)-calcium pantothenate agrees with the D-specific CHEBI:31345 structure; generic lipoic acid has no selected stereochemistry that contradicts source DL. The source cysteine hydrochloride monohydrate is supported by CHEBI:91248 definition. Cellulose maps to the beta-D-glucan class, which does not specify the grade, purity or paper/cotton alternatives. Retain those source qualifiers separately.

### Gas atmosphere, sterilization, acid-stock freshness and pH

consistency: concern. Targets: CultureMech:004192.

DSMZ owner preserves the three source paragraphs: main 80% N2/20% CO2 anoxic preparation, distinct sterile-stock additions with 100% N2 versus mixed gas, filtration of cellobiose/vitamins, final pH 7.2–7.4 and the cellulose substitution; mineral-stock KOH pH adjustment; and freshly prepared ferrous stock. Target and KOMODO owner omit all three and retain Aerobic: Yes with scalar pH 7.2. Scalar 7.2 is a permitted endpoint, but it loses the explicit complete-medium range. The primary does not state autoclave duration/temperature, storage or shelf life; none is inferred.

### Catalog classification and selected formulation scope

scope: concern. Targets: CultureMech:004192.

MediaDive labels this medium complex, while the KOMODO row has is_complex=false. The maintained records assert COMPLEX/UNDEFINED without recording a selected cellobiose/cellulose material branch. The explicit source ingredients and alternative grades should guide reassessment; neither catalog flag alone proves composition type for every branch. LIQUID is consistent with the absence of a gelling-agent recipe; suspended cellulose does not by itself make an agar solid medium. Bacterial filing and generic cultivation do not establish organism growth.

### Append-only history and timestamp interpretation

provenance: concern. Targets: CultureMech:004192.

29 exact timestamp instances were examined; 4 lack valid syntax or explicit timezone. No local timestamp was assumed UTC or rewritten. Process and confidence annotations are not independent scientific evidence.

[{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[0].timestamp", "value": "2026-01-27T01:15:02.fZ", "valid_ISO_datetime": false, "timezone_aware": false}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:18.940996", "valid_ISO_datetime": true, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[0].timestamp", "value": "2026-01-27T01:15:02.fZ", "valid_ISO_datetime": false, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:18.940996", "valid_ISO_datetime": true, "timezone_aware": false}]

### Every stored amount, stock dose and source-stage dependency

quantity: concern. Targets: CultureMech:004192.

All 35 ingredient amounts in the target and each owner are traced to all 49 literal provider recipe rows, two unquantified preparation additions and five quantitative preparation contexts. The inventory distinguishes direct amounts, five stock doses, stock strengths, solvents, optional substitution and source normality, with arithmetic outside exact quotations. Conditional stock contributions do not establish measured final volume.

[{"field_path": "source solution 283 recipe[0] (not represented)", "name": "Mineral solution 1", "current": null, "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Mineral solution 1\",\n                        \"solution_id\": 284,\n                        \"amount\": 75,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[0]", "preparation_stage": "Main sol. 165 (solution 283, declared 1001 mL)", "decision_rationale": "The main recipe explicitly adds 75 ml of stock 284. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-1", "affected_local_fields": [], "source_amount": 75, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "source solution 283 recipe[1] (not represented)", "name": "Mineral solution 2", "current": null, "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Mineral solution 2\",\n                        \"solution_id\": 285,\n                        \"amount\": 75,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[1]", "preparation_stage": "Main sol. 165 (solution 283, declared 1001 mL)", "decision_rationale": "The main recipe explicitly adds 75 ml of stock 285. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-2", "affected_local_fields": [], "source_amount": 75, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "source solution 283 recipe[2] (not represented)", "name": "Modified Wolin's mineral solution", "current": null, "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[2]", "preparation_stage": "Main sol. 165 (solution 283, declared 1001 mL)", "decision_rationale": "The main recipe explicitly adds 10 ml of stock 241. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-3", "affected_local_fields": [], "source_amount": 10, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "source solution 283 recipe[3] (not represented)", "name": "FeSO4 x 7 H2O solution (0.1% w/v)", "current": null, "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"FeSO4 x 7 H2O solution (0.1% w/v)\",\n                        \"solution_id\": 5861,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[3]", "preparation_stage": "Main sol. 165 (solution 283, declared 1001 mL)", "decision_rationale": "The main recipe explicitly adds 20 ml of stock 5861. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-4", "affected_local_fields": [], "source_amount": 20, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[0].concentration", "name": "Sodium resazurin", "current": {"value": "0.0004995", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0004995,\n                        \"mmol_l\": 0.0019887,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[4]", "preparation_stage": "Main sol. 165 (solution 283, declared 1001 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1001 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-5", "arithmetic_separate_from_quote": "0.1% w/v means 0.1 g per 100 mL; 0.5 mL contains 0.0005 g. Dividing by provider-declared 1001/1000 L gives 0.0004995004995004995004995004995 g/L; reported g_l is 0.0004995. Preserve this source stock dose separately.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "name": "Sodium resazurin", "current": {"value": "0.0004995", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "name": "Sodium resazurin", "current": {"value": "0.0004995", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[0].concentration", "name": "Sodium resazurin", "current": {"value": "0.0004995", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "ml", "source_attribute": "0.1% w/v", "provider_g_l": 0.0004995, "provider_stage_volume_ml": 1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[1].concentration", "name": "Na2CO3", "current": {"value": "1.4985", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.4985,\n                        \"mmol_l\": 14.1384,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[5]", "preparation_stage": "Main sol. 165 (solution 283, declared 1001 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1001 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-6", "arithmetic_separate_from_quote": "Original 1.5 g × 1 g/g ÷ (1001 mL / 1000 mL per L) = 1.498501498501498501498501499 g/L on the provider-declared stage volume; reported g_l is 1.4985. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "name": "Na2CO3", "current": {"value": "1.4985", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "name": "Na2CO3", "current": {"value": "1.4985", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[1].concentration", "name": "Na2CO3", "current": {"value": "1.4985", "unit": "G_PER_L"}}], "source_amount": 1.5, "source_unit": "g", "source_attribute": null, "provider_g_l": 1.4985, "provider_stage_volume_ml": 1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[2].concentration", "name": "Cellobiose", "current": {"value": "2.997", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Cellobiose\",\n                        \"compound_id\": 214,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.997,\n                        \"mmol_l\": 8.75549,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[6]", "preparation_stage": "Main sol. 165 (solution 283, declared 1001 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1001 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-7", "arithmetic_separate_from_quote": "Original 3 g × 1 g/g ÷ (1001 mL / 1000 mL per L) = 2.997002997002997002997002997 g/L on the provider-declared stage volume; reported g_l is 2.997. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "name": "Cellobiose", "current": {"value": "2.997", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "name": "Cellobiose", "current": {"value": "2.997", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[2].concentration", "name": "Cellobiose", "current": {"value": "2.997", "unit": "G_PER_L"}}], "source_amount": 3, "source_unit": "g", "source_attribute": null, "provider_g_l": 2.997, "provider_stage_volume_ml": 1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[3].concentration", "name": "Cellulose", "current": {"value": "2.997", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Cellulose\",\n                        \"compound_id\": 400,\n                        \"attribute\": \"MN300\",\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.997,\n                        \"optional\": 1\n                    }", "source_locator": "$.data.solutions[0].recipe[7]", "preparation_stage": "Main sol. 165 (solution 283, declared 1001 mL)", "decision_rationale": "The source gives cellulose 3 g as an alternative to cellobiose, not an extra carbon source added to the same selected recipe. Retain the source amount and grade/alternative condition; provider g_l 2.997 follows its declared 1001 mL basis.", "evidence_id": "quantity-8", "arithmetic_separate_from_quote": "3 g / 1.001 L = 2.997002997... g/L on the provider basis only; this calculation does not establish the selected carbon-source branch.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "name": "Cellulose", "current": {"value": "2.997", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "name": "Cellulose", "current": {"value": "2.997", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[3].concentration", "name": "Cellulose", "current": {"value": "2.997", "unit": "G_PER_L"}}], "source_amount": 3, "source_unit": "g", "source_attribute": "MN300", "provider_g_l": 2.997, "provider_stage_volume_ml": 1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "source solution 283 recipe[8] (not represented)", "name": "Wolin's vitamin solution (10x)", "current": null, "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[8]", "preparation_stage": "Main sol. 165 (solution 283, declared 1001 mL)", "decision_rationale": "The main recipe explicitly adds 1 ml of stock 5980. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-9", "affected_local_fields": [], "source_amount": 1, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[4].concentration", "name": "L-Cysteine HCl x H2O", "current": {"value": "0.24975", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.24975,\n                        \"mmol_l\": 1.42198,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[9]", "preparation_stage": "Main sol. 165 (solution 283, declared 1001 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1001 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-10", "arithmetic_separate_from_quote": "Original 0.25 g × 1 g/g ÷ (1001 mL / 1000 mL per L) = 0.2497502497502497502497502498 g/L on the provider-declared stage volume; reported g_l is 0.24975. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "name": "L-Cysteine HCl x H2O", "current": {"value": "0.24975", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "name": "L-Cysteine HCl x H2O", "current": {"value": "0.24975", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[4].concentration", "name": "L-Cysteine HCl x H2O", "current": {"value": "0.24975", "unit": "G_PER_L"}}], "source_amount": 0.25, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.24975, "provider_stage_volume_ml": 1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[5].concentration", "name": "Na2S x 9 H2O", "current": {"value": "0.24975", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.24975,\n                        \"mmol_l\": 1.03984,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[10]", "preparation_stage": "Main sol. 165 (solution 283, declared 1001 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1001 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-11", "arithmetic_separate_from_quote": "Original 0.25 g × 1 g/g ÷ (1001 mL / 1000 mL per L) = 0.2497502497502497502497502498 g/L on the provider-declared stage volume; reported g_l is 0.24975. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "name": "Na2S x 9 H2O", "current": {"value": "0.24975", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "name": "Na2S x 9 H2O", "current": {"value": "0.24975", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[5].concentration", "name": "Na2S x 9 H2O", "current": {"value": "0.24975", "unit": "G_PER_L"}}], "source_amount": 0.25, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.24975, "provider_stage_volume_ml": 1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "source solution 283 recipe[11] (not represented)", "name": "Distilled water", "current": null, "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 820,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[11]", "preparation_stage": "Main sol. 165 (solution 283, declared 1001 mL)", "decision_rationale": "Preserve the source solvent quantity 820 ml in its own stage. The provider declares this solution volume as 1001 mL; water addition is not independent proof of measured final volume.", "evidence_id": "quantity-12", "affected_local_fields": [], "source_amount": 820, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[6].concentration", "name": "K2HPO4", "current": {"value": "3.9", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 3.9,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.9,\n                        \"mmol_l\": 22.3911,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[0]", "preparation_stage": "Mineral solution 1 (solution 284, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-13", "arithmetic_separate_from_quote": "Original 3.9 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 3.9 g/L on the provider-declared stage volume; reported g_l is 3.9. This is not a receiving-medium dilution. Conditional receiving contribution: 3.9 g/L stock × 0.075 L / 1.001 L = 0.2922077922077922077922077922 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "name": "K2HPO4", "current": {"value": "3.9", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "name": "K2HPO4", "current": {"value": "3.9", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[6].concentration", "name": "K2HPO4", "current": {"value": "3.9", "unit": "G_PER_L"}}], "source_amount": 3.9, "source_unit": "g", "source_attribute": null, "provider_g_l": 3.9, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "source solution 284 recipe[1] (not represented)", "name": "Distilled water", "current": null, "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[1]", "preparation_stage": "Mineral solution 1 (solution 284, declared 1000 mL)", "decision_rationale": "Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume.", "evidence_id": "quantity-14", "affected_local_fields": [], "source_amount": 1000, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[7].concentration", "name": "KH2PO4", "current": {"value": "2.4", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 2.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.4,\n                        \"mmol_l\": 17.636,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[0]", "preparation_stage": "Mineral solution 2 (solution 285, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-15", "arithmetic_separate_from_quote": "Original 2.4 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 2.4 g/L on the provider-declared stage volume; reported g_l is 2.4. This is not a receiving-medium dilution. Conditional receiving contribution: 2.4 g/L stock × 0.075 L / 1.001 L = 0.1798201798201798201798201798 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "name": "KH2PO4", "current": {"value": "2.4", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "name": "KH2PO4", "current": {"value": "2.4", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[7].concentration", "name": "KH2PO4", "current": {"value": "2.4", "unit": "G_PER_L"}}], "source_amount": 2.4, "source_unit": "g", "source_attribute": null, "provider_g_l": 2.4, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[8].concentration", "name": "(NH4)2SO4", "current": {"value": "6", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"mmol_l\": 45.4064,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[1]", "preparation_stage": "Mineral solution 2 (solution 285, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-16", "arithmetic_separate_from_quote": "Original 6 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 6 g/L on the provider-declared stage volume; reported g_l is 6. This is not a receiving-medium dilution. Conditional receiving contribution: 6 g/L stock × 0.075 L / 1.001 L = 0.4495504495504495504495504496 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "name": "(NH4)2SO4", "current": {"value": "6", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "name": "(NH4)2SO4", "current": {"value": "6", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[8].concentration", "name": "(NH4)2SO4", "current": {"value": "6", "unit": "G_PER_L"}}], "source_amount": 6, "source_unit": "g", "source_attribute": null, "provider_g_l": 6, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[9].concentration", "name": "NaCl", "current": {"value": "1.5899999999999999", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 0.59,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.59,\n                        \"mmol_l\": 10.0958,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[2]", "preparation_stage": "Mineral solution 2 (solution 285, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-17", "arithmetic_separate_from_quote": "Original 0.59 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.59 g/L on the provider-declared stage volume; reported g_l is 0.59. This is not a receiving-medium dilution. Conditional receiving contribution: 0.59 g/L stock × 0.075 L / 1.001 L = 0.04420579420579420579420579421 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "name": "NaCl", "current": {"value": "1.5899999999999999", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "name": "NaCl", "current": {"value": "1.5899999999999999", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[9].concentration", "name": "NaCl", "current": {"value": "1.5899999999999999", "unit": "G_PER_L"}}], "source_amount": 0.59, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.59, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[10].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "4.2", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 1.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.2,\n                        \"mmol_l\": 4.86863,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[3]", "preparation_stage": "Mineral solution 2 (solution 285, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-18", "arithmetic_separate_from_quote": "Original 1.2 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 1.2 g/L on the provider-declared stage volume; reported g_l is 1.2. This is not a receiving-medium dilution. Conditional receiving contribution: 1.2 g/L stock × 0.075 L / 1.001 L = 0.08991008991008991008991008991 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "4.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "4.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[10].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "4.2", "unit": "G_PER_L"}}], "source_amount": 1.2, "source_unit": "g", "source_attribute": null, "provider_g_l": 1.2, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[11].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.82", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.72,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.72,\n                        \"mmol_l\": 4.89746,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[4]", "preparation_stage": "Mineral solution 2 (solution 285, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-19", "arithmetic_separate_from_quote": "Original 0.72 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.72 g/L on the provider-declared stage volume; reported g_l is 0.72. This is not a receiving-medium dilution. Conditional receiving contribution: 0.72 g/L stock × 0.075 L / 1.001 L = 0.05394605394605394605394605395 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.82", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.82", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[11].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.82", "unit": "G_PER_L"}}], "source_amount": 0.72, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.72, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "source solution 285 recipe[5] (not represented)", "name": "Distilled water", "current": null, "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[5]", "preparation_stage": "Mineral solution 2 (solution 285, declared 1000 mL)", "decision_rationale": "Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume.", "evidence_id": "quantity-20", "affected_local_fields": [], "source_amount": 1000, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[12].concentration", "name": "Nitrilotriacetic acid", "current": {"value": "1.5", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[0]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-21", "arithmetic_separate_from_quote": "Original 1.5 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 1.5 g/L on the provider-declared stage volume; reported g_l is 1.5. This is not a receiving-medium dilution. Conditional receiving contribution: 1.5 g/L stock × 0.010 L / 1.001 L = 0.01498501498501498501498501499 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "name": "Nitrilotriacetic acid", "current": {"value": "1.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "name": "Nitrilotriacetic acid", "current": {"value": "1.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[12].concentration", "name": "Nitrilotriacetic acid", "current": {"value": "1.5", "unit": "G_PER_L"}}], "source_amount": 1.5, "source_unit": "g", "source_attribute": null, "provider_g_l": 1.5, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[10].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "4.2", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[1]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-22", "arithmetic_separate_from_quote": "Original 3 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 3 g/L on the provider-declared stage volume; reported g_l is 3. This is not a receiving-medium dilution. Conditional receiving contribution: 3 g/L stock × 0.010 L / 1.001 L = 0.02997002997002997002997002997 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "4.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "4.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[10].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "4.2", "unit": "G_PER_L"}}], "source_amount": 3, "source_unit": "g", "source_attribute": null, "provider_g_l": 3, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[13].concentration", "name": "MnSO4 x H2O", "current": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.9583,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[2]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-23", "arithmetic_separate_from_quote": "Original 0.5 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.5 g/L on the provider-declared stage volume; reported g_l is 0.5. This is not a receiving-medium dilution. Conditional receiving contribution: 0.5 g/L stock × 0.010 L / 1.001 L = 0.004995004995004995004995004995 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "name": "MnSO4 x H2O", "current": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "name": "MnSO4 x H2O", "current": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[13].concentration", "name": "MnSO4 x H2O", "current": {"value": "0.5", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.5, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[9].concentration", "name": "NaCl", "current": {"value": "1.5899999999999999", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[3]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-24", "arithmetic_separate_from_quote": "Original 1 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 1 g/L on the provider-declared stage volume; reported g_l is 1. This is not a receiving-medium dilution. Conditional receiving contribution: 1 g/L stock × 0.010 L / 1.001 L = 0.009990009990009990009990009990 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "name": "NaCl", "current": {"value": "1.5899999999999999", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "name": "NaCl", "current": {"value": "1.5899999999999999", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[9].concentration", "name": "NaCl", "current": {"value": "1.5899999999999999", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "g", "source_attribute": null, "provider_g_l": 1, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[14].concentration", "name": "FeSO4 x 7 H2O", "current": {"value": "1.1", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[4]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-25", "arithmetic_separate_from_quote": "Original 0.1 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.1 g/L on the provider-declared stage volume; reported g_l is 0.1. This is not a receiving-medium dilution. Conditional receiving contribution: 0.1 g/L stock × 0.010 L / 1.001 L = 0.0009990009990009990009990009990 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "name": "FeSO4 x 7 H2O", "current": {"value": "1.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "name": "FeSO4 x 7 H2O", "current": {"value": "1.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[14].concentration", "name": "FeSO4 x 7 H2O", "current": {"value": "1.1", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[15].concentration", "name": "CoSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 1.16132,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[5]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-26", "arithmetic_separate_from_quote": "Original 0.18 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.18 g/L on the provider-declared stage volume; reported g_l is 0.18. This is not a receiving-medium dilution. Conditional receiving contribution: 0.18 g/L stock × 0.010 L / 1.001 L = 0.001798201798201798201798201798 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "name": "CoSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "name": "CoSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[15].concentration", "name": "CoSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}], "source_amount": 0.18, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.18, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[11].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.82", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[6]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-27", "arithmetic_separate_from_quote": "Original 0.1 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.1 g/L on the provider-declared stage volume; reported g_l is 0.1. This is not a receiving-medium dilution. Conditional receiving contribution: 0.1 g/L stock × 0.010 L / 1.001 L = 0.0009990009990009990009990009990 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.82", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.82", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[11].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.82", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[16].concentration", "name": "ZnSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.625954,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[7]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-28", "arithmetic_separate_from_quote": "Original 0.18 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.18 g/L on the provider-declared stage volume; reported g_l is 0.18. This is not a receiving-medium dilution. Conditional receiving contribution: 0.18 g/L stock × 0.010 L / 1.001 L = 0.001798201798201798201798201798 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "name": "ZnSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "name": "ZnSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[16].concentration", "name": "ZnSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}], "source_amount": 0.18, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.18, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[17].concentration", "name": "CuSO4 x 5 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[8]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-29", "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01. This is not a receiving-medium dilution. Conditional receiving contribution: 0.01 g/L stock × 0.010 L / 1.001 L = 0.00009990009990009990009990009990 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "name": "CuSO4 x 5 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "name": "CuSO4 x 5 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[17].concentration", "name": "CuSO4 x 5 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.01, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[18].concentration", "name": "AlK(SO4)2 x 12 H2O", "current": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0421596,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[9]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-30", "arithmetic_separate_from_quote": "Original 0.02 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.02 g/L on the provider-declared stage volume; reported g_l is 0.02. This is not a receiving-medium dilution. Conditional receiving contribution: 0.02 g/L stock × 0.010 L / 1.001 L = 0.0001998001998001998001998001998 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "name": "AlK(SO4)2 x 12 H2O", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "name": "AlK(SO4)2 x 12 H2O", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[18].concentration", "name": "AlK(SO4)2 x 12 H2O", "current": {"value": "0.02", "unit": "G_PER_L"}}], "source_amount": 0.02, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.02, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[19].concentration", "name": "H3BO3", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[10]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-31", "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01. This is not a receiving-medium dilution. Conditional receiving contribution: 0.01 g/L stock × 0.010 L / 1.001 L = 0.00009990009990009990009990009990 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "name": "H3BO3", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "name": "H3BO3", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[19].concentration", "name": "H3BO3", "current": {"value": "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.01, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[20].concentration", "name": "Na2MoO4 x 2 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[11]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-32", "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01. This is not a receiving-medium dilution. Conditional receiving contribution: 0.01 g/L stock × 0.010 L / 1.001 L = 0.00009990009990009990009990009990 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "name": "Na2MoO4 x 2 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "name": "Na2MoO4 x 2 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[20].concentration", "name": "Na2MoO4 x 2 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.01, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[21].concentration", "name": "NiCl2 x 6 H2O", "current": {"value": "0.03", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.231483,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[12]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-33", "arithmetic_separate_from_quote": "Original 0.03 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.03 g/L on the provider-declared stage volume; reported g_l is 0.03. This is not a receiving-medium dilution. Conditional receiving contribution: 0.03 g/L stock × 0.010 L / 1.001 L = 0.0002997002997002997002997002997 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "name": "NiCl2 x 6 H2O", "current": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "name": "NiCl2 x 6 H2O", "current": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[21].concentration", "name": "NiCl2 x 6 H2O", "current": {"value": "0.03", "unit": "G_PER_L"}}], "source_amount": 0.03, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.03, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[22].concentration", "name": "Na2SeO3 x 5 H2O", "current": {"value": "0.0003", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\": 0.00114062,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[13]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-34", "arithmetic_separate_from_quote": "Original 0.3 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.0003 g/L on the provider-declared stage volume; reported g_l is 0.0003. This is not a receiving-medium dilution. Conditional receiving contribution: 0.0003 g/L stock × 0.010 L / 1.001 L = 0.000002997002997002997002997002997 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "name": "Na2SeO3 x 5 H2O", "current": {"value": "0.0003", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "name": "Na2SeO3 x 5 H2O", "current": {"value": "0.0003", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[22].concentration", "name": "Na2SeO3 x 5 H2O", "current": {"value": "0.0003", "unit": "G_PER_L"}}], "source_amount": 0.3, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.0003, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[23].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\": 0.00121267,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[14]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-35", "arithmetic_separate_from_quote": "Original 0.4 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.0004 g/L on the provider-declared stage volume; reported g_l is 0.0004. This is not a receiving-medium dilution. Conditional receiving contribution: 0.0004 g/L stock × 0.010 L / 1.001 L = 0.000003996003996003996003996003996 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[23].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004", "unit": "G_PER_L"}}], "source_amount": 0.4, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.0004, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "source solution 241 recipe[15] (not represented)", "name": "Distilled water", "current": null, "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[15]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume.", "evidence_id": "quantity-36", "affected_local_fields": [], "source_amount": 1000, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[14].concentration", "name": "FeSO4 x 7 H2O", "current": {"value": "1.1", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 3.59693,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[4].recipe[0]", "preparation_stage": "FeSO4 x 7 H2O solution (0.1% w/v) (solution 5861, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-37", "arithmetic_separate_from_quote": "Original 1 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 1 g/L on the provider-declared stage volume; reported g_l is 1. This is not a receiving-medium dilution. Conditional receiving contribution: 1 g/L stock × 0.020 L / 1.001 L = 0.01998001998001998001998001998 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "name": "FeSO4 x 7 H2O", "current": {"value": "1.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "name": "FeSO4 x 7 H2O", "current": {"value": "1.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[14].concentration", "name": "FeSO4 x 7 H2O", "current": {"value": "1.1", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "g", "source_attribute": null, "provider_g_l": 1, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[24].concentration", "name": "H2SO4", "current": {"value": "1000", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H2SO4\",\n                        \"compound_id\": 122,\n                        \"attribute\": \"0.1 N\",\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[4].recipe[1]", "preparation_stage": "FeSO4 x 7 H2O solution (0.1% w/v) (solution 5861, declared 1000 mL)", "decision_rationale": "The exact row is 1000 mL of 0.1 N H2SO4 in the ferrous sulfate stock. Local 1000 G_PER_L is a liquid-volume-to-mass-unit error and a stage error. Retain the dilute acid solvent and its normality; do not treat it as neat acid or infer density.", "evidence_id": "quantity-38", "arithmetic_separate_from_quote": "No mass conversion is required or asserted. The source uses this acid in stock 5861; the main medium adds only 20 mL of that stock.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "name": "H2SO4", "current": {"value": "1000", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "name": "H2SO4", "current": {"value": "1000", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[24].concentration", "name": "H2SO4", "current": {"value": "1000", "unit": "G_PER_L"}}], "source_amount": 1000, "source_unit": "ml", "source_attribute": "0.1 N", "provider_g_l": null, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[25].concentration", "name": "Biotin", "current": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[5].recipe[0]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-39", "arithmetic_separate_from_quote": "Original 20 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.020 g/L on the provider-declared stage volume; reported g_l is 0.02. This is not a receiving-medium dilution. Conditional receiving contribution: 0.02 g/L stock × 0.001 L / 1.001 L = 0.00001998001998001998001998001998 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "name": "Biotin", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "name": "Biotin", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[25].concentration", "name": "Biotin", "current": {"value": "0.02", "unit": "G_PER_L"}}], "source_amount": 20, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.02, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[26].concentration", "name": "Folic acid", "current": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[5].recipe[1]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-40", "arithmetic_separate_from_quote": "Original 20 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.020 g/L on the provider-declared stage volume; reported g_l is 0.02. This is not a receiving-medium dilution. Conditional receiving contribution: 0.02 g/L stock × 0.001 L / 1.001 L = 0.00001998001998001998001998001998 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "name": "Folic acid", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "name": "Folic acid", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[26].concentration", "name": "Folic acid", "current": {"value": "0.02", "unit": "G_PER_L"}}], "source_amount": 20, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.02, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[27].concentration", "name": "Pyridoxine hydrochloride", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[5].recipe[2]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-41", "arithmetic_separate_from_quote": "Original 100 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.100 g/L on the provider-declared stage volume; reported g_l is 0.1. This is not a receiving-medium dilution. Conditional receiving contribution: 0.1 g/L stock × 0.001 L / 1.001 L = 0.00009990009990009990009990009990 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "name": "Pyridoxine hydrochloride", "current": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "name": "Pyridoxine hydrochloride", "current": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[27].concentration", "name": "Pyridoxine hydrochloride", "current": {"value": "0.1", "unit": "G_PER_L"}}], "source_amount": 100, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[28].concentration", "name": "Thiamine HCl", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[5].recipe[3]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-42", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional receiving contribution: 0.05 g/L stock × 0.001 L / 1.001 L = 0.00004995004995004995004995004995 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "name": "Thiamine HCl", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "name": "Thiamine HCl", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[28].concentration", "name": "Thiamine HCl", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[29].concentration", "name": "Riboflavin", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[5].recipe[4]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-43", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional receiving contribution: 0.05 g/L stock × 0.001 L / 1.001 L = 0.00004995004995004995004995004995 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "name": "Riboflavin", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "name": "Riboflavin", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[29].concentration", "name": "Riboflavin", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[30].concentration", "name": "Nicotinic acid", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[5].recipe[5]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-44", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional receiving contribution: 0.05 g/L stock × 0.001 L / 1.001 L = 0.00004995004995004995004995004995 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "name": "Nicotinic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "name": "Nicotinic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[30].concentration", "name": "Nicotinic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[31].concentration", "name": "Calcium D-(+)-pantothenate", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[5].recipe[6]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-45", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional receiving contribution: 0.05 g/L stock × 0.001 L / 1.001 L = 0.00004995004995004995004995004995 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "name": "Calcium D-(+)-pantothenate", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "name": "Calcium D-(+)-pantothenate", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[31].concentration", "name": "Calcium D-(+)-pantothenate", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[32].concentration", "name": "Vitamin B12", "current": {"value": "0.001", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[5].recipe[7]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-46", "arithmetic_separate_from_quote": "Original 1 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.001 g/L on the provider-declared stage volume; reported g_l is 0.001. This is not a receiving-medium dilution. Conditional receiving contribution: 0.001 g/L stock × 0.001 L / 1.001 L = 9.990009990009990009990009990E-7 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[32].concentration", "name": "Vitamin B12", "current": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[32].concentration", "name": "Vitamin B12", "current": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[32].concentration", "name": "Vitamin B12", "current": {"value": "0.001", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.001, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[33].concentration", "name": "p-Aminobenzoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[5].recipe[8]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-47", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional receiving contribution: 0.05 g/L stock × 0.001 L / 1.001 L = 0.00004995004995004995004995004995 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[33].concentration", "name": "p-Aminobenzoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[33].concentration", "name": "p-Aminobenzoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[33].concentration", "name": "p-Aminobenzoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[34].concentration", "name": "(DL)-alpha-Lipoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[5].recipe[9]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-48", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional receiving contribution: 0.05 g/L stock × 0.001 L / 1.001 L = 0.00004995004995004995004995004995 g/L. The source stock remains a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[34].concentration", "name": "(DL)-alpha-Lipoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "ingredients[34].concentration", "name": "(DL)-alpha-Lipoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "ingredients[34].concentration", "name": "(DL)-alpha-Lipoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "source solution 5980 recipe[10] (not represented)", "name": "Distilled water", "current": null, "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[5].recipe[10]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume.", "evidence_id": "quantity-49", "affected_local_fields": [], "source_amount": 1000, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "mineral stock KOH addition (not quantified)", "name": "KOH", "current": null, "decision": "not_quantified", "source_key": "dsmz165", "source_quote": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust", "source_locator": "page 2, Modified Wolin mineral stock preparation", "preparation_stage": "mineral stock", "decision_rationale": "Source adjusts pH to 6.5 and then 7.0 with KOH without specifying a fixed amount. Do not fill that absence with zero or a guessed dose.", "evidence_id": "quantity-50"}, {"field_path": "later sterile stock volumes (not quantified)", "name": "Post-autoclave anoxic additions", "current": null, "decision": "not_quantified", "source_key": "dsmz165", "source_quote": "autoclave. Add cellobiose, vitamins, cysteine and sulfide from sterile anoxic stock solutions", "source_locator": "page 1, main preparation paragraph", "preparation_stage": "main preparation after autoclaving", "decision_rationale": "Cellobiose, vitamins, cysteine, sulfide and carbonate have stated ingredient amounts, but not all later stock volumes are specified. Their sterile/anoxic handling and separate gas atmospheres cannot establish a measured final volume.", "evidence_id": "quantity-51"}, {"field_path": "ph_value / ph_range", "name": "Complete-medium pH", "current": 7.2, "decision": "correct", "source_key": "dsmz165", "source_quote": "filtration. Prior to use adjust pH of complete medium to 7.2 - 7.4. Cellulose (MN 300,", "source_locator": "page 1, main preparation paragraph", "preparation_stage": "complete medium", "decision_rationale": "Target pH 7.2 is a permitted endpoint, but the exact source and DSMZ owner specify the complete-medium range 7.2–7.4. Preserve its scope and range rather than replacing it with a midpoint.", "evidence_id": "quantity-52"}, {"field_path": "preparation_steps.initial_gas", "name": "Initial gas composition", "current": null, "decision": "add", "source_key": "dsmz165", "source_quote": "sparge medium with 80% N2 and 20% CO2 gas mixture for 30 – 45 min to make it anoxic.", "source_locator": "page 1, main preparation paragraph", "preparation_stage": "initial anoxic preparation", "decision_rationale": "Preserve the source 80% N2 / 20% CO2 gas mixture as preparation context, not an organism phenotype.", "evidence_id": "quantity-53"}, {"field_path": "preparation_steps.sparging_duration", "name": "Sparging duration", "current": null, "decision": "add", "source_key": "dsmz165", "source_quote": "sparge medium with 80% N2 and 20% CO2 gas mixture for 30 – 45 min to make it anoxic.", "source_locator": "page 1, main preparation paragraph", "preparation_stage": "initial anoxic preparation", "decision_rationale": "The source specifies 30–45 min; preserve the interval without choosing a midpoint.", "evidence_id": "quantity-54"}, {"field_path": "preparation_steps.addition_stock_gas", "name": "Gas for separate addition stocks", "current": null, "decision": "add", "source_key": "dsmz165", "source_quote": "prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared", "source_locator": "page 1, main preparation paragraph", "preparation_stage": "cellobiose/vitamin/cysteine/sulfide stock preparation", "decision_rationale": "The specified stocks are prepared under 100% N2; the separately qualified carbonate stock has a different atmosphere.", "evidence_id": "quantity-55"}, {"field_path": "preparation_steps.carbonate_stock_gas", "name": "Gas for carbonate stock", "current": null, "decision": "add", "source_key": "dsmz165", "source_quote": "under 80% N2 and 20% CO2 gas mixture. Cellobiose and vitamins have to be sterilized by", "source_locator": "page 1, main preparation paragraph", "preparation_stage": "carbonate stock preparation", "decision_rationale": "Preserve the separate carbonate-stock preparation under 80% N2 / 20% CO2; do not transfer the 100% N2 instruction from the preceding stocks.", "evidence_id": "quantity-56"}]

### Claim-level source support and actual reference-check coverage

evidence: concern. Targets: CultureMech:004192.

No reviewed layer has claim-level quantity evidence. The target reference check performed zero evidence checks. This review supplies exact raw snippets and stable locators from the bound original captures; references, stock-dose evidence and ingredient evidence should be added in their existing schema locations only during separate curation.

### Bounded biological claims and optional entities

scope: not_applicable. Targets: CultureMech:004192.

No reviewed layer asserts organism/strain identifiers, assemblies, DOI/PMID papers, growth outcomes or KG-Microbe matches. Catalog source names and generic cultivation applications do not establish strain-specific growth. Source formulation alternatives are assessed separately without adding organisms or inventing evidence.

## Findings

### f1: Five stocks are flattened and dilute acid volume becomes mass concentration

blocker / open / confirmed; issue key: cm004192-stock-stage-and-acid-units.

The source adds stocks at 75, 75, 10, 20 and 1 mL, but the target and owners encode their undiluted component strengths as direct ingredients. Four rows sum different stock values (NaCl 0.59+1, MgSO4 heptahydrate 1.2+3, calcium chloride dihydrate 0.72+0.1, FeSO4 heptahydrate 0.1+1). Most conspicuously, 1000 mL H2SO4 at 0.1 N within the ferrous stock becomes 1000 g/L direct acid. The 49 source rows plus two unquantified additions preserve exact stages and units; provider 1001 mL and listed-liquid 1001.5 mL remain distinct.

### f2: Nickel hydrate and sodium indicator identities disagree with source forms

major / open / confirmed; issue key: cm004192-salt-hydrate-grounding.

NiCl2 x 6 H2O maps to nickel dichloride without waters, and Sodium resazurin maps to neutral Resazurin without sodium. Label validation and MIM coverage cannot resolve these form mismatches.

### f3: Preparation and the alternative carbon-source branch are omitted

major / open / confirmed; issue key: cm004192-preparation-and-carbon-branch-lost.

The generated target and KOMODO owner omit the exact anoxic and differential sterilization sequence, mineral-stock pH adjustment and ferrous-stock freshness retained by the DSMZ owner. They also weaken cellulose-as-an-alternative-to-cellobiose into a generic optional row, retain an incompatible Aerobic: Yes note, and reduce the pH range to one endpoint. The source catalog classification flags disagree, so branch-specific composition type also needs reassessment rather than a forced replacement.

### f4: Four inherited timestamp instances are malformed or timezone-naive

minor / open / confirmed; issue key: cm004192-history-timezones.

The target and KOMODO owner each contain one malformed .fZ import timestamp and one timezone-naive resolver timestamp. DSMZ owner history is valid and timezone-aware. No timezone is inferred for older values.

## Recommended Actions And Acceptance Checks

### a1

Restore all five stocks and their exact doses; keep dilute acid solvent normality/volume, original source forms and stock-specific amounts separate. Recalculate any receiving-medium concentration only after its volume basis is explicitly resolved, and attach narrow evidence before authorized regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Verify and align exact supplied-form identifiers in both maintained owners, retaining source masses and qualifiers; do not invent replacement IDs or anhydrous-to-hydrate conversions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the complete source preparation and explicit carbon-source substitution, reconcile the catalog aerobic note, retain stage-specific pH and assess composition type for the documented branch. Preview current formulation-aware merging so unlike source assertions are not silently collapsed.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve append-only history while documenting the unresolved historical timezone and improving future timestamp emission only under separate authorization.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch015/143/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch015/143/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| source-catalog | /private/tmp/culturemech-review-work-batch015/source-preflight-bound/143/source-catalog.json; Complete bound per-record catalog, raw/text/metadata hashes and actual original capture times | context_only | [{"key": "komodoMediaList", "url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList", "status": 200, "accessed_at": "2026-10-19T23:42:38.189631Z", "sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a", "metadata_sha256": "30928bcdb2a03f00076baf3d9b9ac299b82966aeb81f08b2b71f21d0d0bcffb5", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/140/komodoMediaList.json"}, {"key": "dsmz165", "url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf", "status": 200, "accessed_at": "2026-10-21T09:46:49.704361Z", "sha256": "d9fb409f692ec6f6dee9a2dc6def7d9cb3e6817d80d3a94684c98740c2dc6f87", "metadata_sha256": "77b9c62706e539ae0213e8d0d8b99efb19fd75837a1912fedc504c80018f66b0", "content_limit": null, "reused_capture_from": null}, {"key": "mediadive165api", "url": "https://mediadive.dsmz.de/rest/medium/165", "status": 200, "accessed_at": "2026-10-21T09:46:48.818058Z", "sha256": "aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2", "metadata_sha256": "c609b5f6bde5688045f285a9232382cb7670536b10e0257a30ea564a8643f6b6", "content_limit": null, "reused_capture_from": null}, {"key": "chebi131361", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361", "status": 200, "accessed_at": "2026-10-21T07:33:27.980786Z", "sha256": "643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10", "metadata_sha256": "5d44d78951b5b99db68dfdd05054154c671875341a46403fdc8d27437540ddb1", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi131361.json"}, {"key": "chebi131527", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527", "status": 200, "accessed_at": "2026-10-20T07:22:08.349487Z", "sha256": "349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3", "metadata_sha256": "aba7fec29187e4c7bc3a8a54feeedbb3806ec0426ce879dbd520a44a35468d79", "content_limit": "Identity/provenance and exact identifier metadata only; no operational formulation or culture-procedure assessment.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/139/chebi131527.json"}, {"key": "chebi15940", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940", "status": 200, "accessed_at": "2026-10-20T06:55:11.874279Z", "sha256": "3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1", "metadata_sha256": "278ba834982df08ae7c95c23b926035d15f9042dc4e44ffb88d50e2a0ebd4a3a", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15940.json"}, {"key": "chebi15956", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956", "status": 200, "accessed_at": "2026-10-21T08:42:30.425993Z", "sha256": "d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd", "metadata_sha256": "0da9b84b7103b8ff5cafc029c9c6659c18d1443961c6c1e08777f11bffd97c5b", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15956.json"}, {"key": "chebi16494", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494", "status": 200, "accessed_at": "2026-10-20T06:55:13.001958Z", "sha256": "aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1", "metadata_sha256": "38201a72db2e1cd4730248b9f9b2cc30446eeadb363aa164541dc5bda3842eca", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/129/chebi16494.json"}, {"key": "chebi17015", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015", "status": 200, "accessed_at": "2026-10-20T06:55:11.583596Z", "sha256": "f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4", "metadata_sha256": "b174d58ee7a958d55e27e18fdf27f848d5fde113702d1d09f473be6cda5ea8a5", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi17015.json"}, {"key": "chebi17057", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057", "status": 200, "accessed_at": "2026-10-21T09:27:39.796651Z", "sha256": "3548f79d3274a33683125152944998cffa00bd4fce774c8d872db9003222ed06", "metadata_sha256": "e419fc989c1340514749cb79f20ed3a81c93ce9f6ecf2254c32a23604fae594f", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/133/chebi17057.json"}, {"key": "chebi176843", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843", "status": 200, "accessed_at": "2026-10-21T08:17:26.997779Z", "sha256": "b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9", "metadata_sha256": "859d21e6b301f60e533507c16b7f0f85177f0cc295bb35589e692ce6407cf6f0", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi176843.json"}, {"key": "chebi18246", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18246", "status": 200, "accessed_at": "2026-10-21T09:46:50.902901Z", "sha256": "f7abaf5dd620c7de0e80d8e5718cbab4fa7a6455577d0a176847d4e8829be90c", "metadata_sha256": "4fdf55bc4468100dc2f3e75e26fa45e05404dd3e495008c4f207db579be7e80a", "content_limit": null, "reused_capture_from": null}, {"key": "chebi26710", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710", "status": 200, "accessed_at": "2026-10-21T08:42:42.219040Z", "sha256": "2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e", "metadata_sha256": "e0382f73927eabf48723fea9777a995e4bfa23ab150b3001948cfcfffc60cf95", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi26710.json"}, {"key": "chebi26836", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836", "status": 200, "accessed_at": "2026-10-20T07:29:13.222926Z", "sha256": "19e202cd697eed2be3130d5b0b29cc0c1d18575ad103110877303ee678779737", "metadata_sha256": "fb7282192b913ddd73c808d7b751c3a508689bd8601894cd945f264a1228f4dd", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/132/chebi26836.json"}, {"key": "chebi27470", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470", "status": 200, "accessed_at": "2026-10-20T06:55:10.450814Z", "sha256": "fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f", "metadata_sha256": "9e8e57c5284b980b5aa17435d9505822ebd06e287db0bf493ea8920154d9cf6a", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi27470.json"}, {"key": "chebi29377", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377", "status": 200, "accessed_at": "2026-10-21T07:31:16.500548Z", "sha256": "21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1", "metadata_sha256": "77182343b05bacc1609ae5c11cc2089160d43fa53fb520181dcea1f5d3402106", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/133/chebi29377.json"}, {"key": "chebi30753", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753", "status": 200, "accessed_at": "2026-10-20T06:55:12.829785Z", "sha256": "97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a", "metadata_sha256": "fb67c8541d62fb8bd8ae6ea3a09093bbc436b3e1e7b66a85873057066111e61c", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi30753.json"}, {"key": "chebi30961", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961", "status": 200, "accessed_at": "2026-10-21T08:42:44.571163Z", "sha256": "f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d", "metadata_sha256": "3536eeeda597cc3f7d3801c48cb4cf60e25acd9eccfd2ac09a70480f3e807498", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi30961.json"}, {"key": "chebi31345", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345", "status": 200, "accessed_at": "2026-10-20T06:55:12.450283Z", "sha256": "56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d", "metadata_sha256": "416294de70d6830383c166ab53a10432a014f76693d277eb0fc6ec5d79281596", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi31345.json"}, {"key": "chebi31440", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440", "status": 200, "accessed_at": "2026-10-21T08:17:28.489501Z", "sha256": "e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9", "metadata_sha256": "12ee42b288c244804759ab710c027ddb0c6c9e84ea74fb3143ebfb10b55d0c3e", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi31440.json"}, {"key": "chebi31795", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795", "status": 200, "accessed_at": "2026-10-21T08:42:45.232212Z", "sha256": "45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb", "metadata_sha256": "87aa39e726d0dfb956224cc3184e7f2c1be3a6321fe87f9970f63a887d7b4713", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/140/chebi31795.json"}, {"key": "chebi32312", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312", "status": 200, "accessed_at": "2026-10-21T08:17:28.879505Z", "sha256": "eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9", "metadata_sha256": "dbd95f34340e0738d58dade746941220627116ed30e84e78d0dadd929d4a152e", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi32312.json"}, {"key": "chebi33118", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118", "status": 200, "accessed_at": "2026-10-21T08:17:29.364390Z", "sha256": "f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87", "metadata_sha256": "9823d8f911fabf1b9c9d90b526371b4c6e7530b655a124021f4b63fbec2f6df3", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi33118.json"}, {"key": "chebi34887", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887", "status": 200, "accessed_at": "2026-10-21T08:04:44.093348Z", "sha256": "f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc", "metadata_sha256": "a062ba8057ab64ce0563bbf34b48539314d319ed573a2dd021e96e8eb7ebc0e2", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi34887.json"}, {"key": "chebi44557", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557", "status": 200, "accessed_at": "2026-10-21T08:46:15.250117Z", "sha256": "de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2", "metadata_sha256": "95bb74bc642b7d04229226a2c41b9753c003b85dc3cb555e91877f9c9c38faca", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi44557.json"}, {"key": "chebi49105", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105", "status": 200, "accessed_at": "2026-10-20T06:55:10.911379Z", "sha256": "0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4", "metadata_sha256": "b91259f77f726aa843dfe458caf0385142a7ee96b6d2ff44962e8a6216900df0", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi49105.json"}, {"key": "chebi62946", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946", "status": 200, "accessed_at": "2026-10-21T08:43:02.566401Z", "sha256": "10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5", "metadata_sha256": "a1e2087355e82043f5be7288ebed6f8ab8cbfdebd53011232aef45e19175eec5", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/128/chebi62946.json"}, {"key": "chebi63036", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036", "status": 200, "accessed_at": "2026-10-21T08:17:29.666916Z", "sha256": "48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3", "metadata_sha256": "5cd56ae554a6253e89c1c4d59c748a4d8317e4d50f36ed7630254546676fb064", "content_limit": "Identity/provenance and exact identifier metadata only; no operational formulation or culture-procedure assessment.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/139/chebi63036.json"}, {"key": "chebi63939", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939", "status": 200, "accessed_at": "2026-10-20T06:55:09.796192Z", "sha256": "987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a", "metadata_sha256": "8c032341c1a6b15dac7678091c6975c069edebe9da22033b56f1def86e880ddd", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi63939.json"}, {"key": "chebi75213", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213", "status": 200, "accessed_at": "2026-10-21T08:17:29.756647Z", "sha256": "b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083", "metadata_sha256": "b1c20b370483e053434ad0326c01e497cd8bfffd8f35c39849a7f13c51c0d917", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/136/chebi75213.json"}, {"key": "chebi75836", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836", "status": 200, "accessed_at": "2026-10-20T06:55:07.038393Z", "sha256": "14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525", "metadata_sha256": "a67ef16d6982948181b6ffcaa5b7fb60f01395984f15dbcef47d22b89f3b0742", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi75836.json"}, {"key": "chebi76209", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209", "status": 200, "accessed_at": "2026-10-20T06:55:04.847843Z", "sha256": "f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c", "metadata_sha256": "dc171ad292a4aa60637997f5ea8e33445dd20bece656874532f77ef2a8ed042f", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi76209.json"}, {"key": "chebi86158", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158", "status": 200, "accessed_at": "2026-10-21T08:17:30.011607Z", "sha256": "b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61", "metadata_sha256": "5f2731864627245c55ffd72fece700a4c38708d4e012db3f84fed6082bd5b8db", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi86158.json"}, {"key": "chebi86364", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364", "status": 200, "accessed_at": "2026-10-21T07:33:35.036768Z", "sha256": "f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069", "metadata_sha256": "56ac3d72114b46620bb2e8c277cfc2a4e64eb2bc6d44627ca2c89f9d6f5d50a7", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/134/chebi86364.json"}, {"key": "chebi86465", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465", "status": 200, "accessed_at": "2026-10-20T06:55:08.054799Z", "sha256": "5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c", "metadata_sha256": "c59ef7887fb48413e94272e2b074ec89f12a16f7b3e50ba4331369294f4c8a0d", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi86465.json"}, {"key": "chebi8806", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806", "status": 200, "accessed_at": "2026-10-21T08:17:30.774007Z", "sha256": "e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5", "metadata_sha256": "dcd51a6da87370a91395f3c0583d8632b494b3f441318d9106664896fc5dc1e7", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi8806.json"}, {"key": "chebi91244", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244", "status": 200, "accessed_at": "2026-10-20T06:55:07.079384Z", "sha256": "dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa", "metadata_sha256": "b6b1af84fbd1f1f98a674c7b3d3439d2bd5207f16cf1ac6d6541f935b63016f9", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-work-batch004/sources/chebi91244.json"}, {"key": "chebi91248", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248", "status": 200, "accessed_at": "2026-10-21T08:42:32.136441Z", "sha256": "7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683", "metadata_sha256": "77ade3f6455526983b08c040e632f2ab50a091385f21a60e8a2a7fb278a5ac89", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/133/chebi91248.json"}] |
| dsmz165 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf; pages 1–2, complete main recipe and five stock sections | supports | DSMZ 165 ACETIVIBRIO CELLULOLYTICUS MEDIUM, two-page collection recipe. Both pages were inspected visually and in extracted text, including the acid normality, five stock definitions, cellulose alternatives and preparation. Footer ©2022 DSMZ is preserved without inventing individual authors or a separately verified publication date. |
| mediadive165api | https://mediadive.dsmz.de/rest/medium/165; $.data.medium; $.data.solutions[0:6] | supports | Exact MediaDive medium 165 response, main 283 and stocks 284/285/241/5861/5980, with all amounts, stock doses, declared volumes, optional flag and source-specific preparation. |
| komodoMediaList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; MediaList table row with first cell 165 | context_only | Exact KOMODO row 165 links DSMZ Medium165.pdf, gives pH 7.2 and Aerobic=true, and has is_complex=false. These catalog fields are preserved as provenance and compared with the primary; they are not organism phenotypes or independent formulation evidence. |
| quantity-1 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[0].recipe[0] | supports | The main recipe explicitly adds 75 ml of stock 284. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution. |
| quantity-2 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[0].recipe[1] | supports | The main recipe explicitly adds 75 ml of stock 285. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution. |
| quantity-3 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[0].recipe[2] | supports | The main recipe explicitly adds 10 ml of stock 241. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution. |
| quantity-4 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[0].recipe[3] | supports | The main recipe explicitly adds 20 ml of stock 5861. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution. |
| quantity-5 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[0].recipe[4] | supports | The current value follows provider g_l on its declared 1001 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-6 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[0].recipe[5] | supports | The current value follows provider g_l on its declared 1001 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-7 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[0].recipe[6] | supports | The current value follows provider g_l on its declared 1001 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-8 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[0].recipe[7] | context_only | The source gives cellulose 3 g as an alternative to cellobiose, not an extra carbon source added to the same selected recipe. Retain the source amount and grade/alternative condition; provider g_l 2.997 follows its declared 1001 mL basis. |
| quantity-9 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[0].recipe[8] | supports | The main recipe explicitly adds 1 ml of stock 5980. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution. |
| quantity-10 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[0].recipe[9] | supports | The current value follows provider g_l on its declared 1001 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-11 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[0].recipe[10] | supports | The current value follows provider g_l on its declared 1001 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-12 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[0].recipe[11] | supports | Preserve the source solvent quantity 820 ml in its own stage. The provider declares this solution volume as 1001 mL; water addition is not independent proof of measured final volume. |
| quantity-13 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[1].recipe[0] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-14 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[1].recipe[1] | supports | Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume. |
| quantity-15 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[2].recipe[0] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-16 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[2].recipe[1] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-17 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[2].recipe[2] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-18 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[2].recipe[3] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-19 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[2].recipe[4] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-20 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[2].recipe[5] | supports | Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume. |
| quantity-21 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[0] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-22 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[1] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-23 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[2] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-24 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[3] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-25 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[4] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-26 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[5] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-27 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[6] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-28 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[7] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-29 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[8] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-30 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[9] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-31 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[10] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-32 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[11] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-33 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[12] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-34 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[13] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-35 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[14] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-36 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[3].recipe[15] | supports | Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume. |
| quantity-37 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[4].recipe[0] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-38 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[4].recipe[1] | context_only | The exact row is 1000 mL of 0.1 N H2SO4 in the ferrous sulfate stock. Local 1000 G_PER_L is a liquid-volume-to-mass-unit error and a stage error. Retain the dilute acid solvent and its normality; do not treat it as neat acid or infer density. |
| quantity-39 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[5].recipe[0] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-40 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[5].recipe[1] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-41 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[5].recipe[2] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-42 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[5].recipe[3] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-43 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[5].recipe[4] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-44 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[5].recipe[5] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-45 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[5].recipe[6] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-46 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[5].recipe[7] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-47 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[5].recipe[8] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-48 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[5].recipe[9] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-49 | https://mediadive.dsmz.de/rest/medium/165; $.data.solutions[5].recipe[10] | supports | Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume. |
| quantity-50 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf; page 2, Modified Wolin mineral stock preparation | supports | Source adjusts pH to 6.5 and then 7.0 with KOH without specifying a fixed amount. Do not fill that absence with zero or a guessed dose. |
| quantity-51 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf; page 1, main preparation paragraph | supports | Cellobiose, vitamins, cysteine, sulfide and carbonate have stated ingredient amounts, but not all later stock volumes are specified. Their sterile/anoxic handling and separate gas atmospheres cannot establish a measured final volume. |
| quantity-52 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf; page 1, main preparation paragraph | context_only | Target pH 7.2 is a permitted endpoint, but the exact source and DSMZ owner specify the complete-medium range 7.2–7.4. Preserve its scope and range rather than replacing it with a midpoint. |
| quantity-53 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf; page 1, main preparation paragraph | supports | Preserve the source 80% N2 / 20% CO2 gas mixture as preparation context, not an organism phenotype. |
| quantity-54 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf; page 1, main preparation paragraph | supports | The source specifies 30–45 min; preserve the interval without choosing a midpoint. |
| quantity-55 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf; page 1, main preparation paragraph | supports | The specified stocks are prepared under 100% N2; the separately qualified carbonate stock has a different atmosphere. |
| quantity-56 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf; page 1, main preparation paragraph | supports | Preserve the separate carbonate-stock preparation under 80% N2 / 20% CO2; do not transfer the 100% N2 instruction from the preceding stocks. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; $._embedded.terms[0] | supports | CHEBI:8806 resolves to Resazurin and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; $._embedded.terms[0] | supports | CHEBI:29377 resolves to sodium carbonate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi17057 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057; $._embedded.terms[0] | supports | CHEBI:17057 resolves to cellobiose and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi18246 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18246; $._embedded.terms[0] | supports | CHEBI:18246 resolves to (1-&gt;4)-beta-D-glucan and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; $._embedded.terms[0] | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; $._embedded.terms[0] | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0] | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0] | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; $._embedded.terms[0] | supports | CHEBI:62946 resolves to ammonium sulfate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0] | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0] | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0] | supports | CHEBI:86158 resolves to calcium chloride dihydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; $._embedded.terms[0] | supports | CHEBI:44557 resolves to nitrilotriacetic acid and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; $._embedded.terms[0] | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; $._embedded.terms[0] | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; $._embedded.terms[0] | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; $._embedded.terms[0] | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; $._embedded.terms[0] | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; $._embedded.terms[0] | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0] | supports | CHEBI:33118 resolves to boric acid and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0] | supports | CHEBI:75213 resolves to sodium molybdate dihydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0] | supports | CHEBI:34887 resolves to nickel dichloride and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; $._embedded.terms[0] | supports | CHEBI:131361 resolves to disodium selenite pentahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; $._embedded.terms[0] | supports | CHEBI:63939 resolves to sodium tungstate dihydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi26836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836; $._embedded.terms[0] | supports | CHEBI:26836 resolves to sulfuric acid and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; $._embedded.terms[0] | supports | CHEBI:15956 resolves to biotin and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; $._embedded.terms[0] | supports | CHEBI:27470 resolves to folic acid and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; $._embedded.terms[0] | supports | CHEBI:30961 resolves to pyridoxine hydrochloride and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; $._embedded.terms[0] | supports | CHEBI:49105 resolves to thiamine hydrochloride and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; $._embedded.terms[0] | supports | CHEBI:17015 resolves to riboflavin and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; $._embedded.terms[0] | supports | CHEBI:15940 resolves to nicotinic acid and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; $._embedded.terms[0] | supports | CHEBI:31345 resolves to Calcium pantothenate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; $._embedded.terms[0] | supports | CHEBI:176843 resolves to vitamin B12 and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; $._embedded.terms[0] | supports | CHEBI:30753 resolves to 4-aminobenzoic acid and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; $._embedded.terms[0] | supports | CHEBI:16494 resolves to lipoic acid and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned snapshot; exact MAPPED/preferred_term rows for asserted CHEBI keys and exact legacy-key lookup | supports | {"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count": 9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id", "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"}, "counts": {"target": {"ingredient_instances": 35, "primary_CHEBI_instances": 35, "secondary_current_asserted_instances": 33, "secondary_current_verified_instances": 33, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 100.0, "secondary_verified_percent": 94.29}, "owner-0": {"ingredient_instances": 35, "primary_CHEBI_instances": 35, "secondary_current_asserted_instances": 33, "secondary_current_verified_instances": 33, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 100.0, "secondary_verified_percent": 94.29}, "owner-1": {"ingredient_instances": 35, "primary_CHEBI_instances": 35, "secondary_current_asserted_instances": 33, "secondary_current_verified_instances": 33, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 100.0, "secondary_verified_percent": 94.29}}, "instances": [{"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[0]", "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806", "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3", "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"], "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]}, "synonyms": ["Resazurin"]}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[1]", "name": "Na2CO3", "primary": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "canonical_label": "sodium carbonate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:497-19-8", "ppdb:594"], "generalized_empirical_formula": ["CO3.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:29377"], "inchi_key_string": ["CDBYLPFSWZWCQE-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/CH2O3.2Na/c2-1(3)4;;/h(H2,2,3,4);;/q;2*+1/p-2"], "mass": ["105.988"], "monoisotopic_mass": ["105.96428"], "smiles_string": ["O=C([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2CO3", "Natriumkarbonat", "disodium carbonate", "disodium trioxidocarbonate", "disodium trioxidocarbonate", "sodium carbonate", "sodium carbonate"], "secondary": {"asserted": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "exact_current_rows": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[2]", "name": "Cellobiose", "primary": {"id": "CHEBI:17057", "label": "cellobiose"}, "canonical_label": "cellobiose", "label_equal": true, "definition": ["A glycosylglucose consisting of two glucose units linked via a β(1→4) bond."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1292744", "cas:528-50-7", "drugbank:DB02061", "kegg.compound:C00185", "knapsack:C00001134", "pubmed:19669625", "pubmed:19968554", "wikipedia.en:Cellobiose"], "generalized_empirical_formula": ["C12H22O11"], "has_alternative_id": ["CHEBI:13952", "CHEBI:23061", "CHEBI:28108", "CHEBI:3522"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17057"], "inchi_key_string": ["GUBGYTABKSRVRQ-CUHNMECISA-N"], "inchi_string": ["InChI=1S/C12H22O11/c13-1-3-5(15)6(16)9(19)12(22-3)23-10-4(2-14)21-11(20)8(18)7(10)17/h3-20H,1-2H2/t3-,4-,5-,6+,7-,8-,9-,10-,11?,12+/m1/s1"], "mass": ["342.297"], "monoisotopic_mass": ["342.11621"], "smiles_string": ["OC[C@H]1O[C@@H](O[C@H]2[C@H](O)[C@@H](O)C(O)O[C@@H]2CO)[C@H](O)[C@@H](O)[C@@H]1O"], "wurcs_representation": ["WURCS=2.0/2,2,1/[a2122h-1x_1-5][a2122h-1b_1-5]/1-2/a4-b1"]}, "synonyms": ["1-beta-D-Glucopyranosyl-4-D-glucopyranose", "4-(beta-D-glucosido)-D-glucose", "4-O-beta-D-glucopyranosyl-D-glucopyranose", "4-beta-D-glucopyranosyl-D-glucopyranose", "Cellobiose", "D-(+)-cellobiose", "D-celiobiose", "D-cellobiose", "D-glucosyl-beta-(1-4)-D-glucose", "beta-D-glucopyranosyl-(1-&gt;4)-D-glucopyranose", "beta-D-glucopyranosyl-(1-&gt;4)-D-glucopyranose", "cellose"], "secondary": {"asserted": {"id": "CHEBI:17057", "label": "cellobiose"}, "exact_current_rows": [{"label": "Cellobiose", "match_type": "preferred_term", "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[3]", "name": "Cellulose", "primary": {"id": "CHEBI:18246", "label": "(1-&gt;4)-beta-D-glucan"}, "canonical_label": "(1-&gt;4)-beta-D-glucan", "label_equal": true, "definition": ["A β-&lt;small&gt;D&lt;/small&gt;-glucan in which the glucose units are connected by (1→4) linkages."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:9004-34-6", "hmdb:HMDB0006944", "kegg.compound:C00760", "kegg.drug:D00093", "kegg.glycan:G10481"], "generalized_empirical_formula": ["(C6H10O5)n.H2O"], "has_alternative_id": ["CHEBI:10812", "CHEBI:23063", "CHEBI:3529"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:18246"], "inchi_key_string": ["WQZGKKKJIJFFOK-VFUOTHLCSA-N"], "inchi_string": ["InChI=1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5-,6-/m1/s1"], "mass": ["180.156"], "monoisotopic_mass": ["180.06339"], "smiles_string": ["[H]O[C@@H]1O[C@H](CO)[C@@H](O)[C@H](O)[C@H]1O"], "wurcs_representation": ["WURCS=2.0/1,1,0/[a2122h-1b_1-5]/1/"]}, "synonyms": ["(1,4-beta-D-Glucosyl)n", "(1,4-beta-D-Glucosyl)n+1", "(1,4-beta-D-Glucosyl)n-1", "(1,4-beta-D-glucosyl)(n)", "(1,4-beta-D-glucosyl)n", "(1-&gt;4)-beta-D-glucopyranan", "(1-&gt;4)-beta-D-glucopyranan", "1,4-beta-D-Glucan", "Cellulose"], "secondary": {"asserted": {"id": "CHEBI:18246", "label": "(1-&gt;4)-beta-D-glucan"}, "exact_current_rows": [{"label": "Cellulose", "match_type": "preferred_term", "identifier": "CHEBI:18246", "preferred_term": "Cellulose", "ontology_id": "CHEBI:18246", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[4]", "name": "L-Cysteine HCl x H2O", "primary": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride hydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of &lt;small&gt;L&lt;/small&gt;-cysteine hydrochloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326", "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"], "inchi_key_string": ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"], "mass": ["175.637"], "monoisotopic_mass": ["175.00699"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]}, "synonyms": ["(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride monohydrate", "Cysteine hydrochloride", "L-Cysteine monohydrate monochloride", "L-cysteine hydrochloride monohydrate", "L-cysteine hydrochloride--water (1/1)", "L-cysteine hydrochloride--water (1/1)"], "secondary": {"asserted": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "exact_current_rows": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[5]", "name": "Na2S x 9 H2O", "primary": {"id": "CHEBI:76209", "label": "sodium sulfide nonahydrate"}, "canonical_label": "sodium sulfide nonahydrate", "label_equal": true, "definition": ["A hydrate with formula Na&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;S·9H&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;O."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:1313-84-4", "kegg.drug:D09001", "pubmed:19810706", "reaxys:14636099"], "generalized_empirical_formula": ["9H2O.2Na.S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:76209"], "inchi_key_string": ["ZGHLCBJZQLNUAZ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.9H2O.S/h;;9*1H2;/q2*+1;;;;;;;;;;-2"], "mass": ["240.182"], "monoisotopic_mass": ["240.04669"], "smiles_string": ["O.O.O.O.O.O.O.O.O.[Na+].[Na+].[S-2]"]}, "synonyms": ["Na2S.9H2O", "Sodium sulfide (USP)", "disodium sulfide nonahydrate", "disodium sulfide--water (1/9)", "disodium sulfide--water (1/9)", "sodium monosulfide nonahydrate", "sodium monosulfide.9H2O", "sodium sulfide.9H2O"], "secondary": {"asserted": {"id": "CHEBI:76209", "label": "sodium sulfide nonahydrate"}, "exact_current_rows": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[6]", "name": "K2HPO4", "primary": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "canonical_label": "dipotassium hydrogen phosphate", "label_equal": true, "definition": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-11-4", "kegg.compound:C13197", "kegg.drug:D02403", "metacyc.compound:CPD0-2433", "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"], "generalized_empirical_formula": ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131527"], "inchi_key_string": ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "secondary": {"asserted": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "exact_current_rows": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[7]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "canonical_label": "potassium dihydrogen phosphate", "label_equal": true, "definition": ["A potassium salt in which dihydrogen phosphate(1−) is the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"], "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"], "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]}, "synonyms": ["MKP", "Monopotassium dihydrogen phosphate", "Monopotassium monophosphate", "Monopotassium orthophosphate", "Monopotassium phosphate", "Orthophosphoric acid, monopotassium salt", "Phosphoric acid, monopotassium salt", "Phosphoric acid, potassium salt (1:1)", "Potassium acid phosphate", "Potassium dihydrogen orthophosphate", "Potassium dihydrogen phosphate", "Potassium phosphate monobasic", "Potassium phosphate", "Sorensen's potassium phosphate", "potassium dihydrogen phosphate", "potassium dihydrogen phosphate"], "secondary": {"asserted": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "exact_current_rows": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[8]", "name": "(NH4)2SO4", "primary": {"id": "CHEBI:62946", "label": "ammonium sulfate"}, "canonical_label": "ammonium sulfate", "label_equal": true, "definition": ["An inorganic sulfate salt obtained by reaction of sulfuric acid with two equivalents of ammonia. A high-melting (decomposes above 280°C) white solid which is very soluble in water (70.6 g/100 g water at 0°C; 103.8 g/100 g water at 100°C), it is widely used as a fertilizer for alkaline soils."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7783-20-2", "kegg.drug:D08853", "metacyc.compound:NH42SO4", "ppdb:36", "pubmed:20556652", "reaxys:11343144", "wikipedia.en:Ammonium_sulfate"], "generalized_empirical_formula": ["2H4N.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:62946"], "inchi_key_string": ["BFNBIHQBYMNNAN-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2H3N.H2O4S/c;;1-5(2,3)4/h2*1H3;(H2,1,2,3,4)"], "mass": ["132.141"], "monoisotopic_mass": ["132.02048"], "smiles_string": ["O=S(=O)([O-])[O-].[NH4+].[NH4+]"]}, "synonyms": ["(NH4)2SO4", "ammonium sulfate (2:1)", "ammonium sulphate", "diammonium sulfate", "diazanium sulfate", "diazanium sulfate", "mascagnite", "sulfuric acid ammonium salt (1:2)", "sulfuric acid, diammonium salt", "sulphate of ammonia"], "secondary": {"asserted": {"id": "CHEBI:62946", "label": "ammonium sulfate"}, "exact_current_rows": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[9]", "name": "NaCl", "primary": {"id": "CHEBI:26710", "label": "sodium chloride"}, "canonical_label": "sodium chloride", "label_equal": true, "definition": ["An inorganic chloride salt having sodium(1+) as the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula": ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string": ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]}, "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "secondary": {"asserted": {"id": "CHEBI:26710", "label": "sodium chloride"}, "exact_current_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[10]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "canonical_label": "magnesium sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505", "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222", "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"], "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "exact_current_rows": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[11]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "canonical_label": "calcium chloride dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of calcium chloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8", "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"], "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass": ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}, "synonyms": ["CaCl2.2H2O", "Calcium chloride hydrate", "Calcium chloride", "calcium chloride--water (1/2)", "calcium chloride--water (1/2)", "calcium dichloride dihydrate"], "secondary": {"asserted": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "exact_current_rows": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[12]", "name": "Nitrilotriacetic acid", "primary": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "canonical_label": "nitrilotriacetic acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1710776", "cas:139-13-9", "drugbank:DB03040", "gmelin:3726", "kegg.compound:C14695", "pdb-ccd:NTA"], "generalized_empirical_formula": ["C6H9NO6"], "has_alternative_id": ["CHEBI:34889", "CHEBI:44555"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:44557"], "inchi_key_string": ["MGFYIUFZLHCRTH-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"], "mass": ["191.139"], "monoisotopic_mass": ["191.04299"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]}, "synonyms": ["Complexon I", "H3nta", "Komplexon I", "N(CH2-COOH)3", "N,N-bis(carboxymethyl)glycine", "N,N-bis(carboxymethyl)glycine", "NITRILOTRIACETIC ACID", "NTA", "Nitrilotriacetate", "Nitrilotriacetic acid", "Nitrilotriessigsaeure", "Triglycollamic acid", "Trilon A", "alpha,alpha',alpha''-trimethylaminetricarboxylic acid", "nitrilo-2,2',2''-triacetic acid", "tri(carboxymethyl)amine", "triglycine"], "secondary": {"asserted": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "exact_current_rows": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[13]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "canonical_label": "manganese(II) sulfate monohydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of manganese(II) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-96-5", "kegg.drug:D04854", "pubmed:26097037", "reaxys:13153017", "wikipedia.en:Manganese(II)_sulfate"], "generalized_empirical_formula": ["H2O.Mn.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86364"], "inchi_key_string": ["ISPYRSDWRDQNSW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mn.H2O4S.H2O/c;1-5(2,3)4;/h;(H2,1,2,3,4);1H2/q+2;;/p-2"], "mass": ["169.016"], "monoisotopic_mass": ["168.90034"], "smiles_string": ["O.O=S(=O)([O-])[O-].[Mn+2]"]}, "synonyms": ["Manganese sulfate hydrate", "Manganese sulfate monohydrate", "Manganese sulfate", "Manganous sulfate monohydrate", "MnSO4.H2O", "manganese(2+) sulfate monohydrate", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulphate monohydrate", "manganese(II) sulphate monohydrate"], "secondary": {"asserted": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "exact_current_rows": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[14]", "name": "FeSO4 x 7 H2O", "primary": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "canonical_label": "iron(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used)."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]}, "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O", "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"], "secondary": {"asserted": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[15]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "canonical_label": "cobalt(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of cobalt(2+) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10026-24-1", "pubmed:10504146", "pubmed:12187935", "pubmed:12209163", "pubmed:12579202", "pubmed:12948248", "pubmed:2227161", "pubmed:24359163", "pubmed:25896363", "wikipedia.en:Cobalt(II)_sulfate"], "generalized_empirical_formula": ["Co.7H2O.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91244"], "inchi_key_string": ["MEYVLGVRTYSQHI-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Co.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["281.101"], "monoisotopic_mass": ["280.95888"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Co+2]"]}, "synonyms": ["Cobalt monosulfate heptahydrate", "cobalt sulfate heptahydrate", "cobalt(2+) sulfate--water (1/7)", "cobalt(2+) sulfate--water (1/7)", "cobalt(II) sulfate heptahydrate", "cobaltous sulfate heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[16]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "canonical_label": "zinc sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of zinc sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7446-20-0", "gmelin:47216", "kegg.drug:D01081", "wikipedia.en:Zinc_Sulfate"], "generalized_empirical_formula": ["7H2O.O4S.Zn"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32312"], "inchi_key_string": ["RZLVQBNCHSJZPX-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/H2O4S.7H2O.Zn/c1-5(2,3)4;;;;;;;;/h(H2,1,2,3,4);7*1H2;/q;;;;;;;;+2/p-2"], "mass": ["287.558"], "monoisotopic_mass": ["285.95482"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Zn+2]"]}, "synonyms": ["Zinc sulfate", "ZnSO4.7H2O", "zinc sulfate (1:1) heptahydrate", "zinc sulfate heptahydrate (1:1:7)", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate--water (1/7)", "zinc(2+) sulfate--water (1/7)"], "secondary": {"asserted": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "exact_current_rows": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[17]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "canonical_label": "copper(II) sulfate pentahydrate", "label_equal": true, "definition": ["The pentahydrate of copper(2+) sulfate. A bright blue crystalline solid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-99-8", "kegg.drug:D03613", "pubmed:11407502", "pubmed:12209195", "pubmed:12484481", "pubmed:15040745", "pubmed:15607472", "pubmed:15824790", "pubmed:19346702", "pubmed:2002460", "pubmed:20132934", "pubmed:2913309", "pubmed:3351847", "pubmed:7615984", "pubmed:8878264", "pubmed:9521458", "pubmed:9776063", "reaxys:16499970", "wikipedia.en:Copper(II)_sulfate"], "generalized_empirical_formula": ["Cu.5H2O.O4S"], "has_alternative_id": ["CHEBI:121741", "CHEBI:370227"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31440"], "inchi_key_string": ["JZCCFEFSEZPSOG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Cu.H2O4S.5H2O/c;1-5(2,3)4;;;;;/h;(H2,1,2,3,4);5*1H2/q+2;;;;;;/p-2"], "mass": ["249.684"], "monoisotopic_mass": ["248.93415"], "smiles_string": ["O=S(=O)([O-])[O-].[Cu+2].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H]"]}, "synonyms": ["CuSO4.5H2O", "Cupric sulfate", "copper sulphate(5.H2O)", "copper(2+) sulfate (1:1) pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate--water (1/5)", "copper(2+) sulfate--water (1/5)", "copper(II) sulfate, pentahydrate", "cupric sulfate pentahydrate"], "secondary": {"asserted": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "exact_current_rows": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[18]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "canonical_label": "potassium aluminium sulfate dodecahydrate", "label_equal": true, "definition": ["A hydrate resulting from the the formal combination of anhydrous potassium aluminium sulfate with 12 mol eq. of water."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7784-24-9", "reaxys:14851666", "wikipedia.en:Potassium_alum"], "generalized_empirical_formula": ["Al.12H2O.K.2O4S"], "has_alternative_id": ["CHEBI:31192"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86465"], "inchi_key_string": ["GNHOJBNSNUXZQA-UHFFFAOYSA-J"], "inchi_string": ["InChI=1S/Al.K.2H2O4S.12H2O/c;;2*1-5(2,3)4;;;;;;;;;;;;/h;;2*(H2,1,2,3,4);12*1H2/q+3;+1;;;;;;;;;;;;;;/p-4"], "mass": ["474.386"], "monoisotopic_mass": ["473.97548"], "smiles_string": ["O.O.O.O.O.O.O.O.O.O.O.O.O=S(=O)([O-])[O-].O=S(=O)([O-])[O-].[Al+3].[K+]"]}, "synonyms": ["AlK(SO4)2.12H2O", "Aluminum potassium disulfate dodecahydrate", "Aluminum potassium sulfate dodecahydrate", "Kalinite", "Potash alum dodecahydrate", "Potassium alum dodecahydrate", "Potassium aluminum disulfate dodecahydrate", "aluminium potassium sulfate--water (1/12)", "aluminium potassium sulfate--water (1/12)"], "secondary": {"asserted": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "exact_current_rows": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[19]", "name": "H3BO3", "primary": {"id": "CHEBI:33118", "label": "boric acid"}, "canonical_label": "boric acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["bpdb:2136", "cas:10043-35-3", "cas:11113-50-1", "drugcentral:3035", "gmelin:1585", "kegg.compound:C12486", "kegg.drug:D01089", "molbase:1644", "pdb-ccd:BO3", "ppdb:2136"], "generalized_empirical_formula": ["H3BO3"], "has_alternative_id": ["CHEBI:22911", "CHEBI:31299", "CHEBI:41248"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:33118"], "inchi_key_string": ["KGBXLFKZBHKPEV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"], "mass": ["61.833"], "monoisotopic_mass": ["62.01752"], "smiles_string": ["[H]OB(O[H])O[H]"]}, "synonyms": ["B(OH)3", "BORIC ACID", "Boric acid", "H3BO3", "[B(OH)3]", "boric acid", "boron trihydroxide", "orthoboric acid", "trihydroxidoboron", "trihydroxidoboron"], "secondary": {"asserted": {"id": "CHEBI:33118", "label": "boric acid"}, "exact_current_rows": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[20]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "canonical_label": "sodium molybdate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium molybdate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10102-40-6", "pubmed:20645132", "pubmed:20813395", "pubmed:22663766", "pubmed:3382795", "reaxys:19032996", "wikipedia.en:Sodium_molybdate"], "generalized_empirical_formula": ["2H2O.MoO4.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75213"], "inchi_key_string": ["FDEIWTXVNPKYDL-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/Mo.2Na.2H2O.4O/h;;;2*1H2;;;;/q;2*+1;;;;;2*-1"], "mass": ["241.946"], "monoisotopic_mass": ["243.88573"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]}, "synonyms": ["Disodium molybdate dihydrate", "Molybdic acid, disodium salt, dihydrate", "Na2MoO4.2H2O", "Sodium molybdate(VI) dihydrate", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium orthomolybdate dihydrate"], "secondary": {"asserted": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "exact_current_rows": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[21]", "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "canonical_label": "nickel dichloride", "label_equal": true, "definition": ["A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7718-54-9", "kegg.compound:C14711", "pubmed:11739495", "pubmed:12603851", "pubmed:21928331", "pubmed:23179351", "pubmed:23622879", "pubmed:23702803", "pubmed:23735035", "pubmed:7671317", "reaxys:3902827", "reaxys:8128171", "wikipedia.en:Nickel_dichloride"], "generalized_empirical_formula": ["Cl2Ni"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:34887"], "inchi_key_string": ["QMMRZOWCJAIUJA-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"], "mass": ["129.599"], "monoisotopic_mass": ["127.87305"], "smiles_string": ["[Cl][Ni][Cl]"]}, "synonyms": ["NiCl2", "Nickel chloride", "Nickel(II) chloride", "[NiCl2]", "nickel dichloride", "nickel dichloride", "nickel(2+) chloride", "nickel(2+) chloride", "nickel(II) chloride", "nickel(II) chloride", "nickelous chloride"], "secondary": {"asserted": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "exact_current_rows": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[22]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "canonical_label": "disodium selenite pentahydrate", "label_equal": true, "definition": ["A hydrate that is the pentahydrate form of disodium selenite."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:26970-82-1", "pubmed:15259772", "pubmed:15559373", "pubmed:16126997", "pubmed:17873396", "pubmed:24479345", "pubmed:24716537", "reaxys:14666014", "wikipedia.en:Sodium_selenite"], "generalized_empirical_formula": ["5H2O.2Na.O3Se"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131361"], "inchi_key_string": ["TUANAMBRHOLYTH-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"], "mass": ["263.012"], "monoisotopic_mass": ["263.93363"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2SeO3.5H2O", "Selenious acid disodium salt, pentahydrate", "Sodium selenite pentahydrate", "disodium selenite hydrate", "sodium selenite hydrate", "sodium selenite--water (1/5)", "sodium selenite--water (1/5)"], "secondary": {"asserted": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "exact_current_rows": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[23]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "canonical_label": "sodium tungstate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines to nitrones"], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10213-10-2", "reaxys:13157884", "wikipedia.en:Sodium_tungstate"], "generalized_empirical_formula": ["2H2O.2Na.O4W"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63939"], "inchi_key_string": ["WPZFLQRLSGVIAA-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.2H2O.4O.W/h;;2*1H2;;;;;/q2*+1;;;;;2*-1;"], "mass": ["329.846"], "monoisotopic_mass": ["329.93126"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]}, "synonyms": ["Na2WO4.2H2O", "Tungstic acid, sodium salt, dihydrate", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium orthotungstate dihydrate", "sodium tungstate(VI) dihydrate"], "secondary": {"asserted": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "exact_current_rows": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[24]", "name": "H2SO4", "primary": {"id": "CHEBI:26836", "label": "sulfuric acid"}, "canonical_label": "sulfuric acid", "label_equal": true, "definition": ["A sulfur oxoacid that consists of two oxo and two hydroxy groups joined covalently to a central sulfur atom."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7664-93-9", "gmelin:2122", "kegg.compound:C00059", "kegg.drug:D05963", "knapsack:C00007530", "molbase:4", "ppdb:606", "pubmed:13568755", "pubmed:16122922", "pubmed:19397353", "pubmed:22047659", "pubmed:22136045", "pubmed:22204399", "pubmed:22267186", "pubmed:22296037", "pubmed:22364556", "pubmed:22435616", "reaxys:2037554", "wikipedia.en:Sulfuric_acid"], "generalized_empirical_formula": ["H2O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26836"], "inchi_key_string": ["QAOWNCQODCNURD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O4S/c1-5(2,3)4/h(H2,1,2,3,4)"], "mass": ["98.079"], "monoisotopic_mass": ["97.96738"], "smiles_string": ["[H]OS(=O)(=O)O[H]"]}, "synonyms": ["Acide sulfurique", "Acido sulfurico", "Acidum sulfuricum", "H2SO4", "Schwefelsaeureloesungen", "Sulfuric acid", "[S(OH)2O2]", "[SO2(OH)2]", "dihydrogen tetraoxosulfate", "dihydrogen tetraoxosulfate", "dihydroxidodioxidosulfur", "dihydroxidodioxidosulfur", "hydrogen tetraoxosulfate(2-)", "hydrogen tetraoxosulfate(2-)", "hydrogen tetraoxosulfate(VI)", "hydrogen tetraoxosulfate(VI)", "sulfuric acid", "sulfuric acid", "sulphuric acid", "tetraoxosulfuric acid", "tetraoxosulfuric acid"], "secondary": {"asserted": {"id": "CHEBI:26836", "label": "sulfuric acid"}, "exact_current_rows": [{"label": "H2SO4", "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[25]", "name": "Biotin", "primary": {"id": "CHEBI:15956", "label": "biotin"}, "canonical_label": "biotin", "label_equal": true, "definition": ["An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:58-85-5", "chemspider:149962", "drugbank:DB00121", "drugcentral:373", "foodb.food:FDB014510", "gmelin:1918703", "hmdb:HMDB0000030", "kegg.compound:C00120", "kegg.drug:D00029", "knapsack:C00000756", "lincs.smallmolecule:LSM-3994", "metacyc.compound:BIOTIN", "pdb-ccd:BTN", "pmc:PMC8089577", "pubmed:10064317", "pubmed:10215065", "pubmed:10577274", "pubmed:11435506", "pubmed:11481419", "pubmed:11800048", "pubmed:12055344", "pubmed:12070309", "pubmed:12603856", "pubmed:12803839", "pubmed:15012185", "pubmed:15202718", "pubmed:15272000", "pubmed:15690449", "pubmed:15863846", "pubmed:15899401", "pubmed:15992684", "pubmed:16011464", "pubmed:16195795", "pubmed:16419467", "pubmed:16676358", "pubmed:16677798", "pubmed:16704206", "pubmed:16769720", "pubmed:17297119", "pubmed:1814646", "pubmed:18202531", "pubmed:18452485", "pubmed:18509457", "pubmed:19212411", "pubmed:19319844", "pubmed:19727438", "pubmed:19928962", "pubmed:20967359", "pubmed:20974274", "pubmed:2100006", "pubmed:21248194", "pubmed:21356565", "pubmed:21373679", "pubmed:21596550", "pubmed:21871906", "pubmed:25515858", "pubmed:33346513", "pubmed:33461365", "pubmed:34077272", "pubmed:8333586", "pubmed:8750932", "pubmed:9022537", "pubmed:9038855", "pubmed:9094878", "pubmed:9164991", "pubmed:9176832", "pubmed:9371938", "pubmed:9416479", "reaxys:86838", "wikipedia.en:Biotin"], "generalized_empirical_formula": ["C10H16N2O3S"], "has_alternative_id": ["CHEBI:13905", "CHEBI:22882", "CHEBI:22884", "CHEBI:3108", "CHEBI:41236"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15956"], "inchi_key_string": ["YBJHBAHKTGYVGT-ZKWXMUAHSA-N"], "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"], "mass": ["244.316"], "monoisotopic_mass": ["244.08816"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]}, "synonyms": ["(+)-cis-Hexahydro-2-oxo-1H-thieno[3,4]imidazole-4-valeric acid", "(3aS,4S,6aR)-Hexahydro-2-oxo-1H-thieno[3,4-d]imidazole-4-valeric acid", "5-(2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl)pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "BIOTIN", "Coenzyme R", "D-(+)-biotin", "D-Biotin", "Vitamin H", "biotin", "biotina", "biotine", "biotinum", "cis-(+)-Tetrahydro-2-oxothieno[3,4]imidazoline-4-valeric acid", "cis-Hexahydro-2-oxo-1H-thieno(3,4)imidazole-4-valeric acid", "cis-Tetrahydro-2-oxothieno(3,4-d)imidazoline-4-valeric acid", "vitamin B7"], "secondary": {"asserted": {"id": "CHEBI:15956", "label": "biotin"}, "exact_current_rows": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[26]", "name": "Folic acid", "primary": {"id": "CHEBI:27470", "label": "folic acid"}, "canonical_label": "folic acid", "label_equal": true, "definition": ["An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND606960789", "cas:59-30-3", "chemspider:5815", "drugbank:DB00158", "drugcentral:1231", "foodb.food:FDB014504", "hmdb:HMDB0000121", "kegg.compound:C00504", "kegg.drug:D00070", "knapsack:C00001539", "lincs.smallmolecule:LSM-5355", "metacyc.compound:CPD-12826", "pdb-ccd:FOL", "pubmed:10138938", "pubmed:10897644", "pubmed:10958818", "pubmed:11261364", "pubmed:11451208", "pubmed:11959400", "pubmed:14387833", "pubmed:15321809", "pubmed:15523939", "pubmed:15754725", "pubmed:15797531", "pubmed:15797685", "pubmed:15831910", "pubmed:15990733", "pubmed:16093404", "pubmed:16277678", "pubmed:16380297", "pubmed:16871332", "pubmed:17784727", "pubmed:18788725", "pubmed:19121630", "pubmed:19335717", "pubmed:19355913", "pubmed:24650098", "pubmed:33624660", "pubmed:33965562", "pubmed:33968971", "pubmed:34207319", "pubmed:34219855", "pubmed:7738698", "pubmed:8235383", "pubmed:9040515", "pubmed:9420019", "pubmed:9565830", "pubmed:9683174", "pubmed:9781393", "pubmed:9808640", "pubmed:9808641", "reaxys:100781", "wikipedia.en:Folic_Acid"], "generalized_empirical_formula": ["C19H19N7O6"], "has_alternative_id": ["CHEBI:24075", "CHEBI:42610", "CHEBI:5140", "CHEBI:569217"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:27470"], "inchi_key_string": ["OVBPIULPVIDEAO-LBPRGKRZSA-N"], "inchi_string": ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"], "mass": ["441.404"], "monoisotopic_mass": ["441.13968"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]}, "synonyms": ["(2S)-2-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzamido)pentanedioic acid", "Acfol", "Folate", "Folicet", "Folsaeure", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-[(4-{[(2-amino-4-oxo-1,4-dihydropteridin-6-yl)methyl]amino}phenyl)carbonyl]-L-glutamic acid", "N-pteroyl-L-glutamic acid", "PGA", "PteGlu", "acide folique", "acido folico", "acidum folicum", "folic acid", "pteroyl-L-glutamic acid", "pteroyl-L-monoglutamic acid", "pteroylglutamic acid", "pteroylmonoglutamic acid", "vitamin B11", "vitamin B9", "vitamin Bc", "vitamin Be", "vitamin M"], "secondary": {"asserted": {"id": "CHEBI:27470", "label": "folic acid"}, "exact_current_rows": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[27]", "name": "Pyridoxine hydrochloride", "primary": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "canonical_label": "pyridoxine hydrochloride", "label_equal": true, "definition": ["The hydrochloride salt of pyridoxine."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND500675659", "beilstein:3632435", "cas:58-56-0", "drugbank:DBSALT000151", "foodb.food:FDB000575", "gmelin:1067921", "kegg.drug:D02179", "pubmed:15098856", "pubmed:17416572", "pubmed:17891511", "pubmed:18243627", "pubmed:19481898", "pubmed:20645279", "pubmed:21781646", "pubmed:24421551", "pubmed:27468034", "pubmed:28095734", "pubmed:32460509", "pubmed:33209152", "pubmed:33936292", "pubmed:34140989"], "generalized_empirical_formula": ["C8H11NO3.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30961"], "inchi_key_string": ["ZUFQODAHGAHPFQ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H11NO3.ClH/c1-5-8(12)7(4-11)6(3-10)2-9-5;/h2,10-12H,3-4H2,1H3;1H"], "mass": ["205.641"], "monoisotopic_mass": ["205.05057"], "smiles_string": ["Cc1ncc(CO)c(CO)c1O.Cl"]}, "synonyms": ["2-methyl-3-hydroxy-4,5-bis(hydroxymethyl)pyridine hydrochloride", "3-hydroxy-4,5-dimethylol-alpha-picoline hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "5-hydroxy-6-methyl-3,4-pyridinedimethanol hydrochloride", "pyridoxol hydrochloride", "vitamin B6 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "exact_current_rows": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[28]", "name": "Thiamine HCl", "primary": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "canonical_label": "thiamine hydrochloride", "label_equal": true, "definition": ["A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND605711145", "agr:IND606057536", "beilstein:3642937", "beilstein:3851771", "cas:67-03-8", "chemspider:5967", "drugbank:DBSALT000205", "foodb.food:FDB008416", "gmelin:31154", "gmelin:691133", "kegg.drug:D02094", "pubmed:11548854", "pubmed:12224421", "pubmed:21212548", "pubmed:22305197", "pubmed:24399744", "pubmed:25977858", "pubmed:26616989", "pubmed:27163892", "pubmed:28763984", "pubmed:28784494", "pubmed:30131156", "pubmed:31270735", "pubmed:31664290", "pubmed:32009117", "pubmed:32562525", "pubmed:32824791", "reaxys:17124533"], "generalized_empirical_formula": ["C12H17N4OS.Cl.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:49105"], "inchi_key_string": ["DPJRMOMPQZCRJU-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C12H17N4OS.2ClH/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H/q+1;;/p-1"], "mass": ["337.276"], "monoisotopic_mass": ["336.05784"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1.Cl.[Cl-]"]}, "synonyms": ["3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "thiamin dichloride", "thiamin hydrochloride", "thiamine HCl", "thiamine chloride hydrochloride", "thiamine dichloride", "thiamine(2+) dichloride", "thiaminium chloride hydrochloride", "vitamin B1 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "exact_current_rows": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[29]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015", "label": "riboflavin"}, "canonical_label": "riboflavin", "label_equal": true, "definition": ["&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:83-88-5", "chemspider:431981", "drugbank:DB00140", "drugcentral:2834", "foodb.food:FDB012160", "hmdb:HMDB0000244", "kegg.compound:C00255", "kegg.drug:D00050", "knapsack:C00001552", "lincs.smallmolecule:LSM-4084", "metacyc.compound:RIBOFLAVIN", "patent:US2807611", "patent:US2876169", "pdb-ccd:RBF", "pubmed:10566553", "pubmed:11399071", "pubmed:11606856", "pubmed:12083520", "pubmed:12354259", "pubmed:12927541", "pubmed:14963913", "pubmed:16273338", "pubmed:16460756", "pubmed:16658098", "pubmed:182198", "pubmed:18832377", "pubmed:19169240", "pubmed:19212411", "pubmed:19854891", "pubmed:22770225", "pubmed:2369885", "pubmed:23818044", "pubmed:24643482", "pubmed:24816110", "pubmed:25108762", "pubmed:25468971", "pubmed:25887755", "pubmed:2631092", "pubmed:29937405", "pubmed:3142982", "pubmed:33154451", "pubmed:33304888", "pubmed:33886098", "pubmed:33892358", "pubmed:34156642", "pubmed:3592624", "pubmed:3878498", "pubmed:4019261", "pubmed:6475825", "pubmed:6546833", "pubmed:6650303", "pubmed:7101408", "pubmed:7883462", "pubmed:8487103", "pubmed:8604671", "pubmed:8678471", "pubmed:8976642", "pubmed:9184778", "pubmed:9808225", "pubmed:9874201", "reaxys:97831", "wikipedia.en:Riboflavin"], "generalized_empirical_formula": ["C17H20N4O6"], "has_alternative_id": ["CHEBI:15044", "CHEBI:27299", "CHEBI:45214", "CHEBI:529204", "CHEBI:8843"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17015"], "inchi_key_string": ["AUNGANRZJHBGPY-SCRDCRAPSA-N"], "inchi_string": ["InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23)14(25)12(24)6-22)15-13(18-9)16(26)20-17(27)19-15/h3-4,11-12,14,22-25H,5-6H2,1-2H3,(H,20,26,27)/t11-,12+,14-/m0/s1"], "mass": ["376.369"], "monoisotopic_mass": ["376.13828"], "smiles_string": ["Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)CO)c2cc1C"]}, "synonyms": ["1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol", "5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "6,7-dimethyl-9-D-ribitylisoalloxazine", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine", "7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-ribitylisoalloxazine", "Aqua-Flave", "Beflavin", "Beflavine", "Bisulase", "Dermadram", "E101", "Fiboflavin", "Flavaxin", "Flavin Bb", "Flaxain", "Hyflavin", "Vitamin B2", "lactoflavin", "riboflavin (vit B2)", "riboflavin", "riboflavina", "riboflavine", "riboflavinum", "vitamin B2", "vitamin G", "vitasan B2"], "secondary": {"asserted": {"id": "CHEBI:17015", "label": "riboflavin"}, "exact_current_rows": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[30]", "name": "Nicotinic acid", "primary": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "canonical_label": "nicotinic acid", "label_equal": true, "definition": ["A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND607088605", "cas:59-67-6", "chemspider:913", "drugbank:DB00627", "drugcentral:2835", "foodb.food:FDB001014", "gmelin:3340", "hmdb:HMDB0001488", "kegg.compound:C00253", "kegg.drug:D00049", "knapsack:C00000208", "lincs.smallmolecule:LSM-4676", "metacyc.compound:NIACINE", "pdb-ccd:NIO", "pubmed:10540864", "pubmed:113218", "pubmed:12563315", "pubmed:12789870", "pubmed:135660", "pubmed:14550884", "pubmed:15037193", "pubmed:15183629", "pubmed:15205990", "pubmed:15311728", "pubmed:15627518", "pubmed:15651982", "pubmed:16018787", "pubmed:16172771", "pubmed:16322787", "pubmed:16400392", "pubmed:16449845", "pubmed:16767301", "pubmed:16877271", "pubmed:16945375", "pubmed:18037924", "pubmed:182198", "pubmed:186078", "pubmed:18993152", "pubmed:18996527", "pubmed:19369827", "pubmed:19592242", "pubmed:19678716", "pubmed:19779335", "pubmed:20979384", "pubmed:21632263", "pubmed:22116693", "pubmed:22155410", "pubmed:22229411", "pubmed:22366213", "pubmed:22458880", "pubmed:22770225", "pubmed:24029555", "pubmed:24568240", "pubmed:24675661", "pubmed:24848081", "pubmed:24975217", "pubmed:25040591", "pubmed:25241762", "pubmed:25429652", "pubmed:32954525", "pubmed:33273654", "pubmed:33932650", "pubmed:34066686", "pubmed:34085526", "pubmed:34117670", "pubmed:4033386", "pubmed:4259917", "pubmed:582105", "pubmed:699281", "pubmed:7217784", "pubmed:7581845", "pubmed:8306147", "pubmed:8423912", "pubmed:8679452", "pubmed:9107536", "reaxys:109591", "wikipedia.en:Niacin"], "generalized_empirical_formula": ["C6H5NO2"], "has_alternative_id": ["CHEBI:25538", "CHEBI:44319", "CHEBI:7559"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15940"], "inchi_key_string": ["PVNIIMVLHYAWGP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"], "mass": ["123.111"], "monoisotopic_mass": ["123.03203"], "smiles_string": ["O=C(O)c1cccnc1"]}, "synonyms": ["3-Pyridylcarboxylic acid", "3-carboxylpyridine", "3-carboxypyridine", "3-pyridinecarboxylic acid", "NICOTINIC ACID", "NICOTINIC ACID", "Niacin", "Niacor", "Niaspan", "Nicotinic acid", "Nicotinic acid", "Nicotinsaure", "Nikotinsaeure", "P.P. factor", "PP factor", "acide nicotinique", "acido nicotinico", "acidum nicotinicum", "anti-pellagra vitamin", "beta-pyridinecarboxylic acid", "m-pyridinecarboxylic acid", "nicotinic acid", "nicotinic acid", "pellagra preventive factor", "pyridine-3-carboxylic acid", "pyridine-3-carboxylic acid", "pyridine-beta-carboxylic acid", "pyridine-carboxylique-3", "vitamin B3"], "secondary": {"asserted": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "exact_current_rows": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[31]", "name": "Calcium D-(+)-pantothenate", "primary": {"id": "CHEBI:31345", "label": "Calcium pantothenate"}, "canonical_label": "Calcium pantothenate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:137-08-6", "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278", "pubmed:20553011", "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula": ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"], "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"], "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]}, "synonyms": ["Calcium pantotenate", "Calcium pantothenate", "Calcium pantothenate, d-", "Calpan", "D-ca pantothenate", "D-calcium pantothenate", "NSC-36292", "Pantholin", "Pantothenic acid (as calcium)", "Pantothenic acid calcium salt", "Vitamin b5, calcium salt", "pantotenato de calcio", "pantothenate de calcium"]}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[32]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843", "label": "vitamin B12"}, "canonical_label": "vitamin B12", "label_equal": true, "definition": ["Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives)."], "annotations": {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:176843"]}, "synonyms": ["vitamin B-12", "vitamin B12 vitamer", "vitamin B12 vitamers", "vitamin B12", "vitamins B12"], "secondary": {"asserted": {"id": "CHEBI:176843", "label": "vitamin B12"}, "exact_current_rows": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[33]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "canonical_label": "4-aminobenzoic acid", "label_equal": true, "definition": ["An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:150-13-0", "drugbank:DB02362", "drugcentral:2049", "ecmdb:ECMDB01392", "gmelin:50150", "hmdb:HMDB0001392", "kegg.compound:C00568", "kegg.drug:D02456", "knapsack:C00001401", "pdb-ccd:PAB", "pubmed:12039592", "pubmed:14745019", "pubmed:15115392", "pubmed:1527790", "pubmed:16290145", "pubmed:17149871", "pubmed:17743450", "pubmed:17800214", "pubmed:19469519", "pubmed:22767283", "pubmed:22994574", "pubmed:23063996", "pubmed:23084339", "pubmed:23144588", "pubmed:23471007", "pubmed:3599019", "pubmed:3820215", "pubmed:3950915", "pubmed:8411009", "pubmed:9406595", "reaxys:471605", "wikipedia.en:4-Aminobenzoic_acid", "ymdb:YMDB00493"], "generalized_empirical_formula": ["C7H7NO2"], "has_alternative_id": ["CHEBI:113372", "CHEBI:1783", "CHEBI:20315", "CHEBI:44778"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30753"], "inchi_key_string": ["ALYNCZNDIQEVRV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"], "mass": ["137.138"], "monoisotopic_mass": ["137.04768"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]}, "synonyms": ["1-Amino-4-carboxybenzene", "4-AMINOBENZOIC ACID", "4-AMINOBENZOIC ACID", "4-Amino-benzoic acid", "4-Aminobenzoesaeure", "4-Aminobenzoic acid", "4-Aminobenzoic acid", "4-Carboxyaniline", "4-Carboxyphenylamine", "4-aminobenzoic acid", "4-aminobenzoic acid", "ABEE", "PABA", "gamma-Aminobenzoic acid", "gamma-aminobenzoic acid", "p-Aminobenzoesaeure", "p-aminobenzoic acid", "p-carboxyaniline", "p-carboxyphenylamine", "para-aminobenzoic acid"], "secondary": {"asserted": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "exact_current_rows": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[34]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id": "CHEBI:16494", "label": "lipoic acid"}, "canonical_label": "lipoic acid", "label_equal": true, "definition": ["A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:122410", "cas:62-46-4", "drugbank:DB00166", "drugcentral:4732", "ecmdb:ECMDB01451", "gmelin:720915", "kegg.compound:C00725", "kegg.drug:D00086", "pubmed:15328413", "pubmed:7519986", "pubmed:7548757", "reaxys:81853", "wikipedia.en:Lipoic_acid", "ymdb:YMDB00334"], "generalized_empirical_formula": ["C8H14O2S2"], "has_alternative_id": ["CHEBI:146958", "CHEBI:25058", "CHEBI:6492"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16494"], "inchi_key_string": ["AGBQKNBQESQNJD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H14O2S2/c9-8(10)4-2-1-3-7-5-6-11-12-7/h7H,1-6H2,(H,9,10)"], "mass": ["206.332"], "monoisotopic_mass": ["206.04352"], "smiles_string": ["O=C(O)CCCCC1CCSS1"]}, "synonyms": ["1,2-dithiolane-3-pentanoic acid", "1,2-dithiolane-3-valeric acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)valeric acid", "5-(dithiolan-3-yl)valeric acid", "5-[3-(1,2-dithiolanyl)]pentanoic acid", "6,8-thioctic acid", "6,8-thiotic acid", "6-thioctic acid", "6-thiotic acid", "Acetate-replacing factor", "Biletan", "Lipoic acid", "Thioctansaeure", "Thioctic acid", "Thioctsaeure", "Thioktsaeure", "alpha-Lipoic acid", "alpha-Liponsaeure", "alpha-lipoic acid", "liponic acid"], "secondary": {"asserted": {"id": "CHEBI:16494", "label": "lipoic acid"}, "exact_current_rows": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[0]", "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806", "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3", "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"], "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]}, "synonyms": ["Resazurin"]}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[1]", "name": "Na2CO3", "primary": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "canonical_label": "sodium carbonate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:497-19-8", "ppdb:594"], "generalized_empirical_formula": ["CO3.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:29377"], "inchi_key_string": ["CDBYLPFSWZWCQE-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/CH2O3.2Na/c2-1(3)4;;/h(H2,2,3,4);;/q;2*+1/p-2"], "mass": ["105.988"], "monoisotopic_mass": ["105.96428"], "smiles_string": ["O=C([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2CO3", "Natriumkarbonat", "disodium carbonate", "disodium trioxidocarbonate", "disodium trioxidocarbonate", "sodium carbonate", "sodium carbonate"], "secondary": {"asserted": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "exact_current_rows": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[2]", "name": "Cellobiose", "primary": {"id": "CHEBI:17057", "label": "cellobiose"}, "canonical_label": "cellobiose", "label_equal": true, "definition": ["A glycosylglucose consisting of two glucose units linked via a β(1→4) bond."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1292744", "cas:528-50-7", "drugbank:DB02061", "kegg.compound:C00185", "knapsack:C00001134", "pubmed:19669625", "pubmed:19968554", "wikipedia.en:Cellobiose"], "generalized_empirical_formula": ["C12H22O11"], "has_alternative_id": ["CHEBI:13952", "CHEBI:23061", "CHEBI:28108", "CHEBI:3522"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17057"], "inchi_key_string": ["GUBGYTABKSRVRQ-CUHNMECISA-N"], "inchi_string": ["InChI=1S/C12H22O11/c13-1-3-5(15)6(16)9(19)12(22-3)23-10-4(2-14)21-11(20)8(18)7(10)17/h3-20H,1-2H2/t3-,4-,5-,6+,7-,8-,9-,10-,11?,12+/m1/s1"], "mass": ["342.297"], "monoisotopic_mass": ["342.11621"], "smiles_string": ["OC[C@H]1O[C@@H](O[C@H]2[C@H](O)[C@@H](O)C(O)O[C@@H]2CO)[C@H](O)[C@@H](O)[C@@H]1O"], "wurcs_representation": ["WURCS=2.0/2,2,1/[a2122h-1x_1-5][a2122h-1b_1-5]/1-2/a4-b1"]}, "synonyms": ["1-beta-D-Glucopyranosyl-4-D-glucopyranose", "4-(beta-D-glucosido)-D-glucose", "4-O-beta-D-glucopyranosyl-D-glucopyranose", "4-beta-D-glucopyranosyl-D-glucopyranose", "Cellobiose", "D-(+)-cellobiose", "D-celiobiose", "D-cellobiose", "D-glucosyl-beta-(1-4)-D-glucose", "beta-D-glucopyranosyl-(1-&gt;4)-D-glucopyranose", "beta-D-glucopyranosyl-(1-&gt;4)-D-glucopyranose", "cellose"], "secondary": {"asserted": {"id": "CHEBI:17057", "label": "cellobiose"}, "exact_current_rows": [{"label": "Cellobiose", "match_type": "preferred_term", "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[3]", "name": "Cellulose", "primary": {"id": "CHEBI:18246", "label": "(1-&gt;4)-beta-D-glucan"}, "canonical_label": "(1-&gt;4)-beta-D-glucan", "label_equal": true, "definition": ["A β-&lt;small&gt;D&lt;/small&gt;-glucan in which the glucose units are connected by (1→4) linkages."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:9004-34-6", "hmdb:HMDB0006944", "kegg.compound:C00760", "kegg.drug:D00093", "kegg.glycan:G10481"], "generalized_empirical_formula": ["(C6H10O5)n.H2O"], "has_alternative_id": ["CHEBI:10812", "CHEBI:23063", "CHEBI:3529"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:18246"], "inchi_key_string": ["WQZGKKKJIJFFOK-VFUOTHLCSA-N"], "inchi_string": ["InChI=1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5-,6-/m1/s1"], "mass": ["180.156"], "monoisotopic_mass": ["180.06339"], "smiles_string": ["[H]O[C@@H]1O[C@H](CO)[C@@H](O)[C@H](O)[C@H]1O"], "wurcs_representation": ["WURCS=2.0/1,1,0/[a2122h-1b_1-5]/1/"]}, "synonyms": ["(1,4-beta-D-Glucosyl)n", "(1,4-beta-D-Glucosyl)n+1", "(1,4-beta-D-Glucosyl)n-1", "(1,4-beta-D-glucosyl)(n)", "(1,4-beta-D-glucosyl)n", "(1-&gt;4)-beta-D-glucopyranan", "(1-&gt;4)-beta-D-glucopyranan", "1,4-beta-D-Glucan", "Cellulose"], "secondary": {"asserted": {"id": "CHEBI:18246", "label": "(1-&gt;4)-beta-D-glucan"}, "exact_current_rows": [{"label": "Cellulose", "match_type": "preferred_term", "identifier": "CHEBI:18246", "preferred_term": "Cellulose", "ontology_id": "CHEBI:18246", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[4]", "name": "L-Cysteine HCl x H2O", "primary": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride hydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of &lt;small&gt;L&lt;/small&gt;-cysteine hydrochloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326", "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"], "inchi_key_string": ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"], "mass": ["175.637"], "monoisotopic_mass": ["175.00699"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]}, "synonyms": ["(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride monohydrate", "Cysteine hydrochloride", "L-Cysteine monohydrate monochloride", "L-cysteine hydrochloride monohydrate", "L-cysteine hydrochloride--water (1/1)", "L-cysteine hydrochloride--water (1/1)"], "secondary": {"asserted": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "exact_current_rows": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[5]", "name": "Na2S x 9 H2O", "primary": {"id": "CHEBI:76209", "label": "sodium sulfide nonahydrate"}, "canonical_label": "sodium sulfide nonahydrate", "label_equal": true, "definition": ["A hydrate with formula Na&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;S·9H&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;O."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:1313-84-4", "kegg.drug:D09001", "pubmed:19810706", "reaxys:14636099"], "generalized_empirical_formula": ["9H2O.2Na.S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:76209"], "inchi_key_string": ["ZGHLCBJZQLNUAZ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.9H2O.S/h;;9*1H2;/q2*+1;;;;;;;;;;-2"], "mass": ["240.182"], "monoisotopic_mass": ["240.04669"], "smiles_string": ["O.O.O.O.O.O.O.O.O.[Na+].[Na+].[S-2]"]}, "synonyms": ["Na2S.9H2O", "Sodium sulfide (USP)", "disodium sulfide nonahydrate", "disodium sulfide--water (1/9)", "disodium sulfide--water (1/9)", "sodium monosulfide nonahydrate", "sodium monosulfide.9H2O", "sodium sulfide.9H2O"], "secondary": {"asserted": {"id": "CHEBI:76209", "label": "sodium sulfide nonahydrate"}, "exact_current_rows": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[6]", "name": "K2HPO4", "primary": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "canonical_label": "dipotassium hydrogen phosphate", "label_equal": true, "definition": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-11-4", "kegg.compound:C13197", "kegg.drug:D02403", "metacyc.compound:CPD0-2433", "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"], "generalized_empirical_formula": ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131527"], "inchi_key_string": ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "secondary": {"asserted": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "exact_current_rows": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[7]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "canonical_label": "potassium dihydrogen phosphate", "label_equal": true, "definition": ["A potassium salt in which dihydrogen phosphate(1−) is the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"], "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"], "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]}, "synonyms": ["MKP", "Monopotassium dihydrogen phosphate", "Monopotassium monophosphate", "Monopotassium orthophosphate", "Monopotassium phosphate", "Orthophosphoric acid, monopotassium salt", "Phosphoric acid, monopotassium salt", "Phosphoric acid, potassium salt (1:1)", "Potassium acid phosphate", "Potassium dihydrogen orthophosphate", "Potassium dihydrogen phosphate", "Potassium phosphate monobasic", "Potassium phosphate", "Sorensen's potassium phosphate", "potassium dihydrogen phosphate", "potassium dihydrogen phosphate"], "secondary": {"asserted": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "exact_current_rows": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[8]", "name": "(NH4)2SO4", "primary": {"id": "CHEBI:62946", "label": "ammonium sulfate"}, "canonical_label": "ammonium sulfate", "label_equal": true, "definition": ["An inorganic sulfate salt obtained by reaction of sulfuric acid with two equivalents of ammonia. A high-melting (decomposes above 280°C) white solid which is very soluble in water (70.6 g/100 g water at 0°C; 103.8 g/100 g water at 100°C), it is widely used as a fertilizer for alkaline soils."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7783-20-2", "kegg.drug:D08853", "metacyc.compound:NH42SO4", "ppdb:36", "pubmed:20556652", "reaxys:11343144", "wikipedia.en:Ammonium_sulfate"], "generalized_empirical_formula": ["2H4N.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:62946"], "inchi_key_string": ["BFNBIHQBYMNNAN-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2H3N.H2O4S/c;;1-5(2,3)4/h2*1H3;(H2,1,2,3,4)"], "mass": ["132.141"], "monoisotopic_mass": ["132.02048"], "smiles_string": ["O=S(=O)([O-])[O-].[NH4+].[NH4+]"]}, "synonyms": ["(NH4)2SO4", "ammonium sulfate (2:1)", "ammonium sulphate", "diammonium sulfate", "diazanium sulfate", "diazanium sulfate", "mascagnite", "sulfuric acid ammonium salt (1:2)", "sulfuric acid, diammonium salt", "sulphate of ammonia"], "secondary": {"asserted": {"id": "CHEBI:62946", "label": "ammonium sulfate"}, "exact_current_rows": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[9]", "name": "NaCl", "primary": {"id": "CHEBI:26710", "label": "sodium chloride"}, "canonical_label": "sodium chloride", "label_equal": true, "definition": ["An inorganic chloride salt having sodium(1+) as the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula": ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string": ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]}, "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "secondary": {"asserted": {"id": "CHEBI:26710", "label": "sodium chloride"}, "exact_current_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[10]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "canonical_label": "magnesium sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505", "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222", "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"], "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "exact_current_rows": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[11]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "canonical_label": "calcium chloride dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of calcium chloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8", "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"], "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass": ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}, "synonyms": ["CaCl2.2H2O", "Calcium chloride hydrate", "Calcium chloride", "calcium chloride--water (1/2)", "calcium chloride--water (1/2)", "calcium dichloride dihydrate"], "secondary": {"asserted": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "exact_current_rows": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[12]", "name": "Nitrilotriacetic acid", "primary": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "canonical_label": "nitrilotriacetic acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1710776", "cas:139-13-9", "drugbank:DB03040", "gmelin:3726", "kegg.compound:C14695", "pdb-ccd:NTA"], "generalized_empirical_formula": ["C6H9NO6"], "has_alternative_id": ["CHEBI:34889", "CHEBI:44555"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:44557"], "inchi_key_string": ["MGFYIUFZLHCRTH-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"], "mass": ["191.139"], "monoisotopic_mass": ["191.04299"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]}, "synonyms": ["Complexon I", "H3nta", "Komplexon I", "N(CH2-COOH)3", "N,N-bis(carboxymethyl)glycine", "N,N-bis(carboxymethyl)glycine", "NITRILOTRIACETIC ACID", "NTA", "Nitrilotriacetate", "Nitrilotriacetic acid", "Nitrilotriessigsaeure", "Triglycollamic acid", "Trilon A", "alpha,alpha',alpha''-trimethylaminetricarboxylic acid", "nitrilo-2,2',2''-triacetic acid", "tri(carboxymethyl)amine", "triglycine"], "secondary": {"asserted": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "exact_current_rows": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[13]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "canonical_label": "manganese(II) sulfate monohydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of manganese(II) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-96-5", "kegg.drug:D04854", "pubmed:26097037", "reaxys:13153017", "wikipedia.en:Manganese(II)_sulfate"], "generalized_empirical_formula": ["H2O.Mn.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86364"], "inchi_key_string": ["ISPYRSDWRDQNSW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mn.H2O4S.H2O/c;1-5(2,3)4;/h;(H2,1,2,3,4);1H2/q+2;;/p-2"], "mass": ["169.016"], "monoisotopic_mass": ["168.90034"], "smiles_string": ["O.O=S(=O)([O-])[O-].[Mn+2]"]}, "synonyms": ["Manganese sulfate hydrate", "Manganese sulfate monohydrate", "Manganese sulfate", "Manganous sulfate monohydrate", "MnSO4.H2O", "manganese(2+) sulfate monohydrate", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulphate monohydrate", "manganese(II) sulphate monohydrate"], "secondary": {"asserted": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "exact_current_rows": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[14]", "name": "FeSO4 x 7 H2O", "primary": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "canonical_label": "iron(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used)."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]}, "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O", "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"], "secondary": {"asserted": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[15]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "canonical_label": "cobalt(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of cobalt(2+) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10026-24-1", "pubmed:10504146", "pubmed:12187935", "pubmed:12209163", "pubmed:12579202", "pubmed:12948248", "pubmed:2227161", "pubmed:24359163", "pubmed:25896363", "wikipedia.en:Cobalt(II)_sulfate"], "generalized_empirical_formula": ["Co.7H2O.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91244"], "inchi_key_string": ["MEYVLGVRTYSQHI-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Co.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["281.101"], "monoisotopic_mass": ["280.95888"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Co+2]"]}, "synonyms": ["Cobalt monosulfate heptahydrate", "cobalt sulfate heptahydrate", "cobalt(2+) sulfate--water (1/7)", "cobalt(2+) sulfate--water (1/7)", "cobalt(II) sulfate heptahydrate", "cobaltous sulfate heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[16]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "canonical_label": "zinc sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of zinc sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7446-20-0", "gmelin:47216", "kegg.drug:D01081", "wikipedia.en:Zinc_Sulfate"], "generalized_empirical_formula": ["7H2O.O4S.Zn"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32312"], "inchi_key_string": ["RZLVQBNCHSJZPX-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/H2O4S.7H2O.Zn/c1-5(2,3)4;;;;;;;;/h(H2,1,2,3,4);7*1H2;/q;;;;;;;;+2/p-2"], "mass": ["287.558"], "monoisotopic_mass": ["285.95482"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Zn+2]"]}, "synonyms": ["Zinc sulfate", "ZnSO4.7H2O", "zinc sulfate (1:1) heptahydrate", "zinc sulfate heptahydrate (1:1:7)", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate--water (1/7)", "zinc(2+) sulfate--water (1/7)"], "secondary": {"asserted": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "exact_current_rows": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[17]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "canonical_label": "copper(II) sulfate pentahydrate", "label_equal": true, "definition": ["The pentahydrate of copper(2+) sulfate. A bright blue crystalline solid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-99-8", "kegg.drug:D03613", "pubmed:11407502", "pubmed:12209195", "pubmed:12484481", "pubmed:15040745", "pubmed:15607472", "pubmed:15824790", "pubmed:19346702", "pubmed:2002460", "pubmed:20132934", "pubmed:2913309", "pubmed:3351847", "pubmed:7615984", "pubmed:8878264", "pubmed:9521458", "pubmed:9776063", "reaxys:16499970", "wikipedia.en:Copper(II)_sulfate"], "generalized_empirical_formula": ["Cu.5H2O.O4S"], "has_alternative_id": ["CHEBI:121741", "CHEBI:370227"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31440"], "inchi_key_string": ["JZCCFEFSEZPSOG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Cu.H2O4S.5H2O/c;1-5(2,3)4;;;;;/h;(H2,1,2,3,4);5*1H2/q+2;;;;;;/p-2"], "mass": ["249.684"], "monoisotopic_mass": ["248.93415"], "smiles_string": ["O=S(=O)([O-])[O-].[Cu+2].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H]"]}, "synonyms": ["CuSO4.5H2O", "Cupric sulfate", "copper sulphate(5.H2O)", "copper(2+) sulfate (1:1) pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate--water (1/5)", "copper(2+) sulfate--water (1/5)", "copper(II) sulfate, pentahydrate", "cupric sulfate pentahydrate"], "secondary": {"asserted": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "exact_current_rows": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[18]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "canonical_label": "potassium aluminium sulfate dodecahydrate", "label_equal": true, "definition": ["A hydrate resulting from the the formal combination of anhydrous potassium aluminium sulfate with 12 mol eq. of water."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7784-24-9", "reaxys:14851666", "wikipedia.en:Potassium_alum"], "generalized_empirical_formula": ["Al.12H2O.K.2O4S"], "has_alternative_id": ["CHEBI:31192"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86465"], "inchi_key_string": ["GNHOJBNSNUXZQA-UHFFFAOYSA-J"], "inchi_string": ["InChI=1S/Al.K.2H2O4S.12H2O/c;;2*1-5(2,3)4;;;;;;;;;;;;/h;;2*(H2,1,2,3,4);12*1H2/q+3;+1;;;;;;;;;;;;;;/p-4"], "mass": ["474.386"], "monoisotopic_mass": ["473.97548"], "smiles_string": ["O.O.O.O.O.O.O.O.O.O.O.O.O=S(=O)([O-])[O-].O=S(=O)([O-])[O-].[Al+3].[K+]"]}, "synonyms": ["AlK(SO4)2.12H2O", "Aluminum potassium disulfate dodecahydrate", "Aluminum potassium sulfate dodecahydrate", "Kalinite", "Potash alum dodecahydrate", "Potassium alum dodecahydrate", "Potassium aluminum disulfate dodecahydrate", "aluminium potassium sulfate--water (1/12)", "aluminium potassium sulfate--water (1/12)"], "secondary": {"asserted": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "exact_current_rows": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[19]", "name": "H3BO3", "primary": {"id": "CHEBI:33118", "label": "boric acid"}, "canonical_label": "boric acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["bpdb:2136", "cas:10043-35-3", "cas:11113-50-1", "drugcentral:3035", "gmelin:1585", "kegg.compound:C12486", "kegg.drug:D01089", "molbase:1644", "pdb-ccd:BO3", "ppdb:2136"], "generalized_empirical_formula": ["H3BO3"], "has_alternative_id": ["CHEBI:22911", "CHEBI:31299", "CHEBI:41248"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:33118"], "inchi_key_string": ["KGBXLFKZBHKPEV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"], "mass": ["61.833"], "monoisotopic_mass": ["62.01752"], "smiles_string": ["[H]OB(O[H])O[H]"]}, "synonyms": ["B(OH)3", "BORIC ACID", "Boric acid", "H3BO3", "[B(OH)3]", "boric acid", "boron trihydroxide", "orthoboric acid", "trihydroxidoboron", "trihydroxidoboron"], "secondary": {"asserted": {"id": "CHEBI:33118", "label": "boric acid"}, "exact_current_rows": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[20]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "canonical_label": "sodium molybdate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium molybdate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10102-40-6", "pubmed:20645132", "pubmed:20813395", "pubmed:22663766", "pubmed:3382795", "reaxys:19032996", "wikipedia.en:Sodium_molybdate"], "generalized_empirical_formula": ["2H2O.MoO4.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75213"], "inchi_key_string": ["FDEIWTXVNPKYDL-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/Mo.2Na.2H2O.4O/h;;;2*1H2;;;;/q;2*+1;;;;;2*-1"], "mass": ["241.946"], "monoisotopic_mass": ["243.88573"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]}, "synonyms": ["Disodium molybdate dihydrate", "Molybdic acid, disodium salt, dihydrate", "Na2MoO4.2H2O", "Sodium molybdate(VI) dihydrate", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium orthomolybdate dihydrate"], "secondary": {"asserted": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "exact_current_rows": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[21]", "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "canonical_label": "nickel dichloride", "label_equal": true, "definition": ["A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7718-54-9", "kegg.compound:C14711", "pubmed:11739495", "pubmed:12603851", "pubmed:21928331", "pubmed:23179351", "pubmed:23622879", "pubmed:23702803", "pubmed:23735035", "pubmed:7671317", "reaxys:3902827", "reaxys:8128171", "wikipedia.en:Nickel_dichloride"], "generalized_empirical_formula": ["Cl2Ni"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:34887"], "inchi_key_string": ["QMMRZOWCJAIUJA-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"], "mass": ["129.599"], "monoisotopic_mass": ["127.87305"], "smiles_string": ["[Cl][Ni][Cl]"]}, "synonyms": ["NiCl2", "Nickel chloride", "Nickel(II) chloride", "[NiCl2]", "nickel dichloride", "nickel dichloride", "nickel(2+) chloride", "nickel(2+) chloride", "nickel(II) chloride", "nickel(II) chloride", "nickelous chloride"], "secondary": {"asserted": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "exact_current_rows": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[22]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "canonical_label": "disodium selenite pentahydrate", "label_equal": true, "definition": ["A hydrate that is the pentahydrate form of disodium selenite."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:26970-82-1", "pubmed:15259772", "pubmed:15559373", "pubmed:16126997", "pubmed:17873396", "pubmed:24479345", "pubmed:24716537", "reaxys:14666014", "wikipedia.en:Sodium_selenite"], "generalized_empirical_formula": ["5H2O.2Na.O3Se"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131361"], "inchi_key_string": ["TUANAMBRHOLYTH-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"], "mass": ["263.012"], "monoisotopic_mass": ["263.93363"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2SeO3.5H2O", "Selenious acid disodium salt, pentahydrate", "Sodium selenite pentahydrate", "disodium selenite hydrate", "sodium selenite hydrate", "sodium selenite--water (1/5)", "sodium selenite--water (1/5)"], "secondary": {"asserted": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "exact_current_rows": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[23]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "canonical_label": "sodium tungstate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines to nitrones"], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10213-10-2", "reaxys:13157884", "wikipedia.en:Sodium_tungstate"], "generalized_empirical_formula": ["2H2O.2Na.O4W"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63939"], "inchi_key_string": ["WPZFLQRLSGVIAA-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.2H2O.4O.W/h;;2*1H2;;;;;/q2*+1;;;;;2*-1;"], "mass": ["329.846"], "monoisotopic_mass": ["329.93126"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]}, "synonyms": ["Na2WO4.2H2O", "Tungstic acid, sodium salt, dihydrate", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium orthotungstate dihydrate", "sodium tungstate(VI) dihydrate"], "secondary": {"asserted": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "exact_current_rows": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[24]", "name": "H2SO4", "primary": {"id": "CHEBI:26836", "label": "sulfuric acid"}, "canonical_label": "sulfuric acid", "label_equal": true, "definition": ["A sulfur oxoacid that consists of two oxo and two hydroxy groups joined covalently to a central sulfur atom."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7664-93-9", "gmelin:2122", "kegg.compound:C00059", "kegg.drug:D05963", "knapsack:C00007530", "molbase:4", "ppdb:606", "pubmed:13568755", "pubmed:16122922", "pubmed:19397353", "pubmed:22047659", "pubmed:22136045", "pubmed:22204399", "pubmed:22267186", "pubmed:22296037", "pubmed:22364556", "pubmed:22435616", "reaxys:2037554", "wikipedia.en:Sulfuric_acid"], "generalized_empirical_formula": ["H2O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26836"], "inchi_key_string": ["QAOWNCQODCNURD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O4S/c1-5(2,3)4/h(H2,1,2,3,4)"], "mass": ["98.079"], "monoisotopic_mass": ["97.96738"], "smiles_string": ["[H]OS(=O)(=O)O[H]"]}, "synonyms": ["Acide sulfurique", "Acido sulfurico", "Acidum sulfuricum", "H2SO4", "Schwefelsaeureloesungen", "Sulfuric acid", "[S(OH)2O2]", "[SO2(OH)2]", "dihydrogen tetraoxosulfate", "dihydrogen tetraoxosulfate", "dihydroxidodioxidosulfur", "dihydroxidodioxidosulfur", "hydrogen tetraoxosulfate(2-)", "hydrogen tetraoxosulfate(2-)", "hydrogen tetraoxosulfate(VI)", "hydrogen tetraoxosulfate(VI)", "sulfuric acid", "sulfuric acid", "sulphuric acid", "tetraoxosulfuric acid", "tetraoxosulfuric acid"], "secondary": {"asserted": {"id": "CHEBI:26836", "label": "sulfuric acid"}, "exact_current_rows": [{"label": "H2SO4", "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[25]", "name": "Biotin", "primary": {"id": "CHEBI:15956", "label": "biotin"}, "canonical_label": "biotin", "label_equal": true, "definition": ["An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:58-85-5", "chemspider:149962", "drugbank:DB00121", "drugcentral:373", "foodb.food:FDB014510", "gmelin:1918703", "hmdb:HMDB0000030", "kegg.compound:C00120", "kegg.drug:D00029", "knapsack:C00000756", "lincs.smallmolecule:LSM-3994", "metacyc.compound:BIOTIN", "pdb-ccd:BTN", "pmc:PMC8089577", "pubmed:10064317", "pubmed:10215065", "pubmed:10577274", "pubmed:11435506", "pubmed:11481419", "pubmed:11800048", "pubmed:12055344", "pubmed:12070309", "pubmed:12603856", "pubmed:12803839", "pubmed:15012185", "pubmed:15202718", "pubmed:15272000", "pubmed:15690449", "pubmed:15863846", "pubmed:15899401", "pubmed:15992684", "pubmed:16011464", "pubmed:16195795", "pubmed:16419467", "pubmed:16676358", "pubmed:16677798", "pubmed:16704206", "pubmed:16769720", "pubmed:17297119", "pubmed:1814646", "pubmed:18202531", "pubmed:18452485", "pubmed:18509457", "pubmed:19212411", "pubmed:19319844", "pubmed:19727438", "pubmed:19928962", "pubmed:20967359", "pubmed:20974274", "pubmed:2100006", "pubmed:21248194", "pubmed:21356565", "pubmed:21373679", "pubmed:21596550", "pubmed:21871906", "pubmed:25515858", "pubmed:33346513", "pubmed:33461365", "pubmed:34077272", "pubmed:8333586", "pubmed:8750932", "pubmed:9022537", "pubmed:9038855", "pubmed:9094878", "pubmed:9164991", "pubmed:9176832", "pubmed:9371938", "pubmed:9416479", "reaxys:86838", "wikipedia.en:Biotin"], "generalized_empirical_formula": ["C10H16N2O3S"], "has_alternative_id": ["CHEBI:13905", "CHEBI:22882", "CHEBI:22884", "CHEBI:3108", "CHEBI:41236"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15956"], "inchi_key_string": ["YBJHBAHKTGYVGT-ZKWXMUAHSA-N"], "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"], "mass": ["244.316"], "monoisotopic_mass": ["244.08816"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]}, "synonyms": ["(+)-cis-Hexahydro-2-oxo-1H-thieno[3,4]imidazole-4-valeric acid", "(3aS,4S,6aR)-Hexahydro-2-oxo-1H-thieno[3,4-d]imidazole-4-valeric acid", "5-(2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl)pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "BIOTIN", "Coenzyme R", "D-(+)-biotin", "D-Biotin", "Vitamin H", "biotin", "biotina", "biotine", "biotinum", "cis-(+)-Tetrahydro-2-oxothieno[3,4]imidazoline-4-valeric acid", "cis-Hexahydro-2-oxo-1H-thieno(3,4)imidazole-4-valeric acid", "cis-Tetrahydro-2-oxothieno(3,4-d)imidazoline-4-valeric acid", "vitamin B7"], "secondary": {"asserted": {"id": "CHEBI:15956", "label": "biotin"}, "exact_current_rows": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[26]", "name": "Folic acid", "primary": {"id": "CHEBI:27470", "label": "folic acid"}, "canonical_label": "folic acid", "label_equal": true, "definition": ["An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND606960789", "cas:59-30-3", "chemspider:5815", "drugbank:DB00158", "drugcentral:1231", "foodb.food:FDB014504", "hmdb:HMDB0000121", "kegg.compound:C00504", "kegg.drug:D00070", "knapsack:C00001539", "lincs.smallmolecule:LSM-5355", "metacyc.compound:CPD-12826", "pdb-ccd:FOL", "pubmed:10138938", "pubmed:10897644", "pubmed:10958818", "pubmed:11261364", "pubmed:11451208", "pubmed:11959400", "pubmed:14387833", "pubmed:15321809", "pubmed:15523939", "pubmed:15754725", "pubmed:15797531", "pubmed:15797685", "pubmed:15831910", "pubmed:15990733", "pubmed:16093404", "pubmed:16277678", "pubmed:16380297", "pubmed:16871332", "pubmed:17784727", "pubmed:18788725", "pubmed:19121630", "pubmed:19335717", "pubmed:19355913", "pubmed:24650098", "pubmed:33624660", "pubmed:33965562", "pubmed:33968971", "pubmed:34207319", "pubmed:34219855", "pubmed:7738698", "pubmed:8235383", "pubmed:9040515", "pubmed:9420019", "pubmed:9565830", "pubmed:9683174", "pubmed:9781393", "pubmed:9808640", "pubmed:9808641", "reaxys:100781", "wikipedia.en:Folic_Acid"], "generalized_empirical_formula": ["C19H19N7O6"], "has_alternative_id": ["CHEBI:24075", "CHEBI:42610", "CHEBI:5140", "CHEBI:569217"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:27470"], "inchi_key_string": ["OVBPIULPVIDEAO-LBPRGKRZSA-N"], "inchi_string": ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"], "mass": ["441.404"], "monoisotopic_mass": ["441.13968"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]}, "synonyms": ["(2S)-2-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzamido)pentanedioic acid", "Acfol", "Folate", "Folicet", "Folsaeure", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-[(4-{[(2-amino-4-oxo-1,4-dihydropteridin-6-yl)methyl]amino}phenyl)carbonyl]-L-glutamic acid", "N-pteroyl-L-glutamic acid", "PGA", "PteGlu", "acide folique", "acido folico", "acidum folicum", "folic acid", "pteroyl-L-glutamic acid", "pteroyl-L-monoglutamic acid", "pteroylglutamic acid", "pteroylmonoglutamic acid", "vitamin B11", "vitamin B9", "vitamin Bc", "vitamin Be", "vitamin M"], "secondary": {"asserted": {"id": "CHEBI:27470", "label": "folic acid"}, "exact_current_rows": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[27]", "name": "Pyridoxine hydrochloride", "primary": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "canonical_label": "pyridoxine hydrochloride", "label_equal": true, "definition": ["The hydrochloride salt of pyridoxine."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND500675659", "beilstein:3632435", "cas:58-56-0", "drugbank:DBSALT000151", "foodb.food:FDB000575", "gmelin:1067921", "kegg.drug:D02179", "pubmed:15098856", "pubmed:17416572", "pubmed:17891511", "pubmed:18243627", "pubmed:19481898", "pubmed:20645279", "pubmed:21781646", "pubmed:24421551", "pubmed:27468034", "pubmed:28095734", "pubmed:32460509", "pubmed:33209152", "pubmed:33936292", "pubmed:34140989"], "generalized_empirical_formula": ["C8H11NO3.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30961"], "inchi_key_string": ["ZUFQODAHGAHPFQ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H11NO3.ClH/c1-5-8(12)7(4-11)6(3-10)2-9-5;/h2,10-12H,3-4H2,1H3;1H"], "mass": ["205.641"], "monoisotopic_mass": ["205.05057"], "smiles_string": ["Cc1ncc(CO)c(CO)c1O.Cl"]}, "synonyms": ["2-methyl-3-hydroxy-4,5-bis(hydroxymethyl)pyridine hydrochloride", "3-hydroxy-4,5-dimethylol-alpha-picoline hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "5-hydroxy-6-methyl-3,4-pyridinedimethanol hydrochloride", "pyridoxol hydrochloride", "vitamin B6 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "exact_current_rows": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[28]", "name": "Thiamine HCl", "primary": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "canonical_label": "thiamine hydrochloride", "label_equal": true, "definition": ["A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND605711145", "agr:IND606057536", "beilstein:3642937", "beilstein:3851771", "cas:67-03-8", "chemspider:5967", "drugbank:DBSALT000205", "foodb.food:FDB008416", "gmelin:31154", "gmelin:691133", "kegg.drug:D02094", "pubmed:11548854", "pubmed:12224421", "pubmed:21212548", "pubmed:22305197", "pubmed:24399744", "pubmed:25977858", "pubmed:26616989", "pubmed:27163892", "pubmed:28763984", "pubmed:28784494", "pubmed:30131156", "pubmed:31270735", "pubmed:31664290", "pubmed:32009117", "pubmed:32562525", "pubmed:32824791", "reaxys:17124533"], "generalized_empirical_formula": ["C12H17N4OS.Cl.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:49105"], "inchi_key_string": ["DPJRMOMPQZCRJU-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C12H17N4OS.2ClH/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H/q+1;;/p-1"], "mass": ["337.276"], "monoisotopic_mass": ["336.05784"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1.Cl.[Cl-]"]}, "synonyms": ["3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "thiamin dichloride", "thiamin hydrochloride", "thiamine HCl", "thiamine chloride hydrochloride", "thiamine dichloride", "thiamine(2+) dichloride", "thiaminium chloride hydrochloride", "vitamin B1 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "exact_current_rows": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[29]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015", "label": "riboflavin"}, "canonical_label": "riboflavin", "label_equal": true, "definition": ["&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:83-88-5", "chemspider:431981", "drugbank:DB00140", "drugcentral:2834", "foodb.food:FDB012160", "hmdb:HMDB0000244", "kegg.compound:C00255", "kegg.drug:D00050", "knapsack:C00001552", "lincs.smallmolecule:LSM-4084", "metacyc.compound:RIBOFLAVIN", "patent:US2807611", "patent:US2876169", "pdb-ccd:RBF", "pubmed:10566553", "pubmed:11399071", "pubmed:11606856", "pubmed:12083520", "pubmed:12354259", "pubmed:12927541", "pubmed:14963913", "pubmed:16273338", "pubmed:16460756", "pubmed:16658098", "pubmed:182198", "pubmed:18832377", "pubmed:19169240", "pubmed:19212411", "pubmed:19854891", "pubmed:22770225", "pubmed:2369885", "pubmed:23818044", "pubmed:24643482", "pubmed:24816110", "pubmed:25108762", "pubmed:25468971", "pubmed:25887755", "pubmed:2631092", "pubmed:29937405", "pubmed:3142982", "pubmed:33154451", "pubmed:33304888", "pubmed:33886098", "pubmed:33892358", "pubmed:34156642", "pubmed:3592624", "pubmed:3878498", "pubmed:4019261", "pubmed:6475825", "pubmed:6546833", "pubmed:6650303", "pubmed:7101408", "pubmed:7883462", "pubmed:8487103", "pubmed:8604671", "pubmed:8678471", "pubmed:8976642", "pubmed:9184778", "pubmed:9808225", "pubmed:9874201", "reaxys:97831", "wikipedia.en:Riboflavin"], "generalized_empirical_formula": ["C17H20N4O6"], "has_alternative_id": ["CHEBI:15044", "CHEBI:27299", "CHEBI:45214", "CHEBI:529204", "CHEBI:8843"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17015"], "inchi_key_string": ["AUNGANRZJHBGPY-SCRDCRAPSA-N"], "inchi_string": ["InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23)14(25)12(24)6-22)15-13(18-9)16(26)20-17(27)19-15/h3-4,11-12,14,22-25H,5-6H2,1-2H3,(H,20,26,27)/t11-,12+,14-/m0/s1"], "mass": ["376.369"], "monoisotopic_mass": ["376.13828"], "smiles_string": ["Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)CO)c2cc1C"]}, "synonyms": ["1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol", "5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "6,7-dimethyl-9-D-ribitylisoalloxazine", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine", "7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-ribitylisoalloxazine", "Aqua-Flave", "Beflavin", "Beflavine", "Bisulase", "Dermadram", "E101", "Fiboflavin", "Flavaxin", "Flavin Bb", "Flaxain", "Hyflavin", "Vitamin B2", "lactoflavin", "riboflavin (vit B2)", "riboflavin", "riboflavina", "riboflavine", "riboflavinum", "vitamin B2", "vitamin G", "vitasan B2"], "secondary": {"asserted": {"id": "CHEBI:17015", "label": "riboflavin"}, "exact_current_rows": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[30]", "name": "Nicotinic acid", "primary": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "canonical_label": "nicotinic acid", "label_equal": true, "definition": ["A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND607088605", "cas:59-67-6", "chemspider:913", "drugbank:DB00627", "drugcentral:2835", "foodb.food:FDB001014", "gmelin:3340", "hmdb:HMDB0001488", "kegg.compound:C00253", "kegg.drug:D00049", "knapsack:C00000208", "lincs.smallmolecule:LSM-4676", "metacyc.compound:NIACINE", "pdb-ccd:NIO", "pubmed:10540864", "pubmed:113218", "pubmed:12563315", "pubmed:12789870", "pubmed:135660", "pubmed:14550884", "pubmed:15037193", "pubmed:15183629", "pubmed:15205990", "pubmed:15311728", "pubmed:15627518", "pubmed:15651982", "pubmed:16018787", "pubmed:16172771", "pubmed:16322787", "pubmed:16400392", "pubmed:16449845", "pubmed:16767301", "pubmed:16877271", "pubmed:16945375", "pubmed:18037924", "pubmed:182198", "pubmed:186078", "pubmed:18993152", "pubmed:18996527", "pubmed:19369827", "pubmed:19592242", "pubmed:19678716", "pubmed:19779335", "pubmed:20979384", "pubmed:21632263", "pubmed:22116693", "pubmed:22155410", "pubmed:22229411", "pubmed:22366213", "pubmed:22458880", "pubmed:22770225", "pubmed:24029555", "pubmed:24568240", "pubmed:24675661", "pubmed:24848081", "pubmed:24975217", "pubmed:25040591", "pubmed:25241762", "pubmed:25429652", "pubmed:32954525", "pubmed:33273654", "pubmed:33932650", "pubmed:34066686", "pubmed:34085526", "pubmed:34117670", "pubmed:4033386", "pubmed:4259917", "pubmed:582105", "pubmed:699281", "pubmed:7217784", "pubmed:7581845", "pubmed:8306147", "pubmed:8423912", "pubmed:8679452", "pubmed:9107536", "reaxys:109591", "wikipedia.en:Niacin"], "generalized_empirical_formula": ["C6H5NO2"], "has_alternative_id": ["CHEBI:25538", "CHEBI:44319", "CHEBI:7559"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15940"], "inchi_key_string": ["PVNIIMVLHYAWGP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"], "mass": ["123.111"], "monoisotopic_mass": ["123.03203"], "smiles_string": ["O=C(O)c1cccnc1"]}, "synonyms": ["3-Pyridylcarboxylic acid", "3-carboxylpyridine", "3-carboxypyridine", "3-pyridinecarboxylic acid", "NICOTINIC ACID", "NICOTINIC ACID", "Niacin", "Niacor", "Niaspan", "Nicotinic acid", "Nicotinic acid", "Nicotinsaure", "Nikotinsaeure", "P.P. factor", "PP factor", "acide nicotinique", "acido nicotinico", "acidum nicotinicum", "anti-pellagra vitamin", "beta-pyridinecarboxylic acid", "m-pyridinecarboxylic acid", "nicotinic acid", "nicotinic acid", "pellagra preventive factor", "pyridine-3-carboxylic acid", "pyridine-3-carboxylic acid", "pyridine-beta-carboxylic acid", "pyridine-carboxylique-3", "vitamin B3"], "secondary": {"asserted": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "exact_current_rows": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[31]", "name": "Calcium D-(+)-pantothenate", "primary": {"id": "CHEBI:31345", "label": "Calcium pantothenate"}, "canonical_label": "Calcium pantothenate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:137-08-6", "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278", "pubmed:20553011", "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula": ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"], "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"], "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]}, "synonyms": ["Calcium pantotenate", "Calcium pantothenate", "Calcium pantothenate, d-", "Calpan", "D-ca pantothenate", "D-calcium pantothenate", "NSC-36292", "Pantholin", "Pantothenic acid (as calcium)", "Pantothenic acid calcium salt", "Vitamin b5, calcium salt", "pantotenato de calcio", "pantothenate de calcium"]}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[32]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843", "label": "vitamin B12"}, "canonical_label": "vitamin B12", "label_equal": true, "definition": ["Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives)."], "annotations": {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:176843"]}, "synonyms": ["vitamin B-12", "vitamin B12 vitamer", "vitamin B12 vitamers", "vitamin B12", "vitamins B12"], "secondary": {"asserted": {"id": "CHEBI:176843", "label": "vitamin B12"}, "exact_current_rows": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[33]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "canonical_label": "4-aminobenzoic acid", "label_equal": true, "definition": ["An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:150-13-0", "drugbank:DB02362", "drugcentral:2049", "ecmdb:ECMDB01392", "gmelin:50150", "hmdb:HMDB0001392", "kegg.compound:C00568", "kegg.drug:D02456", "knapsack:C00001401", "pdb-ccd:PAB", "pubmed:12039592", "pubmed:14745019", "pubmed:15115392", "pubmed:1527790", "pubmed:16290145", "pubmed:17149871", "pubmed:17743450", "pubmed:17800214", "pubmed:19469519", "pubmed:22767283", "pubmed:22994574", "pubmed:23063996", "pubmed:23084339", "pubmed:23144588", "pubmed:23471007", "pubmed:3599019", "pubmed:3820215", "pubmed:3950915", "pubmed:8411009", "pubmed:9406595", "reaxys:471605", "wikipedia.en:4-Aminobenzoic_acid", "ymdb:YMDB00493"], "generalized_empirical_formula": ["C7H7NO2"], "has_alternative_id": ["CHEBI:113372", "CHEBI:1783", "CHEBI:20315", "CHEBI:44778"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30753"], "inchi_key_string": ["ALYNCZNDIQEVRV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"], "mass": ["137.138"], "monoisotopic_mass": ["137.04768"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]}, "synonyms": ["1-Amino-4-carboxybenzene", "4-AMINOBENZOIC ACID", "4-AMINOBENZOIC ACID", "4-Amino-benzoic acid", "4-Aminobenzoesaeure", "4-Aminobenzoic acid", "4-Aminobenzoic acid", "4-Carboxyaniline", "4-Carboxyphenylamine", "4-aminobenzoic acid", "4-aminobenzoic acid", "ABEE", "PABA", "gamma-Aminobenzoic acid", "gamma-aminobenzoic acid", "p-Aminobenzoesaeure", "p-aminobenzoic acid", "p-carboxyaniline", "p-carboxyphenylamine", "para-aminobenzoic acid"], "secondary": {"asserted": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "exact_current_rows": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[34]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id": "CHEBI:16494", "label": "lipoic acid"}, "canonical_label": "lipoic acid", "label_equal": true, "definition": ["A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:122410", "cas:62-46-4", "drugbank:DB00166", "drugcentral:4732", "ecmdb:ECMDB01451", "gmelin:720915", "kegg.compound:C00725", "kegg.drug:D00086", "pubmed:15328413", "pubmed:7519986", "pubmed:7548757", "reaxys:81853", "wikipedia.en:Lipoic_acid", "ymdb:YMDB00334"], "generalized_empirical_formula": ["C8H14O2S2"], "has_alternative_id": ["CHEBI:146958", "CHEBI:25058", "CHEBI:6492"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16494"], "inchi_key_string": ["AGBQKNBQESQNJD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H14O2S2/c9-8(10)4-2-1-3-7-5-6-11-12-7/h7H,1-6H2,(H,9,10)"], "mass": ["206.332"], "monoisotopic_mass": ["206.04352"], "smiles_string": ["O=C(O)CCCCC1CCSS1"]}, "synonyms": ["1,2-dithiolane-3-pentanoic acid", "1,2-dithiolane-3-valeric acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)valeric acid", "5-(dithiolan-3-yl)valeric acid", "5-[3-(1,2-dithiolanyl)]pentanoic acid", "6,8-thioctic acid", "6,8-thiotic acid", "6-thioctic acid", "6-thiotic acid", "Acetate-replacing factor", "Biletan", "Lipoic acid", "Thioctansaeure", "Thioctic acid", "Thioctsaeure", "Thioktsaeure", "alpha-Lipoic acid", "alpha-Liponsaeure", "alpha-lipoic acid", "liponic acid"], "secondary": {"asserted": {"id": "CHEBI:16494", "label": "lipoic acid"}, "exact_current_rows": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[0]", "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806", "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3", "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"], "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]}, "synonyms": ["Resazurin"]}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[1]", "name": "Na2CO3", "primary": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "canonical_label": "sodium carbonate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:497-19-8", "ppdb:594"], "generalized_empirical_formula": ["CO3.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:29377"], "inchi_key_string": ["CDBYLPFSWZWCQE-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/CH2O3.2Na/c2-1(3)4;;/h(H2,2,3,4);;/q;2*+1/p-2"], "mass": ["105.988"], "monoisotopic_mass": ["105.96428"], "smiles_string": ["O=C([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2CO3", "Natriumkarbonat", "disodium carbonate", "disodium trioxidocarbonate", "disodium trioxidocarbonate", "sodium carbonate", "sodium carbonate"], "secondary": {"asserted": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "exact_current_rows": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[2]", "name": "Cellobiose", "primary": {"id": "CHEBI:17057", "label": "cellobiose"}, "canonical_label": "cellobiose", "label_equal": true, "definition": ["A glycosylglucose consisting of two glucose units linked via a β(1→4) bond."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1292744", "cas:528-50-7", "drugbank:DB02061", "kegg.compound:C00185", "knapsack:C00001134", "pubmed:19669625", "pubmed:19968554", "wikipedia.en:Cellobiose"], "generalized_empirical_formula": ["C12H22O11"], "has_alternative_id": ["CHEBI:13952", "CHEBI:23061", "CHEBI:28108", "CHEBI:3522"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17057"], "inchi_key_string": ["GUBGYTABKSRVRQ-CUHNMECISA-N"], "inchi_string": ["InChI=1S/C12H22O11/c13-1-3-5(15)6(16)9(19)12(22-3)23-10-4(2-14)21-11(20)8(18)7(10)17/h3-20H,1-2H2/t3-,4-,5-,6+,7-,8-,9-,10-,11?,12+/m1/s1"], "mass": ["342.297"], "monoisotopic_mass": ["342.11621"], "smiles_string": ["OC[C@H]1O[C@@H](O[C@H]2[C@H](O)[C@@H](O)C(O)O[C@@H]2CO)[C@H](O)[C@@H](O)[C@@H]1O"], "wurcs_representation": ["WURCS=2.0/2,2,1/[a2122h-1x_1-5][a2122h-1b_1-5]/1-2/a4-b1"]}, "synonyms": ["1-beta-D-Glucopyranosyl-4-D-glucopyranose", "4-(beta-D-glucosido)-D-glucose", "4-O-beta-D-glucopyranosyl-D-glucopyranose", "4-beta-D-glucopyranosyl-D-glucopyranose", "Cellobiose", "D-(+)-cellobiose", "D-celiobiose", "D-cellobiose", "D-glucosyl-beta-(1-4)-D-glucose", "beta-D-glucopyranosyl-(1-&gt;4)-D-glucopyranose", "beta-D-glucopyranosyl-(1-&gt;4)-D-glucopyranose", "cellose"], "secondary": {"asserted": {"id": "CHEBI:17057", "label": "cellobiose"}, "exact_current_rows": [{"label": "Cellobiose", "match_type": "preferred_term", "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[3]", "name": "Cellulose", "primary": {"id": "CHEBI:18246", "label": "(1-&gt;4)-beta-D-glucan"}, "canonical_label": "(1-&gt;4)-beta-D-glucan", "label_equal": true, "definition": ["A β-&lt;small&gt;D&lt;/small&gt;-glucan in which the glucose units are connected by (1→4) linkages."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:9004-34-6", "hmdb:HMDB0006944", "kegg.compound:C00760", "kegg.drug:D00093", "kegg.glycan:G10481"], "generalized_empirical_formula": ["(C6H10O5)n.H2O"], "has_alternative_id": ["CHEBI:10812", "CHEBI:23063", "CHEBI:3529"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:18246"], "inchi_key_string": ["WQZGKKKJIJFFOK-VFUOTHLCSA-N"], "inchi_string": ["InChI=1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5-,6-/m1/s1"], "mass": ["180.156"], "monoisotopic_mass": ["180.06339"], "smiles_string": ["[H]O[C@@H]1O[C@H](CO)[C@@H](O)[C@H](O)[C@H]1O"], "wurcs_representation": ["WURCS=2.0/1,1,0/[a2122h-1b_1-5]/1/"]}, "synonyms": ["(1,4-beta-D-Glucosyl)n", "(1,4-beta-D-Glucosyl)n+1", "(1,4-beta-D-Glucosyl)n-1", "(1,4-beta-D-glucosyl)(n)", "(1,4-beta-D-glucosyl)n", "(1-&gt;4)-beta-D-glucopyranan", "(1-&gt;4)-beta-D-glucopyranan", "1,4-beta-D-Glucan", "Cellulose"], "secondary": {"asserted": {"id": "CHEBI:18246", "label": "(1-&gt;4)-beta-D-glucan"}, "exact_current_rows": [{"label": "Cellulose", "match_type": "preferred_term", "identifier": "CHEBI:18246", "preferred_term": "Cellulose", "ontology_id": "CHEBI:18246", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[4]", "name": "L-Cysteine HCl x H2O", "primary": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride hydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of &lt;small&gt;L&lt;/small&gt;-cysteine hydrochloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326", "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"], "inchi_key_string": ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"], "mass": ["175.637"], "monoisotopic_mass": ["175.00699"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]}, "synonyms": ["(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride monohydrate", "Cysteine hydrochloride", "L-Cysteine monohydrate monochloride", "L-cysteine hydrochloride monohydrate", "L-cysteine hydrochloride--water (1/1)", "L-cysteine hydrochloride--water (1/1)"], "secondary": {"asserted": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "exact_current_rows": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[5]", "name": "Na2S x 9 H2O", "primary": {"id": "CHEBI:76209", "label": "sodium sulfide nonahydrate"}, "canonical_label": "sodium sulfide nonahydrate", "label_equal": true, "definition": ["A hydrate with formula Na&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;S·9H&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;O."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:1313-84-4", "kegg.drug:D09001", "pubmed:19810706", "reaxys:14636099"], "generalized_empirical_formula": ["9H2O.2Na.S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:76209"], "inchi_key_string": ["ZGHLCBJZQLNUAZ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.9H2O.S/h;;9*1H2;/q2*+1;;;;;;;;;;-2"], "mass": ["240.182"], "monoisotopic_mass": ["240.04669"], "smiles_string": ["O.O.O.O.O.O.O.O.O.[Na+].[Na+].[S-2]"]}, "synonyms": ["Na2S.9H2O", "Sodium sulfide (USP)", "disodium sulfide nonahydrate", "disodium sulfide--water (1/9)", "disodium sulfide--water (1/9)", "sodium monosulfide nonahydrate", "sodium monosulfide.9H2O", "sodium sulfide.9H2O"], "secondary": {"asserted": {"id": "CHEBI:76209", "label": "sodium sulfide nonahydrate"}, "exact_current_rows": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[6]", "name": "K2HPO4", "primary": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "canonical_label": "dipotassium hydrogen phosphate", "label_equal": true, "definition": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-11-4", "kegg.compound:C13197", "kegg.drug:D02403", "metacyc.compound:CPD0-2433", "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"], "generalized_empirical_formula": ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131527"], "inchi_key_string": ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "secondary": {"asserted": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "exact_current_rows": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[7]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "canonical_label": "potassium dihydrogen phosphate", "label_equal": true, "definition": ["A potassium salt in which dihydrogen phosphate(1−) is the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"], "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"], "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]}, "synonyms": ["MKP", "Monopotassium dihydrogen phosphate", "Monopotassium monophosphate", "Monopotassium orthophosphate", "Monopotassium phosphate", "Orthophosphoric acid, monopotassium salt", "Phosphoric acid, monopotassium salt", "Phosphoric acid, potassium salt (1:1)", "Potassium acid phosphate", "Potassium dihydrogen orthophosphate", "Potassium dihydrogen phosphate", "Potassium phosphate monobasic", "Potassium phosphate", "Sorensen's potassium phosphate", "potassium dihydrogen phosphate", "potassium dihydrogen phosphate"], "secondary": {"asserted": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "exact_current_rows": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[8]", "name": "(NH4)2SO4", "primary": {"id": "CHEBI:62946", "label": "ammonium sulfate"}, "canonical_label": "ammonium sulfate", "label_equal": true, "definition": ["An inorganic sulfate salt obtained by reaction of sulfuric acid with two equivalents of ammonia. A high-melting (decomposes above 280°C) white solid which is very soluble in water (70.6 g/100 g water at 0°C; 103.8 g/100 g water at 100°C), it is widely used as a fertilizer for alkaline soils."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7783-20-2", "kegg.drug:D08853", "metacyc.compound:NH42SO4", "ppdb:36", "pubmed:20556652", "reaxys:11343144", "wikipedia.en:Ammonium_sulfate"], "generalized_empirical_formula": ["2H4N.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:62946"], "inchi_key_string": ["BFNBIHQBYMNNAN-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2H3N.H2O4S/c;;1-5(2,3)4/h2*1H3;(H2,1,2,3,4)"], "mass": ["132.141"], "monoisotopic_mass": ["132.02048"], "smiles_string": ["O=S(=O)([O-])[O-].[NH4+].[NH4+]"]}, "synonyms": ["(NH4)2SO4", "ammonium sulfate (2:1)", "ammonium sulphate", "diammonium sulfate", "diazanium sulfate", "diazanium sulfate", "mascagnite", "sulfuric acid ammonium salt (1:2)", "sulfuric acid, diammonium salt", "sulphate of ammonia"], "secondary": {"asserted": {"id": "CHEBI:62946", "label": "ammonium sulfate"}, "exact_current_rows": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[9]", "name": "NaCl", "primary": {"id": "CHEBI:26710", "label": "sodium chloride"}, "canonical_label": "sodium chloride", "label_equal": true, "definition": ["An inorganic chloride salt having sodium(1+) as the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula": ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string": ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]}, "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "secondary": {"asserted": {"id": "CHEBI:26710", "label": "sodium chloride"}, "exact_current_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[10]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "canonical_label": "magnesium sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505", "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222", "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"], "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "exact_current_rows": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[11]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "canonical_label": "calcium chloride dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of calcium chloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8", "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"], "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass": ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}, "synonyms": ["CaCl2.2H2O", "Calcium chloride hydrate", "Calcium chloride", "calcium chloride--water (1/2)", "calcium chloride--water (1/2)", "calcium dichloride dihydrate"], "secondary": {"asserted": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "exact_current_rows": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[12]", "name": "Nitrilotriacetic acid", "primary": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "canonical_label": "nitrilotriacetic acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1710776", "cas:139-13-9", "drugbank:DB03040", "gmelin:3726", "kegg.compound:C14695", "pdb-ccd:NTA"], "generalized_empirical_formula": ["C6H9NO6"], "has_alternative_id": ["CHEBI:34889", "CHEBI:44555"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:44557"], "inchi_key_string": ["MGFYIUFZLHCRTH-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"], "mass": ["191.139"], "monoisotopic_mass": ["191.04299"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]}, "synonyms": ["Complexon I", "H3nta", "Komplexon I", "N(CH2-COOH)3", "N,N-bis(carboxymethyl)glycine", "N,N-bis(carboxymethyl)glycine", "NITRILOTRIACETIC ACID", "NTA", "Nitrilotriacetate", "Nitrilotriacetic acid", "Nitrilotriessigsaeure", "Triglycollamic acid", "Trilon A", "alpha,alpha',alpha''-trimethylaminetricarboxylic acid", "nitrilo-2,2',2''-triacetic acid", "tri(carboxymethyl)amine", "triglycine"], "secondary": {"asserted": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "exact_current_rows": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[13]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "canonical_label": "manganese(II) sulfate monohydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of manganese(II) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-96-5", "kegg.drug:D04854", "pubmed:26097037", "reaxys:13153017", "wikipedia.en:Manganese(II)_sulfate"], "generalized_empirical_formula": ["H2O.Mn.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86364"], "inchi_key_string": ["ISPYRSDWRDQNSW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mn.H2O4S.H2O/c;1-5(2,3)4;/h;(H2,1,2,3,4);1H2/q+2;;/p-2"], "mass": ["169.016"], "monoisotopic_mass": ["168.90034"], "smiles_string": ["O.O=S(=O)([O-])[O-].[Mn+2]"]}, "synonyms": ["Manganese sulfate hydrate", "Manganese sulfate monohydrate", "Manganese sulfate", "Manganous sulfate monohydrate", "MnSO4.H2O", "manganese(2+) sulfate monohydrate", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulphate monohydrate", "manganese(II) sulphate monohydrate"], "secondary": {"asserted": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "exact_current_rows": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[14]", "name": "FeSO4 x 7 H2O", "primary": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "canonical_label": "iron(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used)."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]}, "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O", "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"], "secondary": {"asserted": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[15]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "canonical_label": "cobalt(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of cobalt(2+) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10026-24-1", "pubmed:10504146", "pubmed:12187935", "pubmed:12209163", "pubmed:12579202", "pubmed:12948248", "pubmed:2227161", "pubmed:24359163", "pubmed:25896363", "wikipedia.en:Cobalt(II)_sulfate"], "generalized_empirical_formula": ["Co.7H2O.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91244"], "inchi_key_string": ["MEYVLGVRTYSQHI-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Co.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["281.101"], "monoisotopic_mass": ["280.95888"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Co+2]"]}, "synonyms": ["Cobalt monosulfate heptahydrate", "cobalt sulfate heptahydrate", "cobalt(2+) sulfate--water (1/7)", "cobalt(2+) sulfate--water (1/7)", "cobalt(II) sulfate heptahydrate", "cobaltous sulfate heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[16]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "canonical_label": "zinc sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of zinc sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7446-20-0", "gmelin:47216", "kegg.drug:D01081", "wikipedia.en:Zinc_Sulfate"], "generalized_empirical_formula": ["7H2O.O4S.Zn"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32312"], "inchi_key_string": ["RZLVQBNCHSJZPX-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/H2O4S.7H2O.Zn/c1-5(2,3)4;;;;;;;;/h(H2,1,2,3,4);7*1H2;/q;;;;;;;;+2/p-2"], "mass": ["287.558"], "monoisotopic_mass": ["285.95482"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Zn+2]"]}, "synonyms": ["Zinc sulfate", "ZnSO4.7H2O", "zinc sulfate (1:1) heptahydrate", "zinc sulfate heptahydrate (1:1:7)", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate--water (1/7)", "zinc(2+) sulfate--water (1/7)"], "secondary": {"asserted": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "exact_current_rows": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[17]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "canonical_label": "copper(II) sulfate pentahydrate", "label_equal": true, "definition": ["The pentahydrate of copper(2+) sulfate. A bright blue crystalline solid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-99-8", "kegg.drug:D03613", "pubmed:11407502", "pubmed:12209195", "pubmed:12484481", "pubmed:15040745", "pubmed:15607472", "pubmed:15824790", "pubmed:19346702", "pubmed:2002460", "pubmed:20132934", "pubmed:2913309", "pubmed:3351847", "pubmed:7615984", "pubmed:8878264", "pubmed:9521458", "pubmed:9776063", "reaxys:16499970", "wikipedia.en:Copper(II)_sulfate"], "generalized_empirical_formula": ["Cu.5H2O.O4S"], "has_alternative_id": ["CHEBI:121741", "CHEBI:370227"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31440"], "inchi_key_string": ["JZCCFEFSEZPSOG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Cu.H2O4S.5H2O/c;1-5(2,3)4;;;;;/h;(H2,1,2,3,4);5*1H2/q+2;;;;;;/p-2"], "mass": ["249.684"], "monoisotopic_mass": ["248.93415"], "smiles_string": ["O=S(=O)([O-])[O-].[Cu+2].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H]"]}, "synonyms": ["CuSO4.5H2O", "Cupric sulfate", "copper sulphate(5.H2O)", "copper(2+) sulfate (1:1) pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate--water (1/5)", "copper(2+) sulfate--water (1/5)", "copper(II) sulfate, pentahydrate", "cupric sulfate pentahydrate"], "secondary": {"asserted": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "exact_current_rows": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[18]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "canonical_label": "potassium aluminium sulfate dodecahydrate", "label_equal": true, "definition": ["A hydrate resulting from the the formal combination of anhydrous potassium aluminium sulfate with 12 mol eq. of water."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7784-24-9", "reaxys:14851666", "wikipedia.en:Potassium_alum"], "generalized_empirical_formula": ["Al.12H2O.K.2O4S"], "has_alternative_id": ["CHEBI:31192"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86465"], "inchi_key_string": ["GNHOJBNSNUXZQA-UHFFFAOYSA-J"], "inchi_string": ["InChI=1S/Al.K.2H2O4S.12H2O/c;;2*1-5(2,3)4;;;;;;;;;;;;/h;;2*(H2,1,2,3,4);12*1H2/q+3;+1;;;;;;;;;;;;;;/p-4"], "mass": ["474.386"], "monoisotopic_mass": ["473.97548"], "smiles_string": ["O.O.O.O.O.O.O.O.O.O.O.O.O=S(=O)([O-])[O-].O=S(=O)([O-])[O-].[Al+3].[K+]"]}, "synonyms": ["AlK(SO4)2.12H2O", "Aluminum potassium disulfate dodecahydrate", "Aluminum potassium sulfate dodecahydrate", "Kalinite", "Potash alum dodecahydrate", "Potassium alum dodecahydrate", "Potassium aluminum disulfate dodecahydrate", "aluminium potassium sulfate--water (1/12)", "aluminium potassium sulfate--water (1/12)"], "secondary": {"asserted": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "exact_current_rows": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[19]", "name": "H3BO3", "primary": {"id": "CHEBI:33118", "label": "boric acid"}, "canonical_label": "boric acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["bpdb:2136", "cas:10043-35-3", "cas:11113-50-1", "drugcentral:3035", "gmelin:1585", "kegg.compound:C12486", "kegg.drug:D01089", "molbase:1644", "pdb-ccd:BO3", "ppdb:2136"], "generalized_empirical_formula": ["H3BO3"], "has_alternative_id": ["CHEBI:22911", "CHEBI:31299", "CHEBI:41248"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:33118"], "inchi_key_string": ["KGBXLFKZBHKPEV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"], "mass": ["61.833"], "monoisotopic_mass": ["62.01752"], "smiles_string": ["[H]OB(O[H])O[H]"]}, "synonyms": ["B(OH)3", "BORIC ACID", "Boric acid", "H3BO3", "[B(OH)3]", "boric acid", "boron trihydroxide", "orthoboric acid", "trihydroxidoboron", "trihydroxidoboron"], "secondary": {"asserted": {"id": "CHEBI:33118", "label": "boric acid"}, "exact_current_rows": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[20]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "canonical_label": "sodium molybdate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium molybdate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10102-40-6", "pubmed:20645132", "pubmed:20813395", "pubmed:22663766", "pubmed:3382795", "reaxys:19032996", "wikipedia.en:Sodium_molybdate"], "generalized_empirical_formula": ["2H2O.MoO4.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75213"], "inchi_key_string": ["FDEIWTXVNPKYDL-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/Mo.2Na.2H2O.4O/h;;;2*1H2;;;;/q;2*+1;;;;;2*-1"], "mass": ["241.946"], "monoisotopic_mass": ["243.88573"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]}, "synonyms": ["Disodium molybdate dihydrate", "Molybdic acid, disodium salt, dihydrate", "Na2MoO4.2H2O", "Sodium molybdate(VI) dihydrate", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium orthomolybdate dihydrate"], "secondary": {"asserted": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "exact_current_rows": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[21]", "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "canonical_label": "nickel dichloride", "label_equal": true, "definition": ["A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7718-54-9", "kegg.compound:C14711", "pubmed:11739495", "pubmed:12603851", "pubmed:21928331", "pubmed:23179351", "pubmed:23622879", "pubmed:23702803", "pubmed:23735035", "pubmed:7671317", "reaxys:3902827", "reaxys:8128171", "wikipedia.en:Nickel_dichloride"], "generalized_empirical_formula": ["Cl2Ni"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:34887"], "inchi_key_string": ["QMMRZOWCJAIUJA-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"], "mass": ["129.599"], "monoisotopic_mass": ["127.87305"], "smiles_string": ["[Cl][Ni][Cl]"]}, "synonyms": ["NiCl2", "Nickel chloride", "Nickel(II) chloride", "[NiCl2]", "nickel dichloride", "nickel dichloride", "nickel(2+) chloride", "nickel(2+) chloride", "nickel(II) chloride", "nickel(II) chloride", "nickelous chloride"], "secondary": {"asserted": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "exact_current_rows": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[22]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "canonical_label": "disodium selenite pentahydrate", "label_equal": true, "definition": ["A hydrate that is the pentahydrate form of disodium selenite."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:26970-82-1", "pubmed:15259772", "pubmed:15559373", "pubmed:16126997", "pubmed:17873396", "pubmed:24479345", "pubmed:24716537", "reaxys:14666014", "wikipedia.en:Sodium_selenite"], "generalized_empirical_formula": ["5H2O.2Na.O3Se"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131361"], "inchi_key_string": ["TUANAMBRHOLYTH-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"], "mass": ["263.012"], "monoisotopic_mass": ["263.93363"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2SeO3.5H2O", "Selenious acid disodium salt, pentahydrate", "Sodium selenite pentahydrate", "disodium selenite hydrate", "sodium selenite hydrate", "sodium selenite--water (1/5)", "sodium selenite--water (1/5)"], "secondary": {"asserted": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "exact_current_rows": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[23]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "canonical_label": "sodium tungstate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines to nitrones"], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10213-10-2", "reaxys:13157884", "wikipedia.en:Sodium_tungstate"], "generalized_empirical_formula": ["2H2O.2Na.O4W"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63939"], "inchi_key_string": ["WPZFLQRLSGVIAA-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.2H2O.4O.W/h;;2*1H2;;;;;/q2*+1;;;;;2*-1;"], "mass": ["329.846"], "monoisotopic_mass": ["329.93126"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]}, "synonyms": ["Na2WO4.2H2O", "Tungstic acid, sodium salt, dihydrate", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium orthotungstate dihydrate", "sodium tungstate(VI) dihydrate"], "secondary": {"asserted": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "exact_current_rows": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[24]", "name": "H2SO4", "primary": {"id": "CHEBI:26836", "label": "sulfuric acid"}, "canonical_label": "sulfuric acid", "label_equal": true, "definition": ["A sulfur oxoacid that consists of two oxo and two hydroxy groups joined covalently to a central sulfur atom."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7664-93-9", "gmelin:2122", "kegg.compound:C00059", "kegg.drug:D05963", "knapsack:C00007530", "molbase:4", "ppdb:606", "pubmed:13568755", "pubmed:16122922", "pubmed:19397353", "pubmed:22047659", "pubmed:22136045", "pubmed:22204399", "pubmed:22267186", "pubmed:22296037", "pubmed:22364556", "pubmed:22435616", "reaxys:2037554", "wikipedia.en:Sulfuric_acid"], "generalized_empirical_formula": ["H2O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26836"], "inchi_key_string": ["QAOWNCQODCNURD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O4S/c1-5(2,3)4/h(H2,1,2,3,4)"], "mass": ["98.079"], "monoisotopic_mass": ["97.96738"], "smiles_string": ["[H]OS(=O)(=O)O[H]"]}, "synonyms": ["Acide sulfurique", "Acido sulfurico", "Acidum sulfuricum", "H2SO4", "Schwefelsaeureloesungen", "Sulfuric acid", "[S(OH)2O2]", "[SO2(OH)2]", "dihydrogen tetraoxosulfate", "dihydrogen tetraoxosulfate", "dihydroxidodioxidosulfur", "dihydroxidodioxidosulfur", "hydrogen tetraoxosulfate(2-)", "hydrogen tetraoxosulfate(2-)", "hydrogen tetraoxosulfate(VI)", "hydrogen tetraoxosulfate(VI)", "sulfuric acid", "sulfuric acid", "sulphuric acid", "tetraoxosulfuric acid", "tetraoxosulfuric acid"], "secondary": {"asserted": {"id": "CHEBI:26836", "label": "sulfuric acid"}, "exact_current_rows": [{"label": "H2SO4", "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[25]", "name": "Biotin", "primary": {"id": "CHEBI:15956", "label": "biotin"}, "canonical_label": "biotin", "label_equal": true, "definition": ["An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:58-85-5", "chemspider:149962", "drugbank:DB00121", "drugcentral:373", "foodb.food:FDB014510", "gmelin:1918703", "hmdb:HMDB0000030", "kegg.compound:C00120", "kegg.drug:D00029", "knapsack:C00000756", "lincs.smallmolecule:LSM-3994", "metacyc.compound:BIOTIN", "pdb-ccd:BTN", "pmc:PMC8089577", "pubmed:10064317", "pubmed:10215065", "pubmed:10577274", "pubmed:11435506", "pubmed:11481419", "pubmed:11800048", "pubmed:12055344", "pubmed:12070309", "pubmed:12603856", "pubmed:12803839", "pubmed:15012185", "pubmed:15202718", "pubmed:15272000", "pubmed:15690449", "pubmed:15863846", "pubmed:15899401", "pubmed:15992684", "pubmed:16011464", "pubmed:16195795", "pubmed:16419467", "pubmed:16676358", "pubmed:16677798", "pubmed:16704206", "pubmed:16769720", "pubmed:17297119", "pubmed:1814646", "pubmed:18202531", "pubmed:18452485", "pubmed:18509457", "pubmed:19212411", "pubmed:19319844", "pubmed:19727438", "pubmed:19928962", "pubmed:20967359", "pubmed:20974274", "pubmed:2100006", "pubmed:21248194", "pubmed:21356565", "pubmed:21373679", "pubmed:21596550", "pubmed:21871906", "pubmed:25515858", "pubmed:33346513", "pubmed:33461365", "pubmed:34077272", "pubmed:8333586", "pubmed:8750932", "pubmed:9022537", "pubmed:9038855", "pubmed:9094878", "pubmed:9164991", "pubmed:9176832", "pubmed:9371938", "pubmed:9416479", "reaxys:86838", "wikipedia.en:Biotin"], "generalized_empirical_formula": ["C10H16N2O3S"], "has_alternative_id": ["CHEBI:13905", "CHEBI:22882", "CHEBI:22884", "CHEBI:3108", "CHEBI:41236"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15956"], "inchi_key_string": ["YBJHBAHKTGYVGT-ZKWXMUAHSA-N"], "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"], "mass": ["244.316"], "monoisotopic_mass": ["244.08816"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]}, "synonyms": ["(+)-cis-Hexahydro-2-oxo-1H-thieno[3,4]imidazole-4-valeric acid", "(3aS,4S,6aR)-Hexahydro-2-oxo-1H-thieno[3,4-d]imidazole-4-valeric acid", "5-(2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl)pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "BIOTIN", "Coenzyme R", "D-(+)-biotin", "D-Biotin", "Vitamin H", "biotin", "biotina", "biotine", "biotinum", "cis-(+)-Tetrahydro-2-oxothieno[3,4]imidazoline-4-valeric acid", "cis-Hexahydro-2-oxo-1H-thieno(3,4)imidazole-4-valeric acid", "cis-Tetrahydro-2-oxothieno(3,4-d)imidazoline-4-valeric acid", "vitamin B7"], "secondary": {"asserted": {"id": "CHEBI:15956", "label": "biotin"}, "exact_current_rows": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[26]", "name": "Folic acid", "primary": {"id": "CHEBI:27470", "label": "folic acid"}, "canonical_label": "folic acid", "label_equal": true, "definition": ["An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND606960789", "cas:59-30-3", "chemspider:5815", "drugbank:DB00158", "drugcentral:1231", "foodb.food:FDB014504", "hmdb:HMDB0000121", "kegg.compound:C00504", "kegg.drug:D00070", "knapsack:C00001539", "lincs.smallmolecule:LSM-5355", "metacyc.compound:CPD-12826", "pdb-ccd:FOL", "pubmed:10138938", "pubmed:10897644", "pubmed:10958818", "pubmed:11261364", "pubmed:11451208", "pubmed:11959400", "pubmed:14387833", "pubmed:15321809", "pubmed:15523939", "pubmed:15754725", "pubmed:15797531", "pubmed:15797685", "pubmed:15831910", "pubmed:15990733", "pubmed:16093404", "pubmed:16277678", "pubmed:16380297", "pubmed:16871332", "pubmed:17784727", "pubmed:18788725", "pubmed:19121630", "pubmed:19335717", "pubmed:19355913", "pubmed:24650098", "pubmed:33624660", "pubmed:33965562", "pubmed:33968971", "pubmed:34207319", "pubmed:34219855", "pubmed:7738698", "pubmed:8235383", "pubmed:9040515", "pubmed:9420019", "pubmed:9565830", "pubmed:9683174", "pubmed:9781393", "pubmed:9808640", "pubmed:9808641", "reaxys:100781", "wikipedia.en:Folic_Acid"], "generalized_empirical_formula": ["C19H19N7O6"], "has_alternative_id": ["CHEBI:24075", "CHEBI:42610", "CHEBI:5140", "CHEBI:569217"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:27470"], "inchi_key_string": ["OVBPIULPVIDEAO-LBPRGKRZSA-N"], "inchi_string": ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"], "mass": ["441.404"], "monoisotopic_mass": ["441.13968"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]}, "synonyms": ["(2S)-2-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzamido)pentanedioic acid", "Acfol", "Folate", "Folicet", "Folsaeure", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-[(4-{[(2-amino-4-oxo-1,4-dihydropteridin-6-yl)methyl]amino}phenyl)carbonyl]-L-glutamic acid", "N-pteroyl-L-glutamic acid", "PGA", "PteGlu", "acide folique", "acido folico", "acidum folicum", "folic acid", "pteroyl-L-glutamic acid", "pteroyl-L-monoglutamic acid", "pteroylglutamic acid", "pteroylmonoglutamic acid", "vitamin B11", "vitamin B9", "vitamin Bc", "vitamin Be", "vitamin M"], "secondary": {"asserted": {"id": "CHEBI:27470", "label": "folic acid"}, "exact_current_rows": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[27]", "name": "Pyridoxine hydrochloride", "primary": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "canonical_label": "pyridoxine hydrochloride", "label_equal": true, "definition": ["The hydrochloride salt of pyridoxine."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND500675659", "beilstein:3632435", "cas:58-56-0", "drugbank:DBSALT000151", "foodb.food:FDB000575", "gmelin:1067921", "kegg.drug:D02179", "pubmed:15098856", "pubmed:17416572", "pubmed:17891511", "pubmed:18243627", "pubmed:19481898", "pubmed:20645279", "pubmed:21781646", "pubmed:24421551", "pubmed:27468034", "pubmed:28095734", "pubmed:32460509", "pubmed:33209152", "pubmed:33936292", "pubmed:34140989"], "generalized_empirical_formula": ["C8H11NO3.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30961"], "inchi_key_string": ["ZUFQODAHGAHPFQ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H11NO3.ClH/c1-5-8(12)7(4-11)6(3-10)2-9-5;/h2,10-12H,3-4H2,1H3;1H"], "mass": ["205.641"], "monoisotopic_mass": ["205.05057"], "smiles_string": ["Cc1ncc(CO)c(CO)c1O.Cl"]}, "synonyms": ["2-methyl-3-hydroxy-4,5-bis(hydroxymethyl)pyridine hydrochloride", "3-hydroxy-4,5-dimethylol-alpha-picoline hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "5-hydroxy-6-methyl-3,4-pyridinedimethanol hydrochloride", "pyridoxol hydrochloride", "vitamin B6 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "exact_current_rows": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[28]", "name": "Thiamine HCl", "primary": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "canonical_label": "thiamine hydrochloride", "label_equal": true, "definition": ["A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND605711145", "agr:IND606057536", "beilstein:3642937", "beilstein:3851771", "cas:67-03-8", "chemspider:5967", "drugbank:DBSALT000205", "foodb.food:FDB008416", "gmelin:31154", "gmelin:691133", "kegg.drug:D02094", "pubmed:11548854", "pubmed:12224421", "pubmed:21212548", "pubmed:22305197", "pubmed:24399744", "pubmed:25977858", "pubmed:26616989", "pubmed:27163892", "pubmed:28763984", "pubmed:28784494", "pubmed:30131156", "pubmed:31270735", "pubmed:31664290", "pubmed:32009117", "pubmed:32562525", "pubmed:32824791", "reaxys:17124533"], "generalized_empirical_formula": ["C12H17N4OS.Cl.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:49105"], "inchi_key_string": ["DPJRMOMPQZCRJU-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C12H17N4OS.2ClH/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H/q+1;;/p-1"], "mass": ["337.276"], "monoisotopic_mass": ["336.05784"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1.Cl.[Cl-]"]}, "synonyms": ["3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "thiamin dichloride", "thiamin hydrochloride", "thiamine HCl", "thiamine chloride hydrochloride", "thiamine dichloride", "thiamine(2+) dichloride", "thiaminium chloride hydrochloride", "vitamin B1 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "exact_current_rows": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[29]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015", "label": "riboflavin"}, "canonical_label": "riboflavin", "label_equal": true, "definition": ["&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:83-88-5", "chemspider:431981", "drugbank:DB00140", "drugcentral:2834", "foodb.food:FDB012160", "hmdb:HMDB0000244", "kegg.compound:C00255", "kegg.drug:D00050", "knapsack:C00001552", "lincs.smallmolecule:LSM-4084", "metacyc.compound:RIBOFLAVIN", "patent:US2807611", "patent:US2876169", "pdb-ccd:RBF", "pubmed:10566553", "pubmed:11399071", "pubmed:11606856", "pubmed:12083520", "pubmed:12354259", "pubmed:12927541", "pubmed:14963913", "pubmed:16273338", "pubmed:16460756", "pubmed:16658098", "pubmed:182198", "pubmed:18832377", "pubmed:19169240", "pubmed:19212411", "pubmed:19854891", "pubmed:22770225", "pubmed:2369885", "pubmed:23818044", "pubmed:24643482", "pubmed:24816110", "pubmed:25108762", "pubmed:25468971", "pubmed:25887755", "pubmed:2631092", "pubmed:29937405", "pubmed:3142982", "pubmed:33154451", "pubmed:33304888", "pubmed:33886098", "pubmed:33892358", "pubmed:34156642", "pubmed:3592624", "pubmed:3878498", "pubmed:4019261", "pubmed:6475825", "pubmed:6546833", "pubmed:6650303", "pubmed:7101408", "pubmed:7883462", "pubmed:8487103", "pubmed:8604671", "pubmed:8678471", "pubmed:8976642", "pubmed:9184778", "pubmed:9808225", "pubmed:9874201", "reaxys:97831", "wikipedia.en:Riboflavin"], "generalized_empirical_formula": ["C17H20N4O6"], "has_alternative_id": ["CHEBI:15044", "CHEBI:27299", "CHEBI:45214", "CHEBI:529204", "CHEBI:8843"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17015"], "inchi_key_string": ["AUNGANRZJHBGPY-SCRDCRAPSA-N"], "inchi_string": ["InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23)14(25)12(24)6-22)15-13(18-9)16(26)20-17(27)19-15/h3-4,11-12,14,22-25H,5-6H2,1-2H3,(H,20,26,27)/t11-,12+,14-/m0/s1"], "mass": ["376.369"], "monoisotopic_mass": ["376.13828"], "smiles_string": ["Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)CO)c2cc1C"]}, "synonyms": ["1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol", "5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "6,7-dimethyl-9-D-ribitylisoalloxazine", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine", "7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-ribitylisoalloxazine", "Aqua-Flave", "Beflavin", "Beflavine", "Bisulase", "Dermadram", "E101", "Fiboflavin", "Flavaxin", "Flavin Bb", "Flaxain", "Hyflavin", "Vitamin B2", "lactoflavin", "riboflavin (vit B2)", "riboflavin", "riboflavina", "riboflavine", "riboflavinum", "vitamin B2", "vitamin G", "vitasan B2"], "secondary": {"asserted": {"id": "CHEBI:17015", "label": "riboflavin"}, "exact_current_rows": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[30]", "name": "Nicotinic acid", "primary": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "canonical_label": "nicotinic acid", "label_equal": true, "definition": ["A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND607088605", "cas:59-67-6", "chemspider:913", "drugbank:DB00627", "drugcentral:2835", "foodb.food:FDB001014", "gmelin:3340", "hmdb:HMDB0001488", "kegg.compound:C00253", "kegg.drug:D00049", "knapsack:C00000208", "lincs.smallmolecule:LSM-4676", "metacyc.compound:NIACINE", "pdb-ccd:NIO", "pubmed:10540864", "pubmed:113218", "pubmed:12563315", "pubmed:12789870", "pubmed:135660", "pubmed:14550884", "pubmed:15037193", "pubmed:15183629", "pubmed:15205990", "pubmed:15311728", "pubmed:15627518", "pubmed:15651982", "pubmed:16018787", "pubmed:16172771", "pubmed:16322787", "pubmed:16400392", "pubmed:16449845", "pubmed:16767301", "pubmed:16877271", "pubmed:16945375", "pubmed:18037924", "pubmed:182198", "pubmed:186078", "pubmed:18993152", "pubmed:18996527", "pubmed:19369827", "pubmed:19592242", "pubmed:19678716", "pubmed:19779335", "pubmed:20979384", "pubmed:21632263", "pubmed:22116693", "pubmed:22155410", "pubmed:22229411", "pubmed:22366213", "pubmed:22458880", "pubmed:22770225", "pubmed:24029555", "pubmed:24568240", "pubmed:24675661", "pubmed:24848081", "pubmed:24975217", "pubmed:25040591", "pubmed:25241762", "pubmed:25429652", "pubmed:32954525", "pubmed:33273654", "pubmed:33932650", "pubmed:34066686", "pubmed:34085526", "pubmed:34117670", "pubmed:4033386", "pubmed:4259917", "pubmed:582105", "pubmed:699281", "pubmed:7217784", "pubmed:7581845", "pubmed:8306147", "pubmed:8423912", "pubmed:8679452", "pubmed:9107536", "reaxys:109591", "wikipedia.en:Niacin"], "generalized_empirical_formula": ["C6H5NO2"], "has_alternative_id": ["CHEBI:25538", "CHEBI:44319", "CHEBI:7559"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15940"], "inchi_key_string": ["PVNIIMVLHYAWGP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"], "mass": ["123.111"], "monoisotopic_mass": ["123.03203"], "smiles_string": ["O=C(O)c1cccnc1"]}, "synonyms": ["3-Pyridylcarboxylic acid", "3-carboxylpyridine", "3-carboxypyridine", "3-pyridinecarboxylic acid", "NICOTINIC ACID", "NICOTINIC ACID", "Niacin", "Niacor", "Niaspan", "Nicotinic acid", "Nicotinic acid", "Nicotinsaure", "Nikotinsaeure", "P.P. factor", "PP factor", "acide nicotinique", "acido nicotinico", "acidum nicotinicum", "anti-pellagra vitamin", "beta-pyridinecarboxylic acid", "m-pyridinecarboxylic acid", "nicotinic acid", "nicotinic acid", "pellagra preventive factor", "pyridine-3-carboxylic acid", "pyridine-3-carboxylic acid", "pyridine-beta-carboxylic acid", "pyridine-carboxylique-3", "vitamin B3"], "secondary": {"asserted": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "exact_current_rows": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[31]", "name": "Calcium D-(+)-pantothenate", "primary": {"id": "CHEBI:31345", "label": "Calcium pantothenate"}, "canonical_label": "Calcium pantothenate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:137-08-6", "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278", "pubmed:20553011", "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula": ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"], "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"], "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]}, "synonyms": ["Calcium pantotenate", "Calcium pantothenate", "Calcium pantothenate, d-", "Calpan", "D-ca pantothenate", "D-calcium pantothenate", "NSC-36292", "Pantholin", "Pantothenic acid (as calcium)", "Pantothenic acid calcium salt", "Vitamin b5, calcium salt", "pantotenato de calcio", "pantothenate de calcium"]}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[32]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843", "label": "vitamin B12"}, "canonical_label": "vitamin B12", "label_equal": true, "definition": ["Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives)."], "annotations": {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:176843"]}, "synonyms": ["vitamin B-12", "vitamin B12 vitamer", "vitamin B12 vitamers", "vitamin B12", "vitamins B12"], "secondary": {"asserted": {"id": "CHEBI:176843", "label": "vitamin B12"}, "exact_current_rows": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[33]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "canonical_label": "4-aminobenzoic acid", "label_equal": true, "definition": ["An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:150-13-0", "drugbank:DB02362", "drugcentral:2049", "ecmdb:ECMDB01392", "gmelin:50150", "hmdb:HMDB0001392", "kegg.compound:C00568", "kegg.drug:D02456", "knapsack:C00001401", "pdb-ccd:PAB", "pubmed:12039592", "pubmed:14745019", "pubmed:15115392", "pubmed:1527790", "pubmed:16290145", "pubmed:17149871", "pubmed:17743450", "pubmed:17800214", "pubmed:19469519", "pubmed:22767283", "pubmed:22994574", "pubmed:23063996", "pubmed:23084339", "pubmed:23144588", "pubmed:23471007", "pubmed:3599019", "pubmed:3820215", "pubmed:3950915", "pubmed:8411009", "pubmed:9406595", "reaxys:471605", "wikipedia.en:4-Aminobenzoic_acid", "ymdb:YMDB00493"], "generalized_empirical_formula": ["C7H7NO2"], "has_alternative_id": ["CHEBI:113372", "CHEBI:1783", "CHEBI:20315", "CHEBI:44778"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30753"], "inchi_key_string": ["ALYNCZNDIQEVRV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"], "mass": ["137.138"], "monoisotopic_mass": ["137.04768"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]}, "synonyms": ["1-Amino-4-carboxybenzene", "4-AMINOBENZOIC ACID", "4-AMINOBENZOIC ACID", "4-Amino-benzoic acid", "4-Aminobenzoesaeure", "4-Aminobenzoic acid", "4-Aminobenzoic acid", "4-Carboxyaniline", "4-Carboxyphenylamine", "4-aminobenzoic acid", "4-aminobenzoic acid", "ABEE", "PABA", "gamma-Aminobenzoic acid", "gamma-aminobenzoic acid", "p-Aminobenzoesaeure", "p-aminobenzoic acid", "p-carboxyaniline", "p-carboxyphenylamine", "para-aminobenzoic acid"], "secondary": {"asserted": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "exact_current_rows": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field": "ingredients[34]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id": "CHEBI:16494", "label": "lipoic acid"}, "canonical_label": "lipoic acid", "label_equal": true, "definition": ["A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:122410", "cas:62-46-4", "drugbank:DB00166", "drugcentral:4732", "ecmdb:ECMDB01451", "gmelin:720915", "kegg.compound:C00725", "kegg.drug:D00086", "pubmed:15328413", "pubmed:7519986", "pubmed:7548757", "reaxys:81853", "wikipedia.en:Lipoic_acid", "ymdb:YMDB00334"], "generalized_empirical_formula": ["C8H14O2S2"], "has_alternative_id": ["CHEBI:146958", "CHEBI:25058", "CHEBI:6492"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16494"], "inchi_key_string": ["AGBQKNBQESQNJD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H14O2S2/c9-8(10)4-2-1-3-7-5-6-11-12-7/h7H,1-6H2,(H,9,10)"], "mass": ["206.332"], "monoisotopic_mass": ["206.04352"], "smiles_string": ["O=C(O)CCCCC1CCSS1"]}, "synonyms": ["1,2-dithiolane-3-pentanoic acid", "1,2-dithiolane-3-valeric acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)valeric acid", "5-(dithiolan-3-yl)valeric acid", "5-[3-(1,2-dithiolanyl)]pentanoic acid", "6,8-thioctic acid", "6,8-thiotic acid", "6-thioctic acid", "6-thiotic acid", "Acetate-replacing factor", "Biletan", "Lipoic acid", "Thioctansaeure", "Thioctic acid", "Thioctsaeure", "Thioktsaeure", "alpha-Lipoic acid", "alpha-Liponsaeure", "alpha-lipoic acid", "liponic acid"], "secondary": {"asserted": {"id": "CHEBI:16494", "label": "lipoic acid"}, "exact_current_rows": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}], "legacy": []} |
| importer | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _parse_api_solutions; _normalize_unit | context_only | Current importer selects main ingredients, preserves solution_id and percentage-stock rows and maps ml as ML_PER_L. This does not validate old flattened values or prove their precise historical cause. |
| resolver | src/culturemech/enrich/dsmz_resolver.py; merge_composition; _add_enrichment_metadata | context_only | Current resolver copies ingredients/solutions and selected metadata but not preparation in this method, retaining an existing scalar pH. It writes timezone-naive local timestamps. The present code is contextual, not a replay of the historical import. |
| cleanup | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current cleanup no longer sums unequal duplicates. Actual owner notes retain earlier NaCl, magnesium, calcium and iron sums across stock stages, which require source-specific curation. |
| history | data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml; Every target and maintained owner history and ingredient curation timestamp | refutes | [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[0].timestamp", "value": "2026-01-27T01:15:02.fZ", "valid_ISO_datetime": false, "timezone_aware": false}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:18.940996", "valid_ISO_datetime": true, "timezone_aware": false}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[2].timestamp", "value": "2026-02-06T05:10:54.113555Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[3].timestamp", "value": "2026-03-13T03:09:42.427704Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[4].timestamp", "value": "2026-03-13T06:19:25.750970Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[5].timestamp", "value": "2026-03-17T06:30:54.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[6].timestamp", "value": "2026-03-17T19:45:40.702498+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[7].timestamp", "value": "2026-06-05T07:40:21.357759+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[8].timestamp", "value": "2026-06-10T07:46:44.288307+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[9].timestamp", "value": "2026-08-06T03:04:43.901578+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[10].timestamp", "value": "2026-08-06T03:04:43.901623+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[0].timestamp", "value": "2026-01-27T01:15:02.fZ", "valid_ISO_datetime": false, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:18.940996", "valid_ISO_datetime": true, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[2].timestamp", "value": "2026-02-06T05:10:54.113555Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[3].timestamp", "value": "2026-03-13T03:09:42.427704Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[4].timestamp", "value": "2026-03-13T06:19:25.750970Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[5].timestamp", "value": "2026-03-17T06:30:54.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[6].timestamp", "value": "2026-03-17T19:45:40.702498+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[7].timestamp", "value": "2026-06-05T07:40:21.357759+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path": "curation_history[8].timestamp", "value": "2026-06-10T07:46:44.288307+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "curation_history[0].timestamp", "value": "2026-01-26T17:53:10.381491Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "curation_history[1].timestamp", "value": "2026-02-06T05:10:38.188874Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "curation_history[2].timestamp", "value": "2026-03-13T03:09:18.337390Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "curation_history[3].timestamp", "value": "2026-03-13T06:19:01.575354Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "curation_history[4].timestamp", "value": "2026-03-17T06:30:26.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "curation_history[5].timestamp", "value": "2026-03-17T19:45:13.309524+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "curation_history[6].timestamp", "value": "2026-05-20T06:01:07.039986+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "curation_history[7].timestamp", "value": "2026-06-05T07:40:46.684516+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field_path": "curation_history[8].timestamp", "value": "2026-06-10T07:46:52.368320+00:00", "valid_ISO_datetime": true, "timezone_aware": true}] |
| merge | src/culturemech/merge/merger.py; RecipeMerger; merge_formulation_evidence; maintained formulation-aware merge context | context_only | The target is a generated merge with the exact normalized contributors pinned by inspection. The old ingredient-set fingerprint is not concentration, preparation or source equivalence. Current formulation-aware merging preserves only compatible assertions. No merge was run; verify owners and preview current grouping before separately authorized regeneration. |
| exporter | src/culturemech/export/kgx_export.py; medium_to_ingredient_edge; medium_to_solution_edge; _resolved_ingredient_id; _quantity | context_only | Current export consumes structured ingredient/solution identities and quantities, resolving against the pinned MIM index before fallback. It does not independently recover missing stock stages, source qualifiers or final volume. No export or resulting edge count is claimed. |

## Limits And Additional Notes

- The provider declares 1001 mL for the main solution; the listed liquid additions sum 1001.5 mL, and preparation mentions later sterile stocks without all dose volumes. Neither value is presented as independently measured final volume.
- Stock dilution calculations use the explicitly stated provider basis conditionally. They are not applied corrections and do not authorize double-counting expanded ingredients and stock doses.
- The source lists cellulose grades as alternatives to cellobiose. No selected branch or composition of Kleenex/HCl-treated cotton is inferred, and no branch-specific DEFINED/COMPLEX replacement is invented.
- Source accessions identify recipes, not strains. No taxonomic, growth, assembly or optimal-condition claim is inferred from the medium title.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T100542Z-culturemech-004192-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acetivibrio_cellulolyticus_medium (CultureMech:004192)'
started_at: '2026-10-21T09:56:43Z'
finished_at: '2026-10-21T10:05:42Z'
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
summary: 'KOMODO 165 and the exact DSMZ 165 recipe identify the medium, but the generated
  target and both owners flatten five stocks and sum amounts from distinct stages.
  Sulfuric acid is especially misrepresented: 1000 mL of 0.1 N acid used in a ferrous
  stock becomes 1000 g/L in the medium. The generated/KOMODO representations also
  lose the DSMZ owner preparation and the cellulose-for-cellobiose alternative. Nickel
  hydrate and sodium-resazurin mappings disagree with the supplied forms. All four
  diagnostics pass; four inherited timestamps remain malformed or timezone-naive.'
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
  - path: data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
    sha256: 65ddef94343cc1a757935a7941b49389e69697e9dc8957c4d139305dbecfc8ca
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
    sha256: 2d3abaaba7577ac182c119c513ead08eff805820455b3de2d18ed4ee72183e98
    role: context
  - path: data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml
    sha256: a57ed8bd827d95bc0180e6e4f57b04724af65f8a3b8459e2abb164bc22a22734
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
  selection: Task review 143; batch 015 item 3 of 10, selected in Python lexicographic
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
  - CultureMech:004192
targets:
- target_id: CultureMech:004192
  path: data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
  label: acetivibrio_cellulolyticus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:004192
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch015/143/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch015/143/strict.tsv"
  target_ids:
  - CultureMech:004192
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:004192
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:004192
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
  - CultureMech:004192
- check_id: scoped-history
  name: Scoped timestamp syntax and timezone inspection
  required: false
  status: failed
  summary: 29 timestamps inspected, 4 invalid or timezone-naive; old provenance remains
    unchanged.
  target_ids:
  - CultureMech:004192
  evidence_ids:
  - history
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T10:05:42Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:05:42Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:05:42Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:57:56.481171Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch015/143/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T09:57:59.550345Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch015/143/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:58:03.252523Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:58:05.530234Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: source-catalog
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch015/source-preflight-bound/143/source-catalog.json
  locator: Complete bound per-record catalog, raw/text/metadata hashes and actual
    original capture times
  accessed_at: '2026-10-21T10:05:42Z'
  support: context_only
  summary: '[{"key": "komodoMediaList", "url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
    "status": 200, "accessed_at": "2026-10-19T23:42:38.189631Z", "sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a",
    "metadata_sha256": "30928bcdb2a03f00076baf3d9b9ac299b82966aeb81f08b2b71f21d0d0bcffb5",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/140/komodoMediaList.json"},
    {"key": "dsmz165", "url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf",
    "status": 200, "accessed_at": "2026-10-21T09:46:49.704361Z", "sha256": "d9fb409f692ec6f6dee9a2dc6def7d9cb3e6817d80d3a94684c98740c2dc6f87",
    "metadata_sha256": "77b9c62706e539ae0213e8d0d8b99efb19fd75837a1912fedc504c80018f66b0",
    "content_limit": null, "reused_capture_from": null}, {"key": "mediadive165api",
    "url": "https://mediadive.dsmz.de/rest/medium/165", "status": 200, "accessed_at":
    "2026-10-21T09:46:48.818058Z", "sha256": "aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2",
    "metadata_sha256": "c609b5f6bde5688045f285a9232382cb7670536b10e0257a30ea564a8643f6b6",
    "content_limit": null, "reused_capture_from": null}, {"key": "chebi131361", "url":
    "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361",
    "status": 200, "accessed_at": "2026-10-21T07:33:27.980786Z", "sha256": "643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10",
    "metadata_sha256": "5d44d78951b5b99db68dfdd05054154c671875341a46403fdc8d27437540ddb1",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi131361.json"},
    {"key": "chebi131527", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527",
    "status": 200, "accessed_at": "2026-10-20T07:22:08.349487Z", "sha256": "349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3",
    "metadata_sha256": "aba7fec29187e4c7bc3a8a54feeedbb3806ec0426ce879dbd520a44a35468d79",
    "content_limit": "Identity/provenance and exact identifier metadata only; no operational
    formulation or culture-procedure assessment.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/139/chebi131527.json"},
    {"key": "chebi15940", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940",
    "status": 200, "accessed_at": "2026-10-20T06:55:11.874279Z", "sha256": "3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1",
    "metadata_sha256": "278ba834982df08ae7c95c23b926035d15f9042dc4e44ffb88d50e2a0ebd4a3a",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15940.json"},
    {"key": "chebi15956", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956",
    "status": 200, "accessed_at": "2026-10-21T08:42:30.425993Z", "sha256": "d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd",
    "metadata_sha256": "0da9b84b7103b8ff5cafc029c9c6659c18d1443961c6c1e08777f11bffd97c5b",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15956.json"},
    {"key": "chebi16494", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494",
    "status": 200, "accessed_at": "2026-10-20T06:55:13.001958Z", "sha256": "aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1",
    "metadata_sha256": "38201a72db2e1cd4730248b9f9b2cc30446eeadb363aa164541dc5bda3842eca",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/129/chebi16494.json"},
    {"key": "chebi17015", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015",
    "status": 200, "accessed_at": "2026-10-20T06:55:11.583596Z", "sha256": "f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4",
    "metadata_sha256": "b174d58ee7a958d55e27e18fdf27f848d5fde113702d1d09f473be6cda5ea8a5",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi17015.json"},
    {"key": "chebi17057", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057",
    "status": 200, "accessed_at": "2026-10-21T09:27:39.796651Z", "sha256": "3548f79d3274a33683125152944998cffa00bd4fce774c8d872db9003222ed06",
    "metadata_sha256": "e419fc989c1340514749cb79f20ed3a81c93ce9f6ecf2254c32a23604fae594f",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/133/chebi17057.json"},
    {"key": "chebi176843", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843",
    "status": 200, "accessed_at": "2026-10-21T08:17:26.997779Z", "sha256": "b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9",
    "metadata_sha256": "859d21e6b301f60e533507c16b7f0f85177f0cc295bb35589e692ce6407cf6f0",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi176843.json"},
    {"key": "chebi18246", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18246",
    "status": 200, "accessed_at": "2026-10-21T09:46:50.902901Z", "sha256": "f7abaf5dd620c7de0e80d8e5718cbab4fa7a6455577d0a176847d4e8829be90c",
    "metadata_sha256": "4fdf55bc4468100dc2f3e75e26fa45e05404dd3e495008c4f207db579be7e80a",
    "content_limit": null, "reused_capture_from": null}, {"key": "chebi26710", "url":
    "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710",
    "status": 200, "accessed_at": "2026-10-21T08:42:42.219040Z", "sha256": "2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e",
    "metadata_sha256": "e0382f73927eabf48723fea9777a995e4bfa23ab150b3001948cfcfffc60cf95",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi26710.json"},
    {"key": "chebi26836", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836",
    "status": 200, "accessed_at": "2026-10-20T07:29:13.222926Z", "sha256": "19e202cd697eed2be3130d5b0b29cc0c1d18575ad103110877303ee678779737",
    "metadata_sha256": "fb7282192b913ddd73c808d7b751c3a508689bd8601894cd945f264a1228f4dd",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/132/chebi26836.json"},
    {"key": "chebi27470", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470",
    "status": 200, "accessed_at": "2026-10-20T06:55:10.450814Z", "sha256": "fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f",
    "metadata_sha256": "9e8e57c5284b980b5aa17435d9505822ebd06e287db0bf493ea8920154d9cf6a",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi27470.json"},
    {"key": "chebi29377", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377",
    "status": 200, "accessed_at": "2026-10-21T07:31:16.500548Z", "sha256": "21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1",
    "metadata_sha256": "77182343b05bacc1609ae5c11cc2089160d43fa53fb520181dcea1f5d3402106",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/133/chebi29377.json"},
    {"key": "chebi30753", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753",
    "status": 200, "accessed_at": "2026-10-20T06:55:12.829785Z", "sha256": "97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a",
    "metadata_sha256": "fb67c8541d62fb8bd8ae6ea3a09093bbc436b3e1e7b66a85873057066111e61c",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi30753.json"},
    {"key": "chebi30961", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961",
    "status": 200, "accessed_at": "2026-10-21T08:42:44.571163Z", "sha256": "f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d",
    "metadata_sha256": "3536eeeda597cc3f7d3801c48cb4cf60e25acd9eccfd2ac09a70480f3e807498",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi30961.json"},
    {"key": "chebi31345", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345",
    "status": 200, "accessed_at": "2026-10-20T06:55:12.450283Z", "sha256": "56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d",
    "metadata_sha256": "416294de70d6830383c166ab53a10432a014f76693d277eb0fc6ec5d79281596",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi31345.json"},
    {"key": "chebi31440", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440",
    "status": 200, "accessed_at": "2026-10-21T08:17:28.489501Z", "sha256": "e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9",
    "metadata_sha256": "12ee42b288c244804759ab710c027ddb0c6c9e84ea74fb3143ebfb10b55d0c3e",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi31440.json"},
    {"key": "chebi31795", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795",
    "status": 200, "accessed_at": "2026-10-21T08:42:45.232212Z", "sha256": "45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb",
    "metadata_sha256": "87aa39e726d0dfb956224cc3184e7f2c1be3a6321fe87f9970f63a887d7b4713",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/140/chebi31795.json"},
    {"key": "chebi32312", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312",
    "status": 200, "accessed_at": "2026-10-21T08:17:28.879505Z", "sha256": "eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9",
    "metadata_sha256": "dbd95f34340e0738d58dade746941220627116ed30e84e78d0dadd929d4a152e",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi32312.json"},
    {"key": "chebi33118", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118",
    "status": 200, "accessed_at": "2026-10-21T08:17:29.364390Z", "sha256": "f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87",
    "metadata_sha256": "9823d8f911fabf1b9c9d90b526371b4c6e7530b655a124021f4b63fbec2f6df3",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi33118.json"},
    {"key": "chebi34887", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887",
    "status": 200, "accessed_at": "2026-10-21T08:04:44.093348Z", "sha256": "f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc",
    "metadata_sha256": "a062ba8057ab64ce0563bbf34b48539314d319ed573a2dd021e96e8eb7ebc0e2",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi34887.json"},
    {"key": "chebi44557", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557",
    "status": 200, "accessed_at": "2026-10-21T08:46:15.250117Z", "sha256": "de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2",
    "metadata_sha256": "95bb74bc642b7d04229226a2c41b9753c003b85dc3cb555e91877f9c9c38faca",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi44557.json"},
    {"key": "chebi49105", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105",
    "status": 200, "accessed_at": "2026-10-20T06:55:10.911379Z", "sha256": "0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4",
    "metadata_sha256": "b91259f77f726aa843dfe458caf0385142a7ee96b6d2ff44962e8a6216900df0",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi49105.json"},
    {"key": "chebi62946", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946",
    "status": 200, "accessed_at": "2026-10-21T08:43:02.566401Z", "sha256": "10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5",
    "metadata_sha256": "a1e2087355e82043f5be7288ebed6f8ab8cbfdebd53011232aef45e19175eec5",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/128/chebi62946.json"},
    {"key": "chebi63036", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036",
    "status": 200, "accessed_at": "2026-10-21T08:17:29.666916Z", "sha256": "48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3",
    "metadata_sha256": "5cd56ae554a6253e89c1c4d59c748a4d8317e4d50f36ed7630254546676fb064",
    "content_limit": "Identity/provenance and exact identifier metadata only; no operational
    formulation or culture-procedure assessment.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/139/chebi63036.json"},
    {"key": "chebi63939", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939",
    "status": 200, "accessed_at": "2026-10-20T06:55:09.796192Z", "sha256": "987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a",
    "metadata_sha256": "8c032341c1a6b15dac7678091c6975c069edebe9da22033b56f1def86e880ddd",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi63939.json"},
    {"key": "chebi75213", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213",
    "status": 200, "accessed_at": "2026-10-21T08:17:29.756647Z", "sha256": "b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083",
    "metadata_sha256": "b1c20b370483e053434ad0326c01e497cd8bfffd8f35c39849a7f13c51c0d917",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/136/chebi75213.json"},
    {"key": "chebi75836", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836",
    "status": 200, "accessed_at": "2026-10-20T06:55:07.038393Z", "sha256": "14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525",
    "metadata_sha256": "a67ef16d6982948181b6ffcaa5b7fb60f01395984f15dbcef47d22b89f3b0742",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi75836.json"},
    {"key": "chebi76209", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209",
    "status": 200, "accessed_at": "2026-10-20T06:55:04.847843Z", "sha256": "f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c",
    "metadata_sha256": "dc171ad292a4aa60637997f5ea8e33445dd20bece656874532f77ef2a8ed042f",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi76209.json"},
    {"key": "chebi86158", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158",
    "status": 200, "accessed_at": "2026-10-21T08:17:30.011607Z", "sha256": "b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61",
    "metadata_sha256": "5f2731864627245c55ffd72fece700a4c38708d4e012db3f84fed6082bd5b8db",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi86158.json"},
    {"key": "chebi86364", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364",
    "status": 200, "accessed_at": "2026-10-21T07:33:35.036768Z", "sha256": "f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069",
    "metadata_sha256": "56ac3d72114b46620bb2e8c277cfc2a4e64eb2bc6d44627ca2c89f9d6f5d50a7",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/134/chebi86364.json"},
    {"key": "chebi86465", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465",
    "status": 200, "accessed_at": "2026-10-20T06:55:08.054799Z", "sha256": "5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c",
    "metadata_sha256": "c59ef7887fb48413e94272e2b074ec89f12a16f7b3e50ba4331369294f4c8a0d",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi86465.json"},
    {"key": "chebi8806", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806",
    "status": 200, "accessed_at": "2026-10-21T08:17:30.774007Z", "sha256": "e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5",
    "metadata_sha256": "dcd51a6da87370a91395f3c0583d8632b494b3f441318d9106664896fc5dc1e7",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi8806.json"},
    {"key": "chebi91244", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244",
    "status": 200, "accessed_at": "2026-10-20T06:55:07.079384Z", "sha256": "dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa",
    "metadata_sha256": "b6b1af84fbd1f1f98a674c7b3d3439d2bd5207f16cf1ac6d6541f935b63016f9",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-work-batch004/sources/chebi91244.json"},
    {"key": "chebi91248", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248",
    "status": 200, "accessed_at": "2026-10-21T08:42:32.136441Z", "sha256": "7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683",
    "metadata_sha256": "77ade3f6455526983b08c040e632f2ab50a091385f21a60e8a2a7fb278a5ac89",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/133/chebi91248.json"}]'
  snapshot_sha256: 696e623ae58cc7909d15a21cd28e8ab45cfa475758fe0246a19041775d84bc57
- evidence_id: dsmz165
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf
  locator: pages 1–2, complete main recipe and five stock sections
  accessed_at: '2026-10-21T09:46:49.704361Z'
  support: supports
  summary: DSMZ 165 ACETIVIBRIO CELLULOLYTICUS MEDIUM, two-page collection recipe.
    Both pages were inspected visually and in extracted text, including the acid normality,
    five stock definitions, cellulose alternatives and preparation. Footer ©2022 DSMZ
    is preserved without inventing individual authors or a separately verified publication
    date.
  snapshot_sha256: d9fb409f692ec6f6dee9a2dc6def7d9cb3e6817d80d3a94684c98740c2dc6f87
- evidence_id: mediadive165api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.medium; $.data.solutions[0:6]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: Exact MediaDive medium 165 response, main 283 and stocks 284/285/241/5861/5980,
    with all amounts, stock doses, declared volumes, optional flag and source-specific
    preparation.
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: komodoMediaList
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: MediaList table row with first cell 165
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: context_only
  summary: Exact KOMODO row 165 links DSMZ Medium165.pdf, gives pH 7.2 and Aerobic=true,
    and has is_complex=false. These catalog fields are preserved as provenance and
    compared with the primary; they are not organism phenotypes or independent formulation
    evidence.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: quantity-1
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[0].recipe[0]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: The main recipe explicitly adds 75 ml of stock 284. Restore this dose and
    the separate stock definition; the stored flat ingredient strengths do not encode
    its dilution.
  quote: "{\n                        \"recipe_order\": 1,\n                      \
    \  \"solution\": \"Mineral solution 1\",\n                        \"solution_id\"\
    : 284,\n                        \"amount\": 75,\n                        \"unit\"\
    : \"ml\",\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-2
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[0].recipe[1]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: The main recipe explicitly adds 75 ml of stock 285. Restore this dose and
    the separate stock definition; the stored flat ingredient strengths do not encode
    its dilution.
  quote: "{\n                        \"recipe_order\": 2,\n                      \
    \  \"solution\": \"Mineral solution 2\",\n                        \"solution_id\"\
    : 285,\n                        \"amount\": 75,\n                        \"unit\"\
    : \"ml\",\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-3
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[0].recipe[2]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: The main recipe explicitly adds 10 ml of stock 241. Restore this dose and
    the separate stock definition; the stored flat ingredient strengths do not encode
    its dilution.
  quote: "{\n                        \"recipe_order\": 3,\n                      \
    \  \"solution\": \"Modified Wolin's mineral solution\",\n                    \
    \    \"solution_id\": 241,\n                        \"amount\": 10,\n        \
    \                \"unit\": \"ml\",\n                        \"optional\": 0\n\
    \                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-4
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[0].recipe[3]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: The main recipe explicitly adds 20 ml of stock 5861. Restore this dose
    and the separate stock definition; the stored flat ingredient strengths do not
    encode its dilution.
  quote: "{\n                        \"recipe_order\": 4,\n                      \
    \  \"solution\": \"FeSO4 x 7 H2O solution (0.1% w/v)\",\n                    \
    \    \"solution_id\": 5861,\n                        \"amount\": 20,\n       \
    \                 \"unit\": \"ml\",\n                        \"optional\": 0\n\
    \                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-5
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[0].recipe[4]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1001 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 5,\n                      \
    \  \"compound\": \"Sodium resazurin\",\n                        \"compound_id\"\
    : 1852,\n                        \"attribute\": \"0.1% w/v\",\n              \
    \          \"amount\": 0.5,\n                        \"unit\": \"ml\",\n     \
    \                   \"g_l\": 0.0004995,\n                        \"mmol_l\": 0.0019887,\n\
    \                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-6
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[0].recipe[5]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1001 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 6,\n                      \
    \  \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n \
    \                       \"amount\": 1.5,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 1.4985,\n                        \"mmol_l\"\
    : 14.1384,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-7
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[0].recipe[6]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1001 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 7,\n                      \
    \  \"compound\": \"Cellobiose\",\n                        \"compound_id\": 214,\n\
    \                        \"amount\": 3,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 2.997,\n                        \"mmol_l\"\
    : 8.75549,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-8
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[0].recipe[7]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: The source gives cellulose 3 g as an alternative to cellobiose, not an
    extra carbon source added to the same selected recipe. Retain the source amount
    and grade/alternative condition; provider g_l 2.997 follows its declared 1001
    mL basis.
  quote: "{\n                        \"recipe_order\": 8,\n                      \
    \  \"compound\": \"Cellulose\",\n                        \"compound_id\": 400,\n\
    \                        \"attribute\": \"MN300\",\n                        \"\
    amount\": 3,\n                        \"unit\": \"g\",\n                     \
    \   \"g_l\": 2.997,\n                        \"optional\": 1\n               \
    \     }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-9
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[0].recipe[8]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: The main recipe explicitly adds 1 ml of stock 5980. Restore this dose and
    the separate stock definition; the stored flat ingredient strengths do not encode
    its dilution.
  quote: "{\n                        \"recipe_order\": 9,\n                      \
    \  \"solution\": \"Wolin's vitamin solution (10x)\",\n                       \
    \ \"solution_id\": 5980,\n                        \"amount\": 1,\n           \
    \             \"unit\": \"ml\",\n                        \"optional\": 0\n   \
    \                 }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-10
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[0].recipe[9]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1001 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 10,\n                     \
    \   \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\"\
    : 770,\n                        \"amount\": 0.25,\n                        \"\
    unit\": \"g\",\n                        \"g_l\": 0.24975,\n                  \
    \      \"mmol_l\": 1.42198,\n                        \"optional\": 0\n       \
    \             }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-11
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[0].recipe[10]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1001 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 11,\n                     \
    \   \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":\
    \ 54,\n                        \"amount\": 0.25,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.24975,\n                        \"\
    mmol_l\": 1.03984,\n                        \"optional\": 0\n                \
    \    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-12
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[0].recipe[11]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: Preserve the source solvent quantity 820 ml in its own stage. The provider
    declares this solution volume as 1001 mL; water addition is not independent proof
    of measured final volume.
  quote: "{\n                        \"recipe_order\": 12,\n                     \
    \   \"compound\": \"Distilled water\",\n                        \"compound_id\"\
    : 4,\n                        \"amount\": 820,\n                        \"unit\"\
    : \"ml\",\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-13
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[1].recipe[0]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 1,\n                      \
    \  \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n \
    \                       \"amount\": 3.9,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 3.9,\n                        \"mmol_l\"\
    : 22.3911,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-14
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[1].recipe[1]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: Preserve the source solvent quantity 1000 ml in its own stage. The provider
    declares this solution volume as 1000 mL; water addition is not independent proof
    of measured final volume.
  quote: "{\n                        \"recipe_order\": 2,\n                      \
    \  \"compound\": \"Distilled water\",\n                        \"compound_id\"\
    : 4,\n                        \"amount\": 1000,\n                        \"unit\"\
    : \"ml\",\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-15
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[2].recipe[0]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 1,\n                      \
    \  \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n \
    \                       \"amount\": 2.4,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 2.4,\n                        \"mmol_l\"\
    : 17.636,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-16
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[2].recipe[1]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 2,\n                      \
    \  \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n\
    \                        \"amount\": 6,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 6,\n                        \"mmol_l\"\
    : 45.4064,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-17
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[2].recipe[2]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 3,\n                      \
    \  \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n   \
    \                     \"amount\": 0.59,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 0.59,\n                        \"mmol_l\"\
    : 10.0958,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-18
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[2].recipe[3]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 4,\n                      \
    \  \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":\
    \ 8,\n                        \"amount\": 1.2,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 1.2,\n                        \"mmol_l\"\
    : 4.86863,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-19
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[2].recipe[4]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 5,\n                      \
    \  \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":\
    \ 7,\n                        \"amount\": 0.72,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.72,\n                        \"mmol_l\"\
    : 4.89746,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-20
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[2].recipe[5]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: Preserve the source solvent quantity 1000 ml in its own stage. The provider
    declares this solution volume as 1000 mL; water addition is not independent proof
    of measured final volume.
  quote: "{\n                        \"recipe_order\": 6,\n                      \
    \  \"compound\": \"Distilled water\",\n                        \"compound_id\"\
    : 4,\n                        \"amount\": 1000,\n                        \"unit\"\
    : \"ml\",\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-21
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[0]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 1,\n                      \
    \  \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\"\
    : 189,\n                        \"amount\": 1.5,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\"\
    : 7.84765,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-22
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[1]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 2,\n                      \
    \  \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":\
    \ 8,\n                        \"amount\": 3,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\"\
    : 12.1716,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-23
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[2]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 3,\n                      \
    \  \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n\
    \                        \"amount\": 0.5,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\"\
    : 2.9583,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-24
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[3]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 4,\n                      \
    \  \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n   \
    \                     \"amount\": 1,\n                        \"unit\": \"g\"\
    ,\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n\
    \                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-25
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[4]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 5,\n                      \
    \  \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":\
    \ 12,\n                        \"amount\": 0.1,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\"\
    : 0.359693,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-26
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[5]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 6,\n                      \
    \  \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\":\
    \ 198,\n                        \"amount\": 0.18,\n                        \"\
    unit\": \"g\",\n                        \"g_l\": 0.18,\n                     \
    \   \"mmol_l\": 1.16132,\n                        \"optional\": 0\n          \
    \          }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-27
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[6]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 7,\n                      \
    \  \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":\
    \ 7,\n                        \"amount\": 0.1,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\"\
    : 0.680203,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-28
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[7]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 8,\n                      \
    \  \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":\
    \ 35,\n                        \"amount\": 0.18,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\"\
    : 0.625954,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-29
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[8]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 9,\n                      \
    \  \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\":\
    \ 121,\n                        \"amount\": 0.01,\n                        \"\
    unit\": \"g\",\n                        \"g_l\": 0.01,\n                     \
    \   \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n        \
    \            }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-30
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[9]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 10,\n                     \
    \   \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\"\
    : 908,\n                        \"amount\": 0.02,\n                        \"\
    unit\": \"g\",\n                        \"g_l\": 0.02,\n                     \
    \   \"mmol_l\": 0.0421596,\n                        \"optional\": 0\n        \
    \            }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-31
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[10]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 11,\n                     \
    \   \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n \
    \                       \"amount\": 0.01,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\"\
    : 0.161708,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-32
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[11]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 12,\n                     \
    \   \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\"\
    : 9,\n                        \"amount\": 0.01,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\"\
    : 0.0413309,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-33
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[12]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 13,\n                     \
    \   \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\"\
    : 40,\n                        \"amount\": 0.03,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\"\
    : 0.231483,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-34
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[13]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 14,\n                     \
    \   \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\"\
    : 107,\n                        \"amount\": 0.3,\n                        \"unit\"\
    : \"mg\",\n                        \"g_l\": 0.0003,\n                        \"\
    mmol_l\": 0.00114062,\n                        \"optional\": 0\n             \
    \       }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-35
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[14]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 15,\n                     \
    \   \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\"\
    : 249,\n                        \"amount\": 0.4,\n                        \"unit\"\
    : \"mg\",\n                        \"g_l\": 0.0004,\n                        \"\
    mmol_l\": 0.00121267,\n                        \"optional\": 0\n             \
    \       }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-36
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[3].recipe[15]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: Preserve the source solvent quantity 1000 ml in its own stage. The provider
    declares this solution volume as 1000 mL; water addition is not independent proof
    of measured final volume.
  quote: "{\n                        \"recipe_order\": 16,\n                     \
    \   \"compound\": \"Distilled water\",\n                        \"compound_id\"\
    : 4,\n                        \"amount\": 1000,\n                        \"unit\"\
    : \"ml\",\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-37
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[4].recipe[0]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 2,\n                      \
    \  \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":\
    \ 12,\n                        \"amount\": 1,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\"\
    : 3.59693,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-38
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[4].recipe[1]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: The exact row is 1000 mL of 0.1 N H2SO4 in the ferrous sulfate stock. Local
    1000 G_PER_L is a liquid-volume-to-mass-unit error and a stage error. Retain the
    dilute acid solvent and its normality; do not treat it as neat acid or infer density.
  quote: "{\n                        \"recipe_order\": 3,\n                      \
    \  \"compound\": \"H2SO4\",\n                        \"compound_id\": 122,\n \
    \                       \"attribute\": \"0.1 N\",\n                        \"\
    amount\": 1000,\n                        \"unit\": \"ml\",\n                 \
    \       \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-39
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[5].recipe[0]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 1,\n                      \
    \  \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n \
    \                       \"amount\": 20,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\"\
    : 0.0818632,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-40
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[5].recipe[1]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 2,\n                      \
    \  \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n\
    \                        \"amount\": 20,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\"\
    : 0.0453104,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-41
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[5].recipe[2]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 3,\n                      \
    \  \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\"\
    : 519,\n                        \"amount\": 100,\n                        \"unit\"\
    : \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\"\
    : 0.486287,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-42
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[5].recipe[3]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 4,\n                      \
    \  \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n\
    \                        \"amount\": 50,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\"\
    : 0.148236,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-43
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[5].recipe[4]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 5,\n                      \
    \  \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n\
    \                        \"amount\": 50,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\"\
    : 0.132837,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-44
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[5].recipe[5]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 6,\n                      \
    \  \"compound\": \"Nicotinic acid\",\n                        \"compound_id\"\
    : 139,\n                        \"amount\": 50,\n                        \"unit\"\
    : \"mg\",\n                        \"g_l\": 0.05,\n                        \"\
    mmol_l\": 0.406141,\n                        \"optional\": 0\n               \
    \     }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-45
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[5].recipe[6]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 7,\n                      \
    \  \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\"\
    : 1512,\n                        \"amount\": 50,\n                        \"unit\"\
    : \"mg\",\n                        \"g_l\": 0.05,\n                        \"\
    mmol_l\": 0.209846,\n                        \"optional\": 0\n               \
    \     }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-46
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[5].recipe[7]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 8,\n                      \
    \  \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n\
    \                        \"amount\": 1,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\"\
    : 0.00073779,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-47
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[5].recipe[8]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 9,\n                      \
    \  \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\"\
    : 47,\n                        \"amount\": 50,\n                        \"unit\"\
    : \"mg\",\n                        \"g_l\": 0.05,\n                        \"\
    mmol_l\": 0.364591,\n                        \"optional\": 0\n               \
    \     }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-48
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[5].recipe[9]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 10,\n                     \
    \   \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\"\
    : 252,\n                        \"amount\": 50,\n                        \"unit\"\
    : \"mg\",\n                        \"g_l\": 0.05,\n                        \"\
    mmol_l\": 0.24233,\n                        \"optional\": 0\n                \
    \    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-49
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/165
  locator: $.data.solutions[5].recipe[10]
  accessed_at: '2026-10-21T09:46:48.818058Z'
  support: supports
  summary: Preserve the source solvent quantity 1000 ml in its own stage. The provider
    declares this solution volume as 1000 mL; water addition is not independent proof
    of measured final volume.
  quote: "{\n                        \"recipe_order\": 11,\n                     \
    \   \"compound\": \"Distilled water\",\n                        \"compound_id\"\
    : 4,\n                        \"amount\": 1000,\n                        \"unit\"\
    : \"ml\",\n                        \"optional\": 0\n                    }"
  snapshot_sha256: aa1aa68534434f879e441aeed823afc2cb125abc5f8fa11a34c98fb319c142f2
- evidence_id: quantity-50
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf
  locator: page 2, Modified Wolin mineral stock preparation
  accessed_at: '2026-10-21T09:46:49.704361Z'
  support: supports
  summary: Source adjusts pH to 6.5 and then 7.0 with KOH without specifying a fixed
    amount. Do not fill that absence with zero or a guessed dose.
  quote: First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then
    add minerals. Adjust
  snapshot_sha256: d9fb409f692ec6f6dee9a2dc6def7d9cb3e6817d80d3a94684c98740c2dc6f87
- evidence_id: quantity-51
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf
  locator: page 1, main preparation paragraph
  accessed_at: '2026-10-21T09:46:49.704361Z'
  support: supports
  summary: Cellobiose, vitamins, cysteine, sulfide and carbonate have stated ingredient
    amounts, but not all later stock volumes are specified. Their sterile/anoxic handling
    and separate gas atmospheres cannot establish a measured final volume.
  quote: autoclave. Add cellobiose, vitamins, cysteine and sulfide from sterile anoxic
    stock solutions
  snapshot_sha256: d9fb409f692ec6f6dee9a2dc6def7d9cb3e6817d80d3a94684c98740c2dc6f87
- evidence_id: quantity-52
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf
  locator: page 1, main preparation paragraph
  accessed_at: '2026-10-21T09:46:49.704361Z'
  support: context_only
  summary: Target pH 7.2 is a permitted endpoint, but the exact source and DSMZ owner
    specify the complete-medium range 7.2–7.4. Preserve its scope and range rather
    than replacing it with a midpoint.
  quote: filtration. Prior to use adjust pH of complete medium to 7.2 - 7.4. Cellulose
    (MN 300,
  snapshot_sha256: d9fb409f692ec6f6dee9a2dc6def7d9cb3e6817d80d3a94684c98740c2dc6f87
- evidence_id: quantity-53
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf
  locator: page 1, main preparation paragraph
  accessed_at: '2026-10-21T09:46:49.704361Z'
  support: supports
  summary: Preserve the source 80% N2 / 20% CO2 gas mixture as preparation context,
    not an organism phenotype.
  quote: sparge medium with 80% N2 and 20% CO2 gas mixture for 30 – 45 min to make
    it anoxic.
  snapshot_sha256: d9fb409f692ec6f6dee9a2dc6def7d9cb3e6817d80d3a94684c98740c2dc6f87
- evidence_id: quantity-54
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf
  locator: page 1, main preparation paragraph
  accessed_at: '2026-10-21T09:46:49.704361Z'
  support: supports
  summary: The source specifies 30–45 min; preserve the interval without choosing
    a midpoint.
  quote: sparge medium with 80% N2 and 20% CO2 gas mixture for 30 – 45 min to make
    it anoxic.
  snapshot_sha256: d9fb409f692ec6f6dee9a2dc6def7d9cb3e6817d80d3a94684c98740c2dc6f87
- evidence_id: quantity-55
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf
  locator: page 1, main preparation paragraph
  accessed_at: '2026-10-21T09:46:49.704361Z'
  support: supports
  summary: The specified stocks are prepared under 100% N2; the separately qualified
    carbonate stock has a different atmosphere.
  quote: prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution
    prepared
  snapshot_sha256: d9fb409f692ec6f6dee9a2dc6def7d9cb3e6817d80d3a94684c98740c2dc6f87
- evidence_id: quantity-56
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium165.pdf
  locator: page 1, main preparation paragraph
  accessed_at: '2026-10-21T09:46:49.704361Z'
  support: supports
  summary: Preserve the separate carbonate-stock preparation under 80% N2 / 20% CO2;
    do not transfer the 100% N2 instruction from the preceding stocks.
  quote: under 80% N2 and 20% CO2 gas mixture. Cellobiose and vitamins have to be
    sterilized by
  snapshot_sha256: d9fb409f692ec6f6dee9a2dc6def7d9cb3e6817d80d3a94684c98740c2dc6f87
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: CHEBI:8806 resolves to Resazurin and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi29377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T07:31:16.500548Z'
  support: supports
  summary: CHEBI:29377 resolves to sodium carbonate and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: chebi17057
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T09:27:39.796651Z'
  support: supports
  summary: CHEBI:17057 resolves to cellobiose and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: 3548f79d3274a33683125152944998cffa00bd4fce774c8d872db9003222ed06
- evidence_id: chebi18246
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18246
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T09:46:50.902901Z'
  support: supports
  summary: CHEBI:18246 resolves to (1->4)-beta-D-glucan and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: f7abaf5dd620c7de0e80d8e5718cbab4fa7a6455577d0a176847d4e8829be90c
- evidence_id: chebi91248
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:42:32.136441Z'
  support: supports
  summary: CHEBI:91248 resolves to L-cysteine hydrochloride hydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: CHEBI:76209 resolves to sodium sulfide nonahydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: CHEBI:62946 resolves to ammonium sulfate and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi44557
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:46:15.250117Z'
  support: supports
  summary: CHEBI:44557 resolves to nitrilotriacetic acid and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
- evidence_id: chebi86364
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T07:33:35.036768Z'
  support: supports
  summary: CHEBI:86364 resolves to manganese(II) sulfate monohydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi91244
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:07.079384Z'
  support: supports
  summary: CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: CHEBI:32312 resolves to zinc sulfate heptahydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:28.489501Z'
  support: supports
  summary: CHEBI:31440 resolves to copper(II) sulfate pentahydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi86465
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:08.054799Z'
  support: supports
  summary: CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate and is
    not obsolete. Available definitions, formulae, structures and synonyms were inspected;
    recipe amounts and supplied forms are assessed separately.
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: CHEBI:34887 resolves to nickel dichloride and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi131361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T07:33:27.980786Z'
  support: supports
  summary: CHEBI:131361 resolves to disodium selenite pentahydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: CHEBI:63939 resolves to sodium tungstate dihydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi26836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T07:29:13.222926Z'
  support: supports
  summary: CHEBI:26836 resolves to sulfuric acid and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: 19e202cd697eed2be3130d5b0b29cc0c1d18575ad103110877303ee678779737
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: CHEBI:15956 resolves to biotin and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: CHEBI:27470 resolves to folic acid and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: CHEBI:30961 resolves to pyridoxine hydrochloride and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: CHEBI:49105 resolves to thiamine hydrochloride and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: CHEBI:17015 resolves to riboflavin and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: CHEBI:15940 resolves to nicotinic acid and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: CHEBI:31345 resolves to Calcium pantothenate and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: CHEBI:176843 resolves to vitamin B12 and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: CHEBI:30753 resolves to 4-aminobenzoic acid and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi16494
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T06:55:13.001958Z'
  support: supports
  summary: CHEBI:16494 resolves to lipoic acid and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned snapshot; exact MAPPED/preferred_term rows for asserted CHEBI
    keys and exact legacy-key lookup
  accessed_at: '2026-10-21T10:05:42Z'
  support: supports
  summary: '{"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count":
    9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id",
    "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech",
    "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5",
    "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"},
    "counts": {"target": {"ingredient_instances": 35, "primary_CHEBI_instances": 35,
    "secondary_current_asserted_instances": 33, "secondary_current_verified_instances":
    33, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 100.0, "secondary_verified_percent":
    94.29}, "owner-0": {"ingredient_instances": 35, "primary_CHEBI_instances": 35,
    "secondary_current_asserted_instances": 33, "secondary_current_verified_instances":
    33, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 100.0, "secondary_verified_percent":
    94.29}, "owner-1": {"ingredient_instances": 35, "primary_CHEBI_instances": 35,
    "secondary_current_asserted_instances": 33, "secondary_current_verified_instances":
    33, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 100.0, "secondary_verified_percent":
    94.29}}, "instances": [{"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[0]", "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806",
    "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition":
    [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3",
    "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"],
    "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]},
    "synonyms": ["Resazurin"]}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[1]", "name": "Na2CO3", "primary": {"id": "CHEBI:29377",
    "label": "sodium carbonate"}, "canonical_label": "sodium carbonate", "label_equal":
    true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:497-19-8", "ppdb:594"], "generalized_empirical_formula": ["CO3.2Na"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:29377"], "inchi_key_string": ["CDBYLPFSWZWCQE-UHFFFAOYSA-L"],
    "inchi_string": ["InChI=1S/CH2O3.2Na/c2-1(3)4;;/h(H2,2,3,4);;/q;2*+1/p-2"], "mass":
    ["105.988"], "monoisotopic_mass": ["105.96428"], "smiles_string": ["O=C([O-])[O-].[Na+].[Na+]"]},
    "synonyms": ["Na2CO3", "Natriumkarbonat", "disodium carbonate", "disodium trioxidocarbonate",
    "disodium trioxidocarbonate", "sodium carbonate", "sodium carbonate"], "secondary":
    {"asserted": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "exact_current_rows":
    [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377",
    "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[2]", "name": "Cellobiose", "primary": {"id": "CHEBI:17057",
    "label": "cellobiose"}, "canonical_label": "cellobiose", "label_equal": true,
    "definition": ["A glycosylglucose consisting of two glucose units linked via a
    β(1→4) bond."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1292744",
    "cas:528-50-7", "drugbank:DB02061", "kegg.compound:C00185", "knapsack:C00001134",
    "pubmed:19669625", "pubmed:19968554", "wikipedia.en:Cellobiose"], "generalized_empirical_formula":
    ["C12H22O11"], "has_alternative_id": ["CHEBI:13952", "CHEBI:23061", "CHEBI:28108",
    "CHEBI:3522"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17057"],
    "inchi_key_string": ["GUBGYTABKSRVRQ-CUHNMECISA-N"], "inchi_string": ["InChI=1S/C12H22O11/c13-1-3-5(15)6(16)9(19)12(22-3)23-10-4(2-14)21-11(20)8(18)7(10)17/h3-20H,1-2H2/t3-,4-,5-,6+,7-,8-,9-,10-,11?,12+/m1/s1"],
    "mass": ["342.297"], "monoisotopic_mass": ["342.11621"], "smiles_string": ["OC[C@H]1O[C@@H](O[C@H]2[C@H](O)[C@@H](O)C(O)O[C@@H]2CO)[C@H](O)[C@@H](O)[C@@H]1O"],
    "wurcs_representation": ["WURCS=2.0/2,2,1/[a2122h-1x_1-5][a2122h-1b_1-5]/1-2/a4-b1"]},
    "synonyms": ["1-beta-D-Glucopyranosyl-4-D-glucopyranose", "4-(beta-D-glucosido)-D-glucose",
    "4-O-beta-D-glucopyranosyl-D-glucopyranose", "4-beta-D-glucopyranosyl-D-glucopyranose",
    "Cellobiose", "D-(+)-cellobiose", "D-celiobiose", "D-cellobiose", "D-glucosyl-beta-(1-4)-D-glucose",
    "beta-D-glucopyranosyl-(1->4)-D-glucopyranose", "beta-D-glucopyranosyl-(1->4)-D-glucopyranose",
    "cellose"], "secondary": {"asserted": {"id": "CHEBI:17057", "label": "cellobiose"},
    "exact_current_rows": [{"label": "Cellobiose", "match_type": "preferred_term",
    "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path":
    "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[3]",
    "name": "Cellulose", "primary": {"id": "CHEBI:18246", "label": "(1->4)-beta-D-glucan"},
    "canonical_label": "(1->4)-beta-D-glucan", "label_equal": true, "definition":
    ["A β-<small>D</small>-glucan in which the glucose units are connected by (1→4)
    linkages."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:9004-34-6",
    "hmdb:HMDB0006944", "kegg.compound:C00760", "kegg.drug:D00093", "kegg.glycan:G10481"],
    "generalized_empirical_formula": ["(C6H10O5)n.H2O"], "has_alternative_id": ["CHEBI:10812",
    "CHEBI:23063", "CHEBI:3529"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:18246"],
    "inchi_key_string": ["WQZGKKKJIJFFOK-VFUOTHLCSA-N"], "inchi_string": ["InChI=1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5-,6-/m1/s1"],
    "mass": ["180.156"], "monoisotopic_mass": ["180.06339"], "smiles_string": ["[H]O[C@@H]1O[C@H](CO)[C@@H](O)[C@H](O)[C@H]1O"],
    "wurcs_representation": ["WURCS=2.0/1,1,0/[a2122h-1b_1-5]/1/"]}, "synonyms": ["(1,4-beta-D-Glucosyl)n",
    "(1,4-beta-D-Glucosyl)n+1", "(1,4-beta-D-Glucosyl)n-1", "(1,4-beta-D-glucosyl)(n)",
    "(1,4-beta-D-glucosyl)n", "(1->4)-beta-D-glucopyranan", "(1->4)-beta-D-glucopyranan",
    "1,4-beta-D-Glucan", "Cellulose"], "secondary": {"asserted": {"id": "CHEBI:18246",
    "label": "(1->4)-beta-D-glucan"}, "exact_current_rows": [{"label": "Cellulose",
    "match_type": "preferred_term", "identifier": "CHEBI:18246", "preferred_term":
    "Cellulose", "ontology_id": "CHEBI:18246", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[4]", "name": "L-Cysteine HCl x H2O", "primary": {"id": "CHEBI:91248",
    "label": "L-cysteine hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride
    hydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate
    form of <small>L</small>-cysteine hydrochloride."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326",
    "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"], "inchi_key_string":
    ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"],
    "mass": ["175.637"], "monoisotopic_mass": ["175.00699"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]},
    "synonyms": ["(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)",
    "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(2R)-2-Amino-3-sulfanyl-propanoic
    acid hydrochloride monohydrate", "Cysteine hydrochloride", "L-Cysteine monohydrate
    monochloride", "L-cysteine hydrochloride monohydrate", "L-cysteine hydrochloride--water
    (1/1)", "L-cysteine hydrochloride--water (1/1)"], "secondary": {"asserted": {"id":
    "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "exact_current_rows":
    [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path":
    "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[5]",
    "name": "Na2S x 9 H2O", "primary": {"id": "CHEBI:76209", "label": "sodium sulfide
    nonahydrate"}, "canonical_label": "sodium sulfide nonahydrate", "label_equal":
    true, "definition": ["A hydrate with formula Na<small><sub>2</sub></small>S·9H<small><sub>2</sub></small>O."],
    "annotations": {"charge": [0.0], "database_cross_reference": ["cas:1313-84-4",
    "kegg.drug:D09001", "pubmed:19810706", "reaxys:14636099"], "generalized_empirical_formula":
    ["9H2O.2Na.S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:76209"],
    "inchi_key_string": ["ZGHLCBJZQLNUAZ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.9H2O.S/h;;9*1H2;/q2*+1;;;;;;;;;;-2"],
    "mass": ["240.182"], "monoisotopic_mass": ["240.04669"], "smiles_string": ["O.O.O.O.O.O.O.O.O.[Na+].[Na+].[S-2]"]},
    "synonyms": ["Na2S.9H2O", "Sodium sulfide (USP)", "disodium sulfide nonahydrate",
    "disodium sulfide--water (1/9)", "disodium sulfide--water (1/9)", "sodium monosulfide
    nonahydrate", "sodium monosulfide.9H2O", "sodium sulfide.9H2O"], "secondary":
    {"asserted": {"id": "CHEBI:76209", "label": "sodium sulfide nonahydrate"}, "exact_current_rows":
    [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[6]", "name": "K2HPO4", "primary": {"id": "CHEBI:131527",
    "label": "dipotassium hydrogen phosphate"}, "canonical_label": "dipotassium hydrogen
    phosphate", "label_equal": true, "definition": ["A potassium salt that is the
    dipotassium salt of phosphoric acid."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7758-11-4", "kegg.compound:C13197", "kegg.drug:D02403", "metacyc.compound:CPD0-2433",
    "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"], "generalized_empirical_formula":
    ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:131527"], "inchi_key_string": ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"],
    "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]},
    "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate",
    "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium
    orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4",
    "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium
    monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)",
    "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium
    hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate
    trihydrate"], "secondary": {"asserted": {"id": "CHEBI:131527", "label": "dipotassium
    hydrogen phosphate"}, "exact_current_rows": [{"label": "K2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[7]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036",
    "label": "potassium dihydrogen phosphate"}, "canonical_label": "potassium dihydrogen
    phosphate", "label_equal": true, "definition": ["A potassium salt in which dihydrogen
    phosphate(1−) is the counterion."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"],
    "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string":
    ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"],
    "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]},
    "synonyms": ["MKP", "Monopotassium dihydrogen phosphate", "Monopotassium monophosphate",
    "Monopotassium orthophosphate", "Monopotassium phosphate", "Orthophosphoric acid,
    monopotassium salt", "Phosphoric acid, monopotassium salt", "Phosphoric acid,
    potassium salt (1:1)", "Potassium acid phosphate", "Potassium dihydrogen orthophosphate",
    "Potassium dihydrogen phosphate", "Potassium phosphate monobasic", "Potassium
    phosphate", "Sorensen''s potassium phosphate", "potassium dihydrogen phosphate",
    "potassium dihydrogen phosphate"], "secondary": {"asserted": {"id": "CHEBI:63036",
    "label": "potassium dihydrogen phosphate"}, "exact_current_rows": [{"label": "KH2PO4",
    "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[8]", "name": "(NH4)2SO4", "primary": {"id": "CHEBI:62946",
    "label": "ammonium sulfate"}, "canonical_label": "ammonium sulfate", "label_equal":
    true, "definition": ["An inorganic sulfate salt obtained by reaction of sulfuric
    acid with two equivalents of ammonia. A high-melting (decomposes above 280°C)
    white solid which is very soluble in water (70.6 g/100 g water at 0°C; 103.8 g/100
    g water at 100°C), it is widely used as a fertilizer for alkaline soils."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7783-20-2", "kegg.drug:D08853",
    "metacyc.compound:NH42SO4", "ppdb:36", "pubmed:20556652", "reaxys:11343144", "wikipedia.en:Ammonium_sulfate"],
    "generalized_empirical_formula": ["2H4N.O4S"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:62946"], "inchi_key_string": ["BFNBIHQBYMNNAN-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/2H3N.H2O4S/c;;1-5(2,3)4/h2*1H3;(H2,1,2,3,4)"], "mass": ["132.141"],
    "monoisotopic_mass": ["132.02048"], "smiles_string": ["O=S(=O)([O-])[O-].[NH4+].[NH4+]"]},
    "synonyms": ["(NH4)2SO4", "ammonium sulfate (2:1)", "ammonium sulphate", "diammonium
    sulfate", "diazanium sulfate", "diazanium sulfate", "mascagnite", "sulfuric acid
    ammonium salt (1:2)", "sulfuric acid, diammonium salt", "sulphate of ammonia"],
    "secondary": {"asserted": {"id": "CHEBI:62946", "label": "ammonium sulfate"},
    "exact_current_rows": [{"label": "(NH4)2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path":
    "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[9]",
    "name": "NaCl", "primary": {"id": "CHEBI:26710", "label": "sodium chloride"},
    "canonical_label": "sodium chloride", "label_equal": true, "definition": ["An
    inorganic chloride salt having sodium(1+) as the counterion."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673",
    "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595",
    "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula":
    ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string":
    ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"],
    "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]},
    "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro
    sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium
    chloride", "sodium chloride", "table salt"], "secondary": {"asserted": {"id":
    "CHEBI:26710", "label": "sodium chloride"}, "exact_current_rows": [{"label": "NaCl",
    "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term":
    "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[10]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795",
    "label": "magnesium sulfate heptahydrate"}, "canonical_label": "magnesium sulfate
    heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate
    form of magnesium sulfate."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505",
    "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222",
    "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"],
    "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]},
    "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom
    salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate
    heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)",
    "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"],
    "secondary": {"asserted": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"},
    "exact_current_rows": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[11]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158",
    "label": "calcium chloride dihydrate"}, "canonical_label": "calcium chloride dihydrate",
    "label_equal": true, "definition": ["A hydrate that is the dihydrate form of calcium
    chloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8",
    "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"],
    "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass":
    ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}, "synonyms": ["CaCl2.2H2O",
    "Calcium chloride hydrate", "Calcium chloride", "calcium chloride--water (1/2)",
    "calcium chloride--water (1/2)", "calcium dichloride dihydrate"], "secondary":
    {"asserted": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "exact_current_rows":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[12]", "name": "Nitrilotriacetic acid", "primary": {"id":
    "CHEBI:44557", "label": "nitrilotriacetic acid"}, "canonical_label": "nitrilotriacetic
    acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0],
    "database_cross_reference": ["beilstein:1710776", "cas:139-13-9", "drugbank:DB03040",
    "gmelin:3726", "kegg.compound:C14695", "pdb-ccd:NTA"], "generalized_empirical_formula":
    ["C6H9NO6"], "has_alternative_id": ["CHEBI:34889", "CHEBI:44555"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:44557"], "inchi_key_string": ["MGFYIUFZLHCRTH-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"],
    "mass": ["191.139"], "monoisotopic_mass": ["191.04299"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]},
    "synonyms": ["Complexon I", "H3nta", "Komplexon I", "N(CH2-COOH)3", "N,N-bis(carboxymethyl)glycine",
    "N,N-bis(carboxymethyl)glycine", "NITRILOTRIACETIC ACID", "NTA", "Nitrilotriacetate",
    "Nitrilotriacetic acid", "Nitrilotriessigsaeure", "Triglycollamic acid", "Trilon
    A", "alpha,alpha'',alpha''''-trimethylaminetricarboxylic acid", "nitrilo-2,2'',2''''-triacetic
    acid", "tri(carboxymethyl)amine", "triglycine"], "secondary": {"asserted": {"id":
    "CHEBI:44557", "label": "nitrilotriacetic acid"}, "exact_current_rows": [{"label":
    "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557",
    "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[13]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364",
    "label": "manganese(II) sulfate monohydrate"}, "canonical_label": "manganese(II)
    sulfate monohydrate", "label_equal": true, "definition": ["A hydrate that is the
    monohydrate form of manganese(II) sulfate."], "annotations": {"charge": [0.0],
    "database_cross_reference": ["cas:10034-96-5", "kegg.drug:D04854", "pubmed:26097037",
    "reaxys:13153017", "wikipedia.en:Manganese(II)_sulfate"], "generalized_empirical_formula":
    ["H2O.Mn.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86364"],
    "inchi_key_string": ["ISPYRSDWRDQNSW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mn.H2O4S.H2O/c;1-5(2,3)4;/h;(H2,1,2,3,4);1H2/q+2;;/p-2"],
    "mass": ["169.016"], "monoisotopic_mass": ["168.90034"], "smiles_string": ["O.O=S(=O)([O-])[O-].[Mn+2]"]},
    "synonyms": ["Manganese sulfate hydrate", "Manganese sulfate monohydrate", "Manganese
    sulfate", "Manganous sulfate monohydrate", "MnSO4.H2O", "manganese(2+) sulfate
    monohydrate", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulfate--water
    (1/1)", "manganese(2+) sulphate monohydrate", "manganese(II) sulphate monohydrate"],
    "secondary": {"asserted": {"id": "CHEBI:86364", "label": "manganese(II) sulfate
    monohydrate"}, "exact_current_rows": [{"label": "MnSO4 x H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path":
    "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[14]",
    "name": "FeSO4 x 7 H2O", "primary": {"id": "CHEBI:75836", "label": "iron(2+) sulfate
    heptahydrate"}, "canonical_label": "iron(2+) sulfate heptahydrate", "label_equal":
    true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate.
    It is used as a source of iron in the treatment of iron-deficiency anaemia (generally
    in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally
    used)."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0",
    "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"],
    "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string":
    ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]},
    "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous
    sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol",
    "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O",
    "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"], "secondary": {"asserted":
    {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "exact_current_rows":
    [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[15]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244",
    "label": "cobalt(2+) sulfate heptahydrate"}, "canonical_label": "cobalt(2+) sulfate
    heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate
    form of cobalt(2+) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:10026-24-1", "pubmed:10504146", "pubmed:12187935", "pubmed:12209163", "pubmed:12579202",
    "pubmed:12948248", "pubmed:2227161", "pubmed:24359163", "pubmed:25896363", "wikipedia.en:Cobalt(II)_sulfate"],
    "generalized_empirical_formula": ["Co.7H2O.O4S"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:91244"], "inchi_key_string": ["MEYVLGVRTYSQHI-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Co.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["281.101"], "monoisotopic_mass": ["280.95888"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Co+2]"]},
    "synonyms": ["Cobalt monosulfate heptahydrate", "cobalt sulfate heptahydrate",
    "cobalt(2+) sulfate--water (1/7)", "cobalt(2+) sulfate--water (1/7)", "cobalt(II)
    sulfate heptahydrate", "cobaltous sulfate heptahydrate"], "secondary": {"asserted":
    {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "exact_current_rows":
    [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244",
    "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[16]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312",
    "label": "zinc sulfate heptahydrate"}, "canonical_label": "zinc sulfate heptahydrate",
    "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of
    zinc sulfate."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7446-20-0", "gmelin:47216", "kegg.drug:D01081", "wikipedia.en:Zinc_Sulfate"],
    "generalized_empirical_formula": ["7H2O.O4S.Zn"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:32312"], "inchi_key_string": ["RZLVQBNCHSJZPX-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/H2O4S.7H2O.Zn/c1-5(2,3)4;;;;;;;;/h(H2,1,2,3,4);7*1H2;/q;;;;;;;;+2/p-2"],
    "mass": ["287.558"], "monoisotopic_mass": ["285.95482"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Zn+2]"]},
    "synonyms": ["Zinc sulfate", "ZnSO4.7H2O", "zinc sulfate (1:1) heptahydrate",
    "zinc sulfate heptahydrate (1:1:7)", "zinc(2+) sulfate heptahydrate", "zinc(2+)
    sulfate heptahydrate", "zinc(2+) sulfate--water (1/7)", "zinc(2+) sulfate--water
    (1/7)"], "secondary": {"asserted": {"id": "CHEBI:32312", "label": "zinc sulfate
    heptahydrate"}, "exact_current_rows": [{"label": "ZnSO4 x 7 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O",
    "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}},
    {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[17]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440",
    "label": "copper(II) sulfate pentahydrate"}, "canonical_label": "copper(II) sulfate
    pentahydrate", "label_equal": true, "definition": ["The pentahydrate of copper(2+)
    sulfate. A bright blue crystalline solid."], "annotations": {"charge": [0.0],
    "database_cross_reference": ["cas:7758-99-8", "kegg.drug:D03613", "pubmed:11407502",
    "pubmed:12209195", "pubmed:12484481", "pubmed:15040745", "pubmed:15607472", "pubmed:15824790",
    "pubmed:19346702", "pubmed:2002460", "pubmed:20132934", "pubmed:2913309", "pubmed:3351847",
    "pubmed:7615984", "pubmed:8878264", "pubmed:9521458", "pubmed:9776063", "reaxys:16499970",
    "wikipedia.en:Copper(II)_sulfate"], "generalized_empirical_formula": ["Cu.5H2O.O4S"],
    "has_alternative_id": ["CHEBI:121741", "CHEBI:370227"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:31440"], "inchi_key_string": ["JZCCFEFSEZPSOG-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Cu.H2O4S.5H2O/c;1-5(2,3)4;;;;;/h;(H2,1,2,3,4);5*1H2/q+2;;;;;;/p-2"],
    "mass": ["249.684"], "monoisotopic_mass": ["248.93415"], "smiles_string": ["O=S(=O)([O-])[O-].[Cu+2].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H]"]},
    "synonyms": ["CuSO4.5H2O", "Cupric sulfate", "copper sulphate(5.H2O)", "copper(2+)
    sulfate (1:1) pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate
    pentahydrate", "copper(2+) sulfate--water (1/5)", "copper(2+) sulfate--water (1/5)",
    "copper(II) sulfate, pentahydrate", "cupric sulfate pentahydrate"], "secondary":
    {"asserted": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"},
    "exact_current_rows": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[18]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465",
    "label": "potassium aluminium sulfate dodecahydrate"}, "canonical_label": "potassium
    aluminium sulfate dodecahydrate", "label_equal": true, "definition": ["A hydrate
    resulting from the the formal combination of anhydrous potassium aluminium sulfate
    with 12 mol eq. of water."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7784-24-9", "reaxys:14851666", "wikipedia.en:Potassium_alum"], "generalized_empirical_formula":
    ["Al.12H2O.K.2O4S"], "has_alternative_id": ["CHEBI:31192"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:86465"], "inchi_key_string": ["GNHOJBNSNUXZQA-UHFFFAOYSA-J"],
    "inchi_string": ["InChI=1S/Al.K.2H2O4S.12H2O/c;;2*1-5(2,3)4;;;;;;;;;;;;/h;;2*(H2,1,2,3,4);12*1H2/q+3;+1;;;;;;;;;;;;;;/p-4"],
    "mass": ["474.386"], "monoisotopic_mass": ["473.97548"], "smiles_string": ["O.O.O.O.O.O.O.O.O.O.O.O.O=S(=O)([O-])[O-].O=S(=O)([O-])[O-].[Al+3].[K+]"]},
    "synonyms": ["AlK(SO4)2.12H2O", "Aluminum potassium disulfate dodecahydrate",
    "Aluminum potassium sulfate dodecahydrate", "Kalinite", "Potash alum dodecahydrate",
    "Potassium alum dodecahydrate", "Potassium aluminum disulfate dodecahydrate",
    "aluminium potassium sulfate--water (1/12)", "aluminium potassium sulfate--water
    (1/12)"], "secondary": {"asserted": {"id": "CHEBI:86465", "label": "potassium
    aluminium sulfate dodecahydrate"}, "exact_current_rows": [{"label": "AlK(SO4)2
    x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term":
    "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[19]", "name": "H3BO3", "primary": {"id": "CHEBI:33118",
    "label": "boric acid"}, "canonical_label": "boric acid", "label_equal": true,
    "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["bpdb:2136", "cas:10043-35-3", "cas:11113-50-1", "drugcentral:3035", "gmelin:1585",
    "kegg.compound:C12486", "kegg.drug:D01089", "molbase:1644", "pdb-ccd:BO3", "ppdb:2136"],
    "generalized_empirical_formula": ["H3BO3"], "has_alternative_id": ["CHEBI:22911",
    "CHEBI:31299", "CHEBI:41248"], "has_obo_namespace": ["chebi_ontology"], "id":
    ["CHEBI:33118"], "inchi_key_string": ["KGBXLFKZBHKPEV-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"], "mass": ["61.833"], "monoisotopic_mass": ["62.01752"],
    "smiles_string": ["[H]OB(O[H])O[H]"]}, "synonyms": ["B(OH)3", "BORIC ACID", "Boric
    acid", "H3BO3", "[B(OH)3]", "boric acid", "boron trihydroxide", "orthoboric acid",
    "trihydroxidoboron", "trihydroxidoboron"], "secondary": {"asserted": {"id": "CHEBI:33118",
    "label": "boric acid"}, "exact_current_rows": [{"label": "H3BO3", "match_type":
    "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[20]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213",
    "label": "sodium molybdate dihydrate"}, "canonical_label": "sodium molybdate dihydrate",
    "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium
    molybdate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10102-40-6",
    "pubmed:20645132", "pubmed:20813395", "pubmed:22663766", "pubmed:3382795", "reaxys:19032996",
    "wikipedia.en:Sodium_molybdate"], "generalized_empirical_formula": ["2H2O.MoO4.2Na"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75213"], "inchi_key_string":
    ["FDEIWTXVNPKYDL-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/Mo.2Na.2H2O.4O/h;;;2*1H2;;;;/q;2*+1;;;;;2*-1"],
    "mass": ["241.946"], "monoisotopic_mass": ["243.88573"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]},
    "synonyms": ["Disodium molybdate dihydrate", "Molybdic acid, disodium salt, dihydrate",
    "Na2MoO4.2H2O", "Sodium molybdate(VI) dihydrate", "sodium dioxido(dioxo)molybdenum--water
    (1/2)", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium orthomolybdate
    dihydrate"], "secondary": {"asserted": {"id": "CHEBI:75213", "label": "sodium
    molybdate dihydrate"}, "exact_current_rows": [{"label": "Na2MoO4 x 2 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2
    H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}]}},
    {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[21]", "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887",
    "label": "nickel dichloride"}, "canonical_label": "nickel dichloride", "label_equal":
    true, "definition": ["A compound of nickel and chloride in which the ratio of
    nickel (in the +2 oxidation state) to chloride is 1:2."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:7718-54-9", "kegg.compound:C14711", "pubmed:11739495",
    "pubmed:12603851", "pubmed:21928331", "pubmed:23179351", "pubmed:23622879", "pubmed:23702803",
    "pubmed:23735035", "pubmed:7671317", "reaxys:3902827", "reaxys:8128171", "wikipedia.en:Nickel_dichloride"],
    "generalized_empirical_formula": ["Cl2Ni"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:34887"], "inchi_key_string": ["QMMRZOWCJAIUJA-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"], "mass": ["129.599"], "monoisotopic_mass":
    ["127.87305"], "smiles_string": ["[Cl][Ni][Cl]"]}, "synonyms": ["NiCl2", "Nickel
    chloride", "Nickel(II) chloride", "[NiCl2]", "nickel dichloride", "nickel dichloride",
    "nickel(2+) chloride", "nickel(2+) chloride", "nickel(II) chloride", "nickel(II)
    chloride", "nickelous chloride"], "secondary": {"asserted": {"id": "CHEBI:34887",
    "label": "nickel dichloride"}, "exact_current_rows": [{"label": "NiCl2", "match_type":
    "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id":
    "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[22]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361",
    "label": "disodium selenite pentahydrate"}, "canonical_label": "disodium selenite
    pentahydrate", "label_equal": true, "definition": ["A hydrate that is the pentahydrate
    form of disodium selenite."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:26970-82-1", "pubmed:15259772", "pubmed:15559373", "pubmed:16126997", "pubmed:17873396",
    "pubmed:24479345", "pubmed:24716537", "reaxys:14666014", "wikipedia.en:Sodium_selenite"],
    "generalized_empirical_formula": ["5H2O.2Na.O3Se"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:131361"], "inchi_key_string": ["TUANAMBRHOLYTH-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"],
    "mass": ["263.012"], "monoisotopic_mass": ["263.93363"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]},
    "synonyms": ["Na2SeO3.5H2O", "Selenious acid disodium salt, pentahydrate", "Sodium
    selenite pentahydrate", "disodium selenite hydrate", "sodium selenite hydrate",
    "sodium selenite--water (1/5)", "sodium selenite--water (1/5)"], "secondary":
    {"asserted": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"},
    "exact_current_rows": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id":
    "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[23]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939",
    "label": "sodium tungstate dihydrate"}, "canonical_label": "sodium tungstate dihydrate",
    "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium
    tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines
    to nitrones"], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10213-10-2",
    "reaxys:13157884", "wikipedia.en:Sodium_tungstate"], "generalized_empirical_formula":
    ["2H2O.2Na.O4W"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63939"],
    "inchi_key_string": ["WPZFLQRLSGVIAA-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.2H2O.4O.W/h;;2*1H2;;;;;/q2*+1;;;;;2*-1;"],
    "mass": ["329.846"], "monoisotopic_mass": ["329.93126"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]},
    "synonyms": ["Na2WO4.2H2O", "Tungstic acid, sodium salt, dihydrate", "sodium dioxido(dioxo)tungsten--water
    (1/2)", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium orthotungstate dihydrate",
    "sodium tungstate(VI) dihydrate"], "secondary": {"asserted": {"id": "CHEBI:63939",
    "label": "sodium tungstate dihydrate"}, "exact_current_rows": [{"label": "Na2WO4
    x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term":
    "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[24]", "name": "H2SO4", "primary": {"id": "CHEBI:26836",
    "label": "sulfuric acid"}, "canonical_label": "sulfuric acid", "label_equal":
    true, "definition": ["A sulfur oxoacid that consists of two oxo and two hydroxy
    groups joined covalently to a central sulfur atom."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:7664-93-9", "gmelin:2122", "kegg.compound:C00059",
    "kegg.drug:D05963", "knapsack:C00007530", "molbase:4", "ppdb:606", "pubmed:13568755",
    "pubmed:16122922", "pubmed:19397353", "pubmed:22047659", "pubmed:22136045", "pubmed:22204399",
    "pubmed:22267186", "pubmed:22296037", "pubmed:22364556", "pubmed:22435616", "reaxys:2037554",
    "wikipedia.en:Sulfuric_acid"], "generalized_empirical_formula": ["H2O4S"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:26836"], "inchi_key_string": ["QAOWNCQODCNURD-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/H2O4S/c1-5(2,3)4/h(H2,1,2,3,4)"], "mass": ["98.079"],
    "monoisotopic_mass": ["97.96738"], "smiles_string": ["[H]OS(=O)(=O)O[H]"]}, "synonyms":
    ["Acide sulfurique", "Acido sulfurico", "Acidum sulfuricum", "H2SO4", "Schwefelsaeureloesungen",
    "Sulfuric acid", "[S(OH)2O2]", "[SO2(OH)2]", "dihydrogen tetraoxosulfate", "dihydrogen
    tetraoxosulfate", "dihydroxidodioxidosulfur", "dihydroxidodioxidosulfur", "hydrogen
    tetraoxosulfate(2-)", "hydrogen tetraoxosulfate(2-)", "hydrogen tetraoxosulfate(VI)",
    "hydrogen tetraoxosulfate(VI)", "sulfuric acid", "sulfuric acid", "sulphuric acid",
    "tetraoxosulfuric acid", "tetraoxosulfuric acid"], "secondary": {"asserted": {"id":
    "CHEBI:26836", "label": "sulfuric acid"}, "exact_current_rows": [{"label": "H2SO4",
    "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term":
    "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[25]", "name": "Biotin", "primary": {"id": "CHEBI:15956",
    "label": "biotin"}, "canonical_label": "biotin", "label_equal": true, "definition":
    ["An organic heterobicyclic compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
    having a valeric acid substituent attached to the tetrahydrothiophene ring. The
    parent of the class of biotins."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:58-85-5", "chemspider:149962", "drugbank:DB00121", "drugcentral:373", "foodb.food:FDB014510",
    "gmelin:1918703", "hmdb:HMDB0000030", "kegg.compound:C00120", "kegg.drug:D00029",
    "knapsack:C00000756", "lincs.smallmolecule:LSM-3994", "metacyc.compound:BIOTIN",
    "pdb-ccd:BTN", "pmc:PMC8089577", "pubmed:10064317", "pubmed:10215065", "pubmed:10577274",
    "pubmed:11435506", "pubmed:11481419", "pubmed:11800048", "pubmed:12055344", "pubmed:12070309",
    "pubmed:12603856", "pubmed:12803839", "pubmed:15012185", "pubmed:15202718", "pubmed:15272000",
    "pubmed:15690449", "pubmed:15863846", "pubmed:15899401", "pubmed:15992684", "pubmed:16011464",
    "pubmed:16195795", "pubmed:16419467", "pubmed:16676358", "pubmed:16677798", "pubmed:16704206",
    "pubmed:16769720", "pubmed:17297119", "pubmed:1814646", "pubmed:18202531", "pubmed:18452485",
    "pubmed:18509457", "pubmed:19212411", "pubmed:19319844", "pubmed:19727438", "pubmed:19928962",
    "pubmed:20967359", "pubmed:20974274", "pubmed:2100006", "pubmed:21248194", "pubmed:21356565",
    "pubmed:21373679", "pubmed:21596550", "pubmed:21871906", "pubmed:25515858", "pubmed:33346513",
    "pubmed:33461365", "pubmed:34077272", "pubmed:8333586", "pubmed:8750932", "pubmed:9022537",
    "pubmed:9038855", "pubmed:9094878", "pubmed:9164991", "pubmed:9176832", "pubmed:9371938",
    "pubmed:9416479", "reaxys:86838", "wikipedia.en:Biotin"], "generalized_empirical_formula":
    ["C10H16N2O3S"], "has_alternative_id": ["CHEBI:13905", "CHEBI:22882", "CHEBI:22884",
    "CHEBI:3108", "CHEBI:41236"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15956"],
    "inchi_key_string": ["YBJHBAHKTGYVGT-ZKWXMUAHSA-N"], "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"],
    "mass": ["244.316"], "monoisotopic_mass": ["244.08816"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]},
    "synonyms": ["(+)-cis-Hexahydro-2-oxo-1H-thieno[3,4]imidazole-4-valeric acid",
    "(3aS,4S,6aR)-Hexahydro-2-oxo-1H-thieno[3,4-d]imidazole-4-valeric acid", "5-(2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl)pentanoic
    acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic
    acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic
    acid", "BIOTIN", "Coenzyme R", "D-(+)-biotin", "D-Biotin", "Vitamin H", "biotin",
    "biotina", "biotine", "biotinum", "cis-(+)-Tetrahydro-2-oxothieno[3,4]imidazoline-4-valeric
    acid", "cis-Hexahydro-2-oxo-1H-thieno(3,4)imidazole-4-valeric acid", "cis-Tetrahydro-2-oxothieno(3,4-d)imidazoline-4-valeric
    acid", "vitamin B7"], "secondary": {"asserted": {"id": "CHEBI:15956", "label":
    "biotin"}, "exact_current_rows": [{"label": "Biotin", "match_type": "preferred_term",
    "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path":
    "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[26]",
    "name": "Folic acid", "primary": {"id": "CHEBI:27470", "label": "folic acid"},
    "canonical_label": "folic acid", "label_equal": true, "definition": ["An <em>N</em>-acyl-amino
    acid that is a form of the water-soluble vitamin B<small><sub>9</sub></small>.
    Its biologically active forms (tetrahydrofolate and others) are essential for
    nucleotide biosynthesis and homocysteine remethylation."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["agr:IND606960789", "cas:59-30-3", "chemspider:5815",
    "drugbank:DB00158", "drugcentral:1231", "foodb.food:FDB014504", "hmdb:HMDB0000121",
    "kegg.compound:C00504", "kegg.drug:D00070", "knapsack:C00001539", "lincs.smallmolecule:LSM-5355",
    "metacyc.compound:CPD-12826", "pdb-ccd:FOL", "pubmed:10138938", "pubmed:10897644",
    "pubmed:10958818", "pubmed:11261364", "pubmed:11451208", "pubmed:11959400", "pubmed:14387833",
    "pubmed:15321809", "pubmed:15523939", "pubmed:15754725", "pubmed:15797531", "pubmed:15797685",
    "pubmed:15831910", "pubmed:15990733", "pubmed:16093404", "pubmed:16277678", "pubmed:16380297",
    "pubmed:16871332", "pubmed:17784727", "pubmed:18788725", "pubmed:19121630", "pubmed:19335717",
    "pubmed:19355913", "pubmed:24650098", "pubmed:33624660", "pubmed:33965562", "pubmed:33968971",
    "pubmed:34207319", "pubmed:34219855", "pubmed:7738698", "pubmed:8235383", "pubmed:9040515",
    "pubmed:9420019", "pubmed:9565830", "pubmed:9683174", "pubmed:9781393", "pubmed:9808640",
    "pubmed:9808641", "reaxys:100781", "wikipedia.en:Folic_Acid"], "generalized_empirical_formula":
    ["C19H19N7O6"], "has_alternative_id": ["CHEBI:24075", "CHEBI:42610", "CHEBI:5140",
    "CHEBI:569217"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:27470"],
    "inchi_key_string": ["OVBPIULPVIDEAO-LBPRGKRZSA-N"], "inchi_string": ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"],
    "mass": ["441.404"], "monoisotopic_mass": ["441.13968"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]},
    "synonyms": ["(2S)-2-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzamido)pentanedioic
    acid", "Acfol", "Folate", "Folicet", "Folsaeure", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic
    acid", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic
    acid", "N-[(4-{[(2-amino-4-oxo-1,4-dihydropteridin-6-yl)methyl]amino}phenyl)carbonyl]-L-glutamic
    acid", "N-pteroyl-L-glutamic acid", "PGA", "PteGlu", "acide folique", "acido folico",
    "acidum folicum", "folic acid", "pteroyl-L-glutamic acid", "pteroyl-L-monoglutamic
    acid", "pteroylglutamic acid", "pteroylmonoglutamic acid", "vitamin B11", "vitamin
    B9", "vitamin Bc", "vitamin Be", "vitamin M"], "secondary": {"asserted": {"id":
    "CHEBI:27470", "label": "folic acid"}, "exact_current_rows": [{"label": "Folic
    acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[27]", "name": "Pyridoxine hydrochloride", "primary": {"id":
    "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "canonical_label": "pyridoxine
    hydrochloride", "label_equal": true, "definition": ["The hydrochloride salt of
    pyridoxine."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND500675659",
    "beilstein:3632435", "cas:58-56-0", "drugbank:DBSALT000151", "foodb.food:FDB000575",
    "gmelin:1067921", "kegg.drug:D02179", "pubmed:15098856", "pubmed:17416572", "pubmed:17891511",
    "pubmed:18243627", "pubmed:19481898", "pubmed:20645279", "pubmed:21781646", "pubmed:24421551",
    "pubmed:27468034", "pubmed:28095734", "pubmed:32460509", "pubmed:33209152", "pubmed:33936292",
    "pubmed:34140989"], "generalized_empirical_formula": ["C8H11NO3.HCl"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:30961"], "inchi_key_string": ["ZUFQODAHGAHPFQ-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C8H11NO3.ClH/c1-5-8(12)7(4-11)6(3-10)2-9-5;/h2,10-12H,3-4H2,1H3;1H"],
    "mass": ["205.641"], "monoisotopic_mass": ["205.05057"], "smiles_string": ["Cc1ncc(CO)c(CO)c1O.Cl"]},
    "synonyms": ["2-methyl-3-hydroxy-4,5-bis(hydroxymethyl)pyridine hydrochloride",
    "3-hydroxy-4,5-dimethylol-alpha-picoline hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol
    hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "5-hydroxy-6-methyl-3,4-pyridinedimethanol
    hydrochloride", "pyridoxol hydrochloride", "vitamin B6 hydrochloride"], "secondary":
    {"asserted": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "exact_current_rows":
    [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier":
    "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path":
    "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[28]",
    "name": "Thiamine HCl", "primary": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"},
    "canonical_label": "thiamine hydrochloride", "label_equal": true, "definition":
    ["A hydrochloride obtained by combining thiamine chloride with one molar equivalent
    of hydrochloric acid."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["agr:IND605711145", "agr:IND606057536", "beilstein:3642937", "beilstein:3851771",
    "cas:67-03-8", "chemspider:5967", "drugbank:DBSALT000205", "foodb.food:FDB008416",
    "gmelin:31154", "gmelin:691133", "kegg.drug:D02094", "pubmed:11548854", "pubmed:12224421",
    "pubmed:21212548", "pubmed:22305197", "pubmed:24399744", "pubmed:25977858", "pubmed:26616989",
    "pubmed:27163892", "pubmed:28763984", "pubmed:28784494", "pubmed:30131156", "pubmed:31270735",
    "pubmed:31664290", "pubmed:32009117", "pubmed:32562525", "pubmed:32824791", "reaxys:17124533"],
    "generalized_empirical_formula": ["C12H17N4OS.Cl.HCl"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:49105"], "inchi_key_string": ["DPJRMOMPQZCRJU-UHFFFAOYSA-M"], "inchi_string":
    ["InChI=1S/C12H17N4OS.2ClH/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H/q+1;;/p-1"],
    "mass": ["337.276"], "monoisotopic_mass": ["336.05784"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1.Cl.[Cl-]"]},
    "synonyms": ["3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    chloride hydrochloride", "3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    chloride hydrochloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    dichloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    dichloride", "thiamin dichloride", "thiamin hydrochloride", "thiamine HCl", "thiamine
    chloride hydrochloride", "thiamine dichloride", "thiamine(2+) dichloride", "thiaminium
    chloride hydrochloride", "vitamin B1 hydrochloride"], "secondary": {"asserted":
    {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "exact_current_rows":
    [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105",
    "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[29]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015",
    "label": "riboflavin"}, "canonical_label": "riboflavin", "label_equal": true,
    "definition": ["<small>D</small>-Ribitol in which the hydroxy group at position
    5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[<em>g</em>]pteridin-10(2<em>H</em>)-yl
    moiety. It is a nutritional factor found in milk, eggs, malted barley, liver,
    kidney, heart, and leafy vegetables, but the richest natural source is yeast.
    The free form occurs only in the retina of the eye, in whey, and in urine; its
    principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine
    dinucleotide."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:83-88-5", "chemspider:431981", "drugbank:DB00140", "drugcentral:2834", "foodb.food:FDB012160",
    "hmdb:HMDB0000244", "kegg.compound:C00255", "kegg.drug:D00050", "knapsack:C00001552",
    "lincs.smallmolecule:LSM-4084", "metacyc.compound:RIBOFLAVIN", "patent:US2807611",
    "patent:US2876169", "pdb-ccd:RBF", "pubmed:10566553", "pubmed:11399071", "pubmed:11606856",
    "pubmed:12083520", "pubmed:12354259", "pubmed:12927541", "pubmed:14963913", "pubmed:16273338",
    "pubmed:16460756", "pubmed:16658098", "pubmed:182198", "pubmed:18832377", "pubmed:19169240",
    "pubmed:19212411", "pubmed:19854891", "pubmed:22770225", "pubmed:2369885", "pubmed:23818044",
    "pubmed:24643482", "pubmed:24816110", "pubmed:25108762", "pubmed:25468971", "pubmed:25887755",
    "pubmed:2631092", "pubmed:29937405", "pubmed:3142982", "pubmed:33154451", "pubmed:33304888",
    "pubmed:33886098", "pubmed:33892358", "pubmed:34156642", "pubmed:3592624", "pubmed:3878498",
    "pubmed:4019261", "pubmed:6475825", "pubmed:6546833", "pubmed:6650303", "pubmed:7101408",
    "pubmed:7883462", "pubmed:8487103", "pubmed:8604671", "pubmed:8678471", "pubmed:8976642",
    "pubmed:9184778", "pubmed:9808225", "pubmed:9874201", "reaxys:97831", "wikipedia.en:Riboflavin"],
    "generalized_empirical_formula": ["C17H20N4O6"], "has_alternative_id": ["CHEBI:15044",
    "CHEBI:27299", "CHEBI:45214", "CHEBI:529204", "CHEBI:8843"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:17015"], "inchi_key_string": ["AUNGANRZJHBGPY-SCRDCRAPSA-N"],
    "inchi_string": ["InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23)14(25)12(24)6-22)15-13(18-9)16(26)20-17(27)19-15/h3-4,11-12,14,22-25H,5-6H2,1-2H3,(H,20,26,27)/t11-,12+,14-/m0/s1"],
    "mass": ["376.369"], "monoisotopic_mass": ["376.13828"], "smiles_string": ["Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)CO)c2cc1C"]},
    "synonyms": ["1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol",
    "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol",
    "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol",
    "5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol",
    "6,7-dimethyl-9-D-ribitylisoalloxazine", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione",
    "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine", "7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione",
    "7,8-dimethyl-10-ribitylisoalloxazine", "Aqua-Flave", "Beflavin", "Beflavine",
    "Bisulase", "Dermadram", "E101", "Fiboflavin", "Flavaxin", "Flavin Bb", "Flaxain",
    "Hyflavin", "Vitamin B2", "lactoflavin", "riboflavin (vit B2)", "riboflavin",
    "riboflavina", "riboflavine", "riboflavinum", "vitamin B2", "vitamin G", "vitasan
    B2"], "secondary": {"asserted": {"id": "CHEBI:17015", "label": "riboflavin"},
    "exact_current_rows": [{"label": "Riboflavin", "match_type": "preferred_term",
    "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path":
    "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field": "ingredients[30]",
    "name": "Nicotinic acid", "primary": {"id": "CHEBI:15940", "label": "nicotinic
    acid"}, "canonical_label": "nicotinic acid", "label_equal": true, "definition":
    ["A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position
    3 is replaced by a carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["agr:IND607088605", "cas:59-67-6", "chemspider:913", "drugbank:DB00627", "drugcentral:2835",
    "foodb.food:FDB001014", "gmelin:3340", "hmdb:HMDB0001488", "kegg.compound:C00253",
    "kegg.drug:D00049", "knapsack:C00000208", "lincs.smallmolecule:LSM-4676", "metacyc.compound:NIACINE",
    "pdb-ccd:NIO", "pubmed:10540864", "pubmed:113218", "pubmed:12563315", "pubmed:12789870",
    "pubmed:135660", "pubmed:14550884", "pubmed:15037193", "pubmed:15183629", "pubmed:15205990",
    "pubmed:15311728", "pubmed:15627518", "pubmed:15651982", "pubmed:16018787", "pubmed:16172771",
    "pubmed:16322787", "pubmed:16400392", "pubmed:16449845", "pubmed:16767301", "pubmed:16877271",
    "pubmed:16945375", "pubmed:18037924", "pubmed:182198", "pubmed:186078", "pubmed:18993152",
    "pubmed:18996527", "pubmed:19369827", "pubmed:19592242", "pubmed:19678716", "pubmed:19779335",
    "pubmed:20979384", "pubmed:21632263", "pubmed:22116693", "pubmed:22155410", "pubmed:22229411",
    "pubmed:22366213", "pubmed:22458880", "pubmed:22770225", "pubmed:24029555", "pubmed:24568240",
    "pubmed:24675661", "pubmed:24848081", "pubmed:24975217", "pubmed:25040591", "pubmed:25241762",
    "pubmed:25429652", "pubmed:32954525", "pubmed:33273654", "pubmed:33932650", "pubmed:34066686",
    "pubmed:34085526", "pubmed:34117670", "pubmed:4033386", "pubmed:4259917", "pubmed:582105",
    "pubmed:699281", "pubmed:7217784", "pubmed:7581845", "pubmed:8306147", "pubmed:8423912",
    "pubmed:8679452", "pubmed:9107536", "reaxys:109591", "wikipedia.en:Niacin"], "generalized_empirical_formula":
    ["C6H5NO2"], "has_alternative_id": ["CHEBI:25538", "CHEBI:44319", "CHEBI:7559"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15940"], "inchi_key_string":
    ["PVNIIMVLHYAWGP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"],
    "mass": ["123.111"], "monoisotopic_mass": ["123.03203"], "smiles_string": ["O=C(O)c1cccnc1"]},
    "synonyms": ["3-Pyridylcarboxylic acid", "3-carboxylpyridine", "3-carboxypyridine",
    "3-pyridinecarboxylic acid", "NICOTINIC ACID", "NICOTINIC ACID", "Niacin", "Niacor",
    "Niaspan", "Nicotinic acid", "Nicotinic acid", "Nicotinsaure", "Nikotinsaeure",
    "P.P. factor", "PP factor", "acide nicotinique", "acido nicotinico", "acidum nicotinicum",
    "anti-pellagra vitamin", "beta-pyridinecarboxylic acid", "m-pyridinecarboxylic
    acid", "nicotinic acid", "nicotinic acid", "pellagra preventive factor", "pyridine-3-carboxylic
    acid", "pyridine-3-carboxylic acid", "pyridine-beta-carboxylic acid", "pyridine-carboxylique-3",
    "vitamin B3"], "secondary": {"asserted": {"id": "CHEBI:15940", "label": "nicotinic
    acid"}, "exact_current_rows": [{"label": "Nicotinic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id":
    "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[31]", "name": "Calcium D-(+)-pantothenate", "primary": {"id":
    "CHEBI:31345", "label": "Calcium pantothenate"}, "canonical_label": "Calcium pantothenate",
    "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:137-08-6", "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278",
    "pubmed:20553011", "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula":
    ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"],
    "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"],
    "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]},
    "synonyms": ["Calcium pantotenate", "Calcium pantothenate", "Calcium pantothenate,
    d-", "Calpan", "D-ca pantothenate", "D-calcium pantothenate", "NSC-36292", "Pantholin",
    "Pantothenic acid (as calcium)", "Pantothenic acid calcium salt", "Vitamin b5,
    calcium salt", "pantotenato de calcio", "pantothenate de calcium"]}, {"layer":
    "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[32]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843",
    "label": "vitamin B12"}, "canonical_label": "vitamin B12", "label_equal": true,
    "definition": ["Any member of a group of cobalamin vitamers that exhibit biological
    activity against vitamin B<small><sub>12</sub></small> deficiency. Vitamin B<small><sub>12</sub></small>
    deficiency is associated with low red blood cell count and anemia. The vitamers
    are found in foods such as cereals, meat, fish, and poultry. The vitamers include
    adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin
    and methylcobabalamin (also includes their ionized, salt and phosphate derivatives)."],
    "annotations": {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:176843"]},
    "synonyms": ["vitamin B-12", "vitamin B12 vitamer", "vitamin B12 vitamers", "vitamin
    B12", "vitamins B12"], "secondary": {"asserted": {"id": "CHEBI:176843", "label":
    "vitamin B12"}, "exact_current_rows": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}},
    {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[33]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753",
    "label": "4-aminobenzoic acid"}, "canonical_label": "4-aminobenzoic acid", "label_equal":
    true, "definition": ["An aminobenzoic acid in which the amino group is <em>para</em>
    to the carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:150-13-0", "drugbank:DB02362", "drugcentral:2049", "ecmdb:ECMDB01392", "gmelin:50150",
    "hmdb:HMDB0001392", "kegg.compound:C00568", "kegg.drug:D02456", "knapsack:C00001401",
    "pdb-ccd:PAB", "pubmed:12039592", "pubmed:14745019", "pubmed:15115392", "pubmed:1527790",
    "pubmed:16290145", "pubmed:17149871", "pubmed:17743450", "pubmed:17800214", "pubmed:19469519",
    "pubmed:22767283", "pubmed:22994574", "pubmed:23063996", "pubmed:23084339", "pubmed:23144588",
    "pubmed:23471007", "pubmed:3599019", "pubmed:3820215", "pubmed:3950915", "pubmed:8411009",
    "pubmed:9406595", "reaxys:471605", "wikipedia.en:4-Aminobenzoic_acid", "ymdb:YMDB00493"],
    "generalized_empirical_formula": ["C7H7NO2"], "has_alternative_id": ["CHEBI:113372",
    "CHEBI:1783", "CHEBI:20315", "CHEBI:44778"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:30753"], "inchi_key_string": ["ALYNCZNDIQEVRV-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"], "mass": ["137.138"],
    "monoisotopic_mass": ["137.04768"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]}, "synonyms":
    ["1-Amino-4-carboxybenzene", "4-AMINOBENZOIC ACID", "4-AMINOBENZOIC ACID", "4-Amino-benzoic
    acid", "4-Aminobenzoesaeure", "4-Aminobenzoic acid", "4-Aminobenzoic acid", "4-Carboxyaniline",
    "4-Carboxyphenylamine", "4-aminobenzoic acid", "4-aminobenzoic acid", "ABEE",
    "PABA", "gamma-Aminobenzoic acid", "gamma-aminobenzoic acid", "p-Aminobenzoesaeure",
    "p-aminobenzoic acid", "p-carboxyaniline", "p-carboxyphenylamine", "para-aminobenzoic
    acid"], "secondary": {"asserted": {"id": "CHEBI:30753", "label": "4-aminobenzoic
    acid"}, "exact_current_rows": [{"label": "p-Aminobenzoic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic
    acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[34]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id":
    "CHEBI:16494", "label": "lipoic acid"}, "canonical_label": "lipoic acid", "label_equal":
    true, "definition": ["A heterocyclic thia fatty acid comprising pentanoic acid
    with a 1,2-dithiolan-3-yl group at the 5-position."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["beilstein:122410", "cas:62-46-4", "drugbank:DB00166",
    "drugcentral:4732", "ecmdb:ECMDB01451", "gmelin:720915", "kegg.compound:C00725",
    "kegg.drug:D00086", "pubmed:15328413", "pubmed:7519986", "pubmed:7548757", "reaxys:81853",
    "wikipedia.en:Lipoic_acid", "ymdb:YMDB00334"], "generalized_empirical_formula":
    ["C8H14O2S2"], "has_alternative_id": ["CHEBI:146958", "CHEBI:25058", "CHEBI:6492"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16494"], "inchi_key_string":
    ["AGBQKNBQESQNJD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H14O2S2/c9-8(10)4-2-1-3-7-5-6-11-12-7/h7H,1-6H2,(H,9,10)"],
    "mass": ["206.332"], "monoisotopic_mass": ["206.04352"], "smiles_string": ["O=C(O)CCCCC1CCSS1"]},
    "synonyms": ["1,2-dithiolane-3-pentanoic acid", "1,2-dithiolane-3-valeric acid",
    "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)pentanoic acid",
    "5-(1,2-dithiolan-3-yl)valeric acid", "5-(dithiolan-3-yl)valeric acid", "5-[3-(1,2-dithiolanyl)]pentanoic
    acid", "6,8-thioctic acid", "6,8-thiotic acid", "6-thioctic acid", "6-thiotic
    acid", "Acetate-replacing factor", "Biletan", "Lipoic acid", "Thioctansaeure",
    "Thioctic acid", "Thioctsaeure", "Thioktsaeure", "alpha-Lipoic acid", "alpha-Liponsaeure",
    "alpha-lipoic acid", "liponic acid"], "secondary": {"asserted": {"id": "CHEBI:16494",
    "label": "lipoic acid"}, "exact_current_rows": [{"label": "(DL)-alpha-Lipoic acid",
    "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term":
    "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[0]", "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806",
    "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition":
    [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3",
    "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"],
    "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]},
    "synonyms": ["Resazurin"]}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[1]", "name": "Na2CO3", "primary": {"id": "CHEBI:29377",
    "label": "sodium carbonate"}, "canonical_label": "sodium carbonate", "label_equal":
    true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:497-19-8", "ppdb:594"], "generalized_empirical_formula": ["CO3.2Na"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:29377"], "inchi_key_string": ["CDBYLPFSWZWCQE-UHFFFAOYSA-L"],
    "inchi_string": ["InChI=1S/CH2O3.2Na/c2-1(3)4;;/h(H2,2,3,4);;/q;2*+1/p-2"], "mass":
    ["105.988"], "monoisotopic_mass": ["105.96428"], "smiles_string": ["O=C([O-])[O-].[Na+].[Na+]"]},
    "synonyms": ["Na2CO3", "Natriumkarbonat", "disodium carbonate", "disodium trioxidocarbonate",
    "disodium trioxidocarbonate", "sodium carbonate", "sodium carbonate"], "secondary":
    {"asserted": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "exact_current_rows":
    [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377",
    "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[2]", "name": "Cellobiose", "primary": {"id": "CHEBI:17057",
    "label": "cellobiose"}, "canonical_label": "cellobiose", "label_equal": true,
    "definition": ["A glycosylglucose consisting of two glucose units linked via a
    β(1→4) bond."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1292744",
    "cas:528-50-7", "drugbank:DB02061", "kegg.compound:C00185", "knapsack:C00001134",
    "pubmed:19669625", "pubmed:19968554", "wikipedia.en:Cellobiose"], "generalized_empirical_formula":
    ["C12H22O11"], "has_alternative_id": ["CHEBI:13952", "CHEBI:23061", "CHEBI:28108",
    "CHEBI:3522"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17057"],
    "inchi_key_string": ["GUBGYTABKSRVRQ-CUHNMECISA-N"], "inchi_string": ["InChI=1S/C12H22O11/c13-1-3-5(15)6(16)9(19)12(22-3)23-10-4(2-14)21-11(20)8(18)7(10)17/h3-20H,1-2H2/t3-,4-,5-,6+,7-,8-,9-,10-,11?,12+/m1/s1"],
    "mass": ["342.297"], "monoisotopic_mass": ["342.11621"], "smiles_string": ["OC[C@H]1O[C@@H](O[C@H]2[C@H](O)[C@@H](O)C(O)O[C@@H]2CO)[C@H](O)[C@@H](O)[C@@H]1O"],
    "wurcs_representation": ["WURCS=2.0/2,2,1/[a2122h-1x_1-5][a2122h-1b_1-5]/1-2/a4-b1"]},
    "synonyms": ["1-beta-D-Glucopyranosyl-4-D-glucopyranose", "4-(beta-D-glucosido)-D-glucose",
    "4-O-beta-D-glucopyranosyl-D-glucopyranose", "4-beta-D-glucopyranosyl-D-glucopyranose",
    "Cellobiose", "D-(+)-cellobiose", "D-celiobiose", "D-cellobiose", "D-glucosyl-beta-(1-4)-D-glucose",
    "beta-D-glucopyranosyl-(1->4)-D-glucopyranose", "beta-D-glucopyranosyl-(1->4)-D-glucopyranose",
    "cellose"], "secondary": {"asserted": {"id": "CHEBI:17057", "label": "cellobiose"},
    "exact_current_rows": [{"label": "Cellobiose", "match_type": "preferred_term",
    "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path":
    "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[3]", "name": "Cellulose", "primary": {"id": "CHEBI:18246",
    "label": "(1->4)-beta-D-glucan"}, "canonical_label": "(1->4)-beta-D-glucan", "label_equal":
    true, "definition": ["A β-<small>D</small>-glucan in which the glucose units are
    connected by (1→4) linkages."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:9004-34-6", "hmdb:HMDB0006944", "kegg.compound:C00760", "kegg.drug:D00093",
    "kegg.glycan:G10481"], "generalized_empirical_formula": ["(C6H10O5)n.H2O"], "has_alternative_id":
    ["CHEBI:10812", "CHEBI:23063", "CHEBI:3529"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:18246"], "inchi_key_string": ["WQZGKKKJIJFFOK-VFUOTHLCSA-N"], "inchi_string":
    ["InChI=1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5-,6-/m1/s1"],
    "mass": ["180.156"], "monoisotopic_mass": ["180.06339"], "smiles_string": ["[H]O[C@@H]1O[C@H](CO)[C@@H](O)[C@H](O)[C@H]1O"],
    "wurcs_representation": ["WURCS=2.0/1,1,0/[a2122h-1b_1-5]/1/"]}, "synonyms": ["(1,4-beta-D-Glucosyl)n",
    "(1,4-beta-D-Glucosyl)n+1", "(1,4-beta-D-Glucosyl)n-1", "(1,4-beta-D-glucosyl)(n)",
    "(1,4-beta-D-glucosyl)n", "(1->4)-beta-D-glucopyranan", "(1->4)-beta-D-glucopyranan",
    "1,4-beta-D-Glucan", "Cellulose"], "secondary": {"asserted": {"id": "CHEBI:18246",
    "label": "(1->4)-beta-D-glucan"}, "exact_current_rows": [{"label": "Cellulose",
    "match_type": "preferred_term", "identifier": "CHEBI:18246", "preferred_term":
    "Cellulose", "ontology_id": "CHEBI:18246", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[4]", "name": "L-Cysteine HCl x H2O", "primary": {"id": "CHEBI:91248",
    "label": "L-cysteine hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride
    hydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate
    form of <small>L</small>-cysteine hydrochloride."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326",
    "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"], "inchi_key_string":
    ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"],
    "mass": ["175.637"], "monoisotopic_mass": ["175.00699"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]},
    "synonyms": ["(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)",
    "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(2R)-2-Amino-3-sulfanyl-propanoic
    acid hydrochloride monohydrate", "Cysteine hydrochloride", "L-Cysteine monohydrate
    monochloride", "L-cysteine hydrochloride monohydrate", "L-cysteine hydrochloride--water
    (1/1)", "L-cysteine hydrochloride--water (1/1)"], "secondary": {"asserted": {"id":
    "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "exact_current_rows":
    [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path":
    "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[5]", "name": "Na2S x 9 H2O", "primary": {"id": "CHEBI:76209",
    "label": "sodium sulfide nonahydrate"}, "canonical_label": "sodium sulfide nonahydrate",
    "label_equal": true, "definition": ["A hydrate with formula Na<small><sub>2</sub></small>S·9H<small><sub>2</sub></small>O."],
    "annotations": {"charge": [0.0], "database_cross_reference": ["cas:1313-84-4",
    "kegg.drug:D09001", "pubmed:19810706", "reaxys:14636099"], "generalized_empirical_formula":
    ["9H2O.2Na.S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:76209"],
    "inchi_key_string": ["ZGHLCBJZQLNUAZ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.9H2O.S/h;;9*1H2;/q2*+1;;;;;;;;;;-2"],
    "mass": ["240.182"], "monoisotopic_mass": ["240.04669"], "smiles_string": ["O.O.O.O.O.O.O.O.O.[Na+].[Na+].[S-2]"]},
    "synonyms": ["Na2S.9H2O", "Sodium sulfide (USP)", "disodium sulfide nonahydrate",
    "disodium sulfide--water (1/9)", "disodium sulfide--water (1/9)", "sodium monosulfide
    nonahydrate", "sodium monosulfide.9H2O", "sodium sulfide.9H2O"], "secondary":
    {"asserted": {"id": "CHEBI:76209", "label": "sodium sulfide nonahydrate"}, "exact_current_rows":
    [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[6]", "name": "K2HPO4", "primary": {"id": "CHEBI:131527",
    "label": "dipotassium hydrogen phosphate"}, "canonical_label": "dipotassium hydrogen
    phosphate", "label_equal": true, "definition": ["A potassium salt that is the
    dipotassium salt of phosphoric acid."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7758-11-4", "kegg.compound:C13197", "kegg.drug:D02403", "metacyc.compound:CPD0-2433",
    "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"], "generalized_empirical_formula":
    ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:131527"], "inchi_key_string": ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"],
    "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]},
    "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate",
    "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium
    orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4",
    "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium
    monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)",
    "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium
    hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate
    trihydrate"], "secondary": {"asserted": {"id": "CHEBI:131527", "label": "dipotassium
    hydrogen phosphate"}, "exact_current_rows": [{"label": "K2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[7]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036",
    "label": "potassium dihydrogen phosphate"}, "canonical_label": "potassium dihydrogen
    phosphate", "label_equal": true, "definition": ["A potassium salt in which dihydrogen
    phosphate(1−) is the counterion."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"],
    "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string":
    ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"],
    "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]},
    "synonyms": ["MKP", "Monopotassium dihydrogen phosphate", "Monopotassium monophosphate",
    "Monopotassium orthophosphate", "Monopotassium phosphate", "Orthophosphoric acid,
    monopotassium salt", "Phosphoric acid, monopotassium salt", "Phosphoric acid,
    potassium salt (1:1)", "Potassium acid phosphate", "Potassium dihydrogen orthophosphate",
    "Potassium dihydrogen phosphate", "Potassium phosphate monobasic", "Potassium
    phosphate", "Sorensen''s potassium phosphate", "potassium dihydrogen phosphate",
    "potassium dihydrogen phosphate"], "secondary": {"asserted": {"id": "CHEBI:63036",
    "label": "potassium dihydrogen phosphate"}, "exact_current_rows": [{"label": "KH2PO4",
    "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[8]", "name": "(NH4)2SO4", "primary": {"id": "CHEBI:62946",
    "label": "ammonium sulfate"}, "canonical_label": "ammonium sulfate", "label_equal":
    true, "definition": ["An inorganic sulfate salt obtained by reaction of sulfuric
    acid with two equivalents of ammonia. A high-melting (decomposes above 280°C)
    white solid which is very soluble in water (70.6 g/100 g water at 0°C; 103.8 g/100
    g water at 100°C), it is widely used as a fertilizer for alkaline soils."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7783-20-2", "kegg.drug:D08853",
    "metacyc.compound:NH42SO4", "ppdb:36", "pubmed:20556652", "reaxys:11343144", "wikipedia.en:Ammonium_sulfate"],
    "generalized_empirical_formula": ["2H4N.O4S"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:62946"], "inchi_key_string": ["BFNBIHQBYMNNAN-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/2H3N.H2O4S/c;;1-5(2,3)4/h2*1H3;(H2,1,2,3,4)"], "mass": ["132.141"],
    "monoisotopic_mass": ["132.02048"], "smiles_string": ["O=S(=O)([O-])[O-].[NH4+].[NH4+]"]},
    "synonyms": ["(NH4)2SO4", "ammonium sulfate (2:1)", "ammonium sulphate", "diammonium
    sulfate", "diazanium sulfate", "diazanium sulfate", "mascagnite", "sulfuric acid
    ammonium salt (1:2)", "sulfuric acid, diammonium salt", "sulphate of ammonia"],
    "secondary": {"asserted": {"id": "CHEBI:62946", "label": "ammonium sulfate"},
    "exact_current_rows": [{"label": "(NH4)2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path":
    "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[9]", "name": "NaCl", "primary": {"id": "CHEBI:26710", "label":
    "sodium chloride"}, "canonical_label": "sodium chloride", "label_equal": true,
    "definition": ["An inorganic chloride salt having sodium(1+) as the counterion."],
    "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5",
    "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL",
    "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula":
    ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string":
    ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"],
    "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]},
    "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro
    sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium
    chloride", "sodium chloride", "table salt"], "secondary": {"asserted": {"id":
    "CHEBI:26710", "label": "sodium chloride"}, "exact_current_rows": [{"label": "NaCl",
    "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term":
    "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[10]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795",
    "label": "magnesium sulfate heptahydrate"}, "canonical_label": "magnesium sulfate
    heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate
    form of magnesium sulfate."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505",
    "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222",
    "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"],
    "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]},
    "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom
    salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate
    heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)",
    "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"],
    "secondary": {"asserted": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"},
    "exact_current_rows": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[11]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158",
    "label": "calcium chloride dihydrate"}, "canonical_label": "calcium chloride dihydrate",
    "label_equal": true, "definition": ["A hydrate that is the dihydrate form of calcium
    chloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8",
    "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"],
    "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass":
    ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}, "synonyms": ["CaCl2.2H2O",
    "Calcium chloride hydrate", "Calcium chloride", "calcium chloride--water (1/2)",
    "calcium chloride--water (1/2)", "calcium dichloride dihydrate"], "secondary":
    {"asserted": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "exact_current_rows":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[12]", "name": "Nitrilotriacetic acid", "primary": {"id":
    "CHEBI:44557", "label": "nitrilotriacetic acid"}, "canonical_label": "nitrilotriacetic
    acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0],
    "database_cross_reference": ["beilstein:1710776", "cas:139-13-9", "drugbank:DB03040",
    "gmelin:3726", "kegg.compound:C14695", "pdb-ccd:NTA"], "generalized_empirical_formula":
    ["C6H9NO6"], "has_alternative_id": ["CHEBI:34889", "CHEBI:44555"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:44557"], "inchi_key_string": ["MGFYIUFZLHCRTH-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"],
    "mass": ["191.139"], "monoisotopic_mass": ["191.04299"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]},
    "synonyms": ["Complexon I", "H3nta", "Komplexon I", "N(CH2-COOH)3", "N,N-bis(carboxymethyl)glycine",
    "N,N-bis(carboxymethyl)glycine", "NITRILOTRIACETIC ACID", "NTA", "Nitrilotriacetate",
    "Nitrilotriacetic acid", "Nitrilotriessigsaeure", "Triglycollamic acid", "Trilon
    A", "alpha,alpha'',alpha''''-trimethylaminetricarboxylic acid", "nitrilo-2,2'',2''''-triacetic
    acid", "tri(carboxymethyl)amine", "triglycine"], "secondary": {"asserted": {"id":
    "CHEBI:44557", "label": "nitrilotriacetic acid"}, "exact_current_rows": [{"label":
    "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557",
    "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[13]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364",
    "label": "manganese(II) sulfate monohydrate"}, "canonical_label": "manganese(II)
    sulfate monohydrate", "label_equal": true, "definition": ["A hydrate that is the
    monohydrate form of manganese(II) sulfate."], "annotations": {"charge": [0.0],
    "database_cross_reference": ["cas:10034-96-5", "kegg.drug:D04854", "pubmed:26097037",
    "reaxys:13153017", "wikipedia.en:Manganese(II)_sulfate"], "generalized_empirical_formula":
    ["H2O.Mn.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86364"],
    "inchi_key_string": ["ISPYRSDWRDQNSW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mn.H2O4S.H2O/c;1-5(2,3)4;/h;(H2,1,2,3,4);1H2/q+2;;/p-2"],
    "mass": ["169.016"], "monoisotopic_mass": ["168.90034"], "smiles_string": ["O.O=S(=O)([O-])[O-].[Mn+2]"]},
    "synonyms": ["Manganese sulfate hydrate", "Manganese sulfate monohydrate", "Manganese
    sulfate", "Manganous sulfate monohydrate", "MnSO4.H2O", "manganese(2+) sulfate
    monohydrate", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulfate--water
    (1/1)", "manganese(2+) sulphate monohydrate", "manganese(II) sulphate monohydrate"],
    "secondary": {"asserted": {"id": "CHEBI:86364", "label": "manganese(II) sulfate
    monohydrate"}, "exact_current_rows": [{"label": "MnSO4 x H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path":
    "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[14]", "name": "FeSO4 x 7 H2O", "primary": {"id": "CHEBI:75836",
    "label": "iron(2+) sulfate heptahydrate"}, "canonical_label": "iron(2+) sulfate
    heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate
    form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency
    anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the
    monohydrate is normally used)."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890",
    "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id":
    ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"],
    "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]},
    "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous
    sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol",
    "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O",
    "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"], "secondary": {"asserted":
    {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "exact_current_rows":
    [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[15]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244",
    "label": "cobalt(2+) sulfate heptahydrate"}, "canonical_label": "cobalt(2+) sulfate
    heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate
    form of cobalt(2+) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:10026-24-1", "pubmed:10504146", "pubmed:12187935", "pubmed:12209163", "pubmed:12579202",
    "pubmed:12948248", "pubmed:2227161", "pubmed:24359163", "pubmed:25896363", "wikipedia.en:Cobalt(II)_sulfate"],
    "generalized_empirical_formula": ["Co.7H2O.O4S"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:91244"], "inchi_key_string": ["MEYVLGVRTYSQHI-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Co.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["281.101"], "monoisotopic_mass": ["280.95888"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Co+2]"]},
    "synonyms": ["Cobalt monosulfate heptahydrate", "cobalt sulfate heptahydrate",
    "cobalt(2+) sulfate--water (1/7)", "cobalt(2+) sulfate--water (1/7)", "cobalt(II)
    sulfate heptahydrate", "cobaltous sulfate heptahydrate"], "secondary": {"asserted":
    {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "exact_current_rows":
    [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244",
    "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[16]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312",
    "label": "zinc sulfate heptahydrate"}, "canonical_label": "zinc sulfate heptahydrate",
    "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of
    zinc sulfate."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7446-20-0", "gmelin:47216", "kegg.drug:D01081", "wikipedia.en:Zinc_Sulfate"],
    "generalized_empirical_formula": ["7H2O.O4S.Zn"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:32312"], "inchi_key_string": ["RZLVQBNCHSJZPX-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/H2O4S.7H2O.Zn/c1-5(2,3)4;;;;;;;;/h(H2,1,2,3,4);7*1H2;/q;;;;;;;;+2/p-2"],
    "mass": ["287.558"], "monoisotopic_mass": ["285.95482"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Zn+2]"]},
    "synonyms": ["Zinc sulfate", "ZnSO4.7H2O", "zinc sulfate (1:1) heptahydrate",
    "zinc sulfate heptahydrate (1:1:7)", "zinc(2+) sulfate heptahydrate", "zinc(2+)
    sulfate heptahydrate", "zinc(2+) sulfate--water (1/7)", "zinc(2+) sulfate--water
    (1/7)"], "secondary": {"asserted": {"id": "CHEBI:32312", "label": "zinc sulfate
    heptahydrate"}, "exact_current_rows": [{"label": "ZnSO4 x 7 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O",
    "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}},
    {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[17]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440",
    "label": "copper(II) sulfate pentahydrate"}, "canonical_label": "copper(II) sulfate
    pentahydrate", "label_equal": true, "definition": ["The pentahydrate of copper(2+)
    sulfate. A bright blue crystalline solid."], "annotations": {"charge": [0.0],
    "database_cross_reference": ["cas:7758-99-8", "kegg.drug:D03613", "pubmed:11407502",
    "pubmed:12209195", "pubmed:12484481", "pubmed:15040745", "pubmed:15607472", "pubmed:15824790",
    "pubmed:19346702", "pubmed:2002460", "pubmed:20132934", "pubmed:2913309", "pubmed:3351847",
    "pubmed:7615984", "pubmed:8878264", "pubmed:9521458", "pubmed:9776063", "reaxys:16499970",
    "wikipedia.en:Copper(II)_sulfate"], "generalized_empirical_formula": ["Cu.5H2O.O4S"],
    "has_alternative_id": ["CHEBI:121741", "CHEBI:370227"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:31440"], "inchi_key_string": ["JZCCFEFSEZPSOG-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Cu.H2O4S.5H2O/c;1-5(2,3)4;;;;;/h;(H2,1,2,3,4);5*1H2/q+2;;;;;;/p-2"],
    "mass": ["249.684"], "monoisotopic_mass": ["248.93415"], "smiles_string": ["O=S(=O)([O-])[O-].[Cu+2].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H]"]},
    "synonyms": ["CuSO4.5H2O", "Cupric sulfate", "copper sulphate(5.H2O)", "copper(2+)
    sulfate (1:1) pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate
    pentahydrate", "copper(2+) sulfate--water (1/5)", "copper(2+) sulfate--water (1/5)",
    "copper(II) sulfate, pentahydrate", "cupric sulfate pentahydrate"], "secondary":
    {"asserted": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"},
    "exact_current_rows": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[18]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465",
    "label": "potassium aluminium sulfate dodecahydrate"}, "canonical_label": "potassium
    aluminium sulfate dodecahydrate", "label_equal": true, "definition": ["A hydrate
    resulting from the the formal combination of anhydrous potassium aluminium sulfate
    with 12 mol eq. of water."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7784-24-9", "reaxys:14851666", "wikipedia.en:Potassium_alum"], "generalized_empirical_formula":
    ["Al.12H2O.K.2O4S"], "has_alternative_id": ["CHEBI:31192"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:86465"], "inchi_key_string": ["GNHOJBNSNUXZQA-UHFFFAOYSA-J"],
    "inchi_string": ["InChI=1S/Al.K.2H2O4S.12H2O/c;;2*1-5(2,3)4;;;;;;;;;;;;/h;;2*(H2,1,2,3,4);12*1H2/q+3;+1;;;;;;;;;;;;;;/p-4"],
    "mass": ["474.386"], "monoisotopic_mass": ["473.97548"], "smiles_string": ["O.O.O.O.O.O.O.O.O.O.O.O.O=S(=O)([O-])[O-].O=S(=O)([O-])[O-].[Al+3].[K+]"]},
    "synonyms": ["AlK(SO4)2.12H2O", "Aluminum potassium disulfate dodecahydrate",
    "Aluminum potassium sulfate dodecahydrate", "Kalinite", "Potash alum dodecahydrate",
    "Potassium alum dodecahydrate", "Potassium aluminum disulfate dodecahydrate",
    "aluminium potassium sulfate--water (1/12)", "aluminium potassium sulfate--water
    (1/12)"], "secondary": {"asserted": {"id": "CHEBI:86465", "label": "potassium
    aluminium sulfate dodecahydrate"}, "exact_current_rows": [{"label": "AlK(SO4)2
    x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term":
    "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[19]", "name": "H3BO3", "primary": {"id": "CHEBI:33118",
    "label": "boric acid"}, "canonical_label": "boric acid", "label_equal": true,
    "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["bpdb:2136", "cas:10043-35-3", "cas:11113-50-1", "drugcentral:3035", "gmelin:1585",
    "kegg.compound:C12486", "kegg.drug:D01089", "molbase:1644", "pdb-ccd:BO3", "ppdb:2136"],
    "generalized_empirical_formula": ["H3BO3"], "has_alternative_id": ["CHEBI:22911",
    "CHEBI:31299", "CHEBI:41248"], "has_obo_namespace": ["chebi_ontology"], "id":
    ["CHEBI:33118"], "inchi_key_string": ["KGBXLFKZBHKPEV-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"], "mass": ["61.833"], "monoisotopic_mass": ["62.01752"],
    "smiles_string": ["[H]OB(O[H])O[H]"]}, "synonyms": ["B(OH)3", "BORIC ACID", "Boric
    acid", "H3BO3", "[B(OH)3]", "boric acid", "boron trihydroxide", "orthoboric acid",
    "trihydroxidoboron", "trihydroxidoboron"], "secondary": {"asserted": {"id": "CHEBI:33118",
    "label": "boric acid"}, "exact_current_rows": [{"label": "H3BO3", "match_type":
    "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[20]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213",
    "label": "sodium molybdate dihydrate"}, "canonical_label": "sodium molybdate dihydrate",
    "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium
    molybdate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10102-40-6",
    "pubmed:20645132", "pubmed:20813395", "pubmed:22663766", "pubmed:3382795", "reaxys:19032996",
    "wikipedia.en:Sodium_molybdate"], "generalized_empirical_formula": ["2H2O.MoO4.2Na"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75213"], "inchi_key_string":
    ["FDEIWTXVNPKYDL-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/Mo.2Na.2H2O.4O/h;;;2*1H2;;;;/q;2*+1;;;;;2*-1"],
    "mass": ["241.946"], "monoisotopic_mass": ["243.88573"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]},
    "synonyms": ["Disodium molybdate dihydrate", "Molybdic acid, disodium salt, dihydrate",
    "Na2MoO4.2H2O", "Sodium molybdate(VI) dihydrate", "sodium dioxido(dioxo)molybdenum--water
    (1/2)", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium orthomolybdate
    dihydrate"], "secondary": {"asserted": {"id": "CHEBI:75213", "label": "sodium
    molybdate dihydrate"}, "exact_current_rows": [{"label": "Na2MoO4 x 2 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2
    H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}]}},
    {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[21]", "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887",
    "label": "nickel dichloride"}, "canonical_label": "nickel dichloride", "label_equal":
    true, "definition": ["A compound of nickel and chloride in which the ratio of
    nickel (in the +2 oxidation state) to chloride is 1:2."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:7718-54-9", "kegg.compound:C14711", "pubmed:11739495",
    "pubmed:12603851", "pubmed:21928331", "pubmed:23179351", "pubmed:23622879", "pubmed:23702803",
    "pubmed:23735035", "pubmed:7671317", "reaxys:3902827", "reaxys:8128171", "wikipedia.en:Nickel_dichloride"],
    "generalized_empirical_formula": ["Cl2Ni"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:34887"], "inchi_key_string": ["QMMRZOWCJAIUJA-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"], "mass": ["129.599"], "monoisotopic_mass":
    ["127.87305"], "smiles_string": ["[Cl][Ni][Cl]"]}, "synonyms": ["NiCl2", "Nickel
    chloride", "Nickel(II) chloride", "[NiCl2]", "nickel dichloride", "nickel dichloride",
    "nickel(2+) chloride", "nickel(2+) chloride", "nickel(II) chloride", "nickel(II)
    chloride", "nickelous chloride"], "secondary": {"asserted": {"id": "CHEBI:34887",
    "label": "nickel dichloride"}, "exact_current_rows": [{"label": "NiCl2", "match_type":
    "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id":
    "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[22]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361",
    "label": "disodium selenite pentahydrate"}, "canonical_label": "disodium selenite
    pentahydrate", "label_equal": true, "definition": ["A hydrate that is the pentahydrate
    form of disodium selenite."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:26970-82-1", "pubmed:15259772", "pubmed:15559373", "pubmed:16126997", "pubmed:17873396",
    "pubmed:24479345", "pubmed:24716537", "reaxys:14666014", "wikipedia.en:Sodium_selenite"],
    "generalized_empirical_formula": ["5H2O.2Na.O3Se"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:131361"], "inchi_key_string": ["TUANAMBRHOLYTH-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"],
    "mass": ["263.012"], "monoisotopic_mass": ["263.93363"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]},
    "synonyms": ["Na2SeO3.5H2O", "Selenious acid disodium salt, pentahydrate", "Sodium
    selenite pentahydrate", "disodium selenite hydrate", "sodium selenite hydrate",
    "sodium selenite--water (1/5)", "sodium selenite--water (1/5)"], "secondary":
    {"asserted": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"},
    "exact_current_rows": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id":
    "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[23]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939",
    "label": "sodium tungstate dihydrate"}, "canonical_label": "sodium tungstate dihydrate",
    "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium
    tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines
    to nitrones"], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10213-10-2",
    "reaxys:13157884", "wikipedia.en:Sodium_tungstate"], "generalized_empirical_formula":
    ["2H2O.2Na.O4W"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63939"],
    "inchi_key_string": ["WPZFLQRLSGVIAA-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.2H2O.4O.W/h;;2*1H2;;;;;/q2*+1;;;;;2*-1;"],
    "mass": ["329.846"], "monoisotopic_mass": ["329.93126"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]},
    "synonyms": ["Na2WO4.2H2O", "Tungstic acid, sodium salt, dihydrate", "sodium dioxido(dioxo)tungsten--water
    (1/2)", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium orthotungstate dihydrate",
    "sodium tungstate(VI) dihydrate"], "secondary": {"asserted": {"id": "CHEBI:63939",
    "label": "sodium tungstate dihydrate"}, "exact_current_rows": [{"label": "Na2WO4
    x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term":
    "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[24]", "name": "H2SO4", "primary": {"id": "CHEBI:26836",
    "label": "sulfuric acid"}, "canonical_label": "sulfuric acid", "label_equal":
    true, "definition": ["A sulfur oxoacid that consists of two oxo and two hydroxy
    groups joined covalently to a central sulfur atom."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:7664-93-9", "gmelin:2122", "kegg.compound:C00059",
    "kegg.drug:D05963", "knapsack:C00007530", "molbase:4", "ppdb:606", "pubmed:13568755",
    "pubmed:16122922", "pubmed:19397353", "pubmed:22047659", "pubmed:22136045", "pubmed:22204399",
    "pubmed:22267186", "pubmed:22296037", "pubmed:22364556", "pubmed:22435616", "reaxys:2037554",
    "wikipedia.en:Sulfuric_acid"], "generalized_empirical_formula": ["H2O4S"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:26836"], "inchi_key_string": ["QAOWNCQODCNURD-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/H2O4S/c1-5(2,3)4/h(H2,1,2,3,4)"], "mass": ["98.079"],
    "monoisotopic_mass": ["97.96738"], "smiles_string": ["[H]OS(=O)(=O)O[H]"]}, "synonyms":
    ["Acide sulfurique", "Acido sulfurico", "Acidum sulfuricum", "H2SO4", "Schwefelsaeureloesungen",
    "Sulfuric acid", "[S(OH)2O2]", "[SO2(OH)2]", "dihydrogen tetraoxosulfate", "dihydrogen
    tetraoxosulfate", "dihydroxidodioxidosulfur", "dihydroxidodioxidosulfur", "hydrogen
    tetraoxosulfate(2-)", "hydrogen tetraoxosulfate(2-)", "hydrogen tetraoxosulfate(VI)",
    "hydrogen tetraoxosulfate(VI)", "sulfuric acid", "sulfuric acid", "sulphuric acid",
    "tetraoxosulfuric acid", "tetraoxosulfuric acid"], "secondary": {"asserted": {"id":
    "CHEBI:26836", "label": "sulfuric acid"}, "exact_current_rows": [{"label": "H2SO4",
    "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term":
    "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[25]", "name": "Biotin", "primary": {"id": "CHEBI:15956",
    "label": "biotin"}, "canonical_label": "biotin", "label_equal": true, "definition":
    ["An organic heterobicyclic compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
    having a valeric acid substituent attached to the tetrahydrothiophene ring. The
    parent of the class of biotins."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:58-85-5", "chemspider:149962", "drugbank:DB00121", "drugcentral:373", "foodb.food:FDB014510",
    "gmelin:1918703", "hmdb:HMDB0000030", "kegg.compound:C00120", "kegg.drug:D00029",
    "knapsack:C00000756", "lincs.smallmolecule:LSM-3994", "metacyc.compound:BIOTIN",
    "pdb-ccd:BTN", "pmc:PMC8089577", "pubmed:10064317", "pubmed:10215065", "pubmed:10577274",
    "pubmed:11435506", "pubmed:11481419", "pubmed:11800048", "pubmed:12055344", "pubmed:12070309",
    "pubmed:12603856", "pubmed:12803839", "pubmed:15012185", "pubmed:15202718", "pubmed:15272000",
    "pubmed:15690449", "pubmed:15863846", "pubmed:15899401", "pubmed:15992684", "pubmed:16011464",
    "pubmed:16195795", "pubmed:16419467", "pubmed:16676358", "pubmed:16677798", "pubmed:16704206",
    "pubmed:16769720", "pubmed:17297119", "pubmed:1814646", "pubmed:18202531", "pubmed:18452485",
    "pubmed:18509457", "pubmed:19212411", "pubmed:19319844", "pubmed:19727438", "pubmed:19928962",
    "pubmed:20967359", "pubmed:20974274", "pubmed:2100006", "pubmed:21248194", "pubmed:21356565",
    "pubmed:21373679", "pubmed:21596550", "pubmed:21871906", "pubmed:25515858", "pubmed:33346513",
    "pubmed:33461365", "pubmed:34077272", "pubmed:8333586", "pubmed:8750932", "pubmed:9022537",
    "pubmed:9038855", "pubmed:9094878", "pubmed:9164991", "pubmed:9176832", "pubmed:9371938",
    "pubmed:9416479", "reaxys:86838", "wikipedia.en:Biotin"], "generalized_empirical_formula":
    ["C10H16N2O3S"], "has_alternative_id": ["CHEBI:13905", "CHEBI:22882", "CHEBI:22884",
    "CHEBI:3108", "CHEBI:41236"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15956"],
    "inchi_key_string": ["YBJHBAHKTGYVGT-ZKWXMUAHSA-N"], "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"],
    "mass": ["244.316"], "monoisotopic_mass": ["244.08816"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]},
    "synonyms": ["(+)-cis-Hexahydro-2-oxo-1H-thieno[3,4]imidazole-4-valeric acid",
    "(3aS,4S,6aR)-Hexahydro-2-oxo-1H-thieno[3,4-d]imidazole-4-valeric acid", "5-(2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl)pentanoic
    acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic
    acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic
    acid", "BIOTIN", "Coenzyme R", "D-(+)-biotin", "D-Biotin", "Vitamin H", "biotin",
    "biotina", "biotine", "biotinum", "cis-(+)-Tetrahydro-2-oxothieno[3,4]imidazoline-4-valeric
    acid", "cis-Hexahydro-2-oxo-1H-thieno(3,4)imidazole-4-valeric acid", "cis-Tetrahydro-2-oxothieno(3,4-d)imidazoline-4-valeric
    acid", "vitamin B7"], "secondary": {"asserted": {"id": "CHEBI:15956", "label":
    "biotin"}, "exact_current_rows": [{"label": "Biotin", "match_type": "preferred_term",
    "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path":
    "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[26]", "name": "Folic acid", "primary": {"id": "CHEBI:27470",
    "label": "folic acid"}, "canonical_label": "folic acid", "label_equal": true,
    "definition": ["An <em>N</em>-acyl-amino acid that is a form of the water-soluble
    vitamin B<small><sub>9</sub></small>. Its biologically active forms (tetrahydrofolate
    and others) are essential for nucleotide biosynthesis and homocysteine remethylation."],
    "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND606960789",
    "cas:59-30-3", "chemspider:5815", "drugbank:DB00158", "drugcentral:1231", "foodb.food:FDB014504",
    "hmdb:HMDB0000121", "kegg.compound:C00504", "kegg.drug:D00070", "knapsack:C00001539",
    "lincs.smallmolecule:LSM-5355", "metacyc.compound:CPD-12826", "pdb-ccd:FOL", "pubmed:10138938",
    "pubmed:10897644", "pubmed:10958818", "pubmed:11261364", "pubmed:11451208", "pubmed:11959400",
    "pubmed:14387833", "pubmed:15321809", "pubmed:15523939", "pubmed:15754725", "pubmed:15797531",
    "pubmed:15797685", "pubmed:15831910", "pubmed:15990733", "pubmed:16093404", "pubmed:16277678",
    "pubmed:16380297", "pubmed:16871332", "pubmed:17784727", "pubmed:18788725", "pubmed:19121630",
    "pubmed:19335717", "pubmed:19355913", "pubmed:24650098", "pubmed:33624660", "pubmed:33965562",
    "pubmed:33968971", "pubmed:34207319", "pubmed:34219855", "pubmed:7738698", "pubmed:8235383",
    "pubmed:9040515", "pubmed:9420019", "pubmed:9565830", "pubmed:9683174", "pubmed:9781393",
    "pubmed:9808640", "pubmed:9808641", "reaxys:100781", "wikipedia.en:Folic_Acid"],
    "generalized_empirical_formula": ["C19H19N7O6"], "has_alternative_id": ["CHEBI:24075",
    "CHEBI:42610", "CHEBI:5140", "CHEBI:569217"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:27470"], "inchi_key_string": ["OVBPIULPVIDEAO-LBPRGKRZSA-N"], "inchi_string":
    ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"],
    "mass": ["441.404"], "monoisotopic_mass": ["441.13968"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]},
    "synonyms": ["(2S)-2-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzamido)pentanedioic
    acid", "Acfol", "Folate", "Folicet", "Folsaeure", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic
    acid", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic
    acid", "N-[(4-{[(2-amino-4-oxo-1,4-dihydropteridin-6-yl)methyl]amino}phenyl)carbonyl]-L-glutamic
    acid", "N-pteroyl-L-glutamic acid", "PGA", "PteGlu", "acide folique", "acido folico",
    "acidum folicum", "folic acid", "pteroyl-L-glutamic acid", "pteroyl-L-monoglutamic
    acid", "pteroylglutamic acid", "pteroylmonoglutamic acid", "vitamin B11", "vitamin
    B9", "vitamin Bc", "vitamin Be", "vitamin M"], "secondary": {"asserted": {"id":
    "CHEBI:27470", "label": "folic acid"}, "exact_current_rows": [{"label": "Folic
    acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[27]", "name": "Pyridoxine hydrochloride", "primary": {"id":
    "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "canonical_label": "pyridoxine
    hydrochloride", "label_equal": true, "definition": ["The hydrochloride salt of
    pyridoxine."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND500675659",
    "beilstein:3632435", "cas:58-56-0", "drugbank:DBSALT000151", "foodb.food:FDB000575",
    "gmelin:1067921", "kegg.drug:D02179", "pubmed:15098856", "pubmed:17416572", "pubmed:17891511",
    "pubmed:18243627", "pubmed:19481898", "pubmed:20645279", "pubmed:21781646", "pubmed:24421551",
    "pubmed:27468034", "pubmed:28095734", "pubmed:32460509", "pubmed:33209152", "pubmed:33936292",
    "pubmed:34140989"], "generalized_empirical_formula": ["C8H11NO3.HCl"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:30961"], "inchi_key_string": ["ZUFQODAHGAHPFQ-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C8H11NO3.ClH/c1-5-8(12)7(4-11)6(3-10)2-9-5;/h2,10-12H,3-4H2,1H3;1H"],
    "mass": ["205.641"], "monoisotopic_mass": ["205.05057"], "smiles_string": ["Cc1ncc(CO)c(CO)c1O.Cl"]},
    "synonyms": ["2-methyl-3-hydroxy-4,5-bis(hydroxymethyl)pyridine hydrochloride",
    "3-hydroxy-4,5-dimethylol-alpha-picoline hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol
    hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "5-hydroxy-6-methyl-3,4-pyridinedimethanol
    hydrochloride", "pyridoxol hydrochloride", "vitamin B6 hydrochloride"], "secondary":
    {"asserted": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "exact_current_rows":
    [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier":
    "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path":
    "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[28]", "name": "Thiamine HCl", "primary": {"id": "CHEBI:49105",
    "label": "thiamine hydrochloride"}, "canonical_label": "thiamine hydrochloride",
    "label_equal": true, "definition": ["A hydrochloride obtained by combining thiamine
    chloride with one molar equivalent of hydrochloric acid."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["agr:IND605711145", "agr:IND606057536", "beilstein:3642937",
    "beilstein:3851771", "cas:67-03-8", "chemspider:5967", "drugbank:DBSALT000205",
    "foodb.food:FDB008416", "gmelin:31154", "gmelin:691133", "kegg.drug:D02094", "pubmed:11548854",
    "pubmed:12224421", "pubmed:21212548", "pubmed:22305197", "pubmed:24399744", "pubmed:25977858",
    "pubmed:26616989", "pubmed:27163892", "pubmed:28763984", "pubmed:28784494", "pubmed:30131156",
    "pubmed:31270735", "pubmed:31664290", "pubmed:32009117", "pubmed:32562525", "pubmed:32824791",
    "reaxys:17124533"], "generalized_empirical_formula": ["C12H17N4OS.Cl.HCl"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:49105"], "inchi_key_string": ["DPJRMOMPQZCRJU-UHFFFAOYSA-M"],
    "inchi_string": ["InChI=1S/C12H17N4OS.2ClH/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H/q+1;;/p-1"],
    "mass": ["337.276"], "monoisotopic_mass": ["336.05784"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1.Cl.[Cl-]"]},
    "synonyms": ["3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    chloride hydrochloride", "3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    chloride hydrochloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    dichloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    dichloride", "thiamin dichloride", "thiamin hydrochloride", "thiamine HCl", "thiamine
    chloride hydrochloride", "thiamine dichloride", "thiamine(2+) dichloride", "thiaminium
    chloride hydrochloride", "vitamin B1 hydrochloride"], "secondary": {"asserted":
    {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "exact_current_rows":
    [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105",
    "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[29]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015",
    "label": "riboflavin"}, "canonical_label": "riboflavin", "label_equal": true,
    "definition": ["<small>D</small>-Ribitol in which the hydroxy group at position
    5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[<em>g</em>]pteridin-10(2<em>H</em>)-yl
    moiety. It is a nutritional factor found in milk, eggs, malted barley, liver,
    kidney, heart, and leafy vegetables, but the richest natural source is yeast.
    The free form occurs only in the retina of the eye, in whey, and in urine; its
    principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine
    dinucleotide."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:83-88-5", "chemspider:431981", "drugbank:DB00140", "drugcentral:2834", "foodb.food:FDB012160",
    "hmdb:HMDB0000244", "kegg.compound:C00255", "kegg.drug:D00050", "knapsack:C00001552",
    "lincs.smallmolecule:LSM-4084", "metacyc.compound:RIBOFLAVIN", "patent:US2807611",
    "patent:US2876169", "pdb-ccd:RBF", "pubmed:10566553", "pubmed:11399071", "pubmed:11606856",
    "pubmed:12083520", "pubmed:12354259", "pubmed:12927541", "pubmed:14963913", "pubmed:16273338",
    "pubmed:16460756", "pubmed:16658098", "pubmed:182198", "pubmed:18832377", "pubmed:19169240",
    "pubmed:19212411", "pubmed:19854891", "pubmed:22770225", "pubmed:2369885", "pubmed:23818044",
    "pubmed:24643482", "pubmed:24816110", "pubmed:25108762", "pubmed:25468971", "pubmed:25887755",
    "pubmed:2631092", "pubmed:29937405", "pubmed:3142982", "pubmed:33154451", "pubmed:33304888",
    "pubmed:33886098", "pubmed:33892358", "pubmed:34156642", "pubmed:3592624", "pubmed:3878498",
    "pubmed:4019261", "pubmed:6475825", "pubmed:6546833", "pubmed:6650303", "pubmed:7101408",
    "pubmed:7883462", "pubmed:8487103", "pubmed:8604671", "pubmed:8678471", "pubmed:8976642",
    "pubmed:9184778", "pubmed:9808225", "pubmed:9874201", "reaxys:97831", "wikipedia.en:Riboflavin"],
    "generalized_empirical_formula": ["C17H20N4O6"], "has_alternative_id": ["CHEBI:15044",
    "CHEBI:27299", "CHEBI:45214", "CHEBI:529204", "CHEBI:8843"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:17015"], "inchi_key_string": ["AUNGANRZJHBGPY-SCRDCRAPSA-N"],
    "inchi_string": ["InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23)14(25)12(24)6-22)15-13(18-9)16(26)20-17(27)19-15/h3-4,11-12,14,22-25H,5-6H2,1-2H3,(H,20,26,27)/t11-,12+,14-/m0/s1"],
    "mass": ["376.369"], "monoisotopic_mass": ["376.13828"], "smiles_string": ["Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)CO)c2cc1C"]},
    "synonyms": ["1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol",
    "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol",
    "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol",
    "5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol",
    "6,7-dimethyl-9-D-ribitylisoalloxazine", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione",
    "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine", "7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione",
    "7,8-dimethyl-10-ribitylisoalloxazine", "Aqua-Flave", "Beflavin", "Beflavine",
    "Bisulase", "Dermadram", "E101", "Fiboflavin", "Flavaxin", "Flavin Bb", "Flaxain",
    "Hyflavin", "Vitamin B2", "lactoflavin", "riboflavin (vit B2)", "riboflavin",
    "riboflavina", "riboflavine", "riboflavinum", "vitamin B2", "vitamin G", "vitasan
    B2"], "secondary": {"asserted": {"id": "CHEBI:17015", "label": "riboflavin"},
    "exact_current_rows": [{"label": "Riboflavin", "match_type": "preferred_term",
    "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path":
    "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[30]", "name": "Nicotinic acid", "primary": {"id": "CHEBI:15940",
    "label": "nicotinic acid"}, "canonical_label": "nicotinic acid", "label_equal":
    true, "definition": ["A pyridinemonocarboxylic acid that is pyridine in which
    the hydrogen at position 3 is replaced by a carboxy group."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["agr:IND607088605", "cas:59-67-6", "chemspider:913",
    "drugbank:DB00627", "drugcentral:2835", "foodb.food:FDB001014", "gmelin:3340",
    "hmdb:HMDB0001488", "kegg.compound:C00253", "kegg.drug:D00049", "knapsack:C00000208",
    "lincs.smallmolecule:LSM-4676", "metacyc.compound:NIACINE", "pdb-ccd:NIO", "pubmed:10540864",
    "pubmed:113218", "pubmed:12563315", "pubmed:12789870", "pubmed:135660", "pubmed:14550884",
    "pubmed:15037193", "pubmed:15183629", "pubmed:15205990", "pubmed:15311728", "pubmed:15627518",
    "pubmed:15651982", "pubmed:16018787", "pubmed:16172771", "pubmed:16322787", "pubmed:16400392",
    "pubmed:16449845", "pubmed:16767301", "pubmed:16877271", "pubmed:16945375", "pubmed:18037924",
    "pubmed:182198", "pubmed:186078", "pubmed:18993152", "pubmed:18996527", "pubmed:19369827",
    "pubmed:19592242", "pubmed:19678716", "pubmed:19779335", "pubmed:20979384", "pubmed:21632263",
    "pubmed:22116693", "pubmed:22155410", "pubmed:22229411", "pubmed:22366213", "pubmed:22458880",
    "pubmed:22770225", "pubmed:24029555", "pubmed:24568240", "pubmed:24675661", "pubmed:24848081",
    "pubmed:24975217", "pubmed:25040591", "pubmed:25241762", "pubmed:25429652", "pubmed:32954525",
    "pubmed:33273654", "pubmed:33932650", "pubmed:34066686", "pubmed:34085526", "pubmed:34117670",
    "pubmed:4033386", "pubmed:4259917", "pubmed:582105", "pubmed:699281", "pubmed:7217784",
    "pubmed:7581845", "pubmed:8306147", "pubmed:8423912", "pubmed:8679452", "pubmed:9107536",
    "reaxys:109591", "wikipedia.en:Niacin"], "generalized_empirical_formula": ["C6H5NO2"],
    "has_alternative_id": ["CHEBI:25538", "CHEBI:44319", "CHEBI:7559"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:15940"], "inchi_key_string": ["PVNIIMVLHYAWGP-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"], "mass":
    ["123.111"], "monoisotopic_mass": ["123.03203"], "smiles_string": ["O=C(O)c1cccnc1"]},
    "synonyms": ["3-Pyridylcarboxylic acid", "3-carboxylpyridine", "3-carboxypyridine",
    "3-pyridinecarboxylic acid", "NICOTINIC ACID", "NICOTINIC ACID", "Niacin", "Niacor",
    "Niaspan", "Nicotinic acid", "Nicotinic acid", "Nicotinsaure", "Nikotinsaeure",
    "P.P. factor", "PP factor", "acide nicotinique", "acido nicotinico", "acidum nicotinicum",
    "anti-pellagra vitamin", "beta-pyridinecarboxylic acid", "m-pyridinecarboxylic
    acid", "nicotinic acid", "nicotinic acid", "pellagra preventive factor", "pyridine-3-carboxylic
    acid", "pyridine-3-carboxylic acid", "pyridine-beta-carboxylic acid", "pyridine-carboxylique-3",
    "vitamin B3"], "secondary": {"asserted": {"id": "CHEBI:15940", "label": "nicotinic
    acid"}, "exact_current_rows": [{"label": "Nicotinic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id":
    "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[31]", "name": "Calcium D-(+)-pantothenate", "primary": {"id":
    "CHEBI:31345", "label": "Calcium pantothenate"}, "canonical_label": "Calcium pantothenate",
    "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:137-08-6", "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278",
    "pubmed:20553011", "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula":
    ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"],
    "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"],
    "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]},
    "synonyms": ["Calcium pantotenate", "Calcium pantothenate", "Calcium pantothenate,
    d-", "Calpan", "D-ca pantothenate", "D-calcium pantothenate", "NSC-36292", "Pantholin",
    "Pantothenic acid (as calcium)", "Pantothenic acid calcium salt", "Vitamin b5,
    calcium salt", "pantotenato de calcio", "pantothenate de calcium"]}, {"layer":
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[32]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843",
    "label": "vitamin B12"}, "canonical_label": "vitamin B12", "label_equal": true,
    "definition": ["Any member of a group of cobalamin vitamers that exhibit biological
    activity against vitamin B<small><sub>12</sub></small> deficiency. Vitamin B<small><sub>12</sub></small>
    deficiency is associated with low red blood cell count and anemia. The vitamers
    are found in foods such as cereals, meat, fish, and poultry. The vitamers include
    adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin
    and methylcobabalamin (also includes their ionized, salt and phosphate derivatives)."],
    "annotations": {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:176843"]},
    "synonyms": ["vitamin B-12", "vitamin B12 vitamer", "vitamin B12 vitamers", "vitamin
    B12", "vitamins B12"], "secondary": {"asserted": {"id": "CHEBI:176843", "label":
    "vitamin B12"}, "exact_current_rows": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}},
    {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[33]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753",
    "label": "4-aminobenzoic acid"}, "canonical_label": "4-aminobenzoic acid", "label_equal":
    true, "definition": ["An aminobenzoic acid in which the amino group is <em>para</em>
    to the carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:150-13-0", "drugbank:DB02362", "drugcentral:2049", "ecmdb:ECMDB01392", "gmelin:50150",
    "hmdb:HMDB0001392", "kegg.compound:C00568", "kegg.drug:D02456", "knapsack:C00001401",
    "pdb-ccd:PAB", "pubmed:12039592", "pubmed:14745019", "pubmed:15115392", "pubmed:1527790",
    "pubmed:16290145", "pubmed:17149871", "pubmed:17743450", "pubmed:17800214", "pubmed:19469519",
    "pubmed:22767283", "pubmed:22994574", "pubmed:23063996", "pubmed:23084339", "pubmed:23144588",
    "pubmed:23471007", "pubmed:3599019", "pubmed:3820215", "pubmed:3950915", "pubmed:8411009",
    "pubmed:9406595", "reaxys:471605", "wikipedia.en:4-Aminobenzoic_acid", "ymdb:YMDB00493"],
    "generalized_empirical_formula": ["C7H7NO2"], "has_alternative_id": ["CHEBI:113372",
    "CHEBI:1783", "CHEBI:20315", "CHEBI:44778"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:30753"], "inchi_key_string": ["ALYNCZNDIQEVRV-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"], "mass": ["137.138"],
    "monoisotopic_mass": ["137.04768"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]}, "synonyms":
    ["1-Amino-4-carboxybenzene", "4-AMINOBENZOIC ACID", "4-AMINOBENZOIC ACID", "4-Amino-benzoic
    acid", "4-Aminobenzoesaeure", "4-Aminobenzoic acid", "4-Aminobenzoic acid", "4-Carboxyaniline",
    "4-Carboxyphenylamine", "4-aminobenzoic acid", "4-aminobenzoic acid", "ABEE",
    "PABA", "gamma-Aminobenzoic acid", "gamma-aminobenzoic acid", "p-Aminobenzoesaeure",
    "p-aminobenzoic acid", "p-carboxyaniline", "p-carboxyphenylamine", "para-aminobenzoic
    acid"], "secondary": {"asserted": {"id": "CHEBI:30753", "label": "4-aminobenzoic
    acid"}, "exact_current_rows": [{"label": "p-Aminobenzoic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic
    acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field": "ingredients[34]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id":
    "CHEBI:16494", "label": "lipoic acid"}, "canonical_label": "lipoic acid", "label_equal":
    true, "definition": ["A heterocyclic thia fatty acid comprising pentanoic acid
    with a 1,2-dithiolan-3-yl group at the 5-position."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["beilstein:122410", "cas:62-46-4", "drugbank:DB00166",
    "drugcentral:4732", "ecmdb:ECMDB01451", "gmelin:720915", "kegg.compound:C00725",
    "kegg.drug:D00086", "pubmed:15328413", "pubmed:7519986", "pubmed:7548757", "reaxys:81853",
    "wikipedia.en:Lipoic_acid", "ymdb:YMDB00334"], "generalized_empirical_formula":
    ["C8H14O2S2"], "has_alternative_id": ["CHEBI:146958", "CHEBI:25058", "CHEBI:6492"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16494"], "inchi_key_string":
    ["AGBQKNBQESQNJD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H14O2S2/c9-8(10)4-2-1-3-7-5-6-11-12-7/h7H,1-6H2,(H,9,10)"],
    "mass": ["206.332"], "monoisotopic_mass": ["206.04352"], "smiles_string": ["O=C(O)CCCCC1CCSS1"]},
    "synonyms": ["1,2-dithiolane-3-pentanoic acid", "1,2-dithiolane-3-valeric acid",
    "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)pentanoic acid",
    "5-(1,2-dithiolan-3-yl)valeric acid", "5-(dithiolan-3-yl)valeric acid", "5-[3-(1,2-dithiolanyl)]pentanoic
    acid", "6,8-thioctic acid", "6,8-thiotic acid", "6-thioctic acid", "6-thiotic
    acid", "Acetate-replacing factor", "Biletan", "Lipoic acid", "Thioctansaeure",
    "Thioctic acid", "Thioctsaeure", "Thioktsaeure", "alpha-Lipoic acid", "alpha-Liponsaeure",
    "alpha-lipoic acid", "liponic acid"], "secondary": {"asserted": {"id": "CHEBI:16494",
    "label": "lipoic acid"}, "exact_current_rows": [{"label": "(DL)-alpha-Lipoic acid",
    "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term":
    "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[0]", "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806",
    "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition":
    [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3",
    "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"],
    "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]},
    "synonyms": ["Resazurin"]}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[1]", "name": "Na2CO3", "primary": {"id": "CHEBI:29377",
    "label": "sodium carbonate"}, "canonical_label": "sodium carbonate", "label_equal":
    true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:497-19-8", "ppdb:594"], "generalized_empirical_formula": ["CO3.2Na"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:29377"], "inchi_key_string": ["CDBYLPFSWZWCQE-UHFFFAOYSA-L"],
    "inchi_string": ["InChI=1S/CH2O3.2Na/c2-1(3)4;;/h(H2,2,3,4);;/q;2*+1/p-2"], "mass":
    ["105.988"], "monoisotopic_mass": ["105.96428"], "smiles_string": ["O=C([O-])[O-].[Na+].[Na+]"]},
    "synonyms": ["Na2CO3", "Natriumkarbonat", "disodium carbonate", "disodium trioxidocarbonate",
    "disodium trioxidocarbonate", "sodium carbonate", "sodium carbonate"], "secondary":
    {"asserted": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "exact_current_rows":
    [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377",
    "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[2]", "name": "Cellobiose", "primary": {"id": "CHEBI:17057",
    "label": "cellobiose"}, "canonical_label": "cellobiose", "label_equal": true,
    "definition": ["A glycosylglucose consisting of two glucose units linked via a
    β(1→4) bond."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1292744",
    "cas:528-50-7", "drugbank:DB02061", "kegg.compound:C00185", "knapsack:C00001134",
    "pubmed:19669625", "pubmed:19968554", "wikipedia.en:Cellobiose"], "generalized_empirical_formula":
    ["C12H22O11"], "has_alternative_id": ["CHEBI:13952", "CHEBI:23061", "CHEBI:28108",
    "CHEBI:3522"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17057"],
    "inchi_key_string": ["GUBGYTABKSRVRQ-CUHNMECISA-N"], "inchi_string": ["InChI=1S/C12H22O11/c13-1-3-5(15)6(16)9(19)12(22-3)23-10-4(2-14)21-11(20)8(18)7(10)17/h3-20H,1-2H2/t3-,4-,5-,6+,7-,8-,9-,10-,11?,12+/m1/s1"],
    "mass": ["342.297"], "monoisotopic_mass": ["342.11621"], "smiles_string": ["OC[C@H]1O[C@@H](O[C@H]2[C@H](O)[C@@H](O)C(O)O[C@@H]2CO)[C@H](O)[C@@H](O)[C@@H]1O"],
    "wurcs_representation": ["WURCS=2.0/2,2,1/[a2122h-1x_1-5][a2122h-1b_1-5]/1-2/a4-b1"]},
    "synonyms": ["1-beta-D-Glucopyranosyl-4-D-glucopyranose", "4-(beta-D-glucosido)-D-glucose",
    "4-O-beta-D-glucopyranosyl-D-glucopyranose", "4-beta-D-glucopyranosyl-D-glucopyranose",
    "Cellobiose", "D-(+)-cellobiose", "D-celiobiose", "D-cellobiose", "D-glucosyl-beta-(1-4)-D-glucose",
    "beta-D-glucopyranosyl-(1->4)-D-glucopyranose", "beta-D-glucopyranosyl-(1->4)-D-glucopyranose",
    "cellose"], "secondary": {"asserted": {"id": "CHEBI:17057", "label": "cellobiose"},
    "exact_current_rows": [{"label": "Cellobiose", "match_type": "preferred_term",
    "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path":
    "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field":
    "ingredients[3]", "name": "Cellulose", "primary": {"id": "CHEBI:18246", "label":
    "(1->4)-beta-D-glucan"}, "canonical_label": "(1->4)-beta-D-glucan", "label_equal":
    true, "definition": ["A β-<small>D</small>-glucan in which the glucose units are
    connected by (1→4) linkages."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:9004-34-6", "hmdb:HMDB0006944", "kegg.compound:C00760", "kegg.drug:D00093",
    "kegg.glycan:G10481"], "generalized_empirical_formula": ["(C6H10O5)n.H2O"], "has_alternative_id":
    ["CHEBI:10812", "CHEBI:23063", "CHEBI:3529"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:18246"], "inchi_key_string": ["WQZGKKKJIJFFOK-VFUOTHLCSA-N"], "inchi_string":
    ["InChI=1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5-,6-/m1/s1"],
    "mass": ["180.156"], "monoisotopic_mass": ["180.06339"], "smiles_string": ["[H]O[C@@H]1O[C@H](CO)[C@@H](O)[C@H](O)[C@H]1O"],
    "wurcs_representation": ["WURCS=2.0/1,1,0/[a2122h-1b_1-5]/1/"]}, "synonyms": ["(1,4-beta-D-Glucosyl)n",
    "(1,4-beta-D-Glucosyl)n+1", "(1,4-beta-D-Glucosyl)n-1", "(1,4-beta-D-glucosyl)(n)",
    "(1,4-beta-D-glucosyl)n", "(1->4)-beta-D-glucopyranan", "(1->4)-beta-D-glucopyranan",
    "1,4-beta-D-Glucan", "Cellulose"], "secondary": {"asserted": {"id": "CHEBI:18246",
    "label": "(1->4)-beta-D-glucan"}, "exact_current_rows": [{"label": "Cellulose",
    "match_type": "preferred_term", "identifier": "CHEBI:18246", "preferred_term":
    "Cellulose", "ontology_id": "CHEBI:18246", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[4]", "name": "L-Cysteine HCl x H2O", "primary": {"id": "CHEBI:91248",
    "label": "L-cysteine hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride
    hydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate
    form of <small>L</small>-cysteine hydrochloride."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326",
    "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"], "inchi_key_string":
    ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"],
    "mass": ["175.637"], "monoisotopic_mass": ["175.00699"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]},
    "synonyms": ["(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)",
    "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(2R)-2-Amino-3-sulfanyl-propanoic
    acid hydrochloride monohydrate", "Cysteine hydrochloride", "L-Cysteine monohydrate
    monochloride", "L-cysteine hydrochloride monohydrate", "L-cysteine hydrochloride--water
    (1/1)", "L-cysteine hydrochloride--water (1/1)"], "secondary": {"asserted": {"id":
    "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "exact_current_rows":
    [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path":
    "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field":
    "ingredients[5]", "name": "Na2S x 9 H2O", "primary": {"id": "CHEBI:76209", "label":
    "sodium sulfide nonahydrate"}, "canonical_label": "sodium sulfide nonahydrate",
    "label_equal": true, "definition": ["A hydrate with formula Na<small><sub>2</sub></small>S·9H<small><sub>2</sub></small>O."],
    "annotations": {"charge": [0.0], "database_cross_reference": ["cas:1313-84-4",
    "kegg.drug:D09001", "pubmed:19810706", "reaxys:14636099"], "generalized_empirical_formula":
    ["9H2O.2Na.S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:76209"],
    "inchi_key_string": ["ZGHLCBJZQLNUAZ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.9H2O.S/h;;9*1H2;/q2*+1;;;;;;;;;;-2"],
    "mass": ["240.182"], "monoisotopic_mass": ["240.04669"], "smiles_string": ["O.O.O.O.O.O.O.O.O.[Na+].[Na+].[S-2]"]},
    "synonyms": ["Na2S.9H2O", "Sodium sulfide (USP)", "disodium sulfide nonahydrate",
    "disodium sulfide--water (1/9)", "disodium sulfide--water (1/9)", "sodium monosulfide
    nonahydrate", "sodium monosulfide.9H2O", "sodium sulfide.9H2O"], "secondary":
    {"asserted": {"id": "CHEBI:76209", "label": "sodium sulfide nonahydrate"}, "exact_current_rows":
    [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[6]", "name": "K2HPO4", "primary": {"id": "CHEBI:131527",
    "label": "dipotassium hydrogen phosphate"}, "canonical_label": "dipotassium hydrogen
    phosphate", "label_equal": true, "definition": ["A potassium salt that is the
    dipotassium salt of phosphoric acid."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7758-11-4", "kegg.compound:C13197", "kegg.drug:D02403", "metacyc.compound:CPD0-2433",
    "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"], "generalized_empirical_formula":
    ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:131527"], "inchi_key_string": ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"],
    "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]},
    "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate",
    "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium
    orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4",
    "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium
    monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)",
    "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium
    hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate
    trihydrate"], "secondary": {"asserted": {"id": "CHEBI:131527", "label": "dipotassium
    hydrogen phosphate"}, "exact_current_rows": [{"label": "K2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[7]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036",
    "label": "potassium dihydrogen phosphate"}, "canonical_label": "potassium dihydrogen
    phosphate", "label_equal": true, "definition": ["A potassium salt in which dihydrogen
    phosphate(1−) is the counterion."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"],
    "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string":
    ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"],
    "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]},
    "synonyms": ["MKP", "Monopotassium dihydrogen phosphate", "Monopotassium monophosphate",
    "Monopotassium orthophosphate", "Monopotassium phosphate", "Orthophosphoric acid,
    monopotassium salt", "Phosphoric acid, monopotassium salt", "Phosphoric acid,
    potassium salt (1:1)", "Potassium acid phosphate", "Potassium dihydrogen orthophosphate",
    "Potassium dihydrogen phosphate", "Potassium phosphate monobasic", "Potassium
    phosphate", "Sorensen''s potassium phosphate", "potassium dihydrogen phosphate",
    "potassium dihydrogen phosphate"], "secondary": {"asserted": {"id": "CHEBI:63036",
    "label": "potassium dihydrogen phosphate"}, "exact_current_rows": [{"label": "KH2PO4",
    "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[8]", "name": "(NH4)2SO4", "primary": {"id": "CHEBI:62946",
    "label": "ammonium sulfate"}, "canonical_label": "ammonium sulfate", "label_equal":
    true, "definition": ["An inorganic sulfate salt obtained by reaction of sulfuric
    acid with two equivalents of ammonia. A high-melting (decomposes above 280°C)
    white solid which is very soluble in water (70.6 g/100 g water at 0°C; 103.8 g/100
    g water at 100°C), it is widely used as a fertilizer for alkaline soils."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7783-20-2", "kegg.drug:D08853",
    "metacyc.compound:NH42SO4", "ppdb:36", "pubmed:20556652", "reaxys:11343144", "wikipedia.en:Ammonium_sulfate"],
    "generalized_empirical_formula": ["2H4N.O4S"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:62946"], "inchi_key_string": ["BFNBIHQBYMNNAN-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/2H3N.H2O4S/c;;1-5(2,3)4/h2*1H3;(H2,1,2,3,4)"], "mass": ["132.141"],
    "monoisotopic_mass": ["132.02048"], "smiles_string": ["O=S(=O)([O-])[O-].[NH4+].[NH4+]"]},
    "synonyms": ["(NH4)2SO4", "ammonium sulfate (2:1)", "ammonium sulphate", "diammonium
    sulfate", "diazanium sulfate", "diazanium sulfate", "mascagnite", "sulfuric acid
    ammonium salt (1:2)", "sulfuric acid, diammonium salt", "sulphate of ammonia"],
    "secondary": {"asserted": {"id": "CHEBI:62946", "label": "ammonium sulfate"},
    "exact_current_rows": [{"label": "(NH4)2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path":
    "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field":
    "ingredients[9]", "name": "NaCl", "primary": {"id": "CHEBI:26710", "label": "sodium
    chloride"}, "canonical_label": "sodium chloride", "label_equal": true, "definition":
    ["An inorganic chloride salt having sodium(1+) as the counterion."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673",
    "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595",
    "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula":
    ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string":
    ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"],
    "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]},
    "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro
    sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium
    chloride", "sodium chloride", "table salt"], "secondary": {"asserted": {"id":
    "CHEBI:26710", "label": "sodium chloride"}, "exact_current_rows": [{"label": "NaCl",
    "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term":
    "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[10]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795",
    "label": "magnesium sulfate heptahydrate"}, "canonical_label": "magnesium sulfate
    heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate
    form of magnesium sulfate."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505",
    "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222",
    "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"],
    "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]},
    "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom
    salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate
    heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)",
    "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"],
    "secondary": {"asserted": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"},
    "exact_current_rows": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[11]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158",
    "label": "calcium chloride dihydrate"}, "canonical_label": "calcium chloride dihydrate",
    "label_equal": true, "definition": ["A hydrate that is the dihydrate form of calcium
    chloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8",
    "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"],
    "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass":
    ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}, "synonyms": ["CaCl2.2H2O",
    "Calcium chloride hydrate", "Calcium chloride", "calcium chloride--water (1/2)",
    "calcium chloride--water (1/2)", "calcium dichloride dihydrate"], "secondary":
    {"asserted": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "exact_current_rows":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[12]", "name": "Nitrilotriacetic acid", "primary": {"id":
    "CHEBI:44557", "label": "nitrilotriacetic acid"}, "canonical_label": "nitrilotriacetic
    acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0],
    "database_cross_reference": ["beilstein:1710776", "cas:139-13-9", "drugbank:DB03040",
    "gmelin:3726", "kegg.compound:C14695", "pdb-ccd:NTA"], "generalized_empirical_formula":
    ["C6H9NO6"], "has_alternative_id": ["CHEBI:34889", "CHEBI:44555"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:44557"], "inchi_key_string": ["MGFYIUFZLHCRTH-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"],
    "mass": ["191.139"], "monoisotopic_mass": ["191.04299"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]},
    "synonyms": ["Complexon I", "H3nta", "Komplexon I", "N(CH2-COOH)3", "N,N-bis(carboxymethyl)glycine",
    "N,N-bis(carboxymethyl)glycine", "NITRILOTRIACETIC ACID", "NTA", "Nitrilotriacetate",
    "Nitrilotriacetic acid", "Nitrilotriessigsaeure", "Triglycollamic acid", "Trilon
    A", "alpha,alpha'',alpha''''-trimethylaminetricarboxylic acid", "nitrilo-2,2'',2''''-triacetic
    acid", "tri(carboxymethyl)amine", "triglycine"], "secondary": {"asserted": {"id":
    "CHEBI:44557", "label": "nitrilotriacetic acid"}, "exact_current_rows": [{"label":
    "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557",
    "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[13]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364",
    "label": "manganese(II) sulfate monohydrate"}, "canonical_label": "manganese(II)
    sulfate monohydrate", "label_equal": true, "definition": ["A hydrate that is the
    monohydrate form of manganese(II) sulfate."], "annotations": {"charge": [0.0],
    "database_cross_reference": ["cas:10034-96-5", "kegg.drug:D04854", "pubmed:26097037",
    "reaxys:13153017", "wikipedia.en:Manganese(II)_sulfate"], "generalized_empirical_formula":
    ["H2O.Mn.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86364"],
    "inchi_key_string": ["ISPYRSDWRDQNSW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mn.H2O4S.H2O/c;1-5(2,3)4;/h;(H2,1,2,3,4);1H2/q+2;;/p-2"],
    "mass": ["169.016"], "monoisotopic_mass": ["168.90034"], "smiles_string": ["O.O=S(=O)([O-])[O-].[Mn+2]"]},
    "synonyms": ["Manganese sulfate hydrate", "Manganese sulfate monohydrate", "Manganese
    sulfate", "Manganous sulfate monohydrate", "MnSO4.H2O", "manganese(2+) sulfate
    monohydrate", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulfate--water
    (1/1)", "manganese(2+) sulphate monohydrate", "manganese(II) sulphate monohydrate"],
    "secondary": {"asserted": {"id": "CHEBI:86364", "label": "manganese(II) sulfate
    monohydrate"}, "exact_current_rows": [{"label": "MnSO4 x H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path":
    "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field":
    "ingredients[14]", "name": "FeSO4 x 7 H2O", "primary": {"id": "CHEBI:75836", "label":
    "iron(2+) sulfate heptahydrate"}, "canonical_label": "iron(2+) sulfate heptahydrate",
    "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of
    iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency
    anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the
    monohydrate is normally used)."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890",
    "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id":
    ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"],
    "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]},
    "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous
    sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol",
    "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O",
    "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"], "secondary": {"asserted":
    {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "exact_current_rows":
    [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[15]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244",
    "label": "cobalt(2+) sulfate heptahydrate"}, "canonical_label": "cobalt(2+) sulfate
    heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate
    form of cobalt(2+) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:10026-24-1", "pubmed:10504146", "pubmed:12187935", "pubmed:12209163", "pubmed:12579202",
    "pubmed:12948248", "pubmed:2227161", "pubmed:24359163", "pubmed:25896363", "wikipedia.en:Cobalt(II)_sulfate"],
    "generalized_empirical_formula": ["Co.7H2O.O4S"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:91244"], "inchi_key_string": ["MEYVLGVRTYSQHI-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Co.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["281.101"], "monoisotopic_mass": ["280.95888"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Co+2]"]},
    "synonyms": ["Cobalt monosulfate heptahydrate", "cobalt sulfate heptahydrate",
    "cobalt(2+) sulfate--water (1/7)", "cobalt(2+) sulfate--water (1/7)", "cobalt(II)
    sulfate heptahydrate", "cobaltous sulfate heptahydrate"], "secondary": {"asserted":
    {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "exact_current_rows":
    [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244",
    "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[16]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312",
    "label": "zinc sulfate heptahydrate"}, "canonical_label": "zinc sulfate heptahydrate",
    "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of
    zinc sulfate."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7446-20-0", "gmelin:47216", "kegg.drug:D01081", "wikipedia.en:Zinc_Sulfate"],
    "generalized_empirical_formula": ["7H2O.O4S.Zn"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:32312"], "inchi_key_string": ["RZLVQBNCHSJZPX-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/H2O4S.7H2O.Zn/c1-5(2,3)4;;;;;;;;/h(H2,1,2,3,4);7*1H2;/q;;;;;;;;+2/p-2"],
    "mass": ["287.558"], "monoisotopic_mass": ["285.95482"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Zn+2]"]},
    "synonyms": ["Zinc sulfate", "ZnSO4.7H2O", "zinc sulfate (1:1) heptahydrate",
    "zinc sulfate heptahydrate (1:1:7)", "zinc(2+) sulfate heptahydrate", "zinc(2+)
    sulfate heptahydrate", "zinc(2+) sulfate--water (1/7)", "zinc(2+) sulfate--water
    (1/7)"], "secondary": {"asserted": {"id": "CHEBI:32312", "label": "zinc sulfate
    heptahydrate"}, "exact_current_rows": [{"label": "ZnSO4 x 7 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O",
    "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}},
    {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[17]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440",
    "label": "copper(II) sulfate pentahydrate"}, "canonical_label": "copper(II) sulfate
    pentahydrate", "label_equal": true, "definition": ["The pentahydrate of copper(2+)
    sulfate. A bright blue crystalline solid."], "annotations": {"charge": [0.0],
    "database_cross_reference": ["cas:7758-99-8", "kegg.drug:D03613", "pubmed:11407502",
    "pubmed:12209195", "pubmed:12484481", "pubmed:15040745", "pubmed:15607472", "pubmed:15824790",
    "pubmed:19346702", "pubmed:2002460", "pubmed:20132934", "pubmed:2913309", "pubmed:3351847",
    "pubmed:7615984", "pubmed:8878264", "pubmed:9521458", "pubmed:9776063", "reaxys:16499970",
    "wikipedia.en:Copper(II)_sulfate"], "generalized_empirical_formula": ["Cu.5H2O.O4S"],
    "has_alternative_id": ["CHEBI:121741", "CHEBI:370227"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:31440"], "inchi_key_string": ["JZCCFEFSEZPSOG-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Cu.H2O4S.5H2O/c;1-5(2,3)4;;;;;/h;(H2,1,2,3,4);5*1H2/q+2;;;;;;/p-2"],
    "mass": ["249.684"], "monoisotopic_mass": ["248.93415"], "smiles_string": ["O=S(=O)([O-])[O-].[Cu+2].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H]"]},
    "synonyms": ["CuSO4.5H2O", "Cupric sulfate", "copper sulphate(5.H2O)", "copper(2+)
    sulfate (1:1) pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate
    pentahydrate", "copper(2+) sulfate--water (1/5)", "copper(2+) sulfate--water (1/5)",
    "copper(II) sulfate, pentahydrate", "cupric sulfate pentahydrate"], "secondary":
    {"asserted": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"},
    "exact_current_rows": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[18]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465",
    "label": "potassium aluminium sulfate dodecahydrate"}, "canonical_label": "potassium
    aluminium sulfate dodecahydrate", "label_equal": true, "definition": ["A hydrate
    resulting from the the formal combination of anhydrous potassium aluminium sulfate
    with 12 mol eq. of water."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7784-24-9", "reaxys:14851666", "wikipedia.en:Potassium_alum"], "generalized_empirical_formula":
    ["Al.12H2O.K.2O4S"], "has_alternative_id": ["CHEBI:31192"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:86465"], "inchi_key_string": ["GNHOJBNSNUXZQA-UHFFFAOYSA-J"],
    "inchi_string": ["InChI=1S/Al.K.2H2O4S.12H2O/c;;2*1-5(2,3)4;;;;;;;;;;;;/h;;2*(H2,1,2,3,4);12*1H2/q+3;+1;;;;;;;;;;;;;;/p-4"],
    "mass": ["474.386"], "monoisotopic_mass": ["473.97548"], "smiles_string": ["O.O.O.O.O.O.O.O.O.O.O.O.O=S(=O)([O-])[O-].O=S(=O)([O-])[O-].[Al+3].[K+]"]},
    "synonyms": ["AlK(SO4)2.12H2O", "Aluminum potassium disulfate dodecahydrate",
    "Aluminum potassium sulfate dodecahydrate", "Kalinite", "Potash alum dodecahydrate",
    "Potassium alum dodecahydrate", "Potassium aluminum disulfate dodecahydrate",
    "aluminium potassium sulfate--water (1/12)", "aluminium potassium sulfate--water
    (1/12)"], "secondary": {"asserted": {"id": "CHEBI:86465", "label": "potassium
    aluminium sulfate dodecahydrate"}, "exact_current_rows": [{"label": "AlK(SO4)2
    x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term":
    "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[19]", "name": "H3BO3", "primary": {"id": "CHEBI:33118",
    "label": "boric acid"}, "canonical_label": "boric acid", "label_equal": true,
    "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["bpdb:2136", "cas:10043-35-3", "cas:11113-50-1", "drugcentral:3035", "gmelin:1585",
    "kegg.compound:C12486", "kegg.drug:D01089", "molbase:1644", "pdb-ccd:BO3", "ppdb:2136"],
    "generalized_empirical_formula": ["H3BO3"], "has_alternative_id": ["CHEBI:22911",
    "CHEBI:31299", "CHEBI:41248"], "has_obo_namespace": ["chebi_ontology"], "id":
    ["CHEBI:33118"], "inchi_key_string": ["KGBXLFKZBHKPEV-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"], "mass": ["61.833"], "monoisotopic_mass": ["62.01752"],
    "smiles_string": ["[H]OB(O[H])O[H]"]}, "synonyms": ["B(OH)3", "BORIC ACID", "Boric
    acid", "H3BO3", "[B(OH)3]", "boric acid", "boron trihydroxide", "orthoboric acid",
    "trihydroxidoboron", "trihydroxidoboron"], "secondary": {"asserted": {"id": "CHEBI:33118",
    "label": "boric acid"}, "exact_current_rows": [{"label": "H3BO3", "match_type":
    "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[20]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213",
    "label": "sodium molybdate dihydrate"}, "canonical_label": "sodium molybdate dihydrate",
    "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium
    molybdate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10102-40-6",
    "pubmed:20645132", "pubmed:20813395", "pubmed:22663766", "pubmed:3382795", "reaxys:19032996",
    "wikipedia.en:Sodium_molybdate"], "generalized_empirical_formula": ["2H2O.MoO4.2Na"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75213"], "inchi_key_string":
    ["FDEIWTXVNPKYDL-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/Mo.2Na.2H2O.4O/h;;;2*1H2;;;;/q;2*+1;;;;;2*-1"],
    "mass": ["241.946"], "monoisotopic_mass": ["243.88573"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]},
    "synonyms": ["Disodium molybdate dihydrate", "Molybdic acid, disodium salt, dihydrate",
    "Na2MoO4.2H2O", "Sodium molybdate(VI) dihydrate", "sodium dioxido(dioxo)molybdenum--water
    (1/2)", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium orthomolybdate
    dihydrate"], "secondary": {"asserted": {"id": "CHEBI:75213", "label": "sodium
    molybdate dihydrate"}, "exact_current_rows": [{"label": "Na2MoO4 x 2 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2
    H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}]}},
    {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[21]", "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887",
    "label": "nickel dichloride"}, "canonical_label": "nickel dichloride", "label_equal":
    true, "definition": ["A compound of nickel and chloride in which the ratio of
    nickel (in the +2 oxidation state) to chloride is 1:2."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:7718-54-9", "kegg.compound:C14711", "pubmed:11739495",
    "pubmed:12603851", "pubmed:21928331", "pubmed:23179351", "pubmed:23622879", "pubmed:23702803",
    "pubmed:23735035", "pubmed:7671317", "reaxys:3902827", "reaxys:8128171", "wikipedia.en:Nickel_dichloride"],
    "generalized_empirical_formula": ["Cl2Ni"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:34887"], "inchi_key_string": ["QMMRZOWCJAIUJA-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"], "mass": ["129.599"], "monoisotopic_mass":
    ["127.87305"], "smiles_string": ["[Cl][Ni][Cl]"]}, "synonyms": ["NiCl2", "Nickel
    chloride", "Nickel(II) chloride", "[NiCl2]", "nickel dichloride", "nickel dichloride",
    "nickel(2+) chloride", "nickel(2+) chloride", "nickel(II) chloride", "nickel(II)
    chloride", "nickelous chloride"], "secondary": {"asserted": {"id": "CHEBI:34887",
    "label": "nickel dichloride"}, "exact_current_rows": [{"label": "NiCl2", "match_type":
    "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id":
    "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[22]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361",
    "label": "disodium selenite pentahydrate"}, "canonical_label": "disodium selenite
    pentahydrate", "label_equal": true, "definition": ["A hydrate that is the pentahydrate
    form of disodium selenite."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:26970-82-1", "pubmed:15259772", "pubmed:15559373", "pubmed:16126997", "pubmed:17873396",
    "pubmed:24479345", "pubmed:24716537", "reaxys:14666014", "wikipedia.en:Sodium_selenite"],
    "generalized_empirical_formula": ["5H2O.2Na.O3Se"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:131361"], "inchi_key_string": ["TUANAMBRHOLYTH-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"],
    "mass": ["263.012"], "monoisotopic_mass": ["263.93363"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]},
    "synonyms": ["Na2SeO3.5H2O", "Selenious acid disodium salt, pentahydrate", "Sodium
    selenite pentahydrate", "disodium selenite hydrate", "sodium selenite hydrate",
    "sodium selenite--water (1/5)", "sodium selenite--water (1/5)"], "secondary":
    {"asserted": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"},
    "exact_current_rows": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id":
    "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[23]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939",
    "label": "sodium tungstate dihydrate"}, "canonical_label": "sodium tungstate dihydrate",
    "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium
    tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines
    to nitrones"], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10213-10-2",
    "reaxys:13157884", "wikipedia.en:Sodium_tungstate"], "generalized_empirical_formula":
    ["2H2O.2Na.O4W"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63939"],
    "inchi_key_string": ["WPZFLQRLSGVIAA-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.2H2O.4O.W/h;;2*1H2;;;;;/q2*+1;;;;;2*-1;"],
    "mass": ["329.846"], "monoisotopic_mass": ["329.93126"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]},
    "synonyms": ["Na2WO4.2H2O", "Tungstic acid, sodium salt, dihydrate", "sodium dioxido(dioxo)tungsten--water
    (1/2)", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium orthotungstate dihydrate",
    "sodium tungstate(VI) dihydrate"], "secondary": {"asserted": {"id": "CHEBI:63939",
    "label": "sodium tungstate dihydrate"}, "exact_current_rows": [{"label": "Na2WO4
    x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term":
    "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[24]", "name": "H2SO4", "primary": {"id": "CHEBI:26836",
    "label": "sulfuric acid"}, "canonical_label": "sulfuric acid", "label_equal":
    true, "definition": ["A sulfur oxoacid that consists of two oxo and two hydroxy
    groups joined covalently to a central sulfur atom."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:7664-93-9", "gmelin:2122", "kegg.compound:C00059",
    "kegg.drug:D05963", "knapsack:C00007530", "molbase:4", "ppdb:606", "pubmed:13568755",
    "pubmed:16122922", "pubmed:19397353", "pubmed:22047659", "pubmed:22136045", "pubmed:22204399",
    "pubmed:22267186", "pubmed:22296037", "pubmed:22364556", "pubmed:22435616", "reaxys:2037554",
    "wikipedia.en:Sulfuric_acid"], "generalized_empirical_formula": ["H2O4S"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:26836"], "inchi_key_string": ["QAOWNCQODCNURD-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/H2O4S/c1-5(2,3)4/h(H2,1,2,3,4)"], "mass": ["98.079"],
    "monoisotopic_mass": ["97.96738"], "smiles_string": ["[H]OS(=O)(=O)O[H]"]}, "synonyms":
    ["Acide sulfurique", "Acido sulfurico", "Acidum sulfuricum", "H2SO4", "Schwefelsaeureloesungen",
    "Sulfuric acid", "[S(OH)2O2]", "[SO2(OH)2]", "dihydrogen tetraoxosulfate", "dihydrogen
    tetraoxosulfate", "dihydroxidodioxidosulfur", "dihydroxidodioxidosulfur", "hydrogen
    tetraoxosulfate(2-)", "hydrogen tetraoxosulfate(2-)", "hydrogen tetraoxosulfate(VI)",
    "hydrogen tetraoxosulfate(VI)", "sulfuric acid", "sulfuric acid", "sulphuric acid",
    "tetraoxosulfuric acid", "tetraoxosulfuric acid"], "secondary": {"asserted": {"id":
    "CHEBI:26836", "label": "sulfuric acid"}, "exact_current_rows": [{"label": "H2SO4",
    "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term":
    "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[25]", "name": "Biotin", "primary": {"id": "CHEBI:15956",
    "label": "biotin"}, "canonical_label": "biotin", "label_equal": true, "definition":
    ["An organic heterobicyclic compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
    having a valeric acid substituent attached to the tetrahydrothiophene ring. The
    parent of the class of biotins."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:58-85-5", "chemspider:149962", "drugbank:DB00121", "drugcentral:373", "foodb.food:FDB014510",
    "gmelin:1918703", "hmdb:HMDB0000030", "kegg.compound:C00120", "kegg.drug:D00029",
    "knapsack:C00000756", "lincs.smallmolecule:LSM-3994", "metacyc.compound:BIOTIN",
    "pdb-ccd:BTN", "pmc:PMC8089577", "pubmed:10064317", "pubmed:10215065", "pubmed:10577274",
    "pubmed:11435506", "pubmed:11481419", "pubmed:11800048", "pubmed:12055344", "pubmed:12070309",
    "pubmed:12603856", "pubmed:12803839", "pubmed:15012185", "pubmed:15202718", "pubmed:15272000",
    "pubmed:15690449", "pubmed:15863846", "pubmed:15899401", "pubmed:15992684", "pubmed:16011464",
    "pubmed:16195795", "pubmed:16419467", "pubmed:16676358", "pubmed:16677798", "pubmed:16704206",
    "pubmed:16769720", "pubmed:17297119", "pubmed:1814646", "pubmed:18202531", "pubmed:18452485",
    "pubmed:18509457", "pubmed:19212411", "pubmed:19319844", "pubmed:19727438", "pubmed:19928962",
    "pubmed:20967359", "pubmed:20974274", "pubmed:2100006", "pubmed:21248194", "pubmed:21356565",
    "pubmed:21373679", "pubmed:21596550", "pubmed:21871906", "pubmed:25515858", "pubmed:33346513",
    "pubmed:33461365", "pubmed:34077272", "pubmed:8333586", "pubmed:8750932", "pubmed:9022537",
    "pubmed:9038855", "pubmed:9094878", "pubmed:9164991", "pubmed:9176832", "pubmed:9371938",
    "pubmed:9416479", "reaxys:86838", "wikipedia.en:Biotin"], "generalized_empirical_formula":
    ["C10H16N2O3S"], "has_alternative_id": ["CHEBI:13905", "CHEBI:22882", "CHEBI:22884",
    "CHEBI:3108", "CHEBI:41236"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15956"],
    "inchi_key_string": ["YBJHBAHKTGYVGT-ZKWXMUAHSA-N"], "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"],
    "mass": ["244.316"], "monoisotopic_mass": ["244.08816"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]},
    "synonyms": ["(+)-cis-Hexahydro-2-oxo-1H-thieno[3,4]imidazole-4-valeric acid",
    "(3aS,4S,6aR)-Hexahydro-2-oxo-1H-thieno[3,4-d]imidazole-4-valeric acid", "5-(2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl)pentanoic
    acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic
    acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic
    acid", "BIOTIN", "Coenzyme R", "D-(+)-biotin", "D-Biotin", "Vitamin H", "biotin",
    "biotina", "biotine", "biotinum", "cis-(+)-Tetrahydro-2-oxothieno[3,4]imidazoline-4-valeric
    acid", "cis-Hexahydro-2-oxo-1H-thieno(3,4)imidazole-4-valeric acid", "cis-Tetrahydro-2-oxothieno(3,4-d)imidazoline-4-valeric
    acid", "vitamin B7"], "secondary": {"asserted": {"id": "CHEBI:15956", "label":
    "biotin"}, "exact_current_rows": [{"label": "Biotin", "match_type": "preferred_term",
    "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path":
    "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field":
    "ingredients[26]", "name": "Folic acid", "primary": {"id": "CHEBI:27470", "label":
    "folic acid"}, "canonical_label": "folic acid", "label_equal": true, "definition":
    ["An <em>N</em>-acyl-amino acid that is a form of the water-soluble vitamin B<small><sub>9</sub></small>.
    Its biologically active forms (tetrahydrofolate and others) are essential for
    nucleotide biosynthesis and homocysteine remethylation."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["agr:IND606960789", "cas:59-30-3", "chemspider:5815",
    "drugbank:DB00158", "drugcentral:1231", "foodb.food:FDB014504", "hmdb:HMDB0000121",
    "kegg.compound:C00504", "kegg.drug:D00070", "knapsack:C00001539", "lincs.smallmolecule:LSM-5355",
    "metacyc.compound:CPD-12826", "pdb-ccd:FOL", "pubmed:10138938", "pubmed:10897644",
    "pubmed:10958818", "pubmed:11261364", "pubmed:11451208", "pubmed:11959400", "pubmed:14387833",
    "pubmed:15321809", "pubmed:15523939", "pubmed:15754725", "pubmed:15797531", "pubmed:15797685",
    "pubmed:15831910", "pubmed:15990733", "pubmed:16093404", "pubmed:16277678", "pubmed:16380297",
    "pubmed:16871332", "pubmed:17784727", "pubmed:18788725", "pubmed:19121630", "pubmed:19335717",
    "pubmed:19355913", "pubmed:24650098", "pubmed:33624660", "pubmed:33965562", "pubmed:33968971",
    "pubmed:34207319", "pubmed:34219855", "pubmed:7738698", "pubmed:8235383", "pubmed:9040515",
    "pubmed:9420019", "pubmed:9565830", "pubmed:9683174", "pubmed:9781393", "pubmed:9808640",
    "pubmed:9808641", "reaxys:100781", "wikipedia.en:Folic_Acid"], "generalized_empirical_formula":
    ["C19H19N7O6"], "has_alternative_id": ["CHEBI:24075", "CHEBI:42610", "CHEBI:5140",
    "CHEBI:569217"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:27470"],
    "inchi_key_string": ["OVBPIULPVIDEAO-LBPRGKRZSA-N"], "inchi_string": ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"],
    "mass": ["441.404"], "monoisotopic_mass": ["441.13968"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]},
    "synonyms": ["(2S)-2-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzamido)pentanedioic
    acid", "Acfol", "Folate", "Folicet", "Folsaeure", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic
    acid", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic
    acid", "N-[(4-{[(2-amino-4-oxo-1,4-dihydropteridin-6-yl)methyl]amino}phenyl)carbonyl]-L-glutamic
    acid", "N-pteroyl-L-glutamic acid", "PGA", "PteGlu", "acide folique", "acido folico",
    "acidum folicum", "folic acid", "pteroyl-L-glutamic acid", "pteroyl-L-monoglutamic
    acid", "pteroylglutamic acid", "pteroylmonoglutamic acid", "vitamin B11", "vitamin
    B9", "vitamin Bc", "vitamin Be", "vitamin M"], "secondary": {"asserted": {"id":
    "CHEBI:27470", "label": "folic acid"}, "exact_current_rows": [{"label": "Folic
    acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[27]", "name": "Pyridoxine hydrochloride", "primary": {"id":
    "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "canonical_label": "pyridoxine
    hydrochloride", "label_equal": true, "definition": ["The hydrochloride salt of
    pyridoxine."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND500675659",
    "beilstein:3632435", "cas:58-56-0", "drugbank:DBSALT000151", "foodb.food:FDB000575",
    "gmelin:1067921", "kegg.drug:D02179", "pubmed:15098856", "pubmed:17416572", "pubmed:17891511",
    "pubmed:18243627", "pubmed:19481898", "pubmed:20645279", "pubmed:21781646", "pubmed:24421551",
    "pubmed:27468034", "pubmed:28095734", "pubmed:32460509", "pubmed:33209152", "pubmed:33936292",
    "pubmed:34140989"], "generalized_empirical_formula": ["C8H11NO3.HCl"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:30961"], "inchi_key_string": ["ZUFQODAHGAHPFQ-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C8H11NO3.ClH/c1-5-8(12)7(4-11)6(3-10)2-9-5;/h2,10-12H,3-4H2,1H3;1H"],
    "mass": ["205.641"], "monoisotopic_mass": ["205.05057"], "smiles_string": ["Cc1ncc(CO)c(CO)c1O.Cl"]},
    "synonyms": ["2-methyl-3-hydroxy-4,5-bis(hydroxymethyl)pyridine hydrochloride",
    "3-hydroxy-4,5-dimethylol-alpha-picoline hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol
    hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "5-hydroxy-6-methyl-3,4-pyridinedimethanol
    hydrochloride", "pyridoxol hydrochloride", "vitamin B6 hydrochloride"], "secondary":
    {"asserted": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "exact_current_rows":
    [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier":
    "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path":
    "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field":
    "ingredients[28]", "name": "Thiamine HCl", "primary": {"id": "CHEBI:49105", "label":
    "thiamine hydrochloride"}, "canonical_label": "thiamine hydrochloride", "label_equal":
    true, "definition": ["A hydrochloride obtained by combining thiamine chloride
    with one molar equivalent of hydrochloric acid."], "annotations": {"charge": [0.0],
    "database_cross_reference": ["agr:IND605711145", "agr:IND606057536", "beilstein:3642937",
    "beilstein:3851771", "cas:67-03-8", "chemspider:5967", "drugbank:DBSALT000205",
    "foodb.food:FDB008416", "gmelin:31154", "gmelin:691133", "kegg.drug:D02094", "pubmed:11548854",
    "pubmed:12224421", "pubmed:21212548", "pubmed:22305197", "pubmed:24399744", "pubmed:25977858",
    "pubmed:26616989", "pubmed:27163892", "pubmed:28763984", "pubmed:28784494", "pubmed:30131156",
    "pubmed:31270735", "pubmed:31664290", "pubmed:32009117", "pubmed:32562525", "pubmed:32824791",
    "reaxys:17124533"], "generalized_empirical_formula": ["C12H17N4OS.Cl.HCl"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:49105"], "inchi_key_string": ["DPJRMOMPQZCRJU-UHFFFAOYSA-M"],
    "inchi_string": ["InChI=1S/C12H17N4OS.2ClH/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H/q+1;;/p-1"],
    "mass": ["337.276"], "monoisotopic_mass": ["336.05784"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1.Cl.[Cl-]"]},
    "synonyms": ["3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    chloride hydrochloride", "3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    chloride hydrochloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    dichloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    dichloride", "thiamin dichloride", "thiamin hydrochloride", "thiamine HCl", "thiamine
    chloride hydrochloride", "thiamine dichloride", "thiamine(2+) dichloride", "thiaminium
    chloride hydrochloride", "vitamin B1 hydrochloride"], "secondary": {"asserted":
    {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "exact_current_rows":
    [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105",
    "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[29]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015",
    "label": "riboflavin"}, "canonical_label": "riboflavin", "label_equal": true,
    "definition": ["<small>D</small>-Ribitol in which the hydroxy group at position
    5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[<em>g</em>]pteridin-10(2<em>H</em>)-yl
    moiety. It is a nutritional factor found in milk, eggs, malted barley, liver,
    kidney, heart, and leafy vegetables, but the richest natural source is yeast.
    The free form occurs only in the retina of the eye, in whey, and in urine; its
    principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine
    dinucleotide."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:83-88-5", "chemspider:431981", "drugbank:DB00140", "drugcentral:2834", "foodb.food:FDB012160",
    "hmdb:HMDB0000244", "kegg.compound:C00255", "kegg.drug:D00050", "knapsack:C00001552",
    "lincs.smallmolecule:LSM-4084", "metacyc.compound:RIBOFLAVIN", "patent:US2807611",
    "patent:US2876169", "pdb-ccd:RBF", "pubmed:10566553", "pubmed:11399071", "pubmed:11606856",
    "pubmed:12083520", "pubmed:12354259", "pubmed:12927541", "pubmed:14963913", "pubmed:16273338",
    "pubmed:16460756", "pubmed:16658098", "pubmed:182198", "pubmed:18832377", "pubmed:19169240",
    "pubmed:19212411", "pubmed:19854891", "pubmed:22770225", "pubmed:2369885", "pubmed:23818044",
    "pubmed:24643482", "pubmed:24816110", "pubmed:25108762", "pubmed:25468971", "pubmed:25887755",
    "pubmed:2631092", "pubmed:29937405", "pubmed:3142982", "pubmed:33154451", "pubmed:33304888",
    "pubmed:33886098", "pubmed:33892358", "pubmed:34156642", "pubmed:3592624", "pubmed:3878498",
    "pubmed:4019261", "pubmed:6475825", "pubmed:6546833", "pubmed:6650303", "pubmed:7101408",
    "pubmed:7883462", "pubmed:8487103", "pubmed:8604671", "pubmed:8678471", "pubmed:8976642",
    "pubmed:9184778", "pubmed:9808225", "pubmed:9874201", "reaxys:97831", "wikipedia.en:Riboflavin"],
    "generalized_empirical_formula": ["C17H20N4O6"], "has_alternative_id": ["CHEBI:15044",
    "CHEBI:27299", "CHEBI:45214", "CHEBI:529204", "CHEBI:8843"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:17015"], "inchi_key_string": ["AUNGANRZJHBGPY-SCRDCRAPSA-N"],
    "inchi_string": ["InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23)14(25)12(24)6-22)15-13(18-9)16(26)20-17(27)19-15/h3-4,11-12,14,22-25H,5-6H2,1-2H3,(H,20,26,27)/t11-,12+,14-/m0/s1"],
    "mass": ["376.369"], "monoisotopic_mass": ["376.13828"], "smiles_string": ["Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)CO)c2cc1C"]},
    "synonyms": ["1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol",
    "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol",
    "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol",
    "5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol",
    "6,7-dimethyl-9-D-ribitylisoalloxazine", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione",
    "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine", "7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione",
    "7,8-dimethyl-10-ribitylisoalloxazine", "Aqua-Flave", "Beflavin", "Beflavine",
    "Bisulase", "Dermadram", "E101", "Fiboflavin", "Flavaxin", "Flavin Bb", "Flaxain",
    "Hyflavin", "Vitamin B2", "lactoflavin", "riboflavin (vit B2)", "riboflavin",
    "riboflavina", "riboflavine", "riboflavinum", "vitamin B2", "vitamin G", "vitasan
    B2"], "secondary": {"asserted": {"id": "CHEBI:17015", "label": "riboflavin"},
    "exact_current_rows": [{"label": "Riboflavin", "match_type": "preferred_term",
    "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path":
    "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml", "field":
    "ingredients[30]", "name": "Nicotinic acid", "primary": {"id": "CHEBI:15940",
    "label": "nicotinic acid"}, "canonical_label": "nicotinic acid", "label_equal":
    true, "definition": ["A pyridinemonocarboxylic acid that is pyridine in which
    the hydrogen at position 3 is replaced by a carboxy group."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["agr:IND607088605", "cas:59-67-6", "chemspider:913",
    "drugbank:DB00627", "drugcentral:2835", "foodb.food:FDB001014", "gmelin:3340",
    "hmdb:HMDB0001488", "kegg.compound:C00253", "kegg.drug:D00049", "knapsack:C00000208",
    "lincs.smallmolecule:LSM-4676", "metacyc.compound:NIACINE", "pdb-ccd:NIO", "pubmed:10540864",
    "pubmed:113218", "pubmed:12563315", "pubmed:12789870", "pubmed:135660", "pubmed:14550884",
    "pubmed:15037193", "pubmed:15183629", "pubmed:15205990", "pubmed:15311728", "pubmed:15627518",
    "pubmed:15651982", "pubmed:16018787", "pubmed:16172771", "pubmed:16322787", "pubmed:16400392",
    "pubmed:16449845", "pubmed:16767301", "pubmed:16877271", "pubmed:16945375", "pubmed:18037924",
    "pubmed:182198", "pubmed:186078", "pubmed:18993152", "pubmed:18996527", "pubmed:19369827",
    "pubmed:19592242", "pubmed:19678716", "pubmed:19779335", "pubmed:20979384", "pubmed:21632263",
    "pubmed:22116693", "pubmed:22155410", "pubmed:22229411", "pubmed:22366213", "pubmed:22458880",
    "pubmed:22770225", "pubmed:24029555", "pubmed:24568240", "pubmed:24675661", "pubmed:24848081",
    "pubmed:24975217", "pubmed:25040591", "pubmed:25241762", "pubmed:25429652", "pubmed:32954525",
    "pubmed:33273654", "pubmed:33932650", "pubmed:34066686", "pubmed:34085526", "pubmed:34117670",
    "pubmed:4033386", "pubmed:4259917", "pubmed:582105", "pubmed:699281", "pubmed:7217784",
    "pubmed:7581845", "pubmed:8306147", "pubmed:8423912", "pubmed:8679452", "pubmed:9107536",
    "reaxys:109591", "wikipedia.en:Niacin"], "generalized_empirical_formula": ["C6H5NO2"],
    "has_alternative_id": ["CHEBI:25538", "CHEBI:44319", "CHEBI:7559"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:15940"], "inchi_key_string": ["PVNIIMVLHYAWGP-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"], "mass":
    ["123.111"], "monoisotopic_mass": ["123.03203"], "smiles_string": ["O=C(O)c1cccnc1"]},
    "synonyms": ["3-Pyridylcarboxylic acid", "3-carboxylpyridine", "3-carboxypyridine",
    "3-pyridinecarboxylic acid", "NICOTINIC ACID", "NICOTINIC ACID", "Niacin", "Niacor",
    "Niaspan", "Nicotinic acid", "Nicotinic acid", "Nicotinsaure", "Nikotinsaeure",
    "P.P. factor", "PP factor", "acide nicotinique", "acido nicotinico", "acidum nicotinicum",
    "anti-pellagra vitamin", "beta-pyridinecarboxylic acid", "m-pyridinecarboxylic
    acid", "nicotinic acid", "nicotinic acid", "pellagra preventive factor", "pyridine-3-carboxylic
    acid", "pyridine-3-carboxylic acid", "pyridine-beta-carboxylic acid", "pyridine-carboxylique-3",
    "vitamin B3"], "secondary": {"asserted": {"id": "CHEBI:15940", "label": "nicotinic
    acid"}, "exact_current_rows": [{"label": "Nicotinic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id":
    "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[31]", "name": "Calcium D-(+)-pantothenate", "primary": {"id":
    "CHEBI:31345", "label": "Calcium pantothenate"}, "canonical_label": "Calcium pantothenate",
    "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:137-08-6", "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278",
    "pubmed:20553011", "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula":
    ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"],
    "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"],
    "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]},
    "synonyms": ["Calcium pantotenate", "Calcium pantothenate", "Calcium pantothenate,
    d-", "Calpan", "D-ca pantothenate", "D-calcium pantothenate", "NSC-36292", "Pantholin",
    "Pantothenic acid (as calcium)", "Pantothenic acid calcium salt", "Vitamin b5,
    calcium salt", "pantotenato de calcio", "pantothenate de calcium"]}, {"layer":
    "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[32]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843",
    "label": "vitamin B12"}, "canonical_label": "vitamin B12", "label_equal": true,
    "definition": ["Any member of a group of cobalamin vitamers that exhibit biological
    activity against vitamin B<small><sub>12</sub></small> deficiency. Vitamin B<small><sub>12</sub></small>
    deficiency is associated with low red blood cell count and anemia. The vitamers
    are found in foods such as cereals, meat, fish, and poultry. The vitamers include
    adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin
    and methylcobabalamin (also includes their ionized, salt and phosphate derivatives)."],
    "annotations": {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:176843"]},
    "synonyms": ["vitamin B-12", "vitamin B12 vitamer", "vitamin B12 vitamers", "vitamin
    B12", "vitamins B12"], "secondary": {"asserted": {"id": "CHEBI:176843", "label":
    "vitamin B12"}, "exact_current_rows": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}},
    {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[33]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753",
    "label": "4-aminobenzoic acid"}, "canonical_label": "4-aminobenzoic acid", "label_equal":
    true, "definition": ["An aminobenzoic acid in which the amino group is <em>para</em>
    to the carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:150-13-0", "drugbank:DB02362", "drugcentral:2049", "ecmdb:ECMDB01392", "gmelin:50150",
    "hmdb:HMDB0001392", "kegg.compound:C00568", "kegg.drug:D02456", "knapsack:C00001401",
    "pdb-ccd:PAB", "pubmed:12039592", "pubmed:14745019", "pubmed:15115392", "pubmed:1527790",
    "pubmed:16290145", "pubmed:17149871", "pubmed:17743450", "pubmed:17800214", "pubmed:19469519",
    "pubmed:22767283", "pubmed:22994574", "pubmed:23063996", "pubmed:23084339", "pubmed:23144588",
    "pubmed:23471007", "pubmed:3599019", "pubmed:3820215", "pubmed:3950915", "pubmed:8411009",
    "pubmed:9406595", "reaxys:471605", "wikipedia.en:4-Aminobenzoic_acid", "ymdb:YMDB00493"],
    "generalized_empirical_formula": ["C7H7NO2"], "has_alternative_id": ["CHEBI:113372",
    "CHEBI:1783", "CHEBI:20315", "CHEBI:44778"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:30753"], "inchi_key_string": ["ALYNCZNDIQEVRV-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"], "mass": ["137.138"],
    "monoisotopic_mass": ["137.04768"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]}, "synonyms":
    ["1-Amino-4-carboxybenzene", "4-AMINOBENZOIC ACID", "4-AMINOBENZOIC ACID", "4-Amino-benzoic
    acid", "4-Aminobenzoesaeure", "4-Aminobenzoic acid", "4-Aminobenzoic acid", "4-Carboxyaniline",
    "4-Carboxyphenylamine", "4-aminobenzoic acid", "4-aminobenzoic acid", "ABEE",
    "PABA", "gamma-Aminobenzoic acid", "gamma-aminobenzoic acid", "p-Aminobenzoesaeure",
    "p-aminobenzoic acid", "p-carboxyaniline", "p-carboxyphenylamine", "para-aminobenzoic
    acid"], "secondary": {"asserted": {"id": "CHEBI:30753", "label": "4-aminobenzoic
    acid"}, "exact_current_rows": [{"label": "p-Aminobenzoic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic
    acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field": "ingredients[34]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id":
    "CHEBI:16494", "label": "lipoic acid"}, "canonical_label": "lipoic acid", "label_equal":
    true, "definition": ["A heterocyclic thia fatty acid comprising pentanoic acid
    with a 1,2-dithiolan-3-yl group at the 5-position."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["beilstein:122410", "cas:62-46-4", "drugbank:DB00166",
    "drugcentral:4732", "ecmdb:ECMDB01451", "gmelin:720915", "kegg.compound:C00725",
    "kegg.drug:D00086", "pubmed:15328413", "pubmed:7519986", "pubmed:7548757", "reaxys:81853",
    "wikipedia.en:Lipoic_acid", "ymdb:YMDB00334"], "generalized_empirical_formula":
    ["C8H14O2S2"], "has_alternative_id": ["CHEBI:146958", "CHEBI:25058", "CHEBI:6492"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16494"], "inchi_key_string":
    ["AGBQKNBQESQNJD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H14O2S2/c9-8(10)4-2-1-3-7-5-6-11-12-7/h7H,1-6H2,(H,9,10)"],
    "mass": ["206.332"], "monoisotopic_mass": ["206.04352"], "smiles_string": ["O=C(O)CCCCC1CCSS1"]},
    "synonyms": ["1,2-dithiolane-3-pentanoic acid", "1,2-dithiolane-3-valeric acid",
    "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)pentanoic acid",
    "5-(1,2-dithiolan-3-yl)valeric acid", "5-(dithiolan-3-yl)valeric acid", "5-[3-(1,2-dithiolanyl)]pentanoic
    acid", "6,8-thioctic acid", "6,8-thiotic acid", "6-thioctic acid", "6-thiotic
    acid", "Acetate-replacing factor", "Biletan", "Lipoic acid", "Thioctansaeure",
    "Thioctic acid", "Thioctsaeure", "Thioktsaeure", "alpha-Lipoic acid", "alpha-Liponsaeure",
    "alpha-lipoic acid", "liponic acid"], "secondary": {"asserted": {"id": "CHEBI:16494",
    "label": "lipoic acid"}, "exact_current_rows": [{"label": "(DL)-alpha-Lipoic acid",
    "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term":
    "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}], "legacy": []}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _parse_api_solutions; _normalize_unit
  accessed_at: '2026-10-21T10:05:42Z'
  support: context_only
  summary: Current importer selects main ingredients, preserves solution_id and percentage-stock
    rows and maps ml as ML_PER_L. This does not validate old flattened values or prove
    their precise historical cause.
- evidence_id: resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: merge_composition; _add_enrichment_metadata
  accessed_at: '2026-10-21T10:05:42Z'
  support: context_only
  summary: Current resolver copies ingredients/solutions and selected metadata but
    not preparation in this method, retaining an existing scalar pH. It writes timezone-naive
    local timestamps. The present code is contextual, not a replay of the historical
    import.
- evidence_id: cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-21T10:05:42Z'
  support: context_only
  summary: Current cleanup no longer sums unequal duplicates. Actual owner notes retain
    earlier NaCl, magnesium, calcium and iron sums across stock stages, which require
    source-specific curation.
- evidence_id: history
  kind: record_content
  reference: data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
  locator: Every target and maintained owner history and ingredient curation timestamp
  accessed_at: '2026-10-21T10:05:42Z'
  support: refutes
  summary: '[{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[0].timestamp", "value": "2026-01-27T01:15:02.fZ",
    "valid_ISO_datetime": false, "timezone_aware": false}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:18.940996",
    "valid_ISO_datetime": true, "timezone_aware": false}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[2].timestamp", "value": "2026-02-06T05:10:54.113555Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[3].timestamp", "value": "2026-03-13T03:09:42.427704Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[4].timestamp", "value": "2026-03-13T06:19:25.750970Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[5].timestamp", "value": "2026-03-17T06:30:54.000000Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[6].timestamp", "value": "2026-03-17T19:45:40.702498+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[7].timestamp", "value": "2026-06-05T07:40:21.357759+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[8].timestamp", "value": "2026-06-10T07:46:44.288307+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[9].timestamp", "value": "2026-08-06T03:04:43.901578+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[10].timestamp", "value": "2026-08-06T03:04:43.901623+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[0].timestamp", "value": "2026-01-27T01:15:02.fZ",
    "valid_ISO_datetime": false, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:18.940996",
    "valid_ISO_datetime": true, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[2].timestamp", "value": "2026-02-06T05:10:54.113555Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[3].timestamp", "value": "2026-03-13T03:09:42.427704Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[4].timestamp", "value": "2026-03-13T06:19:25.750970Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[5].timestamp", "value": "2026-03-17T06:30:54.000000Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[6].timestamp", "value": "2026-03-17T19:45:40.702498+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[7].timestamp", "value": "2026-06-05T07:40:21.357759+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[8].timestamp", "value": "2026-06-10T07:46:44.288307+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "curation_history[0].timestamp", "value": "2026-01-26T17:53:10.381491Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "curation_history[1].timestamp", "value": "2026-02-06T05:10:38.188874Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "curation_history[2].timestamp", "value": "2026-03-13T03:09:18.337390Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "curation_history[3].timestamp", "value": "2026-03-13T06:19:01.575354Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "curation_history[4].timestamp", "value": "2026-03-17T06:30:26.000000Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "curation_history[5].timestamp", "value": "2026-03-17T19:45:13.309524+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "curation_history[6].timestamp", "value": "2026-05-20T06:01:07.039986+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "curation_history[7].timestamp", "value": "2026-06-05T07:40:46.684516+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "curation_history[8].timestamp", "value": "2026-06-10T07:46:52.368320+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}]'
- evidence_id: merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger; merge_formulation_evidence; maintained formulation-aware
    merge context
  accessed_at: '2026-10-21T10:05:42Z'
  support: context_only
  summary: The target is a generated merge with the exact normalized contributors
    pinned by inspection. The old ingredient-set fingerprint is not concentration,
    preparation or source equivalence. Current formulation-aware merging preserves
    only compatible assertions. No merge was run; verify owners and preview current
    grouping before separately authorized regeneration.
- evidence_id: exporter
  kind: record_content
  reference: src/culturemech/export/kgx_export.py
  locator: medium_to_ingredient_edge; medium_to_solution_edge; _resolved_ingredient_id;
    _quantity
  accessed_at: '2026-10-21T10:05:42Z'
  support: context_only
  summary: Current export consumes structured ingredient/solution identities and quantities,
    resolving against the pinned MIM index before fallback. It does not independently
    recover missing stock stages, source qualifiers or final volume. No export or
    resulting edge count is claimed.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:004192
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Stable source identity and exact contributors
  outcome: supported
  summary: The target CM004192 derives from the KOMODO 165 owner and DSMZ owner CM001142,
    both explicitly named in merge metadata. The exact KOMODO accession link and current
    DSMZ title agree. The owners have the same 35 ingredient values but differ in
    preparation, pH representation and notes; the old ingredient fingerprint does
    not erase those differences. All inspected input hashes match.
  target_ids:
  - CultureMech:004192
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz165
  - mediadive165api
  - komodoMediaList
- assessment_id: relationships
  area: scope
  topic: Source contributors and bounded carbon-source alternatives
  outcome: concern
  summary: There is no explicit parent_media or variant_children relationship in these
    three records. The two source contributors are identified by the actual merge
    event. The exact primary treats cellulose as an alternative to cellobiose; the
    target/KOMODO owner encode only Optional ingredient beside a simultaneous cellobiose
    row. That does not document a selected branch or preserve the mutual substitution
    stated in the DSMZ owner preparation.
  target_ids:
  - CultureMech:004192
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz165
  - mediadive165api
- assessment_id: grounding
  area: grounding
  topic: Primary labels/forms and pinned secondary correspondence
  outcome: supported
  summary: 'Layer-specific counts are {"target": {"ingredient_instances": 35, "primary_CHEBI_instances":
    35, "secondary_current_asserted_instances": 33, "secondary_current_verified_instances":
    33, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 100.0, "secondary_verified_percent":
    94.29}, "owner-0": {"ingredient_instances": 35, "primary_CHEBI_instances": 35,
    "secondary_current_asserted_instances": 33, "secondary_current_verified_instances":
    33, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 100.0, "secondary_verified_percent":
    94.29}, "owner-1": {"ingredient_instances": 35, "primary_CHEBI_instances": 35,
    "secondary_current_asserted_instances": 33, "secondary_current_verified_instances":
    33, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 100.0, "secondary_verified_percent":
    94.29}}. Percentages are 0–100 linkage coverage over direct ingredient instances,
    not scientific accuracy. The 0 legacy link instances across reviewed layers are
    unverified by the current CHEBI-keyed snapshot; absence here does not prove historical
    invalidity. Current secondary keys without a live preferred-term row are []. No
    secondary linked-set percentage is invented for an empty set.'
  target_ids:
  - CultureMech:004192
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - mim
  - chebi8806
  - chebi29377
  - chebi17057
  - chebi18246
  - chebi91248
  - chebi76209
  - chebi131527
  - chebi63036
  - chebi62946
  - chebi26710
  - chebi31795
  - chebi86158
  - chebi44557
  - chebi86364
  - chebi75836
  - chebi91244
  - chebi32312
  - chebi31440
  - chebi86465
  - chebi33118
  - chebi75213
  - chebi34887
  - chebi131361
  - chebi63939
  - chebi26836
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
  details: '{"label_drift": [], "legacy": [], "missing_current_secondary": []}'
- assessment_id: forms
  area: grounding
  topic: Supplied hydrates, redox indicator and carbon-source materials
  outcome: concern
  summary: All 35 asserted primary CHEBI instances resolve with canonical labels,
    and all 33 asserted current secondary keys have live pinned-index rows. Nevertheless
    NiCl2 x 6 H2O maps to CHEBI:34887 with no waters, and sodium resazurin maps to
    neutral CHEBI:8806 with no sodium. D-(+)-calcium pantothenate agrees with the
    D-specific CHEBI:31345 structure; generic lipoic acid has no selected stereochemistry
    that contradicts source DL. The source cysteine hydrochloride monohydrate is supported
    by CHEBI:91248 definition. Cellulose maps to the beta-D-glucan class, which does
    not specify the grade, purity or paper/cotton alternatives. Retain those source
    qualifiers separately.
  target_ids:
  - CultureMech:004192
  evidence_ids:
  - dsmz165
  - mediadive165api
  - chebi8806
  - chebi29377
  - chebi17057
  - chebi18246
  - chebi91248
  - chebi76209
  - chebi131527
  - chebi63036
  - chebi62946
  - chebi26710
  - chebi31795
  - chebi86158
  - chebi44557
  - chebi86364
  - chebi75836
  - chebi91244
  - chebi32312
  - chebi31440
  - chebi86465
  - chebi33118
  - chebi75213
  - chebi34887
  - chebi131361
  - chebi63939
  - chebi26836
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
  area: consistency
  topic: Gas atmosphere, sterilization, acid-stock freshness and pH
  outcome: concern
  summary: 'DSMZ owner preserves the three source paragraphs: main 80% N2/20% CO2
    anoxic preparation, distinct sterile-stock additions with 100% N2 versus mixed
    gas, filtration of cellobiose/vitamins, final pH 7.2–7.4 and the cellulose substitution;
    mineral-stock KOH pH adjustment; and freshly prepared ferrous stock. Target and
    KOMODO owner omit all three and retain Aerobic: Yes with scalar pH 7.2. Scalar
    7.2 is a permitted endpoint, but it loses the explicit complete-medium range.
    The primary does not state autoclave duration/temperature, storage or shelf life;
    none is inferred.'
  target_ids:
  - CultureMech:004192
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz165
  - mediadive165api
  - komodoMediaList
  - resolver
- assessment_id: classification
  area: scope
  topic: Catalog classification and selected formulation scope
  outcome: concern
  summary: MediaDive labels this medium complex, while the KOMODO row has is_complex=false.
    The maintained records assert COMPLEX/UNDEFINED without recording a selected cellobiose/cellulose
    material branch. The explicit source ingredients and alternative grades should
    guide reassessment; neither catalog flag alone proves composition type for every
    branch. LIQUID is consistent with the absence of a gelling-agent recipe; suspended
    cellulose does not by itself make an agar solid medium. Bacterial filing and generic
    cultivation do not establish organism growth.
  target_ids:
  - CultureMech:004192
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - komodoMediaList
  - dsmz165
  - mediadive165api
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp interpretation
  outcome: concern
  summary: 29 exact timestamp instances were examined; 4 lack valid syntax or explicit
    timezone. No local timestamp was assumed UTC or rewritten. Process and confidence
    annotations are not independent scientific evidence.
  target_ids:
  - CultureMech:004192
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - history
  details: '[{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[0].timestamp", "value": "2026-01-27T01:15:02.fZ",
    "valid_ISO_datetime": false, "timezone_aware": false}, {"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:18.940996",
    "valid_ISO_datetime": true, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[0].timestamp", "value": "2026-01-27T01:15:02.fZ",
    "valid_ISO_datetime": false, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:18.940996",
    "valid_ISO_datetime": true, "timezone_aware": false}]'
- assessment_id: quantities
  area: quantity
  topic: Every stored amount, stock dose and source-stage dependency
  outcome: concern
  summary: All 35 ingredient amounts in the target and each owner are traced to all
    49 literal provider recipe rows, two unquantified preparation additions and five
    quantitative preparation contexts. The inventory distinguishes direct amounts,
    five stock doses, stock strengths, solvents, optional substitution and source
    normality, with arithmetic outside exact quotations. Conditional stock contributions
    do not establish measured final volume.
  target_ids:
  - CultureMech:004192
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - quantity-1
  - quantity-2
  - quantity-3
  - quantity-4
  - quantity-5
  - quantity-6
  - quantity-7
  - quantity-8
  - quantity-9
  - quantity-10
  - quantity-11
  - quantity-12
  - quantity-13
  - quantity-14
  - quantity-15
  - quantity-16
  - quantity-17
  - quantity-18
  - quantity-19
  - quantity-20
  - quantity-21
  - quantity-22
  - quantity-23
  - quantity-24
  - quantity-25
  - quantity-26
  - quantity-27
  - quantity-28
  - quantity-29
  - quantity-30
  - quantity-31
  - quantity-32
  - quantity-33
  - quantity-34
  - quantity-35
  - quantity-36
  - quantity-37
  - quantity-38
  - quantity-39
  - quantity-40
  - quantity-41
  - quantity-42
  - quantity-43
  - quantity-44
  - quantity-45
  - quantity-46
  - quantity-47
  - quantity-48
  - quantity-49
  - quantity-50
  - quantity-51
  - quantity-52
  - quantity-53
  - quantity-54
  - quantity-55
  - quantity-56
  details: '[{"field_path": "source solution 283 recipe[0] (not represented)", "name":
    "Mineral solution 1", "current": null, "decision": "add", "source_key": "mediadive165api",
    "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\":
    \"Mineral solution 1\",\n                        \"solution_id\": 284,\n                        \"amount\":
    75,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[0].recipe[0]",
    "preparation_stage": "Main sol. 165 (solution 283, declared 1001 mL)", "decision_rationale":
    "The main recipe explicitly adds 75 ml of stock 284. Restore this dose and the
    separate stock definition; the stored flat ingredient strengths do not encode
    its dilution.", "evidence_id": "quantity-1", "affected_local_fields": [], "source_amount":
    75, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml":
    1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "source solution
    283 recipe[1] (not represented)", "name": "Mineral solution 2", "current": null,
    "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"solution\": \"Mineral solution 2\",\n                        \"solution_id\":
    285,\n                        \"amount\": 75,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[1]", "preparation_stage": "Main sol. 165 (solution
    283, declared 1001 mL)", "decision_rationale": "The main recipe explicitly adds
    75 ml of stock 285. Restore this dose and the separate stock definition; the stored
    flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-2",
    "affected_local_fields": [], "source_amount": 75, "source_unit": "ml", "source_attribute":
    null, "provider_g_l": null, "provider_stage_volume_ml": 1001, "primary_source_evidence_id":
    "dsmz165"}, {"field_path": "source solution 283 recipe[2] (not represented)",
    "name": "Modified Wolin''s mineral solution", "current": null, "decision": "add",
    "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Modified Wolin''s mineral solution\",\n                        \"solution_id\":
    241,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[2]", "preparation_stage": "Main sol. 165 (solution
    283, declared 1001 mL)", "decision_rationale": "The main recipe explicitly adds
    10 ml of stock 241. Restore this dose and the separate stock definition; the stored
    flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-3",
    "affected_local_fields": [], "source_amount": 10, "source_unit": "ml", "source_attribute":
    null, "provider_g_l": null, "provider_stage_volume_ml": 1001, "primary_source_evidence_id":
    "dsmz165"}, {"field_path": "source solution 283 recipe[3] (not represented)",
    "name": "FeSO4 x 7 H2O solution (0.1% w/v)", "current": null, "decision": "add",
    "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"solution\": \"FeSO4 x 7 H2O solution (0.1% w/v)\",\n                        \"solution_id\":
    5861,\n                        \"amount\": 20,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[3]", "preparation_stage": "Main sol. 165 (solution
    283, declared 1001 mL)", "decision_rationale": "The main recipe explicitly adds
    20 ml of stock 5861. Restore this dose and the separate stock definition; the
    stored flat ingredient strengths do not encode its dilution.", "evidence_id":
    "quantity-4", "affected_local_fields": [], "source_amount": 20, "source_unit":
    "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml":
    1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[0].concentration",
    "name": "Sodium resazurin", "current": {"value": "0.0004995", "unit": "G_PER_L"},
    "decision": "evidence_only", "source_key": "mediadive165api", "source_quote":
    "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.0004995,\n                        \"mmol_l\":
    0.0019887,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[4]", "preparation_stage": "Main sol. 165 (solution
    283, declared 1001 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1001 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-5", "arithmetic_separate_from_quote":
    "0.1% w/v means 0.1 g per 100 mL; 0.5 mL contains 0.0005 g. Dividing by provider-declared
    1001/1000 L gives 0.0004995004995004995004995004995 g/L; reported g_l is 0.0004995.
    Preserve this source stock dose separately.", "affected_local_fields": [{"path":
    "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path":
    "ingredients[0].concentration", "name": "Sodium resazurin", "current": {"value":
    "0.0004995", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "name": "Sodium resazurin", "current":
    {"value": "0.0004995", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[0].concentration", "name": "Sodium resazurin", "current":
    {"value": "0.0004995", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit":
    "ml", "source_attribute": "0.1% w/v", "provider_g_l": 0.0004995, "provider_stage_volume_ml":
    1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[1].concentration",
    "name": "Na2CO3", "current": {"value": "1.4985", "unit": "G_PER_L"}, "decision":
    "evidence_only", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.4985,\n                        \"mmol_l\":
    14.1384,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[5]", "preparation_stage": "Main sol. 165 (solution
    283, declared 1001 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1001 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-6", "arithmetic_separate_from_quote":
    "Original 1.5 g × 1 g/g ÷ (1001 mL / 1000 mL per L) = 1.498501498501498501498501499
    g/L on the provider-declared stage volume; reported g_l is 1.4985. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "name": "Na2CO3", "current": {"value":
    "1.4985", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "name": "Na2CO3", "current": {"value":
    "1.4985", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[1].concentration", "name": "Na2CO3", "current": {"value":
    "1.4985", "unit": "G_PER_L"}}], "source_amount": 1.5, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 1.4985, "provider_stage_volume_ml": 1001, "primary_source_evidence_id":
    "dsmz165"}, {"field_path": "ingredients[2].concentration", "name": "Cellobiose",
    "current": {"value": "2.997", "unit": "G_PER_L"}, "decision": "evidence_only",
    "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Cellobiose\",\n                        \"compound_id\":
    214,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.997,\n                        \"mmol_l\":
    8.75549,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[6]", "preparation_stage": "Main sol. 165 (solution
    283, declared 1001 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1001 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-7", "arithmetic_separate_from_quote":
    "Original 3 g × 1 g/g ÷ (1001 mL / 1000 mL per L) = 2.997002997002997002997002997
    g/L on the provider-declared stage volume; reported g_l is 2.997. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "name": "Cellobiose", "current":
    {"value": "2.997", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "name": "Cellobiose", "current":
    {"value": "2.997", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[2].concentration", "name": "Cellobiose", "current":
    {"value": "2.997", "unit": "G_PER_L"}}], "source_amount": 3, "source_unit": "g",
    "source_attribute": null, "provider_g_l": 2.997, "provider_stage_volume_ml": 1001,
    "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[3].concentration",
    "name": "Cellulose", "current": {"value": "2.997", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Cellulose\",\n                        \"compound_id\":
    400,\n                        \"attribute\": \"MN300\",\n                        \"amount\":
    3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    2.997,\n                        \"optional\": 1\n                    }", "source_locator":
    "$.data.solutions[0].recipe[7]", "preparation_stage": "Main sol. 165 (solution
    283, declared 1001 mL)", "decision_rationale": "The source gives cellulose 3 g
    as an alternative to cellobiose, not an extra carbon source added to the same
    selected recipe. Retain the source amount and grade/alternative condition; provider
    g_l 2.997 follows its declared 1001 mL basis.", "evidence_id": "quantity-8", "arithmetic_separate_from_quote":
    "3 g / 1.001 L = 2.997002997... g/L on the provider basis only; this calculation
    does not establish the selected carbon-source branch.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path":
    "ingredients[3].concentration", "name": "Cellulose", "current": {"value": "2.997",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "name": "Cellulose", "current":
    {"value": "2.997", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[3].concentration", "name": "Cellulose", "current":
    {"value": "2.997", "unit": "G_PER_L"}}], "source_amount": 3, "source_unit": "g",
    "source_attribute": "MN300", "provider_g_l": 2.997, "provider_stage_volume_ml":
    1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "source solution
    283 recipe[8] (not represented)", "name": "Wolin''s vitamin solution (10x)", "current":
    null, "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[8]", "preparation_stage": "Main sol. 165 (solution
    283, declared 1001 mL)", "decision_rationale": "The main recipe explicitly adds
    1 ml of stock 5980. Restore this dose and the separate stock definition; the stored
    flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-9",
    "affected_local_fields": [], "source_amount": 1, "source_unit": "ml", "source_attribute":
    null, "provider_g_l": null, "provider_stage_volume_ml": 1001, "primary_source_evidence_id":
    "dsmz165"}, {"field_path": "ingredients[4].concentration", "name": "L-Cysteine
    HCl x H2O", "current": {"value": "0.24975", "unit": "G_PER_L"}, "decision": "evidence_only",
    "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\":
    770,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.24975,\n                        \"mmol_l\":
    1.42198,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[9]", "preparation_stage": "Main sol. 165 (solution
    283, declared 1001 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1001 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-10", "arithmetic_separate_from_quote":
    "Original 0.25 g × 1 g/g ÷ (1001 mL / 1000 mL per L) = 0.2497502497502497502497502498
    g/L on the provider-declared stage volume; reported g_l is 0.24975. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "name": "L-Cysteine HCl x H2O",
    "current": {"value": "0.24975", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "name": "L-Cysteine HCl x H2O",
    "current": {"value": "0.24975", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[4].concentration", "name": "L-Cysteine HCl x H2O",
    "current": {"value": "0.24975", "unit": "G_PER_L"}}], "source_amount": 0.25, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.24975, "provider_stage_volume_ml":
    1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[5].concentration",
    "name": "Na2S x 9 H2O", "current": {"value": "0.24975", "unit": "G_PER_L"}, "decision":
    "evidence_only", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.24975,\n                        \"mmol_l\":
    1.03984,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[10]", "preparation_stage": "Main sol. 165 (solution
    283, declared 1001 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1001 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-11", "arithmetic_separate_from_quote":
    "Original 0.25 g × 1 g/g ÷ (1001 mL / 1000 mL per L) = 0.2497502497502497502497502498
    g/L on the provider-declared stage volume; reported g_l is 0.24975. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "name": "Na2S x 9 H2O", "current":
    {"value": "0.24975", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "name": "Na2S x 9 H2O", "current":
    {"value": "0.24975", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[5].concentration", "name": "Na2S x 9 H2O", "current":
    {"value": "0.24975", "unit": "G_PER_L"}}], "source_amount": 0.25, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.24975, "provider_stage_volume_ml":
    1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "source solution
    283 recipe[11] (not represented)", "name": "Distilled water", "current": null,
    "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 820,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[11]", "preparation_stage": "Main sol. 165 (solution
    283, declared 1001 mL)", "decision_rationale": "Preserve the source solvent quantity
    820 ml in its own stage. The provider declares this solution volume as 1001 mL;
    water addition is not independent proof of measured final volume.", "evidence_id":
    "quantity-12", "affected_local_fields": [], "source_amount": 820, "source_unit":
    "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml":
    1001, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[6].concentration",
    "name": "K2HPO4", "current": {"value": "3.9", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 3.9,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.9,\n                        \"mmol_l\":
    22.3911,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[0]", "preparation_stage": "Mineral solution 1 (solution
    284, declared 1000 mL)", "decision_rationale": "This is a stock composition or
    a direct contribution currently combined with a stock value. Preserve original
    batch amount, exact source form and stock stage; do not use this stock strength
    as a direct final-medium concentration.", "evidence_id": "quantity-13", "arithmetic_separate_from_quote":
    "Original 3.9 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 3.9 g/L on the provider-declared
    stage volume; reported g_l is 3.9. This is not a receiving-medium dilution. Conditional
    receiving contribution: 3.9 g/L stock × 0.075 L / 1.001 L = 0.2922077922077922077922077922
    g/L. The source stock remains a separate preparation; do not encode both expansion
    and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "name": "K2HPO4", "current": {"value":
    "3.9", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "name": "K2HPO4", "current": {"value":
    "3.9", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[6].concentration", "name": "K2HPO4", "current": {"value":
    "3.9", "unit": "G_PER_L"}}], "source_amount": 3.9, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 3.9, "provider_stage_volume_ml": 1000, "primary_source_evidence_id":
    "dsmz165"}, {"field_path": "source solution 284 recipe[1] (not represented)",
    "name": "Distilled water", "current": null, "decision": "add", "source_key": "mediadive165api",
    "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[1].recipe[1]",
    "preparation_stage": "Mineral solution 1 (solution 284, declared 1000 mL)", "decision_rationale":
    "Preserve the source solvent quantity 1000 ml in its own stage. The provider declares
    this solution volume as 1000 mL; water addition is not independent proof of measured
    final volume.", "evidence_id": "quantity-14", "affected_local_fields": [], "source_amount":
    1000, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[7].concentration",
    "name": "KH2PO4", "current": {"value": "2.4", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 2.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.4,\n                        \"mmol_l\":
    17.636,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[0]", "preparation_stage": "Mineral solution 2 (solution
    285, declared 1000 mL)", "decision_rationale": "This is a stock composition or
    a direct contribution currently combined with a stock value. Preserve original
    batch amount, exact source form and stock stage; do not use this stock strength
    as a direct final-medium concentration.", "evidence_id": "quantity-15", "arithmetic_separate_from_quote":
    "Original 2.4 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 2.4 g/L on the provider-declared
    stage volume; reported g_l is 2.4. This is not a receiving-medium dilution. Conditional
    receiving contribution: 2.4 g/L stock × 0.075 L / 1.001 L = 0.1798201798201798201798201798
    g/L. The source stock remains a separate preparation; do not encode both expansion
    and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "name": "KH2PO4", "current": {"value":
    "2.4", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "name": "KH2PO4", "current": {"value":
    "2.4", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[7].concentration", "name": "KH2PO4", "current": {"value":
    "2.4", "unit": "G_PER_L"}}], "source_amount": 2.4, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 2.4, "provider_stage_volume_ml": 1000, "primary_source_evidence_id":
    "dsmz165"}, {"field_path": "ingredients[8].concentration", "name": "(NH4)2SO4",
    "current": {"value": "6", "unit": "G_PER_L"}, "decision": "correct", "source_key":
    "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\":
    27,\n                        \"amount\": 6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 6,\n                        \"mmol_l\":
    45.4064,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[1]", "preparation_stage": "Mineral solution 2 (solution
    285, declared 1000 mL)", "decision_rationale": "This is a stock composition or
    a direct contribution currently combined with a stock value. Preserve original
    batch amount, exact source form and stock stage; do not use this stock strength
    as a direct final-medium concentration.", "evidence_id": "quantity-16", "arithmetic_separate_from_quote":
    "Original 6 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 6 g/L on the provider-declared
    stage volume; reported g_l is 6. This is not a receiving-medium dilution. Conditional
    receiving contribution: 6 g/L stock × 0.075 L / 1.001 L = 0.4495504495504495504495504496
    g/L. The source stock remains a separate preparation; do not encode both expansion
    and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "name": "(NH4)2SO4", "current":
    {"value": "6", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "name": "(NH4)2SO4", "current":
    {"value": "6", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[8].concentration", "name": "(NH4)2SO4", "current":
    {"value": "6", "unit": "G_PER_L"}}], "source_amount": 6, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 6, "provider_stage_volume_ml": 1000, "primary_source_evidence_id":
    "dsmz165"}, {"field_path": "ingredients[9].concentration", "name": "NaCl", "current":
    {"value": "1.5899999999999999", "unit": "G_PER_L"}, "decision": "correct", "source_key":
    "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 0.59,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.59,\n                        \"mmol_l\":
    10.0958,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[2]", "preparation_stage": "Mineral solution 2 (solution
    285, declared 1000 mL)", "decision_rationale": "This is a stock composition or
    a direct contribution currently combined with a stock value. Preserve original
    batch amount, exact source form and stock stage; do not use this stock strength
    as a direct final-medium concentration.", "evidence_id": "quantity-17", "arithmetic_separate_from_quote":
    "Original 0.59 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.59 g/L on the provider-declared
    stage volume; reported g_l is 0.59. This is not a receiving-medium dilution. Conditional
    receiving contribution: 0.59 g/L stock × 0.075 L / 1.001 L = 0.04420579420579420579420579421
    g/L. The source stock remains a separate preparation; do not encode both expansion
    and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "name": "NaCl", "current": {"value":
    "1.5899999999999999", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "name": "NaCl", "current": {"value":
    "1.5899999999999999", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[9].concentration", "name": "NaCl", "current": {"value":
    "1.5899999999999999", "unit": "G_PER_L"}}], "source_amount": 0.59, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.59, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[10].concentration",
    "name": "MgSO4 x 7 H2O", "current": {"value": "4.2", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 1.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.2,\n                        \"mmol_l\":
    4.86863,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[3]", "preparation_stage": "Mineral solution 2 (solution
    285, declared 1000 mL)", "decision_rationale": "This is a stock composition or
    a direct contribution currently combined with a stock value. Preserve original
    batch amount, exact source form and stock stage; do not use this stock strength
    as a direct final-medium concentration.", "evidence_id": "quantity-18", "arithmetic_separate_from_quote":
    "Original 1.2 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 1.2 g/L on the provider-declared
    stage volume; reported g_l is 1.2. This is not a receiving-medium dilution. Conditional
    receiving contribution: 1.2 g/L stock × 0.075 L / 1.001 L = 0.08991008991008991008991008991
    g/L. The source stock remains a separate preparation; do not encode both expansion
    and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "name": "MgSO4 x 7 H2O", "current":
    {"value": "4.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "name": "MgSO4 x 7 H2O", "current":
    {"value": "4.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[10].concentration", "name": "MgSO4 x 7 H2O", "current":
    {"value": "4.2", "unit": "G_PER_L"}}], "source_amount": 1.2, "source_unit": "g",
    "source_attribute": null, "provider_g_l": 1.2, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[11].concentration",
    "name": "CaCl2 x 2 H2O", "current": {"value": "0.82", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.72,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.72,\n                        \"mmol_l\":
    4.89746,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[4]", "preparation_stage": "Mineral solution 2 (solution
    285, declared 1000 mL)", "decision_rationale": "This is a stock composition or
    a direct contribution currently combined with a stock value. Preserve original
    batch amount, exact source form and stock stage; do not use this stock strength
    as a direct final-medium concentration.", "evidence_id": "quantity-19", "arithmetic_separate_from_quote":
    "Original 0.72 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.72 g/L on the provider-declared
    stage volume; reported g_l is 0.72. This is not a receiving-medium dilution. Conditional
    receiving contribution: 0.72 g/L stock × 0.075 L / 1.001 L = 0.05394605394605394605394605395
    g/L. The source stock remains a separate preparation; do not encode both expansion
    and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "name": "CaCl2 x 2 H2O", "current":
    {"value": "0.82", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "name": "CaCl2 x 2 H2O", "current":
    {"value": "0.82", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[11].concentration", "name": "CaCl2 x 2 H2O", "current":
    {"value": "0.82", "unit": "G_PER_L"}}], "source_amount": 0.72, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.72, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "source solution
    285 recipe[5] (not represented)", "name": "Distilled water", "current": null,
    "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[5]", "preparation_stage": "Mineral solution 2 (solution
    285, declared 1000 mL)", "decision_rationale": "Preserve the source solvent quantity
    1000 ml in its own stage. The provider declares this solution volume as 1000 mL;
    water addition is not independent proof of measured final volume.", "evidence_id":
    "quantity-20", "affected_local_fields": [], "source_amount": 1000, "source_unit":
    "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[12].concentration",
    "name": "Nitrilotriacetic acid", "current": {"value": "1.5", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\":
    189,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.84765,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[3].recipe[0]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-21",
    "arithmetic_separate_from_quote": "Original 1.5 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 1.5 g/L on the provider-declared stage volume; reported g_l is 1.5. This
    is not a receiving-medium dilution. Conditional receiving contribution: 1.5 g/L
    stock × 0.010 L / 1.001 L = 0.01498501498501498501498501499 g/L. The source stock
    remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "name": "Nitrilotriacetic acid",
    "current": {"value": "1.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "name": "Nitrilotriacetic acid",
    "current": {"value": "1.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[12].concentration", "name": "Nitrilotriacetic acid",
    "current": {"value": "1.5", "unit": "G_PER_L"}}], "source_amount": 1.5, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 1.5, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[10].concentration",
    "name": "MgSO4 x 7 H2O", "current": {"value": "4.2", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    12.1716,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[3].recipe[1]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-22",
    "arithmetic_separate_from_quote": "Original 3 g × 1 g/g ÷ (1000 mL / 1000 mL per
    L) = 3 g/L on the provider-declared stage volume; reported g_l is 3. This is not
    a receiving-medium dilution. Conditional receiving contribution: 3 g/L stock ×
    0.010 L / 1.001 L = 0.02997002997002997002997002997 g/L. The source stock remains
    a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path":
    "ingredients[10].concentration", "name": "MgSO4 x 7 H2O", "current": {"value":
    "4.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "name": "MgSO4 x 7 H2O", "current":
    {"value": "4.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[10].concentration", "name": "MgSO4 x 7 H2O", "current":
    {"value": "4.2", "unit": "G_PER_L"}}], "source_amount": 3, "source_unit": "g",
    "source_attribute": null, "provider_g_l": 3, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[13].concentration",
    "name": "MnSO4 x H2O", "current": {"value": "0.5", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\":
    14,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.9583,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[3].recipe[2]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-23",
    "arithmetic_separate_from_quote": "Original 0.5 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.5 g/L on the provider-declared stage volume; reported g_l is 0.5. This
    is not a receiving-medium dilution. Conditional receiving contribution: 0.5 g/L
    stock × 0.010 L / 1.001 L = 0.004995004995004995004995004995 g/L. The source stock
    remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "name": "MnSO4 x H2O", "current":
    {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "name": "MnSO4 x H2O", "current":
    {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[13].concentration", "name": "MnSO4 x H2O", "current":
    {"value": "0.5", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "g",
    "source_attribute": null, "provider_g_l": 0.5, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[9].concentration",
    "name": "NaCl", "current": {"value": "1.5899999999999999", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    17.1116,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[3].recipe[3]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-24",
    "arithmetic_separate_from_quote": "Original 1 g × 1 g/g ÷ (1000 mL / 1000 mL per
    L) = 1 g/L on the provider-declared stage volume; reported g_l is 1. This is not
    a receiving-medium dilution. Conditional receiving contribution: 1 g/L stock ×
    0.010 L / 1.001 L = 0.009990009990009990009990009990 g/L. The source stock remains
    a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path":
    "ingredients[9].concentration", "name": "NaCl", "current": {"value": "1.5899999999999999",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "name": "NaCl", "current": {"value":
    "1.5899999999999999", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[9].concentration", "name": "NaCl", "current": {"value":
    "1.5899999999999999", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 1, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[14].concentration",
    "name": "FeSO4 x 7 H2O", "current": {"value": "1.1", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.359693,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[3].recipe[4]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-25",
    "arithmetic_separate_from_quote": "Original 0.1 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.1 g/L on the provider-declared stage volume; reported g_l is 0.1. This
    is not a receiving-medium dilution. Conditional receiving contribution: 0.1 g/L
    stock × 0.010 L / 1.001 L = 0.0009990009990009990009990009990 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "name": "FeSO4 x 7 H2O", "current":
    {"value": "1.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "name": "FeSO4 x 7 H2O", "current":
    {"value": "1.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[14].concentration", "name": "FeSO4 x 7 H2O", "current":
    {"value": "1.1", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit": "g",
    "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[15].concentration",
    "name": "CoSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\":
    198,\n                        \"amount\": 0.18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\":
    1.16132,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[3].recipe[5]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-26",
    "arithmetic_separate_from_quote": "Original 0.18 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.18 g/L on the provider-declared stage volume; reported g_l is 0.18.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.18
    g/L stock × 0.010 L / 1.001 L = 0.001798201798201798201798201798 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "name": "CoSO4 x 7 H2O", "current":
    {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "name": "CoSO4 x 7 H2O", "current":
    {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[15].concentration", "name": "CoSO4 x 7 H2O", "current":
    {"value": "0.18", "unit": "G_PER_L"}}], "source_amount": 0.18, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.18, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[11].concentration",
    "name": "CaCl2 x 2 H2O", "current": {"value": "0.82", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.680203,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[3].recipe[6]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-27",
    "arithmetic_separate_from_quote": "Original 0.1 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.1 g/L on the provider-declared stage volume; reported g_l is 0.1. This
    is not a receiving-medium dilution. Conditional receiving contribution: 0.1 g/L
    stock × 0.010 L / 1.001 L = 0.0009990009990009990009990009990 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "name": "CaCl2 x 2 H2O", "current":
    {"value": "0.82", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "name": "CaCl2 x 2 H2O", "current":
    {"value": "0.82", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[11].concentration", "name": "CaCl2 x 2 H2O", "current":
    {"value": "0.82", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit": "g",
    "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[16].concentration",
    "name": "ZnSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 0.18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\":
    0.625954,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[3].recipe[7]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-28",
    "arithmetic_separate_from_quote": "Original 0.18 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.18 g/L on the provider-declared stage volume; reported g_l is 0.18.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.18
    g/L stock × 0.010 L / 1.001 L = 0.001798201798201798201798201798 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "name": "ZnSO4 x 7 H2O", "current":
    {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "name": "ZnSO4 x 7 H2O", "current":
    {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[16].concentration", "name": "ZnSO4 x 7 H2O", "current":
    {"value": "0.18", "unit": "G_PER_L"}}], "source_amount": 0.18, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.18, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[17].concentration",
    "name": "CuSO4 x 5 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\":
    121,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0400503,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[3].recipe[8]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-29",
    "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.01
    g/L stock × 0.010 L / 1.001 L = 0.00009990009990009990009990009990 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "name": "CuSO4 x 5 H2O", "current":
    {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "name": "CuSO4 x 5 H2O", "current":
    {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[17].concentration", "name": "CuSO4 x 5 H2O", "current":
    {"value": "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.01, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[18].concentration",
    "name": "AlK(SO4)2 x 12 H2O", "current": {"value": "0.02", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\":
    908,\n                        \"amount\": 0.02,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0421596,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[3].recipe[9]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-30",
    "arithmetic_separate_from_quote": "Original 0.02 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.02 g/L on the provider-declared stage volume; reported g_l is 0.02.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.02
    g/L stock × 0.010 L / 1.001 L = 0.0001998001998001998001998001998 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "name": "AlK(SO4)2 x 12 H2O", "current":
    {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "name": "AlK(SO4)2 x 12 H2O", "current":
    {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[18].concentration", "name": "AlK(SO4)2 x 12 H2O", "current":
    {"value": "0.02", "unit": "G_PER_L"}}], "source_amount": 0.02, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.02, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[19].concentration",
    "name": "H3BO3", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.161708,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[3].recipe[10]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-31",
    "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.01
    g/L stock × 0.010 L / 1.001 L = 0.00009990009990009990009990009990 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[19].concentration", "name": "H3BO3", "current": {"value":
    "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[19].concentration", "name": "H3BO3", "current": {"value":
    "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[19].concentration", "name": "H3BO3", "current": {"value":
    "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 0.01, "provider_stage_volume_ml": 1000, "primary_source_evidence_id":
    "dsmz165"}, {"field_path": "ingredients[20].concentration", "name": "Na2MoO4 x
    2 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct",
    "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0413309,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[3].recipe[11]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-32",
    "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.01
    g/L stock × 0.010 L / 1.001 L = 0.00009990009990009990009990009990 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[20].concentration", "name": "Na2MoO4 x 2 H2O", "current":
    {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[20].concentration", "name": "Na2MoO4 x 2 H2O", "current":
    {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[20].concentration", "name": "Na2MoO4 x 2 H2O", "current":
    {"value": "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.01, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[21].concentration",
    "name": "NiCl2 x 6 H2O", "current": {"value": "0.03", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.231483,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[3].recipe[12]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-33",
    "arithmetic_separate_from_quote": "Original 0.03 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.03 g/L on the provider-declared stage volume; reported g_l is 0.03.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.03
    g/L stock × 0.010 L / 1.001 L = 0.0002997002997002997002997002997 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "name": "NiCl2 x 6 H2O", "current":
    {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "name": "NiCl2 x 6 H2O", "current":
    {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[21].concentration", "name": "NiCl2 x 6 H2O", "current":
    {"value": "0.03", "unit": "G_PER_L"}}], "source_amount": 0.03, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.03, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[22].concentration",
    "name": "Na2SeO3 x 5 H2O", "current": {"value": "0.0003", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\":
    0.00114062,\n                        \"optional\": 0\n                    }",
    "source_locator": "$.data.solutions[3].recipe[13]", "preparation_stage": "Modified
    Wolin''s mineral solution (solution 241, declared 1000 mL)", "decision_rationale":
    "This is a stock composition or a direct contribution currently combined with
    a stock value. Preserve original batch amount, exact source form and stock stage;
    do not use this stock strength as a direct final-medium concentration.", "evidence_id":
    "quantity-34", "arithmetic_separate_from_quote": "Original 0.3 mg × 0.001 g/mg
    ÷ (1000 mL / 1000 mL per L) = 0.0003 g/L on the provider-declared stage volume;
    reported g_l is 0.0003. This is not a receiving-medium dilution. Conditional receiving
    contribution: 0.0003 g/L stock × 0.010 L / 1.001 L = 0.000002997002997002997002997002997
    g/L. The source stock remains a separate preparation; do not encode both expansion
    and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "name": "Na2SeO3 x 5 H2O", "current":
    {"value": "0.0003", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "name": "Na2SeO3 x 5 H2O", "current":
    {"value": "0.0003", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[22].concentration", "name": "Na2SeO3 x 5 H2O", "current":
    {"value": "0.0003", "unit": "G_PER_L"}}], "source_amount": 0.3, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.0003, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[23].concentration",
    "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\":
    0.00121267,\n                        \"optional\": 0\n                    }",
    "source_locator": "$.data.solutions[3].recipe[14]", "preparation_stage": "Modified
    Wolin''s mineral solution (solution 241, declared 1000 mL)", "decision_rationale":
    "This is a stock composition or a direct contribution currently combined with
    a stock value. Preserve original batch amount, exact source form and stock stage;
    do not use this stock strength as a direct final-medium concentration.", "evidence_id":
    "quantity-35", "arithmetic_separate_from_quote": "Original 0.4 mg × 0.001 g/mg
    ÷ (1000 mL / 1000 mL per L) = 0.0004 g/L on the provider-declared stage volume;
    reported g_l is 0.0004. This is not a receiving-medium dilution. Conditional receiving
    contribution: 0.0004 g/L stock × 0.010 L / 1.001 L = 0.000003996003996003996003996003996
    g/L. The source stock remains a separate preparation; do not encode both expansion
    and stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[23].concentration", "name": "Na2WO4 x 2 H2O", "current":
    {"value": "0.0004", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[23].concentration", "name": "Na2WO4 x 2 H2O", "current":
    {"value": "0.0004", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[23].concentration", "name": "Na2WO4 x 2 H2O", "current":
    {"value": "0.0004", "unit": "G_PER_L"}}], "source_amount": 0.4, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.0004, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "source solution
    241 recipe[15] (not represented)", "name": "Distilled water", "current": null,
    "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[3].recipe[15]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "Preserve the
    source solvent quantity 1000 ml in its own stage. The provider declares this solution
    volume as 1000 mL; water addition is not independent proof of measured final volume.",
    "evidence_id": "quantity-36", "affected_local_fields": [], "source_amount": 1000,
    "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[14].concentration",
    "name": "FeSO4 x 7 H2O", "current": {"value": "1.1", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    3.59693,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[4].recipe[0]", "preparation_stage": "FeSO4 x 7 H2O solution
    (0.1% w/v) (solution 5861, declared 1000 mL)", "decision_rationale": "This is
    a stock composition or a direct contribution currently combined with a stock value.
    Preserve original batch amount, exact source form and stock stage; do not use
    this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-37",
    "arithmetic_separate_from_quote": "Original 1 g × 1 g/g ÷ (1000 mL / 1000 mL per
    L) = 1 g/L on the provider-declared stage volume; reported g_l is 1. This is not
    a receiving-medium dilution. Conditional receiving contribution: 1 g/L stock ×
    0.020 L / 1.001 L = 0.01998001998001998001998001998 g/L. The source stock remains
    a separate preparation; do not encode both expansion and stock addition.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path":
    "ingredients[14].concentration", "name": "FeSO4 x 7 H2O", "current": {"value":
    "1.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "name": "FeSO4 x 7 H2O", "current":
    {"value": "1.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[14].concentration", "name": "FeSO4 x 7 H2O", "current":
    {"value": "1.1", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "g",
    "source_attribute": null, "provider_g_l": 1, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[24].concentration",
    "name": "H2SO4", "current": {"value": "1000", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"H2SO4\",\n                        \"compound_id\":
    122,\n                        \"attribute\": \"0.1 N\",\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[4].recipe[1]",
    "preparation_stage": "FeSO4 x 7 H2O solution (0.1% w/v) (solution 5861, declared
    1000 mL)", "decision_rationale": "The exact row is 1000 mL of 0.1 N H2SO4 in the
    ferrous sulfate stock. Local 1000 G_PER_L is a liquid-volume-to-mass-unit error
    and a stage error. Retain the dilute acid solvent and its normality; do not treat
    it as neat acid or infer density.", "evidence_id": "quantity-38", "arithmetic_separate_from_quote":
    "No mass conversion is required or asserted. The source uses this acid in stock
    5861; the main medium adds only 20 mL of that stock.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml", "field_path":
    "ingredients[24].concentration", "name": "H2SO4", "current": {"value": "1000",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[24].concentration", "name": "H2SO4", "current": {"value":
    "1000", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[24].concentration", "name": "H2SO4", "current": {"value":
    "1000", "unit": "G_PER_L"}}], "source_amount": 1000, "source_unit": "ml", "source_attribute":
    "0.1 N", "provider_g_l": null, "provider_stage_volume_ml": 1000, "primary_source_evidence_id":
    "dsmz165"}, {"field_path": "ingredients[25].concentration", "name": "Biotin",
    "current": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "source_key":
    "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[5].recipe[0]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-39",
    "arithmetic_separate_from_quote": "Original 20 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.020 g/L on the provider-declared stage volume; reported g_l is 0.02.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.02
    g/L stock × 0.001 L / 1.001 L = 0.00001998001998001998001998001998 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[25].concentration", "name": "Biotin", "current": {"value":
    "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[25].concentration", "name": "Biotin", "current": {"value":
    "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[25].concentration", "name": "Biotin", "current": {"value":
    "0.02", "unit": "G_PER_L"}}], "source_amount": 20, "source_unit": "mg", "source_attribute":
    null, "provider_g_l": 0.02, "provider_stage_volume_ml": 1000, "primary_source_evidence_id":
    "dsmz165"}, {"field_path": "ingredients[26].concentration", "name": "Folic acid",
    "current": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "source_key":
    "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[5].recipe[1]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-40",
    "arithmetic_separate_from_quote": "Original 20 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.020 g/L on the provider-declared stage volume; reported g_l is 0.02.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.02
    g/L stock × 0.001 L / 1.001 L = 0.00001998001998001998001998001998 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "name": "Folic acid", "current":
    {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "name": "Folic acid", "current":
    {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[26].concentration", "name": "Folic acid", "current":
    {"value": "0.02", "unit": "G_PER_L"}}], "source_amount": 20, "source_unit": "mg",
    "source_attribute": null, "provider_g_l": 0.02, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[27].concentration",
    "name": "Pyridoxine hydrochloride", "current": {"value": "0.1", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[5].recipe[2]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-41",
    "arithmetic_separate_from_quote": "Original 100 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.100 g/L on the provider-declared stage volume; reported g_l is 0.1.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.1
    g/L stock × 0.001 L / 1.001 L = 0.00009990009990009990009990009990 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[27].concentration", "name": "Pyridoxine hydrochloride",
    "current": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[27].concentration", "name": "Pyridoxine hydrochloride",
    "current": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[27].concentration", "name": "Pyridoxine hydrochloride",
    "current": {"value": "0.1", "unit": "G_PER_L"}}], "source_amount": 100, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[28].concentration",
    "name": "Thiamine HCl", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[5].recipe[3]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-42",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.05
    g/L stock × 0.001 L / 1.001 L = 0.00004995004995004995004995004995 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[28].concentration", "name": "Thiamine HCl", "current":
    {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[28].concentration", "name": "Thiamine HCl", "current":
    {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[28].concentration", "name": "Thiamine HCl", "current":
    {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg",
    "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[29].concentration",
    "name": "Riboflavin", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[5].recipe[4]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-43",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.05
    g/L stock × 0.001 L / 1.001 L = 0.00004995004995004995004995004995 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[29].concentration", "name": "Riboflavin", "current":
    {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[29].concentration", "name": "Riboflavin", "current":
    {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[29].concentration", "name": "Riboflavin", "current":
    {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg",
    "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[30].concentration",
    "name": "Nicotinic acid", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[5].recipe[5]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-44",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.05
    g/L stock × 0.001 L / 1.001 L = 0.00004995004995004995004995004995 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[30].concentration", "name": "Nicotinic acid", "current":
    {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[30].concentration", "name": "Nicotinic acid", "current":
    {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[30].concentration", "name": "Nicotinic acid", "current":
    {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg",
    "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[31].concentration",
    "name": "Calcium D-(+)-pantothenate", "current": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[5].recipe[6]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-45",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.05
    g/L stock × 0.001 L / 1.001 L = 0.00004995004995004995004995004995 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[31].concentration", "name": "Calcium D-(+)-pantothenate",
    "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[31].concentration", "name": "Calcium D-(+)-pantothenate",
    "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[31].concentration", "name": "Calcium D-(+)-pantothenate",
    "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[32].concentration",
    "name": "Vitamin B12", "current": {"value": "0.001", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }",
    "source_locator": "$.data.solutions[5].recipe[7]", "preparation_stage": "Wolin''s
    vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale":
    "This is a stock composition or a direct contribution currently combined with
    a stock value. Preserve original batch amount, exact source form and stock stage;
    do not use this stock strength as a direct final-medium concentration.", "evidence_id":
    "quantity-46", "arithmetic_separate_from_quote": "Original 1 mg × 0.001 g/mg ÷
    (1000 mL / 1000 mL per L) = 0.001 g/L on the provider-declared stage volume; reported
    g_l is 0.001. This is not a receiving-medium dilution. Conditional receiving contribution:
    0.001 g/L stock × 0.001 L / 1.001 L = 9.990009990009990009990009990E-7 g/L. The
    source stock remains a separate preparation; do not encode both expansion and
    stock addition.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[32].concentration", "name": "Vitamin B12", "current":
    {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[32].concentration", "name": "Vitamin B12", "current":
    {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[32].concentration", "name": "Vitamin B12", "current":
    {"value": "0.001", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "mg",
    "source_attribute": null, "provider_g_l": 0.001, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[33].concentration",
    "name": "p-Aminobenzoic acid", "current": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[5].recipe[8]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-47",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.05
    g/L stock × 0.001 L / 1.001 L = 0.00004995004995004995004995004995 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[33].concentration", "name": "p-Aminobenzoic acid",
    "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[33].concentration", "name": "p-Aminobenzoic acid",
    "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[33].concentration", "name": "p-Aminobenzoic acid",
    "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "ingredients[34].concentration",
    "name": "(DL)-alpha-Lipoic acid", "current": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[5].recipe[9]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-48",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional receiving contribution: 0.05
    g/L stock × 0.001 L / 1.001 L = 0.00004995004995004995004995004995 g/L. The source
    stock remains a separate preparation; do not encode both expansion and stock addition.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[34].concentration", "name": "(DL)-alpha-Lipoic acid",
    "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml",
    "field_path": "ingredients[34].concentration", "name": "(DL)-alpha-Lipoic acid",
    "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml",
    "field_path": "ingredients[34].concentration", "name": "(DL)-alpha-Lipoic acid",
    "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "source solution
    5980 recipe[10] (not represented)", "name": "Distilled water", "current": null,
    "decision": "add", "source_key": "mediadive165api", "source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[5].recipe[10]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "Preserve the
    source solvent quantity 1000 ml in its own stage. The provider declares this solution
    volume as 1000 mL; water addition is not independent proof of measured final volume.",
    "evidence_id": "quantity-49", "affected_local_fields": [], "source_amount": 1000,
    "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz165"}, {"field_path": "mineral stock
    KOH addition (not quantified)", "name": "KOH", "current": null, "decision": "not_quantified",
    "source_key": "dsmz165", "source_quote": "First dissolve nitrilotriacetic acid
    and adjust pH to 6.5 with KOH, then add minerals. Adjust", "source_locator": "page
    2, Modified Wolin mineral stock preparation", "preparation_stage": "mineral stock",
    "decision_rationale": "Source adjusts pH to 6.5 and then 7.0 with KOH without
    specifying a fixed amount. Do not fill that absence with zero or a guessed dose.",
    "evidence_id": "quantity-50"}, {"field_path": "later sterile stock volumes (not
    quantified)", "name": "Post-autoclave anoxic additions", "current": null, "decision":
    "not_quantified", "source_key": "dsmz165", "source_quote": "autoclave. Add cellobiose,
    vitamins, cysteine and sulfide from sterile anoxic stock solutions", "source_locator":
    "page 1, main preparation paragraph", "preparation_stage": "main preparation after
    autoclaving", "decision_rationale": "Cellobiose, vitamins, cysteine, sulfide and
    carbonate have stated ingredient amounts, but not all later stock volumes are
    specified. Their sterile/anoxic handling and separate gas atmospheres cannot establish
    a measured final volume.", "evidence_id": "quantity-51"}, {"field_path": "ph_value
    / ph_range", "name": "Complete-medium pH", "current": 7.2, "decision": "correct",
    "source_key": "dsmz165", "source_quote": "filtration. Prior to use adjust pH of
    complete medium to 7.2 - 7.4. Cellulose (MN 300,", "source_locator": "page 1,
    main preparation paragraph", "preparation_stage": "complete medium", "decision_rationale":
    "Target pH 7.2 is a permitted endpoint, but the exact source and DSMZ owner specify
    the complete-medium range 7.2–7.4. Preserve its scope and range rather than replacing
    it with a midpoint.", "evidence_id": "quantity-52"}, {"field_path": "preparation_steps.initial_gas",
    "name": "Initial gas composition", "current": null, "decision": "add", "source_key":
    "dsmz165", "source_quote": "sparge medium with 80% N2 and 20% CO2 gas mixture
    for 30 – 45 min to make it anoxic.", "source_locator": "page 1, main preparation
    paragraph", "preparation_stage": "initial anoxic preparation", "decision_rationale":
    "Preserve the source 80% N2 / 20% CO2 gas mixture as preparation context, not
    an organism phenotype.", "evidence_id": "quantity-53"}, {"field_path": "preparation_steps.sparging_duration",
    "name": "Sparging duration", "current": null, "decision": "add", "source_key":
    "dsmz165", "source_quote": "sparge medium with 80% N2 and 20% CO2 gas mixture
    for 30 – 45 min to make it anoxic.", "source_locator": "page 1, main preparation
    paragraph", "preparation_stage": "initial anoxic preparation", "decision_rationale":
    "The source specifies 30–45 min; preserve the interval without choosing a midpoint.",
    "evidence_id": "quantity-54"}, {"field_path": "preparation_steps.addition_stock_gas",
    "name": "Gas for separate addition stocks", "current": null, "decision": "add",
    "source_key": "dsmz165", "source_quote": "prepared under 100% N2 gas and carbonate
    from a sterile anoxic stock solution prepared", "source_locator": "page 1, main
    preparation paragraph", "preparation_stage": "cellobiose/vitamin/cysteine/sulfide
    stock preparation", "decision_rationale": "The specified stocks are prepared under
    100% N2; the separately qualified carbonate stock has a different atmosphere.",
    "evidence_id": "quantity-55"}, {"field_path": "preparation_steps.carbonate_stock_gas",
    "name": "Gas for carbonate stock", "current": null, "decision": "add", "source_key":
    "dsmz165", "source_quote": "under 80% N2 and 20% CO2 gas mixture. Cellobiose and
    vitamins have to be sterilized by", "source_locator": "page 1, main preparation
    paragraph", "preparation_stage": "carbonate stock preparation", "decision_rationale":
    "Preserve the separate carbonate-stock preparation under 80% N2 / 20% CO2; do
    not transfer the 100% N2 instruction from the preceding stocks.", "evidence_id":
    "quantity-56"}]'
- assessment_id: evidence
  area: evidence
  topic: Claim-level source support and actual reference-check coverage
  outcome: concern
  summary: No reviewed layer has claim-level quantity evidence. The target reference
    check performed zero evidence checks. This review supplies exact raw snippets
    and stable locators from the bound original captures; references, stock-dose evidence
    and ingredient evidence should be added in their existing schema locations only
    during separate curation.
  target_ids:
  - CultureMech:004192
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - validate-references
  - source-catalog
- assessment_id: organisms
  area: scope
  topic: Bounded biological claims and optional entities
  outcome: not_applicable
  summary: No reviewed layer asserts organism/strain identifiers, assemblies, DOI/PMID
    papers, growth outcomes or KG-Microbe matches. Catalog source names and generic
    cultivation applications do not establish strain-specific growth. Source formulation
    alternatives are assessed separately without adding organisms or inventing evidence.
  target_ids:
  - CultureMech:004192
  evidence_ids:
  - record
  - owner-0
  - owner-1
findings:
- finding_id: f1
  issue_key: cm004192-stock-stage-and-acid-units
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Five stocks are flattened and dilute acid volume becomes mass concentration
  description: The source adds stocks at 75, 75, 10, 20 and 1 mL, but the target and
    owners encode their undiluted component strengths as direct ingredients. Four
    rows sum different stock values (NaCl 0.59+1, MgSO4 heptahydrate 1.2+3, calcium
    chloride dihydrate 0.72+0.1, FeSO4 heptahydrate 0.1+1). Most conspicuously, 1000
    mL H2SO4 at 0.1 N within the ferrous stock becomes 1000 g/L direct acid. The 49
    source rows plus two unquantified additions preserve exact stages and units; provider
    1001 mL and listed-liquid 1001.5 mL remain distinct.
  target_ids:
  - CultureMech:004192
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz165
  - mediadive165api
  - importer
  - cleanup
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P1
  native_severity: P1
  normalization_reason: 'Native P1 scientific formulation blocker: 1000 mL of 0.1
    N acid becomes 1000 g/L direct acid and all five stock additions lose their preparation
    stages. The encoded formulation is unusable as the named source recipe; this is
    not a schema P1.1 failure, and all target diagnostics passed.'
- finding_id: f2
  issue_key: cm004192-salt-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydrate and sodium indicator identities disagree with source forms
  description: NiCl2 x 6 H2O maps to nickel dichloride without waters, and Sodium
    resazurin maps to neutral Resazurin without sodium. Label validation and MIM coverage
    cannot resolve these form mismatches.
  target_ids:
  - CultureMech:004192
  field_paths:
  - ingredients[21].term
  - ingredients[21].mediaingredientmech_chebi_term
  - ingredients[0].term
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz165
  - chebi34887
  - chebi8806
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml
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
  issue_key: cm004192-preparation-and-carbon-branch-lost
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation and the alternative carbon-source branch are omitted
  description: 'The generated target and KOMODO owner omit the exact anoxic and differential
    sterilization sequence, mineral-stock pH adjustment and ferrous-stock freshness
    retained by the DSMZ owner. They also weaken cellulose-as-an-alternative-to-cellobiose
    into a generic optional row, retain an incompatible Aerobic: Yes note, and reduce
    the pH range to one endpoint. The source catalog classification flags disagree,
    so branch-specific composition type also needs reassessment rather than a forced
    replacement.'
  target_ids:
  - CultureMech:004192
  field_paths:
  - preparation_steps
  - ingredients[3].notes
  - ph_value
  - notes
  - medium_type
  - composition_type
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz165
  - komodoMediaList
  - mediadive165api
  - resolver
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: Native P3.5 with related P3.4 is major because omission of
    the exact anoxic/differential sterilization process and carbon-source substitution
    materially changes the reproducible formulation; this is not a generic formatting
    or optional-field concern.
- finding_id: f4
  issue_key: cm004192-history-timezones
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Four inherited timestamp instances are malformed or timezone-naive
  description: The target and KOMODO owner each contain one malformed .fZ import timestamp
    and one timezone-naive resolver timestamp. DSMZ owner history is valid and timezone-aware.
    No timezone is inferred for older values.
  target_ids:
  - CultureMech:004192
  field_paths:
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - history
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.4
  native_severity: P4
  normalization_reason: Native P4.4 history completeness is minor here because malformed
    or timezone-naive timestamps impair provenance interpretation without changing
    the independently captured source quantities.
actions:
- action_id: a1
  description: Restore all five stocks and their exact doses; keep dilute acid solvent
    normality/volume, original source forms and stock-specific amounts separate. Recalculate
    any receiving-medium concentration only after its volume basis is explicitly resolved,
    and attach narrow evidence before authorized regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:004192
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml
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
  description: Verify and align exact supplied-form identifiers in both maintained
    owners, retaining source masses and qualifiers; do not invent replacement IDs
    or anhydrous-to-hydrate conversions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:004192
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml
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
  description: Preserve the complete source preparation and explicit carbon-source
    substitution, reconcile the catalog aerobic note, retain stage-specific pH and
    assess composition type for the documented branch. Preview current formulation-aware
    merging so unlike source assertions are not silently collapsed.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:004192
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml
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
  description: Preserve append-only history while documenting the unresolved historical
    timezone and improving future timestamp emission only under separate authorization.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:004192
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_165_ACETIVIBRIO_CELLULOLYTICUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetivibrio_cellulolyticus_medium.yaml
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
- The provider declares 1001 mL for the main solution; the listed liquid additions
  sum 1001.5 mL, and preparation mentions later sterile stocks without all dose volumes.
  Neither value is presented as independently measured final volume.
- Stock dilution calculations use the explicitly stated provider basis conditionally.
  They are not applied corrections and do not authorize double-counting expanded ingredients
  and stock doses.
- The source lists cellulose grades as alternatives to cellobiose. No selected branch
  or composition of Kleenex/HCl-treated cotton is inferred, and no branch-specific
  DEFINED/COMPLEX replacement is invented.
- Source accessions identify recipes, not strains. No taxonomic, growth, assembly
  or optimal-condition claim is inferred from the medium title.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-015
- generated-medium
```
