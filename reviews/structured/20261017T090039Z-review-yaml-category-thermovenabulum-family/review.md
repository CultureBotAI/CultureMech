# Category and merge-boundary review of the Thermovenabulum medium record family

- Review: 20261017T090039Z-review-yaml-category-thermovenabulum-family
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-17T08:58:39Z
- Finished UTC: 2026-10-17T09:00:39Z
- Reviewer: antigravity-agent (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Category and merge-boundary audit of all 6 normalized and merged records named 'THERMOVENABULUM MEDIUM' / 'thermovenabulum_medium' under review-yaml-category and review-ingredient-concentrations. Direct inspection of the 6 on-disk YAML records proves that they represent three chemically distinct DSMZ media that share the ambiguous normalized name 'thermovenabulum_medium': (1) Formulation Group A — DSMZ Medium 962a (target-2 DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml and its merged output target-1 THERMOVENABULUM_MEDIUM.yaml, CultureMech:002143), a fumarate + meat extract + bicarbonate medium (3.16518 G_PER_L Na2-fumarate, 2.96736 G_PER_L Meat extract, 0.692384 G_PER_L NaHCO3); (2) Formulation Group B — DSMZ Medium 1255 (target-3 thermovenabulum_medium.yaml CultureMech:000714, target-4 KOMODO_1255_THERMOVENABULUM_medium.yaml CultureMech:004016, and their merged output target-6 thermovenabulum_medium__41e13ba4.yaml CultureMech:004016), a D-glucose + tryptone + PIPES + Na2S medium (1.97628 G_PER_L D-Glucose, 1.97628 G_PER_L Tryptone, 3.75494 G_PER_L PIPES, 0.494071 G_PER_L Na2S x 9 H2O); and (3) Formulation Group C — DSMZ Medium 962 (target-5 KOMODO_962_THERMOVENABULUM_medium.yaml CultureMech:006919), which is Thermincola ferriacetica medium containing 7.91296 G_PER_L Na2-9,10-anthraquinone-2,6-disulfonate (AQDS) and 2.96736 G_PER_L Na-acetate (already linked via parent_media to thermincola_ferriacetica_medium.yaml CultureMech:002142). All 6 files suffer from unscaled 100x–1000x stock flattening: Groups A and C inline Wolin's trace elements and vitamins at undiluted 1 L stock strengths (100x) and sum base + stock CaCl2 x 2 H2O into 0.42640900000000004 G_PER_L, while Group B inlines SL-10 trace elements (1000x, e.g., HCl 2.5 G_PER_L, FeCl2 x 4 H2O 1.5 G_PER_L) and vitamins (100x).

## Scope And Provenance

Complete family and category boundary review of all 6 records sharing the Thermovenabulum medium name across data/normalized_yaml/bacterial/ and data/merge_yaml/merged/.

Selection: All 6 repository records matching *thermovenabulum* (case-insensitive).
Coverage: full; 6 reviewed / 6 in the declared population.
Source: git_commit at Git base 4c69a62c25dd5419766533205c215b0aaa5d14f7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| target-1 | data/merge_yaml/merged/THERMOVENABULUM_MEDIUM.yaml | generated | CultureMech:002143 - THERMOVENABULUM MEDIUM (merged 962a) |
| target-2 | data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml | maintained | CultureMech:002143 - THERMOVENABULUM MEDIUM (DSMZ 962a) |
| target-3 | data/normalized_yaml/bacterial/thermovenabulum_medium.yaml | maintained | CultureMech:000714 - THERMOVENABULUM MEDIUM (DSMZ 1255) |
| target-4 | data/normalized_yaml/bacterial/KOMODO_1255_THERMOVENABULUM_medium.yaml | maintained | CultureMech:004016 - THERMOVENABULUM medium (KOMODO 1255) |
| target-5 | data/normalized_yaml/bacterial/KOMODO_962_THERMOVENABULUM_medium.yaml | maintained | CultureMech:006919 - THERMOVENABULUM medium (KOMODO 962 / DSMZ 962) |
| target-6 | data/merge_yaml/merged/thermovenabulum_medium__41e13ba4.yaml | generated | CultureMech:004016 - thermovenabulum_medium (merged 1255) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Four-validator suite on the 4 normalized Thermovenabulum records | passed | True | target-2, target-3, target-4, target-5 | All 4 normalized records (target-2, target-3, target-4, target-5) pass linkml-validate, validate_strict.py, validate_recipe_references.py, and linkml-term-validator. |
| Reference and ontology term validation on the 2 merged Thermovenabulum records | passed | True | target-1, target-6 | target-1 and target-6 pass recipe reference and ontology term validation (while exhibiting the known schema gap for merge_fingerprint/merged_from). |

## Scientific And Domain Assessments

### Category boundary partitioning across DSMZ 962a, DSMZ 1255, and DSMZ 962

consistency: concern. Targets: target-1, target-2, target-3, target-4, target-5, target-6.

All 6 files share the normalized name 'thermovenabulum_medium' despite spanning three distinct chemical formulations: Group A (DSMZ 962a: target-1, target-2), Group B (DSMZ 1255: target-3, target-4, target-6), and Group C (DSMZ 962: target-5).

### Unscaled 100x–1000x trace element and vitamin stock flattening across all 6 records

quantity: concern. Targets: target-1, target-2, target-3, target-4, target-5, target-6.

Groups A (target-1, target-2) and C (target-5) flatten Wolin's trace element and vitamin solutions (10 mL/L) at undiluted 1 L stock concentrations (100x inflation) and sum base + stock CaCl2 x 2 H2O into 0.42640900000000004 G_PER_L, while Group B (target-3, target-4, target-6) flattens SL-10 trace elements (1 mL/L -&gt; 1000x inflation) and vitamin solution (10 mL/L -&gt; 100x inflation).

## Findings

### F1: Three chemically distinct DSMZ media (962a, 1255, and 962) collide under name: thermovenabulum_medium

major / open / confirmed; issue key: nomenclature.name_collision.thermovenabulum_family.

DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml (DSMZ 962a: Na2-fumarate + Meat extract + NaHCO3), thermovenabulum_medium.yaml / KOMODO_1255_THERMOVENABULUM_medium.yaml (DSMZ 1255: D-Glucose + Tryptone + PIPES + Na2S), and KOMODO_962_THERMOVENABULUM_medium.yaml (DSMZ 962: Thermincola ferriacetica medium with AQDS + Na-acetate) all share name: thermovenabulum_medium.

### F2: Unscaled 100x–1000x stock flattening across all 6 Thermovenabulum records and duplicate CaCl2 x 2 H2O sum in DSMZ 962a and KOMODO 962

major / open / confirmed; issue key: concentration.unscaled_stock_inlining.thermovenabulum_family.

All 4 normalized records (and both generated merged records) flatten their trace element and vitamin stock solutions at undiluted 1 L stock concentrations without applying dilution factors: target-2 (and target-1) and target-5 inflate Wolin's trace elements and vitamins 100-fold and sum base + stock CaCl2 x 2 H2O to 0.42640900000000004 G_PER_L (' [Merged 2 duplicates: 0.326409, 0.1]'), while target-3 and target-4 (and target-6) inflate SL-10 trace elements 1000-fold (e.g., HCl 2.5 G_PER_L, FeCl2 x 4 H2O 1.5 G_PER_L) and vitamin solution 100-fold.

### F3: Undeclared merge metadata slots on target-1/target-6 and missing mediaingredientmech_chebi_term on shared ingredients

minor / open / confirmed; issue key: grounding.missing_mim_and_merge_slots.thermovenabulum_family.

target-1 and target-6 emit undeclared merge_fingerprint and merged_from slots, and all 6 records lack mediaingredientmech_chebi_term on Yeast extract, Sodium resazurin (CHEBI:8806), and Calcium D-(+)-pantothenate (CHEBI:31345) (plus Meat extract in Group A, Tryptone in Group B, and Na2-9,10-anthraquinone-2,6-disulfonate in Group C).

## Recommended Actions And Acceptance Checks

### ACT1

Disambiguate normalized names across DSMZ 962a (target-2), DSMZ 1255 (target-3, target-4), and DSMZ 962 (target-5), extract or scale the flattened Wolin/SL-10 trace element and vitamin stocks by their 1 mL/L and 10 mL/L dilution factors, declare merge_fingerprint and merged_from in culturemech.yaml, and backfill missing mediaingredientmech_chebi_term identifiers.

- Group A (DSMZ 962a), Group B (DSMZ 1255), and Group C (DSMZ 962) have distinct normalized names and remain separate merge clusters.
- Trace element and vitamin concentrations in all 4 normalized records reflect 1 mL/L (SL-10) and 10 mL/L (Wolin trace/vitamin) dilution factors.
- Merged files validate cleanly under linkml-validate and scripts/validate_strict.py.

## Category Boundaries

- split: target-1, target-2, target-3, target-4, target-5, target-6. Partition the 6 records named thermovenabulum_medium into three chemically distinct formulation clusters: Group A (DSMZ 962a fumarate + meat extract), Group B (DSMZ 1255 D-glucose + tryptone + PIPES + Na2S), and Group C (DSMZ 962 Thermincola ferriacetica medium with AQDS + Na-acetate).
- lump: target-3, target-4, target-6. target-3 (thermovenabulum_medium.yaml, CultureMech:000714) and target-4 (KOMODO_1255_THERMOVENABULUM_medium.yaml, CultureMech:004016) share identical 31-ingredient DSMZ 1255 compositions and rightly merge into target-6 (thermovenabulum_medium__41e13ba4.yaml).

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | Thermovenabulum record family in data/normalized_yaml/bacterial/ and data/merge_yaml/merged/; target-1..target-6 | supports | Comparison of on-disk ingredient lists across target-1..target-6: Group A (target-1, target-2) has 33 ingredients with Na2-fumarate (3.16518 G_PER_L), Meat extract (2.96736 G_PER_L), summed CaCl2 x 2 H2O (0.42640900000000004 G_PER_L), and unscaled Wolin stocks; Group B (target-3, target-4, target-6) has 31 ingredients with D-Glucose (1.97628 G_PER_L), Tryptone (1.97628 G_PER_L), PIPES (3.75494 G_PER_L), Na2S x 9 H2O (0.494071 G_PER_L), and unscaled SL-10/vitamin stocks; Group C (target-5) has 32 ingredients with AQDS (7.91296 G_PER_L), Na-acetate (2.96736 G_PER_L), summed CaCl2 x 2 H2O (0.42640900000000004 G_PER_L), and parent_media CultureMech:002142. |
| E2 | Validator suite outputs across all 6 Thermovenabulum records; stdout | supports | All 4 normalized records pass all 4 validators; both merged records (target-1 and target-6) pass reference and term checks but fail closed-schema validation due to undeclared merge_fingerprint and merged_from slots. |
| E3 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium962a.pdf; DSMZ Medium 962, 962a, and 1255 specifications | refutes | DSMZ 962 (Thermincola ferriacetica medium with AQDS/acetate), DSMZ 962a (fumarate/meat extract modification with 10 mL/L Wolin trace elements and 10 mL/L vitamins), and DSMZ 1255 (Thermovenabulum medium with glucose/tryptone/PIPES/sulfide, 1 mL/L SL-10, and 10 mL/L vitamins) are three chemically distinct media whose trace element and vitamin stocks are added at 1–10 mL/L rather than 1000 mL/L. |

## Limits And Additional Notes

- Review is a non-mutating observation; target YAML files were not modified.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T090039Z-review-yaml-category-thermovenabulum-family
kind: category
repository: CultureBotAI/CultureMech
title: Category and merge-boundary review of the Thermovenabulum medium record family
started_at: '2026-10-17T08:58:39Z'
finished_at: '2026-10-17T09:00:39Z'
reviewer:
  identity: antigravity-agent
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Independent agent review against primary literature/database
    sources and deterministic LinkML validators without modifying target records.
skill: review-yaml-category
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Category and merge-boundary audit of all 6 normalized and merged records
  named ''THERMOVENABULUM MEDIUM'' / ''thermovenabulum_medium'' under review-yaml-category
  and review-ingredient-concentrations. Direct inspection of the 6 on-disk YAML records
  proves that they represent three chemically distinct DSMZ media that share the ambiguous
  normalized name ''thermovenabulum_medium'': (1) Formulation Group A — DSMZ Medium
  962a (target-2 DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml and its merged output target-1
  THERMOVENABULUM_MEDIUM.yaml, CultureMech:002143), a fumarate + meat extract + bicarbonate
  medium (3.16518 G_PER_L Na2-fumarate, 2.96736 G_PER_L Meat extract, 0.692384 G_PER_L
  NaHCO3); (2) Formulation Group B — DSMZ Medium 1255 (target-3 thermovenabulum_medium.yaml
  CultureMech:000714, target-4 KOMODO_1255_THERMOVENABULUM_medium.yaml CultureMech:004016,
  and their merged output target-6 thermovenabulum_medium__41e13ba4.yaml CultureMech:004016),
  a D-glucose + tryptone + PIPES + Na2S medium (1.97628 G_PER_L D-Glucose, 1.97628
  G_PER_L Tryptone, 3.75494 G_PER_L PIPES, 0.494071 G_PER_L Na2S x 9 H2O); and (3)
  Formulation Group C — DSMZ Medium 962 (target-5 KOMODO_962_THERMOVENABULUM_medium.yaml
  CultureMech:006919), which is Thermincola ferriacetica medium containing 7.91296
  G_PER_L Na2-9,10-anthraquinone-2,6-disulfonate (AQDS) and 2.96736 G_PER_L Na-acetate
  (already linked via parent_media to thermincola_ferriacetica_medium.yaml CultureMech:002142).
  All 6 files suffer from unscaled 100x–1000x stock flattening: Groups A and C inline
  Wolin''s trace elements and vitamins at undiluted 1 L stock strengths (100x) and
  sum base + stock CaCl2 x 2 H2O into 0.42640900000000004 G_PER_L, while Group B inlines
  SL-10 trace elements (1000x, e.g., HCl 2.5 G_PER_L, FeCl2 x 4 H2O 1.5 G_PER_L) and
  vitamins (100x).'
source:
  git_revision: 4c69a62c25dd5419766533205c215b0aaa5d14f7
  state: git_commit
  inputs:
  - path: data/merge_yaml/merged/THERMOVENABULUM_MEDIUM.yaml
    sha256: c9aa366d36e9cc35a6dcf14b690a0927d725a66d980fa1ec5b2320525427d8f7
    role: target
  - path: data/merge_yaml/merged/thermovenabulum_medium__41e13ba4.yaml
    sha256: 28919a93d39ca61022643418a8b280d599e9c9553e61d2093f0ddba215f55a85
    role: target
  - path: data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml
    sha256: faef12985852dfdfe6d55fd632294a1097dd39f3a7d481ad4a5c2815e8973a71
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1255_THERMOVENABULUM_medium.yaml
    sha256: 9fbfb82fd9878017afa5be7bef2615f0e5c4da0d6b638f7e7aa701a41dc91e8e
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_962_THERMOVENABULUM_medium.yaml
    sha256: 460eeaf6f1751612abb45f82f2ec6e9308a9fe1da8dc56d152d97d592a8c3c9f
    role: target
  - path: data/normalized_yaml/bacterial/thermovenabulum_medium.yaml
    sha256: ba0856ddde784a86329e28fe6a186912bf49ea964dbcfd0c116c2ed6e6da4403
    role: target
  - path: src/culturemech/merge/merge_recipes.py
    sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: Complete family and category boundary review of all 6 records sharing
    the Thermovenabulum medium name across data/normalized_yaml/bacterial/ and data/merge_yaml/merged/.
  selection: All 6 repository records matching *thermovenabulum* (case-insensitive).
  coverage: full
  population_size: 6
  reviewed_target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
targets:
- target_id: target-1
  path: data/merge_yaml/merged/THERMOVENABULUM_MEDIUM.yaml
  label: CultureMech:002143 - THERMOVENABULUM MEDIUM (merged 962a)
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml
    role: maintained_record
- target_id: target-2
  path: data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml
  label: CultureMech:002143 - THERMOVENABULUM MEDIUM (DSMZ 962a)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml
    role: maintained_record
- target_id: target-3
  path: data/normalized_yaml/bacterial/thermovenabulum_medium.yaml
  label: CultureMech:000714 - THERMOVENABULUM MEDIUM (DSMZ 1255)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thermovenabulum_medium.yaml
    role: maintained_record
- target_id: target-4
  path: data/normalized_yaml/bacterial/KOMODO_1255_THERMOVENABULUM_medium.yaml
  label: CultureMech:004016 - THERMOVENABULUM medium (KOMODO 1255)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1255_THERMOVENABULUM_medium.yaml
    role: maintained_record
- target_id: target-5
  path: data/normalized_yaml/bacterial/KOMODO_962_THERMOVENABULUM_medium.yaml
  label: CultureMech:006919 - THERMOVENABULUM medium (KOMODO 962 / DSMZ 962)
  record_class: MediaRecipe
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_962_THERMOVENABULUM_medium.yaml
    role: maintained_record
- target_id: target-6
  path: data/merge_yaml/merged/thermovenabulum_medium__41e13ba4.yaml
  label: CultureMech:004016 - thermovenabulum_medium (merged 1255)
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1255_THERMOVENABULUM_medium.yaml
    role: maintained_record
checks:
- check_id: chk-normalized-family-validators
  name: Four-validator suite on the 4 normalized Thermovenabulum records
  status: passed
  required: true
  summary: All 4 normalized records (target-2, target-3, target-4, target-5) pass
    linkml-validate, validate_strict.py, validate_recipe_references.py, and linkml-term-validator.
  target_ids:
  - target-2
  - target-3
  - target-4
  - target-5
  command: python scripts/validate_strict.py data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml
    data/normalized_yaml/bacterial/thermovenabulum_medium.yaml data/normalized_yaml/bacterial/KOMODO_1255_THERMOVENABULUM_medium.yaml
    data/normalized_yaml/bacterial/KOMODO_962_THERMOVENABULUM_medium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - E2
- check_id: chk-merged-family-validators
  name: Reference and ontology term validation on the 2 merged Thermovenabulum records
  status: passed
  required: true
  summary: target-1 and target-6 pass recipe reference and ontology term validation
    (while exhibiting the known schema gap for merge_fingerprint/merged_from).
  target_ids:
  - target-1
  - target-6
  command: python scripts/validate_recipe_references.py --file data/merge_yaml/merged/THERMOVENABULUM_MEDIUM.yaml
    && python scripts/validate_recipe_references.py --file data/merge_yaml/merged/thermovenabulum_medium__41e13ba4.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - E2
evidence:
- evidence_id: E1
  kind: record_content
  reference: Thermovenabulum record family in data/normalized_yaml/bacterial/ and
    data/merge_yaml/merged/
  locator: target-1..target-6
  accessed_at: '2026-10-17T08:59:39Z'
  support: supports
  summary: 'Comparison of on-disk ingredient lists across target-1..target-6: Group
    A (target-1, target-2) has 33 ingredients with Na2-fumarate (3.16518 G_PER_L),
    Meat extract (2.96736 G_PER_L), summed CaCl2 x 2 H2O (0.42640900000000004 G_PER_L),
    and unscaled Wolin stocks; Group B (target-3, target-4, target-6) has 31 ingredients
    with D-Glucose (1.97628 G_PER_L), Tryptone (1.97628 G_PER_L), PIPES (3.75494 G_PER_L),
    Na2S x 9 H2O (0.494071 G_PER_L), and unscaled SL-10/vitamin stocks; Group C (target-5)
    has 32 ingredients with AQDS (7.91296 G_PER_L), Na-acetate (2.96736 G_PER_L),
    summed CaCl2 x 2 H2O (0.42640900000000004 G_PER_L), and parent_media CultureMech:002142.'
- evidence_id: E2
  kind: validation
  reference: Validator suite outputs across all 6 Thermovenabulum records
  locator: stdout
  accessed_at: '2026-10-17T08:59:39Z'
  support: supports
  summary: All 4 normalized records pass all 4 validators; both merged records (target-1
    and target-6) pass reference and term checks but fail closed-schema validation
    due to undeclared merge_fingerprint and merged_from slots.
- evidence_id: E3
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium962a.pdf
  locator: DSMZ Medium 962, 962a, and 1255 specifications
  accessed_at: '2026-10-17T08:59:39Z'
  support: refutes
  summary: DSMZ 962 (Thermincola ferriacetica medium with AQDS/acetate), DSMZ 962a
    (fumarate/meat extract modification with 10 mL/L Wolin trace elements and 10 mL/L
    vitamins), and DSMZ 1255 (Thermovenabulum medium with glucose/tryptone/PIPES/sulfide,
    1 mL/L SL-10, and 10 mL/L vitamins) are three chemically distinct media whose
    trace element and vitamin stocks are added at 1–10 mL/L rather than 1000 mL/L.
  snapshot_sha256: 6734e5de05db31cb26c9a3de2404156f97b49e39d5b1fb6548fd980614f524c6
assessments:
- assessment_id: A1
  area: consistency
  topic: Category boundary partitioning across DSMZ 962a, DSMZ 1255, and DSMZ 962
  outcome: concern
  summary: 'All 6 files share the normalized name ''thermovenabulum_medium'' despite
    spanning three distinct chemical formulations: Group A (DSMZ 962a: target-1, target-2),
    Group B (DSMZ 1255: target-3, target-4, target-6), and Group C (DSMZ 962: target-5).'
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
  - E3
- assessment_id: A2
  area: quantity
  topic: Unscaled 100x–1000x trace element and vitamin stock flattening across all
    6 records
  outcome: concern
  summary: Groups A (target-1, target-2) and C (target-5) flatten Wolin's trace element
    and vitamin solutions (10 mL/L) at undiluted 1 L stock concentrations (100x inflation)
    and sum base + stock CaCl2 x 2 H2O into 0.42640900000000004 G_PER_L, while Group
    B (target-3, target-4, target-6) flattens SL-10 trace elements (1 mL/L -> 1000x
    inflation) and vitamin solution (10 mL/L -> 100x inflation).
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  evidence_ids:
  - E1
  - E3
findings:
- finding_id: F1
  issue_key: nomenclature.name_collision.thermovenabulum_family
  category: nomenclature
  severity: major
  status: open
  certainty: confirmed
  title: 'Three chemically distinct DSMZ media (962a, 1255, and 962) collide under
    name: thermovenabulum_medium'
  description: 'DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml (DSMZ 962a: Na2-fumarate + Meat
    extract + NaHCO3), thermovenabulum_medium.yaml / KOMODO_1255_THERMOVENABULUM_medium.yaml
    (DSMZ 1255: D-Glucose + Tryptone + PIPES + Na2S), and KOMODO_962_THERMOVENABULUM_medium.yaml
    (DSMZ 962: Thermincola ferriacetica medium with AQDS + Na-acetate) all share name:
    thermovenabulum_medium.'
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  field_paths:
  - name
  - original_name
  evidence_ids:
  - E1
  - E3
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thermovenabulum_medium.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1255_THERMOVENABULUM_medium.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_962_THERMOVENABULUM_medium.yaml
    role: maintained_record
- finding_id: F2
  issue_key: concentration.unscaled_stock_inlining.thermovenabulum_family
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Unscaled 100x–1000x stock flattening across all 6 Thermovenabulum records
    and duplicate CaCl2 x 2 H2O sum in DSMZ 962a and KOMODO 962
  description: 'All 4 normalized records (and both generated merged records) flatten
    their trace element and vitamin stock solutions at undiluted 1 L stock concentrations
    without applying dilution factors: target-2 (and target-1) and target-5 inflate
    Wolin''s trace elements and vitamins 100-fold and sum base + stock CaCl2 x 2 H2O
    to 0.42640900000000004 G_PER_L ('' [Merged 2 duplicates: 0.326409, 0.1]''), while
    target-3 and target-4 (and target-6) inflate SL-10 trace elements 1000-fold (e.g.,
    HCl 2.5 G_PER_L, FeCl2 x 4 H2O 1.5 G_PER_L) and vitamin solution 100-fold.'
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  field_paths:
  - ingredients
  evidence_ids:
  - E1
  - E3
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thermovenabulum_medium.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1255_THERMOVENABULUM_medium.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_962_THERMOVENABULUM_medium.yaml
    role: maintained_record
- finding_id: F3
  issue_key: grounding.missing_mim_and_merge_slots.thermovenabulum_family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Undeclared merge metadata slots on target-1/target-6 and missing mediaingredientmech_chebi_term
    on shared ingredients
  description: target-1 and target-6 emit undeclared merge_fingerprint and merged_from
    slots, and all 6 records lack mediaingredientmech_chebi_term on Yeast extract,
    Sodium resazurin (CHEBI:8806), and Calcium D-(+)-pantothenate (CHEBI:31345) (plus
    Meat extract in Group A, Tryptone in Group B, and Na2-9,10-anthraquinone-2,6-disulfonate
    in Group C).
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  field_paths:
  - merge_fingerprint
  - merged_from
  - ingredients
  evidence_ids:
  - E1
  - E2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/schema/culturemech.yaml
    role: linkml_schema
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thermovenabulum_medium.yaml
    role: maintained_record
actions:
- action_id: ACT1
  description: Disambiguate normalized names across DSMZ 962a (target-2), DSMZ 1255
    (target-3, target-4), and DSMZ 962 (target-5), extract or scale the flattened
    Wolin/SL-10 trace element and vitamin stocks by their 1 mL/L and 10 mL/L dilution
    factors, declare merge_fingerprint and merged_from in culturemech.yaml, and backfill
    missing mediaingredientmech_chebi_term identifiers.
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
    path: data/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/thermovenabulum_medium.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1255_THERMOVENABULUM_medium.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_962_THERMOVENABULUM_medium.yaml
    role: maintained_record
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/schema/culturemech.yaml
    role: linkml_schema
  acceptance_checks:
  - Group A (DSMZ 962a), Group B (DSMZ 1255), and Group C (DSMZ 962) have distinct
    normalized names and remain separate merge clusters.
  - Trace element and vitamin concentrations in all 4 normalized records reflect 1
    mL/L (SL-10) and 10 mL/L (Wolin trace/vitamin) dilution factors.
  - Merged files validate cleanly under linkml-validate and scripts/validate_strict.py.
boundary_decisions:
- action: split
  target_ids:
  - target-1
  - target-2
  - target-3
  - target-4
  - target-5
  - target-6
  rationale: 'Partition the 6 records named thermovenabulum_medium into three chemically
    distinct formulation clusters: Group A (DSMZ 962a fumarate + meat extract), Group
    B (DSMZ 1255 D-glucose + tryptone + PIPES + Na2S), and Group C (DSMZ 962 Thermincola
    ferriacetica medium with AQDS + Na-acetate).'
  evidence_ids:
  - E1
  - E3
  proposed_groups:
  - label: 'Group A: DSMZ Medium 962a (Na2-fumarate + Meat extract + NaHCO3)'
    target_ids:
    - target-1
    - target-2
  - label: 'Group B: DSMZ Medium 1255 (D-Glucose + Tryptone + PIPES + Na2S x 9 H2O)'
    target_ids:
    - target-3
    - target-4
    - target-6
  - label: 'Group C: DSMZ Medium 962 / Thermincola ferriacetica medium (AQDS + Na-acetate)'
    target_ids:
    - target-5
- action: lump
  target_ids:
  - target-3
  - target-4
  - target-6
  rationale: target-3 (thermovenabulum_medium.yaml, CultureMech:000714) and target-4
    (KOMODO_1255_THERMOVENABULUM_medium.yaml, CultureMech:004016) share identical
    31-ingredient DSMZ 1255 compositions and rightly merge into target-6 (thermovenabulum_medium__41e13ba4.yaml).
  evidence_ids:
  - E1
  - E2
limitations:
- Review is a non-mutating observation; target YAML files were not modified.
tags:
- review-yaml-category
- review-ingredient-concentrations
- review-recipes
- Thermovenabulum
- DSMZ_962a
- DSMZ_1255
```
