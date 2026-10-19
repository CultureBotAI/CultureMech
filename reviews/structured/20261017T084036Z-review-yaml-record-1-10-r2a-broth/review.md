# Record and concentration audit of 1/10 R2A BROTH (CultureMech:003150)

- Review: 20261017T084036Z-review-yaml-record-1-10-r2a-broth
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-17T08:38:36Z
- Finished UTC: 2026-10-17T08:40:36Z
- Reviewer: antigravity-agent (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Normalized bacterial MediaRecipe 1_10_r2a_broth (CultureMech:003150) passes all four deterministic validators (linkml-validate, validate_strict.py, validate_recipe_references.py, and linkml-term-validator) and accurately captures the JCM Medium 805 / TOGO Medium M732 1:10 diluted R2A broth preparation: 0.32 G_PER_L R2A broth (DAIGO) (Nihon Pharm. Co.) in 1.0 L Distilled water at pH 7.2, autoclaved. Two structured limitations remain: (1) ingredients[0] ('R2A broth (DAIGO)', 0.32 G_PER_L) is grounded to culturemech_term CultureMech:003183 (r2a_broth_daigo) but lacks a CHEBI term or mediaingredientmech_chebi_term (leaving CHEBI and MediaIngredientMech coverage at 50.0%, 1/2) and does not expand the commercial dehydrate sub-ingredients inline; and (2) ingredients[1] ('Distilled water', 1.0 L) records the batch preparation water volume alongside a per-liter solute concentration.

## Scope And Provenance

Single-record structural, ontology, and primary-source concentration audit of CultureMech:003150 (1/10 R2A BROTH).

Selection: Target record selected for review-yaml-record and review-ingredient-concentrations.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 4c69a62c25dd5419766533205c215b0aaa5d14f7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| target-1 | data/normalized_yaml/bacterial/1_10_r2a_broth.yaml | maintained | CultureMech:003150 - 1/10 R2A BROTH |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation | passed | True | target-1 | linkml-validate passed with 0 errors on 1_10_r2a_broth.yaml. |
| Strict schema, recipe reference, and ontology term validation | passed | True | target-1 | validate_strict.py, validate_recipe_references.py, and linkml-term-validator all passed with 0 errors. |

## Scientific And Domain Assessments

### LinkML schema, strict validation, and quantitative alignment with JCM 805

schema: supported. Targets: target-1.

1_10_r2a_broth.yaml conforms to MediaRecipe schema rules and accurately reflects 0.32 G_PER_L R2A broth (DAIGO) in 1.0 L Distilled water at pH 7.2.

### Commercial dehydrate premix grounding and batch solvent representation

grounding: concern. Targets: target-1.

ingredients[0] ('R2A broth (DAIGO)') is linked via culturemech_term CultureMech:003183 but lacks a MediaIngredientMech/CHEBI mapping and sub-ingredient breakdown, while ingredients[1] ('Distilled water', 1.0 L) records the batch preparation water volume.

## Findings

### F1: Commercial premix R2A broth (DAIGO) lacks a MediaIngredientMech mapping and sub-ingredient breakdown

minor / open / confirmed; issue key: grounding.missing_mim_term.CultureMech_003150.r2a_broth_daigo.

ingredients[0] ('R2A broth (DAIGO)', 0.32 G_PER_L) carries culturemech_term CultureMech:003183 (r2a_broth_daigo) and manufacturer metadata ('Nihon Pharm. Co.'), but lacks a mediaingredientmech_chebi_term/mediaingredientmech_term identifier and does not expand the constituent R2A sub-ingredients inline.

### F2: Solvent Distilled water (1.0 L) is listed as an ingredient alongside a G_PER_L solute

informational / open / confirmed; issue key: representation.batch_water_volume.CultureMech_003150.

ingredients[1] ('Distilled water', 1.0 L) represents the 1.0 L batch preparation water volume from JCM Medium 805 alongside ingredients[0] ('R2A broth (DAIGO)', 0.32 G_PER_L).

## Recommended Actions And Acceptance Checks

### ACT1

Assign a MediaIngredientMech complex-premix identifier for R2A broth (DAIGO) (CultureMech:003183) or link its constituent 1/10 R2A sub-ingredient breakdown.

- ingredients[0] carries a valid MediaIngredientMech complex-mixture reference or expanded sub-ingredient breakdown.
- linkml-validate and scripts/validate_strict.py pass with 0 errors.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/normalized_yaml/bacterial/1_10_r2a_broth.yaml; lines 1-128 | supports | Normalized YAML record for CultureMech:003150 containing 2 ingredients: R2A broth (DAIGO) at 0.32 G_PER_L (culturemech_term: CultureMech:003183) and Distilled water at 1.0 L (CHEBI:15377). |
| E2 | Four-validator suite execution on 1_10_r2a_broth.yaml; stdout | supports | All four required validators exited with code 0 and reported zero schema, reference, or ontology label errors. |
| E3 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=805; JCM Medium No. 805 / TOGO Medium M732 recipe specification | supports | JCM Medium No. 805 (1/10 R2A BROTH) specifies 0.32 g R2A broth (DAIGO, Nihon Pharm. Co.) in 1.0 L distilled water, pH 7.2, autoclaved at 121 °C for 15 min. |

## Limits And Additional Notes

- Review is a non-mutating observation; target YAML file was not modified.
- R2A broth (DAIGO) is a commercial dehydrate blend grounded to CultureMech:003183 without a single CHEBI entity.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T084036Z-review-yaml-record-1-10-r2a-broth
kind: record
repository: CultureBotAI/CultureMech
title: Record and concentration audit of 1/10 R2A BROTH (CultureMech:003150)
started_at: '2026-10-17T08:38:36Z'
finished_at: '2026-10-17T08:40:36Z'
reviewer:
  identity: antigravity-agent
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Independent agent review against primary literature/database
    sources and deterministic LinkML validators without modifying target records.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Normalized bacterial MediaRecipe 1_10_r2a_broth (CultureMech:003150) passes
  all four deterministic validators (linkml-validate, validate_strict.py, validate_recipe_references.py,
  and linkml-term-validator) and accurately captures the JCM Medium 805 / TOGO Medium
  M732 1:10 diluted R2A broth preparation: 0.32 G_PER_L R2A broth (DAIGO) (Nihon Pharm.
  Co.) in 1.0 L Distilled water at pH 7.2, autoclaved. Two structured limitations
  remain: (1) ingredients[0] (''R2A broth (DAIGO)'', 0.32 G_PER_L) is grounded to
  culturemech_term CultureMech:003183 (r2a_broth_daigo) but lacks a CHEBI term or
  mediaingredientmech_chebi_term (leaving CHEBI and MediaIngredientMech coverage at
  50.0%, 1/2) and does not expand the commercial dehydrate sub-ingredients inline;
  and (2) ingredients[1] (''Distilled water'', 1.0 L) records the batch preparation
  water volume alongside a per-liter solute concentration.'
source:
  git_revision: 4c69a62c25dd5419766533205c215b0aaa5d14f7
  state: git_commit
  inputs:
  - path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    sha256: 199ec4c42f3e624cad33b581c95fd5ffef8deda69f66b19443684b543a6c2c1b
    role: target
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: Single-record structural, ontology, and primary-source concentration
    audit of CultureMech:003150 (1/10 R2A BROTH).
  selection: Target record selected for review-yaml-record and review-ingredient-concentrations.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - target-1
targets:
- target_id: target-1
  path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
  label: CultureMech:003150 - 1/10 R2A BROTH
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    role: maintained_record
checks:
- check_id: chk-linkml-schema
  name: LinkML schema validation
  status: passed
  required: true
  summary: linkml-validate passed with 0 errors on 1_10_r2a_broth.yaml.
  target_ids:
  - target-1
  command: linkml-validate -s src/culturemech/schema/culturemech.yaml -C MediaRecipe
    data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - E2
- check_id: chk-strict-references-terms
  name: Strict schema, recipe reference, and ontology term validation
  status: passed
  required: true
  summary: validate_strict.py, validate_recipe_references.py, and linkml-term-validator
    all passed with 0 errors.
  target_ids:
  - target-1
  command: python scripts/validate_strict.py data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    && python scripts/validate_recipe_references.py --file data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    && linkml-term-validator validate-data data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - E2
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
  locator: lines 1-128
  accessed_at: '2026-10-17T08:39:36Z'
  support: supports
  summary: 'Normalized YAML record for CultureMech:003150 containing 2 ingredients:
    R2A broth (DAIGO) at 0.32 G_PER_L (culturemech_term: CultureMech:003183) and Distilled
    water at 1.0 L (CHEBI:15377).'
  quote: 'id: CultureMech:003150 / name: 1_10_r2a_broth / preferred_term: R2A broth
    (DAIGO) 0.32 G_PER_L (CultureMech:003183) / preferred_term: Distilled water 1.0
    L (CHEBI:15377)'
  snapshot_sha256: 199ec4c42f3e624cad33b581c95fd5ffef8deda69f66b19443684b543a6c2c1b
- evidence_id: E2
  kind: validation
  reference: Four-validator suite execution on 1_10_r2a_broth.yaml
  locator: stdout
  accessed_at: '2026-10-17T08:39:36Z'
  support: supports
  summary: All four required validators exited with code 0 and reported zero schema,
    reference, or ontology label errors.
  quote: 'No issues found / VALID: 1 files passed all checks / VALID: All recipe references
    resolved / Validation passed'
- evidence_id: E3
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=805
  locator: JCM Medium No. 805 / TOGO Medium M732 recipe specification
  accessed_at: '2026-10-17T08:39:36Z'
  support: supports
  summary: JCM Medium No. 805 (1/10 R2A BROTH) specifies 0.32 g R2A broth (DAIGO,
    Nihon Pharm. Co.) in 1.0 L distilled water, pH 7.2, autoclaved at 121 °C for 15
    min.
  quote: R2A broth (DAIGO) 0.32 g / Distilled water 1.0 L / pH 7.2
assessments:
- assessment_id: A1
  area: schema
  topic: LinkML schema, strict validation, and quantitative alignment with JCM 805
  outcome: supported
  summary: 1_10_r2a_broth.yaml conforms to MediaRecipe schema rules and accurately
    reflects 0.32 G_PER_L R2A broth (DAIGO) in 1.0 L Distilled water at pH 7.2.
  target_ids:
  - target-1
  evidence_ids:
  - E1
  - E2
  - E3
  metrics:
  - name: mediaingredientmech_coverage
    value: 50.0
    unit: percent
    definition: Percentage of direct ingredients with a populated mediaingredientmech_chebi_term.id
      (1/2).
    denominator: 2
    minimum: 0.0
    maximum: 100.0
  - name: chebi_coverage
    value: 50.0
    unit: percent
    definition: Percentage of direct ingredients with a populated CHEBI term.id (1/2).
    denominator: 2
    minimum: 0.0
    maximum: 100.0
- assessment_id: A2
  area: grounding
  topic: Commercial dehydrate premix grounding and batch solvent representation
  outcome: concern
  summary: ingredients[0] ('R2A broth (DAIGO)') is linked via culturemech_term CultureMech:003183
    but lacks a MediaIngredientMech/CHEBI mapping and sub-ingredient breakdown, while
    ingredients[1] ('Distilled water', 1.0 L) records the batch preparation water
    volume.
  target_ids:
  - target-1
  evidence_ids:
  - E1
  - E3
findings:
- finding_id: F1
  issue_key: grounding.missing_mim_term.CultureMech_003150.r2a_broth_daigo
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Commercial premix R2A broth (DAIGO) lacks a MediaIngredientMech mapping and
    sub-ingredient breakdown
  description: ingredients[0] ('R2A broth (DAIGO)', 0.32 G_PER_L) carries culturemech_term
    CultureMech:003183 (r2a_broth_daigo) and manufacturer metadata ('Nihon Pharm.
    Co.'), but lacks a mediaingredientmech_chebi_term/mediaingredientmech_term identifier
    and does not expand the constituent R2A sub-ingredients inline.
  target_ids:
  - target-1
  field_paths:
  - ingredients[0].term
  - ingredients[0].mediaingredientmech_chebi_term
  - ingredients[0].culturemech_term
  evidence_ids:
  - E1
  - E3
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    role: maintained_record
- finding_id: F2
  issue_key: representation.batch_water_volume.CultureMech_003150
  category: representation
  severity: informational
  status: open
  certainty: confirmed
  title: Solvent Distilled water (1.0 L) is listed as an ingredient alongside a G_PER_L
    solute
  description: ingredients[1] ('Distilled water', 1.0 L) represents the 1.0 L batch
    preparation water volume from JCM Medium 805 alongside ingredients[0] ('R2A broth
    (DAIGO)', 0.32 G_PER_L).
  target_ids:
  - target-1
  field_paths:
  - ingredients[1].concentration
  evidence_ids:
  - E1
  - E3
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    role: maintained_record
actions:
- action_id: ACT1
  description: Assign a MediaIngredientMech complex-premix identifier for R2A broth
    (DAIGO) (CultureMech:003183) or link its constituent 1/10 R2A sub-ingredient breakdown.
  finding_ids:
  - F1
  - F2
  target_ids:
  - target-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    role: maintained_record
  acceptance_checks:
  - ingredients[0] carries a valid MediaIngredientMech complex-mixture reference or
    expanded sub-ingredient breakdown.
  - linkml-validate and scripts/validate_strict.py pass with 0 errors.
limitations:
- Review is a non-mutating observation; target YAML file was not modified.
- R2A broth (DAIGO) is a commercial dehydrate blend grounded to CultureMech:003183
  without a single CHEBI entity.
tags:
- review-yaml-record
- review-ingredient-concentrations
- CultureMech_003150
- JCM_J805
```
