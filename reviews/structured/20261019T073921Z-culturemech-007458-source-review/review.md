# Source and formulation review: 1135 (CultureMech:007458)

- Review: 20261019T073921Z-culturemech-007458-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-19T07:31:46Z
- Finished UTC: 2026-10-19T07:39:21Z
- Reviewer: OpenAI Codex with delegated source and validator checks (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Generated record 1135 is a stale, malformed rendering of NBRC1132 Malt Extract Ebios Agar. The official source and repaired maintained owner resolve the identity and formulation, while the generated target still contains concatenated components and a text-valued concentration.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 10 of the first ten uncovered paths in Python lexicographic repository-relative path order. Initial scripts/record_review.py list validated 34 existing bundles, whose targets covered 0 of 6320 merged records. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007458 | data/merge_yaml/merged/1135.yaml | generated | 1135 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007458 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007458 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work/010/strict.tsv |
| validate-terms | passed | True | CultureMech:007458 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007458 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007458 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007458.

The four documented recipes completed; interpret the scope of each separately.

### NBRC identity and owner

identity: supported. Targets: CultureMech:007458.

CultureMech:007458 and merged_from resolve to NBRC_1135.yaml; the actual source accession is NBRC1132. The number 1135 is the historical local label, not verified as the source medium number.

### Entire generated composition

representation: concern. Targets: CultureMech:007458.

Neither generated ingredient row faithfully represents the four source ingredients.

ingredients[0] concatenates malt extract, Ebios tablets, water, agar and the supplier footnote with a VARIABLE quantity; ingredients[1] has empty preferred_term and value Malt extract with G_PER_L. Both require correction through source-to-output generation. Preserve batch amounts 20 g malt extract,1 g tablet product, 1 L water, 15 g agar, without inventing a defined chemical composition for Ebios or a measured final volume. All those components are separately represented in the maintained owner.

### Preparation, classification and provenance

consistency: concern. Targets: CultureMech:007458.

Step 3 encodes DISSOLVE while describing sterilization; generic pH adjustment and autoclaving are not supported by the inspected medium page.

The owner has corrected name, source term and component rows absent from generated output. Complex/undefined classification and agar state fit the composition. Bacterial filing is not established by the recipe alone and is not treated as a biological restriction. No taxon/growth outcome, chemical CURIE or internal stock reference is asserted by the generated target. Embedded history describes the older merge, not the later owner repair.

## Findings

### f1: Generated ingredient rows do not represent NBRC1132

blocker / open / confirmed; issue key: cm-007458-generated-component-collapse.

The entire composition is collapsed into a single blob plus an unnamed ingredient whose G_PER_L value is Malt extract. The maintained owner already restores four source components and the official name, but the generated target predates these repairs.

### f2: Generic preparation includes unsupported and miscoded statements

major / open / confirmed; issue key: cm-007458-generated-preparation-claims.

The target advises unspecified pH adjustment and calls an autoclaving sentence DISSOLVE. The inspected source page specifies no pH or autoclave protocol; a generic plausible step is not source evidence.

## Recommended Actions And Acceptance Checks

### a1

Reconcile the normalized NBRC1132 owner with the official source and regenerate the derived record, preserving the stable CultureMech ID and commercial Ebios boundary.

- Require four separate source components and numerical amounts/appropriate units with an explicitly unmapped Ebios product where necessary.
- Compare identity and composition source-to-output, run focused schema/strict validation and just audit-merge-freshness.

### a2

Verify preparation against a collection protocol before retaining generic pH or sterilization claims; correct action/text mismatch in maintained inputs if relevant before regeneration.

- Each retained preparation statement has inspected source support or an explicit unresolved status.
- No invented pH or autoclave cycle; action tokens agree with supported text.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1135.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_1135.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1135.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1135.yaml --workers 1 --out /private/tmp/culturemech-review-work/010/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work/010/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1135.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1135.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1132; Medium Detail Information, Composition and product footnote | supports | NBRC1132 identifies Malt Extract Ebios Agar (MEBA), listing malt extract 20 g, Ebios tablets 1 g, distilled water 1 L and agar 15 g. Its footnote names the tablet manufacturer/distributor; no incubation or sterilization cycle is stated. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. The reference recipe performed zero excerpt checks for this target; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T073921Z-culturemech-007458-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1135 (CultureMech:007458)'
started_at: '2026-10-19T07:31:46Z'
finished_at: '2026-10-19T07:39:21Z'
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
summary: Generated record 1135 is a stale, malformed rendering of NBRC1132 Malt Extract
  Ebios Agar. The official source and repaired maintained owner resolve the identity
  and formulation, while the generated target still contains concatenated components
  and a text-valued concentration.
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
  - path: data/merge_yaml/merged/1135.yaml
    sha256: 3f1ffda2479edcbcb75c7f03937db7b3bf6cce34feee218efeca3a65bc113fe2
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_1135.yaml
    sha256: e917651747b216b30b83013f16e19dac0f881efebf0f54315640a1380a231349
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
  selection: Record 10 of the first ten uncovered paths in Python lexicographic repository-relative
    path order. Initial scripts/record_review.py list validated 34 existing bundles,
    whose targets covered 0 of 6320 merged records. This bundle selects only the named
    record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007458
targets:
- target_id: CultureMech:007458
  path: data/merge_yaml/merged/1135.yaml
  label: '1135'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1135.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1135.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007458
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1135.yaml --workers 1 --out
    /private/tmp/culturemech-review-work/010/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work/010/strict.tsv"
  target_ids:
  - CultureMech:007458
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1135.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007458
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1135.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007458
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
  - CultureMech:007458
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1135.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-19T07:39:21Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_1135.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-19T07:39:21Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1135.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T07:34:10.016002Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1135.yaml --workers 1 --out
    /private/tmp/culturemech-review-work/010/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-19T07:34:13.128832Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work/010/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1135.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T07:34:17.626681Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1135.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T07:34:19.246483Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1132
  locator: Medium Detail Information, Composition and product footnote
  accessed_at: '2026-10-19T07:32:40Z'
  support: supports
  summary: NBRC1132 identifies Malt Extract Ebios Agar (MEBA), listing malt extract
    20 g, Ebios tablets 1 g, distilled water 1 L and agar 15 g. Its footnote names
    the tablet manufacturer/distributor; no incubation or sterilization cycle is stated.
  quote: Malt Extract Ebios Agar (MEBA)
  snapshot_sha256: b08728692d11b1f111b9dff19fa1cbbd0f3f2b929ff5be0dbc4336f56b59eec2
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007458
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: NBRC identity and owner
  outcome: supported
  summary: CultureMech:007458 and merged_from resolve to NBRC_1135.yaml; the actual
    source accession is NBRC1132. The number 1135 is the historical local label, not
    verified as the source medium number.
  target_ids:
  - CultureMech:007458
  evidence_ids:
  - record
  - owner-0
  - nbrc
- assessment_id: quantities
  area: representation
  topic: Entire generated composition
  outcome: concern
  summary: Neither generated ingredient row faithfully represents the four source
    ingredients.
  target_ids:
  - CultureMech:007458
  evidence_ids:
  - record
  - owner-0
  - nbrc
  details: ingredients[0] concatenates malt extract, Ebios tablets, water, agar and
    the supplier footnote with a VARIABLE quantity; ingredients[1] has empty preferred_term
    and value Malt extract with G_PER_L. Both require correction through source-to-output
    generation. Preserve batch amounts 20 g malt extract,1 g tablet product, 1 L water,
    15 g agar, without inventing a defined chemical composition for Ebios or a measured
    final volume. All those components are separately represented in the maintained
    owner.
- assessment_id: protocol
  area: consistency
  topic: Preparation, classification and provenance
  outcome: concern
  summary: Step 3 encodes DISSOLVE while describing sterilization; generic pH adjustment
    and autoclaving are not supported by the inspected medium page.
  target_ids:
  - CultureMech:007458
  evidence_ids:
  - record
  - owner-0
  - nbrc
  details: The owner has corrected name, source term and component rows absent from
    generated output. Complex/undefined classification and agar state fit the composition.
    Bacterial filing is not established by the recipe alone and is not treated as
    a biological restriction. No taxon/growth outcome, chemical CURIE or internal
    stock reference is asserted by the generated target. Embedded history describes
    the older merge, not the later owner repair.
findings:
- finding_id: f1
  issue_key: cm-007458-generated-component-collapse
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated ingredient rows do not represent NBRC1132
  description: The entire composition is collapsed into a single blob plus an unnamed
    ingredient whose G_PER_L value is Malt extract. The maintained owner already restores
    four source components and the official name, but the generated target predates
    these repairs.
  target_ids:
  - CultureMech:007458
  field_paths:
  - name
  - original_name
  - ingredients[0]
  - ingredients[1]
  - media_term
  evidence_ids:
  - record
  - owner-0
  - nbrc
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1135.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: cm-007458-generated-preparation-claims
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generic preparation includes unsupported and miscoded statements
  description: The target advises unspecified pH adjustment and calls an autoclaving
    sentence DISSOLVE. The inspected source page specifies no pH or autoclave protocol;
    a generic plausible step is not source evidence.
  target_ids:
  - CultureMech:007458
  field_paths:
  - preparation_steps[1]
  - preparation_steps[2]
  evidence_ids:
  - record
  - owner-0
  - nbrc
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1135.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Reconcile the normalized NBRC1132 owner with the official source and
    regenerate the derived record, preserving the stable CultureMech ID and commercial
    Ebios boundary.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007458
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1135.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Require four separate source components and numerical amounts/appropriate units
    with an explicitly unmapped Ebios product where necessary.
  - Compare identity and composition source-to-output, run focused schema/strict validation
    and just audit-merge-freshness.
- action_id: a2
  description: Verify preparation against a collection protocol before retaining generic
    pH or sterilization claims; correct action/text mismatch in maintained inputs
    if relevant before regeneration.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007458
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1135.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Each retained preparation statement has inspected source support or an explicit
    unresolved status.
  - No invented pH or autoclave cycle; action tokens agree with supported text.
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
