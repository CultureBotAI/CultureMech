# Record and concentration audit of DAS Vitamin Cocktail (CultureMech:015445)

- Review: 20261017T084537Z-review-yaml-record-das-vitamin-cocktail
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-17T08:43:37Z
- Finished UTC: 2026-10-17T08:45:37Z
- Reviewer: antigravity-agent (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Normalized SolutionRecipe DAS_Vitamin_Cocktail.yaml (CultureMech:015445) passes all four deterministic validators with 100% CHEBI and MediaIngredientMech coverage across all 6 composition[] items and accurate 10x conversion from the 100 mL UTEX stock recipe (https://utex.org/products/das-vitamin-cocktail) to G_PER_L (Tricine (pH 8) 9.0 G_PER_L, Thiamine hydrochloride 0.67 G_PER_L, Biotin 0.01 G_PER_L, Vitamin B12 (Cobalamin) 0.008 G_PER_L, Calcium D-(+)-pantothenate 0.02 G_PER_L, and 4-aminobenzoic acid 0.04 G_PER_L). However, three curation issues require resolution: (1) this UTEX algal vitamin stock ('Vitamin Stock Solution for Dasycladales Seawater Medium') is typed as a SolutionRecipe yet stored under data/normalized_yaml/bacterial/ with category: bacterial and a non-snake_case name ('DAS Vitamin Cocktail'); (2) the root solution term.id retains a placeholder identifier (MediaIngredientMech:UNMAPPED_0045); and (3) composition[3].notes (Vitamin B12) documents an unresolved conflict in the UTEX source between the table note ('add after autoclaving') and general directions ('Sterilize via 0.45 µm Millipore filter').

## Scope And Provenance

Single-record structural, ontology, provenance, and concentration audit of SolutionRecipe CultureMech:015445 (DAS Vitamin Cocktail).

Selection: Target SolutionRecipe selected for review-yaml-record and review-ingredient-concentrations.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 4c69a62c25dd5419766533205c215b0aaa5d14f7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| target-1 | data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml | maintained | CultureMech:015445 - DAS Vitamin Cocktail |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML SolutionRecipe schema validation | passed | True | target-1 | linkml-validate (-C SolutionRecipe) passed with 0 errors on DAS_Vitamin_Cocktail.yaml. |
| Strict schema, recipe reference, and ontology term validation | passed | True | target-1 | validate_strict.py, validate_recipe_references.py, and linkml-term-validator (-t SolutionRecipe) passed with 0 errors. |

## Scientific And Domain Assessments

### Component ontology grounding and 10x concentration scaling from 100 mL UTEX stock to G_PER_L

quantity: supported. Targets: target-1.

All 6 composition[] items have verified CHEBI and mediaingredientmech_chebi_term identifiers (100% coverage) and accurately scale the UTEX g/100 mL stock weights by 10x to G_PER_L (9.0, 0.67, 0.01, 0.008, 0.02, and 0.04 G_PER_L).

### Category assignment, root solution term placeholder, and UTEX sterilization conflict

scope: concern. Targets: target-1.

The UTEX algal stock solution is placed under category: bacterial in data/normalized_yaml/bacterial/, retains root term.id MediaIngredientMech:UNMAPPED_0045, and documents an unresolved primary-source sterilization contradiction on Vitamin B12.

## Findings

### F1: UTEX algal SolutionRecipe is misclassified under category: bacterial with a non-snake_case name

major / open / confirmed; issue key: scope.misclassified_category.CultureMech_015445.

DAS_Vitamin_Cocktail.yaml is a SolutionRecipe for UTEX Dasycladales Seawater Medium (green algae, https://utex.org/products/das-vitamin-cocktail), but is stored in data/normalized_yaml/bacterial/ with category: bacterial and non-snake_case name: 'DAS Vitamin Cocktail'.

### F2: Root solution term.id retains placeholder MediaIngredientMech:UNMAPPED_0045

minor / open / confirmed; issue key: grounding.unmapped_root_solution_term.CultureMech_015445.

Although all 6 items in composition[] carry verified CHEBI and mediaingredientmech_chebi_term identifiers, top-level term.id is still set to the placeholder MediaIngredientMech:UNMAPPED_0045.

### F3: Unresolved UTEX sterilization contradiction on composition[3] (Vitamin B12)

minor / open / confirmed; issue key: provenance.sterilization_conflict.CultureMech_015445.vitamin_b12.

composition[3].notes (Vitamin B12 (Cobalamin), 0.008 G_PER_L) documents that the UTEX component table states 'add after autoclaving' whereas the UTEX general directions specify sterilizing the cocktail via a 0.45 µm Millipore filter.

## Recommended Actions And Acceptance Checks

### ACT1

Reclassify DAS_Vitamin_Cocktail.yaml from category: bacterial to algae (or solution), normalize name to snake_case ('das_vitamin_cocktail'), replace root term.id MediaIngredientMech:UNMAPPED_0045 with a permanent identifier, and record filter sterilization (0.45 µm) as authoritative over the table note.

- category and directory placement reflect UTEX algal solution provenance and name is snake_case.
- Root term.id no longer uses an UNMAPPED_* placeholder.
- linkml-validate -C SolutionRecipe and scripts/validate_strict.py pass with 0 errors.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml; lines 1-344 | supports | Normalized SolutionRecipe YAML for CultureMech:015445 with category: bacterial, root term MediaIngredientMech:UNMAPPED_0045, and 6 composition[] items scaled 10x from g/100 mL to G_PER_L. |
| E2 | Four-validator suite execution on DAS_Vitamin_Cocktail.yaml; stdout | supports | All four validators passed with zero structural or ontology label errors. |
| E3 | https://utex.org/products/das-vitamin-cocktail; UTEX Culture Collection of Algae DAS Vitamin Cocktail recipe | supports | UTEX specifies preparing 100 mL of DAS Vitamin Cocktail for Dasycladales Seawater Medium with 0.9 g Tricine (pH 8), 0.067 g Thiamine HCl (Sigma T1270), 0.001 g Biotin (Sigma B4639), 0.0008 g Cyanocobalamin (Sigma V6629, table note 'add after autoclaving'), 0.002 g Calcium pantothenate (Sigma P2250), and 0.004 g p-Aminobenzoic acid (Sigma A1174), with general directions to sterilize via 0.45 µm Millipore filter. |

## Limits And Additional Notes

- Review is a non-mutating observation; target YAML file was not modified.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T084537Z-review-yaml-record-das-vitamin-cocktail
kind: record
repository: CultureBotAI/CultureMech
title: Record and concentration audit of DAS Vitamin Cocktail (CultureMech:015445)
started_at: '2026-10-17T08:43:37Z'
finished_at: '2026-10-17T08:45:37Z'
reviewer:
  identity: antigravity-agent
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Independent agent review against primary literature/database
    sources and deterministic LinkML validators without modifying target records.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Normalized SolutionRecipe DAS_Vitamin_Cocktail.yaml (CultureMech:015445)
  passes all four deterministic validators with 100% CHEBI and MediaIngredientMech
  coverage across all 6 composition[] items and accurate 10x conversion from the 100
  mL UTEX stock recipe (https://utex.org/products/das-vitamin-cocktail) to G_PER_L
  (Tricine (pH 8) 9.0 G_PER_L, Thiamine hydrochloride 0.67 G_PER_L, Biotin 0.01 G_PER_L,
  Vitamin B12 (Cobalamin) 0.008 G_PER_L, Calcium D-(+)-pantothenate 0.02 G_PER_L,
  and 4-aminobenzoic acid 0.04 G_PER_L). However, three curation issues require resolution:
  (1) this UTEX algal vitamin stock (''Vitamin Stock Solution for Dasycladales Seawater
  Medium'') is typed as a SolutionRecipe yet stored under data/normalized_yaml/bacterial/
  with category: bacterial and a non-snake_case name (''DAS Vitamin Cocktail''); (2)
  the root solution term.id retains a placeholder identifier (MediaIngredientMech:UNMAPPED_0045);
  and (3) composition[3].notes (Vitamin B12) documents an unresolved conflict in the
  UTEX source between the table note (''add after autoclaving'') and general directions
  (''Sterilize via 0.45 µm Millipore filter'').'
source:
  git_revision: 4c69a62c25dd5419766533205c215b0aaa5d14f7
  state: git_commit
  inputs:
  - path: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    sha256: d143385b1f41d48d17049fd88e9389975dedd8349fdaad2d5b3c27cb795a67be
    role: target
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: Single-record structural, ontology, provenance, and concentration audit
    of SolutionRecipe CultureMech:015445 (DAS Vitamin Cocktail).
  selection: Target SolutionRecipe selected for review-yaml-record and review-ingredient-concentrations.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - target-1
targets:
- target_id: target-1
  path: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
  label: CultureMech:015445 - DAS Vitamin Cocktail
  record_class: SolutionRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    role: maintained_record
checks:
- check_id: chk-linkml-schema-solution
  name: LinkML SolutionRecipe schema validation
  status: passed
  required: true
  summary: linkml-validate (-C SolutionRecipe) passed with 0 errors on DAS_Vitamin_Cocktail.yaml.
  target_ids:
  - target-1
  command: linkml-validate -s src/culturemech/schema/culturemech.yaml -C SolutionRecipe
    data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - E2
- check_id: chk-strict-references-terms
  name: Strict schema, recipe reference, and ontology term validation
  status: passed
  required: true
  summary: validate_strict.py, validate_recipe_references.py, and linkml-term-validator
    (-t SolutionRecipe) passed with 0 errors.
  target_ids:
  - target-1
  command: python scripts/validate_strict.py data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    && python scripts/validate_recipe_references.py --file data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    && linkml-term-validator validate-data data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    -s src/culturemech/schema/culturemech.yaml -t SolutionRecipe --labels
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - E2
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
  locator: lines 1-344
  accessed_at: '2026-10-17T08:44:37Z'
  support: supports
  summary: 'Normalized SolutionRecipe YAML for CultureMech:015445 with category: bacterial,
    root term MediaIngredientMech:UNMAPPED_0045, and 6 composition[] items scaled
    10x from g/100 mL to G_PER_L.'
  quote: 'id: CultureMech:015445 / name: DAS Vitamin Cocktail / category: bacterial
    / term.id: MediaIngredientMech:UNMAPPED_0045 / Tricine (pH 8) 9.0 G_PER_L / Thiamine
    hydrochloride 0.67 G_PER_L / Biotin 0.01 G_PER_L / Vitamin B12 (Cobalamin) 0.008
    G_PER_L / Calcium D-(+)-pantothenate 0.02 G_PER_L / 4-aminobenzoic acid 0.04 G_PER_L'
  snapshot_sha256: d143385b1f41d48d17049fd88e9389975dedd8349fdaad2d5b3c27cb795a67be
- evidence_id: E2
  kind: validation
  reference: Four-validator suite execution on DAS_Vitamin_Cocktail.yaml
  locator: stdout
  accessed_at: '2026-10-17T08:44:37Z'
  support: supports
  summary: All four validators passed with zero structural or ontology label errors.
  quote: 'No issues found / VALID: 1 files passed all checks / VALID: All recipe references
    resolved / Validation passed'
- evidence_id: E3
  kind: primary_source
  reference: https://utex.org/products/das-vitamin-cocktail
  locator: UTEX Culture Collection of Algae DAS Vitamin Cocktail recipe
  accessed_at: '2026-10-17T08:44:37Z'
  support: supports
  summary: UTEX specifies preparing 100 mL of DAS Vitamin Cocktail for Dasycladales
    Seawater Medium with 0.9 g Tricine (pH 8), 0.067 g Thiamine HCl (Sigma T1270),
    0.001 g Biotin (Sigma B4639), 0.0008 g Cyanocobalamin (Sigma V6629, table note
    'add after autoclaving'), 0.002 g Calcium pantothenate (Sigma P2250), and 0.004
    g p-Aminobenzoic acid (Sigma A1174), with general directions to sterilize via
    0.45 µm Millipore filter.
  quote: Tricine (pH 8) 0.9 g/100 mL; Thiamine HCl 0.067 g/100 mL; Biotin 0.001 g/100
    mL; Vitamin B12 0.0008 g/100 mL (add after autoclaving); Calcium pantothenate
    0.002 g/100 mL; p-Aminobenzoic acid 0.004 g/100 mL. Sterilize via 0.45 µm Millipore
    filter.
assessments:
- assessment_id: A1
  area: quantity
  topic: Component ontology grounding and 10x concentration scaling from 100 mL UTEX
    stock to G_PER_L
  outcome: supported
  summary: All 6 composition[] items have verified CHEBI and mediaingredientmech_chebi_term
    identifiers (100% coverage) and accurately scale the UTEX g/100 mL stock weights
    by 10x to G_PER_L (9.0, 0.67, 0.01, 0.008, 0.02, and 0.04 G_PER_L).
  target_ids:
  - target-1
  evidence_ids:
  - E1
  - E2
  - E3
  metrics:
  - name: mediaingredientmech_coverage
    value: 100.0
    unit: percent
    definition: Percentage of composition items with a populated mediaingredientmech_chebi_term.id
      (6/6).
    denominator: 6
    minimum: 0.0
    maximum: 100.0
  - name: chebi_coverage
    value: 100.0
    unit: percent
    definition: Percentage of composition items with a populated CHEBI term.id (6/6).
    denominator: 6
    minimum: 0.0
    maximum: 100.0
- assessment_id: A2
  area: scope
  topic: Category assignment, root solution term placeholder, and UTEX sterilization
    conflict
  outcome: concern
  summary: 'The UTEX algal stock solution is placed under category: bacterial in data/normalized_yaml/bacterial/,
    retains root term.id MediaIngredientMech:UNMAPPED_0045, and documents an unresolved
    primary-source sterilization contradiction on Vitamin B12.'
  target_ids:
  - target-1
  evidence_ids:
  - E1
  - E3
findings:
- finding_id: F1
  issue_key: scope.misclassified_category.CultureMech_015445
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: 'UTEX algal SolutionRecipe is misclassified under category: bacterial with
    a non-snake_case name'
  description: 'DAS_Vitamin_Cocktail.yaml is a SolutionRecipe for UTEX Dasycladales
    Seawater Medium (green algae, https://utex.org/products/das-vitamin-cocktail),
    but is stored in data/normalized_yaml/bacterial/ with category: bacterial and
    non-snake_case name: ''DAS Vitamin Cocktail''.'
  target_ids:
  - target-1
  field_paths:
  - category
  - name
  evidence_ids:
  - E1
  - E3
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    role: maintained_record
- finding_id: F2
  issue_key: grounding.unmapped_root_solution_term.CultureMech_015445
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Root solution term.id retains placeholder MediaIngredientMech:UNMAPPED_0045
  description: Although all 6 items in composition[] carry verified CHEBI and mediaingredientmech_chebi_term
    identifiers, top-level term.id is still set to the placeholder MediaIngredientMech:UNMAPPED_0045.
  target_ids:
  - target-1
  field_paths:
  - term.id
  evidence_ids:
  - E1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    role: maintained_record
- finding_id: F3
  issue_key: provenance.sterilization_conflict.CultureMech_015445.vitamin_b12
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Unresolved UTEX sterilization contradiction on composition[3] (Vitamin B12)
  description: composition[3].notes (Vitamin B12 (Cobalamin), 0.008 G_PER_L) documents
    that the UTEX component table states 'add after autoclaving' whereas the UTEX
    general directions specify sterilizing the cocktail via a 0.45 µm Millipore filter.
  target_ids:
  - target-1
  field_paths:
  - composition[3].notes
  - sterilization.method
  evidence_ids:
  - E1
  - E3
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    role: maintained_record
actions:
- action_id: ACT1
  description: 'Reclassify DAS_Vitamin_Cocktail.yaml from category: bacterial to algae
    (or solution), normalize name to snake_case (''das_vitamin_cocktail''), replace
    root term.id MediaIngredientMech:UNMAPPED_0045 with a permanent identifier, and
    record filter sterilization (0.45 µm) as authoritative over the table note.'
  finding_ids:
  - F1
  - F2
  - F3
  target_ids:
  - target-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml
    role: maintained_record
  acceptance_checks:
  - category and directory placement reflect UTEX algal solution provenance and name
    is snake_case.
  - Root term.id no longer uses an UNMAPPED_* placeholder.
  - linkml-validate -C SolutionRecipe and scripts/validate_strict.py pass with 0 errors.
limitations:
- Review is a non-mutating observation; target YAML file was not modified.
tags:
- review-yaml-record
- review-ingredient-concentrations
- CultureMech_015445
- UTEX
```
