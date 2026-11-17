# Source and formulation review: acetobacterium_dehalogenans_medium (CultureMech:000819)

- Review: 20261021T101058Z-culturemech-000819-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T09:56:51Z
- Finished UTC: 2026-10-21T10:10:58Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 135b identifies the medium, but the target and normalized owner flatten three stock recipes into the medium, add stock and direct magnesium values, and encode 50 mL of 5 N NaOH as 50 g/L. All four preparation steps are retained, including the later syringate feed; the syringate-stock starting water volume and pH follow MediaDive and conflict with the current collection PDF. Nickel hydrate and sodium-resazurin groundings lose supplied-form identity. The owner has a later, supported syringic-acid grounding absent from the generated target. All four diagnostics passed.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 146; batch 015 item 6 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding fourteen task batches contain 140 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 142 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000819 | data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml | generated | acetobacterium_dehalogenans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000819 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:000819 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch015/146/strict.tsv |
| validate-terms | passed | True | CultureMech:000819 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:000819 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:000819 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Scoped timestamp syntax and timezone inspection | passed | False | CultureMech:000819 | 18 timestamps inspected, 0 invalid or timezone-naive; old provenance remains unchanged. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:000819.

The four documented recipes completed; interpret the scope of each separately.

### Exact source identity and maintained owner

identity: supported. Targets: CultureMech:000819.

The target and sole normalized owner share CM000819 and DSMZ/MediaDive accession 135b. The exact primary and provider title agree with both. The generated merge explicitly names this owner; the later owner syringic-acid grounding is assessed separately. All current inspected input hashes match.

### Stock references and source-section boundaries

scope: concern. Targets: CultureMech:000819.

The source medium explicitly adds mineral stock 241, vitamin stock 5980 and syringate stock 6318 at 20, 1 and 15 mL. Their complete definitions occur within the exact medium PDF and API. The parent-medium labels 141 and 120 identify the included mineral and vitamin sections; no whole parent basal medium is substituted. Neither local layer encodes solutions, parent_media, variant_children or a separate initial-versus-fed variant. The existing post-start feed is retained as an ordered instruction.

### Primary labels/forms and pinned secondary correspondence

grounding: supported. Targets: CultureMech:000819.

Layer-specific counts are {"target": {"ingredient_instances": 34, "primary_CHEBI_instances": 32, "secondary_current_asserted_instances": 30, "secondary_current_verified_instances": 30, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 94.12, "secondary_verified_percent": 88.24}, "owner-0": {"ingredient_instances": 34, "primary_CHEBI_instances": 33, "secondary_current_asserted_instances": 30, "secondary_current_verified_instances": 30, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.06, "secondary_verified_percent": 88.24}}. Percentages are 0–100 linkage coverage over direct ingredient instances, not scientific accuracy. The 0 legacy link instances across reviewed layers are unverified by the current CHEBI-keyed snapshot; absence here does not prove historical invalidity. Current secondary keys without a live preferred-term row are []. No secondary linked-set percentage is invented for an empty set.

{"label_drift": [], "legacy": [], "missing_current_secondary": []}

### Exact supplied forms and salt preparation

grounding: concern. Targets: CultureMech:000819.

Every asserted primary term resolves with its current canonical label. Nickel hexahydrate is nevertheless mapped to anhydrous CHEBI:34887, and sodium resazurin to sodium-free CHEBI:8806. The other explicit hydrate forms, including cysteine hydrochloride monohydrate, are supported at their stated scope. D-(+)-calcium pantothenate agrees with the D-specific CHEBI:31345 structure; generic CHEBI:16494 has no selected stereochemistry contradicting source DL lipoic acid. Owner CHEBI:68329 denotes the neutral syringic-acid precursor, not sodium syringate in the prepared stock. Vitamin B12 remains the source-level class without selecting a specific cobalamin. Yeast extract remains unresolved rather than receiving a guessed ID.

### Preserved process, explicit stock-version conflict and feed scope

consistency: concern. Targets: CultureMech:000819.

All four preparation steps occur in both local layers. Main anoxic preparation, separate gas atmospheres, filtration of vitamins, final pH 7.4, mineral-stock pH 6.5 then 7.0, the after-growth final 2 g/L Na-syringate feed and stock 121 °C sterilization are retained. The syringate dissolution text follows MediaDive 700 mL/about pH 7.5 rather than the current DSMZ PDF 800 mL/about pH 7.0. Both retain makeup to 1000 mL and approximately 50 mL of 5 N NaOH. No source states the stock autoclave duration or all later addition volumes; no generic cycle or measured final volume is supplied.

### Composition, physical state and application scope

scope: supported. Targets: CultureMech:000819.

COMPLEX/UNDEFINED agrees with explicit yeast extract and provider complex_medium=yes. LIQUID is consistent with this exact nongelled recipe. Bacterial filing and generic microbial cultivation are catalog-level descriptions; the name is not evidence for a taxon, strain, growth outcome or optima.

### Append-only history and timestamp interpretation

provenance: supported. Targets: CultureMech:000819.

18 exact timestamp instances were examined; 0 lack valid syntax or explicit timezone. No local timestamp was assumed UTC or rewritten. Process and confidence annotations are not independent scientific evidence.

[]

### Every stored amount, stock dose and source-stage dependency

quantity: concern. Targets: CultureMech:000819.

All 34 ingredient amounts in each local layer are traced to all 42 literal provider recipe rows and 16 explicit quantitative preparation or unquantified-dose decisions. Each has a native decision token, exact quote and locator, stage and rationale; arithmetic is separate. Main magnesium would contain 0.10 g + (3 g/L × 0.020 L) = 0.16 g before a receiving-volume division, not the local sum of concentrations. Main listed liquids total 1006.5 mL versus provider 1006 mL. Nominal syringate-stock 60 g/L acid × 15 mL is 0.9 g acid precursor, distinct from the after-growth final 2 g/L sodium salt condition. No measured final volume or exact feed volume is invented.

[{"field_path": "ingredients[0].concentration", "name": "NH4Cl", "current": {"value": "0.994036", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.994036,\n                        \"mmol_l\": 18.5836,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[0]", "preparation_stage": "Main sol. 135b (solution 233, declared 1006 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1006 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-1", "arithmetic_separate_from_quote": "Original 1 g × 1 g/g ÷ (1006 mL / 1000 mL per L) = 0.9940357852882703777335984095 g/L on the provider-declared stage volume; reported g_l is 0.994036. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "name": "NH4Cl", "current": {"value": "0.994036", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[0].concentration", "name": "NH4Cl", "current": {"value": "0.994036", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.994036, "provider_stage_volume_ml": 1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[1].concentration", "name": "KH2PO4", "current": {"value": "0.328032", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.328032,\n                        \"mmol_l\": 2.41049,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[1]", "preparation_stage": "Main sol. 135b (solution 233, declared 1006 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1006 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-2", "arithmetic_separate_from_quote": "Original 0.33 g × 1 g/g ÷ (1006 mL / 1000 mL per L) = 0.3280318091451292246520874751 g/L on the provider-declared stage volume; reported g_l is 0.328032. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "name": "KH2PO4", "current": {"value": "0.328032", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[1].concentration", "name": "KH2PO4", "current": {"value": "0.328032", "unit": "G_PER_L"}}], "source_amount": 0.33, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.328032, "provider_stage_volume_ml": 1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[2].concentration", "name": "K2HPO4", "current": {"value": "0.447316", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.45,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.447316,\n                        \"mmol_l\": 2.56818,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[2]", "preparation_stage": "Main sol. 135b (solution 233, declared 1006 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1006 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-3", "arithmetic_separate_from_quote": "Original 0.45 g × 1 g/g ÷ (1006 mL / 1000 mL per L) = 0.4473161033797216699801192843 g/L on the provider-declared stage volume; reported g_l is 0.447316. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "name": "K2HPO4", "current": {"value": "0.447316", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[2].concentration", "name": "K2HPO4", "current": {"value": "0.447316", "unit": "G_PER_L"}}], "source_amount": 0.45, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.447316, "provider_stage_volume_ml": 1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[3].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "3.0994036", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0994036,\n                        \"mmol_l\": 0.403299,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[3]", "preparation_stage": "Main sol. 135b (solution 233, declared 1006 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-4", "arithmetic_separate_from_quote": "Original 0.1 g × 1 g/g ÷ (1006 mL / 1000 mL per L) = 0.09940357852882703777335984095 g/L on the provider-declared stage volume; reported g_l is 0.0994036. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "3.0994036", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[3].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "3.0994036", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.0994036, "provider_stage_volume_ml": 1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "source solution 233 recipe[4] (not represented)", "name": "Modified Wolin's mineral solution", "current": null, "decision": "add", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[4]", "preparation_stage": "Main sol. 135b (solution 233, declared 1006 mL)", "decision_rationale": "The main recipe explicitly adds 20 ml of stock 241. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-5", "affected_local_fields": [], "source_amount": 20, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[4].concentration", "name": "Yeast extract", "current": {"value": "1.98807", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.98807,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[5]", "preparation_stage": "Main sol. 135b (solution 233, declared 1006 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1006 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-6", "arithmetic_separate_from_quote": "Original 2 g × 1 g/g ÷ (1006 mL / 1000 mL per L) = 1.988071570576540755467196819 g/L on the provider-declared stage volume; reported g_l is 1.98807. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "name": "Yeast extract", "current": {"value": "1.98807", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[4].concentration", "name": "Yeast extract", "current": {"value": "1.98807", "unit": "G_PER_L"}}], "source_amount": 2, "source_unit": "g", "source_attribute": null, "provider_g_l": 1.98807, "provider_stage_volume_ml": 1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[5].concentration", "name": "Sodium resazurin", "current": {"value": "0.000497018", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000497018,\n                        \"mmol_l\": 0.00197881,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[6]", "preparation_stage": "Main sol. 135b (solution 233, declared 1006 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1006 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-7", "arithmetic_separate_from_quote": "0.1% w/v means 0.1 g per 100 mL; 0.5 mL contains 0.0005 g. Dividing by provider-declared 1006/1000 L gives 0.0004970178926441351888667992048 g/L; reported g_l is 0.000497018. Preserve this source stock dose separately.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "name": "Sodium resazurin", "current": {"value": "0.000497018", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[5].concentration", "name": "Sodium resazurin", "current": {"value": "0.000497018", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "ml", "source_attribute": "0.1% w/v", "provider_g_l": 0.000497018, "provider_stage_volume_ml": 1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[6].concentration", "name": "Na2CO3", "current": {"value": "1.49105", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.49105,\n                        \"mmol_l\": 14.0681,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[7]", "preparation_stage": "Main sol. 135b (solution 233, declared 1006 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1006 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-8", "arithmetic_separate_from_quote": "Original 1.5 g × 1 g/g ÷ (1006 mL / 1000 mL per L) = 1.491053677932405566600397614 g/L on the provider-declared stage volume; reported g_l is 1.49105. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "name": "Na2CO3", "current": {"value": "1.49105", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[6].concentration", "name": "Na2CO3", "current": {"value": "1.49105", "unit": "G_PER_L"}}], "source_amount": 1.5, "source_unit": "g", "source_attribute": null, "provider_g_l": 1.49105, "provider_stage_volume_ml": 1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "source solution 233 recipe[8] (not represented)", "name": "Na-syringate solution (0.3 M)", "current": null, "decision": "add", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Na-syringate solution (0.3 M)\",\n                        \"solution_id\": 6318,\n                        \"amount\": 15,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[8]", "preparation_stage": "Main sol. 135b (solution 233, declared 1006 mL)", "decision_rationale": "The main recipe explicitly adds 15 ml of stock 6318. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-9", "affected_local_fields": [], "source_amount": 15, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "source solution 233 recipe[9] (not represented)", "name": "Wolin's vitamin solution (10x)", "current": null, "decision": "add", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 10,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[9]", "preparation_stage": "Main sol. 135b (solution 233, declared 1006 mL)", "decision_rationale": "The main recipe explicitly adds 1 ml of stock 5980. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-10", "affected_local_fields": [], "source_amount": 1, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[7].concentration", "name": "L-Cysteine HCl x H2O", "current": {"value": "0.497018", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.497018,\n                        \"mmol_l\": 2.82982,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[10]", "preparation_stage": "Main sol. 135b (solution 233, declared 1006 mL)", "decision_rationale": "The current value follows provider g_l on its declared 1006 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume.", "evidence_id": "quantity-11", "arithmetic_separate_from_quote": "Original 0.5 g × 1 g/g ÷ (1006 mL / 1000 mL per L) = 0.4970178926441351888667992048 g/L on the provider-declared stage volume; reported g_l is 0.497018. This is not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "name": "L-Cysteine HCl x H2O", "current": {"value": "0.497018", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[7].concentration", "name": "L-Cysteine HCl x H2O", "current": {"value": "0.497018", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.497018, "provider_stage_volume_ml": 1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "source solution 233 recipe[11] (not represented)", "name": "Distilled water", "current": null, "decision": "add", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 970,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[0].recipe[11]", "preparation_stage": "Main sol. 135b (solution 233, declared 1006 mL)", "decision_rationale": "Preserve the source solvent quantity 970 ml in its own stage. The provider declares this solution volume as 1006 mL; water addition is not independent proof of measured final volume.", "evidence_id": "quantity-12", "affected_local_fields": [], "source_amount": 970, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[8].concentration", "name": "Nitrilotriacetic acid", "current": {"value": "1.5", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[0]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-13", "arithmetic_separate_from_quote": "Original 1.5 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 1.5 g/L on the provider-declared stage volume; reported g_l is 1.5. This is not a receiving-medium dilution. Conditional stock contribution: 1.5 g/L stock × 0.020 L / 1.006 L = 0.02982107355864811133200795229 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "name": "Nitrilotriacetic acid", "current": {"value": "1.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[8].concentration", "name": "Nitrilotriacetic acid", "current": {"value": "1.5", "unit": "G_PER_L"}}], "source_amount": 1.5, "source_unit": "g", "source_attribute": null, "provider_g_l": 1.5, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[3].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "3.0994036", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[1]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-14", "arithmetic_separate_from_quote": "Original 3 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 3 g/L on the provider-declared stage volume; reported g_l is 3. This is not a receiving-medium dilution. Conditional stock contribution: 3 g/L stock × 0.020 L / 1.006 L = 0.05964214711729622266401590457 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "3.0994036", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[3].concentration", "name": "MgSO4 x 7 H2O", "current": {"value": "3.0994036", "unit": "G_PER_L"}}], "source_amount": 3, "source_unit": "g", "source_attribute": null, "provider_g_l": 3, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[9].concentration", "name": "MnSO4 x H2O", "current": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.9583,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[2]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-15", "arithmetic_separate_from_quote": "Original 0.5 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.5 g/L on the provider-declared stage volume; reported g_l is 0.5. This is not a receiving-medium dilution. Conditional stock contribution: 0.5 g/L stock × 0.020 L / 1.006 L = 0.009940357852882703777335984095 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "name": "MnSO4 x H2O", "current": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[9].concentration", "name": "MnSO4 x H2O", "current": {"value": "0.5", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.5, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[10].concentration", "name": "NaCl", "current": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[3]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-16", "arithmetic_separate_from_quote": "Original 1 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 1 g/L on the provider-declared stage volume; reported g_l is 1. This is not a receiving-medium dilution. Conditional stock contribution: 1 g/L stock × 0.020 L / 1.006 L = 0.01988071570576540755467196819 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "name": "NaCl", "current": {"value": "1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[10].concentration", "name": "NaCl", "current": {"value": "1", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "g", "source_attribute": null, "provider_g_l": 1, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[11].concentration", "name": "FeSO4 x 7 H2O", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[4]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-17", "arithmetic_separate_from_quote": "Original 0.1 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.1 g/L on the provider-declared stage volume; reported g_l is 0.1. This is not a receiving-medium dilution. Conditional stock contribution: 0.1 g/L stock × 0.020 L / 1.006 L = 0.001988071570576540755467196819 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "name": "FeSO4 x 7 H2O", "current": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[11].concentration", "name": "FeSO4 x 7 H2O", "current": {"value": "0.1", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[12].concentration", "name": "CoSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 1.16132,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[5]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-18", "arithmetic_separate_from_quote": "Original 0.18 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.18 g/L on the provider-declared stage volume; reported g_l is 0.18. This is not a receiving-medium dilution. Conditional stock contribution: 0.18 g/L stock × 0.020 L / 1.006 L = 0.003578528827037773359840954274 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "name": "CoSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[12].concentration", "name": "CoSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}], "source_amount": 0.18, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.18, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[13].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[6]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-19", "arithmetic_separate_from_quote": "Original 0.1 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.1 g/L on the provider-declared stage volume; reported g_l is 0.1. This is not a receiving-medium dilution. Conditional stock contribution: 0.1 g/L stock × 0.020 L / 1.006 L = 0.001988071570576540755467196819 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[13].concentration", "name": "CaCl2 x 2 H2O", "current": {"value": "0.1", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[14].concentration", "name": "ZnSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.625954,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[7]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-20", "arithmetic_separate_from_quote": "Original 0.18 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.18 g/L on the provider-declared stage volume; reported g_l is 0.18. This is not a receiving-medium dilution. Conditional stock contribution: 0.18 g/L stock × 0.020 L / 1.006 L = 0.003578528827037773359840954274 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "name": "ZnSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[14].concentration", "name": "ZnSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}}], "source_amount": 0.18, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.18, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[15].concentration", "name": "CuSO4 x 5 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[8]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-21", "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01. This is not a receiving-medium dilution. Conditional stock contribution: 0.01 g/L stock × 0.020 L / 1.006 L = 0.0001988071570576540755467196819 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "name": "CuSO4 x 5 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[15].concentration", "name": "CuSO4 x 5 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.01, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[16].concentration", "name": "AlK(SO4)2 x 12 H2O", "current": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0421596,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[9]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-22", "arithmetic_separate_from_quote": "Original 0.02 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.02 g/L on the provider-declared stage volume; reported g_l is 0.02. This is not a receiving-medium dilution. Conditional stock contribution: 0.02 g/L stock × 0.020 L / 1.006 L = 0.0003976143141153081510934393638 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "name": "AlK(SO4)2 x 12 H2O", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[16].concentration", "name": "AlK(SO4)2 x 12 H2O", "current": {"value": "0.02", "unit": "G_PER_L"}}], "source_amount": 0.02, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.02, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[17].concentration", "name": "H3BO3", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[10]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-23", "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01. This is not a receiving-medium dilution. Conditional stock contribution: 0.01 g/L stock × 0.020 L / 1.006 L = 0.0001988071570576540755467196819 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "name": "H3BO3", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[17].concentration", "name": "H3BO3", "current": {"value": "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.01, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[18].concentration", "name": "Na2MoO4 x 2 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[11]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-24", "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01. This is not a receiving-medium dilution. Conditional stock contribution: 0.01 g/L stock × 0.020 L / 1.006 L = 0.0001988071570576540755467196819 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "name": "Na2MoO4 x 2 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[18].concentration", "name": "Na2MoO4 x 2 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.01, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[19].concentration", "name": "NiCl2 x 6 H2O", "current": {"value": "0.03", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.231483,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[12]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-25", "arithmetic_separate_from_quote": "Original 0.03 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 0.03 g/L on the provider-declared stage volume; reported g_l is 0.03. This is not a receiving-medium dilution. Conditional stock contribution: 0.03 g/L stock × 0.020 L / 1.006 L = 0.0005964214711729622266401590457 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "name": "NiCl2 x 6 H2O", "current": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[19].concentration", "name": "NiCl2 x 6 H2O", "current": {"value": "0.03", "unit": "G_PER_L"}}], "source_amount": 0.03, "source_unit": "g", "source_attribute": null, "provider_g_l": 0.03, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[20].concentration", "name": "Na2SeO3 x 5 H2O", "current": {"value": "0.0003", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\": 0.00114062,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[13]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-26", "arithmetic_separate_from_quote": "Original 0.3 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.0003 g/L on the provider-declared stage volume; reported g_l is 0.0003. This is not a receiving-medium dilution. Conditional stock contribution: 0.0003 g/L stock × 0.020 L / 1.006 L = 0.000005964214711729622266401590457 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "name": "Na2SeO3 x 5 H2O", "current": {"value": "0.0003", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[20].concentration", "name": "Na2SeO3 x 5 H2O", "current": {"value": "0.0003", "unit": "G_PER_L"}}], "source_amount": 0.3, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.0003, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[21].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\": 0.00121267,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[14]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-27", "arithmetic_separate_from_quote": "Original 0.4 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.0004 g/L on the provider-declared stage volume; reported g_l is 0.0004. This is not a receiving-medium dilution. Conditional stock contribution: 0.0004 g/L stock × 0.020 L / 1.006 L = 0.000007952286282306163021868787276 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[21].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004", "unit": "G_PER_L"}}], "source_amount": 0.4, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.0004, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "source solution 241 recipe[15] (not represented)", "name": "Distilled water", "current": null, "decision": "add", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[1].recipe[15]", "preparation_stage": "Modified Wolin's mineral solution (solution 241, declared 1000 mL)", "decision_rationale": "Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume.", "evidence_id": "quantity-28", "affected_local_fields": [], "source_amount": 1000, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[22].concentration", "name": "Biotin", "current": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[0]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-29", "arithmetic_separate_from_quote": "Original 20 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.020 g/L on the provider-declared stage volume; reported g_l is 0.02. This is not a receiving-medium dilution. Conditional stock contribution: 0.02 g/L stock × 0.001 L / 1.006 L = 0.00001988071570576540755467196819 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "name": "Biotin", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[22].concentration", "name": "Biotin", "current": {"value": "0.02", "unit": "G_PER_L"}}], "source_amount": 20, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.02, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[23].concentration", "name": "Folic acid", "current": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[1]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-30", "arithmetic_separate_from_quote": "Original 20 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.020 g/L on the provider-declared stage volume; reported g_l is 0.02. This is not a receiving-medium dilution. Conditional stock contribution: 0.02 g/L stock × 0.001 L / 1.006 L = 0.00001988071570576540755467196819 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "name": "Folic acid", "current": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[23].concentration", "name": "Folic acid", "current": {"value": "0.02", "unit": "G_PER_L"}}], "source_amount": 20, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.02, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[24].concentration", "name": "Pyridoxine hydrochloride", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[2]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-31", "arithmetic_separate_from_quote": "Original 100 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.100 g/L on the provider-declared stage volume; reported g_l is 0.1. This is not a receiving-medium dilution. Conditional stock contribution: 0.1 g/L stock × 0.001 L / 1.006 L = 0.00009940357852882703777335984095 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "name": "Pyridoxine hydrochloride", "current": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[24].concentration", "name": "Pyridoxine hydrochloride", "current": {"value": "0.1", "unit": "G_PER_L"}}], "source_amount": 100, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[25].concentration", "name": "Thiamine HCl", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[3]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-32", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional stock contribution: 0.05 g/L stock × 0.001 L / 1.006 L = 0.00004970178926441351888667992048 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "name": "Thiamine HCl", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[25].concentration", "name": "Thiamine HCl", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[26].concentration", "name": "Riboflavin", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[4]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-33", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional stock contribution: 0.05 g/L stock × 0.001 L / 1.006 L = 0.00004970178926441351888667992048 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "name": "Riboflavin", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[26].concentration", "name": "Riboflavin", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[27].concentration", "name": "Nicotinic acid", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[5]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-34", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional stock contribution: 0.05 g/L stock × 0.001 L / 1.006 L = 0.00004970178926441351888667992048 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "name": "Nicotinic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[27].concentration", "name": "Nicotinic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[28].concentration", "name": "Calcium D-(+)-pantothenate", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[6]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-35", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional stock contribution: 0.05 g/L stock × 0.001 L / 1.006 L = 0.00004970178926441351888667992048 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "name": "Calcium D-(+)-pantothenate", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[28].concentration", "name": "Calcium D-(+)-pantothenate", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[29].concentration", "name": "Vitamin B12", "current": {"value": "0.001", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[7]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-36", "arithmetic_separate_from_quote": "Original 1 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.001 g/L on the provider-declared stage volume; reported g_l is 0.001. This is not a receiving-medium dilution. Conditional stock contribution: 0.001 g/L stock × 0.001 L / 1.006 L = 9.940357852882703777335984095E-7 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "name": "Vitamin B12", "current": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[29].concentration", "name": "Vitamin B12", "current": {"value": "0.001", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.001, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[30].concentration", "name": "p-Aminobenzoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[8]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-37", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional stock contribution: 0.05 g/L stock × 0.001 L / 1.006 L = 0.00004970178926441351888667992048 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "name": "p-Aminobenzoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[30].concentration", "name": "p-Aminobenzoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[31].concentration", "name": "(DL)-alpha-Lipoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[9]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-38", "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000 mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05. This is not a receiving-medium dilution. Conditional stock contribution: 0.05 g/L stock × 0.001 L / 1.006 L = 0.00004970178926441351888667992048 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "name": "(DL)-alpha-Lipoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[31].concentration", "name": "(DL)-alpha-Lipoic acid", "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "source solution 5980 recipe[10] (not represented)", "name": "Distilled water", "current": null, "decision": "add", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[2].recipe[10]", "preparation_stage": "Wolin's vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume.", "evidence_id": "quantity-39", "affected_local_fields": [], "source_amount": 1000, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[32].concentration", "name": "Syringic  acid", "current": {"value": "60", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Syringic  acid\",\n                        \"compound_id\": 2124,\n                        \"attribute\": \"SIGMA S6881\",\n                        \"amount\": 60,\n                        \"unit\": \"g\",\n                        \"g_l\": 60,\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[0]", "preparation_stage": "Na-syringate solution (0.3 M) (solution 6318, declared 1000 mL)", "decision_rationale": "This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration.", "evidence_id": "quantity-40", "arithmetic_separate_from_quote": "Original 60 g × 1 g/g ÷ (1000 mL / 1000 mL per L) = 60 g/L on the provider-declared stage volume; reported g_l is 60. This is not a receiving-medium dilution. Conditional stock contribution: 60 g/L stock × 0.015 L / 1.006 L = 0.8946322067594433399602385686 g/L on the provider basis only. For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate concentration. Do not encode both stock addition and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[32].concentration", "name": "Syringic  acid", "current": {"value": "60", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[32].concentration", "name": "Syringic  acid", "current": {"value": "60", "unit": "G_PER_L"}}], "source_amount": 60, "source_unit": "g", "source_attribute": "SIGMA S6881", "provider_g_l": 60, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[33].concentration", "name": "NaOH", "current": {"value": "50", "unit": "G_PER_L"}, "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"attribute\": \"5 N\",\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[1]", "preparation_stage": "Na-syringate solution (0.3 M) (solution 6318, declared 1000 mL)", "decision_rationale": "The row specifies 50 mL of 5 N NaOH in the syringate stock, not 50 g/L direct NaOH. Preserve normality, liquid dose, titration qualifier and stock stage. Both source preparations describe about/around 50 mL, so no exact endpoint-dependent mass is asserted.", "evidence_id": "quantity-41", "arithmetic_separate_from_quote": "For monobasic NaOH, a nominal 50 mL of 5 equivalents/L contains 0.25 mol; using captured CHEBI:32145 mass 39.997 g/mol gives 9.99925 g before dilution or reaction, not 50 g. This conditional illustration is not a replacement stock recipe or a measured final concentration.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "ingredients[33].concentration", "name": "NaOH", "current": {"value": "50", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "ingredients[33].concentration", "name": "NaOH", "current": {"value": "50", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "ml", "source_attribute": "5 N", "provider_g_l": null, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "source solution 6318 recipe[2] (not represented)", "name": "Distilled water", "current": null, "decision": "add", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 950,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_locator": "$.data.solutions[3].recipe[2]", "preparation_stage": "Na-syringate solution (0.3 M) (solution 6318, declared 1000 mL)", "decision_rationale": "Preserve the source solvent quantity 950 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume.", "evidence_id": "quantity-42", "affected_local_fields": [], "source_amount": 950, "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml": 1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "preparation_steps[0].description", "name": "Initial gas composition", "current": "80% N2 / 20% CO2", "decision": "evidence_only", "source_key": "dsmz135b", "source_quote": "bring to the boil and cool to room temperature under 80% N2 and 20% CO2 gas", "source_locator": "page 1, main preparation step 1", "preparation_stage": "initial assembly", "decision_rationale": "The initial gas mixture and same-atmosphere dispensing are retained in both local layers; this is preparation evidence, not a strain phenotype.", "evidence_id": "quantity-43"}, {"field_path": "preparation_steps[0].description", "name": "Gas for separate syringate/vitamin/cysteine stocks", "current": "100% N2", "decision": "evidence_only", "source_key": "dsmz135b", "source_quote": "sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile", "source_locator": "page 1, main preparation step 1", "preparation_stage": "separate sterile addition stocks", "decision_rationale": "Retain the explicit 100% N2 stock-preparation qualifier and its scope; the following carbonate stock has a different atmosphere.", "evidence_id": "quantity-44"}, {"field_path": "preparation_steps[0].description", "name": "Carbonate-stock gas", "current": "80% N2 / 20% CO2", "decision": "evidence_only", "source_key": "dsmz135b", "source_quote": "anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Vitamins", "source_locator": "page 1, main preparation step 1", "preparation_stage": "carbonate stock", "decision_rationale": "The carbonate-stock atmosphere is preserved independently of the preceding 100% N2 stocks.", "evidence_id": "quantity-45"}, {"field_path": "ph_value / preparation_steps[0].description", "name": "Completed-medium pH", "current": 7.4, "decision": "evidence_only", "source_key": "dsmz135b", "source_quote": "should be sterilized by filtration. The pH of the completed medium should be at 7.4.", "source_locator": "page 1, main preparation step 1", "preparation_stage": "completed medium", "decision_rationale": "Both local layers preserve the exact pH 7.4 condition and vitamin filtration. No pH range is invented.", "evidence_id": "quantity-46"}, {"field_path": "preparation_steps[1].description", "name": "After-growth Na-syringate final concentration", "current": "2.00 g/L after growth starts", "decision": "evidence_only", "source_key": "dsmz135b", "source_quote": "a final concentration of 2.00 g/l.", "source_locator": "page 1, main preparation step 2, following explicit after-growth trigger", "preparation_stage": "post-start feed", "decision_rationale": "The target and owner preserve the source after-growth final concentration. This is not 2 g added per original batch, nor the initial 15 mL stock dose; salt-versus-acid mass basis and feed volume are not inferred.", "evidence_id": "quantity-47"}, {"field_path": "preparation_steps[2].description", "name": "Mineral-stock initial pH", "current": 6.5, "decision": "evidence_only", "source_key": "dsmz135b", "source_quote": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust", "source_locator": "page 2, continuation of mineral-stock preparation", "preparation_stage": "mineral stock before other minerals", "decision_rationale": "Preserve the initial pH 6.5 titration stage.", "evidence_id": "quantity-48"}, {"field_path": "preparation_steps[2].description", "name": "Mineral-stock final pH", "current": 7.0, "decision": "evidence_only", "source_key": "dsmz135b", "source_quote": "final to pH 7.0 with KOH.", "source_locator": "page 2, mineral-stock preparation", "preparation_stage": "completed mineral stock", "decision_rationale": "Preserve final pH 7.0 separately from the preceding pH 6.5 step.", "evidence_id": "quantity-49"}, {"field_path": "mineral stock KOH amount", "name": "KOH", "current": null, "decision": "not_quantified", "source_key": "dsmz135b", "source_quote": "final to pH 7.0 with KOH.", "source_locator": "page 2, mineral-stock preparation", "preparation_stage": "mineral-stock titration", "decision_rationale": "The source identifies KOH but gives no fixed amount. Preserve titration without assigning zero or a guessed concentration.", "evidence_id": "quantity-50"}, {"field_path": "preparation_steps[3].description", "name": "Starting water volume", "current": "700 mL", "decision": "conflict", "source_key": "dsmz135b", "source_quote": "Dissolve syringic acid in 800 ml distilled water, add around 50 ml 5 N NaOH, and adjust pH", "source_locator": "page 2, Na-syringate stock preparation", "preparation_stage": "syringate stock dissolution", "decision_rationale": "Current collection PDF specifies 800 mL initially, while the local records and current MediaDive preparation specify 700 mL. Both versions are preserved. Neither initial quantity is the table water amount 950 mL or the final makeup volume.", "evidence_id": "quantity-51"}, {"field_path": "preparation_steps[3].description", "name": "Stock pH endpoint", "current": "about 7.5", "decision": "conflict", "source_key": "dsmz135b", "source_quote": "to about 7.0. Then add water to reach a volume of 1000 ml. Make the solution anoxic by", "source_locator": "page 2, Na-syringate stock preparation", "preparation_stage": "syringate-stock titration", "decision_rationale": "Current PDF specifies about pH 7.0, whereas local/provider text gives about 7.5. This is an explicit source-version conflict; no chronology or automatic replacement is assumed.", "evidence_id": "quantity-52"}, {"field_path": "preparation_steps[3].description", "name": "Approximate NaOH titration dose", "current": "about 50 mL of 5 N", "decision": "evidence_only", "source_key": "dsmz135b", "source_quote": "Dissolve syringic acid in 800 ml distilled water, add around 50 ml 5 N NaOH, and adjust pH", "source_locator": "page 2, Na-syringate stock preparation", "preparation_stage": "syringate-stock titration", "decision_rationale": "Both source versions preserve approximately 50 mL of 5 N NaOH. The approximate dose and pH endpoint qualify the exact-looking table amount; no density conversion is used.", "evidence_id": "quantity-53"}, {"field_path": "preparation_steps[3].description", "name": "Final syringate-stock makeup volume", "current": "1000 mL", "decision": "evidence_only", "source_key": "dsmz135b", "source_quote": "to about 7.0. Then add water to reach a volume of 1000 ml. Make the solution anoxic by", "source_locator": "page 2, Na-syringate stock preparation", "preparation_stage": "syringate-stock final makeup", "decision_rationale": "The 1000 mL instruction is a final makeup volume, distinct from table water 950 mL and initial dissolution water 800/700 mL. Do not add all three water quantities.", "evidence_id": "quantity-54"}, {"field_path": "preparation_steps[3].description", "name": "Syringate-stock gas", "current": "100% N2", "decision": "evidence_only", "source_key": "dsmz135b", "source_quote": "sparging with 100% N2 gas, distribute in anoxic serum vials and autoclave at 121°C.", "source_locator": "page 2, Na-syringate stock preparation", "preparation_stage": "stock anoxic handling", "decision_rationale": "Both local records preserve 100% N2 sparging and anoxic dispensing.", "evidence_id": "quantity-55"}, {"field_path": "preparation_steps[3].description", "name": "Syringate-stock autoclave temperature", "current": "121 °C", "decision": "evidence_only", "source_key": "dsmz135b", "source_quote": "sparging with 100% N2 gas, distribute in anoxic serum vials and autoclave at 121°C.", "source_locator": "page 2, Na-syringate stock preparation", "preparation_stage": "stock sterilization", "decision_rationale": "The source gives 121 °C for this stock. Do not transfer this numeric temperature to the main-medium instruction or invent a cycle duration.", "evidence_id": "quantity-56"}, {"field_path": "preparation_steps[3].duration", "name": "Syringate-stock autoclave duration", "current": null, "decision": "not_quantified", "source_key": "dsmz135b", "source_quote": "sparging with 100% N2 gas, distribute in anoxic serum vials and autoclave at 121°C.", "source_locator": "page 2, Na-syringate stock preparation", "preparation_stage": "stock sterilization", "decision_rationale": "No duration is specified in the complete stock instruction. This is an evidence limit, not permission to insert a generic cycle.", "evidence_id": "quantity-57"}, {"field_path": "later sterile stock volumes", "name": "Unspecified addition-stock volumes", "current": null, "decision": "not_quantified", "source_key": "dsmz135b", "source_quote": "sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from a sterile", "source_locator": "page 1, main preparation step 1", "preparation_stage": "later cysteine/carbonate addition", "decision_rationale": "The source gives their ingredient masses but not all sterile-stock dose volumes. These additions do not establish an exact measured final volume.", "evidence_id": "quantity-58"}]

### Claim-level source support and actual reference-check coverage

evidence: concern. Targets: CultureMech:000819.

Neither local layer supplies claim-level amount evidence; the reference diagnostic performs zero evidence checks. Exact bound collection and provider evidence now traces every amount and version conflict. Their absence from the source records does not imply that quantities are scientifically validated by schema or term checks. Narrow evidence should be attached during separately authorized curation.

### Bounded biological claims and optional entities

scope: not_applicable. Targets: CultureMech:000819.

No organism identifiers, strain assertions, assemblies, DOI/PMID papers, growth results or KG-Microbe matches occur in either complete local record. Generic cultivation and the species-like medium title do not establish such claims. No growth targets or alternate experimental recipes are added.

## Findings

### f1: Stock strengths and liquid NaOH dose replace the named medium formulation

blocker / open / confirmed; issue key: cm000819-stocks-and-naoh-unit.

The local 34-row formula incorporates three undiluted stock recipes instead of their 20, 1 and 15 mL additions. Magnesium is stored as 0.0994036 + 3 = 3.0994036 g/L even though the stock adds only 20 mL; 60 g/L syringic-acid precursor is also a stock strength. The source 50 mL of 5 N NaOH becomes direct 50 g/L. These stage and unit errors make the encoded formula unusable as the named source recipe. Provider 1006 mL and listed liquid 1006.5 mL are preserved as different quantities.

### f2: Nickel hydrate and sodium indicator mappings lose supplied-form identity

major / open / confirmed; issue key: cm000819-hydrate-and-sodium-form.

The explicit NiCl2 x 6 H2O stock constituent maps to CHEBI:34887, whose formula contains no waters, and Sodium resazurin maps to neutral CHEBI:8806 without sodium. Canonical-label and secondary-index correspondence do not prove source-form agreement.

### f3: Syringate-stock preparation differs between the cited collection and provider

major / open / confirmed; issue key: cm000819-syringate-stock-version.

Both local layers retain provider starting water 700 mL and about pH 7.5, while the current exact DSMZ PDF specifies initial 800 mL and about pH 7.0. The source versions agree on approximate 50 mL of 5 N NaOH, makeup to 1000 mL, 100% N2 and 121 °C. Table water 950 mL is a separate representation, not another addition. The record cites the collection PDF without identifying this provider-specific procedural version.

### f4: Generated target lacks the owner’s later syringic-acid grounding

minor / open / confirmed; issue key: cm000819-generated-grounding-lag.

The normalized owner contains CHEBI:68329 for ingredient 32 and a timezone-aware 20 August grounding event. The generated target retains the earlier 6 August merge and has no primary term for that row. Current OLS supports the owner’s neutral acid identity. This comparison does not independently authenticate the historical MIM publication or predict current exporter edge counts.

## Recommended Actions And Acceptance Checks

### a1

Restore three stock definitions and exact doses in the maintained owner, preserve dilute NaOH normality/volume and titration scope, separate direct and stock magnesium contributions, and attach source evidence. Resolve the receiving-volume basis before any final concentration derivation; then preview authorized regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Verify exact supplied-form identifiers in the maintained owner and preserve source masses, hydrates and salt qualifiers. Do not invent replacements or silently convert masses.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve and document the intended source version for the maintained stock preparation, preserving both observed versions and their exact evidence until adjudicated. Keep initial water, table water, final makeup and pH stage distinct; retain the source duration limit.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Retain the verified owner grounding when the source-stage corrections are curated and the generated product is separately regenerated. Preserve append-only history; do not patch the generated file or treat this as a new sodium-syringate grounding.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch015/146/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch015/146/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| source-catalog | /private/tmp/culturemech-review-work-batch015/source-preflight-bound/146/source-catalog.json; Complete bound per-record catalog, raw/text/metadata hashes and actual original capture times | context_only | [{"key": "dsmz135b", "url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf", "status": 200, "accessed_at": "2026-10-21T09:49:54.063702Z", "sha256": "349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2", "metadata_sha256": "0b960e474d68296edbfa5a196561043afe7e87e91656c54a7957ae28f439b63a", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": null}, {"key": "mediadive135bapi", "url": "https://mediadive.dsmz.de/rest/medium/135b", "status": 200, "accessed_at": "2026-10-21T09:49:53.218168Z", "sha256": "6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631", "metadata_sha256": "7c9822a238e3435c7d8eec6355e8803b30add7ecffa8e91b971f61e744f3cf64", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": null}, {"key": "chebi131361", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361", "status": 200, "accessed_at": "2026-10-21T07:33:27.980786Z", "sha256": "643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10", "metadata_sha256": "6db2617d6db6dbd86bf7d3a556b38ea9c4ce51def5fe8bba9af365858cd75d91", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi131361.json"}, {"key": "chebi131527", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527", "status": 200, "accessed_at": "2026-10-20T07:22:08.349487Z", "sha256": "349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3", "metadata_sha256": "3a766b9f2333e4e878844dfc870ba817519bc0f162e20241867c63578da23d0c", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/139/chebi131527.json"}, {"key": "chebi15940", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940", "status": 200, "accessed_at": "2026-10-20T06:55:11.874279Z", "sha256": "3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1", "metadata_sha256": "e7562fd7849a085522d6f2816b44426f9441f649cc5eb073b01dbdfc1f014c03", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15940.json"}, {"key": "chebi15956", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956", "status": 200, "accessed_at": "2026-10-21T08:42:30.425993Z", "sha256": "d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd", "metadata_sha256": "e52c2340aa05039b4c3db0486ec28605382c809f66c738d247c5a79bf847e018", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15956.json"}, {"key": "chebi16494", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494", "status": 200, "accessed_at": "2026-10-20T06:55:13.001958Z", "sha256": "aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1", "metadata_sha256": "5dc4cdf6b7e18e3e9a1cc3b257d7e0390151a592c44d2140fc816236358152a8", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/129/chebi16494.json"}, {"key": "chebi17015", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015", "status": 200, "accessed_at": "2026-10-20T06:55:11.583596Z", "sha256": "f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4", "metadata_sha256": "550b9c89dbe67561dbeff24d27f909c466dee50e589a6b87bd8dec1d776343a1", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi17015.json"}, {"key": "chebi176843", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843", "status": 200, "accessed_at": "2026-10-21T08:17:26.997779Z", "sha256": "b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9", "metadata_sha256": "acfbff41d59e80b1235ae594244cc033d9c608fbc00dd7e14f958a79ce3047fe", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi176843.json"}, {"key": "chebi26710", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710", "status": 200, "accessed_at": "2026-10-21T08:42:42.219040Z", "sha256": "2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e", "metadata_sha256": "b958fd70f3637fa701eeaad458e38c7d16b7054e332506fcdaa247cf75ec5368", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi26710.json"}, {"key": "chebi27470", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470", "status": 200, "accessed_at": "2026-10-20T06:55:10.450814Z", "sha256": "fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f", "metadata_sha256": "72fc9858223c889295c3a4f38bed8284d4bc656950129d666afeefc3e38bfa1e", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi27470.json"}, {"key": "chebi29377", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377", "status": 200, "accessed_at": "2026-10-21T07:31:16.500548Z", "sha256": "21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1", "metadata_sha256": "e874e563999cbf540698c26bbdb00295a3d8b10dcff2c3b999951b75d8532e9d", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/133/chebi29377.json"}, {"key": "chebi30753", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753", "status": 200, "accessed_at": "2026-10-20T06:55:12.829785Z", "sha256": "97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a", "metadata_sha256": "693c039bb1b4c8c97d6e544865a7bd86fe43a028630cbb707e55b715405a05da", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi30753.json"}, {"key": "chebi30961", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961", "status": 200, "accessed_at": "2026-10-21T08:42:44.571163Z", "sha256": "f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d", "metadata_sha256": "3764cce319cbb0849d074b03930586fe88d38b3715e3a03ebba947816c8ca08d", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi30961.json"}, {"key": "chebi31206", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206", "status": 200, "accessed_at": "2026-10-21T08:17:28.439407Z", "sha256": "ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76", "metadata_sha256": "2429062a66eb2c4070802bd9c331cd52c04dc31177203bc5faf978801bfd0cd2", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi31206.json"}, {"key": "chebi31345", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345", "status": 200, "accessed_at": "2026-10-20T06:55:12.450283Z", "sha256": "56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d", "metadata_sha256": "80a34fd39f06278b7a513d5f5f094e77bd7199099d1c3117179a9630f3c1178d", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi31345.json"}, {"key": "chebi31440", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440", "status": 200, "accessed_at": "2026-10-21T08:17:28.489501Z", "sha256": "e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9", "metadata_sha256": "2c5574b80e0c5cdb1912319692ad52060ead0884b613a14d7d8a0ac24d68ae78", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi31440.json"}, {"key": "chebi31795", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795", "status": 200, "accessed_at": "2026-10-21T08:42:45.232212Z", "sha256": "45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb", "metadata_sha256": "f4a78752383e9b0e4bf4d231bd5c6d6812b9083dcd0e3b7ce132fd768157ebb2", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/140/chebi31795.json"}, {"key": "chebi32145", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145", "status": 200, "accessed_at": "2026-10-21T07:33:28.263004Z", "sha256": "db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1", "metadata_sha256": "c5d92c8ffa74d83a51a4511c8930c40eb8fc3f7feecbc5e8a9ef115f2d175603", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch009-tail/087/chebi32145.json"}, {"key": "chebi32312", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312", "status": 200, "accessed_at": "2026-10-21T08:17:28.879505Z", "sha256": "eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9", "metadata_sha256": "15af6d0097b16e29579d099bdfccdaff7965d9fcc8519053242b34f9549d8370", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi32312.json"}, {"key": "chebi33118", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118", "status": 200, "accessed_at": "2026-10-21T08:17:29.364390Z", "sha256": "f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87", "metadata_sha256": "cc933d351148d7c0715ab8a426f30f5b337f0ade4cefae27db6e4b01503e384a", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi33118.json"}, {"key": "chebi34887", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887", "status": 200, "accessed_at": "2026-10-21T08:04:44.093348Z", "sha256": "f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc", "metadata_sha256": "ace22ea0a6afa3fef5a976ed08800e02c88d5027903966b27e57fd6f168edc8a", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi34887.json"}, {"key": "chebi44557", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557", "status": 200, "accessed_at": "2026-10-21T08:46:15.250117Z", "sha256": "de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2", "metadata_sha256": "ed0fbe1210115b31327b59b358a5a8390a3f9b87070a3f1328d1f15844b32f81", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi44557.json"}, {"key": "chebi49105", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105", "status": 200, "accessed_at": "2026-10-20T06:55:10.911379Z", "sha256": "0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4", "metadata_sha256": "5962aead9fc53da7aee732642350213639d620e3292cb1211ff62dcc374fe4e9", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi49105.json"}, {"key": "chebi63036", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036", "status": 200, "accessed_at": "2026-10-21T08:17:29.666916Z", "sha256": "48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3", "metadata_sha256": "b93addd6bedfb21bf70655ad0b6e76e0f59d30bed59ffb79f8ab5dd7c785603b", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/139/chebi63036.json"}, {"key": "chebi63939", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939", "status": 200, "accessed_at": "2026-10-20T06:55:09.796192Z", "sha256": "987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a", "metadata_sha256": "db4f37074b96a1ac5b960deb9fc6a16aa1397619968bc14e31edc1b5844c6017", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi63939.json"}, {"key": "chebi68329", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_68329", "status": 200, "accessed_at": "2026-10-21T09:49:55.684762Z", "sha256": "ab4909b4d8849b2be576c308144e611e48498c72e62bbf71a50ab599f11a241a", "metadata_sha256": "d40b185437a07920a0c4df1c896dc72078ac9153a2fee9aaec52f5c6c0a12c40", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": null}, {"key": "chebi75213", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213", "status": 200, "accessed_at": "2026-10-21T08:17:29.756647Z", "sha256": "b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083", "metadata_sha256": "86cdd4c07b0a7b3c2c4a858d56c49f819c30701d4a7669d89ecacd9dcd07ed91", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/136/chebi75213.json"}, {"key": "chebi75836", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836", "status": 200, "accessed_at": "2026-10-20T06:55:07.038393Z", "sha256": "14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525", "metadata_sha256": "3cc3b4f20f8bba8a11d5f43d16fe9479fe773959c3b9092a18caf6bd410924d7", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi75836.json"}, {"key": "chebi86158", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158", "status": 200, "accessed_at": "2026-10-21T08:17:30.011607Z", "sha256": "b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61", "metadata_sha256": "cad4db43580fd7a702ca8a3e89015b1d837dd83826aca0f237013819dcc80952", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi86158.json"}, {"key": "chebi86364", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364", "status": 200, "accessed_at": "2026-10-21T07:33:35.036768Z", "sha256": "f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069", "metadata_sha256": "bbb983bc358d6ab5b74b0d327e75e243992232621d1b827e9c5cd5d4a2b368a4", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/134/chebi86364.json"}, {"key": "chebi86465", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465", "status": 200, "accessed_at": "2026-10-20T06:55:08.054799Z", "sha256": "5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c", "metadata_sha256": "0b9b603fad389586c6b0e471233285e94bfda8db575e6558608a521f3d7da66d", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi86465.json"}, {"key": "chebi8806", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806", "status": 200, "accessed_at": "2026-10-21T08:17:30.774007Z", "sha256": "e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5", "metadata_sha256": "5b204c6d41931db1f3d77249fa43adfeabb2f474e8054f132da0b2065702882b", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi8806.json"}, {"key": "chebi91244", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244", "status": 200, "accessed_at": "2026-10-20T06:55:07.079384Z", "sha256": "dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa", "metadata_sha256": "0ae2a87eac7f4b379b0dd8645092ea312c0f1ce0774318d6b10ac055f4a37a27", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-work-batch004/sources/chebi91244.json"}, {"key": "chebi91248", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248", "status": 200, "accessed_at": "2026-10-21T08:42:32.136441Z", "sha256": "7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683", "metadata_sha256": "07e956bc7f4e172fd975d96f93fe9c9d096c1ead9bc1b9ec6d48490af2d17083", "content_limit": "Exact source capture for later source-scoped review; no final scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/133/chebi91248.json"}] |
| dsmz135b | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; pages 1–2, complete formulation and preparation | supports | Exact DSMZ 135b collection recipe, both pages read completely and visually inspected from the bound PDF. Main recipe, three named stock sections, after-growth feed and preparation were checked. Footer ©2023 DSMZ is retained without inferring a separate publication date. |
| mediadive135bapi | https://mediadive.dsmz.de/rest/medium/135b; $.data.medium and $.data.solutions[0:4] | supports | Exact medium 135b response: main solution 233 and stocks 241, 5980 and 6318. All recipe rows, source attributes, declared stage volumes and steps inspected. |
| quantity-1 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[0].recipe[0] | supports | The current value follows provider g_l on its declared 1006 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-2 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[0].recipe[1] | supports | The current value follows provider g_l on its declared 1006 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-3 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[0].recipe[2] | supports | The current value follows provider g_l on its declared 1006 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-4 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[0].recipe[3] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-5 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[0].recipe[4] | supports | The main recipe explicitly adds 20 ml of stock 241. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution. |
| quantity-6 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[0].recipe[5] | supports | The current value follows provider g_l on its declared 1006 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-7 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[0].recipe[6] | supports | The current value follows provider g_l on its declared 1006 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-8 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[0].recipe[7] | supports | The current value follows provider g_l on its declared 1006 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-9 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[0].recipe[8] | supports | The main recipe explicitly adds 15 ml of stock 6318. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution. |
| quantity-10 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[0].recipe[9] | supports | The main recipe explicitly adds 1 ml of stock 5980. Restore this dose and the separate stock definition; the stored flat ingredient strengths do not encode its dilution. |
| quantity-11 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[0].recipe[10] | supports | The current value follows provider g_l on its declared 1006 mL basis. Attach exact source evidence and retain any percentage-stock attribute and dose. This is provider normalization, not an independently measured final volume. |
| quantity-12 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[0].recipe[11] | supports | Preserve the source solvent quantity 970 ml in its own stage. The provider declares this solution volume as 1006 mL; water addition is not independent proof of measured final volume. |
| quantity-13 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[0] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-14 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[1] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-15 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[2] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-16 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[3] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-17 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[4] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-18 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[5] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-19 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[6] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-20 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[7] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-21 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[8] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-22 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[9] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-23 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[10] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-24 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[11] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-25 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[12] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-26 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[13] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-27 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[14] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-28 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[1].recipe[15] | supports | Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume. |
| quantity-29 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[2].recipe[0] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-30 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[2].recipe[1] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-31 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[2].recipe[2] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-32 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[2].recipe[3] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-33 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[2].recipe[4] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-34 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[2].recipe[5] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-35 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[2].recipe[6] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-36 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[2].recipe[7] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-37 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[2].recipe[8] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-38 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[2].recipe[9] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-39 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[2].recipe[10] | supports | Preserve the source solvent quantity 1000 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume. |
| quantity-40 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[3].recipe[0] | context_only | This is a stock composition or a direct contribution currently combined with a stock value. Preserve original batch amount, exact source form and stock stage; do not use this stock strength as a direct final-medium concentration. |
| quantity-41 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[3].recipe[1] | context_only | The row specifies 50 mL of 5 N NaOH in the syringate stock, not 50 g/L direct NaOH. Preserve normality, liquid dose, titration qualifier and stock stage. Both source preparations describe about/around 50 mL, so no exact endpoint-dependent mass is asserted. |
| quantity-42 | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[3].recipe[2] | supports | Preserve the source solvent quantity 950 ml in its own stage. The provider declares this solution volume as 1000 mL; water addition is not independent proof of measured final volume. |
| quantity-43 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 1, main preparation step 1 | supports | The initial gas mixture and same-atmosphere dispensing are retained in both local layers; this is preparation evidence, not a strain phenotype. |
| quantity-44 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 1, main preparation step 1 | supports | Retain the explicit 100% N2 stock-preparation qualifier and its scope; the following carbonate stock has a different atmosphere. |
| quantity-45 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 1, main preparation step 1 | supports | The carbonate-stock atmosphere is preserved independently of the preceding 100% N2 stocks. |
| quantity-46 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 1, main preparation step 1 | supports | Both local layers preserve the exact pH 7.4 condition and vitamin filtration. No pH range is invented. |
| quantity-47 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 1, main preparation step 2, following explicit after-growth trigger | supports | The target and owner preserve the source after-growth final concentration. This is not 2 g added per original batch, nor the initial 15 mL stock dose; salt-versus-acid mass basis and feed volume are not inferred. |
| quantity-48 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 2, continuation of mineral-stock preparation | supports | Preserve the initial pH 6.5 titration stage. |
| quantity-49 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 2, mineral-stock preparation | supports | Preserve final pH 7.0 separately from the preceding pH 6.5 step. |
| quantity-50 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 2, mineral-stock preparation | supports | The source identifies KOH but gives no fixed amount. Preserve titration without assigning zero or a guessed concentration. |
| quantity-51 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 2, Na-syringate stock preparation | context_only | Current collection PDF specifies 800 mL initially, while the local records and current MediaDive preparation specify 700 mL. Both versions are preserved. Neither initial quantity is the table water amount 950 mL or the final makeup volume. |
| quantity-52 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 2, Na-syringate stock preparation | context_only | Current PDF specifies about pH 7.0, whereas local/provider text gives about 7.5. This is an explicit source-version conflict; no chronology or automatic replacement is assumed. |
| quantity-53 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 2, Na-syringate stock preparation | supports | Both source versions preserve approximately 50 mL of 5 N NaOH. The approximate dose and pH endpoint qualify the exact-looking table amount; no density conversion is used. |
| quantity-54 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 2, Na-syringate stock preparation | supports | The 1000 mL instruction is a final makeup volume, distinct from table water 950 mL and initial dissolution water 800/700 mL. Do not add all three water quantities. |
| quantity-55 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 2, Na-syringate stock preparation | supports | Both local records preserve 100% N2 sparging and anoxic dispensing. |
| quantity-56 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 2, Na-syringate stock preparation | supports | The source gives 121 °C for this stock. Do not transfer this numeric temperature to the main-medium instruction or invent a cycle duration. |
| quantity-57 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 2, Na-syringate stock preparation | supports | No duration is specified in the complete stock instruction. This is an evidence limit, not permission to insert a generic cycle. |
| quantity-58 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf; page 1, main preparation step 1 | supports | The source gives their ingredient masses but not all sterile-stock dose volumes. These additions do not establish an exact measured final volume. |
| provider-stock-preparation | https://mediadive.dsmz.de/rest/medium/135b; $.data.solutions[3].steps[0].step | context_only | The complete current provider stock instruction agrees with local 700 mL and about pH 7.5 while preserving approximately 50 mL of 5 N NaOH, makeup to 1000 mL, 100% N2 and 121 °C. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; $._embedded.terms[0] | supports | CHEBI:31206 resolves to ammonium chloride and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0] | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0] | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0] | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; $._embedded.terms[0] | supports | CHEBI:8806 resolves to Resazurin and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; $._embedded.terms[0] | supports | CHEBI:29377 resolves to sodium carbonate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; $._embedded.terms[0] | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; $._embedded.terms[0] | supports | CHEBI:44557 resolves to nitrilotriacetic acid and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; $._embedded.terms[0] | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0] | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; $._embedded.terms[0] | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; $._embedded.terms[0] | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0] | supports | CHEBI:86158 resolves to calcium chloride dihydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; $._embedded.terms[0] | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; $._embedded.terms[0] | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; $._embedded.terms[0] | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0] | supports | CHEBI:33118 resolves to boric acid and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0] | supports | CHEBI:75213 resolves to sodium molybdate dihydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0] | supports | CHEBI:34887 resolves to nickel dichloride and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; $._embedded.terms[0] | supports | CHEBI:131361 resolves to disodium selenite pentahydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; $._embedded.terms[0] | supports | CHEBI:63939 resolves to sodium tungstate dihydrate and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
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
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; $._embedded.terms[0] | supports | CHEBI:32145 resolves to sodium hydroxide and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| chebi68329 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_68329; $._embedded.terms[0] | supports | CHEBI:68329 resolves to syringic acid and is not obsolete. Available definitions, formulae, structures and synonyms were inspected; recipe amounts and supplied forms are assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned snapshot; exact MAPPED/preferred_term rows for asserted CHEBI keys and exact legacy-key lookup | supports | {"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count": 9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id", "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech", "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"}, "counts": {"target": {"ingredient_instances": 34, "primary_CHEBI_instances": 32, "secondary_current_asserted_instances": 30, "secondary_current_verified_instances": 30, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 94.12, "secondary_verified_percent": 88.24}, "owner-0": {"ingredient_instances": 34, "primary_CHEBI_instances": 33, "secondary_current_asserted_instances": 30, "secondary_current_verified_instances": 30, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.06, "secondary_verified_percent": 88.24}}, "instances": [{"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[0]", "name": "NH4Cl", "primary": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "canonical_label": "ammonium chloride", "label_equal": true, "definition": ["An inorganic chloride having ammonium as the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:12125-02-9", "gmelin:10120", "kegg.compound:C12538", "kegg.drug:D01139", "wikipedia.en:Ammonium_Chloride"], "generalized_empirical_formula": ["Cl.H4N"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31206"], "inchi_key_string": ["NLXLAEXVIDQMFP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/ClH.H3N/h1H;1H3"], "mass": ["53.492"], "monoisotopic_mass": ["53.00323"], "smiles_string": ["[Cl-].[H][N+]([H])([H])[H]"]}, "synonyms": ["Ammonium chloride", "Ammoniumchlorid", "NH4Cl", "[NH4]Cl", "ammonium chloride", "ammonium chloride", "azanium chloride"], "secondary": {"asserted": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "exact_current_rows": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[1]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "canonical_label": "potassium dihydrogen phosphate", "label_equal": true, "definition": ["A potassium salt in which dihydrogen phosphate(1−) is the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"], "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"], "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]}, "synonyms": ["MKP", "Monopotassium dihydrogen phosphate", "Monopotassium monophosphate", "Monopotassium orthophosphate", "Monopotassium phosphate", "Orthophosphoric acid, monopotassium salt", "Phosphoric acid, monopotassium salt", "Phosphoric acid, potassium salt (1:1)", "Potassium acid phosphate", "Potassium dihydrogen orthophosphate", "Potassium dihydrogen phosphate", "Potassium phosphate monobasic", "Potassium phosphate", "Sorensen's potassium phosphate", "potassium dihydrogen phosphate", "potassium dihydrogen phosphate"], "secondary": {"asserted": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "exact_current_rows": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[2]", "name": "K2HPO4", "primary": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "canonical_label": "dipotassium hydrogen phosphate", "label_equal": true, "definition": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-11-4", "kegg.compound:C13197", "kegg.drug:D02403", "metacyc.compound:CPD0-2433", "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"], "generalized_empirical_formula": ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131527"], "inchi_key_string": ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "secondary": {"asserted": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "exact_current_rows": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[3]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "canonical_label": "magnesium sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505", "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222", "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"], "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "exact_current_rows": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[4]", "name": "Yeast extract"}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[5]", "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806", "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3", "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"], "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]}, "synonyms": ["Resazurin"]}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[6]", "name": "Na2CO3", "primary": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "canonical_label": "sodium carbonate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:497-19-8", "ppdb:594"], "generalized_empirical_formula": ["CO3.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:29377"], "inchi_key_string": ["CDBYLPFSWZWCQE-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/CH2O3.2Na/c2-1(3)4;;/h(H2,2,3,4);;/q;2*+1/p-2"], "mass": ["105.988"], "monoisotopic_mass": ["105.96428"], "smiles_string": ["O=C([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2CO3", "Natriumkarbonat", "disodium carbonate", "disodium trioxidocarbonate", "disodium trioxidocarbonate", "sodium carbonate", "sodium carbonate"], "secondary": {"asserted": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "exact_current_rows": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[7]", "name": "L-Cysteine HCl x H2O", "primary": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride hydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of &lt;small&gt;L&lt;/small&gt;-cysteine hydrochloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326", "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"], "inchi_key_string": ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"], "mass": ["175.637"], "monoisotopic_mass": ["175.00699"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]}, "synonyms": ["(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride monohydrate", "Cysteine hydrochloride", "L-Cysteine monohydrate monochloride", "L-cysteine hydrochloride monohydrate", "L-cysteine hydrochloride--water (1/1)", "L-cysteine hydrochloride--water (1/1)"], "secondary": {"asserted": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "exact_current_rows": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[8]", "name": "Nitrilotriacetic acid", "primary": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "canonical_label": "nitrilotriacetic acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1710776", "cas:139-13-9", "drugbank:DB03040", "gmelin:3726", "kegg.compound:C14695", "pdb-ccd:NTA"], "generalized_empirical_formula": ["C6H9NO6"], "has_alternative_id": ["CHEBI:34889", "CHEBI:44555"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:44557"], "inchi_key_string": ["MGFYIUFZLHCRTH-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"], "mass": ["191.139"], "monoisotopic_mass": ["191.04299"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]}, "synonyms": ["Complexon I", "H3nta", "Komplexon I", "N(CH2-COOH)3", "N,N-bis(carboxymethyl)glycine", "N,N-bis(carboxymethyl)glycine", "NITRILOTRIACETIC ACID", "NTA", "Nitrilotriacetate", "Nitrilotriacetic acid", "Nitrilotriessigsaeure", "Triglycollamic acid", "Trilon A", "alpha,alpha',alpha''-trimethylaminetricarboxylic acid", "nitrilo-2,2',2''-triacetic acid", "tri(carboxymethyl)amine", "triglycine"], "secondary": {"asserted": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "exact_current_rows": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[9]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "canonical_label": "manganese(II) sulfate monohydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of manganese(II) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-96-5", "kegg.drug:D04854", "pubmed:26097037", "reaxys:13153017", "wikipedia.en:Manganese(II)_sulfate"], "generalized_empirical_formula": ["H2O.Mn.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86364"], "inchi_key_string": ["ISPYRSDWRDQNSW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mn.H2O4S.H2O/c;1-5(2,3)4;/h;(H2,1,2,3,4);1H2/q+2;;/p-2"], "mass": ["169.016"], "monoisotopic_mass": ["168.90034"], "smiles_string": ["O.O=S(=O)([O-])[O-].[Mn+2]"]}, "synonyms": ["Manganese sulfate hydrate", "Manganese sulfate monohydrate", "Manganese sulfate", "Manganous sulfate monohydrate", "MnSO4.H2O", "manganese(2+) sulfate monohydrate", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulphate monohydrate", "manganese(II) sulphate monohydrate"], "secondary": {"asserted": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "exact_current_rows": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[10]", "name": "NaCl", "primary": {"id": "CHEBI:26710", "label": "sodium chloride"}, "canonical_label": "sodium chloride", "label_equal": true, "definition": ["An inorganic chloride salt having sodium(1+) as the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula": ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string": ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]}, "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "secondary": {"asserted": {"id": "CHEBI:26710", "label": "sodium chloride"}, "exact_current_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[11]", "name": "FeSO4 x 7 H2O", "primary": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "canonical_label": "iron(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used)."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]}, "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O", "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"], "secondary": {"asserted": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[12]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "canonical_label": "cobalt(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of cobalt(2+) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10026-24-1", "pubmed:10504146", "pubmed:12187935", "pubmed:12209163", "pubmed:12579202", "pubmed:12948248", "pubmed:2227161", "pubmed:24359163", "pubmed:25896363", "wikipedia.en:Cobalt(II)_sulfate"], "generalized_empirical_formula": ["Co.7H2O.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91244"], "inchi_key_string": ["MEYVLGVRTYSQHI-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Co.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["281.101"], "monoisotopic_mass": ["280.95888"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Co+2]"]}, "synonyms": ["Cobalt monosulfate heptahydrate", "cobalt sulfate heptahydrate", "cobalt(2+) sulfate--water (1/7)", "cobalt(2+) sulfate--water (1/7)", "cobalt(II) sulfate heptahydrate", "cobaltous sulfate heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[13]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "canonical_label": "calcium chloride dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of calcium chloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8", "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"], "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass": ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}, "synonyms": ["CaCl2.2H2O", "Calcium chloride hydrate", "Calcium chloride", "calcium chloride--water (1/2)", "calcium chloride--water (1/2)", "calcium dichloride dihydrate"], "secondary": {"asserted": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "exact_current_rows": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[14]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "canonical_label": "zinc sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of zinc sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7446-20-0", "gmelin:47216", "kegg.drug:D01081", "wikipedia.en:Zinc_Sulfate"], "generalized_empirical_formula": ["7H2O.O4S.Zn"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32312"], "inchi_key_string": ["RZLVQBNCHSJZPX-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/H2O4S.7H2O.Zn/c1-5(2,3)4;;;;;;;;/h(H2,1,2,3,4);7*1H2;/q;;;;;;;;+2/p-2"], "mass": ["287.558"], "monoisotopic_mass": ["285.95482"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Zn+2]"]}, "synonyms": ["Zinc sulfate", "ZnSO4.7H2O", "zinc sulfate (1:1) heptahydrate", "zinc sulfate heptahydrate (1:1:7)", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate--water (1/7)", "zinc(2+) sulfate--water (1/7)"], "secondary": {"asserted": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "exact_current_rows": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[15]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "canonical_label": "copper(II) sulfate pentahydrate", "label_equal": true, "definition": ["The pentahydrate of copper(2+) sulfate. A bright blue crystalline solid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-99-8", "kegg.drug:D03613", "pubmed:11407502", "pubmed:12209195", "pubmed:12484481", "pubmed:15040745", "pubmed:15607472", "pubmed:15824790", "pubmed:19346702", "pubmed:2002460", "pubmed:20132934", "pubmed:2913309", "pubmed:3351847", "pubmed:7615984", "pubmed:8878264", "pubmed:9521458", "pubmed:9776063", "reaxys:16499970", "wikipedia.en:Copper(II)_sulfate"], "generalized_empirical_formula": ["Cu.5H2O.O4S"], "has_alternative_id": ["CHEBI:121741", "CHEBI:370227"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31440"], "inchi_key_string": ["JZCCFEFSEZPSOG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Cu.H2O4S.5H2O/c;1-5(2,3)4;;;;;/h;(H2,1,2,3,4);5*1H2/q+2;;;;;;/p-2"], "mass": ["249.684"], "monoisotopic_mass": ["248.93415"], "smiles_string": ["O=S(=O)([O-])[O-].[Cu+2].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H]"]}, "synonyms": ["CuSO4.5H2O", "Cupric sulfate", "copper sulphate(5.H2O)", "copper(2+) sulfate (1:1) pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate--water (1/5)", "copper(2+) sulfate--water (1/5)", "copper(II) sulfate, pentahydrate", "cupric sulfate pentahydrate"], "secondary": {"asserted": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "exact_current_rows": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[16]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "canonical_label": "potassium aluminium sulfate dodecahydrate", "label_equal": true, "definition": ["A hydrate resulting from the the formal combination of anhydrous potassium aluminium sulfate with 12 mol eq. of water."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7784-24-9", "reaxys:14851666", "wikipedia.en:Potassium_alum"], "generalized_empirical_formula": ["Al.12H2O.K.2O4S"], "has_alternative_id": ["CHEBI:31192"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86465"], "inchi_key_string": ["GNHOJBNSNUXZQA-UHFFFAOYSA-J"], "inchi_string": ["InChI=1S/Al.K.2H2O4S.12H2O/c;;2*1-5(2,3)4;;;;;;;;;;;;/h;;2*(H2,1,2,3,4);12*1H2/q+3;+1;;;;;;;;;;;;;;/p-4"], "mass": ["474.386"], "monoisotopic_mass": ["473.97548"], "smiles_string": ["O.O.O.O.O.O.O.O.O.O.O.O.O=S(=O)([O-])[O-].O=S(=O)([O-])[O-].[Al+3].[K+]"]}, "synonyms": ["AlK(SO4)2.12H2O", "Aluminum potassium disulfate dodecahydrate", "Aluminum potassium sulfate dodecahydrate", "Kalinite", "Potash alum dodecahydrate", "Potassium alum dodecahydrate", "Potassium aluminum disulfate dodecahydrate", "aluminium potassium sulfate--water (1/12)", "aluminium potassium sulfate--water (1/12)"], "secondary": {"asserted": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "exact_current_rows": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[17]", "name": "H3BO3", "primary": {"id": "CHEBI:33118", "label": "boric acid"}, "canonical_label": "boric acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["bpdb:2136", "cas:10043-35-3", "cas:11113-50-1", "drugcentral:3035", "gmelin:1585", "kegg.compound:C12486", "kegg.drug:D01089", "molbase:1644", "pdb-ccd:BO3", "ppdb:2136"], "generalized_empirical_formula": ["H3BO3"], "has_alternative_id": ["CHEBI:22911", "CHEBI:31299", "CHEBI:41248"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:33118"], "inchi_key_string": ["KGBXLFKZBHKPEV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"], "mass": ["61.833"], "monoisotopic_mass": ["62.01752"], "smiles_string": ["[H]OB(O[H])O[H]"]}, "synonyms": ["B(OH)3", "BORIC ACID", "Boric acid", "H3BO3", "[B(OH)3]", "boric acid", "boron trihydroxide", "orthoboric acid", "trihydroxidoboron", "trihydroxidoboron"], "secondary": {"asserted": {"id": "CHEBI:33118", "label": "boric acid"}, "exact_current_rows": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[18]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "canonical_label": "sodium molybdate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium molybdate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10102-40-6", "pubmed:20645132", "pubmed:20813395", "pubmed:22663766", "pubmed:3382795", "reaxys:19032996", "wikipedia.en:Sodium_molybdate"], "generalized_empirical_formula": ["2H2O.MoO4.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75213"], "inchi_key_string": ["FDEIWTXVNPKYDL-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/Mo.2Na.2H2O.4O/h;;;2*1H2;;;;/q;2*+1;;;;;2*-1"], "mass": ["241.946"], "monoisotopic_mass": ["243.88573"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]}, "synonyms": ["Disodium molybdate dihydrate", "Molybdic acid, disodium salt, dihydrate", "Na2MoO4.2H2O", "Sodium molybdate(VI) dihydrate", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium orthomolybdate dihydrate"], "secondary": {"asserted": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "exact_current_rows": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[19]", "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "canonical_label": "nickel dichloride", "label_equal": true, "definition": ["A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7718-54-9", "kegg.compound:C14711", "pubmed:11739495", "pubmed:12603851", "pubmed:21928331", "pubmed:23179351", "pubmed:23622879", "pubmed:23702803", "pubmed:23735035", "pubmed:7671317", "reaxys:3902827", "reaxys:8128171", "wikipedia.en:Nickel_dichloride"], "generalized_empirical_formula": ["Cl2Ni"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:34887"], "inchi_key_string": ["QMMRZOWCJAIUJA-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"], "mass": ["129.599"], "monoisotopic_mass": ["127.87305"], "smiles_string": ["[Cl][Ni][Cl]"]}, "synonyms": ["NiCl2", "Nickel chloride", "Nickel(II) chloride", "[NiCl2]", "nickel dichloride", "nickel dichloride", "nickel(2+) chloride", "nickel(2+) chloride", "nickel(II) chloride", "nickel(II) chloride", "nickelous chloride"], "secondary": {"asserted": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "exact_current_rows": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[20]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "canonical_label": "disodium selenite pentahydrate", "label_equal": true, "definition": ["A hydrate that is the pentahydrate form of disodium selenite."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:26970-82-1", "pubmed:15259772", "pubmed:15559373", "pubmed:16126997", "pubmed:17873396", "pubmed:24479345", "pubmed:24716537", "reaxys:14666014", "wikipedia.en:Sodium_selenite"], "generalized_empirical_formula": ["5H2O.2Na.O3Se"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131361"], "inchi_key_string": ["TUANAMBRHOLYTH-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"], "mass": ["263.012"], "monoisotopic_mass": ["263.93363"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2SeO3.5H2O", "Selenious acid disodium salt, pentahydrate", "Sodium selenite pentahydrate", "disodium selenite hydrate", "sodium selenite hydrate", "sodium selenite--water (1/5)", "sodium selenite--water (1/5)"], "secondary": {"asserted": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "exact_current_rows": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[21]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "canonical_label": "sodium tungstate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines to nitrones"], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10213-10-2", "reaxys:13157884", "wikipedia.en:Sodium_tungstate"], "generalized_empirical_formula": ["2H2O.2Na.O4W"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63939"], "inchi_key_string": ["WPZFLQRLSGVIAA-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.2H2O.4O.W/h;;2*1H2;;;;;/q2*+1;;;;;2*-1;"], "mass": ["329.846"], "monoisotopic_mass": ["329.93126"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]}, "synonyms": ["Na2WO4.2H2O", "Tungstic acid, sodium salt, dihydrate", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium orthotungstate dihydrate", "sodium tungstate(VI) dihydrate"], "secondary": {"asserted": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "exact_current_rows": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[22]", "name": "Biotin", "primary": {"id": "CHEBI:15956", "label": "biotin"}, "canonical_label": "biotin", "label_equal": true, "definition": ["An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:58-85-5", "chemspider:149962", "drugbank:DB00121", "drugcentral:373", "foodb.food:FDB014510", "gmelin:1918703", "hmdb:HMDB0000030", "kegg.compound:C00120", "kegg.drug:D00029", "knapsack:C00000756", "lincs.smallmolecule:LSM-3994", "metacyc.compound:BIOTIN", "pdb-ccd:BTN", "pmc:PMC8089577", "pubmed:10064317", "pubmed:10215065", "pubmed:10577274", "pubmed:11435506", "pubmed:11481419", "pubmed:11800048", "pubmed:12055344", "pubmed:12070309", "pubmed:12603856", "pubmed:12803839", "pubmed:15012185", "pubmed:15202718", "pubmed:15272000", "pubmed:15690449", "pubmed:15863846", "pubmed:15899401", "pubmed:15992684", "pubmed:16011464", "pubmed:16195795", "pubmed:16419467", "pubmed:16676358", "pubmed:16677798", "pubmed:16704206", "pubmed:16769720", "pubmed:17297119", "pubmed:1814646", "pubmed:18202531", "pubmed:18452485", "pubmed:18509457", "pubmed:19212411", "pubmed:19319844", "pubmed:19727438", "pubmed:19928962", "pubmed:20967359", "pubmed:20974274", "pubmed:2100006", "pubmed:21248194", "pubmed:21356565", "pubmed:21373679", "pubmed:21596550", "pubmed:21871906", "pubmed:25515858", "pubmed:33346513", "pubmed:33461365", "pubmed:34077272", "pubmed:8333586", "pubmed:8750932", "pubmed:9022537", "pubmed:9038855", "pubmed:9094878", "pubmed:9164991", "pubmed:9176832", "pubmed:9371938", "pubmed:9416479", "reaxys:86838", "wikipedia.en:Biotin"], "generalized_empirical_formula": ["C10H16N2O3S"], "has_alternative_id": ["CHEBI:13905", "CHEBI:22882", "CHEBI:22884", "CHEBI:3108", "CHEBI:41236"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15956"], "inchi_key_string": ["YBJHBAHKTGYVGT-ZKWXMUAHSA-N"], "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"], "mass": ["244.316"], "monoisotopic_mass": ["244.08816"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]}, "synonyms": ["(+)-cis-Hexahydro-2-oxo-1H-thieno[3,4]imidazole-4-valeric acid", "(3aS,4S,6aR)-Hexahydro-2-oxo-1H-thieno[3,4-d]imidazole-4-valeric acid", "5-(2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl)pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "BIOTIN", "Coenzyme R", "D-(+)-biotin", "D-Biotin", "Vitamin H", "biotin", "biotina", "biotine", "biotinum", "cis-(+)-Tetrahydro-2-oxothieno[3,4]imidazoline-4-valeric acid", "cis-Hexahydro-2-oxo-1H-thieno(3,4)imidazole-4-valeric acid", "cis-Tetrahydro-2-oxothieno(3,4-d)imidazoline-4-valeric acid", "vitamin B7"], "secondary": {"asserted": {"id": "CHEBI:15956", "label": "biotin"}, "exact_current_rows": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[23]", "name": "Folic acid", "primary": {"id": "CHEBI:27470", "label": "folic acid"}, "canonical_label": "folic acid", "label_equal": true, "definition": ["An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND606960789", "cas:59-30-3", "chemspider:5815", "drugbank:DB00158", "drugcentral:1231", "foodb.food:FDB014504", "hmdb:HMDB0000121", "kegg.compound:C00504", "kegg.drug:D00070", "knapsack:C00001539", "lincs.smallmolecule:LSM-5355", "metacyc.compound:CPD-12826", "pdb-ccd:FOL", "pubmed:10138938", "pubmed:10897644", "pubmed:10958818", "pubmed:11261364", "pubmed:11451208", "pubmed:11959400", "pubmed:14387833", "pubmed:15321809", "pubmed:15523939", "pubmed:15754725", "pubmed:15797531", "pubmed:15797685", "pubmed:15831910", "pubmed:15990733", "pubmed:16093404", "pubmed:16277678", "pubmed:16380297", "pubmed:16871332", "pubmed:17784727", "pubmed:18788725", "pubmed:19121630", "pubmed:19335717", "pubmed:19355913", "pubmed:24650098", "pubmed:33624660", "pubmed:33965562", "pubmed:33968971", "pubmed:34207319", "pubmed:34219855", "pubmed:7738698", "pubmed:8235383", "pubmed:9040515", "pubmed:9420019", "pubmed:9565830", "pubmed:9683174", "pubmed:9781393", "pubmed:9808640", "pubmed:9808641", "reaxys:100781", "wikipedia.en:Folic_Acid"], "generalized_empirical_formula": ["C19H19N7O6"], "has_alternative_id": ["CHEBI:24075", "CHEBI:42610", "CHEBI:5140", "CHEBI:569217"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:27470"], "inchi_key_string": ["OVBPIULPVIDEAO-LBPRGKRZSA-N"], "inchi_string": ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"], "mass": ["441.404"], "monoisotopic_mass": ["441.13968"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]}, "synonyms": ["(2S)-2-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzamido)pentanedioic acid", "Acfol", "Folate", "Folicet", "Folsaeure", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-[(4-{[(2-amino-4-oxo-1,4-dihydropteridin-6-yl)methyl]amino}phenyl)carbonyl]-L-glutamic acid", "N-pteroyl-L-glutamic acid", "PGA", "PteGlu", "acide folique", "acido folico", "acidum folicum", "folic acid", "pteroyl-L-glutamic acid", "pteroyl-L-monoglutamic acid", "pteroylglutamic acid", "pteroylmonoglutamic acid", "vitamin B11", "vitamin B9", "vitamin Bc", "vitamin Be", "vitamin M"], "secondary": {"asserted": {"id": "CHEBI:27470", "label": "folic acid"}, "exact_current_rows": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[24]", "name": "Pyridoxine hydrochloride", "primary": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "canonical_label": "pyridoxine hydrochloride", "label_equal": true, "definition": ["The hydrochloride salt of pyridoxine."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND500675659", "beilstein:3632435", "cas:58-56-0", "drugbank:DBSALT000151", "foodb.food:FDB000575", "gmelin:1067921", "kegg.drug:D02179", "pubmed:15098856", "pubmed:17416572", "pubmed:17891511", "pubmed:18243627", "pubmed:19481898", "pubmed:20645279", "pubmed:21781646", "pubmed:24421551", "pubmed:27468034", "pubmed:28095734", "pubmed:32460509", "pubmed:33209152", "pubmed:33936292", "pubmed:34140989"], "generalized_empirical_formula": ["C8H11NO3.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30961"], "inchi_key_string": ["ZUFQODAHGAHPFQ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H11NO3.ClH/c1-5-8(12)7(4-11)6(3-10)2-9-5;/h2,10-12H,3-4H2,1H3;1H"], "mass": ["205.641"], "monoisotopic_mass": ["205.05057"], "smiles_string": ["Cc1ncc(CO)c(CO)c1O.Cl"]}, "synonyms": ["2-methyl-3-hydroxy-4,5-bis(hydroxymethyl)pyridine hydrochloride", "3-hydroxy-4,5-dimethylol-alpha-picoline hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "5-hydroxy-6-methyl-3,4-pyridinedimethanol hydrochloride", "pyridoxol hydrochloride", "vitamin B6 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "exact_current_rows": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[25]", "name": "Thiamine HCl", "primary": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "canonical_label": "thiamine hydrochloride", "label_equal": true, "definition": ["A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND605711145", "agr:IND606057536", "beilstein:3642937", "beilstein:3851771", "cas:67-03-8", "chemspider:5967", "drugbank:DBSALT000205", "foodb.food:FDB008416", "gmelin:31154", "gmelin:691133", "kegg.drug:D02094", "pubmed:11548854", "pubmed:12224421", "pubmed:21212548", "pubmed:22305197", "pubmed:24399744", "pubmed:25977858", "pubmed:26616989", "pubmed:27163892", "pubmed:28763984", "pubmed:28784494", "pubmed:30131156", "pubmed:31270735", "pubmed:31664290", "pubmed:32009117", "pubmed:32562525", "pubmed:32824791", "reaxys:17124533"], "generalized_empirical_formula": ["C12H17N4OS.Cl.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:49105"], "inchi_key_string": ["DPJRMOMPQZCRJU-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C12H17N4OS.2ClH/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H/q+1;;/p-1"], "mass": ["337.276"], "monoisotopic_mass": ["336.05784"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1.Cl.[Cl-]"]}, "synonyms": ["3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "thiamin dichloride", "thiamin hydrochloride", "thiamine HCl", "thiamine chloride hydrochloride", "thiamine dichloride", "thiamine(2+) dichloride", "thiaminium chloride hydrochloride", "vitamin B1 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "exact_current_rows": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[26]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015", "label": "riboflavin"}, "canonical_label": "riboflavin", "label_equal": true, "definition": ["&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:83-88-5", "chemspider:431981", "drugbank:DB00140", "drugcentral:2834", "foodb.food:FDB012160", "hmdb:HMDB0000244", "kegg.compound:C00255", "kegg.drug:D00050", "knapsack:C00001552", "lincs.smallmolecule:LSM-4084", "metacyc.compound:RIBOFLAVIN", "patent:US2807611", "patent:US2876169", "pdb-ccd:RBF", "pubmed:10566553", "pubmed:11399071", "pubmed:11606856", "pubmed:12083520", "pubmed:12354259", "pubmed:12927541", "pubmed:14963913", "pubmed:16273338", "pubmed:16460756", "pubmed:16658098", "pubmed:182198", "pubmed:18832377", "pubmed:19169240", "pubmed:19212411", "pubmed:19854891", "pubmed:22770225", "pubmed:2369885", "pubmed:23818044", "pubmed:24643482", "pubmed:24816110", "pubmed:25108762", "pubmed:25468971", "pubmed:25887755", "pubmed:2631092", "pubmed:29937405", "pubmed:3142982", "pubmed:33154451", "pubmed:33304888", "pubmed:33886098", "pubmed:33892358", "pubmed:34156642", "pubmed:3592624", "pubmed:3878498", "pubmed:4019261", "pubmed:6475825", "pubmed:6546833", "pubmed:6650303", "pubmed:7101408", "pubmed:7883462", "pubmed:8487103", "pubmed:8604671", "pubmed:8678471", "pubmed:8976642", "pubmed:9184778", "pubmed:9808225", "pubmed:9874201", "reaxys:97831", "wikipedia.en:Riboflavin"], "generalized_empirical_formula": ["C17H20N4O6"], "has_alternative_id": ["CHEBI:15044", "CHEBI:27299", "CHEBI:45214", "CHEBI:529204", "CHEBI:8843"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17015"], "inchi_key_string": ["AUNGANRZJHBGPY-SCRDCRAPSA-N"], "inchi_string": ["InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23)14(25)12(24)6-22)15-13(18-9)16(26)20-17(27)19-15/h3-4,11-12,14,22-25H,5-6H2,1-2H3,(H,20,26,27)/t11-,12+,14-/m0/s1"], "mass": ["376.369"], "monoisotopic_mass": ["376.13828"], "smiles_string": ["Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)CO)c2cc1C"]}, "synonyms": ["1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol", "5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "6,7-dimethyl-9-D-ribitylisoalloxazine", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine", "7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-ribitylisoalloxazine", "Aqua-Flave", "Beflavin", "Beflavine", "Bisulase", "Dermadram", "E101", "Fiboflavin", "Flavaxin", "Flavin Bb", "Flaxain", "Hyflavin", "Vitamin B2", "lactoflavin", "riboflavin (vit B2)", "riboflavin", "riboflavina", "riboflavine", "riboflavinum", "vitamin B2", "vitamin G", "vitasan B2"], "secondary": {"asserted": {"id": "CHEBI:17015", "label": "riboflavin"}, "exact_current_rows": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[27]", "name": "Nicotinic acid", "primary": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "canonical_label": "nicotinic acid", "label_equal": true, "definition": ["A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND607088605", "cas:59-67-6", "chemspider:913", "drugbank:DB00627", "drugcentral:2835", "foodb.food:FDB001014", "gmelin:3340", "hmdb:HMDB0001488", "kegg.compound:C00253", "kegg.drug:D00049", "knapsack:C00000208", "lincs.smallmolecule:LSM-4676", "metacyc.compound:NIACINE", "pdb-ccd:NIO", "pubmed:10540864", "pubmed:113218", "pubmed:12563315", "pubmed:12789870", "pubmed:135660", "pubmed:14550884", "pubmed:15037193", "pubmed:15183629", "pubmed:15205990", "pubmed:15311728", "pubmed:15627518", "pubmed:15651982", "pubmed:16018787", "pubmed:16172771", "pubmed:16322787", "pubmed:16400392", "pubmed:16449845", "pubmed:16767301", "pubmed:16877271", "pubmed:16945375", "pubmed:18037924", "pubmed:182198", "pubmed:186078", "pubmed:18993152", "pubmed:18996527", "pubmed:19369827", "pubmed:19592242", "pubmed:19678716", "pubmed:19779335", "pubmed:20979384", "pubmed:21632263", "pubmed:22116693", "pubmed:22155410", "pubmed:22229411", "pubmed:22366213", "pubmed:22458880", "pubmed:22770225", "pubmed:24029555", "pubmed:24568240", "pubmed:24675661", "pubmed:24848081", "pubmed:24975217", "pubmed:25040591", "pubmed:25241762", "pubmed:25429652", "pubmed:32954525", "pubmed:33273654", "pubmed:33932650", "pubmed:34066686", "pubmed:34085526", "pubmed:34117670", "pubmed:4033386", "pubmed:4259917", "pubmed:582105", "pubmed:699281", "pubmed:7217784", "pubmed:7581845", "pubmed:8306147", "pubmed:8423912", "pubmed:8679452", "pubmed:9107536", "reaxys:109591", "wikipedia.en:Niacin"], "generalized_empirical_formula": ["C6H5NO2"], "has_alternative_id": ["CHEBI:25538", "CHEBI:44319", "CHEBI:7559"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15940"], "inchi_key_string": ["PVNIIMVLHYAWGP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"], "mass": ["123.111"], "monoisotopic_mass": ["123.03203"], "smiles_string": ["O=C(O)c1cccnc1"]}, "synonyms": ["3-Pyridylcarboxylic acid", "3-carboxylpyridine", "3-carboxypyridine", "3-pyridinecarboxylic acid", "NICOTINIC ACID", "NICOTINIC ACID", "Niacin", "Niacor", "Niaspan", "Nicotinic acid", "Nicotinic acid", "Nicotinsaure", "Nikotinsaeure", "P.P. factor", "PP factor", "acide nicotinique", "acido nicotinico", "acidum nicotinicum", "anti-pellagra vitamin", "beta-pyridinecarboxylic acid", "m-pyridinecarboxylic acid", "nicotinic acid", "nicotinic acid", "pellagra preventive factor", "pyridine-3-carboxylic acid", "pyridine-3-carboxylic acid", "pyridine-beta-carboxylic acid", "pyridine-carboxylique-3", "vitamin B3"], "secondary": {"asserted": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "exact_current_rows": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[28]", "name": "Calcium D-(+)-pantothenate", "primary": {"id": "CHEBI:31345", "label": "Calcium pantothenate"}, "canonical_label": "Calcium pantothenate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:137-08-6", "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278", "pubmed:20553011", "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula": ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"], "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"], "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]}, "synonyms": ["Calcium pantotenate", "Calcium pantothenate", "Calcium pantothenate, d-", "Calpan", "D-ca pantothenate", "D-calcium pantothenate", "NSC-36292", "Pantholin", "Pantothenic acid (as calcium)", "Pantothenic acid calcium salt", "Vitamin b5, calcium salt", "pantotenato de calcio", "pantothenate de calcium"]}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[29]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843", "label": "vitamin B12"}, "canonical_label": "vitamin B12", "label_equal": true, "definition": ["Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives)."], "annotations": {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:176843"]}, "synonyms": ["vitamin B-12", "vitamin B12 vitamer", "vitamin B12 vitamers", "vitamin B12", "vitamins B12"], "secondary": {"asserted": {"id": "CHEBI:176843", "label": "vitamin B12"}, "exact_current_rows": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[30]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "canonical_label": "4-aminobenzoic acid", "label_equal": true, "definition": ["An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:150-13-0", "drugbank:DB02362", "drugcentral:2049", "ecmdb:ECMDB01392", "gmelin:50150", "hmdb:HMDB0001392", "kegg.compound:C00568", "kegg.drug:D02456", "knapsack:C00001401", "pdb-ccd:PAB", "pubmed:12039592", "pubmed:14745019", "pubmed:15115392", "pubmed:1527790", "pubmed:16290145", "pubmed:17149871", "pubmed:17743450", "pubmed:17800214", "pubmed:19469519", "pubmed:22767283", "pubmed:22994574", "pubmed:23063996", "pubmed:23084339", "pubmed:23144588", "pubmed:23471007", "pubmed:3599019", "pubmed:3820215", "pubmed:3950915", "pubmed:8411009", "pubmed:9406595", "reaxys:471605", "wikipedia.en:4-Aminobenzoic_acid", "ymdb:YMDB00493"], "generalized_empirical_formula": ["C7H7NO2"], "has_alternative_id": ["CHEBI:113372", "CHEBI:1783", "CHEBI:20315", "CHEBI:44778"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30753"], "inchi_key_string": ["ALYNCZNDIQEVRV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"], "mass": ["137.138"], "monoisotopic_mass": ["137.04768"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]}, "synonyms": ["1-Amino-4-carboxybenzene", "4-AMINOBENZOIC ACID", "4-AMINOBENZOIC ACID", "4-Amino-benzoic acid", "4-Aminobenzoesaeure", "4-Aminobenzoic acid", "4-Aminobenzoic acid", "4-Carboxyaniline", "4-Carboxyphenylamine", "4-aminobenzoic acid", "4-aminobenzoic acid", "ABEE", "PABA", "gamma-Aminobenzoic acid", "gamma-aminobenzoic acid", "p-Aminobenzoesaeure", "p-aminobenzoic acid", "p-carboxyaniline", "p-carboxyphenylamine", "para-aminobenzoic acid"], "secondary": {"asserted": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "exact_current_rows": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[31]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id": "CHEBI:16494", "label": "lipoic acid"}, "canonical_label": "lipoic acid", "label_equal": true, "definition": ["A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:122410", "cas:62-46-4", "drugbank:DB00166", "drugcentral:4732", "ecmdb:ECMDB01451", "gmelin:720915", "kegg.compound:C00725", "kegg.drug:D00086", "pubmed:15328413", "pubmed:7519986", "pubmed:7548757", "reaxys:81853", "wikipedia.en:Lipoic_acid", "ymdb:YMDB00334"], "generalized_empirical_formula": ["C8H14O2S2"], "has_alternative_id": ["CHEBI:146958", "CHEBI:25058", "CHEBI:6492"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16494"], "inchi_key_string": ["AGBQKNBQESQNJD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H14O2S2/c9-8(10)4-2-1-3-7-5-6-11-12-7/h7H,1-6H2,(H,9,10)"], "mass": ["206.332"], "monoisotopic_mass": ["206.04352"], "smiles_string": ["O=C(O)CCCCC1CCSS1"]}, "synonyms": ["1,2-dithiolane-3-pentanoic acid", "1,2-dithiolane-3-valeric acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)valeric acid", "5-(dithiolan-3-yl)valeric acid", "5-[3-(1,2-dithiolanyl)]pentanoic acid", "6,8-thioctic acid", "6,8-thiotic acid", "6-thioctic acid", "6-thiotic acid", "Acetate-replacing factor", "Biletan", "Lipoic acid", "Thioctansaeure", "Thioctic acid", "Thioctsaeure", "Thioktsaeure", "alpha-Lipoic acid", "alpha-Liponsaeure", "alpha-lipoic acid", "liponic acid"], "secondary": {"asserted": {"id": "CHEBI:16494", "label": "lipoic acid"}, "exact_current_rows": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[32]", "name": "Syringic  acid"}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[33]", "name": "NaOH", "primary": {"id": "CHEBI:32145", "label": "sodium hydroxide"}, "canonical_label": "sodium hydroxide", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:1310-73-2", "gmelin:68430", "kegg.compound:C12569", "kegg.drug:D01169"], "generalized_empirical_formula": ["HO.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32145"], "inchi_key_string": ["HEMHJVSKTPXQMS-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/Na.H2O/h;1H2/q+1;/p-1"], "mass": ["39.997"], "monoisotopic_mass": ["39.99251"], "smiles_string": ["[Na+].[OH-]"]}, "synonyms": ["Aetznatron", "NaOH", "Natriumhydroxid", "Sodium hydroxide", "caustic soda", "hydroxyde de sodium", "soda lye", "sodium hydrate", "sodium hydroxide", "sodium hydroxide", "soude caustique"], "secondary": {"asserted": {"id": "CHEBI:32145", "label": "sodium hydroxide"}, "exact_current_rows": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[0]", "name": "NH4Cl", "primary": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "canonical_label": "ammonium chloride", "label_equal": true, "definition": ["An inorganic chloride having ammonium as the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:12125-02-9", "gmelin:10120", "kegg.compound:C12538", "kegg.drug:D01139", "wikipedia.en:Ammonium_Chloride"], "generalized_empirical_formula": ["Cl.H4N"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31206"], "inchi_key_string": ["NLXLAEXVIDQMFP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/ClH.H3N/h1H;1H3"], "mass": ["53.492"], "monoisotopic_mass": ["53.00323"], "smiles_string": ["[Cl-].[H][N+]([H])([H])[H]"]}, "synonyms": ["Ammonium chloride", "Ammoniumchlorid", "NH4Cl", "[NH4]Cl", "ammonium chloride", "ammonium chloride", "azanium chloride"], "secondary": {"asserted": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "exact_current_rows": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[1]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "canonical_label": "potassium dihydrogen phosphate", "label_equal": true, "definition": ["A potassium salt in which dihydrogen phosphate(1−) is the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"], "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"], "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]}, "synonyms": ["MKP", "Monopotassium dihydrogen phosphate", "Monopotassium monophosphate", "Monopotassium orthophosphate", "Monopotassium phosphate", "Orthophosphoric acid, monopotassium salt", "Phosphoric acid, monopotassium salt", "Phosphoric acid, potassium salt (1:1)", "Potassium acid phosphate", "Potassium dihydrogen orthophosphate", "Potassium dihydrogen phosphate", "Potassium phosphate monobasic", "Potassium phosphate", "Sorensen's potassium phosphate", "potassium dihydrogen phosphate", "potassium dihydrogen phosphate"], "secondary": {"asserted": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "exact_current_rows": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[2]", "name": "K2HPO4", "primary": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "canonical_label": "dipotassium hydrogen phosphate", "label_equal": true, "definition": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-11-4", "kegg.compound:C13197", "kegg.drug:D02403", "metacyc.compound:CPD0-2433", "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"], "generalized_empirical_formula": ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131527"], "inchi_key_string": ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}, "synonyms": ["Dibasic potassium phosphate", "Dipotassium hydrogenorthophosphate", "Dipotassium monohydrogen phosphate", "Dipotassium monophosphate", "Dipotassium orthophosphate", "Dipotassium phosphate", "Hydrogen dipotassium phosphate", "K2HPO4", "Phosphoric acid, dipotassium salt", "Potassium dibasic phosphate", "Potassium monohydrogen phosphate", "Potassium monophosphate", "Potassium phosphate (dibasic)", "Potassium phosphate, dibasic", "dipotassium hydrogen phosphate", "dipotassium hydrogen phosphate", "dipotassium hydrogenphosphate", "potassium dibasic phosphate trihydrate"], "secondary": {"asserted": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "exact_current_rows": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[3]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "canonical_label": "magnesium sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505", "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222", "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"], "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}, "synonyms": ["Magnesium sulfate heptahydrate", "MgSO4.7H2O", "bitter salt", "epsom salt", "epsomite", "magnesium sulfate (1:1) heptahydrate", "magnesium sulfate heptahydrate", "magnesium sulfate--water (1/7)", "magnesium sulfate--water (1/7)", "magnesium sulphate heptahydrate", "sulfuric acid magnesium salt heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "exact_current_rows": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[4]", "name": "Yeast extract"}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[5]", "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806", "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3", "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"], "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]}, "synonyms": ["Resazurin"]}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[6]", "name": "Na2CO3", "primary": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "canonical_label": "sodium carbonate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:497-19-8", "ppdb:594"], "generalized_empirical_formula": ["CO3.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:29377"], "inchi_key_string": ["CDBYLPFSWZWCQE-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/CH2O3.2Na/c2-1(3)4;;/h(H2,2,3,4);;/q;2*+1/p-2"], "mass": ["105.988"], "monoisotopic_mass": ["105.96428"], "smiles_string": ["O=C([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2CO3", "Natriumkarbonat", "disodium carbonate", "disodium trioxidocarbonate", "disodium trioxidocarbonate", "sodium carbonate", "sodium carbonate"], "secondary": {"asserted": {"id": "CHEBI:29377", "label": "sodium carbonate"}, "exact_current_rows": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[7]", "name": "L-Cysteine HCl x H2O", "primary": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "canonical_label": "L-cysteine hydrochloride hydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of &lt;small&gt;L&lt;/small&gt;-cysteine hydrochloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7048-04-6", "drugbank:DB00151", "kegg.drug:D02326", "reaxys:5158059", "wikipedia.en:Cysteine"], "generalized_empirical_formula": ["C3H7NO2S.H2O.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91248"], "inchi_key_string": ["QIJRTFXNRTXDIP-JIZZDEOASA-N"], "inchi_string": ["InChI=1S/C3H7NO2S.ClH.H2O/c4-2(1-7)3(5)6;;/h2,7H,1,4H2,(H,5,6);1H;1H2/t2-;;/m0../s1"], "mass": ["175.637"], "monoisotopic_mass": ["175.00699"], "smiles_string": ["Cl.N[C@@H](CS)C(=O)O.O"]}, "synonyms": ["(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)", "(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride monohydrate", "Cysteine hydrochloride", "L-Cysteine monohydrate monochloride", "L-cysteine hydrochloride monohydrate", "L-cysteine hydrochloride--water (1/1)", "L-cysteine hydrochloride--water (1/1)"], "secondary": {"asserted": {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}, "exact_current_rows": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[8]", "name": "Nitrilotriacetic acid", "primary": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "canonical_label": "nitrilotriacetic acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1710776", "cas:139-13-9", "drugbank:DB03040", "gmelin:3726", "kegg.compound:C14695", "pdb-ccd:NTA"], "generalized_empirical_formula": ["C6H9NO6"], "has_alternative_id": ["CHEBI:34889", "CHEBI:44555"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:44557"], "inchi_key_string": ["MGFYIUFZLHCRTH-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"], "mass": ["191.139"], "monoisotopic_mass": ["191.04299"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]}, "synonyms": ["Complexon I", "H3nta", "Komplexon I", "N(CH2-COOH)3", "N,N-bis(carboxymethyl)glycine", "N,N-bis(carboxymethyl)glycine", "NITRILOTRIACETIC ACID", "NTA", "Nitrilotriacetate", "Nitrilotriacetic acid", "Nitrilotriessigsaeure", "Triglycollamic acid", "Trilon A", "alpha,alpha',alpha''-trimethylaminetricarboxylic acid", "nitrilo-2,2',2''-triacetic acid", "tri(carboxymethyl)amine", "triglycine"], "secondary": {"asserted": {"id": "CHEBI:44557", "label": "nitrilotriacetic acid"}, "exact_current_rows": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[9]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "canonical_label": "manganese(II) sulfate monohydrate", "label_equal": true, "definition": ["A hydrate that is the monohydrate form of manganese(II) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10034-96-5", "kegg.drug:D04854", "pubmed:26097037", "reaxys:13153017", "wikipedia.en:Manganese(II)_sulfate"], "generalized_empirical_formula": ["H2O.Mn.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86364"], "inchi_key_string": ["ISPYRSDWRDQNSW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mn.H2O4S.H2O/c;1-5(2,3)4;/h;(H2,1,2,3,4);1H2/q+2;;/p-2"], "mass": ["169.016"], "monoisotopic_mass": ["168.90034"], "smiles_string": ["O.O=S(=O)([O-])[O-].[Mn+2]"]}, "synonyms": ["Manganese sulfate hydrate", "Manganese sulfate monohydrate", "Manganese sulfate", "Manganous sulfate monohydrate", "MnSO4.H2O", "manganese(2+) sulfate monohydrate", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulfate--water (1/1)", "manganese(2+) sulphate monohydrate", "manganese(II) sulphate monohydrate"], "secondary": {"asserted": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "exact_current_rows": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[10]", "name": "NaCl", "primary": {"id": "CHEBI:26710", "label": "sodium chloride"}, "canonical_label": "sodium chloride", "label_equal": true, "definition": ["An inorganic chloride salt having sodium(1+) as the counterion."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula": ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string": ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]}, "synonyms": ["Kochsalz", "NaCl", "Natriumchlorid", "chlorure de sodium", "cloruro sodico", "common salt", "halite", "natrii chloridum", "rock salt", "salt", "sodium chloride", "sodium chloride", "table salt"], "secondary": {"asserted": {"id": "CHEBI:26710", "label": "sodium chloride"}, "exact_current_rows": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[11]", "name": "FeSO4 x 7 H2O", "primary": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "canonical_label": "iron(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used)."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]}, "synonyms": ["FeSO4.7H2O", "Fero-Gradumet", "Tetucur-S", "copperas", "ferrous sulfate heptahydrate", "ferrous sulfate.7H2O", "green vitriol", "iron vitriol", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate--water (1/7)", "iron(2+) sulfate.7H2O", "iron(II) sulfate.7H2O", "melanterite mineral", "melanterite"], "secondary": {"asserted": {"id": "CHEBI:75836", "label": "iron(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[12]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "canonical_label": "cobalt(2+) sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of cobalt(2+) sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10026-24-1", "pubmed:10504146", "pubmed:12187935", "pubmed:12209163", "pubmed:12579202", "pubmed:12948248", "pubmed:2227161", "pubmed:24359163", "pubmed:25896363", "wikipedia.en:Cobalt(II)_sulfate"], "generalized_empirical_formula": ["Co.7H2O.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91244"], "inchi_key_string": ["MEYVLGVRTYSQHI-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Co.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["281.101"], "monoisotopic_mass": ["280.95888"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Co+2]"]}, "synonyms": ["Cobalt monosulfate heptahydrate", "cobalt sulfate heptahydrate", "cobalt(2+) sulfate--water (1/7)", "cobalt(2+) sulfate--water (1/7)", "cobalt(II) sulfate heptahydrate", "cobaltous sulfate heptahydrate"], "secondary": {"asserted": {"id": "CHEBI:91244", "label": "cobalt(2+) sulfate heptahydrate"}, "exact_current_rows": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[13]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "canonical_label": "calcium chloride dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of calcium chloride."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8", "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"], "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass": ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}, "synonyms": ["CaCl2.2H2O", "Calcium chloride hydrate", "Calcium chloride", "calcium chloride--water (1/2)", "calcium chloride--water (1/2)", "calcium dichloride dihydrate"], "secondary": {"asserted": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "exact_current_rows": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[14]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "canonical_label": "zinc sulfate heptahydrate", "label_equal": true, "definition": ["A hydrate that is the heptahydrate form of zinc sulfate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7446-20-0", "gmelin:47216", "kegg.drug:D01081", "wikipedia.en:Zinc_Sulfate"], "generalized_empirical_formula": ["7H2O.O4S.Zn"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32312"], "inchi_key_string": ["RZLVQBNCHSJZPX-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/H2O4S.7H2O.Zn/c1-5(2,3)4;;;;;;;;/h(H2,1,2,3,4);7*1H2;/q;;;;;;;;+2/p-2"], "mass": ["287.558"], "monoisotopic_mass": ["285.95482"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Zn+2]"]}, "synonyms": ["Zinc sulfate", "ZnSO4.7H2O", "zinc sulfate (1:1) heptahydrate", "zinc sulfate heptahydrate (1:1:7)", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate heptahydrate", "zinc(2+) sulfate--water (1/7)", "zinc(2+) sulfate--water (1/7)"], "secondary": {"asserted": {"id": "CHEBI:32312", "label": "zinc sulfate heptahydrate"}, "exact_current_rows": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[15]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "canonical_label": "copper(II) sulfate pentahydrate", "label_equal": true, "definition": ["The pentahydrate of copper(2+) sulfate. A bright blue crystalline solid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7758-99-8", "kegg.drug:D03613", "pubmed:11407502", "pubmed:12209195", "pubmed:12484481", "pubmed:15040745", "pubmed:15607472", "pubmed:15824790", "pubmed:19346702", "pubmed:2002460", "pubmed:20132934", "pubmed:2913309", "pubmed:3351847", "pubmed:7615984", "pubmed:8878264", "pubmed:9521458", "pubmed:9776063", "reaxys:16499970", "wikipedia.en:Copper(II)_sulfate"], "generalized_empirical_formula": ["Cu.5H2O.O4S"], "has_alternative_id": ["CHEBI:121741", "CHEBI:370227"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31440"], "inchi_key_string": ["JZCCFEFSEZPSOG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Cu.H2O4S.5H2O/c;1-5(2,3)4;;;;;/h;(H2,1,2,3,4);5*1H2/q+2;;;;;;/p-2"], "mass": ["249.684"], "monoisotopic_mass": ["248.93415"], "smiles_string": ["O=S(=O)([O-])[O-].[Cu+2].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H]"]}, "synonyms": ["CuSO4.5H2O", "Cupric sulfate", "copper sulphate(5.H2O)", "copper(2+) sulfate (1:1) pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate pentahydrate", "copper(2+) sulfate--water (1/5)", "copper(2+) sulfate--water (1/5)", "copper(II) sulfate, pentahydrate", "cupric sulfate pentahydrate"], "secondary": {"asserted": {"id": "CHEBI:31440", "label": "copper(II) sulfate pentahydrate"}, "exact_current_rows": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[16]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "canonical_label": "potassium aluminium sulfate dodecahydrate", "label_equal": true, "definition": ["A hydrate resulting from the the formal combination of anhydrous potassium aluminium sulfate with 12 mol eq. of water."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7784-24-9", "reaxys:14851666", "wikipedia.en:Potassium_alum"], "generalized_empirical_formula": ["Al.12H2O.K.2O4S"], "has_alternative_id": ["CHEBI:31192"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86465"], "inchi_key_string": ["GNHOJBNSNUXZQA-UHFFFAOYSA-J"], "inchi_string": ["InChI=1S/Al.K.2H2O4S.12H2O/c;;2*1-5(2,3)4;;;;;;;;;;;;/h;;2*(H2,1,2,3,4);12*1H2/q+3;+1;;;;;;;;;;;;;;/p-4"], "mass": ["474.386"], "monoisotopic_mass": ["473.97548"], "smiles_string": ["O.O.O.O.O.O.O.O.O.O.O.O.O=S(=O)([O-])[O-].O=S(=O)([O-])[O-].[Al+3].[K+]"]}, "synonyms": ["AlK(SO4)2.12H2O", "Aluminum potassium disulfate dodecahydrate", "Aluminum potassium sulfate dodecahydrate", "Kalinite", "Potash alum dodecahydrate", "Potassium alum dodecahydrate", "Potassium aluminum disulfate dodecahydrate", "aluminium potassium sulfate--water (1/12)", "aluminium potassium sulfate--water (1/12)"], "secondary": {"asserted": {"id": "CHEBI:86465", "label": "potassium aluminium sulfate dodecahydrate"}, "exact_current_rows": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[17]", "name": "H3BO3", "primary": {"id": "CHEBI:33118", "label": "boric acid"}, "canonical_label": "boric acid", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["bpdb:2136", "cas:10043-35-3", "cas:11113-50-1", "drugcentral:3035", "gmelin:1585", "kegg.compound:C12486", "kegg.drug:D01089", "molbase:1644", "pdb-ccd:BO3", "ppdb:2136"], "generalized_empirical_formula": ["H3BO3"], "has_alternative_id": ["CHEBI:22911", "CHEBI:31299", "CHEBI:41248"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:33118"], "inchi_key_string": ["KGBXLFKZBHKPEV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"], "mass": ["61.833"], "monoisotopic_mass": ["62.01752"], "smiles_string": ["[H]OB(O[H])O[H]"]}, "synonyms": ["B(OH)3", "BORIC ACID", "Boric acid", "H3BO3", "[B(OH)3]", "boric acid", "boron trihydroxide", "orthoboric acid", "trihydroxidoboron", "trihydroxidoboron"], "secondary": {"asserted": {"id": "CHEBI:33118", "label": "boric acid"}, "exact_current_rows": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[18]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "canonical_label": "sodium molybdate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium molybdate."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10102-40-6", "pubmed:20645132", "pubmed:20813395", "pubmed:22663766", "pubmed:3382795", "reaxys:19032996", "wikipedia.en:Sodium_molybdate"], "generalized_empirical_formula": ["2H2O.MoO4.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75213"], "inchi_key_string": ["FDEIWTXVNPKYDL-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/Mo.2Na.2H2O.4O/h;;;2*1H2;;;;/q;2*+1;;;;;2*-1"], "mass": ["241.946"], "monoisotopic_mass": ["243.88573"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]}, "synonyms": ["Disodium molybdate dihydrate", "Molybdic acid, disodium salt, dihydrate", "Na2MoO4.2H2O", "Sodium molybdate(VI) dihydrate", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium dioxido(dioxo)molybdenum--water (1/2)", "sodium orthomolybdate dihydrate"], "secondary": {"asserted": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"}, "exact_current_rows": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[19]", "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "canonical_label": "nickel dichloride", "label_equal": true, "definition": ["A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:7718-54-9", "kegg.compound:C14711", "pubmed:11739495", "pubmed:12603851", "pubmed:21928331", "pubmed:23179351", "pubmed:23622879", "pubmed:23702803", "pubmed:23735035", "pubmed:7671317", "reaxys:3902827", "reaxys:8128171", "wikipedia.en:Nickel_dichloride"], "generalized_empirical_formula": ["Cl2Ni"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:34887"], "inchi_key_string": ["QMMRZOWCJAIUJA-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"], "mass": ["129.599"], "monoisotopic_mass": ["127.87305"], "smiles_string": ["[Cl][Ni][Cl]"]}, "synonyms": ["NiCl2", "Nickel chloride", "Nickel(II) chloride", "[NiCl2]", "nickel dichloride", "nickel dichloride", "nickel(2+) chloride", "nickel(2+) chloride", "nickel(II) chloride", "nickel(II) chloride", "nickelous chloride"], "secondary": {"asserted": {"id": "CHEBI:34887", "label": "nickel dichloride"}, "exact_current_rows": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[20]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "canonical_label": "disodium selenite pentahydrate", "label_equal": true, "definition": ["A hydrate that is the pentahydrate form of disodium selenite."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:26970-82-1", "pubmed:15259772", "pubmed:15559373", "pubmed:16126997", "pubmed:17873396", "pubmed:24479345", "pubmed:24716537", "reaxys:14666014", "wikipedia.en:Sodium_selenite"], "generalized_empirical_formula": ["5H2O.2Na.O3Se"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131361"], "inchi_key_string": ["TUANAMBRHOLYTH-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"], "mass": ["263.012"], "monoisotopic_mass": ["263.93363"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]}, "synonyms": ["Na2SeO3.5H2O", "Selenious acid disodium salt, pentahydrate", "Sodium selenite pentahydrate", "disodium selenite hydrate", "sodium selenite hydrate", "sodium selenite--water (1/5)", "sodium selenite--water (1/5)"], "secondary": {"asserted": {"id": "CHEBI:131361", "label": "disodium selenite pentahydrate"}, "exact_current_rows": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[21]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "canonical_label": "sodium tungstate dihydrate", "label_equal": true, "definition": ["A hydrate that is the dihydrate form of sodium tungstate. Combines with hydrogen peroxide for the oxidation of secondary amines to nitrones"], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:10213-10-2", "reaxys:13157884", "wikipedia.en:Sodium_tungstate"], "generalized_empirical_formula": ["2H2O.2Na.O4W"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63939"], "inchi_key_string": ["WPZFLQRLSGVIAA-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.2H2O.4O.W/h;;2*1H2;;;;;/q2*+1;;;;;2*-1;"], "mass": ["329.846"], "monoisotopic_mass": ["329.93126"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]}, "synonyms": ["Na2WO4.2H2O", "Tungstic acid, sodium salt, dihydrate", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium dioxido(dioxo)tungsten--water (1/2)", "sodium orthotungstate dihydrate", "sodium tungstate(VI) dihydrate"], "secondary": {"asserted": {"id": "CHEBI:63939", "label": "sodium tungstate dihydrate"}, "exact_current_rows": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[22]", "name": "Biotin", "primary": {"id": "CHEBI:15956", "label": "biotin"}, "canonical_label": "biotin", "label_equal": true, "definition": ["An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:58-85-5", "chemspider:149962", "drugbank:DB00121", "drugcentral:373", "foodb.food:FDB014510", "gmelin:1918703", "hmdb:HMDB0000030", "kegg.compound:C00120", "kegg.drug:D00029", "knapsack:C00000756", "lincs.smallmolecule:LSM-3994", "metacyc.compound:BIOTIN", "pdb-ccd:BTN", "pmc:PMC8089577", "pubmed:10064317", "pubmed:10215065", "pubmed:10577274", "pubmed:11435506", "pubmed:11481419", "pubmed:11800048", "pubmed:12055344", "pubmed:12070309", "pubmed:12603856", "pubmed:12803839", "pubmed:15012185", "pubmed:15202718", "pubmed:15272000", "pubmed:15690449", "pubmed:15863846", "pubmed:15899401", "pubmed:15992684", "pubmed:16011464", "pubmed:16195795", "pubmed:16419467", "pubmed:16676358", "pubmed:16677798", "pubmed:16704206", "pubmed:16769720", "pubmed:17297119", "pubmed:1814646", "pubmed:18202531", "pubmed:18452485", "pubmed:18509457", "pubmed:19212411", "pubmed:19319844", "pubmed:19727438", "pubmed:19928962", "pubmed:20967359", "pubmed:20974274", "pubmed:2100006", "pubmed:21248194", "pubmed:21356565", "pubmed:21373679", "pubmed:21596550", "pubmed:21871906", "pubmed:25515858", "pubmed:33346513", "pubmed:33461365", "pubmed:34077272", "pubmed:8333586", "pubmed:8750932", "pubmed:9022537", "pubmed:9038855", "pubmed:9094878", "pubmed:9164991", "pubmed:9176832", "pubmed:9371938", "pubmed:9416479", "reaxys:86838", "wikipedia.en:Biotin"], "generalized_empirical_formula": ["C10H16N2O3S"], "has_alternative_id": ["CHEBI:13905", "CHEBI:22882", "CHEBI:22884", "CHEBI:3108", "CHEBI:41236"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15956"], "inchi_key_string": ["YBJHBAHKTGYVGT-ZKWXMUAHSA-N"], "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"], "mass": ["244.316"], "monoisotopic_mass": ["244.08816"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]}, "synonyms": ["(+)-cis-Hexahydro-2-oxo-1H-thieno[3,4]imidazole-4-valeric acid", "(3aS,4S,6aR)-Hexahydro-2-oxo-1H-thieno[3,4-d]imidazole-4-valeric acid", "5-(2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl)pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid", "BIOTIN", "Coenzyme R", "D-(+)-biotin", "D-Biotin", "Vitamin H", "biotin", "biotina", "biotine", "biotinum", "cis-(+)-Tetrahydro-2-oxothieno[3,4]imidazoline-4-valeric acid", "cis-Hexahydro-2-oxo-1H-thieno(3,4)imidazole-4-valeric acid", "cis-Tetrahydro-2-oxothieno(3,4-d)imidazoline-4-valeric acid", "vitamin B7"], "secondary": {"asserted": {"id": "CHEBI:15956", "label": "biotin"}, "exact_current_rows": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[23]", "name": "Folic acid", "primary": {"id": "CHEBI:27470", "label": "folic acid"}, "canonical_label": "folic acid", "label_equal": true, "definition": ["An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND606960789", "cas:59-30-3", "chemspider:5815", "drugbank:DB00158", "drugcentral:1231", "foodb.food:FDB014504", "hmdb:HMDB0000121", "kegg.compound:C00504", "kegg.drug:D00070", "knapsack:C00001539", "lincs.smallmolecule:LSM-5355", "metacyc.compound:CPD-12826", "pdb-ccd:FOL", "pubmed:10138938", "pubmed:10897644", "pubmed:10958818", "pubmed:11261364", "pubmed:11451208", "pubmed:11959400", "pubmed:14387833", "pubmed:15321809", "pubmed:15523939", "pubmed:15754725", "pubmed:15797531", "pubmed:15797685", "pubmed:15831910", "pubmed:15990733", "pubmed:16093404", "pubmed:16277678", "pubmed:16380297", "pubmed:16871332", "pubmed:17784727", "pubmed:18788725", "pubmed:19121630", "pubmed:19335717", "pubmed:19355913", "pubmed:24650098", "pubmed:33624660", "pubmed:33965562", "pubmed:33968971", "pubmed:34207319", "pubmed:34219855", "pubmed:7738698", "pubmed:8235383", "pubmed:9040515", "pubmed:9420019", "pubmed:9565830", "pubmed:9683174", "pubmed:9781393", "pubmed:9808640", "pubmed:9808641", "reaxys:100781", "wikipedia.en:Folic_Acid"], "generalized_empirical_formula": ["C19H19N7O6"], "has_alternative_id": ["CHEBI:24075", "CHEBI:42610", "CHEBI:5140", "CHEBI:569217"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:27470"], "inchi_key_string": ["OVBPIULPVIDEAO-LBPRGKRZSA-N"], "inchi_string": ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"], "mass": ["441.404"], "monoisotopic_mass": ["441.13968"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]}, "synonyms": ["(2S)-2-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzamido)pentanedioic acid", "Acfol", "Folate", "Folicet", "Folsaeure", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid", "N-[(4-{[(2-amino-4-oxo-1,4-dihydropteridin-6-yl)methyl]amino}phenyl)carbonyl]-L-glutamic acid", "N-pteroyl-L-glutamic acid", "PGA", "PteGlu", "acide folique", "acido folico", "acidum folicum", "folic acid", "pteroyl-L-glutamic acid", "pteroyl-L-monoglutamic acid", "pteroylglutamic acid", "pteroylmonoglutamic acid", "vitamin B11", "vitamin B9", "vitamin Bc", "vitamin Be", "vitamin M"], "secondary": {"asserted": {"id": "CHEBI:27470", "label": "folic acid"}, "exact_current_rows": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[24]", "name": "Pyridoxine hydrochloride", "primary": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "canonical_label": "pyridoxine hydrochloride", "label_equal": true, "definition": ["The hydrochloride salt of pyridoxine."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND500675659", "beilstein:3632435", "cas:58-56-0", "drugbank:DBSALT000151", "foodb.food:FDB000575", "gmelin:1067921", "kegg.drug:D02179", "pubmed:15098856", "pubmed:17416572", "pubmed:17891511", "pubmed:18243627", "pubmed:19481898", "pubmed:20645279", "pubmed:21781646", "pubmed:24421551", "pubmed:27468034", "pubmed:28095734", "pubmed:32460509", "pubmed:33209152", "pubmed:33936292", "pubmed:34140989"], "generalized_empirical_formula": ["C8H11NO3.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30961"], "inchi_key_string": ["ZUFQODAHGAHPFQ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H11NO3.ClH/c1-5-8(12)7(4-11)6(3-10)2-9-5;/h2,10-12H,3-4H2,1H3;1H"], "mass": ["205.641"], "monoisotopic_mass": ["205.05057"], "smiles_string": ["Cc1ncc(CO)c(CO)c1O.Cl"]}, "synonyms": ["2-methyl-3-hydroxy-4,5-bis(hydroxymethyl)pyridine hydrochloride", "3-hydroxy-4,5-dimethylol-alpha-picoline hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "4,5-bis(hydroxymethyl)-2-methylpyridin-3-ol hydrochloride", "5-hydroxy-6-methyl-3,4-pyridinedimethanol hydrochloride", "pyridoxol hydrochloride", "vitamin B6 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:30961", "label": "pyridoxine hydrochloride"}, "exact_current_rows": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[25]", "name": "Thiamine HCl", "primary": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "canonical_label": "thiamine hydrochloride", "label_equal": true, "definition": ["A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND605711145", "agr:IND606057536", "beilstein:3642937", "beilstein:3851771", "cas:67-03-8", "chemspider:5967", "drugbank:DBSALT000205", "foodb.food:FDB008416", "gmelin:31154", "gmelin:691133", "kegg.drug:D02094", "pubmed:11548854", "pubmed:12224421", "pubmed:21212548", "pubmed:22305197", "pubmed:24399744", "pubmed:25977858", "pubmed:26616989", "pubmed:27163892", "pubmed:28763984", "pubmed:28784494", "pubmed:30131156", "pubmed:31270735", "pubmed:31664290", "pubmed:32009117", "pubmed:32562525", "pubmed:32824791", "reaxys:17124533"], "generalized_empirical_formula": ["C12H17N4OS.Cl.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:49105"], "inchi_key_string": ["DPJRMOMPQZCRJU-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C12H17N4OS.2ClH/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H/q+1;;/p-1"], "mass": ["337.276"], "monoisotopic_mass": ["336.05784"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1.Cl.[Cl-]"]}, "synonyms": ["3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride", "thiamin dichloride", "thiamin hydrochloride", "thiamine HCl", "thiamine chloride hydrochloride", "thiamine dichloride", "thiamine(2+) dichloride", "thiaminium chloride hydrochloride", "vitamin B1 hydrochloride"], "secondary": {"asserted": {"id": "CHEBI:49105", "label": "thiamine hydrochloride"}, "exact_current_rows": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[26]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015", "label": "riboflavin"}, "canonical_label": "riboflavin", "label_equal": true, "definition": ["&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:83-88-5", "chemspider:431981", "drugbank:DB00140", "drugcentral:2834", "foodb.food:FDB012160", "hmdb:HMDB0000244", "kegg.compound:C00255", "kegg.drug:D00050", "knapsack:C00001552", "lincs.smallmolecule:LSM-4084", "metacyc.compound:RIBOFLAVIN", "patent:US2807611", "patent:US2876169", "pdb-ccd:RBF", "pubmed:10566553", "pubmed:11399071", "pubmed:11606856", "pubmed:12083520", "pubmed:12354259", "pubmed:12927541", "pubmed:14963913", "pubmed:16273338", "pubmed:16460756", "pubmed:16658098", "pubmed:182198", "pubmed:18832377", "pubmed:19169240", "pubmed:19212411", "pubmed:19854891", "pubmed:22770225", "pubmed:2369885", "pubmed:23818044", "pubmed:24643482", "pubmed:24816110", "pubmed:25108762", "pubmed:25468971", "pubmed:25887755", "pubmed:2631092", "pubmed:29937405", "pubmed:3142982", "pubmed:33154451", "pubmed:33304888", "pubmed:33886098", "pubmed:33892358", "pubmed:34156642", "pubmed:3592624", "pubmed:3878498", "pubmed:4019261", "pubmed:6475825", "pubmed:6546833", "pubmed:6650303", "pubmed:7101408", "pubmed:7883462", "pubmed:8487103", "pubmed:8604671", "pubmed:8678471", "pubmed:8976642", "pubmed:9184778", "pubmed:9808225", "pubmed:9874201", "reaxys:97831", "wikipedia.en:Riboflavin"], "generalized_empirical_formula": ["C17H20N4O6"], "has_alternative_id": ["CHEBI:15044", "CHEBI:27299", "CHEBI:45214", "CHEBI:529204", "CHEBI:8843"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17015"], "inchi_key_string": ["AUNGANRZJHBGPY-SCRDCRAPSA-N"], "inchi_string": ["InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23)14(25)12(24)6-22)15-13(18-9)16(26)20-17(27)19-15/h3-4,11-12,14,22-25H,5-6H2,1-2H3,(H,20,26,27)/t11-,12+,14-/m0/s1"], "mass": ["376.369"], "monoisotopic_mass": ["376.13828"], "smiles_string": ["Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)CO)c2cc1C"]}, "synonyms": ["1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol", "5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol", "6,7-dimethyl-9-D-ribitylisoalloxazine", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine", "7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione", "7,8-dimethyl-10-ribitylisoalloxazine", "Aqua-Flave", "Beflavin", "Beflavine", "Bisulase", "Dermadram", "E101", "Fiboflavin", "Flavaxin", "Flavin Bb", "Flaxain", "Hyflavin", "Vitamin B2", "lactoflavin", "riboflavin (vit B2)", "riboflavin", "riboflavina", "riboflavine", "riboflavinum", "vitamin B2", "vitamin G", "vitasan B2"], "secondary": {"asserted": {"id": "CHEBI:17015", "label": "riboflavin"}, "exact_current_rows": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[27]", "name": "Nicotinic acid", "primary": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "canonical_label": "nicotinic acid", "label_equal": true, "definition": ["A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["agr:IND607088605", "cas:59-67-6", "chemspider:913", "drugbank:DB00627", "drugcentral:2835", "foodb.food:FDB001014", "gmelin:3340", "hmdb:HMDB0001488", "kegg.compound:C00253", "kegg.drug:D00049", "knapsack:C00000208", "lincs.smallmolecule:LSM-4676", "metacyc.compound:NIACINE", "pdb-ccd:NIO", "pubmed:10540864", "pubmed:113218", "pubmed:12563315", "pubmed:12789870", "pubmed:135660", "pubmed:14550884", "pubmed:15037193", "pubmed:15183629", "pubmed:15205990", "pubmed:15311728", "pubmed:15627518", "pubmed:15651982", "pubmed:16018787", "pubmed:16172771", "pubmed:16322787", "pubmed:16400392", "pubmed:16449845", "pubmed:16767301", "pubmed:16877271", "pubmed:16945375", "pubmed:18037924", "pubmed:182198", "pubmed:186078", "pubmed:18993152", "pubmed:18996527", "pubmed:19369827", "pubmed:19592242", "pubmed:19678716", "pubmed:19779335", "pubmed:20979384", "pubmed:21632263", "pubmed:22116693", "pubmed:22155410", "pubmed:22229411", "pubmed:22366213", "pubmed:22458880", "pubmed:22770225", "pubmed:24029555", "pubmed:24568240", "pubmed:24675661", "pubmed:24848081", "pubmed:24975217", "pubmed:25040591", "pubmed:25241762", "pubmed:25429652", "pubmed:32954525", "pubmed:33273654", "pubmed:33932650", "pubmed:34066686", "pubmed:34085526", "pubmed:34117670", "pubmed:4033386", "pubmed:4259917", "pubmed:582105", "pubmed:699281", "pubmed:7217784", "pubmed:7581845", "pubmed:8306147", "pubmed:8423912", "pubmed:8679452", "pubmed:9107536", "reaxys:109591", "wikipedia.en:Niacin"], "generalized_empirical_formula": ["C6H5NO2"], "has_alternative_id": ["CHEBI:25538", "CHEBI:44319", "CHEBI:7559"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15940"], "inchi_key_string": ["PVNIIMVLHYAWGP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"], "mass": ["123.111"], "monoisotopic_mass": ["123.03203"], "smiles_string": ["O=C(O)c1cccnc1"]}, "synonyms": ["3-Pyridylcarboxylic acid", "3-carboxylpyridine", "3-carboxypyridine", "3-pyridinecarboxylic acid", "NICOTINIC ACID", "NICOTINIC ACID", "Niacin", "Niacor", "Niaspan", "Nicotinic acid", "Nicotinic acid", "Nicotinsaure", "Nikotinsaeure", "P.P. factor", "PP factor", "acide nicotinique", "acido nicotinico", "acidum nicotinicum", "anti-pellagra vitamin", "beta-pyridinecarboxylic acid", "m-pyridinecarboxylic acid", "nicotinic acid", "nicotinic acid", "pellagra preventive factor", "pyridine-3-carboxylic acid", "pyridine-3-carboxylic acid", "pyridine-beta-carboxylic acid", "pyridine-carboxylique-3", "vitamin B3"], "secondary": {"asserted": {"id": "CHEBI:15940", "label": "nicotinic acid"}, "exact_current_rows": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[28]", "name": "Calcium D-(+)-pantothenate", "primary": {"id": "CHEBI:31345", "label": "Calcium pantothenate"}, "canonical_label": "Calcium pantothenate", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:137-08-6", "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278", "pubmed:20553011", "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula": ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"], "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"], "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]}, "synonyms": ["Calcium pantotenate", "Calcium pantothenate", "Calcium pantothenate, d-", "Calpan", "D-ca pantothenate", "D-calcium pantothenate", "NSC-36292", "Pantholin", "Pantothenic acid (as calcium)", "Pantothenic acid calcium salt", "Vitamin b5, calcium salt", "pantotenato de calcio", "pantothenate de calcium"]}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[29]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843", "label": "vitamin B12"}, "canonical_label": "vitamin B12", "label_equal": true, "definition": ["Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives)."], "annotations": {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:176843"]}, "synonyms": ["vitamin B-12", "vitamin B12 vitamer", "vitamin B12 vitamers", "vitamin B12", "vitamins B12"], "secondary": {"asserted": {"id": "CHEBI:176843", "label": "vitamin B12"}, "exact_current_rows": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[30]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "canonical_label": "4-aminobenzoic acid", "label_equal": true, "definition": ["An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:150-13-0", "drugbank:DB02362", "drugcentral:2049", "ecmdb:ECMDB01392", "gmelin:50150", "hmdb:HMDB0001392", "kegg.compound:C00568", "kegg.drug:D02456", "knapsack:C00001401", "pdb-ccd:PAB", "pubmed:12039592", "pubmed:14745019", "pubmed:15115392", "pubmed:1527790", "pubmed:16290145", "pubmed:17149871", "pubmed:17743450", "pubmed:17800214", "pubmed:19469519", "pubmed:22767283", "pubmed:22994574", "pubmed:23063996", "pubmed:23084339", "pubmed:23144588", "pubmed:23471007", "pubmed:3599019", "pubmed:3820215", "pubmed:3950915", "pubmed:8411009", "pubmed:9406595", "reaxys:471605", "wikipedia.en:4-Aminobenzoic_acid", "ymdb:YMDB00493"], "generalized_empirical_formula": ["C7H7NO2"], "has_alternative_id": ["CHEBI:113372", "CHEBI:1783", "CHEBI:20315", "CHEBI:44778"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30753"], "inchi_key_string": ["ALYNCZNDIQEVRV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"], "mass": ["137.138"], "monoisotopic_mass": ["137.04768"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]}, "synonyms": ["1-Amino-4-carboxybenzene", "4-AMINOBENZOIC ACID", "4-AMINOBENZOIC ACID", "4-Amino-benzoic acid", "4-Aminobenzoesaeure", "4-Aminobenzoic acid", "4-Aminobenzoic acid", "4-Carboxyaniline", "4-Carboxyphenylamine", "4-aminobenzoic acid", "4-aminobenzoic acid", "ABEE", "PABA", "gamma-Aminobenzoic acid", "gamma-aminobenzoic acid", "p-Aminobenzoesaeure", "p-aminobenzoic acid", "p-carboxyaniline", "p-carboxyphenylamine", "para-aminobenzoic acid"], "secondary": {"asserted": {"id": "CHEBI:30753", "label": "4-aminobenzoic acid"}, "exact_current_rows": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[31]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id": "CHEBI:16494", "label": "lipoic acid"}, "canonical_label": "lipoic acid", "label_equal": true, "definition": ["A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position."], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:122410", "cas:62-46-4", "drugbank:DB00166", "drugcentral:4732", "ecmdb:ECMDB01451", "gmelin:720915", "kegg.compound:C00725", "kegg.drug:D00086", "pubmed:15328413", "pubmed:7519986", "pubmed:7548757", "reaxys:81853", "wikipedia.en:Lipoic_acid", "ymdb:YMDB00334"], "generalized_empirical_formula": ["C8H14O2S2"], "has_alternative_id": ["CHEBI:146958", "CHEBI:25058", "CHEBI:6492"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16494"], "inchi_key_string": ["AGBQKNBQESQNJD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H14O2S2/c9-8(10)4-2-1-3-7-5-6-11-12-7/h7H,1-6H2,(H,9,10)"], "mass": ["206.332"], "monoisotopic_mass": ["206.04352"], "smiles_string": ["O=C(O)CCCCC1CCSS1"]}, "synonyms": ["1,2-dithiolane-3-pentanoic acid", "1,2-dithiolane-3-valeric acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)pentanoic acid", "5-(1,2-dithiolan-3-yl)valeric acid", "5-(dithiolan-3-yl)valeric acid", "5-[3-(1,2-dithiolanyl)]pentanoic acid", "6,8-thioctic acid", "6,8-thiotic acid", "6-thioctic acid", "6-thiotic acid", "Acetate-replacing factor", "Biletan", "Lipoic acid", "Thioctansaeure", "Thioctic acid", "Thioctsaeure", "Thioktsaeure", "alpha-Lipoic acid", "alpha-Liponsaeure", "alpha-lipoic acid", "liponic acid"], "secondary": {"asserted": {"id": "CHEBI:16494", "label": "lipoic acid"}, "exact_current_rows": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[32]", "name": "Syringic  acid", "primary": {"id": "CHEBI:68329", "label": "syringic acid"}, "canonical_label": "syringic acid", "label_equal": true, "definition": ["A dimethoxybenzene that is 3,5-dimethyl ether derivative of gallic acid."], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:530-57-4", "kegg.compound:C10833", "knapsack:C00002674", "lincs.smallmolecule:LSM-19009", "pubmed:21192716", "pubmed:21261296", "reaxys:2115262", "wikipedia.en:Syringic_acid"], "generalized_empirical_formula": ["C9H10O5"], "has_alternative_id": ["CHEBI:9379"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:68329"], "inchi_key_string": ["JMSVCTWVEWCHDZ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C9H10O5/c1-13-6-3-5(9(11)12)4-7(14-2)8(6)10/h3-4,10H,1-2H3,(H,11,12)"], "mass": ["198.174"], "monoisotopic_mass": ["198.05282"], "smiles_string": ["COc1cc(C(=O)O)cc(OC)c1O"]}, "synonyms": ["4-hydroxy-3,5-dimethoxybenzoic acid", "4-hydroxy-3,5-dimethoxybenzoic acid", "Cedar acid", "Gallic acid 3,5-dimethyl ether"]}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field": "ingredients[33]", "name": "NaOH", "primary": {"id": "CHEBI:32145", "label": "sodium hydroxide"}, "canonical_label": "sodium hydroxide", "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:1310-73-2", "gmelin:68430", "kegg.compound:C12569", "kegg.drug:D01169"], "generalized_empirical_formula": ["HO.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32145"], "inchi_key_string": ["HEMHJVSKTPXQMS-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/Na.H2O/h;1H2/q+1;/p-1"], "mass": ["39.997"], "monoisotopic_mass": ["39.99251"], "smiles_string": ["[Na+].[OH-]"]}, "synonyms": ["Aetznatron", "NaOH", "Natriumhydroxid", "Sodium hydroxide", "caustic soda", "hydroxyde de sodium", "soda lye", "sodium hydrate", "sodium hydroxide", "sodium hydroxide", "soude caustique"], "secondary": {"asserted": {"id": "CHEBI:32145", "label": "sodium hydroxide"}, "exact_current_rows": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}], "legacy": []} |
| importer | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _parse_api_solutions; _normalize_unit | context_only | Current importer separates the primary recipe and stock additions, preserves solution IDs/attributes and maps ml as ML_PER_L. It does not validate the inherited flattened recipe; no historical replay was performed. |
| cleanup | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current cleanup does not sum unequal duplicates. The actual local note documents 0.0994036 + 3.0 for magnesium across main and mineral-stock stages, requiring source-specific repair. |
| grounding-writer | scripts/apply_mim_groundings.py; missing-grounding exactMatch application and append-only event | context_only | Current writer adds a missing primary grounding while retaining existing groundings. The actual owner later event and term are inspected; the historical published mapping itself was not replayed. No export-absence inference is taken from an older script docstring. |
| history | data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml; Every target and maintained owner history and ingredient curation timestamp | supports | [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "curation_history[0].timestamp", "value": "2026-01-26T17:53:10.281602Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "curation_history[1].timestamp", "value": "2026-02-06T05:10:54.746247Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "curation_history[2].timestamp", "value": "2026-03-13T03:09:43.348143Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "curation_history[3].timestamp", "value": "2026-03-13T06:18:58.612636Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "curation_history[4].timestamp", "value": "2026-03-17T06:30:56.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "curation_history[5].timestamp", "value": "2026-03-17T19:45:10.047663+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "curation_history[6].timestamp", "value": "2026-06-05T07:40:46.749673+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "curation_history[7].timestamp", "value": "2026-06-10T07:46:52.381517+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path": "curation_history[8].timestamp", "value": "2026-08-06T03:05:21.479289+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "curation_history[0].timestamp", "value": "2026-01-26T17:53:10.281602Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "curation_history[1].timestamp", "value": "2026-02-06T05:10:54.746247Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "curation_history[2].timestamp", "value": "2026-03-13T03:09:43.348143Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "curation_history[3].timestamp", "value": "2026-03-13T06:18:58.612636Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "curation_history[4].timestamp", "value": "2026-03-17T06:30:56.000000Z", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "curation_history[5].timestamp", "value": "2026-03-17T19:45:10.047663+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "curation_history[6].timestamp", "value": "2026-06-05T07:40:46.749673+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "curation_history[7].timestamp", "value": "2026-06-10T07:46:52.381517+00:00", "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field_path": "curation_history[8].timestamp", "value": "2026-08-20T19:01:30.651337+00:00", "valid_ISO_datetime": true, "timezone_aware": true}] |
| merge | src/culturemech/merge/merger.py; RecipeMerger; merge_formulation_evidence; maintained formulation-aware merge context | context_only | The target is a generated merge with the exact normalized contributors pinned by inspection. The old ingredient-set fingerprint is not concentration, preparation or source equivalence. Current formulation-aware merging preserves only compatible assertions. No merge was run; verify owners and preview current grouping before separately authorized regeneration. |
| exporter | src/culturemech/export/kgx_export.py; medium_to_ingredient_edge; medium_to_solution_edge; _resolved_ingredient_id; _quantity | context_only | Current export consumes structured ingredient/solution identities and quantities, resolving against the pinned MIM index before fallback. It does not independently recover missing stock stages, source qualifiers or final volume. No export or resulting edge count is claimed. |

## Limits And Additional Notes

- The provider declares a 1006 mL main solution, whereas listed liquid additions sum 1006.5 mL; later sterile additions have incompletely specified stock volumes. Neither number is treated as independently measured final volume.
- Current DSMZ PDF and current MediaDive stock preparation differ. Both inspected versions are preserved; their relative historical chronology is not inferred from retrieval times or the PDF footer.
- The nominal 0.3 M initial syringate stock and the later final 2 g/L Na-syringate feed have different stages and chemical-basis qualifiers. No additional feed volume or salt mass is inferred from the acid precursor alone.
- SIGMA S6881 is retained as a source product designation; no separate manufacturer specification or equivalence was authenticated. Historical MIM publication provenance is recorded, not independently replayed.
- No strain-specific growth, taxonomy, assembly, literature experiment or optimization claim is inferred from the medium name.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T101058Z-culturemech-000819-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acetobacterium_dehalogenans_medium (CultureMech:000819)'
started_at: '2026-10-21T09:56:51Z'
finished_at: '2026-10-21T10:10:58Z'
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
summary: DSMZ 135b identifies the medium, but the target and normalized owner flatten
  three stock recipes into the medium, add stock and direct magnesium values, and
  encode 50 mL of 5 N NaOH as 50 g/L. All four preparation steps are retained, including
  the later syringate feed; the syringate-stock starting water volume and pH follow
  MediaDive and conflict with the current collection PDF. Nickel hydrate and sodium-resazurin
  groundings lose supplied-form identity. The owner has a later, supported syringic-acid
  grounding absent from the generated target. All four diagnostics passed.
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
  - path: data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml
    sha256: 309ad02c1932414af7e020483a0b660d547297020aebafb9903eca656504040f
    role: target
  - path: data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml
    sha256: a6845863a22bffdd940f08649e4271f9a5a2db251362983432c344b4142ee874
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
  selection: Task review 146; batch 015 item 6 of 10, selected in Python lexicographic
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
  - CultureMech:000819
targets:
- target_id: CultureMech:000819
  path: data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml
  label: acetobacterium_dehalogenans_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:000819
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch015/146/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch015/146/strict.tsv"
  target_ids:
  - CultureMech:000819
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:000819
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:000819
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
  - CultureMech:000819
- check_id: scoped-history
  name: Scoped timestamp syntax and timezone inspection
  required: false
  status: passed
  summary: 18 timestamps inspected, 0 invalid or timezone-naive; old provenance remains
    unchanged.
  target_ids:
  - CultureMech:000819
  evidence_ids:
  - history
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T10:10:58Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:10:58Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:57:36.792966Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch015/146/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T09:57:41.181886Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch015/146/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:57:45.893636Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:57:49.214191Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: source-catalog
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch015/source-preflight-bound/146/source-catalog.json
  locator: Complete bound per-record catalog, raw/text/metadata hashes and actual
    original capture times
  accessed_at: '2026-10-21T10:10:58Z'
  support: context_only
  summary: '[{"key": "dsmz135b", "url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf",
    "status": 200, "accessed_at": "2026-10-21T09:49:54.063702Z", "sha256": "349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2",
    "metadata_sha256": "0b960e474d68296edbfa5a196561043afe7e87e91656c54a7957ae28f439b63a",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": null}, {"key": "mediadive135bapi",
    "url": "https://mediadive.dsmz.de/rest/medium/135b", "status": 200, "accessed_at":
    "2026-10-21T09:49:53.218168Z", "sha256": "6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631",
    "metadata_sha256": "7c9822a238e3435c7d8eec6355e8803b30add7ecffa8e91b971f61e744f3cf64",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": null}, {"key": "chebi131361",
    "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361",
    "status": 200, "accessed_at": "2026-10-21T07:33:27.980786Z", "sha256": "643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10",
    "metadata_sha256": "6db2617d6db6dbd86bf7d3a556b38ea9c4ce51def5fe8bba9af365858cd75d91",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch012-tail/119/chebi131361.json"},
    {"key": "chebi131527", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527",
    "status": 200, "accessed_at": "2026-10-20T07:22:08.349487Z", "sha256": "349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3",
    "metadata_sha256": "3a766b9f2333e4e878844dfc870ba817519bc0f162e20241867c63578da23d0c",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/139/chebi131527.json"},
    {"key": "chebi15940", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940",
    "status": 200, "accessed_at": "2026-10-20T06:55:11.874279Z", "sha256": "3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1",
    "metadata_sha256": "e7562fd7849a085522d6f2816b44426f9441f649cc5eb073b01dbdfc1f014c03",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15940.json"},
    {"key": "chebi15956", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956",
    "status": 200, "accessed_at": "2026-10-21T08:42:30.425993Z", "sha256": "d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd",
    "metadata_sha256": "e52c2340aa05039b4c3db0486ec28605382c809f66c738d247c5a79bf847e018",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi15956.json"},
    {"key": "chebi16494", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494",
    "status": 200, "accessed_at": "2026-10-20T06:55:13.001958Z", "sha256": "aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1",
    "metadata_sha256": "5dc4cdf6b7e18e3e9a1cc3b257d7e0390151a592c44d2140fc816236358152a8",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/129/chebi16494.json"},
    {"key": "chebi17015", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015",
    "status": 200, "accessed_at": "2026-10-20T06:55:11.583596Z", "sha256": "f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4",
    "metadata_sha256": "550b9c89dbe67561dbeff24d27f909c466dee50e589a6b87bd8dec1d776343a1",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi17015.json"},
    {"key": "chebi176843", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843",
    "status": 200, "accessed_at": "2026-10-21T08:17:26.997779Z", "sha256": "b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9",
    "metadata_sha256": "acfbff41d59e80b1235ae594244cc033d9c608fbc00dd7e14f958a79ce3047fe",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi176843.json"},
    {"key": "chebi26710", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710",
    "status": 200, "accessed_at": "2026-10-21T08:42:42.219040Z", "sha256": "2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e",
    "metadata_sha256": "b958fd70f3637fa701eeaad458e38c7d16b7054e332506fcdaa247cf75ec5368",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi26710.json"},
    {"key": "chebi27470", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470",
    "status": 200, "accessed_at": "2026-10-20T06:55:10.450814Z", "sha256": "fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f",
    "metadata_sha256": "72fc9858223c889295c3a4f38bed8284d4bc656950129d666afeefc3e38bfa1e",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi27470.json"},
    {"key": "chebi29377", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377",
    "status": 200, "accessed_at": "2026-10-21T07:31:16.500548Z", "sha256": "21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1",
    "metadata_sha256": "e874e563999cbf540698c26bbdb00295a3d8b10dcff2c3b999951b75d8532e9d",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/133/chebi29377.json"},
    {"key": "chebi30753", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753",
    "status": 200, "accessed_at": "2026-10-20T06:55:12.829785Z", "sha256": "97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a",
    "metadata_sha256": "693c039bb1b4c8c97d6e544865a7bd86fe43a028630cbb707e55b715405a05da",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi30753.json"},
    {"key": "chebi30961", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961",
    "status": 200, "accessed_at": "2026-10-21T08:42:44.571163Z", "sha256": "f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d",
    "metadata_sha256": "3764cce319cbb0849d074b03930586fe88d38b3715e3a03ebba947816c8ca08d",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi30961.json"},
    {"key": "chebi31206", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206",
    "status": 200, "accessed_at": "2026-10-21T08:17:28.439407Z", "sha256": "ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76",
    "metadata_sha256": "2429062a66eb2c4070802bd9c331cd52c04dc31177203bc5faf978801bfd0cd2",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi31206.json"},
    {"key": "chebi31345", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345",
    "status": 200, "accessed_at": "2026-10-20T06:55:12.450283Z", "sha256": "56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d",
    "metadata_sha256": "80a34fd39f06278b7a513d5f5f094e77bd7199099d1c3117179a9630f3c1178d",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi31345.json"},
    {"key": "chebi31440", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440",
    "status": 200, "accessed_at": "2026-10-21T08:17:28.489501Z", "sha256": "e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9",
    "metadata_sha256": "2c5574b80e0c5cdb1912319692ad52060ead0884b613a14d7d8a0ac24d68ae78",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi31440.json"},
    {"key": "chebi31795", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795",
    "status": 200, "accessed_at": "2026-10-21T08:42:45.232212Z", "sha256": "45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb",
    "metadata_sha256": "f4a78752383e9b0e4bf4d231bd5c6d6812b9083dcd0e3b7ce132fd768157ebb2",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/140/chebi31795.json"},
    {"key": "chebi32145", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145",
    "status": 200, "accessed_at": "2026-10-21T07:33:28.263004Z", "sha256": "db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1",
    "metadata_sha256": "c5d92c8ffa74d83a51a4511c8930c40eb8fc3f7feecbc5e8a9ef115f2d175603",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch009-tail/087/chebi32145.json"},
    {"key": "chebi32312", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312",
    "status": 200, "accessed_at": "2026-10-21T08:17:28.879505Z", "sha256": "eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9",
    "metadata_sha256": "15af6d0097b16e29579d099bdfccdaff7965d9fcc8519053242b34f9549d8370",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi32312.json"},
    {"key": "chebi33118", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118",
    "status": 200, "accessed_at": "2026-10-21T08:17:29.364390Z", "sha256": "f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87",
    "metadata_sha256": "cc933d351148d7c0715ab8a426f30f5b337f0ade4cefae27db6e4b01503e384a",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/131/chebi33118.json"},
    {"key": "chebi34887", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887",
    "status": 200, "accessed_at": "2026-10-21T08:04:44.093348Z", "sha256": "f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc",
    "metadata_sha256": "ace22ea0a6afa3fef5a976ed08800e02c88d5027903966b27e57fd6f168edc8a",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi34887.json"},
    {"key": "chebi44557", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557",
    "status": 200, "accessed_at": "2026-10-21T08:46:15.250117Z", "sha256": "de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2",
    "metadata_sha256": "ed0fbe1210115b31327b59b358a5a8390a3f9b87070a3f1328d1f15844b32f81",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi44557.json"},
    {"key": "chebi49105", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105",
    "status": 200, "accessed_at": "2026-10-20T06:55:10.911379Z", "sha256": "0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4",
    "metadata_sha256": "5962aead9fc53da7aee732642350213639d620e3292cb1211ff62dcc374fe4e9",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi49105.json"},
    {"key": "chebi63036", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036",
    "status": 200, "accessed_at": "2026-10-21T08:17:29.666916Z", "sha256": "48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3",
    "metadata_sha256": "b93addd6bedfb21bf70655ad0b6e76e0f59d30bed59ffb79f8ab5dd7c785603b",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/139/chebi63036.json"},
    {"key": "chebi63939", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939",
    "status": 200, "accessed_at": "2026-10-20T06:55:09.796192Z", "sha256": "987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a",
    "metadata_sha256": "db4f37074b96a1ac5b960deb9fc6a16aa1397619968bc14e31edc1b5844c6017",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi63939.json"},
    {"key": "chebi68329", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_68329",
    "status": 200, "accessed_at": "2026-10-21T09:49:55.684762Z", "sha256": "ab4909b4d8849b2be576c308144e611e48498c72e62bbf71a50ab599f11a241a",
    "metadata_sha256": "d40b185437a07920a0c4df1c896dc72078ac9153a2fee9aaec52f5c6c0a12c40",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": null}, {"key": "chebi75213",
    "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213",
    "status": 200, "accessed_at": "2026-10-21T08:17:29.756647Z", "sha256": "b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083",
    "metadata_sha256": "86cdd4c07b0a7b3c2c4a858d56c49f819c30701d4a7669d89ecacd9dcd07ed91",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/136/chebi75213.json"},
    {"key": "chebi75836", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836",
    "status": 200, "accessed_at": "2026-10-20T06:55:07.038393Z", "sha256": "14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525",
    "metadata_sha256": "3cc3b4f20f8bba8a11d5f43d16fe9479fe773959c3b9092a18caf6bd410924d7",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi75836.json"},
    {"key": "chebi86158", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158",
    "status": 200, "accessed_at": "2026-10-21T08:17:30.011607Z", "sha256": "b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61",
    "metadata_sha256": "cad4db43580fd7a702ca8a3e89015b1d837dd83826aca0f237013819dcc80952",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/137/chebi86158.json"},
    {"key": "chebi86364", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364",
    "status": 200, "accessed_at": "2026-10-21T07:33:35.036768Z", "sha256": "f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069",
    "metadata_sha256": "bbb983bc358d6ab5b74b0d327e75e243992232621d1b827e9c5cd5d4a2b368a4",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/134/chebi86364.json"},
    {"key": "chebi86465", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465",
    "status": 200, "accessed_at": "2026-10-20T06:55:08.054799Z", "sha256": "5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c",
    "metadata_sha256": "0b9b603fad389586c6b0e471233285e94bfda8db575e6558608a521f3d7da66d",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch013-tail/130/chebi86465.json"},
    {"key": "chebi8806", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806",
    "status": 200, "accessed_at": "2026-10-21T08:17:30.774007Z", "sha256": "e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5",
    "metadata_sha256": "5b204c6d41931db1f3d77249fa43adfeabb2f474e8054f132da0b2065702882b",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014-tail/138/chebi8806.json"},
    {"key": "chebi91244", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244",
    "status": 200, "accessed_at": "2026-10-20T06:55:07.079384Z", "sha256": "dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa",
    "metadata_sha256": "0ae2a87eac7f4b379b0dd8645092ea312c0f1ce0774318d6b10ac055f4a37a27",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-work-batch004/sources/chebi91244.json"},
    {"key": "chebi91248", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248",
    "status": 200, "accessed_at": "2026-10-21T08:42:32.136441Z", "sha256": "7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683",
    "metadata_sha256": "07e956bc7f4e172fd975d96f93fe9c9d096c1ead9bc1b9ec6d48490af2d17083",
    "content_limit": "Exact source capture for later source-scoped review; no final
    scientific assessment made.", "reused_capture_from": "/private/tmp/culturemech-review-source-preflight-batch014/133/chebi91248.json"}]'
  snapshot_sha256: 12b190afa130ee0dbd9b61864c77864b3cb73551c6db45ab1e5cb26f845524fc
- evidence_id: dsmz135b
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: pages 1–2, complete formulation and preparation
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: supports
  summary: Exact DSMZ 135b collection recipe, both pages read completely and visually
    inspected from the bound PDF. Main recipe, three named stock sections, after-growth
    feed and preparation were checked. Footer ©2023 DSMZ is retained without inferring
    a separate publication date.
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: mediadive135bapi
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.medium and $.data.solutions[0:4]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: supports
  summary: 'Exact medium 135b response: main solution 233 and stocks 241, 5980 and
    6318. All recipe rows, source attributes, declared stage volumes and steps inspected.'
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-1
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[0].recipe[0]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1006 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 1,\n                      \
    \  \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n  \
    \                      \"amount\": 1,\n                        \"unit\": \"g\"\
    ,\n                        \"g_l\": 0.994036,\n                        \"mmol_l\"\
    : 18.5836,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-2
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[0].recipe[1]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1006 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 2,\n                      \
    \  \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n \
    \                       \"amount\": 0.33,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 0.328032,\n                        \"mmol_l\"\
    : 2.41049,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-3
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[0].recipe[2]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1006 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 3,\n                      \
    \  \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n \
    \                       \"amount\": 0.45,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 0.447316,\n                        \"mmol_l\"\
    : 2.56818,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-4
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[0].recipe[3]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 4,\n                      \
    \  \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":\
    \ 8,\n                        \"amount\": 0.1,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.0994036,\n                      \
    \  \"mmol_l\": 0.403299,\n                        \"optional\": 0\n          \
    \          }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-5
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[0].recipe[4]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: supports
  summary: The main recipe explicitly adds 20 ml of stock 241. Restore this dose and
    the separate stock definition; the stored flat ingredient strengths do not encode
    its dilution.
  quote: "{\n                        \"recipe_order\": 5,\n                      \
    \  \"solution\": \"Modified Wolin's mineral solution\",\n                    \
    \    \"solution_id\": 241,\n                        \"amount\": 20,\n        \
    \                \"unit\": \"ml\",\n                        \"optional\": 0\n\
    \                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-6
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[0].recipe[5]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1006 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 6,\n                      \
    \  \"compound\": \"Yeast extract\",\n                        \"compound_id\":\
    \ 16,\n                        \"amount\": 2,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 1.98807,\n                        \"\
    optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-7
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[0].recipe[6]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1006 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 7,\n                      \
    \  \"compound\": \"Sodium resazurin\",\n                        \"compound_id\"\
    : 1852,\n                        \"attribute\": \"0.1% w/v\",\n              \
    \          \"amount\": 0.5,\n                        \"unit\": \"ml\",\n     \
    \                   \"g_l\": 0.000497018,\n                        \"mmol_l\"\
    : 0.00197881,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-8
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[0].recipe[7]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1006 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 8,\n                      \
    \  \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n \
    \                       \"amount\": 1.5,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 1.49105,\n                        \"mmol_l\"\
    : 14.0681,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-9
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[0].recipe[8]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: supports
  summary: The main recipe explicitly adds 15 ml of stock 6318. Restore this dose
    and the separate stock definition; the stored flat ingredient strengths do not
    encode its dilution.
  quote: "{\n                        \"recipe_order\": 9,\n                      \
    \  \"solution\": \"Na-syringate solution (0.3 M)\",\n                        \"\
    solution_id\": 6318,\n                        \"amount\": 15,\n              \
    \          \"unit\": \"ml\",\n                        \"optional\": 0\n      \
    \              }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-10
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[0].recipe[9]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: supports
  summary: The main recipe explicitly adds 1 ml of stock 5980. Restore this dose and
    the separate stock definition; the stored flat ingredient strengths do not encode
    its dilution.
  quote: "{\n                        \"recipe_order\": 10,\n                     \
    \   \"solution\": \"Wolin's vitamin solution (10x)\",\n                      \
    \  \"solution_id\": 5980,\n                        \"amount\": 1,\n          \
    \              \"unit\": \"ml\",\n                        \"optional\": 0\n  \
    \                  }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-11
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[0].recipe[10]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: supports
  summary: The current value follows provider g_l on its declared 1006 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.
  quote: "{\n                        \"recipe_order\": 11,\n                     \
    \   \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\"\
    : 770,\n                        \"amount\": 0.5,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.497018,\n                       \
    \ \"mmol_l\": 2.82982,\n                        \"optional\": 0\n            \
    \        }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-12
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[0].recipe[11]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: supports
  summary: Preserve the source solvent quantity 970 ml in its own stage. The provider
    declares this solution volume as 1006 mL; water addition is not independent proof
    of measured final volume.
  quote: "{\n                        \"recipe_order\": 12,\n                     \
    \   \"compound\": \"Distilled water\",\n                        \"compound_id\"\
    : 4,\n                        \"amount\": 970,\n                        \"unit\"\
    : \"ml\",\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-13
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[0]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 1,\n                      \
    \  \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\"\
    : 189,\n                        \"amount\": 1.5,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\"\
    : 7.84765,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-14
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[1]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 2,\n                      \
    \  \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":\
    \ 8,\n                        \"amount\": 3,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\"\
    : 12.1716,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-15
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[2]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 3,\n                      \
    \  \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n\
    \                        \"amount\": 0.5,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\"\
    : 2.9583,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-16
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[3]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 4,\n                      \
    \  \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n   \
    \                     \"amount\": 1,\n                        \"unit\": \"g\"\
    ,\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n\
    \                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-17
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[4]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 5,\n                      \
    \  \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":\
    \ 12,\n                        \"amount\": 0.1,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\"\
    : 0.359693,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-18
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[5]
  accessed_at: '2026-10-21T09:49:53.218168Z'
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
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-19
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[6]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 7,\n                      \
    \  \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":\
    \ 7,\n                        \"amount\": 0.1,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\"\
    : 0.680203,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-20
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[7]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 8,\n                      \
    \  \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":\
    \ 35,\n                        \"amount\": 0.18,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\"\
    : 0.625954,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-21
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[8]
  accessed_at: '2026-10-21T09:49:53.218168Z'
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
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-22
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[9]
  accessed_at: '2026-10-21T09:49:53.218168Z'
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
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-23
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[10]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 11,\n                     \
    \   \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n \
    \                       \"amount\": 0.01,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\"\
    : 0.161708,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-24
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[11]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 12,\n                     \
    \   \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\"\
    : 9,\n                        \"amount\": 0.01,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\"\
    : 0.0413309,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-25
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[12]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 13,\n                     \
    \   \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\"\
    : 40,\n                        \"amount\": 0.03,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\"\
    : 0.231483,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-26
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[13]
  accessed_at: '2026-10-21T09:49:53.218168Z'
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
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-27
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[14]
  accessed_at: '2026-10-21T09:49:53.218168Z'
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
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-28
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[1].recipe[15]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: supports
  summary: Preserve the source solvent quantity 1000 ml in its own stage. The provider
    declares this solution volume as 1000 mL; water addition is not independent proof
    of measured final volume.
  quote: "{\n                        \"recipe_order\": 16,\n                     \
    \   \"compound\": \"Distilled water\",\n                        \"compound_id\"\
    : 4,\n                        \"amount\": 1000,\n                        \"unit\"\
    : \"ml\",\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-29
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[2].recipe[0]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 1,\n                      \
    \  \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n \
    \                       \"amount\": 20,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\"\
    : 0.0818632,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-30
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[2].recipe[1]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 2,\n                      \
    \  \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n\
    \                        \"amount\": 20,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\"\
    : 0.0453104,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-31
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[2].recipe[2]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 3,\n                      \
    \  \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\"\
    : 519,\n                        \"amount\": 100,\n                        \"unit\"\
    : \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\"\
    : 0.486287,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-32
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[2].recipe[3]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 4,\n                      \
    \  \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n\
    \                        \"amount\": 50,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\"\
    : 0.148236,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-33
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[2].recipe[4]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 5,\n                      \
    \  \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n\
    \                        \"amount\": 50,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\"\
    : 0.132837,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-34
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[2].recipe[5]
  accessed_at: '2026-10-21T09:49:53.218168Z'
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
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-35
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[2].recipe[6]
  accessed_at: '2026-10-21T09:49:53.218168Z'
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
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-36
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[2].recipe[7]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 8,\n                      \
    \  \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n\
    \                        \"amount\": 1,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\"\
    : 0.00073779,\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-37
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[2].recipe[8]
  accessed_at: '2026-10-21T09:49:53.218168Z'
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
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-38
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[2].recipe[9]
  accessed_at: '2026-10-21T09:49:53.218168Z'
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
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-39
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[2].recipe[10]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: supports
  summary: Preserve the source solvent quantity 1000 ml in its own stage. The provider
    declares this solution volume as 1000 mL; water addition is not independent proof
    of measured final volume.
  quote: "{\n                        \"recipe_order\": 11,\n                     \
    \   \"compound\": \"Distilled water\",\n                        \"compound_id\"\
    : 4,\n                        \"amount\": 1000,\n                        \"unit\"\
    : \"ml\",\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-40
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[3].recipe[0]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: This is a stock composition or a direct contribution currently combined
    with a stock value. Preserve original batch amount, exact source form and stock
    stage; do not use this stock strength as a direct final-medium concentration.
  quote: "{\n                        \"recipe_order\": 1,\n                      \
    \  \"compound\": \"Syringic  acid\",\n                        \"compound_id\"\
    : 2124,\n                        \"attribute\": \"SIGMA S6881\",\n           \
    \             \"amount\": 60,\n                        \"unit\": \"g\",\n    \
    \                    \"g_l\": 60,\n                        \"optional\": 0\n \
    \                   }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-41
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[3].recipe[1]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: The row specifies 50 mL of 5 N NaOH in the syringate stock, not 50 g/L
    direct NaOH. Preserve normality, liquid dose, titration qualifier and stock stage.
    Both source preparations describe about/around 50 mL, so no exact endpoint-dependent
    mass is asserted.
  quote: "{\n                        \"recipe_order\": 2,\n                      \
    \  \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n  \
    \                      \"attribute\": \"5 N\",\n                        \"amount\"\
    : 50,\n                        \"unit\": \"ml\",\n                        \"optional\"\
    : 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-42
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[3].recipe[2]
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: supports
  summary: Preserve the source solvent quantity 950 ml in its own stage. The provider
    declares this solution volume as 1000 mL; water addition is not independent proof
    of measured final volume.
  quote: "{\n                        \"recipe_order\": 3,\n                      \
    \  \"compound\": \"Distilled water\",\n                        \"compound_id\"\
    : 4,\n                        \"amount\": 950,\n                        \"unit\"\
    : \"ml\",\n                        \"optional\": 0\n                    }"
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
- evidence_id: quantity-43
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 1, main preparation step 1
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: supports
  summary: The initial gas mixture and same-atmosphere dispensing are retained in
    both local layers; this is preparation evidence, not a strain phenotype.
  quote: bring to the boil and cool to room temperature under 80% N2 and 20% CO2 gas
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: quantity-44
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 1, main preparation step 1
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: supports
  summary: Retain the explicit 100% N2 stock-preparation qualifier and its scope;
    the following carbonate stock has a different atmosphere.
  quote: sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from
    a sterile
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: quantity-45
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 1, main preparation step 1
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: supports
  summary: The carbonate-stock atmosphere is preserved independently of the preceding
    100% N2 stocks.
  quote: anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Vitamins
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: quantity-46
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 1, main preparation step 1
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: supports
  summary: Both local layers preserve the exact pH 7.4 condition and vitamin filtration.
    No pH range is invented.
  quote: should be sterilized by filtration. The pH of the completed medium should
    be at 7.4.
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: quantity-47
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 1, main preparation step 2, following explicit after-growth trigger
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: supports
  summary: The target and owner preserve the source after-growth final concentration.
    This is not 2 g added per original batch, nor the initial 15 mL stock dose; salt-versus-acid
    mass basis and feed volume are not inferred.
  quote: a final concentration of 2.00 g/l.
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: quantity-48
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 2, continuation of mineral-stock preparation
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: supports
  summary: Preserve the initial pH 6.5 titration stage.
  quote: First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then
    add minerals. Adjust
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: quantity-49
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 2, mineral-stock preparation
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: supports
  summary: Preserve final pH 7.0 separately from the preceding pH 6.5 step.
  quote: final to pH 7.0 with KOH.
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: quantity-50
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 2, mineral-stock preparation
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: supports
  summary: The source identifies KOH but gives no fixed amount. Preserve titration
    without assigning zero or a guessed concentration.
  quote: final to pH 7.0 with KOH.
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: quantity-51
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 2, Na-syringate stock preparation
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: context_only
  summary: Current collection PDF specifies 800 mL initially, while the local records
    and current MediaDive preparation specify 700 mL. Both versions are preserved.
    Neither initial quantity is the table water amount 950 mL or the final makeup
    volume.
  quote: Dissolve syringic acid in 800 ml distilled water, add around 50 ml 5 N NaOH,
    and adjust pH
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: quantity-52
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 2, Na-syringate stock preparation
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: context_only
  summary: Current PDF specifies about pH 7.0, whereas local/provider text gives about
    7.5. This is an explicit source-version conflict; no chronology or automatic replacement
    is assumed.
  quote: to about 7.0. Then add water to reach a volume of 1000 ml. Make the solution
    anoxic by
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: quantity-53
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 2, Na-syringate stock preparation
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: supports
  summary: Both source versions preserve approximately 50 mL of 5 N NaOH. The approximate
    dose and pH endpoint qualify the exact-looking table amount; no density conversion
    is used.
  quote: Dissolve syringic acid in 800 ml distilled water, add around 50 ml 5 N NaOH,
    and adjust pH
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: quantity-54
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 2, Na-syringate stock preparation
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: supports
  summary: The 1000 mL instruction is a final makeup volume, distinct from table water
    950 mL and initial dissolution water 800/700 mL. Do not add all three water quantities.
  quote: to about 7.0. Then add water to reach a volume of 1000 ml. Make the solution
    anoxic by
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: quantity-55
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 2, Na-syringate stock preparation
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: supports
  summary: Both local records preserve 100% N2 sparging and anoxic dispensing.
  quote: sparging with 100% N2 gas, distribute in anoxic serum vials and autoclave
    at 121°C.
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: quantity-56
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 2, Na-syringate stock preparation
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: supports
  summary: The source gives 121 °C for this stock. Do not transfer this numeric temperature
    to the main-medium instruction or invent a cycle duration.
  quote: sparging with 100% N2 gas, distribute in anoxic serum vials and autoclave
    at 121°C.
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: quantity-57
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 2, Na-syringate stock preparation
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: supports
  summary: No duration is specified in the complete stock instruction. This is an
    evidence limit, not permission to insert a generic cycle.
  quote: sparging with 100% N2 gas, distribute in anoxic serum vials and autoclave
    at 121°C.
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: quantity-58
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium135b.pdf
  locator: page 1, main preparation step 1
  accessed_at: '2026-10-21T09:49:54.063702Z'
  support: supports
  summary: The source gives their ingredient masses but not all sterile-stock dose
    volumes. These additions do not establish an exact measured final volume.
  quote: sterile anoxic stock solutions prepared under 100% N2 gas and carbonate from
    a sterile
  snapshot_sha256: 349ee1bc14163bb547c7338030a32bfa7f34b350bc8be5fe4511e58a26b15ed2
- evidence_id: provider-stock-preparation
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/135b
  locator: $.data.solutions[3].steps[0].step
  accessed_at: '2026-10-21T09:49:53.218168Z'
  support: context_only
  summary: The complete current provider stock instruction agrees with local 700 mL
    and about pH 7.5 while preserving approximately 50 mL of 5 N NaOH, makeup to 1000
    mL, 100% N2 and 121 °C.
  quote: Add syringic acid to 700 ml distilled water, add about 50 ml of 5 N NaOH
    and adjust the pH to about 7.5 to dissolve it. Then make up to a volume of 1000
    ml with water. Make the solution anoxic by sparging with 100% N2 gas, distribute
    in anoxic serum vials and autoclave at 121°C.
  snapshot_sha256: 6f12fdbe8b801a9c6d0ecb3cb9b4c7ee670821e2e7b6f7a01df714129df0f631
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
- evidence_id: chebi32145
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T07:33:28.263004Z'
  support: supports
  summary: CHEBI:32145 resolves to sodium hydroxide and is not obsolete. Available
    definitions, formulae, structures and synonyms were inspected; recipe amounts
    and supplied forms are assessed separately.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi68329
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_68329
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-21T09:49:55.684762Z'
  support: supports
  summary: CHEBI:68329 resolves to syringic acid and is not obsolete. Available definitions,
    formulae, structures and synonyms were inspected; recipe amounts and supplied
    forms are assessed separately.
  snapshot_sha256: ab4909b4d8849b2be576c308144e611e48498c72e62bbf71a50ab599f11a241a
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned snapshot; exact MAPPED/preferred_term rows for asserted CHEBI
    keys and exact legacy-key lookup
  accessed_at: '2026-10-21T10:10:58Z'
  support: supports
  summary: '{"metadata": {"byte_count": 824387, "consumer_contract_version": 1, "data_row_count":
    9077, "header": ["label", "match_type", "identifier", "preferred_term", "ontology_id",
    "mapping_status", "ambiguity"], "repository": "https://github.com/CultureBotAI/MediaIngredientMech",
    "sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5",
    "source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "source_path": "docs/data/label_index.csv"},
    "counts": {"target": {"ingredient_instances": 34, "primary_CHEBI_instances": 32,
    "secondary_current_asserted_instances": 30, "secondary_current_verified_instances":
    30, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 94.12, "secondary_verified_percent":
    88.24}, "owner-0": {"ingredient_instances": 34, "primary_CHEBI_instances": 33,
    "secondary_current_asserted_instances": 30, "secondary_current_verified_instances":
    30, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.06, "secondary_verified_percent":
    88.24}}, "instances": [{"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[0]", "name": "NH4Cl", "primary": {"id": "CHEBI:31206", "label":
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
    "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[1]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036",
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
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[2]", "name": "K2HPO4", "primary": {"id": "CHEBI:131527",
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
    "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[3]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795",
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
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[4]", "name": "Yeast extract"}, {"layer": "target", "path":
    "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[5]",
    "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806", "label": "Resazurin"},
    "canonical_label": "Resazurin", "label_equal": true, "definition": [], "annotations":
    {"charge": [0.0], "database_cross_reference": ["cas:550-82-3", "kegg.compound:C11178"],
    "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"],
    "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]},
    "synonyms": ["Resazurin"]}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[6]", "name": "Na2CO3", "primary": {"id": "CHEBI:29377",
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
    "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[7]", "name": "L-Cysteine HCl x H2O", "primary": {"id": "CHEBI:91248",
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
    "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[8]",
    "name": "Nitrilotriacetic acid", "primary": {"id": "CHEBI:44557", "label": "nitrilotriacetic
    acid"}, "canonical_label": "nitrilotriacetic acid", "label_equal": true, "definition":
    [], "annotations": {"charge": [0.0], "database_cross_reference": ["beilstein:1710776",
    "cas:139-13-9", "drugbank:DB03040", "gmelin:3726", "kegg.compound:C14695", "pdb-ccd:NTA"],
    "generalized_empirical_formula": ["C6H9NO6"], "has_alternative_id": ["CHEBI:34889",
    "CHEBI:44555"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:44557"],
    "inchi_key_string": ["MGFYIUFZLHCRTH-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"],
    "mass": ["191.139"], "monoisotopic_mass": ["191.04299"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]},
    "synonyms": ["Complexon I", "H3nta", "Komplexon I", "N(CH2-COOH)3", "N,N-bis(carboxymethyl)glycine",
    "N,N-bis(carboxymethyl)glycine", "NITRILOTRIACETIC ACID", "NTA", "Nitrilotriacetate",
    "Nitrilotriacetic acid", "Nitrilotriessigsaeure", "Triglycollamic acid", "Trilon
    A", "alpha,alpha'',alpha''''-trimethylaminetricarboxylic acid", "nitrilo-2,2'',2''''-triacetic
    acid", "tri(carboxymethyl)amine", "triglycine"], "secondary": {"asserted": {"id":
    "CHEBI:44557", "label": "nitrilotriacetic acid"}, "exact_current_rows": [{"label":
    "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557",
    "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[9]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364",
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
    "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[10]",
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
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[11]", "name": "FeSO4 x 7 H2O", "primary": {"id": "CHEBI:75836",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[12]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[13]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[14]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312",
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
    {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[15]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440",
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
    "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[16]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465",
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
    "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[17]", "name": "H3BO3", "primary": {"id": "CHEBI:33118",
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
    "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[18]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213",
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
    {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[19]", "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887",
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
    "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[20]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361",
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
    "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[21]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939",
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
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[22]", "name": "Biotin", "primary": {"id": "CHEBI:15956",
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
    "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[23]",
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
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[24]", "name": "Pyridoxine hydrochloride", "primary": {"id":
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
    "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[25]",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[26]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015",
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
    "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[27]",
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
    "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[28]", "name": "Calcium D-(+)-pantothenate", "primary": {"id":
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
    "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[29]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843",
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
    {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[30]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753",
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
    "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[31]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id":
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
    "ambiguity": "unique"}]}}, {"layer": "target", "path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field": "ingredients[32]", "name": "Syringic  acid"}, {"layer": "target", "path":
    "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field": "ingredients[33]",
    "name": "NaOH", "primary": {"id": "CHEBI:32145", "label": "sodium hydroxide"},
    "canonical_label": "sodium hydroxide", "label_equal": true, "definition": [],
    "annotations": {"charge": [0.0], "database_cross_reference": ["cas:1310-73-2",
    "gmelin:68430", "kegg.compound:C12569", "kegg.drug:D01169"], "generalized_empirical_formula":
    ["HO.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32145"], "inchi_key_string":
    ["HEMHJVSKTPXQMS-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/Na.H2O/h;1H2/q+1;/p-1"],
    "mass": ["39.997"], "monoisotopic_mass": ["39.99251"], "smiles_string": ["[Na+].[OH-]"]},
    "synonyms": ["Aetznatron", "NaOH", "Natriumhydroxid", "Sodium hydroxide", "caustic
    soda", "hydroxyde de sodium", "soda lye", "sodium hydrate", "sodium hydroxide",
    "sodium hydroxide", "soude caustique"], "secondary": {"asserted": {"id": "CHEBI:32145",
    "label": "sodium hydroxide"}, "exact_current_rows": [{"label": "NaOH", "match_type":
    "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id":
    "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}, {"layer":
    "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[0]", "name": "NH4Cl", "primary": {"id": "CHEBI:31206", "label":
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
    "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[1]", "name": "KH2PO4", "primary": {"id": "CHEBI:63036",
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
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[2]", "name": "K2HPO4", "primary": {"id": "CHEBI:131527",
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
    "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[3]", "name": "MgSO4 x 7 H2O", "primary": {"id": "CHEBI:31795",
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
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[4]", "name": "Yeast extract"}, {"layer": "owner-0", "path":
    "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field":
    "ingredients[5]", "name": "Sodium resazurin", "primary": {"id": "CHEBI:8806",
    "label": "Resazurin"}, "canonical_label": "Resazurin", "label_equal": true, "definition":
    [], "annotations": {"charge": [0.0], "database_cross_reference": ["cas:550-82-3",
    "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"],
    "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]},
    "synonyms": ["Resazurin"]}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[6]", "name": "Na2CO3", "primary": {"id": "CHEBI:29377",
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
    "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[7]", "name": "L-Cysteine HCl x H2O", "primary": {"id": "CHEBI:91248",
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
    "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field":
    "ingredients[8]", "name": "Nitrilotriacetic acid", "primary": {"id": "CHEBI:44557",
    "label": "nitrilotriacetic acid"}, "canonical_label": "nitrilotriacetic acid",
    "label_equal": true, "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["beilstein:1710776", "cas:139-13-9", "drugbank:DB03040", "gmelin:3726", "kegg.compound:C14695",
    "pdb-ccd:NTA"], "generalized_empirical_formula": ["C6H9NO6"], "has_alternative_id":
    ["CHEBI:34889", "CHEBI:44555"], "has_obo_namespace": ["chebi_ontology"], "id":
    ["CHEBI:44557"], "inchi_key_string": ["MGFYIUFZLHCRTH-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"],
    "mass": ["191.139"], "monoisotopic_mass": ["191.04299"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]},
    "synonyms": ["Complexon I", "H3nta", "Komplexon I", "N(CH2-COOH)3", "N,N-bis(carboxymethyl)glycine",
    "N,N-bis(carboxymethyl)glycine", "NITRILOTRIACETIC ACID", "NTA", "Nitrilotriacetate",
    "Nitrilotriacetic acid", "Nitrilotriessigsaeure", "Triglycollamic acid", "Trilon
    A", "alpha,alpha'',alpha''''-trimethylaminetricarboxylic acid", "nitrilo-2,2'',2''''-triacetic
    acid", "tri(carboxymethyl)amine", "triglycine"], "secondary": {"asserted": {"id":
    "CHEBI:44557", "label": "nitrilotriacetic acid"}, "exact_current_rows": [{"label":
    "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557",
    "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[9]", "name": "MnSO4 x H2O", "primary": {"id": "CHEBI:86364",
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
    "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field":
    "ingredients[10]", "name": "NaCl", "primary": {"id": "CHEBI:26710", "label": "sodium
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
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[11]", "name": "FeSO4 x 7 H2O", "primary": {"id": "CHEBI:75836",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[12]", "name": "CoSO4 x 7 H2O", "primary": {"id": "CHEBI:91244",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[13]", "name": "CaCl2 x 2 H2O", "primary": {"id": "CHEBI:86158",
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[14]", "name": "ZnSO4 x 7 H2O", "primary": {"id": "CHEBI:32312",
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
    {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[15]", "name": "CuSO4 x 5 H2O", "primary": {"id": "CHEBI:31440",
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
    "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[16]", "name": "AlK(SO4)2 x 12 H2O", "primary": {"id": "CHEBI:86465",
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
    "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[17]", "name": "H3BO3", "primary": {"id": "CHEBI:33118",
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
    "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[18]", "name": "Na2MoO4 x 2 H2O", "primary": {"id": "CHEBI:75213",
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
    {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[19]", "name": "NiCl2 x 6 H2O", "primary": {"id": "CHEBI:34887",
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
    "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[20]", "name": "Na2SeO3 x 5 H2O", "primary": {"id": "CHEBI:131361",
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
    "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[21]", "name": "Na2WO4 x 2 H2O", "primary": {"id": "CHEBI:63939",
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
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[22]", "name": "Biotin", "primary": {"id": "CHEBI:15956",
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
    "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field":
    "ingredients[23]", "name": "Folic acid", "primary": {"id": "CHEBI:27470", "label":
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
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[24]", "name": "Pyridoxine hydrochloride", "primary": {"id":
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
    "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field":
    "ingredients[25]", "name": "Thiamine HCl", "primary": {"id": "CHEBI:49105", "label":
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
    "MAPPED", "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[26]", "name": "Riboflavin", "primary": {"id": "CHEBI:17015",
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
    "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml", "field":
    "ingredients[27]", "name": "Nicotinic acid", "primary": {"id": "CHEBI:15940",
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
    "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[28]", "name": "Calcium D-(+)-pantothenate", "primary": {"id":
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
    "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[29]", "name": "Vitamin B12", "primary": {"id": "CHEBI:176843",
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
    {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[30]", "name": "p-Aminobenzoic acid", "primary": {"id": "CHEBI:30753",
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
    "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[31]", "name": "(DL)-alpha-Lipoic acid", "primary": {"id":
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
    "ambiguity": "unique"}]}}, {"layer": "owner-0", "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[32]", "name": "Syringic  acid", "primary": {"id": "CHEBI:68329",
    "label": "syringic acid"}, "canonical_label": "syringic acid", "label_equal":
    true, "definition": ["A dimethoxybenzene that is 3,5-dimethyl ether derivative
    of gallic acid."], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:530-57-4", "kegg.compound:C10833", "knapsack:C00002674", "lincs.smallmolecule:LSM-19009",
    "pubmed:21192716", "pubmed:21261296", "reaxys:2115262", "wikipedia.en:Syringic_acid"],
    "generalized_empirical_formula": ["C9H10O5"], "has_alternative_id": ["CHEBI:9379"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:68329"], "inchi_key_string":
    ["JMSVCTWVEWCHDZ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C9H10O5/c1-13-6-3-5(9(11)12)4-7(14-2)8(6)10/h3-4,10H,1-2H3,(H,11,12)"],
    "mass": ["198.174"], "monoisotopic_mass": ["198.05282"], "smiles_string": ["COc1cc(C(=O)O)cc(OC)c1O"]},
    "synonyms": ["4-hydroxy-3,5-dimethoxybenzoic acid", "4-hydroxy-3,5-dimethoxybenzoic
    acid", "Cedar acid", "Gallic acid 3,5-dimethyl ether"]}, {"layer": "owner-0",
    "path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field": "ingredients[33]", "name": "NaOH", "primary": {"id": "CHEBI:32145", "label":
    "sodium hydroxide"}, "canonical_label": "sodium hydroxide", "label_equal": true,
    "definition": [], "annotations": {"charge": [0.0], "database_cross_reference":
    ["cas:1310-73-2", "gmelin:68430", "kegg.compound:C12569", "kegg.drug:D01169"],
    "generalized_empirical_formula": ["HO.Na"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:32145"], "inchi_key_string": ["HEMHJVSKTPXQMS-UHFFFAOYSA-M"], "inchi_string":
    ["InChI=1S/Na.H2O/h;1H2/q+1;/p-1"], "mass": ["39.997"], "monoisotopic_mass": ["39.99251"],
    "smiles_string": ["[Na+].[OH-]"]}, "synonyms": ["Aetznatron", "NaOH", "Natriumhydroxid",
    "Sodium hydroxide", "caustic soda", "hydroxyde de sodium", "soda lye", "sodium
    hydrate", "sodium hydroxide", "sodium hydroxide", "soude caustique"], "secondary":
    {"asserted": {"id": "CHEBI:32145", "label": "sodium hydroxide"}, "exact_current_rows":
    [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145",
    "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}], "legacy": []}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _parse_api_solutions; _normalize_unit
  accessed_at: '2026-10-21T10:10:58Z'
  support: context_only
  summary: Current importer separates the primary recipe and stock additions, preserves
    solution IDs/attributes and maps ml as ML_PER_L. It does not validate the inherited
    flattened recipe; no historical replay was performed.
- evidence_id: cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-21T10:10:58Z'
  support: context_only
  summary: Current cleanup does not sum unequal duplicates. The actual local note
    documents 0.0994036 + 3.0 for magnesium across main and mineral-stock stages,
    requiring source-specific repair.
- evidence_id: grounding-writer
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: missing-grounding exactMatch application and append-only event
  accessed_at: '2026-10-21T10:10:58Z'
  support: context_only
  summary: Current writer adds a missing primary grounding while retaining existing
    groundings. The actual owner later event and term are inspected; the historical
    published mapping itself was not replayed. No export-absence inference is taken
    from an older script docstring.
- evidence_id: history
  kind: record_content
  reference: data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml
  locator: Every target and maintained owner history and ingredient curation timestamp
  accessed_at: '2026-10-21T10:10:58Z'
  support: supports
  summary: '[{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "curation_history[0].timestamp", "value": "2026-01-26T17:53:10.281602Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "curation_history[1].timestamp", "value": "2026-02-06T05:10:54.746247Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "curation_history[2].timestamp", "value": "2026-03-13T03:09:43.348143Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "curation_history[3].timestamp", "value": "2026-03-13T06:18:58.612636Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "curation_history[4].timestamp", "value": "2026-03-17T06:30:56.000000Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "curation_history[5].timestamp", "value": "2026-03-17T19:45:10.047663+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "curation_history[6].timestamp", "value": "2026-06-05T07:40:46.749673+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "curation_history[7].timestamp", "value": "2026-06-10T07:46:52.381517+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "curation_history[8].timestamp", "value": "2026-08-06T03:05:21.479289+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "curation_history[0].timestamp", "value": "2026-01-26T17:53:10.281602Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "curation_history[1].timestamp", "value": "2026-02-06T05:10:54.746247Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "curation_history[2].timestamp", "value": "2026-03-13T03:09:43.348143Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "curation_history[3].timestamp", "value": "2026-03-13T06:18:58.612636Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "curation_history[4].timestamp", "value": "2026-03-17T06:30:56.000000Z",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "curation_history[5].timestamp", "value": "2026-03-17T19:45:10.047663+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "curation_history[6].timestamp", "value": "2026-06-05T07:40:46.749673+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "curation_history[7].timestamp", "value": "2026-06-10T07:46:52.381517+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "curation_history[8].timestamp", "value": "2026-08-20T19:01:30.651337+00:00",
    "valid_ISO_datetime": true, "timezone_aware": true}]'
- evidence_id: merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger; merge_formulation_evidence; maintained formulation-aware
    merge context
  accessed_at: '2026-10-21T10:10:58Z'
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
  accessed_at: '2026-10-21T10:10:58Z'
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
  - CultureMech:000819
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact source identity and maintained owner
  outcome: supported
  summary: The target and sole normalized owner share CM000819 and DSMZ/MediaDive
    accession 135b. The exact primary and provider title agree with both. The generated
    merge explicitly names this owner; the later owner syringic-acid grounding is
    assessed separately. All current inspected input hashes match.
  target_ids:
  - CultureMech:000819
  evidence_ids:
  - record
  - owner-0
  - dsmz135b
  - mediadive135bapi
- assessment_id: relationships
  area: scope
  topic: Stock references and source-section boundaries
  outcome: concern
  summary: The source medium explicitly adds mineral stock 241, vitamin stock 5980
    and syringate stock 6318 at 20, 1 and 15 mL. Their complete definitions occur
    within the exact medium PDF and API. The parent-medium labels 141 and 120 identify
    the included mineral and vitamin sections; no whole parent basal medium is substituted.
    Neither local layer encodes solutions, parent_media, variant_children or a separate
    initial-versus-fed variant. The existing post-start feed is retained as an ordered
    instruction.
  target_ids:
  - CultureMech:000819
  evidence_ids:
  - record
  - owner-0
  - dsmz135b
  - mediadive135bapi
- assessment_id: grounding
  area: grounding
  topic: Primary labels/forms and pinned secondary correspondence
  outcome: supported
  summary: 'Layer-specific counts are {"target": {"ingredient_instances": 34, "primary_CHEBI_instances":
    32, "secondary_current_asserted_instances": 30, "secondary_current_verified_instances":
    30, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 94.12, "secondary_verified_percent":
    88.24}, "owner-0": {"ingredient_instances": 34, "primary_CHEBI_instances": 33,
    "secondary_current_asserted_instances": 30, "secondary_current_verified_instances":
    30, "legacy_secondary_instances": 0, "primary_CHEBI_percent": 97.06, "secondary_verified_percent":
    88.24}}. Percentages are 0–100 linkage coverage over direct ingredient instances,
    not scientific accuracy. The 0 legacy link instances across reviewed layers are
    unverified by the current CHEBI-keyed snapshot; absence here does not prove historical
    invalidity. Current secondary keys without a live preferred-term row are []. No
    secondary linked-set percentage is invented for an empty set.'
  target_ids:
  - CultureMech:000819
  evidence_ids:
  - record
  - owner-0
  - mim
  - chebi31206
  - chebi63036
  - chebi131527
  - chebi31795
  - chebi8806
  - chebi29377
  - chebi91248
  - chebi44557
  - chebi86364
  - chebi26710
  - chebi75836
  - chebi91244
  - chebi86158
  - chebi32312
  - chebi31440
  - chebi86465
  - chebi33118
  - chebi75213
  - chebi34887
  - chebi131361
  - chebi63939
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
  - chebi32145
  - chebi68329
  details: '{"label_drift": [], "legacy": [], "missing_current_secondary": []}'
- assessment_id: forms
  area: grounding
  topic: Exact supplied forms and salt preparation
  outcome: concern
  summary: Every asserted primary term resolves with its current canonical label.
    Nickel hexahydrate is nevertheless mapped to anhydrous CHEBI:34887, and sodium
    resazurin to sodium-free CHEBI:8806. The other explicit hydrate forms, including
    cysteine hydrochloride monohydrate, are supported at their stated scope. D-(+)-calcium
    pantothenate agrees with the D-specific CHEBI:31345 structure; generic CHEBI:16494
    has no selected stereochemistry contradicting source DL lipoic acid. Owner CHEBI:68329
    denotes the neutral syringic-acid precursor, not sodium syringate in the prepared
    stock. Vitamin B12 remains the source-level class without selecting a specific
    cobalamin. Yeast extract remains unresolved rather than receiving a guessed ID.
  target_ids:
  - CultureMech:000819
  evidence_ids:
  - record
  - owner-0
  - dsmz135b
  - chebi31206
  - chebi63036
  - chebi131527
  - chebi31795
  - chebi8806
  - chebi29377
  - chebi91248
  - chebi44557
  - chebi86364
  - chebi26710
  - chebi75836
  - chebi91244
  - chebi86158
  - chebi32312
  - chebi31440
  - chebi86465
  - chebi33118
  - chebi75213
  - chebi34887
  - chebi131361
  - chebi63939
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
  - chebi32145
  - chebi68329
- assessment_id: preparation
  area: consistency
  topic: Preserved process, explicit stock-version conflict and feed scope
  outcome: concern
  summary: All four preparation steps occur in both local layers. Main anoxic preparation,
    separate gas atmospheres, filtration of vitamins, final pH 7.4, mineral-stock
    pH 6.5 then 7.0, the after-growth final 2 g/L Na-syringate feed and stock 121
    °C sterilization are retained. The syringate dissolution text follows MediaDive
    700 mL/about pH 7.5 rather than the current DSMZ PDF 800 mL/about pH 7.0. Both
    retain makeup to 1000 mL and approximately 50 mL of 5 N NaOH. No source states
    the stock autoclave duration or all later addition volumes; no generic cycle or
    measured final volume is supplied.
  target_ids:
  - CultureMech:000819
  evidence_ids:
  - record
  - owner-0
  - dsmz135b
  - mediadive135bapi
  - provider-stock-preparation
- assessment_id: classification
  area: scope
  topic: Composition, physical state and application scope
  outcome: supported
  summary: COMPLEX/UNDEFINED agrees with explicit yeast extract and provider complex_medium=yes.
    LIQUID is consistent with this exact nongelled recipe. Bacterial filing and generic
    microbial cultivation are catalog-level descriptions; the name is not evidence
    for a taxon, strain, growth outcome or optima.
  target_ids:
  - CultureMech:000819
  evidence_ids:
  - record
  - owner-0
  - dsmz135b
  - mediadive135bapi
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp interpretation
  outcome: supported
  summary: 18 exact timestamp instances were examined; 0 lack valid syntax or explicit
    timezone. No local timestamp was assumed UTC or rewritten. Process and confidence
    annotations are not independent scientific evidence.
  target_ids:
  - CultureMech:000819
  evidence_ids:
  - record
  - owner-0
  - history
  details: '[]'
- assessment_id: quantities
  area: quantity
  topic: Every stored amount, stock dose and source-stage dependency
  outcome: concern
  summary: All 34 ingredient amounts in each local layer are traced to all 42 literal
    provider recipe rows and 16 explicit quantitative preparation or unquantified-dose
    decisions. Each has a native decision token, exact quote and locator, stage and
    rationale; arithmetic is separate. Main magnesium would contain 0.10 g + (3 g/L
    × 0.020 L) = 0.16 g before a receiving-volume division, not the local sum of concentrations.
    Main listed liquids total 1006.5 mL versus provider 1006 mL. Nominal syringate-stock
    60 g/L acid × 15 mL is 0.9 g acid precursor, distinct from the after-growth final
    2 g/L sodium salt condition. No measured final volume or exact feed volume is
    invented.
  target_ids:
  - CultureMech:000819
  evidence_ids:
  - record
  - owner-0
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
  - quantity-57
  - quantity-58
  details: '[{"field_path": "ingredients[0].concentration", "name": "NH4Cl", "current":
    {"value": "0.994036", "unit": "G_PER_L"}, "decision": "evidence_only", "source_key":
    "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.994036,\n                        \"mmol_l\":
    18.5836,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[0]", "preparation_stage": "Main sol. 135b (solution
    233, declared 1006 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1006 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-1", "arithmetic_separate_from_quote":
    "Original 1 g × 1 g/g ÷ (1006 mL / 1000 mL per L) = 0.9940357852882703777335984095
    g/L on the provider-declared stage volume; reported g_l is 0.994036. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "name": "NH4Cl", "current": {"value":
    "0.994036", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[0].concentration", "name": "NH4Cl", "current": {"value":
    "0.994036", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 0.994036, "provider_stage_volume_ml": 1006, "primary_source_evidence_id":
    "dsmz135b"}, {"field_path": "ingredients[1].concentration", "name": "KH2PO4",
    "current": {"value": "0.328032", "unit": "G_PER_L"}, "decision": "evidence_only",
    "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.328032,\n                        \"mmol_l\":
    2.41049,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[1]", "preparation_stage": "Main sol. 135b (solution
    233, declared 1006 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1006 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-2", "arithmetic_separate_from_quote":
    "Original 0.33 g × 1 g/g ÷ (1006 mL / 1000 mL per L) = 0.3280318091451292246520874751
    g/L on the provider-declared stage volume; reported g_l is 0.328032. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "name": "KH2PO4", "current": {"value":
    "0.328032", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[1].concentration", "name": "KH2PO4", "current": {"value":
    "0.328032", "unit": "G_PER_L"}}], "source_amount": 0.33, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 0.328032, "provider_stage_volume_ml": 1006, "primary_source_evidence_id":
    "dsmz135b"}, {"field_path": "ingredients[2].concentration", "name": "K2HPO4",
    "current": {"value": "0.447316", "unit": "G_PER_L"}, "decision": "evidence_only",
    "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.45,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.447316,\n                        \"mmol_l\":
    2.56818,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[2]", "preparation_stage": "Main sol. 135b (solution
    233, declared 1006 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1006 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-3", "arithmetic_separate_from_quote":
    "Original 0.45 g × 1 g/g ÷ (1006 mL / 1000 mL per L) = 0.4473161033797216699801192843
    g/L on the provider-declared stage volume; reported g_l is 0.447316. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "name": "K2HPO4", "current": {"value":
    "0.447316", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[2].concentration", "name": "K2HPO4", "current": {"value":
    "0.447316", "unit": "G_PER_L"}}], "source_amount": 0.45, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 0.447316, "provider_stage_volume_ml": 1006, "primary_source_evidence_id":
    "dsmz135b"}, {"field_path": "ingredients[3].concentration", "name": "MgSO4 x 7
    H2O", "current": {"value": "3.0994036", "unit": "G_PER_L"}, "decision": "correct",
    "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0994036,\n                        \"mmol_l\":
    0.403299,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[3]", "preparation_stage": "Main sol. 135b (solution
    233, declared 1006 mL)", "decision_rationale": "This is a stock composition or
    a direct contribution currently combined with a stock value. Preserve original
    batch amount, exact source form and stock stage; do not use this stock strength
    as a direct final-medium concentration.", "evidence_id": "quantity-4", "arithmetic_separate_from_quote":
    "Original 0.1 g × 1 g/g ÷ (1006 mL / 1000 mL per L) = 0.09940357852882703777335984095
    g/L on the provider-declared stage volume; reported g_l is 0.0994036. This is
    not a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "name": "MgSO4 x 7 H2O", "current":
    {"value": "3.0994036", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[3].concentration", "name": "MgSO4 x 7 H2O", "current":
    {"value": "3.0994036", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.0994036, "provider_stage_volume_ml":
    1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "source solution
    233 recipe[4] (not represented)", "name": "Modified Wolin''s mineral solution",
    "current": null, "decision": "add", "source_key": "mediadive135bapi", "source_quote":
    "{\n                        \"recipe_order\": 5,\n                        \"solution\":
    \"Modified Wolin''s mineral solution\",\n                        \"solution_id\":
    241,\n                        \"amount\": 20,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[4]", "preparation_stage": "Main sol. 135b (solution
    233, declared 1006 mL)", "decision_rationale": "The main recipe explicitly adds
    20 ml of stock 241. Restore this dose and the separate stock definition; the stored
    flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-5",
    "affected_local_fields": [], "source_amount": 20, "source_unit": "ml", "source_attribute":
    null, "provider_g_l": null, "provider_stage_volume_ml": 1006, "primary_source_evidence_id":
    "dsmz135b"}, {"field_path": "ingredients[4].concentration", "name": "Yeast extract",
    "current": {"value": "1.98807", "unit": "G_PER_L"}, "decision": "evidence_only",
    "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.98807,\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[0].recipe[5]",
    "preparation_stage": "Main sol. 135b (solution 233, declared 1006 mL)", "decision_rationale":
    "The current value follows provider g_l on its declared 1006 mL basis. Attach
    exact source evidence and retain any percentage-stock attribute and dose. This
    is provider normalization, not an independently measured final volume.", "evidence_id":
    "quantity-6", "arithmetic_separate_from_quote": "Original 2 g × 1 g/g ÷ (1006
    mL / 1000 mL per L) = 1.988071570576540755467196819 g/L on the provider-declared
    stage volume; reported g_l is 1.98807. This is not a receiving-medium dilution.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "name": "Yeast extract", "current":
    {"value": "1.98807", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[4].concentration", "name": "Yeast extract", "current":
    {"value": "1.98807", "unit": "G_PER_L"}}], "source_amount": 2, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 1.98807, "provider_stage_volume_ml":
    1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[5].concentration",
    "name": "Sodium resazurin", "current": {"value": "0.000497018", "unit": "G_PER_L"},
    "decision": "evidence_only", "source_key": "mediadive135bapi", "source_quote":
    "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.000497018,\n                        \"mmol_l\":
    0.00197881,\n                        \"optional\": 0\n                    }",
    "source_locator": "$.data.solutions[0].recipe[6]", "preparation_stage": "Main
    sol. 135b (solution 233, declared 1006 mL)", "decision_rationale": "The current
    value follows provider g_l on its declared 1006 mL basis. Attach exact source
    evidence and retain any percentage-stock attribute and dose. This is provider
    normalization, not an independently measured final volume.", "evidence_id": "quantity-7",
    "arithmetic_separate_from_quote": "0.1% w/v means 0.1 g per 100 mL; 0.5 mL contains
    0.0005 g. Dividing by provider-declared 1006/1000 L gives 0.0004970178926441351888667992048
    g/L; reported g_l is 0.000497018. Preserve this source stock dose separately.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "name": "Sodium resazurin", "current":
    {"value": "0.000497018", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[5].concentration", "name": "Sodium resazurin", "current":
    {"value": "0.000497018", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit":
    "ml", "source_attribute": "0.1% w/v", "provider_g_l": 0.000497018, "provider_stage_volume_ml":
    1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[6].concentration",
    "name": "Na2CO3", "current": {"value": "1.49105", "unit": "G_PER_L"}, "decision":
    "evidence_only", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.49105,\n                        \"mmol_l\":
    14.0681,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[7]", "preparation_stage": "Main sol. 135b (solution
    233, declared 1006 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1006 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-8", "arithmetic_separate_from_quote":
    "Original 1.5 g × 1 g/g ÷ (1006 mL / 1000 mL per L) = 1.491053677932405566600397614
    g/L on the provider-declared stage volume; reported g_l is 1.49105. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "name": "Na2CO3", "current": {"value":
    "1.49105", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[6].concentration", "name": "Na2CO3", "current": {"value":
    "1.49105", "unit": "G_PER_L"}}], "source_amount": 1.5, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 1.49105, "provider_stage_volume_ml": 1006, "primary_source_evidence_id":
    "dsmz135b"}, {"field_path": "source solution 233 recipe[8] (not represented)",
    "name": "Na-syringate solution (0.3 M)", "current": null, "decision": "add", "source_key":
    "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Na-syringate solution (0.3 M)\",\n                        \"solution_id\":
    6318,\n                        \"amount\": 15,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[8]", "preparation_stage": "Main sol. 135b (solution
    233, declared 1006 mL)", "decision_rationale": "The main recipe explicitly adds
    15 ml of stock 6318. Restore this dose and the separate stock definition; the
    stored flat ingredient strengths do not encode its dilution.", "evidence_id":
    "quantity-9", "affected_local_fields": [], "source_amount": 15, "source_unit":
    "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml":
    1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "source solution
    233 recipe[9] (not represented)", "name": "Wolin''s vitamin solution (10x)", "current":
    null, "decision": "add", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[9]", "preparation_stage": "Main sol. 135b (solution
    233, declared 1006 mL)", "decision_rationale": "The main recipe explicitly adds
    1 ml of stock 5980. Restore this dose and the separate stock definition; the stored
    flat ingredient strengths do not encode its dilution.", "evidence_id": "quantity-10",
    "affected_local_fields": [], "source_amount": 1, "source_unit": "ml", "source_attribute":
    null, "provider_g_l": null, "provider_stage_volume_ml": 1006, "primary_source_evidence_id":
    "dsmz135b"}, {"field_path": "ingredients[7].concentration", "name": "L-Cysteine
    HCl x H2O", "current": {"value": "0.497018", "unit": "G_PER_L"}, "decision": "evidence_only",
    "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\":
    770,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.497018,\n                        \"mmol_l\":
    2.82982,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[10]", "preparation_stage": "Main sol. 135b (solution
    233, declared 1006 mL)", "decision_rationale": "The current value follows provider
    g_l on its declared 1006 mL basis. Attach exact source evidence and retain any
    percentage-stock attribute and dose. This is provider normalization, not an independently
    measured final volume.", "evidence_id": "quantity-11", "arithmetic_separate_from_quote":
    "Original 0.5 g × 1 g/g ÷ (1006 mL / 1000 mL per L) = 0.4970178926441351888667992048
    g/L on the provider-declared stage volume; reported g_l is 0.497018. This is not
    a receiving-medium dilution.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "name": "L-Cysteine HCl x H2O",
    "current": {"value": "0.497018", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[7].concentration", "name": "L-Cysteine HCl x H2O",
    "current": {"value": "0.497018", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.497018, "provider_stage_volume_ml":
    1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "source solution
    233 recipe[11] (not represented)", "name": "Distilled water", "current": null,
    "decision": "add", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 970,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[0].recipe[11]", "preparation_stage": "Main sol. 135b (solution
    233, declared 1006 mL)", "decision_rationale": "Preserve the source solvent quantity
    970 ml in its own stage. The provider declares this solution volume as 1006 mL;
    water addition is not independent proof of measured final volume.", "evidence_id":
    "quantity-12", "affected_local_fields": [], "source_amount": 970, "source_unit":
    "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml":
    1006, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[8].concentration",
    "name": "Nitrilotriacetic acid", "current": {"value": "1.5", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\":
    189,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.84765,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[0]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-13",
    "arithmetic_separate_from_quote": "Original 1.5 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 1.5 g/L on the provider-declared stage volume; reported g_l is 1.5. This
    is not a receiving-medium dilution. Conditional stock contribution: 1.5 g/L stock
    × 0.020 L / 1.006 L = 0.02982107355864811133200795229 g/L on the provider basis
    only. For syringic acid this is acid-precursor mass accounting, not proof of final
    sodium-syringate concentration. Do not encode both stock addition and expanded
    constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "name": "Nitrilotriacetic acid",
    "current": {"value": "1.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[8].concentration", "name": "Nitrilotriacetic acid",
    "current": {"value": "1.5", "unit": "G_PER_L"}}], "source_amount": 1.5, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 1.5, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[3].concentration",
    "name": "MgSO4 x 7 H2O", "current": {"value": "3.0994036", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    12.1716,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[1]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-14",
    "arithmetic_separate_from_quote": "Original 3 g × 1 g/g ÷ (1000 mL / 1000 mL per
    L) = 3 g/L on the provider-declared stage volume; reported g_l is 3. This is not
    a receiving-medium dilution. Conditional stock contribution: 3 g/L stock × 0.020
    L / 1.006 L = 0.05964214711729622266401590457 g/L on the provider basis only.
    For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate
    concentration. Do not encode both stock addition and expanded constituents.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "name": "MgSO4 x 7 H2O", "current":
    {"value": "3.0994036", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[3].concentration", "name": "MgSO4 x 7 H2O", "current":
    {"value": "3.0994036", "unit": "G_PER_L"}}], "source_amount": 3, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 3, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[9].concentration",
    "name": "MnSO4 x H2O", "current": {"value": "0.5", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\":
    14,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.9583,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[2]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-15",
    "arithmetic_separate_from_quote": "Original 0.5 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.5 g/L on the provider-declared stage volume; reported g_l is 0.5. This
    is not a receiving-medium dilution. Conditional stock contribution: 0.5 g/L stock
    × 0.020 L / 1.006 L = 0.009940357852882703777335984095 g/L on the provider basis
    only. For syringic acid this is acid-precursor mass accounting, not proof of final
    sodium-syringate concentration. Do not encode both stock addition and expanded
    constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "name": "MnSO4 x H2O", "current":
    {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[9].concentration", "name": "MnSO4 x H2O", "current":
    {"value": "0.5", "unit": "G_PER_L"}}], "source_amount": 0.5, "source_unit": "g",
    "source_attribute": null, "provider_g_l": 0.5, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[10].concentration",
    "name": "NaCl", "current": {"value": "1", "unit": "G_PER_L"}, "decision": "correct",
    "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    17.1116,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[3]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-16",
    "arithmetic_separate_from_quote": "Original 1 g × 1 g/g ÷ (1000 mL / 1000 mL per
    L) = 1 g/L on the provider-declared stage volume; reported g_l is 1. This is not
    a receiving-medium dilution. Conditional stock contribution: 1 g/L stock × 0.020
    L / 1.006 L = 0.01988071570576540755467196819 g/L on the provider basis only.
    For syringic acid this is acid-precursor mass accounting, not proof of final sodium-syringate
    concentration. Do not encode both stock addition and expanded constituents.",
    "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "name": "NaCl", "current": {"value":
    "1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[10].concentration", "name": "NaCl", "current": {"value":
    "1", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 1, "provider_stage_volume_ml": 1000, "primary_source_evidence_id":
    "dsmz135b"}, {"field_path": "ingredients[11].concentration", "name": "FeSO4 x
    7 H2O", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct",
    "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.359693,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[4]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-17",
    "arithmetic_separate_from_quote": "Original 0.1 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.1 g/L on the provider-declared stage volume; reported g_l is 0.1. This
    is not a receiving-medium dilution. Conditional stock contribution: 0.1 g/L stock
    × 0.020 L / 1.006 L = 0.001988071570576540755467196819 g/L on the provider basis
    only. For syringic acid this is acid-precursor mass accounting, not proof of final
    sodium-syringate concentration. Do not encode both stock addition and expanded
    constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "name": "FeSO4 x 7 H2O", "current":
    {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[11].concentration", "name": "FeSO4 x 7 H2O", "current":
    {"value": "0.1", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit": "g",
    "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[12].concentration",
    "name": "CoSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\":
    198,\n                        \"amount\": 0.18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\":
    1.16132,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[5]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-18",
    "arithmetic_separate_from_quote": "Original 0.18 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.18 g/L on the provider-declared stage volume; reported g_l is 0.18.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.18
    g/L stock × 0.020 L / 1.006 L = 0.003578528827037773359840954274 g/L on the provider
    basis only. For syringic acid this is acid-precursor mass accounting, not proof
    of final sodium-syringate concentration. Do not encode both stock addition and
    expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "name": "CoSO4 x 7 H2O", "current":
    {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[12].concentration", "name": "CoSO4 x 7 H2O", "current":
    {"value": "0.18", "unit": "G_PER_L"}}], "source_amount": 0.18, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.18, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[13].concentration",
    "name": "CaCl2 x 2 H2O", "current": {"value": "0.1", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.680203,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[6]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-19",
    "arithmetic_separate_from_quote": "Original 0.1 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.1 g/L on the provider-declared stage volume; reported g_l is 0.1. This
    is not a receiving-medium dilution. Conditional stock contribution: 0.1 g/L stock
    × 0.020 L / 1.006 L = 0.001988071570576540755467196819 g/L on the provider basis
    only. For syringic acid this is acid-precursor mass accounting, not proof of final
    sodium-syringate concentration. Do not encode both stock addition and expanded
    constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "name": "CaCl2 x 2 H2O", "current":
    {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[13].concentration", "name": "CaCl2 x 2 H2O", "current":
    {"value": "0.1", "unit": "G_PER_L"}}], "source_amount": 0.1, "source_unit": "g",
    "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[14].concentration",
    "name": "ZnSO4 x 7 H2O", "current": {"value": "0.18", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 0.18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\":
    0.625954,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[7]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-20",
    "arithmetic_separate_from_quote": "Original 0.18 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.18 g/L on the provider-declared stage volume; reported g_l is 0.18.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.18
    g/L stock × 0.020 L / 1.006 L = 0.003578528827037773359840954274 g/L on the provider
    basis only. For syringic acid this is acid-precursor mass accounting, not proof
    of final sodium-syringate concentration. Do not encode both stock addition and
    expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "name": "ZnSO4 x 7 H2O", "current":
    {"value": "0.18", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[14].concentration", "name": "ZnSO4 x 7 H2O", "current":
    {"value": "0.18", "unit": "G_PER_L"}}], "source_amount": 0.18, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.18, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[15].concentration",
    "name": "CuSO4 x 5 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\":
    121,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0400503,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[8]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-21",
    "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.01
    g/L stock × 0.020 L / 1.006 L = 0.0001988071570576540755467196819 g/L on the provider
    basis only. For syringic acid this is acid-precursor mass accounting, not proof
    of final sodium-syringate concentration. Do not encode both stock addition and
    expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "name": "CuSO4 x 5 H2O", "current":
    {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[15].concentration", "name": "CuSO4 x 5 H2O", "current":
    {"value": "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.01, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[16].concentration",
    "name": "AlK(SO4)2 x 12 H2O", "current": {"value": "0.02", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\":
    908,\n                        \"amount\": 0.02,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0421596,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[9]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-22",
    "arithmetic_separate_from_quote": "Original 0.02 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.02 g/L on the provider-declared stage volume; reported g_l is 0.02.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.02
    g/L stock × 0.020 L / 1.006 L = 0.0003976143141153081510934393638 g/L on the provider
    basis only. For syringic acid this is acid-precursor mass accounting, not proof
    of final sodium-syringate concentration. Do not encode both stock addition and
    expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "name": "AlK(SO4)2 x 12 H2O", "current":
    {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[16].concentration", "name": "AlK(SO4)2 x 12 H2O", "current":
    {"value": "0.02", "unit": "G_PER_L"}}], "source_amount": 0.02, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.02, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[17].concentration",
    "name": "H3BO3", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.161708,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[10]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-23",
    "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.01
    g/L stock × 0.020 L / 1.006 L = 0.0001988071570576540755467196819 g/L on the provider
    basis only. For syringic acid this is acid-precursor mass accounting, not proof
    of final sodium-syringate concentration. Do not encode both stock addition and
    expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "name": "H3BO3", "current": {"value":
    "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[17].concentration", "name": "H3BO3", "current": {"value":
    "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit": "g", "source_attribute":
    null, "provider_g_l": 0.01, "provider_stage_volume_ml": 1000, "primary_source_evidence_id":
    "dsmz135b"}, {"field_path": "ingredients[18].concentration", "name": "Na2MoO4
    x 2 H2O", "current": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct",
    "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0413309,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[11]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-24",
    "arithmetic_separate_from_quote": "Original 0.01 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.01 g/L on the provider-declared stage volume; reported g_l is 0.01.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.01
    g/L stock × 0.020 L / 1.006 L = 0.0001988071570576540755467196819 g/L on the provider
    basis only. For syringic acid this is acid-precursor mass accounting, not proof
    of final sodium-syringate concentration. Do not encode both stock addition and
    expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "name": "Na2MoO4 x 2 H2O", "current":
    {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[18].concentration", "name": "Na2MoO4 x 2 H2O", "current":
    {"value": "0.01", "unit": "G_PER_L"}}], "source_amount": 0.01, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.01, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[19].concentration",
    "name": "NiCl2 x 6 H2O", "current": {"value": "0.03", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.231483,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[12]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-25",
    "arithmetic_separate_from_quote": "Original 0.03 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 0.03 g/L on the provider-declared stage volume; reported g_l is 0.03.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.03
    g/L stock × 0.020 L / 1.006 L = 0.0005964214711729622266401590457 g/L on the provider
    basis only. For syringic acid this is acid-precursor mass accounting, not proof
    of final sodium-syringate concentration. Do not encode both stock addition and
    expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[19].concentration", "name": "NiCl2 x 6 H2O", "current":
    {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[19].concentration", "name": "NiCl2 x 6 H2O", "current":
    {"value": "0.03", "unit": "G_PER_L"}}], "source_amount": 0.03, "source_unit":
    "g", "source_attribute": null, "provider_g_l": 0.03, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[20].concentration",
    "name": "Na2SeO3 x 5 H2O", "current": {"value": "0.0003", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\":
    0.00114062,\n                        \"optional\": 0\n                    }",
    "source_locator": "$.data.solutions[1].recipe[13]", "preparation_stage": "Modified
    Wolin''s mineral solution (solution 241, declared 1000 mL)", "decision_rationale":
    "This is a stock composition or a direct contribution currently combined with
    a stock value. Preserve original batch amount, exact source form and stock stage;
    do not use this stock strength as a direct final-medium concentration.", "evidence_id":
    "quantity-26", "arithmetic_separate_from_quote": "Original 0.3 mg × 0.001 g/mg
    ÷ (1000 mL / 1000 mL per L) = 0.0003 g/L on the provider-declared stage volume;
    reported g_l is 0.0003. This is not a receiving-medium dilution. Conditional stock
    contribution: 0.0003 g/L stock × 0.020 L / 1.006 L = 0.000005964214711729622266401590457
    g/L on the provider basis only. For syringic acid this is acid-precursor mass
    accounting, not proof of final sodium-syringate concentration. Do not encode both
    stock addition and expanded constituents.", "affected_local_fields": [{"path":
    "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path":
    "ingredients[20].concentration", "name": "Na2SeO3 x 5 H2O", "current": {"value":
    "0.0003", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[20].concentration", "name": "Na2SeO3 x 5 H2O", "current":
    {"value": "0.0003", "unit": "G_PER_L"}}], "source_amount": 0.3, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.0003, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[21].concentration",
    "name": "Na2WO4 x 2 H2O", "current": {"value": "0.0004", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\":
    0.00121267,\n                        \"optional\": 0\n                    }",
    "source_locator": "$.data.solutions[1].recipe[14]", "preparation_stage": "Modified
    Wolin''s mineral solution (solution 241, declared 1000 mL)", "decision_rationale":
    "This is a stock composition or a direct contribution currently combined with
    a stock value. Preserve original batch amount, exact source form and stock stage;
    do not use this stock strength as a direct final-medium concentration.", "evidence_id":
    "quantity-27", "arithmetic_separate_from_quote": "Original 0.4 mg × 0.001 g/mg
    ÷ (1000 mL / 1000 mL per L) = 0.0004 g/L on the provider-declared stage volume;
    reported g_l is 0.0004. This is not a receiving-medium dilution. Conditional stock
    contribution: 0.0004 g/L stock × 0.020 L / 1.006 L = 0.000007952286282306163021868787276
    g/L on the provider basis only. For syringic acid this is acid-precursor mass
    accounting, not proof of final sodium-syringate concentration. Do not encode both
    stock addition and expanded constituents.", "affected_local_fields": [{"path":
    "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml", "field_path":
    "ingredients[21].concentration", "name": "Na2WO4 x 2 H2O", "current": {"value":
    "0.0004", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[21].concentration", "name": "Na2WO4 x 2 H2O", "current":
    {"value": "0.0004", "unit": "G_PER_L"}}], "source_amount": 0.4, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.0004, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "source solution
    241 recipe[15] (not represented)", "name": "Distilled water", "current": null,
    "decision": "add", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[1].recipe[15]", "preparation_stage": "Modified Wolin''s mineral
    solution (solution 241, declared 1000 mL)", "decision_rationale": "Preserve the
    source solvent quantity 1000 ml in its own stage. The provider declares this solution
    volume as 1000 mL; water addition is not independent proof of measured final volume.",
    "evidence_id": "quantity-28", "affected_local_fields": [], "source_amount": 1000,
    "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[22].concentration",
    "name": "Biotin", "current": {"value": "0.02", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[0]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-29",
    "arithmetic_separate_from_quote": "Original 20 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.020 g/L on the provider-declared stage volume; reported g_l is 0.02.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.02
    g/L stock × 0.001 L / 1.006 L = 0.00001988071570576540755467196819 g/L on the
    provider basis only. For syringic acid this is acid-precursor mass accounting,
    not proof of final sodium-syringate concentration. Do not encode both stock addition
    and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "name": "Biotin", "current": {"value":
    "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[22].concentration", "name": "Biotin", "current": {"value":
    "0.02", "unit": "G_PER_L"}}], "source_amount": 20, "source_unit": "mg", "source_attribute":
    null, "provider_g_l": 0.02, "provider_stage_volume_ml": 1000, "primary_source_evidence_id":
    "dsmz135b"}, {"field_path": "ingredients[23].concentration", "name": "Folic acid",
    "current": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "source_key":
    "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[1]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-30",
    "arithmetic_separate_from_quote": "Original 20 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.020 g/L on the provider-declared stage volume; reported g_l is 0.02.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.02
    g/L stock × 0.001 L / 1.006 L = 0.00001988071570576540755467196819 g/L on the
    provider basis only. For syringic acid this is acid-precursor mass accounting,
    not proof of final sodium-syringate concentration. Do not encode both stock addition
    and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[23].concentration", "name": "Folic acid", "current":
    {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[23].concentration", "name": "Folic acid", "current":
    {"value": "0.02", "unit": "G_PER_L"}}], "source_amount": 20, "source_unit": "mg",
    "source_attribute": null, "provider_g_l": 0.02, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[24].concentration",
    "name": "Pyridoxine hydrochloride", "current": {"value": "0.1", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[2]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-31",
    "arithmetic_separate_from_quote": "Original 100 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.100 g/L on the provider-declared stage volume; reported g_l is 0.1.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.1 g/L
    stock × 0.001 L / 1.006 L = 0.00009940357852882703777335984095 g/L on the provider
    basis only. For syringic acid this is acid-precursor mass accounting, not proof
    of final sodium-syringate concentration. Do not encode both stock addition and
    expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[24].concentration", "name": "Pyridoxine hydrochloride",
    "current": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[24].concentration", "name": "Pyridoxine hydrochloride",
    "current": {"value": "0.1", "unit": "G_PER_L"}}], "source_amount": 100, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.1, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[25].concentration",
    "name": "Thiamine HCl", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[3]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-32",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.05
    g/L stock × 0.001 L / 1.006 L = 0.00004970178926441351888667992048 g/L on the
    provider basis only. For syringic acid this is acid-precursor mass accounting,
    not proof of final sodium-syringate concentration. Do not encode both stock addition
    and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[25].concentration", "name": "Thiamine HCl", "current":
    {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[25].concentration", "name": "Thiamine HCl", "current":
    {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg",
    "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[26].concentration",
    "name": "Riboflavin", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[4]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-33",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.05
    g/L stock × 0.001 L / 1.006 L = 0.00004970178926441351888667992048 g/L on the
    provider basis only. For syringic acid this is acid-precursor mass accounting,
    not proof of final sodium-syringate concentration. Do not encode both stock addition
    and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "name": "Riboflavin", "current":
    {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[26].concentration", "name": "Riboflavin", "current":
    {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg",
    "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[27].concentration",
    "name": "Nicotinic acid", "current": {"value": "0.05", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[5]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-34",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.05
    g/L stock × 0.001 L / 1.006 L = 0.00004970178926441351888667992048 g/L on the
    provider basis only. For syringic acid this is acid-precursor mass accounting,
    not proof of final sodium-syringate concentration. Do not encode both stock addition
    and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[27].concentration", "name": "Nicotinic acid", "current":
    {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[27].concentration", "name": "Nicotinic acid", "current":
    {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "mg",
    "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[28].concentration",
    "name": "Calcium D-(+)-pantothenate", "current": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[6]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-35",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.05
    g/L stock × 0.001 L / 1.006 L = 0.00004970178926441351888667992048 g/L on the
    provider basis only. For syringic acid this is acid-precursor mass accounting,
    not proof of final sodium-syringate concentration. Do not encode both stock addition
    and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[28].concentration", "name": "Calcium D-(+)-pantothenate",
    "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[28].concentration", "name": "Calcium D-(+)-pantothenate",
    "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[29].concentration",
    "name": "Vitamin B12", "current": {"value": "0.001", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }",
    "source_locator": "$.data.solutions[2].recipe[7]", "preparation_stage": "Wolin''s
    vitamin solution (10x) (solution 5980, declared 1000 mL)", "decision_rationale":
    "This is a stock composition or a direct contribution currently combined with
    a stock value. Preserve original batch amount, exact source form and stock stage;
    do not use this stock strength as a direct final-medium concentration.", "evidence_id":
    "quantity-36", "arithmetic_separate_from_quote": "Original 1 mg × 0.001 g/mg ÷
    (1000 mL / 1000 mL per L) = 0.001 g/L on the provider-declared stage volume; reported
    g_l is 0.001. This is not a receiving-medium dilution. Conditional stock contribution:
    0.001 g/L stock × 0.001 L / 1.006 L = 9.940357852882703777335984095E-7 g/L on
    the provider basis only. For syringic acid this is acid-precursor mass accounting,
    not proof of final sodium-syringate concentration. Do not encode both stock addition
    and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[29].concentration", "name": "Vitamin B12", "current":
    {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[29].concentration", "name": "Vitamin B12", "current":
    {"value": "0.001", "unit": "G_PER_L"}}], "source_amount": 1, "source_unit": "mg",
    "source_attribute": null, "provider_g_l": 0.001, "provider_stage_volume_ml": 1000,
    "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[30].concentration",
    "name": "p-Aminobenzoic acid", "current": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[8]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-37",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.05
    g/L stock × 0.001 L / 1.006 L = 0.00004970178926441351888667992048 g/L on the
    provider basis only. For syringic acid this is acid-precursor mass accounting,
    not proof of final sodium-syringate concentration. Do not encode both stock addition
    and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[30].concentration", "name": "p-Aminobenzoic acid",
    "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[30].concentration", "name": "p-Aminobenzoic acid",
    "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[31].concentration",
    "name": "(DL)-alpha-Lipoic acid", "current": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[9]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-38",
    "arithmetic_separate_from_quote": "Original 50 mg × 0.001 g/mg ÷ (1000 mL / 1000
    mL per L) = 0.050 g/L on the provider-declared stage volume; reported g_l is 0.05.
    This is not a receiving-medium dilution. Conditional stock contribution: 0.05
    g/L stock × 0.001 L / 1.006 L = 0.00004970178926441351888667992048 g/L on the
    provider basis only. For syringic acid this is acid-precursor mass accounting,
    not proof of final sodium-syringate concentration. Do not encode both stock addition
    and expanded constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[31].concentration", "name": "(DL)-alpha-Lipoic acid",
    "current": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[31].concentration", "name": "(DL)-alpha-Lipoic acid",
    "current": {"value": "0.05", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit":
    "mg", "source_attribute": null, "provider_g_l": 0.05, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "source solution
    5980 recipe[10] (not represented)", "name": "Distilled water", "current": null,
    "decision": "add", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[2].recipe[10]", "preparation_stage": "Wolin''s vitamin solution
    (10x) (solution 5980, declared 1000 mL)", "decision_rationale": "Preserve the
    source solvent quantity 1000 ml in its own stage. The provider declares this solution
    volume as 1000 mL; water addition is not independent proof of measured final volume.",
    "evidence_id": "quantity-39", "affected_local_fields": [], "source_amount": 1000,
    "source_unit": "ml", "source_attribute": null, "provider_g_l": null, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[32].concentration",
    "name": "Syringic  acid", "current": {"value": "60", "unit": "G_PER_L"}, "decision":
    "correct", "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Syringic  acid\",\n                        \"compound_id\":
    2124,\n                        \"attribute\": \"SIGMA S6881\",\n                        \"amount\":
    60,\n                        \"unit\": \"g\",\n                        \"g_l\":
    60,\n                        \"optional\": 0\n                    }", "source_locator":
    "$.data.solutions[3].recipe[0]", "preparation_stage": "Na-syringate solution (0.3
    M) (solution 6318, declared 1000 mL)", "decision_rationale": "This is a stock
    composition or a direct contribution currently combined with a stock value. Preserve
    original batch amount, exact source form and stock stage; do not use this stock
    strength as a direct final-medium concentration.", "evidence_id": "quantity-40",
    "arithmetic_separate_from_quote": "Original 60 g × 1 g/g ÷ (1000 mL / 1000 mL
    per L) = 60 g/L on the provider-declared stage volume; reported g_l is 60. This
    is not a receiving-medium dilution. Conditional stock contribution: 60 g/L stock
    × 0.015 L / 1.006 L = 0.8946322067594433399602385686 g/L on the provider basis
    only. For syringic acid this is acid-precursor mass accounting, not proof of final
    sodium-syringate concentration. Do not encode both stock addition and expanded
    constituents.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[32].concentration", "name": "Syringic  acid", "current":
    {"value": "60", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[32].concentration", "name": "Syringic  acid", "current":
    {"value": "60", "unit": "G_PER_L"}}], "source_amount": 60, "source_unit": "g",
    "source_attribute": "SIGMA S6881", "provider_g_l": 60, "provider_stage_volume_ml":
    1000, "primary_source_evidence_id": "dsmz135b"}, {"field_path": "ingredients[33].concentration",
    "name": "NaOH", "current": {"value": "50", "unit": "G_PER_L"}, "decision": "correct",
    "source_key": "mediadive135bapi", "source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\":
    256,\n                        \"attribute\": \"5 N\",\n                        \"amount\":
    50,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[3].recipe[1]",
    "preparation_stage": "Na-syringate solution (0.3 M) (solution 6318, declared 1000
    mL)", "decision_rationale": "The row specifies 50 mL of 5 N NaOH in the syringate
    stock, not 50 g/L direct NaOH. Preserve normality, liquid dose, titration qualifier
    and stock stage. Both source preparations describe about/around 50 mL, so no exact
    endpoint-dependent mass is asserted.", "evidence_id": "quantity-41", "arithmetic_separate_from_quote":
    "For monobasic NaOH, a nominal 50 mL of 5 equivalents/L contains 0.25 mol; using
    captured CHEBI:32145 mass 39.997 g/mol gives 9.99925 g before dilution or reaction,
    not 50 g. This conditional illustration is not a replacement stock recipe or a
    measured final concentration.", "affected_local_fields": [{"path": "data/merge_yaml/merged/ACETOBACTERIUM_DEHALOGENANS_MEDIUM.yaml",
    "field_path": "ingredients[33].concentration", "name": "NaOH", "current": {"value":
    "50", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml",
    "field_path": "ingredients[33].concentration", "name": "NaOH", "current": {"value":
    "50", "unit": "G_PER_L"}}], "source_amount": 50, "source_unit": "ml", "source_attribute":
    "5 N", "provider_g_l": null, "provider_stage_volume_ml": 1000, "primary_source_evidence_id":
    "dsmz135b"}, {"field_path": "source solution 6318 recipe[2] (not represented)",
    "name": "Distilled water", "current": null, "decision": "add", "source_key": "mediadive135bapi",
    "source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    950,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "source_locator": "$.data.solutions[3].recipe[2]",
    "preparation_stage": "Na-syringate solution (0.3 M) (solution 6318, declared 1000
    mL)", "decision_rationale": "Preserve the source solvent quantity 950 ml in its
    own stage. The provider declares this solution volume as 1000 mL; water addition
    is not independent proof of measured final volume.", "evidence_id": "quantity-42",
    "affected_local_fields": [], "source_amount": 950, "source_unit": "ml", "source_attribute":
    null, "provider_g_l": null, "provider_stage_volume_ml": 1000, "primary_source_evidence_id":
    "dsmz135b"}, {"field_path": "preparation_steps[0].description", "name": "Initial
    gas composition", "current": "80% N2 / 20% CO2", "decision": "evidence_only",
    "source_key": "dsmz135b", "source_quote": "bring to the boil and cool to room
    temperature under 80% N2 and 20% CO2 gas", "source_locator": "page 1, main preparation
    step 1", "preparation_stage": "initial assembly", "decision_rationale": "The initial
    gas mixture and same-atmosphere dispensing are retained in both local layers;
    this is preparation evidence, not a strain phenotype.", "evidence_id": "quantity-43"},
    {"field_path": "preparation_steps[0].description", "name": "Gas for separate syringate/vitamin/cysteine
    stocks", "current": "100% N2", "decision": "evidence_only", "source_key": "dsmz135b",
    "source_quote": "sterile anoxic stock solutions prepared under 100% N2 gas and
    carbonate from a sterile", "source_locator": "page 1, main preparation step 1",
    "preparation_stage": "separate sterile addition stocks", "decision_rationale":
    "Retain the explicit 100% N2 stock-preparation qualifier and its scope; the following
    carbonate stock has a different atmosphere.", "evidence_id": "quantity-44"}, {"field_path":
    "preparation_steps[0].description", "name": "Carbonate-stock gas", "current":
    "80% N2 / 20% CO2", "decision": "evidence_only", "source_key": "dsmz135b", "source_quote":
    "anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Vitamins",
    "source_locator": "page 1, main preparation step 1", "preparation_stage": "carbonate
    stock", "decision_rationale": "The carbonate-stock atmosphere is preserved independently
    of the preceding 100% N2 stocks.", "evidence_id": "quantity-45"}, {"field_path":
    "ph_value / preparation_steps[0].description", "name": "Completed-medium pH",
    "current": 7.4, "decision": "evidence_only", "source_key": "dsmz135b", "source_quote":
    "should be sterilized by filtration. The pH of the completed medium should be
    at 7.4.", "source_locator": "page 1, main preparation step 1", "preparation_stage":
    "completed medium", "decision_rationale": "Both local layers preserve the exact
    pH 7.4 condition and vitamin filtration. No pH range is invented.", "evidence_id":
    "quantity-46"}, {"field_path": "preparation_steps[1].description", "name": "After-growth
    Na-syringate final concentration", "current": "2.00 g/L after growth starts",
    "decision": "evidence_only", "source_key": "dsmz135b", "source_quote": "a final
    concentration of 2.00 g/l.", "source_locator": "page 1, main preparation step
    2, following explicit after-growth trigger", "preparation_stage": "post-start
    feed", "decision_rationale": "The target and owner preserve the source after-growth
    final concentration. This is not 2 g added per original batch, nor the initial
    15 mL stock dose; salt-versus-acid mass basis and feed volume are not inferred.",
    "evidence_id": "quantity-47"}, {"field_path": "preparation_steps[2].description",
    "name": "Mineral-stock initial pH", "current": 6.5, "decision": "evidence_only",
    "source_key": "dsmz135b", "source_quote": "First dissolve nitrilotriacetic acid
    and adjust pH to 6.5 with KOH, then add minerals. Adjust", "source_locator": "page
    2, continuation of mineral-stock preparation", "preparation_stage": "mineral stock
    before other minerals", "decision_rationale": "Preserve the initial pH 6.5 titration
    stage.", "evidence_id": "quantity-48"}, {"field_path": "preparation_steps[2].description",
    "name": "Mineral-stock final pH", "current": 7.0, "decision": "evidence_only",
    "source_key": "dsmz135b", "source_quote": "final to pH 7.0 with KOH.", "source_locator":
    "page 2, mineral-stock preparation", "preparation_stage": "completed mineral stock",
    "decision_rationale": "Preserve final pH 7.0 separately from the preceding pH
    6.5 step.", "evidence_id": "quantity-49"}, {"field_path": "mineral stock KOH amount",
    "name": "KOH", "current": null, "decision": "not_quantified", "source_key": "dsmz135b",
    "source_quote": "final to pH 7.0 with KOH.", "source_locator": "page 2, mineral-stock
    preparation", "preparation_stage": "mineral-stock titration", "decision_rationale":
    "The source identifies KOH but gives no fixed amount. Preserve titration without
    assigning zero or a guessed concentration.", "evidence_id": "quantity-50"}, {"field_path":
    "preparation_steps[3].description", "name": "Starting water volume", "current":
    "700 mL", "decision": "conflict", "source_key": "dsmz135b", "source_quote": "Dissolve
    syringic acid in 800 ml distilled water, add around 50 ml 5 N NaOH, and adjust
    pH", "source_locator": "page 2, Na-syringate stock preparation", "preparation_stage":
    "syringate stock dissolution", "decision_rationale": "Current collection PDF specifies
    800 mL initially, while the local records and current MediaDive preparation specify
    700 mL. Both versions are preserved. Neither initial quantity is the table water
    amount 950 mL or the final makeup volume.", "evidence_id": "quantity-51"}, {"field_path":
    "preparation_steps[3].description", "name": "Stock pH endpoint", "current": "about
    7.5", "decision": "conflict", "source_key": "dsmz135b", "source_quote": "to about
    7.0. Then add water to reach a volume of 1000 ml. Make the solution anoxic by",
    "source_locator": "page 2, Na-syringate stock preparation", "preparation_stage":
    "syringate-stock titration", "decision_rationale": "Current PDF specifies about
    pH 7.0, whereas local/provider text gives about 7.5. This is an explicit source-version
    conflict; no chronology or automatic replacement is assumed.", "evidence_id":
    "quantity-52"}, {"field_path": "preparation_steps[3].description", "name": "Approximate
    NaOH titration dose", "current": "about 50 mL of 5 N", "decision": "evidence_only",
    "source_key": "dsmz135b", "source_quote": "Dissolve syringic acid in 800 ml distilled
    water, add around 50 ml 5 N NaOH, and adjust pH", "source_locator": "page 2, Na-syringate
    stock preparation", "preparation_stage": "syringate-stock titration", "decision_rationale":
    "Both source versions preserve approximately 50 mL of 5 N NaOH. The approximate
    dose and pH endpoint qualify the exact-looking table amount; no density conversion
    is used.", "evidence_id": "quantity-53"}, {"field_path": "preparation_steps[3].description",
    "name": "Final syringate-stock makeup volume", "current": "1000 mL", "decision":
    "evidence_only", "source_key": "dsmz135b", "source_quote": "to about 7.0. Then
    add water to reach a volume of 1000 ml. Make the solution anoxic by", "source_locator":
    "page 2, Na-syringate stock preparation", "preparation_stage": "syringate-stock
    final makeup", "decision_rationale": "The 1000 mL instruction is a final makeup
    volume, distinct from table water 950 mL and initial dissolution water 800/700
    mL. Do not add all three water quantities.", "evidence_id": "quantity-54"}, {"field_path":
    "preparation_steps[3].description", "name": "Syringate-stock gas", "current":
    "100% N2", "decision": "evidence_only", "source_key": "dsmz135b", "source_quote":
    "sparging with 100% N2 gas, distribute in anoxic serum vials and autoclave at
    121°C.", "source_locator": "page 2, Na-syringate stock preparation", "preparation_stage":
    "stock anoxic handling", "decision_rationale": "Both local records preserve 100%
    N2 sparging and anoxic dispensing.", "evidence_id": "quantity-55"}, {"field_path":
    "preparation_steps[3].description", "name": "Syringate-stock autoclave temperature",
    "current": "121 °C", "decision": "evidence_only", "source_key": "dsmz135b", "source_quote":
    "sparging with 100% N2 gas, distribute in anoxic serum vials and autoclave at
    121°C.", "source_locator": "page 2, Na-syringate stock preparation", "preparation_stage":
    "stock sterilization", "decision_rationale": "The source gives 121 °C for this
    stock. Do not transfer this numeric temperature to the main-medium instruction
    or invent a cycle duration.", "evidence_id": "quantity-56"}, {"field_path": "preparation_steps[3].duration",
    "name": "Syringate-stock autoclave duration", "current": null, "decision": "not_quantified",
    "source_key": "dsmz135b", "source_quote": "sparging with 100% N2 gas, distribute
    in anoxic serum vials and autoclave at 121°C.", "source_locator": "page 2, Na-syringate
    stock preparation", "preparation_stage": "stock sterilization", "decision_rationale":
    "No duration is specified in the complete stock instruction. This is an evidence
    limit, not permission to insert a generic cycle.", "evidence_id": "quantity-57"},
    {"field_path": "later sterile stock volumes", "name": "Unspecified addition-stock
    volumes", "current": null, "decision": "not_quantified", "source_key": "dsmz135b",
    "source_quote": "sterile anoxic stock solutions prepared under 100% N2 gas and
    carbonate from a sterile", "source_locator": "page 1, main preparation step 1",
    "preparation_stage": "later cysteine/carbonate addition", "decision_rationale":
    "The source gives their ingredient masses but not all sterile-stock dose volumes.
    These additions do not establish an exact measured final volume.", "evidence_id":
    "quantity-58"}]'
- assessment_id: evidence
  area: evidence
  topic: Claim-level source support and actual reference-check coverage
  outcome: concern
  summary: Neither local layer supplies claim-level amount evidence; the reference
    diagnostic performs zero evidence checks. Exact bound collection and provider
    evidence now traces every amount and version conflict. Their absence from the
    source records does not imply that quantities are scientifically validated by
    schema or term checks. Narrow evidence should be attached during separately authorized
    curation.
  target_ids:
  - CultureMech:000819
  evidence_ids:
  - record
  - owner-0
  - validate-references
  - source-catalog
- assessment_id: organisms
  area: scope
  topic: Bounded biological claims and optional entities
  outcome: not_applicable
  summary: No organism identifiers, strain assertions, assemblies, DOI/PMID papers,
    growth results or KG-Microbe matches occur in either complete local record. Generic
    cultivation and the species-like medium title do not establish such claims. No
    growth targets or alternate experimental recipes are added.
  target_ids:
  - CultureMech:000819
  evidence_ids:
  - record
  - owner-0
findings:
- finding_id: f1
  issue_key: cm000819-stocks-and-naoh-unit
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock strengths and liquid NaOH dose replace the named medium formulation
  description: The local 34-row formula incorporates three undiluted stock recipes
    instead of their 20, 1 and 15 mL additions. Magnesium is stored as 0.0994036 +
    3 = 3.0994036 g/L even though the stock adds only 20 mL; 60 g/L syringic-acid
    precursor is also a stock strength. The source 50 mL of 5 N NaOH becomes direct
    50 g/L. These stage and unit errors make the encoded formula unusable as the named
    source recipe. Provider 1006 mL and listed liquid 1006.5 mL are preserved as different
    quantities.
  target_ids:
  - CultureMech:000819
  field_paths:
  - ingredients
  - ingredients[3].concentration
  - ingredients[32].concentration
  - ingredients[33].concentration
  - solutions
  evidence_ids:
  - record
  - owner-0
  - dsmz135b
  - mediadive135bapi
  - importer
  - cleanup
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P1
  native_severity: P1
  normalization_reason: 'Native P1 scientific formulation blocker: stock-strength
    ingredients and a liquid-to-mass error change the named recipe. This is not P1.1
    schema failure; all four target diagnostics passed.'
- finding_id: f2
  issue_key: cm000819-hydrate-and-sodium-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydrate and sodium indicator mappings lose supplied-form identity
  description: The explicit NiCl2 x 6 H2O stock constituent maps to CHEBI:34887, whose
    formula contains no waters, and Sodium resazurin maps to neutral CHEBI:8806 without
    sodium. Canonical-label and secondary-index correspondence do not prove source-form
    agreement.
  target_ids:
  - CultureMech:000819
  field_paths:
  - ingredients[19].term
  - ingredients[19].mediaingredientmech_chebi_term
  - ingredients[5].term
  evidence_ids:
  - record
  - owner-0
  - dsmz135b
  - chebi34887
  - chebi8806
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml
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
  issue_key: cm000819-syringate-stock-version
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Syringate-stock preparation differs between the cited collection and provider
  description: Both local layers retain provider starting water 700 mL and about pH
    7.5, while the current exact DSMZ PDF specifies initial 800 mL and about pH 7.0.
    The source versions agree on approximate 50 mL of 5 N NaOH, makeup to 1000 mL,
    100% N2 and 121 °C. Table water 950 mL is a separate representation, not another
    addition. The record cites the collection PDF without identifying this provider-specific
    procedural version.
  target_ids:
  - CultureMech:000819
  field_paths:
  - preparation_steps[3].description
  - notes
  evidence_ids:
  - record
  - owner-0
  - dsmz135b
  - provider-stock-preparation
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: Native P3.5 is major because conflicting initial volume and
    titration endpoint materially affect reproducible stock preparation; the process
    is present, not omitted.
- finding_id: f4
  issue_key: cm000819-generated-grounding-lag
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated target lacks the owner’s later syringic-acid grounding
  description: The normalized owner contains CHEBI:68329 for ingredient 32 and a timezone-aware
    20 August grounding event. The generated target retains the earlier 6 August merge
    and has no primary term for that row. Current OLS supports the owner’s neutral
    acid identity. This comparison does not independently authenticate the historical
    MIM publication or predict current exporter edge counts.
  target_ids:
  - CultureMech:000819
  field_paths:
  - ingredients[32].term
  - curation_history
  - merge_fingerprint
  evidence_ids:
  - record
  - owner-0
  - chebi68329
  - grounding-writer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.4
  native_severity: P4
  normalization_reason: 'Minor generated-provenance lag: the chemically appropriate
    acid term is already in the maintained owner; the dominant scientific formulation
    errors are assessed separately.'
actions:
- action_id: a1
  description: Restore three stock definitions and exact doses in the maintained owner,
    preserve dilute NaOH normality/volume and titration scope, separate direct and
    stock magnesium contributions, and attach source evidence. Resolve the receiving-volume
    basis before any final concentration derivation; then preview authorized regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000819
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml
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
  description: Verify exact supplied-form identifiers in the maintained owner and
    preserve source masses, hydrates and salt qualifiers. Do not invent replacements
    or silently convert masses.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000819
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml
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
  description: Resolve and document the intended source version for the maintained
    stock preparation, preserving both observed versions and their exact evidence
    until adjudicated. Keep initial water, table water, final makeup and pH stage
    distinct; retain the source duration limit.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000819
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml
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
  description: Retain the verified owner grounding when the source-stage corrections
    are curated and the generated product is separately regenerated. Preserve append-only
    history; do not patch the generated file or treat this as a new sodium-syringate
    grounding.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000819
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_dehalogenans_medium.yaml
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
- The provider declares a 1006 mL main solution, whereas listed liquid additions sum
  1006.5 mL; later sterile additions have incompletely specified stock volumes. Neither
  number is treated as independently measured final volume.
- Current DSMZ PDF and current MediaDive stock preparation differ. Both inspected
  versions are preserved; their relative historical chronology is not inferred from
  retrieval times or the PDF footer.
- The nominal 0.3 M initial syringate stock and the later final 2 g/L Na-syringate
  feed have different stages and chemical-basis qualifiers. No additional feed volume
  or salt mass is inferred from the acid precursor alone.
- SIGMA S6881 is retained as a source product designation; no separate manufacturer
  specification or equivalence was authenticated. Historical MIM publication provenance
  is recorded, not independently replayed.
- No strain-specific growth, taxonomy, assembly, literature experiment or optimization
  claim is inferred from the medium name.
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
