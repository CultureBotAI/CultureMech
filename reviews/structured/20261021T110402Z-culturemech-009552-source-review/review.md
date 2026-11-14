# Source and formulation review: acidilobus_medium (CultureMech:009552)

- Review: 20261021T110402Z-culturemech-009552-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T10:48:47Z
- Finished UTC: 2026-10-21T11:04:02Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact TOGO M303/JCM 308 medium and all three referenced stock definitions resolve. Water, resazurin and stock doses have incorrect units, source batch amounts are presented as unqualified final concentrations, and three stock compositions and source preparation are missing. The sulfur CHEBI concept is live, but its distinct legacy MediaIngredientMech correspondence remains unresolved; the scientific review is partial for that required identity check.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence. Required historical identity verification of MediaIngredientMech:001072 is unavailable; live CHEBI metadata does not resolve that separate linkage.

Selection: Task review 169; batch 017 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding sixteen task batches contain 160 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 162 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009552 | data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml | generated | acidilobus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009552 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009552 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch017/169/strict.tsv |
| validate-terms | passed | True | CultureMech:009552 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009552 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009552 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Historical MediaIngredientMech:001072 correspondence | unavailable | True | CultureMech:009552 | Exact historical source correspondence remains unavailable in the inspected pinned catalogue/tree and current local inputs. No fuzzy replacement was selected. Live CHEBI:33403 existence is a different check. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009552.

The four documented recipes completed; interpret the scope of each separately.

### Exact source accession and stock reference resolution

identity: supported. Targets: CultureMech:009552.

TOGO M303 identifies JCM 308; its maintained owner is exact. M180 maps to JCM 187 and M190 to JCM 197, with the three named subsections independently resolved by MediaDive stock IDs 3846, 3847 and 3861. Their parent media are not substitutions for this medium.

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:009552.

12 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 12/13 primary and 6/13 secondary instances; All current CHEBI-based secondary keys have exact pinned MIM rows; this does not verify the separate historical MediaIngredientMech:001072 link, whose unresolved correspondence makes grounding a concern. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 13: primary 92.31%; secondary 46.15%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Distinct legacy sulfur identifier

grounding: unknown. Targets: CultureMech:009552.

CHEBI:33403 is a live elemental-sulfur concept compatible with the source powder description. That does not establish what MediaIngredientMech:001072 historically denoted. The exact legacy link remains unresolved, so scope and completion remain partial.

### Every direct amount, stock dose, missing stock constituent and preparation quantity

quantity: concern. Targets: CultureMech:009552.

The 45-row inventory covers all 13 direct ingredients, three stock doses, 22 missing stock rows and seven preparation contexts. Literal source masses and liquid additions remain distinct from provider-normalized concentrations and from unmeasured final volumes.

[{"field_path": "ingredients[0].concentration", "current": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "Distilled water", "volume": 1, "unit": "L"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[0]", "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "The literal 1 L is a water addition, not 1 g/L and not a final-volume make-up. Preserve solvent/batch scope."}, {"field_path": "ingredients[1].concentration", "current": {"value": "0.33", "unit": "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "CaCl2・2H2O", "volume": 0.33, "unit": "g"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[1]", "exact_source_quote": "\"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "The numeric value matches the original mass in grams, but the source specifies a receiving batch with 1 L water plus liquid additions, not that mass per exact final liter. Correct the unsupported denominator while retaining the original mass and form. The corroborating provider explicitly uses 1012 ml and reports a different g_l; that declared calculation basis is not a measured final volume."}, {"field_path": "ingredients[2].concentration", "current": {"value": "0.33", "unit": "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "KH2PO4", "volume": 0.33, "unit": "g"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[2]", "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "The numeric value matches the original mass in grams, but the source specifies a receiving batch with 1 L water plus liquid additions, not that mass per exact final liter. Correct the unsupported denominator while retaining the original mass and form. The corroborating provider explicitly uses 1012 ml and reports a different g_l; that declared calculation basis is not a measured final volume."}, {"field_path": "ingredients[3].concentration", "current": {"value": "0.33", "unit": "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "NH4Cl", "volume": 0.33, "unit": "g"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[3]", "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "The numeric value matches the original mass in grams, but the source specifies a receiving batch with 1 L water plus liquid additions, not that mass per exact final liter. Correct the unsupported denominator while retaining the original mass and form. The corroborating provider explicitly uses 1012 ml and reports a different g_l; that declared calculation basis is not a measured final volume."}, {"field_path": "ingredients[4].concentration", "current": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "Resazurin", "volume": 1, "unit": "mg"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[4]", "exact_source_quote": "\"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "The source gives 1 mg of resazurin, not 1 g/L. 1 mg equals 0.001 g as an absolute mass; no final-medium conversion is justified from water alone."}, {"field_path": "ingredients[5].concentration", "current": {"value": "0.33", "unit": "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "MgCl2・6H2O", "volume": 0.33, "unit": "g"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[5]", "exact_source_quote": "\"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "The numeric value matches the original mass in grams, but the source specifies a receiving batch with 1 L water plus liquid additions, not that mass per exact final liter. Correct the unsupported denominator while retaining the original mass and form. The corroborating provider explicitly uses 1012 ml and reports a different g_l; that declared calculation basis is not a measured final volume."}, {"field_path": "ingredients[6].concentration", "current": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "Na2S・9H2O", "volume": 0.5, "unit": "g"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[6]", "exact_source_quote": "\"component_name\": \"Na2S・9H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "The numeric value matches the original mass in grams, but the source specifies a receiving batch with 1 L water plus liquid additions, not that mass per exact final liter. Correct the unsupported denominator while retaining the original mass and form. The corroborating provider explicitly uses 1012 ml and reports a different g_l; that declared calculation basis is not a measured final volume."}, {"field_path": "ingredients[7].concentration", "current": {"value": "0.33", "unit": "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "KCl", "volume": 0.33, "unit": "g"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[7]", "exact_source_quote": "\"component_name\": \"KCl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "The numeric value matches the original mass in grams, but the source specifies a receiving batch with 1 L water plus liquid additions, not that mass per exact final liter. Correct the unsupported denominator while retaining the original mass and form. The corroborating provider explicitly uses 1012 ml and reports a different g_l; that declared calculation basis is not a measured final volume."}, {"field_path": "ingredients[8].concentration", "current": {"value": "10", "unit": "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "Sulfur (powder)", "volume": 10, "unit": "g"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[8]", "exact_source_quote": "\"component_name\": \"Sulfur (powder)\",\n          \"volume\": 10,\n          \"unit\": \"g\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "The numeric value matches the original mass in grams, but the source specifies a receiving batch with 1 L water plus liquid additions, not that mass per exact final liter. Correct the unsupported denominator while retaining the original mass and form. The corroborating provider explicitly uses 1012 ml and reports a different g_l; that declared calculation basis is not a measured final volume."}, {"field_path": "ingredients[9].concentration", "current": {"value": "0.3", "unit": "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "Yeast extract (BD-Difco)", "volume": 0.3, "unit": "g"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[9]", "exact_source_quote": "\"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "The numeric value matches the original mass in grams, but the source specifies a receiving batch with 1 L water plus liquid additions, not that mass per exact final liter. Correct the unsupported denominator while retaining the original mass and form. The corroborating provider explicitly uses 1012 ml and reports a different g_l; that declared calculation basis is not a measured final volume."}, {"field_path": "solutions[0].concentration", "current": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "FeCl2 solution (see Medium [M180])", "volume": 1, "unit": "ml"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[10]", "exact_source_quote": "\"component_name\": \"FeCl2 solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "This is a liquid stock addition to the receiving batch (1, 1 or 10 ml), not a mass concentration. Resolve the exact named composition/reference and preserve dose separately; do not assume final volume or flatten the stock."}, {"field_path": "solutions[1].concentration", "current": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "Trace element solution (see Medium [M180])", "volume": 1, "unit": "ml"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[11]", "exact_source_quote": "\"component_name\": \"Trace element solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "This is a liquid stock addition to the receiving batch (1, 1 or 10 ml), not a mass concentration. Resolve the exact named composition/reference and preserve dose separately; do not assume final volume or flatten the stock."}, {"field_path": "solutions[2].concentration", "current": {"value": "10", "unit": "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "Trace vitamins (see Medium [M190])", "volume": 10, "unit": "ml"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[12]", "exact_source_quote": "\"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "This is a liquid stock addition to the receiving batch (1, 1 or 10 ml), not a mass concentration. Resolve the exact named composition/reference and preserve dose separately; do not assume final volume or flatten the stock."}, {"field_path": "ingredients[10].concentration", "current": {"value": "variable", "unit": "VARIABLE"}, "decision": "not_quantified", "source_original": {"component_name": "H2SO4", "conc_value": 1, "conc_unit": "N"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[13]", "exact_source_quote": "\"component_name\": \"H2SO4\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"N\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "The 1 N label is sulfuric-acid reagent strength; addition volume is not quantified. VARIABLE must not hide that known strength or turn it into a final-medium normality."}, {"field_path": "ingredients[11].concentration", "current": {"value": "variable", "unit": "VARIABLE"}, "decision": "not_quantified", "source_original": {"component_name": "Carbon dioxide gas"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[14]", "exact_source_quote": "\"component_name\": \"Carbon dioxide gas\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "Gas quantity is not supplied as a mass or liquid dose. Keep it unquantified while restoring the separately explicit gas mixture and pressure at their source preparation stages."}, {"field_path": "ingredients[12].concentration", "current": {"value": "variable", "unit": "VARIABLE"}, "decision": "not_quantified", "source_original": {"component_name": "Nitrogen gas"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.components[0].items[15]", "exact_source_quote": "\"component_name\": \"Nitrogen gas\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "Gas quantity is not supplied as a mass or liquid dose. Keep it unquantified while restoring the separately explicit gas mixture and pressure at their source preparation stages."}, {"field_path": "solutions[0].composition (source row 0)", "current": null, "decision": "add", "source_stage": "FeCl2 solution", "source_original_amount": 10, "source_original_unit": "ml", "source_snippets": [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_locator": "$.components[1].items[0]", "exact_source_quote": "\"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\"", "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. The reagent is explicitly 7.7 M, labelled 25% without a percent basis. Preserve the 10 ml dose. Do not adopt provider g_l=2.5 or infer density/percent basis."}, {"field_path": "solutions[0].composition (source row 1)", "current": null, "decision": "add", "source_stage": "FeCl2 solution", "source_original_amount": 990, "source_original_unit": "ml", "source_snippets": [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_locator": "$.components[1].items[1]", "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\"", "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. This solvent amount is not itself proof of final stock volume."}, {"field_path": "solutions[0].composition (source row 2)", "current": null, "decision": "add", "source_stage": "FeCl2 solution", "source_original_amount": 1.5, "source_original_unit": "g", "source_snippets": [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_locator": "$.components[1].items[2]", "exact_source_quote": "\"component_name\": \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"", "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 1.5 g = 1.5 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "solutions[1].composition (source row 0)", "current": null, "decision": "add", "source_stage": "Trace element solution", "source_original_amount": 1, "source_original_unit": "L", "source_snippets": [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_locator": "$.components[2].items[0]", "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"", "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. This solvent amount is not itself proof of final stock volume."}, {"field_path": "solutions[1].composition (source row 1)", "current": null, "decision": "add", "source_stage": "Trace element solution", "source_original_amount": 36, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_locator": "$.components[2].items[1]", "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\"", "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 36 mg = 0.036 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "solutions[1].composition (source row 2)", "current": null, "decision": "add", "source_stage": "Trace element solution", "source_original_amount": 6, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_locator": "$.components[2].items[2]", "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\"", "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 6 mg = 0.006 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "solutions[1].composition (source row 3)", "current": null, "decision": "add", "source_stage": "Trace element solution", "source_original_amount": 100, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_locator": "$.components[2].items[3]", "exact_source_quote": "\"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\"", "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 100 mg = 0.100 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "solutions[1].composition (source row 4)", "current": null, "decision": "add", "source_stage": "Trace element solution", "source_original_amount": 190, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_locator": "$.components[2].items[4]", "exact_source_quote": "\"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\"", "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 190 mg = 0.190 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "solutions[1].composition (source row 5)", "current": null, "decision": "add", "source_stage": "Trace element solution", "source_original_amount": 24, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_locator": "$.components[2].items[5]", "exact_source_quote": "\"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\"", "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 24 mg = 0.024 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution. Resolve the source hexahydrate before reusing the standalone stock annotation CHEBI:34887, which is anhydrous."}, {"field_path": "solutions[1].composition (source row 6)", "current": null, "decision": "add", "source_stage": "Trace element solution", "source_original_amount": 2, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_locator": "$.components[2].items[6]", "exact_source_quote": "\"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\"", "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 2 mg = 0.002 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "solutions[1].composition (source row 7)", "current": null, "decision": "add", "source_stage": "Trace element solution", "source_original_amount": 70, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180", "source_locator": "$.components[2].items[7]", "exact_source_quote": "\"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\"", "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 70 mg = 0.070 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "solutions[2].composition (source row 0)", "current": null, "decision": "add", "source_stage": "Trace vitamins", "source_original_amount": 1, "source_original_unit": "L", "source_snippets": [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "source_locator": "$.components[1].items[0]", "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"", "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. This solvent amount is not itself proof of final stock volume."}, {"field_path": "solutions[2].composition (source row 1)", "current": null, "decision": "add", "source_stage": "Trace vitamins", "source_original_amount": 2, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "source_locator": "$.components[1].items[1]", "exact_source_quote": "\"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\"", "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 2 mg = 0.002 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "solutions[2].composition (source row 2)", "current": null, "decision": "add", "source_stage": "Trace vitamins", "source_original_amount": 5, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "source_locator": "$.components[1].items[2]", "exact_source_quote": "\"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"", "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 5 mg = 0.005 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "solutions[2].composition (source row 3)", "current": null, "decision": "add", "source_stage": "Trace vitamins", "source_original_amount": 5, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "source_locator": "$.components[1].items[3]", "exact_source_quote": "\"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\"", "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 5 mg = 0.005 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "solutions[2].composition (source row 4)", "current": null, "decision": "add", "source_stage": "Trace vitamins", "source_original_amount": 5, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "source_locator": "$.components[1].items[4]", "exact_source_quote": "\"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\"", "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 5 mg = 0.005 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution. The source does not specify stereochemistry; the standalone CHEBI:31345 structure is stereospecific. Do not treat a generic matching label as confirmation of the D form."}, {"field_path": "solutions[2].composition (source row 5)", "current": null, "decision": "add", "source_stage": "Trace vitamins", "source_original_amount": 10, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "source_locator": "$.components[1].items[5]", "exact_source_quote": "\"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\"", "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 10 mg = 0.010 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "solutions[2].composition (source row 6)", "current": null, "decision": "add", "source_stage": "Trace vitamins", "source_original_amount": 2, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "source_locator": "$.components[1].items[6]", "exact_source_quote": "\"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\"", "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 2 mg = 0.002 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "solutions[2].composition (source row 7)", "current": null, "decision": "add", "source_stage": "Trace vitamins", "source_original_amount": 0.1, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "source_locator": "$.components[1].items[7]", "exact_source_quote": "\"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\"", "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 0.1 mg = 0.0001 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "solutions[2].composition (source row 8)", "current": null, "decision": "add", "source_stage": "Trace vitamins", "source_original_amount": 5, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "source_locator": "$.components[1].items[8]", "exact_source_quote": "\"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\"", "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 5 mg = 0.005 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "solutions[2].composition (source row 9)", "current": null, "decision": "add", "source_stage": "Trace vitamins", "source_original_amount": 5, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "source_locator": "$.components[1].items[9]", "exact_source_quote": "\"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"", "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 5 mg = 0.005 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "solutions[2].composition (source row 10)", "current": null, "decision": "add", "source_stage": "Trace vitamins", "source_original_amount": 5, "source_original_unit": "mg", "source_snippets": [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "source_locator": "$.components[1].items[10]", "exact_source_quote": "\"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"", "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation": "Add this exact source-original amount at the named stock stage, keeping its water/solvent context separate from the receiving dose. The target and owner currently have empty composition arrays; do not transplant the parent medium. Absolute mass conversion only: 5 mg = 0.005 g. Provider stock g_l uses its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path": "preparation_steps (missing main atmosphere)", "current": null, "decision": "add", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.comments[0].comment", "exact_source_quote": "N2--CO2 (80:20) gas atmosphere", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "The explicit ratio belongs to the main autoclaving and later addition stages. Do not convert it to a mass concentration."}, {"field_path": "preparation_steps (missing yeast stock strength)", "current": null, "decision": "add", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.comments[0].comment", "exact_source_quote": "10% (w/v) yeast extract solution", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "Preserve this explicitly mass/volume stock strength and its separate autoclaving under nitrogen. It is not the final medium yeast concentration."}, {"field_path": "preparation_steps (missing sulfide stock strength)", "current": null, "decision": "add", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.comments[0].comment", "exact_source_quote": "5% (w/v) Na2S・9H2O solution", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "Preserve the supplied nonahydrate, explicitly mass/volume stock strength, separate sterilization and delayed addition."}, {"field_path": "preparation_steps (missing sulfur sterilization)", "current": null, "decision": "add", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.comments[0].comment", "exact_source_quote": "3 hr on each of 3 successive days", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "Preserve this sulfur-specific steam treatment, not the global default autoclave cycle."}, {"field_path": "preparation_steps (missing final pH and adjustment reagent)", "current": null, "decision": "add", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.comments[0].comment", "exact_source_quote": "adjust pH to 3.5 -- 3.8 with sterile 1 N H2SO4", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "Recover the exact range and stock normality. MediaDive pH 3.6 is not a replacement for this collection/TOGO range; no acid addition amount is supplied."}, {"field_path": "preparation_steps (missing bottle pressure and gas)", "current": null, "decision": "add", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator": "$.comments[0].comment", "exact_source_quote": "100 kPa N2--CO2 (80:20)", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation": "Preserve the pressure and gas ratio at this stated stage. The source does not identify gauge versus absolute pressure."}, {"field_path": "preparation_steps (JCM default autoclave cycle)", "current": null, "decision": "add", "source_snippets": [{"source_key": "jcm308", "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308", "source_locator": "JCM page global default qualifier before medium heading", "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.", "snapshot_sha256": "a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c", "parsed_text_sha256": "fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207"}], "explanation": "The collection supplies this default with an explicit exception qualifier. Apply only to source autoclave stages; do not override specified filtration or sulfur steam treatment."}]

### Current direct forms and bounded stock-recovery cautions

grounding: supported. Targets: CultureMech:009552.

Current direct calcium/magnesium chlorides and sodium sulfide preserve the specified hydrates; elemental sulfur and neutral resazurin match the source-level identities. Yeast extract remains an undefined product without an invented pure-molecule ID. Stock recovery must not import the candidate nickel anhydrous mapping or treat generic calcium pantothenate as demonstrated D stereochemistry. The standalone cobalt annotation is CHEBI:53503, already the hexahydrate; it is not the anhydrous cobalt annotation elsewhere in parent-medium context.

### Source-specific staged preparation and pH

completeness: concern. Targets: CultureMech:009552.

Target and owner omit all source preparation and pH. Recover the separate main/yeast/sulfide/sulfur/vitamin stages, gas contexts, delayed additions, exact pH range, pressure and qualified JCM default. The M190 mineral-stock pH instruction is unrelated to the vitamin reference and must not be imported.

### Classification, inherited roles and organism assertions

scope: supported. Targets: CultureMech:009552.

COMPLEX/SEMI_DEFINED is compatible with specified salts and undefined yeast extract; LIQUID is compatible with the source recipe. Existing role/property notes trace to TOGO annotations and do not supply independent growth evidence. Archaea filing and the medium name are not used to invent target-organism taxonomy, incubation conditions or phenotype.

### Claim-specific concentration and stock evidence

evidence: concern. Targets: CultureMech:009552.

Source URLs and stock cross-reference prose do not substitute for ingredient evidence, complete stock references/compositions or preparation support. Existing standalone-stock evidence must retain stock scope; root receiving-dose evidence needs exact solution paths. The unrelated M190 basal sulfide excerpt in historical dependency material is not used as vitamin support.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009552.

25 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

## Findings

### f1: Incorrect units and empty stock representations change the formulation

blocker / open / confirmed; issue key: togo-m303-units-batch-stocks.

Both layers encode water as 1 G_PER_L, source resazurin 1 mg as 1 G_PER_L, and stock additions 1/1/10 ml as G_PER_L. All three stock compositions are empty and named Unknown solution. Other direct masses lack a verified final-volume denominator. Exact source/stock data are available; these are representation defects, not source unavailability.

### f2: Source pH and separate preparation stages are missing

major / open / confirmed; issue key: jcm308-missing-preparation.

Neither local layer retains the available pH range or staged source preparation. One generic sterilization step would erase the separate sulfur, vitamin, yeast and sulfide treatment and addition boundaries.

### f3: Legacy sulfur linkage lacks verified historical correspondence

major / open / confirmed; issue key: mim001072-historical-correspondence.

The exact MediaIngredientMech:001072 link remains in ingredients[8] of target and owner. It is absent from the complete inspected pinned catalogue, while CHEBI:33403 is live. Those facts cannot establish the legacy identifier was invalid historically or identify a replacement. Required historical verification remains unavailable.

## Recommended Actions And Acceptance Checks

### a1

Correct the normalized owner using original source units and explicit receiving/stock batch scopes. Restore the exact three stock identities/compositions and addition amounts, retaining water as solvent and explicit unknown final volumes. Preserve source forms and assess candidate stock annotations before reuse; add narrowly placed evidence and regenerate only afterward.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Recover and cite exact JCM 308 preparation, pH range, stock strengths, gas and pressure contexts with their qualifiers. Keep acid/gas dose unknown where unstated and retain JCM default exceptions. Do not copy the basal recipes or unrelated pH instructions from JCM 187/197.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve the legacy correspondence from an authoritative historical MIM artifact before asserting a replacement or continuing to treat it as verified. If support cannot be recovered, document and withdraw the unsupported legacy assertion in a separately authorized curation, preserving historical events append-only. Do not substitute a same-name current CHEBI key as proof of historical identity.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch017/169/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch017/169/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml:1:id: CultureMech:009552<br>./data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml:1:id: CultureMech:009552<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch017/source-preflight-bound/169/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 51 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308; JCM medium 308 heading, main table, preparation paragraph and global default qualifier | supports | Exact collection formulation is available. Its source cross-references distinguish two stocks in JCM 187 and vitamins in JCM 197. The copyright year is not a recipe publication date. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303; $.meta, components[0], comments[0] | supports | TOGO M303 explicitly maps to JCM_M308, including the pH range, source quantities, separate stock references and preparation. Ingredient role/property notes are provider annotations, not independent biological evidence. |
| secondary-provider | https://mediadive.dsmz.de/rest/medium/J308; $.data.medium and solutions IDs 4022, 3846, 3847, 3861 | supports | The corroborating provider declares a 1012 ml main basis and 1000 ml stocks. It reports pH 3.6, whereas the original collection and TOGO give 3.5–3.8. Preserve the primary range; do not invent a chronology or measured final volume. |
| stock-primary-metal | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; Only FeCl2 solution and Trace element solution tables | supports | The two exact referenced stock subsections support composition and solvent amounts. Their parent basal medium and parent preparation are outside this target source scope. |
| stock-primary-vitamin | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Only Trace vitamins table | supports | The ten vitamin amounts and stock water resolve. The separate Trace mineral subsection and its final pH instruction are outside the vitamin cross-reference. |
| stock-togo-metal | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180; $.components[1] FeCl2 solution; components[2] Trace element solution | supports | Exact TOGO stock definitions corroborate JCM 187 with original mass units and the hydrochloric-acid reagent label. |
| stock-togo-vitamin | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; $.components[1] Trace vitamins | supports | Only the Trace vitamins subsection is used, not the parent medium or its unrelated mineral/pH instructions. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16526 resolves to carbon dioxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26836 resolves to sulfuric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33403 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33403; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33403 resolves to elemental sulfur. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26836": [{"label": "H2SO4", "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| legacy-catalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Complete 2953-row catalogue at the packaged index source commit; exact legacy token search | unknown | The exact legacy identifier is not found in any value of the complete inspected catalogue. This is a bounded absence at one revision, not evidence that the identifier never existed. |
| legacy-tree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Complete captured recursive tree at commit 6643131b0f12ab40b66f98135245fca04027e0e9 | unknown | The pinned repository tree establishes inspected revision identity. It does not provide the historical legacy-to-current correspondence needed for this remaining record link. |
| legacy-local-search | /private/tmp/culturemech-review-work-batch017/169/legacy-id-local-search.json; Exact-token lookup in normalized corpus and packaged MIM inputs, including ignored and hidden files | context_only | Local occurrences preserve the historical assertion; no authoritative historical identity correspondence is established by repeating them. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch017/169/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| stock-api-3846 | https://mediadive.dsmz.de/rest/solution/3846; $.data identity and exact recipe objects | supports | The exact independently captured stock API corroborates its source identity. Existing source evidence in the corresponding stock is scoped to that stock, not the receiving medium. |
| stock-api-3847 | https://mediadive.dsmz.de/rest/solution/3847; $.data identity and exact recipe objects | supports | The exact independently captured stock API corroborates its source identity. Existing source evidence in the corresponding stock is scoped to that stock, not the receiving medium. |
| stock-api-3861 | https://mediadive.dsmz.de/rest/solution/3861; $.data identity and exact recipe objects | supports | The exact independently captured stock API corroborates its source identity. Existing source evidence in the corresponding stock is scoped to that stock, not the receiving medium. |
| stock-dependencies | data/normalized_yaml/bacterial/mediadive_3846_FeCl2_solution.yaml; data/normalized_yaml/bacterial/mediadive_3847_Trace_element_solution.yaml; data/normalized_yaml/bacterial/mediadive_3861_Trace_vitamins.yaml; Current exact stock IDs, composition and chemical-form annotations; source-scoped evidence | context_only | Dependency identity summary: [{"path": "data/normalized_yaml/bacterial/mediadive_3846_FeCl2_solution.yaml", "id": "CultureMech:012919", "sha256": "b2e4c8ae5f0ec6756471724d2280bce9385e9928b686cc8e74f4ee7f946961b6", "composition_rows": 2}, {"path": "data/normalized_yaml/bacterial/mediadive_3847_Trace_element_solution.yaml", "id": "CultureMech:012920", "sha256": "e5e1e4c877006ddb55ed1495e22dd88c4a1c352828d5b1d7c3ad4934c90f2cde", "composition_rows": 8}, {"path": "data/normalized_yaml/bacterial/mediadive_3861_Trace_vitamins.yaml", "id": "CultureMech:012935", "sha256": "331158ab8c7f0f1857f8ecc2645fda25e3b98cf12aa19ef5017c3eb24909fac7", "composition_rows": 11}]. These are candidates for a corrected reference, not new whole-stock reviews or automatic approval of every annotation. |
| dependency-chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS label, formula and stereochemical structure where provided | supports | Dependency form context only: anhydrous nickel CHEBI:34887 cannot stand for source hexahydrate; cobalt CHEBI:53503 is explicitly hydrated; CHEBI:31345 has stereospecific structure beyond the generic source label; CHEBI:176843 retains generic vitamin-B12 scope. |
| dependency-chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS label, formula and stereochemical structure where provided | supports | Dependency form context only: anhydrous nickel CHEBI:34887 cannot stand for source hexahydrate; cobalt CHEBI:53503 is explicitly hydrated; CHEBI:31345 has stereospecific structure beyond the generic source label; CHEBI:176843 retains generic vitamin-B12 scope. |
| dependency-chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS label, formula and stereochemical structure where provided | supports | Dependency form context only: anhydrous nickel CHEBI:34887 cannot stand for source hexahydrate; cobalt CHEBI:53503 is explicitly hydrated; CHEBI:31345 has stereospecific structure beyond the generic source label; CHEBI:176843 retains generic vitamin-B12 scope. |
| dependency-chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS label, formula and stereochemical structure where provided | supports | Dependency form context only: anhydrous nickel CHEBI:34887 cannot stand for source hexahydrate; cobalt CHEBI:53503 is explicitly hydrated; CHEBI:31345 has stereospecific structure beyond the generic source label; CHEBI:176843 retains generic vitamin-B12 scope. |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO primary extraction separates stock references and preparation comments; mg and ml have explicit unit mappings and water L is preserved. Its local stock basis can use a water anchor or matching liquid total, which is not experimental final-volume evidence; bare concentration-unit fallbacks also need source checks. Do not blame historical owner units or missing comments on the current updated functions without version evidence. Current merge rejects incompatible formulation fields. |
| writer-1 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO primary extraction separates stock references and preparation comments; mg and ml have explicit unit mappings and water L is preserved. Its local stock basis can use a water anchor or matching liquid total, which is not experimental final-volume evidence; bare concentration-unit fallbacks also need source checks. Do not blame historical owner units or missing comments on the current updated functions without version evidence. Current merge rejects incompatible formulation fields. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO primary extraction separates stock references and preparation comments; mg and ml have explicit unit mappings and water L is preserved. Its local stock basis can use a water anchor or matching liquid total, which is not experimental final-volume evidence; bare concentration-unit fallbacks also need source checks. Do not blame historical owner units or missing comments on the current updated functions without version evidence. Current merge rejects incompatible formulation fields. |
| history-metadata | data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml; data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml", "events": 12, "timestamp_issues": []}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Partial completion is specifically due to unavailable required historical MediaIngredientMech:001072 correspondence. The exact collection recipe, TOGO source and all three stock definitions are available and inspected.
- No measured final medium/stock volumes, unqualified HCl percent basis, pressure reference convention or pantothenate stereochemistry is inferred. Source recipes are formulation evidence, not broad organism-growth evidence.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T110402Z-culturemech-009552-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acidilobus_medium (CultureMech:009552)'
started_at: '2026-10-21T10:48:47Z'
finished_at: '2026-10-21T11:04:02Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify the assessed recipe bytes.
    This is an independent agent review of captured local inputs and inspected primary/database
    sources, not experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The exact TOGO M303/JCM 308 medium and all three referenced stock definitions
  resolve. Water, resazurin and stock doses have incorrect units, source batch amounts
  are presented as unqualified final concentrations, and three stock compositions
  and source preparation are missing. The sulfur CHEBI concept is live, but its distinct
  legacy MediaIngredientMech correspondence remains unresolved; the scientific review
  is partial for that required identity check.
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
  - path: data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml
    sha256: 033f9fe338049519cc243a9c479c6aa060928939eed8fb62ef56847ace96aa03
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
    role: context
  - path: data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml
    sha256: df344bcb429f5d3acaa5fdb780c31b6be78b168701e633f31e601b4ebd41f8d1
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_3846_FeCl2_solution.yaml
    sha256: b2e4c8ae5f0ec6756471724d2280bce9385e9928b686cc8e74f4ee7f946961b6
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_3847_Trace_element_solution.yaml
    sha256: e5e1e4c877006ddb55ed1495e22dd88c4a1c352828d5b1d7c3ad4934c90f2cde
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_3861_Trace_vitamins.yaml
    sha256: 331158ab8c7f0f1857f8ecc2645fda25e3b98cf12aa19ef5017c3eb24909fac7
    role: context
  - path: data/normalized_yaml/bacterial/togo_medium_m190.yaml
    sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
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
  - path: scripts/enrich_solutions_with_chebi.py
    sha256: b4054fb4f13ecfb8362d421c549dfd34f1e94823caa107f2d1bf2d4462697b29
    role: context
  - path: scripts/enrich_with_chebi.py
    sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
    role: context
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
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
  - path: scripts/review_solution_concentration_evidence.py
    sha256: 40a5bb439caf0791caff746a1eac8d5069525f381c7f3b52556c26937741f65a
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
    provenance, and maintained-input correspondence. Required historical identity
    verification of MediaIngredientMech:001072 is unavailable; live CHEBI metadata
    does not resolve that separate linkage.
  selection: Task review 169; batch 017 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding sixteen task batches
    contain 160 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 162 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009552
targets:
- target_id: CultureMech:009552
  path: data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml
  label: acidilobus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009552
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch017/169/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch017/169/strict.tsv"
  target_ids:
  - CultureMech:009552
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009552
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009552
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
  - CultureMech:009552
- check_id: legacy-mim-identity
  name: Historical MediaIngredientMech:001072 correspondence
  required: true
  status: unavailable
  summary: Exact historical source correspondence remains unavailable in the inspected
    pinned catalogue/tree and current local inputs. No fuzzy replacement was selected.
    Live CHEBI:33403 existence is a different check.
  target_ids:
  - CultureMech:009552
  evidence_ids:
  - legacy-catalog
  - legacy-tree
  - legacy-local-search
  - chebi33403
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T11:04:01Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:04:01Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:44.663421Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch017/169/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:46.884427Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-017/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch017/169/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:49.451982Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T10:49:50.441023Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T11:04:01Z'
  support: supports
  summary: './data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml:1:id:
    CultureMech:009552

    ./data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml:1:id: CultureMech:009552

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/source-preflight-bound/169/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T11:04:01Z'
  support: supports
  summary: 51 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 68a8989cbe0e09917cb7c18a4e99d198802a177ba7727e1236b2bf8b0654e169
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308
  locator: JCM medium 308 heading, main table, preparation paragraph and global default
    qualifier
  accessed_at: '2026-10-21T10:35:30.491607Z'
  support: supports
  summary: Exact collection formulation is available. Its source cross-references
    distinguish two stocks in JCM 187 and vitamins in JCM 197. The copyright year
    is not a recipe publication date.
  snapshot_sha256: a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303
  locator: $.meta, components[0], comments[0]
  accessed_at: '2026-10-21T10:35:28.701540Z'
  support: supports
  summary: TOGO M303 explicitly maps to JCM_M308, including the pH range, source quantities,
    separate stock references and preparation. Ingredient role/property notes are
    provider annotations, not independent biological evidence.
  snapshot_sha256: 3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58
- evidence_id: secondary-provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J308
  locator: $.data.medium and solutions IDs 4022, 3846, 3847, 3861
  accessed_at: '2026-10-21T10:35:27.446668Z'
  support: supports
  summary: The corroborating provider declares a 1012 ml main basis and 1000 ml stocks.
    It reports pH 3.6, whereas the original collection and TOGO give 3.5–3.8. Preserve
    the primary range; do not invent a chronology or measured final volume.
  snapshot_sha256: 5fd506632b3d93d26b7bdc844525d6cf718294c706960192c342b9550c06d8e5
- evidence_id: stock-primary-metal
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187
  locator: Only FeCl2 solution and Trace element solution tables
  accessed_at: '2026-10-21T10:35:30.362855Z'
  support: supports
  summary: The two exact referenced stock subsections support composition and solvent
    amounts. Their parent basal medium and parent preparation are outside this target
    source scope.
  snapshot_sha256: e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804
- evidence_id: stock-primary-vitamin
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: Only Trace vitamins table
  accessed_at: '2026-10-20T06:58:05.867253Z'
  support: supports
  summary: The ten vitamin amounts and stock water resolve. The separate Trace mineral
    subsection and its final pH instruction are outside the vitamin cross-reference.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: stock-togo-metal
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180
  locator: $.components[1] FeCl2 solution; components[2] Trace element solution
  accessed_at: '2026-10-21T10:35:28.558157Z'
  support: supports
  summary: Exact TOGO stock definitions corroborate JCM 187 with original mass units
    and the hydrochloric-acid reagent label.
  snapshot_sha256: a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba
- evidence_id: stock-togo-vitamin
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  locator: $.components[1] Trace vitamins
  accessed_at: '2026-10-21T09:28:25.418127Z'
  support: supports
  summary: Only the Trace vitamins subsection is used, not the parent medium or its
    unrelated mineral/pH instructions.
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: CHEBI:15377 resolves to water. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi16526
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.337128Z'
  support: supports
  summary: CHEBI:16526 resolves to carbon dioxide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi17997
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:27.385647Z'
  support: supports
  summary: CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi26836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:29:13.222926Z'
  support: supports
  summary: CHEBI:26836 resolves to sulfuric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 19e202cd697eed2be3130d5b0b29cc0c1d18575ad103110877303ee678779737
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: CHEBI:31206 resolves to ammonium chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
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
- evidence_id: chebi33403
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33403
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:26:28.748668Z'
  support: supports
  summary: CHEBI:33403 resolves to elemental sulfur. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: b349493be5d8cb371d1e71751510f9205880ab9d0a14f560191e05606c127a60
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
  accessed_at: '2026-10-21T11:04:01Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26836": [{"label": "H2SO4", "match_type":
    "preferred_term", "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id":
    "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term",
    "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: legacy-catalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Complete 2953-row catalogue at the packaged index source commit; exact
    legacy token search
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: unknown
  summary: The exact legacy identifier is not found in any value of the complete inspected
    catalogue. This is a bounded absence at one revision, not evidence that the identifier
    never existed.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: legacy-tree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Complete captured recursive tree at commit 6643131b0f12ab40b66f98135245fca04027e0e9
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: unknown
  summary: The pinned repository tree establishes inspected revision identity. It
    does not provide the historical legacy-to-current correspondence needed for this
    remaining record link.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: legacy-local-search
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/169/legacy-id-local-search.json
  locator: Exact-token lookup in normalized corpus and packaged MIM inputs, including
    ignored and hidden files
  accessed_at: '2026-10-21T11:04:01Z'
  support: context_only
  summary: Local occurrences preserve the historical assertion; no authoritative historical
    identity correspondence is established by repeating them.
  snapshot_sha256: 5dca3e1e603f89214e65e1a9688fd632488e4202ce1bb1c9c9a9c00dccac3e93
  search_scope: rg --no-ignore --hidden over normalized corpus and packaged MIM inputs;
    complete pinned public catalogue searched separately.
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch017/169/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T11:04:01Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: c651171b1518157c94e4ea138629cccb3e798d639ea366f0ef9d23d0afbd69da
- evidence_id: stock-api-3846
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/3846
  locator: $.data identity and exact recipe objects
  accessed_at: '2026-10-21T10:37:16.847261Z'
  support: supports
  summary: The exact independently captured stock API corroborates its source identity.
    Existing source evidence in the corresponding stock is scoped to that stock, not
    the receiving medium.
  snapshot_sha256: 3b17c2e79a0ef85051dc8c41ff95bb0361a83b12179a510184b61ef9edbb96f0
- evidence_id: stock-api-3847
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/3847
  locator: $.data identity and exact recipe objects
  accessed_at: '2026-10-21T10:37:16.847414Z'
  support: supports
  summary: The exact independently captured stock API corroborates its source identity.
    Existing source evidence in the corresponding stock is scoped to that stock, not
    the receiving medium.
  snapshot_sha256: 12084302b4c979541441db0b0961a5744d937930e17ed9c7a326c75e2f787dd8
- evidence_id: stock-api-3861
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/3861
  locator: $.data identity and exact recipe objects
  accessed_at: '2026-10-20T06:58:06.579458Z'
  support: supports
  summary: The exact independently captured stock API corroborates its source identity.
    Existing source evidence in the corresponding stock is scoped to that stock, not
    the receiving medium.
  snapshot_sha256: c6829f83ad6e234909db1d65f45a27c24993e0280ff68c4d7355a8f6344335b9
- evidence_id: stock-dependencies
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_3846_FeCl2_solution.yaml; data/normalized_yaml/bacterial/mediadive_3847_Trace_element_solution.yaml;
    data/normalized_yaml/bacterial/mediadive_3861_Trace_vitamins.yaml
  locator: Current exact stock IDs, composition and chemical-form annotations; source-scoped
    evidence
  accessed_at: '2026-10-21T11:04:01Z'
  support: context_only
  summary: 'Dependency identity summary: [{"path": "data/normalized_yaml/bacterial/mediadive_3846_FeCl2_solution.yaml",
    "id": "CultureMech:012919", "sha256": "b2e4c8ae5f0ec6756471724d2280bce9385e9928b686cc8e74f4ee7f946961b6",
    "composition_rows": 2}, {"path": "data/normalized_yaml/bacterial/mediadive_3847_Trace_element_solution.yaml",
    "id": "CultureMech:012920", "sha256": "e5e1e4c877006ddb55ed1495e22dd88c4a1c352828d5b1d7c3ad4934c90f2cde",
    "composition_rows": 8}, {"path": "data/normalized_yaml/bacterial/mediadive_3861_Trace_vitamins.yaml",
    "id": "CultureMech:012935", "sha256": "331158ab8c7f0f1857f8ecc2645fda25e3b98cf12aa19ef5017c3eb24909fac7",
    "composition_rows": 11}]. These are candidates for a corrected reference, not
    new whole-stock reviews or automatic approval of every annotation.'
- evidence_id: dependency-chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS label, formula and stereochemical structure where provided
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: 'Dependency form context only: anhydrous nickel CHEBI:34887 cannot stand
    for source hexahydrate; cobalt CHEBI:53503 is explicitly hydrated; CHEBI:31345
    has stereospecific structure beyond the generic source label; CHEBI:176843 retains
    generic vitamin-B12 scope.'
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: dependency-chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact OLS label, formula and stereochemical structure where provided
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: 'Dependency form context only: anhydrous nickel CHEBI:34887 cannot stand
    for source hexahydrate; cobalt CHEBI:53503 is explicitly hydrated; CHEBI:31345
    has stereospecific structure beyond the generic source label; CHEBI:176843 retains
    generic vitamin-B12 scope.'
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: dependency-chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS label, formula and stereochemical structure where provided
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: 'Dependency form context only: anhydrous nickel CHEBI:34887 cannot stand
    for source hexahydrate; cobalt CHEBI:53503 is explicitly hydrated; CHEBI:31345
    has stereospecific structure beyond the generic source label; CHEBI:176843 retains
    generic vitamin-B12 scope.'
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: dependency-chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS label, formula and stereochemical structure where provided
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: 'Dependency form context only: anhydrous nickel CHEBI:34887 cannot stand
    for source hexahydrate; cobalt CHEBI:53503 is explicitly hydrated; CHEBI:31345
    has stereospecific structure beyond the generic source label; CHEBI:176843 retains
    generic vitamin-B12 scope.'
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:04:01Z'
  support: context_only
  summary: Current TOGO primary extraction separates stock references and preparation
    comments; mg and ml have explicit unit mappings and water L is preserved. Its
    local stock basis can use a water anchor or matching liquid total, which is not
    experimental final-volume evidence; bare concentration-unit fallbacks also need
    source checks. Do not blame historical owner units or missing comments on the
    current updated functions without version evidence. Current merge rejects incompatible
    formulation fields.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:04:01Z'
  support: context_only
  summary: Current TOGO primary extraction separates stock references and preparation
    comments; mg and ml have explicit unit mappings and water L is preserved. Its
    local stock basis can use a water anchor or matching liquid total, which is not
    experimental final-volume evidence; bare concentration-unit fallbacks also need
    source checks. Do not blame historical owner units or missing comments on the
    current updated functions without version evidence. Current merge rejects incompatible
    formulation fields.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:04:01Z'
  support: context_only
  summary: Current TOGO primary extraction separates stock references and preparation
    comments; mg and ml have explicit unit mappings and water L is preserved. Its
    local stock basis can use a water anchor or matching liquid total, which is not
    experimental final-volume evidence; bare concentration-unit fallbacks also need
    source checks. Do not blame historical owner units or missing comments on the
    current updated functions without version evidence. Current merge rejects incompatible
    formulation fields.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml; data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T11:04:01Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml", "events": 12,
    "timestamp_issues": []}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009552
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact source accession and stock reference resolution
  outcome: supported
  summary: TOGO M303 identifies JCM 308; its maintained owner is exact. M180 maps
    to JCM 187 and M190 to JCM 197, with the three named subsections independently
    resolved by MediaDive stock IDs 3846, 3847 and 3861. Their parent media are not
    substitutions for this medium.
  target_ids:
  - CultureMech:009552
  evidence_ids:
  - record
  - owner-0
  - id-search
  - primary
  - provider
  - secondary-provider
  - stock-primary-metal
  - stock-primary-vitamin
  - stock-togo-metal
  - stock-togo-vitamin
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '12 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 12/13 primary and 6/13 secondary
    instances; All current CHEBI-based secondary keys have exact pinned MIM rows;
    this does not verify the separate historical MediaIngredientMech:001072 link,
    whose unresolved correspondence makes grounding a concern. Source forms are assessed
    separately.'
  target_ids:
  - CultureMech:009552
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi16526
  - chebi17997
  - chebi26836
  - chebi31206
  - chebi32588
  - chebi33403
  - chebi63036
  - chebi76209
  - chebi86158
  - chebi86345
  - chebi8806
  details: 'Instance coverage on a 0–100 percent scale, denominator 13: primary 92.31%;
    secondary 46.15%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: legacy-identity
  area: grounding
  topic: Distinct legacy sulfur identifier
  outcome: unknown
  summary: CHEBI:33403 is a live elemental-sulfur concept compatible with the source
    powder description. That does not establish what MediaIngredientMech:001072 historically
    denoted. The exact legacy link remains unresolved, so scope and completion remain
    partial.
  target_ids:
  - CultureMech:009552
  evidence_ids:
  - record
  - owner-0
  - chebi33403
  - legacy-catalog
  - legacy-tree
  - legacy-local-search
- assessment_id: quantities
  area: quantity
  topic: Every direct amount, stock dose, missing stock constituent and preparation
    quantity
  outcome: concern
  summary: The 45-row inventory covers all 13 direct ingredients, three stock doses,
    22 missing stock rows and seven preparation contexts. Literal source masses and
    liquid additions remain distinct from provider-normalized concentrations and from
    unmeasured final volumes.
  target_ids:
  - CultureMech:009552
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - secondary-provider
  - stock-primary-metal
  - stock-primary-vitamin
  - stock-togo-metal
  - stock-togo-vitamin
  - quantity-inventory
  details: '[{"field_path": "ingredients[0].concentration", "current": {"value": "1",
    "unit": "G_PER_L"}, "decision": "correct", "source_original": {"component_name":
    "Distilled water", "volume": 1, "unit": "L"}, "source_stage": "Main JCM 308 receiving
    batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.components[0].items[0]", "exact_source_quote": "\"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"", "snapshot_sha256":
    "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation":
    "The literal 1 L is a water addition, not 1 g/L and not a final-volume make-up.
    Preserve solvent/batch scope."}, {"field_path": "ingredients[1].concentration",
    "current": {"value": "0.33", "unit": "G_PER_L"}, "decision": "correct", "source_original":
    {"component_name": "CaCl2・2H2O", "volume": 0.33, "unit": "g"}, "source_stage":
    "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303",
    "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.components[0].items[1]", "exact_source_quote": "\"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"", "snapshot_sha256":
    "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation":
    "The numeric value matches the original mass in grams, but the source specifies
    a receiving batch with 1 L water plus liquid additions, not that mass per exact
    final liter. Correct the unsupported denominator while retaining the original
    mass and form. The corroborating provider explicitly uses 1012 ml and reports
    a different g_l; that declared calculation basis is not a measured final volume."},
    {"field_path": "ingredients[2].concentration", "current": {"value": "0.33", "unit":
    "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "KH2PO4",
    "volume": 0.33, "unit": "g"}, "source_stage": "Main JCM 308 receiving batch",
    "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.components[0].items[2]", "exact_source_quote": "\"component_name\":
    \"KH2PO4\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"", "snapshot_sha256":
    "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation":
    "The numeric value matches the original mass in grams, but the source specifies
    a receiving batch with 1 L water plus liquid additions, not that mass per exact
    final liter. Correct the unsupported denominator while retaining the original
    mass and form. The corroborating provider explicitly uses 1012 ml and reports
    a different g_l; that declared calculation basis is not a measured final volume."},
    {"field_path": "ingredients[3].concentration", "current": {"value": "0.33", "unit":
    "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "NH4Cl",
    "volume": 0.33, "unit": "g"}, "source_stage": "Main JCM 308 receiving batch",
    "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.components[0].items[3]", "exact_source_quote": "\"component_name\":
    \"NH4Cl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"", "snapshot_sha256":
    "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation":
    "The numeric value matches the original mass in grams, but the source specifies
    a receiving batch with 1 L water plus liquid additions, not that mass per exact
    final liter. Correct the unsupported denominator while retaining the original
    mass and form. The corroborating provider explicitly uses 1012 ml and reports
    a different g_l; that declared calculation basis is not a measured final volume."},
    {"field_path": "ingredients[4].concentration", "current": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "Resazurin",
    "volume": 1, "unit": "mg"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets":
    [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.components[0].items[4]", "exact_source_quote": "\"component_name\":
    \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation":
    "The source gives 1 mg of resazurin, not 1 g/L. 1 mg equals 0.001 g as an absolute
    mass; no final-medium conversion is justified from water alone."}, {"field_path":
    "ingredients[5].concentration", "current": {"value": "0.33", "unit": "G_PER_L"},
    "decision": "correct", "source_original": {"component_name": "MgCl2・6H2O", "volume":
    0.33, "unit": "g"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets":
    [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.components[0].items[5]", "exact_source_quote": "\"component_name\":
    \"MgCl2・6H2O\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"", "snapshot_sha256":
    "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation":
    "The numeric value matches the original mass in grams, but the source specifies
    a receiving batch with 1 L water plus liquid additions, not that mass per exact
    final liter. Correct the unsupported denominator while retaining the original
    mass and form. The corroborating provider explicitly uses 1012 ml and reports
    a different g_l; that declared calculation basis is not a measured final volume."},
    {"field_path": "ingredients[6].concentration", "current": {"value": "0.5", "unit":
    "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "Na2S・9H2O",
    "volume": 0.5, "unit": "g"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets":
    [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.components[0].items[6]", "exact_source_quote": "\"component_name\":
    \"Na2S・9H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"", "snapshot_sha256":
    "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation":
    "The numeric value matches the original mass in grams, but the source specifies
    a receiving batch with 1 L water plus liquid additions, not that mass per exact
    final liter. Correct the unsupported denominator while retaining the original
    mass and form. The corroborating provider explicitly uses 1012 ml and reports
    a different g_l; that declared calculation basis is not a measured final volume."},
    {"field_path": "ingredients[7].concentration", "current": {"value": "0.33", "unit":
    "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "KCl",
    "volume": 0.33, "unit": "g"}, "source_stage": "Main JCM 308 receiving batch",
    "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.components[0].items[7]", "exact_source_quote": "\"component_name\":
    \"KCl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"", "snapshot_sha256":
    "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation":
    "The numeric value matches the original mass in grams, but the source specifies
    a receiving batch with 1 L water plus liquid additions, not that mass per exact
    final liter. Correct the unsupported denominator while retaining the original
    mass and form. The corroborating provider explicitly uses 1012 ml and reports
    a different g_l; that declared calculation basis is not a measured final volume."},
    {"field_path": "ingredients[8].concentration", "current": {"value": "10", "unit":
    "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "Sulfur
    (powder)", "volume": 10, "unit": "g"}, "source_stage": "Main JCM 308 receiving
    batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.components[0].items[8]", "exact_source_quote": "\"component_name\":
    \"Sulfur (powder)\",\n          \"volume\": 10,\n          \"unit\": \"g\"", "snapshot_sha256":
    "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation":
    "The numeric value matches the original mass in grams, but the source specifies
    a receiving batch with 1 L water plus liquid additions, not that mass per exact
    final liter. Correct the unsupported denominator while retaining the original
    mass and form. The corroborating provider explicitly uses 1012 ml and reports
    a different g_l; that declared calculation basis is not a measured final volume."},
    {"field_path": "ingredients[9].concentration", "current": {"value": "0.3", "unit":
    "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "Yeast
    extract (BD-Difco)", "volume": 0.3, "unit": "g"}, "source_stage": "Main JCM 308
    receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator":
    "$.components[0].items[9]", "exact_source_quote": "\"component_name\": \"Yeast
    extract (BD-Difco)\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"",
    "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}],
    "explanation": "The numeric value matches the original mass in grams, but the
    source specifies a receiving batch with 1 L water plus liquid additions, not that
    mass per exact final liter. Correct the unsupported denominator while retaining
    the original mass and form. The corroborating provider explicitly uses 1012 ml
    and reports a different g_l; that declared calculation basis is not a measured
    final volume."}, {"field_path": "solutions[0].concentration", "current": {"value":
    "1", "unit": "G_PER_L"}, "decision": "correct", "source_original": {"component_name":
    "FeCl2 solution (see Medium [M180])", "volume": 1, "unit": "ml"}, "source_stage":
    "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303",
    "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.components[0].items[10]", "exact_source_quote": "\"component_name\":
    \"FeCl2 solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}],
    "explanation": "This is a liquid stock addition to the receiving batch (1, 1 or
    10 ml), not a mass concentration. Resolve the exact named composition/reference
    and preserve dose separately; do not assume final volume or flatten the stock."},
    {"field_path": "solutions[1].concentration", "current": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "Trace
    element solution (see Medium [M180])", "volume": 1, "unit": "ml"}, "source_stage":
    "Main JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303",
    "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.components[0].items[11]", "exact_source_quote": "\"component_name\":
    \"Trace element solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}],
    "explanation": "This is a liquid stock addition to the receiving batch (1, 1 or
    10 ml), not a mass concentration. Resolve the exact named composition/reference
    and preserve dose separately; do not assume final volume or flatten the stock."},
    {"field_path": "solutions[2].concentration", "current": {"value": "10", "unit":
    "G_PER_L"}, "decision": "correct", "source_original": {"component_name": "Trace
    vitamins (see Medium [M190])", "volume": 10, "unit": "ml"}, "source_stage": "Main
    JCM 308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator":
    "$.components[0].items[12]", "exact_source_quote": "\"component_name\": \"Trace
    vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\":
    \"ml\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}],
    "explanation": "This is a liquid stock addition to the receiving batch (1, 1 or
    10 ml), not a mass concentration. Resolve the exact named composition/reference
    and preserve dose separately; do not assume final volume or flatten the stock."},
    {"field_path": "ingredients[10].concentration", "current": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "not_quantified", "source_original": {"component_name":
    "H2SO4", "conc_value": 1, "conc_unit": "N"}, "source_stage": "Main JCM 308 receiving
    batch", "source_snippets": [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.components[0].items[13]", "exact_source_quote": "\"component_name\":
    \"H2SO4\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"N\"", "snapshot_sha256":
    "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}], "explanation":
    "The 1 N label is sulfuric-acid reagent strength; addition volume is not quantified.
    VARIABLE must not hide that known strength or turn it into a final-medium normality."},
    {"field_path": "ingredients[11].concentration", "current": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "not_quantified", "source_original": {"component_name":
    "Carbon dioxide gas"}, "source_stage": "Main JCM 308 receiving batch", "source_snippets":
    [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.components[0].items[14]", "exact_source_quote": "\"component_name\":
    \"Carbon dioxide gas\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}],
    "explanation": "Gas quantity is not supplied as a mass or liquid dose. Keep it
    unquantified while restoring the separately explicit gas mixture and pressure
    at their source preparation stages."}, {"field_path": "ingredients[12].concentration",
    "current": {"value": "variable", "unit": "VARIABLE"}, "decision": "not_quantified",
    "source_original": {"component_name": "Nitrogen gas"}, "source_stage": "Main JCM
    308 receiving batch", "source_snippets": [{"source_key": "togoM303", "source_url":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator":
    "$.components[0].items[15]", "exact_source_quote": "\"component_name\": \"Nitrogen
    gas\"", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}],
    "explanation": "Gas quantity is not supplied as a mass or liquid dose. Keep it
    unquantified while restoring the separately explicit gas mixture and pressure
    at their source preparation stages."}, {"field_path": "solutions[0].composition
    (source row 0)", "current": null, "decision": "add", "source_stage": "FeCl2 solution",
    "source_original_amount": 10, "source_original_unit": "ml", "source_snippets":
    [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_locator": "$.components[1].items[0]", "exact_source_quote": "\"component_name\":
    \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\":
    25,\n          \"conc_unit\": \"%\"", "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}],
    "explanation": "Add this exact source-original amount at the named stock stage,
    keeping its water/solvent context separate from the receiving dose. The target
    and owner currently have empty composition arrays; do not transplant the parent
    medium. The reagent is explicitly 7.7 M, labelled 25% without a percent basis.
    Preserve the 10 ml dose. Do not adopt provider g_l=2.5 or infer density/percent
    basis."}, {"field_path": "solutions[0].composition (source row 1)", "current":
    null, "decision": "add", "source_stage": "FeCl2 solution", "source_original_amount":
    990, "source_original_unit": "ml", "source_snippets": [{"source_key": "togoM180",
    "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_locator": "$.components[1].items[1]", "exact_source_quote": "\"component_name\":
    \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\"",
    "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}],
    "explanation": "Add this exact source-original amount at the named stock stage,
    keeping its water/solvent context separate from the receiving dose. The target
    and owner currently have empty composition arrays; do not transplant the parent
    medium. This solvent amount is not itself proof of final stock volume."}, {"field_path":
    "solutions[0].composition (source row 2)", "current": null, "decision": "add",
    "source_stage": "FeCl2 solution", "source_original_amount": 1.5, "source_original_unit":
    "g", "source_snippets": [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_locator": "$.components[1].items[2]", "exact_source_quote": "\"component_name\":
    \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"", "snapshot_sha256":
    "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 1.5 g = 1.5 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution."}, {"field_path": "solutions[1].composition
    (source row 0)", "current": null, "decision": "add", "source_stage": "Trace element
    solution", "source_original_amount": 1, "source_original_unit": "L", "source_snippets":
    [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_locator": "$.components[2].items[0]", "exact_source_quote": "\"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"", "snapshot_sha256":
    "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. This solvent amount
    is not itself proof of final stock volume."}, {"field_path": "solutions[1].composition
    (source row 1)", "current": null, "decision": "add", "source_stage": "Trace element
    solution", "source_original_amount": 36, "source_original_unit": "mg", "source_snippets":
    [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_locator": "$.components[2].items[1]", "exact_source_quote": "\"component_name\":
    \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 36 mg = 0.036 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution."}, {"field_path": "solutions[1].composition
    (source row 2)", "current": null, "decision": "add", "source_stage": "Trace element
    solution", "source_original_amount": 6, "source_original_unit": "mg", "source_snippets":
    [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_locator": "$.components[2].items[2]", "exact_source_quote": "\"component_name\":
    \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 6 mg = 0.006 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution."}, {"field_path": "solutions[1].composition
    (source row 3)", "current": null, "decision": "add", "source_stage": "Trace element
    solution", "source_original_amount": 100, "source_original_unit": "mg", "source_snippets":
    [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_locator": "$.components[2].items[3]", "exact_source_quote": "\"component_name\":
    \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 100 mg = 0.100 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution."}, {"field_path": "solutions[1].composition
    (source row 4)", "current": null, "decision": "add", "source_stage": "Trace element
    solution", "source_original_amount": 190, "source_original_unit": "mg", "source_snippets":
    [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_locator": "$.components[2].items[4]", "exact_source_quote": "\"component_name\":
    \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 190 mg = 0.190 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution."}, {"field_path": "solutions[1].composition
    (source row 5)", "current": null, "decision": "add", "source_stage": "Trace element
    solution", "source_original_amount": 24, "source_original_unit": "mg", "source_snippets":
    [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_locator": "$.components[2].items[5]", "exact_source_quote": "\"component_name\":
    \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 24 mg = 0.024 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution. Resolve the source hexahydrate before reusing
    the standalone stock annotation CHEBI:34887, which is anhydrous."}, {"field_path":
    "solutions[1].composition (source row 6)", "current": null, "decision": "add",
    "source_stage": "Trace element solution", "source_original_amount": 2, "source_original_unit":
    "mg", "source_snippets": [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_locator": "$.components[2].items[6]", "exact_source_quote": "\"component_name\":
    \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 2 mg = 0.002 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution."}, {"field_path": "solutions[1].composition
    (source row 7)", "current": null, "decision": "add", "source_stage": "Trace element
    solution", "source_original_amount": 70, "source_original_unit": "mg", "source_snippets":
    [{"source_key": "togoM180", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
    "source_locator": "$.components[2].items[7]", "exact_source_quote": "\"component_name\":
    \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 70 mg = 0.070 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution."}, {"field_path": "solutions[2].composition
    (source row 0)", "current": null, "decision": "add", "source_stage": "Trace vitamins",
    "source_original_amount": 1, "source_original_unit": "L", "source_snippets": [{"source_key":
    "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "source_locator": "$.components[1].items[0]", "exact_source_quote": "\"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"", "snapshot_sha256":
    "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. This solvent amount
    is not itself proof of final stock volume."}, {"field_path": "solutions[2].composition
    (source row 1)", "current": null, "decision": "add", "source_stage": "Trace vitamins",
    "source_original_amount": 2, "source_original_unit": "mg", "source_snippets":
    [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "source_locator": "$.components[1].items[1]", "exact_source_quote": "\"component_name\":
    \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 2 mg = 0.002 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution."}, {"field_path": "solutions[2].composition
    (source row 2)", "current": null, "decision": "add", "source_stage": "Trace vitamins",
    "source_original_amount": 5, "source_original_unit": "mg", "source_snippets":
    [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "source_locator": "$.components[1].items[2]", "exact_source_quote": "\"component_name\":
    \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
    "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}],
    "explanation": "Add this exact source-original amount at the named stock stage,
    keeping its water/solvent context separate from the receiving dose. The target
    and owner currently have empty composition arrays; do not transplant the parent
    medium. Absolute mass conversion only: 5 mg = 0.005 g. Provider stock g_l uses
    its declared 1000 ml basis; this is not a new final-medium dilution."}, {"field_path":
    "solutions[2].composition (source row 3)", "current": null, "decision": "add",
    "source_stage": "Trace vitamins", "source_original_amount": 5, "source_original_unit":
    "mg", "source_snippets": [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "source_locator": "$.components[1].items[3]", "exact_source_quote": "\"component_name\":
    \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 5 mg = 0.005 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution."}, {"field_path": "solutions[2].composition
    (source row 4)", "current": null, "decision": "add", "source_stage": "Trace vitamins",
    "source_original_amount": 5, "source_original_unit": "mg", "source_snippets":
    [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "source_locator": "$.components[1].items[4]", "exact_source_quote": "\"component_name\":
    \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
    "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}],
    "explanation": "Add this exact source-original amount at the named stock stage,
    keeping its water/solvent context separate from the receiving dose. The target
    and owner currently have empty composition arrays; do not transplant the parent
    medium. Absolute mass conversion only: 5 mg = 0.005 g. Provider stock g_l uses
    its declared 1000 ml basis; this is not a new final-medium dilution. The source
    does not specify stereochemistry; the standalone CHEBI:31345 structure is stereospecific.
    Do not treat a generic matching label as confirmation of the D form."}, {"field_path":
    "solutions[2].composition (source row 5)", "current": null, "decision": "add",
    "source_stage": "Trace vitamins", "source_original_amount": 10, "source_original_unit":
    "mg", "source_snippets": [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "source_locator": "$.components[1].items[5]", "exact_source_quote": "\"component_name\":
    \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 10 mg = 0.010 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution."}, {"field_path": "solutions[2].composition
    (source row 6)", "current": null, "decision": "add", "source_stage": "Trace vitamins",
    "source_original_amount": 2, "source_original_unit": "mg", "source_snippets":
    [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "source_locator": "$.components[1].items[6]", "exact_source_quote": "\"component_name\":
    \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 2 mg = 0.002 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution."}, {"field_path": "solutions[2].composition
    (source row 7)", "current": null, "decision": "add", "source_stage": "Trace vitamins",
    "source_original_amount": 0.1, "source_original_unit": "mg", "source_snippets":
    [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "source_locator": "$.components[1].items[7]", "exact_source_quote": "\"component_name\":
    \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 0.1 mg = 0.0001 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution."}, {"field_path": "solutions[2].composition
    (source row 8)", "current": null, "decision": "add", "source_stage": "Trace vitamins",
    "source_original_amount": 5, "source_original_unit": "mg", "source_snippets":
    [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "source_locator": "$.components[1].items[8]", "exact_source_quote": "\"component_name\":
    \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 5 mg = 0.005 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution."}, {"field_path": "solutions[2].composition
    (source row 9)", "current": null, "decision": "add", "source_stage": "Trace vitamins",
    "source_original_amount": 5, "source_original_unit": "mg", "source_snippets":
    [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "source_locator": "$.components[1].items[9]", "exact_source_quote": "\"component_name\":
    \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 5 mg = 0.005 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution."}, {"field_path": "solutions[2].composition
    (source row 10)", "current": null, "decision": "add", "source_stage": "Trace vitamins",
    "source_original_amount": 5, "source_original_unit": "mg", "source_snippets":
    [{"source_key": "togoM190", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "source_locator": "$.components[1].items[10]", "exact_source_quote": "\"component_name\":
    \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"", "snapshot_sha256":
    "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"}], "explanation":
    "Add this exact source-original amount at the named stock stage, keeping its water/solvent
    context separate from the receiving dose. The target and owner currently have
    empty composition arrays; do not transplant the parent medium. Absolute mass conversion
    only: 5 mg = 0.005 g. Provider stock g_l uses its declared 1000 ml basis; this
    is not a new final-medium dilution."}, {"field_path": "preparation_steps (missing
    main atmosphere)", "current": null, "decision": "add", "source_snippets": [{"source_key":
    "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.comments[0].comment", "exact_source_quote": "N2--CO2 (80:20)
    gas atmosphere", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}],
    "explanation": "The explicit ratio belongs to the main autoclaving and later addition
    stages. Do not convert it to a mass concentration."}, {"field_path": "preparation_steps
    (missing yeast stock strength)", "current": null, "decision": "add", "source_snippets":
    [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.comments[0].comment", "exact_source_quote": "10% (w/v) yeast
    extract solution", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}],
    "explanation": "Preserve this explicitly mass/volume stock strength and its separate
    autoclaving under nitrogen. It is not the final medium yeast concentration."},
    {"field_path": "preparation_steps (missing sulfide stock strength)", "current":
    null, "decision": "add", "source_snippets": [{"source_key": "togoM303", "source_url":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303", "source_locator":
    "$.comments[0].comment", "exact_source_quote": "5% (w/v) Na2S・9H2O solution",
    "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}],
    "explanation": "Preserve the supplied nonahydrate, explicitly mass/volume stock
    strength, separate sterilization and delayed addition."}, {"field_path": "preparation_steps
    (missing sulfur sterilization)", "current": null, "decision": "add", "source_snippets":
    [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.comments[0].comment", "exact_source_quote": "3 hr on each
    of 3 successive days", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}],
    "explanation": "Preserve this sulfur-specific steam treatment, not the global
    default autoclave cycle."}, {"field_path": "preparation_steps (missing final pH
    and adjustment reagent)", "current": null, "decision": "add", "source_snippets":
    [{"source_key": "togoM303", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.comments[0].comment", "exact_source_quote": "adjust pH to
    3.5 -- 3.8 with sterile 1 N H2SO4", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}],
    "explanation": "Recover the exact range and stock normality. MediaDive pH 3.6
    is not a replacement for this collection/TOGO range; no acid addition amount is
    supplied."}, {"field_path": "preparation_steps (missing bottle pressure and gas)",
    "current": null, "decision": "add", "source_snippets": [{"source_key": "togoM303",
    "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M303",
    "source_locator": "$.comments[0].comment", "exact_source_quote": "100 kPa N2--CO2
    (80:20)", "snapshot_sha256": "3507fbaaba4e3b55bfb457f85b87f2994fae4978b38cb1885373124caf864d58"}],
    "explanation": "Preserve the pressure and gas ratio at this stated stage. The
    source does not identify gauge versus absolute pressure."}, {"field_path": "preparation_steps
    (JCM default autoclave cycle)", "current": null, "decision": "add", "source_snippets":
    [{"source_key": "jcm308", "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308",
    "source_locator": "JCM page global default qualifier before medium heading", "exact_source_quote":
    "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
    "snapshot_sha256": "a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c",
    "parsed_text_sha256": "fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207"}],
    "explanation": "The collection supplies this default with an explicit exception
    qualifier. Apply only to source autoclave stages; do not override specified filtration
    or sulfur steam treatment."}]'
- assessment_id: forms
  area: grounding
  topic: Current direct forms and bounded stock-recovery cautions
  outcome: supported
  summary: Current direct calcium/magnesium chlorides and sodium sulfide preserve
    the specified hydrates; elemental sulfur and neutral resazurin match the source-level
    identities. Yeast extract remains an undefined product without an invented pure-molecule
    ID. Stock recovery must not import the candidate nickel anhydrous mapping or treat
    generic calcium pantothenate as demonstrated D stereochemistry. The standalone
    cobalt annotation is CHEBI:53503, already the hexahydrate; it is not the anhydrous
    cobalt annotation elsewhere in parent-medium context.
  target_ids:
  - CultureMech:009552
  evidence_ids:
  - primary
  - provider
  - stock-primary-metal
  - stock-primary-vitamin
  - stock-dependencies
  - dependency-chebi34887
  - dependency-chebi53503
  - dependency-chebi31345
  - dependency-chebi176843
- assessment_id: preparation
  area: completeness
  topic: Source-specific staged preparation and pH
  outcome: concern
  summary: Target and owner omit all source preparation and pH. Recover the separate
    main/yeast/sulfide/sulfur/vitamin stages, gas contexts, delayed additions, exact
    pH range, pressure and qualified JCM default. The M190 mineral-stock pH instruction
    is unrelated to the vitamin reference and must not be imported.
  target_ids:
  - CultureMech:009552
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - stock-primary-vitamin
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Classification, inherited roles and organism assertions
  outcome: supported
  summary: COMPLEX/SEMI_DEFINED is compatible with specified salts and undefined yeast
    extract; LIQUID is compatible with the source recipe. Existing role/property notes
    trace to TOGO annotations and do not supply independent growth evidence. Archaea
    filing and the medium name are not used to invent target-organism taxonomy, incubation
    conditions or phenotype.
  target_ids:
  - CultureMech:009552
  evidence_ids:
  - record
  - provider
  - primary
- assessment_id: evidence-placement
  area: evidence
  topic: Claim-specific concentration and stock evidence
  outcome: concern
  summary: Source URLs and stock cross-reference prose do not substitute for ingredient
    evidence, complete stock references/compositions or preparation support. Existing
    standalone-stock evidence must retain stock scope; root receiving-dose evidence
    needs exact solution paths. The unrelated M190 basal sulfide excerpt in historical
    dependency material is not used as vitamin support.
  target_ids:
  - CultureMech:009552
  evidence_ids:
  - record
  - owner-0
  - provider
  - primary
  - stock-dependencies
  - quantity-inventory
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 25 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:009552
  evidence_ids:
  - record
  - history-metadata
  - owner-0
findings:
- finding_id: f1
  issue_key: togo-m303-units-batch-stocks
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Incorrect units and empty stock representations change the formulation
  description: Both layers encode water as 1 G_PER_L, source resazurin 1 mg as 1 G_PER_L,
    and stock additions 1/1/10 ml as G_PER_L. All three stock compositions are empty
    and named Unknown solution. Other direct masses lack a verified final-volume denominator.
    Exact source/stock data are available; these are representation defects, not source
    unavailability.
  target_ids:
  - CultureMech:009552
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - secondary-provider
  - stock-primary-metal
  - stock-primary-vitamin
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml
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
  issue_key: jcm308-missing-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source pH and separate preparation stages are missing
  description: Neither local layer retains the available pH range or staged source
    preparation. One generic sterilization step would erase the separate sulfur, vitamin,
    yeast and sulfide treatment and addition boundaries.
  target_ids:
  - CultureMech:009552
  field_paths:
  - preparation_steps
  - ingredients[10].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3
  normalization_reason: P3.4 is normally minor; major is justified because the absent
    separate sterilization/addition stages and source pH materially change this source
    formulation.
- finding_id: f3
  issue_key: mim001072-historical-correspondence
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Legacy sulfur linkage lacks verified historical correspondence
  description: The exact MediaIngredientMech:001072 link remains in ingredients[8]
    of target and owner. It is absent from the complete inspected pinned catalogue,
    while CHEBI:33403 is live. Those facts cannot establish the legacy identifier
    was invalid historically or identify a replacement. Required historical verification
    remains unavailable.
  target_ids:
  - CultureMech:009552
  field_paths:
  - ingredients[8].mediaingredientmech_term
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - legacy-catalog
  - legacy-tree
  - legacy-local-search
  - chebi33403
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml
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
  description: Correct the normalized owner using original source units and explicit
    receiving/stock batch scopes. Restore the exact three stock identities/compositions
    and addition amounts, retaining water as solvent and explicit unknown final volumes.
    Preserve source forms and assess candidate stock annotations before reuse; add
    narrowly placed evidence and regenerate only afterward.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009552
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml
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
  description: Recover and cite exact JCM 308 preparation, pH range, stock strengths,
    gas and pressure contexts with their qualifiers. Keep acid/gas dose unknown where
    unstated and retain JCM default exceptions. Do not copy the basal recipes or unrelated
    pH instructions from JCM 187/197.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009552
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml
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
  description: Resolve the legacy correspondence from an authoritative historical
    MIM artifact before asserting a replacement or continuing to treat it as verified.
    If support cannot be recovered, document and withdraw the unsupported legacy assertion
    in a separately authorized curation, preserving historical events append-only.
    Do not substitute a same-name current CHEBI key as proof of historical identity.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009552
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml
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
- Partial completion is specifically due to unavailable required historical MediaIngredientMech:001072
  correspondence. The exact collection recipe, TOGO source and all three stock definitions
  are available and inspected.
- No measured final medium/stock volumes, unqualified HCl percent basis, pressure
  reference convention or pantothenate stereochemistry is inferred. Source recipes
  are formulation evidence, not broad organism-growth evidence.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-017
- generated-medium
```
