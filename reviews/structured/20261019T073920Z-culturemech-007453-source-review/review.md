# Source and formulation review: 1063 (CultureMech:007453)

- Review: 20261019T073920Z-culturemech-007453-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-19T07:31:34Z
- Finished UTC: 2026-10-19T07:39:20Z
- Reviewer: OpenAI Codex with delegated source and validator checks (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Generated NBRC record 1063 is a stale, malformed rendering of the maintained Pae I Medium + 0.1% (w/v) Urea record (NBRC 1062). The official source and repaired owner support a resolvable identity, but the generated ingredient representation and pH instructions require repair through the maintained generation path.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 5 of the first ten uncovered paths in Python lexicographic repository-relative path order. Initial scripts/record_review.py list validated 34 existing bundles, whose targets covered 0 of 6320 merged records. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007453 | data/merge_yaml/merged/1063.yaml | generated | 1063 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007453 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007453 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work/005/strict.tsv |
| validate-terms | passed | True | CultureMech:007453 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007453 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007453 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007453.

The four documented recipes completed; interpret the scope of each separately.

### Generated identity and maintained owner

identity: supported. Targets: CultureMech:007453.

CultureMech:007453 and the merge source resolve unambiguously to normalized NBRC_1063.yaml; its source accession is NBRC 1062, not NBRC 1063.

### Every listed ingredient and concentration

quantity: concern. Targets: CultureMech:007453.

Both generated ingredient rows are unusable as component quantities.

ingredients[0] concatenates six components and the buffer instruction as a single preferred_term with VARIABLE concentration; ingredients[1] has an empty preferred_term and concentration.value=Tryptone with G_PER_L. Neither is a supported quantity claim. The source quantities are retained separately in the maintained owner; preserve its 1 L water basis and optional agar. No final-volume or density conversion is justified. Decision=correct for both generated rows; not_quantified for buffer addition volume.

### Preparation, state, classification and evidence scope

completeness: concern. Targets: CultureMech:007453.

The pH 8.5/buffer instruction survives inside the concatenated ingredient name but is absent from ph_value and the operative preparation steps; an autoclaving sentence is miscoded as DISSOLVE. Its SOLID_AGAR classification is meaningful only for the optional-agar variant.

The source supports an undefined complex formulation, with no organism/growth outcome, incubation condition, shelf-life, or autoclave cycle stated on the inspected recipe. Generic autoclaving text in the owner is not independently certified by this page. Embedded history is readable and the August merge precedes the owner repair events; do not rewrite that history to imply the generated target was repaired. No ingredient ontology CURIE or internal stock reference is asserted in the generated ingredient rows.

## Findings

### f1: Generated ingredient rows collapse the source formulation

blocker / open / confirmed; issue key: cm-007453-generated-component-collapse.

The generated target still has a concatenated ingredient/protocol blob, an empty ingredient name, and a nonnumeric Tryptone concentration. The owner already contains separately structured components and identifies NBRC 1062. Passing schema gates do not make these rows a usable recipe.

### f2: Generated preparation strands the specified pH in an ingredient blob

major / open / confirmed; issue key: cm-007453-generated-preparation-loss.

The source requires pH 8.5 with 50 mM Tris-HCl, whereas generated preparation merely says adjust if needed and the explicit instruction is stranded in ingredients[0].preferred_term; step 3 has action DISSOLVE but describes autoclaving. The repaired owner contains pH and explicit buffer context.

## Recommended Actions And Acceptance Checks

### a1

Reconcile the maintained NBRC1062 owner with the official source, then regenerate this target through the merge code; retain the permanent CultureMech ID and do not patch generated rows.

- Check generated name/accession and all six source components against NBRC1062; preserve optional agar and the distinct buffer instruction.
- Run just validate-schema and just validate-strict on the regenerated target, then just audit-merge-freshness and source-to-output component comparison.

### a2

Preserve the source pH/buffer boundary during regeneration and separately verify any sterilization assertion against an official protocol before treating it as source-backed.

- Verify pH 8.5 and 50 mM buffer context are retained without inventing a buffer dose.
- Check preparation action/text agreement and cite source support for sterilization if retained.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1063.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_1063.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1063.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1063.yaml --workers 1 --out /private/tmp/culturemech-review-work/005/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work/005/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1063.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1063.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1062; Medium Detail Information: number, name, Composition and final instruction | supports | NBRC accession 1062 names Pae I Medium + 0.1% (w/v) Urea; lists tryptone 5 g, yeast extract 3 g, NaCl 10 g, urea 1 g, water 1 L, optional agar 15 g, and pH 8.5 adjustment using 50 mM Tris-HCl. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. The reference recipe performed zero excerpt checks for this target; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The maintained owner maps its Tris-HCl buffer to CHEBI:9754 (tris free base). Verify this owner-only salt/solution identity before regeneration; this generated-target review does not certify that mapping.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T073920Z-culturemech-007453-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1063 (CultureMech:007453)'
started_at: '2026-10-19T07:31:34Z'
finished_at: '2026-10-19T07:39:20Z'
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
summary: Generated NBRC record 1063 is a stale, malformed rendering of the maintained
  Pae I Medium + 0.1% (w/v) Urea record (NBRC 1062). The official source and repaired
  owner support a resolvable identity, but the generated ingredient representation
  and pH instructions require repair through the maintained generation path.
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
  - path: data/merge_yaml/merged/1063.yaml
    sha256: 431749549fdfbb0f4bd00c460c3499489fa1beed514866384f92631d271e7d11
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_1063.yaml
    sha256: a99d9cfc2c82f40a75c1a3a536d0bff8dc4f6740bfd593294f3bda76b3c8ee23
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
  selection: Record 5 of the first ten uncovered paths in Python lexicographic repository-relative
    path order. Initial scripts/record_review.py list validated 34 existing bundles,
    whose targets covered 0 of 6320 merged records. This bundle selects only the named
    record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007453
targets:
- target_id: CultureMech:007453
  path: data/merge_yaml/merged/1063.yaml
  label: '1063'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1063.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1063.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007453
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1063.yaml --workers 1 --out
    /private/tmp/culturemech-review-work/005/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work/005/strict.tsv"
  target_ids:
  - CultureMech:007453
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1063.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007453
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1063.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007453
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
  - CultureMech:007453
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1063.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-19T07:39:20Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_1063.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-19T07:39:20Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1063.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T07:33:25.233003Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1063.yaml --workers 1 --out
    /private/tmp/culturemech-review-work/005/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-19T07:33:28.762873Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work/005/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1063.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T07:33:32.536004Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1063.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T07:33:35.140066Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1062
  locator: 'Medium Detail Information: number, name, Composition and final instruction'
  accessed_at: '2026-10-19T07:32:40Z'
  support: supports
  summary: NBRC accession 1062 names Pae I Medium + 0.1% (w/v) Urea; lists tryptone
    5 g, yeast extract 3 g, NaCl 10 g, urea 1 g, water 1 L, optional agar 15 g, and
    pH 8.5 adjustment using 50 mM Tris-HCl.
  quote: Adjust pH to 8.5
  snapshot_sha256: 1d0d12bb71098f31c743b7de1a002bb01d7eda5fd1b07860b4511e3cd620be3f
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007453
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Generated identity and maintained owner
  outcome: supported
  summary: CultureMech:007453 and the merge source resolve unambiguously to normalized
    NBRC_1063.yaml; its source accession is NBRC 1062, not NBRC 1063.
  target_ids:
  - CultureMech:007453
  evidence_ids:
  - record
  - owner-0
  - nbrc
- assessment_id: quantities
  area: quantity
  topic: Every listed ingredient and concentration
  outcome: concern
  summary: Both generated ingredient rows are unusable as component quantities.
  target_ids:
  - CultureMech:007453
  evidence_ids:
  - record
  - owner-0
  - nbrc
  details: ingredients[0] concatenates six components and the buffer instruction as
    a single preferred_term with VARIABLE concentration; ingredients[1] has an empty
    preferred_term and concentration.value=Tryptone with G_PER_L. Neither is a supported
    quantity claim. The source quantities are retained separately in the maintained
    owner; preserve its 1 L water basis and optional agar. No final-volume or density
    conversion is justified. Decision=correct for both generated rows; not_quantified
    for buffer addition volume.
- assessment_id: protocol
  area: completeness
  topic: Preparation, state, classification and evidence scope
  outcome: concern
  summary: The pH 8.5/buffer instruction survives inside the concatenated ingredient
    name but is absent from ph_value and the operative preparation steps; an autoclaving
    sentence is miscoded as DISSOLVE. Its SOLID_AGAR classification is meaningful
    only for the optional-agar variant.
  target_ids:
  - CultureMech:007453
  evidence_ids:
  - record
  - owner-0
  - nbrc
  details: The source supports an undefined complex formulation, with no organism/growth
    outcome, incubation condition, shelf-life, or autoclave cycle stated on the inspected
    recipe. Generic autoclaving text in the owner is not independently certified by
    this page. Embedded history is readable and the August merge precedes the owner
    repair events; do not rewrite that history to imply the generated target was repaired.
    No ingredient ontology CURIE or internal stock reference is asserted in the generated
    ingredient rows.
findings:
- finding_id: f1
  issue_key: cm-007453-generated-component-collapse
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated ingredient rows collapse the source formulation
  description: The generated target still has a concatenated ingredient/protocol blob,
    an empty ingredient name, and a nonnumeric Tryptone concentration. The owner already
    contains separately structured components and identifies NBRC 1062. Passing schema
    gates do not make these rows a usable recipe.
  target_ids:
  - CultureMech:007453
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
    path: data/normalized_yaml/bacterial/NBRC_1063.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: cm-007453-generated-preparation-loss
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated preparation strands the specified pH in an ingredient blob
  description: The source requires pH 8.5 with 50 mM Tris-HCl, whereas generated preparation
    merely says adjust if needed and the explicit instruction is stranded in ingredients[0].preferred_term;
    step 3 has action DISSOLVE but describes autoclaving. The repaired owner contains
    pH and explicit buffer context.
  target_ids:
  - CultureMech:007453
  field_paths:
  - ph_value
  - preparation_steps[1]
  - preparation_steps[2]
  evidence_ids:
  - record
  - owner-0
  - nbrc
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1063.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Reconcile the maintained NBRC1062 owner with the official source, then
    regenerate this target through the merge code; retain the permanent CultureMech
    ID and do not patch generated rows.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007453
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1063.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Check generated name/accession and all six source components against NBRC1062;
    preserve optional agar and the distinct buffer instruction.
  - Run just validate-schema and just validate-strict on the regenerated target, then
    just audit-merge-freshness and source-to-output component comparison.
- action_id: a2
  description: Preserve the source pH/buffer boundary during regeneration and separately
    verify any sterilization assertion against an official protocol before treating
    it as source-backed.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007453
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1063.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify pH 8.5 and 50 mM buffer context are retained without inventing a buffer
    dose.
  - Check preparation action/text agreement and cite source support for sterilization
    if retained.
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. The reference recipe performed zero excerpt checks for this target; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- The maintained owner maps its Tris-HCl buffer to CHEBI:9754 (tris free base). Verify
  this owner-only salt/solution identity before regeneration; this generated-target
  review does not certify that mapping.
tags:
- unreviewed-records
- batch-001
- generated-medium
```
