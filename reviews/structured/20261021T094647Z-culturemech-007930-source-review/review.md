# Source and formulation review: abss2 (CultureMech:007930)

- Review: 20261021T094647Z-culturemech-007930-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T09:35:31Z
- Finished UTC: 2026-10-21T09:46:47Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

ABSS2 is JCM 1298 via TOGO M1395. Both local layers flatten the vitamin stock, relabel volume doses and several milligram stock amounts as g/L, and leave seven stock stubs incomplete. Current JCM and TOGO disagree on water and four stock additions, including phosphate strength. Preparation, source evidence and DL-pantothenate identity require curation; a later owner water repair has not reached the generated target.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 137; batch 014 item 7 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirteen task batches contain 130 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 132 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007930 | data/merge_yaml/merged/ABSS2.yaml | generated | abss2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007930 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007930 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch014/137/strict.tsv |
| validate-terms | passed | True | CultureMech:007930 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007930 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007930 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007930.

The four documented recipes completed; interpret the scope of each separately.

### Exact primary labels and current secondary linkage coverage

grounding: supported. Targets: CultureMech:007930.

15 unique asserted CHEBI identifiers resolve with exact labels. Primary linkage 15/15 (100.00%); verified current secondary linkage 11/15 (73.33%). This is a 0–100 ingredient-instance linkage scale, not scientific correctness. Missing current secondary keys: []. Legacy links and chemical-form correctness are assessed separately.

### Every direct, stock, stock-addition and preparation quantity

quantity: concern. Targets: CultureMech:007930.

Thirty-seven decisions reconcile all 23 main/addition/vitamin source rows, all 10 referenced SL-7 rows and 4 preparation contexts. Every primary quotation is literal; every provider row excerpt is a literal slice of captured raw JSON. Source discrepancies remain conflict decisions.

[{"field_path": "ingredients[0].concentration", "decision": "conflict", "stage": "basal medium before stock additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "Distilled water 930.0 ml", "source_locator": "JCM1298 basal medium before stock additions; primary entry identified by literal text: Distilled water 930.0 ml", "explanation": "Current JCM water 930 ml conflicts with TOGO main water 1 L. The generated target 2 g/L also sums the independent vitamin-stock water 1 L; owner repair changes 2 to 1 but neither restores solvent units nor stock scope. Do not infer version chronology or measured final volume.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[0].items[0]", "provider_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"", "provider_original_amount": 1, "provider_original_unit": "L"}, {"field_path": "ingredients[1].concentration", "decision": "evidence_only", "stage": "basal medium before stock additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "NaCl 11.8 g", "source_locator": "JCM1298 basal medium before stock additions; primary entry identified by literal text: NaCl 11.8 g", "explanation": "Both sources agree on the basal salt mass. The local g/L number agrees on the source per-liter recipe basis, but narrow source evidence and stage are absent. Source water addition alone does not prove measured final volume.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[0].items[1]", "provider_quote": "{\n          \"component_name\": \"NaCl\",\n          \"volume\": 11.8,\n          \"unit\": \"g\"", "provider_original_amount": 11.8, "provider_original_unit": "g"}, {"field_path": "ingredients[2].concentration", "decision": "evidence_only", "stage": "basal medium before stock additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "CaCl 2 ·2H 2 O 0.3 g", "source_locator": "JCM1298 basal medium before stock additions; primary entry identified by literal text: CaCl 2 ·2H 2 O 0.3 g", "explanation": "Both sources agree on the basal salt mass. The local g/L number agrees on the source per-liter recipe basis, but narrow source evidence and stage are absent. Source water addition alone does not prove measured final volume.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[0].items[2]", "provider_quote": "{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"", "provider_original_amount": 0.3, "provider_original_unit": "g"}, {"field_path": "ingredients[3].concentration", "decision": "evidence_only", "stage": "basal medium before stock additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "MgCl 2 ·6H 2 O 2.2 g", "source_locator": "JCM1298 basal medium before stock additions; primary entry identified by literal text: MgCl 2 ·6H 2 O 2.2 g", "explanation": "Both sources agree on the basal salt mass. The local g/L number agrees on the source per-liter recipe basis, but narrow source evidence and stage are absent. Source water addition alone does not prove measured final volume.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[0].items[3]", "provider_quote": "{\n          \"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 2.2,\n          \"unit\": \"g\"", "provider_original_amount": 2.2, "provider_original_unit": "g"}, {"field_path": "ingredients[4].concentration", "decision": "evidence_only", "stage": "basal medium before stock additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "KCl 0.4 g", "source_locator": "JCM1298 basal medium before stock additions; primary entry identified by literal text: KCl 0.4 g", "explanation": "Both sources agree on the basal salt mass. The local g/L number agrees on the source per-liter recipe basis, but narrow source evidence and stage are absent. Source water addition alone does not prove measured final volume.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[0].items[4]", "provider_quote": "{\n          \"component_name\": \"KCl\",\n          \"volume\": 0.4,\n          \"unit\": \"g\"", "provider_original_amount": 0.4, "provider_original_unit": "g"}, {"field_path": "solutions[0].concentration", "decision": "conflict", "stage": "addition per liter after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "1 M NaHCO 3 solution* 30.0 ml", "source_locator": "JCM1298 addition per liter after basal medium cooling; primary entry identified by literal text: 1 M NaHCO 3 solution* 30.0 ml", "explanation": "Current JCM specifies 30 ml of 1 M bicarbonate, versus TOGO 3 ml of 1 M. Local 3 g/L is neither a valid volume dose nor a source-version resolution.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[1].items[0]", "provider_quote": "{\n          \"component_name\": \"1 M NaHCO3 solution*\",\n          \"volume\": 3,\n          \"unit\": \"ml\"", "provider_original_amount": 3, "provider_original_unit": "ml"}, {"field_path": "solutions[1].concentration", "decision": "conflict", "stage": "addition per liter after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "100 mM NH 4 Cl solution 10.0 ml", "source_locator": "JCM1298 addition per liter after basal medium cooling; primary entry identified by literal text: 100 mM NH 4 Cl solution 10.0 ml", "explanation": "Current JCM specifies 10 ml of 100 mM NH4Cl, versus TOGO 20 ul of 100 mM. 20 ul equals 0.020 ml; both differ from the local 20 g/L claim.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[1].items[1]", "provider_quote": "{\n          \"component_name\": \"100 mM NH4Cl solution\",\n          \"volume\": 20,\n          \"unit\": \"ul\"", "provider_original_amount": 20, "provider_original_unit": "ul"}, {"field_path": "solutions[2].concentration", "decision": "conflict", "stage": "addition per liter after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "100 mM Na 2 HPO 4 solution 10.0 ml", "source_locator": "JCM1298 addition per liter after basal medium cooling; primary entry identified by literal text: 100 mM Na 2 HPO 4 solution 10.0 ml", "explanation": "Current JCM specifies 10 ml of 100 mM Na2HPO4, versus TOGO 100 ul of 10 mM. 100 ul equals 0.100 ml. Both stock strength and addition differ; local 100 g/L is not supported.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[1].items[2]", "provider_quote": "{\n          \"component_name\": \"10 mM Na2HPO4 solution\",\n          \"volume\": 100,\n          \"unit\": \"ul\"", "provider_original_amount": 100, "provider_original_unit": "ul"}, {"field_path": "solutions[3].concentration", "decision": "correct", "stage": "addition per liter after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "500 mM MnO 2 solution 10.0 ml", "source_locator": "JCM1298 addition per liter after basal medium cooling; primary entry identified by literal text: 500 mM MnO 2 solution 10.0 ml", "explanation": "Preserve the original source unit and explicit stage. The current G_PER_L number cannot substitute for a stock dose or a stock-formulation quantity.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[1].items[3]", "provider_quote": "{\n          \"component_name\": \"500 mM MnO2 solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\"", "provider_original_amount": 10, "provider_original_unit": "ml"}, {"field_path": "solutions[4].concentration", "decision": "correct", "stage": "addition per liter after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "300 mM Na 2 S 2 O 3 solution 10.0 ml", "source_locator": "JCM1298 addition per liter after basal medium cooling; primary entry identified by literal text: 300 mM Na 2 S 2 O 3 solution 10.0 ml", "explanation": "Preserve the original source unit and explicit stage. The current G_PER_L number cannot substitute for a stock dose or a stock-formulation quantity.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[1].items[4]", "provider_quote": "{\n          \"component_name\": \"300 mM Na2S2O3 solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\"", "provider_original_amount": 10, "provider_original_unit": "ml"}, {"field_path": "solutions[5].concentration", "decision": "conflict", "stage": "addition per liter after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "SL-7 trace element solution (see Medium No. 536 ) 1.0 ml", "source_locator": "JCM1298 addition per liter after basal medium cooling; primary entry identified by literal text: SL-7 trace element solution (see Medium No. 536 ) 1.0 ml", "explanation": "Current JCM specifies 1 ml SL-7, versus TOGO 100 ul (0.100 ml). The stock composition itself agrees across the scoped external sources, but that does not resolve the differing addition doses.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[1].items[5]", "provider_quote": "{\n          \"component_name\": \"SL--7 trace element solution (see Medium [M538])\",\n          \"volume\": 100,\n          \"unit\": \"ul\"", "provider_original_amount": 100, "provider_original_unit": "ul"}, {"field_path": "solutions[6].concentration", "decision": "correct", "stage": "addition per liter after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "Vitamin solution* (see below) 0.42 ml", "source_locator": "JCM1298 addition per liter after basal medium cooling; primary entry identified by literal text: Vitamin solution* (see below) 0.42 ml", "explanation": "TOGO 420 ul equals JCM 0.42 ml exactly (420/1000=0.42). This is a vitamin-stock addition per liter, not 420 g/L or an instruction to add every undiluted stock ingredient directly.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[1].items[6]", "provider_quote": "{\n          \"component_name\": \"Vitamin solution* (see below)\",\n          \"volume\": 420,\n          \"unit\": \"ul\"", "provider_original_amount": 420, "provider_original_unit": "ul"}, {"field_path": "ingredients[5].concentration", "decision": "not_quantified", "stage": "addition per liter after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture", "source_locator": "JCM1298 pH-adjustment gas-mixture sentence", "explanation": "Source gives N2/CO2 at 4:1 by volume while adjusting pH 7.5, but no absolute gas dose, flow, headspace volume or dissolved-gas concentration. VARIABLE does not preserve the missing gas ratio and preparation stage.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[1].items[7]", "provider_quote": "{\n          \"component_name\": \"Carbon dioxide gas\"", "provider_original_amount": null, "provider_original_unit": null}, {"field_path": "ingredients[6].concentration", "decision": "not_quantified", "stage": "addition per liter after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture", "source_locator": "JCM1298 pH-adjustment gas-mixture sentence", "explanation": "Source gives N2/CO2 at 4:1 by volume while adjusting pH 7.5, but no absolute gas dose, flow, headspace volume or dissolved-gas concentration. VARIABLE does not preserve the missing gas ratio and preparation stage.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[1].items[8]", "provider_quote": "{\n          \"component_name\": \"Nitrogen gas\"", "provider_original_amount": null, "provider_original_unit": null}, {"field_path": "ingredients[0].concentration", "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "Distilled water 1.0 L", "source_locator": "JCM1298 vitamin stock before its 0.42 ml per-liter addition; primary entry identified by literal text: Distilled water 1.0 L", "explanation": "Both sources agree on this separately prepared vitamin-stock row. Preserve it within the stock, not as a direct medium component or summed main solvent.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[2].items[0]", "provider_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"", "provider_original_amount": 1, "provider_original_unit": "L"}, {"field_path": "ingredients[7].concentration", "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "Biotin 10.0 mg", "source_locator": "JCM1298 vitamin stock before its 0.42 ml per-liter addition; primary entry identified by literal text: Biotin 10.0 mg", "explanation": "Both sources agree on this separately prepared vitamin-stock row. Preserve it within the stock, not as a direct medium component or summed main solvent. The source 10 mg equals 0.01 g within that stock; the current number in g/L is not that conversion and still omits subsequent stock dilution.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[2].items[1]", "provider_quote": "{\n          \"component_name\": \"Biotin\",\n          \"volume\": 10,\n          \"unit\": \"mg\"", "provider_original_amount": 10, "provider_original_unit": "mg"}, {"field_path": "ingredients[8].concentration", "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "p -Aminobenzoic acid 100.0 mg", "source_locator": "JCM1298 vitamin stock before its 0.42 ml per-liter addition; primary entry identified by literal text: p -Aminobenzoic acid 100.0 mg", "explanation": "Both sources agree on this separately prepared vitamin-stock row. Preserve it within the stock, not as a direct medium component or summed main solvent. The source 100 mg equals 0.1 g within that stock; the current number in g/L is not that conversion and still omits subsequent stock dilution.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[2].items[2]", "provider_quote": "{\n          \"component_name\": \"p-Aminobenzoic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\"", "provider_original_amount": 100, "provider_original_unit": "mg"}, {"field_path": "ingredients[9].concentration", "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "Thiamine-HCl 2.0 g", "source_locator": "JCM1298 vitamin stock before its 0.42 ml per-liter addition; primary entry identified by literal text: Thiamine-HCl 2.0 g", "explanation": "Both sources agree on this separately prepared vitamin-stock row. Preserve it within the stock, not as a direct medium component or summed main solvent.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[2].items[3]", "provider_quote": "{\n          \"component_name\": \"Thiamine-HCl\",\n          \"volume\": 2,\n          \"unit\": \"g\"", "provider_original_amount": 2, "provider_original_unit": "g"}, {"field_path": "ingredients[10].concentration", "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "Folic acid 10.0 mg", "source_locator": "JCM1298 vitamin stock before its 0.42 ml per-liter addition; primary entry identified by literal text: Folic acid 10.0 mg", "explanation": "Both sources agree on this separately prepared vitamin-stock row. Preserve it within the stock, not as a direct medium component or summed main solvent. The source 10 mg equals 0.01 g within that stock; the current number in g/L is not that conversion and still omits subsequent stock dilution.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[2].items[4]", "provider_quote": "{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 10,\n          \"unit\": \"mg\"", "provider_original_amount": 10, "provider_original_unit": "mg"}, {"field_path": "ingredients[11].concentration", "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "Vitamin B 12 10.0 mg", "source_locator": "JCM1298 vitamin stock before its 0.42 ml per-liter addition; primary entry identified by literal text: Vitamin B 12 10.0 mg", "explanation": "Both sources agree on this separately prepared vitamin-stock row. Preserve it within the stock, not as a direct medium component or summed main solvent. The source 10 mg equals 0.01 g within that stock; the current number in g/L is not that conversion and still omits subsequent stock dilution.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[2].items[5]", "provider_quote": "{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 10,\n          \"unit\": \"mg\"", "provider_original_amount": 10, "provider_original_unit": "mg"}, {"field_path": "ingredients[12].concentration", "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "Nicotinic acid 1.0 g", "source_locator": "JCM1298 vitamin stock before its 0.42 ml per-liter addition; primary entry identified by literal text: Nicotinic acid 1.0 g", "explanation": "Both sources agree on this separately prepared vitamin-stock row. Preserve it within the stock, not as a direct medium component or summed main solvent.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[2].items[6]", "provider_quote": "{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 1,\n          \"unit\": \"g\"", "provider_original_amount": 1, "provider_original_unit": "g"}, {"field_path": "ingredients[13].concentration", "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "Inositol 10.0 mg", "source_locator": "JCM1298 vitamin stock before its 0.42 ml per-liter addition; primary entry identified by literal text: Inositol 10.0 mg", "explanation": "Both sources agree on this separately prepared vitamin-stock row. Preserve it within the stock, not as a direct medium component or summed main solvent. The source 10 mg equals 0.01 g within that stock; the current number in g/L is not that conversion and still omits subsequent stock dilution.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[2].items[7]", "provider_quote": "{\n          \"component_name\": \"Inositol\",\n          \"volume\": 10,\n          \"unit\": \"mg\"", "provider_original_amount": 10, "provider_original_unit": "mg"}, {"field_path": "ingredients[14].concentration", "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "DL-Calcium pantothenate 1.0 g", "source_locator": "JCM1298 vitamin stock before its 0.42 ml per-liter addition; primary entry identified by literal text: DL-Calcium pantothenate 1.0 g", "explanation": "Both sources agree on this separately prepared vitamin-stock row. Preserve it within the stock, not as a direct medium component or summed main solvent. Explicit DL material must not be narrowed to a single stereoisomer by the linked ontology structure.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator": "$.components[2].items[8]", "provider_quote": "{\n          \"component_name\": \"DL-Calcium pantothenate\",\n          \"volume\": 1,\n          \"unit\": \"g\"", "provider_original_amount": 1, "provider_original_unit": "g"}, {"field_path": "solutions[5].composition (missing source item 25% HCl (7.7 M))", "decision": "add", "stage": "SL-7 stock preparation", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536", "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802", "source_quote": "25% HCl (7.7 M) 10.0 ml", "source_locator": "JCM536 SL-7 subsection only; exact 25% HCl (7.7 M) row", "explanation": "Source-supported nested SL-7 stock composition is absent from the empty local stub. Keep its stock batch and later source-dependent addition separate; do not import the PHE91 basal or vitamin recipes. Preserve the source 25% and 7.7 M labels without inventing the unstated percentage convention or performing a density conversion.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538", "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550", "provider_locator": "$.components[2].items[0]", "provider_quote": "{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\"", "original_source_amount": 10, "original_source_unit": "ml"}, {"field_path": "solutions[5].composition (missing source item Distilled water)", "decision": "add", "stage": "SL-7 stock preparation", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536", "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802", "source_quote": "Distilled water 1.0 L", "source_locator": "JCM536 SL-7 subsection only; exact Distilled water row", "explanation": "Source-supported nested SL-7 stock composition is absent from the empty local stub. Keep its stock batch and later source-dependent addition separate; do not import the PHE91 basal or vitamin recipes.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538", "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550", "provider_locator": "$.components[2].items[1]", "provider_quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"", "original_source_amount": 1, "original_source_unit": "L"}, {"field_path": "solutions[5].composition (missing source item Na2MoO4・2H2O)", "decision": "add", "stage": "SL-7 stock preparation", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536", "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802", "source_quote": "Na 2 MoO 4 ·2H 2 O 36.0 mg", "source_locator": "JCM536 SL-7 subsection only; exact Na2MoO4・2H2O row", "explanation": "Source-supported nested SL-7 stock composition is absent from the empty local stub. Keep its stock batch and later source-dependent addition separate; do not import the PHE91 basal or vitamin recipes. Within this stock only, 36 mg=0.036 g.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538", "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550", "provider_locator": "$.components[2].items[2]", "provider_quote": "{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\"", "original_source_amount": 36, "original_source_unit": "mg"}, {"field_path": "solutions[5].composition (missing source item H3BO3)", "decision": "add", "stage": "SL-7 stock preparation", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536", "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802", "source_quote": "H 3 BO 3 62.0 mg", "source_locator": "JCM536 SL-7 subsection only; exact H3BO3 row", "explanation": "Source-supported nested SL-7 stock composition is absent from the empty local stub. Keep its stock batch and later source-dependent addition separate; do not import the PHE91 basal or vitamin recipes. Within this stock only, 62 mg=0.062 g.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538", "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550", "provider_locator": "$.components[2].items[3]", "provider_quote": "{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 62,\n          \"unit\": \"mg\"", "original_source_amount": 62, "original_source_unit": "mg"}, {"field_path": "solutions[5].composition (missing source item MnCl2・4H2O)", "decision": "add", "stage": "SL-7 stock preparation", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536", "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802", "source_quote": "MnCl 2 ·4H 2 O 100.0 mg", "source_locator": "JCM536 SL-7 subsection only; exact MnCl2・4H2O row", "explanation": "Source-supported nested SL-7 stock composition is absent from the empty local stub. Keep its stock batch and later source-dependent addition separate; do not import the PHE91 basal or vitamin recipes. Within this stock only, 100 mg=0.1 g.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538", "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550", "provider_locator": "$.components[2].items[4]", "provider_quote": "{\n          \"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\"", "original_source_amount": 100, "original_source_unit": "mg"}, {"field_path": "solutions[5].composition (missing source item CoCl2・6H2O)", "decision": "add", "stage": "SL-7 stock preparation", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536", "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802", "source_quote": "CoCl 2 ·6H 2 O 190.0 mg", "source_locator": "JCM536 SL-7 subsection only; exact CoCl2・6H2O row", "explanation": "Source-supported nested SL-7 stock composition is absent from the empty local stub. Keep its stock batch and later source-dependent addition separate; do not import the PHE91 basal or vitamin recipes. Within this stock only, 190 mg=0.19 g.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538", "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550", "provider_locator": "$.components[2].items[5]", "provider_quote": "{\n          \"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\"", "original_source_amount": 190, "original_source_unit": "mg"}, {"field_path": "solutions[5].composition (missing source item NiCl2・6H2O)", "decision": "add", "stage": "SL-7 stock preparation", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536", "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802", "source_quote": "NiCl 2 ·6H 2 O 24.0 mg", "source_locator": "JCM536 SL-7 subsection only; exact NiCl2・6H2O row", "explanation": "Source-supported nested SL-7 stock composition is absent from the empty local stub. Keep its stock batch and later source-dependent addition separate; do not import the PHE91 basal or vitamin recipes. Within this stock only, 24 mg=0.024 g.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538", "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550", "provider_locator": "$.components[2].items[6]", "provider_quote": "{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\"", "original_source_amount": 24, "original_source_unit": "mg"}, {"field_path": "solutions[5].composition (missing source item CuCl2・2H2O)", "decision": "add", "stage": "SL-7 stock preparation", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536", "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802", "source_quote": "CuCl 2 ·2H 2 O 17.0 mg", "source_locator": "JCM536 SL-7 subsection only; exact CuCl2・2H2O row", "explanation": "Source-supported nested SL-7 stock composition is absent from the empty local stub. Keep its stock batch and later source-dependent addition separate; do not import the PHE91 basal or vitamin recipes. Within this stock only, 17 mg=0.017 g.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538", "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550", "provider_locator": "$.components[2].items[7]", "provider_quote": "{\n          \"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 17,\n          \"unit\": \"mg\"", "original_source_amount": 17, "original_source_unit": "mg"}, {"field_path": "solutions[5].composition (missing source item ZnCl2)", "decision": "add", "stage": "SL-7 stock preparation", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536", "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802", "source_quote": "ZnCl 2 70.0 mg", "source_locator": "JCM536 SL-7 subsection only; exact ZnCl2 row", "explanation": "Source-supported nested SL-7 stock composition is absent from the empty local stub. Keep its stock batch and later source-dependent addition separate; do not import the PHE91 basal or vitamin recipes. Within this stock only, 70 mg=0.07 g.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538", "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550", "provider_locator": "$.components[2].items[8]", "provider_quote": "{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\"", "original_source_amount": 70, "original_source_unit": "mg"}, {"field_path": "solutions[5].composition (missing source item FeCl2・4H2O)", "decision": "add", "stage": "SL-7 stock preparation", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536", "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802", "source_quote": "FeCl 2 ·4H 2 O 1.5 g", "source_locator": "JCM536 SL-7 subsection only; exact FeCl2・4H2O row", "explanation": "Source-supported nested SL-7 stock composition is absent from the empty local stub. Keep its stock batch and later source-dependent addition separate; do not import the PHE91 basal or vitamin recipes.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538", "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550", "provider_locator": "$.components[2].items[9]", "provider_quote": "{\n          \"component_name\": \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"", "original_source_amount": 1.5, "original_source_unit": "g"}, {"field_path": "ph_value; preparation_steps", "decision": "add", "stage": "gas-mediated pH adjustment", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "Adjust pH to 7.5 by bubbling", "source_locator": "JCM1298 preparation/default", "explanation": "Both layers omit source target pH 7.5 and its adjustment stage. This is a target pH, not a measured post-growth value."}, {"field_path": "sterilization; preparation_steps", "decision": "add", "stage": "JCM default for autoclaved components", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.", "source_locator": "JCM1298 preparation/default", "explanation": "Retain the primary page-wide default with the explicit starred filter-sterilization exceptions. Do not apply the default to the starred bicarbonate/vitamin stocks."}, {"field_path": "preparation_steps; solutions[*].preparation_notes", "decision": "add", "stage": "post-cooling additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3", "source_quote": "After cooling, aseptically and anaerobically add per liter the following solutions (autoclaved or *filter-sterilized):", "source_locator": "JCM1298 preparation/default", "explanation": "Retain the source ordering, aseptic/anaerobic context and per-liter basis; stock names alone do not encode this preparation."}, {"field_path": "solutions[5].preparation_notes", "decision": "add", "stage": "SL-7 subsection preparation only", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536", "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802", "source_quote": "Initially, dissolve FeCl 2 ·4H 2 O in 25% HCl, then add distilled water followed by the other components.", "source_locator": "JCM536 SL-7 subsection ending before Vitamin solution", "explanation": "Preserve only this directly associated stock instruction; no other PHE91 preparation is imported."}]

### Exact medium accession and linked source scope

identity: supported. Targets: CultureMech:007930.

TOGO M1395 and JCM1298 denote ABSS2. The linked M538 denotes JCM536 PHE91, but the explicit cross-reference is only to its SL-7 stock; that stock section agrees with JCM. This does not make the full PHE91 medium or its other stocks part of ABSS2.

### Current primary and provider conflicts

consistency: concern. Targets: CultureMech:007930.

Water differs930 ml versus 1 L. Bicarbonate differs 30 versus 3 ml; ammonium chloride 10 ml versus 20 ul; phosphate 100 mM/10 ml versus 10 mM/100 ul; SL-7 differs 1 ml versus 100 ul. Vitamin 420 ul equals 0.42 ml and manganese/thiosulfate each 10 ml agree. Retrieval timestamps do not establish the origin or chronological direction of differences.

### Source salts, vitamins and stereochemistry

grounding: concern. Targets: CultureMech:007930.

Basal calcium dihydrate and magnesium hexahydrate are correctly named and grounded. Generic vitamin B12 and inositol retain broad terms without invented vitamer/isomer specificity. Thiamine-HCl is retained without guessing an additional hydrate. DL-calcium pantothenate conflicts with the explicit single-stereoisomer structure in CHEBI:31345 despite its generic canonical label and a live MIM row; two REJECTED preferred-term rows in the same index are not proof that the live mapped row is absent.

### Seven local stock stubs and source-linked composition

completeness: concern. Targets: CultureMech:007930.

All seven solution entries have empty compositions and Unknown solution names. Five stock names supply source strengths, but dose and strength must remain separate, including the explicit phosphate-source conflict. The exact vitamin recipe is flattened into direct ingredients; SL-7 has a resolvable ten-row external definition. No cyclic expansion is necessary and unrelated referenced-medium stocks are excluded.

### Sterilization, sequencing, gas ratio and target pH

completeness: concern. Targets: CultureMech:007930.

Both sources require main autoclaving, cooling, aseptic/anaerobic stock additions and target pH 7.5 using N2/CO2 at 4:1(v/v). JCM supplies the page-wide 121 C/15 min default and stars bicarbonate/vitamin for filtration. None of these preparation details survives in either local layer. Gas VARIABLE values are intentionally unquantified but cannot replace the missing ratio/context.

### Classification and biological scope

scope: concern. Targets: CultureMech:007930.

LIQUID is consistent with a non-agar medium; it does not assert every material is fully dissolved. COMPLEX/UNDEFINED lacks reconciliation with the explicitly enumerated salt/vitamin/trace recipe and should be reassessed after the stock and source-version corrections. No target organism, strain, demonstrated growth, parent, native variant or KG match is asserted. Do not infer biological outcomes from this recipe alone.

### Owner/target disagreement and claim evidence

provenance: concern. Targets: CultureMech:007930.

All 12 target and 12 owner timestamps include timezones. The target ends with its August merge; owner ends with September duplicate repair, changing water 2 to 1 and its note. All other ingredients and stocks agree. That repair does not recover distinct stock/main water stages or volume units. Neither fully read layer contains claim-level source excerpts or preparation references; canonical reference checking does not establish missing scientific support.

## Findings

### f1: Stock quantities and additions are represented as direct g/L

blocker / open / confirmed; issue key: CM007930-unit-and-stock-stage-collapse.

Eight vitamin-stock components are flattened into the medium. Five vitamin milligram numbers are relabeled as g/L; three gram quantities remain at stock scale. All seven volume additions become g/L, and separate main/vitamin water quantities are conflated. This materially changes the formulation despite passing structure/term checks.

### f2: Current primary and TOGO disagree on five formulation claims

major / open / confirmed; issue key: CM007930-unresolved-source-version.

The disagreement concerns main water and bicarbonate, ammonium chloride, phosphate and SL-7 additions; phosphate also differs in stock strength. Equal names and successful lookup cannot select a source version or date when it changed.

### f3: Source-defined stocks remain empty placeholders

major / open / confirmed; issue key: CM007930-stock-definitions-missing.

The vitamin formulation and ten-row SL-7 recipe are accessible, but all seven local solution compositions remain empty and their names say Unknown solution. Named molar stocks also lack structured source-scoped strength/identity context.

### f4: Source preparation, gas ratio and target pH are absent

major / open / confirmed; issue key: CM007930-preparation-and-ph-omission.

Neither layer preserves the source main autoclaving, cooling, aseptic/anaerobic additions, starred filtration exceptions, N2/CO2 ratio 4:1(v/v), or target pH 7.5. JCM’s page-wide autoclave default must remain subordinate to the explicit stock exceptions.

### f5: DL material maps to a stereospecific calcium pantothenate structure

major / open / confirmed; issue key: CM007930-dl-pantothenate-structure.

Both recipe sources and preferred terms explicitly specify DL-calcium pantothenate. CHEBI:31345 contains stereospecified pantothenate structures; its generic label and valid MIM preferred-term row do not establish correspondence to the DL material.

### f6: Generated water differs from its maintained owner and source evidence is absent

minor / open / confirmed; issue key: CM007930-owner-water-and-evidence-drift.

The owner’s September repair changes the duplicate-summed water 2 to 1 while the generated target remains 2. Neither g/L value represents the source solvent correctly, so merely propagating the owner value is insufficient. Source claims also lack narrow evidence despite generic source URLs. COMPLEX/UNDEFINED requires source-scoped reassessment.

## Recommended Actions And Acceptance Checks

### a1

Restore exact original units and main/stock/addition boundaries. Preserve source-version conflicts explicitly and do not derive final concentrations without a verified volume basis.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve the intended accession/version using source-specific provenance, retain both conflicting captures and make any version choice explicit. Do not average or silently substitute a current primary value into an undocumented historical variant.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Represent each exact source stock and its strength independently of its addition dose; preserve vitamin and SL-7 compositions without flattening. Scope M538/JCM536 only to SL-7, and resolve unsupported forms rather than inventing salt hydrates.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Retain exact source preparation order, target pH, gas ratio and scoped sterilization instructions with narrow quotations. Do not invent absolute gas quantities, flow, incubation conditions or a measured final pH.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Resolve the exact DL source material against a verified ontology representation or explicitly retain unresolved grounding. Preserve the stock amount and do not substitute a D-only or L-only form by name similarity.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Correct the maintained scientific representation first, preserve append-only history, attach source-version-specific excerpts and then regenerate with merge/freshness checks. Reassess composition classification from the corrected complete stock-aware formulation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ABSS2.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ABSS2.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ABSS2.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch014/137/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch014/137/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ABSS2.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ABSS2.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ABSS2.yaml:1:id: CultureMech:007930<br>./data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml:1:id: CultureMech:007930<br> |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:15377 resolves to water; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7732-18-5", "gmelin:117", "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001", "metacyc.compound:WATER", "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"], "generalized_empirical_formula": ["H2O"], "has_alternative_id": ["CHEBI:10743", "CHEBI:13352", "CHEBI:27313", "CHEBI:42043", "CHEBI:42857", "CHEBI:43228", "CHEBI:44292", "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15377"], "inchi_key_string": ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "monoisotopic_mass": ["18.01056"], "smiles_string": ["[H]O[H]"]} |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:15940 resolves to nicotinic acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["agr:IND607088605", "cas:59-67-6", "chemspider:913", "drugbank:DB00627", "drugcentral:2835", "foodb.food:FDB001014", "gmelin:3340", "hmdb:HMDB0001488", "kegg.compound:C00253", "kegg.drug:D00049", "knapsack:C00000208", "lincs.smallmolecule:LSM-4676", "metacyc.compound:NIACINE", "pdb-ccd:NIO", "pubmed:10540864", "pubmed:113218", "pubmed:12563315", "pubmed:12789870", "pubmed:135660", "pubmed:14550884", "pubmed:15037193", "pubmed:15183629", "pubmed:15205990", "pubmed:15311728", "pubmed:15627518", "pubmed:15651982", "pubmed:16018787", "pubmed:16172771", "pubmed:16322787", "pubmed:16400392", "pubmed:16449845", "pubmed:16767301", "pubmed:16877271", "pubmed:16945375", "pubmed:18037924", "pubmed:182198", "pubmed:186078", "pubmed:18993152", "pubmed:18996527", "pubmed:19369827", "pubmed:19592242", "pubmed:19678716", "pubmed:19779335", "pubmed:20979384", "pubmed:21632263", "pubmed:22116693", "pubmed:22155410", "pubmed:22229411", "pubmed:22366213", "pubmed:22458880", "pubmed:22770225", "pubmed:24029555", "pubmed:24568240", "pubmed:24675661", "pubmed:24848081", "pubmed:24975217", "pubmed:25040591", "pubmed:25241762", "pubmed:25429652", "pubmed:32954525", "pubmed:33273654", "pubmed:33932650", "pubmed:34066686", "pubmed:34085526", "pubmed:34117670", "pubmed:4033386", "pubmed:4259917", "pubmed:582105", "pubmed:699281", "pubmed:7217784", "pubmed:7581845", "pubmed:8306147", "pubmed:8423912", "pubmed:8679452", "pubmed:9107536", "reaxys:109591", "wikipedia.en:Niacin"], "generalized_empirical_formula": ["C6H5NO2"], "has_alternative_id": ["CHEBI:25538", "CHEBI:44319", "CHEBI:7559"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15940"], "inchi_key_string": ["PVNIIMVLHYAWGP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"], "mass": ["123.111"], "monoisotopic_mass": ["123.03203"], "smiles_string": ["O=C(O)c1cccnc1"]} |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:15956 resolves to biotin; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:58-85-5", "chemspider:149962", "drugbank:DB00121", "drugcentral:373", "foodb.food:FDB014510", "gmelin:1918703", "hmdb:HMDB0000030", "kegg.compound:C00120", "kegg.drug:D00029", "knapsack:C00000756", "lincs.smallmolecule:LSM-3994", "metacyc.compound:BIOTIN", "pdb-ccd:BTN", "pmc:PMC8089577", "pubmed:10064317", "pubmed:10215065", "pubmed:10577274", "pubmed:11435506", "pubmed:11481419", "pubmed:11800048", "pubmed:12055344", "pubmed:12070309", "pubmed:12603856", "pubmed:12803839", "pubmed:15012185", "pubmed:15202718", "pubmed:15272000", "pubmed:15690449", "pubmed:15863846", "pubmed:15899401", "pubmed:15992684", "pubmed:16011464", "pubmed:16195795", "pubmed:16419467", "pubmed:16676358", "pubmed:16677798", "pubmed:16704206", "pubmed:16769720", "pubmed:17297119", "pubmed:1814646", "pubmed:18202531", "pubmed:18452485", "pubmed:18509457", "pubmed:19212411", "pubmed:19319844", "pubmed:19727438", "pubmed:19928962", "pubmed:20967359", "pubmed:20974274", "pubmed:2100006", "pubmed:21248194", "pubmed:21356565", "pubmed:21373679", "pubmed:21596550", "pubmed:21871906", "pubmed:25515858", "pubmed:33346513", "pubmed:33461365", "pubmed:34077272", "pubmed:8333586", "pubmed:8750932", "pubmed:9022537", "pubmed:9038855", "pubmed:9094878", "pubmed:9164991", "pubmed:9176832", "pubmed:9371938", "pubmed:9416479", "reaxys:86838", "wikipedia.en:Biotin"], "generalized_empirical_formula": ["C10H16N2O3S"], "has_alternative_id": ["CHEBI:13905", "CHEBI:22882", "CHEBI:22884", "CHEBI:3108", "CHEBI:41236"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15956"], "inchi_key_string": ["YBJHBAHKTGYVGT-ZKWXMUAHSA-N"], "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"], "mass": ["244.316"], "monoisotopic_mass": ["244.08816"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]} |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:16526 resolves to carbon dioxide; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:124-38-9", "drugcentral:4256", "gmelin:989", "hmdb:HMDB0001967", "kegg.compound:C00011", "kegg.drug:D00004", "metacyc.compound:CARBON-DIOXIDE", "molbase:752", "pdb-ccd:CO2", "ppdb:119", "pubmed:10826146", "pubmed:11094503", "pubmed:11584085", "pubmed:11802652", "pubmed:14639145", "pubmed:15050588", "pubmed:16591971", "pubmed:16656478", "pubmed:16659660", "pubmed:17190796", "pubmed:17448243", "pubmed:17878298", "pubmed:17884085", "pubmed:19043767", "pubmed:19259576", "pubmed:19854893", "pubmed:23384758", "pubmed:23828359", "pubmed:24258718", "pubmed:8482095", "pubmed:8818713", "pubmed:8869828", "pubmed:9611769", "pubmed:9730350", "reaxys:1900390", "umbbd.compound:c0131", "wikipedia.en:Carbon_dioxide"], "generalized_empirical_formula": ["CO2"], "has_alternative_id": ["CHEBI:13282", "CHEBI:13283", "CHEBI:13284", "CHEBI:13285", "CHEBI:23011", "CHEBI:3283", "CHEBI:48829"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16526"], "inchi_key_string": ["CURLTUGMZLYLDI-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/CO2/c2-1-3"], "mass": ["44.009"], "monoisotopic_mass": ["43.98983"], "smiles_string": ["O=C=O"]} |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:176843 resolves to vitamin B12; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:176843"]} |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:17997 resolves to dinitrogen; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7727-37-9", "drugcentral:4251", "gmelin:150", "hmdb:HMDB0001371", "kegg.compound:C00697", "kegg.drug:D00083", "metacyc.compound:NITROGEN-MOLECULE", "pdb-ccd:HDZ", "pubmed:18334638", "pubmed:22237545", "reaxys:15940095", "wikipedia.en:Nitrogen"], "generalized_empirical_formula": ["N2"], "has_alternative_id": ["CHEBI:13388", "CHEBI:14660", "CHEBI:25365", "CHEBI:43128", "CHEBI:7593"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17997"], "inchi_key_string": ["IJGRMHOSHXDMSA-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/N2/c1-2"], "mass": ["28.014"], "monoisotopic_mass": ["28.00615"], "smiles_string": ["N#N"]} |
| chebi24848 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_24848; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:24848 resolves to inositol; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "generalized_empirical_formula": ["C6H12O6"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:24848"], "inchi_key_string": ["CDAISMWEOUEBRE-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H12O6/c7-1-2(8)4(10)6(12)5(11)3(1)9/h1-12H"], "mass": ["180.156"], "monoisotopic_mass": ["180.06339"], "smiles_string": ["OC1C(O)C(O)C(O)C(O)C1O"]} |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:26710 resolves to sodium chloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula": ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string": ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]} |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:27470 resolves to folic acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["agr:IND606960789", "cas:59-30-3", "chemspider:5815", "drugbank:DB00158", "drugcentral:1231", "foodb.food:FDB014504", "hmdb:HMDB0000121", "kegg.compound:C00504", "kegg.drug:D00070", "knapsack:C00001539", "lincs.smallmolecule:LSM-5355", "metacyc.compound:CPD-12826", "pdb-ccd:FOL", "pubmed:10138938", "pubmed:10897644", "pubmed:10958818", "pubmed:11261364", "pubmed:11451208", "pubmed:11959400", "pubmed:14387833", "pubmed:15321809", "pubmed:15523939", "pubmed:15754725", "pubmed:15797531", "pubmed:15797685", "pubmed:15831910", "pubmed:15990733", "pubmed:16093404", "pubmed:16277678", "pubmed:16380297", "pubmed:16871332", "pubmed:17784727", "pubmed:18788725", "pubmed:19121630", "pubmed:19335717", "pubmed:19355913", "pubmed:24650098", "pubmed:33624660", "pubmed:33965562", "pubmed:33968971", "pubmed:34207319", "pubmed:34219855", "pubmed:7738698", "pubmed:8235383", "pubmed:9040515", "pubmed:9420019", "pubmed:9565830", "pubmed:9683174", "pubmed:9781393", "pubmed:9808640", "pubmed:9808641", "reaxys:100781", "wikipedia.en:Folic_Acid"], "generalized_empirical_formula": ["C19H19N7O6"], "has_alternative_id": ["CHEBI:24075", "CHEBI:42610", "CHEBI:5140", "CHEBI:569217"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:27470"], "inchi_key_string": ["OVBPIULPVIDEAO-LBPRGKRZSA-N"], "inchi_string": ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"], "mass": ["441.404"], "monoisotopic_mass": ["441.13968"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]} |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:30753 resolves to 4-aminobenzoic acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:150-13-0", "drugbank:DB02362", "drugcentral:2049", "ecmdb:ECMDB01392", "gmelin:50150", "hmdb:HMDB0001392", "kegg.compound:C00568", "kegg.drug:D02456", "knapsack:C00001401", "pdb-ccd:PAB", "pubmed:12039592", "pubmed:14745019", "pubmed:15115392", "pubmed:1527790", "pubmed:16290145", "pubmed:17149871", "pubmed:17743450", "pubmed:17800214", "pubmed:19469519", "pubmed:22767283", "pubmed:22994574", "pubmed:23063996", "pubmed:23084339", "pubmed:23144588", "pubmed:23471007", "pubmed:3599019", "pubmed:3820215", "pubmed:3950915", "pubmed:8411009", "pubmed:9406595", "reaxys:471605", "wikipedia.en:4-Aminobenzoic_acid", "ymdb:YMDB00493"], "generalized_empirical_formula": ["C7H7NO2"], "has_alternative_id": ["CHEBI:113372", "CHEBI:1783", "CHEBI:20315", "CHEBI:44778"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30753"], "inchi_key_string": ["ALYNCZNDIQEVRV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"], "mass": ["137.138"], "monoisotopic_mass": ["137.04768"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]} |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:31345 resolves to Calcium pantothenate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:137-08-6", "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278", "pubmed:20553011", "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula": ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"], "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"], "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]} |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:32588 resolves to potassium chloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7447-40-7", "drugbank:DB00761", "kegg.drug:D02060", "metacyc.compound:KCL", "molbase:881", "reaxys:3534978", "wikipedia.en:Potassium_Chloride"], "generalized_empirical_formula": ["Cl.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32588"], "inchi_key_string": ["WCUXLLCKKVVCTQ-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "monoisotopic_mass": ["73.93256"], "smiles_string": ["[Cl-].[K+]"]} |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:49105 resolves to thiamine hydrochloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["agr:IND605711145", "agr:IND606057536", "beilstein:3642937", "beilstein:3851771", "cas:67-03-8", "chemspider:5967", "drugbank:DBSALT000205", "foodb.food:FDB008416", "gmelin:31154", "gmelin:691133", "kegg.drug:D02094", "pubmed:11548854", "pubmed:12224421", "pubmed:21212548", "pubmed:22305197", "pubmed:24399744", "pubmed:25977858", "pubmed:26616989", "pubmed:27163892", "pubmed:28763984", "pubmed:28784494", "pubmed:30131156", "pubmed:31270735", "pubmed:31664290", "pubmed:32009117", "pubmed:32562525", "pubmed:32824791", "reaxys:17124533"], "generalized_empirical_formula": ["C12H17N4OS.Cl.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:49105"], "inchi_key_string": ["DPJRMOMPQZCRJU-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C12H17N4OS.2ClH/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H/q+1;;/p-1"], "mass": ["337.276"], "monoisotopic_mass": ["336.05784"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1.Cl.[Cl-]"]} |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:86158 resolves to calcium chloride dihydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8", "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"], "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass": ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]} |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7791-18-6", "kegg.drug:D04834", "pubmed:24831644", "pubmed:25148974", "pubmed:25430969", "reaxys:11343754"], "generalized_empirical_formula": ["2Cl.6H2O.Mg"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86345"], "inchi_key_string": ["DHRRIBDTHFBPNG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass": ["203.301"], "monoisotopic_mass": ["201.98614"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]} |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned CSV; preferred-term MAPPED rows for every asserted secondary CHEBI key | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:24848": [{"label": "Inositol", "match_type": "preferred_term", "identifier": "CHEBI:24848", "preferred_term": "Inositol", "ontology_id": "CHEBI:24848", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31345": [{"label": "Calcium pantothenate", "match_type": "preferred_term", "identifier": "CHEBI:31345", "preferred_term": "Calcium pantothenate", "ontology_id": "CHEBI:31345", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395; $.meta; all three $.components sections; $.comments[0:2] | supports | TOGO M1395 identifies JCM_M1298 ABSS2. Its main components, seven stock additions, two unquantified gases and separate vitamin recipe are independently enumerated. Original unit and stage boundaries are retained in this review. |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298; JCM 1298 full composition, seven additions, vitamin recipe, gas/pH instruction and page-wide default | supports | Current JCM ABSS2 supplies water 930 ml, four basal salts, seven additions per liter, pH 7.5 with N2/CO2 and a separate vitamin formulation. It differs from TOGO in water and four stock-dose/strength claims; exact conflicts remain explicit. |
| sl-togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538; Only $.components[2] (paragraph 4, SL--7 trace element solution) and $.comments[1] (paragraph 5) | supports | TOGO M538 identifies JCM_M536. Only its SL-7 stock recipe and immediately associated iron/acid mixing instruction are relevant to ABSS2; all other sections are excluded. |
| sl-jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536; Only SL-7 trace element solution subsection, ending before the next Vitamin solution heading | supports | JCM 536 provides the same ten SL-7 stock rows and iron/acid mixing instruction as the scoped TOGO section. Its PHE91 medium and separate vitamin stock are not ABSS2 sources. |
| quantities | /private/tmp/culturemech-review-work-batch014/137/quantity-inventory.json; Complete source-linked quantity decision inventory | context_only | Thirty-seven decisions reconcile all 23 main/addition/vitamin source rows, all 10 referenced SL-7 rows and 4 preparation contexts. Every primary quotation is literal; every provider row excerpt is a literal slice of captured raw JSON. Source discrepancies remain conflict decisions. |
| writer | src/culturemech/import/togo_importer.py; scripts/migrate_solutions_from_ingredients.py; scripts/repair_merged_duplicates.py; _extract_primary_components/_solution_from_item/_extract_preparation_steps; _resolve_solution; repair_ingredient | context_only | Current importer distinguishes primary and named-stock sections; current migrator can create empty cross-reference stubs while copying concentrations. repair_ingredient collapses equal numerical duplicate parts without establishing their preparation-stage identity. This current-code context does not prove exact historical execution or scientific validity of that collapse. |

## Limits And Additional Notes

- The captured current JCM and TOGO recipes disagree, but their retrieval times do not establish when either formulation changed or which version was used during the January import. No silently preferred version or historical correction chronology is inferred.
- Only the SL-7 subsection and its immediately associated preparation instruction are borrowed from JCM 536/TOGO M538. Their basal medium, separate vitamin formulation, other stocks and cultivation instructions are excluded.
- Source solvent additions are not proof of measured final volume. No density, unspecified salt hydrate, gas flow/absolute volume, vitamin-B12 vitamer, inositol stereoisomer or final solute concentration is inferred from a stock name alone.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T094647Z-culturemech-007930-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: abss2 (CultureMech:007930)'
started_at: '2026-10-21T09:35:31Z'
finished_at: '2026-10-21T09:46:47Z'
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
summary: ABSS2 is JCM 1298 via TOGO M1395. Both local layers flatten the vitamin stock,
  relabel volume doses and several milligram stock amounts as g/L, and leave seven
  stock stubs incomplete. Current JCM and TOGO disagree on water and four stock additions,
  including phosphate strength. Preparation, source evidence and DL-pantothenate identity
  require curation; a later owner water repair has not reached the generated target.
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
  - path: data/merge_yaml/merged/ABSS2.yaml
    sha256: 516faaa5fe2e42860a61075f6547cd67aeb0b92a3a906ea9e54b567d262522ec
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml
    sha256: 742d87d09efb2cb661b89fe30ffb94259e9d28704f407754e9a16ab174476153
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
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 137; batch 014 item 7 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirteen task batches
    contain 130 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 132 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007930
targets:
- target_id: CultureMech:007930
  path: data/merge_yaml/merged/ABSS2.yaml
  label: abss2
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ABSS2.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007930
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ABSS2.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch014/137/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch014/137/strict.tsv"
  target_ids:
  - CultureMech:007930
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ABSS2.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007930
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ABSS2.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007930
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
  - CultureMech:007930
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ABSS2.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T09:46:44Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T09:46:44Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ABSS2.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:20.882763Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ABSS2.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch014/137/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:23.965682Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch014/137/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ABSS2.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:26.794008Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ABSS2.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:28.357223Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T09:46:44Z'
  support: supports
  summary: './data/merge_yaml/merged/ABSS2.yaml:1:id: CultureMech:007930

    ./data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml:1:id: CultureMech:007930

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: 'CHEBI:15377 resolves to water; canonical label and live status alone do
    not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"charge": [0.0], "database_cross_reference": ["cas:7732-18-5", "gmelin:117",
    "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001", "metacyc.compound:WATER",
    "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"], "generalized_empirical_formula":
    ["H2O"], "has_alternative_id": ["CHEBI:10743", "CHEBI:13352", "CHEBI:27313", "CHEBI:42043",
    "CHEBI:42857", "CHEBI:43228", "CHEBI:44292", "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15377"], "inchi_key_string":
    ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass":
    ["18.015"], "monoisotopic_mass": ["18.01056"], "smiles_string": ["[H]O[H]"]}'
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: 'CHEBI:15940 resolves to nicotinic acid; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["agr:IND607088605",
    "cas:59-67-6", "chemspider:913", "drugbank:DB00627", "drugcentral:2835", "foodb.food:FDB001014",
    "gmelin:3340", "hmdb:HMDB0001488", "kegg.compound:C00253", "kegg.drug:D00049",
    "knapsack:C00000208", "lincs.smallmolecule:LSM-4676", "metacyc.compound:NIACINE",
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
    "mass": ["123.111"], "monoisotopic_mass": ["123.03203"], "smiles_string": ["O=C(O)c1cccnc1"]}'
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
    {"charge": [0.0], "database_cross_reference": ["cas:58-85-5", "chemspider:149962",
    "drugbank:DB00121", "drugcentral:373", "foodb.food:FDB014510", "gmelin:1918703",
    "hmdb:HMDB0000030", "kegg.compound:C00120", "kegg.drug:D00029", "knapsack:C00000756",
    "lincs.smallmolecule:LSM-3994", "metacyc.compound:BIOTIN", "pdb-ccd:BTN", "pmc:PMC8089577",
    "pubmed:10064317", "pubmed:10215065", "pubmed:10577274", "pubmed:11435506", "pubmed:11481419",
    "pubmed:11800048", "pubmed:12055344", "pubmed:12070309", "pubmed:12603856", "pubmed:12803839",
    "pubmed:15012185", "pubmed:15202718", "pubmed:15272000", "pubmed:15690449", "pubmed:15863846",
    "pubmed:15899401", "pubmed:15992684", "pubmed:16011464", "pubmed:16195795", "pubmed:16419467",
    "pubmed:16676358", "pubmed:16677798", "pubmed:16704206", "pubmed:16769720", "pubmed:17297119",
    "pubmed:1814646", "pubmed:18202531", "pubmed:18452485", "pubmed:18509457", "pubmed:19212411",
    "pubmed:19319844", "pubmed:19727438", "pubmed:19928962", "pubmed:20967359", "pubmed:20974274",
    "pubmed:2100006", "pubmed:21248194", "pubmed:21356565", "pubmed:21373679", "pubmed:21596550",
    "pubmed:21871906", "pubmed:25515858", "pubmed:33346513", "pubmed:33461365", "pubmed:34077272",
    "pubmed:8333586", "pubmed:8750932", "pubmed:9022537", "pubmed:9038855", "pubmed:9094878",
    "pubmed:9164991", "pubmed:9176832", "pubmed:9371938", "pubmed:9416479", "reaxys:86838",
    "wikipedia.en:Biotin"], "generalized_empirical_formula": ["C10H16N2O3S"], "has_alternative_id":
    ["CHEBI:13905", "CHEBI:22882", "CHEBI:22884", "CHEBI:3108", "CHEBI:41236"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:15956"], "inchi_key_string": ["YBJHBAHKTGYVGT-ZKWXMUAHSA-N"],
    "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"],
    "mass": ["244.316"], "monoisotopic_mass": ["244.08816"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]}'
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16526
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:26.337128Z'
  support: supports
  summary: 'CHEBI:16526 resolves to carbon dioxide; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:124-38-9",
    "drugcentral:4256", "gmelin:989", "hmdb:HMDB0001967", "kegg.compound:C00011",
    "kegg.drug:D00004", "metacyc.compound:CARBON-DIOXIDE", "molbase:752", "pdb-ccd:CO2",
    "ppdb:119", "pubmed:10826146", "pubmed:11094503", "pubmed:11584085", "pubmed:11802652",
    "pubmed:14639145", "pubmed:15050588", "pubmed:16591971", "pubmed:16656478", "pubmed:16659660",
    "pubmed:17190796", "pubmed:17448243", "pubmed:17878298", "pubmed:17884085", "pubmed:19043767",
    "pubmed:19259576", "pubmed:19854893", "pubmed:23384758", "pubmed:23828359", "pubmed:24258718",
    "pubmed:8482095", "pubmed:8818713", "pubmed:8869828", "pubmed:9611769", "pubmed:9730350",
    "reaxys:1900390", "umbbd.compound:c0131", "wikipedia.en:Carbon_dioxide"], "generalized_empirical_formula":
    ["CO2"], "has_alternative_id": ["CHEBI:13282", "CHEBI:13283", "CHEBI:13284", "CHEBI:13285",
    "CHEBI:23011", "CHEBI:3283", "CHEBI:48829"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:16526"], "inchi_key_string": ["CURLTUGMZLYLDI-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/CO2/c2-1-3"], "mass": ["44.009"], "monoisotopic_mass": ["43.98983"],
    "smiles_string": ["O=C=O"]}'
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: 'CHEBI:176843 resolves to vitamin B12; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:176843"]}'
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi17997
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:27.385647Z'
  support: supports
  summary: 'CHEBI:17997 resolves to dinitrogen; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"charge": [0.0], "database_cross_reference": ["cas:7727-37-9", "drugcentral:4251",
    "gmelin:150", "hmdb:HMDB0001371", "kegg.compound:C00697", "kegg.drug:D00083",
    "metacyc.compound:NITROGEN-MOLECULE", "pdb-ccd:HDZ", "pubmed:18334638", "pubmed:22237545",
    "reaxys:15940095", "wikipedia.en:Nitrogen"], "generalized_empirical_formula":
    ["N2"], "has_alternative_id": ["CHEBI:13388", "CHEBI:14660", "CHEBI:25365", "CHEBI:43128",
    "CHEBI:7593"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17997"],
    "inchi_key_string": ["IJGRMHOSHXDMSA-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/N2/c1-2"],
    "mass": ["28.014"], "monoisotopic_mass": ["28.00615"], "smiles_string": ["N#N"]}'
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi24848
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_24848
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T07:23:17.153630Z'
  support: supports
  summary: 'CHEBI:24848 resolves to inositol; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"charge": [0.0], "generalized_empirical_formula": ["C6H12O6"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:24848"], "inchi_key_string": ["CDAISMWEOUEBRE-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C6H12O6/c7-1-2(8)4(10)6(12)5(11)3(1)9/h1-12H"], "mass":
    ["180.156"], "monoisotopic_mass": ["180.06339"], "smiles_string": ["OC1C(O)C(O)C(O)C(O)C1O"]}'
  snapshot_sha256: 3fa2e0500a67481ab6bb14c94ab5bf54099850527cad5e97b5f191ea4325ce8d
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: 'CHEBI:26710 resolves to sodium chloride; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5",
    "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL",
    "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula":
    ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string":
    ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"],
    "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]}'
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
    {"charge": [0.0], "database_cross_reference": ["agr:IND606960789", "cas:59-30-3",
    "chemspider:5815", "drugbank:DB00158", "drugcentral:1231", "foodb.food:FDB014504",
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
    "mass": ["441.404"], "monoisotopic_mass": ["441.13968"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]}'
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
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:150-13-0",
    "drugbank:DB02362", "drugcentral:2049", "ecmdb:ECMDB01392", "gmelin:50150", "hmdb:HMDB0001392",
    "kegg.compound:C00568", "kegg.drug:D02456", "knapsack:C00001401", "pdb-ccd:PAB",
    "pubmed:12039592", "pubmed:14745019", "pubmed:15115392", "pubmed:1527790", "pubmed:16290145",
    "pubmed:17149871", "pubmed:17743450", "pubmed:17800214", "pubmed:19469519", "pubmed:22767283",
    "pubmed:22994574", "pubmed:23063996", "pubmed:23084339", "pubmed:23144588", "pubmed:23471007",
    "pubmed:3599019", "pubmed:3820215", "pubmed:3950915", "pubmed:8411009", "pubmed:9406595",
    "reaxys:471605", "wikipedia.en:4-Aminobenzoic_acid", "ymdb:YMDB00493"], "generalized_empirical_formula":
    ["C7H7NO2"], "has_alternative_id": ["CHEBI:113372", "CHEBI:1783", "CHEBI:20315",
    "CHEBI:44778"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30753"],
    "inchi_key_string": ["ALYNCZNDIQEVRV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"],
    "mass": ["137.138"], "monoisotopic_mass": ["137.04768"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]}'
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: 'CHEBI:31345 resolves to Calcium pantothenate; canonical label and live
    status alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:137-08-6",
    "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278", "pubmed:20553011",
    "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula":
    ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"],
    "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"],
    "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]}'
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: 'CHEBI:32588 resolves to potassium chloride; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7447-40-7",
    "drugbank:DB00761", "kegg.drug:D02060", "metacyc.compound:KCL", "molbase:881",
    "reaxys:3534978", "wikipedia.en:Potassium_Chloride"], "generalized_empirical_formula":
    ["Cl.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32588"], "inchi_key_string":
    ["WCUXLLCKKVVCTQ-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.K/h1H;/q;+1/p-1"],
    "mass": ["74.551"], "monoisotopic_mass": ["73.93256"], "smiles_string": ["[Cl-].[K+]"]}'
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: 'CHEBI:49105 resolves to thiamine hydrochloride; canonical label and live
    status alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["agr:IND605711145",
    "agr:IND606057536", "beilstein:3642937", "beilstein:3851771", "cas:67-03-8", "chemspider:5967",
    "drugbank:DBSALT000205", "foodb.food:FDB008416", "gmelin:31154", "gmelin:691133",
    "kegg.drug:D02094", "pubmed:11548854", "pubmed:12224421", "pubmed:21212548", "pubmed:22305197",
    "pubmed:24399744", "pubmed:25977858", "pubmed:26616989", "pubmed:27163892", "pubmed:28763984",
    "pubmed:28784494", "pubmed:30131156", "pubmed:31270735", "pubmed:31664290", "pubmed:32009117",
    "pubmed:32562525", "pubmed:32824791", "reaxys:17124533"], "generalized_empirical_formula":
    ["C12H17N4OS.Cl.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:49105"],
    "inchi_key_string": ["DPJRMOMPQZCRJU-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C12H17N4OS.2ClH/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H/q+1;;/p-1"],
    "mass": ["337.276"], "monoisotopic_mass": ["336.05784"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1.Cl.[Cl-]"]}'
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: 'CHEBI:86158 resolves to calcium chloride dihydrate; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8",
    "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"],
    "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass":
    ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}'
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: 'CHEBI:86345 resolves to magnesium dichloride hexahydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:7791-18-6", "kegg.drug:D04834", "pubmed:24831644", "pubmed:25148974", "pubmed:25430969",
    "reaxys:11343754"], "generalized_empirical_formula": ["2Cl.6H2O.Mg"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:86345"], "inchi_key_string": ["DHRRIBDTHFBPNG-UHFFFAOYSA-L"],
    "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass":
    ["203.301"], "monoisotopic_mass": ["201.98614"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}'
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned CSV; preferred-term MAPPED rows for every asserted secondary
    CHEBI key
  accessed_at: '2026-10-21T09:46:44Z'
  support: supports
  summary: '{"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label":
    "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term":
    "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105":
    [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105",
    "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid",
    "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier":
    "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843",
    "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:15940": [{"label":
    "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940",
    "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:24848": [{"label": "Inositol", "match_type":
    "preferred_term", "identifier": "CHEBI:24848", "preferred_term": "Inositol", "ontology_id":
    "CHEBI:24848", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31345":
    [{"label": "Calcium pantothenate", "match_type": "preferred_term", "identifier":
    "CHEBI:31345", "preferred_term": "Calcium pantothenate", "ontology_id": "CHEBI:31345",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395
  locator: $.meta; all three $.components sections; $.comments[0:2]
  accessed_at: '2026-10-21T09:28:24.720678Z'
  support: supports
  summary: TOGO M1395 identifies JCM_M1298 ABSS2. Its main components, seven stock
    additions, two unquantified gases and separate vitamin recipe are independently
    enumerated. Original unit and stage boundaries are retained in this review.
  snapshot_sha256: 8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590
- evidence_id: jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298
  locator: JCM 1298 full composition, seven additions, vitamin recipe, gas/pH instruction
    and page-wide default
  accessed_at: '2026-10-21T09:28:27.664424Z'
  support: supports
  summary: Current JCM ABSS2 supplies water 930 ml, four basal salts, seven additions
    per liter, pH 7.5 with N2/CO2 and a separate vitamin formulation. It differs from
    TOGO in water and four stock-dose/strength claims; exact conflicts remain explicit.
  snapshot_sha256: 3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3
- evidence_id: sl-togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538
  locator: Only $.components[2] (paragraph 4, SL--7 trace element solution) and $.comments[1]
    (paragraph 5)
  accessed_at: '2026-10-21T09:28:25.633514Z'
  support: supports
  summary: TOGO M538 identifies JCM_M536. Only its SL-7 stock recipe and immediately
    associated iron/acid mixing instruction are relevant to ABSS2; all other sections
    are excluded.
  snapshot_sha256: 73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550
- evidence_id: sl-jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536
  locator: Only SL-7 trace element solution subsection, ending before the next Vitamin
    solution heading
  accessed_at: '2026-10-21T09:30:02.552770Z'
  support: supports
  summary: JCM 536 provides the same ten SL-7 stock rows and iron/acid mixing instruction
    as the scoped TOGO section. Its PHE91 medium and separate vitamin stock are not
    ABSS2 sources.
  snapshot_sha256: ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802
- evidence_id: quantities
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch014/137/quantity-inventory.json
  locator: Complete source-linked quantity decision inventory
  accessed_at: '2026-10-21T09:46:44Z'
  support: context_only
  summary: Thirty-seven decisions reconcile all 23 main/addition/vitamin source rows,
    all 10 referenced SL-7 rows and 4 preparation contexts. Every primary quotation
    is literal; every provider row excerpt is a literal slice of captured raw JSON.
    Source discrepancies remain conflict decisions.
  snapshot_sha256: 8fe978986b54078292b7657123cb526dfbc29b72d375157a8249a41fde178f51
- evidence_id: writer
  kind: record_content
  reference: src/culturemech/import/togo_importer.py; scripts/migrate_solutions_from_ingredients.py;
    scripts/repair_merged_duplicates.py
  locator: _extract_primary_components/_solution_from_item/_extract_preparation_steps;
    _resolve_solution; repair_ingredient
  accessed_at: '2026-10-21T09:46:44Z'
  support: context_only
  summary: Current importer distinguishes primary and named-stock sections; current
    migrator can create empty cross-reference stubs while copying concentrations.
    repair_ingredient collapses equal numerical duplicate parts without establishing
    their preparation-stage identity. This current-code context does not prove exact
    historical execution or scientific validity of that collapse.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007930
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding-coverage
  area: grounding
  topic: Exact primary labels and current secondary linkage coverage
  outcome: supported
  summary: '15 unique asserted CHEBI identifiers resolve with exact labels. Primary
    linkage 15/15 (100.00%); verified current secondary linkage 11/15 (73.33%). This
    is a 0–100 ingredient-instance linkage scale, not scientific correctness. Missing
    current secondary keys: []. Legacy links and chemical-form correctness are assessed
    separately.'
  target_ids:
  - CultureMech:007930
  evidence_ids:
  - record
  - mim
  - chebi15377
  - chebi15940
  - chebi15956
  - chebi16526
  - chebi176843
  - chebi17997
  - chebi24848
  - chebi26710
  - chebi27470
  - chebi30753
  - chebi31345
  - chebi32588
  - chebi49105
  - chebi86158
  - chebi86345
- assessment_id: quantities
  area: quantity
  topic: Every direct, stock, stock-addition and preparation quantity
  outcome: concern
  summary: Thirty-seven decisions reconcile all 23 main/addition/vitamin source rows,
    all 10 referenced SL-7 rows and 4 preparation contexts. Every primary quotation
    is literal; every provider row excerpt is a literal slice of captured raw JSON.
    Source discrepancies remain conflict decisions.
  target_ids:
  - CultureMech:007930
  evidence_ids:
  - record
  - owner-0
  - quantities
  details: '[{"field_path": "ingredients[0].concentration", "decision": "conflict",
    "stage": "basal medium before stock additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "Distilled water 930.0 ml", "source_locator": "JCM1298 basal medium
    before stock additions; primary entry identified by literal text: Distilled water
    930.0 ml", "explanation": "Current JCM water 930 ml conflicts with TOGO main water
    1 L. The generated target 2 g/L also sums the independent vitamin-stock water
    1 L; owner repair changes 2 to 1 but neither restores solvent units nor stock
    scope. Do not infer version chronology or measured final volume.", "provider_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256":
    "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator":
    "$.components[0].items[0]", "provider_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"", "provider_original_amount":
    1, "provider_original_unit": "L"}, {"field_path": "ingredients[1].concentration",
    "decision": "evidence_only", "stage": "basal medium before stock additions", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "NaCl 11.8 g", "source_locator": "JCM1298 basal medium before
    stock additions; primary entry identified by literal text: NaCl 11.8 g", "explanation":
    "Both sources agree on the basal salt mass. The local g/L number agrees on the
    source per-liter recipe basis, but narrow source evidence and stage are absent.
    Source water addition alone does not prove measured final volume.", "provider_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256":
    "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator":
    "$.components[0].items[1]", "provider_quote": "{\n          \"component_name\":
    \"NaCl\",\n          \"volume\": 11.8,\n          \"unit\": \"g\"", "provider_original_amount":
    11.8, "provider_original_unit": "g"}, {"field_path": "ingredients[2].concentration",
    "decision": "evidence_only", "stage": "basal medium before stock additions", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "CaCl 2 ·2H 2 O 0.3 g", "source_locator": "JCM1298 basal medium
    before stock additions; primary entry identified by literal text: CaCl 2 ·2H 2
    O 0.3 g", "explanation": "Both sources agree on the basal salt mass. The local
    g/L number agrees on the source per-liter recipe basis, but narrow source evidence
    and stage are absent. Source water addition alone does not prove measured final
    volume.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[0].items[2]", "provider_quote": "{\n          \"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"", "provider_original_amount":
    0.3, "provider_original_unit": "g"}, {"field_path": "ingredients[3].concentration",
    "decision": "evidence_only", "stage": "basal medium before stock additions", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "MgCl 2 ·6H 2 O 2.2 g", "source_locator": "JCM1298 basal medium
    before stock additions; primary entry identified by literal text: MgCl 2 ·6H 2
    O 2.2 g", "explanation": "Both sources agree on the basal salt mass. The local
    g/L number agrees on the source per-liter recipe basis, but narrow source evidence
    and stage are absent. Source water addition alone does not prove measured final
    volume.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[0].items[3]", "provider_quote": "{\n          \"component_name\":
    \"MgCl2・6H2O\",\n          \"volume\": 2.2,\n          \"unit\": \"g\"", "provider_original_amount":
    2.2, "provider_original_unit": "g"}, {"field_path": "ingredients[4].concentration",
    "decision": "evidence_only", "stage": "basal medium before stock additions", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "KCl 0.4 g", "source_locator": "JCM1298 basal medium before stock
    additions; primary entry identified by literal text: KCl 0.4 g", "explanation":
    "Both sources agree on the basal salt mass. The local g/L number agrees on the
    source per-liter recipe basis, but narrow source evidence and stage are absent.
    Source water addition alone does not prove measured final volume.", "provider_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256":
    "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator":
    "$.components[0].items[4]", "provider_quote": "{\n          \"component_name\":
    \"KCl\",\n          \"volume\": 0.4,\n          \"unit\": \"g\"", "provider_original_amount":
    0.4, "provider_original_unit": "g"}, {"field_path": "solutions[0].concentration",
    "decision": "conflict", "stage": "addition per liter after basal medium cooling",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "1 M NaHCO 3 solution* 30.0 ml", "source_locator": "JCM1298 addition
    per liter after basal medium cooling; primary entry identified by literal text:
    1 M NaHCO 3 solution* 30.0 ml", "explanation": "Current JCM specifies 30 ml of
    1 M bicarbonate, versus TOGO 3 ml of 1 M. Local 3 g/L is neither a valid volume
    dose nor a source-version resolution.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[1].items[0]", "provider_quote": "{\n          \"component_name\":
    \"1 M NaHCO3 solution*\",\n          \"volume\": 3,\n          \"unit\": \"ml\"",
    "provider_original_amount": 3, "provider_original_unit": "ml"}, {"field_path":
    "solutions[1].concentration", "decision": "conflict", "stage": "addition per liter
    after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "100 mM NH 4 Cl solution 10.0 ml", "source_locator": "JCM1298
    addition per liter after basal medium cooling; primary entry identified by literal
    text: 100 mM NH 4 Cl solution 10.0 ml", "explanation": "Current JCM specifies
    10 ml of 100 mM NH4Cl, versus TOGO 20 ul of 100 mM. 20 ul equals 0.020 ml; both
    differ from the local 20 g/L claim.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[1].items[1]", "provider_quote": "{\n          \"component_name\":
    \"100 mM NH4Cl solution\",\n          \"volume\": 20,\n          \"unit\": \"ul\"",
    "provider_original_amount": 20, "provider_original_unit": "ul"}, {"field_path":
    "solutions[2].concentration", "decision": "conflict", "stage": "addition per liter
    after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "100 mM Na 2 HPO 4 solution 10.0 ml", "source_locator": "JCM1298
    addition per liter after basal medium cooling; primary entry identified by literal
    text: 100 mM Na 2 HPO 4 solution 10.0 ml", "explanation": "Current JCM specifies
    10 ml of 100 mM Na2HPO4, versus TOGO 100 ul of 10 mM. 100 ul equals 0.100 ml.
    Both stock strength and addition differ; local 100 g/L is not supported.", "provider_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256":
    "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator":
    "$.components[1].items[2]", "provider_quote": "{\n          \"component_name\":
    \"10 mM Na2HPO4 solution\",\n          \"volume\": 100,\n          \"unit\": \"ul\"",
    "provider_original_amount": 100, "provider_original_unit": "ul"}, {"field_path":
    "solutions[3].concentration", "decision": "correct", "stage": "addition per liter
    after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "500 mM MnO 2 solution 10.0 ml", "source_locator": "JCM1298 addition
    per liter after basal medium cooling; primary entry identified by literal text:
    500 mM MnO 2 solution 10.0 ml", "explanation": "Preserve the original source unit
    and explicit stage. The current G_PER_L number cannot substitute for a stock dose
    or a stock-formulation quantity.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[1].items[3]", "provider_quote": "{\n          \"component_name\":
    \"500 mM MnO2 solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
    "provider_original_amount": 10, "provider_original_unit": "ml"}, {"field_path":
    "solutions[4].concentration", "decision": "correct", "stage": "addition per liter
    after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "300 mM Na 2 S 2 O 3 solution 10.0 ml", "source_locator": "JCM1298
    addition per liter after basal medium cooling; primary entry identified by literal
    text: 300 mM Na 2 S 2 O 3 solution 10.0 ml", "explanation": "Preserve the original
    source unit and explicit stage. The current G_PER_L number cannot substitute for
    a stock dose or a stock-formulation quantity.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[1].items[4]", "provider_quote": "{\n          \"component_name\":
    \"300 mM Na2S2O3 solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
    "provider_original_amount": 10, "provider_original_unit": "ml"}, {"field_path":
    "solutions[5].concentration", "decision": "conflict", "stage": "addition per liter
    after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "SL-7 trace element solution (see Medium No. 536 ) 1.0 ml", "source_locator":
    "JCM1298 addition per liter after basal medium cooling; primary entry identified
    by literal text: SL-7 trace element solution (see Medium No. 536 ) 1.0 ml", "explanation":
    "Current JCM specifies 1 ml SL-7, versus TOGO 100 ul (0.100 ml). The stock composition
    itself agrees across the scoped external sources, but that does not resolve the
    differing addition doses.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[1].items[5]", "provider_quote": "{\n          \"component_name\":
    \"SL--7 trace element solution (see Medium [M538])\",\n          \"volume\": 100,\n          \"unit\":
    \"ul\"", "provider_original_amount": 100, "provider_original_unit": "ul"}, {"field_path":
    "solutions[6].concentration", "decision": "correct", "stage": "addition per liter
    after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "Vitamin solution* (see below) 0.42 ml", "source_locator": "JCM1298
    addition per liter after basal medium cooling; primary entry identified by literal
    text: Vitamin solution* (see below) 0.42 ml", "explanation": "TOGO 420 ul equals
    JCM 0.42 ml exactly (420/1000=0.42). This is a vitamin-stock addition per liter,
    not 420 g/L or an instruction to add every undiluted stock ingredient directly.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[1].items[6]", "provider_quote": "{\n          \"component_name\":
    \"Vitamin solution* (see below)\",\n          \"volume\": 420,\n          \"unit\":
    \"ul\"", "provider_original_amount": 420, "provider_original_unit": "ul"}, {"field_path":
    "ingredients[5].concentration", "decision": "not_quantified", "stage": "addition
    per liter after basal medium cooling", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture", "source_locator": "JCM1298
    pH-adjustment gas-mixture sentence", "explanation": "Source gives N2/CO2 at 4:1
    by volume while adjusting pH 7.5, but no absolute gas dose, flow, headspace volume
    or dissolved-gas concentration. VARIABLE does not preserve the missing gas ratio
    and preparation stage.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[1].items[7]", "provider_quote": "{\n          \"component_name\":
    \"Carbon dioxide gas\"", "provider_original_amount": null, "provider_original_unit":
    null}, {"field_path": "ingredients[6].concentration", "decision": "not_quantified",
    "stage": "addition per liter after basal medium cooling", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture", "source_locator": "JCM1298
    pH-adjustment gas-mixture sentence", "explanation": "Source gives N2/CO2 at 4:1
    by volume while adjusting pH 7.5, but no absolute gas dose, flow, headspace volume
    or dissolved-gas concentration. VARIABLE does not preserve the missing gas ratio
    and preparation stage.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[1].items[8]", "provider_quote": "{\n          \"component_name\":
    \"Nitrogen gas\"", "provider_original_amount": null, "provider_original_unit":
    null}, {"field_path": "ingredients[0].concentration", "decision": "correct", "stage":
    "vitamin stock before its 0.42 ml per-liter addition", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "Distilled water 1.0 L", "source_locator": "JCM1298 vitamin stock
    before its 0.42 ml per-liter addition; primary entry identified by literal text:
    Distilled water 1.0 L", "explanation": "Both sources agree on this separately
    prepared vitamin-stock row. Preserve it within the stock, not as a direct medium
    component or summed main solvent.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[2].items[0]", "provider_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"", "provider_original_amount":
    1, "provider_original_unit": "L"}, {"field_path": "ingredients[7].concentration",
    "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "Biotin 10.0 mg", "source_locator": "JCM1298 vitamin stock before
    its 0.42 ml per-liter addition; primary entry identified by literal text: Biotin
    10.0 mg", "explanation": "Both sources agree on this separately prepared vitamin-stock
    row. Preserve it within the stock, not as a direct medium component or summed
    main solvent. The source 10 mg equals 0.01 g within that stock; the current number
    in g/L is not that conversion and still omits subsequent stock dilution.", "provider_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256":
    "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator":
    "$.components[2].items[1]", "provider_quote": "{\n          \"component_name\":
    \"Biotin\",\n          \"volume\": 10,\n          \"unit\": \"mg\"", "provider_original_amount":
    10, "provider_original_unit": "mg"}, {"field_path": "ingredients[8].concentration",
    "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "p -Aminobenzoic acid 100.0 mg", "source_locator": "JCM1298 vitamin
    stock before its 0.42 ml per-liter addition; primary entry identified by literal
    text: p -Aminobenzoic acid 100.0 mg", "explanation": "Both sources agree on this
    separately prepared vitamin-stock row. Preserve it within the stock, not as a
    direct medium component or summed main solvent. The source 100 mg equals 0.1 g
    within that stock; the current number in g/L is not that conversion and still
    omits subsequent stock dilution.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[2].items[2]", "provider_quote": "{\n          \"component_name\":
    \"p-Aminobenzoic acid\",\n          \"volume\": 100,\n          \"unit\": \"mg\"",
    "provider_original_amount": 100, "provider_original_unit": "mg"}, {"field_path":
    "ingredients[9].concentration", "decision": "correct", "stage": "vitamin stock
    before its 0.42 ml per-liter addition", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "Thiamine-HCl 2.0 g", "source_locator": "JCM1298 vitamin stock
    before its 0.42 ml per-liter addition; primary entry identified by literal text:
    Thiamine-HCl 2.0 g", "explanation": "Both sources agree on this separately prepared
    vitamin-stock row. Preserve it within the stock, not as a direct medium component
    or summed main solvent.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[2].items[3]", "provider_quote": "{\n          \"component_name\":
    \"Thiamine-HCl\",\n          \"volume\": 2,\n          \"unit\": \"g\"", "provider_original_amount":
    2, "provider_original_unit": "g"}, {"field_path": "ingredients[10].concentration",
    "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "Folic acid 10.0 mg", "source_locator": "JCM1298 vitamin stock
    before its 0.42 ml per-liter addition; primary entry identified by literal text:
    Folic acid 10.0 mg", "explanation": "Both sources agree on this separately prepared
    vitamin-stock row. Preserve it within the stock, not as a direct medium component
    or summed main solvent. The source 10 mg equals 0.01 g within that stock; the
    current number in g/L is not that conversion and still omits subsequent stock
    dilution.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[2].items[4]", "provider_quote": "{\n          \"component_name\":
    \"Folic acid\",\n          \"volume\": 10,\n          \"unit\": \"mg\"", "provider_original_amount":
    10, "provider_original_unit": "mg"}, {"field_path": "ingredients[11].concentration",
    "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "Vitamin B 12 10.0 mg", "source_locator": "JCM1298 vitamin stock
    before its 0.42 ml per-liter addition; primary entry identified by literal text:
    Vitamin B 12 10.0 mg", "explanation": "Both sources agree on this separately prepared
    vitamin-stock row. Preserve it within the stock, not as a direct medium component
    or summed main solvent. The source 10 mg equals 0.01 g within that stock; the
    current number in g/L is not that conversion and still omits subsequent stock
    dilution.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[2].items[5]", "provider_quote": "{\n          \"component_name\":
    \"Vitamin B12\",\n          \"volume\": 10,\n          \"unit\": \"mg\"", "provider_original_amount":
    10, "provider_original_unit": "mg"}, {"field_path": "ingredients[12].concentration",
    "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "Nicotinic acid 1.0 g", "source_locator": "JCM1298 vitamin stock
    before its 0.42 ml per-liter addition; primary entry identified by literal text:
    Nicotinic acid 1.0 g", "explanation": "Both sources agree on this separately prepared
    vitamin-stock row. Preserve it within the stock, not as a direct medium component
    or summed main solvent.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395",
    "provider_sha256": "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590",
    "provider_locator": "$.components[2].items[6]", "provider_quote": "{\n          \"component_name\":
    \"Nicotinic acid\",\n          \"volume\": 1,\n          \"unit\": \"g\"", "provider_original_amount":
    1, "provider_original_unit": "g"}, {"field_path": "ingredients[13].concentration",
    "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "Inositol 10.0 mg", "source_locator": "JCM1298 vitamin stock before
    its 0.42 ml per-liter addition; primary entry identified by literal text: Inositol
    10.0 mg", "explanation": "Both sources agree on this separately prepared vitamin-stock
    row. Preserve it within the stock, not as a direct medium component or summed
    main solvent. The source 10 mg equals 0.01 g within that stock; the current number
    in g/L is not that conversion and still omits subsequent stock dilution.", "provider_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256":
    "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator":
    "$.components[2].items[7]", "provider_quote": "{\n          \"component_name\":
    \"Inositol\",\n          \"volume\": 10,\n          \"unit\": \"mg\"", "provider_original_amount":
    10, "provider_original_unit": "mg"}, {"field_path": "ingredients[14].concentration",
    "decision": "correct", "stage": "vitamin stock before its 0.42 ml per-liter addition",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "DL-Calcium pantothenate 1.0 g", "source_locator": "JCM1298 vitamin
    stock before its 0.42 ml per-liter addition; primary entry identified by literal
    text: DL-Calcium pantothenate 1.0 g", "explanation": "Both sources agree on this
    separately prepared vitamin-stock row. Preserve it within the stock, not as a
    direct medium component or summed main solvent. Explicit DL material must not
    be narrowed to a single stereoisomer by the linked ontology structure.", "provider_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1395", "provider_sha256":
    "8eb0bf115725f7f9b83bdff2f90a4ba4903899207138cb746d9761576bb34590", "provider_locator":
    "$.components[2].items[8]", "provider_quote": "{\n          \"component_name\":
    \"DL-Calcium pantothenate\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
    "provider_original_amount": 1, "provider_original_unit": "g"}, {"field_path":
    "solutions[5].composition (missing source item 25% HCl (7.7 M))", "decision":
    "add", "stage": "SL-7 stock preparation", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536",
    "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802",
    "source_quote": "25% HCl (7.7 M) 10.0 ml", "source_locator": "JCM536 SL-7 subsection
    only; exact 25% HCl (7.7 M) row", "explanation": "Source-supported nested SL-7
    stock composition is absent from the empty local stub. Keep its stock batch and
    later source-dependent addition separate; do not import the PHE91 basal or vitamin
    recipes. Preserve the source 25% and 7.7 M labels without inventing the unstated
    percentage convention or performing a density conversion.", "provider_reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538", "provider_sha256":
    "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550", "provider_locator":
    "$.components[2].items[0]", "provider_quote": "{\n          \"component_name\":
    \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
    "original_source_amount": 10, "original_source_unit": "ml"}, {"field_path": "solutions[5].composition
    (missing source item Distilled water)", "decision": "add", "stage": "SL-7 stock
    preparation", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536",
    "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802",
    "source_quote": "Distilled water 1.0 L", "source_locator": "JCM536 SL-7 subsection
    only; exact Distilled water row", "explanation": "Source-supported nested SL-7
    stock composition is absent from the empty local stub. Keep its stock batch and
    later source-dependent addition separate; do not import the PHE91 basal or vitamin
    recipes.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538",
    "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550",
    "provider_locator": "$.components[2].items[1]", "provider_quote": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"", "original_source_amount":
    1, "original_source_unit": "L"}, {"field_path": "solutions[5].composition (missing
    source item Na2MoO4・2H2O)", "decision": "add", "stage": "SL-7 stock preparation",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536",
    "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802",
    "source_quote": "Na 2 MoO 4 ·2H 2 O 36.0 mg", "source_locator": "JCM536 SL-7 subsection
    only; exact Na2MoO4・2H2O row", "explanation": "Source-supported nested SL-7 stock
    composition is absent from the empty local stub. Keep its stock batch and later
    source-dependent addition separate; do not import the PHE91 basal or vitamin recipes.
    Within this stock only, 36 mg=0.036 g.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538",
    "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550",
    "provider_locator": "$.components[2].items[2]", "provider_quote": "{\n          \"component_name\":
    \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\"", "original_source_amount":
    36, "original_source_unit": "mg"}, {"field_path": "solutions[5].composition (missing
    source item H3BO3)", "decision": "add", "stage": "SL-7 stock preparation", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536", "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802",
    "source_quote": "H 3 BO 3 62.0 mg", "source_locator": "JCM536 SL-7 subsection
    only; exact H3BO3 row", "explanation": "Source-supported nested SL-7 stock composition
    is absent from the empty local stub. Keep its stock batch and later source-dependent
    addition separate; do not import the PHE91 basal or vitamin recipes. Within this
    stock only, 62 mg=0.062 g.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538",
    "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550",
    "provider_locator": "$.components[2].items[3]", "provider_quote": "{\n          \"component_name\":
    \"H3BO3\",\n          \"volume\": 62,\n          \"unit\": \"mg\"", "original_source_amount":
    62, "original_source_unit": "mg"}, {"field_path": "solutions[5].composition (missing
    source item MnCl2・4H2O)", "decision": "add", "stage": "SL-7 stock preparation",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536",
    "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802",
    "source_quote": "MnCl 2 ·4H 2 O 100.0 mg", "source_locator": "JCM536 SL-7 subsection
    only; exact MnCl2・4H2O row", "explanation": "Source-supported nested SL-7 stock
    composition is absent from the empty local stub. Keep its stock batch and later
    source-dependent addition separate; do not import the PHE91 basal or vitamin recipes.
    Within this stock only, 100 mg=0.1 g.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538",
    "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550",
    "provider_locator": "$.components[2].items[4]", "provider_quote": "{\n          \"component_name\":
    \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\"", "original_source_amount":
    100, "original_source_unit": "mg"}, {"field_path": "solutions[5].composition (missing
    source item CoCl2・6H2O)", "decision": "add", "stage": "SL-7 stock preparation",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536",
    "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802",
    "source_quote": "CoCl 2 ·6H 2 O 190.0 mg", "source_locator": "JCM536 SL-7 subsection
    only; exact CoCl2・6H2O row", "explanation": "Source-supported nested SL-7 stock
    composition is absent from the empty local stub. Keep its stock batch and later
    source-dependent addition separate; do not import the PHE91 basal or vitamin recipes.
    Within this stock only, 190 mg=0.19 g.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538",
    "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550",
    "provider_locator": "$.components[2].items[5]", "provider_quote": "{\n          \"component_name\":
    \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\"", "original_source_amount":
    190, "original_source_unit": "mg"}, {"field_path": "solutions[5].composition (missing
    source item NiCl2・6H2O)", "decision": "add", "stage": "SL-7 stock preparation",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536",
    "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802",
    "source_quote": "NiCl 2 ·6H 2 O 24.0 mg", "source_locator": "JCM536 SL-7 subsection
    only; exact NiCl2・6H2O row", "explanation": "Source-supported nested SL-7 stock
    composition is absent from the empty local stub. Keep its stock batch and later
    source-dependent addition separate; do not import the PHE91 basal or vitamin recipes.
    Within this stock only, 24 mg=0.024 g.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538",
    "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550",
    "provider_locator": "$.components[2].items[6]", "provider_quote": "{\n          \"component_name\":
    \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\"", "original_source_amount":
    24, "original_source_unit": "mg"}, {"field_path": "solutions[5].composition (missing
    source item CuCl2・2H2O)", "decision": "add", "stage": "SL-7 stock preparation",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536",
    "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802",
    "source_quote": "CuCl 2 ·2H 2 O 17.0 mg", "source_locator": "JCM536 SL-7 subsection
    only; exact CuCl2・2H2O row", "explanation": "Source-supported nested SL-7 stock
    composition is absent from the empty local stub. Keep its stock batch and later
    source-dependent addition separate; do not import the PHE91 basal or vitamin recipes.
    Within this stock only, 17 mg=0.017 g.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538",
    "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550",
    "provider_locator": "$.components[2].items[7]", "provider_quote": "{\n          \"component_name\":
    \"CuCl2・2H2O\",\n          \"volume\": 17,\n          \"unit\": \"mg\"", "original_source_amount":
    17, "original_source_unit": "mg"}, {"field_path": "solutions[5].composition (missing
    source item ZnCl2)", "decision": "add", "stage": "SL-7 stock preparation", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536", "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802",
    "source_quote": "ZnCl 2 70.0 mg", "source_locator": "JCM536 SL-7 subsection only;
    exact ZnCl2 row", "explanation": "Source-supported nested SL-7 stock composition
    is absent from the empty local stub. Keep its stock batch and later source-dependent
    addition separate; do not import the PHE91 basal or vitamin recipes. Within this
    stock only, 70 mg=0.07 g.", "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538",
    "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550",
    "provider_locator": "$.components[2].items[8]", "provider_quote": "{\n          \"component_name\":
    \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\"", "original_source_amount":
    70, "original_source_unit": "mg"}, {"field_path": "solutions[5].composition (missing
    source item FeCl2・4H2O)", "decision": "add", "stage": "SL-7 stock preparation",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536",
    "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802",
    "source_quote": "FeCl 2 ·4H 2 O 1.5 g", "source_locator": "JCM536 SL-7 subsection
    only; exact FeCl2・4H2O row", "explanation": "Source-supported nested SL-7 stock
    composition is absent from the empty local stub. Keep its stock batch and later
    source-dependent addition separate; do not import the PHE91 basal or vitamin recipes.",
    "provider_reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M538",
    "provider_sha256": "73fa4756b0dae7e23f67e507276298997f7266a486e79548816dadcc9d12d550",
    "provider_locator": "$.components[2].items[9]", "provider_quote": "{\n          \"component_name\":
    \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"", "original_source_amount":
    1.5, "original_source_unit": "g"}, {"field_path": "ph_value; preparation_steps",
    "decision": "add", "stage": "gas-mediated pH adjustment", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298", "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "Adjust pH to 7.5 by bubbling", "source_locator": "JCM1298 preparation/default",
    "explanation": "Both layers omit source target pH 7.5 and its adjustment stage.
    This is a target pH, not a measured post-growth value."}, {"field_path": "sterilization;
    preparation_steps", "decision": "add", "stage": "JCM default for autoclaved components",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C
    for 15 min.", "source_locator": "JCM1298 preparation/default", "explanation":
    "Retain the primary page-wide default with the explicit starred filter-sterilization
    exceptions. Do not apply the default to the starred bicarbonate/vitamin stocks."},
    {"field_path": "preparation_steps; solutions[*].preparation_notes", "decision":
    "add", "stage": "post-cooling additions", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1298",
    "source_sha256": "3102cbc5d456c03492e7995b39ad044e31d4087a3f335565595307288faa2dc3",
    "source_quote": "After cooling, aseptically and anaerobically add per liter the
    following solutions (autoclaved or *filter-sterilized):", "source_locator": "JCM1298
    preparation/default", "explanation": "Retain the source ordering, aseptic/anaerobic
    context and per-liter basis; stock names alone do not encode this preparation."},
    {"field_path": "solutions[5].preparation_notes", "decision": "add", "stage": "SL-7
    subsection preparation only", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=536",
    "source_sha256": "ae766826b5764300ae505b08d305d7d89822c87f3934e9c5cec1c93a770be802",
    "source_quote": "Initially, dissolve FeCl 2 ·4H 2 O in 25% HCl, then add distilled
    water followed by the other components.", "source_locator": "JCM536 SL-7 subsection
    ending before Vitamin solution", "explanation": "Preserve only this directly associated
    stock instruction; no other PHE91 preparation is imported."}]'
- assessment_id: identity
  area: identity
  topic: Exact medium accession and linked source scope
  outcome: supported
  summary: TOGO M1395 and JCM1298 denote ABSS2. The linked M538 denotes JCM536 PHE91,
    but the explicit cross-reference is only to its SL-7 stock; that stock section
    agrees with JCM. This does not make the full PHE91 medium or its other stocks
    part of ABSS2.
  target_ids:
  - CultureMech:007930
  evidence_ids:
  - record
  - owner-0
  - id-search
  - togo
  - jcm
  - sl-togo
  - sl-jcm
- assessment_id: versions
  area: consistency
  topic: Current primary and provider conflicts
  outcome: concern
  summary: Water differs930 ml versus 1 L. Bicarbonate differs 30 versus 3 ml; ammonium
    chloride 10 ml versus 20 ul; phosphate 100 mM/10 ml versus 10 mM/100 ul; SL-7
    differs 1 ml versus 100 ul. Vitamin 420 ul equals 0.42 ml and manganese/thiosulfate
    each 10 ml agree. Retrieval timestamps do not establish the origin or chronological
    direction of differences.
  target_ids:
  - CultureMech:007930
  evidence_ids:
  - jcm
  - togo
  - quantities
- assessment_id: forms
  area: grounding
  topic: Source salts, vitamins and stereochemistry
  outcome: concern
  summary: Basal calcium dihydrate and magnesium hexahydrate are correctly named and
    grounded. Generic vitamin B12 and inositol retain broad terms without invented
    vitamer/isomer specificity. Thiamine-HCl is retained without guessing an additional
    hydrate. DL-calcium pantothenate conflicts with the explicit single-stereoisomer
    structure in CHEBI:31345 despite its generic canonical label and a live MIM row;
    two REJECTED preferred-term rows in the same index are not proof that the live
    mapped row is absent.
  target_ids:
  - CultureMech:007930
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - mim
  - chebi31345
  - chebi176843
  - chebi24848
  - chebi49105
  - chebi86158
  - chebi86345
- assessment_id: stocks
  area: completeness
  topic: Seven local stock stubs and source-linked composition
  outcome: concern
  summary: All seven solution entries have empty compositions and Unknown solution
    names. Five stock names supply source strengths, but dose and strength must remain
    separate, including the explicit phosphate-source conflict. The exact vitamin
    recipe is flattened into direct ingredients; SL-7 has a resolvable ten-row external
    definition. No cyclic expansion is necessary and unrelated referenced-medium stocks
    are excluded.
  target_ids:
  - CultureMech:007930
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - sl-jcm
  - sl-togo
  - quantities
- assessment_id: preparation
  area: completeness
  topic: Sterilization, sequencing, gas ratio and target pH
  outcome: concern
  summary: Both sources require main autoclaving, cooling, aseptic/anaerobic stock
    additions and target pH 7.5 using N2/CO2 at 4:1(v/v). JCM supplies the page-wide
    121 C/15 min default and stars bicarbonate/vitamin for filtration. None of these
    preparation details survives in either local layer. Gas VARIABLE values are intentionally
    unquantified but cannot replace the missing ratio/context.
  target_ids:
  - CultureMech:007930
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - quantities
- assessment_id: family
  area: scope
  topic: Classification and biological scope
  outcome: concern
  summary: LIQUID is consistent with a non-agar medium; it does not assert every material
    is fully dissolved. COMPLEX/UNDEFINED lacks reconciliation with the explicitly
    enumerated salt/vitamin/trace recipe and should be reassessed after the stock
    and source-version corrections. No target organism, strain, demonstrated growth,
    parent, native variant or KG match is asserted. Do not infer biological outcomes
    from this recipe alone.
  target_ids:
  - CultureMech:007930
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - sl-jcm
- assessment_id: history
  area: provenance
  topic: Owner/target disagreement and claim evidence
  outcome: concern
  summary: All 12 target and 12 owner timestamps include timezones. The target ends
    with its August merge; owner ends with September duplicate repair, changing water
    2 to 1 and its note. All other ingredients and stocks agree. That repair does
    not recover distinct stock/main water stages or volume units. Neither fully read
    layer contains claim-level source excerpts or preparation references; canonical
    reference checking does not establish missing scientific support.
  target_ids:
  - CultureMech:007930
  evidence_ids:
  - record
  - owner-0
  - writer
  - validate-references
findings:
- finding_id: f1
  issue_key: CM007930-unit-and-stock-stage-collapse
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock quantities and additions are represented as direct g/L
  description: Eight vitamin-stock components are flattened into the medium. Five
    vitamin milligram numbers are relabeled as g/L; three gram quantities remain at
    stock scale. All seven volume additions become g/L, and separate main/vitamin
    water quantities are conflated. This materially changes the formulation despite
    passing structure/term checks.
  target_ids:
  - CultureMech:007930
  field_paths:
  - ingredients[*].concentration
  - solutions[*].concentration
  - solutions[6].composition
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - quantities
  - writer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CM007930-unresolved-source-version
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Current primary and TOGO disagree on five formulation claims
  description: The disagreement concerns main water and bicarbonate, ammonium chloride,
    phosphate and SL-7 additions; phosphate also differs in stock strength. Equal
    names and successful lookup cannot select a source version or date when it changed.
  target_ids:
  - CultureMech:007930
  field_paths:
  - ingredients[0]
  - solutions[0]
  - solutions[1]
  - solutions[2]
  - solutions[5]
  - references
  evidence_ids:
  - jcm
  - togo
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: CM007930-stock-definitions-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source-defined stocks remain empty placeholders
  description: The vitamin formulation and ten-row SL-7 recipe are accessible, but
    all seven local solution compositions remain empty and their names say Unknown
    solution. Named molar stocks also lack structured source-scoped strength/identity
    context.
  target_ids:
  - CultureMech:007930
  field_paths:
  - solutions[*].composition
  - solutions[*].name
  - solutions[*].preparation_notes
  evidence_ids:
  - record
  - owner-0
  - jcm
  - sl-jcm
  - sl-togo
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: CM007930-preparation-and-ph-omission
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation, gas ratio and target pH are absent
  description: Neither layer preserves the source main autoclaving, cooling, aseptic/anaerobic
    additions, starred filtration exceptions, N2/CO2 ratio 4:1(v/v), or target pH
    7.5. JCM’s page-wide autoclave default must remain subordinate to the explicit
    stock exceptions.
  target_ids:
  - CultureMech:007930
  field_paths:
  - preparation_steps
  - sterilization
  - ph_value
  - ingredients[5:7]
  - solutions[*].preparation_notes
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: CM007930-dl-pantothenate-structure
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: DL material maps to a stereospecific calcium pantothenate structure
  description: Both recipe sources and preferred terms explicitly specify DL-calcium
    pantothenate. CHEBI:31345 contains stereospecified pantothenate structures; its
    generic label and valid MIM preferred-term row do not establish correspondence
    to the DL material.
  target_ids:
  - CultureMech:007930
  field_paths:
  - ingredients[14].term
  - ingredients[14].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - chebi31345
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: CM007930-owner-water-and-evidence-drift
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated water differs from its maintained owner and source evidence is
    absent
  description: The owner’s September repair changes the duplicate-summed water 2 to
    1 while the generated target remains 2. Neither g/L value represents the source
    solvent correctly, so merely propagating the owner value is insufficient. Source
    claims also lack narrow evidence despite generic source URLs. COMPLEX/UNDEFINED
    requires source-scoped reassessment.
  target_ids:
  - CultureMech:007930
  field_paths:
  - ingredients[0]
  - curation_history
  - references
  - ingredients[*].evidence
  - medium_type
  - composition_type
  evidence_ids:
  - record
  - owner-0
  - writer
  - jcm
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml
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
  description: Restore exact original units and main/stock/addition boundaries. Preserve
    source-version conflicts explicitly and do not derive final concentrations without
    a verified volume basis.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007930
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml
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
  description: Resolve the intended accession/version using source-specific provenance,
    retain both conflicting captures and make any version choice explicit. Do not
    average or silently substitute a current primary value into an undocumented historical
    variant.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007930
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml
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
  description: Represent each exact source stock and its strength independently of
    its addition dose; preserve vitamin and SL-7 compositions without flattening.
    Scope M538/JCM536 only to SL-7, and resolve unsupported forms rather than inventing
    salt hydrates.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007930
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml
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
  description: Retain exact source preparation order, target pH, gas ratio and scoped
    sterilization instructions with narrow quotations. Do not invent absolute gas
    quantities, flow, incubation conditions or a measured final pH.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007930
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml
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
  description: Resolve the exact DL source material against a verified ontology representation
    or explicitly retain unresolved grounding. Preserve the stock amount and do not
    substitute a D-only or L-only form by name similarity.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:007930
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml
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
  description: Correct the maintained scientific representation first, preserve append-only
    history, attach source-version-specific excerpts and then regenerate with merge/freshness
    checks. Reassess composition classification from the corrected complete stock-aware
    formulation.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:007930
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1395_ABSS2.yaml
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
- The captured current JCM and TOGO recipes disagree, but their retrieval times do
  not establish when either formulation changed or which version was used during the
  January import. No silently preferred version or historical correction chronology
  is inferred.
- Only the SL-7 subsection and its immediately associated preparation instruction
  are borrowed from JCM 536/TOGO M538. Their basal medium, separate vitamin formulation,
  other stocks and cultivation instructions are excluded.
- Source solvent additions are not proof of measured final volume. No density, unspecified
  salt hydrate, gas flow/absolute volume, vitamin-B12 vitamer, inositol stereoisomer
  or final solute concentration is inferred from a stock name alone.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-014
- generated-medium
```
