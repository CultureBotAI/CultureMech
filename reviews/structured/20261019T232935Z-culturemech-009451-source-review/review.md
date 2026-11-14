# Source and formulation review: 10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate (CultureMech:009451)

- Review: 20261019T232935Z-culturemech-009451-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-19T07:31:44Z
- Finished UTC: 2026-10-19T23:29:35Z
- Reviewer: OpenAI Codex with delegated source and validator checks (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated TOGO M2916 record loses the source 10% (w/w) skim-milk concentration and preparation sequence, retaining an erroneous 1 G_PER_L skim-milk value. The source API confirms 1 mM sodium formate and the maintained owner already repairs the material omissions.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 9 of the first ten uncovered paths in Python lexicographic repository-relative path order. Initial scripts/record_review.py list validated 34 existing bundles, whose targets covered 0 of 6320 merged records. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009451 | data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml | generated | 10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009451 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009451 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work/009/strict.tsv |
| validate-terms | passed | True | CultureMech:009451 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009451 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009451 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009451.

The four documented recipes completed; interpret the scope of each separately.

### TOGO accession and medium variant

identity: supported. Targets: CultureMech:009451.

TOGO M2916 matches the label and identifies the formate-supplemented skim-milk variant. The generated record and maintained owner share CultureMech:009451.

### Both ingredient quantities

quantity: concern. Targets: CultureMech:009451.

Sodium formate 1 MILLIMOLAR is directly supported; skim milk 1 G_PER_L is not.

ingredients[0]: correct; preserve 10 PERCENT_W_W and distinguish source preparation volume 1 L from concentration. No density-based conversion to g/L is justified. ingredients[1]: verified 1 mM sodium formate, no mass conversion made. Source supplier Wako supports the product-name provenance, not a specific catalog number. The generated record asserts no chemical CURIE or internal stock reference.

### Preparation and strain-specific scope

completeness: concern. Targets: CultureMech:009451.

Source heat/cool/supplement sequence is lost in the generated target but represented by the maintained owner.

The source distinguishes formate-supplemented L. bulgaricus 2038 monoculture from a casein-peptide S. thermophilus 1131 variant and unsupplemented coculture. These are source-scoping observations, not newly asserted growth records or validated taxonomic identifiers. The inspected API contains no linked primary paper URL; exhaustive underlying-paper and taxonomy research was not performed. No supplied pH, storage, atmosphere or numerical growth claims are silently added.

## Findings

### f1: Ten-percent milk concentration became 1 G_PER_L

major / open / confirmed; issue key: cm-009451-generated-milk-concentration.

TOGO separately encodes a 1 L preparation volume and 10% w/w concentration. Generated ingredients[0] collapses these into 1 G_PER_L, contradicting the source and its own title. The normalized owner now records 10 PERCENT_W_W.

### f2: Generated output omits the source heat and cooling sequence

major / open / confirmed; issue key: cm-009451-generated-preparation-loss.

TOGO specifies 95 C for 2 minutes followed by immediate cooling to 43 C before supplementation. Generated output has no preparation_steps; the repaired owner contains all three stages.

## Recommended Actions And Acceptance Checks

### a1

Reconcile source-matching maintained quantities and regenerate while preserving mass-fraction concentration and its distinct preparation-volume context.

- Read back 10 PERCENT_W_W skim milk and 1 MILLIMOLAR sodium formate against TOGO M2916.
- No mass/volume percentage conversion without measured density; run focused schema/strict and merge-freshness checks.

### a2

Preserve source-backed preparation and reference context from the normalized owner during regeneration, retaining the monoculture/formulation distinction.

- Verify ordered 95 C heating for 2 minutes, immediate cooling to 43 C, and 1 mM formate addition.
- Keep optional organism evidence strain-specific and verify identifiers separately before adding a growth assertion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml --workers 1 --out /private/tmp/culturemech-review-work/009/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work/009/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2916; meta; components[0].items; comments[0:2] | supports | M2916 lists skim milk volume 1 L with conc_value 10 and conc_unit w/w; sodium formate 1 mM. Comments specify heating to 95 C for 2 minutes, immediate cooling to 43 C, and formate supplementation for L. bulgaricus 2038 monoculture. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. The reference recipe performed zero excerpt checks for this target; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T232935Z-culturemech-009451-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate
  (CultureMech:009451)'
started_at: '2026-10-19T07:31:44Z'
finished_at: '2026-10-19T23:29:35Z'
reviewer:
  identity: OpenAI Codex with delegated source and validator checks
  kind: agent
  independence: independent
  independence_basis: Review team did not author or edit the assessed recipe bytes;
    findings were assessed against the frozen checkout and inspected source documents.
    This is an agent review, not experimental verification.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The generated TOGO M2916 record loses the source 10% (w/w) skim-milk concentration
  and preparation sequence, retaining an erroneous 1 G_PER_L skim-milk value. The
  source API confirms 1 mM sodium formate and the maintained owner already repairs
  the material omissions.
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
  - path: data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
    sha256: 1fbcbd6d1da23c04ccdfb9d892a7733b6fc580831df6985f9b778af0b1781ef0
    role: target
  - path: data/normalized_yaml/bacterial/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
    sha256: ee6dbf237c54abdcfb480f60801e38d3b9ed2f6284d5a1734c82824360e00096
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
  selection: Record 9 of the first ten uncovered paths in Python lexicographic repository-relative
    path order. Initial scripts/record_review.py list validated 34 existing bundles,
    whose targets covered 0 of 6320 merged records. This bundle selects only the named
    record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009451
targets:
- target_id: CultureMech:009451
  path: data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
  label: 10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009451
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
    --workers 1 --out /private/tmp/culturemech-review-work/009/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work/009/strict.tsv"
  target_ids:
  - CultureMech:009451
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009451
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009451
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
  - CultureMech:009451
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-19T07:39:20Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-19T07:39:20Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T07:34:03.348927Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
    --workers 1 --out /private/tmp/culturemech-review-work/009/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-19T07:34:05.023328Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work/009/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T07:34:06.977457Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T07:34:08.156624Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2916
  locator: meta; components[0].items; comments[0:2]
  accessed_at: '2026-10-19T07:34:04Z'
  support: supports
  summary: M2916 lists skim milk volume 1 L with conc_value 10 and conc_unit w/w;
    sodium formate 1 mM. Comments specify heating to 95 C for 2 minutes, immediate
    cooling to 43 C, and formate supplementation for L. bulgaricus 2038 monoculture.
  quote: 10% (wt/wt) skim milk
  snapshot_sha256: 93cd4395e10cb0b251380a3b005a142ca7d1c7a3fbcb6376587aa7c99e28882e
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009451
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: TOGO accession and medium variant
  outcome: supported
  summary: TOGO M2916 matches the label and identifies the formate-supplemented skim-milk
    variant. The generated record and maintained owner share CultureMech:009451.
  target_ids:
  - CultureMech:009451
  evidence_ids:
  - record
  - owner-0
  - togo
- assessment_id: quantities
  area: quantity
  topic: Both ingredient quantities
  outcome: concern
  summary: Sodium formate 1 MILLIMOLAR is directly supported; skim milk 1 G_PER_L
    is not.
  target_ids:
  - CultureMech:009451
  evidence_ids:
  - record
  - owner-0
  - togo
  details: 'ingredients[0]: correct; preserve 10 PERCENT_W_W and distinguish source
    preparation volume 1 L from concentration. No density-based conversion to g/L
    is justified. ingredients[1]: verified 1 mM sodium formate, no mass conversion
    made. Source supplier Wako supports the product-name provenance, not a specific
    catalog number. The generated record asserts no chemical CURIE or internal stock
    reference.'
- assessment_id: protocol
  area: completeness
  topic: Preparation and strain-specific scope
  outcome: concern
  summary: Source heat/cool/supplement sequence is lost in the generated target but
    represented by the maintained owner.
  target_ids:
  - CultureMech:009451
  evidence_ids:
  - record
  - owner-0
  - togo
  details: The source distinguishes formate-supplemented L. bulgaricus 2038 monoculture
    from a casein-peptide S. thermophilus 1131 variant and unsupplemented coculture.
    These are source-scoping observations, not newly asserted growth records or validated
    taxonomic identifiers. The inspected API contains no linked primary paper URL;
    exhaustive underlying-paper and taxonomy research was not performed. No supplied
    pH, storage, atmosphere or numerical growth claims are silently added.
findings:
- finding_id: f1
  issue_key: cm-009451-generated-milk-concentration
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Ten-percent milk concentration became 1 G_PER_L
  description: TOGO separately encodes a 1 L preparation volume and 10% w/w concentration.
    Generated ingredients[0] collapses these into 1 G_PER_L, contradicting the source
    and its own title. The normalized owner now records 10 PERCENT_W_W.
  target_ids:
  - CultureMech:009451
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: cm-009451-generated-preparation-loss
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated output omits the source heat and cooling sequence
  description: TOGO specifies 95 C for 2 minutes followed by immediate cooling to
    43 C before supplementation. Generated output has no preparation_steps; the repaired
    owner contains all three stages.
  target_ids:
  - CultureMech:009451
  field_paths:
  - preparation_steps
  - references
  evidence_ids:
  - record
  - owner-0
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3
  normalization_reason: P3.4 normally maps to minor. Here the entire source-specified
    95 C for 2 minutes and immediate cooling to 43 C sequence is omitted, materially
    changing preparation reproducibility; this specific omission is normalized to
    major.
actions:
- action_id: a1
  description: Reconcile source-matching maintained quantities and regenerate while
    preserving mass-fraction concentration and its distinct preparation-volume context.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009451
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Read back 10 PERCENT_W_W skim milk and 1 MILLIMOLAR sodium formate against TOGO
    M2916.
  - No mass/volume percentage conversion without measured density; run focused schema/strict
    and merge-freshness checks.
- action_id: a2
  description: Preserve source-backed preparation and reference context from the normalized
    owner during regeneration, retaining the monoculture/formulation distinction.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009451
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify ordered 95 C heating for 2 minutes, immediate cooling to 43 C, and 1 mM
    formate addition.
  - Keep optional organism evidence strain-specific and verify identifiers separately
    before adding a growth assertion.
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. The reference recipe performed zero excerpt checks for this target; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-001
- generated-medium
```
