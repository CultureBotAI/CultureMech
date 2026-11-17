# Batch recipe quality and cross-category audit across all 6 CultureMech categories (15,910 records)

- Review: 20261017T090539Z-review-recipes-and-categories-corpus-audit
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-17T09:03:39Z
- Finished UTC: 2026-10-17T09:05:39Z
- Reviewer: antigravity-agent (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Executed full-corpus quality analysis via scripts/batch_review_recipes.py and scripts/assign_culturemech_ids.py --check across all 15,910 normalized records and performed deep per-record reviews on 6 stratified category representatives across algae, archaea, bacterial, fungal, solution, and specialized recipes. While all 15,910 records (100.0%) pass current P1/P2 checks and carry unique canonical CultureMech IDs, deep inspection uncovered both a validation blind spot in scripts/batch_review_recipes.py and concrete curation defects in all 6 category representatives: (1) scripts/batch_review_recipes.py's _validate_solution() never checks SolutionDescriptor records for P3.1 placeholder ingredients ('See source for composition') and ignores chebi_term when computing ontology coverage; (2) target-1 (Bold_Basal_Medium.yaml, CultureMech:000034) has 100% CHEBI and MediaIngredientMech coverage across all 7 top-level ingredients and 4 nested solutions (15 items), but misclassifies a completely defined mineral algal medium as medium_type: COMPLEX / composition_type: UNDEFINED and notes an unresolved UTEX source typo ('MnCl•4H2O') on solutions[3].composition[3]; (3) target-2 (DSMZ_1399_HALOPHILIC_MEDIUM.yaml, CultureMech:000252) maps Distilled water at ingredients[4] (0.333 L) and solutions[0].composition[8] (1 L) to mediadive.compound:4 instead of CHEBI:15377 and lacks MIM links on Proteose peptone no. 3 and Yeast extract (10/14 = 71.43% MIM coverage); (4) target-3 (1_10_r2a_broth.yaml, CultureMech:003150) has 1/2 (50.0%) MIM/CHEBI coverage because R2A broth (DAIGO) is linked only to CultureMech:003183; (5) target-4 (yeast_optimized_defined_medium_glucose.yaml, CultureMech:010554) has 27/28 (96.43%) CHEBI coverage (missing on ingredients[12] DL-Serine) and 15/28 (53.57%) mediaingredientmech_chebi_term coverage; (6) target-5 (mediadive_177_Main_sol_104a.yaml, CultureMech:011215) is a SolutionRecipe in data/normalized_yaml/bacterial/ that retains a stale placeholder ingredients[0] ('See source for composition', VARIABLE) alongside 9 composition[] items (6/9 with chebi_term, 0/9 with mediaingredientmech_chebi_term) and encodes 960 mL Distilled water as 960 PERCENT_V_V; and (7) target-6 (2x_uga_defined_nocarbon.yaml, CultureMech:015480) has 32/32 (100%) CHEBI coverage, 0/32 (0%) mediaingredientmech_chebi_term coverage, a stale data_quality_flags: [has_unmapped_ingredients], a non-snake_case name ('2x UGA defined nocarbon'), and duplicate top-level mineral salts (Magnesium sulfate heptahydrate, Calcium chloride dihydrate, Sodium Chloride) from flattening ATCC Wolfe's mineral mix.

## Scope And Provenance

Stratified batch review of 6 category representative records combined with full-corpus deterministic scan of all 15,910 recipes across algae (254), archaea (744), bacterial (9,546), fungal (126), solution (4,785), and specialized (455).

Selection: 1 representative YAML record per category plus full-corpus scan via scripts/batch_review_recipes.py.
Coverage: sampled; 6 reviewed / 15910 in the declared population.
Source: git_commit at Git base 4c69a62c25dd5419766533205c215b0aaa5d14f7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| target-1 | data/normalized_yaml/algae/Bold_Basal_Medium.yaml | maintained | CultureMech:000034 - Bold Basal Medium (algae) |
| target-2 | data/normalized_yaml/archaea/DSMZ_1399_HALOPHILIC_MEDIUM.yaml | maintained | CultureMech:000252 - HALOPHILIC MEDIUM (archaea) |
| target-3 | data/normalized_yaml/bacterial/1_10_r2a_broth.yaml | maintained | CultureMech:003150 - 1/10 R2A BROTH (bacterial) |
| target-4 | data/normalized_yaml/fungal/yeast_optimized_defined_medium_glucose.yaml | maintained | CultureMech:010554 - yeast_optimized_defined_medium_glucose (fungal) |
| target-5 | data/normalized_yaml/bacterial/mediadive_177_Main_sol_104a.yaml | maintained | CultureMech:011215 - Main sol. 104a (solution) |
| target-6 | data/normalized_yaml/specialized/2x_uga_defined_nocarbon.yaml | maintained | CultureMech:015480 - 2X UGA defined medium without carbon (specialized) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical CultureMech ID uniqueness and coverage check | passed | True | target-1, target-2, target-3, target-4, target-5, target-6 | Scanned 15,910 files: every record has one canonical, unique, unreused CultureMech ID (highest ID: CultureMech:015915). |
| Full-corpus batch_review_recipes.py P1-P4 scan | passed | True | target-1, target-2, target-3, target-4, target-5, target-6 | 15,910 / 15,910 recipes valid on P1/P2 (0 P1 errors, 0 P2 errors, 24,383 P3 issues, 19,148 P4 issues; 60.7% overall MediaIngredientMech coverage). |
| Strict schema and reference validation on all 6 category representatives | passed | True | target-1, target-2, target-3, target-4, target-5, target-6 | All 6 category representative records pass linkml-validate, validate_strict.py, validate_recipe_references.py, and linkml-term-validator. |

## Scientific And Domain Assessments

### Corpus-wide P1/P2 schema validity and SolutionDescriptor validator blind spots

schema: concern. Targets: target-1, target-2, target-3, target-4, target-5, target-6.

All 15,910 normalized records pass current P1/P2 checks, but scripts/batch_review_recipes.py's _validate_solution() fails to check SolutionDescriptor records for P3.1 placeholder ingredients/notes and ignores chebi_term when computing ontology coverage.

### Cross-category ontology grounding, unit integrity, and metadata consistency across the 6 representatives

grounding: concern. Targets: target-1, target-2, target-3, target-4, target-5, target-6.

Every sampled category representative exhibits actionable curation defects: COMPLEX/UNDEFINED misclassification on defined Bold Basal Medium (target-1), mediadive.compound:4 water CURIEs in DSMZ 1399 (target-2), unmapped R2A premix in target-3, unmapped DL-Serine and 15/28 MIM coverage in target-4, 960 PERCENT_V_V water and stale placeholder ingredients[] in target-5, and 0/32 MIM coverage, stale has_unmapped_ingredients flag, non-snake_case name, and duplicate flattened salts in target-6.

## Findings

### F1: SolutionRecipe mediadive_177_Main_sol_104a.yaml retains placeholder ingredients[], encodes 960 mL water as 960 PERCENT_V_V, and exposes _validate_solution() blind spots

major / open / confirmed; issue key: tooling.solution_validator_blind_spots.batch_review_recipes.

In target-5 (mediadive_177_Main_sol_104a.yaml, CultureMech:011215), an obsolete ingredients[0] ('See source for composition', VARIABLE) and data_quality_flags: [incomplete_composition] remain alongside 9 populated composition[] items (6/9 with chebi_term, 0/9 with mediaingredientmech_chebi_term), and composition[8] (Distilled water) is recorded as '960 PERCENT_V_V' instead of 960 mL (0.96 L). Furthermore, scripts/batch_review_recipes.py's _validate_solution() never checks SolutionDescriptor records for P3.1 placeholders ('See source for composition') and ignores chebi_term when computing ontology coverage.

### F2: Incomplete MediaIngredientMech/CHEBI grounding and stale flags across archaea, bacterial, fungal, and specialized representatives

minor / open / confirmed; issue key: grounding.cross_category_mim_and_chebi_gaps.representatives.

In target-2 (DSMZ_1399_HALOPHILIC_MEDIUM.yaml, CultureMech:000252), Distilled water at ingredients[4] (0.333 L) and solutions[0].composition[8] (1 L) is mapped to mediadive.compound:4 instead of CHEBI:15377 and lacks mediaingredientmech_chebi_term (along with Proteose peptone no. 3 and Yeast extract; 10/14 = 71.43% MIM coverage). In target-3 (1_10_r2a_broth.yaml, CultureMech:003150), R2A broth (DAIGO) lacks mediaingredientmech_chebi_term (1/2 = 50.0%). In target-4 (yeast_optimized_defined_medium_glucose.yaml, CultureMech:010554), 27/28 ingredients (96.43%) have CHEBI terms (missing on ingredients[12] DL-Serine, 1.028 MILLIMOLAR) and 15/28 (53.57%) have mediaingredientmech_chebi_term. In target-6 (2x_uga_defined_nocarbon.yaml, CultureMech:015480), 32/32 ingredients (100%) have CHEBI terms but 0/32 (0%) have mediaingredientmech_chebi_term, while data_quality_flags retains a stale has_unmapped_ingredients flag.

### F3: Bold Basal Medium misclassified as COMPLEX/UNDEFINED and duplicate flattened mineral salts in 2x_uga_defined_nocarbon.yaml

minor / open / confirmed; issue key: representation.defined_misclassification_and_duplicate_salts.representatives.

target-1 (Bold_Basal_Medium.yaml, CultureMech:000034) has 100% CHEBI and mediaingredientmech_chebi_term coverage across all 22 top-level and nested inorganic/EDTA components, but sets medium_type: COMPLEX and composition_type: UNDEFINED (and records an unresolved UTEX typo note 'Listed as MnCl•4H2O in source' on solutions[3].composition[3]). target-6 (2x_uga_defined_nocarbon.yaml, CultureMech:015480) uses a non-snake_case name ('2x UGA defined nocarbon') and contains duplicate top-level mineral entries for Magnesium sulfate heptahydrate (0.4 and 0.06 G_PER_L), Calcium chloride dihydrate (0.1 and 0.002 G_PER_L), and Sodium Chloride (0.8 and 0.02 G_PER_L) from flattening ATCC Wolfe's mineral solution.

## Recommended Actions And Acceptance Checks

### ACT1

Update scripts/batch_review_recipes.py's _validate_solution() to detect P3.1 placeholder ingredients/notes on SolutionDescriptor records and count chebi_term grounding alongside MediaIngredientMech links, with unit tests in tests/test_batch_review_recipes.py.

- _validate_solution() flags P3.1 placeholder entries on SolutionDescriptor records such as CultureMech:011215.
- _validate_solution() recognizes chebi_term grounding in composition[] items.
- pytest tests/test_batch_review_recipes.py passes.

### ACT2

Remediate the curated record defects across target-1..target-6: set DEFINED on Bold_Basal_Medium.yaml, normalize mediadive.compound:4 water terms to CHEBI:15377 in DSMZ_1399_HALOPHILIC_MEDIUM.yaml, map DL-Serine and backfill mediaingredientmech_chebi_term in yeast_optimized_defined_medium_glucose.yaml and 2x_uga_defined_nocarbon.yaml, fix 960 PERCENT_V_V water and remove stale placeholder ingredients[0] in mediadive_177_Main_sol_104a.yaml, and deduplicate flattened Wolfe's mineral salts in 2x_uga_defined_nocarbon.yaml.

- All 6 representative records pass strict schema, reference, and ontology validation without stale flags or placeholder ingredients.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | scripts/batch_review_recipes.py and scripts/assign_culturemech_ids.py --check output; corpus summary and scripts/batch_review_recipes.py:_validate_solution | supports | 15,910 recipes scanned: 100.0% valid on current P1/P2 checks, 122,099 / 201,090 ingredients linked to MediaIngredientMech (60.7%). Inspection of scripts/batch_review_recipes.py lines 199-243 shows _validate_solution() omits P3.1 placeholder checks and ignores chebi_term on SolutionDescriptor composition items. |
| E2 | Six stratified category representative YAML records (target-1..target-6); target-1..target-6 | supports | Direct on-disk inspection of Bold_Basal_Medium.yaml (CultureMech:000034: 22/22 CHEBI &amp; MIM, medium_type: COMPLEX), DSMZ_1399_HALOPHILIC_MEDIUM.yaml (CultureMech:000252: 10/14 MIM, Distilled water mapped to mediadive.compound:4), 1_10_r2a_broth.yaml (CultureMech:003150: 1/2 MIM &amp; CHEBI), yeast_optimized_defined_medium_glucose.yaml (CultureMech:010554: 27/28 CHEBI, 15/28 MIM, unmapped DL-Serine), mediadive_177_Main_sol_104a.yaml (CultureMech:011215: 6/9 chebi_term, 0/9 MIM, stale 'See source for composition' ingredient, Distilled water at 960 PERCENT_V_V), and 2x_uga_defined_nocarbon.yaml (CultureMech:015480: 32/32 CHEBI, 0/32 MIM, stale has_unmapped_ingredients flag, non-snake_case name, and duplicate MgSO4·7H2O / CaCl2·2H2O / NaCl entries). |

## Limits And Additional Notes

- Full deterministic P1-P4 batch scan covered all 15,910 normalized records; deep manual inspection in this batch bundle sampled 6 stratified category representatives (1 per category).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T090539Z-review-recipes-and-categories-corpus-audit
kind: batch
repository: CultureBotAI/CultureMech
title: Batch recipe quality and cross-category audit across all 6 CultureMech categories
  (15,910 records)
started_at: '2026-10-17T09:03:39Z'
finished_at: '2026-10-17T09:05:39Z'
reviewer:
  identity: antigravity-agent
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Independent agent review against primary literature/database
    sources and deterministic LinkML validators without modifying target records.
skill: review-recipes
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Executed full-corpus quality analysis via scripts/batch_review_recipes.py
  and scripts/assign_culturemech_ids.py --check across all 15,910 normalized records
  and performed deep per-record reviews on 6 stratified category representatives across
  algae, archaea, bacterial, fungal, solution, and specialized recipes. While all
  15,910 records (100.0%) pass current P1/P2 checks and carry unique canonical CultureMech
  IDs, deep inspection uncovered both a validation blind spot in scripts/batch_review_recipes.py
  and concrete curation defects in all 6 category representatives: (1) scripts/batch_review_recipes.py''s
  _validate_solution() never checks SolutionDescriptor records for P3.1 placeholder
  ingredients (''See source for composition'') and ignores chebi_term when computing
  ontology coverage; (2) target-1 (Bold_Basal_Medium.yaml, CultureMech:000034) has
  100% CHEBI and MediaIngredientMech coverage across all 7 top-level ingredients and
  4 nested solutions (15 items), but misclassifies a completely defined mineral algal
  medium as medium_type: COMPLEX / composition_type: UNDEFINED and notes an unresolved
  UTEX source typo (''MnCl•4H2O'') on solutions[3].composition[3]; (3) target-2 (DSMZ_1399_HALOPHILIC_MEDIUM.yaml,
  CultureMech:000252) maps Distilled water at ingredients[4] (0.333 L) and solutions[0].composition[8]
  (1 L) to mediadive.compound:4 instead of CHEBI:15377 and lacks MIM links on Proteose
  peptone no. 3 and Yeast extract (10/14 = 71.43% MIM coverage); (4) target-3 (1_10_r2a_broth.yaml,
  CultureMech:003150) has 1/2 (50.0%) MIM/CHEBI coverage because R2A broth (DAIGO)
  is linked only to CultureMech:003183; (5) target-4 (yeast_optimized_defined_medium_glucose.yaml,
  CultureMech:010554) has 27/28 (96.43%) CHEBI coverage (missing on ingredients[12]
  DL-Serine) and 15/28 (53.57%) mediaingredientmech_chebi_term coverage; (6) target-5
  (mediadive_177_Main_sol_104a.yaml, CultureMech:011215) is a SolutionRecipe in data/normalized_yaml/bacterial/
  that retains a stale placeholder ingredients[0] (''See source for composition'',
  VARIABLE) alongside 9 composition[] items (6/9 with chebi_term, 0/9 with mediaingredientmech_chebi_term)
  and encodes 960 mL Distilled water as 960 PERCENT_V_V; and (7) target-6 (2x_uga_defined_nocarbon.yaml,
  CultureMech:015480) has 32/32 (100%) CHEBI coverage, 0/32 (0%) mediaingredientmech_chebi_term
  coverage, a stale data_quality_flags: [has_unmapped_ingredients], a non-snake_case
  name (''2x UGA defined nocarbon''), and duplicate top-level mineral salts (Magnesium
  sulfate heptahydrate, Calcium chloride dihydrate, Sodium Chloride) from flattening
  ATCC Wolfe''s mineral mix.'
source:
  git_revision: 4c69a62c25dd5419766533205c215b0aaa5d14f7
  state: git_commit
  inputs:
  - path: data/normalized_yaml/algae/Bold_Basal_Medium.yaml
    sha256: 073dd99ce0c96a8bad3716df581bfeabed16a83e98a967e1f0305ada5504af53
    role: target
  - path: data/normalized_yaml/archaea/DSMZ_1399_HALOPHILIC_MEDIUM.yaml
    sha256: 90d9cb52a972d7e7bbac78adfcb2500bdebeabf25c196faebac76b78e27e2bca
    role: target
  - path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    sha256: 199ec4c42f3e624cad33b581c95fd5ffef8deda69f66b19443684b543a6c2c1b
    role: target
  - path: data/normalized_yaml/bacterial/mediadive_177_Main_sol_104a.yaml
    sha256: 32ce5195c24b77876dcb3ef5074e03a0aaa83bba97dabe70981416f4c73616bf
    role: target
  - path: data/normalized_yaml/fungal/yeast_optimized_defined_medium_glucose.yaml
    sha256: f568b0e5236ea8be314cc0e572662b8b01711913bf94b4d7c3b7256979be5f7a
    role: target
  - path: data/normalized_yaml/specialized/2x_uga_defined_nocarbon.yaml
    sha256: 9b63eb14efa4b45717f4b2df419d7f6aa9ec88c6adeda52a04e5a3aaf13f9396
    role: target
  - path: scripts/assign_culturemech_ids.py
    sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
    role: context
  - path: scripts/batch_review_recipes.py
    sha256: 65b3fdd0610e454244a8411c26a6b60c83d0a45b4b7905d63bb3da38867dbae8
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: Stratified batch review of 6 category representative records combined
    with full-corpus deterministic scan of all 15,910 recipes across algae (254),
    archaea (744), bacterial (9,546), fungal (126), solution (4,785), and specialized
    (455).
  selection: 1 representative YAML record per category plus full-corpus scan via scripts/batch_review_recipes.py.
  coverage: sampled
  population_size: 15910
  reviewed_target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  sampling_method: Stratified deterministic selection of one representative record
    per CultureMech category (algae, archaea, bacterial, fungal, solution, specialized)
    paired with complete 15,910-record execution of scripts/batch_review_recipes.py
    and scripts/assign_culturemech_ids.py --check.
targets:
- target_id: target-1
  path: data/normalized_yaml/algae/Bold_Basal_Medium.yaml
  label: CultureMech:000034 - Bold Basal Medium (algae)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/Bold_Basal_Medium.yaml
    role: maintained_record
- target_id: target-2
  path: data/normalized_yaml/archaea/DSMZ_1399_HALOPHILIC_MEDIUM.yaml
  label: CultureMech:000252 - HALOPHILIC MEDIUM (archaea)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/DSMZ_1399_HALOPHILIC_MEDIUM.yaml
    role: maintained_record
- target_id: target-3
  path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
  label: CultureMech:003150 - 1/10 R2A BROTH (bacterial)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    role: maintained_record
- target_id: target-4
  path: data/normalized_yaml/fungal/yeast_optimized_defined_medium_glucose.yaml
  label: CultureMech:010554 - yeast_optimized_defined_medium_glucose (fungal)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/yeast_optimized_defined_medium_glucose.yaml
    role: maintained_record
- target_id: target-5
  path: data/normalized_yaml/bacterial/mediadive_177_Main_sol_104a.yaml
  label: CultureMech:011215 - Main sol. 104a (solution)
  record_class: SolutionRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_177_Main_sol_104a.yaml
    role: maintained_record
- target_id: target-6
  path: data/normalized_yaml/specialized/2x_uga_defined_nocarbon.yaml
  label: CultureMech:015480 - 2X UGA defined medium without carbon (specialized)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/2x_uga_defined_nocarbon.yaml
    role: maintained_record
checks:
- check_id: chk-assign-culturemech-ids
  name: Canonical CultureMech ID uniqueness and coverage check
  status: passed
  required: true
  summary: 'Scanned 15,910 files: every record has one canonical, unique, unreused
    CultureMech ID (highest ID: CultureMech:015915).'
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  command: python scripts/assign_culturemech_ids.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - E1
- check_id: chk-batch-review-corpus
  name: Full-corpus batch_review_recipes.py P1-P4 scan
  status: passed
  required: true
  summary: 15,910 / 15,910 recipes valid on P1/P2 (0 P1 errors, 0 P2 errors, 24,383
    P3 issues, 19,148 P4 issues; 60.7% overall MediaIngredientMech coverage).
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  command: python scripts/batch_review_recipes.py --format markdown
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - E1
- check_id: chk-strict-representatives
  name: Strict schema and reference validation on all 6 category representatives
  status: passed
  required: true
  summary: All 6 category representative records pass linkml-validate, validate_strict.py,
    validate_recipe_references.py, and linkml-term-validator.
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  command: python scripts/validate_strict.py data/normalized_yaml/algae/Bold_Basal_Medium.yaml
    data/normalized_yaml/archaea/DSMZ_1399_HALOPHILIC_MEDIUM.yaml data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    data/normalized_yaml/fungal/yeast_optimized_defined_medium_glucose.yaml data/normalized_yaml/bacterial/mediadive_177_Main_sol_104a.yaml
    data/normalized_yaml/specialized/2x_uga_defined_nocarbon.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - E2
evidence:
- evidence_id: E1
  kind: validation
  reference: scripts/batch_review_recipes.py and scripts/assign_culturemech_ids.py
    --check output
  locator: corpus summary and scripts/batch_review_recipes.py:_validate_solution
  accessed_at: '2026-10-17T09:04:39Z'
  support: supports
  summary: '15,910 recipes scanned: 100.0% valid on current P1/P2 checks, 122,099
    / 201,090 ingredients linked to MediaIngredientMech (60.7%). Inspection of scripts/batch_review_recipes.py
    lines 199-243 shows _validate_solution() omits P3.1 placeholder checks and ignores
    chebi_term on SolutionDescriptor composition items.'
- evidence_id: E2
  kind: record_content
  reference: Six stratified category representative YAML records (target-1..target-6)
  locator: target-1..target-6
  accessed_at: '2026-10-17T09:04:39Z'
  support: supports
  summary: 'Direct on-disk inspection of Bold_Basal_Medium.yaml (CultureMech:000034:
    22/22 CHEBI & MIM, medium_type: COMPLEX), DSMZ_1399_HALOPHILIC_MEDIUM.yaml (CultureMech:000252:
    10/14 MIM, Distilled water mapped to mediadive.compound:4), 1_10_r2a_broth.yaml
    (CultureMech:003150: 1/2 MIM & CHEBI), yeast_optimized_defined_medium_glucose.yaml
    (CultureMech:010554: 27/28 CHEBI, 15/28 MIM, unmapped DL-Serine), mediadive_177_Main_sol_104a.yaml
    (CultureMech:011215: 6/9 chebi_term, 0/9 MIM, stale ''See source for composition''
    ingredient, Distilled water at 960 PERCENT_V_V), and 2x_uga_defined_nocarbon.yaml
    (CultureMech:015480: 32/32 CHEBI, 0/32 MIM, stale has_unmapped_ingredients flag,
    non-snake_case name, and duplicate MgSO4·7H2O / CaCl2·2H2O / NaCl entries).'
assessments:
- assessment_id: A1
  area: schema
  topic: Corpus-wide P1/P2 schema validity and SolutionDescriptor validator blind
    spots
  outcome: concern
  summary: All 15,910 normalized records pass current P1/P2 checks, but scripts/batch_review_recipes.py's
    _validate_solution() fails to check SolutionDescriptor records for P3.1 placeholder
    ingredients/notes and ignores chebi_term when computing ontology coverage.
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  evidence_ids:
  - E1
  - E2
  metrics:
  - name: corpus_p1_p2_valid_rate
    value: 100.0
    unit: percent
    definition: Percentage of normalized recipes with zero P1 or P2 errors (15910/15910).
    denominator: 15910
    minimum: 0.0
    maximum: 100.0
  - name: corpus_mediaingredientmech_coverage
    value: 60.72
    unit: percent
    definition: Percentage of ingredient instances across the 15,910 recipes with
      a populated MediaIngredientMech link (122099/201090).
    denominator: 201090
    minimum: 0.0
    maximum: 100.0
- assessment_id: A2
  area: grounding
  topic: Cross-category ontology grounding, unit integrity, and metadata consistency
    across the 6 representatives
  outcome: concern
  summary: 'Every sampled category representative exhibits actionable curation defects:
    COMPLEX/UNDEFINED misclassification on defined Bold Basal Medium (target-1), mediadive.compound:4
    water CURIEs in DSMZ 1399 (target-2), unmapped R2A premix in target-3, unmapped
    DL-Serine and 15/28 MIM coverage in target-4, 960 PERCENT_V_V water and stale
    placeholder ingredients[] in target-5, and 0/32 MIM coverage, stale has_unmapped_ingredients
    flag, non-snake_case name, and duplicate flattened salts in target-6.'
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  evidence_ids:
  - E1
  - E2
findings:
- finding_id: F1
  issue_key: tooling.solution_validator_blind_spots.batch_review_recipes
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: SolutionRecipe mediadive_177_Main_sol_104a.yaml retains placeholder ingredients[],
    encodes 960 mL water as 960 PERCENT_V_V, and exposes _validate_solution() blind
    spots
  description: 'In target-5 (mediadive_177_Main_sol_104a.yaml, CultureMech:011215),
    an obsolete ingredients[0] (''See source for composition'', VARIABLE) and data_quality_flags:
    [incomplete_composition] remain alongside 9 populated composition[] items (6/9
    with chebi_term, 0/9 with mediaingredientmech_chebi_term), and composition[8]
    (Distilled water) is recorded as ''960 PERCENT_V_V'' instead of 960 mL (0.96 L).
    Furthermore, scripts/batch_review_recipes.py''s _validate_solution() never checks
    SolutionDescriptor records for P3.1 placeholders (''See source for composition'')
    and ignores chebi_term when computing ontology coverage.'
  target_ids:
  - target-5
  field_paths:
  - ingredients[0].preferred_term
  - composition[8].concentration
  - data_quality_flags
  evidence_ids:
  - E1
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: scripts/batch_review_recipes.py
    role: validation_script
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_177_Main_sol_104a.yaml
    role: maintained_record
- finding_id: F2
  issue_key: grounding.cross_category_mim_and_chebi_gaps.representatives
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Incomplete MediaIngredientMech/CHEBI grounding and stale flags across archaea,
    bacterial, fungal, and specialized representatives
  description: In target-2 (DSMZ_1399_HALOPHILIC_MEDIUM.yaml, CultureMech:000252),
    Distilled water at ingredients[4] (0.333 L) and solutions[0].composition[8] (1
    L) is mapped to mediadive.compound:4 instead of CHEBI:15377 and lacks mediaingredientmech_chebi_term
    (along with Proteose peptone no. 3 and Yeast extract; 10/14 = 71.43% MIM coverage).
    In target-3 (1_10_r2a_broth.yaml, CultureMech:003150), R2A broth (DAIGO) lacks
    mediaingredientmech_chebi_term (1/2 = 50.0%). In target-4 (yeast_optimized_defined_medium_glucose.yaml,
    CultureMech:010554), 27/28 ingredients (96.43%) have CHEBI terms (missing on ingredients[12]
    DL-Serine, 1.028 MILLIMOLAR) and 15/28 (53.57%) have mediaingredientmech_chebi_term.
    In target-6 (2x_uga_defined_nocarbon.yaml, CultureMech:015480), 32/32 ingredients
    (100%) have CHEBI terms but 0/32 (0%) have mediaingredientmech_chebi_term, while
    data_quality_flags retains a stale has_unmapped_ingredients flag.
  target_ids:
  - target-2
  - target-3
  - target-4
  - target-6
  field_paths:
  - ingredients
  - solutions
  - data_quality_flags
  evidence_ids:
  - E1
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/DSMZ_1399_HALOPHILIC_MEDIUM.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/yeast_optimized_defined_medium_glucose.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/2x_uga_defined_nocarbon.yaml
    role: maintained_record
- finding_id: F3
  issue_key: representation.defined_misclassification_and_duplicate_salts.representatives
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Bold Basal Medium misclassified as COMPLEX/UNDEFINED and duplicate flattened
    mineral salts in 2x_uga_defined_nocarbon.yaml
  description: 'target-1 (Bold_Basal_Medium.yaml, CultureMech:000034) has 100% CHEBI
    and mediaingredientmech_chebi_term coverage across all 22 top-level and nested
    inorganic/EDTA components, but sets medium_type: COMPLEX and composition_type:
    UNDEFINED (and records an unresolved UTEX typo note ''Listed as MnCl•4H2O in source''
    on solutions[3].composition[3]). target-6 (2x_uga_defined_nocarbon.yaml, CultureMech:015480)
    uses a non-snake_case name (''2x UGA defined nocarbon'') and contains duplicate
    top-level mineral entries for Magnesium sulfate heptahydrate (0.4 and 0.06 G_PER_L),
    Calcium chloride dihydrate (0.1 and 0.002 G_PER_L), and Sodium Chloride (0.8 and
    0.02 G_PER_L) from flattening ATCC Wolfe''s mineral solution.'
  target_ids:
  - target-1
  - target-6
  field_paths:
  - medium_type
  - composition_type
  - name
  - ingredients
  evidence_ids:
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/Bold_Basal_Medium.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/2x_uga_defined_nocarbon.yaml
    role: maintained_record
actions:
- action_id: ACT1
  description: Update scripts/batch_review_recipes.py's _validate_solution() to detect
    P3.1 placeholder ingredients/notes on SolutionDescriptor records and count chebi_term
    grounding alongside MediaIngredientMech links, with unit tests in tests/test_batch_review_recipes.py.
  finding_ids:
  - F1
  target_ids:
  - target-5
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: scripts/batch_review_recipes.py
    role: validation_script
  acceptance_checks:
  - _validate_solution() flags P3.1 placeholder entries on SolutionDescriptor records
    such as CultureMech:011215.
  - _validate_solution() recognizes chebi_term grounding in composition[] items.
  - pytest tests/test_batch_review_recipes.py passes.
- action_id: ACT2
  description: 'Remediate the curated record defects across target-1..target-6: set
    DEFINED on Bold_Basal_Medium.yaml, normalize mediadive.compound:4 water terms
    to CHEBI:15377 in DSMZ_1399_HALOPHILIC_MEDIUM.yaml, map DL-Serine and backfill
    mediaingredientmech_chebi_term in yeast_optimized_defined_medium_glucose.yaml
    and 2x_uga_defined_nocarbon.yaml, fix 960 PERCENT_V_V water and remove stale placeholder
    ingredients[0] in mediadive_177_Main_sol_104a.yaml, and deduplicate flattened
    Wolfe''s mineral salts in 2x_uga_defined_nocarbon.yaml.'
  finding_ids:
  - F1
  - F2
  - F3
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/Bold_Basal_Medium.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/DSMZ_1399_HALOPHILIC_MEDIUM.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_177_Main_sol_104a.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/yeast_optimized_defined_medium_glucose.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/2x_uga_defined_nocarbon.yaml
    role: maintained_record
  acceptance_checks:
  - All 6 representative records pass strict schema, reference, and ontology validation
    without stale flags or placeholder ingredients.
limitations:
- Full deterministic P1-P4 batch scan covered all 15,910 normalized records; deep
  manual inspection in this batch bundle sampled 6 stratified category representatives
  (1 per category).
tags:
- review-recipes
- review-yaml-category
- batch-review
- corpus-audit
```
