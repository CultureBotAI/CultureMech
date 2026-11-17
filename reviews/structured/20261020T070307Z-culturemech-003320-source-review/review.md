# Source and formulation review: 1_2_sme_medium_for_ya (CultureMech:003320)

- Review: 20261020T070307Z-culturemech-003320-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-20T06:57:58Z
- Finished UTC: 2026-10-20T07:03:07Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The target resolves to JCM 971, but all 37 quantity assertions inherit lost stock boundaries, unsupported normalization or volume-to-mass substitutions. Four ingredient amounts sum distinct stock contexts. The stock pH is promoted to the main medium. These defects already occur in the maintained owner. Scientific completion is partial because two historical MIM identifiers remain unresolved.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 40 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003320 | data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml | generated | 1_2_sme_medium_for_ya |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003320 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003320 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/040/strict.tsv |
| validate-terms | passed | True | CultureMech:003320 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003320 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003320 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Historical ingredient identifier verification | unavailable | True | CultureMech:003320 | MediaIngredientMech:000198 and MediaIngredientMech:000232 have no matching current pinned-index entries; authoritative historical mappings are unavailable. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003320.

The four documented recipes completed; interpret the scope of each separately.

### Medium accession and maintained ownership

identity: supported. Targets: CultureMech:003320.

CultureMech:003320 and its sole normalized owner resolve unambiguously to JCM J971 / GRMD 971. The scientific defects are present in both owner and generated target.

The target is one medium, not a standalone stock. Identical ingredient names across source sections do not make them duplicates at the same concentration stage. The historical cleanup merged four such cross-context names; preserving that history does not certify its result.

### ingredients[0].concentration (KH2PO4)

quantity: concern. Targets: CultureMech:003320.

conflict: target 0.451671 G_PER_L. The original mass is source-supported, but this g_l uses provider volume 1107 mL, which incorporates a separate mineral-stock preparation batch. Final-medium normalization must be reassessed after restoring boundaries.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[1]", "solution_id": 4994, "stage": "main", "source_amount": 0.5, "source_unit": "g", "api_g_l": 0.451671, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[1].concentration (NH4Cl)

quantity: concern. Targets: CultureMech:003320.

conflict: target 0.271003 G_PER_L. The original mass is source-supported, but this g_l uses provider volume 1107 mL, which incorporates a separate mineral-stock preparation batch. Final-medium normalization must be reassessed after restoring boundaries.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[2]", "solution_id": 4994, "stage": "main", "source_amount": 0.3, "source_unit": "g", "api_g_l": 0.271003, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[2].concentration (Sodium acetate trihydrate)

quantity: concern. Targets: CultureMech:003320.

conflict: target 0.97561 G_PER_L. The original mass is source-supported, but this g_l uses provider volume 1107 mL, which incorporates a separate mineral-stock preparation batch. Final-medium normalization must be reassessed after restoring boundaries.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[3]", "solution_id": 4994, "stage": "main", "source_amount": 1.08, "source_unit": "g", "api_g_l": 0.97561, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[3].concentration (Yeast extract)

quantity: concern. Targets: CultureMech:003320.

conflict: target 0.180668 G_PER_L. The original mass is source-supported, but this g_l uses provider volume 1107 mL, which incorporates a separate mineral-stock preparation batch. Final-medium normalization must be reassessed after restoring boundaries.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[4]", "solution_id": 4994, "stage": "main", "source_amount": 0.2, "source_unit": "g", "api_g_l": 0.180668, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[4].concentration (Modified Wolfe's minerals)

quantity: concern. Targets: CultureMech:003320.

correct: target 1 G_PER_L. A source stock-addition volume was copied into a G_PER_L field. Preserve the dose and stock identity separately; no mass conversion is supported.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[5]", "solution_id": 4994, "stage": "main", "source_amount": 1, "source_unit": "ml", "api_g_l": null, "attribute": "10 x, see below"}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[5].concentration (Resazurin)

quantity: concern. Targets: CultureMech:003320.

conflict: target 0.000903342 G_PER_L. The original mass is source-supported, but this g_l uses provider volume 1107 mL, which incorporates a separate mineral-stock preparation batch. Final-medium normalization must be reassessed after restoring boundaries.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[7]", "solution_id": 4994, "stage": "main", "source_amount": 1, "source_unit": "mg", "api_g_l": 0.000903342, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[6].concentration (NaHCO3)

quantity: concern. Targets: CultureMech:003320.

conflict: target 2.71003 G_PER_L. The original mass is source-supported, but this g_l uses provider volume 1107 mL, which incorporates a separate mineral-stock preparation batch. Final-medium normalization must be reassessed after restoring boundaries.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[9]", "solution_id": 4994, "stage": "main", "source_amount": 3, "source_unit": "g", "api_g_l": 2.71003, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[7].concentration (Na2S x 9 H2O)

quantity: concern. Targets: CultureMech:003320.

correct: target 6 G_PER_L. A source stock-addition volume was copied into a G_PER_L field. Preserve the dose and stock identity separately; no mass conversion is supported.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[10]", "solution_id": 4994, "stage": "main", "source_amount": 6, "source_unit": "ml", "api_g_l": null, "attribute": "5%"}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[8].concentration (MgSO4 x 7 H2O)

quantity: concern. Targets: CultureMech:003320.

correct: target 16.71003 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations and summed across separate source contexts. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[11]", "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount": 3, "source_unit": "g", "api_g_l": 2.71003, "attribute": null}, {"api_pointer": "data.solutions[1].recipe[1]", "solution_id": 4432, "stage": "seawater_stock", "source_amount": 14, "source_unit": "g", "api_g_l": 14, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[9].concentration (MnSO4 x n H2O)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.451671 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[12]", "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount": 0.5, "source_unit": "g", "api_g_l": 0.451671, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[10].concentration (NaCl)

quantity: concern. Targets: CultureMech:003320.

correct: target 56.303342 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations and summed across separate source contexts. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[13]", "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount": 1, "source_unit": "g", "api_g_l": 0.903342, "attribute": null}, {"api_pointer": "data.solutions[1].recipe[0]", "solution_id": 4432, "stage": "seawater_stock", "source_amount": 55.4, "source_unit": "g", "api_g_l": 55.4, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[11].concentration (FeSO4 x 7 H2O)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.0903342 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[14]", "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount": 0.1, "source_unit": "g", "api_g_l": 0.0903342, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[12].concentration (CoSO4 x 7 H2O)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.162602 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[15]", "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount": 0.18, "source_unit": "g", "api_g_l": 0.162602, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[13].concentration (CaCl2 x 2 H2O)

quantity: concern. Targets: CultureMech:003320.

correct: target 1.5903342 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations and summed across separate source contexts. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[16]", "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount": 0.1, "source_unit": "g", "api_g_l": 0.0903342, "attribute": null}, {"api_pointer": "data.solutions[1].recipe[8]", "solution_id": 4432, "stage": "seawater_stock", "source_amount": 1.5, "source_unit": "g", "api_g_l": 1.5, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[14].concentration (ZnSO4 x 7 H2O)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.162602 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[17]", "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount": 0.18, "source_unit": "g", "api_g_l": 0.162602, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[15].concentration (CuSO4 x 5 H2O)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.00903342 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[18]", "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount": 0.01, "source_unit": "g", "api_g_l": 0.00903342, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[16].concentration (AlK(SO4)2 x 12 H2O)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.0162602 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[19]", "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount": 0.018, "source_unit": "g", "api_g_l": 0.0162602, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[17].concentration (H3BO3)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.06903342 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations and summed across separate source contexts. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[20]", "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount": 0.01, "source_unit": "g", "api_g_l": 0.00903342, "attribute": null}, {"api_pointer": "data.solutions[1].recipe[5]", "solution_id": 4432, "stage": "seawater_stock", "source_amount": 0.06, "source_unit": "g", "api_g_l": 0.06, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[18].concentration (Na2MoO4 x 2 H2O)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.00903342 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[21]", "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount": 0.01, "source_unit": "g", "api_g_l": 0.00903342, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[19].concentration ((NH4)2Ni(SO4)2 x 6 H2O)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.252936 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[22]", "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount": 0.28, "source_unit": "g", "api_g_l": 0.252936, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[20].concentration (Na2SeO4)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.00903342 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[23]", "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount": 0.01, "source_unit": "g", "api_g_l": 0.00903342, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[21].concentration (Na2WO4 x 2 H2O)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.00903342 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[24]", "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount": 0.01, "source_unit": "g", "api_g_l": 0.00903342, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[22].concentration (MgCl2 x 6 H2O)

quantity: concern. Targets: CultureMech:003320.

correct: target 11 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[1].recipe[2]", "solution_id": 4432, "stage": "seawater_stock", "source_amount": 11, "source_unit": "g", "api_g_l": 11, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[23].concentration (KCl)

quantity: concern. Targets: CultureMech:003320.

correct: target 1.3 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[1].recipe[3]", "solution_id": 4432, "stage": "seawater_stock", "source_amount": 1.3, "source_unit": "g", "api_g_l": 1.3, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[24].concentration (NaBr)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.2 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[1].recipe[4]", "solution_id": 4432, "stage": "seawater_stock", "source_amount": 0.2, "source_unit": "g", "api_g_l": 0.2, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[25].concentration (SrCl2 x 6 H2O)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.03 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[1].recipe[6]", "solution_id": 4432, "stage": "seawater_stock", "source_amount": 0.03, "source_unit": "g", "api_g_l": 0.03, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[26].concentration (KI)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.0001 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[1].recipe[7]", "solution_id": 4432, "stage": "seawater_stock", "source_amount": 0.1, "source_unit": "mg", "api_g_l": 0.0001, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[27].concentration (Biotin)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.002 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[0]", "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 2, "source_unit": "mg", "api_g_l": 0.002, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[28].concentration (Folic acid)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.002 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[1]", "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 2, "source_unit": "mg", "api_g_l": 0.002, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[29].concentration (Pyridoxine hydrochloride)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.01 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[2]", "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 10, "source_unit": "mg", "api_g_l": 0.01, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[30].concentration (Thiamine HCl)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.005 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[3]", "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 5, "source_unit": "mg", "api_g_l": 0.005, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[31].concentration (Riboflavin)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.005 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[4]", "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 5, "source_unit": "mg", "api_g_l": 0.005, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[32].concentration (Nicotinic acid)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.005 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[5]", "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 5, "source_unit": "mg", "api_g_l": 0.005, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[33].concentration (Calcium pantothenate)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.005 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[6]", "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 5, "source_unit": "mg", "api_g_l": 0.005, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[34].concentration (Vitamin B12)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.0001 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[7]", "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 0.1, "source_unit": "mg", "api_g_l": 0.0001, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[35].concentration (p-Aminobenzoic acid)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.005 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[8]", "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 5, "source_unit": "mg", "api_g_l": 0.005, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### ingredients[36].concentration (Lipoic acid)

quantity: concern. Targets: CultureMech:003320.

correct: target 0.005 G_PER_L. Stock-level quantities were exposed as direct main-medium concentrations. Preserve stock composition and actual addition dose separately before any final concentration calculation.

Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[9]", "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 5, "source_unit": "mg", "api_g_l": 0.005, "attribute": null}]. Mechanical copy/sum reproduces the target, but no revised final-medium value is supplied. All source stock additions and preparation-stage restrictions remain necessary.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:003320.

35 primary CHEBI identities resolve with matching labels; 32 of 32 current secondary keys have live pinned-index rows. Unresolved keys: [].

37 direct ingredient instances; primary coverage 35/37 (94.59%), verified secondary coverage 32/37 (86.49%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Chemical specificity and unresolved historical links

grounding: unknown. Targets: CultureMech:003320.

All 35 primary CHEBI identifiers resolve with the recorded labels and all 32 current secondary CHEBI keys have live registry entries. Two additional historical MIM links remain unresolved.

The manganese source label retains an unspecified hydrate count; its generic sulfate term does not verify an exact hydrate or support an anhydrous molarity conversion. Calcium pantothenate label correspondence is verified without claiming unreported stereochemical/purity specifications. Vitamin B12 remains a broad vitamer class, not an invented cyanocobalamin identity. Fixed hydrate labels elsewhere agree with inspected ontology formula/definitions. Ingredient-ID coverage is not evidence for any concentration.

### Main-medium versus three stock compositions

representation: concern. Targets: CultureMech:003320.

The mineral stock, synthetic seawater and vitamins are not represented as separate stock contexts. Their source doses are omitted or mis-typed, and four duplicate-name sums mix stock values.

Source additions are 250 mL synthetic seawater, 1 mL mineral stock and 10 mL vitamin stock. The separate sulfide solution is added later. The target instead has 37 direct rows and zero stock descriptors. Existing local seawater/vitamin IDs provide exact source-identity leads for future curation; no automatic reuse, new ID minting or link insertion is performed. The mineral stock is defined in the primary JCM 971 entry itself.

### Provider denominator and source batch arithmetic

quantity: concern. Targets: CultureMech:003320.

The provider volume 1107 mL includes the mineral-stock section’s 100 mL water as though the entire stock preparation were added to the medium. The actual source calls for a 1 mL aliquot.

Source liquid additions total 740+250+1+10+6=1007 mL; adding the separate stock-batch water produces 1107. This is a diagnostic sum, not a final-volume assertion. Dissolution, acid adjustment and source-volume convention remain unresolved. The two independent 1000 mL seawater/vitamin stock batches are likewise not direct final-volume additions.

### Main-medium versus stock pH and preparation order

consistency: concern. Targets: CultureMech:003320.

Primary JCM instructions give main-medium pH 7.0; pH 1.0 belongs to the separate mineral stock. The target uses 1.0 at root and leaves the stock-acidification step at the main level.

The target retains parts of the main preparation narrative, but its flattened ingredient ordering no longer identifies the later additions coherently. Stock preparation headings and acid adjustment must be scoped to the stock. The applicable JCM default complements the source autoclave instruction; unrelated preparation from JCM 197, 590 or 244 must not be copied into this receiving medium.

### Classification, physical state and unsupported growth claims

scope: supported. Targets: CultureMech:003320.

COMPLEX/UNDEFINED is consistent with yeast extract and the API annotation; LIQUID is consistent with the absence of a solidifier. No organism, strain, taxon, DOI, PMID, pathway or transcriptomic assertion is present.

Generic cultivation and bacterial filing are not experimental growth evidence. No unreported organism or condition is added. Current deterministic validator passes do not address stock boundaries or source pH context.

### History and missing claim-level context

provenance: concern. Targets: CultureMech:003320.

The source accession, URL and transformation history are recoverable, but neither target nor owner includes scoped concentration evidence. The reference gate examined zero excerpts.

The full target and its complete owner were read. Source rows, comments, secondary stock references and all 37 current amounts were assessed. Primary source section boundaries refute the scope of the provider normalization even where numbers match it. No generated file or historical curation entry is edited.

## Findings

### f1: Stock compositions and cross-stock sums replace the receiving formulation

blocker / open / confirmed; issue key: culturemech-003320-stock-boundaries-flattened.

The target exposes stock ingredients directly and adds four repeated-name quantities from different stages. The resulting 37-row composition is not the receiving medium specified by the primary source.

### f2: Two stock addition volumes are encoded as mass concentrations

major / open / confirmed; issue key: culturemech-003320-stock-volume-mass-substitution.

Modified Wolfe minerals and sulfide are source volume additions, but target and owner encode their raw numeric doses as G_PER_L and discard concentration-context attributes.

### f3: Main normalization includes water used to prepare a separate stock

major / open / confirmed; issue key: culturemech-003320-provider-volume-scope-error.

Provider 1107 mL normalization incorporates a separate mineral-stock batch. The target copies the resulting main-recipe g_l values, which therefore do not establish valid final-medium concentrations.

### f4: Stock acidification is applied to the main medium

major / open / confirmed; issue key: culturemech-003320-stock-ph-promoted-to-medium.

The source main-medium pH and stock pH have distinct scopes. The target root pH and final unscoped preparation step apply the stock value to the receiving medium.

### f5: Source references lack claim and preparation-stage evidence

minor / open / confirmed; issue key: culturemech-003320-evidence-stage-gap.

No target/owner amount assertion has a scoped supporting excerpt that distinguishes main medium, stock composition or stock addition. A recoverable URL and matching provider value do not resolve that omission.

## Recommended Actions And Acceptance Checks

### a1

Restore the stock/receiving-medium structure in maintained inputs and inspect source-specific importer/nesting behavior. Reuse existing source-identified stocks only after checking their exact content. Do not flatten unchanged stock concentrations or sum different stages.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Review the complete primary JCM 971 page and its referenced stock sections; do not accept a matching API number without preparation-stage agreement.
- Retain stock composition, actual addition dose, source water basis and unknown final-volume/percent/hydrate details separately.

### a2

Preserve each original volume dose, source stock identity and timing in schema-supported fields. Retain the unspecified sulfide percentage basis; do not infer a mass from volume without evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Review the complete primary JCM 971 page and its referenced stock sections; do not accept a matching API number without preparation-stage agreement.
- Retain stock composition, actual addition dose, source water basis and unknown final-volume/percent/hydrate details separately.

### a3

Reconcile original mass and stock-dose boundaries before re-normalizing. Preserve unresolved final volume explicitly and correct the maintained source transform rather than merely trusting provider g_l.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Review the complete primary JCM 971 page and its referenced stock sections; do not accept a matching API number without preparation-stage agreement.
- Retain stock composition, actual addition dose, source water basis and unknown final-volume/percent/hydrate details separately.

### a4

Restore main and stock conditions to their separate source-defined scopes, including preparation-stage boundaries. Retain the primary-source distinction even where provider summary metadata is wrong.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Review the complete primary JCM 971 page and its referenced stock sections; do not accept a matching API number without preparation-stage agreement.
- Retain stock composition, actual addition dose, source water basis and unknown final-volume/percent/hydrate details separately.

### a5

Attach concise exact primary-source excerpts and section locators to the restructured maintained claims, including unresolved or conflicting source metadata rather than masking it.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Review the complete primary JCM 971 page and its referenced stock sections; do not accept a matching API number without preparation-stage agreement.
- Retain stock composition, actual addition dose, source water basis and unknown final-volume/percent/hydrate details separately.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch004/040/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/040/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml:1:id: CultureMech:003320<br>./data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml:1:id: CultureMech:003320<br> |
| jcm971 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=971; Complete medium entry and separate mineral-stock section | supports | JCM 971 distinguishes main ingredients, three stock additions, a later sulfide-solution addition, main-medium pH and a separate Modified Wolfe minerals stock with its own water and acidification. |
| api | https://mediadive.dsmz.de/rest/medium/J971; data.medium and all three complete solutions, recipe rows, attributes and steps | supports | J971 links to JCM 971. API main solution 4994 incorporates the mineral-stock rows into its main recipe and reports volume 1107 mL and pH 1. Separate source solutions 4432 and 3861 are included with their original stock compositions. |
| bacmedia | https://bacmedia.dsmz.de/pdf/J971; Both pages; headers, main rows, mineral stock and nested seawater/vitamin tables | supports | The two-page rendering repeats the provider main-volume/pH metadata and shows distinct stock headings. Its provider normalization cannot override the collection’s preparation boundaries. |
| jcm590 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=590; Synthetic seawater reference in first row | supports | JCM 590 is the synthetic-seawater cross-reference used by JCM 971; it redirects the stock definition to JCM 244. Only that identity trail is used, not the receiving-medium recipe or its conditions. |
| jcm244 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244; Synthetic seawater (2 x) subsection only | supports | The separately headed Synthetic seawater (2 x) section specifies the nine stock solutes and water; it agrees with API solution 4432. Other sections of this page are unrelated to this target. |
| jcm197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Trace vitamins subsection only | supports | The separately headed Trace vitamins section specifies ten vitamin masses and water, matching API solution 3861. The parent medium and its preparation are not imported into JCM 971. |
| solution4432 | https://mediadive.dsmz.de/rest/solution/4432; data.id, data.name, data.volume and full recipe | supports | The exact source solution endpoint resolves and preserves its independent stock identity, volume and composition. Values are stock-level assertions, not final J971 concentrations. |
| solution3861 | https://mediadive.dsmz.de/rest/solution/3861; data.id, data.name, data.volume and full recipe | supports | The exact source solution endpoint resolves and preserves its independent stock identity, volume and composition. Values are stock-level assertions, not final J971 concentrations. |
| mapping | data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml; All 37 concentration fields traced to exact upstream rows and stage boundaries | context_only | Each target value equals either a copied provider g_l, copied volume number or the sum of two provider quantities. That mechanical equality is not scientific validation. The per-field source/stage mappings are recorded in the quantity assessments below. |
| local-stocks | repository checkout; Exact local source-solution identifiers, full composition projections and root metadata | context_only | CultureMech:013415 resolves to mediadive.solution:4432; CultureMech:012935 resolves to mediadive.solution:3861. Their composition projections preserve stock concentrations. These are contextual reuse candidates, not asserted links in the target or independently completed stock reviews. |
| legacy-search | repository checkout; Ignored-inclusive exact legacy-ID searches and current pinned index lookup | context_only | [{"identifier": "MediaIngredientMech:000198", "command": ["rg", "--no-ignore", "--hidden", "-l", "MediaIngredientMech:000198", "."], "files_with_occurrences": 211}, {"identifier": "MediaIngredientMech:000232", "command": ["rg", "--no-ignore", "--hidden", "-l", "MediaIngredientMech:000232", "."], "files_with_occurrences": 156}]; current index matches: {"MediaIngredientMech:000198": [], "MediaIngredientMech:000232": []}. Occurrences do not establish historical identity. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15940 resolves to nicotinic acid and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15956 resolves to biotin and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:16494 resolves to lipoic acid and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17015 resolves to riboflavin and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:176843 resolves to vitamin B12 and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:27470 resolves to folic acid and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:30753 resolves to 4-aminobenzoic acid and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:30961 resolves to pyridoxine hydrochloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31206 resolves to ammonium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31345 resolves to Calcium pantothenate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32138 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32138; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32138 resolves to sodium acetate trihydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32139 resolves to sodium hydrogencarbonate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32588 resolves to potassium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:33118 resolves to boric acid and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi36385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_36385; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:36385 resolves to strontium dichloride hexahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:49105 resolves to thiamine hydrochloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi63004 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63004; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:63004 resolves to sodium bromide and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:63939 resolves to sodium tungstate dihydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:75213 resolves to sodium molybdate dihydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi77775 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_77775; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:77775 resolves to sodium selenate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi8346 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8346; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:8346 resolves to potassium iodide and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86149; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86149 resolves to ammonium nickel sulfate hexahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86158 resolves to calcium chloride dihydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86360 resolves to manganese(II) sulfate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:8806 resolves to Resazurin and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32138": [{"label": "Sodium acetate trihydrate", "match_type": "preferred_term", "identifier": "CHEBI:32138", "preferred_term": "Sodium acetate trihydrate", "ontology_id": "CHEBI:32138", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86149": [{"label": "(NH4)2Ni(SO4)2", "match_type": "preferred_term", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63004": [{"label": "NaBr", "match_type": "preferred_term", "identifier": "CHEBI:63004", "preferred_term": "NaBr", "ontology_id": "CHEBI:63004", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:36385": [{"label": "SrCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:36385", "preferred_term": "SrCl2 x 6 H2O", "ontology_id": "CHEBI:36385", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31345": [{"label": "Calcium pantothenate", "match_type": "preferred_term", "identifier": "CHEBI:31345", "preferred_term": "Calcium pantothenate", "ontology_id": "CHEBI:31345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact final-medium volume remains unresolved after restoring source stock boundaries. A sum of source liquid additions is not an independently measured final volume; no new final concentrations are asserted.
- The sulfide stock percentage basis and manganese-sulfate hydrate count are unspecified. No density, fixed hydrate, molarity or percent conversion is inferred.
- The two local stock records were inspected for identity, composition and root context only; their entire evidence/history was not fully reviewed because the initial combined output was truncated. This bundle does not certify those records.
- Two historical MIM identifiers remain unresolved; valid primary CHEBI identities do not prove their historical meaning.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T070307Z-culturemech-003320-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_2_sme_medium_for_ya (CultureMech:003320)'
started_at: '2026-10-20T06:57:58Z'
finished_at: '2026-10-20T07:03:07Z'
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
summary: The target resolves to JCM 971, but all 37 quantity assertions inherit lost
  stock boundaries, unsupported normalization or volume-to-mass substitutions. Four
  ingredient amounts sum distinct stock contexts. The stock pH is promoted to the
  main medium. These defects already occur in the maintained owner. Scientific completion
  is partial because two historical MIM identifiers remain unresolved.
source:
  git_revision: 7c568537897ee4bba1b8e97f8172133c1572aec0
  state: working_tree
  inputs:
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
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/oak_config.yaml
    sha256: e35781d4fd66de4289411141b4c8a94189782d864ba6c45e49bf46537c46c5a1
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml
    sha256: f72ba4e1eddc95f77124b965b490c5e0d6b734c69e83eaae89339fbdb619d4fb
    role: target
  - path: data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml
    sha256: d9fc6e5f591dbb56de32e6ecdca2b43533f0d4ec6a9b197e0607283d92c72400
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_3861_Trace_vitamins.yaml
    sha256: 331158ab8c7f0f1857f8ecc2645fda25e3b98cf12aa19ef5017c3eb24909fac7
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4432_Synthetic_seawater_2_x.yaml
    sha256: b12249fa1bee845ecdbd4f0acaf7b8093f10c899016d1ceea6ff89aa90717adb
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
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
    role: context
  - path: scripts/fetch_mediadive_solution_volumes.py
    sha256: 408cdfa3f5c446e8f9c32ac98d7ea8a3a36553b23c032f3b7551f6a1661fd39a
    role: context
  - path: scripts/import_mediadive_solutions.py
    sha256: f97db7607d76c46b75d2d2428e8a425a5735e52beb3a9c28fd0af03ab5b31aa8
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
  selection: Record 40 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003320
targets:
- target_id: CultureMech:003320
  path: data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml
  label: 1_2_sme_medium_for_ya
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch004/040/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/040/strict.tsv"
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003320
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
  - CultureMech:003320
- check_id: legacy-mim-identities
  name: Historical ingredient identifier verification
  required: true
  status: unavailable
  summary: MediaIngredientMech:000198 and MediaIngredientMech:000232 have no matching
    current pinned-index entries; authoritative historical mappings are unavailable.
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - legacy-search
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-20T07:03:05Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T07:03:05Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T06:58:00.466374Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch004/040/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-20T06:58:01.871274Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/040/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T06:58:05.509992Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T06:58:07.086589Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-20T07:03:05Z'
  support: supports
  summary: './data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml:1:id: CultureMech:003320

    ./data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml:1:id: CultureMech:003320

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: jcm971
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=971
  locator: Complete medium entry and separate mineral-stock section
  accessed_at: '2026-10-20T06:54:57.007859Z'
  support: supports
  summary: JCM 971 distinguishes main ingredients, three stock additions, a later
    sulfide-solution addition, main-medium pH and a separate Modified Wolfe minerals
    stock with its own water and acidification.
  snapshot_sha256: 458a724f40215a3651f70b2ea74df6463f1c1c32a49dc7e86916f12dce29567a
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J971
  locator: data.medium and all three complete solutions, recipe rows, attributes and
    steps
  accessed_at: '2026-10-20T06:54:57.767238Z'
  support: supports
  summary: J971 links to JCM 971. API main solution 4994 incorporates the mineral-stock
    rows into its main recipe and reports volume 1107 mL and pH 1. Separate source
    solutions 4432 and 3861 are included with their original stock compositions.
  snapshot_sha256: 2fc1f872756c3fa57009ea9737d978038b6f070724442fc99212d4da75c59416
- evidence_id: bacmedia
  kind: database
  reference: https://bacmedia.dsmz.de/pdf/J971
  locator: Both pages; headers, main rows, mineral stock and nested seawater/vitamin
    tables
  accessed_at: '2026-10-20T06:54:57.767407Z'
  support: supports
  summary: The two-page rendering repeats the provider main-volume/pH metadata and
    shows distinct stock headings. Its provider normalization cannot override the
    collection’s preparation boundaries.
  snapshot_sha256: aa5e72bc27003538c6339327555bdc06dca9f7c2c3ab8ea7d069969992607662
- evidence_id: jcm590
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=590
  locator: Synthetic seawater reference in first row
  accessed_at: '2026-10-20T06:58:05.196415Z'
  support: supports
  summary: JCM 590 is the synthetic-seawater cross-reference used by JCM 971; it redirects
    the stock definition to JCM 244. Only that identity trail is used, not the receiving-medium
    recipe or its conditions.
  snapshot_sha256: 40d0cbf27cd2114c408d3ffca154fb8d5cd32aa188d8b139149c6dd4c615da58
- evidence_id: jcm244
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244
  locator: Synthetic seawater (2 x) subsection only
  accessed_at: '2026-10-20T07:00:02.868822Z'
  support: supports
  summary: The separately headed Synthetic seawater (2 x) section specifies the nine
    stock solutes and water; it agrees with API solution 4432. Other sections of this
    page are unrelated to this target.
  snapshot_sha256: 112072cc87d6839b575287734b39edcce1bd55c1660d8b221ccc679d496ae97e
- evidence_id: jcm197
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: Trace vitamins subsection only
  accessed_at: '2026-10-20T06:58:05.867253Z'
  support: supports
  summary: The separately headed Trace vitamins section specifies ten vitamin masses
    and water, matching API solution 3861. The parent medium and its preparation are
    not imported into JCM 971.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: solution4432
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4432
  locator: data.id, data.name, data.volume and full recipe
  accessed_at: '2026-10-20T06:58:07.253591Z'
  support: supports
  summary: The exact source solution endpoint resolves and preserves its independent
    stock identity, volume and composition. Values are stock-level assertions, not
    final J971 concentrations.
  snapshot_sha256: 3327f4037c10bc8039b0b7eb0841cc32986c7582c313ac68cda429ece006030c
- evidence_id: solution3861
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/3861
  locator: data.id, data.name, data.volume and full recipe
  accessed_at: '2026-10-20T06:58:06.579458Z'
  support: supports
  summary: The exact source solution endpoint resolves and preserves its independent
    stock identity, volume and composition. Values are stock-level assertions, not
    final J971 concentrations.
  snapshot_sha256: c6829f83ad6e234909db1d65f45a27c24993e0280ff68c4d7355a8f6344335b9
- evidence_id: mapping
  kind: record_content
  reference: data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml
  locator: All 37 concentration fields traced to exact upstream rows and stage boundaries
  accessed_at: '2026-10-20T07:01:18.841712Z'
  support: context_only
  summary: Each target value equals either a copied provider g_l, copied volume number
    or the sum of two provider quantities. That mechanical equality is not scientific
    validation. The per-field source/stage mappings are recorded in the quantity assessments
    below.
- evidence_id: local-stocks
  kind: record_content
  reference: repository checkout
  locator: Exact local source-solution identifiers, full composition projections and
    root metadata
  accessed_at: '2026-10-20T07:01:18.841712Z'
  support: context_only
  summary: CultureMech:013415 resolves to mediadive.solution:4432; CultureMech:012935
    resolves to mediadive.solution:3861. Their composition projections preserve stock
    concentrations. These are contextual reuse candidates, not asserted links in the
    target or independently completed stock reviews.
  search_scope: rg --files --no-ignore --hidden in data/normalized_yaml; exact API
    solution IDs matched filenames and parsed term IDs. Full combined stock-file output
    was truncated; only identity/composition/root-metadata projections are certified
    as inspected.
- evidence_id: legacy-search
  kind: record_content
  reference: repository checkout
  locator: Ignored-inclusive exact legacy-ID searches and current pinned index lookup
  accessed_at: '2026-10-20T07:01:18.841712Z'
  support: context_only
  summary: '[{"identifier": "MediaIngredientMech:000198", "command": ["rg", "--no-ignore",
    "--hidden", "-l", "MediaIngredientMech:000198", "."], "files_with_occurrences":
    211}, {"identifier": "MediaIngredientMech:000232", "command": ["rg", "--no-ignore",
    "--hidden", "-l", "MediaIngredientMech:000232", "."], "files_with_occurrences":
    156}]; current index matches: {"MediaIngredientMech:000198": [], "MediaIngredientMech:000232":
    []}. Occurrences do not establish historical identity.'
  search_scope: Whole-checkout rg --no-ignore --hidden for both legacy IDs; all current
    index rows checked for exact keys. Earlier ignored-inclusive registry discovery
    found no usable historical mapping in this checkout; external historical nonexistence
    is not claimed.
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: CHEBI:15940 resolves to nicotinic acid and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:10.040495Z'
  support: supports
  summary: CHEBI:15956 resolves to biotin and is not obsolete. This verifies the asserted
    generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond
    the record is inferred.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16494
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:13.001958Z'
  support: supports
  summary: CHEBI:16494 resolves to lipoic acid and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: CHEBI:17015 resolves to riboflavin and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:12.693131Z'
  support: supports
  summary: CHEBI:176843 resolves to vitamin B12 and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:54:57.767507Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: CHEBI:27470 resolves to folic acid and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: CHEBI:30753 resolves to 4-aminobenzoic acid and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:10.799046Z'
  support: supports
  summary: CHEBI:30961 resolves to pyridoxine hydrochloride and is not obsolete. This
    verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:05.220665Z'
  support: supports
  summary: CHEBI:31206 resolves to ammonium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: CHEBI:31345 resolves to Calcium pantothenate and is not obsolete. This
    verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:07.786285Z'
  support: supports
  summary: CHEBI:31440 resolves to copper(II) sulfate pentahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T03:57:34.006322Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32138
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32138
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:05.869898Z'
  support: supports
  summary: CHEBI:32138 resolves to sodium acetate trihydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 74faec6ae9b146967356e528305ebfcaaceca793993fd6cca01e1cf3af2b470b
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:03.674645Z'
  support: supports
  summary: CHEBI:32139 resolves to sodium hydrogencarbonate and is not obsolete. This
    verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:07.609898Z'
  support: supports
  summary: CHEBI:32312 resolves to zinc sulfate heptahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:00.737662Z'
  support: supports
  summary: CHEBI:32588 resolves to potassium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:02.761234Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi36385
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_36385
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:02.785349Z'
  support: supports
  summary: CHEBI:36385 resolves to strontium dichloride hexahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: a81397c907aeb36242c9f0a2aa24979df4b9aad2f624e8991ccd87a4ff9428b5
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: CHEBI:49105 resolves to thiamine hydrochloride and is not obsolete. This
    verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi63004
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63004
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:01.973244Z'
  support: supports
  summary: CHEBI:63004 resolves to sodium bromide and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 2665f3a4301ab51b67b814a8694bc906c1a13c9b301c85a4416891d3f9412c90
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T04:02:35.727546Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: CHEBI:63939 resolves to sodium tungstate dihydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:08.404288Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: CHEBI:76209 resolves to sodium sulfide nonahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi77775
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_77775
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:09.354177Z'
  support: supports
  summary: CHEBI:77775 resolves to sodium selenate and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: a1a4ab87bbf08908fef7df53a788a85d9f6eee32350f082895e0563d6344c908
- evidence_id: chebi8346
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8346
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:02.892064Z'
  support: supports
  summary: CHEBI:8346 resolves to potassium iodide and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 261d4862f5ae3627f515eefe14ca4f27cfed8c87604dbf8b8206b81af884631d
- evidence_id: chebi86149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86149
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:08.844455Z'
  support: supports
  summary: CHEBI:86149 resolves to ammonium nickel sulfate hexahydrate and is not
    obsolete. This verifies the asserted generic chemical identity; no source grade,
    salt, hydrate or stereochemistry beyond the record is inferred.
  snapshot_sha256: 930d93c33f6115f19153868ae36f0153b69406fd555708237a7ccccfb010cd97
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:01.682554Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:54:59.898295Z'
  support: supports
  summary: CHEBI:86345 resolves to magnesium dichloride hexahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86360
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:05.958063Z'
  support: supports
  summary: CHEBI:86360 resolves to manganese(II) sulfate and is not obsolete. This
    verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: ee3b60385f389c4eeb301cfe59996112ffa9c3c135268559b79e91810a14932b
- evidence_id: chebi86465
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:08.054799Z'
  support: supports
  summary: CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate and is
    not obsolete. This verifies the asserted generic chemical identity; no source
    grade, salt, hydrate or stereochemistry beyond the record is inferred.
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:04.324083Z'
  support: supports
  summary: CHEBI:8806 resolves to Resazurin and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi91244
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:07.079384Z'
  support: supports
  summary: CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-20T07:03:05Z'
  support: supports
  summary: '{"CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type":
    "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id":
    "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32138":
    [{"label": "Sodium acetate trihydrate", "match_type": "preferred_term", "identifier":
    "CHEBI:32138", "preferred_term": "Sodium acetate trihydrate", "ontology_id": "CHEBI:32138",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label":
    "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term":
    "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term",
    "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label":
    "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term":
    "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label":
    "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term":
    "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312":
    [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id":
    "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118":
    [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2
    H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86149": [{"label": "(NH4)2Ni(SO4)2", "match_type": "preferred_term", "identifier":
    "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2", "ontology_id": "CHEBI:86149",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86149", "preferred_term":
    "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O",
    "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63004": [{"label": "NaBr", "match_type":
    "preferred_term", "identifier": "CHEBI:63004", "preferred_term": "NaBr", "ontology_id":
    "CHEBI:63004", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:36385":
    [{"label": "SrCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:36385",
    "preferred_term": "SrCl2 x 6 H2O", "ontology_id": "CHEBI:36385", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type":
    "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id":
    "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470":
    [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470",
    "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride",
    "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term":
    "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type":
    "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl",
    "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier":
    "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid",
    "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term":
    "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31345": [{"label": "Calcium pantothenate", "match_type": "preferred_term",
    "identifier": "CHEBI:31345", "preferred_term": "Calcium pantothenate", "ontology_id":
    "CHEBI:31345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843":
    [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843",
    "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status":
    "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:30753": [{"label": "p-Aminobenzoic
    acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term":
    "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic
    acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Medium accession and maintained ownership
  outcome: supported
  summary: CultureMech:003320 and its sole normalized owner resolve unambiguously
    to JCM J971 / GRMD 971. The scientific defects are present in both owner and generated
    target.
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - owner-0
  - id-search
  - jcm971
  - api
  details: The target is one medium, not a standalone stock. Identical ingredient
    names across source sections do not make them duplicates at the same concentration
    stage. The historical cleanup merged four such cross-context names; preserving
    that history does not certify its result.
- assessment_id: amount-0
  area: quantity
  topic: ingredients[0].concentration (KH2PO4)
  outcome: concern
  summary: 'conflict: target 0.451671 G_PER_L. The original mass is source-supported,
    but this g_l uses provider volume 1107 mL, which incorporates a separate mineral-stock
    preparation batch. Final-medium normalization must be reassessed after restoring
    boundaries.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[1]",
    "solution_id": 4994, "stage": "main", "source_amount": 0.5, "source_unit": "g",
    "api_g_l": 0.451671, "attribute": null}]. Mechanical copy/sum reproduces the target,
    but no revised final-medium value is supplied. All source stock additions and
    preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: conflict
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-1
  area: quantity
  topic: ingredients[1].concentration (NH4Cl)
  outcome: concern
  summary: 'conflict: target 0.271003 G_PER_L. The original mass is source-supported,
    but this g_l uses provider volume 1107 mL, which incorporates a separate mineral-stock
    preparation batch. Final-medium normalization must be reassessed after restoring
    boundaries.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[2]",
    "solution_id": 4994, "stage": "main", "source_amount": 0.3, "source_unit": "g",
    "api_g_l": 0.271003, "attribute": null}]. Mechanical copy/sum reproduces the target,
    but no revised final-medium value is supplied. All source stock additions and
    preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: conflict
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-2
  area: quantity
  topic: ingredients[2].concentration (Sodium acetate trihydrate)
  outcome: concern
  summary: 'conflict: target 0.97561 G_PER_L. The original mass is source-supported,
    but this g_l uses provider volume 1107 mL, which incorporates a separate mineral-stock
    preparation batch. Final-medium normalization must be reassessed after restoring
    boundaries.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[3]",
    "solution_id": 4994, "stage": "main", "source_amount": 1.08, "source_unit": "g",
    "api_g_l": 0.97561, "attribute": null}]. Mechanical copy/sum reproduces the target,
    but no revised final-medium value is supplied. All source stock additions and
    preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: conflict
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-3
  area: quantity
  topic: ingredients[3].concentration (Yeast extract)
  outcome: concern
  summary: 'conflict: target 0.180668 G_PER_L. The original mass is source-supported,
    but this g_l uses provider volume 1107 mL, which incorporates a separate mineral-stock
    preparation batch. Final-medium normalization must be reassessed after restoring
    boundaries.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[4]",
    "solution_id": 4994, "stage": "main", "source_amount": 0.2, "source_unit": "g",
    "api_g_l": 0.180668, "attribute": null}]. Mechanical copy/sum reproduces the target,
    but no revised final-medium value is supplied. All source stock additions and
    preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: conflict
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-4
  area: quantity
  topic: ingredients[4].concentration (Modified Wolfe's minerals)
  outcome: concern
  summary: 'correct: target 1 G_PER_L. A source stock-addition volume was copied into
    a G_PER_L field. Preserve the dose and stock identity separately; no mass conversion
    is supported.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[5]",
    "solution_id": 4994, "stage": "main", "source_amount": 1, "source_unit": "ml",
    "api_g_l": null, "attribute": "10 x, see below"}]. Mechanical copy/sum reproduces
    the target, but no revised final-medium value is supplied. All source stock additions
    and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-5
  area: quantity
  topic: ingredients[5].concentration (Resazurin)
  outcome: concern
  summary: 'conflict: target 0.000903342 G_PER_L. The original mass is source-supported,
    but this g_l uses provider volume 1107 mL, which incorporates a separate mineral-stock
    preparation batch. Final-medium normalization must be reassessed after restoring
    boundaries.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[7]",
    "solution_id": 4994, "stage": "main", "source_amount": 1, "source_unit": "mg",
    "api_g_l": 0.000903342, "attribute": null}]. Mechanical copy/sum reproduces the
    target, but no revised final-medium value is supplied. All source stock additions
    and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: conflict
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-6
  area: quantity
  topic: ingredients[6].concentration (NaHCO3)
  outcome: concern
  summary: 'conflict: target 2.71003 G_PER_L. The original mass is source-supported,
    but this g_l uses provider volume 1107 mL, which incorporates a separate mineral-stock
    preparation batch. Final-medium normalization must be reassessed after restoring
    boundaries.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[9]",
    "solution_id": 4994, "stage": "main", "source_amount": 3, "source_unit": "g",
    "api_g_l": 2.71003, "attribute": null}]. Mechanical copy/sum reproduces the target,
    but no revised final-medium value is supplied. All source stock additions and
    preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: conflict
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-7
  area: quantity
  topic: ingredients[7].concentration (Na2S x 9 H2O)
  outcome: concern
  summary: 'correct: target 6 G_PER_L. A source stock-addition volume was copied into
    a G_PER_L field. Preserve the dose and stock identity separately; no mass conversion
    is supported.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[10]",
    "solution_id": 4994, "stage": "main", "source_amount": 6, "source_unit": "ml",
    "api_g_l": null, "attribute": "5%"}]. Mechanical copy/sum reproduces the target,
    but no revised final-medium value is supplied. All source stock additions and
    preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-8
  area: quantity
  topic: ingredients[8].concentration (MgSO4 x 7 H2O)
  outcome: concern
  summary: 'correct: target 16.71003 G_PER_L. Stock-level quantities were exposed
    as direct main-medium concentrations and summed across separate source contexts.
    Preserve stock composition and actual addition dose separately before any final
    concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[11]",
    "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount":
    3, "source_unit": "g", "api_g_l": 2.71003, "attribute": null}, {"api_pointer":
    "data.solutions[1].recipe[1]", "solution_id": 4432, "stage": "seawater_stock",
    "source_amount": 14, "source_unit": "g", "api_g_l": 14, "attribute": null}]. Mechanical
    copy/sum reproduces the target, but no revised final-medium value is supplied.
    All source stock additions and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-9
  area: quantity
  topic: ingredients[9].concentration (MnSO4 x n H2O)
  outcome: concern
  summary: 'correct: target 0.451671 G_PER_L. Stock-level quantities were exposed
    as direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[12]",
    "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount":
    0.5, "source_unit": "g", "api_g_l": 0.451671, "attribute": null}]. Mechanical
    copy/sum reproduces the target, but no revised final-medium value is supplied.
    All source stock additions and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-10
  area: quantity
  topic: ingredients[10].concentration (NaCl)
  outcome: concern
  summary: 'correct: target 56.303342 G_PER_L. Stock-level quantities were exposed
    as direct main-medium concentrations and summed across separate source contexts.
    Preserve stock composition and actual addition dose separately before any final
    concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[13]",
    "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount":
    1, "source_unit": "g", "api_g_l": 0.903342, "attribute": null}, {"api_pointer":
    "data.solutions[1].recipe[0]", "solution_id": 4432, "stage": "seawater_stock",
    "source_amount": 55.4, "source_unit": "g", "api_g_l": 55.4, "attribute": null}].
    Mechanical copy/sum reproduces the target, but no revised final-medium value is
    supplied. All source stock additions and preparation-stage restrictions remain
    necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-11
  area: quantity
  topic: ingredients[11].concentration (FeSO4 x 7 H2O)
  outcome: concern
  summary: 'correct: target 0.0903342 G_PER_L. Stock-level quantities were exposed
    as direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[14]",
    "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount":
    0.1, "source_unit": "g", "api_g_l": 0.0903342, "attribute": null}]. Mechanical
    copy/sum reproduces the target, but no revised final-medium value is supplied.
    All source stock additions and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-12
  area: quantity
  topic: ingredients[12].concentration (CoSO4 x 7 H2O)
  outcome: concern
  summary: 'correct: target 0.162602 G_PER_L. Stock-level quantities were exposed
    as direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[15]",
    "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount":
    0.18, "source_unit": "g", "api_g_l": 0.162602, "attribute": null}]. Mechanical
    copy/sum reproduces the target, but no revised final-medium value is supplied.
    All source stock additions and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-13
  area: quantity
  topic: ingredients[13].concentration (CaCl2 x 2 H2O)
  outcome: concern
  summary: 'correct: target 1.5903342 G_PER_L. Stock-level quantities were exposed
    as direct main-medium concentrations and summed across separate source contexts.
    Preserve stock composition and actual addition dose separately before any final
    concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[16]",
    "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount":
    0.1, "source_unit": "g", "api_g_l": 0.0903342, "attribute": null}, {"api_pointer":
    "data.solutions[1].recipe[8]", "solution_id": 4432, "stage": "seawater_stock",
    "source_amount": 1.5, "source_unit": "g", "api_g_l": 1.5, "attribute": null}].
    Mechanical copy/sum reproduces the target, but no revised final-medium value is
    supplied. All source stock additions and preparation-stage restrictions remain
    necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-14
  area: quantity
  topic: ingredients[14].concentration (ZnSO4 x 7 H2O)
  outcome: concern
  summary: 'correct: target 0.162602 G_PER_L. Stock-level quantities were exposed
    as direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[17]",
    "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount":
    0.18, "source_unit": "g", "api_g_l": 0.162602, "attribute": null}]. Mechanical
    copy/sum reproduces the target, but no revised final-medium value is supplied.
    All source stock additions and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-15
  area: quantity
  topic: ingredients[15].concentration (CuSO4 x 5 H2O)
  outcome: concern
  summary: 'correct: target 0.00903342 G_PER_L. Stock-level quantities were exposed
    as direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[18]",
    "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount":
    0.01, "source_unit": "g", "api_g_l": 0.00903342, "attribute": null}]. Mechanical
    copy/sum reproduces the target, but no revised final-medium value is supplied.
    All source stock additions and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-16
  area: quantity
  topic: ingredients[16].concentration (AlK(SO4)2 x 12 H2O)
  outcome: concern
  summary: 'correct: target 0.0162602 G_PER_L. Stock-level quantities were exposed
    as direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[19]",
    "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount":
    0.018, "source_unit": "g", "api_g_l": 0.0162602, "attribute": null}]. Mechanical
    copy/sum reproduces the target, but no revised final-medium value is supplied.
    All source stock additions and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-17
  area: quantity
  topic: ingredients[17].concentration (H3BO3)
  outcome: concern
  summary: 'correct: target 0.06903342 G_PER_L. Stock-level quantities were exposed
    as direct main-medium concentrations and summed across separate source contexts.
    Preserve stock composition and actual addition dose separately before any final
    concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[20]",
    "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount":
    0.01, "source_unit": "g", "api_g_l": 0.00903342, "attribute": null}, {"api_pointer":
    "data.solutions[1].recipe[5]", "solution_id": 4432, "stage": "seawater_stock",
    "source_amount": 0.06, "source_unit": "g", "api_g_l": 0.06, "attribute": null}].
    Mechanical copy/sum reproduces the target, but no revised final-medium value is
    supplied. All source stock additions and preparation-stage restrictions remain
    necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-18
  area: quantity
  topic: ingredients[18].concentration (Na2MoO4 x 2 H2O)
  outcome: concern
  summary: 'correct: target 0.00903342 G_PER_L. Stock-level quantities were exposed
    as direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[21]",
    "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount":
    0.01, "source_unit": "g", "api_g_l": 0.00903342, "attribute": null}]. Mechanical
    copy/sum reproduces the target, but no revised final-medium value is supplied.
    All source stock additions and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-19
  area: quantity
  topic: ingredients[19].concentration ((NH4)2Ni(SO4)2 x 6 H2O)
  outcome: concern
  summary: 'correct: target 0.252936 G_PER_L. Stock-level quantities were exposed
    as direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[22]",
    "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount":
    0.28, "source_unit": "g", "api_g_l": 0.252936, "attribute": null}]. Mechanical
    copy/sum reproduces the target, but no revised final-medium value is supplied.
    All source stock additions and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-20
  area: quantity
  topic: ingredients[20].concentration (Na2SeO4)
  outcome: concern
  summary: 'correct: target 0.00903342 G_PER_L. Stock-level quantities were exposed
    as direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[23]",
    "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount":
    0.01, "source_unit": "g", "api_g_l": 0.00903342, "attribute": null}]. Mechanical
    copy/sum reproduces the target, but no revised final-medium value is supplied.
    All source stock additions and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-21
  area: quantity
  topic: ingredients[21].concentration (Na2WO4 x 2 H2O)
  outcome: concern
  summary: 'correct: target 0.00903342 G_PER_L. Stock-level quantities were exposed
    as direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[0].recipe[24]",
    "solution_id": 4994, "stage": "modified_wolfe_stock_misplaced_in_API_main", "source_amount":
    0.01, "source_unit": "g", "api_g_l": 0.00903342, "attribute": null}]. Mechanical
    copy/sum reproduces the target, but no revised final-medium value is supplied.
    All source stock additions and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-22
  area: quantity
  topic: ingredients[22].concentration (MgCl2 x 6 H2O)
  outcome: concern
  summary: 'correct: target 11 G_PER_L. Stock-level quantities were exposed as direct
    main-medium concentrations. Preserve stock composition and actual addition dose
    separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[1].recipe[2]",
    "solution_id": 4432, "stage": "seawater_stock", "source_amount": 11, "source_unit":
    "g", "api_g_l": 11, "attribute": null}]. Mechanical copy/sum reproduces the target,
    but no revised final-medium value is supplied. All source stock additions and
    preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-23
  area: quantity
  topic: ingredients[23].concentration (KCl)
  outcome: concern
  summary: 'correct: target 1.3 G_PER_L. Stock-level quantities were exposed as direct
    main-medium concentrations. Preserve stock composition and actual addition dose
    separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[1].recipe[3]",
    "solution_id": 4432, "stage": "seawater_stock", "source_amount": 1.3, "source_unit":
    "g", "api_g_l": 1.3, "attribute": null}]. Mechanical copy/sum reproduces the target,
    but no revised final-medium value is supplied. All source stock additions and
    preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-24
  area: quantity
  topic: ingredients[24].concentration (NaBr)
  outcome: concern
  summary: 'correct: target 0.2 G_PER_L. Stock-level quantities were exposed as direct
    main-medium concentrations. Preserve stock composition and actual addition dose
    separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[1].recipe[4]",
    "solution_id": 4432, "stage": "seawater_stock", "source_amount": 0.2, "source_unit":
    "g", "api_g_l": 0.2, "attribute": null}]. Mechanical copy/sum reproduces the target,
    but no revised final-medium value is supplied. All source stock additions and
    preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-25
  area: quantity
  topic: ingredients[25].concentration (SrCl2 x 6 H2O)
  outcome: concern
  summary: 'correct: target 0.03 G_PER_L. Stock-level quantities were exposed as direct
    main-medium concentrations. Preserve stock composition and actual addition dose
    separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[1].recipe[6]",
    "solution_id": 4432, "stage": "seawater_stock", "source_amount": 0.03, "source_unit":
    "g", "api_g_l": 0.03, "attribute": null}]. Mechanical copy/sum reproduces the
    target, but no revised final-medium value is supplied. All source stock additions
    and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-26
  area: quantity
  topic: ingredients[26].concentration (KI)
  outcome: concern
  summary: 'correct: target 0.0001 G_PER_L. Stock-level quantities were exposed as
    direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[1].recipe[7]",
    "solution_id": 4432, "stage": "seawater_stock", "source_amount": 0.1, "source_unit":
    "mg", "api_g_l": 0.0001, "attribute": null}]. Mechanical copy/sum reproduces the
    target, but no revised final-medium value is supplied. All source stock additions
    and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-27
  area: quantity
  topic: ingredients[27].concentration (Biotin)
  outcome: concern
  summary: 'correct: target 0.002 G_PER_L. Stock-level quantities were exposed as
    direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[0]",
    "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 2, "source_unit":
    "mg", "api_g_l": 0.002, "attribute": null}]. Mechanical copy/sum reproduces the
    target, but no revised final-medium value is supplied. All source stock additions
    and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-28
  area: quantity
  topic: ingredients[28].concentration (Folic acid)
  outcome: concern
  summary: 'correct: target 0.002 G_PER_L. Stock-level quantities were exposed as
    direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[1]",
    "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 2, "source_unit":
    "mg", "api_g_l": 0.002, "attribute": null}]. Mechanical copy/sum reproduces the
    target, but no revised final-medium value is supplied. All source stock additions
    and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-29
  area: quantity
  topic: ingredients[29].concentration (Pyridoxine hydrochloride)
  outcome: concern
  summary: 'correct: target 0.01 G_PER_L. Stock-level quantities were exposed as direct
    main-medium concentrations. Preserve stock composition and actual addition dose
    separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[2]",
    "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 10, "source_unit":
    "mg", "api_g_l": 0.01, "attribute": null}]. Mechanical copy/sum reproduces the
    target, but no revised final-medium value is supplied. All source stock additions
    and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-30
  area: quantity
  topic: ingredients[30].concentration (Thiamine HCl)
  outcome: concern
  summary: 'correct: target 0.005 G_PER_L. Stock-level quantities were exposed as
    direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[3]",
    "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 5, "source_unit":
    "mg", "api_g_l": 0.005, "attribute": null}]. Mechanical copy/sum reproduces the
    target, but no revised final-medium value is supplied. All source stock additions
    and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-31
  area: quantity
  topic: ingredients[31].concentration (Riboflavin)
  outcome: concern
  summary: 'correct: target 0.005 G_PER_L. Stock-level quantities were exposed as
    direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[4]",
    "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 5, "source_unit":
    "mg", "api_g_l": 0.005, "attribute": null}]. Mechanical copy/sum reproduces the
    target, but no revised final-medium value is supplied. All source stock additions
    and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-32
  area: quantity
  topic: ingredients[32].concentration (Nicotinic acid)
  outcome: concern
  summary: 'correct: target 0.005 G_PER_L. Stock-level quantities were exposed as
    direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[5]",
    "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 5, "source_unit":
    "mg", "api_g_l": 0.005, "attribute": null}]. Mechanical copy/sum reproduces the
    target, but no revised final-medium value is supplied. All source stock additions
    and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-33
  area: quantity
  topic: ingredients[33].concentration (Calcium pantothenate)
  outcome: concern
  summary: 'correct: target 0.005 G_PER_L. Stock-level quantities were exposed as
    direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[6]",
    "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 5, "source_unit":
    "mg", "api_g_l": 0.005, "attribute": null}]. Mechanical copy/sum reproduces the
    target, but no revised final-medium value is supplied. All source stock additions
    and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-34
  area: quantity
  topic: ingredients[34].concentration (Vitamin B12)
  outcome: concern
  summary: 'correct: target 0.0001 G_PER_L. Stock-level quantities were exposed as
    direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[7]",
    "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 0.1, "source_unit":
    "mg", "api_g_l": 0.0001, "attribute": null}]. Mechanical copy/sum reproduces the
    target, but no revised final-medium value is supplied. All source stock additions
    and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-35
  area: quantity
  topic: ingredients[35].concentration (p-Aminobenzoic acid)
  outcome: concern
  summary: 'correct: target 0.005 G_PER_L. Stock-level quantities were exposed as
    direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[8]",
    "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 5, "source_unit":
    "mg", "api_g_l": 0.005, "attribute": null}]. Mechanical copy/sum reproduces the
    target, but no revised final-medium value is supplied. All source stock additions
    and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: amount-36
  area: quantity
  topic: ingredients[36].concentration (Lipoic acid)
  outcome: concern
  summary: 'correct: target 0.005 G_PER_L. Stock-level quantities were exposed as
    direct main-medium concentrations. Preserve stock composition and actual addition
    dose separately before any final concentration calculation.'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mapping
  - jcm971
  - api
  - jcm244
  - jcm197
  details: 'Exact observed source rows: [{"api_pointer": "data.solutions[2].recipe[9]",
    "solution_id": 3861, "stage": "vitamin_stock", "source_amount": 5, "source_unit":
    "mg", "api_g_l": 0.005, "attribute": null}]. Mechanical copy/sum reproduces the
    target, but no revised final-medium value is supplied. All source stock additions
    and preparation-stage restrictions remain necessary.'
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact target amount after distinguishing source
      mass, stock composition, stock dose and normalization volume
    evidence_ids:
    - jcm971
    - api
    - mapping
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '35 primary CHEBI identities resolve with matching labels; 32 of 32 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mim
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi176843
  - chebi26710
  - chebi27470
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi31440
  - chebi31795
  - chebi32138
  - chebi32139
  - chebi32312
  - chebi32588
  - chebi33118
  - chebi36385
  - chebi49105
  - chebi63004
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi75836
  - chebi76209
  - chebi77775
  - chebi8346
  - chebi86149
  - chebi86158
  - chebi86345
  - chebi86360
  - chebi86465
  - chebi8806
  - chebi91244
  details: 37 direct ingredient instances; primary coverage 35/37 (94.59%), verified
    secondary coverage 32/37 (86.49%). Percentages use a 0–100 linkage scale, not
    a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded
    rather than receiving invented pure-molecule identities.
- assessment_id: forms
  area: grounding
  topic: Chemical specificity and unresolved historical links
  outcome: unknown
  summary: All 35 primary CHEBI identifiers resolve with the recorded labels and all
    32 current secondary CHEBI keys have live registry entries. Two additional historical
    MIM links remain unresolved.
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - mim
  - legacy-search
  - chebi86360
  - chebi31345
  - chebi176843
  details: The manganese source label retains an unspecified hydrate count; its generic
    sulfate term does not verify an exact hydrate or support an anhydrous molarity
    conversion. Calcium pantothenate label correspondence is verified without claiming
    unreported stereochemical/purity specifications. Vitamin B12 remains a broad vitamer
    class, not an invented cyanocobalamin identity. Fixed hydrate labels elsewhere
    agree with inspected ontology formula/definitions. Ingredient-ID coverage is not
    evidence for any concentration.
- assessment_id: stocks
  area: representation
  topic: Main-medium versus three stock compositions
  outcome: concern
  summary: The mineral stock, synthetic seawater and vitamins are not represented
    as separate stock contexts. Their source doses are omitted or mis-typed, and four
    duplicate-name sums mix stock values.
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - owner-0
  - jcm971
  - api
  - jcm590
  - jcm244
  - jcm197
  - solution4432
  - solution3861
  - local-stocks
  details: Source additions are 250 mL synthetic seawater, 1 mL mineral stock and
    10 mL vitamin stock. The separate sulfide solution is added later. The target
    instead has 37 direct rows and zero stock descriptors. Existing local seawater/vitamin
    IDs provide exact source-identity leads for future curation; no automatic reuse,
    new ID minting or link insertion is performed. The mineral stock is defined in
    the primary JCM 971 entry itself.
- assessment_id: volume
  area: quantity
  topic: Provider denominator and source batch arithmetic
  outcome: concern
  summary: The provider volume 1107 mL includes the mineral-stock section’s 100 mL
    water as though the entire stock preparation were added to the medium. The actual
    source calls for a 1 mL aliquot.
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - jcm971
  - api
  - bacmedia
  - mapping
  details: Source liquid additions total 740+250+1+10+6=1007 mL; adding the separate
    stock-batch water produces 1107. This is a diagnostic sum, not a final-volume
    assertion. Dissolution, acid adjustment and source-volume convention remain unresolved.
    The two independent 1000 mL seawater/vitamin stock batches are likewise not direct
    final-volume additions.
- assessment_id: ph
  area: consistency
  topic: Main-medium versus stock pH and preparation order
  outcome: concern
  summary: Primary JCM instructions give main-medium pH 7.0; pH 1.0 belongs to the
    separate mineral stock. The target uses 1.0 at root and leaves the stock-acidification
    step at the main level.
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - owner-0
  - jcm971
  - api
  - bacmedia
  details: The target retains parts of the main preparation narrative, but its flattened
    ingredient ordering no longer identifies the later additions coherently. Stock
    preparation headings and acid adjustment must be scoped to the stock. The applicable
    JCM default complements the source autoclave instruction; unrelated preparation
    from JCM 197, 590 or 244 must not be copied into this receiving medium.
- assessment_id: scope
  area: scope
  topic: Classification, physical state and unsupported growth claims
  outcome: supported
  summary: COMPLEX/UNDEFINED is consistent with yeast extract and the API annotation;
    LIQUID is consistent with the absence of a solidifier. No organism, strain, taxon,
    DOI, PMID, pathway or transcriptomic assertion is present.
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - jcm971
  - api
  details: Generic cultivation and bacterial filing are not experimental growth evidence.
    No unreported organism or condition is added. Current deterministic validator
    passes do not address stock boundaries or source pH context.
- assessment_id: evidence
  area: provenance
  topic: History and missing claim-level context
  outcome: concern
  summary: The source accession, URL and transformation history are recoverable, but
    neither target nor owner includes scoped concentration evidence. The reference
    gate examined zero excerpts.
  target_ids:
  - CultureMech:003320
  evidence_ids:
  - record
  - owner-0
  - validate-references
  - jcm971
  - api
  details: The full target and its complete owner were read. Source rows, comments,
    secondary stock references and all 37 current amounts were assessed. Primary source
    section boundaries refute the scope of the provider normalization even where numbers
    match it. No generated file or historical curation entry is edited.
findings:
- finding_id: f1
  issue_key: culturemech-003320-stock-boundaries-flattened
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock compositions and cross-stock sums replace the receiving formulation
  description: The target exposes stock ingredients directly and adds four repeated-name
    quantities from different stages. The resulting 37-row composition is not the
    receiving medium specified by the primary source.
  target_ids:
  - CultureMech:003320
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - jcm971
  - api
  - jcm244
  - jcm197
  - mapping
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: culturemech-003320-stock-volume-mass-substitution
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Two stock addition volumes are encoded as mass concentrations
  description: Modified Wolfe minerals and sulfide are source volume additions, but
    target and owner encode their raw numeric doses as G_PER_L and discard concentration-context
    attributes.
  target_ids:
  - CultureMech:003320
  field_paths:
  - ingredients[4].concentration
  - ingredients[7].concentration
  evidence_ids:
  - record
  - owner-0
  - jcm971
  - api
  - mapping
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: culturemech-003320-provider-volume-scope-error
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Main normalization includes water used to prepare a separate stock
  description: Provider 1107 mL normalization incorporates a separate mineral-stock
    batch. The target copies the resulting main-recipe g_l values, which therefore
    do not establish valid final-medium concentrations.
  target_ids:
  - CultureMech:003320
  field_paths:
  - ingredients[0:4].concentration
  - ingredients[5:7].concentration
  evidence_ids:
  - record
  - owner-0
  - jcm971
  - api
  - bacmedia
  - mapping
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: culturemech-003320-stock-ph-promoted-to-medium
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Stock acidification is applied to the main medium
  description: The source main-medium pH and stock pH have distinct scopes. The target
    root pH and final unscoped preparation step apply the stock value to the receiving
    medium.
  target_ids:
  - CultureMech:003320
  field_paths:
  - ph_value
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm971
  - api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f5
  issue_key: culturemech-003320-evidence-stage-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source references lack claim and preparation-stage evidence
  description: No target/owner amount assertion has a scoped supporting excerpt that
    distinguishes main medium, stock composition or stock addition. A recoverable
    URL and matching provider value do not resolve that omission.
  target_ids:
  - CultureMech:003320
  field_paths:
  - ingredients[*].evidence
  - references
  - notes
  evidence_ids:
  - record
  - owner-0
  - validate-references
  - jcm971
  - api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Restore the stock/receiving-medium structure in maintained inputs and
    inspect source-specific importer/nesting behavior. Reuse existing source-identified
    stocks only after checking their exact content. Do not flatten unchanged stock
    concentrations or sum different stages.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003320
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml
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
  - Review the complete primary JCM 971 page and its referenced stock sections; do
    not accept a matching API number without preparation-stage agreement.
  - Retain stock composition, actual addition dose, source water basis and unknown
    final-volume/percent/hydrate details separately.
- action_id: a2
  description: Preserve each original volume dose, source stock identity and timing
    in schema-supported fields. Retain the unspecified sulfide percentage basis; do
    not infer a mass from volume without evidence.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003320
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml
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
  - Review the complete primary JCM 971 page and its referenced stock sections; do
    not accept a matching API number without preparation-stage agreement.
  - Retain stock composition, actual addition dose, source water basis and unknown
    final-volume/percent/hydrate details separately.
- action_id: a3
  description: Reconcile original mass and stock-dose boundaries before re-normalizing.
    Preserve unresolved final volume explicitly and correct the maintained source
    transform rather than merely trusting provider g_l.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003320
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml
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
  - Review the complete primary JCM 971 page and its referenced stock sections; do
    not accept a matching API number without preparation-stage agreement.
  - Retain stock composition, actual addition dose, source water basis and unknown
    final-volume/percent/hydrate details separately.
- action_id: a4
  description: Restore main and stock conditions to their separate source-defined
    scopes, including preparation-stage boundaries. Retain the primary-source distinction
    even where provider summary metadata is wrong.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003320
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml
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
  - Review the complete primary JCM 971 page and its referenced stock sections; do
    not accept a matching API number without preparation-stage agreement.
  - Retain stock composition, actual addition dose, source water basis and unknown
    final-volume/percent/hydrate details separately.
- action_id: a5
  description: Attach concise exact primary-source excerpts and section locators to
    the restructured maintained claims, including unresolved or conflicting source
    metadata rather than masking it.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:003320
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_sme_medium_for_ya.yaml
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
  - Review the complete primary JCM 971 page and its referenced stock sections; do
    not accept a matching API number without preparation-stage agreement.
  - Retain stock composition, actual addition dose, source water basis and unknown
    final-volume/percent/hydrate details separately.
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- Exact final-medium volume remains unresolved after restoring source stock boundaries.
  A sum of source liquid additions is not an independently measured final volume;
  no new final concentrations are asserted.
- The sulfide stock percentage basis and manganese-sulfate hydrate count are unspecified.
  No density, fixed hydrate, molarity or percent conversion is inferred.
- The two local stock records were inspected for identity, composition and root context
  only; their entire evidence/history was not fully reviewed because the initial combined
  output was truncated. This bundle does not certify those records.
- Two historical MIM identifiers remain unresolved; valid primary CHEBI identities
  do not prove their historical meaning.
tags:
- unreviewed-records
- batch-004
- generated-medium
```
