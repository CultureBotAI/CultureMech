# Source and formulation review: acetitomaculum_medium (CultureMech:005968)

- Review: 20261021T100353Z-culturemech-005968-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T09:56:38Z
- Finished UTC: 2026-10-21T10:03:53Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact KOMODO 540 and DSMZ 540 sources identify this medium and its two maintained contributors. The generated target and both owners flatten two stocks into direct concentrations and sum amounts from different preparation stages. Nickel chloride hexahydrate and sodium resazurin also have incompatible asserted chemical forms. The DSMZ owner preserves the anoxic preparation, while the KOMODO owner and generated target omit it and retain an Aerobic: Yes catalog note. All four documented diagnostics pass; four historical timestamp instances remain malformed or timezone-naive.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 141; batch 015 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding fourteen task batches contain 140 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 142 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:005968 | data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml | generated | acetitomaculum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:005968 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:005968 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch015/141/strict.tsv |
| validate-terms | passed | True | CultureMech:005968 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:005968 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:005968 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Scoped timestamp syntax and timezone inspection | failed | False | CultureMech:005968 | 31 timestamps inspected, 4 invalid or timezone-naive; old provenance remains unchanged. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:005968.

The four documented recipes completed; interpret the scope of each separately.

### Stable record, source accession and maintained contributors

identity: supported. Targets: CultureMech:005968.

CultureMech:005968 is the generated KOMODO 540 canonical record, with explicit merge contributors CM005968 and DSMZ owner CM001673. The exact KOMODO link and current DSMZ title establish source identity. Both full owner records retain the same 40 ingredient values, but preparation and catalog notes differ. All hashes match the native inspection.

### Reciprocal SOURCE_DUPLICATE relation

scope: supported. Targets: CultureMech:005968.

The target/KOMODO parent_media points to DSMZ owner CM001673 and its exact path; that owner reciprocally lists CM005968 in variant_children. Both internal IDs and paths resolve in the inspected inputs. This is supported as same-accession source duplication, without treating the differing preparation/notes as identical or claiming experimental equivalence.

### Boundary-precision difference in three provider g_l values

quantity: concern. Targets: CultureMech:005968.

For NH4Cl, cysteine hydrochloride monohydrate and sodium sulfide nonahydrate, the provider gives 0.3 g, 1015 mL and g_l 0.295566. Exact division is 0.295566502463... g/L and ordinary six-decimal rounding gives 0.295567, so the displayed provider value differs by 5.02463e-7 g/L, slightly beyond half a final decimal place. The existing local values reproduce the provider, but the strict arithmetic guard would not independently confirm that last digit. Preserve the provider value and this small rounding limit; no scale error or new correction is asserted.

### Primary labels/forms and pinned secondary correspondence

grounding: supported. Targets: CultureMech:005968.

Layer-specific counts are {"target": {"ingredient_instances": 40, "primary_CHEBI_instances": 39, "secondary_current_asserted_instances": 37, "secondary_current_verified_instances": 37, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.5, "secondary_verified_percent": 92.5}, "owner-0": {"ingredient_instances": 40, "primary_CHEBI_instances": 39, "secondary_current_asserted_instances": 37, "secondary_current_verified_instances": 37, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.5, "secondary_verified_percent": 92.5}, "owner-1": {"ingredient_instances": 40, "primary_CHEBI_instances": 39, "secondary_current_asserted_instances": 37, "secondary_current_verified_instances": 37, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.5, "secondary_verified_percent": 92.5}}. Percentages are 0–100 linkage coverage over direct ingredient instances, not scientific accuracy. The 0 legacy link instances across reviewed layers are unverified by the current CHEBI-keyed snapshot; absence here does not prove historical invalidity. Current secondary keys without a live preferred-term row are []. No secondary linked-set percentage is invented for an empty set.

{"label_drift": [], "legacy": [], "missing_current_secondary": []}

### Supplied salt, hydrate and stereochemical forms

grounding: concern. Targets: CultureMech:005968.

Every asserted primary label resolves, but chemical-form comparison exposes two disagreements: NiCl2 x 6 H2O is assigned CHEBI:34887 (Cl2Ni, no waters), and Sodium resazurin is assigned CHEBI:8806 (neutral C12H7NO4, no sodium). Both primary and secondary nickel assertions need source-form review. The calcium D-(+)-pantothenate source agrees with CHEBI:31345 D-specific synonyms/structure; its short generic label is not an error. CHEBI:16494 has no selected stereochemistry, so it does not contradict DL lipoic acid, whose qualifier should remain explicit. CHEBI:91248 explicitly defines the cysteine hydrochloride monohydrate. Other source hydrates and generic vitamin B12 are preserved without molecular-weight substitution or inferred purity.

### Anoxic process, pH and sterilization scope

consistency: concern. Targets: CultureMech:005968.

The primary and DSMZ owner specify initial 80% N2/20% CO2 sparging for 30–45 min, bicarbonate/pH equilibration, same-atmosphere dispensing/autoclaving, sterile anoxic glucose/vitamin/cysteine/sulfide additions under 100% N2, vitamin filtration and final medium pH 6.8–7.0. The mineral-stock pH 6.5 then 7.0 is a separate stage. Target and KOMODO owner omit all preparation steps and retain Aerobic: Yes. That note must be reconciled as catalog provenance, not promoted to an incubation phenotype. The source does not give autoclave time/temperature, storage or shelf life; none is invented.

### Composition type, state and bounded use

scope: supported. Targets: CultureMech:005968.

COMPLEX/UNDEFINED are compatible with the explicit yeast extract and provider complex_medium=yes. LIQUID is consistent with the exact formulation lacking a gelling-agent branch. Bacterial filing and Microbial cultivation are broad catalog context, not verified growth for any named organism. Catalog aerobic wording is handled separately as a preparation inconsistency.

### Append-only history and timestamp interpretation

provenance: concern. Targets: CultureMech:005968.

31 exact timestamp instances were examined; 4 lack valid syntax or explicit timezone. No local timestamp was assumed UTC or rewritten. Process and confidence annotations are not independent scientific evidence.

[{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "curation_history[0].timestamp", "value": "2026-01-27T01:15:03.fZ", "valid_ISO_datetime": false, "timezone_aware": false}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:07.640681", "valid_ISO_datetime": true, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "curation_history[0].timestamp", "value": "2026-01-27T01:15:03.fZ", "valid_ISO_datetime": false, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:07.640681", "valid_ISO_datetime": true, "timezone_aware": false}]

### Every stored amount, stock dose and source-stage dependency

quantity: concern. Targets: CultureMech:005968.

All 40 stored ingredient amounts in the target and each of two owners are traced to the 49 literal provider recipe rows at their own stages, plus two explicitly unquantified preparation additions and five quantitative preparation contexts. Direct g_l evidence, stock strengths/doses, solvent quantities and conditional dilution arithmetic are kept distinct. Source salt/hydrate mismatches remain separate from quantity arithmetic.

[{"field_path": "ingredients[0].concentration", "name": "KH2PO4", "current": {"value": "0.197044", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.197044,\n                        \"mmol_l\": 1.44795,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[0]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-1", "arithmetic_separate_from_quote": "Original 0.2 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 0.1970443349753694581280788177 g/L on the provider-declared stage volume; reported g_l is 0.197044. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "name": "KH2PO4", "current": {"value": "0.197044", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[0].concentration", "name": "KH2PO4", "current": {"value": "0.197044", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[0].concentration", "name": "KH2PO4", "current": {"value": "0.197044", "unit": "G_PER_L"}}], "source_amount": 0.2, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.197044, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[1].concentration", "name": "Na2SO4", "current": {"value": "0.0985222", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0985222,\n                        \"mmol_l\": 0.693623,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[1]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-2", "arithmetic_separate_from_quote": "Original 0.1 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 0.09852216748768472906403940887 g/L on the provider-declared stage volume; reported g_l is 0.0985222. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "name": "Na2SO4", "current": {"value": "0.0985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[1].concentration", "name": "Na2SO4", "current": {"value": "0.0985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[1].concentration", "name": "Na2SO4", "current": {"value": "0.0985222", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.0985222, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[2].concentration", "name": "NH4Cl", "current": {"value": "0.295566", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.295566,\n                        \"mmol_l\": 5.52564,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[2]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-3", "arithmetic_separate_from_quote": "Original 0.3 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 0.2955665024630541871921182266 g/L on the provider-declared stage volume; reported g_l is 0.295566. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "name": "NH4Cl", "current": {"value": "0.295566", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[2].concentration", "name": "NH4Cl", "current": {"value": "0.295566", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[2].concentration", "name": "NH4Cl", "current": {"value": "0.295566", "unit": "G_PER_L"}}], "source_amount": 0.3, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.295566, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[3].concentration", "name": "KCl", "current": {"value": "0.492611", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.492611,\n                        \"mmol_l\": 6.60779,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[3]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-4", "arithmetic_separate_from_quote": "Original 0.5 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 0.4926108374384236453201970443 g/L on the provider-declared stage volume; reported g_l is 0.492611. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "name": "KCl", "current": {"value": "0.492611", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[3].concentration", "name": "KCl", "current": {"value": "0.492611", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[3].concentration", "name": "KCl", "current": {"value": "0.492611", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.492611, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[4].concentration", "name": "NaCl", "current": {"value": "7.89655", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 7,\n                        \"unit\": \"g\",\n                        \"g_l\": 6.89655,\n                        \"mmol_l\": 118.011,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[4]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-5", "arithmetic_separate_from_quote": "Original 7 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 6.896551724137931034482758621 g/L on the provider-declared stage volume; reported g_l is 6.89655. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "name": "NaCl", "current": {"value": "7.89655", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[4].concentration", "name": "NaCl", "current": {"value": "7.89655", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[4].concentration", "name": "NaCl", "current": {"value": "7.89655", "unit": "G_PER_L"}}], "source_amount": 7, "source_unit": "g", "source_attribute": null, "provider_g_l": 6.89655, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[5].concentration", "name": "MgCl2 x 6 H2O", "current": {"value": "1.18227", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 1.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.18227,\n                        \"mmol_l\": 5.81529,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[5]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-6", "arithmetic_separate_from_quote": "Original 1.2 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 1.182266009852216748768472906 g/L on the provider-declared stage volume; reported g_l is 1.18227. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "name": "MgCl2 x 6 H2O", "current": {"value": "1.18227", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[5].concentration", "name": "MgCl2 x 6 H2O", "current": {"value": "1.18227", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[5].concentration", "name": "MgCl2 x 6 H2O", "current": {"value": "1.18227", "unit": "G_PER_L"}}], "source_amount": 1.2, "source_unit": "g", "source_attribute": null, "provider_g_l": 1.18227, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[6].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.247783", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.147783,\n                        \"mmol_l\": 1.00523,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[6]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-7", "arithmetic_separate_from_quote": "Original 0.15 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 0.1477832512315270935960591133 g/L on the provider-declared stage volume; reported g_l is 0.147783. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.247783", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[6].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.247783", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[6].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.247783", "unit": "G_PER_L"}}], "source_amount": 0.15, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.147783, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[7].concentration", "name": "Yeast extract", "current": {"value": "1.47783", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.47783,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[7]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-8", "arithmetic_separate_from_quote": "Original 1.5 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 1.477832512315270935960591133 g/L on the provider-declared stage volume; reported g_l is 1.47783. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "name": "Yeast extract", "current": {"value": "1.47783", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[7].concentration", "name": "Yeast extract", "current": {"value": "1.47783", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[7].concentration", "name": "Yeast extract", "current": {"value": "1.47783", "unit": "G_PER_L"}}], "source_amount": 1.5, "source_unit": "g", "source_attribute": null, "provider_g_l": 1.47783, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "source solution 1194 recipe[8] (not represented)", "name": "Modified Wolin's mineral solution", "current": null, "decision": "add", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[8]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The main recipe explicitly adds 10 ml of stock 241. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-9", "affected_local_fields": [], "source_amount": 10, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[8].concentration", "name": "NiCl2 x 6 H2O", "current": {"value": "0.030985222", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000985222,\n                        \"mmol_l\": 0.00760208,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[9]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-10", "arithmetic_separate_from_quote": "0.1% w/v means 0.1 g per 100 mL; 1 mL contains 0.001 g. Dividing by provider-declared 1015/1000 L gives 0.0009852216748768472906403940887 g/L; reported g_l is 0.000985222. Preserve this source stock dose separately.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "name": "NiCl2 x 6 H2O", "current": {"value": "0.030985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[8].concentration", "name": "NiCl2 x 6 H2O", "current": {"value": "0.030985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[8].concentration", "name": "NiCl2 x 6 H2O", "current": {"value": "0.030985222", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "ml", "source_attribute": "0.1% w/v", "provider_g_l": 0.000985222, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[9].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004985222", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 9.85222e-5,\n                        \"mmol_l\": 0.000298688,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[10]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-11", "arithmetic_separate_from_quote": "0.1% w/v means 0.1 g per 100 mL; 0.1 mL contains 0.0001 g. Dividing by provider-declared 1015/1000 L gives 0.00009852216748768472906403940887 g/L; reported g_l is 9.85222e-05. Preserve this source stock dose separately.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[9].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[9].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004985222", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit": "ml", "source_attribute": "0.1% w/v", "provider_g_l": 9.85222e-05, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[10].concentration", "name": "Ascorbic acid", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Ascorbic acid\",\n                        \"compound_id\": 112,\n                        \"attribute\": \"0.01% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 4.92611e-5,\n                        \"mmol_l\": 0.000279702,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[11]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-12", "arithmetic_separate_from_quote": "0.01% w/v means 0.01 g per 100 mL; 0.5 mL contains 0.00005 g. Dividing by provider-declared 1015/1000 L gives 0.00004926108374384236453201970443 g/L; reported g_l is 4.92611e-05. Preserve this source stock dose separately.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "name": "Ascorbic acid", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[10].concentration", "name": "Ascorbic acid", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[10].concentration", "name": "Ascorbic acid", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "ml", "source_attribute": "0.01% w/v", "provider_g_l": 4.92611e-05, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[11].concentration", "name": "Myo-inositol", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Myo-inositol\",\n                        \"compound_id\": 557,\n                        \"attribute\": \"0.01% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 4.92611e-5,\n                        \"mmol_l\": 0.00027343,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[12]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-13", "arithmetic_separate_from_quote": "0.01% w/v means 0.01 g per 100 mL; 0.5 mL contains 0.00005 g. Dividing by provider-declared 1015/1000 L gives 0.00004926108374384236453201970443 g/L; reported g_l is 4.92611e-05. Preserve this source stock dose separately.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "name": "Myo-inositol", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[11].concentration", "name": "Myo-inositol", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[11].concentration", "name": "Myo-inositol", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "ml", "source_attribute": "0.01% w/v", "provider_g_l": 4.92611e-05, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[12].concentration", "name": "Niacinamide", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Niacinamide\",\n                        \"compound_id\": 558,\n                        \"attribute\": \"0.01% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 4.92611e-5,\n                        \"mmol_l\": 0.000403366,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[13]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-14", "arithmetic_separate_from_quote": "0.01% w/v means 0.01 g per 100 mL; 0.5 mL contains 0.00005 g. Dividing by provider-declared 1015/1000 L gives 0.00004926108374384236453201970443 g/L; reported g_l is 4.92611e-05. Preserve this source stock dose separately.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "name": "Niacinamide", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[12].concentration", "name": "Niacinamide", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[12].concentration", "name": "Niacinamide", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "ml", "source_attribute": "0.01% w/v", "provider_g_l": 4.92611e-05, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[13].concentration", "name": "Choline chloride", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Choline chloride\",\n                        \"compound_id\": 115,\n                        \"attribute\": \"0.01% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 4.92611e-5,\n                        \"mmol_l\": 0.000352823,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[14]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-15", "arithmetic_separate_from_quote": "0.01% w/v means 0.01 g per 100 mL; 0.5 mL contains 0.00005 g. Dividing by provider-declared 1015/1000 L gives 0.00004926108374384236453201970443 g/L; reported g_l is 4.92611e-05. Preserve this source stock dose separately.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "name": "Choline chloride", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[13].concentration", "name": "Choline chloride", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[13].concentration", "name": "Choline chloride", "current": {"value": "4.92611e-05", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "ml", "source_attribute": "0.01% w/v", "provider_g_l": 4.92611e-05, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[14].concentration", "name": "Sodium resazurin", "current": {"value": "0.000492611", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000492611,\n                        \"mmol_l\": 0.00196126,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[15]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-16", "arithmetic_separate_from_quote": "0.1% w/v means 0.1 g per 100 mL; 0.5 mL contains 0.0005 g. Dividing by provider-declared 1015/1000 L gives 0.0004926108374384236453201970443 g/L; reported g_l is 0.000492611. Preserve this source stock dose separately.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "name": "Sodium resazurin", "current": {"value": "0.000492611", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[14].concentration", "name": "Sodium resazurin", "current": {"value": "0.000492611", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[14].concentration", "name": "Sodium resazurin", "current": {"value": "0.000492611", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "ml", "source_attribute": "0.1% w/v", "provider_g_l": 0.000492611, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[15].concentration", "name": "NaHCO3", "current": {"value": "3.94089", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 17,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.94089,\n                        \"mmol_l\": 46.9114,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[16]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-17", "arithmetic_separate_from_quote": "Original 4 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 3.940886699507389162561576355 g/L on the provider-declared stage volume; reported g_l is 3.94089. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "name": "NaHCO3", "current": {"value": "3.94089", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[15].concentration", "name": "NaHCO3", "current": {"value": "3.94089", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[15].concentration", "name": "NaHCO3", "current": {"value": "3.94089", "unit": "G_PER_L"}}], "source_amount": 4, "source_unit": "g", "source_attribute": null, "provider_g_l": 3.94089, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[16].concentration", "name": "D-Glucose", "current": {"value": "4.92611", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 18,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.92611,\n                        \"mmol_l\": 27.343,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[17]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-18", "arithmetic_separate_from_quote": "Original 5 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 4.926108374384236453201970443 g/L on the provider-declared stage volume; reported g_l is 4.92611. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "name": "D-Glucose", "current": {"value": "4.92611", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[16].concentration", "name": "D-Glucose", "current": {"value": "4.92611", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[16].concentration", "name": "D-Glucose", "current": {"value": "4.92611", "unit": "G_PER_L"}}], "source_amount": 5, "source_unit": "g", "source_attribute": null, "provider_g_l": 4.92611, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "source solution 1194 recipe[18] (not represented)", "name": "Wolin's vitamin solution (10x)", "current": null, "decision": "add", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 19,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[18]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The main recipe explicitly adds 1 ml of stock 5980. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-19", "affected_local_fields": [], "source_amount": 1, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[17].concentration", "name": "L-Cysteine HCl x H2O", "current": {"value": "0.295566", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 20,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.295566,\n                        \"mmol_l\": 1.68284,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[19]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-20", "arithmetic_separate_from_quote": "Original 0.3 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 0.2955665024630541871921182266 g/L on the provider-declared stage volume; reported g_l is 0.295566. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "name": "L-Cysteine HCl x H2O", "current": {"value": "0.295566", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[17].concentration", "name": "L-Cysteine HCl x H2O", "current": {"value": "0.295566", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[17].concentration", "name": "L-Cysteine HCl x H2O", "current": {"value": "0.295566", "unit": "G_PER_L"}}], "source_amount": 0.3, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.295566, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[18].concentration", "name": "Na2S x 9 H2O", "current": {"value": "0.295566", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 21,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.295566,\n                        \"mmol_l\": 1.23059,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[20]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-21", "arithmetic_separate_from_quote": "Original 0.3 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 0.2955665024630541871921182266 g/L on the provider-declared stage volume; reported g_l is 0.295566. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "name": "Na2S x 9 H2O", "current": {"value": "0.295566", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[18].concentration", "name": "Na2S x 9 H2O", "current": {"value": "0.295566", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[18].concentration", "name": "Na2S x 9 H2O", "current": {"value": "0.295566", "unit": "G_PER_L"}}], "source_amount": 0.3, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.295566, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "source solution 1194 recipe[21] (not represented)", "name": "Distilled water", "current": null, "decision": "add", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 22,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[21]", "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1015 mL; water addition is not independent proof of measured final volume.", "evidence_id": "quantity-22", "affected_local_fields": [], "source_amount": 1000, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[19].concentration", "name": "Nitrilotriacetic acid", "current": {"value": "1.5", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[0]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-23", "arithmetic_separate_from_quote": "Original 1.5 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 1.5 g/L on the provider-declared stage volume; reported g_l is 1.5. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 1.5 g/L × 0.010 L / 1.015 L = 0.01477832512315270935960591133 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "name": "Nitrilotriacetic acid", "current": {"value": "1.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[19].concentration", "name": "Nitrilotriacetic acid", "current": {"value": "1.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[19].concentration", "name": "Nitrilotriacetic acid", "current": {"value": "1.5", "unit": "G_PER_L"}}], "source_amount": 1.5, "source_unit": "g", "source_attribute": null, "provider_g_l": 1.5, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[20].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "3", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[1]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-24", "arithmetic_separate_from_quote": "Original 3 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 3 g/L on the provider-declared stage volume; reported g_l is 3. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 3 g/L × 0.010 L / 1.015 L = 0.02955665024630541871921182266 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "3", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[20].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "3", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[20].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "3", "unit": "G_PER_L"}}], "source_amount": 3, "source_unit": "g", "source_attribute": null, "provider_g_l": 3, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[21].concentration", "name": "MnSO4 x H2O", "current": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.9583,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[2]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-25", "arithmetic_separate_from_quote": "Original 0.5 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.5 g/L on the provider-declared stage volume; reported g_l is 0.5. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.5 g/L × 0.010 L / 1.015 L = 0.004926108374384236453201970443 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "name": "MnSO4 x H2O", "current": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[21].concentration", "name": "MnSO4 x H2O", "current": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[21].concentration", "name": "MnSO4 x H2O", "current": {"value": "0.5", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.5, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[4].concentration", "name": "NaCl", "current": {"value": "7.89655", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[3]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-26", "arithmetic_separate_from_quote": "Original 1 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 1 g/L on the provider-declared stage volume; reported g_l is 1. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 1 g/L × 0.010 L / 1.015 L = 0.009852216748768472906403940887 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "name": "NaCl", "current": {"value": "7.89655", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[4].concentration", "name": "NaCl", "current": {"value": "7.89655", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[4].concentration", "name": "NaCl", "current": {"value": "7.89655", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "g", "source_attribute": null, "provider_g_l": 1, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[22].concentration", "name": "FeSO4 x 7 H2O", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[4]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-27", "arithmetic_separate_from_quote": "Original 0.1 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.1 g/L on the provider-declared stage volume; reported g_l is 0.1. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.1 g/L × 0.010 L / 1.015 L = 0.0009852216748768472906403940887 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "name": "FeSO4 x 7 H2O", "current": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[22].concentration", "name": "FeSO4 x 7 H2O", "current": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[22].concentration", "name": "FeSO4 x 7 H2O", "current": {"value": "0.1", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[23].concentration", "name": "CoSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 1.16132,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[5]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-28", "arithmetic_separate_from_quote": "Original 0.18 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.18 g/L on the provider-declared stage volume; reported g_l is 0.18. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.18 g/L × 0.010 L / 1.015 L = 0.001773399014778325123152709360 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "name": "CoSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[23].concentration", "name": "CoSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[23].concentration", "name": "CoSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}], "source_amount": 0.18, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.18, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[6].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.247783", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[6]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-29", "arithmetic_separate_from_quote": "Original 0.1 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.1 g/L on the provider-declared stage volume; reported g_l is 0.1. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.1 g/L × 0.010 L / 1.015 L = 0.0009852216748768472906403940887 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.247783", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[6].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.247783", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[6].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.247783", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[24].concentration", "name": "ZnSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.625954,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[7]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-30", "arithmetic_separate_from_quote": "Original 0.18 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.18 g/L on the provider-declared stage volume; reported g_l is 0.18. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.18 g/L × 0.010 L / 1.015 L = 0.001773399014778325123152709360 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "name": "ZnSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[24].concentration", "name": "ZnSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[24].concentration", "name": "ZnSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}], "source_amount": 0.18, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.18, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[25].concentration", "name": "CuSO4 x 5 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[8]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-31", "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.01 g/L × 0.010 L / 1.015 L = 0.00009852216748768472906403940887 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "name": "CuSO4 x 5 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[25].concentration", "name": "CuSO4 x 5 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[25].concentration", "name": "CuSO4 x 5 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.01, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[26].concentration", "name": "AlK(SO4)2 x 12 H2O", "current": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0421596,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[9]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-32", "arithmetic_separate_from_quote": "Original 0.02 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.02 g/L on the provider-declared stage volume; reported g_l is 0.02. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.02 g/L × 0.010 L / 1.015 L = 0.0001970443349753694581280788177 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "name": "AlK(SO4)2 x 12 H2O", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[26].concentration", "name": "AlK(SO4)2 x 12 H2O", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[26].concentration", "name": "AlK(SO4)2 x 12 H2O", "current": {"value": "0.02", "unit": "G_PER_L"}}], "source_amount": 0.02, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.02, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[27].concentration", "name": "H3BO3", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[10]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-33", "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.01 g/L × 0.010 L / 1.015 L = 0.00009852216748768472906403940887 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "name": "H3BO3", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[27].concentration", "name": "H3BO3", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[27].concentration", "name": "H3BO3", "current": {"value": "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.01, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[28].concentration", "name": "Na2MoO4 x 2 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[11]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-34", "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.01 g/L × 0.010 L / 1.015 L = 0.00009852216748768472906403940887 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "name": "Na2MoO4 x 2 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[28].concentration", "name": "Na2MoO4 x 2 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[28].concentration", "name": "Na2MoO4 x 2 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.01, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[8].concentration", "name": "NiCl2 x 6 H2O", "current": {"value": "0.030985222", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.231483,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[12]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-35", "arithmetic_separate_from_quote": "Original 0.03 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.03 g/L on the provider-declared stage volume; reported g_l is 0.03. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.03 g/L × 0.010 L / 1.015 L = 0.0002955665024630541871921182266 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "name": "NiCl2 x 6 H2O", "current": {"value": "0.030985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[8].concentration", "name": "NiCl2 x 6 H2O", "current": {"value": "0.030985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[8].concentration", "name": "NiCl2 x 6 H2O", "current": {"value": "0.030985222", "unit": "G_PER_L"}}], "source_amount": 0.03, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.03, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[29].concentration", "name": "Na2SeO3 x 5 H2O", "current": {"value": "0.0003", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\": 0.00114062,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[13]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-36", "arithmetic_separate_from_quote": "Original 0.3 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.0003 g/L on the provider-declared stage volume; reported g_l is 0.0003. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.0003 g/L × 0.010 L / 1.015 L = 0.000002955665024630541871921182266 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "name": "Na2SeO3 x 5 H2O", "current": {"value": "0.0003", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[29].concentration", "name": "Na2SeO3 x 5 H2O", "current": {"value": "0.0003", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[29].concentration", "name": "Na2SeO3 x 5 H2O", "current": {"value": "0.0003", "unit": "G_PER_L"}}], "source_amount": 0.3, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.0003, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[9].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004985222", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\": 0.00121267,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[14]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-37", "arithmetic_separate_from_quote": "Original 0.4 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.0004 g/L on the provider-declared stage volume; reported g_l is 0.0004. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.0004 g/L × 0.010 L / 1.015 L = 0.000003940886699507389162561576355 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[9].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[9].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004985222", "unit": "G_PER_L"}}], "source_amount": 0.4, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.0004, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "source solution 241 recipe[15] (not represented)", "name": "Distilled water", "current": null, "decision": "add", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[15]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume.", "evidence_id": "quantity-38", "affected_local_fields": [], "source_amount": 1000, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[30].concentration", "name": "Biotin", "current": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[0]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-39", "arithmetic_separate_from_quote": "Original 20 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.020 g/L on the provider-declared stage volume; reported g_l is 0.02. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.02 g/L × 0.001 L / 1.015 L = 0.00001970443349753694581280788177 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "name": "Biotin", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[30].concentration", "name": "Biotin", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[30].concentration", "name": "Biotin", "current": {"value": "0.02", "unit": "G_PER_L"}}], "source_amount": 20, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.02, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[31].concentration", "name": "Folic acid", "current": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[1]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-40", "arithmetic_separate_from_quote": "Original 20 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.020 g/L on the provider-declared stage volume; reported g_l is 0.02. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.02 g/L × 0.001 L / 1.015 L = 0.00001970443349753694581280788177 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "name": "Folic acid", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[31].concentration", "name": "Folic acid", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[31].concentration", "name": "Folic acid", "current": {"value": "0.02", "unit": "G_PER_L"}}], "source_amount": 20, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.02, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[32].concentration", "name": "Pyridoxine hydrochloride", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[2]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-41", "arithmetic_separate_from_quote": "Original 100 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.100 g/L on the provider-declared stage volume; reported g_l is 0.1. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.1 g/L × 0.001 L / 1.015 L = 0.00009852216748768472906403940887 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[32].concentration", "name": "Pyridoxine hydrochloride", "current": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[32].concentration", "name": "Pyridoxine hydrochloride", "current": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[32].concentration", "name": "Pyridoxine hydrochloride", "current": {"value": "0.1", "unit": "G_PER_L"}}], "source_amount": 100, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[33].concentration", "name": "Thiamine HCl", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[3]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-42", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.05 g/L × 0.001 L / 1.015 L = 0.00004926108374384236453201970443 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[33].concentration", "name": "Thiamine HCl", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[33].concentration", "name": "Thiamine HCl", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[33].concentration", "name": "Thiamine HCl", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[34].concentration", "name": "Riboflavin", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[4]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-43", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.05 g/L × 0.001 L / 1.015 L = 0.00004926108374384236453201970443 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[34].concentration", "name": "Riboflavin", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[34].concentration", "name": "Riboflavin", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[34].concentration", "name": "Riboflavin", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[35].concentration", "name": "Nicotinic acid", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[5]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-44", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.05 g/L × 0.001 L / 1.015 L = 0.00004926108374384236453201970443 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[35].concentration", "name": "Nicotinic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[35].concentration", "name": "Nicotinic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[35].concentration", "name": "Nicotinic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[36].concentration", "name": "Calcium D-(+)-pantothenate", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[6]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-45", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.05 g/L × 0.001 L / 1.015 L = 0.00004926108374384236453201970443 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[36].concentration", "name": "Calcium D-(+)-pantothenate", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[36].concentration", "name": "Calcium D-(+)-pantothenate", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[36].concentration", "name": "Calcium D-(+)-pantothenate", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[37].concentration", "name": "Vitamin B12", "current": {"value": "0.001", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[7]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-46", "arithmetic_separate_from_quote": "Original 1 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.001 g/L on the provider-declared stage volume; reported g_l is 0.001. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.001 g/L × 0.001 L / 1.015 L = 9.852216748768472906403940887E-7 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[37].concentration", "name": "Vitamin B12", "current": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[37].concentration", "name": "Vitamin B12", "current": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[37].concentration", "name": "Vitamin B12", "current": {"value": "0.001", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.001, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[38].concentration", "name": "p-Aminobenzoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[8]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-47", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.05 g/L × 0.001 L / 1.015 L = 0.00004926108374384236453201970443 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[38].concentration", "name": "p-Aminobenzoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[38].concentration", "name": "p-Aminobenzoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[38].concentration", "name": "p-Aminobenzoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[39].concentration", "name": "(DL)-alpha-Lipoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[9]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-48", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional receiving-medium contribution only: provider stock 0.05 g/L × 0.001 L / 1.015 L = 0.00004926108374384236453201970443 g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[39].concentration", "name": "(DL)-alpha-Lipoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "ingredients[39].concentration", "name": "(DL)-alpha-Lipoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "ingredients[39].concentration", "name": "(DL)-alpha-Lipoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "source solution 5980 recipe[10] (not represented)", "name": "Distilled water", "current": null, "decision": "add", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[10]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume.", "evidence_id": "quantity-49", "affected_local_fields": [], "source_amount": 1000, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "mineral stock KOH addition (not quantified)", "name": "mineral stock KOH addition (not quantified)", "current": null, "decision": "not_quantified", "source_key": "dsmz540", "source_quote": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust", "source_locator": "pages 1–2, relevant preparation paragraph", "preparation_stage": "mineral stock", "decision_rationale": "KOH is used to set pH 6.5 and then final stock pH 7.0. No fixed KOH mass or volume is specified; do not infer zero or a typical dose.", "evidence_id": "quantity-50"}, {"field_path": "later sterile anoxic stock volumes (not quantified)", "name": "later sterile anoxic stock volumes (not quantified)", "current": null, "decision": "not_quantified", "source_key": "dsmz540", "source_quote": "and autoclave. Add glucose, vitamins, cysteine and sulfide from sterile anoxic stock", "source_locator": "pages 1–2, relevant preparation paragraph", "preparation_stage": "main medium after autoclaving", "decision_rationale": "The named glucose, vitamin, cysteine and sulfide amounts remain explicit above; this preparation passage does not specify all later anoxic-stock volumes. They cannot be used to claim an independently measured final receiving volume.", "evidence_id": "quantity-51"}, {"field_path": "preparation_steps.initial_pH", "name": "Initial pH", "current": null, "decision": "add", "source_key": "dsmz540", "source_quote": "Add solid bicarbonate and equilibrate pH to 6.8 with 80% N2 and 20% CO2 gas mixture,", "source_locator": "page 1, main preparation sentence 2", "preparation_stage": "main preparation before dispensing", "decision_rationale": "Preserve the explicit initial pH 6.8 adjustment; it is separate from final complete-medium pH.", "evidence_id": "quantity-52"}, {"field_path": "ph_range", "name": "Complete-medium pH", "current": {"min": 6.8, "max": 7.0}, "decision": "evidence_only", "source_key": "dsmz540", "source_quote": "filtration. Adjust pH of complete medium to 6.8 - 7.0, if necessary.", "source_locator": "page 1, final main preparation sentence", "preparation_stage": "complete medium", "decision_rationale": "The existing 6.8–7.0 range matches the exact source and each owner; retain its complete-medium and if-necessary scope.", "evidence_id": "quantity-53"}, {"field_path": "preparation_steps.initial_gas", "name": "Initial gas composition", "current": null, "decision": "add", "source_key": "dsmz540", "source_quote": "sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.", "source_locator": "page 1, first preparation sentence", "preparation_stage": "initial anoxic preparation", "decision_rationale": "Restore the explicitly stated 80% N2 / 20% CO2 preparation atmosphere; it is not an organism incubation phenotype.", "evidence_id": "quantity-54"}, {"field_path": "preparation_steps.sparging_duration", "name": "Sparging duration", "current": null, "decision": "add", "source_key": "dsmz540", "source_quote": "sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.", "source_locator": "page 1, first preparation sentence", "preparation_stage": "initial anoxic preparation", "decision_rationale": "Restore the literal 30–45 min interval; do not replace the range by a midpoint.", "evidence_id": "quantity-55"}, {"field_path": "preparation_steps.addition_stock_gas", "name": "Gas for separately prepared stocks", "current": null, "decision": "add", "source_key": "dsmz540", "source_quote": "solutions prepared under 100% N2 gas atmosphere. Vitamins should be sterilized by", "source_locator": "page 1, later stock preparation sentence", "preparation_stage": "separately prepared anoxic additions", "decision_rationale": "The later glucose, vitamin, cysteine and sulfide stocks are prepared under 100% N2. Preserve this distinct stage and the following vitamin filtration instruction.", "evidence_id": "quantity-56"}]

### Claim-level source support and actual reference-check coverage

evidence: concern. Targets: CultureMech:005968.

Neither target nor either maintained owner contains claim-level ingredient amount evidence; the target reference diagnostic checked zero evidence references. Exact source URLs, original access times/hashes, literal quantity snippets and locators are supplied in this review. Add properly scoped evidence in a separate curation task, without fabricating evidence slots.

### Bounded biological claims and optional entities

scope: not_applicable. Targets: CultureMech:005968.

No reviewed layer asserts organism or strain identifiers, assemblies, DOI/PMID papers, growth outcomes or KG-Microbe matches. The SOURCE_DUPLICATE relationship is assessed separately and does not establish growth equivalence. The broad applications and source title do not justify adding organism claims.

## Findings

### f1: Stock strengths and direct contributions are combined as final-medium concentrations

major / open / confirmed; issue key: cm005968-stock-stage-collapse.

The source adds 10 mL of mineral stock and 1 mL of 10x vitamin stock, each defined separately per 1000 mL. The target and both owners omit those doses and store their component strengths directly. Four rows additionally sum direct and stock values: NaCl 7.89655, calcium chloride dihydrate 0.247783, nickel chloride hexahydrate 0.030985222 and sodium tungstate dihydrate 0.0004985222 g/L. These values do not represent the source preparation stages. The full 49-row source inventory and two unquantified preparation additions preserve every amount and basis; provider 1015 mL is not a measured final volume.

### f2: Nickel hydrate and sodium resazurin map to different supplied forms

major / open / confirmed; issue key: cm005968-salt-hydrate-grounding.

The explicit nickel chloride hexahydrate is grounded to anhydrous-form nickel dichloride, and sodium resazurin to neutral Resazurin. Canonical labels and current MIM-key correspondence pass but do not establish these supplied forms. No replacement ID is invented and no hydrate mass is converted with an anhydrous molecular weight.

### f3: The generated recipe omits source-specific anoxic preparation

major / open / confirmed; issue key: cm005968-anoxic-preparation-lost.

The target and KOMODO owner omit the preparation and filtration/autoclaving sequence retained in the DSMZ owner, while presenting Aerobic: Yes. Following those incomplete representations would not reproduce the source preparation. The missing protocol is specific and recoverable; a generic sterilization step or invented cycle would not resolve it.

### f4: Four inherited timestamps have invalid syntax or no timezone

minor / open / confirmed; issue key: cm005968-history-timezones.

The target and KOMODO owner each retain one malformed .fZ import timestamp and one timezone-naive resolver timestamp. The DSMZ owner history is valid and timezone-aware. Preserve the old history and distinguish its unknown timezone from source retrieval times.

## Recommended Actions And Acceptance Checks

### a1

Restore the two source-specific stock definitions and their addition doses in both maintained contributors; separate direct additions from stock components and retain original units/percentage attributes and explicit provider-volume limits. Attach narrow evidence to ingredients and root evidence for stock doses, then preview source-compatible regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Verify the exact salt/hydrate identities against authoritative terms and align primary and secondary mappings while retaining source masses and names. Leave genuinely unresolved replacements explicit.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Reconcile the KOMODO note as source catalog context and preserve the exact DSMZ preparation in the maintained representation, including gas atmospheres, sequencing, filtration and stage-specific pH. Ensure authorized regeneration retains the chosen source-supported protocol.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Document historical timestamp interpretation without rewriting append-only history; separately authorized future writer changes should emit valid timezone-aware UTC timestamps.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/acetitomaculum_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch015/141/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch015/141/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| source-catalog | /private/tmp/culturemech-review-work-batch015/source-preflight-bound/141/source-catalog.json; Complete bound per-record catalog, raw/text/metadata hashes and actual original capture times | context_only | [{"key": "komodoMediaList", "url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList", "status": 200, "accessed_at": "2026-10-19T23:42:38.189631Z", "sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a", "metadata_sha256": "5ae47834f48dba0f36513d02684ae6d3ea3da54369ea1af0816f5beed8ee4e9e", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/140/komodoMediaList.json"}, {"key": "dsmz540", "url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf", "status": 200, "accessed_at": "2026-10-21T09:46:50.018755Z", "sha256": "cd6c6ccfc802d539f0376010548c985fc6ce8ac4847ea3b2d7a8db172deef2e7", "metadata_sha256": "404aecc94a7630eefdbd68fed6015e745d30cb643f3a1fb5f4061a4e28eb852b", "content_limit": null, "reused_capture_from": null}, {"key": "mediadive540api", "url": "https://mediadive.dsmz.de/rest/medium/540", "status": 200, "accessed_at": "2026-10-21T09:46:48.818833Z", "sha256": "71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8", "metadata_sha256": "dc3a47da5ca6512bb64e331baad52abac9eb5a0716fb3d85f558cf62bbedae5b", "content_limit": null, "reused_capture_from": null}, {"key": "chebi131361", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361", "status": 200, "accessed_at": "2026-10-21T07:33:27.980786Z", "sha256": "643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10", "metadata_sha256": "138d55ceb95cbfe0acf7201bb4eae4ab07af0fe03c84508c2ef3938ecfc4b2ae", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi131361.json"}, {"key": "chebi133341", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_133341", "status": 200, "accessed_at": "2026-10-21T09:46:50.859176Z", "sha256": "c98da0c6eaa91e6310bb2bb611e829e756e5daf36c1091566dffdd927decad2c", "metadata_sha256": "7016ad1cc452cf4a2f46d83de6d6e72d9eef6cadd33652e82aff070f49a0646a", "content_limit": null, "reused_capture_from": null}, {"key": "chebi15940", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940", "status": 200, "accessed_at": "2026-10-20T06:55:11.874279Z", "sha256": "3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1", "metadata_sha256": "ccd1adbb48f9064f617fe0e1c711d9418783efece2365f0d809996f357056838", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15940.json"}, {"key": "chebi15956", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956", "status": 200, "accessed_at": "2026-10-21T08:42:30.425993Z", "sha256": "d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd", "metadata_sha256": "0c95f29d357c5632b7ecdd16e0abafbd370595935f299ff000aeb2c7292732cd", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15956.json"}, {"key": "chebi16494", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494", "status": 200, "accessed_at": "2026-10-20T06:55:13.001958Z", "sha256": "aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1", "metadata_sha256": "3892bef535e884d560fe3f958457da63e9f8827421ea13a7a0bc83bb2b85220a", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/129/chebi16494.json"}, {"key": "chebi17015", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015", "status": 200, "accessed_at": "2026-10-20T06:55:11.583596Z", "sha256": "f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4", "metadata_sha256": "5244e9ca4c3ee1f0d2b9dee9e0e441d575939d1d98f70e5143e087b070ff8691", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi17015.json"}, {"key": "chebi17154", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17154", "status": 200, "accessed_at": "2026-10-21T09:46:50.867358Z", "sha256": "45306ecefbab1f5ece64d269af2560e313330916a57d04fa168f19044dfe37d8", "metadata_sha256": "01f55abd61e5e36e372614f5798a00eb8fd821326b4c0e04af63c9c59835cce2", "content_limit": null, "reused_capture_from": null}, {"key": "chebi17268", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17268", "status": 200, "accessed_at": "2026-10-21T07:16:23.488883Z", "sha256": "0b0cce127edf288993722217ac5a9c05a0bb876b8c34a481b3a41a20ed847888", "metadata_sha256": "9d0cfc50ee2bb18ec4fee24c71d594fa5eeb4cc4f7017906675d48ca99b3ac6e", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch008-tail/078/chebi17268.json"}, {"key": "chebi17634", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634", "status": 200, "accessed_at": "2026-10-21T08:42:33.425023Z", "sha256": "d11b31a8e91c3fffe7744f612dab69cdb4e02f42068cd2eb1458acee4503a62f", "metadata_sha256": "823621e9d5c44510193f8576b9daa3c609d37e380edec45ffa6d3e071a6bbbc4", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/135/chebi17634.json"}, {"key": "chebi176843", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843", "status": 200, "accessed_at": "2026-10-21T08:17:26.997779Z", "sha256": "b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9", "metadata_sha256": "bc634d788a5dcfee20a97e574f01fc036d79198f4f352ed9a665c58b6a139c27", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi176843.json"}, {"key": "chebi22652", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_22652", "status": 200, "accessed_at": "2026-10-21T09:46:50.925101Z", "sha256": "c68de040add50ab599a1ba691b32fc29c32be018d9be69fe785bf045c681ba12", "metadata_sha256": "b35765127b999e4a6339858572d0e85da18044275115de6d672d3924276f8242", "content_limit": null, "reused_capture_from": null}, {"key": "chebi26710", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710", "status": 200, "accessed_at": "2026-10-21T08:42:42.219040Z", "sha256": "2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e", "metadata_sha256": "a5aa981220b7ff257c8fa376bc078c656fdb9441a2c751a80c2ee406aa299eb3", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi26710.json"}, {"key": "chebi27470", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470", "status": 200, "accessed_at": "2026-10-20T06:55:10.450814Z", "sha256": "fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f", "metadata_sha256": "555d29814a58871f010427bc65a64246287ef8f70ef7479fc990e91b7b994449", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi27470.json"}, {"key": "chebi30753", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753", "status": 200, "accessed_at": "2026-10-20T06:55:12.829785Z", "sha256": "97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a", "metadata_sha256": "41064c33af959c4414c4024ed69c380390cf92d289e4eecb77ead20db28b43eb", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi30753.json"}, {"key": "chebi30961", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961", "status": 200, "accessed_at": "2026-10-21T08:42:44.571163Z", "sha256": "f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d", "metadata_sha256": "995fa39c43445f662677b9f51c2fd4d3277e38c0e48a4132ba24cd0b288c2797", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi30961.json"}, {"key": "chebi31206", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206", "status": 200, "accessed_at": "2026-10-21T08:17:28.439407Z", "sha256": "ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76", "metadata_sha256": "b39788c1cff4fc2c0477e4b621c8361080ec6d810817c5cbf03469abeb0d1c5e", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi31206.json"}, {"key": "chebi31345", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345", "status": 200, "accessed_at": "2026-10-20T06:55:12.450283Z", "sha256": "56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d", "metadata_sha256": "d8032b0cee899225ed4bd68c612cdabf64005609adb65b9fe90bb6f8858ae717", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi31345.json"}, {"key": "chebi31440", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440", "status": 200, "accessed_at": "2026-10-21T08:17:28.489501Z", "sha256": "e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9", "metadata_sha256": "6529882a5af14272d6b6a6d84fb5d7491494ad5b39e77fd2e78c8976caae47c7", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi31440.json"}, {"key": "chebi31795", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795", "status": 200, "accessed_at": "2026-10-21T08:42:45.232212Z", "sha256": "45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb", "metadata_sha256": "b1c7b3fb9390c8507df21d5c6ebe5844d8aec7a45d9e4f06faa1fca81b1e734c", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/140/chebi31795.json"}, {"key": "chebi32139", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139", "status": 200, "accessed_at": "2026-10-21T07:16:24.226823Z", "sha256": "2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe", "metadata_sha256": "f0831ae485cbda8dad2d8fd86898a29b1ecc50a8b66baf746916b8c70550be12", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/135/chebi32139.json"}, {"key": "chebi32149", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149", "status": 200, "accessed_at": "2026-10-20T07:18:34.792120Z", "sha256": "49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8", "metadata_sha256": "cb6ee285a5c1cdd29b54e5703c2b09c5a8e40185b943bebaba219091a7139ff4", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-work-batch005/sources/chebi32149.json"}, {"key": "chebi32312", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312", "status": 200, "accessed_at": "2026-10-21T08:17:28.879505Z", "sha256": "eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9", "metadata_sha256": "10c5840f2d9d4bc7eead8c7932802d70dea909d22b84a3eae2db24decc771f7c", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi32312.json"}, {"key": "chebi32588", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588", "status": 200, "accessed_at": "2026-10-21T08:17:29.045588Z", "sha256": "536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411", "metadata_sha256": "84fd80bc5626e941e713cd7853594cd3fb8fe81cec73c96d5d59310a97899de8", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi32588.json"}, {"key": "chebi33118", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118", "status": 200, "accessed_at": "2026-10-21T08:17:29.364390Z", "sha256": "f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87", "metadata_sha256": "2923d04cbdf5a6902c6bf2c9e955ce632c93ae8e2434a471d14eda937843d042", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi33118.json"}, {"key": "chebi34887", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887", "status": 200, "accessed_at": "2026-10-21T08:04:44.093348Z", "sha256": "f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc", "metadata_sha256": "9705696a27f4729870b5b870d8c1444abc00c65d3d347612b84b85632b8cb1c4", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi34887.json"}, {"key": "chebi44557", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557", "status": 200, "accessed_at": "2026-10-21T08:46:15.250117Z", "sha256": "de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2", "metadata_sha256": "feed10fc8ed84d40251835261cafc8decb2a008053459a2690e5ef05886c80ff", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi44557.json"}, {"key": "chebi49105", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105", "status": 200, "accessed_at": "2026-10-20T06:55:10.911379Z", "sha256": "0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4", "metadata_sha256": "bd1e98656da4ad0ffa12b011265b26b5fe482f34339e7149bfd9d0c2e39fb7bf", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi49105.json"}, {"key": "chebi63036", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036", "status": 200, "accessed_at": "2026-10-21T08:17:29.666916Z", "sha256": "48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3", "metadata_sha256": "1843775fdea6d581cb66b25165bf6af2bd3a85c6fa50d2c5994a3286e78ba892", "content_limit": "Identity/provenance and exact identifier metadata only; no operational formulation or culture-procedure assessment.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/139/chebi63036.json"}, {"key": "chebi63939", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939", "status": 200, "accessed_at": "2026-10-20T06:55:09.796192Z", "sha256": "987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a", "metadata_sha256": "4c37e2dabf6db6e10b0fc6b772539f62bc384372f98ec49b4f201d976074d795", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi63939.json"}, {"key": "chebi75213", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213", "status": 200, "accessed_at": "2026-10-21T08:17:29.756647Z", "sha256": "b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083", "metadata_sha256": "a14596f3ed5f8fa7c6c875d74e2cbebe4e54bff8015fd47b6133aea3bc31f841", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/136/chebi75213.json"}, {"key": "chebi75836", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836", "status": 200, "accessed_at": "2026-10-20T06:55:07.038393Z", "sha256": "14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525", "metadata_sha256": "694f8da78dabe14df8225398e8ae7a89b065404f2537f45d7aa9d962a8ff52e3", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi75836.json"}, {"key": "chebi76209", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209", "status": 200, "accessed_at": "2026-10-20T06:55:04.847843Z", "sha256": "f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c", "metadata_sha256": "a0e76167a80501539f05f6062b393f9d766eb0ea5c3afa19dd19b9cb44bcb5af", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi76209.json"}, {"key": "chebi86158", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158", "status": 200, "accessed_at": "2026-10-21T08:17:30.011607Z", "sha256": "b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61", "metadata_sha256": "f54e4f9aa0c2ac289fe12c9c2b129c3920e4a7a840155eb643be8ebd96e24312", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi86158.json"}, {"key": "chebi86345", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345", "status": 200, "accessed_at": "2026-10-21T08:17:30.382026Z", "sha256": "08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133", "metadata_sha256": "830c202293bdd9b33596da6ee8d681936953e8f4d6dedfa5f7961b3849897fdf", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi86345.json"}, {"key": "chebi86364", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364", "status": 200, "accessed_at": "2026-10-21T07:33:35.036768Z", "sha256": "f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069", "metadata_sha256": "0c1118b30c6e2b638fac40a7713732248bc5cf56e75d08e4b240d24260227605", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/134/chebi86364.json"}, {"key": "chebi86465", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465", "status": 200, "accessed_at": "2026-10-20T06:55:08.054799Z", "sha256": "5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c", "metadata_sha256": "1db2987c153637737d264d3e81bf48b00324e32adc78942497f4ba3621f70f21", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi86465.json"}, {"key": "chebi8806", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806", "status": 200, "accessed_at": "2026-10-21T08:17:30.774007Z", "sha256": "e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5", "metadata_sha256": "d974cb479c2306995b3f56fd12b92afd92628806b24556d226c3cb7acc229a2c", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi8806.json"}, {"key": "chebi91244", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244", "status": 200, "accessed_at": "2026-10-20T06:55:07.079384Z", "sha256": "dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa", "metadata_sha256": "7bcc41c0e2d4ad81aab32a98f42a8d405cd5881fa4653a783906ef034b881014", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-work-batch004/sources/chebi91244.json"}, {"key": "chebi91248", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248", "status": 200, "accessed_at": "2026-10-21T08:42:32.136441Z", "sha256": "7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683", "metadata_sha256": "0cc7abb8217070f092c46ab0885d1eaa608a536610e8b15bca2336754018e9cf", "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/133/chebi91248.json"}] |
| dsmz540 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf; pages 1–2, entire main recipe and reproduced mineral/vitamin stock sections | supports | DSMZ 540 ACETITOMACULUM MEDIUM, two-page collection recipe. Both pages were inspected visually and in extracted text, including all main and stock rows and preparation paragraphs. The footer says ©2022 DSMZ; no individual authors or separately verified publication date are supplied. |
| mediadive540api | https://mediadive.dsmz.de/rest/medium/540; $.data.medium; $.data.solutions[0:3] | supports | Exact MediaDive medium 540 dataset response: main solution 1194, mineral stock 241 and vitamin stock 5980; complete amounts, units, percentage attributes, declared volumes and preparation. |
| komodoMediaList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; MediaList table row with first cell 540 | context_only | Exact row 540 names ACETITOMACULUM medium and links DSMZ Medium540.pdf. It gives pH 6.8–7.0 and the aerobic flag, but supplies no quantities or strain-growth evidence. |
| quantity-1 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[0] | supports | The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-2 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[1] | supports | The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-3 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[2] | supports | The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-4 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[3] | supports | The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-5 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[4] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-6 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[5] | supports | The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-7 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[6] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-8 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[7] | supports | The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-9 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[8] | supports | The main recipe explicitly adds 10 ml of stock 241. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution. |
| quantity-10 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[9] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-11 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[10] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-12 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[11] | supports | The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-13 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[12] | supports | The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-14 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[13] | supports | The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-15 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[14] | supports | The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-16 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[15] | supports | The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-17 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[16] | supports | The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-18 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[17] | supports | The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-19 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[18] | supports | The main recipe explicitly adds 1 ml of stock 5980. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution. |
| quantity-20 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[19] | supports | The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-21 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[20] | supports | The current value follows provider g_l on its declared 1015 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-22 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[0].recipe[21] | supports | Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1015 mL; water addition is not independent proof of measured final volume. |
| quantity-23 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[0] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-24 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[1] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-25 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[2] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-26 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[3] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-27 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[4] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-28 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[5] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-29 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[6] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-30 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[7] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-31 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[8] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-32 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[9] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-33 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[10] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-34 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[11] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-35 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[12] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-36 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[13] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-37 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[14] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-38 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[1].recipe[15] | supports | Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume. |
| quantity-39 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[2].recipe[0] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-40 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[2].recipe[1] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-41 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[2].recipe[2] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-42 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[2].recipe[3] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-43 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[2].recipe[4] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-44 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[2].recipe[5] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-45 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[2].recipe[6] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-46 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[2].recipe[7] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-47 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[2].recipe[8] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-48 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[2].recipe[9] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-49 | https://mediadive.dsmz.de/rest/medium/540; $.data.solutions[2].recipe[10] | supports | Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume. |
| quantity-50 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf; pages 1–2, relevant preparation paragraph | supports | KOH is used to set pH 6.5 and then final stock pH 7.0. No fixed KOH mass or volume is specified; do not infer zero or a typical dose. |
| quantity-51 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf; pages 1–2, relevant preparation paragraph | supports | The named glucose, vitamin, cysteine and sulfide amounts remain explicit above; this preparation passage does not specify all later anoxic-stock volumes. They cannot be used to claim an independently measured final receiving volume. |
| quantity-52 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf; page 1, main preparation sentence 2 | supports | Preserve the explicit initial pH 6.8 adjustment; it is separate from final complete-medium pH. |
| quantity-53 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf; page 1, final main preparation sentence | supports | The existing 6.8–7.0 range matches the exact source and each owner; retain its complete-medium and if-necessary scope. |
| quantity-54 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf; page 1, first preparation sentence | supports | Restore the explicitly stated 80% N2 / 20% CO2 preparation atmosphere; it is not an organism incubation phenotype. |
| quantity-55 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf; page 1, first preparation sentence | supports | Restore the literal 30–45 min interval; do not replace the range by a midpoint. |
| quantity-56 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf; page 1, later stock preparation sentence | supports | The later glucose, vitamin, cysteine and sulfide stocks are prepared under 100% N2. Preserve this distinct stage and the following vitamin filtration instruction. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0] | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; $._embedded.terms[0] | supports | CHEBI:32149 resolves to sodium sulfate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; $._embedded.terms[0] | supports | CHEBI:31206 resolves to ammonium chloride and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; $._embedded.terms[0] | supports | CHEBI:32588 resolves to potassium chloride and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0] | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; $._embedded.terms[0] | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0] | supports | CHEBI:86158 resolves to calcium chloride dihydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0] | supports | CHEBI:34887 resolves to nickel dichloride and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; $._embedded.terms[0] | supports | CHEBI:63939 resolves to sodium tungstate dihydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi22652 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_22652; $._embedded.terms[0] | supports | CHEBI:22652 resolves to ascorbic acid and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi17268 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17268; $._embedded.terms[0] | supports | CHEBI:17268 resolves to myo-inositol and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi17154 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17154; $._embedded.terms[0] | supports | CHEBI:17154 resolves to nicotinamide and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi133341 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_133341; $._embedded.terms[0] | supports | CHEBI:133341 resolves to choline chloride and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; $._embedded.terms[0] | supports | CHEBI:8806 resolves to Resazurin and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; $._embedded.terms[0] | supports | CHEBI:32139 resolves to sodium hydrogencarbonate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; $._embedded.terms[0] | supports | CHEBI:17634 resolves to D-glucose and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; $._embedded.terms[0] | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; $._embedded.terms[0] | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; $._embedded.terms[0] | supports | CHEBI:44557 resolves to nitrilotriacetic acid and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0] | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; $._embedded.terms[0] | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; $._embedded.terms[0] | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; $._embedded.terms[0] | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; $._embedded.terms[0] | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; $._embedded.terms[0] | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; $._embedded.terms[0] | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0] | supports | CHEBI:33118 resolves to boric acid and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0] | supports | CHEBI:75213 resolves to sodium molybdate dihydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; $._embedded.terms[0] | supports | CHEBI:131361 resolves to disodium selenite pentahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
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
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned snapshot; exact MAPPED/preferred_term rows for asserted CHEBI keys and exact legacy-key lookup | supports | {"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count": 9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id", "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"}, "counts": {"target": {"ingredient_instances": 40, "primary_CHEBI_instances": 39, "secondary_current_asserted_instances": 37, "secondary_current_verified_instances": 37, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.5, "secondary_verified_percent": 92.5}, "owner-0": {"ingredient_instances": 40, "primary_CHEBI_instances": 39, "secondary_current_asserted_instances": 37, "secondary_current_verified_instances": 37, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.5, "secondary_verified_percent": 92.5}, "owner-1": {"ingredient_instances": 40, "primary_CHEBI_instances": 39, "secondary_current_asserted_instances": 37, "secondary_current_verified_instances": 37, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.5, "secondary_verified_percent": 92.5}}, "instances": [{"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[0]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "canonical_label": "potassium dihydrogen phosphate", "label_equal": true, "definition": ["A potassium salt in which dihydrogen phosphate(1−) is the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"], "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"], "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]}, "synonyms": ["MKP", "Monopotassium dihydrogen phosphate", "Monopotassium monophosphate", "Monopotassium orthophosphate", "Monopotassium phosphate", "Orthophosphoric acid, monopotassium salt", "Phosphoric acid, monopotassium salt", "Phosphoric acid, potassium salt (1:1)", "Potassium acid phosphate", "Potassium dihydrogen orthophosphate", "Potassium dihydrogen phosphate", "Potassium phosphate monobasic", "Potassium phosphate", "Sorensen's potassium phosphate", "potassium dihydrogen phosphate", "potassium dihydrogen phosphate"], "secondary": {"asserted": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "exact_current_rows": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[1]", "name": "Na2SO4", "primary": {"id": "CHEBI:32149", "label": "sodium sulfate"}, "canonical_label": "sodium sulfate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7757-82-6", "kegg.compound:C13199", "kegg.drug:D01732"], "generalized_empirical_formula": ["2Na.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32149"], "inchi_key_string": ["PMZURENOXWZQFD-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2Na.H2O4S/c;;1-5(2,3)4/h;;(H2,1,2,3,4)/q2*+1;/p-2"], "mass": ["142.043"], "monoisotopic_mass": ["141.93127"], "smiles_string": ["O=S(=O)([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2SO4", "Natriumsulfat", "Sodium sulfate", "disodium sulfate", "disodium sulphate", "salt cake", "sodium sulfate", "sodium sulfate", "sodium sulfate, anhydrous", "sodium sulphate"], "secondary": {"asserted": {"id": "CHEBI:32149", "label": "sodium sulfate"}, "exact_current_rows": [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[2]", "name": "NH4Cl", "primary": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "canonical_label": "ammonium chloride", "label_equal": true, "definition": ["An inorganic chloride having ammonium as the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:12125-02-9", "gmelin:10120", "kegg.compound:C12538", "kegg.drug:D01139", "wikipedia.en:Ammonium_Chloride"], "generalized_empirical_formula": ["Cl.H4N"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31206"], "inchi_key_string": ["NLXLAEXVIDQMFP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/ClH.H3N/h1H;1H3"], "mass": ["53.492"], "monoisotopic_mass": ["53.00323"], "smiles_string": ["[Cl-].[H][N+]([H])([H])[H]"]}, "synonyms": ["Ammonium chloride", "Ammoniumchlorid", "NH4Cl", "[NH4]Cl", "ammonium chloride", "ammonium chloride", "azanium chloride"], "secondary": {"asserted": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "exact_current_rows": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[3]", "name": "KCl", "primary": {"id": "CHEBI:32588", "label": "potassium chloride"}, "canonical_label": "potassium chloride", "label_equal": true, "definition": ["A metal chloride salt with a K(+) counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7447-40-7", "drugbank:DB00761", "kegg.drug:D02060", "metacyc.compound:KCL", "molbase:881", "reaxys:3534978", "wikipedia.en:Potassium_Chloride"], "generalized_empirical_formula": ["Cl.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32588"], "inchi_key_string": ["WCUXLLCKKVVCTQ-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "monoisotopic_mass": ["73.93256"], "smiles_string": ["[Cl-].[K+]"]}, "synonyms": ["KCl", "Kaliumchlorid", "Kaon-Cl 10", "Klor-con", "Klotrix", "Monopotassium chloride", "[KCl]", "muriate of potash", "potassium chloride", "potassium chloride", "sylvite"], "secondary": {"asserted": {"id": "CHEBI:32588", "label": "potassium chloride"}, "exact_current_rows": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[4]", "name": "NaCl", "primary": {"id": "CHEBI:26710", "label": "sodium chloride"}, "canonical_label": "sodium chloride", "label_equal": true, "definition": ["An inorganic chloride salt having sodium(1+) as the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula": ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string": ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]}, "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "secondary": {"asserted": {"id": "CHEBI:26710", "label": "sodium chloride"}, "exact_current_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[5]", "name": "MgCl2 x 6 H2O", "primary": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "canonical_label": "magnesium dichloride hexahydrate", "label_equal": true, "definition": ["A hydrate that is the hexahydrate form of magnesium dichloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7791-18-6", "kegg.drug:D04834", "pubmed:24831644", "pubmed:25148974", "pubmed:25430969", "reaxys:11343754"], "generalized_empirical_formula": ["2Cl.6H2O.Mg"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86345"], "inchi_key_string": ["DHRRIBDTHFBPNG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass": ["203.301"], "monoisotopic_mass": ["201.98614"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}, "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate", "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"], "secondary": {"asserted": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "exact_current_rows": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[6]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "canonical_label": "calcium chloride dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of calcium chloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8", "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"], "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass": ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}, "synonyms": ["CaCl2.2H2O", "Calcium chloride hydrate", "Calcium chloride", "calcium chloride--water (1/2)", "calcium chloride--water (1/2)", "calcium dichloride dihydrate"], "secondary": {"asserted": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "exact_current_rows": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[7]", "name": "Yeast extract"}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[8]", "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "canonical_label": "nickel dichloride", "label_equal": true, "definition": ["A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7718-54-9", "kegg.compound:C14711", "pubmed:11739495", "pubmed:12603851", "pubmed:21928331", "pubmed:23179351", "pubmed:23622879", "pubmed:23702803", "pubmed:23735035", "pubmed:7671317", "reaxys:3902827", "reaxys:8128171", "wikipedia.en:Nickel_dichloride"], "generalized_empirical_formula": ["Cl2Ni"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:34887"], "inchi_key_string": ["QMMRZOWCJAIUJA-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"], "mass": ["129.599"], "monoisotopic_mass": ["127.87305"], "smiles_string": ["[Cl][Ni][Cl]"]}, "synonyms": ["NiCl2", "Nickel chloride", "Nickel(II) chloride", "[NiCl2]", "nickel dichloride", "nickel dichloride", "nickel(2+) chloride", "nickel(2+) chloride", "nickel(II) chloride", "nickel(II) chloride", "nickelous chloride"], "secondary": {"asserted": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "exact_current_rows": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[9]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "canonical_label": "sodium tungstate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines to nitrones"], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10213-10-2", "reaxys:13157884", "wikipedia.en:Sodium_tungstate"], "generalized_empirical_formula": ["2H2O.2Na.O4W"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63939"], "inchi_key_string": ["WPZFLQRLSGVIAA-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.2H2O.4O.W/h;;2*1H2;;;;;/q2*+1;;;;;2*-1;"], "mass": ["329.846"], "monoisotopic_mass": ["329.93126"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]}, "synonyms": ["Na2WO4.2H2O", "Tungstic acid, sodium salt, dihydrate", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium orthotungstate dihydrate", "sodium tungstate(VI) dihydrate"], "secondary": {"asserted": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "exact_current_rows": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[10]", "name": "Ascorbic acid", "primary": {"id": "CHEBI:22652", "label": "ascorbic acid"}, "canonical_label": "ascorbic acid", "label_equal": true, "definition": [], "annotations": {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:22652"]}, "synonyms": [], "secondary": {"asserted": {"id": "CHEBI:22652", "label": "ascorbic acid"}, "exact_current_rows": [{"label": "Ascorbic acid", "match_type": "preferred_term", "identifier": "CHEBI:22652", "preferred_term": "Ascorbic acid", "ontology_id": "CHEBI:22652", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[11]", "name": "Myo-inositol", "primary": {"id": "CHEBI:17268", "label": "myo-inositol"}, "canonical_label": "myo-inositol", "label_equal": true, "definition": ["An inositol having &lt;i&gt;myo&lt;/i&gt;- configuration."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:87-89-8", "drugbank:DB03106", "drugcentral:1444", "gmelin:82918", "hmdb:HMDB0000211", "kegg.compound:C00137", "kegg.drug:D08079", "knapsack:C00001164", "metacyc.compound:MYO-INOSITOL", "pdb-ccd:INS", "pubmed:11034685", "pubmed:11244303", "pubmed:11323092", "pubmed:11772411", "pubmed:12478879", "pubmed:12832083", "pubmed:14583919", "pubmed:14681857", "pubmed:15181167", "pubmed:15295080", "pubmed:15558078", "pubmed:16410747", "pubmed:1694860", "pubmed:17439666", "pubmed:17722064", "pubmed:18650262", "pubmed:18854045", "pubmed:19097871", "pubmed:19383710", "pubmed:22285975", "pubmed:22461977", "pubmed:22517104", "pubmed:838172", "reaxys:1907329", "wikipedia.en:Inositol"], "generalized_empirical_formula": ["C6H12O6"], "has_alternative_id": ["CHEBI:10601", "CHEBI:12826", "CHEBI:12831", "CHEBI:25451", "CHEBI:43559"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17268"], "inchi_key_string": ["CDAISMWEOUEBRE-GPIVLXJGSA-N"], "inchi_string": ["InChI=1S/C6H12O6/c7-1-2(8)4(10)6(12)5(11)3(1)9/h1-12H/t1-,2-,3-,4+,5-,6-"], "mass": ["180.156"], "monoisotopic_mass": ["180.06339"], "smiles_string": ["O[C@H]1[C@H](O)[C@@H](O)[C@H](O)[C@@H](O)[C@H]1O"]}, "synonyms": ["(1r,2R,3S,4s,5R,6S)-cyclohexane-1,2,3,4,5,6-hexol", "1,2,3,4,5,6-HEXAHYDROXY-CYCLOHEXANE", "1,2,3,5/4,6-cyclohexanehexol", "1D-myo-Inositol", "1L-myo-Inositol", "Bios I", "Cyclohexitol", "D-myo-Inositol", "Dambose", "Inositol", "Ins", "L-myo-Inositol", "Meat sugar", "Myoinositol", "cis-1,2,3,5-trans-4,6-cyclohexanehexol", "i-inositol", "inosite", "meso-Inositol", "myo-Inositol", "myo-Inositol", "myo-inositol", "myo-inositol"], "secondary": {"asserted": {"id": "CHEBI:17268", "label": "myo-inositol"}, "exact_current_rows": [{"label": "myo-Inositol", "match_type": "preferred_term", "identifier": "CHEBI:17268", "preferred_term": "myo-Inositol", "ontology_id": "CHEBI:17268", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[12]", "name": "Niacinamide", "primary": {"id": "CHEBI:17154", "label": "nicotinamide"}, "canonical_label": "nicotinamide", "label_equal": true, "definition": ["A pyridinecarboxamide that is pyridine in which the hydrogen at position 3 is replaced by a carboxamide group."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:98-92-0", "drugbank:DB02701", "drugcentral:1906", "foodb.food:FDB012485", "gmelin:3336", "hmdb:HMDB0001406", "kegg.compound:C00153", "kegg.drug:D00036", "knapsack:C00000209", "lincs.smallmolecule:LSM-5428", "metacyc.compound:NIACINAMIDE", "patent:US2904552", "patent:US2993051", "pdb-ccd:NCA", "pubmed:10884473", "pubmed:11355130", "pubmed:11814060", "pubmed:12014919", "pubmed:12487919", "pubmed:12519385", "pubmed:12709297", "pubmed:12782109", "pubmed:12890690", "pubmed:14729974", "pubmed:14757966", "pubmed:14871431", "pubmed:15497767", "pubmed:15563975", "pubmed:15780941", "pubmed:15807725", "pubmed:15834926", "pubmed:15995937", "pubmed:16029679", "pubmed:16209160", "pubmed:16596767", "pubmed:16766489", "pubmed:16871361", "pubmed:17021258", "pubmed:17129213", "pubmed:18234191", "pubmed:18316796", "pubmed:18368629", "pubmed:18373238", "pubmed:18389009", "pubmed:18514428", "pubmed:18930755", "pubmed:18987186", "pubmed:19212411", "pubmed:19539713", "pubmed:19544437", "pubmed:2026685", "pubmed:21503886", "pubmed:21891976", "pubmed:21918528", "pubmed:21926578", "pubmed:22067079", "pubmed:22160932", "pubmed:22207684", "pubmed:22232263", "pubmed:22281243", "pubmed:22359146", "pubmed:22361740", "pubmed:22407380", "pubmed:22456321", "pubmed:22536229", "pubmed:22543086", "pubmed:22626821", "pubmed:22699421", "pubmed:22709272", "pubmed:22763693", "pubmed:22770225", "pubmed:23016598", "pubmed:23028781", "pubmed:23043891", "pubmed:23047329", "pubmed:24027187", "pubmed:24077178", "pubmed:24559077", "pubmed:24635573", "pubmed:25504347", "pubmed:25561219", "pubmed:31710686", "pubmed:32249824", "pubmed:33196157", "pubmed:33471934", "pubmed:8620561", "pubmed:8767167", "pubmed:9518388", "reaxys:383619", "wikipedia.en:Nicotinamide"], "generalized_empirical_formula": ["C6H6N2O"], "has_alternative_id": ["CHEBI:14645", "CHEBI:25521", "CHEBI:44258", "CHEBI:7556"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17154"], "inchi_key_string": ["DFPAKSUCGFBDDF-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H6N2O/c7-6(9)5-2-1-3-8-4-5/h1-4H,(H2,7,9)"], "mass": ["122.127"], "monoisotopic_mass": ["122.04801"], "smiles_string": ["NC(=O)c1cccnc1"]}, "synonyms": ["3-carbamoylpyridine", "3-pyridinecarboxamide", "Niacinamide", "Nicotinamid", "Nicotinsaeureamid", "Nikotinamid", "Nikotinsaeureamid", "Vitamin PP", "beta-pyridinecarboxamide", "m-(aminocarbonyl)pyridine", "niacin", "niamide", "nicotinamida", "nicotinamide", "nicotinamidum", "nicotine acid amide", "nicotine amide", "nicotinic acid amide", "nicotinic amide", "nicotylamide", "pyridine-3-carboxamide", "pyridine-3-carboxamide", "pyridine-3-carboxylic acid amide", "vitamin B3"], "secondary": {"asserted": {"id": "CHEBI:17154", "label": "nicotinamide"}, "exact_current_rows": [{"label": "Nicotinamide", "match_type": "preferred_term", "identifier": "CHEBI:17154", "preferred_term": "Nicotinamide", "ontology_id": "CHEBI:17154", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[13]", "name": "Choline chloride", "primary": {"id": "CHEBI:133341", "label": "choline chloride"}, "canonical_label": "choline chloride", "label_equal": true, "definition": ["A quaternary ammonium salt with choline cation and chloride anion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:67-48-1", "ppdb:161", "pubmed:12962717", "pubmed:17596274", "pubmed:20396712", "pubmed:24905385", "pubmed:25037344", "pubmed:6196640", "pubmed:8047569", "reaxys:3563126", "vsdb:161", "wikipedia.en:Choline_chloride"], "generalized_empirical_formula": ["C5H14NO.Cl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:133341"], "inchi_key_string": ["SGMZJAMFUVOLNK-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C5H14NO.ClH/c1-6(2,3)4-5-7;/h7H,4-5H2,1-3H3;1H/q+1;/p-1"], "mass": ["139.626"], "monoisotopic_mass": ["139.07639"], "smiles_string": ["C[N+](C)(C)CCO.[Cl-]"]}, "synonyms": ["(2-Hydroxyethyl)trimethylammonium chloride", "(beta-Hydroxyethyl)trimethylammonium chloride", "2-Hydroxy-N,N,N,-trimethylethanaminium chloride", "2-hydroxy-N,N,N-trimethylethanaminium chloride", "2-hydroxy-N,N,N-trimethylethanaminium chloride", "Bilineurin chloride", "Biocolina", "Biocoline", "Chloride de choline", "Chlorure de choline", "Choline chlorhydrate", "Choline hydrochloride", "Cholini chloridum", "Cholinium chloride", "Cloruro de colina", "Hepacholine", "Lipotril", "Luridin chloride", "Paresan", "Trimethyl(2-hydroxyethyl)ammonium chloride", "choline chloride"], "secondary": {"asserted": {"id": "CHEBI:133341", "label": "choline chloride"}, "exact_current_rows": [{"label": "Choline chloride", "match_type": "preferred_term", "identifier": "CHEBI:133341", "preferred_term": "Choline chloride", "ontology_id": "CHEBI:133341", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[14]", "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806", "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3", "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"], "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]}, "synonyms": ["Resazurin"]}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[15]", "name": "NaHCO3", "primary": {"id": "CHEBI:32139", "label": "sodium hydrogencarbonate"}, "canonical_label": "sodium hydrogencarbonate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:144-55-8", "drugbank:DB01390", "kegg.compound:C12603", "kegg.drug:D01203", "ppdb:2873", "wikipedia.en:Sodium_Bicarbonate"], "generalized_empirical_formula": ["CHO3.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32139"], "inchi_key_string": ["UIIMBOGNXHQVGW-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/CH2O3.Na/c2-1(3)4;/h(H2,2,3,4);/q;+1/p-1"], "mass": ["84.006"], "monoisotopic_mass": ["83.98234"], "smiles_string": ["O=C([O-])O.[Na+]"]}, "synonyms": ["E 500", "E-500", "E500", "NaHCO3", "Natriumhydrogenkarbonat", "Sodium bicarbonate", "Sodium hydrogencarbonate", "baking soda", "bicarbonate of soda", "carbonic acid monosodium salt", "sodium acid carbonate", "sodium hydrogen carbonate", "sodium hydrogencarbonate", "sodium hydrogencarbonate"], "secondary": {"asserted": {"id": "CHEBI:32139", "label": "sodium hydrogencarbonate"}, "exact_current_rows": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[16]", "name": "D-Glucose", "primary": {"id": "CHEBI:17634", "label": "D-glucose"}, "canonical_label": "D-glucose", "label_equal": true, "definition": ["A glucose with &lt;small&gt;D&lt;/small&gt;-configuration."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:50-99-7"], "generalized_empirical_formula": ["C6H12O6"], "has_alternative_id": ["CHEBI:12965", "CHEBI:20999"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17634"], "mass": ["180.156"], "monoisotopic_mass": ["180.06339"]}, "synonyms": ["D(+)-glucose", "D-(+)-glucose", "D-gluco-hexose", "D-gluco-hexose", "D-glucose", "D-glucose", "Traubenzucker", "dextrose", "grape sugar"], "secondary": {"asserted": {"id": "CHEBI:17634", "label": "D-glucose"}, "exact_current_rows": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[17]", "name": "L-Cysteine HCl x H2O", "primary": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride hydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of &lt;small&gt;L&lt;/small&gt;-cysteine hydrochloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326", "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"], "inchi_key_string": ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"], "mass": ["175.637"], "monoisotopic_mass": ["175.00699"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]}, "synonyms": ["(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride monohydrate", "Cysteine hydrochloride", "L-Cysteine monohydrate monochloride", "L-cysteine hydrochloride monohydrate", "L-cysteine hydrochloride--water (1/1)", "L-cysteine hydrochloride--water (1/1)"], "secondary": {"asserted": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "exact_current_rows": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[18]", "name": "Na2S x 9 H2O", "primary": {"id": "CHEBI:76209", "label": "sodium sulfide nonahydrate"}, "canonical_label": "sodium sulfide nonahydrate", "label_equal": true, "definition": ["A hydrate with formula Na&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;S·9H&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;O."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:1313-84-4", "kegg.drug:D09001", "pubmed:19810706", "reaxys:14636099"], "generalized_empirical_formula": ["9H2O.2Na.S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:76209"], "inchi_key_string": ["ZGHLCBJZQLNUAZ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.9H2O.S/h;;9*1H2;/q2*+1;;;;;;;;;;-2"], "mass": ["240.182"], "monoisotopic_mass": ["240.04669"], "smiles_string": ["O.O.O.O.O.O.O.O.O.[Na+].[Na+].[S-2]"]}, "synonyms": ["Na2S.9H2O", "Sodium sulfide (USP)", "disodium sulfide nonahydrate", "disodium sulfide--water (1/9)", "disodium sulfide--water (1/9)", "sodium monosulfide nonahydrate", "sodium monosulfide.9H2O", "sodium sulfide.9H2O"], "secondary": {"asserted": {"id": "CHEBI:76209", "label": "sodium sulfide nonahydrate"}, "exact_current_rows": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[19]", "name": "Nitrilotriacetic acid", "primary": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "canonical_label": "nitrilotriacetic acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1710776", "cas:139-13-9", "drugbank:DB03040", "gmelin:3726", "kegg.compound:C14695", "pdb-ccd:NTA"], "generalized_empirical_formula": ["C6H9NO6"], "has_alternative_id": ["CHEBI:34889", "CHEBI:44555"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:44557"], "inchi_key_string": ["MGFYIUFZLHCRTH-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"], "mass": ["191.139"], "monoisotopic_mass": ["191.04299"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]}, "synonyms": ["Complexon I", "H3nta", "Komplexon I", "N(CH2-COOH)3", "N,N-bis(carboxymethyl)glycine", "N,N-bis(carboxymethyl)glycine", "NITRILOTRIACETIC ACID", "NTA", "Nitrilotriacetate", "Nitrilotriacetic acid", "Nitrilotriessigsaeure", "Triglycollamic acid", "Trilon A", "alpha,alpha',alpha''-trimethylaminetricarboxylic acid", "nitrilo-2,2',2''-triacetic acid", "tri(carboxymethyl)amine", "triglycine"], "secondary": {"asserted": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "exact_current_rows": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[20]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "canonical_label": "magnesium sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505", "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222", "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"], "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "exact_current_rows": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[21]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "canonical_label": "manganese(II) sulfate monohydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of manganese(II) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-96-5", "kegg.drug:D04854", "pubmed:26097037", "reaxys:13153017", "wikipedia.en:Manganese(II)_sulfate"], "generalized_empirical_formula": ["H2O.Mn.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86364"], "inchi_key_string": ["ISPYRSDWRDQNSW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mn.H2O4S.H2O/c;1-5(2,3)4;/h;(H2,1,2,3,4);1H2/q+2;;/p-2"], "mass": ["169.016"], "monoisotopic_mass": ["168.90034"], "smiles_string": ["O.O=S(=O)([O-])[O-].[Mn+2]"]}, "synonyms": ["Manganese sulfate hydrate", "Manganese sulfate monohydrate", "Manganese sulfate", "Manganous sulfate monohydrate", "MnSO4.H2O", "manganese(2+) sulfate monohydrate", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulphate monohydrate", "manganese(II) sulphate monohydrate"], "secondary": {"asserted": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "exact_current_rows": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[22]", "name": "FeSO4 x 7 H2O", "primary": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "canonical_label": "iron(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used)."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]}, "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O", "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"], "secondary": {"asserted": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[23]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "canonical_label": "cobalt(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of cobalt(2+) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10026-24-1", "pubmed:10504146", "pubmed:12187935", "pubmed:12209163", "pubmed:12579202", "pubmed:12948248", "pubmed:2227161", "pubmed:24359163", "pubmed:25896363", "wikipedia.en:Cobalt(II)_sulfate"], "generalized_empirical_formula": ["Co.7H2O.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91244"], "inchi_key_string": ["MEYVLGVRTYSQHI-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Co.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["281.101"], "monoisotopic_mass": ["280.95888"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Co+2]"]}, "synonyms": ["Cobalt monosulfate heptahydrate", "cobalt sulfate heptahydrate", "cobalt(2+) sulfate--water (1/7)", "cobalt(2+) sulfate--water (1/7)", "cobalt(II) sulfate heptahydrate", "cobaltous sulfate heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[24]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "canonical_label": "zinc sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of zinc sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7446-20-0", "gmelin:47216", "kegg.drug:D01081", "wikipedia.en:Zinc_Sulfate"], "generalized_empirical_formula": ["7H2O.O4S.Zn"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32312"], "inchi_key_string": ["RZLVQBNCHSJZPX-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/H2O4S.7H2O.Zn/c1-5(2,3)4;;;;;;;;/h(H2,1,2,3,4);7*1H2;/q;;;;;;;;+2/p-2"], "mass": ["287.558"], "monoisotopic_mass": ["285.95482"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Zn+2]"]}, "synonyms": ["Zinc sulfate", "ZnSO4.7H2O", "zinc sulfate (1:1) heptahydrate", "zinc sulfate heptahydrate (1:1:7)", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate--water (1/7)", "zinc(2+) sulfate--water (1/7)"], "secondary": {"asserted": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "exact_current_rows": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[25]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "canonical_label": "copper(II) sulfate pentahydrate", "label_equal": true, "definition": ["The pentahydrate of copper(2+) sulfate. A bright blue crystalline solid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-99-8", "kegg.drug:D03613", "pubmed:11407502", "pubmed:12209195", "pubmed:12484481", "pubmed:15040745", "pubmed:15607472", "pubmed:15824790", "pubmed:19346702", "pubmed:2002460", "pubmed:20132934", "pubmed:2913309", "pubmed:3351847", "pubmed:7615984", "pubmed:8878264", "pubmed:9521458", "pubmed:9776063", "reaxys:16499970", "wikipedia.en:Copper(II)_sulfate"], "generalized_empirical_formula": ["Cu.5H2O.O4S"], "has_alternative_id": ["CHEBI:121741", "CHEBI:370227"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31440"], "inchi_key_string": ["JZCCFEFSEZPSOG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Cu.H2O4S.5H2O/c;1-5(2,3)4;;;;;/h;(H2,1,2,3,4);5*1H2/q+2;;;;;;/p-2"], "mass": ["249.684"], "monoisotopic_mass": ["248.93415"], "smiles_string": ["O=S(=O)([O-])[O-].[Cu+2].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H]"]}, "synonyms": ["CuSO4.5H2O", "Cupric sulfate", "copper sulphate(5.H2O)", "copper(2+) sulfate (1:1) pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate--water (1/5)", "copper(2+) sulfate--water (1/5)", "copper(II) sulfate, pentahydrate", "cupric sulfate pentahydrate"], "secondary": {"asserted": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "exact_current_rows": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[26]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "canonical_label": "potassium aluminium sulfate dodecahydrate", "label_equal": true, "definition": ["A hydrate resulting from the the formal combination of anhydrous potassium aluminium sulfate with 12 mol eq. of water."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7784-24-9", "reaxys:14851666", "wikipedia.en:Potassium_alum"], "generalized_empirical_formula": ["Al.12H2O.K.2O4S"], "has_alternative_id": ["CHEBI:31192"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86465"], "inchi_key_string": ["GNHOJBNSNUXZQA-UHFFFAOYSA-J"], "inchi_string": ["InChI=1S/Al.K.2H2O4S.12H2O/c;;2*1-5(2,3)4;;;;;;;;;;;;/h;;2*(H2,1,2,3,4);12*1H2/q+3;+1;;;;;;;;;;;;;;/p-4"], "mass": ["474.386"], "monoisotopic_mass": ["473.97548"], "smiles_string": ["O.O.O.O.O.O.O.O.O.O.O.O.O=S(=O)([O-])[O-].O=S(=O)([O-])[O-].[Al+3].[K+]"]}, "synonyms": ["AlK(SO4)2.12H2O", "Aluminum potassium disulfate dodecahydrate", "Aluminum potassium sulfate dodecahydrate", "Kalinite", "Potash alum dodecahydrate", "Potassium alum dodecahydrate", "Potassium aluminum disulfate dodecahydrate", "aluminium potassium sulfate--water (1/12)", "aluminium potassium sulfate--water (1/12)"], "secondary": {"asserted": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "exact_current_rows": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[27]", "name": "H3BO3", "primary": {"id": "CHEBI:33118", "label": "boric acid"}, "canonical_label": "boric acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["bpdb:2136", "cas:10043-35-3", "cas:11113-50-1", "drugcentral:3035", "gmelin:1585", "kegg.compound:C12486", "kegg.drug:D01089", "molbase:1644", "pdb-ccd:BO3", "ppdb:2136"], "generalized_empirical_formula": ["H3BO3"], "has_alternative_id": ["CHEBI:22911", "CHEBI:31299", "CHEBI:41248"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:33118"], "inchi_key_string": ["KGBXLFKZBHKPEV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"], "mass": ["61.833"], "monoisotopic_mass": ["62.01752"], "smiles_string": ["[H]OB(O[H])O[H]"]}, "synonyms": ["B(OH)3", "BORIC ACID", "Boric acid", "H3BO3", "[B(OH)3]", "boric acid", "boron trihydroxide", "orthoboric acid", "trihydroxidoboron", "trihydroxidoboron"], "secondary": {"asserted": {"id": "CHEBI:33118", "label": "boric acid"}, "exact_current_rows": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[28]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "canonical_label": "sodium molybdate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium molybdate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10102-40-6", "pubmed:20645132", "pubmed:20813395", "pubmed:22663766", "pubmed:3382795", "reaxys:19032996", "wikipedia.en:Sodium_molybdate"], "generalized_empirical_formula": ["2H2O.MoO4.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75213"], "inchi_key_string": ["FDEIWTXVNPKYDL-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/Mo.2Na.2H2O.4O/h;;;2*1H2;;;;/q;2*+1;;;;;2*-1"], "mass": ["241.946"], "monoisotopic_mass": ["243.88573"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]}, "synonyms": ["Disodium molybdate dihydrate", "Molybdic acid, disodium salt, dihydrate", "Na2MoO4.2H2O", "Sodium molybdate(VI) dihydrate", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium orthomolybdate dihydrate"], "secondary": {"asserted": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "exact_current_rows": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[29]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "canonical_label": "disodium selenite pentahydrate", "label_equal": true, "definition": ["A hydrate that is the pentahydrate form of disodium selenite."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:26970-82-1", "pubmed:15259772", "pubmed:15559373", "pubmed:16126997", "pubmed:17873396", "pubmed:24479345", "pubmed:24716537", "reaxys:14666014", "wikipedia.en:Sodium_selenite"], "generalized_empirical_formula": ["5H2O.2Na.O3Se"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131361"], "inchi_key_string": ["TUANAMBRHOLYTH-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"], "mass": ["263.012"], "monoisotopic_mass": ["263.93363"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2SeO3.5H2O", "Selenious acid disodium salt, pentahydrate", "Sodium selenite pentahydrate", "disodium selenite hydrate", "sodium selenite hydrate", "sodium selenite--water (1/5)", "sodium selenite--water (1/5)"], "secondary": {"asserted": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "exact_current_rows": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[30]", "name": "Biotin", "primary": {"id": "CHEBI:15956", "label": "biotin"}, "canonical_label": "biotin", "label_equal": true, "definition": ["An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:58-85-5", "chemspider:149962", "drugbank:DB00121", "drugcentral:373", "foodb.food:FDB014510", "gmelin:1918703", "hmdb:HMDB0000030", "kegg.compound:C00120", "kegg.drug:D00029", "knapsack:C00000756", "lincs.smallmolecule:LSM-3994", "metacyc.compound:BIOTIN", "pdb-ccd:BTN", "pmc:PMC8089577", "pubmed:10064317", "pubmed:10215065", "pubmed:10577274", "pubmed:11435506", "pubmed:11481419", "pubmed:11800048", "pubmed:12055344", "pubmed:12070309", "pubmed:12603856", "pubmed:12803839", "pubmed:15012185", "pubmed:15202718", "pubmed:15272000", "pubmed:15690449", "pubmed:15863846", "pubmed:15899401", "pubmed:15992684", "pubmed:16011464", "pubmed:16195795", "pubmed:16419467", "pubmed:16676358", "pubmed:16677798", "pubmed:16704206", "pubmed:16769720", "pubmed:17297119", "pubmed:1814646", "pubmed:18202531", "pubmed:18452485", "pubmed:18509457", "pubmed:19212411", "pubmed:19319844", "pubmed:19727438", "pubmed:19928962", "pubmed:20967359", "pubmed:20974274", "pubmed:2100006", "pubmed:21248194", "pubmed:21356565", "pubmed:21373679", "pubmed:21596550", "pubmed:21871906", "pubmed:25515858", "pubmed:33346513", "pubmed:33461365", "pubmed:34077272", "pubmed:8333586", "pubmed:8750932", "pubmed:9022537", "pubmed:9038855", "pubmed:9094878", "pubmed:9164991", "pubmed:9176832", "pubmed:9371938", "pubmed:9416479", "reaxys:86838", "wikipedia.en:Biotin"], "generalized_empirical_formula": ["C10H16N2O3S"], "has_alternative_id": ["CHEBI:13905", "CHEBI:22882", "CHEBI:22884", "CHEBI:3108", "CHEBI:41236"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15956"], "inchi_key_string": ["YBJHBAHKTGYVGT-ZKWXMUAHSA-N"], "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"], "mass": ["244.316"], "monoisotopic_mass": ["244.08816"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]}, "synonyms": ["(+)-cis-Hexahydro-2-oxo-1H-thieno[3,4]imidazole-4-valeric acid", "(3aS,4S,6aR)-Hexahydro-2-oxo-1H-thieno[3,4-d]imidazole-4-valeric acid", "5-(2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl)pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "BIOTIN", "Coenzyme R", "D-(+)-biotin", "D-Biotin", "Vitamin H", "biotin", "biotina", "biotine", "biotinum", "cis-(+)-Tetrahydro-2-oxothieno[3,4]imidazoline-4-valeric acid", "cis-Hexahydro-2-oxo-1H-thieno(3,4)imidazole-4-valeric acid", "cis-Tetrahydro-2-oxothieno(3,4-d)imidazoline-4-valeric acid", "vitamin B7"], "secondary": {"asserted": {"id": "CHEBI:15956", "label": "biotin"}, "exact_current_rows": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[31]", "name": "Folic acid", "primary": {"id": "CHEBI:27470", "label": "folic acid"}, "canonical_label": "folic acid", "label_equal": true, "definition": ["An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND606960789", "cas:59-30-3", "chemspider:5815", "drugbank:DB00158", "drugcentral:1231", "foodb.food:FDB014504", "hmdb:HMDB0000121", "kegg.compound:C00504", "kegg.drug:D00070", "knapsack:C00001539", "lincs.smallmolecule:LSM-5355", "metacyc.compound:CPD-12826", "pdb-ccd:FOL", "pubmed:10138938", "pubmed:10897644", "pubmed:10958818", "pubmed:11261364", "pubmed:11451208", "pubmed:11959400", "pubmed:14387833", "pubmed:15321809", "pubmed:15523939", "pubmed:15754725", "pubmed:15797531", "pubmed:15797685", "pubmed:15831910", "pubmed:15990733", "pubmed:16093404", "pubmed:16277678", "pubmed:16380297", "pubmed:16871332", "pubmed:17784727", "pubmed:18788725", "pubmed:19121630", "pubmed:19335717", "pubmed:19355913", "pubmed:24650098", "pubmed:33624660", "pubmed:33965562", "pubmed:33968971", "pubmed:34207319", "pubmed:34219855", "pubmed:7738698", "pubmed:8235383", "pubmed:9040515", "pubmed:9420019", "pubmed:9565830", "pubmed:9683174", "pubmed:9781393", "pubmed:9808640", "pubmed:9808641", "reaxys:100781", "wikipedia.en:Folic_Acid"], "generalized_empirical_formula": ["C19H19N7O6"], "has_alternative_id": ["CHEBI:24075", "CHEBI:42610", "CHEBI:5140", "CHEBI:569217"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:27470"], "inchi_key_string": ["OVBPIULPVIDEAO-LBPRGKRZSA-N"], "inchi_string": ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"], "mass": ["441.404"], "monoisotopic_mass": ["441.13968"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]}, "synonyms": ["(2S)-2-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzamido)pentanedioic acid", "Acfol", "Folate", "Folicet", "Folsaeure", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-[(4-{[(2-amino-4-oxo-1,4-dihydropteridin-6-yl)methyl]amino}phenyl)carbonyl]-L-glutamic acid", "N-pteroyl-L-glutamic acid", "PGA", "PteGlu", "acide folique", "acido folico", "acidum folicum", "folic acid", "pteroyl-L-glutamic acid", "pteroyl-L-monoglutamic acid", "pteroylglutamic acid", "pteroylmonoglutamic acid", "vitamin B11", "vitamin B9", "vitamin Bc", "vitamin Be", "vitamin M"], "secondary": {"asserted": {"id": "CHEBI:27470", "label": "folic acid"}, "exact_current_rows": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[32]", "name": "Pyridoxine hydrochloride", "primary": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "canonical_label": "pyridoxine hydrochloride", "label_equal": true, "definition": ["The hydrochloride salt of pyridoxine."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND500675659", "beilstein:3632435", "cas:58-56-0", "drugbank:DBSALT000151", "foodb.food:FDB000575", "gmelin:1067921", "kegg.drug:D02179", "pubmed:15098856", "pubmed:17416572", "pubmed:17891511", "pubmed:18243627", "pubmed:19481898", "pubmed:20645279", "pubmed:21781646", "pubmed:24421551", "pubmed:27468034", "pubmed:28095734", "pubmed:32460509", "pubmed:33209152", "pubmed:33936292", "pubmed:34140989"], "generalized_empirical_formula": ["C8H11NO3.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30961"], "inchi_key_string": ["ZUFQODAHGAHPFQ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H11NO3.ClH/c1-5-8(12)7(4-11)6(3-10)2-9-5;/h2,10-12H,3-4H2,1H3;1H"], "mass": ["205.641"], "monoisotopic_mass": ["205.05057"], "smiles_string": ["Cc1ncc(CO)c(CO)c1O.Cl"]}, "synonyms": ["2-methyl-3-hydroxy-4,5-bis(hydroxymethyl)pyridine hydrochloride", "3-hydroxy-4,5-dimethylol-alpha-picoline hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "5-hydroxy-6-methyl-3,4-pyridinedimethanol hydrochloride", "pyridoxol hydrochloride", "vitamin B6 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "exact_current_rows": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[33]", "name": "Thiamine HCl", "primary": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "canonical_label": "thiamine hydrochloride", "label_equal": true, "definition": ["A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND605711145", "agr:IND606057536", "beilstein:3642937", "beilstein:3851771", "cas:67-03-8", "chemspider:5967", "drugbank:DBSALT000205", "foodb.food:FDB008416", "gmelin:31154", "gmelin:691133", "kegg.drug:D02094", "pubmed:11548854", "pubmed:12224421", "pubmed:21212548", "pubmed:22305197", "pubmed:24399744", "pubmed:25977858", "pubmed:26616989", "pubmed:27163892", "pubmed:28763984", "pubmed:28784494", "pubmed:30131156", "pubmed:31270735", "pubmed:31664290", "pubmed:32009117", "pubmed:32562525", "pubmed:32824791", "reaxys:17124533"], "generalized_empirical_formula": ["C12H17N4OS.Cl.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:49105"], "inchi_key_string": ["DPJRMOMPQZCRJU-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C12H17N4OS.2ClH/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H/q+1;;/p-1"], "mass": ["337.276"], "monoisotopic_mass": ["336.05784"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1.Cl.[Cl-]"]}, "synonyms": ["3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "thiamin dichloride", "thiamin hydrochloride", "thiamine HCl", "thiamine chloride hydrochloride", "thiamine dichloride", "thiamine(2+) dichloride", "thiaminium chloride hydrochloride", "vitamin B1 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "exact_current_rows": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[34]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015", "label": "riboflavin"}, "canonical_label": "riboflavin", "label_equal": true, "definition": ["&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:83-88-5", "chemspider:431981", "drugbank:DB00140", "drugcentral:2834", "foodb.food:FDB012160", "hmdb:HMDB0000244", "kegg.compound:C00255", "kegg.drug:D00050", "knapsack:C00001552", "lincs.smallmolecule:LSM-4084", "metacyc.compound:RIBOFLAVIN", "patent:US2807611", "patent:US2876169", "pdb-ccd:RBF", "pubmed:10566553", "pubmed:11399071", "pubmed:11606856", "pubmed:12083520", "pubmed:12354259", "pubmed:12927541", "pubmed:14963913", "pubmed:16273338", "pubmed:16460756", "pubmed:16658098", "pubmed:182198", "pubmed:18832377", "pubmed:19169240", "pubmed:19212411", "pubmed:19854891", "pubmed:22770225", "pubmed:2369885", "pubmed:23818044", "pubmed:24643482", "pubmed:24816110", "pubmed:25108762", "pubmed:25468971", "pubmed:25887755", "pubmed:2631092", "pubmed:29937405", "pubmed:3142982", "pubmed:33154451", "pubmed:33304888", "pubmed:33886098", "pubmed:33892358", "pubmed:34156642", "pubmed:3592624", "pubmed:3878498", "pubmed:4019261", "pubmed:6475825", "pubmed:6546833", "pubmed:6650303", "pubmed:7101408", "pubmed:7883462", "pubmed:8487103", "pubmed:8604671", "pubmed:8678471", "pubmed:8976642", "pubmed:9184778", "pubmed:9808225", "pubmed:9874201", "reaxys:97831", "wikipedia.en:Riboflavin"], "generalized_empirical_formula": ["C17H20N4O6"], "has_alternative_id": ["CHEBI:15044", "CHEBI:27299", "CHEBI:45214", "CHEBI:529204", "CHEBI:8843"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17015"], "inchi_key_string": ["AUNGANRZJHBGPY-SCRDCRAPSA-N"], "inchi_string": ["InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23)14(25)12(24)6-22)15-13(18-9)16(26)20-17(27)19-15/h3-4,11-12,14,22-25H,5-6H2,1-2H3,(H,20,26,27)/t11-,12+,14-/m0/s1"], "mass": ["376.369"], "monoisotopic_mass": ["376.13828"], "smiles_string": ["Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)CO)c2cc1C"]}, "synonyms": ["1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol", "5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "6,7-dimethyl-9-D-ribitylisoalloxazine", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine", "7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-ribitylisoalloxazine", "Aqua-Flave", "Beflavin", "Beflavine", "Bisulase", "Dermadram", "E101", "Fiboflavin", "Flavaxin", "Flavin Bb", "Flaxain", "Hyflavin", "Vitamin B2", "lactoflavin", "riboflavin (vit B2)", "riboflavin", "riboflavina", "riboflavine", "riboflavinum", "vitamin B2", "vitamin G", "vitasan B2"], "secondary": {"asserted": {"id": "CHEBI:17015", "label": "riboflavin"}, "exact_current_rows": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[35]", "name": "Nicotinic acid", "primary": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "canonical_label": "nicotinic acid", "label_equal": true, "definition": ["A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND607088605", "cas:59-67-6", "chemspider:913", "drugbank:DB00627", "drugcentral:2835", "foodb.food:FDB001014", "gmelin:3340", "hmdb:HMDB0001488", "kegg.compound:C00253", "kegg.drug:D00049", "knapsack:C00000208", "lincs.smallmolecule:LSM-4676", "metacyc.compound:NIACINE", "pdb-ccd:NIO", "pubmed:10540864", "pubmed:113218", "pubmed:12563315", "pubmed:12789870", "pubmed:135660", "pubmed:14550884", "pubmed:15037193", "pubmed:15183629", "pubmed:15205990", "pubmed:15311728", "pubmed:15627518", "pubmed:15651982", "pubmed:16018787", "pubmed:16172771", "pubmed:16322787", "pubmed:16400392", "pubmed:16449845", "pubmed:16767301", "pubmed:16877271", "pubmed:16945375", "pubmed:18037924", "pubmed:182198", "pubmed:186078", "pubmed:18993152", "pubmed:18996527", "pubmed:19369827", "pubmed:19592242", "pubmed:19678716", "pubmed:19779335", "pubmed:20979384", "pubmed:21632263", "pubmed:22116693", "pubmed:22155410", "pubmed:22229411", "pubmed:22366213", "pubmed:22458880", "pubmed:22770225", "pubmed:24029555", "pubmed:24568240", "pubmed:24675661", "pubmed:24848081", "pubmed:24975217", "pubmed:25040591", "pubmed:25241762", "pubmed:25429652", "pubmed:32954525", "pubmed:33273654", "pubmed:33932650", "pubmed:34066686", "pubmed:34085526", "pubmed:34117670", "pubmed:4033386", "pubmed:4259917", "pubmed:582105", "pubmed:699281", "pubmed:7217784", "pubmed:7581845", "pubmed:8306147", "pubmed:8423912", "pubmed:8679452", "pubmed:9107536", "reaxys:109591", "wikipedia.en:Niacin"], "generalized_empirical_formula": ["C6H5NO2"], "has_alternative_id": ["CHEBI:25538", "CHEBI:44319", "CHEBI:7559"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15940"], "inchi_key_string": ["PVNIIMVLHYAWGP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"], "mass": ["123.111"], "monoisotopic_mass": ["123.03203"], "smiles_string": ["O=C(O)c1cccnc1"]}, "synonyms": ["3-Pyridylcarboxylic acid", "3-carboxylpyridine", "3-carboxypyridine", "3-pyridinecarboxylic acid", "NICOTINIC ACID", "NICOTINIC ACID", "Niacin", "Niacor", "Niaspan", "Nicotinic acid", "Nicotinic acid", "Nicotinsaure", "Nikotinsaeure", "P.P. factor", "PP factor", "acide nicotinique", "acido nicotinico", "acidum nicotinicum", "anti-pellagra vitamin", "beta-pyridinecarboxylic acid", "m-pyridinecarboxylic acid", "nicotinic acid", "nicotinic acid", "pellagra preventive factor", "pyridine-3-carboxylic acid", "pyridine-3-carboxylic acid", "pyridine-beta-carboxylic acid", "pyridine-carboxylique-3", "vitamin B3"], "secondary": {"asserted": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "exact_current_rows": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[36]", "name": "Calcium D-(+)-pantothenate", "primary": {"id": "CHEBI:31345", "label": "Calcium pantothenate"}, "canonical_label": "Calcium pantothenate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:137-08-6", "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278", "pubmed:20553011", "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula": ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"], "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"], "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]}, "synonyms": ["Calcium pantotenate", "Calcium pantothenate", "Calcium pantothenate, d-", "Calpan", "D-ca pantothenate", "D-calcium pantothenate", "NSC-36292", "Pantholin", "Pantothenic acid (as calcium)", "Pantothenic acid calcium salt", "Vitamin b5, calcium salt", "pantotenato de calcio", "pantothenate de calcium"]}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[37]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843", "label": "vitamin B12"}, "canonical_label": "vitamin B12", "label_equal": true, "definition": ["Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives)."], "annotations": {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:176843"]}, "synonyms": ["vitamin B-12", "vitamin B12 vitamer", "vitamin B12 vitamers", "vitamin B12", "vitamins B12"], "secondary": {"asserted": {"id": "CHEBI:176843", "label": "vitamin B12"}, "exact_current_rows": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[38]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "canonical_label": "4-aminobenzoic acid", "label_equal": true, "definition": ["An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:150-13-0", "drugbank:DB02362", "drugcentral:2049", "ecmdb:ECMDB01392", "gmelin:50150", "hmdb:HMDB0001392", "kegg.compound:C00568", "kegg.drug:D02456", "knapsack:C00001401", "pdb-ccd:PAB", "pubmed:12039592", "pubmed:14745019", "pubmed:15115392", "pubmed:1527790", "pubmed:16290145", "pubmed:17149871", "pubmed:17743450", "pubmed:17800214", "pubmed:19469519", "pubmed:22767283", "pubmed:22994574", "pubmed:23063996", "pubmed:23084339", "pubmed:23144588", "pubmed:23471007", "pubmed:3599019", "pubmed:3820215", "pubmed:3950915", "pubmed:8411009", "pubmed:9406595", "reaxys:471605", "wikipedia.en:4-Aminobenzoic_acid", "ymdb:YMDB00493"], "generalized_empirical_formula": ["C7H7NO2"], "has_alternative_id": ["CHEBI:113372", "CHEBI:1783", "CHEBI:20315", "CHEBI:44778"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30753"], "inchi_key_string": ["ALYNCZNDIQEVRV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"], "mass": ["137.138"], "monoisotopic_mass": ["137.04768"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]}, "synonyms": ["1-Amino-4-carboxybenzene", "4-AMINOBENZOIC ACID", "4-AMINOBENZOIC ACID", "4-Amino-benzoic acid", "4-Aminobenzoesaeure", "4-Aminobenzoic acid", "4-Aminobenzoic acid", "4-Carboxyaniline", "4-Carboxyphenylamine", "4-aminobenzoic acid", "4-aminobenzoic acid", "ABEE", "PABA", "gamma-Aminobenzoic acid", "gamma-aminobenzoic acid", "p-Aminobenzoesaeure", "p-aminobenzoic acid", "p-carboxyaniline", "p-carboxyphenylamine", "para-aminobenzoic acid"], "secondary": {"asserted": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "exact_current_rows": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[39]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id": "CHEBI:16494", "label": "lipoic acid"}, "canonical_label": "lipoic acid", "label_equal": true, "definition": ["A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:122410", "cas:62-46-4", "drugbank:DB00166", "drugcentral:4732", "ecmdb:ECMDB01451", "gmelin:720915", "kegg.compound:C00725", "kegg.drug:D00086", "pubmed:15328413", "pubmed:7519986", "pubmed:7548757", "reaxys:81853", "wikipedia.en:Lipoic_acid", "ymdb:YMDB00334"], "generalized_empirical_formula": ["C8H14O2S2"], "has_alternative_id": ["CHEBI:146958", "CHEBI:25058", "CHEBI:6492"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16494"], "inchi_key_string": ["AGBQKNBQESQNJD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H14O2S2/c9-8(10)4-2-1-3-7-5-6-11-12-7/h7H,1-6H2,(H,9,10)"], "mass": ["206.332"], "monoisotopic_mass": ["206.04352"], "smiles_string": ["O=C(O)CCCCC1CCSS1"]}, "synonyms": ["1,2-dithiolane-3-pentanoic acid", "1,2-dithiolane-3-valeric acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)valeric acid", "5-(dithiolan-3-yl)valeric acid", "5-[3-(1,2-dithiolanyl)]pentanoic acid", "6,8-thioctic acid", "6,8-thiotic acid", "6-thioctic acid", "6-thiotic acid", "Acetate-replacing factor", "Biletan", "Lipoic acid", "Thioctansaeure", "Thioctic acid", "Thioctsaeure", "Thioktsaeure", "alpha-Lipoic acid", "alpha-Liponsaeure", "alpha-lipoic acid", "liponic acid"], "secondary": {"asserted": {"id": "CHEBI:16494", "label": "lipoic acid"}, "exact_current_rows": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[0]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "canonical_label": "potassium dihydrogen phosphate", "label_equal": true, "definition": ["A potassium salt in which dihydrogen phosphate(1−) is the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"], "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"], "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]}, "synonyms": ["MKP", "Monopotassium dihydrogen phosphate", "Monopotassium monophosphate", "Monopotassium orthophosphate", "Monopotassium phosphate", "Orthophosphoric acid, monopotassium salt", "Phosphoric acid, monopotassium salt", "Phosphoric acid, potassium salt (1:1)", "Potassium acid phosphate", "Potassium dihydrogen orthophosphate", "Potassium dihydrogen phosphate", "Potassium phosphate monobasic", "Potassium phosphate", "Sorensen's potassium phosphate", "potassium dihydrogen phosphate", "potassium dihydrogen phosphate"], "secondary": {"asserted": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "exact_current_rows": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[1]", "name": "Na2SO4", "primary": {"id": "CHEBI:32149", "label": "sodium sulfate"}, "canonical_label": "sodium sulfate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7757-82-6", "kegg.compound:C13199", "kegg.drug:D01732"], "generalized_empirical_formula": ["2Na.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32149"], "inchi_key_string": ["PMZURENOXWZQFD-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2Na.H2O4S/c;;1-5(2,3)4/h;;(H2,1,2,3,4)/q2*+1;/p-2"], "mass": ["142.043"], "monoisotopic_mass": ["141.93127"], "smiles_string": ["O=S(=O)([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2SO4", "Natriumsulfat", "Sodium sulfate", "disodium sulfate", "disodium sulphate", "salt cake", "sodium sulfate", "sodium sulfate", "sodium sulfate, anhydrous", "sodium sulphate"], "secondary": {"asserted": {"id": "CHEBI:32149", "label": "sodium sulfate"}, "exact_current_rows": [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[2]", "name": "NH4Cl", "primary": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "canonical_label": "ammonium chloride", "label_equal": true, "definition": ["An inorganic chloride having ammonium as the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:12125-02-9", "gmelin:10120", "kegg.compound:C12538", "kegg.drug:D01139", "wikipedia.en:Ammonium_Chloride"], "generalized_empirical_formula": ["Cl.H4N"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31206"], "inchi_key_string": ["NLXLAEXVIDQMFP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/ClH.H3N/h1H;1H3"], "mass": ["53.492"], "monoisotopic_mass": ["53.00323"], "smiles_string": ["[Cl-].[H][N+]([H])([H])[H]"]}, "synonyms": ["Ammonium chloride", "Ammoniumchlorid", "NH4Cl", "[NH4]Cl", "ammonium chloride", "ammonium chloride", "azanium chloride"], "secondary": {"asserted": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "exact_current_rows": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[3]", "name": "KCl", "primary": {"id": "CHEBI:32588", "label": "potassium chloride"}, "canonical_label": "potassium chloride", "label_equal": true, "definition": ["A metal chloride salt with a K(+) counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7447-40-7", "drugbank:DB00761", "kegg.drug:D02060", "metacyc.compound:KCL", "molbase:881", "reaxys:3534978", "wikipedia.en:Potassium_Chloride"], "generalized_empirical_formula": ["Cl.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32588"], "inchi_key_string": ["WCUXLLCKKVVCTQ-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "monoisotopic_mass": ["73.93256"], "smiles_string": ["[Cl-].[K+]"]}, "synonyms": ["KCl", "Kaliumchlorid", "Kaon-Cl 10", "Klor-con", "Klotrix", "Monopotassium chloride", "[KCl]", "muriate of potash", "potassium chloride", "potassium chloride", "sylvite"], "secondary": {"asserted": {"id": "CHEBI:32588", "label": "potassium chloride"}, "exact_current_rows": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[4]", "name": "NaCl", "primary": {"id": "CHEBI:26710", "label": "sodium chloride"}, "canonical_label": "sodium chloride", "label_equal": true, "definition": ["An inorganic chloride salt having sodium(1+) as the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula": ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string": ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]}, "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "secondary": {"asserted": {"id": "CHEBI:26710", "label": "sodium chloride"}, "exact_current_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[5]", "name": "MgCl2 x 6 H2O", "primary": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "canonical_label": "magnesium dichloride hexahydrate", "label_equal": true, "definition": ["A hydrate that is the hexahydrate form of magnesium dichloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7791-18-6", "kegg.drug:D04834", "pubmed:24831644", "pubmed:25148974", "pubmed:25430969", "reaxys:11343754"], "generalized_empirical_formula": ["2Cl.6H2O.Mg"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86345"], "inchi_key_string": ["DHRRIBDTHFBPNG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass": ["203.301"], "monoisotopic_mass": ["201.98614"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}, "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate", "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"], "secondary": {"asserted": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "exact_current_rows": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[6]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "canonical_label": "calcium chloride dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of calcium chloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8", "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"], "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass": ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}, "synonyms": ["CaCl2.2H2O", "Calcium chloride hydrate", "Calcium chloride", "calcium chloride--water (1/2)", "calcium chloride--water (1/2)", "calcium dichloride dihydrate"], "secondary": {"asserted": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "exact_current_rows": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[7]", "name": "Yeast extract"}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[8]", "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "canonical_label": "nickel dichloride", "label_equal": true, "definition": ["A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7718-54-9", "kegg.compound:C14711", "pubmed:11739495", "pubmed:12603851", "pubmed:21928331", "pubmed:23179351", "pubmed:23622879", "pubmed:23702803", "pubmed:23735035", "pubmed:7671317", "reaxys:3902827", "reaxys:8128171", "wikipedia.en:Nickel_dichloride"], "generalized_empirical_formula": ["Cl2Ni"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:34887"], "inchi_key_string": ["QMMRZOWCJAIUJA-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"], "mass": ["129.599"], "monoisotopic_mass": ["127.87305"], "smiles_string": ["[Cl][Ni][Cl]"]}, "synonyms": ["NiCl2", "Nickel chloride", "Nickel(II) chloride", "[NiCl2]", "nickel dichloride", "nickel dichloride", "nickel(2+) chloride", "nickel(2+) chloride", "nickel(II) chloride", "nickel(II) chloride", "nickelous chloride"], "secondary": {"asserted": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "exact_current_rows": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[9]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "canonical_label": "sodium tungstate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines to nitrones"], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10213-10-2", "reaxys:13157884", "wikipedia.en:Sodium_tungstate"], "generalized_empirical_formula": ["2H2O.2Na.O4W"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63939"], "inchi_key_string": ["WPZFLQRLSGVIAA-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.2H2O.4O.W/h;;2*1H2;;;;;/q2*+1;;;;;2*-1;"], "mass": ["329.846"], "monoisotopic_mass": ["329.93126"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]}, "synonyms": ["Na2WO4.2H2O", "Tungstic acid, sodium salt, dihydrate", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium orthotungstate dihydrate", "sodium tungstate(VI) dihydrate"], "secondary": {"asserted": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "exact_current_rows": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[10]", "name": "Ascorbic acid", "primary": {"id": "CHEBI:22652", "label": "ascorbic acid"}, "canonical_label": "ascorbic acid", "label_equal": true, "definition": [], "annotations": {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:22652"]}, "synonyms": [], "secondary": {"asserted": {"id": "CHEBI:22652", "label": "ascorbic acid"}, "exact_current_rows": [{"label": "Ascorbic acid", "match_type": "preferred_term", "identifier": "CHEBI:22652", "preferred_term": "Ascorbic acid", "ontology_id": "CHEBI:22652", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[11]", "name": "Myo-inositol", "primary": {"id": "CHEBI:17268", "label": "myo-inositol"}, "canonical_label": "myo-inositol", "label_equal": true, "definition": ["An inositol having &lt;i&gt;myo&lt;/i&gt;- configuration."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:87-89-8", "drugbank:DB03106", "drugcentral:1444", "gmelin:82918", "hmdb:HMDB0000211", "kegg.compound:C00137", "kegg.drug:D08079", "knapsack:C00001164", "metacyc.compound:MYO-INOSITOL", "pdb-ccd:INS", "pubmed:11034685", "pubmed:11244303", "pubmed:11323092", "pubmed:11772411", "pubmed:12478879", "pubmed:12832083", "pubmed:14583919", "pubmed:14681857", "pubmed:15181167", "pubmed:15295080", "pubmed:15558078", "pubmed:16410747", "pubmed:1694860", "pubmed:17439666", "pubmed:17722064", "pubmed:18650262", "pubmed:18854045", "pubmed:19097871", "pubmed:19383710", "pubmed:22285975", "pubmed:22461977", "pubmed:22517104", "pubmed:838172", "reaxys:1907329", "wikipedia.en:Inositol"], "generalized_empirical_formula": ["C6H12O6"], "has_alternative_id": ["CHEBI:10601", "CHEBI:12826", "CHEBI:12831", "CHEBI:25451", "CHEBI:43559"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17268"], "inchi_key_string": ["CDAISMWEOUEBRE-GPIVLXJGSA-N"], "inchi_string": ["InChI=1S/C6H12O6/c7-1-2(8)4(10)6(12)5(11)3(1)9/h1-12H/t1-,2-,3-,4+,5-,6-"], "mass": ["180.156"], "monoisotopic_mass": ["180.06339"], "smiles_string": ["O[C@H]1[C@H](O)[C@@H](O)[C@H](O)[C@@H](O)[C@H]1O"]}, "synonyms": ["(1r,2R,3S,4s,5R,6S)-cyclohexane-1,2,3,4,5,6-hexol", "1,2,3,4,5,6-HEXAHYDROXY-CYCLOHEXANE", "1,2,3,5/4,6-cyclohexanehexol", "1D-myo-Inositol", "1L-myo-Inositol", "Bios I", "Cyclohexitol", "D-myo-Inositol", "Dambose", "Inositol", "Ins", "L-myo-Inositol", "Meat sugar", "Myoinositol", "cis-1,2,3,5-trans-4,6-cyclohexanehexol", "i-inositol", "inosite", "meso-Inositol", "myo-Inositol", "myo-Inositol", "myo-inositol", "myo-inositol"], "secondary": {"asserted": {"id": "CHEBI:17268", "label": "myo-inositol"}, "exact_current_rows": [{"label": "myo-Inositol", "match_type": "preferred_term", "identifier": "CHEBI:17268", "preferred_term": "myo-Inositol", "ontology_id": "CHEBI:17268", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[12]", "name": "Niacinamide", "primary": {"id": "CHEBI:17154", "label": "nicotinamide"}, "canonical_label": "nicotinamide", "label_equal": true, "definition": ["A pyridinecarboxamide that is pyridine in which the hydrogen at position 3 is replaced by a carboxamide group."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:98-92-0", "drugbank:DB02701", "drugcentral:1906", "foodb.food:FDB012485", "gmelin:3336", "hmdb:HMDB0001406", "kegg.compound:C00153", "kegg.drug:D00036", "knapsack:C00000209", "lincs.smallmolecule:LSM-5428", "metacyc.compound:NIACINAMIDE", "patent:US2904552", "patent:US2993051", "pdb-ccd:NCA", "pubmed:10884473", "pubmed:11355130", "pubmed:11814060", "pubmed:12014919", "pubmed:12487919", "pubmed:12519385", "pubmed:12709297", "pubmed:12782109", "pubmed:12890690", "pubmed:14729974", "pubmed:14757966", "pubmed:14871431", "pubmed:15497767", "pubmed:15563975", "pubmed:15780941", "pubmed:15807725", "pubmed:15834926", "pubmed:15995937", "pubmed:16029679", "pubmed:16209160", "pubmed:16596767", "pubmed:16766489", "pubmed:16871361", "pubmed:17021258", "pubmed:17129213", "pubmed:18234191", "pubmed:18316796", "pubmed:18368629", "pubmed:18373238", "pubmed:18389009", "pubmed:18514428", "pubmed:18930755", "pubmed:18987186", "pubmed:19212411", "pubmed:19539713", "pubmed:19544437", "pubmed:2026685", "pubmed:21503886", "pubmed:21891976", "pubmed:21918528", "pubmed:21926578", "pubmed:22067079", "pubmed:22160932", "pubmed:22207684", "pubmed:22232263", "pubmed:22281243", "pubmed:22359146", "pubmed:22361740", "pubmed:22407380", "pubmed:22456321", "pubmed:22536229", "pubmed:22543086", "pubmed:22626821", "pubmed:22699421", "pubmed:22709272", "pubmed:22763693", "pubmed:22770225", "pubmed:23016598", "pubmed:23028781", "pubmed:23043891", "pubmed:23047329", "pubmed:24027187", "pubmed:24077178", "pubmed:24559077", "pubmed:24635573", "pubmed:25504347", "pubmed:25561219", "pubmed:31710686", "pubmed:32249824", "pubmed:33196157", "pubmed:33471934", "pubmed:8620561", "pubmed:8767167", "pubmed:9518388", "reaxys:383619", "wikipedia.en:Nicotinamide"], "generalized_empirical_formula": ["C6H6N2O"], "has_alternative_id": ["CHEBI:14645", "CHEBI:25521", "CHEBI:44258", "CHEBI:7556"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17154"], "inchi_key_string": ["DFPAKSUCGFBDDF-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H6N2O/c7-6(9)5-2-1-3-8-4-5/h1-4H,(H2,7,9)"], "mass": ["122.127"], "monoisotopic_mass": ["122.04801"], "smiles_string": ["NC(=O)c1cccnc1"]}, "synonyms": ["3-carbamoylpyridine", "3-pyridinecarboxamide", "Niacinamide", "Nicotinamid", "Nicotinsaeureamid", "Nikotinamid", "Nikotinsaeureamid", "Vitamin PP", "beta-pyridinecarboxamide", "m-(aminocarbonyl)pyridine", "niacin", "niamide", "nicotinamida", "nicotinamide", "nicotinamidum", "nicotine acid amide", "nicotine amide", "nicotinic acid amide", "nicotinic amide", "nicotylamide", "pyridine-3-carboxamide", "pyridine-3-carboxamide", "pyridine-3-carboxylic acid amide", "vitamin B3"], "secondary": {"asserted": {"id": "CHEBI:17154", "label": "nicotinamide"}, "exact_current_rows": [{"label": "Nicotinamide", "match_type": "preferred_term", "identifier": "CHEBI:17154", "preferred_term": "Nicotinamide", "ontology_id": "CHEBI:17154", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[13]", "name": "Choline chloride", "primary": {"id": "CHEBI:133341", "label": "choline chloride"}, "canonical_label": "choline chloride", "label_equal": true, "definition": ["A quaternary ammonium salt with choline cation and chloride anion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:67-48-1", "ppdb:161", "pubmed:12962717", "pubmed:17596274", "pubmed:20396712", "pubmed:24905385", "pubmed:25037344", "pubmed:6196640", "pubmed:8047569", "reaxys:3563126", "vsdb:161", "wikipedia.en:Choline_chloride"], "generalized_empirical_formula": ["C5H14NO.Cl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:133341"], "inchi_key_string": ["SGMZJAMFUVOLNK-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C5H14NO.ClH/c1-6(2,3)4-5-7;/h7H,4-5H2,1-3H3;1H/q+1;/p-1"], "mass": ["139.626"], "monoisotopic_mass": ["139.07639"], "smiles_string": ["C[N+](C)(C)CCO.[Cl-]"]}, "synonyms": ["(2-Hydroxyethyl)trimethylammonium chloride", "(beta-Hydroxyethyl)trimethylammonium chloride", "2-Hydroxy-N,N,N,-trimethylethanaminium chloride", "2-hydroxy-N,N,N-trimethylethanaminium chloride", "2-hydroxy-N,N,N-trimethylethanaminium chloride", "Bilineurin chloride", "Biocolina", "Biocoline", "Chloride de choline", "Chlorure de choline", "Choline chlorhydrate", "Choline hydrochloride", "Cholini chloridum", "Cholinium chloride", "Cloruro de colina", "Hepacholine", "Lipotril", "Luridin chloride", "Paresan", "Trimethyl(2-hydroxyethyl)ammonium chloride", "choline chloride"], "secondary": {"asserted": {"id": "CHEBI:133341", "label": "choline chloride"}, "exact_current_rows": [{"label": "Choline chloride", "match_type": "preferred_term", "identifier": "CHEBI:133341", "preferred_term": "Choline chloride", "ontology_id": "CHEBI:133341", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[14]", "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806", "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3", "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"], "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]}, "synonyms": ["Resazurin"]}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[15]", "name": "NaHCO3", "primary": {"id": "CHEBI:32139", "label": "sodium hydrogencarbonate"}, "canonical_label": "sodium hydrogencarbonate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:144-55-8", "drugbank:DB01390", "kegg.compound:C12603", "kegg.drug:D01203", "ppdb:2873", "wikipedia.en:Sodium_Bicarbonate"], "generalized_empirical_formula": ["CHO3.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32139"], "inchi_key_string": ["UIIMBOGNXHQVGW-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/CH2O3.Na/c2-1(3)4;/h(H2,2,3,4);/q;+1/p-1"], "mass": ["84.006"], "monoisotopic_mass": ["83.98234"], "smiles_string": ["O=C([O-])O.[Na+]"]}, "synonyms": ["E 500", "E-500", "E500", "NaHCO3", "Natriumhydrogenkarbonat", "Sodium bicarbonate", "Sodium hydrogencarbonate", "baking soda", "bicarbonate of soda", "carbonic acid monosodium salt", "sodium acid carbonate", "sodium hydrogen carbonate", "sodium hydrogencarbonate", "sodium hydrogencarbonate"], "secondary": {"asserted": {"id": "CHEBI:32139", "label": "sodium hydrogencarbonate"}, "exact_current_rows": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[16]", "name": "D-Glucose", "primary": {"id": "CHEBI:17634", "label": "D-glucose"}, "canonical_label": "D-glucose", "label_equal": true, "definition": ["A glucose with &lt;small&gt;D&lt;/small&gt;-configuration."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:50-99-7"], "generalized_empirical_formula": ["C6H12O6"], "has_alternative_id": ["CHEBI:12965", "CHEBI:20999"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17634"], "mass": ["180.156"], "monoisotopic_mass": ["180.06339"]}, "synonyms": ["D(+)-glucose", "D-(+)-glucose", "D-gluco-hexose", "D-gluco-hexose", "D-glucose", "D-glucose", "Traubenzucker", "dextrose", "grape sugar"], "secondary": {"asserted": {"id": "CHEBI:17634", "label": "D-glucose"}, "exact_current_rows": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[17]", "name": "L-Cysteine HCl x H2O", "primary": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride hydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of &lt;small&gt;L&lt;/small&gt;-cysteine hydrochloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326", "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"], "inchi_key_string": ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"], "mass": ["175.637"], "monoisotopic_mass": ["175.00699"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]}, "synonyms": ["(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride monohydrate", "Cysteine hydrochloride", "L-Cysteine monohydrate monochloride", "L-cysteine hydrochloride monohydrate", "L-cysteine hydrochloride--water (1/1)", "L-cysteine hydrochloride--water (1/1)"], "secondary": {"asserted": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "exact_current_rows": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[18]", "name": "Na2S x 9 H2O", "primary": {"id": "CHEBI:76209", "label": "sodium sulfide nonahydrate"}, "canonical_label": "sodium sulfide nonahydrate", "label_equal": true, "definition": ["A hydrate with formula Na&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;S·9H&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;O."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:1313-84-4", "kegg.drug:D09001", "pubmed:19810706", "reaxys:14636099"], "generalized_empirical_formula": ["9H2O.2Na.S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:76209"], "inchi_key_string": ["ZGHLCBJZQLNUAZ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.9H2O.S/h;;9*1H2;/q2*+1;;;;;;;;;;-2"], "mass": ["240.182"], "monoisotopic_mass": ["240.04669"], "smiles_string": ["O.O.O.O.O.O.O.O.O.[Na+].[Na+].[S-2]"]}, "synonyms": ["Na2S.9H2O", "Sodium sulfide (USP)", "disodium sulfide nonahydrate", "disodium sulfide--water (1/9)", "disodium sulfide--water (1/9)", "sodium monosulfide nonahydrate", "sodium monosulfide.9H2O", "sodium sulfide.9H2O"], "secondary": {"asserted": {"id": "CHEBI:76209", "label": "sodium sulfide nonahydrate"}, "exact_current_rows": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[19]", "name": "Nitrilotriacetic acid", "primary": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "canonical_label": "nitrilotriacetic acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1710776", "cas:139-13-9", "drugbank:DB03040", "gmelin:3726", "kegg.compound:C14695", "pdb-ccd:NTA"], "generalized_empirical_formula": ["C6H9NO6"], "has_alternative_id": ["CHEBI:34889", "CHEBI:44555"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:44557"], "inchi_key_string": ["MGFYIUFZLHCRTH-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"], "mass": ["191.139"], "monoisotopic_mass": ["191.04299"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]}, "synonyms": ["Complexon I", "H3nta", "Komplexon I", "N(CH2-COOH)3", "N,N-bis(carboxymethyl)glycine", "N,N-bis(carboxymethyl)glycine", "NITRILOTRIACETIC ACID", "NTA", "Nitrilotriacetate", "Nitrilotriacetic acid", "Nitrilotriessigsaeure", "Triglycollamic acid", "Trilon A", "alpha,alpha',alpha''-trimethylaminetricarboxylic acid", "nitrilo-2,2',2''-triacetic acid", "tri(carboxymethyl)amine", "triglycine"], "secondary": {"asserted": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "exact_current_rows": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[20]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "canonical_label": "magnesium sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505", "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222", "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"], "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "exact_current_rows": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[21]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "canonical_label": "manganese(II) sulfate monohydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of manganese(II) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-96-5", "kegg.drug:D04854", "pubmed:26097037", "reaxys:13153017", "wikipedia.en:Manganese(II)_sulfate"], "generalized_empirical_formula": ["H2O.Mn.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86364"], "inchi_key_string": ["ISPYRSDWRDQNSW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mn.H2O4S.H2O/c;1-5(2,3)4;/h;(H2,1,2,3,4);1H2/q+2;;/p-2"], "mass": ["169.016"], "monoisotopic_mass": ["168.90034"], "smiles_string": ["O.O=S(=O)([O-])[O-].[Mn+2]"]}, "synonyms": ["Manganese sulfate hydrate", "Manganese sulfate monohydrate", "Manganese sulfate", "Manganous sulfate monohydrate", "MnSO4.H2O", "manganese(2+) sulfate monohydrate", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulphate monohydrate", "manganese(II) sulphate monohydrate"], "secondary": {"asserted": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "exact_current_rows": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[22]", "name": "FeSO4 x 7 H2O", "primary": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "canonical_label": "iron(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used)."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]}, "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O", "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"], "secondary": {"asserted": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[23]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "canonical_label": "cobalt(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of cobalt(2+) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10026-24-1", "pubmed:10504146", "pubmed:12187935", "pubmed:12209163", "pubmed:12579202", "pubmed:12948248", "pubmed:2227161", "pubmed:24359163", "pubmed:25896363", "wikipedia.en:Cobalt(II)_sulfate"], "generalized_empirical_formula": ["Co.7H2O.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91244"], "inchi_key_string": ["MEYVLGVRTYSQHI-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Co.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["281.101"], "monoisotopic_mass": ["280.95888"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Co+2]"]}, "synonyms": ["Cobalt monosulfate heptahydrate", "cobalt sulfate heptahydrate", "cobalt(2+) sulfate--water (1/7)", "cobalt(2+) sulfate--water (1/7)", "cobalt(II) sulfate heptahydrate", "cobaltous sulfate heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[24]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "canonical_label": "zinc sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of zinc sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7446-20-0", "gmelin:47216", "kegg.drug:D01081", "wikipedia.en:Zinc_Sulfate"], "generalized_empirical_formula": ["7H2O.O4S.Zn"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32312"], "inchi_key_string": ["RZLVQBNCHSJZPX-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/H2O4S.7H2O.Zn/c1-5(2,3)4;;;;;;;;/h(H2,1,2,3,4);7*1H2;/q;;;;;;;;+2/p-2"], "mass": ["287.558"], "monoisotopic_mass": ["285.95482"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Zn+2]"]}, "synonyms": ["Zinc sulfate", "ZnSO4.7H2O", "zinc sulfate (1:1) heptahydrate", "zinc sulfate heptahydrate (1:1:7)", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate--water (1/7)", "zinc(2+) sulfate--water (1/7)"], "secondary": {"asserted": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "exact_current_rows": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[25]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "canonical_label": "copper(II) sulfate pentahydrate", "label_equal": true, "definition": ["The pentahydrate of copper(2+) sulfate. A bright blue crystalline solid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-99-8", "kegg.drug:D03613", "pubmed:11407502", "pubmed:12209195", "pubmed:12484481", "pubmed:15040745", "pubmed:15607472", "pubmed:15824790", "pubmed:19346702", "pubmed:2002460", "pubmed:20132934", "pubmed:2913309", "pubmed:3351847", "pubmed:7615984", "pubmed:8878264", "pubmed:9521458", "pubmed:9776063", "reaxys:16499970", "wikipedia.en:Copper(II)_sulfate"], "generalized_empirical_formula": ["Cu.5H2O.O4S"], "has_alternative_id": ["CHEBI:121741", "CHEBI:370227"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31440"], "inchi_key_string": ["JZCCFEFSEZPSOG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Cu.H2O4S.5H2O/c;1-5(2,3)4;;;;;/h;(H2,1,2,3,4);5*1H2/q+2;;;;;;/p-2"], "mass": ["249.684"], "monoisotopic_mass": ["248.93415"], "smiles_string": ["O=S(=O)([O-])[O-].[Cu+2].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H]"]}, "synonyms": ["CuSO4.5H2O", "Cupric sulfate", "copper sulphate(5.H2O)", "copper(2+) sulfate (1:1) pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate--water (1/5)", "copper(2+) sulfate--water (1/5)", "copper(II) sulfate, pentahydrate", "cupric sulfate pentahydrate"], "secondary": {"asserted": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "exact_current_rows": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[26]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "canonical_label": "potassium aluminium sulfate dodecahydrate", "label_equal": true, "definition": ["A hydrate resulting from the the formal combination of anhydrous potassium aluminium sulfate with 12 mol eq. of water."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7784-24-9", "reaxys:14851666", "wikipedia.en:Potassium_alum"], "generalized_empirical_formula": ["Al.12H2O.K.2O4S"], "has_alternative_id": ["CHEBI:31192"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86465"], "inchi_key_string": ["GNHOJBNSNUXZQA-UHFFFAOYSA-J"], "inchi_string": ["InChI=1S/Al.K.2H2O4S.12H2O/c;;2*1-5(2,3)4;;;;;;;;;;;;/h;;2*(H2,1,2,3,4);12*1H2/q+3;+1;;;;;;;;;;;;;;/p-4"], "mass": ["474.386"], "monoisotopic_mass": ["473.97548"], "smiles_string": ["O.O.O.O.O.O.O.O.O.O.O.O.O=S(=O)([O-])[O-].O=S(=O)([O-])[O-].[Al+3].[K+]"]}, "synonyms": ["AlK(SO4)2.12H2O", "Aluminum potassium disulfate dodecahydrate", "Aluminum potassium sulfate dodecahydrate", "Kalinite", "Potash alum dodecahydrate", "Potassium alum dodecahydrate", "Potassium aluminum disulfate dodecahydrate", "aluminium potassium sulfate--water (1/12)", "aluminium potassium sulfate--water (1/12)"], "secondary": {"asserted": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "exact_current_rows": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[27]", "name": "H3BO3", "primary": {"id": "CHEBI:33118", "label": "boric acid"}, "canonical_label": "boric acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["bpdb:2136", "cas:10043-35-3", "cas:11113-50-1", "drugcentral:3035", "gmelin:1585", "kegg.compound:C12486", "kegg.drug:D01089", "molbase:1644", "pdb-ccd:BO3", "ppdb:2136"], "generalized_empirical_formula": ["H3BO3"], "has_alternative_id": ["CHEBI:22911", "CHEBI:31299", "CHEBI:41248"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:33118"], "inchi_key_string": ["KGBXLFKZBHKPEV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"], "mass": ["61.833"], "monoisotopic_mass": ["62.01752"], "smiles_string": ["[H]OB(O[H])O[H]"]}, "synonyms": ["B(OH)3", "BORIC ACID", "Boric acid", "H3BO3", "[B(OH)3]", "boric acid", "boron trihydroxide", "orthoboric acid", "trihydroxidoboron", "trihydroxidoboron"], "secondary": {"asserted": {"id": "CHEBI:33118", "label": "boric acid"}, "exact_current_rows": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[28]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "canonical_label": "sodium molybdate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium molybdate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10102-40-6", "pubmed:20645132", "pubmed:20813395", "pubmed:22663766", "pubmed:3382795", "reaxys:19032996", "wikipedia.en:Sodium_molybdate"], "generalized_empirical_formula": ["2H2O.MoO4.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75213"], "inchi_key_string": ["FDEIWTXVNPKYDL-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/Mo.2Na.2H2O.4O/h;;;2*1H2;;;;/q;2*+1;;;;;2*-1"], "mass": ["241.946"], "monoisotopic_mass": ["243.88573"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]}, "synonyms": ["Disodium molybdate dihydrate", "Molybdic acid, disodium salt, dihydrate", "Na2MoO4.2H2O", "Sodium molybdate(VI) dihydrate", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium orthomolybdate dihydrate"], "secondary": {"asserted": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "exact_current_rows": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[29]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "canonical_label": "disodium selenite pentahydrate", "label_equal": true, "definition": ["A hydrate that is the pentahydrate form of disodium selenite."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:26970-82-1", "pubmed:15259772", "pubmed:15559373", "pubmed:16126997", "pubmed:17873396", "pubmed:24479345", "pubmed:24716537", "reaxys:14666014", "wikipedia.en:Sodium_selenite"], "generalized_empirical_formula": ["5H2O.2Na.O3Se"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131361"], "inchi_key_string": ["TUANAMBRHOLYTH-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"], "mass": ["263.012"], "monoisotopic_mass": ["263.93363"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2SeO3.5H2O", "Selenious acid disodium salt, pentahydrate", "Sodium selenite pentahydrate", "disodium selenite hydrate", "sodium selenite hydrate", "sodium selenite--water (1/5)", "sodium selenite--water (1/5)"], "secondary": {"asserted": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "exact_current_rows": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[30]", "name": "Biotin", "primary": {"id": "CHEBI:15956", "label": "biotin"}, "canonical_label": "biotin", "label_equal": true, "definition": ["An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:58-85-5", "chemspider:149962", "drugbank:DB00121", "drugcentral:373", "foodb.food:FDB014510", "gmelin:1918703", "hmdb:HMDB0000030", "kegg.compound:C00120", "kegg.drug:D00029", "knapsack:C00000756", "lincs.smallmolecule:LSM-3994", "metacyc.compound:BIOTIN", "pdb-ccd:BTN", "pmc:PMC8089577", "pubmed:10064317", "pubmed:10215065", "pubmed:10577274", "pubmed:11435506", "pubmed:11481419", "pubmed:11800048", "pubmed:12055344", "pubmed:12070309", "pubmed:12603856", "pubmed:12803839", "pubmed:15012185", "pubmed:15202718", "pubmed:15272000", "pubmed:15690449", "pubmed:15863846", "pubmed:15899401", "pubmed:15992684", "pubmed:16011464", "pubmed:16195795", "pubmed:16419467", "pubmed:16676358", "pubmed:16677798", "pubmed:16704206", "pubmed:16769720", "pubmed:17297119", "pubmed:1814646", "pubmed:18202531", "pubmed:18452485", "pubmed:18509457", "pubmed:19212411", "pubmed:19319844", "pubmed:19727438", "pubmed:19928962", "pubmed:20967359", "pubmed:20974274", "pubmed:2100006", "pubmed:21248194", "pubmed:21356565", "pubmed:21373679", "pubmed:21596550", "pubmed:21871906", "pubmed:25515858", "pubmed:33346513", "pubmed:33461365", "pubmed:34077272", "pubmed:8333586", "pubmed:8750932", "pubmed:9022537", "pubmed:9038855", "pubmed:9094878", "pubmed:9164991", "pubmed:9176832", "pubmed:9371938", "pubmed:9416479", "reaxys:86838", "wikipedia.en:Biotin"], "generalized_empirical_formula": ["C10H16N2O3S"], "has_alternative_id": ["CHEBI:13905", "CHEBI:22882", "CHEBI:22884", "CHEBI:3108", "CHEBI:41236"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15956"], "inchi_key_string": ["YBJHBAHKTGYVGT-ZKWXMUAHSA-N"], "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"], "mass": ["244.316"], "monoisotopic_mass": ["244.08816"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]}, "synonyms": ["(+)-cis-Hexahydro-2-oxo-1H-thieno[3,4]imidazole-4-valeric acid", "(3aS,4S,6aR)-Hexahydro-2-oxo-1H-thieno[3,4-d]imidazole-4-valeric acid", "5-(2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl)pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "BIOTIN", "Coenzyme R", "D-(+)-biotin", "D-Biotin", "Vitamin H", "biotin", "biotina", "biotine", "biotinum", "cis-(+)-Tetrahydro-2-oxothieno[3,4]imidazoline-4-valeric acid", "cis-Hexahydro-2-oxo-1H-thieno(3,4)imidazole-4-valeric acid", "cis-Tetrahydro-2-oxothieno(3,4-d)imidazoline-4-valeric acid", "vitamin B7"], "secondary": {"asserted": {"id": "CHEBI:15956", "label": "biotin"}, "exact_current_rows": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[31]", "name": "Folic acid", "primary": {"id": "CHEBI:27470", "label": "folic acid"}, "canonical_label": "folic acid", "label_equal": true, "definition": ["An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND606960789", "cas:59-30-3", "chemspider:5815", "drugbank:DB00158", "drugcentral:1231", "foodb.food:FDB014504", "hmdb:HMDB0000121", "kegg.compound:C00504", "kegg.drug:D00070", "knapsack:C00001539", "lincs.smallmolecule:LSM-5355", "metacyc.compound:CPD-12826", "pdb-ccd:FOL", "pubmed:10138938", "pubmed:10897644", "pubmed:10958818", "pubmed:11261364", "pubmed:11451208", "pubmed:11959400", "pubmed:14387833", "pubmed:15321809", "pubmed:15523939", "pubmed:15754725", "pubmed:15797531", "pubmed:15797685", "pubmed:15831910", "pubmed:15990733", "pubmed:16093404", "pubmed:16277678", "pubmed:16380297", "pubmed:16871332", "pubmed:17784727", "pubmed:18788725", "pubmed:19121630", "pubmed:19335717", "pubmed:19355913", "pubmed:24650098", "pubmed:33624660", "pubmed:33965562", "pubmed:33968971", "pubmed:34207319", "pubmed:34219855", "pubmed:7738698", "pubmed:8235383", "pubmed:9040515", "pubmed:9420019", "pubmed:9565830", "pubmed:9683174", "pubmed:9781393", "pubmed:9808640", "pubmed:9808641", "reaxys:100781", "wikipedia.en:Folic_Acid"], "generalized_empirical_formula": ["C19H19N7O6"], "has_alternative_id": ["CHEBI:24075", "CHEBI:42610", "CHEBI:5140", "CHEBI:569217"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:27470"], "inchi_key_string": ["OVBPIULPVIDEAO-LBPRGKRZSA-N"], "inchi_string": ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"], "mass": ["441.404"], "monoisotopic_mass": ["441.13968"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]}, "synonyms": ["(2S)-2-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzamido)pentanedioic acid", "Acfol", "Folate", "Folicet", "Folsaeure", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-[(4-{[(2-amino-4-oxo-1,4-dihydropteridin-6-yl)methyl]amino}phenyl)carbonyl]-L-glutamic acid", "N-pteroyl-L-glutamic acid", "PGA", "PteGlu", "acide folique", "acido folico", "acidum folicum", "folic acid", "pteroyl-L-glutamic acid", "pteroyl-L-monoglutamic acid", "pteroylglutamic acid", "pteroylmonoglutamic acid", "vitamin B11", "vitamin B9", "vitamin Bc", "vitamin Be", "vitamin M"], "secondary": {"asserted": {"id": "CHEBI:27470", "label": "folic acid"}, "exact_current_rows": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[32]", "name": "Pyridoxine hydrochloride", "primary": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "canonical_label": "pyridoxine hydrochloride", "label_equal": true, "definition": ["The hydrochloride salt of pyridoxine."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND500675659", "beilstein:3632435", "cas:58-56-0", "drugbank:DBSALT000151", "foodb.food:FDB000575", "gmelin:1067921", "kegg.drug:D02179", "pubmed:15098856", "pubmed:17416572", "pubmed:17891511", "pubmed:18243627", "pubmed:19481898", "pubmed:20645279", "pubmed:21781646", "pubmed:24421551", "pubmed:27468034", "pubmed:28095734", "pubmed:32460509", "pubmed:33209152", "pubmed:33936292", "pubmed:34140989"], "generalized_empirical_formula": ["C8H11NO3.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30961"], "inchi_key_string": ["ZUFQODAHGAHPFQ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H11NO3.ClH/c1-5-8(12)7(4-11)6(3-10)2-9-5;/h2,10-12H,3-4H2,1H3;1H"], "mass": ["205.641"], "monoisotopic_mass": ["205.05057"], "smiles_string": ["Cc1ncc(CO)c(CO)c1O.Cl"]}, "synonyms": ["2-methyl-3-hydroxy-4,5-bis(hydroxymethyl)pyridine hydrochloride", "3-hydroxy-4,5-dimethylol-alpha-picoline hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "5-hydroxy-6-methyl-3,4-pyridinedimethanol hydrochloride", "pyridoxol hydrochloride", "vitamin B6 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "exact_current_rows": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[33]", "name": "Thiamine HCl", "primary": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "canonical_label": "thiamine hydrochloride", "label_equal": true, "definition": ["A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND605711145", "agr:IND606057536", "beilstein:3642937", "beilstein:3851771", "cas:67-03-8", "chemspider:5967", "drugbank:DBSALT000205", "foodb.food:FDB008416", "gmelin:31154", "gmelin:691133", "kegg.drug:D02094", "pubmed:11548854", "pubmed:12224421", "pubmed:21212548", "pubmed:22305197", "pubmed:24399744", "pubmed:25977858", "pubmed:26616989", "pubmed:27163892", "pubmed:28763984", "pubmed:28784494", "pubmed:30131156", "pubmed:31270735", "pubmed:31664290", "pubmed:32009117", "pubmed:32562525", "pubmed:32824791", "reaxys:17124533"], "generalized_empirical_formula": ["C12H17N4OS.Cl.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:49105"], "inchi_key_string": ["DPJRMOMPQZCRJU-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C12H17N4OS.2ClH/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H/q+1;;/p-1"], "mass": ["337.276"], "monoisotopic_mass": ["336.05784"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1.Cl.[Cl-]"]}, "synonyms": ["3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "thiamin dichloride", "thiamin hydrochloride", "thiamine HCl", "thiamine chloride hydrochloride", "thiamine dichloride", "thiamine(2+) dichloride", "thiaminium chloride hydrochloride", "vitamin B1 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "exact_current_rows": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[34]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015", "label": "riboflavin"}, "canonical_label": "riboflavin", "label_equal": true, "definition": ["&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:83-88-5", "chemspider:431981", "drugbank:DB00140", "drugcentral:2834", "foodb.food:FDB012160", "hmdb:HMDB0000244", "kegg.compound:C00255", "kegg.drug:D00050", "knapsack:C00001552", "lincs.smallmolecule:LSM-4084", "metacyc.compound:RIBOFLAVIN", "patent:US2807611", "patent:US2876169", "pdb-ccd:RBF", "pubmed:10566553", "pubmed:11399071", "pubmed:11606856", "pubmed:12083520", "pubmed:12354259", "pubmed:12927541", "pubmed:14963913", "pubmed:16273338", "pubmed:16460756", "pubmed:16658098", "pubmed:182198", "pubmed:18832377", "pubmed:19169240", "pubmed:19212411", "pubmed:19854891", "pubmed:22770225", "pubmed:2369885", "pubmed:23818044", "pubmed:24643482", "pubmed:24816110", "pubmed:25108762", "pubmed:25468971", "pubmed:25887755", "pubmed:2631092", "pubmed:29937405", "pubmed:3142982", "pubmed:33154451", "pubmed:33304888", "pubmed:33886098", "pubmed:33892358", "pubmed:34156642", "pubmed:3592624", "pubmed:3878498", "pubmed:4019261", "pubmed:6475825", "pubmed:6546833", "pubmed:6650303", "pubmed:7101408", "pubmed:7883462", "pubmed:8487103", "pubmed:8604671", "pubmed:8678471", "pubmed:8976642", "pubmed:9184778", "pubmed:9808225", "pubmed:9874201", "reaxys:97831", "wikipedia.en:Riboflavin"], "generalized_empirical_formula": ["C17H20N4O6"], "has_alternative_id": ["CHEBI:15044", "CHEBI:27299", "CHEBI:45214", "CHEBI:529204", "CHEBI:8843"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17015"], "inchi_key_string": ["AUNGANRZJHBGPY-SCRDCRAPSA-N"], "inchi_string": ["InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23)14(25)12(24)6-22)15-13(18-9)16(26)20-17(27)19-15/h3-4,11-12,14,22-25H,5-6H2,1-2H3,(H,20,26,27)/t11-,12+,14-/m0/s1"], "mass": ["376.369"], "monoisotopic_mass": ["376.13828"], "smiles_string": ["Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)CO)c2cc1C"]}, "synonyms": ["1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol", "5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "6,7-dimethyl-9-D-ribitylisoalloxazine", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine", "7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-ribitylisoalloxazine", "Aqua-Flave", "Beflavin", "Beflavine", "Bisulase", "Dermadram", "E101", "Fiboflavin", "Flavaxin", "Flavin Bb", "Flaxain", "Hyflavin", "Vitamin B2", "lactoflavin", "riboflavin (vit B2)", "riboflavin", "riboflavina", "riboflavine", "riboflavinum", "vitamin B2", "vitamin G", "vitasan B2"], "secondary": {"asserted": {"id": "CHEBI:17015", "label": "riboflavin"}, "exact_current_rows": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[35]", "name": "Nicotinic acid", "primary": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "canonical_label": "nicotinic acid", "label_equal": true, "definition": ["A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND607088605", "cas:59-67-6", "chemspider:913", "drugbank:DB00627", "drugcentral:2835", "foodb.food:FDB001014", "gmelin:3340", "hmdb:HMDB0001488", "kegg.compound:C00253", "kegg.drug:D00049", "knapsack:C00000208", "lincs.smallmolecule:LSM-4676", "metacyc.compound:NIACINE", "pdb-ccd:NIO", "pubmed:10540864", "pubmed:113218", "pubmed:12563315", "pubmed:12789870", "pubmed:135660", "pubmed:14550884", "pubmed:15037193", "pubmed:15183629", "pubmed:15205990", "pubmed:15311728", "pubmed:15627518", "pubmed:15651982", "pubmed:16018787", "pubmed:16172771", "pubmed:16322787", "pubmed:16400392", "pubmed:16449845", "pubmed:16767301", "pubmed:16877271", "pubmed:16945375", "pubmed:18037924", "pubmed:182198", "pubmed:186078", "pubmed:18993152", "pubmed:18996527", "pubmed:19369827", "pubmed:19592242", "pubmed:19678716", "pubmed:19779335", "pubmed:20979384", "pubmed:21632263", "pubmed:22116693", "pubmed:22155410", "pubmed:22229411", "pubmed:22366213", "pubmed:22458880", "pubmed:22770225", "pubmed:24029555", "pubmed:24568240", "pubmed:24675661", "pubmed:24848081", "pubmed:24975217", "pubmed:25040591", "pubmed:25241762", "pubmed:25429652", "pubmed:32954525", "pubmed:33273654", "pubmed:33932650", "pubmed:34066686", "pubmed:34085526", "pubmed:34117670", "pubmed:4033386", "pubmed:4259917", "pubmed:582105", "pubmed:699281", "pubmed:7217784", "pubmed:7581845", "pubmed:8306147", "pubmed:8423912", "pubmed:8679452", "pubmed:9107536", "reaxys:109591", "wikipedia.en:Niacin"], "generalized_empirical_formula": ["C6H5NO2"], "has_alternative_id": ["CHEBI:25538", "CHEBI:44319", "CHEBI:7559"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15940"], "inchi_key_string": ["PVNIIMVLHYAWGP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"], "mass": ["123.111"], "monoisotopic_mass": ["123.03203"], "smiles_string": ["O=C(O)c1cccnc1"]}, "synonyms": ["3-Pyridylcarboxylic acid", "3-carboxylpyridine", "3-carboxypyridine", "3-pyridinecarboxylic acid", "NICOTINIC ACID", "NICOTINIC ACID", "Niacin", "Niacor", "Niaspan", "Nicotinic acid", "Nicotinic acid", "Nicotinsaure", "Nikotinsaeure", "P.P. factor", "PP factor", "acide nicotinique", "acido nicotinico", "acidum nicotinicum", "anti-pellagra vitamin", "beta-pyridinecarboxylic acid", "m-pyridinecarboxylic acid", "nicotinic acid", "nicotinic acid", "pellagra preventive factor", "pyridine-3-carboxylic acid", "pyridine-3-carboxylic acid", "pyridine-beta-carboxylic acid", "pyridine-carboxylique-3", "vitamin B3"], "secondary": {"asserted": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "exact_current_rows": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[36]", "name": "Calcium D-(+)-pantothenate", "primary": {"id": "CHEBI:31345", "label": "Calcium pantothenate"}, "canonical_label": "Calcium pantothenate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:137-08-6", "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278", "pubmed:20553011", "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula": ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"], "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"], "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]}, "synonyms": ["Calcium pantotenate", "Calcium pantothenate", "Calcium pantothenate, d-", "Calpan", "D-ca pantothenate", "D-calcium pantothenate", "NSC-36292", "Pantholin", "Pantothenic acid (as calcium)", "Pantothenic acid calcium salt", "Vitamin b5, calcium salt", "pantotenato de calcio", "pantothenate de calcium"]}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[37]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843", "label": "vitamin B12"}, "canonical_label": "vitamin B12", "label_equal": true, "definition": ["Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives)."], "annotations": {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:176843"]}, "synonyms": ["vitamin B-12", "vitamin B12 vitamer", "vitamin B12 vitamers", "vitamin B12", "vitamins B12"], "secondary": {"asserted": {"id": "CHEBI:176843", "label": "vitamin B12"}, "exact_current_rows": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[38]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "canonical_label": "4-aminobenzoic acid", "label_equal": true, "definition": ["An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:150-13-0", "drugbank:DB02362", "drugcentral:2049", "ecmdb:ECMDB01392", "gmelin:50150", "hmdb:HMDB0001392", "kegg.compound:C00568", "kegg.drug:D02456", "knapsack:C00001401", "pdb-ccd:PAB", "pubmed:12039592", "pubmed:14745019", "pubmed:15115392", "pubmed:1527790", "pubmed:16290145", "pubmed:17149871", "pubmed:17743450", "pubmed:17800214", "pubmed:19469519", "pubmed:22767283", "pubmed:22994574", "pubmed:23063996", "pubmed:23084339", "pubmed:23144588", "pubmed:23471007", "pubmed:3599019", "pubmed:3820215", "pubmed:3950915", "pubmed:8411009", "pubmed:9406595", "reaxys:471605", "wikipedia.en:4-Aminobenzoic_acid", "ymdb:YMDB00493"], "generalized_empirical_formula": ["C7H7NO2"], "has_alternative_id": ["CHEBI:113372", "CHEBI:1783", "CHEBI:20315", "CHEBI:44778"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30753"], "inchi_key_string": ["ALYNCZNDIQEVRV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"], "mass": ["137.138"], "monoisotopic_mass": ["137.04768"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]}, "synonyms": ["1-Amino-4-carboxybenzene", "4-AMINOBENZOIC ACID", "4-AMINOBENZOIC ACID", "4-Amino-benzoic acid", "4-Aminobenzoesaeure", "4-Aminobenzoic acid", "4-Aminobenzoic acid", "4-Carboxyaniline", "4-Carboxyphenylamine", "4-aminobenzoic acid", "4-aminobenzoic acid", "ABEE", "PABA", "gamma-Aminobenzoic acid", "gamma-aminobenzoic acid", "p-Aminobenzoesaeure", "p-aminobenzoic acid", "p-carboxyaniline", "p-carboxyphenylamine", "para-aminobenzoic acid"], "secondary": {"asserted": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "exact_current_rows": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field": "ingredients[39]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id": "CHEBI:16494", "label": "lipoic acid"}, "canonical_label": "lipoic acid", "label_equal": true, "definition": ["A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:122410", "cas:62-46-4", "drugbank:DB00166", "drugcentral:4732", "ecmdb:ECMDB01451", "gmelin:720915", "kegg.compound:C00725", "kegg.drug:D00086", "pubmed:15328413", "pubmed:7519986", "pubmed:7548757", "reaxys:81853", "wikipedia.en:Lipoic_acid", "ymdb:YMDB00334"], "generalized_empirical_formula": ["C8H14O2S2"], "has_alternative_id": ["CHEBI:146958", "CHEBI:25058", "CHEBI:6492"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16494"], "inchi_key_string": ["AGBQKNBQESQNJD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H14O2S2/c9-8(10)4-2-1-3-7-5-6-11-12-7/h7H,1-6H2,(H,9,10)"], "mass": ["206.332"], "monoisotopic_mass": ["206.04352"], "smiles_string": ["O=C(O)CCCCC1CCSS1"]}, "synonyms": ["1,2-dithiolane-3-pentanoic acid", "1,2-dithiolane-3-valeric acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)valeric acid", "5-(dithiolan-3-yl)valeric acid", "5-[3-(1,2-dithiolanyl)]pentanoic acid", "6,8-thioctic acid", "6,8-thiotic acid", "6-thioctic acid", "6-thiotic acid", "Acetate-replacing factor", "Biletan", "Lipoic acid", "Thioctansaeure", "Thioctic acid", "Thioctsaeure", "Thioktsaeure", "alpha-Lipoic acid", "alpha-Liponsaeure", "alpha-lipoic acid", "liponic acid"], "secondary": {"asserted": {"id": "CHEBI:16494", "label": "lipoic acid"}, "exact_current_rows": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[0]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "canonical_label": "potassium dihydrogen phosphate", "label_equal": true, "definition": ["A potassium salt in which dihydrogen phosphate(1−) is the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"], "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"], "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]}, "synonyms": ["MKP", "Monopotassium dihydrogen phosphate", "Monopotassium monophosphate", "Monopotassium orthophosphate", "Monopotassium phosphate", "Orthophosphoric acid, monopotassium salt", "Phosphoric acid, monopotassium salt", "Phosphoric acid, potassium salt (1:1)", "Potassium acid phosphate", "Potassium dihydrogen orthophosphate", "Potassium dihydrogen phosphate", "Potassium phosphate monobasic", "Potassium phosphate", "Sorensen's potassium phosphate", "potassium dihydrogen phosphate", "potassium dihydrogen phosphate"], "secondary": {"asserted": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "exact_current_rows": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[1]", "name": "Na2SO4", "primary": {"id": "CHEBI:32149", "label": "sodium sulfate"}, "canonical_label": "sodium sulfate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7757-82-6", "kegg.compound:C13199", "kegg.drug:D01732"], "generalized_empirical_formula": ["2Na.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32149"], "inchi_key_string": ["PMZURENOXWZQFD-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2Na.H2O4S/c;;1-5(2,3)4/h;;(H2,1,2,3,4)/q2*+1;/p-2"], "mass": ["142.043"], "monoisotopic_mass": ["141.93127"], "smiles_string": ["O=S(=O)([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2SO4", "Natriumsulfat", "Sodium sulfate", "disodium sulfate", "disodium sulphate", "salt cake", "sodium sulfate", "sodium sulfate", "sodium sulfate, anhydrous", "sodium sulphate"], "secondary": {"asserted": {"id": "CHEBI:32149", "label": "sodium sulfate"}, "exact_current_rows": [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[2]", "name": "NH4Cl", "primary": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "canonical_label": "ammonium chloride", "label_equal": true, "definition": ["An inorganic chloride having ammonium as the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:12125-02-9", "gmelin:10120", "kegg.compound:C12538", "kegg.drug:D01139", "wikipedia.en:Ammonium_Chloride"], "generalized_empirical_formula": ["Cl.H4N"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31206"], "inchi_key_string": ["NLXLAEXVIDQMFP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/ClH.H3N/h1H;1H3"], "mass": ["53.492"], "monoisotopic_mass": ["53.00323"], "smiles_string": ["[Cl-].[H][N+]([H])([H])[H]"]}, "synonyms": ["Ammonium chloride", "Ammoniumchlorid", "NH4Cl", "[NH4]Cl", "ammonium chloride", "ammonium chloride", "azanium chloride"], "secondary": {"asserted": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "exact_current_rows": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[3]", "name": "KCl", "primary": {"id": "CHEBI:32588", "label": "potassium chloride"}, "canonical_label": "potassium chloride", "label_equal": true, "definition": ["A metal chloride salt with a K(+) counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7447-40-7", "drugbank:DB00761", "kegg.drug:D02060", "metacyc.compound:KCL", "molbase:881", "reaxys:3534978", "wikipedia.en:Potassium_Chloride"], "generalized_empirical_formula": ["Cl.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32588"], "inchi_key_string": ["WCUXLLCKKVVCTQ-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "monoisotopic_mass": ["73.93256"], "smiles_string": ["[Cl-].[K+]"]}, "synonyms": ["KCl", "Kaliumchlorid", "Kaon-Cl 10", "Klor-con", "Klotrix", "Monopotassium chloride", "[KCl]", "muriate of potash", "potassium chloride", "potassium chloride", "sylvite"], "secondary": {"asserted": {"id": "CHEBI:32588", "label": "potassium chloride"}, "exact_current_rows": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[4]", "name": "NaCl", "primary": {"id": "CHEBI:26710", "label": "sodium chloride"}, "canonical_label": "sodium chloride", "label_equal": true, "definition": ["An inorganic chloride salt having sodium(1+) as the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula": ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string": ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]}, "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "secondary": {"asserted": {"id": "CHEBI:26710", "label": "sodium chloride"}, "exact_current_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[5]", "name": "MgCl2 x 6 H2O", "primary": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "canonical_label": "magnesium dichloride hexahydrate", "label_equal": true, "definition": ["A hydrate that is the hexahydrate form of magnesium dichloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7791-18-6", "kegg.drug:D04834", "pubmed:24831644", "pubmed:25148974", "pubmed:25430969", "reaxys:11343754"], "generalized_empirical_formula": ["2Cl.6H2O.Mg"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86345"], "inchi_key_string": ["DHRRIBDTHFBPNG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass": ["203.301"], "monoisotopic_mass": ["201.98614"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}, "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate", "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"], "secondary": {"asserted": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "exact_current_rows": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[6]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "canonical_label": "calcium chloride dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of calcium chloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8", "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"], "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass": ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}, "synonyms": ["CaCl2.2H2O", "Calcium chloride hydrate", "Calcium chloride", "calcium chloride--water (1/2)", "calcium chloride--water (1/2)", "calcium dichloride dihydrate"], "secondary": {"asserted": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "exact_current_rows": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[7]", "name": "Yeast extract"}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[8]", "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "canonical_label": "nickel dichloride", "label_equal": true, "definition": ["A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7718-54-9", "kegg.compound:C14711", "pubmed:11739495", "pubmed:12603851", "pubmed:21928331", "pubmed:23179351", "pubmed:23622879", "pubmed:23702803", "pubmed:23735035", "pubmed:7671317", "reaxys:3902827", "reaxys:8128171", "wikipedia.en:Nickel_dichloride"], "generalized_empirical_formula": ["Cl2Ni"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:34887"], "inchi_key_string": ["QMMRZOWCJAIUJA-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"], "mass": ["129.599"], "monoisotopic_mass": ["127.87305"], "smiles_string": ["[Cl][Ni][Cl]"]}, "synonyms": ["NiCl2", "Nickel chloride", "Nickel(II) chloride", "[NiCl2]", "nickel dichloride", "nickel dichloride", "nickel(2+) chloride", "nickel(2+) chloride", "nickel(II) chloride", "nickel(II) chloride", "nickelous chloride"], "secondary": {"asserted": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "exact_current_rows": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[9]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "canonical_label": "sodium tungstate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines to nitrones"], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10213-10-2", "reaxys:13157884", "wikipedia.en:Sodium_tungstate"], "generalized_empirical_formula": ["2H2O.2Na.O4W"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63939"], "inchi_key_string": ["WPZFLQRLSGVIAA-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.2H2O.4O.W/h;;2*1H2;;;;;/q2*+1;;;;;2*-1;"], "mass": ["329.846"], "monoisotopic_mass": ["329.93126"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]}, "synonyms": ["Na2WO4.2H2O", "Tungstic acid, sodium salt, dihydrate", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium orthotungstate dihydrate", "sodium tungstate(VI) dihydrate"], "secondary": {"asserted": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "exact_current_rows": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[10]", "name": "Ascorbic acid", "primary": {"id": "CHEBI:22652", "label": "ascorbic acid"}, "canonical_label": "ascorbic acid", "label_equal": true, "definition": [], "annotations": {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:22652"]}, "synonyms": [], "secondary": {"asserted": {"id": "CHEBI:22652", "label": "ascorbic acid"}, "exact_current_rows": [{"label": "Ascorbic acid", "match_type": "preferred_term", "identifier": "CHEBI:22652", "preferred_term": "Ascorbic acid", "ontology_id": "CHEBI:22652", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[11]", "name": "Myo-inositol", "primary": {"id": "CHEBI:17268", "label": "myo-inositol"}, "canonical_label": "myo-inositol", "label_equal": true, "definition": ["An inositol having &lt;i&gt;myo&lt;/i&gt;- configuration."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:87-89-8", "drugbank:DB03106", "drugcentral:1444", "gmelin:82918", "hmdb:HMDB0000211", "kegg.compound:C00137", "kegg.drug:D08079", "knapsack:C00001164", "metacyc.compound:MYO-INOSITOL", "pdb-ccd:INS", "pubmed:11034685", "pubmed:11244303", "pubmed:11323092", "pubmed:11772411", "pubmed:12478879", "pubmed:12832083", "pubmed:14583919", "pubmed:14681857", "pubmed:15181167", "pubmed:15295080", "pubmed:15558078", "pubmed:16410747", "pubmed:1694860", "pubmed:17439666", "pubmed:17722064", "pubmed:18650262", "pubmed:18854045", "pubmed:19097871", "pubmed:19383710", "pubmed:22285975", "pubmed:22461977", "pubmed:22517104", "pubmed:838172", "reaxys:1907329", "wikipedia.en:Inositol"], "generalized_empirical_formula": ["C6H12O6"], "has_alternative_id": ["CHEBI:10601", "CHEBI:12826", "CHEBI:12831", "CHEBI:25451", "CHEBI:43559"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17268"], "inchi_key_string": ["CDAISMWEOUEBRE-GPIVLXJGSA-N"], "inchi_string": ["InChI=1S/C6H12O6/c7-1-2(8)4(10)6(12)5(11)3(1)9/h1-12H/t1-,2-,3-,4+,5-,6-"], "mass": ["180.156"], "monoisotopic_mass": ["180.06339"], "smiles_string": ["O[C@H]1[C@H](O)[C@@H](O)[C@H](O)[C@@H](O)[C@H]1O"]}, "synonyms": ["(1r,2R,3S,4s,5R,6S)-cyclohexane-1,2,3,4,5,6-hexol", "1,2,3,4,5,6-HEXAHYDROXY-CYCLOHEXANE", "1,2,3,5/4,6-cyclohexanehexol", "1D-myo-Inositol", "1L-myo-Inositol", "Bios I", "Cyclohexitol", "D-myo-Inositol", "Dambose", "Inositol", "Ins", "L-myo-Inositol", "Meat sugar", "Myoinositol", "cis-1,2,3,5-trans-4,6-cyclohexanehexol", "i-inositol", "inosite", "meso-Inositol", "myo-Inositol", "myo-Inositol", "myo-inositol", "myo-inositol"], "secondary": {"asserted": {"id": "CHEBI:17268", "label": "myo-inositol"}, "exact_current_rows": [{"label": "myo-Inositol", "match_type": "preferred_term", "identifier": "CHEBI:17268", "preferred_term": "myo-Inositol", "ontology_id": "CHEBI:17268", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[12]", "name": "Niacinamide", "primary": {"id": "CHEBI:17154", "label": "nicotinamide"}, "canonical_label": "nicotinamide", "label_equal": true, "definition": ["A pyridinecarboxamide that is pyridine in which the hydrogen at position 3 is replaced by a carboxamide group."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:98-92-0", "drugbank:DB02701", "drugcentral:1906", "foodb.food:FDB012485", "gmelin:3336", "hmdb:HMDB0001406", "kegg.compound:C00153", "kegg.drug:D00036", "knapsack:C00000209", "lincs.smallmolecule:LSM-5428", "metacyc.compound:NIACINAMIDE", "patent:US2904552", "patent:US2993051", "pdb-ccd:NCA", "pubmed:10884473", "pubmed:11355130", "pubmed:11814060", "pubmed:12014919", "pubmed:12487919", "pubmed:12519385", "pubmed:12709297", "pubmed:12782109", "pubmed:12890690", "pubmed:14729974", "pubmed:14757966", "pubmed:14871431", "pubmed:15497767", "pubmed:15563975", "pubmed:15780941", "pubmed:15807725", "pubmed:15834926", "pubmed:15995937", "pubmed:16029679", "pubmed:16209160", "pubmed:16596767", "pubmed:16766489", "pubmed:16871361", "pubmed:17021258", "pubmed:17129213", "pubmed:18234191", "pubmed:18316796", "pubmed:18368629", "pubmed:18373238", "pubmed:18389009", "pubmed:18514428", "pubmed:18930755", "pubmed:18987186", "pubmed:19212411", "pubmed:19539713", "pubmed:19544437", "pubmed:2026685", "pubmed:21503886", "pubmed:21891976", "pubmed:21918528", "pubmed:21926578", "pubmed:22067079", "pubmed:22160932", "pubmed:22207684", "pubmed:22232263", "pubmed:22281243", "pubmed:22359146", "pubmed:22361740", "pubmed:22407380", "pubmed:22456321", "pubmed:22536229", "pubmed:22543086", "pubmed:22626821", "pubmed:22699421", "pubmed:22709272", "pubmed:22763693", "pubmed:22770225", "pubmed:23016598", "pubmed:23028781", "pubmed:23043891", "pubmed:23047329", "pubmed:24027187", "pubmed:24077178", "pubmed:24559077", "pubmed:24635573", "pubmed:25504347", "pubmed:25561219", "pubmed:31710686", "pubmed:32249824", "pubmed:33196157", "pubmed:33471934", "pubmed:8620561", "pubmed:8767167", "pubmed:9518388", "reaxys:383619", "wikipedia.en:Nicotinamide"], "generalized_empirical_formula": ["C6H6N2O"], "has_alternative_id": ["CHEBI:14645", "CHEBI:25521", "CHEBI:44258", "CHEBI:7556"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17154"], "inchi_key_string": ["DFPAKSUCGFBDDF-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H6N2O/c7-6(9)5-2-1-3-8-4-5/h1-4H,(H2,7,9)"], "mass": ["122.127"], "monoisotopic_mass": ["122.04801"], "smiles_string": ["NC(=O)c1cccnc1"]}, "synonyms": ["3-carbamoylpyridine", "3-pyridinecarboxamide", "Niacinamide", "Nicotinamid", "Nicotinsaeureamid", "Nikotinamid", "Nikotinsaeureamid", "Vitamin PP", "beta-pyridinecarboxamide", "m-(aminocarbonyl)pyridine", "niacin", "niamide", "nicotinamida", "nicotinamide", "nicotinamidum", "nicotine acid amide", "nicotine amide", "nicotinic acid amide", "nicotinic amide", "nicotylamide", "pyridine-3-carboxamide", "pyridine-3-carboxamide", "pyridine-3-carboxylic acid amide", "vitamin B3"], "secondary": {"asserted": {"id": "CHEBI:17154", "label": "nicotinamide"}, "exact_current_rows": [{"label": "Nicotinamide", "match_type": "preferred_term", "identifier": "CHEBI:17154", "preferred_term": "Nicotinamide", "ontology_id": "CHEBI:17154", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[13]", "name": "Choline chloride", "primary": {"id": "CHEBI:133341", "label": "choline chloride"}, "canonical_label": "choline chloride", "label_equal": true, "definition": ["A quaternary ammonium salt with choline cation and chloride anion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:67-48-1", "ppdb:161", "pubmed:12962717", "pubmed:17596274", "pubmed:20396712", "pubmed:24905385", "pubmed:25037344", "pubmed:6196640", "pubmed:8047569", "reaxys:3563126", "vsdb:161", "wikipedia.en:Choline_chloride"], "generalized_empirical_formula": ["C5H14NO.Cl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:133341"], "inchi_key_string": ["SGMZJAMFUVOLNK-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C5H14NO.ClH/c1-6(2,3)4-5-7;/h7H,4-5H2,1-3H3;1H/q+1;/p-1"], "mass": ["139.626"], "monoisotopic_mass": ["139.07639"], "smiles_string": ["C[N+](C)(C)CCO.[Cl-]"]}, "synonyms": ["(2-Hydroxyethyl)trimethylammonium chloride", "(beta-Hydroxyethyl)trimethylammonium chloride", "2-Hydroxy-N,N,N,-trimethylethanaminium chloride", "2-hydroxy-N,N,N-trimethylethanaminium chloride", "2-hydroxy-N,N,N-trimethylethanaminium chloride", "Bilineurin chloride", "Biocolina", "Biocoline", "Chloride de choline", "Chlorure de choline", "Choline chlorhydrate", "Choline hydrochloride", "Cholini chloridum", "Cholinium chloride", "Cloruro de colina", "Hepacholine", "Lipotril", "Luridin chloride", "Paresan", "Trimethyl(2-hydroxyethyl)ammonium chloride", "choline chloride"], "secondary": {"asserted": {"id": "CHEBI:133341", "label": "choline chloride"}, "exact_current_rows": [{"label": "Choline chloride", "match_type": "preferred_term", "identifier": "CHEBI:133341", "preferred_term": "Choline chloride", "ontology_id": "CHEBI:133341", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[14]", "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806", "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3", "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"], "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]}, "synonyms": ["Resazurin"]}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[15]", "name": "NaHCO3", "primary": {"id": "CHEBI:32139", "label": "sodium hydrogencarbonate"}, "canonical_label": "sodium hydrogencarbonate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:144-55-8", "drugbank:DB01390", "kegg.compound:C12603", "kegg.drug:D01203", "ppdb:2873", "wikipedia.en:Sodium_Bicarbonate"], "generalized_empirical_formula": ["CHO3.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32139"], "inchi_key_string": ["UIIMBOGNXHQVGW-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/CH2O3.Na/c2-1(3)4;/h(H2,2,3,4);/q;+1/p-1"], "mass": ["84.006"], "monoisotopic_mass": ["83.98234"], "smiles_string": ["O=C([O-])O.[Na+]"]}, "synonyms": ["E 500", "E-500", "E500", "NaHCO3", "Natriumhydrogenkarbonat", "Sodium bicarbonate", "Sodium hydrogencarbonate", "baking soda", "bicarbonate of soda", "carbonic acid monosodium salt", "sodium acid carbonate", "sodium hydrogen carbonate", "sodium hydrogencarbonate", "sodium hydrogencarbonate"], "secondary": {"asserted": {"id": "CHEBI:32139", "label": "sodium hydrogencarbonate"}, "exact_current_rows": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[16]", "name": "D-Glucose", "primary": {"id": "CHEBI:17634", "label": "D-glucose"}, "canonical_label": "D-glucose", "label_equal": true, "definition": ["A glucose with &lt;small&gt;D&lt;/small&gt;-configuration."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:50-99-7"], "generalized_empirical_formula": ["C6H12O6"], "has_alternative_id": ["CHEBI:12965", "CHEBI:20999"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17634"], "mass": ["180.156"], "monoisotopic_mass": ["180.06339"]}, "synonyms": ["D(+)-glucose", "D-(+)-glucose", "D-gluco-hexose", "D-gluco-hexose", "D-glucose", "D-glucose", "Traubenzucker", "dextrose", "grape sugar"], "secondary": {"asserted": {"id": "CHEBI:17634", "label": "D-glucose"}, "exact_current_rows": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[17]", "name": "L-Cysteine HCl x H2O", "primary": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride hydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of &lt;small&gt;L&lt;/small&gt;-cysteine hydrochloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326", "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"], "inchi_key_string": ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"], "mass": ["175.637"], "monoisotopic_mass": ["175.00699"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]}, "synonyms": ["(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride monohydrate", "Cysteine hydrochloride", "L-Cysteine monohydrate monochloride", "L-cysteine hydrochloride monohydrate", "L-cysteine hydrochloride--water (1/1)", "L-cysteine hydrochloride--water (1/1)"], "secondary": {"asserted": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "exact_current_rows": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[18]", "name": "Na2S x 9 H2O", "primary": {"id": "CHEBI:76209", "label": "sodium sulfide nonahydrate"}, "canonical_label": "sodium sulfide nonahydrate", "label_equal": true, "definition": ["A hydrate with formula Na&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;S·9H&lt;small&gt;&lt;sub&gt;2&lt;/sub&gt;&lt;/small&gt;O."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:1313-84-4", "kegg.drug:D09001", "pubmed:19810706", "reaxys:14636099"], "generalized_empirical_formula": ["9H2O.2Na.S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:76209"], "inchi_key_string": ["ZGHLCBJZQLNUAZ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.9H2O.S/h;;9*1H2;/q2*+1;;;;;;;;;;-2"], "mass": ["240.182"], "monoisotopic_mass": ["240.04669"], "smiles_string": ["O.O.O.O.O.O.O.O.O.[Na+].[Na+].[S-2]"]}, "synonyms": ["Na2S.9H2O", "Sodium sulfide (USP)", "disodium sulfide nonahydrate", "disodium sulfide--water (1/9)", "disodium sulfide--water (1/9)", "sodium monosulfide nonahydrate", "sodium monosulfide.9H2O", "sodium sulfide.9H2O"], "secondary": {"asserted": {"id": "CHEBI:76209", "label": "sodium sulfide nonahydrate"}, "exact_current_rows": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[19]", "name": "Nitrilotriacetic acid", "primary": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "canonical_label": "nitrilotriacetic acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1710776", "cas:139-13-9", "drugbank:DB03040", "gmelin:3726", "kegg.compound:C14695", "pdb-ccd:NTA"], "generalized_empirical_formula": ["C6H9NO6"], "has_alternative_id": ["CHEBI:34889", "CHEBI:44555"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:44557"], "inchi_key_string": ["MGFYIUFZLHCRTH-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"], "mass": ["191.139"], "monoisotopic_mass": ["191.04299"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]}, "synonyms": ["Complexon I", "H3nta", "Komplexon I", "N(CH2-COOH)3", "N,N-bis(carboxymethyl)glycine", "N,N-bis(carboxymethyl)glycine", "NITRILOTRIACETIC ACID", "NTA", "Nitrilotriacetate", "Nitrilotriacetic acid", "Nitrilotriessigsaeure", "Triglycollamic acid", "Trilon A", "alpha,alpha',alpha''-trimethylaminetricarboxylic acid", "nitrilo-2,2',2''-triacetic acid", "tri(carboxymethyl)amine", "triglycine"], "secondary": {"asserted": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "exact_current_rows": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[20]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "canonical_label": "magnesium sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505", "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222", "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"], "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "exact_current_rows": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[21]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "canonical_label": "manganese(II) sulfate monohydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of manganese(II) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-96-5", "kegg.drug:D04854", "pubmed:26097037", "reaxys:13153017", "wikipedia.en:Manganese(II)_sulfate"], "generalized_empirical_formula": ["H2O.Mn.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86364"], "inchi_key_string": ["ISPYRSDWRDQNSW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mn.H2O4S.H2O/c;1-5(2,3)4;/h;(H2,1,2,3,4);1H2/q+2;;/p-2"], "mass": ["169.016"], "monoisotopic_mass": ["168.90034"], "smiles_string": ["O.O=S(=O)([O-])[O-].[Mn+2]"]}, "synonyms": ["Manganese sulfate hydrate", "Manganese sulfate monohydrate", "Manganese sulfate", "Manganous sulfate monohydrate", "MnSO4.H2O", "manganese(2+) sulfate monohydrate", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulphate monohydrate", "manganese(II) sulphate monohydrate"], "secondary": {"asserted": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "exact_current_rows": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[22]", "name": "FeSO4 x 7 H2O", "primary": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "canonical_label": "iron(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used)."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]}, "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O", "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"], "secondary": {"asserted": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[23]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "canonical_label": "cobalt(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of cobalt(2+) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10026-24-1", "pubmed:10504146", "pubmed:12187935", "pubmed:12209163", "pubmed:12579202", "pubmed:12948248", "pubmed:2227161", "pubmed:24359163", "pubmed:25896363", "wikipedia.en:Cobalt(II)_sulfate"], "generalized_empirical_formula": ["Co.7H2O.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91244"], "inchi_key_string": ["MEYVLGVRTYSQHI-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Co.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["281.101"], "monoisotopic_mass": ["280.95888"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Co+2]"]}, "synonyms": ["Cobalt monosulfate heptahydrate", "cobalt sulfate heptahydrate", "cobalt(2+) sulfate--water (1/7)", "cobalt(2+) sulfate--water (1/7)", "cobalt(II) sulfate heptahydrate", "cobaltous sulfate heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[24]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "canonical_label": "zinc sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of zinc sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7446-20-0", "gmelin:47216", "kegg.drug:D01081", "wikipedia.en:Zinc_Sulfate"], "generalized_empirical_formula": ["7H2O.O4S.Zn"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32312"], "inchi_key_string": ["RZLVQBNCHSJZPX-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/H2O4S.7H2O.Zn/c1-5(2,3)4;;;;;;;;/h(H2,1,2,3,4);7*1H2;/q;;;;;;;;+2/p-2"], "mass": ["287.558"], "monoisotopic_mass": ["285.95482"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Zn+2]"]}, "synonyms": ["Zinc sulfate", "ZnSO4.7H2O", "zinc sulfate (1:1) heptahydrate", "zinc sulfate heptahydrate (1:1:7)", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate--water (1/7)", "zinc(2+) sulfate--water (1/7)"], "secondary": {"asserted": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "exact_current_rows": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[25]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "canonical_label": "copper(II) sulfate pentahydrate", "label_equal": true, "definition": ["The pentahydrate of copper(2+) sulfate. A bright blue crystalline solid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-99-8", "kegg.drug:D03613", "pubmed:11407502", "pubmed:12209195", "pubmed:12484481", "pubmed:15040745", "pubmed:15607472", "pubmed:15824790", "pubmed:19346702", "pubmed:2002460", "pubmed:20132934", "pubmed:2913309", "pubmed:3351847", "pubmed:7615984", "pubmed:8878264", "pubmed:9521458", "pubmed:9776063", "reaxys:16499970", "wikipedia.en:Copper(II)_sulfate"], "generalized_empirical_formula": ["Cu.5H2O.O4S"], "has_alternative_id": ["CHEBI:121741", "CHEBI:370227"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31440"], "inchi_key_string": ["JZCCFEFSEZPSOG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Cu.H2O4S.5H2O/c;1-5(2,3)4;;;;;/h;(H2,1,2,3,4);5*1H2/q+2;;;;;;/p-2"], "mass": ["249.684"], "monoisotopic_mass": ["248.93415"], "smiles_string": ["O=S(=O)([O-])[O-].[Cu+2].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H]"]}, "synonyms": ["CuSO4.5H2O", "Cupric sulfate", "copper sulphate(5.H2O)", "copper(2+) sulfate (1:1) pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate--water (1/5)", "copper(2+) sulfate--water (1/5)", "copper(II) sulfate, pentahydrate", "cupric sulfate pentahydrate"], "secondary": {"asserted": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "exact_current_rows": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[26]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "canonical_label": "potassium aluminium sulfate dodecahydrate", "label_equal": true, "definition": ["A hydrate resulting from the the formal combination of anhydrous potassium aluminium sulfate with 12 mol eq. of water."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7784-24-9", "reaxys:14851666", "wikipedia.en:Potassium_alum"], "generalized_empirical_formula": ["Al.12H2O.K.2O4S"], "has_alternative_id": ["CHEBI:31192"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86465"], "inchi_key_string": ["GNHOJBNSNUXZQA-UHFFFAOYSA-J"], "inchi_string": ["InChI=1S/Al.K.2H2O4S.12H2O/c;;2*1-5(2,3)4;;;;;;;;;;;;/h;;2*(H2,1,2,3,4);12*1H2/q+3;+1;;;;;;;;;;;;;;/p-4"], "mass": ["474.386"], "monoisotopic_mass": ["473.97548"], "smiles_string": ["O.O.O.O.O.O.O.O.O.O.O.O.O=S(=O)([O-])[O-].O=S(=O)([O-])[O-].[Al+3].[K+]"]}, "synonyms": ["AlK(SO4)2.12H2O", "Aluminum potassium disulfate dodecahydrate", "Aluminum potassium sulfate dodecahydrate", "Kalinite", "Potash alum dodecahydrate", "Potassium alum dodecahydrate", "Potassium aluminum disulfate dodecahydrate", "aluminium potassium sulfate--water (1/12)", "aluminium potassium sulfate--water (1/12)"], "secondary": {"asserted": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "exact_current_rows": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[27]", "name": "H3BO3", "primary": {"id": "CHEBI:33118", "label": "boric acid"}, "canonical_label": "boric acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["bpdb:2136", "cas:10043-35-3", "cas:11113-50-1", "drugcentral:3035", "gmelin:1585", "kegg.compound:C12486", "kegg.drug:D01089", "molbase:1644", "pdb-ccd:BO3", "ppdb:2136"], "generalized_empirical_formula": ["H3BO3"], "has_alternative_id": ["CHEBI:22911", "CHEBI:31299", "CHEBI:41248"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:33118"], "inchi_key_string": ["KGBXLFKZBHKPEV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"], "mass": ["61.833"], "monoisotopic_mass": ["62.01752"], "smiles_string": ["[H]OB(O[H])O[H]"]}, "synonyms": ["B(OH)3", "BORIC ACID", "Boric acid", "H3BO3", "[B(OH)3]", "boric acid", "boron trihydroxide", "orthoboric acid", "trihydroxidoboron", "trihydroxidoboron"], "secondary": {"asserted": {"id": "CHEBI:33118", "label": "boric acid"}, "exact_current_rows": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[28]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "canonical_label": "sodium molybdate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium molybdate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10102-40-6", "pubmed:20645132", "pubmed:20813395", "pubmed:22663766", "pubmed:3382795", "reaxys:19032996", "wikipedia.en:Sodium_molybdate"], "generalized_empirical_formula": ["2H2O.MoO4.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75213"], "inchi_key_string": ["FDEIWTXVNPKYDL-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/Mo.2Na.2H2O.4O/h;;;2*1H2;;;;/q;2*+1;;;;;2*-1"], "mass": ["241.946"], "monoisotopic_mass": ["243.88573"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]}, "synonyms": ["Disodium molybdate dihydrate", "Molybdic acid, disodium salt, dihydrate", "Na2MoO4.2H2O", "Sodium molybdate(VI) dihydrate", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium orthomolybdate dihydrate"], "secondary": {"asserted": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "exact_current_rows": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[29]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "canonical_label": "disodium selenite pentahydrate", "label_equal": true, "definition": ["A hydrate that is the pentahydrate form of disodium selenite."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:26970-82-1", "pubmed:15259772", "pubmed:15559373", "pubmed:16126997", "pubmed:17873396", "pubmed:24479345", "pubmed:24716537", "reaxys:14666014", "wikipedia.en:Sodium_selenite"], "generalized_empirical_formula": ["5H2O.2Na.O3Se"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131361"], "inchi_key_string": ["TUANAMBRHOLYTH-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"], "mass": ["263.012"], "monoisotopic_mass": ["263.93363"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2SeO3.5H2O", "Selenious acid disodium salt, pentahydrate", "Sodium selenite pentahydrate", "disodium selenite hydrate", "sodium selenite hydrate", "sodium selenite--water (1/5)", "sodium selenite--water (1/5)"], "secondary": {"asserted": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "exact_current_rows": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[30]", "name": "Biotin", "primary": {"id": "CHEBI:15956", "label": "biotin"}, "canonical_label": "biotin", "label_equal": true, "definition": ["An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:58-85-5", "chemspider:149962", "drugbank:DB00121", "drugcentral:373", "foodb.food:FDB014510", "gmelin:1918703", "hmdb:HMDB0000030", "kegg.compound:C00120", "kegg.drug:D00029", "knapsack:C00000756", "lincs.smallmolecule:LSM-3994", "metacyc.compound:BIOTIN", "pdb-ccd:BTN", "pmc:PMC8089577", "pubmed:10064317", "pubmed:10215065", "pubmed:10577274", "pubmed:11435506", "pubmed:11481419", "pubmed:11800048", "pubmed:12055344", "pubmed:12070309", "pubmed:12603856", "pubmed:12803839", "pubmed:15012185", "pubmed:15202718", "pubmed:15272000", "pubmed:15690449", "pubmed:15863846", "pubmed:15899401", "pubmed:15992684", "pubmed:16011464", "pubmed:16195795", "pubmed:16419467", "pubmed:16676358", "pubmed:16677798", "pubmed:16704206", "pubmed:16769720", "pubmed:17297119", "pubmed:1814646", "pubmed:18202531", "pubmed:18452485", "pubmed:18509457", "pubmed:19212411", "pubmed:19319844", "pubmed:19727438", "pubmed:19928962", "pubmed:20967359", "pubmed:20974274", "pubmed:2100006", "pubmed:21248194", "pubmed:21356565", "pubmed:21373679", "pubmed:21596550", "pubmed:21871906", "pubmed:25515858", "pubmed:33346513", "pubmed:33461365", "pubmed:34077272", "pubmed:8333586", "pubmed:8750932", "pubmed:9022537", "pubmed:9038855", "pubmed:9094878", "pubmed:9164991", "pubmed:9176832", "pubmed:9371938", "pubmed:9416479", "reaxys:86838", "wikipedia.en:Biotin"], "generalized_empirical_formula": ["C10H16N2O3S"], "has_alternative_id": ["CHEBI:13905", "CHEBI:22882", "CHEBI:22884", "CHEBI:3108", "CHEBI:41236"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15956"], "inchi_key_string": ["YBJHBAHKTGYVGT-ZKWXMUAHSA-N"], "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"], "mass": ["244.316"], "monoisotopic_mass": ["244.08816"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]}, "synonyms": ["(+)-cis-Hexahydro-2-oxo-1H-thieno[3,4]imidazole-4-valeric acid", "(3aS,4S,6aR)-Hexahydro-2-oxo-1H-thieno[3,4-d]imidazole-4-valeric acid", "5-(2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl)pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "BIOTIN", "Coenzyme R", "D-(+)-biotin", "D-Biotin", "Vitamin H", "biotin", "biotina", "biotine", "biotinum", "cis-(+)-Tetrahydro-2-oxothieno[3,4]imidazoline-4-valeric acid", "cis-Hexahydro-2-oxo-1H-thieno(3,4)imidazole-4-valeric acid", "cis-Tetrahydro-2-oxothieno(3,4-d)imidazoline-4-valeric acid", "vitamin B7"], "secondary": {"asserted": {"id": "CHEBI:15956", "label": "biotin"}, "exact_current_rows": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[31]", "name": "Folic acid", "primary": {"id": "CHEBI:27470", "label": "folic acid"}, "canonical_label": "folic acid", "label_equal": true, "definition": ["An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND606960789", "cas:59-30-3", "chemspider:5815", "drugbank:DB00158", "drugcentral:1231", "foodb.food:FDB014504", "hmdb:HMDB0000121", "kegg.compound:C00504", "kegg.drug:D00070", "knapsack:C00001539", "lincs.smallmolecule:LSM-5355", "metacyc.compound:CPD-12826", "pdb-ccd:FOL", "pubmed:10138938", "pubmed:10897644", "pubmed:10958818", "pubmed:11261364", "pubmed:11451208", "pubmed:11959400", "pubmed:14387833", "pubmed:15321809", "pubmed:15523939", "pubmed:15754725", "pubmed:15797531", "pubmed:15797685", "pubmed:15831910", "pubmed:15990733", "pubmed:16093404", "pubmed:16277678", "pubmed:16380297", "pubmed:16871332", "pubmed:17784727", "pubmed:18788725", "pubmed:19121630", "pubmed:19335717", "pubmed:19355913", "pubmed:24650098", "pubmed:33624660", "pubmed:33965562", "pubmed:33968971", "pubmed:34207319", "pubmed:34219855", "pubmed:7738698", "pubmed:8235383", "pubmed:9040515", "pubmed:9420019", "pubmed:9565830", "pubmed:9683174", "pubmed:9781393", "pubmed:9808640", "pubmed:9808641", "reaxys:100781", "wikipedia.en:Folic_Acid"], "generalized_empirical_formula": ["C19H19N7O6"], "has_alternative_id": ["CHEBI:24075", "CHEBI:42610", "CHEBI:5140", "CHEBI:569217"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:27470"], "inchi_key_string": ["OVBPIULPVIDEAO-LBPRGKRZSA-N"], "inchi_string": ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"], "mass": ["441.404"], "monoisotopic_mass": ["441.13968"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]}, "synonyms": ["(2S)-2-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzamido)pentanedioic acid", "Acfol", "Folate", "Folicet", "Folsaeure", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-[(4-{[(2-amino-4-oxo-1,4-dihydropteridin-6-yl)methyl]amino}phenyl)carbonyl]-L-glutamic acid", "N-pteroyl-L-glutamic acid", "PGA", "PteGlu", "acide folique", "acido folico", "acidum folicum", "folic acid", "pteroyl-L-glutamic acid", "pteroyl-L-monoglutamic acid", "pteroylglutamic acid", "pteroylmonoglutamic acid", "vitamin B11", "vitamin B9", "vitamin Bc", "vitamin Be", "vitamin M"], "secondary": {"asserted": {"id": "CHEBI:27470", "label": "folic acid"}, "exact_current_rows": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[32]", "name": "Pyridoxine hydrochloride", "primary": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "canonical_label": "pyridoxine hydrochloride", "label_equal": true, "definition": ["The hydrochloride salt of pyridoxine."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND500675659", "beilstein:3632435", "cas:58-56-0", "drugbank:DBSALT000151", "foodb.food:FDB000575", "gmelin:1067921", "kegg.drug:D02179", "pubmed:15098856", "pubmed:17416572", "pubmed:17891511", "pubmed:18243627", "pubmed:19481898", "pubmed:20645279", "pubmed:21781646", "pubmed:24421551", "pubmed:27468034", "pubmed:28095734", "pubmed:32460509", "pubmed:33209152", "pubmed:33936292", "pubmed:34140989"], "generalized_empirical_formula": ["C8H11NO3.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30961"], "inchi_key_string": ["ZUFQODAHGAHPFQ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H11NO3.ClH/c1-5-8(12)7(4-11)6(3-10)2-9-5;/h2,10-12H,3-4H2,1H3;1H"], "mass": ["205.641"], "monoisotopic_mass": ["205.05057"], "smiles_string": ["Cc1ncc(CO)c(CO)c1O.Cl"]}, "synonyms": ["2-methyl-3-hydroxy-4,5-bis(hydroxymethyl)pyridine hydrochloride", "3-hydroxy-4,5-dimethylol-alpha-picoline hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "5-hydroxy-6-methyl-3,4-pyridinedimethanol hydrochloride", "pyridoxol hydrochloride", "vitamin B6 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "exact_current_rows": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[33]", "name": "Thiamine HCl", "primary": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "canonical_label": "thiamine hydrochloride", "label_equal": true, "definition": ["A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND605711145", "agr:IND606057536", "beilstein:3642937", "beilstein:3851771", "cas:67-03-8", "chemspider:5967", "drugbank:DBSALT000205", "foodb.food:FDB008416", "gmelin:31154", "gmelin:691133", "kegg.drug:D02094", "pubmed:11548854", "pubmed:12224421", "pubmed:21212548", "pubmed:22305197", "pubmed:24399744", "pubmed:25977858", "pubmed:26616989", "pubmed:27163892", "pubmed:28763984", "pubmed:28784494", "pubmed:30131156", "pubmed:31270735", "pubmed:31664290", "pubmed:32009117", "pubmed:32562525", "pubmed:32824791", "reaxys:17124533"], "generalized_empirical_formula": ["C12H17N4OS.Cl.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:49105"], "inchi_key_string": ["DPJRMOMPQZCRJU-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C12H17N4OS.2ClH/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H/q+1;;/p-1"], "mass": ["337.276"], "monoisotopic_mass": ["336.05784"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1.Cl.[Cl-]"]}, "synonyms": ["3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "thiamin dichloride", "thiamin hydrochloride", "thiamine HCl", "thiamine chloride hydrochloride", "thiamine dichloride", "thiamine(2+) dichloride", "thiaminium chloride hydrochloride", "vitamin B1 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "exact_current_rows": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[34]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015", "label": "riboflavin"}, "canonical_label": "riboflavin", "label_equal": true, "definition": ["&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:83-88-5", "chemspider:431981", "drugbank:DB00140", "drugcentral:2834", "foodb.food:FDB012160", "hmdb:HMDB0000244", "kegg.compound:C00255", "kegg.drug:D00050", "knapsack:C00001552", "lincs.smallmolecule:LSM-4084", "metacyc.compound:RIBOFLAVIN", "patent:US2807611", "patent:US2876169", "pdb-ccd:RBF", "pubmed:10566553", "pubmed:11399071", "pubmed:11606856", "pubmed:12083520", "pubmed:12354259", "pubmed:12927541", "pubmed:14963913", "pubmed:16273338", "pubmed:16460756", "pubmed:16658098", "pubmed:182198", "pubmed:18832377", "pubmed:19169240", "pubmed:19212411", "pubmed:19854891", "pubmed:22770225", "pubmed:2369885", "pubmed:23818044", "pubmed:24643482", "pubmed:24816110", "pubmed:25108762", "pubmed:25468971", "pubmed:25887755", "pubmed:2631092", "pubmed:29937405", "pubmed:3142982", "pubmed:33154451", "pubmed:33304888", "pubmed:33886098", "pubmed:33892358", "pubmed:34156642", "pubmed:3592624", "pubmed:3878498", "pubmed:4019261", "pubmed:6475825", "pubmed:6546833", "pubmed:6650303", "pubmed:7101408", "pubmed:7883462", "pubmed:8487103", "pubmed:8604671", "pubmed:8678471", "pubmed:8976642", "pubmed:9184778", "pubmed:9808225", "pubmed:9874201", "reaxys:97831", "wikipedia.en:Riboflavin"], "generalized_empirical_formula": ["C17H20N4O6"], "has_alternative_id": ["CHEBI:15044", "CHEBI:27299", "CHEBI:45214", "CHEBI:529204", "CHEBI:8843"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17015"], "inchi_key_string": ["AUNGANRZJHBGPY-SCRDCRAPSA-N"], "inchi_string": ["InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23)14(25)12(24)6-22)15-13(18-9)16(26)20-17(27)19-15/h3-4,11-12,14,22-25H,5-6H2,1-2H3,(H,20,26,27)/t11-,12+,14-/m0/s1"], "mass": ["376.369"], "monoisotopic_mass": ["376.13828"], "smiles_string": ["Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)CO)c2cc1C"]}, "synonyms": ["1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol", "5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "6,7-dimethyl-9-D-ribitylisoalloxazine", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine", "7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-ribitylisoalloxazine", "Aqua-Flave", "Beflavin", "Beflavine", "Bisulase", "Dermadram", "E101", "Fiboflavin", "Flavaxin", "Flavin Bb", "Flaxain", "Hyflavin", "Vitamin B2", "lactoflavin", "riboflavin (vit B2)", "riboflavin", "riboflavina", "riboflavine", "riboflavinum", "vitamin B2", "vitamin G", "vitasan B2"], "secondary": {"asserted": {"id": "CHEBI:17015", "label": "riboflavin"}, "exact_current_rows": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[35]", "name": "Nicotinic acid", "primary": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "canonical_label": "nicotinic acid", "label_equal": true, "definition": ["A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND607088605", "cas:59-67-6", "chemspider:913", "drugbank:DB00627", "drugcentral:2835", "foodb.food:FDB001014", "gmelin:3340", "hmdb:HMDB0001488", "kegg.compound:C00253", "kegg.drug:D00049", "knapsack:C00000208", "lincs.smallmolecule:LSM-4676", "metacyc.compound:NIACINE", "pdb-ccd:NIO", "pubmed:10540864", "pubmed:113218", "pubmed:12563315", "pubmed:12789870", "pubmed:135660", "pubmed:14550884", "pubmed:15037193", "pubmed:15183629", "pubmed:15205990", "pubmed:15311728", "pubmed:15627518", "pubmed:15651982", "pubmed:16018787", "pubmed:16172771", "pubmed:16322787", "pubmed:16400392", "pubmed:16449845", "pubmed:16767301", "pubmed:16877271", "pubmed:16945375", "pubmed:18037924", "pubmed:182198", "pubmed:186078", "pubmed:18993152", "pubmed:18996527", "pubmed:19369827", "pubmed:19592242", "pubmed:19678716", "pubmed:19779335", "pubmed:20979384", "pubmed:21632263", "pubmed:22116693", "pubmed:22155410", "pubmed:22229411", "pubmed:22366213", "pubmed:22458880", "pubmed:22770225", "pubmed:24029555", "pubmed:24568240", "pubmed:24675661", "pubmed:24848081", "pubmed:24975217", "pubmed:25040591", "pubmed:25241762", "pubmed:25429652", "pubmed:32954525", "pubmed:33273654", "pubmed:33932650", "pubmed:34066686", "pubmed:34085526", "pubmed:34117670", "pubmed:4033386", "pubmed:4259917", "pubmed:582105", "pubmed:699281", "pubmed:7217784", "pubmed:7581845", "pubmed:8306147", "pubmed:8423912", "pubmed:8679452", "pubmed:9107536", "reaxys:109591", "wikipedia.en:Niacin"], "generalized_empirical_formula": ["C6H5NO2"], "has_alternative_id": ["CHEBI:25538", "CHEBI:44319", "CHEBI:7559"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15940"], "inchi_key_string": ["PVNIIMVLHYAWGP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"], "mass": ["123.111"], "monoisotopic_mass": ["123.03203"], "smiles_string": ["O=C(O)c1cccnc1"]}, "synonyms": ["3-Pyridylcarboxylic acid", "3-carboxylpyridine", "3-carboxypyridine", "3-pyridinecarboxylic acid", "NICOTINIC ACID", "NICOTINIC ACID", "Niacin", "Niacor", "Niaspan", "Nicotinic acid", "Nicotinic acid", "Nicotinsaure", "Nikotinsaeure", "P.P. factor", "PP factor", "acide nicotinique", "acido nicotinico", "acidum nicotinicum", "anti-pellagra vitamin", "beta-pyridinecarboxylic acid", "m-pyridinecarboxylic acid", "nicotinic acid", "nicotinic acid", "pellagra preventive factor", "pyridine-3-carboxylic acid", "pyridine-3-carboxylic acid", "pyridine-beta-carboxylic acid", "pyridine-carboxylique-3", "vitamin B3"], "secondary": {"asserted": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "exact_current_rows": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[36]", "name": "Calcium D-(+)-pantothenate", "primary": {"id": "CHEBI:31345", "label": "Calcium pantothenate"}, "canonical_label": "Calcium pantothenate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:137-08-6", "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278", "pubmed:20553011", "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula": ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"], "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"], "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]}, "synonyms": ["Calcium pantotenate", "Calcium pantothenate", "Calcium pantothenate, d-", "Calpan", "D-ca pantothenate", "D-calcium pantothenate", "NSC-36292", "Pantholin", "Pantothenic acid (as calcium)", "Pantothenic acid calcium salt", "Vitamin b5, calcium salt", "pantotenato de calcio", "pantothenate de calcium"]}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[37]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843", "label": "vitamin B12"}, "canonical_label": "vitamin B12", "label_equal": true, "definition": ["Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives)."], "annotations": {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:176843"]}, "synonyms": ["vitamin B-12", "vitamin B12 vitamer", "vitamin B12 vitamers", "vitamin B12", "vitamins B12"], "secondary": {"asserted": {"id": "CHEBI:176843", "label": "vitamin B12"}, "exact_current_rows": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[38]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "canonical_label": "4-aminobenzoic acid", "label_equal": true, "definition": ["An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:150-13-0", "drugbank:DB02362", "drugcentral:2049", "ecmdb:ECMDB01392", "gmelin:50150", "hmdb:HMDB0001392", "kegg.compound:C00568", "kegg.drug:D02456", "knapsack:C00001401", "pdb-ccd:PAB", "pubmed:12039592", "pubmed:14745019", "pubmed:15115392", "pubmed:1527790", "pubmed:16290145", "pubmed:17149871", "pubmed:17743450", "pubmed:17800214", "pubmed:19469519", "pubmed:22767283", "pubmed:22994574", "pubmed:23063996", "pubmed:23084339", "pubmed:23144588", "pubmed:23471007", "pubmed:3599019", "pubmed:3820215", "pubmed:3950915", "pubmed:8411009", "pubmed:9406595", "reaxys:471605", "wikipedia.en:4-Aminobenzoic_acid", "ymdb:YMDB00493"], "generalized_empirical_formula": ["C7H7NO2"], "has_alternative_id": ["CHEBI:113372", "CHEBI:1783", "CHEBI:20315", "CHEBI:44778"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30753"], "inchi_key_string": ["ALYNCZNDIQEVRV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"], "mass": ["137.138"], "monoisotopic_mass": ["137.04768"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]}, "synonyms": ["1-Amino-4-carboxybenzene", "4-AMINOBENZOIC ACID", "4-AMINOBENZOIC ACID", "4-Amino-benzoic acid", "4-Aminobenzoesaeure", "4-Aminobenzoic acid", "4-Aminobenzoic acid", "4-Carboxyaniline", "4-Carboxyphenylamine", "4-aminobenzoic acid", "4-aminobenzoic acid", "ABEE", "PABA", "gamma-Aminobenzoic acid", "gamma-aminobenzoic acid", "p-Aminobenzoesaeure", "p-aminobenzoic acid", "p-carboxyaniline", "p-carboxyphenylamine", "para-aminobenzoic acid"], "secondary": {"asserted": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "exact_current_rows": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[39]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id": "CHEBI:16494", "label": "lipoic acid"}, "canonical_label": "lipoic acid", "label_equal": true, "definition": ["A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:122410", "cas:62-46-4", "drugbank:DB00166", "drugcentral:4732", "ecmdb:ECMDB01451", "gmelin:720915", "kegg.compound:C00725", "kegg.drug:D00086", "pubmed:15328413", "pubmed:7519986", "pubmed:7548757", "reaxys:81853", "wikipedia.en:Lipoic_acid", "ymdb:YMDB00334"], "generalized_empirical_formula": ["C8H14O2S2"], "has_alternative_id": ["CHEBI:146958", "CHEBI:25058", "CHEBI:6492"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16494"], "inchi_key_string": ["AGBQKNBQESQNJD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H14O2S2/c9-8(10)4-2-1-3-7-5-6-11-12-7/h7H,1-6H2,(H,9,10)"], "mass": ["206.332"], "monoisotopic_mass": ["206.04352"], "smiles_string": ["O=C(O)CCCCC1CCSS1"]}, "synonyms": ["1,2-dithiolane-3-pentanoic acid", "1,2-dithiolane-3-valeric acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)valeric acid", "5-(dithiolan-3-yl)valeric acid", "5-[3-(1,2-dithiolanyl)]pentanoic acid", "6,8-thioctic acid", "6,8-thiotic acid", "6-thioctic acid", "6-thiotic acid", "Acetate-replacing factor", "Biletan", "Lipoic acid", "Thioctansaeure", "Thioctic acid", "Thioctsaeure", "Thioktsaeure", "alpha-Lipoic acid", "alpha-Liponsaeure", "alpha-lipoic acid", "liponic acid"], "secondary": {"asserted": {"id": "CHEBI:16494", "label": "lipoic acid"}, "exact_current_rows": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}], "legacy": []} |
| importer | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions | context_only | Current importer separates source stocks/percentage doses and main ingredients, skips solvent water and prefers provider g_l. Current behavior does not validate or repair these older flat owner values and is not a replay of the historical import. |
| resolver | src/culturemech/enrich/dsmz_resolver.py; merge_composition; _add_enrichment_metadata | context_only | Current resolver copies ingredients, solutions and selected metadata, but not preparation steps in this method; it emits timezone-naive local timestamps. This is relevant writer context, not proof of the exact historical execution. |
| cleanup | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current cleanup collapses equal duplicate amounts or flags disagreement; it no longer sums. The actual owner notes explicitly record four earlier sums across direct and stock values. |
| history | data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml; Every target and maintained owner history and ingredient curation timestamp | refutes | [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "curation_history[0].timestamp", "value": "2026-01-27T01:15:03.fZ", "valid_ISO_datetime": false, "timezone_aware": false}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:07.640681", "valid_ISO_datetime": true, "timezone_aware": false}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "curation_history[2].timestamp", "value": "2026-02-06T05:10:34.477786Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "curation_history[3].timestamp", "value": "2026-03-13T03:09:12.483697Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "curation_history[4].timestamp", "value": "2026-03-13T06:19:37.385850Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "curation_history[5].timestamp", "value": "2026-03-17T06:30:19.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "curation_history[6].timestamp", "value": "2026-03-17T19:45:54.140689+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "curation_history[7].timestamp", "value": "2026-05-20T06:00:52.575341+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "curation_history[8].timestamp", "value": "2026-06-05T07:40:24.499481+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "curation_history[9].timestamp", "value": "2026-06-10T07:46:45.259086+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "curation_history[10].timestamp", "value": "2026-08-06T03:04:55.277889+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "curation_history[11].timestamp", "value": "2026-08-06T03:04:55.277936+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "curation_history[0].timestamp", "value": "2026-01-27T01:15:03.fZ", "valid_ISO_datetime": false, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:07.640681", "valid_ISO_datetime": true, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "curation_history[2].timestamp", "value": "2026-02-06T05:10:34.477786Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "curation_history[3].timestamp", "value": "2026-03-13T03:09:12.483697Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "curation_history[4].timestamp", "value": "2026-03-13T06:19:37.385850Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "curation_history[5].timestamp", "value": "2026-03-17T06:30:19.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "curation_history[6].timestamp", "value": "2026-03-17T19:45:54.140689+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "curation_history[7].timestamp", "value": "2026-05-20T06:00:52.575341+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "curation_history[8].timestamp", "value": "2026-06-05T07:40:24.499481+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path": "curation_history[9].timestamp", "value": "2026-06-10T07:46:45.259086+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "curation_history[0].timestamp", "value": "2026-01-26T17:53:11.569200Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "curation_history[1].timestamp", "value": "2026-02-06T05:10:52.437408Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "curation_history[2].timestamp", "value": "2026-03-13T03:09:39.896308Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "curation_history[3].timestamp", "value": "2026-03-13T06:19:06.368596Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "curation_history[4].timestamp", "value": "2026-03-17T06:30:51.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "curation_history[5].timestamp", "value": "2026-03-17T19:45:18.555904+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "curation_history[6].timestamp", "value": "2026-05-20T06:01:07.006727+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "curation_history[7].timestamp", "value": "2026-06-05T07:40:46.650684+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field_path": "curation_history[8].timestamp", "value": "2026-06-10T07:46:52.354579+00:00", "valid_ISO_datetime": true, "timezone_aware": true}] |
| merge | src/culturemech/merge/merger.py; RecipeMerger; merge_formulation_evidence; maintained formulation-aware merge context | context_only | The target is a generated merge with the exact normalized contributors pinned by inspection. The old ingredient-set fingerprint is not concentration, preparation or source equivalence. Current formulation-aware merging preserves only compatible assertions. No merge was run; verify owners and preview current grouping before separately authorized regeneration. |
| exporter | src/culturemech/export/kgx_export.py; medium_to_ingredient_edge; medium_to_solution_edge; _resolved_ingredient_id; _quantity | context_only | Current export consumes structured ingredient/solution identities and quantities, resolving against the pinned MIM index before fallback. It does not independently recover missing stock stages, source qualifiers or final volume. No export or resulting edge count is claimed. |

## Limits And Additional Notes

- MediaDive declares a 1015 mL main volume. The listed liquid additions total 1014.6 mL, before any unquantified later anoxic-stock additions. Provider normalization is retained as its declared basis, not an independently established final volume.
- All dilution examples are conditional on the explicitly identified provider volume and stock strengths. No corrected numerical concentration is written to the corpus.
- Exact KOMODO accession mapping supports source identity only. No species taxonomy, strain growth, optimal incubation condition or biological aerobic phenotype was inferred from the catalog.
- The primary PDF prints complete stock definitions, so its crossreferences to DSMZ 141 and 120 are assessed through those reproduced stock sections, not through unrelated parent-medium formulations.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- NH4Cl, cysteine hydrochloride monohydrate and sulfide each retain provider g_l 0.295566; strict six-decimal rounding of 0.3/1.015 is 0.295567. This last-digit limit is explicit and no value is silently normalized.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T100353Z-culturemech-005968-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acetitomaculum_medium (CultureMech:005968)'
started_at: '2026-10-21T09:56:38Z'
finished_at: '2026-10-21T10:03:53Z'
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
summary: 'Exact KOMODO 540 and DSMZ 540 sources identify this medium and its two maintained
  contributors. The generated target and both owners flatten two stocks into direct
  concentrations and sum amounts from different preparation stages. Nickel chloride
  hexahydrate and sodium resazurin also have incompatible asserted chemical forms.
  The DSMZ owner preserves the anoxic preparation, while the KOMODO owner and generated
  target omit it and retain an Aerobic: Yes catalog note. All four documented diagnostics
  pass; four historical timestamp instances remain malformed or timezone-naive.'
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
  - path: data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml
    sha256: 255cc0bed27f525e38fd152ca2a9688536aa2af86583f28236377eab163350e8
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml
    sha256: 1c3522b5042c77a99badce26fd9246e96767ed09ade2c3c87fc906e5dd5fe7ac
    role: context
  - path: data/normalized_yaml/bacterial/acetitomaculum_medium.yaml
    sha256: 1905f811e7846230b968434b42ccc1b4ef859d286fca8eae336a4a69905a396c
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
  selection: Task review 141; batch 015 item 1 of 10, selected in Python lexicographic
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
  - CultureMech:005968
targets:
- target_id: CultureMech:005968
  path: data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml
  label: acetitomaculum_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetitomaculum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:005968
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch015/141/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch015/141/strict.tsv"
  target_ids:
  - CultureMech:005968
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:005968
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:005968
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
  - CultureMech:005968
- check_id: scoped-history
  name: Scoped timestamp syntax and timezone inspection
  required: false
  status: failed
  summary: 31 timestamps inspected, 4 invalid or timezone-naive; old provenance remains
    unchanged.
  target_ids:
  - CultureMech:005968
  evidence_ids:
  - history
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T10:03:53Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:03:53Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/acetitomaculum_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:03:53Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:57:26.082119Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch015/141/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T09:57:30.610464Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch015/141/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:57:36.891337Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:57:40.301165Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: source-catalog
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch015/source-preflight-bound/141/source-catalog.json
  locator: Complete bound per-record catalog, raw/text/metadata hashes and actual
    original capture times
  accessed_at: '2026-10-21T10:03:53Z'
  support: context_only
  summary: '[{"key": "komodoMediaList", "url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
    "status": 200, "accessed_at": "2026-10-19T23:42:38.189631Z", "sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a",
    "metadata_sha256": "5ae47834f48dba0f36513d02684ae6d3ea3da54369ea1af0816f5beed8ee4e9e",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/140/komodoMediaList.json"},
    {"key": "dsmz540", "url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf",
    "status": 200, "accessed_at": "2026-10-21T09:46:50.018755Z", "sha256": "cd6c6ccfc802d539f0376010548c985fc6ce8ac4847ea3b2d7a8db172deef2e7",
    "metadata_sha256": "404aecc94a7630eefdbd68fed6015e745d30cb643f3a1fb5f4061a4e28eb852b",
    "content_limit": null, "reused_capture_from": null}, {"key": "mediadive540api",
    "url": "https://mediadive.dsmz.de/rest/medium/540", "status": 200, "accessed_at":
    "2026-10-21T09:46:48.818833Z", "sha256": "71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8",
    "metadata_sha256": "dc3a47da5ca6512bb64e331baad52abac9eb5a0716fb3d85f558cf62bbedae5b",
    "content_limit": null, "reused_capture_from": null}, {"key": "chebi131361", "url":
    "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361",
    "status": 200, "accessed_at": "2026-10-21T07:33:27.980786Z", "sha256": "643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10",
    "metadata_sha256": "138d55ceb95cbfe0acf7201bb4eae4ab07af0fe03c84508c2ef3938ecfc4b2ae",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi131361.json"},
    {"key": "chebi133341", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_133341",
    "status": 200, "accessed_at": "2026-10-21T09:46:50.859176Z", "sha256": "c98da0c6eaa91e6310bb2bb611e829e756e5daf36c1091566dffdd927decad2c",
    "metadata_sha256": "7016ad1cc452cf4a2f46d83de6d6e72d9eef6cadd33652e82aff070f49a0646a",
    "content_limit": null, "reused_capture_from": null}, {"key": "chebi15940", "url":
    "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940",
    "status": 200, "accessed_at": "2026-10-20T06:55:11.874279Z", "sha256": "3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1",
    "metadata_sha256": "ccd1adbb48f9064f617fe0e1c711d9418783efece2365f0d809996f357056838",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15940.json"},
    {"key": "chebi15956", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956",
    "status": 200, "accessed_at": "2026-10-21T08:42:30.425993Z", "sha256": "d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd",
    "metadata_sha256": "0c95f29d357c5632b7ecdd16e0abafbd370595935f299ff000aeb2c7292732cd",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15956.json"},
    {"key": "chebi16494", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494",
    "status": 200, "accessed_at": "2026-10-20T06:55:13.001958Z", "sha256": "aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1",
    "metadata_sha256": "3892bef535e884d560fe3f958457da63e9f8827421ea13a7a0bc83bb2b85220a",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/129/chebi16494.json"},
    {"key": "chebi17015", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015",
    "status": 200, "accessed_at": "2026-10-20T06:55:11.583596Z", "sha256": "f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4",
    "metadata_sha256": "5244e9ca4c3ee1f0d2b9dee9e0e441d575939d1d98f70e5143e087b070ff8691",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi17015.json"},
    {"key": "chebi17154", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17154",
    "status": 200, "accessed_at": "2026-10-21T09:46:50.867358Z", "sha256": "45306ecefbab1f5ece64d269af2560e313330916a57d04fa168f19044dfe37d8",
    "metadata_sha256": "01f55abd61e5e36e372614f5798a00eb8fd821326b4c0e04af63c9c59835cce2",
    "content_limit": null, "reused_capture_from": null}, {"key": "chebi17268", "url":
    "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17268",
    "status": 200, "accessed_at": "2026-10-21T07:16:23.488883Z", "sha256": "0b0cce127edf288993722217ac5a9c05a0bb876b8c34a481b3a41a20ed847888",
    "metadata_sha256": "9d0cfc50ee2bb18ec4fee24c71d594fa5eeb4cc4f7017906675d48ca99b3ac6e",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch008-tail/078/chebi17268.json"},
    {"key": "chebi17634", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634",
    "status": 200, "accessed_at": "2026-10-21T08:42:33.425023Z", "sha256": "d11b31a8e91c3fffe7744f612dab69cdb4e02f42068cd2eb1458acee4503a62f",
    "metadata_sha256": "823621e9d5c44510193f8576b9daa3c609d37e380edec45ffa6d3e071a6bbbc4",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/135/chebi17634.json"},
    {"key": "chebi176843", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843",
    "status": 200, "accessed_at": "2026-10-21T08:17:26.997779Z", "sha256": "b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9",
    "metadata_sha256": "bc634d788a5dcfee20a97e574f01fc036d79198f4f352ed9a665c58b6a139c27",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi176843.json"},
    {"key": "chebi22652", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_22652",
    "status": 200, "accessed_at": "2026-10-21T09:46:50.925101Z", "sha256": "c68de040add50ab599a1ba691b32fc29c32be018d9be69fe785bf045c681ba12",
    "metadata_sha256": "b35765127b999e4a6339858572d0e85da18044275115de6d672d3924276f8242",
    "content_limit": null, "reused_capture_from": null}, {"key": "chebi26710", "url":
    "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710",
    "status": 200, "accessed_at": "2026-10-21T08:42:42.219040Z", "sha256": "2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e",
    "metadata_sha256": "a5aa981220b7ff257c8fa376bc078c656fdb9441a2c751a80c2ee406aa299eb3",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi26710.json"},
    {"key": "chebi27470", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470",
    "status": 200, "accessed_at": "2026-10-20T06:55:10.450814Z", "sha256": "fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f",
    "metadata_sha256": "555d29814a58871f010427bc65a64246287ef8f70ef7479fc990e91b7b994449",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi27470.json"},
    {"key": "chebi30753", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753",
    "status": 200, "accessed_at": "2026-10-20T06:55:12.829785Z", "sha256": "97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a",
    "metadata_sha256": "41064c33af959c4414c4024ed69c380390cf92d289e4eecb77ead20db28b43eb",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi30753.json"},
    {"key": "chebi30961", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961",
    "status": 200, "accessed_at": "2026-10-21T08:42:44.571163Z", "sha256": "f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d",
    "metadata_sha256": "995fa39c43445f662677b9f51c2fd4d3277e38c0e48a4132ba24cd0b288c2797",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi30961.json"},
    {"key": "chebi31206", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206",
    "status": 200, "accessed_at": "2026-10-21T08:17:28.439407Z", "sha256": "ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76",
    "metadata_sha256": "b39788c1cff4fc2c0477e4b621c8361080ec6d810817c5cbf03469abeb0d1c5e",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi31206.json"},
    {"key": "chebi31345", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345",
    "status": 200, "accessed_at": "2026-10-20T06:55:12.450283Z", "sha256": "56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d",
    "metadata_sha256": "d8032b0cee899225ed4bd68c612cdabf64005609adb65b9fe90bb6f8858ae717",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi31345.json"},
    {"key": "chebi31440", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440",
    "status": 200, "accessed_at": "2026-10-21T08:17:28.489501Z", "sha256": "e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9",
    "metadata_sha256": "6529882a5af14272d6b6a6d84fb5d7491494ad5b39e77fd2e78c8976caae47c7",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi31440.json"},
    {"key": "chebi31795", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795",
    "status": 200, "accessed_at": "2026-10-21T08:42:45.232212Z", "sha256": "45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb",
    "metadata_sha256": "b1c7b3fb9390c8507df21d5c6ebe5844d8aec7a45d9e4f06faa1fca81b1e734c",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/140/chebi31795.json"},
    {"key": "chebi32139", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139",
    "status": 200, "accessed_at": "2026-10-21T07:16:24.226823Z", "sha256": "2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe",
    "metadata_sha256": "f0831ae485cbda8dad2d8fd86898a29b1ecc50a8b66baf746916b8c70550be12",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/135/chebi32139.json"},
    {"key": "chebi32149", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149",
    "status": 200, "accessed_at": "2026-10-20T07:18:34.792120Z", "sha256": "49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8",
    "metadata_sha256": "cb6ee285a5c1cdd29b54e5703c2b09c5a8e40185b943bebaba219091a7139ff4",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-work-batch005/sources/chebi32149.json"},
    {"key": "chebi32312", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312",
    "status": 200, "accessed_at": "2026-10-21T08:17:28.879505Z", "sha256": "eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9",
    "metadata_sha256": "10c5840f2d9d4bc7eead8c7932802d70dea909d22b84a3eae2db24decc771f7c",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi32312.json"},
    {"key": "chebi32588", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588",
    "status": 200, "accessed_at": "2026-10-21T08:17:29.045588Z", "sha256": "536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411",
    "metadata_sha256": "84fd80bc5626e941e713cd7853594cd3fb8fe81cec73c96d5d59310a97899de8",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi32588.json"},
    {"key": "chebi33118", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118",
    "status": 200, "accessed_at": "2026-10-21T08:17:29.364390Z", "sha256": "f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87",
    "metadata_sha256": "2923d04cbdf5a6902c6bf2c9e955ce632c93ae8e2434a471d14eda937843d042",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi33118.json"},
    {"key": "chebi34887", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887",
    "status": 200, "accessed_at": "2026-10-21T08:04:44.093348Z", "sha256": "f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc",
    "metadata_sha256": "9705696a27f4729870b5b870d8c1444abc00c65d3d347612b84b85632b8cb1c4",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi34887.json"},
    {"key": "chebi44557", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557",
    "status": 200, "accessed_at": "2026-10-21T08:46:15.250117Z", "sha256": "de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2",
    "metadata_sha256": "feed10fc8ed84d40251835261cafc8decb2a008053459a2690e5ef05886c80ff",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi44557.json"},
    {"key": "chebi49105", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105",
    "status": 200, "accessed_at": "2026-10-20T06:55:10.911379Z", "sha256": "0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4",
    "metadata_sha256": "bd1e98656da4ad0ffa12b011265b26b5fe482f34339e7149bfd9d0c2e39fb7bf",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi49105.json"},
    {"key": "chebi63036", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036",
    "status": 200, "accessed_at": "2026-10-21T08:17:29.666916Z", "sha256": "48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3",
    "metadata_sha256": "1843775fdea6d581cb66b25165bf6af2bd3a85c6fa50d2c5994a3286e78ba892",
    "content_limit": "Identity/provenance and exact identifier metadata only; no operational
    formulation or culture-procedure assessment.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/139/chebi63036.json"},
    {"key": "chebi63939", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939",
    "status": 200, "accessed_at": "2026-10-20T06:55:09.796192Z", "sha256": "987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a",
    "metadata_sha256": "4c37e2dabf6db6e10b0fc6b772539f62bc384372f98ec49b4f201d976074d795",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi63939.json"},
    {"key": "chebi75213", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213",
    "status": 200, "accessed_at": "2026-10-21T08:17:29.756647Z", "sha256": "b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083",
    "metadata_sha256": "a14596f3ed5f8fa7c6c875d74e2cbebe4e54bff8015fd47b6133aea3bc31f841",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/136/chebi75213.json"},
    {"key": "chebi75836", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836",
    "status": 200, "accessed_at": "2026-10-20T06:55:07.038393Z", "sha256": "14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525",
    "metadata_sha256": "694f8da78dabe14df8225398e8ae7a89b065404f2537f45d7aa9d962a8ff52e3",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi75836.json"},
    {"key": "chebi76209", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209",
    "status": 200, "accessed_at": "2026-10-20T06:55:04.847843Z", "sha256": "f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c",
    "metadata_sha256": "a0e76167a80501539f05f6062b393f9d766eb0ea5c3afa19dd19b9cb44bcb5af",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi76209.json"},
    {"key": "chebi86158", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158",
    "status": 200, "accessed_at": "2026-10-21T08:17:30.011607Z", "sha256": "b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61",
    "metadata_sha256": "f54e4f9aa0c2ac289fe12c9c2b129c3920e4a7a840155eb643be8ebd96e24312",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi86158.json"},
    {"key": "chebi86345", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345",
    "status": 200, "accessed_at": "2026-10-21T08:17:30.382026Z", "sha256": "08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133",
    "metadata_sha256": "830c202293bdd9b33596da6ee8d681936953e8f4d6dedfa5f7961b3849897fdf",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi86345.json"},
    {"key": "chebi86364", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364",
    "status": 200, "accessed_at": "2026-10-21T07:33:35.036768Z", "sha256": "f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069",
    "metadata_sha256": "0c1118b30c6e2b638fac40a7713732248bc5cf56e75d08e4b240d24260227605",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/134/chebi86364.json"},
    {"key": "chebi86465", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465",
    "status": 200, "accessed_at": "2026-10-20T06:55:08.054799Z", "sha256": "5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c",
    "metadata_sha256": "1db2987c153637737d264d3e81bf48b00324e32adc78942497f4ba3621f70f21",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi86465.json"},
    {"key": "chebi8806", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806",
    "status": 200, "accessed_at": "2026-10-21T08:17:30.774007Z", "sha256": "e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5",
    "metadata_sha256": "d974cb479c2306995b3f56fd12b92afd92628806b24556d226c3cb7acc229a2c",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi8806.json"},
    {"key": "chebi91244", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244",
    "status": 200, "accessed_at": "2026-10-20T06:55:07.079384Z", "sha256": "dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa",
    "metadata_sha256": "7bcc41c0e2d4ad81aab32a98f42a8d405cd5881fa4653a783906ef034b881014",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-work-batch004/sources/chebi91244.json"},
    {"key": "chebi91248", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248",
    "status": 200, "accessed_at": "2026-10-21T08:42:32.136441Z", "sha256": "7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683",
    "metadata_sha256": "0cc7abb8217070f092c46ab0885d1eaa608a536610e8b15bca2336754018e9cf",
    "content_limit": null, "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/133/chebi91248.json"}]'
  snapshot_sha256: 1ae888b2b8f4500d1ccdb8bacf44d5901f7f1e2e031cd2c2cbba0427a9773d02
- evidence_id: dsmz540
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf
  locator: pages 1–2, entire main recipe and reproduced mineral/vitamin stock sections
  accessed_at: '2026-10-21T09:46:50.018755Z'
  support: supports
  summary: DSMZ 540 ACETITOMACULUM MEDIUM, two-page collection recipe. Both pages
    were inspected visually and in extracted text, including all main and stock rows
    and preparation paragraphs. The footer says ©2022 DSMZ; no individual authors
    or separately verified publication date are supplied.
  snapshot_sha256: cd6c6ccfc802d539f0376010548c985fc6ce8ac4847ea3b2d7a8db172deef2e7
- evidence_id: mediadive540api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.medium; $.data.solutions[0:3]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: 'Exact MediaDive medium 540 dataset response: main solution 1194, mineral
    stock 241 and vitamin stock 5980; complete amounts, units, percentage attributes,
    declared volumes and preparation.'
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: komodoMediaList
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: MediaList table row with first cell 540
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: context_only
  summary: Exact row 540 names ACETITOMACULUM medium and links DSMZ Medium540.pdf.
    It gives pH 6.8–7.0 and the aerobic flag, but supplies no quantities or strain-growth
    evidence.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: quantity-1
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[0]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 1,\n                      \
    \  \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n \
    \                       \"amount\": 0.2,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 0.197044,\n                        \"mmol_l\"\
    : 1.44795,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-2
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[1]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 2,\n                      \
    \  \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n\
    \                        \"amount\": 0.1,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 0.0985222,\n                        \"\
    mmol_l\": 0.693623,\n                        \"optional\": 0\n               \
    \     }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-3
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[2]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 3,\n                      \
    \  \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n  \
    \                      \"amount\": 0.3,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 0.295566,\n                        \"mmol_l\"\
    : 5.52564,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-4
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[3]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 4,\n                      \
    \  \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n    \
    \                    \"amount\": 0.5,\n                        \"unit\": \"g\"\
    ,\n                        \"g_l\": 0.492611,\n                        \"mmol_l\"\
    : 6.60779,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-5
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[4]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 5,\n                      \
    \  \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n   \
    \                     \"amount\": 7,\n                        \"unit\": \"g\"\
    ,\n                        \"g_l\": 6.89655,\n                        \"mmol_l\"\
    : 118.011,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-6
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[5]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 6,\n                      \
    \  \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":\
    \ 79,\n                        \"amount\": 1.2,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 1.18227,\n                        \"\
    mmol_l\": 5.81529,\n                        \"optional\": 0\n                \
    \    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-7
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[6]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 7,\n                      \
    \  \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":\
    \ 7,\n                        \"amount\": 0.15,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.147783,\n                       \
    \ \"mmol_l\": 1.00523,\n                        \"optional\": 0\n            \
    \        }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-8
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[7]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 8,\n                      \
    \  \"compound\": \"Yeast extract\",\n                        \"compound_id\":\
    \ 16,\n                        \"amount\": 1.5,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 1.47783,\n                        \"\
    optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-9
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[8]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The main recipe explicitly adds 10 ml of stock 241. Restore this dose and
    the separate stock definition; the stored flat ingredient strengths do not encode
    its dilution.
  quote: "{\n                        \"recipe_order\": 9,\n                      \
    \  \"solution\": \"Modified Wolin's mineral solution\",\n                    \
    \    \"solution_id\": 241,\n                        \"amount\": 10,\n        \
    \                \"unit\": \"ml\",\n                        \"optional\": 0\n\
    \                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-10
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[9]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 10,\n                     \
    \   \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\"\
    : 40,\n                        \"attribute\": \"0.1% w/v\",\n                \
    \        \"amount\": 1,\n                        \"unit\": \"ml\",\n         \
    \               \"g_l\": 0.000985222,\n                        \"mmol_l\": 0.00760208,\n\
    \                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-11
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[10]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 11,\n                     \
    \   \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\"\
    : 249,\n                        \"attribute\": \"0.1% w/v\",\n               \
    \         \"amount\": 0.1,\n                        \"unit\": \"ml\",\n      \
    \                  \"g_l\": 9.85222e-5,\n                        \"mmol_l\": 0.000298688,\n\
    \                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-12
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[11]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 12,\n                     \
    \   \"compound\": \"Ascorbic acid\",\n                        \"compound_id\"\
    : 112,\n                        \"attribute\": \"0.01% w/v\",\n              \
    \          \"amount\": 0.5,\n                        \"unit\": \"ml\",\n     \
    \                   \"g_l\": 4.92611e-5,\n                        \"mmol_l\":\
    \ 0.000279702,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-13
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[12]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 13,\n                     \
    \   \"compound\": \"Myo-inositol\",\n                        \"compound_id\":\
    \ 557,\n                        \"attribute\": \"0.01% w/v\",\n              \
    \          \"amount\": 0.5,\n                        \"unit\": \"ml\",\n     \
    \                   \"g_l\": 4.92611e-5,\n                        \"mmol_l\":\
    \ 0.00027343,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-14
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[13]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 14,\n                     \
    \   \"compound\": \"Niacinamide\",\n                        \"compound_id\": 558,\n\
    \                        \"attribute\": \"0.01% w/v\",\n                     \
    \   \"amount\": 0.5,\n                        \"unit\": \"ml\",\n            \
    \            \"g_l\": 4.92611e-5,\n                        \"mmol_l\": 0.000403366,\n\
    \                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-15
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[14]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 15,\n                     \
    \   \"compound\": \"Choline chloride\",\n                        \"compound_id\"\
    : 115,\n                        \"attribute\": \"0.01% w/v\",\n              \
    \          \"amount\": 0.5,\n                        \"unit\": \"ml\",\n     \
    \                   \"g_l\": 4.92611e-5,\n                        \"mmol_l\":\
    \ 0.000352823,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-16
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[15]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 16,\n                     \
    \   \"compound\": \"Sodium resazurin\",\n                        \"compound_id\"\
    : 1852,\n                        \"attribute\": \"0.1% w/v\",\n              \
    \          \"amount\": 0.5,\n                        \"unit\": \"ml\",\n     \
    \                   \"g_l\": 0.000492611,\n                        \"mmol_l\"\
    : 0.00196126,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-17
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[16]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 17,\n                     \
    \   \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n\
    \                        \"amount\": 4,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 3.94089,\n                        \"mmol_l\"\
    : 46.9114,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-18
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[17]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 18,\n                     \
    \   \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n\
    \                        \"amount\": 5,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 4.92611,\n                        \"mmol_l\"\
    : 27.343,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-19
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[18]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The main recipe explicitly adds 1 ml of stock 5980. Restore this dose and
    the separate stock definition; the stored flat ingredient strengths do not encode
    its dilution.
  quote: "{\n                        \"recipe_order\": 19,\n                     \
    \   \"solution\": \"Wolin's vitamin solution (10x)\",\n                      \
    \  \"solution_id\": 5980,\n                        \"amount\": 1,\n          \
    \              \"unit\": \"ml\",\n                        \"optional\": 0\n  \
    \                  }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-20
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[19]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 20,\n                     \
    \   \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\"\
    : 770,\n                        \"amount\": 0.3,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.295566,\n                       \
    \ \"mmol_l\": 1.68284,\n                        \"optional\": 0\n            \
    \        }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-21
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[20]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 21,\n                     \
    \   \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":\
    \ 54,\n                        \"amount\": 0.3,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.295566,\n                       \
    \ \"mmol_l\": 1.23059,\n                        \"optional\": 0\n            \
    \        }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-22
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[0].recipe[21]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: Preserve the source solvent quantity 1000 ml in its own stage. The provider
    declares this solution volume as 1015 mL; water addition is not independent proof
    of measured final volume.
  quote: "{\n                        \"recipe_order\": 22,\n                     \
    \   \"compound\": \"Distilled water\",\n                        \"compound_id\"\
    : 4,\n                        \"amount\": 1000,\n                        \"unit\"\
    : \"ml\",\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-23
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[0]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 1,\n                      \
    \  \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\"\
    : 189,\n                        \"amount\": 1.5,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\"\
    : 7.84765,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-24
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[1]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 2,\n                      \
    \  \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":\
    \ 8,\n                        \"amount\": 3,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\"\
    : 12.1716,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-25
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[2]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 3,\n                      \
    \  \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n\
    \                        \"amount\": 0.5,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\"\
    : 2.9583,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-26
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[3]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 4,\n                      \
    \  \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n   \
    \                     \"amount\": 1,\n                        \"unit\": \"g\"\
    ,\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n\
    \                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-27
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[4]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 5,\n                      \
    \  \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":\
    \ 12,\n                        \"amount\": 0.1,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\"\
    : 0.359693,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-28
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[5]
  accessed_at: '2026-10-21T09:46:48.818833Z'
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
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-29
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[6]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 7,\n                      \
    \  \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":\
    \ 7,\n                        \"amount\": 0.1,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\"\
    : 0.680203,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-30
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[7]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 8,\n                      \
    \  \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":\
    \ 35,\n                        \"amount\": 0.18,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\"\
    : 0.625954,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-31
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[8]
  accessed_at: '2026-10-21T09:46:48.818833Z'
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
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-32
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[9]
  accessed_at: '2026-10-21T09:46:48.818833Z'
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
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-33
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[10]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 11,\n                     \
    \   \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n \
    \                       \"amount\": 0.01,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\"\
    : 0.161708,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-34
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[11]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 12,\n                     \
    \   \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\"\
    : 9,\n                        \"amount\": 0.01,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\"\
    : 0.0413309,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-35
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[12]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 13,\n                     \
    \   \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\"\
    : 40,\n                        \"amount\": 0.03,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\"\
    : 0.231483,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-36
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[13]
  accessed_at: '2026-10-21T09:46:48.818833Z'
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
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-37
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[14]
  accessed_at: '2026-10-21T09:46:48.818833Z'
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
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-38
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[1].recipe[15]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: Preserve the source solvent quantity 1000 ml in its own stage. The provider
    declares this solution volume as 1000 mL; water addition is not independent proof
    of measured final volume.
  quote: "{\n                        \"recipe_order\": 16,\n                     \
    \   \"compound\": \"Distilled water\",\n                        \"compound_id\"\
    : 4,\n                        \"amount\": 1000,\n                        \"unit\"\
    : \"ml\",\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-39
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[2].recipe[0]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 1,\n                      \
    \  \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n \
    \                       \"amount\": 20,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\"\
    : 0.0818632,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-40
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[2].recipe[1]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 2,\n                      \
    \  \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n\
    \                        \"amount\": 20,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\"\
    : 0.0453104,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-41
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[2].recipe[2]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 3,\n                      \
    \  \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\"\
    : 519,\n                        \"amount\": 100,\n                        \"unit\"\
    : \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\"\
    : 0.486287,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-42
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[2].recipe[3]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 4,\n                      \
    \  \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n\
    \                        \"amount\": 50,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\"\
    : 0.148236,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-43
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[2].recipe[4]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 5,\n                      \
    \  \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n\
    \                        \"amount\": 50,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\"\
    : 0.132837,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-44
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[2].recipe[5]
  accessed_at: '2026-10-21T09:46:48.818833Z'
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
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-45
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[2].recipe[6]
  accessed_at: '2026-10-21T09:46:48.818833Z'
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
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-46
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[2].recipe[7]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 8,\n                      \
    \  \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n\
    \                        \"amount\": 1,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\"\
    : 0.00073779,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-47
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[2].recipe[8]
  accessed_at: '2026-10-21T09:46:48.818833Z'
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
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-48
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[2].recipe[9]
  accessed_at: '2026-10-21T09:46:48.818833Z'
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
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-49
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/540
  locator: $.data.solutions[2].recipe[10]
  accessed_at: '2026-10-21T09:46:48.818833Z'
  support: supports
  summary: Preserve the source solvent quantity 1000 ml in its own stage. The provider
    declares this solution volume as 1000 mL; water addition is not independent proof
    of measured final volume.
  quote: "{\n                        \"recipe_order\": 11,\n                     \
    \   \"compound\": \"Distilled water\",\n                        \"compound_id\"\
    : 4,\n                        \"amount\": 1000,\n                        \"unit\"\
    : \"ml\",\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 71a6889efa136d259ed055ac5c05d8156c0a4ff245f0f1ebd251da89e24a25c8
- evidence_id: quantity-50
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf
  locator: pages 1–2, relevant preparation paragraph
  accessed_at: '2026-10-21T09:46:50.018755Z'
  support: supports
  summary: KOH is used to set pH 6.5 and then final stock pH 7.0. No fixed KOH mass
    or volume is specified; do not infer zero or a typical dose.
  quote: First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then
    add minerals. Adjust
  snapshot_sha256: cd6c6ccfc802d539f0376010548c985fc6ce8ac4847ea3b2d7a8db172deef2e7
- evidence_id: quantity-51
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf
  locator: pages 1–2, relevant preparation paragraph
  accessed_at: '2026-10-21T09:46:50.018755Z'
  support: supports
  summary: The named glucose, vitamin, cysteine and sulfide amounts remain explicit
    above; this preparation passage does not specify all later anoxic-stock volumes.
    They cannot be used to claim an independently measured final receiving volume.
  quote: and autoclave. Add glucose, vitamins, cysteine and sulfide from sterile anoxic
    stock
  snapshot_sha256: cd6c6ccfc802d539f0376010548c985fc6ce8ac4847ea3b2d7a8db172deef2e7
- evidence_id: quantity-52
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf
  locator: page 1, main preparation sentence 2
  accessed_at: '2026-10-21T09:46:50.018755Z'
  support: supports
  summary: Preserve the explicit initial pH 6.8 adjustment; it is separate from final
    complete-medium pH.
  quote: Add solid bicarbonate and equilibrate pH to 6.8 with 80% N2 and 20% CO2 gas
    mixture,
  snapshot_sha256: cd6c6ccfc802d539f0376010548c985fc6ce8ac4847ea3b2d7a8db172deef2e7
- evidence_id: quantity-53
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf
  locator: page 1, final main preparation sentence
  accessed_at: '2026-10-21T09:46:50.018755Z'
  support: supports
  summary: The existing 6.8–7.0 range matches the exact source and each owner; retain
    its complete-medium and if-necessary scope.
  quote: filtration. Adjust pH of complete medium to 6.8 - 7.0, if necessary.
  snapshot_sha256: cd6c6ccfc802d539f0376010548c985fc6ce8ac4847ea3b2d7a8db172deef2e7
- evidence_id: quantity-54
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf
  locator: page 1, first preparation sentence
  accessed_at: '2026-10-21T09:46:50.018755Z'
  support: supports
  summary: Restore the explicitly stated 80% N2 / 20% CO2 preparation atmosphere;
    it is not an organism incubation phenotype.
  quote: sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make
    it anoxic.
  snapshot_sha256: cd6c6ccfc802d539f0376010548c985fc6ce8ac4847ea3b2d7a8db172deef2e7
- evidence_id: quantity-55
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf
  locator: page 1, first preparation sentence
  accessed_at: '2026-10-21T09:46:50.018755Z'
  support: supports
  summary: Restore the literal 30–45 min interval; do not replace the range by a midpoint.
  quote: sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make
    it anoxic.
  snapshot_sha256: cd6c6ccfc802d539f0376010548c985fc6ce8ac4847ea3b2d7a8db172deef2e7
- evidence_id: quantity-56
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium540.pdf
  locator: page 1, later stock preparation sentence
  accessed_at: '2026-10-21T09:46:50.018755Z'
  support: supports
  summary: The later glucose, vitamin, cysteine and sulfide stocks are prepared under
    100% N2. Preserve this distinct stage and the following vitamin filtration instruction.
  quote: solutions prepared under 100% N2 gas atmosphere. Vitamins should be sterilized
    by
  snapshot_sha256: cd6c6ccfc802d539f0376010548c985fc6ce8ac4847ea3b2d7a8db172deef2e7
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
- evidence_id: chebi32149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-20T07:18:34.792120Z'
  support: supports
  summary: CHEBI:32149 resolves to sodium sulfate and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: CHEBI:31206 resolves to ammonium chloride and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: CHEBI:32588 resolves to potassium chloride and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
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
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: CHEBI:86345 resolves to magnesium dichloride hexahydrate and is not obsolete.
    Available definitions, formulae, structures and synonyms were inspected; recipe
    amounts and supplied forms are assessed separately.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
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
- evidence_id: chebi22652
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_22652
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T09:46:50.925101Z'
  support: supports
  summary: CHEBI:22652 resolves to ascorbic acid and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: c68de040add50ab599a1ba691b32fc29c32be018d9be69fe785bf045c681ba12
- evidence_id: chebi17268
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17268
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T07:16:23.488883Z'
  support: supports
  summary: CHEBI:17268 resolves to myo-inositol and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: 0b0cce127edf288993722217ac5a9c05a0bb876b8c34a481b3a41a20ed847888
- evidence_id: chebi17154
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17154
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T09:46:50.867358Z'
  support: supports
  summary: CHEBI:17154 resolves to nicotinamide and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: 45306ecefbab1f5ece64d269af2560e313330916a57d04fa168f19044dfe37d8
- evidence_id: chebi133341
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_133341
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T09:46:50.859176Z'
  support: supports
  summary: CHEBI:133341 resolves to choline chloride and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: c98da0c6eaa91e6310bb2bb611e829e756e5daf36c1091566dffdd927decad2c
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
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: CHEBI:32139 resolves to sodium hydrogencarbonate and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi17634
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T08:42:33.425023Z'
  support: supports
  summary: CHEBI:17634 resolves to D-glucose and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: d11b31a8e91c3fffe7744f612dab69cdb4e02f42068cd2eb1458acee4503a62f
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
  accessed_at: '2026-10-21T10:03:53Z'
  support: supports
  summary: '{"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count":
    9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id",
    "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech",
    "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5",
    "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"},
    "counts": {"target": {"ingredient_instances": 40, "primary_CHEBI_instances": 39,
    "secondary_current_asserted_instances": 37, "secondary_current_verified_instances":
    37, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.5, "secondary_verified_percent":
    92.5}, "owner-0": {"ingredient_instances": 40, "primary_CHEBI_instances": 39,
    "secondary_current_asserted_instances": 37, "secondary_current_verified_instances":
    37, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.5, "secondary_verified_percent":
    92.5}, "owner-1": {"ingredient_instances": 40, "primary_CHEBI_instances": 39,
    "secondary_current_asserted_instances": 37, "secondary_current_verified_instances":
    37, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.5, "secondary_verified_percent":
    92.5}}, "instances": [{"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[0]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036",
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
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[1]", "name": "Na2SO4", "primary": {"id": "CHEBI:32149",
    "label": "sodium sulfate"}, "canonical_label": "sodium sulfate", "label_equal":
    true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7757-82-6", "kegg.compound:C13199", "kegg.drug:D01732"], "generalized_empirical_formula":
    ["2Na.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32149"], "inchi_key_string":
    ["PMZURENOXWZQFD-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2Na.H2O4S/c;;1-5(2,3)4/h;;(H2,1,2,3,4)/q2*+1;/p-2"],
    "mass": ["142.043"], "monoisotopic_mass": ["141.93127"], "smiles_string": ["O=S(=O)([O-])[O-].[Na+].[Na+]"]},
    "synonyms": ["Na2SO4", "Natriumsulfat", "Sodium sulfate", "disodium sulfate",
    "disodium sulphate", "salt cake", "sodium sulfate", "sodium sulfate", "sodium
    sulfate, anhydrous", "sodium sulphate"], "secondary": {"asserted": {"id": "CHEBI:32149",
    "label": "sodium sulfate"}, "exact_current_rows": [{"label": "Na2SO4", "match_type":
    "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id":
    "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field":
    "ingredients[2]", "name": "NH4Cl", "primary": {"id": "CHEBI:31206", "label": "ammonium
    chloride"}, "canonical_label": "ammonium chloride", "label_equal": true, "definition":
    ["An inorganic chloride having ammonium as the counterion."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:12125-02-9", "gmelin:10120", "kegg.compound:C12538",
    "kegg.drug:D01139", "wikipedia.en:Ammonium_Chloride"], "generalized_empirical_formula":
    ["Cl.H4N"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31206"], "inchi_key_string":
    ["NLXLAEXVIDQMFP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/ClH.H3N/h1H;1H3"],
    "mass": ["53.492"], "monoisotopic_mass": ["53.00323"], "smiles_string": ["[Cl-].[H][N+]([H])([H])[H]"]},
    "synonyms": ["Ammonium chloride", "Ammoniumchlorid", "NH4Cl", "[NH4]Cl", "ammonium
    chloride", "ammonium chloride", "azanium chloride"], "secondary": {"asserted":
    {"id": "CHEBI:31206", "label": "ammonium chloride"}, "exact_current_rows": [{"label":
    "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term":
    "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[3]", "name": "KCl", "primary": {"id": "CHEBI:32588", "label":
    "potassium chloride"}, "canonical_label": "potassium chloride", "label_equal":
    true, "definition": ["A metal chloride salt with a K(+) counterion."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7447-40-7", "drugbank:DB00761",
    "kegg.drug:D02060", "metacyc.compound:KCL", "molbase:881", "reaxys:3534978", "wikipedia.en:Potassium_Chloride"],
    "generalized_empirical_formula": ["Cl.K"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:32588"], "inchi_key_string": ["WCUXLLCKKVVCTQ-UHFFFAOYSA-M"], "inchi_string":
    ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "monoisotopic_mass": ["73.93256"],
    "smiles_string": ["[Cl-].[K+]"]}, "synonyms": ["KCl", "Kaliumchlorid", "Kaon-Cl
    10", "Klor-con", "Klotrix", "Monopotassium chloride", "[KCl]", "muriate of potash",
    "potassium chloride", "potassium chloride", "sylvite"], "secondary": {"asserted":
    {"id": "CHEBI:32588", "label": "potassium chloride"}, "exact_current_rows": [{"label":
    "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[4]", "name": "NaCl", "primary": {"id": "CHEBI:26710", "label":
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
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[5]", "name": "MgCl2 x 6 H2O", "primary": {"id": "CHEBI:86345",
    "label": "magnesium dichloride hexahydrate"}, "canonical_label": "magnesium dichloride
    hexahydrate", "label_equal": true, "definition": ["A hydrate that is the hexahydrate
    form of magnesium dichloride."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7791-18-6", "kegg.drug:D04834", "pubmed:24831644", "pubmed:25148974", "pubmed:25430969",
    "reaxys:11343754"], "generalized_empirical_formula": ["2Cl.6H2O.Mg"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:86345"], "inchi_key_string": ["DHRRIBDTHFBPNG-UHFFFAOYSA-L"],
    "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass":
    ["203.301"], "monoisotopic_mass": ["201.98614"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]},
    "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride
    hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate",
    "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"], "secondary":
    {"asserted": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"},
    "exact_current_rows": [{"label": "Magnesium chloride", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[6]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[7]", "name": "Yeast extract"}, {"layer": "target", "path":
    "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[8]",
    "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887", "label": "nickel dichloride"},
    "canonical_label": "nickel dichloride", "label_equal": true, "definition": ["A
    compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation
    state) to chloride is 1:2."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7718-54-9", "kegg.compound:C14711", "pubmed:11739495", "pubmed:12603851",
    "pubmed:21928331", "pubmed:23179351", "pubmed:23622879", "pubmed:23702803", "pubmed:23735035",
    "pubmed:7671317", "reaxys:3902827", "reaxys:8128171", "wikipedia.en:Nickel_dichloride"],
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
    "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field":
    "ingredients[9]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939", "label":
    "sodium tungstate dihydrate"}, "canonical_label": "sodium tungstate dihydrate",
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
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[10]", "name": "Ascorbic acid", "primary": {"id": "CHEBI:22652",
    "label": "ascorbic acid"}, "canonical_label": "ascorbic acid", "label_equal":
    true, "definition": [], "annotations": {"has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:22652"]}, "synonyms": [], "secondary": {"asserted": {"id": "CHEBI:22652",
    "label": "ascorbic acid"}, "exact_current_rows": [{"label": "Ascorbic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:22652", "preferred_term": "Ascorbic acid",
    "ontology_id": "CHEBI:22652", "mapping_status": "MAPPED", "ambiguity": "unique"}]}},
    {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[11]", "name": "Myo-inositol", "primary": {"id": "CHEBI:17268",
    "label": "myo-inositol"}, "canonical_label": "myo-inositol", "label_equal": true,
    "definition": ["An inositol having <i>myo</i>- configuration."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:87-89-8", "drugbank:DB03106",
    "drugcentral:1444", "gmelin:82918", "hmdb:HMDB0000211", "kegg.compound:C00137",
    "kegg.drug:D08079", "knapsack:C00001164", "metacyc.compound:MYO-INOSITOL", "pdb-ccd:INS",
    "pubmed:11034685", "pubmed:11244303", "pubmed:11323092", "pubmed:11772411", "pubmed:12478879",
    "pubmed:12832083", "pubmed:14583919", "pubmed:14681857", "pubmed:15181167", "pubmed:15295080",
    "pubmed:15558078", "pubmed:16410747", "pubmed:1694860", "pubmed:17439666", "pubmed:17722064",
    "pubmed:18650262", "pubmed:18854045", "pubmed:19097871", "pubmed:19383710", "pubmed:22285975",
    "pubmed:22461977", "pubmed:22517104", "pubmed:838172", "reaxys:1907329", "wikipedia.en:Inositol"],
    "generalized_empirical_formula": ["C6H12O6"], "has_alternative_id": ["CHEBI:10601",
    "CHEBI:12826", "CHEBI:12831", "CHEBI:25451", "CHEBI:43559"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:17268"], "inchi_key_string": ["CDAISMWEOUEBRE-GPIVLXJGSA-N"],
    "inchi_string": ["InChI=1S/C6H12O6/c7-1-2(8)4(10)6(12)5(11)3(1)9/h1-12H/t1-,2-,3-,4+,5-,6-"],
    "mass": ["180.156"], "monoisotopic_mass": ["180.06339"], "smiles_string": ["O[C@H]1[C@H](O)[C@@H](O)[C@H](O)[C@@H](O)[C@H]1O"]},
    "synonyms": ["(1r,2R,3S,4s,5R,6S)-cyclohexane-1,2,3,4,5,6-hexol", "1,2,3,4,5,6-HEXAHYDROXY-CYCLOHEXANE",
    "1,2,3,5/4,6-cyclohexanehexol", "1D-myo-Inositol", "1L-myo-Inositol", "Bios I",
    "Cyclohexitol", "D-myo-Inositol", "Dambose", "Inositol", "Ins", "L-myo-Inositol",
    "Meat sugar", "Myoinositol", "cis-1,2,3,5-trans-4,6-cyclohexanehexol", "i-inositol",
    "inosite", "meso-Inositol", "myo-Inositol", "myo-Inositol", "myo-inositol", "myo-inositol"],
    "secondary": {"asserted": {"id": "CHEBI:17268", "label": "myo-inositol"}, "exact_current_rows":
    [{"label": "myo-Inositol", "match_type": "preferred_term", "identifier": "CHEBI:17268",
    "preferred_term": "myo-Inositol", "ontology_id": "CHEBI:17268", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[12]", "name": "Niacinamide", "primary": {"id": "CHEBI:17154",
    "label": "nicotinamide"}, "canonical_label": "nicotinamide", "label_equal": true,
    "definition": ["A pyridinecarboxamide that is pyridine in which the hydrogen at
    position 3 is replaced by a carboxamide group."], "annotations": {"charge": [0.0],
    "database_cross_reference": ["cas:98-92-0", "drugbank:DB02701", "drugcentral:1906",
    "foodb.food:FDB012485", "gmelin:3336", "hmdb:HMDB0001406", "kegg.compound:C00153",
    "kegg.drug:D00036", "knapsack:C00000209", "lincs.smallmolecule:LSM-5428", "metacyc.compound:NIACINAMIDE",
    "patent:US2904552", "patent:US2993051", "pdb-ccd:NCA", "pubmed:10884473", "pubmed:11355130",
    "pubmed:11814060", "pubmed:12014919", "pubmed:12487919", "pubmed:12519385", "pubmed:12709297",
    "pubmed:12782109", "pubmed:12890690", "pubmed:14729974", "pubmed:14757966", "pubmed:14871431",
    "pubmed:15497767", "pubmed:15563975", "pubmed:15780941", "pubmed:15807725", "pubmed:15834926",
    "pubmed:15995937", "pubmed:16029679", "pubmed:16209160", "pubmed:16596767", "pubmed:16766489",
    "pubmed:16871361", "pubmed:17021258", "pubmed:17129213", "pubmed:18234191", "pubmed:18316796",
    "pubmed:18368629", "pubmed:18373238", "pubmed:18389009", "pubmed:18514428", "pubmed:18930755",
    "pubmed:18987186", "pubmed:19212411", "pubmed:19539713", "pubmed:19544437", "pubmed:2026685",
    "pubmed:21503886", "pubmed:21891976", "pubmed:21918528", "pubmed:21926578", "pubmed:22067079",
    "pubmed:22160932", "pubmed:22207684", "pubmed:22232263", "pubmed:22281243", "pubmed:22359146",
    "pubmed:22361740", "pubmed:22407380", "pubmed:22456321", "pubmed:22536229", "pubmed:22543086",
    "pubmed:22626821", "pubmed:22699421", "pubmed:22709272", "pubmed:22763693", "pubmed:22770225",
    "pubmed:23016598", "pubmed:23028781", "pubmed:23043891", "pubmed:23047329", "pubmed:24027187",
    "pubmed:24077178", "pubmed:24559077", "pubmed:24635573", "pubmed:25504347", "pubmed:25561219",
    "pubmed:31710686", "pubmed:32249824", "pubmed:33196157", "pubmed:33471934", "pubmed:8620561",
    "pubmed:8767167", "pubmed:9518388", "reaxys:383619", "wikipedia.en:Nicotinamide"],
    "generalized_empirical_formula": ["C6H6N2O"], "has_alternative_id": ["CHEBI:14645",
    "CHEBI:25521", "CHEBI:44258", "CHEBI:7556"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:17154"], "inchi_key_string": ["DFPAKSUCGFBDDF-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/C6H6N2O/c7-6(9)5-2-1-3-8-4-5/h1-4H,(H2,7,9)"], "mass": ["122.127"],
    "monoisotopic_mass": ["122.04801"], "smiles_string": ["NC(=O)c1cccnc1"]}, "synonyms":
    ["3-carbamoylpyridine", "3-pyridinecarboxamide", "Niacinamide", "Nicotinamid",
    "Nicotinsaeureamid", "Nikotinamid", "Nikotinsaeureamid", "Vitamin PP", "beta-pyridinecarboxamide",
    "m-(aminocarbonyl)pyridine", "niacin", "niamide", "nicotinamida", "nicotinamide",
    "nicotinamidum", "nicotine acid amide", "nicotine amide", "nicotinic acid amide",
    "nicotinic amide", "nicotylamide", "pyridine-3-carboxamide", "pyridine-3-carboxamide",
    "pyridine-3-carboxylic acid amide", "vitamin B3"], "secondary": {"asserted": {"id":
    "CHEBI:17154", "label": "nicotinamide"}, "exact_current_rows": [{"label": "Nicotinamide",
    "match_type": "preferred_term", "identifier": "CHEBI:17154", "preferred_term":
    "Nicotinamide", "ontology_id": "CHEBI:17154", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[13]", "name": "Choline chloride", "primary": {"id": "CHEBI:133341",
    "label": "choline chloride"}, "canonical_label": "choline chloride", "label_equal":
    true, "definition": ["A quaternary ammonium salt with choline cation and chloride
    anion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:67-48-1",
    "ppdb:161", "pubmed:12962717", "pubmed:17596274", "pubmed:20396712", "pubmed:24905385",
    "pubmed:25037344", "pubmed:6196640", "pubmed:8047569", "reaxys:3563126", "vsdb:161",
    "wikipedia.en:Choline_chloride"], "generalized_empirical_formula": ["C5H14NO.Cl"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:133341"], "inchi_key_string":
    ["SGMZJAMFUVOLNK-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C5H14NO.ClH/c1-6(2,3)4-5-7;/h7H,4-5H2,1-3H3;1H/q+1;/p-1"],
    "mass": ["139.626"], "monoisotopic_mass": ["139.07639"], "smiles_string": ["C[N+](C)(C)CCO.[Cl-]"]},
    "synonyms": ["(2-Hydroxyethyl)trimethylammonium chloride", "(beta-Hydroxyethyl)trimethylammonium
    chloride", "2-Hydroxy-N,N,N,-trimethylethanaminium chloride", "2-hydroxy-N,N,N-trimethylethanaminium
    chloride", "2-hydroxy-N,N,N-trimethylethanaminium chloride", "Bilineurin chloride",
    "Biocolina", "Biocoline", "Chloride de choline", "Chlorure de choline", "Choline
    chlorhydrate", "Choline hydrochloride", "Cholini chloridum", "Cholinium chloride",
    "Cloruro de colina", "Hepacholine", "Lipotril", "Luridin chloride", "Paresan",
    "Trimethyl(2-hydroxyethyl)ammonium chloride", "choline chloride"], "secondary":
    {"asserted": {"id": "CHEBI:133341", "label": "choline chloride"}, "exact_current_rows":
    [{"label": "Choline chloride", "match_type": "preferred_term", "identifier": "CHEBI:133341",
    "preferred_term": "Choline chloride", "ontology_id": "CHEBI:133341", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[14]", "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806",
    "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition":
    [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3",
    "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"],
    "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]},
    "synonyms": ["Resazurin"]}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[15]", "name": "NaHCO3", "primary": {"id": "CHEBI:32139",
    "label": "sodium hydrogencarbonate"}, "canonical_label": "sodium hydrogencarbonate",
    "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:144-55-8", "drugbank:DB01390", "kegg.compound:C12603", "kegg.drug:D01203",
    "ppdb:2873", "wikipedia.en:Sodium_Bicarbonate"], "generalized_empirical_formula":
    ["CHO3.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32139"], "inchi_key_string":
    ["UIIMBOGNXHQVGW-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/CH2O3.Na/c2-1(3)4;/h(H2,2,3,4);/q;+1/p-1"],
    "mass": ["84.006"], "monoisotopic_mass": ["83.98234"], "smiles_string": ["O=C([O-])O.[Na+]"]},
    "synonyms": ["E 500", "E-500", "E500", "NaHCO3", "Natriumhydrogenkarbonat", "Sodium
    bicarbonate", "Sodium hydrogencarbonate", "baking soda", "bicarbonate of soda",
    "carbonic acid monosodium salt", "sodium acid carbonate", "sodium hydrogen carbonate",
    "sodium hydrogencarbonate", "sodium hydrogencarbonate"], "secondary": {"asserted":
    {"id": "CHEBI:32139", "label": "sodium hydrogencarbonate"}, "exact_current_rows":
    [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139",
    "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[16]", "name": "D-Glucose", "primary": {"id": "CHEBI:17634",
    "label": "D-glucose"}, "canonical_label": "D-glucose", "label_equal": true, "definition":
    ["A glucose with <small>D</small>-configuration."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:50-99-7"], "generalized_empirical_formula":
    ["C6H12O6"], "has_alternative_id": ["CHEBI:12965", "CHEBI:20999"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:17634"], "mass": ["180.156"], "monoisotopic_mass":
    ["180.06339"]}, "synonyms": ["D(+)-glucose", "D-(+)-glucose", "D-gluco-hexose",
    "D-gluco-hexose", "D-glucose", "D-glucose", "Traubenzucker", "dextrose", "grape
    sugar"], "secondary": {"asserted": {"id": "CHEBI:17634", "label": "D-glucose"},
    "exact_current_rows": [{"label": "D-Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634",
    "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}}, {"layer": "target",
    "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[17]",
    "name": "L-Cysteine HCl x H2O", "primary": {"id": "CHEBI:91248", "label": "L-cysteine
    hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride hydrate",
    "label_equal": true, "definition": ["A hydrate that is the monohydrate form of
    <small>L</small>-cysteine hydrochloride."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326", "reaxys:5158059", "wikipedia.en:Cysteine"],
    "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:91248"], "inchi_key_string": ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string":
    ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"],
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
    "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[18]",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[19]", "name": "Nitrilotriacetic acid", "primary": {"id":
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[20]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795",
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
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[21]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364",
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
    "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[22]",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[23]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[24]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312",
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
    {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[25]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440",
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
    "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field":
    "ingredients[26]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465",
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
    "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[27]", "name": "H3BO3", "primary": {"id": "CHEBI:33118",
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
    "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field":
    "ingredients[28]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213",
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
    {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[29]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361",
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
    "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field":
    "ingredients[30]", "name": "Biotin", "primary": {"id": "CHEBI:15956", "label":
    "biotin"}, "canonical_label": "biotin", "label_equal": true, "definition": ["An
    organic heterobicyclic compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
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
    "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[31]",
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
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[32]", "name": "Pyridoxine hydrochloride", "primary": {"id":
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
    "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[33]",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[34]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015",
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
    "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field": "ingredients[35]",
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
    "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field":
    "ingredients[36]", "name": "Calcium D-(+)-pantothenate", "primary": {"id": "CHEBI:31345",
    "label": "Calcium pantothenate"}, "canonical_label": "Calcium pantothenate", "label_equal":
    true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:137-08-6", "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278",
    "pubmed:20553011", "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula":
    ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"],
    "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"],
    "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]},
    "synonyms": ["Calcium pantotenate", "Calcium pantothenate", "Calcium pantothenate,
    d-", "Calpan", "D-ca pantothenate", "D-calcium pantothenate", "NSC-36292", "Pantholin",
    "Pantothenic acid (as calcium)", "Pantothenic acid calcium salt", "Vitamin b5,
    calcium salt", "pantotenato de calcio", "pantothenate de calcium"]}, {"layer":
    "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field":
    "ingredients[37]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843", "label":
    "vitamin B12"}, "canonical_label": "vitamin B12", "label_equal": true, "definition":
    ["Any member of a group of cobalamin vitamers that exhibit biological activity
    against vitamin B<small><sub>12</sub></small> deficiency. Vitamin B<small><sub>12</sub></small>
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
    {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[38]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753",
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
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field": "ingredients[39]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id":
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
    "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[0]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036",
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
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[1]", "name": "Na2SO4", "primary": {"id": "CHEBI:32149",
    "label": "sodium sulfate"}, "canonical_label": "sodium sulfate", "label_equal":
    true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7757-82-6", "kegg.compound:C13199", "kegg.drug:D01732"], "generalized_empirical_formula":
    ["2Na.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32149"], "inchi_key_string":
    ["PMZURENOXWZQFD-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2Na.H2O4S/c;;1-5(2,3)4/h;;(H2,1,2,3,4)/q2*+1;/p-2"],
    "mass": ["142.043"], "monoisotopic_mass": ["141.93127"], "smiles_string": ["O=S(=O)([O-])[O-].[Na+].[Na+]"]},
    "synonyms": ["Na2SO4", "Natriumsulfat", "Sodium sulfate", "disodium sulfate",
    "disodium sulphate", "salt cake", "sodium sulfate", "sodium sulfate", "sodium
    sulfate, anhydrous", "sodium sulphate"], "secondary": {"asserted": {"id": "CHEBI:32149",
    "label": "sodium sulfate"}, "exact_current_rows": [{"label": "Na2SO4", "match_type":
    "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id":
    "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[2]", "name": "NH4Cl", "primary": {"id": "CHEBI:31206", "label":
    "ammonium chloride"}, "canonical_label": "ammonium chloride", "label_equal": true,
    "definition": ["An inorganic chloride having ammonium as the counterion."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:12125-02-9", "gmelin:10120",
    "kegg.compound:C12538", "kegg.drug:D01139", "wikipedia.en:Ammonium_Chloride"],
    "generalized_empirical_formula": ["Cl.H4N"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:31206"], "inchi_key_string": ["NLXLAEXVIDQMFP-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/ClH.H3N/h1H;1H3"], "mass": ["53.492"], "monoisotopic_mass": ["53.00323"],
    "smiles_string": ["[Cl-].[H][N+]([H])([H])[H]"]}, "synonyms": ["Ammonium chloride",
    "Ammoniumchlorid", "NH4Cl", "[NH4]Cl", "ammonium chloride", "ammonium chloride",
    "azanium chloride"], "secondary": {"asserted": {"id": "CHEBI:31206", "label":
    "ammonium chloride"}, "exact_current_rows": [{"label": "NH4Cl", "match_type":
    "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id":
    "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[3]", "name": "KCl", "primary": {"id": "CHEBI:32588", "label":
    "potassium chloride"}, "canonical_label": "potassium chloride", "label_equal":
    true, "definition": ["A metal chloride salt with a K(+) counterion."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7447-40-7", "drugbank:DB00761",
    "kegg.drug:D02060", "metacyc.compound:KCL", "molbase:881", "reaxys:3534978", "wikipedia.en:Potassium_Chloride"],
    "generalized_empirical_formula": ["Cl.K"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:32588"], "inchi_key_string": ["WCUXLLCKKVVCTQ-UHFFFAOYSA-M"], "inchi_string":
    ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "monoisotopic_mass": ["73.93256"],
    "smiles_string": ["[Cl-].[K+]"]}, "synonyms": ["KCl", "Kaliumchlorid", "Kaon-Cl
    10", "Klor-con", "Klotrix", "Monopotassium chloride", "[KCl]", "muriate of potash",
    "potassium chloride", "potassium chloride", "sylvite"], "secondary": {"asserted":
    {"id": "CHEBI:32588", "label": "potassium chloride"}, "exact_current_rows": [{"label":
    "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[4]", "name": "NaCl", "primary": {"id": "CHEBI:26710", "label":
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
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[5]", "name": "MgCl2 x 6 H2O", "primary": {"id": "CHEBI:86345",
    "label": "magnesium dichloride hexahydrate"}, "canonical_label": "magnesium dichloride
    hexahydrate", "label_equal": true, "definition": ["A hydrate that is the hexahydrate
    form of magnesium dichloride."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7791-18-6", "kegg.drug:D04834", "pubmed:24831644", "pubmed:25148974", "pubmed:25430969",
    "reaxys:11343754"], "generalized_empirical_formula": ["2Cl.6H2O.Mg"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:86345"], "inchi_key_string": ["DHRRIBDTHFBPNG-UHFFFAOYSA-L"],
    "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass":
    ["203.301"], "monoisotopic_mass": ["201.98614"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]},
    "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride
    hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate",
    "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"], "secondary":
    {"asserted": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"},
    "exact_current_rows": [{"label": "Magnesium chloride", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[6]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[7]", "name": "Yeast extract"}, {"layer": "owner-0", "path":
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field":
    "ingredients[8]", "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887", "label":
    "nickel dichloride"}, "canonical_label": "nickel dichloride", "label_equal": true,
    "definition": ["A compound of nickel and chloride in which the ratio of nickel
    (in the +2 oxidation state) to chloride is 1:2."], "annotations": {"charge": [0.0],
    "database_cross_reference": ["cas:7718-54-9", "kegg.compound:C14711", "pubmed:11739495",
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
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[9]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939",
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
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[10]", "name": "Ascorbic acid", "primary": {"id": "CHEBI:22652",
    "label": "ascorbic acid"}, "canonical_label": "ascorbic acid", "label_equal":
    true, "definition": [], "annotations": {"has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:22652"]}, "synonyms": [], "secondary": {"asserted": {"id": "CHEBI:22652",
    "label": "ascorbic acid"}, "exact_current_rows": [{"label": "Ascorbic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:22652", "preferred_term": "Ascorbic acid",
    "ontology_id": "CHEBI:22652", "mapping_status": "MAPPED", "ambiguity": "unique"}]}},
    {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[11]", "name": "Myo-inositol", "primary": {"id": "CHEBI:17268",
    "label": "myo-inositol"}, "canonical_label": "myo-inositol", "label_equal": true,
    "definition": ["An inositol having <i>myo</i>- configuration."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:87-89-8", "drugbank:DB03106",
    "drugcentral:1444", "gmelin:82918", "hmdb:HMDB0000211", "kegg.compound:C00137",
    "kegg.drug:D08079", "knapsack:C00001164", "metacyc.compound:MYO-INOSITOL", "pdb-ccd:INS",
    "pubmed:11034685", "pubmed:11244303", "pubmed:11323092", "pubmed:11772411", "pubmed:12478879",
    "pubmed:12832083", "pubmed:14583919", "pubmed:14681857", "pubmed:15181167", "pubmed:15295080",
    "pubmed:15558078", "pubmed:16410747", "pubmed:1694860", "pubmed:17439666", "pubmed:17722064",
    "pubmed:18650262", "pubmed:18854045", "pubmed:19097871", "pubmed:19383710", "pubmed:22285975",
    "pubmed:22461977", "pubmed:22517104", "pubmed:838172", "reaxys:1907329", "wikipedia.en:Inositol"],
    "generalized_empirical_formula": ["C6H12O6"], "has_alternative_id": ["CHEBI:10601",
    "CHEBI:12826", "CHEBI:12831", "CHEBI:25451", "CHEBI:43559"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:17268"], "inchi_key_string": ["CDAISMWEOUEBRE-GPIVLXJGSA-N"],
    "inchi_string": ["InChI=1S/C6H12O6/c7-1-2(8)4(10)6(12)5(11)3(1)9/h1-12H/t1-,2-,3-,4+,5-,6-"],
    "mass": ["180.156"], "monoisotopic_mass": ["180.06339"], "smiles_string": ["O[C@H]1[C@H](O)[C@@H](O)[C@H](O)[C@@H](O)[C@H]1O"]},
    "synonyms": ["(1r,2R,3S,4s,5R,6S)-cyclohexane-1,2,3,4,5,6-hexol", "1,2,3,4,5,6-HEXAHYDROXY-CYCLOHEXANE",
    "1,2,3,5/4,6-cyclohexanehexol", "1D-myo-Inositol", "1L-myo-Inositol", "Bios I",
    "Cyclohexitol", "D-myo-Inositol", "Dambose", "Inositol", "Ins", "L-myo-Inositol",
    "Meat sugar", "Myoinositol", "cis-1,2,3,5-trans-4,6-cyclohexanehexol", "i-inositol",
    "inosite", "meso-Inositol", "myo-Inositol", "myo-Inositol", "myo-inositol", "myo-inositol"],
    "secondary": {"asserted": {"id": "CHEBI:17268", "label": "myo-inositol"}, "exact_current_rows":
    [{"label": "myo-Inositol", "match_type": "preferred_term", "identifier": "CHEBI:17268",
    "preferred_term": "myo-Inositol", "ontology_id": "CHEBI:17268", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[12]", "name": "Niacinamide", "primary": {"id": "CHEBI:17154",
    "label": "nicotinamide"}, "canonical_label": "nicotinamide", "label_equal": true,
    "definition": ["A pyridinecarboxamide that is pyridine in which the hydrogen at
    position 3 is replaced by a carboxamide group."], "annotations": {"charge": [0.0],
    "database_cross_reference": ["cas:98-92-0", "drugbank:DB02701", "drugcentral:1906",
    "foodb.food:FDB012485", "gmelin:3336", "hmdb:HMDB0001406", "kegg.compound:C00153",
    "kegg.drug:D00036", "knapsack:C00000209", "lincs.smallmolecule:LSM-5428", "metacyc.compound:NIACINAMIDE",
    "patent:US2904552", "patent:US2993051", "pdb-ccd:NCA", "pubmed:10884473", "pubmed:11355130",
    "pubmed:11814060", "pubmed:12014919", "pubmed:12487919", "pubmed:12519385", "pubmed:12709297",
    "pubmed:12782109", "pubmed:12890690", "pubmed:14729974", "pubmed:14757966", "pubmed:14871431",
    "pubmed:15497767", "pubmed:15563975", "pubmed:15780941", "pubmed:15807725", "pubmed:15834926",
    "pubmed:15995937", "pubmed:16029679", "pubmed:16209160", "pubmed:16596767", "pubmed:16766489",
    "pubmed:16871361", "pubmed:17021258", "pubmed:17129213", "pubmed:18234191", "pubmed:18316796",
    "pubmed:18368629", "pubmed:18373238", "pubmed:18389009", "pubmed:18514428", "pubmed:18930755",
    "pubmed:18987186", "pubmed:19212411", "pubmed:19539713", "pubmed:19544437", "pubmed:2026685",
    "pubmed:21503886", "pubmed:21891976", "pubmed:21918528", "pubmed:21926578", "pubmed:22067079",
    "pubmed:22160932", "pubmed:22207684", "pubmed:22232263", "pubmed:22281243", "pubmed:22359146",
    "pubmed:22361740", "pubmed:22407380", "pubmed:22456321", "pubmed:22536229", "pubmed:22543086",
    "pubmed:22626821", "pubmed:22699421", "pubmed:22709272", "pubmed:22763693", "pubmed:22770225",
    "pubmed:23016598", "pubmed:23028781", "pubmed:23043891", "pubmed:23047329", "pubmed:24027187",
    "pubmed:24077178", "pubmed:24559077", "pubmed:24635573", "pubmed:25504347", "pubmed:25561219",
    "pubmed:31710686", "pubmed:32249824", "pubmed:33196157", "pubmed:33471934", "pubmed:8620561",
    "pubmed:8767167", "pubmed:9518388", "reaxys:383619", "wikipedia.en:Nicotinamide"],
    "generalized_empirical_formula": ["C6H6N2O"], "has_alternative_id": ["CHEBI:14645",
    "CHEBI:25521", "CHEBI:44258", "CHEBI:7556"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:17154"], "inchi_key_string": ["DFPAKSUCGFBDDF-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/C6H6N2O/c7-6(9)5-2-1-3-8-4-5/h1-4H,(H2,7,9)"], "mass": ["122.127"],
    "monoisotopic_mass": ["122.04801"], "smiles_string": ["NC(=O)c1cccnc1"]}, "synonyms":
    ["3-carbamoylpyridine", "3-pyridinecarboxamide", "Niacinamide", "Nicotinamid",
    "Nicotinsaeureamid", "Nikotinamid", "Nikotinsaeureamid", "Vitamin PP", "beta-pyridinecarboxamide",
    "m-(aminocarbonyl)pyridine", "niacin", "niamide", "nicotinamida", "nicotinamide",
    "nicotinamidum", "nicotine acid amide", "nicotine amide", "nicotinic acid amide",
    "nicotinic amide", "nicotylamide", "pyridine-3-carboxamide", "pyridine-3-carboxamide",
    "pyridine-3-carboxylic acid amide", "vitamin B3"], "secondary": {"asserted": {"id":
    "CHEBI:17154", "label": "nicotinamide"}, "exact_current_rows": [{"label": "Nicotinamide",
    "match_type": "preferred_term", "identifier": "CHEBI:17154", "preferred_term":
    "Nicotinamide", "ontology_id": "CHEBI:17154", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[13]", "name": "Choline chloride", "primary": {"id": "CHEBI:133341",
    "label": "choline chloride"}, "canonical_label": "choline chloride", "label_equal":
    true, "definition": ["A quaternary ammonium salt with choline cation and chloride
    anion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:67-48-1",
    "ppdb:161", "pubmed:12962717", "pubmed:17596274", "pubmed:20396712", "pubmed:24905385",
    "pubmed:25037344", "pubmed:6196640", "pubmed:8047569", "reaxys:3563126", "vsdb:161",
    "wikipedia.en:Choline_chloride"], "generalized_empirical_formula": ["C5H14NO.Cl"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:133341"], "inchi_key_string":
    ["SGMZJAMFUVOLNK-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C5H14NO.ClH/c1-6(2,3)4-5-7;/h7H,4-5H2,1-3H3;1H/q+1;/p-1"],
    "mass": ["139.626"], "monoisotopic_mass": ["139.07639"], "smiles_string": ["C[N+](C)(C)CCO.[Cl-]"]},
    "synonyms": ["(2-Hydroxyethyl)trimethylammonium chloride", "(beta-Hydroxyethyl)trimethylammonium
    chloride", "2-Hydroxy-N,N,N,-trimethylethanaminium chloride", "2-hydroxy-N,N,N-trimethylethanaminium
    chloride", "2-hydroxy-N,N,N-trimethylethanaminium chloride", "Bilineurin chloride",
    "Biocolina", "Biocoline", "Chloride de choline", "Chlorure de choline", "Choline
    chlorhydrate", "Choline hydrochloride", "Cholini chloridum", "Cholinium chloride",
    "Cloruro de colina", "Hepacholine", "Lipotril", "Luridin chloride", "Paresan",
    "Trimethyl(2-hydroxyethyl)ammonium chloride", "choline chloride"], "secondary":
    {"asserted": {"id": "CHEBI:133341", "label": "choline chloride"}, "exact_current_rows":
    [{"label": "Choline chloride", "match_type": "preferred_term", "identifier": "CHEBI:133341",
    "preferred_term": "Choline chloride", "ontology_id": "CHEBI:133341", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[14]", "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806",
    "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition":
    [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3",
    "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"],
    "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]},
    "synonyms": ["Resazurin"]}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[15]", "name": "NaHCO3", "primary": {"id": "CHEBI:32139",
    "label": "sodium hydrogencarbonate"}, "canonical_label": "sodium hydrogencarbonate",
    "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:144-55-8", "drugbank:DB01390", "kegg.compound:C12603", "kegg.drug:D01203",
    "ppdb:2873", "wikipedia.en:Sodium_Bicarbonate"], "generalized_empirical_formula":
    ["CHO3.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32139"], "inchi_key_string":
    ["UIIMBOGNXHQVGW-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/CH2O3.Na/c2-1(3)4;/h(H2,2,3,4);/q;+1/p-1"],
    "mass": ["84.006"], "monoisotopic_mass": ["83.98234"], "smiles_string": ["O=C([O-])O.[Na+]"]},
    "synonyms": ["E 500", "E-500", "E500", "NaHCO3", "Natriumhydrogenkarbonat", "Sodium
    bicarbonate", "Sodium hydrogencarbonate", "baking soda", "bicarbonate of soda",
    "carbonic acid monosodium salt", "sodium acid carbonate", "sodium hydrogen carbonate",
    "sodium hydrogencarbonate", "sodium hydrogencarbonate"], "secondary": {"asserted":
    {"id": "CHEBI:32139", "label": "sodium hydrogencarbonate"}, "exact_current_rows":
    [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139",
    "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[16]", "name": "D-Glucose", "primary": {"id": "CHEBI:17634",
    "label": "D-glucose"}, "canonical_label": "D-glucose", "label_equal": true, "definition":
    ["A glucose with <small>D</small>-configuration."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:50-99-7"], "generalized_empirical_formula":
    ["C6H12O6"], "has_alternative_id": ["CHEBI:12965", "CHEBI:20999"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:17634"], "mass": ["180.156"], "monoisotopic_mass":
    ["180.06339"]}, "synonyms": ["D(+)-glucose", "D-(+)-glucose", "D-gluco-hexose",
    "D-gluco-hexose", "D-glucose", "D-glucose", "Traubenzucker", "dextrose", "grape
    sugar"], "secondary": {"asserted": {"id": "CHEBI:17634", "label": "D-glucose"},
    "exact_current_rows": [{"label": "D-Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634",
    "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}}, {"layer": "owner-0",
    "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[17]", "name": "L-Cysteine HCl x H2O", "primary": {"id":
    "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "canonical_label":
    "L-cysteine hydrochloride hydrate", "label_equal": true, "definition": ["A hydrate
    that is the monohydrate form of <small>L</small>-cysteine hydrochloride."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151",
    "kegg.drug:D02326", "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula":
    ["C3H7NO2S.H2O.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"],
    "inchi_key_string": ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"],
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
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field":
    "ingredients[18]", "name": "Na2S x 9 H2O", "primary": {"id": "CHEBI:76209", "label":
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[19]", "name": "Nitrilotriacetic acid", "primary": {"id":
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[20]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795",
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
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[21]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364",
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
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field":
    "ingredients[22]", "name": "FeSO4 x 7 H2O", "primary": {"id": "CHEBI:75836", "label":
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[23]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[24]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312",
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
    {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[25]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440",
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
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[26]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465",
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
    "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[27]", "name": "H3BO3", "primary": {"id": "CHEBI:33118",
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
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[28]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213",
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
    {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[29]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361",
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
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[30]", "name": "Biotin", "primary": {"id": "CHEBI:15956",
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
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field":
    "ingredients[31]", "name": "Folic acid", "primary": {"id": "CHEBI:27470", "label":
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
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[32]", "name": "Pyridoxine hydrochloride", "primary": {"id":
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
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field":
    "ingredients[33]", "name": "Thiamine HCl", "primary": {"id": "CHEBI:49105", "label":
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[34]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015",
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
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field":
    "ingredients[35]", "name": "Nicotinic acid", "primary": {"id": "CHEBI:15940",
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
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[36]", "name": "Calcium D-(+)-pantothenate", "primary": {"id":
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
    "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[37]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843",
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
    {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[38]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753",
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
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field": "ingredients[39]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id":
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
    "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[0]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036",
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
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[1]", "name": "Na2SO4", "primary": {"id": "CHEBI:32149",
    "label": "sodium sulfate"}, "canonical_label": "sodium sulfate", "label_equal":
    true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7757-82-6", "kegg.compound:C13199", "kegg.drug:D01732"], "generalized_empirical_formula":
    ["2Na.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32149"], "inchi_key_string":
    ["PMZURENOXWZQFD-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2Na.H2O4S/c;;1-5(2,3)4/h;;(H2,1,2,3,4)/q2*+1;/p-2"],
    "mass": ["142.043"], "monoisotopic_mass": ["141.93127"], "smiles_string": ["O=S(=O)([O-])[O-].[Na+].[Na+]"]},
    "synonyms": ["Na2SO4", "Natriumsulfat", "Sodium sulfate", "disodium sulfate",
    "disodium sulphate", "salt cake", "sodium sulfate", "sodium sulfate", "sodium
    sulfate, anhydrous", "sodium sulphate"], "secondary": {"asserted": {"id": "CHEBI:32149",
    "label": "sodium sulfate"}, "exact_current_rows": [{"label": "Na2SO4", "match_type":
    "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id":
    "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[2]", "name": "NH4Cl", "primary": {"id": "CHEBI:31206", "label":
    "ammonium chloride"}, "canonical_label": "ammonium chloride", "label_equal": true,
    "definition": ["An inorganic chloride having ammonium as the counterion."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:12125-02-9", "gmelin:10120",
    "kegg.compound:C12538", "kegg.drug:D01139", "wikipedia.en:Ammonium_Chloride"],
    "generalized_empirical_formula": ["Cl.H4N"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:31206"], "inchi_key_string": ["NLXLAEXVIDQMFP-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/ClH.H3N/h1H;1H3"], "mass": ["53.492"], "monoisotopic_mass": ["53.00323"],
    "smiles_string": ["[Cl-].[H][N+]([H])([H])[H]"]}, "synonyms": ["Ammonium chloride",
    "Ammoniumchlorid", "NH4Cl", "[NH4]Cl", "ammonium chloride", "ammonium chloride",
    "azanium chloride"], "secondary": {"asserted": {"id": "CHEBI:31206", "label":
    "ammonium chloride"}, "exact_current_rows": [{"label": "NH4Cl", "match_type":
    "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id":
    "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[3]", "name": "KCl", "primary": {"id": "CHEBI:32588", "label":
    "potassium chloride"}, "canonical_label": "potassium chloride", "label_equal":
    true, "definition": ["A metal chloride salt with a K(+) counterion."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:7447-40-7", "drugbank:DB00761",
    "kegg.drug:D02060", "metacyc.compound:KCL", "molbase:881", "reaxys:3534978", "wikipedia.en:Potassium_Chloride"],
    "generalized_empirical_formula": ["Cl.K"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:32588"], "inchi_key_string": ["WCUXLLCKKVVCTQ-UHFFFAOYSA-M"], "inchi_string":
    ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "monoisotopic_mass": ["73.93256"],
    "smiles_string": ["[Cl-].[K+]"]}, "synonyms": ["KCl", "Kaliumchlorid", "Kaon-Cl
    10", "Klor-con", "Klotrix", "Monopotassium chloride", "[KCl]", "muriate of potash",
    "potassium chloride", "potassium chloride", "sylvite"], "secondary": {"asserted":
    {"id": "CHEBI:32588", "label": "potassium chloride"}, "exact_current_rows": [{"label":
    "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[4]", "name": "NaCl", "primary": {"id": "CHEBI:26710", "label":
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
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[5]", "name": "MgCl2 x 6 H2O", "primary": {"id": "CHEBI:86345",
    "label": "magnesium dichloride hexahydrate"}, "canonical_label": "magnesium dichloride
    hexahydrate", "label_equal": true, "definition": ["A hydrate that is the hexahydrate
    form of magnesium dichloride."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7791-18-6", "kegg.drug:D04834", "pubmed:24831644", "pubmed:25148974", "pubmed:25430969",
    "reaxys:11343754"], "generalized_empirical_formula": ["2Cl.6H2O.Mg"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:86345"], "inchi_key_string": ["DHRRIBDTHFBPNG-UHFFFAOYSA-L"],
    "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass":
    ["203.301"], "monoisotopic_mass": ["201.98614"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]},
    "synonyms": ["CCRIS 3494", "Chlorure de magnesium hydrate", "Magnesium chloride
    hydrate", "Magnesium chloride", "MgCl2.6H2O", "magnesium chloride hexahydrate",
    "magnesium dichloride--water (1/6)", "magnesium dichloride--water (1/6)"], "secondary":
    {"asserted": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"},
    "exact_current_rows": [{"label": "Magnesium chloride", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[6]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[7]", "name": "Yeast extract"}, {"layer": "owner-1", "path":
    "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[8]",
    "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887", "label": "nickel dichloride"},
    "canonical_label": "nickel dichloride", "label_equal": true, "definition": ["A
    compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation
    state) to chloride is 1:2."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:7718-54-9", "kegg.compound:C14711", "pubmed:11739495", "pubmed:12603851",
    "pubmed:21928331", "pubmed:23179351", "pubmed:23622879", "pubmed:23702803", "pubmed:23735035",
    "pubmed:7671317", "reaxys:3902827", "reaxys:8128171", "wikipedia.en:Nickel_dichloride"],
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
    "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[9]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939",
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
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[10]", "name": "Ascorbic acid", "primary": {"id": "CHEBI:22652",
    "label": "ascorbic acid"}, "canonical_label": "ascorbic acid", "label_equal":
    true, "definition": [], "annotations": {"has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:22652"]}, "synonyms": [], "secondary": {"asserted": {"id": "CHEBI:22652",
    "label": "ascorbic acid"}, "exact_current_rows": [{"label": "Ascorbic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:22652", "preferred_term": "Ascorbic acid",
    "ontology_id": "CHEBI:22652", "mapping_status": "MAPPED", "ambiguity": "unique"}]}},
    {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[11]", "name": "Myo-inositol", "primary": {"id": "CHEBI:17268",
    "label": "myo-inositol"}, "canonical_label": "myo-inositol", "label_equal": true,
    "definition": ["An inositol having <i>myo</i>- configuration."], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:87-89-8", "drugbank:DB03106",
    "drugcentral:1444", "gmelin:82918", "hmdb:HMDB0000211", "kegg.compound:C00137",
    "kegg.drug:D08079", "knapsack:C00001164", "metacyc.compound:MYO-INOSITOL", "pdb-ccd:INS",
    "pubmed:11034685", "pubmed:11244303", "pubmed:11323092", "pubmed:11772411", "pubmed:12478879",
    "pubmed:12832083", "pubmed:14583919", "pubmed:14681857", "pubmed:15181167", "pubmed:15295080",
    "pubmed:15558078", "pubmed:16410747", "pubmed:1694860", "pubmed:17439666", "pubmed:17722064",
    "pubmed:18650262", "pubmed:18854045", "pubmed:19097871", "pubmed:19383710", "pubmed:22285975",
    "pubmed:22461977", "pubmed:22517104", "pubmed:838172", "reaxys:1907329", "wikipedia.en:Inositol"],
    "generalized_empirical_formula": ["C6H12O6"], "has_alternative_id": ["CHEBI:10601",
    "CHEBI:12826", "CHEBI:12831", "CHEBI:25451", "CHEBI:43559"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:17268"], "inchi_key_string": ["CDAISMWEOUEBRE-GPIVLXJGSA-N"],
    "inchi_string": ["InChI=1S/C6H12O6/c7-1-2(8)4(10)6(12)5(11)3(1)9/h1-12H/t1-,2-,3-,4+,5-,6-"],
    "mass": ["180.156"], "monoisotopic_mass": ["180.06339"], "smiles_string": ["O[C@H]1[C@H](O)[C@@H](O)[C@H](O)[C@@H](O)[C@H]1O"]},
    "synonyms": ["(1r,2R,3S,4s,5R,6S)-cyclohexane-1,2,3,4,5,6-hexol", "1,2,3,4,5,6-HEXAHYDROXY-CYCLOHEXANE",
    "1,2,3,5/4,6-cyclohexanehexol", "1D-myo-Inositol", "1L-myo-Inositol", "Bios I",
    "Cyclohexitol", "D-myo-Inositol", "Dambose", "Inositol", "Ins", "L-myo-Inositol",
    "Meat sugar", "Myoinositol", "cis-1,2,3,5-trans-4,6-cyclohexanehexol", "i-inositol",
    "inosite", "meso-Inositol", "myo-Inositol", "myo-Inositol", "myo-inositol", "myo-inositol"],
    "secondary": {"asserted": {"id": "CHEBI:17268", "label": "myo-inositol"}, "exact_current_rows":
    [{"label": "myo-Inositol", "match_type": "preferred_term", "identifier": "CHEBI:17268",
    "preferred_term": "myo-Inositol", "ontology_id": "CHEBI:17268", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[12]", "name": "Niacinamide", "primary": {"id": "CHEBI:17154",
    "label": "nicotinamide"}, "canonical_label": "nicotinamide", "label_equal": true,
    "definition": ["A pyridinecarboxamide that is pyridine in which the hydrogen at
    position 3 is replaced by a carboxamide group."], "annotations": {"charge": [0.0],
    "database_cross_reference": ["cas:98-92-0", "drugbank:DB02701", "drugcentral:1906",
    "foodb.food:FDB012485", "gmelin:3336", "hmdb:HMDB0001406", "kegg.compound:C00153",
    "kegg.drug:D00036", "knapsack:C00000209", "lincs.smallmolecule:LSM-5428", "metacyc.compound:NIACINAMIDE",
    "patent:US2904552", "patent:US2993051", "pdb-ccd:NCA", "pubmed:10884473", "pubmed:11355130",
    "pubmed:11814060", "pubmed:12014919", "pubmed:12487919", "pubmed:12519385", "pubmed:12709297",
    "pubmed:12782109", "pubmed:12890690", "pubmed:14729974", "pubmed:14757966", "pubmed:14871431",
    "pubmed:15497767", "pubmed:15563975", "pubmed:15780941", "pubmed:15807725", "pubmed:15834926",
    "pubmed:15995937", "pubmed:16029679", "pubmed:16209160", "pubmed:16596767", "pubmed:16766489",
    "pubmed:16871361", "pubmed:17021258", "pubmed:17129213", "pubmed:18234191", "pubmed:18316796",
    "pubmed:18368629", "pubmed:18373238", "pubmed:18389009", "pubmed:18514428", "pubmed:18930755",
    "pubmed:18987186", "pubmed:19212411", "pubmed:19539713", "pubmed:19544437", "pubmed:2026685",
    "pubmed:21503886", "pubmed:21891976", "pubmed:21918528", "pubmed:21926578", "pubmed:22067079",
    "pubmed:22160932", "pubmed:22207684", "pubmed:22232263", "pubmed:22281243", "pubmed:22359146",
    "pubmed:22361740", "pubmed:22407380", "pubmed:22456321", "pubmed:22536229", "pubmed:22543086",
    "pubmed:22626821", "pubmed:22699421", "pubmed:22709272", "pubmed:22763693", "pubmed:22770225",
    "pubmed:23016598", "pubmed:23028781", "pubmed:23043891", "pubmed:23047329", "pubmed:24027187",
    "pubmed:24077178", "pubmed:24559077", "pubmed:24635573", "pubmed:25504347", "pubmed:25561219",
    "pubmed:31710686", "pubmed:32249824", "pubmed:33196157", "pubmed:33471934", "pubmed:8620561",
    "pubmed:8767167", "pubmed:9518388", "reaxys:383619", "wikipedia.en:Nicotinamide"],
    "generalized_empirical_formula": ["C6H6N2O"], "has_alternative_id": ["CHEBI:14645",
    "CHEBI:25521", "CHEBI:44258", "CHEBI:7556"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:17154"], "inchi_key_string": ["DFPAKSUCGFBDDF-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/C6H6N2O/c7-6(9)5-2-1-3-8-4-5/h1-4H,(H2,7,9)"], "mass": ["122.127"],
    "monoisotopic_mass": ["122.04801"], "smiles_string": ["NC(=O)c1cccnc1"]}, "synonyms":
    ["3-carbamoylpyridine", "3-pyridinecarboxamide", "Niacinamide", "Nicotinamid",
    "Nicotinsaeureamid", "Nikotinamid", "Nikotinsaeureamid", "Vitamin PP", "beta-pyridinecarboxamide",
    "m-(aminocarbonyl)pyridine", "niacin", "niamide", "nicotinamida", "nicotinamide",
    "nicotinamidum", "nicotine acid amide", "nicotine amide", "nicotinic acid amide",
    "nicotinic amide", "nicotylamide", "pyridine-3-carboxamide", "pyridine-3-carboxamide",
    "pyridine-3-carboxylic acid amide", "vitamin B3"], "secondary": {"asserted": {"id":
    "CHEBI:17154", "label": "nicotinamide"}, "exact_current_rows": [{"label": "Nicotinamide",
    "match_type": "preferred_term", "identifier": "CHEBI:17154", "preferred_term":
    "Nicotinamide", "ontology_id": "CHEBI:17154", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[13]", "name": "Choline chloride", "primary": {"id": "CHEBI:133341",
    "label": "choline chloride"}, "canonical_label": "choline chloride", "label_equal":
    true, "definition": ["A quaternary ammonium salt with choline cation and chloride
    anion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:67-48-1",
    "ppdb:161", "pubmed:12962717", "pubmed:17596274", "pubmed:20396712", "pubmed:24905385",
    "pubmed:25037344", "pubmed:6196640", "pubmed:8047569", "reaxys:3563126", "vsdb:161",
    "wikipedia.en:Choline_chloride"], "generalized_empirical_formula": ["C5H14NO.Cl"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:133341"], "inchi_key_string":
    ["SGMZJAMFUVOLNK-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C5H14NO.ClH/c1-6(2,3)4-5-7;/h7H,4-5H2,1-3H3;1H/q+1;/p-1"],
    "mass": ["139.626"], "monoisotopic_mass": ["139.07639"], "smiles_string": ["C[N+](C)(C)CCO.[Cl-]"]},
    "synonyms": ["(2-Hydroxyethyl)trimethylammonium chloride", "(beta-Hydroxyethyl)trimethylammonium
    chloride", "2-Hydroxy-N,N,N,-trimethylethanaminium chloride", "2-hydroxy-N,N,N-trimethylethanaminium
    chloride", "2-hydroxy-N,N,N-trimethylethanaminium chloride", "Bilineurin chloride",
    "Biocolina", "Biocoline", "Chloride de choline", "Chlorure de choline", "Choline
    chlorhydrate", "Choline hydrochloride", "Cholini chloridum", "Cholinium chloride",
    "Cloruro de colina", "Hepacholine", "Lipotril", "Luridin chloride", "Paresan",
    "Trimethyl(2-hydroxyethyl)ammonium chloride", "choline chloride"], "secondary":
    {"asserted": {"id": "CHEBI:133341", "label": "choline chloride"}, "exact_current_rows":
    [{"label": "Choline chloride", "match_type": "preferred_term", "identifier": "CHEBI:133341",
    "preferred_term": "Choline chloride", "ontology_id": "CHEBI:133341", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[14]", "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806",
    "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition":
    [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3",
    "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"],
    "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]},
    "synonyms": ["Resazurin"]}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[15]", "name": "NaHCO3", "primary": {"id": "CHEBI:32139",
    "label": "sodium hydrogencarbonate"}, "canonical_label": "sodium hydrogencarbonate",
    "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:144-55-8", "drugbank:DB01390", "kegg.compound:C12603", "kegg.drug:D01203",
    "ppdb:2873", "wikipedia.en:Sodium_Bicarbonate"], "generalized_empirical_formula":
    ["CHO3.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32139"], "inchi_key_string":
    ["UIIMBOGNXHQVGW-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/CH2O3.Na/c2-1(3)4;/h(H2,2,3,4);/q;+1/p-1"],
    "mass": ["84.006"], "monoisotopic_mass": ["83.98234"], "smiles_string": ["O=C([O-])O.[Na+]"]},
    "synonyms": ["E 500", "E-500", "E500", "NaHCO3", "Natriumhydrogenkarbonat", "Sodium
    bicarbonate", "Sodium hydrogencarbonate", "baking soda", "bicarbonate of soda",
    "carbonic acid monosodium salt", "sodium acid carbonate", "sodium hydrogen carbonate",
    "sodium hydrogencarbonate", "sodium hydrogencarbonate"], "secondary": {"asserted":
    {"id": "CHEBI:32139", "label": "sodium hydrogencarbonate"}, "exact_current_rows":
    [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139",
    "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[16]", "name": "D-Glucose", "primary": {"id": "CHEBI:17634",
    "label": "D-glucose"}, "canonical_label": "D-glucose", "label_equal": true, "definition":
    ["A glucose with <small>D</small>-configuration."], "annotations": {"charge":
    [0.0], "database_cross_reference": ["cas:50-99-7"], "generalized_empirical_formula":
    ["C6H12O6"], "has_alternative_id": ["CHEBI:12965", "CHEBI:20999"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:17634"], "mass": ["180.156"], "monoisotopic_mass":
    ["180.06339"]}, "synonyms": ["D(+)-glucose", "D-(+)-glucose", "D-gluco-hexose",
    "D-gluco-hexose", "D-glucose", "D-glucose", "Traubenzucker", "dextrose", "grape
    sugar"], "secondary": {"asserted": {"id": "CHEBI:17634", "label": "D-glucose"},
    "exact_current_rows": [{"label": "D-Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634",
    "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}}, {"layer": "owner-1",
    "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field":
    "ingredients[17]", "name": "L-Cysteine HCl x H2O", "primary": {"id": "CHEBI:91248",
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
    "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[18]",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[19]", "name": "Nitrilotriacetic acid", "primary": {"id":
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[20]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795",
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
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[21]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364",
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
    "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[22]",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[23]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[24]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312",
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
    {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[25]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440",
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
    "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[26]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465",
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
    "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[27]", "name": "H3BO3", "primary": {"id": "CHEBI:33118",
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
    "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[28]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213",
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
    {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[29]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361",
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
    "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[30]", "name": "Biotin", "primary": {"id": "CHEBI:15956",
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
    "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[31]",
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
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[32]", "name": "Pyridoxine hydrochloride", "primary": {"id":
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
    "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[33]",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[34]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015",
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
    "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml", "field": "ingredients[35]",
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
    "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[36]", "name": "Calcium D-(+)-pantothenate", "primary": {"id":
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
    "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[37]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843",
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
    {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[38]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753",
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
    "unique"}]}}, {"layer": "owner-1", "path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field": "ingredients[39]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id":
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
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions
  accessed_at: '2026-10-21T10:03:53Z'
  support: context_only
  summary: Current importer separates source stocks/percentage doses and main ingredients,
    skips solvent water and prefers provider g_l. Current behavior does not validate
    or repair these older flat owner values and is not a replay of the historical
    import.
- evidence_id: resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: merge_composition; _add_enrichment_metadata
  accessed_at: '2026-10-21T10:03:53Z'
  support: context_only
  summary: Current resolver copies ingredients, solutions and selected metadata, but
    not preparation steps in this method; it emits timezone-naive local timestamps.
    This is relevant writer context, not proof of the exact historical execution.
- evidence_id: cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-21T10:03:53Z'
  support: context_only
  summary: Current cleanup collapses equal duplicate amounts or flags disagreement;
    it no longer sums. The actual owner notes explicitly record four earlier sums
    across direct and stock values.
- evidence_id: history
  kind: record_content
  reference: data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml
  locator: Every target and maintained owner history and ingredient curation timestamp
  accessed_at: '2026-10-21T10:03:53Z'
  support: refutes
  summary: '[{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path":
    "curation_history[0].timestamp", "value": "2026-01-27T01:15:03.fZ", "valid_ISO_datetime":
    false, "timezone_aware": false}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:07.640681",
    "valid_ISO_datetime": true, "timezone_aware": false}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "curation_history[2].timestamp", "value": "2026-02-06T05:10:34.477786Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "curation_history[3].timestamp", "value": "2026-03-13T03:09:12.483697Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "curation_history[4].timestamp", "value": "2026-03-13T06:19:37.385850Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "curation_history[5].timestamp", "value": "2026-03-17T06:30:19.000000Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "curation_history[6].timestamp", "value": "2026-03-17T19:45:54.140689+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "curation_history[7].timestamp", "value": "2026-05-20T06:00:52.575341+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "curation_history[8].timestamp", "value": "2026-06-05T07:40:24.499481+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "curation_history[9].timestamp", "value": "2026-06-10T07:46:45.259086+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "curation_history[10].timestamp", "value": "2026-08-06T03:04:55.277889+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "curation_history[11].timestamp", "value": "2026-08-06T03:04:55.277936+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "curation_history[0].timestamp", "value": "2026-01-27T01:15:03.fZ",
    "valid_ISO_datetime": false, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:07.640681",
    "valid_ISO_datetime": true, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "curation_history[2].timestamp", "value": "2026-02-06T05:10:34.477786Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "curation_history[3].timestamp", "value": "2026-03-13T03:09:12.483697Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "curation_history[4].timestamp", "value": "2026-03-13T06:19:37.385850Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "curation_history[5].timestamp", "value": "2026-03-17T06:30:19.000000Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "curation_history[6].timestamp", "value": "2026-03-17T19:45:54.140689+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "curation_history[7].timestamp", "value": "2026-05-20T06:00:52.575341+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "curation_history[8].timestamp", "value": "2026-06-05T07:40:24.499481+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "curation_history[9].timestamp", "value": "2026-06-10T07:46:45.259086+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "curation_history[0].timestamp", "value": "2026-01-26T17:53:11.569200Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "curation_history[1].timestamp", "value": "2026-02-06T05:10:52.437408Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "curation_history[2].timestamp", "value": "2026-03-13T03:09:39.896308Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "curation_history[3].timestamp", "value": "2026-03-13T06:19:06.368596Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "curation_history[4].timestamp", "value": "2026-03-17T06:30:51.000000Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "curation_history[5].timestamp", "value": "2026-03-17T19:45:18.555904+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "curation_history[6].timestamp", "value": "2026-05-20T06:01:07.006727+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "curation_history[7].timestamp", "value": "2026-06-05T07:40:46.650684+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "curation_history[8].timestamp", "value": "2026-06-10T07:46:52.354579+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}]'
- evidence_id: merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger; merge_formulation_evidence; maintained formulation-aware
    merge context
  accessed_at: '2026-10-21T10:03:53Z'
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
  accessed_at: '2026-10-21T10:03:53Z'
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
  - CultureMech:005968
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Stable record, source accession and maintained contributors
  outcome: supported
  summary: CultureMech:005968 is the generated KOMODO 540 canonical record, with explicit
    merge contributors CM005968 and DSMZ owner CM001673. The exact KOMODO link and
    current DSMZ title establish source identity. Both full owner records retain the
    same 40 ingredient values, but preparation and catalog notes differ. All hashes
    match the native inspection.
  target_ids:
  - CultureMech:005968
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz540
  - mediadive540api
  - komodoMediaList
- assessment_id: relationships
  area: scope
  topic: Reciprocal SOURCE_DUPLICATE relation
  outcome: supported
  summary: The target/KOMODO parent_media points to DSMZ owner CM001673 and its exact
    path; that owner reciprocally lists CM005968 in variant_children. Both internal
    IDs and paths resolve in the inspected inputs. This is supported as same-accession
    source duplication, without treating the differing preparation/notes as identical
    or claiming experimental equivalence.
  target_ids:
  - CultureMech:005968
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - komodoMediaList
  - dsmz540
- assessment_id: provider-rounding
  area: quantity
  topic: Boundary-precision difference in three provider g_l values
  outcome: concern
  summary: For NH4Cl, cysteine hydrochloride monohydrate and sodium sulfide nonahydrate,
    the provider gives 0.3 g, 1015 mL and g_l 0.295566. Exact division is 0.295566502463...
    g/L and ordinary six-decimal rounding gives 0.295567, so the displayed provider
    value differs by 5.02463e-7 g/L, slightly beyond half a final decimal place. The
    existing local values reproduce the provider, but the strict arithmetic guard
    would not independently confirm that last digit. Preserve the provider value and
    this small rounding limit; no scale error or new correction is asserted.
  target_ids:
  - CultureMech:005968
  evidence_ids:
  - mediadive540api
  - quantity-3
  - quantity-20
  - quantity-21
- assessment_id: grounding
  area: grounding
  topic: Primary labels/forms and pinned secondary correspondence
  outcome: supported
  summary: 'Layer-specific counts are {"target": {"ingredient_instances": 40, "primary_CHEBI_instances":
    39, "secondary_current_asserted_instances": 37, "secondary_current_verified_instances":
    37, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.5, "secondary_verified_percent":
    92.5}, "owner-0": {"ingredient_instances": 40, "primary_CHEBI_instances": 39,
    "secondary_current_asserted_instances": 37, "secondary_current_verified_instances":
    37, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.5, "secondary_verified_percent":
    92.5}, "owner-1": {"ingredient_instances": 40, "primary_CHEBI_instances": 39,
    "secondary_current_asserted_instances": 37, "secondary_current_verified_instances":
    37, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.5, "secondary_verified_percent":
    92.5}}. Percentages are 0–100 linkage coverage over direct ingredient instances,
    not scientific accuracy. The 0 legacy link instances across reviewed layers are
    unverified by the current CHEBI-keyed snapshot; absence here does not prove historical
    invalidity. Current secondary keys without a live preferred-term row are []. No
    secondary linked-set percentage is invented for an empty set.'
  target_ids:
  - CultureMech:005968
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - mim
  - chebi63036
  - chebi32149
  - chebi31206
  - chebi32588
  - chebi26710
  - chebi86345
  - chebi86158
  - chebi34887
  - chebi63939
  - chebi22652
  - chebi17268
  - chebi17154
  - chebi133341
  - chebi8806
  - chebi32139
  - chebi17634
  - chebi91248
  - chebi76209
  - chebi44557
  - chebi31795
  - chebi86364
  - chebi75836
  - chebi91244
  - chebi32312
  - chebi31440
  - chebi86465
  - chebi33118
  - chebi75213
  - chebi131361
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
  topic: Supplied salt, hydrate and stereochemical forms
  outcome: concern
  summary: 'Every asserted primary label resolves, but chemical-form comparison exposes
    two disagreements: NiCl2 x 6 H2O is assigned CHEBI:34887 (Cl2Ni, no waters), and
    Sodium resazurin is assigned CHEBI:8806 (neutral C12H7NO4, no sodium). Both primary
    and secondary nickel assertions need source-form review. The calcium D-(+)-pantothenate
    source agrees with CHEBI:31345 D-specific synonyms/structure; its short generic
    label is not an error. CHEBI:16494 has no selected stereochemistry, so it does
    not contradict DL lipoic acid, whose qualifier should remain explicit. CHEBI:91248
    explicitly defines the cysteine hydrochloride monohydrate. Other source hydrates
    and generic vitamin B12 are preserved without molecular-weight substitution or
    inferred purity.'
  target_ids:
  - CultureMech:005968
  evidence_ids:
  - dsmz540
  - mediadive540api
  - chebi63036
  - chebi32149
  - chebi31206
  - chebi32588
  - chebi26710
  - chebi86345
  - chebi86158
  - chebi34887
  - chebi63939
  - chebi22652
  - chebi17268
  - chebi17154
  - chebi133341
  - chebi8806
  - chebi32139
  - chebi17634
  - chebi91248
  - chebi76209
  - chebi44557
  - chebi31795
  - chebi86364
  - chebi75836
  - chebi91244
  - chebi32312
  - chebi31440
  - chebi86465
  - chebi33118
  - chebi75213
  - chebi131361
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
  topic: Anoxic process, pH and sterilization scope
  outcome: concern
  summary: 'The primary and DSMZ owner specify initial 80% N2/20% CO2 sparging for
    30–45 min, bicarbonate/pH equilibration, same-atmosphere dispensing/autoclaving,
    sterile anoxic glucose/vitamin/cysteine/sulfide additions under 100% N2, vitamin
    filtration and final medium pH 6.8–7.0. The mineral-stock pH 6.5 then 7.0 is a
    separate stage. Target and KOMODO owner omit all preparation steps and retain
    Aerobic: Yes. That note must be reconciled as catalog provenance, not promoted
    to an incubation phenotype. The source does not give autoclave time/temperature,
    storage or shelf life; none is invented.'
  target_ids:
  - CultureMech:005968
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz540
  - komodoMediaList
  - resolver
- assessment_id: classification
  area: scope
  topic: Composition type, state and bounded use
  outcome: supported
  summary: COMPLEX/UNDEFINED are compatible with the explicit yeast extract and provider
    complex_medium=yes. LIQUID is consistent with the exact formulation lacking a
    gelling-agent branch. Bacterial filing and Microbial cultivation are broad catalog
    context, not verified growth for any named organism. Catalog aerobic wording is
    handled separately as a preparation inconsistency.
  target_ids:
  - CultureMech:005968
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz540
  - mediadive540api
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp interpretation
  outcome: concern
  summary: 31 exact timestamp instances were examined; 4 lack valid syntax or explicit
    timezone. No local timestamp was assumed UTC or rewritten. Process and confidence
    annotations are not independent scientific evidence.
  target_ids:
  - CultureMech:005968
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - history
  details: '[{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path":
    "curation_history[0].timestamp", "value": "2026-01-27T01:15:03.fZ", "valid_ISO_datetime":
    false, "timezone_aware": false}, {"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:07.640681",
    "valid_ISO_datetime": true, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "curation_history[0].timestamp", "value": "2026-01-27T01:15:03.fZ",
    "valid_ISO_datetime": false, "timezone_aware": false}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "curation_history[1].timestamp", "value": "2026-02-03T11:19:07.640681",
    "valid_ISO_datetime": true, "timezone_aware": false}]'
- assessment_id: quantities
  area: quantity
  topic: Every stored amount, stock dose and source-stage dependency
  outcome: concern
  summary: All 40 stored ingredient amounts in the target and each of two owners are
    traced to the 49 literal provider recipe rows at their own stages, plus two explicitly
    unquantified preparation additions and five quantitative preparation contexts.
    Direct g_l evidence, stock strengths/doses, solvent quantities and conditional
    dilution arithmetic are kept distinct. Source salt/hydrate mismatches remain separate
    from quantity arithmetic.
  target_ids:
  - CultureMech:005968
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
  details: '[{"field_path": "ingredients[0].concentration", "name": "KH2PO4", "current":
    {"value": "0.197044", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key":
    "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.197044,\n                        \"mmol_l\":
    1.44795,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[0]", "preparation_stage": "Main sol. 540 (solution
    1194, declared 1015 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1015 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-1", "arithmetic_separate_from_quote":
    "Original 0.2 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 0.1970443349753694581280788177
    g/L on the provider-declared stage volume; reported g_l is 0.197044. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "name": "KH2PO4", "current": {"value":
    "0.197044", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[0].concentration", "name": "KH2PO4", "current": {"value":
    "0.197044", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[0].concentration", "name": "KH2PO4", "current": {"value":
    "0.197044", "unit": "G_PER_L"}}], "source_amount": 0.2, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 0.197044, "provider_stage_volume_ml": 1015, "primary_source_evidence_id":
    "dsmz540"}, {"field_path": "ingredients[1].concentration", "name": "Na2SO4", "current":
    {"value": "0.0985222", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key":
    "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0985222,\n                        \"mmol_l\":
    0.693623,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[1]", "preparation_stage": "Main sol. 540 (solution
    1194, declared 1015 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1015 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-2", "arithmetic_separate_from_quote":
    "Original 0.1 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 0.09852216748768472906403940887
    g/L on the provider-declared stage volume; reported g_l is 0.0985222. This is
    not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "name": "Na2SO4", "current": {"value":
    "0.0985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[1].concentration", "name": "Na2SO4", "current": {"value":
    "0.0985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[1].concentration", "name": "Na2SO4", "current": {"value":
    "0.0985222", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 0.0985222, "provider_stage_volume_ml": 1015, "primary_source_evidence_id":
    "dsmz540"}, {"field_path": "ingredients[2].concentration", "name": "NH4Cl", "current":
    {"value": "0.295566", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key":
    "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.295566,\n                        \"mmol_l\":
    5.52564,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[2]", "preparation_stage": "Main sol. 540 (solution
    1194, declared 1015 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1015 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-3", "arithmetic_separate_from_quote":
    "Original 0.3 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 0.2955665024630541871921182266
    g/L on the provider-declared stage volume; reported g_l is 0.295566. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "name": "NH4Cl", "current": {"value":
    "0.295566", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[2].concentration", "name": "NH4Cl", "current": {"value":
    "0.295566", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[2].concentration", "name": "NH4Cl", "current": {"value":
    "0.295566", "unit": "G_PER_L"}}], "source_amount": 0.3, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 0.295566, "provider_stage_volume_ml": 1015, "primary_source_evidence_id":
    "dsmz540"}, {"field_path": "ingredients[3].concentration", "name": "KCl", "current":
    {"value": "0.492611", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key":
    "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.492611,\n                        \"mmol_l\":
    6.60779,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[3]", "preparation_stage": "Main sol. 540 (solution
    1194, declared 1015 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1015 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-4", "arithmetic_separate_from_quote":
    "Original 0.5 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 0.4926108374384236453201970443
    g/L on the provider-declared stage volume; reported g_l is 0.492611. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "name": "KCl", "current": {"value":
    "0.492611", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[3].concentration", "name": "KCl", "current": {"value":
    "0.492611", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[3].concentration", "name": "KCl", "current": {"value":
    "0.492611", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 0.492611, "provider_stage_volume_ml": 1015, "primary_source_evidence_id":
    "dsmz540"}, {"field_path": "ingredients[4].concentration", "name": "NaCl", "current":
    {"value": "7.89655", "unit": "G_PER_L"}, "decision": "correct", "source_key":
    "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 7,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 6.89655,\n                        \"mmol_l\":
    118.011,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[4]", "preparation_stage": "Main sol. 540 (solution
    1194, declared 1015 mL)", "decision_rationale": "This is a stock composition or
    a direct contribution currently combined with a stock value. Preserve original
    batch amount, exact source form and stock stage; do not use this stock strength
    as a direct final-medium concentration.", "evidence_id": "quantity-5", "arithmetic_separate_from_quote":
    "Original 7 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 6.896551724137931034482758621
    g/L on the provider-declared stage volume; reported g_l is 6.89655. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "name": "NaCl", "current": {"value":
    "7.89655", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[4].concentration", "name": "NaCl", "current": {"value":
    "7.89655", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[4].concentration", "name": "NaCl", "current": {"value":
    "7.89655", "unit": "G_PER_L"}}], "source_amount": 7, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 6.89655, "provider_stage_volume_ml": 1015, "primary_source_evidence_id":
    "dsmz540"}, {"field_path": "ingredients[5].concentration", "name": "MgCl2 x 6
    H2O", "current": {"value": "1.18227", "unit": "G_PER_L"}, "decision": "evidence_only",
    "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 1.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.18227,\n                        \"mmol_l\":
    5.81529,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[5]", "preparation_stage": "Main sol. 540 (solution
    1194, declared 1015 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1015 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-6", "arithmetic_separate_from_quote":
    "Original 1.2 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 1.182266009852216748768472906
    g/L on the provider-declared stage volume; reported g_l is 1.18227. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "name": "MgCl2 x 6 H2O", "current":
    {"value": "1.18227", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[5].concentration", "name": "MgCl2 x 6 H2O", "current":
    {"value": "1.18227", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[5].concentration", "name": "MgCl2 x 6 H2O", "current":
    {"value": "1.18227", "unit": "G_PER_L"}}], "source_amount": 1.2, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 1.18227, "provider_stage_volume_ml":
    1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[6].concentration",
    "name": "CaCl2 x 2 H2O", "current": {"value": "0.247783", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.147783,\n                        \"mmol_l\":
    1.00523,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[6]", "preparation_stage": "Main sol. 540 (solution
    1194, declared 1015 mL)", "decision_rationale": "This is a stock composition or
    a direct contribution currently combined with a stock value. Preserve original
    batch amount, exact source form and stock stage; do not use this stock strength
    as a direct final-medium concentration.", "evidence_id": "quantity-7", "arithmetic_separate_from_quote":
    "Original 0.15 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 0.1477832512315270935960591133
    g/L on the provider-declared stage volume; reported g_l is 0.147783. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "name": "CaCl2 x 2 H2O", "current":
    {"value": "0.247783", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[6].concentration", "name": "CaCl2 x 2 H2O", "current":
    {"value": "0.247783", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[6].concentration", "name": "CaCl2 x 2 H2O", "current":
    {"value": "0.247783", "unit": "G_PER_L"}}], "source_amount": 0.15, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.147783, "provider_stage_volume_ml":
    1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[7].concentration",
    "name": "Yeast extract", "current": {"value": "1.47783", "unit": "G_PER_L"}, "decision":
    "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.47783,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[0].recipe[7]",
    "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale":
    "The current value follows provider g_l on its declared 1015 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.", "evidence_id":
    "quantity-8", "arithmetic_separate_from_quote": "Original 1.5 g × 1 g/g ÷ (1015
    mL / 1000 mL per L) = 1.477832512315270935960591133 g/L on the provider-declared
    stage volume; reported g_l is 1.47783. This is not a receiving-medium dilution.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "name": "Yeast extract", "current":
    {"value": "1.47783", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[7].concentration", "name": "Yeast extract", "current":
    {"value": "1.47783", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[7].concentration", "name": "Yeast extract", "current":
    {"value": "1.47783", "unit": "G_PER_L"}}], "source_amount": 1.5, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 1.47783, "provider_stage_volume_ml":
    1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "source solution
    1194 recipe[8] (not represented)", "name": "Modified Wolin''s mineral solution",
    "current": null, "decision": "add", "source_key": "mediadive540api", "source_quote":
    "{\n                        \"recipe_order\": 9,\n                        \"solution\":
    \"Modified Wolin''s mineral solution\",\n                        \"solution_id\":
    241,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[8]", "preparation_stage": "Main sol. 540 (solution
    1194, declared 1015 mL)", "decision_rationale": "The main recipe explicitly adds
    10 ml of stock 241. Restore this dose and the separate stock definition; the stored
    flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-9",
    "affected_local_fields": [], "source_amount": 10, "source_unit": "ml", "source_attribute":
    null, "provider_g_l": null, "provider_stage_volume_ml": 1015, "primary_source_evidence_id":
    "dsmz540"}, {"field_path": "ingredients[8].concentration", "name": "NiCl2 x 6
    H2O", "current": {"value": "0.030985222", "unit": "G_PER_L"}, "decision": "correct",
    "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000985222,\n                        \"mmol_l\": 0.00760208,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[0].recipe[9]",
    "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale":
    "This is a stock composition or a direct contribution currently combined with
    a stock value. Preserve original batch amount, exact source form and stock stage;
    do not use this stock strength as a direct final-medium concentration.", "evidence_id":
    "quantity-10", "arithmetic_separate_from_quote": "0.1% w/v means 0.1 g per 100
    mL; 1 mL contains 0.001 g. Dividing by provider-declared 1015/1000 L gives 0.0009852216748768472906403940887
    g/L; reported g_l is 0.000985222. Preserve this source stock dose separately.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "name": "NiCl2 x 6 H2O", "current":
    {"value": "0.030985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[8].concentration", "name": "NiCl2 x 6 H2O", "current":
    {"value": "0.030985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[8].concentration", "name": "NiCl2 x 6 H2O", "current":
    {"value": "0.030985222", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit":
    "ml", "source_attribute": "0.1% w/v", "provider_g_l": 0.000985222, "provider_stage_volume_ml":
    1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[9].concentration",
    "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004985222", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.1,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    9.85222e-5,\n                        \"mmol_l\": 0.000298688,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[0].recipe[10]",
    "preparation_stage": "Main sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale":
    "This is a stock composition or a direct contribution currently combined with
    a stock value. Preserve original batch amount, exact source form and stock stage;
    do not use this stock strength as a direct final-medium concentration.", "evidence_id":
    "quantity-11", "arithmetic_separate_from_quote": "0.1% w/v means 0.1 g per 100
    mL; 0.1 mL contains 0.0001 g. Dividing by provider-declared 1015/1000 L gives
    0.00009852216748768472906403940887 g/L; reported g_l is 9.85222e-05. Preserve
    this source stock dose separately.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "name": "Na2WO4 x 2 H2O", "current":
    {"value": "0.0004985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[9].concentration", "name": "Na2WO4 x 2 H2O", "current":
    {"value": "0.0004985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[9].concentration", "name": "Na2WO4 x 2 H2O", "current":
    {"value": "0.0004985222", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit":
    "ml", "source_attribute": "0.1% w/v", "provider_g_l": 9.85222e-05, "provider_stage_volume_ml":
    1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[10].concentration",
    "name": "Ascorbic acid", "current": {"value": "4.92611e-05", "unit": "G_PER_L"},
    "decision": "evidence_only", "source_key": "mediadive540api", "source_quote":
    "{\n                        \"recipe_order\": 12,\n                        \"compound\":
    \"Ascorbic acid\",\n                        \"compound_id\": 112,\n                        \"attribute\":
    \"0.01% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 4.92611e-5,\n                        \"mmol_l\":
    0.000279702,\n                        \"optional\": 0\n                    }",
    "source_locator": "$.data.solutions[0].recipe[11]", "preparation_stage": "Main
    sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current
    value follows provider g_l on its declared 1015 mL basis. Attach exact source
    evidence and retain any percentage-stock attribute and dose. This is provider
    normalization, not an independently measured final volume.", "evidence_id": "quantity-12",
    "arithmetic_separate_from_quote": "0.01% w/v means 0.01 g per 100 mL; 0.5 mL contains
    0.00005 g. Dividing by provider-declared 1015/1000 L gives 0.00004926108374384236453201970443
    g/L; reported g_l is 4.92611e-05. Preserve this source stock dose separately.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "name": "Ascorbic acid", "current":
    {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[10].concentration", "name": "Ascorbic acid", "current":
    {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[10].concentration", "name": "Ascorbic acid", "current":
    {"value": "4.92611e-05", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit":
    "ml", "source_attribute": "0.01% w/v", "provider_g_l": 4.92611e-05, "provider_stage_volume_ml":
    1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[11].concentration",
    "name": "Myo-inositol", "current": {"value": "4.92611e-05", "unit": "G_PER_L"},
    "decision": "evidence_only", "source_key": "mediadive540api", "source_quote":
    "{\n                        \"recipe_order\": 13,\n                        \"compound\":
    \"Myo-inositol\",\n                        \"compound_id\": 557,\n                        \"attribute\":
    \"0.01% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 4.92611e-5,\n                        \"mmol_l\":
    0.00027343,\n                        \"optional\": 0\n                    }",
    "source_locator": "$.data.solutions[0].recipe[12]", "preparation_stage": "Main
    sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current
    value follows provider g_l on its declared 1015 mL basis. Attach exact source
    evidence and retain any percentage-stock attribute and dose. This is provider
    normalization, not an independently measured final volume.", "evidence_id": "quantity-13",
    "arithmetic_separate_from_quote": "0.01% w/v means 0.01 g per 100 mL; 0.5 mL contains
    0.00005 g. Dividing by provider-declared 1015/1000 L gives 0.00004926108374384236453201970443
    g/L; reported g_l is 4.92611e-05. Preserve this source stock dose separately.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "name": "Myo-inositol", "current":
    {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[11].concentration", "name": "Myo-inositol", "current":
    {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[11].concentration", "name": "Myo-inositol", "current":
    {"value": "4.92611e-05", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit":
    "ml", "source_attribute": "0.01% w/v", "provider_g_l": 4.92611e-05, "provider_stage_volume_ml":
    1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[12].concentration",
    "name": "Niacinamide", "current": {"value": "4.92611e-05", "unit": "G_PER_L"},
    "decision": "evidence_only", "source_key": "mediadive540api", "source_quote":
    "{\n                        \"recipe_order\": 14,\n                        \"compound\":
    \"Niacinamide\",\n                        \"compound_id\": 558,\n                        \"attribute\":
    \"0.01% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 4.92611e-5,\n                        \"mmol_l\":
    0.000403366,\n                        \"optional\": 0\n                    }",
    "source_locator": "$.data.solutions[0].recipe[13]", "preparation_stage": "Main
    sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current
    value follows provider g_l on its declared 1015 mL basis. Attach exact source
    evidence and retain any percentage-stock attribute and dose. This is provider
    normalization, not an independently measured final volume.", "evidence_id": "quantity-14",
    "arithmetic_separate_from_quote": "0.01% w/v means 0.01 g per 100 mL; 0.5 mL contains
    0.00005 g. Dividing by provider-declared 1015/1000 L gives 0.00004926108374384236453201970443
    g/L; reported g_l is 4.92611e-05. Preserve this source stock dose separately.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "name": "Niacinamide", "current":
    {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[12].concentration", "name": "Niacinamide", "current":
    {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[12].concentration", "name": "Niacinamide", "current":
    {"value": "4.92611e-05", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit":
    "ml", "source_attribute": "0.01% w/v", "provider_g_l": 4.92611e-05, "provider_stage_volume_ml":
    1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[13].concentration",
    "name": "Choline chloride", "current": {"value": "4.92611e-05", "unit": "G_PER_L"},
    "decision": "evidence_only", "source_key": "mediadive540api", "source_quote":
    "{\n                        \"recipe_order\": 15,\n                        \"compound\":
    \"Choline chloride\",\n                        \"compound_id\": 115,\n                        \"attribute\":
    \"0.01% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 4.92611e-5,\n                        \"mmol_l\":
    0.000352823,\n                        \"optional\": 0\n                    }",
    "source_locator": "$.data.solutions[0].recipe[14]", "preparation_stage": "Main
    sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current
    value follows provider g_l on its declared 1015 mL basis. Attach exact source
    evidence and retain any percentage-stock attribute and dose. This is provider
    normalization, not an independently measured final volume.", "evidence_id": "quantity-15",
    "arithmetic_separate_from_quote": "0.01% w/v means 0.01 g per 100 mL; 0.5 mL contains
    0.00005 g. Dividing by provider-declared 1015/1000 L gives 0.00004926108374384236453201970443
    g/L; reported g_l is 4.92611e-05. Preserve this source stock dose separately.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "name": "Choline chloride", "current":
    {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[13].concentration", "name": "Choline chloride", "current":
    {"value": "4.92611e-05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[13].concentration", "name": "Choline chloride", "current":
    {"value": "4.92611e-05", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit":
    "ml", "source_attribute": "0.01% w/v", "provider_g_l": 4.92611e-05, "provider_stage_volume_ml":
    1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[14].concentration",
    "name": "Sodium resazurin", "current": {"value": "0.000492611", "unit": "G_PER_L"},
    "decision": "evidence_only", "source_key": "mediadive540api", "source_quote":
    "{\n                        \"recipe_order\": 16,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.000492611,\n                        \"mmol_l\":
    0.00196126,\n                        \"optional\": 0\n                    }",
    "source_locator": "$.data.solutions[0].recipe[15]", "preparation_stage": "Main
    sol. 540 (solution 1194, declared 1015 mL)", "decision_rationale": "The current
    value follows provider g_l on its declared 1015 mL basis. Attach exact source
    evidence and retain any percentage-stock attribute and dose. This is provider
    normalization, not an independently measured final volume.", "evidence_id": "quantity-16",
    "arithmetic_separate_from_quote": "0.1% w/v means 0.1 g per 100 mL; 0.5 mL contains
    0.0005 g. Dividing by provider-declared 1015/1000 L gives 0.0004926108374384236453201970443
    g/L; reported g_l is 0.000492611. Preserve this source stock dose separately.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "name": "Sodium resazurin", "current":
    {"value": "0.000492611", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[14].concentration", "name": "Sodium resazurin", "current":
    {"value": "0.000492611", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[14].concentration", "name": "Sodium resazurin", "current":
    {"value": "0.000492611", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit":
    "ml", "source_attribute": "0.1% w/v", "provider_g_l": 0.000492611, "provider_stage_volume_ml":
    1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[15].concentration",
    "name": "NaHCO3", "current": {"value": "3.94089", "unit": "G_PER_L"}, "decision":
    "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    17,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.94089,\n                        \"mmol_l\":
    46.9114,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[16]", "preparation_stage": "Main sol. 540 (solution
    1194, declared 1015 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1015 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-17", "arithmetic_separate_from_quote":
    "Original 4 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 3.940886699507389162561576355
    g/L on the provider-declared stage volume; reported g_l is 3.94089. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "name": "NaHCO3", "current": {"value":
    "3.94089", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[15].concentration", "name": "NaHCO3", "current": {"value":
    "3.94089", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[15].concentration", "name": "NaHCO3", "current": {"value":
    "3.94089", "unit": "G_PER_L"}}], "source_amount": 4, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 3.94089, "provider_stage_volume_ml": 1015, "primary_source_evidence_id":
    "dsmz540"}, {"field_path": "ingredients[16].concentration", "name": "D-Glucose",
    "current": {"value": "4.92611", "unit": "G_PER_L"}, "decision": "evidence_only",
    "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    18,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\":
    211,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.92611,\n                        \"mmol_l\":
    27.343,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[17]", "preparation_stage": "Main sol. 540 (solution
    1194, declared 1015 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1015 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-18", "arithmetic_separate_from_quote":
    "Original 5 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 4.926108374384236453201970443
    g/L on the provider-declared stage volume; reported g_l is 4.92611. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "name": "D-Glucose", "current":
    {"value": "4.92611", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[16].concentration", "name": "D-Glucose", "current":
    {"value": "4.92611", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[16].concentration", "name": "D-Glucose", "current":
    {"value": "4.92611", "unit": "G_PER_L"}}], "source_amount": 5, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 4.92611, "provider_stage_volume_ml":
    1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "source solution
    1194 recipe[18] (not represented)", "name": "Wolin''s vitamin solution (10x)",
    "current": null, "decision": "add", "source_key": "mediadive540api", "source_quote":
    "{\n                        \"recipe_order\": 19,\n                        \"solution\":
    \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[18]", "preparation_stage": "Main sol. 540 (solution
    1194, declared 1015 mL)", "decision_rationale": "The main recipe explicitly adds
    1 ml of stock 5980. Restore this dose and the separate stock definition; the stored
    flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-19",
    "affected_local_fields": [], "source_amount": 1, "source_unit": "ml", "source_attribute":
    null, "provider_g_l": null, "provider_stage_volume_ml": 1015, "primary_source_evidence_id":
    "dsmz540"}, {"field_path": "ingredients[17].concentration", "name": "L-Cysteine
    HCl x H2O", "current": {"value": "0.295566", "unit": "G_PER_L"}, "decision": "evidence_only",
    "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    20,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\":
    770,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.295566,\n                        \"mmol_l\":
    1.68284,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[19]", "preparation_stage": "Main sol. 540 (solution
    1194, declared 1015 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1015 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-20", "arithmetic_separate_from_quote":
    "Original 0.3 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 0.2955665024630541871921182266
    g/L on the provider-declared stage volume; reported g_l is 0.295566. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "name": "L-Cysteine HCl x H2O",
    "current": {"value": "0.295566", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[17].concentration", "name": "L-Cysteine HCl x H2O",
    "current": {"value": "0.295566", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[17].concentration", "name": "L-Cysteine HCl x H2O",
    "current": {"value": "0.295566", "unit": "G_PER_L"}}], "source_amount": 0.3, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.295566, "provider_stage_volume_ml":
    1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[18].concentration",
    "name": "Na2S x 9 H2O", "current": {"value": "0.295566", "unit": "G_PER_L"}, "decision":
    "evidence_only", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    21,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.295566,\n                        \"mmol_l\":
    1.23059,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[20]", "preparation_stage": "Main sol. 540 (solution
    1194, declared 1015 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1015 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-21", "arithmetic_separate_from_quote":
    "Original 0.3 g × 1 g/g ÷ (1015 mL / 1000 mL per L) = 0.2955665024630541871921182266
    g/L on the provider-declared stage volume; reported g_l is 0.295566. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "name": "Na2S x 9 H2O", "current":
    {"value": "0.295566", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[18].concentration", "name": "Na2S x 9 H2O", "current":
    {"value": "0.295566", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[18].concentration", "name": "Na2S x 9 H2O", "current":
    {"value": "0.295566", "unit": "G_PER_L"}}], "source_amount": 0.3, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.295566, "provider_stage_volume_ml":
    1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "source solution
    1194 recipe[21] (not represented)", "name": "Distilled water", "current": null,
    "decision": "add", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    22,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[21]", "preparation_stage": "Main sol. 540 (solution
    1194, declared 1015 mL)", "decision_rationale": "Preserve the source solvent quantity
    1000 ml in its own stage. The provider declares this solution volume as 1015 mL;
    water addition is not independent proof of measured final volume.", "evidence_id":
    "quantity-22", "affected_local_fields": [], "source_amount": 1000, "source_unit":
    "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml":
    1015, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[19].concentration",
    "name": "Nitrilotriacetic acid", "current": {"value": "1.5", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\":
    189,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.84765,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[0]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-23",
    "arithmetic_separate_from_quote": "Original 1.5 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 1.5 g/L on the provider-declared stage volume; reported g_l is 1.5. This
    is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 1.5 g/L × 0.010 L / 1.015 L = 0.01477832512315270935960591133
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[19].concentration",
    "name": "Nitrilotriacetic acid", "current": {"value": "1.5", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[19].concentration", "name": "Nitrilotriacetic acid",
    "current": {"value": "1.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[19].concentration", "name": "Nitrilotriacetic acid",
    "current": {"value": "1.5", "unit": "G_PER_L"}}], "source_amount": 1.5, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 1.5, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[20].concentration",
    "name": "MgSO4 x 7 H2O", "current": {"value": "3", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    12.1716,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[1]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-24",
    "arithmetic_separate_from_quote": "Original 3 g × 1 g/g ÷ (1000 mL / 1000 mL per
    L) = 3 g/L on the provider-declared stage volume; reported g_l is 3. This is not
    a receiving-medium dilution. Conditional receiving-medium contribution only: provider
    stock 3 g/L × 0.010 L / 1.015 L = 0.02955665024630541871921182266 g/L. Do not
    encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[20].concentration",
    "name": "MgSO4 x 7 H2O", "current": {"value": "3", "unit": "G_PER_L"}}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path":
    "ingredients[20].concentration", "name": "MgSO4 x 7 H2O", "current": {"value":
    "3", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[20].concentration", "name": "MgSO4 x 7 H2O", "current":
    {"value": "3", "unit": "G_PER_L"}}], "source_amount": 3, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 3, "provider_stage_volume_ml": 1000, "primary_source_evidence_id":
    "dsmz540"}, {"field_path": "ingredients[21].concentration", "name": "MnSO4 x H2O",
    "current": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "source_key":
    "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\":
    14,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.9583,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[2]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-25",
    "arithmetic_separate_from_quote": "Original 0.5 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.5 g/L on the provider-declared stage volume; reported g_l is 0.5. This
    is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.5 g/L × 0.010 L / 1.015 L = 0.004926108374384236453201970443
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[21].concentration",
    "name": "MnSO4 x H2O", "current": {"value": "0.5", "unit": "G_PER_L"}}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path":
    "ingredients[21].concentration", "name": "MnSO4 x H2O", "current": {"value": "0.5",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[21].concentration", "name": "MnSO4 x H2O", "current":
    {"value": "0.5", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "g",
    "source_attribute": null, "provider_g_l": 0.5, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[4].concentration",
    "name": "NaCl", "current": {"value": "7.89655", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    17.1116,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[3]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-26",
    "arithmetic_separate_from_quote": "Original 1 g × 1 g/g ÷ (1000 mL / 1000 mL per
    L) = 1 g/L on the provider-declared stage volume; reported g_l is 1. This is not
    a receiving-medium dilution. Conditional receiving-medium contribution only: provider
    stock 1 g/L × 0.010 L / 1.015 L = 0.009852216748768472906403940887 g/L. Do not
    encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[4].concentration",
    "name": "NaCl", "current": {"value": "7.89655", "unit": "G_PER_L"}}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path":
    "ingredients[4].concentration", "name": "NaCl", "current": {"value": "7.89655",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[4].concentration", "name": "NaCl", "current": {"value":
    "7.89655", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 1, "provider_stage_volume_ml": 1000, "primary_source_evidence_id":
    "dsmz540"}, {"field_path": "ingredients[22].concentration", "name": "FeSO4 x 7
    H2O", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "source_key":
    "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.359693,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[4]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-27",
    "arithmetic_separate_from_quote": "Original 0.1 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.1 g/L on the provider-declared stage volume; reported g_l is 0.1. This
    is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.1 g/L × 0.010 L / 1.015 L = 0.0009852216748768472906403940887
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[22].concentration",
    "name": "FeSO4 x 7 H2O", "current": {"value": "0.1", "unit": "G_PER_L"}}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path":
    "ingredients[22].concentration", "name": "FeSO4 x 7 H2O", "current": {"value":
    "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[22].concentration", "name": "FeSO4 x 7 H2O", "current":
    {"value": "0.1", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit": "g",
    "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[23].concentration",
    "name": "CoSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\":
    198,\n                        \"amount\": 0.18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\":
    1.16132,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[5]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-28",
    "arithmetic_separate_from_quote": "Original 0.18 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.18 g/L on the provider-declared stage volume; reported g_l is 0.18.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.18 g/L × 0.010 L / 1.015 L = 0.001773399014778325123152709360
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[23].concentration",
    "name": "CoSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path":
    "ingredients[23].concentration", "name": "CoSO4 x 7 H2O", "current": {"value":
    "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[23].concentration", "name": "CoSO4 x 7 H2O", "current":
    {"value": "0.18", "unit": "G_PER_L"}}], "source_amount": 0.18, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.18, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[6].concentration",
    "name": "CaCl2 x 2 H2O", "current": {"value": "0.247783", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.680203,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[6]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-29",
    "arithmetic_separate_from_quote": "Original 0.1 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.1 g/L on the provider-declared stage volume; reported g_l is 0.1. This
    is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.1 g/L × 0.010 L / 1.015 L = 0.0009852216748768472906403940887
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[6].concentration",
    "name": "CaCl2 x 2 H2O", "current": {"value": "0.247783", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[6].concentration", "name": "CaCl2 x 2 H2O", "current":
    {"value": "0.247783", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[6].concentration", "name": "CaCl2 x 2 H2O", "current":
    {"value": "0.247783", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[24].concentration",
    "name": "ZnSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 0.18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\":
    0.625954,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[7]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-30",
    "arithmetic_separate_from_quote": "Original 0.18 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.18 g/L on the provider-declared stage volume; reported g_l is 0.18.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.18 g/L × 0.010 L / 1.015 L = 0.001773399014778325123152709360
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[24].concentration",
    "name": "ZnSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path":
    "ingredients[24].concentration", "name": "ZnSO4 x 7 H2O", "current": {"value":
    "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[24].concentration", "name": "ZnSO4 x 7 H2O", "current":
    {"value": "0.18", "unit": "G_PER_L"}}], "source_amount": 0.18, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.18, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[25].concentration",
    "name": "CuSO4 x 5 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\":
    121,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0400503,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[8]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-31",
    "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.01 g/L × 0.010 L / 1.015 L = 0.00009852216748768472906403940887
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[25].concentration",
    "name": "CuSO4 x 5 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path":
    "ingredients[25].concentration", "name": "CuSO4 x 5 H2O", "current": {"value":
    "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[25].concentration", "name": "CuSO4 x 5 H2O", "current":
    {"value": "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.01, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[26].concentration",
    "name": "AlK(SO4)2 x 12 H2O", "current": {"value": "0.02", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\":
    908,\n                        \"amount\": 0.02,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0421596,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[9]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-32",
    "arithmetic_separate_from_quote": "Original 0.02 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.02 g/L on the provider-declared stage volume; reported g_l is 0.02.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.02 g/L × 0.010 L / 1.015 L = 0.0001970443349753694581280788177
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[26].concentration",
    "name": "AlK(SO4)2 x 12 H2O", "current": {"value": "0.02", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[26].concentration", "name": "AlK(SO4)2 x 12 H2O", "current":
    {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[26].concentration", "name": "AlK(SO4)2 x 12 H2O", "current":
    {"value": "0.02", "unit": "G_PER_L"}}], "source_amount": 0.02, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.02, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[27].concentration",
    "name": "H3BO3", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.161708,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[10]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-33",
    "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.01 g/L × 0.010 L / 1.015 L = 0.00009852216748768472906403940887
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[27].concentration",
    "name": "H3BO3", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[27].concentration", "name": "H3BO3", "current": {"value":
    "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[27].concentration", "name": "H3BO3", "current": {"value":
    "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 0.01, "provider_stage_volume_ml": 1000, "primary_source_evidence_id":
    "dsmz540"}, {"field_path": "ingredients[28].concentration", "name": "Na2MoO4 x
    2 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct",
    "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0413309,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[11]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-34",
    "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.01 g/L × 0.010 L / 1.015 L = 0.00009852216748768472906403940887
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[28].concentration",
    "name": "Na2MoO4 x 2 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path":
    "ingredients[28].concentration", "name": "Na2MoO4 x 2 H2O", "current": {"value":
    "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[28].concentration", "name": "Na2MoO4 x 2 H2O", "current":
    {"value": "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.01, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[8].concentration",
    "name": "NiCl2 x 6 H2O", "current": {"value": "0.030985222", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.231483,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[12]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-35",
    "arithmetic_separate_from_quote": "Original 0.03 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.03 g/L on the provider-declared stage volume; reported g_l is 0.03.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.03 g/L × 0.010 L / 1.015 L = 0.0002955665024630541871921182266
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[8].concentration",
    "name": "NiCl2 x 6 H2O", "current": {"value": "0.030985222", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[8].concentration", "name": "NiCl2 x 6 H2O", "current":
    {"value": "0.030985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[8].concentration", "name": "NiCl2 x 6 H2O", "current":
    {"value": "0.030985222", "unit": "G_PER_L"}}], "source_amount": 0.03, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.03, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[29].concentration",
    "name": "Na2SeO3 x 5 H2O", "current": {"value": "0.0003", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\":
    0.00114062,\n                        \"optional\": 0\n                    }",
    "source_locator": "$.data.solutions[1].recipe[13]", "preparation_stage": "Modified
    Wolin''s mineral solution (solution 241, declared 1000 mL)", "decision_rationale":
    "This is a stock composition or a direct contribution currently combined with
    a stock value. Preserve original batch amount, exact source form and stock stage;
    do not use this stock strength as a direct final-medium concentration.", "evidence_id":
    "quantity-36", "arithmetic_separate_from_quote": "Original 0.3 mg × 0.001 g/mg
    ÷ (1000 mL / 1000 mL per L) = 0.0003 g/L on the provider-declared stage volume;
    reported g_l is 0.0003. This is not a receiving-medium dilution. Conditional receiving-medium
    contribution only: provider stock 0.0003 g/L × 0.010 L / 1.015 L = 0.000002955665024630541871921182266
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[29].concentration",
    "name": "Na2SeO3 x 5 H2O", "current": {"value": "0.0003", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[29].concentration", "name": "Na2SeO3 x 5 H2O", "current":
    {"value": "0.0003", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[29].concentration", "name": "Na2SeO3 x 5 H2O", "current":
    {"value": "0.0003", "unit": "G_PER_L"}}], "source_amount": 0.3, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.0003, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[9].concentration",
    "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004985222", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\":
    0.00121267,\n                        \"optional\": 0\n                    }",
    "source_locator": "$.data.solutions[1].recipe[14]", "preparation_stage": "Modified
    Wolin''s mineral solution (solution 241, declared 1000 mL)", "decision_rationale":
    "This is a stock composition or a direct contribution currently combined with
    a stock value. Preserve original batch amount, exact source form and stock stage;
    do not use this stock strength as a direct final-medium concentration.", "evidence_id":
    "quantity-37", "arithmetic_separate_from_quote": "Original 0.4 mg × 0.001 g/mg
    ÷ (1000 mL / 1000 mL per L) = 0.0004 g/L on the provider-declared stage volume;
    reported g_l is 0.0004. This is not a receiving-medium dilution. Conditional receiving-medium
    contribution only: provider stock 0.0004 g/L × 0.010 L / 1.015 L = 0.000003940886699507389162561576355
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[9].concentration",
    "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004985222", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[9].concentration", "name": "Na2WO4 x 2 H2O", "current":
    {"value": "0.0004985222", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[9].concentration", "name": "Na2WO4 x 2 H2O", "current":
    {"value": "0.0004985222", "unit": "G_PER_L"}}], "source_amount": 0.4, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.0004, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "source solution
    241 recipe[15] (not represented)", "name": "Distilled water", "current": null,
    "decision": "add", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[15]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "Preserve the
    source solvent quantity 1000 ml in its own stage. The provider declares this solution
    volume as 1000 mL; water addition is not independent proof of measured final volume.",
    "evidence_id": "quantity-38", "affected_local_fields": [], "source_amount": 1000,
    "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[30].concentration",
    "name": "Biotin", "current": {"value": "0.02", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[0]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-39",
    "arithmetic_separate_from_quote": "Original 20 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.020 g/L on the provider-declared stage volume; reported g_l is 0.02.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.02 g/L × 0.001 L / 1.015 L = 0.00001970443349753694581280788177
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[30].concentration",
    "name": "Biotin", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[30].concentration", "name": "Biotin", "current": {"value":
    "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[30].concentration", "name": "Biotin", "current": {"value":
    "0.02", "unit": "G_PER_L"}}], "source_amount": 20, "source_unit": "mg", "source_attribute":
    null, "provider_g_l": 0.02, "provider_stage_volume_ml": 1000, "primary_source_evidence_id":
    "dsmz540"}, {"field_path": "ingredients[31].concentration", "name": "Folic acid",
    "current": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "source_key":
    "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[1]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-40",
    "arithmetic_separate_from_quote": "Original 20 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.020 g/L on the provider-declared stage volume; reported g_l is 0.02.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.02 g/L × 0.001 L / 1.015 L = 0.00001970443349753694581280788177
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[31].concentration",
    "name": "Folic acid", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path":
    "ingredients[31].concentration", "name": "Folic acid", "current": {"value": "0.02",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[31].concentration", "name": "Folic acid", "current":
    {"value": "0.02", "unit": "G_PER_L"}}], "source_amount": 20, "source_unit": "mg",
    "source_attribute": null, "provider_g_l": 0.02, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[32].concentration",
    "name": "Pyridoxine hydrochloride", "current": {"value": "0.1", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[2]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-41",
    "arithmetic_separate_from_quote": "Original 100 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.100 g/L on the provider-declared stage volume; reported g_l is 0.1.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.1 g/L × 0.001 L / 1.015 L = 0.00009852216748768472906403940887
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[32].concentration",
    "name": "Pyridoxine hydrochloride", "current": {"value": "0.1", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[32].concentration", "name": "Pyridoxine hydrochloride",
    "current": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[32].concentration", "name": "Pyridoxine hydrochloride",
    "current": {"value": "0.1", "unit": "G_PER_L"}}], "source_amount": 100, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[33].concentration",
    "name": "Thiamine HCl", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[3]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-42",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.05 g/L × 0.001 L / 1.015 L = 0.00004926108374384236453201970443
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[33].concentration",
    "name": "Thiamine HCl", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path":
    "ingredients[33].concentration", "name": "Thiamine HCl", "current": {"value":
    "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[33].concentration", "name": "Thiamine HCl", "current":
    {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg",
    "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[34].concentration",
    "name": "Riboflavin", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[4]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-43",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.05 g/L × 0.001 L / 1.015 L = 0.00004926108374384236453201970443
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[34].concentration",
    "name": "Riboflavin", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path":
    "ingredients[34].concentration", "name": "Riboflavin", "current": {"value": "0.05",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[34].concentration", "name": "Riboflavin", "current":
    {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg",
    "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[35].concentration",
    "name": "Nicotinic acid", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[5]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-44",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.05 g/L × 0.001 L / 1.015 L = 0.00004926108374384236453201970443
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[35].concentration",
    "name": "Nicotinic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path":
    "ingredients[35].concentration", "name": "Nicotinic acid", "current": {"value":
    "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[35].concentration", "name": "Nicotinic acid", "current":
    {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg",
    "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[36].concentration",
    "name": "Calcium D-(+)-pantothenate", "current": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[6]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-45",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.05 g/L × 0.001 L / 1.015 L = 0.00004926108374384236453201970443
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[36].concentration",
    "name": "Calcium D-(+)-pantothenate", "current": {"value": "0.05", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[36].concentration", "name": "Calcium D-(+)-pantothenate",
    "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[36].concentration", "name": "Calcium D-(+)-pantothenate",
    "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[37].concentration",
    "name": "Vitamin B12", "current": {"value": "0.001", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }",
    "source_locator": "$.data.solutions[2].recipe[7]", "preparation_stage": "Wolin''s
    vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale":
    "This is a stock composition or a direct contribution currently combined with
    a stock value. Preserve original batch amount, exact source form and stock stage;
    do not use this stock strength as a direct final-medium concentration.", "evidence_id":
    "quantity-46", "arithmetic_separate_from_quote": "Original 1 mg × 0.001 g/mg ÷
    (1000 mL / 1000 mL per L) = 0.001 g/L on the provider-declared stage volume; reported
    g_l is 0.001. This is not a receiving-medium dilution. Conditional receiving-medium
    contribution only: provider stock 0.001 g/L × 0.001 L / 1.015 L = 9.852216748768472906403940887E-7
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[37].concentration",
    "name": "Vitamin B12", "current": {"value": "0.001", "unit": "G_PER_L"}}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml", "field_path":
    "ingredients[37].concentration", "name": "Vitamin B12", "current": {"value": "0.001",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[37].concentration", "name": "Vitamin B12", "current":
    {"value": "0.001", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "mg",
    "source_attribute": null, "provider_g_l": 0.001, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[38].concentration",
    "name": "p-Aminobenzoic acid", "current": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[8]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-47",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.05 g/L × 0.001 L / 1.015 L = 0.00004926108374384236453201970443
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[38].concentration",
    "name": "p-Aminobenzoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[38].concentration", "name": "p-Aminobenzoic acid",
    "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[38].concentration", "name": "p-Aminobenzoic acid",
    "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "ingredients[39].concentration",
    "name": "(DL)-alpha-Lipoic acid", "current": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[9]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-48",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional receiving-medium contribution
    only: provider stock 0.05 g/L × 0.001 L / 1.015 L = 0.00004926108374384236453201970443
    g/L. Do not encode both this expanded amount and its stock dose.", "affected_local_fields":
    [{"path": "data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml", "field_path": "ingredients[39].concentration",
    "name": "(DL)-alpha-Lipoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml",
    "field_path": "ingredients[39].concentration", "name": "(DL)-alpha-Lipoic acid",
    "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetitomaculum_medium.yaml",
    "field_path": "ingredients[39].concentration", "name": "(DL)-alpha-Lipoic acid",
    "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "source solution
    5980 recipe[10] (not represented)", "name": "Distilled water", "current": null,
    "decision": "add", "source_key": "mediadive540api", "source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[10]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "Preserve the
    source solvent quantity 1000 ml in its own stage. The provider declares this solution
    volume as 1000 mL; water addition is not independent proof of measured final volume.",
    "evidence_id": "quantity-49", "affected_local_fields": [], "source_amount": 1000,
    "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz540"}, {"field_path": "mineral stock
    KOH addition (not quantified)", "name": "mineral stock KOH addition (not quantified)",
    "current": null, "decision": "not_quantified", "source_key": "dsmz540", "source_quote":
    "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add
    minerals. Adjust", "source_locator": "pages 1–2, relevant preparation paragraph",
    "preparation_stage": "mineral stock", "decision_rationale": "KOH is used to set
    pH 6.5 and then final stock pH 7.0. No fixed KOH mass or volume is specified;
    do not infer zero or a typical dose.", "evidence_id": "quantity-50"}, {"field_path":
    "later sterile anoxic stock volumes (not quantified)", "name": "later sterile
    anoxic stock volumes (not quantified)", "current": null, "decision": "not_quantified",
    "source_key": "dsmz540", "source_quote": "and autoclave. Add glucose, vitamins,
    cysteine and sulfide from sterile anoxic stock", "source_locator": "pages 1–2,
    relevant preparation paragraph", "preparation_stage": "main medium after autoclaving",
    "decision_rationale": "The named glucose, vitamin, cysteine and sulfide amounts
    remain explicit above; this preparation passage does not specify all later anoxic-stock
    volumes. They cannot be used to claim an independently measured final receiving
    volume.", "evidence_id": "quantity-51"}, {"field_path": "preparation_steps.initial_pH",
    "name": "Initial pH", "current": null, "decision": "add", "source_key": "dsmz540",
    "source_quote": "Add solid bicarbonate and equilibrate pH to 6.8 with 80% N2 and
    20% CO2 gas mixture,", "source_locator": "page 1, main preparation sentence 2",
    "preparation_stage": "main preparation before dispensing", "decision_rationale":
    "Preserve the explicit initial pH 6.8 adjustment; it is separate from final complete-medium
    pH.", "evidence_id": "quantity-52"}, {"field_path": "ph_range", "name": "Complete-medium
    pH", "current": {"min": 6.8, "max": 7.0}, "decision": "evidence_only", "source_key":
    "dsmz540", "source_quote": "filtration. Adjust pH of complete medium to 6.8 -
    7.0, if necessary.", "source_locator": "page 1, final main preparation sentence",
    "preparation_stage": "complete medium", "decision_rationale": "The existing 6.8–7.0
    range matches the exact source and each owner; retain its complete-medium and
    if-necessary scope.", "evidence_id": "quantity-53"}, {"field_path": "preparation_steps.initial_gas",
    "name": "Initial gas composition", "current": null, "decision": "add", "source_key":
    "dsmz540", "source_quote": "sparge medium with 80% N2 and 20% CO2 gas mixture
    for 30 - 45 min to make it anoxic.", "source_locator": "page 1, first preparation
    sentence", "preparation_stage": "initial anoxic preparation", "decision_rationale":
    "Restore the explicitly stated 80% N2 / 20% CO2 preparation atmosphere; it is
    not an organism incubation phenotype.", "evidence_id": "quantity-54"}, {"field_path":
    "preparation_steps.sparging_duration", "name": "Sparging duration", "current":
    null, "decision": "add", "source_key": "dsmz540", "source_quote": "sparge medium
    with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.", "source_locator":
    "page 1, first preparation sentence", "preparation_stage": "initial anoxic preparation",
    "decision_rationale": "Restore the literal 30–45 min interval; do not replace
    the range by a midpoint.", "evidence_id": "quantity-55"}, {"field_path": "preparation_steps.addition_stock_gas",
    "name": "Gas for separately prepared stocks", "current": null, "decision": "add",
    "source_key": "dsmz540", "source_quote": "solutions prepared under 100% N2 gas
    atmosphere. Vitamins should be sterilized by", "source_locator": "page 1, later
    stock preparation sentence", "preparation_stage": "separately prepared anoxic
    additions", "decision_rationale": "The later glucose, vitamin, cysteine and sulfide
    stocks are prepared under 100% N2. Preserve this distinct stage and the following
    vitamin filtration instruction.", "evidence_id": "quantity-56"}]'
- assessment_id: evidence
  area: evidence
  topic: Claim-level source support and actual reference-check coverage
  outcome: concern
  summary: Neither target nor either maintained owner contains claim-level ingredient
    amount evidence; the target reference diagnostic checked zero evidence references.
    Exact source URLs, original access times/hashes, literal quantity snippets and
    locators are supplied in this review. Add properly scoped evidence in a separate
    curation task, without fabricating evidence slots.
  target_ids:
  - CultureMech:005968
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
  summary: No reviewed layer asserts organism or strain identifiers, assemblies, DOI/PMID
    papers, growth outcomes or KG-Microbe matches. The SOURCE_DUPLICATE relationship
    is assessed separately and does not establish growth equivalence. The broad applications
    and source title do not justify adding organism claims.
  target_ids:
  - CultureMech:005968
  evidence_ids:
  - record
  - owner-0
  - owner-1
findings:
- finding_id: f1
  issue_key: cm005968-stock-stage-collapse
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Stock strengths and direct contributions are combined as final-medium concentrations
  description: 'The source adds 10 mL of mineral stock and 1 mL of 10x vitamin stock,
    each defined separately per 1000 mL. The target and both owners omit those doses
    and store their component strengths directly. Four rows additionally sum direct
    and stock values: NaCl 7.89655, calcium chloride dihydrate 0.247783, nickel chloride
    hexahydrate 0.030985222 and sodium tungstate dihydrate 0.0004985222 g/L. These
    values do not represent the source preparation stages. The full 49-row source
    inventory and two unquantified preparation additions preserve every amount and
    basis; provider 1015 mL is not a measured final volume.'
  target_ids:
  - CultureMech:005968
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz540
  - mediadive540api
  - importer
  - cleanup
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetitomaculum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: cm005968-salt-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydrate and sodium resazurin map to different supplied forms
  description: The explicit nickel chloride hexahydrate is grounded to anhydrous-form
    nickel dichloride, and sodium resazurin to neutral Resazurin. Canonical labels
    and current MIM-key correspondence pass but do not establish these supplied forms.
    No replacement ID is invented and no hydrate mass is converted with an anhydrous
    molecular weight.
  target_ids:
  - CultureMech:005968
  field_paths:
  - ingredients[8].term
  - ingredients[8].mediaingredientmech_chebi_term
  - ingredients[14].term
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz540
  - chebi34887
  - chebi8806
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetitomaculum_medium.yaml
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
  issue_key: cm005968-anoxic-preparation-lost
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The generated recipe omits source-specific anoxic preparation
  description: 'The target and KOMODO owner omit the preparation and filtration/autoclaving
    sequence retained in the DSMZ owner, while presenting Aerobic: Yes. Following
    those incomplete representations would not reproduce the source preparation. The
    missing protocol is specific and recoverable; a generic sterilization step or
    invented cycle would not resolve it.'
  target_ids:
  - CultureMech:005968
  field_paths:
  - preparation_steps
  - notes
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz540
  - komodoMediaList
  - resolver
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetitomaculum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: Native P3.5 (sterilization not specified), with related P3.4
    preparation absence, is major here because the omitted anoxic and differential
    sterilization sequence materially changes reproducibility; the complete exact
    source and DSMZ owner provide it.
- finding_id: f4
  issue_key: cm005968-history-timezones
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Four inherited timestamps have invalid syntax or no timezone
  description: The target and KOMODO owner each retain one malformed .fZ import timestamp
    and one timezone-naive resolver timestamp. The DSMZ owner history is valid and
    timezone-aware. Preserve the old history and distinguish its unknown timezone
    from source retrieval times.
  target_ids:
  - CultureMech:005968
  field_paths:
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - history
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetitomaculum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.4
  native_severity: P4
  normalization_reason: Native P4.4 history completeness is normalized to minor provenance
    impact because malformed and timezone-naive values impede audit timing; no scientific
    quantity depends on assuming their timezone.
actions:
- action_id: a1
  description: Restore the two source-specific stock definitions and their addition
    doses in both maintained contributors; separate direct additions from stock components
    and retain original units/percentage attributes and explicit provider-volume limits.
    Attach narrow evidence to ingredients and root evidence for stock doses, then
    preview source-compatible regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:005968
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetitomaculum_medium.yaml
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
  description: Verify the exact salt/hydrate identities against authoritative terms
    and align primary and secondary mappings while retaining source masses and names.
    Leave genuinely unresolved replacements explicit.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:005968
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetitomaculum_medium.yaml
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
  description: Reconcile the KOMODO note as source catalog context and preserve the
    exact DSMZ preparation in the maintained representation, including gas atmospheres,
    sequencing, filtration and stage-specific pH. Ensure authorized regeneration retains
    the chosen source-supported protocol.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:005968
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetitomaculum_medium.yaml
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
  description: Document historical timestamp interpretation without rewriting append-only
    history; separately authorized future writer changes should emit valid timezone-aware
    UTC timestamps.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:005968
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetitomaculum_medium.yaml
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
- MediaDive declares a 1015 mL main volume. The listed liquid additions total 1014.6
  mL, before any unquantified later anoxic-stock additions. Provider normalization
  is retained as its declared basis, not an independently established final volume.
- All dilution examples are conditional on the explicitly identified provider volume
  and stock strengths. No corrected numerical concentration is written to the corpus.
- Exact KOMODO accession mapping supports source identity only. No species taxonomy,
  strain growth, optimal incubation condition or biological aerobic phenotype was
  inferred from the catalog.
- The primary PDF prints complete stock definitions, so its crossreferences to DSMZ
  141 and 120 are assessed through those reproduced stock sections, not through unrelated
  parent-medium formulations.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- NH4Cl, cysteine hydrochloride monohydrate and sulfide each retain provider g_l 0.295566;
  strict six-decimal rounding of 0.3/1.015 is 0.295567. This last-digit limit is explicit
  and no value is silently normalized.
tags:
- unreviewed-records
- batch-015
- generated-medium
```
