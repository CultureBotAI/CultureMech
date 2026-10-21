# Stage 5 post-remediation verification across all 17 curated records and 9 carried-forward Stage 4 findings (Issues #634, #635, and #645)

- Review: 20261021T071800Z-stage5-remediation-verification
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T07:10:00Z
- Finished UTC: 2026-10-21T07:18:00Z
- Reviewer: antigravity-agent (independent)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Verified complete resolution of all 9 carried-forward Stage 4 findings (CM-C1S4-001 through CM-C1S4-009) and all 17 open findings across the 6 predecessor structured review bundles (20261017T084036Z through 20261017T090539Z) under GitHub Issues #634 (GRP-C1S5-001), #635 (GRP-C1S5-002), and #645. All 17 remediated YAML records were written through the native guarded writer (write_validated_recipe + record_curation_event) and pass scripts/validate_strict.py with 0 errors and scripts/batch_review_recipes.py with 0 errors/warnings.

## Scope And Provenance

Complete post-remediation re-review of all 17 normalized and merged YAML records modified to resolve Stage 4 carried-forward findings CM-C1S4-001..CM-C1S4-009 and GitHub Issues #634, #635, and #645.

Selection: All 17 target records from the 6 Stage 4 structured review bundles and their linked source/merge duplicates.
Coverage: full; 17 reviewed / 17 in the declared population.
Source: working_tree at Git base 71153bc25dfe85bf0ac858d786aadc52f92d69e2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| target-1 | data/merge_yaml/merged/THERMOVENABULUM_MEDIUM.yaml | maintained | CultureMech:002143 - thermovenabulum_medium_dsmz_962a (merged) |
| target-2 | data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml | maintained | CultureMech:002143 - thermovenabulum_medium_dsmz_962a (bacterial) |
| target-3 | data/normalized_yaml/bacterial/thermovenabulum_medium.yaml | maintained | CultureMech:000714 - thermovenabulum_medium_dsmz_1255 (bacterial) |
| target-4 | data/normalized_yaml/bacterial/KOMODO_1255_THERMOVENABULUM_medium.yaml | maintained | CultureMech:004016 - thermovenabulum_medium_dsmz_1255 (KOMODO 1255) |
| target-5 | data/merge_yaml/merged/thermovenabulum_medium__41e13ba4.yaml | maintained | CultureMech:004016 - thermovenabulum_medium_dsmz_1255 (merged) |
| target-6 | data/normalized_yaml/bacterial/KOMODO_962_THERMOVENABULUM_medium.yaml | maintained | CultureMech:006919 - thermovenabulum_medium_dsmz_962 (KOMODO 962) |
| target-7 | data/normalized_yaml/bacterial/for_dsm_14005.yaml | maintained | CultureMech:006918 - for_dsm_14005 (DSMZ 962 duplicate) |
| target-8 | data/normalized_yaml/bacterial/thermincola_ferriacetica_medium.yaml | maintained | CultureMech:002142 - thermincola_ferriacetica_medium (DSMZ 962) |
| target-9 | data/merge_yaml/merged/THERMINCOLA_FERRIACETICA_MEDIUM.yaml | maintained | CultureMech:002142 - thermincola_ferriacetica_medium (merged) |
| target-10 | data/normalized_yaml/algae/Bold_Basal_Medium.yaml | maintained | CultureMech:000034 - bold_basal_medium (algae) |
| target-11 | data/normalized_yaml/archaea/DSMZ_1399_HALOPHILIC_MEDIUM.yaml | maintained | CultureMech:000252 - halophilic_medium (archaea) |
| target-12 | data/normalized_yaml/bacterial/1_10_r2a_broth.yaml | maintained | CultureMech:003150 - 1_10_r2a_broth (bacterial) |
| target-13 | data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml | maintained | CultureMech:007843 - methylotroph_medium (bacterial) |
| target-14 | data/normalized_yaml/fungal/yeast_optimized_defined_medium_glucose.yaml | maintained | CultureMech:010554 - yeast_optimized_defined_medium_glucose (fungal) |
| target-15 | data/normalized_yaml/bacterial/mediadive_177_Main_sol_104a.yaml | maintained | CultureMech:011215 - Main sol. 104a (SolutionRecipe) |
| target-16 | data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml | maintained | CultureMech:015445 - das_vitamin_cocktail (SolutionRecipe) |
| target-17 | data/normalized_yaml/specialized/2x_uga_defined_nocarbon.yaml | maintained | CultureMech:015480 - 2x_uga_defined_nocarbon (specialized) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict LinkML and reference validation across all 17 remediated YAML records | passed | True | target-1, target-2, target-3, target-4, target-5, target-6, target-7, target-8, target-9, target-10, target-11, target-12, target-13, target-14, target-15, target-16, target-17 | All 17 remediated normalized and merged YAML files pass scripts/validate_strict.py with 0 schema, term, or reference errors. |
| Targeted pytest suite covering KOMODO 962 signature, concentration evidence, UTEX BBM, and batch_review_recipes | passed | True | target-1, target-2, target-3, target-4, target-5, target-6, target-7, target-8, target-9, target-10, target-11, target-12, target-13, target-14, target-15, target-16, target-17 | 115 / 115 unit and regression tests pass after updating schema slots and KOMODO 962 scaled concentration signatures. |

## Scientific And Domain Assessments

### Thermovenabulum / Thermincola family (DSMZ 962a, 1255, 962) nomenclature, stock scaling, and merge schema (Issues #634 and #645)

quantity: supported. Targets: target-1, target-2, target-3, target-4, target-5, target-6, target-7, target-8, target-9.

All 9 records in the Thermovenabulum / Thermincola cohort (target-1..target-9) now carry distinct formulation-specific names, properly scaled per-liter trace element (1:100 or 1:1000) and vitamin (1:100) concentrations, deduplicated CaCl2 x 2 H2O (0.327409 G_PER_L in DSMZ 962/962a; 0.0988142 G_PER_L in DSMZ 1255), 100% MediaIngredientMech/CHEBI grounding across all defined chemical constituents (31/33 in DSMZ 962/962a; 30/32 in DSMZ 1255), and valid LinkML schema declarations.

### Cross-category record and solution remediation across CultureMech:000034, 000252, 003150, 007843, 010554, 011215, 015445, and 015480 (Issues #635 and #645)

grounding: supported. Targets: target-10, target-11, target-12, target-13, target-14, target-15, target-16, target-17.

All 8 curated media and solution records in Group 2 (target-10..target-17) have complete canonical ontology grounding on all defined chemical constituents, accurate medium_type/composition_type classifications, consistent units, deduplicated mineral salts, and zero stale data_quality_flags or placeholder ingredients.

## Findings

### F1: Commercial premix R2A broth (DAIGO) linked via culturemech_term and sub-ingredient breakdown documented in 1_10_r2a_broth.yaml

minor / resolved / confirmed; issue key: grounding.missing_mim_term.CultureMech_003150.r2a_broth_daigo.

Linked R2A broth (DAIGO) to CultureMech:003183 (R2A Broth) via culturemech_term and added an explicit 1/10 R2A constituent breakdown note in data/normalized_yaml/bacterial/1_10_r2a_broth.yaml.

Disposition: Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-004) via write_validated_recipe.

### F2: Solvent Distilled water (1.0 L) removed from solute ingredient list in 1_10_r2a_broth.yaml

informational / resolved / confirmed; issue key: representation.batch_water_volume.CultureMech_003150.

Removed redundant Distilled water (1.0 L) solvent entry from ingredients[] in 1_10_r2a_broth.yaml (retaining the 1.0 L solvent volume in preparation_steps and notes) so all solute concentrations are normalized per liter.

Disposition: Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-004) via write_validated_recipe.

### F3: UTEX algal SolutionRecipe DAS_Vitamin_Cocktail.yaml reclassified to category: algae with snake_case name

major / resolved / confirmed; issue key: scope.misclassified_category.CultureMech_015445.

Updated DAS_Vitamin_Cocktail.yaml (CultureMech:015445) to category: algae and name: das_vitamin_cocktail.

Disposition: Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-007) via write_validated_recipe.

### F4: All 6 composition items on DAS_Vitamin_Cocktail.yaml grounded to canonical ChEBI/MIM terms and root SolutionRecipe routing term documented

minor / resolved / confirmed; issue key: grounding.unmapped_root_solution_term.CultureMech_015445.

Populated canonical ChEBI labels and mediaingredientmech_chebi_term across all 6/6 composition items in DAS_Vitamin_Cocktail.yaml (including calcium pantothenate CHEBI:31345) while retaining root term MediaIngredientMech:UNMAPPED_0045 required by scripts/record_kinds.py:has_solution_shape() for SolutionRecipe schema routing.

Disposition: Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-007) via write_validated_recipe.

### F5: UTEX Vitamin B12 table vs. Directions sterilization note reconciled in DAS_Vitamin_Cocktail.yaml

minor / resolved / confirmed; issue key: provenance.sterilization_conflict.CultureMech_015445.vitamin_b12.

Documented the UTEX source discrepancy between the ingredient table annotation '(add after autoclaving)' on Vitamin B12 (0.0008 g/100 mL = 0.008 G_PER_L) and the UTEX Directions protocol (filter-sterilize the entire solution through a 0.45 µm Millipore filter without heat sterilization) on composition[3] and top-level notes of DAS_Vitamin_Cocktail.yaml.

Disposition: Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-007) via write_validated_recipe.

### F6: LinkML schema root and merge metadata slots aligned in culturemech.yaml

major / resolved / confirmed; issue key: schema.undeclared_merge_slots.merge_recipes.

Set tree_root: true on MediaRecipe and declared SolutionRecipe merge/provenance slots in src/culturemech/schema/culturemech.yaml so both normalized and merged records validate cleanly.

Disposition: Resolved in Stage 5 under Issue #634 (CM-C1S4-001) and verified with scripts/validate_strict.py.

### F7: Scaled 100x-1000x trace element and vitamin stocks and deduplicated CaCl2 x 2 H2O across all Thermovenabulum / Thermincola records

major / resolved / confirmed; issue key: concentration.unscaled_stock_inlining.thermovenabulum_family.

Applied 1:100 (10 mL/L) and 1:1000 (1 mL/L) dilution factors to flattened Wolin trace element and vitamin stock components across target-1..target-9 and consolidated duplicate CaCl2 x 2 H2O to 0.327409 G_PER_L in DSMZ 962/962a and 0.0988142 G_PER_L in DSMZ 1255.

Disposition: Resolved in Stage 5 under Issues #634 and #645 (CM-C1S4-002) via write_validated_recipe.

### F8: Populated missing mediaingredientmech_chebi_term across all defined chemical ingredients in Thermovenabulum family records

minor / resolved / confirmed; issue key: grounding.missing_mim_term.CultureMech_002143.

Added canonical OBO ChEBI labels and mediaingredientmech_chebi_term mappings across all defined chemical ingredients (including resazurin, nitrilotriacetic acid, calcium pantothenate, and sodium selenite; 31/33 in DSMZ 962/962a and 30/32 in DSMZ 1255; complex Meat extract and Yeast extract retain MediaIngredientMech IDs) across target-1..target-9.

Disposition: Resolved in Stage 5 under Issues #634 and #645 (CM-C1S4-001/002) via write_validated_recipe.

### F9: Disambiguated DSMZ 962a, DSMZ 1255, and DSMZ 962 names across the Thermovenabulum family

major / resolved / confirmed; issue key: nomenclature.name_collision.thermovenabulum_family.

Assigned distinct snake_case names: thermovenabulum_medium_dsmz_962a (DSMZ 962a), thermovenabulum_medium_dsmz_1255 (DSMZ 1255), and thermovenabulum_medium_dsmz_962 (KOMODO 962), synchronized THERMINCOLA_FERRIACETICA_MEDIUM.yaml variant_children and scripts/repair_komodo_962_thermincola_score10.py, and updated data/culturemech_recipe_catalog.tsv.

Disposition: Resolved in Stage 5 under Issues #634 and #645 (CM-C1S4-001) via write_validated_recipe.

### F10: Corrected medium_type and composition_type to DEFINED on TOGO_M1308_Methylotroph_Medium.yaml

minor / resolved / confirmed; issue key: representation.defined_misclassified_as_complex.CultureMech_007843.

Updated TOGO_M1308_Methylotroph_Medium.yaml (CultureMech:007843) to medium_type: DEFINED and composition_type: DEFINED.

Disposition: Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-004/005) via write_validated_recipe.

### F11: Grounded CaCl2.2H2O, MgCl2.6H2O, and all 24 nested solution items in TOGO_M1308_Methylotroph_Medium.yaml

minor / resolved / confirmed; issue key: grounding.missing_mim_term.CultureMech_007843.hydrates_and_nested_solutions.

Populated canonical ChEBI labels, mediaingredientmech_chebi_term, and JCM 1219 concentration evidence on all 6 main-table solutes (including CaCl2.2H2O 0.07 G_PER_L and MgCl2.6H2O 0.2 G_PER_L) and all 24 nested solutions[].composition[] items in TOGO_M1308_Methylotroph_Medium.yaml.

Disposition: Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-004/005) via write_validated_recipe.

### F12: Documented 994.81 mL pre-methanol / 999.81 mL post-methanol cumulative liquid addition denominator note in TOGO_M1308_Methylotroph_Medium.yaml

informational / resolved / confirmed; issue key: quantity.volume_denominator_offset.CultureMech_007843.

Added explicit preparation note documenting the 990 mL water + 4.81 mL stock solutions = 994.81 mL before methanol (999.81 mL including 5 mL filter-sterilized methanol) in TOGO_M1308_Methylotroph_Medium.yaml.

Disposition: Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-004/005) via write_validated_recipe.

### F13: Removed placeholder ingredients[] and normalized 0.96 L water and defined chemical ChEBI/MIM terms in mediadive_177_Main_sol_104a.yaml

major / resolved / confirmed; issue key: tooling.solution_validator_blind_spots.batch_review_recipes.

Removed obsolete placeholder ingredients[] and data_quality_flags: [incomplete_composition], converted Distilled water from 960 PERCENT_V_V to 0.96 L, and populated canonical ChEBI/MIM grounding on all 6/9 defined chemical constituents in mediadive_177_Main_sol_104a.yaml (alongside PR #632 fix for Issue #633 in scripts/batch_review_recipes.py).

Disposition: Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-009) via write_validated_recipe.

### F14: Completed canonical CHEBI/MIM grounding and removed stale flags across archaea, bacterial, fungal, and specialized representatives

minor / resolved / confirmed; issue key: grounding.cross_category_mim_and_chebi_gaps.representatives.

Normalized Distilled water to CHEBI:15377 ('water') across 11/13 defined chemical constituents in DSMZ_1399_HALOPHILIC_MEDIUM.yaml, mapped DL-Serine (CHEBI:17822, 'DL-serine') and all 28/28 MIM terms in yeast_optimized_defined_medium_glucose.yaml, and populated 29/29 canonical ChEBI/MIM terms and removed stale has_unmapped_ingredients flag in 2x_uga_defined_nocarbon.yaml.

Disposition: Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-006/008) via write_validated_recipe.

### F15: Set DEFINED on Bold_Basal_Medium.yaml and deduplicated flattened Wolfe's mineral salts in 2x_uga_defined_nocarbon.yaml

minor / resolved / confirmed; issue key: representation.defined_misclassification_and_duplicate_salts.representatives.

Updated Bold_Basal_Medium.yaml (CultureMech:000034) to medium_type: DEFINED / composition_type: DEFINED with canonical ChEBI labels and clarified the UTEX MnCl2.4H2O source note; normalized name to 2x_uga_defined_nocarbon and consolidated duplicate MgSO4.7H2O (0.9919 G_PER_L), CaCl2.2H2O (0.0314 G_PER_L), and NaCl (0.0399 G_PER_L) from 32 entries to 29 unique ingredients in 2x_uga_defined_nocarbon.yaml.

Disposition: Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-003/008) via write_validated_recipe.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | scripts/validate_strict.py and pytest regression suite; src/culturemech/schema/culturemech.yaml and target-1..target-17 | supports | Setting tree_root: true on MediaRecipe and declaring SolutionRecipe provenance/merge slots in src/culturemech/schema/culturemech.yaml enables strict validation across all 17 remediated records with 0 errors and 115 passing tests. |
| E2 | Direct inspection of remediated YAML records target-1..target-17 and DSMZ/UTEX/TOGO/ATCC sources; target-1..target-17 | supports | Group 1 (#634/#645, target-1..target-9): Disambiguated DSMZ 962a (thermovenabulum_medium_dsmz_962a), DSMZ 1255 (thermovenabulum_medium_dsmz_1255), and DSMZ 962 (thermovenabulum_medium_dsmz_962 / thermincola_ferriacetica_medium); synchronized variant_children in THERMINCOLA_FERRIACETICA_MEDIUM.yaml and scripts/repair_komodo_962_thermincola_score10.py; scaled 10 mL/L (1:100) and 1 mL/L (1:1000) trace/vitamin stocks to final per-liter concentrations (CaCl2 x 2 H2O deduplicated to 0.327409 G_PER_L in the 6 DSMZ 962/962a records and 0.0988142 G_PER_L in the 3 DSMZ 1255 records); and populated canonical OBO ChEBI labels and mediaingredientmech_chebi_term links on 100% of defined chemical ingredients (31/33 in DSMZ 962/962a; 30/32 in DSMZ 1255; complex Meat extract and Yeast extract retain MediaIngredientMech IDs without ChEBI terms). Group 2 (#635/#645, target-10..target-17): Set DEFINED and canonical OBO ChEBI labels on Bold_Basal_Medium.yaml (CultureMech:000034) and TOGO_M1308_Methylotroph_Medium.yaml (CultureMech:007843, with JCM 1219 concentration evidence on all 6 main-table solutes and 994.81 mL pre-methanol / 999.81 mL post-methanol batch volume note); normalized DAS_Vitamin_Cocktail.yaml (CultureMech:015445) to category: algae, name: das_vitamin_cocktail, 6/6 composition items mapped to canonical ChEBI/MIM terms (Vitamin B12 0.008 G_PER_L from 0.0008 g/100 mL), reconciled the UTEX table vs. Directions Vitamin B12 sterilization note, and retained root term MediaIngredientMech:UNMAPPED_0045 for SolutionRecipe routing; removed Distilled water (1.0 L) from ingredients[] in 1_10_r2a_broth.yaml and linked R2A broth (DAIGO) to CultureMech:003183 via culturemech_term; removed placeholder ingredients[] and normalized 0.96 L water and 6/9 defined chemical ChEBI/MIM terms in mediadive_177_Main_sol_104a.yaml; grounded DL-Serine (CHEBI:17822, 'DL-serine') and all 28/28 MIM terms in yeast_optimized_defined_medium_glucose.yaml; normalized Distilled water to CHEBI:15377 ('water') across 11/13 defined chemical items in DSMZ_1399_HALOPHILIC_MEDIUM.yaml; and consolidated the 3 duplicate basal + Wolfe mineral salt pairs (MgSO4.7H2O 0.9919 G_PER_L, CaCl2.2H2O 0.0314 G_PER_L, NaCl 0.0399 G_PER_L) from 32 entries to 29 unique ingredients with 29/29 canonical ChEBI/MIM terms in 2x_uga_defined_nocarbon.yaml. |

## Limits And Additional Notes


## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T071800Z-stage5-remediation-verification
kind: batch
repository: CultureBotAI/CultureMech
title: 'Stage 5 post-remediation verification across all 17 curated records and 9
  carried-forward Stage 4 findings (Issues #634, #635, and #645)'
started_at: '2026-10-21T07:10:00Z'
finished_at: '2026-10-21T07:18:00Z'
reviewer:
  identity: antigravity-agent
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Post-remediation verification against primary DSMZ/UTEX/TOGO/ATCC
    formulations, strict LinkML validation (scripts/validate_strict.py), and batch_review_recipes.py.
skill: review-recipes
completion: completed
verdict: pass
scientific_review: true
summary: 'Verified complete resolution of all 9 carried-forward Stage 4 findings (CM-C1S4-001
  through CM-C1S4-009) and all 17 open findings across the 6 predecessor structured
  review bundles (20261017T084036Z through 20261017T090539Z) under GitHub Issues #634
  (GRP-C1S5-001), #635 (GRP-C1S5-002), and #645. All 17 remediated YAML records were
  written through the native guarded writer (write_validated_recipe + record_curation_event)
  and pass scripts/validate_strict.py with 0 errors and scripts/batch_review_recipes.py
  with 0 errors/warnings.'
source:
  git_revision: 71153bc25dfe85bf0ac858d786aadc52f92d69e2
  state: working_tree
  inputs:
  - path: data/merge_yaml/merged/THERMINCOLA_FERRIACETICA_MEDIUM.yaml
    sha256: 748582cc605064b827008de155ad703ed3e0a14892c5d9495ae5d08b4f12db11
    role: target
  - path: data/merge_yaml/merged/THERMOVENABULUM_MEDIUM.yaml
    sha256: 3182fc075d0ded6ca6075b52f591c811b46e7ada2926fd731880143277137559
    role: target
  - path: data/merge_yaml/merged/thermovenabulum_medium__41e13ba4.yaml
    sha256: c0558aca1f9c867d835550d5436bcdd8b7199294841f9edd71e868ec21ae9d54
    role: target
  - path: data/normalized_yaml/algae/Bold_Basal_Medium.yaml
    sha256: acb96b82f986ecdbeaefaa21a1795e61188087e0b961bb9b03f777816c515aa1
    role: target
  - path: data/normalized_yaml/archaea/DSMZ_1399_HALOPHILIC_MEDIUM.yaml
    sha256: 2fa9a8450f6c8a00f4f2105f339924dc0c9327fe9c1e0925db62075bb40e229b
    role: target
  - path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    sha256: 05520acad242488257e1cfc827f51db63f543963021dd2dc1c1ead095fa0d3d7
    role: target
  - path: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    sha256: a9a04bb1818744b936752d1e5c9bd18ac068e6748da6b51c59f564654f3d2a7d
    role: target
  - path: data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml
    sha256: ee9a4efa2e2145a369770d6642a800aefbda0c7b1183b126fa6c6d3076173586
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1255_THERMOVENABULUM_medium.yaml
    sha256: 481f8626e979b2cac180d686be434fad232c61b8ac8a7693b5d484b89ca1db4c
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_962_THERMOVENABULUM_medium.yaml
    sha256: 33c4e0293b8ad59e6db892d04512247e731beb21b9bd826af2c74b448cf7907d
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml
    sha256: 285cfbdfea1ba07ac2b0fa5f97dee2d14b8576f5a0c6ab24d59ce45349ff75bd
    role: target
  - path: data/normalized_yaml/bacterial/for_dsm_14005.yaml
    sha256: 0f64dbfbdfc6fe2fb280e2f39954514c7e21c2a9e08e2722644f3a03171f7812
    role: target
  - path: data/normalized_yaml/bacterial/mediadive_177_Main_sol_104a.yaml
    sha256: b2a9db2818630ed6bd78fcefac2ab45ecec6233444142d733ea195f9db69a19a
    role: target
  - path: data/normalized_yaml/bacterial/thermincola_ferriacetica_medium.yaml
    sha256: 3df022179b998a051fa88cceacdf481623a54499aba6e1eba6ab21507f627ed0
    role: target
  - path: data/normalized_yaml/bacterial/thermovenabulum_medium.yaml
    sha256: d7e38c8e75c074d19cbfb898a0f717a36de826ca0f4fb11d99dd31bb5318e9f2
    role: target
  - path: data/normalized_yaml/fungal/yeast_optimized_defined_medium_glucose.yaml
    sha256: 53c8b7058e1c840aaf59ec5a8ba6b43145f4d0c6a5a7a8d311896cca79d7788f
    role: target
  - path: data/normalized_yaml/specialized/2x_uga_defined_nocarbon.yaml
    sha256: 744578bc12e030aed4e3c84c32ba84d87119007f573af562d138f35b661ebdad
    role: target
  - path: scripts/batch_review_recipes.py
    sha256: 5d4f6c3a8ec68568ecd992544b39edc3c205c3e52172cd2fed33719380de2f50
    role: context
  - path: scripts/repair_komodo_962_thermincola_score10.py
    sha256: 2f41008043b66fe1e831fe7688ca947caaaf8208f9f1a775a19c67816361e5ed
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: a7ecdd03134461a7c16790cd152f6d0d5b5835e21d66c09117f500d876db187b
    role: context
scope:
  description: 'Complete post-remediation re-review of all 17 normalized and merged
    YAML records modified to resolve Stage 4 carried-forward findings CM-C1S4-001..CM-C1S4-009
    and GitHub Issues #634, #635, and #645.'
  selection: All 17 target records from the 6 Stage 4 structured review bundles and
    their linked source/merge duplicates.
  coverage: full
  population_size: 17
  reviewed_target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  - target-7
  - target-8
  - target-9
  - target-10
  - target-11
  - target-12
  - target-13
  - target-14
  - target-15
  - target-16
  - target-17
targets:
- target_id: target-1
  path: data/merge_yaml/merged/THERMOVENABULUM_MEDIUM.yaml
  label: CultureMech:002143 - thermovenabulum_medium_dsmz_962a (merged)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/merge_yaml/merged/THERMOVENABULUM_MEDIUM.yaml
    role: maintained_record
- target_id: target-2
  path: data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml
  label: CultureMech:002143 - thermovenabulum_medium_dsmz_962a (bacterial)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml
    role: maintained_record
- target_id: target-3
  path: data/normalized_yaml/bacterial/thermovenabulum_medium.yaml
  label: CultureMech:000714 - thermovenabulum_medium_dsmz_1255 (bacterial)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thermovenabulum_medium.yaml
    role: maintained_record
- target_id: target-4
  path: data/normalized_yaml/bacterial/KOMODO_1255_THERMOVENABULUM_medium.yaml
  label: CultureMech:004016 - thermovenabulum_medium_dsmz_1255 (KOMODO 1255)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1255_THERMOVENABULUM_medium.yaml
    role: maintained_record
- target_id: target-5
  path: data/merge_yaml/merged/thermovenabulum_medium__41e13ba4.yaml
  label: CultureMech:004016 - thermovenabulum_medium_dsmz_1255 (merged)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/merge_yaml/merged/thermovenabulum_medium__41e13ba4.yaml
    role: maintained_record
- target_id: target-6
  path: data/normalized_yaml/bacterial/KOMODO_962_THERMOVENABULUM_medium.yaml
  label: CultureMech:006919 - thermovenabulum_medium_dsmz_962 (KOMODO 962)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_962_THERMOVENABULUM_medium.yaml
    role: maintained_record
- target_id: target-7
  path: data/normalized_yaml/bacterial/for_dsm_14005.yaml
  label: CultureMech:006918 - for_dsm_14005 (DSMZ 962 duplicate)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14005.yaml
    role: maintained_record
- target_id: target-8
  path: data/normalized_yaml/bacterial/thermincola_ferriacetica_medium.yaml
  label: CultureMech:002142 - thermincola_ferriacetica_medium (DSMZ 962)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thermincola_ferriacetica_medium.yaml
    role: maintained_record
- target_id: target-9
  path: data/merge_yaml/merged/THERMINCOLA_FERRIACETICA_MEDIUM.yaml
  label: CultureMech:002142 - thermincola_ferriacetica_medium (merged)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/merge_yaml/merged/THERMINCOLA_FERRIACETICA_MEDIUM.yaml
    role: maintained_record
- target_id: target-10
  path: data/normalized_yaml/algae/Bold_Basal_Medium.yaml
  label: CultureMech:000034 - bold_basal_medium (algae)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/Bold_Basal_Medium.yaml
    role: maintained_record
- target_id: target-11
  path: data/normalized_yaml/archaea/DSMZ_1399_HALOPHILIC_MEDIUM.yaml
  label: CultureMech:000252 - halophilic_medium (archaea)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/DSMZ_1399_HALOPHILIC_MEDIUM.yaml
    role: maintained_record
- target_id: target-12
  path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
  label: CultureMech:003150 - 1_10_r2a_broth (bacterial)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    role: maintained_record
- target_id: target-13
  path: data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml
  label: CultureMech:007843 - methylotroph_medium (bacterial)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml
    role: maintained_record
- target_id: target-14
  path: data/normalized_yaml/fungal/yeast_optimized_defined_medium_glucose.yaml
  label: CultureMech:010554 - yeast_optimized_defined_medium_glucose (fungal)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/yeast_optimized_defined_medium_glucose.yaml
    role: maintained_record
- target_id: target-15
  path: data/normalized_yaml/bacterial/mediadive_177_Main_sol_104a.yaml
  label: CultureMech:011215 - Main sol. 104a (SolutionRecipe)
  record_class: SolutionRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_177_Main_sol_104a.yaml
    role: maintained_record
- target_id: target-16
  path: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
  label: CultureMech:015445 - das_vitamin_cocktail (SolutionRecipe)
  record_class: SolutionRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    role: maintained_record
- target_id: target-17
  path: data/normalized_yaml/specialized/2x_uga_defined_nocarbon.yaml
  label: CultureMech:015480 - 2x_uga_defined_nocarbon (specialized)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/2x_uga_defined_nocarbon.yaml
    role: maintained_record
checks:
- check_id: chk-validate-strict-all-17
  name: Strict LinkML and reference validation across all 17 remediated YAML records
  status: passed
  required: true
  summary: All 17 remediated normalized and merged YAML files pass scripts/validate_strict.py
    with 0 schema, term, or reference errors.
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  - target-7
  - target-8
  - target-9
  - target-10
  - target-11
  - target-12
  - target-13
  - target-14
  - target-15
  - target-16
  - target-17
  command: python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - E1
  - E2
- check_id: chk-pytest-remediation-suite
  name: Targeted pytest suite covering KOMODO 962 signature, concentration evidence,
    UTEX BBM, and batch_review_recipes
  status: passed
  required: true
  summary: 115 / 115 unit and regression tests pass after updating schema slots and
    KOMODO 962 scaled concentration signatures.
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  - target-7
  - target-8
  - target-9
  - target-10
  - target-11
  - target-12
  - target-13
  - target-14
  - target-15
  - target-16
  - target-17
  command: pytest tests/test_repair_komodo_962_thermincola_score10.py tests/test_jcm_concentration_evidence.py
    tests/test_utex_bristol_bbm.py tests/test_batch_review_recipes.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - E1
  - E2
evidence:
- evidence_id: E1
  kind: validation
  reference: scripts/validate_strict.py and pytest regression suite
  locator: src/culturemech/schema/culturemech.yaml and target-1..target-17
  accessed_at: '2026-10-21T07:15:00Z'
  support: supports
  summary: 'Setting tree_root: true on MediaRecipe and declaring SolutionRecipe provenance/merge
    slots in src/culturemech/schema/culturemech.yaml enables strict validation across
    all 17 remediated records with 0 errors and 115 passing tests.'
- evidence_id: E2
  kind: record_content
  reference: Direct inspection of remediated YAML records target-1..target-17 and
    DSMZ/UTEX/TOGO/ATCC sources
  locator: target-1..target-17
  accessed_at: '2026-10-21T07:16:00Z'
  support: supports
  summary: 'Group 1 (#634/#645, target-1..target-9): Disambiguated DSMZ 962a (thermovenabulum_medium_dsmz_962a),
    DSMZ 1255 (thermovenabulum_medium_dsmz_1255), and DSMZ 962 (thermovenabulum_medium_dsmz_962
    / thermincola_ferriacetica_medium); synchronized variant_children in THERMINCOLA_FERRIACETICA_MEDIUM.yaml
    and scripts/repair_komodo_962_thermincola_score10.py; scaled 10 mL/L (1:100) and
    1 mL/L (1:1000) trace/vitamin stocks to final per-liter concentrations (CaCl2
    x 2 H2O deduplicated to 0.327409 G_PER_L in the 6 DSMZ 962/962a records and 0.0988142
    G_PER_L in the 3 DSMZ 1255 records); and populated canonical OBO ChEBI labels
    and mediaingredientmech_chebi_term links on 100% of defined chemical ingredients
    (31/33 in DSMZ 962/962a; 30/32 in DSMZ 1255; complex Meat extract and Yeast extract
    retain MediaIngredientMech IDs without ChEBI terms). Group 2 (#635/#645, target-10..target-17):
    Set DEFINED and canonical OBO ChEBI labels on Bold_Basal_Medium.yaml (CultureMech:000034)
    and TOGO_M1308_Methylotroph_Medium.yaml (CultureMech:007843, with JCM 1219 concentration
    evidence on all 6 main-table solutes and 994.81 mL pre-methanol / 999.81 mL post-methanol
    batch volume note); normalized DAS_Vitamin_Cocktail.yaml (CultureMech:015445)
    to category: algae, name: das_vitamin_cocktail, 6/6 composition items mapped to
    canonical ChEBI/MIM terms (Vitamin B12 0.008 G_PER_L from 0.0008 g/100 mL), reconciled
    the UTEX table vs. Directions Vitamin B12 sterilization note, and retained root
    term MediaIngredientMech:UNMAPPED_0045 for SolutionRecipe routing; removed Distilled
    water (1.0 L) from ingredients[] in 1_10_r2a_broth.yaml and linked R2A broth (DAIGO)
    to CultureMech:003183 via culturemech_term; removed placeholder ingredients[]
    and normalized 0.96 L water and 6/9 defined chemical ChEBI/MIM terms in mediadive_177_Main_sol_104a.yaml;
    grounded DL-Serine (CHEBI:17822, ''DL-serine'') and all 28/28 MIM terms in yeast_optimized_defined_medium_glucose.yaml;
    normalized Distilled water to CHEBI:15377 (''water'') across 11/13 defined chemical
    items in DSMZ_1399_HALOPHILIC_MEDIUM.yaml; and consolidated the 3 duplicate basal
    + Wolfe mineral salt pairs (MgSO4.7H2O 0.9919 G_PER_L, CaCl2.2H2O 0.0314 G_PER_L,
    NaCl 0.0399 G_PER_L) from 32 entries to 29 unique ingredients with 29/29 canonical
    ChEBI/MIM terms in 2x_uga_defined_nocarbon.yaml.'
assessments:
- assessment_id: A1
  area: quantity
  topic: 'Thermovenabulum / Thermincola family (DSMZ 962a, 1255, 962) nomenclature,
    stock scaling, and merge schema (Issues #634 and #645)'
  outcome: supported
  summary: All 9 records in the Thermovenabulum / Thermincola cohort (target-1..target-9)
    now carry distinct formulation-specific names, properly scaled per-liter trace
    element (1:100 or 1:1000) and vitamin (1:100) concentrations, deduplicated CaCl2
    x 2 H2O (0.327409 G_PER_L in DSMZ 962/962a; 0.0988142 G_PER_L in DSMZ 1255), 100%
    MediaIngredientMech/CHEBI grounding across all defined chemical constituents (31/33
    in DSMZ 962/962a; 30/32 in DSMZ 1255), and valid LinkML schema declarations.
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  - target-7
  - target-8
  - target-9
  evidence_ids:
  - E1
  - E2
  metrics:
  - name: thermovenabulum_cohort_defined_chemical_mim_coverage
    value: 100.0
    unit: percent
    definition: Percentage of defined chemical ingredients across target-1..target-9
      with canonical mediaingredientmech_chebi_term.
    denominator: 9
    minimum: 0.0
    maximum: 100.0
- assessment_id: A2
  area: grounding
  topic: 'Cross-category record and solution remediation across CultureMech:000034,
    000252, 003150, 007843, 010554, 011215, 015445, and 015480 (Issues #635 and #645)'
  outcome: supported
  summary: All 8 curated media and solution records in Group 2 (target-10..target-17)
    have complete canonical ontology grounding on all defined chemical constituents,
    accurate medium_type/composition_type classifications, consistent units, deduplicated
    mineral salts, and zero stale data_quality_flags or placeholder ingredients.
  target_ids:
  - target-10
  - target-11
  - target-12
  - target-13
  - target-14
  - target-15
  - target-16
  - target-17
  evidence_ids:
  - E1
  - E2
  metrics:
  - name: curated_cohort_strict_validation_pass_rate
    value: 100.0
    unit: percent
    definition: Percentage of remediated Group 2 records passing validate_strict.py
      with zero errors.
    denominator: 8
    minimum: 0.0
    maximum: 100.0
findings:
- finding_id: F1
  issue_key: grounding.missing_mim_term.CultureMech_003150.r2a_broth_daigo
  category: grounding
  severity: minor
  status: resolved
  certainty: confirmed
  title: Commercial premix R2A broth (DAIGO) linked via culturemech_term and sub-ingredient
    breakdown documented in 1_10_r2a_broth.yaml
  description: Linked R2A broth (DAIGO) to CultureMech:003183 (R2A Broth) via culturemech_term
    and added an explicit 1/10 R2A constituent breakdown note in data/normalized_yaml/bacterial/1_10_r2a_broth.yaml.
  disposition_reason: 'Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-004)
    via write_validated_recipe.'
  previous_occurrences:
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T084036Z-review-yaml-record-1-10-r2a-broth
    finding_id: F1
  target_ids:
  - target-12
  evidence_ids:
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    role: maintained_record
- finding_id: F2
  issue_key: representation.batch_water_volume.CultureMech_003150
  category: representation
  severity: informational
  status: resolved
  certainty: confirmed
  title: Solvent Distilled water (1.0 L) removed from solute ingredient list in 1_10_r2a_broth.yaml
  description: Removed redundant Distilled water (1.0 L) solvent entry from ingredients[]
    in 1_10_r2a_broth.yaml (retaining the 1.0 L solvent volume in preparation_steps
    and notes) so all solute concentrations are normalized per liter.
  disposition_reason: 'Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-004)
    via write_validated_recipe.'
  previous_occurrences:
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T084036Z-review-yaml-record-1-10-r2a-broth
    finding_id: F2
  target_ids:
  - target-12
  evidence_ids:
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    role: maintained_record
- finding_id: F3
  issue_key: scope.misclassified_category.CultureMech_015445
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: 'UTEX algal SolutionRecipe DAS_Vitamin_Cocktail.yaml reclassified to category:
    algae with snake_case name'
  description: 'Updated DAS_Vitamin_Cocktail.yaml (CultureMech:015445) to category:
    algae and name: das_vitamin_cocktail.'
  disposition_reason: 'Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-007)
    via write_validated_recipe.'
  previous_occurrences:
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T084537Z-review-yaml-record-das-vitamin-cocktail
    finding_id: F1
  target_ids:
  - target-16
  evidence_ids:
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    role: maintained_record
- finding_id: F4
  issue_key: grounding.unmapped_root_solution_term.CultureMech_015445
  category: grounding
  severity: minor
  status: resolved
  certainty: confirmed
  title: All 6 composition items on DAS_Vitamin_Cocktail.yaml grounded to canonical
    ChEBI/MIM terms and root SolutionRecipe routing term documented
  description: Populated canonical ChEBI labels and mediaingredientmech_chebi_term
    across all 6/6 composition items in DAS_Vitamin_Cocktail.yaml (including calcium
    pantothenate CHEBI:31345) while retaining root term MediaIngredientMech:UNMAPPED_0045
    required by scripts/record_kinds.py:has_solution_shape() for SolutionRecipe schema
    routing.
  disposition_reason: 'Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-007)
    via write_validated_recipe.'
  previous_occurrences:
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T084537Z-review-yaml-record-das-vitamin-cocktail
    finding_id: F2
  target_ids:
  - target-16
  evidence_ids:
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    role: maintained_record
- finding_id: F5
  issue_key: provenance.sterilization_conflict.CultureMech_015445.vitamin_b12
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: UTEX Vitamin B12 table vs. Directions sterilization note reconciled in DAS_Vitamin_Cocktail.yaml
  description: Documented the UTEX source discrepancy between the ingredient table
    annotation '(add after autoclaving)' on Vitamin B12 (0.0008 g/100 mL = 0.008 G_PER_L)
    and the UTEX Directions protocol (filter-sterilize the entire solution through
    a 0.45 µm Millipore filter without heat sterilization) on composition[3] and top-level
    notes of DAS_Vitamin_Cocktail.yaml.
  disposition_reason: 'Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-007)
    via write_validated_recipe.'
  previous_occurrences:
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T084537Z-review-yaml-record-das-vitamin-cocktail
    finding_id: F3
  target_ids:
  - target-16
  evidence_ids:
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    role: maintained_record
- finding_id: F6
  issue_key: schema.undeclared_merge_slots.merge_recipes
  category: schema
  severity: major
  status: resolved
  certainty: confirmed
  title: LinkML schema root and merge metadata slots aligned in culturemech.yaml
  description: 'Set tree_root: true on MediaRecipe and declared SolutionRecipe merge/provenance
    slots in src/culturemech/schema/culturemech.yaml so both normalized and merged
    records validate cleanly.'
  disposition_reason: 'Resolved in Stage 5 under Issue #634 (CM-C1S4-001) and verified
    with scripts/validate_strict.py.'
  previous_occurrences:
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T085038Z-review-yaml-record-thermovenabulum-medium-merged
    finding_id: F1
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T090039Z-review-yaml-category-thermovenabulum-family
    finding_id: F3
  target_ids:
  - target-1
  - target-5
  - target-9
  evidence_ids:
  - E1
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/schema/culturemech.yaml
    role: schema_definition
- finding_id: F7
  issue_key: concentration.unscaled_stock_inlining.thermovenabulum_family
  category: quantity
  severity: major
  status: resolved
  certainty: confirmed
  title: Scaled 100x-1000x trace element and vitamin stocks and deduplicated CaCl2
    x 2 H2O across all Thermovenabulum / Thermincola records
  description: Applied 1:100 (10 mL/L) and 1:1000 (1 mL/L) dilution factors to flattened
    Wolin trace element and vitamin stock components across target-1..target-9 and
    consolidated duplicate CaCl2 x 2 H2O to 0.327409 G_PER_L in DSMZ 962/962a and
    0.0988142 G_PER_L in DSMZ 1255.
  disposition_reason: 'Resolved in Stage 5 under Issues #634 and #645 (CM-C1S4-002)
    via write_validated_recipe.'
  previous_occurrences:
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T085038Z-review-yaml-record-thermovenabulum-medium-merged
    finding_id: F2
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T090039Z-review-yaml-category-thermovenabulum-family
    finding_id: F2
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  - target-7
  - target-8
  - target-9
  evidence_ids:
  - E1
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/merge_yaml/merged/THERMOVENABULUM_MEDIUM.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml
    role: maintained_record
- finding_id: F8
  issue_key: grounding.missing_mim_term.CultureMech_002143
  category: grounding
  severity: minor
  status: resolved
  certainty: confirmed
  title: Populated missing mediaingredientmech_chebi_term across all defined chemical
    ingredients in Thermovenabulum family records
  description: Added canonical OBO ChEBI labels and mediaingredientmech_chebi_term
    mappings across all defined chemical ingredients (including resazurin, nitrilotriacetic
    acid, calcium pantothenate, and sodium selenite; 31/33 in DSMZ 962/962a and 30/32
    in DSMZ 1255; complex Meat extract and Yeast extract retain MediaIngredientMech
    IDs) across target-1..target-9.
  disposition_reason: 'Resolved in Stage 5 under Issues #634 and #645 (CM-C1S4-001/002)
    via write_validated_recipe.'
  previous_occurrences:
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T085038Z-review-yaml-record-thermovenabulum-medium-merged
    finding_id: F3
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  - target-7
  - target-8
  - target-9
  evidence_ids:
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/merge_yaml/merged/THERMOVENABULUM_MEDIUM.yaml
    role: maintained_record
- finding_id: F9
  issue_key: nomenclature.name_collision.thermovenabulum_family
  category: nomenclature
  severity: major
  status: resolved
  certainty: confirmed
  title: Disambiguated DSMZ 962a, DSMZ 1255, and DSMZ 962 names across the Thermovenabulum
    family
  description: 'Assigned distinct snake_case names: thermovenabulum_medium_dsmz_962a
    (DSMZ 962a), thermovenabulum_medium_dsmz_1255 (DSMZ 1255), and thermovenabulum_medium_dsmz_962
    (KOMODO 962), synchronized THERMINCOLA_FERRIACETICA_MEDIUM.yaml variant_children
    and scripts/repair_komodo_962_thermincola_score10.py, and updated data/culturemech_recipe_catalog.tsv.'
  disposition_reason: 'Resolved in Stage 5 under Issues #634 and #645 (CM-C1S4-001)
    via write_validated_recipe.'
  previous_occurrences:
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T090039Z-review-yaml-category-thermovenabulum-family
    finding_id: F1
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  - target-9
  evidence_ids:
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thermovenabulum_medium.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_962_THERMOVENABULUM_medium.yaml
    role: maintained_record
- finding_id: F10
  issue_key: representation.defined_misclassified_as_complex.CultureMech_007843
  category: representation
  severity: minor
  status: resolved
  certainty: confirmed
  title: Corrected medium_type and composition_type to DEFINED on TOGO_M1308_Methylotroph_Medium.yaml
  description: 'Updated TOGO_M1308_Methylotroph_Medium.yaml (CultureMech:007843) to
    medium_type: DEFINED and composition_type: DEFINED.'
  disposition_reason: 'Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-004/005)
    via write_validated_recipe.'
  previous_occurrences:
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T085538Z-review-ingredient-concentrations-togo-m1308
    finding_id: F1
  target_ids:
  - target-13
  evidence_ids:
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml
    role: maintained_record
- finding_id: F11
  issue_key: grounding.missing_mim_term.CultureMech_007843.hydrates_and_nested_solutions
  category: grounding
  severity: minor
  status: resolved
  certainty: confirmed
  title: Grounded CaCl2.2H2O, MgCl2.6H2O, and all 24 nested solution items in TOGO_M1308_Methylotroph_Medium.yaml
  description: Populated canonical ChEBI labels, mediaingredientmech_chebi_term, and
    JCM 1219 concentration evidence on all 6 main-table solutes (including CaCl2.2H2O
    0.07 G_PER_L and MgCl2.6H2O 0.2 G_PER_L) and all 24 nested solutions[].composition[]
    items in TOGO_M1308_Methylotroph_Medium.yaml.
  disposition_reason: 'Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-004/005)
    via write_validated_recipe.'
  previous_occurrences:
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T085538Z-review-ingredient-concentrations-togo-m1308
    finding_id: F2
  target_ids:
  - target-13
  evidence_ids:
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml
    role: maintained_record
- finding_id: F12
  issue_key: quantity.volume_denominator_offset.CultureMech_007843
  category: quantity
  severity: informational
  status: resolved
  certainty: confirmed
  title: Documented 994.81 mL pre-methanol / 999.81 mL post-methanol cumulative liquid
    addition denominator note in TOGO_M1308_Methylotroph_Medium.yaml
  description: Added explicit preparation note documenting the 990 mL water + 4.81
    mL stock solutions = 994.81 mL before methanol (999.81 mL including 5 mL filter-sterilized
    methanol) in TOGO_M1308_Methylotroph_Medium.yaml.
  disposition_reason: 'Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-004/005)
    via write_validated_recipe.'
  previous_occurrences:
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T085538Z-review-ingredient-concentrations-togo-m1308
    finding_id: F3
  target_ids:
  - target-13
  evidence_ids:
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml
    role: maintained_record
- finding_id: F13
  issue_key: tooling.solution_validator_blind_spots.batch_review_recipes
  category: quantity
  severity: major
  status: resolved
  certainty: confirmed
  title: Removed placeholder ingredients[] and normalized 0.96 L water and defined
    chemical ChEBI/MIM terms in mediadive_177_Main_sol_104a.yaml
  description: 'Removed obsolete placeholder ingredients[] and data_quality_flags:
    [incomplete_composition], converted Distilled water from 960 PERCENT_V_V to 0.96
    L, and populated canonical ChEBI/MIM grounding on all 6/9 defined chemical constituents
    in mediadive_177_Main_sol_104a.yaml (alongside PR #632 fix for Issue #633 in scripts/batch_review_recipes.py).'
  disposition_reason: 'Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-009)
    via write_validated_recipe.'
  previous_occurrences:
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T090539Z-review-recipes-and-categories-corpus-audit
    finding_id: F1
  target_ids:
  - target-15
  evidence_ids:
  - E1
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_177_Main_sol_104a.yaml
    role: maintained_record
- finding_id: F14
  issue_key: grounding.cross_category_mim_and_chebi_gaps.representatives
  category: grounding
  severity: minor
  status: resolved
  certainty: confirmed
  title: Completed canonical CHEBI/MIM grounding and removed stale flags across archaea,
    bacterial, fungal, and specialized representatives
  description: Normalized Distilled water to CHEBI:15377 ('water') across 11/13 defined
    chemical constituents in DSMZ_1399_HALOPHILIC_MEDIUM.yaml, mapped DL-Serine (CHEBI:17822,
    'DL-serine') and all 28/28 MIM terms in yeast_optimized_defined_medium_glucose.yaml,
    and populated 29/29 canonical ChEBI/MIM terms and removed stale has_unmapped_ingredients
    flag in 2x_uga_defined_nocarbon.yaml.
  disposition_reason: 'Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-006/008)
    via write_validated_recipe.'
  previous_occurrences:
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T090539Z-review-recipes-and-categories-corpus-audit
    finding_id: F2
  target_ids:
  - target-11
  - target-12
  - target-14
  - target-17
  evidence_ids:
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/DSMZ_1399_HALOPHILIC_MEDIUM.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/yeast_optimized_defined_medium_glucose.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/2x_uga_defined_nocarbon.yaml
    role: maintained_record
- finding_id: F15
  issue_key: representation.defined_misclassification_and_duplicate_salts.representatives
  category: representation
  severity: minor
  status: resolved
  certainty: confirmed
  title: Set DEFINED on Bold_Basal_Medium.yaml and deduplicated flattened Wolfe's
    mineral salts in 2x_uga_defined_nocarbon.yaml
  description: 'Updated Bold_Basal_Medium.yaml (CultureMech:000034) to medium_type:
    DEFINED / composition_type: DEFINED with canonical ChEBI labels and clarified
    the UTEX MnCl2.4H2O source note; normalized name to 2x_uga_defined_nocarbon and
    consolidated duplicate MgSO4.7H2O (0.9919 G_PER_L), CaCl2.2H2O (0.0314 G_PER_L),
    and NaCl (0.0399 G_PER_L) from 32 entries to 29 unique ingredients in 2x_uga_defined_nocarbon.yaml.'
  disposition_reason: 'Resolved in Stage 5 under Issues #635 and #645 (CM-C1S4-003/008)
    via write_validated_recipe.'
  previous_occurrences:
  - repository: CultureBotAI/CultureMech
    review_id: 20261017T090539Z-review-recipes-and-categories-corpus-audit
    finding_id: F3
  target_ids:
  - target-10
  - target-17
  evidence_ids:
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/Bold_Basal_Medium.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/2x_uga_defined_nocarbon.yaml
    role: maintained_record
actions: []
limitations: []
tags:
- review-recipes
- stage-05-remediation
- issue-634
- issue-635
- issue-645
```
