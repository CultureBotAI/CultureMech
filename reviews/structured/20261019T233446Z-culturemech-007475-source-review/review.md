# Source and formulation review: 1379 (CultureMech:007475)

- Review: 20261019T233446Z-culturemech-007475-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-19T23:30:28Z
- Finished UTC: 2026-10-19T23:34:46Z
- Reviewer: OpenAI Codex with delegated source and validator checks (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Generated record 1379 remains a malformed rendering of NBRC 1376 MY50G: five source components are concatenated into one descriptor, followed by an unnamed row with a text-valued concentration. The maintained owner restores component rows and the source name, but generated preparation still contains unsupported generic claims.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 17 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; batch002 covers ordinals11-20 after batch001. On fresh origin/main at this batch base, scripts/record_review.py list validated34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007475 | data/merge_yaml/merged/1379.yaml | generated | 1379 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007475 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007475 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch002/017/strict.tsv |
| validate-terms | passed | True | CultureMech:007475 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007475 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007475 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007475.

The four documented recipes completed; interpret the scope of each separately.

### Source accession, stable ID, and generated ownership

identity: supported. Targets: CultureMech:007475.

The import history and maintained owner identify NBRC 1376, MY50G. The numeric local filename/name is not the source accession. The stable CultureMech identifier and merge-event owner agree; the source identity is recoverable despite the uninformative generated name.

### Asserted ingredient identifiers, MIM linkage, and solution references

grounding: concern. Targets: CultureMech:007475.

Neither of the two generated ingredient descriptors carries a chemical CURIE, MIM link, or stock-solution reference. No nonexistent ontology identifier or broken internal link is asserted. The malformed descriptor and empty name must be repaired before ingredient grounding can be assessed meaningfully.

Primary term presence=0/2 encoded descriptors; MIM-link presence=0/2. Those denominators describe encoded rows, not the 5 source components. Owner-only chemical identifiers are not certified by this generated-target review. No replacement ontology identifier is proposed without independent verification.

### History, evidence placement, and source-to-output freshness

provenance: concern. Targets: CultureMech:007475.

The generated August 6 merge predates the maintained August composition recovery and September metadata updates. The later owner history and references are absent from generated output. The historical import source remains recoverable, but there is no scoped ingredient evidence in the target.

The reference validator performed zero excerpt checks. Inline curation history is part of the recipe, not a standalone HistoryRecord. Preserve historical events; do not backdate or rewrite them to imply a generated repair occurred. Follow-up curation belongs in the maintained owner and generation path. The inspected merger code, schema and source-owner bytes are included in the frozen input capture.

### Every encoded row and all five source amounts

quantity: concern. Targets: CultureMech:007475.

Neither generated row represents an individually usable component quantity. The source specifies a high sucrose batch amount explicitly; it must not be replaced by a guessed typical value.

ingredients[0]: correct; preferred_term concatenates all five component names and amounts, while concentration is variable/VARIABLE. ingredients[1]: correct; preferred_term is empty and concentration is Malt extract/G_PER_L, which is nonnumeric. Source component inventory: malt extract 20 g; yeast extract 5 g; sucrose 500 g; distilled water 1 L; agar 20 g. Every mass belongs to the batch containing the specified water addition; none is independently stated as a measured final-volume concentration. All five are separately present in the owner, whose G_PER_L normalizations require explicit source-basis handling before propagation. Source agar is unconditional, unlike optional-agar variants elsewhere.

### Preparation, classification, and unasserted growth scope

consistency: concern. Targets: CultureMech:007475.

COMPLEX/UNDEFINED is consistent with the malt and yeast extracts, and SOLID_AGAR agrees with the specified agar. The generic pH-adjustment and autoclaving statements have no support on the inspected recipe page; the autoclaving sentence is also assigned action DISSOLVE.

Step 1 is an inferred dissolving instruction, not a quoted source protocol. Step 2 says adjust pH if needed although the source gives no pH. Step 3 says sterilize by autoclaving but uses DISSOLVE and gives no cycle. The maintained owner has an empty preparation list; no independent collection-wide protocol was inspected. Absence of species, pH, growth evidence, or storage in the source is a limit, not permission to invent values.

## Findings

### f1: Generated ingredient rows collapse the source formulation

blocker / open / confirmed; issue key: cm-007475-generated-component-collapse.

The generated target retains a five-component ingredient blob and an unnamed row whose G_PER_L value is Malt extract. The source MY50G identity and individual amounts are recoverable, and the maintained owner already restores five rows and the official name, but the generated target predates those repairs.

### f2: Generic preparation asserts unsupported pH and sterilization instructions

major / open / confirmed; issue key: cm-007475-unsupported-preparation.

The inspected NBRC page supplies no pH or autoclaving protocol. Generated preparation nevertheless advises pH adjustment and calls an autoclaving sentence DISSOLVE. A plausible generic operation is not evidence for this source formulation.

## Recommended Actions And Acceptance Checks

### a1

Verify the maintained NBRC 1376 formulation and name against the source, then regenerate through the maintained merge path, retaining the stable CultureMech ID.

- Require 5 distinct source components with numerical amounts and appropriate units; preserve the stated water batch basis without asserting an unmeasured final volume.
- Preserve the explicit 500 g sucrose batch amount, 1 L water addition, and mandatory 20 g agar; do not silently change the formulation or turn added water into measured final volume.
- After separately authorized curation/regeneration, run all four documented target recipes, just verify-merges, just audit-merge-freshness, and an explicit source-to-output component comparison.

### a2

Verify any retained procedure against an applicable primary collection protocol; otherwise preserve the preparation gap. Ensure action tokens agree with source-supported descriptions during regeneration.

- Do not introduce an arbitrary pH or autoclave cycle.
- Every retained preparation claim has an inspected supporting source and a matching action token.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1379.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_1379.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1379.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1379.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch002/017/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch002/017/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1379.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1379.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1376; Medium Detail Information; Medium No.; Medium; all five Composition rows; Comment | supports | NBRC 1376 names MY50G and lists malt extract 20 g, yeast extract 5 g, sucrose 500 g, distilled water 1 L and agar 20 g. Its composition/comment sections give no pH or sterilization protocol. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- This review certifies only the stated target/source comparisons. Maintained-owner ontology mappings and mass-per-liter normalization are not blanket-approved for regeneration.
- The NBRC recipe lists a water addition, not an independently measured final preparation volume. No density, molar-mass, or final-volume conversion is inferred.
- The recipe page does not establish a species-specific growth result or the bacterial category as a biological restriction. No taxon identifier, incubation condition, atmosphere, storage period or growth outcome is invented.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T233446Z-culturemech-007475-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1379 (CultureMech:007475)'
started_at: '2026-10-19T23:30:28Z'
finished_at: '2026-10-19T23:34:46Z'
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
summary: 'Generated record 1379 remains a malformed rendering of NBRC 1376 MY50G:
  five source components are concatenated into one descriptor, followed by an unnamed
  row with a text-valued concentration. The maintained owner restores component rows
  and the source name, but generated preparation still contains unsupported generic
  claims.'
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
  - path: data/merge_yaml/merged/1379.yaml
    sha256: 396fb93910a2df9bddadfc9977cfbb1c52db8552242395c5893eb69a71479547
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_1379.yaml
    sha256: e9b71d254fc51e7a919ca3db0f5b1cbd5963e1da4dd12b8887bf9361bbe25e59
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
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/recover_nbrc_composition.py
    sha256: a723e458895350a68ffae3e446006205b2e00cb185bee13976d5047be56405f0
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/nbrc_raw_yaml.py
    sha256: de5654d4eed2e01a2383dcf417b7d8e2779dbb622de9351c28373fb691812ec1
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/fetch/nbrc_scraper.py
    sha256: 5c5bbda489abe0b6d000b9318a76913ab5496ee83aff58b530c2b42b5989d1e3
    role: context
  - path: src/culturemech/import/nbrc_importer.py
    sha256: 857b7e0ac88aef783ce4bc9b35c4c6a3d9fc38824a5d463010a6046ac4180924
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
  selection: Record 17 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; batch002 covers ordinals11-20 after batch001.
    On fresh origin/main at this batch base, scripts/record_review.py list validated34
    existing bundles and none listed this target path or ID. This bundle selects only
    the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007475
targets:
- target_id: CultureMech:007475
  path: data/merge_yaml/merged/1379.yaml
  label: '1379'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1379.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1379.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007475
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1379.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch002/017/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch002/017/strict.tsv"
  target_ids:
  - CultureMech:007475
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1379.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007475
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1379.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007475
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
  - CultureMech:007475
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1379.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-19T23:34:46Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_1379.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-19T23:34:46Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1379.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:31:52.888115Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1379.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch002/017/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-19T23:31:57.740884Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch002/017/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1379.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:32:00.183674Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1379.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:32:01.284051Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1376
  locator: Medium Detail Information; Medium No.; Medium; all five Composition rows;
    Comment
  accessed_at: '2026-10-19T23:29:38Z'
  support: supports
  summary: NBRC 1376 names MY50G and lists malt extract 20 g, yeast extract 5 g, sucrose
    500 g, distilled water 1 L and agar 20 g. Its composition/comment sections give
    no pH or sterilization protocol.
  snapshot_sha256: 4693881976f4357d5dfa0bc1406d2b136ad8be833686ff92397d9dd4fd7d2916
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007475
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Source accession, stable ID, and generated ownership
  outcome: supported
  summary: The import history and maintained owner identify NBRC 1376, MY50G. The
    numeric local filename/name is not the source accession. The stable CultureMech
    identifier and merge-event owner agree; the source identity is recoverable despite
    the uninformative generated name.
  target_ids:
  - CultureMech:007475
  evidence_ids:
  - record
  - owner-0
  - nbrc
- assessment_id: grounding
  area: grounding
  topic: Asserted ingredient identifiers, MIM linkage, and solution references
  outcome: concern
  summary: Neither of the two generated ingredient descriptors carries a chemical
    CURIE, MIM link, or stock-solution reference. No nonexistent ontology identifier
    or broken internal link is asserted. The malformed descriptor and empty name must
    be repaired before ingredient grounding can be assessed meaningfully.
  target_ids:
  - CultureMech:007475
  evidence_ids:
  - record
  - owner-0
  details: Primary term presence=0/2 encoded descriptors; MIM-link presence=0/2. Those
    denominators describe encoded rows, not the 5 source components. Owner-only chemical
    identifiers are not certified by this generated-target review. No replacement
    ontology identifier is proposed without independent verification.
- assessment_id: provenance
  area: provenance
  topic: History, evidence placement, and source-to-output freshness
  outcome: concern
  summary: The generated August 6 merge predates the maintained August composition
    recovery and September metadata updates. The later owner history and references
    are absent from generated output. The historical import source remains recoverable,
    but there is no scoped ingredient evidence in the target.
  target_ids:
  - CultureMech:007475
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - validate-references
  details: The reference validator performed zero excerpt checks. Inline curation
    history is part of the recipe, not a standalone HistoryRecord. Preserve historical
    events; do not backdate or rewrite them to imply a generated repair occurred.
    Follow-up curation belongs in the maintained owner and generation path. The inspected
    merger code, schema and source-owner bytes are included in the frozen input capture.
- assessment_id: quantities
  area: quantity
  topic: Every encoded row and all five source amounts
  outcome: concern
  summary: Neither generated row represents an individually usable component quantity.
    The source specifies a high sucrose batch amount explicitly; it must not be replaced
    by a guessed typical value.
  target_ids:
  - CultureMech:007475
  evidence_ids:
  - record
  - owner-0
  - nbrc
  details: 'ingredients[0]: correct; preferred_term concatenates all five component
    names and amounts, while concentration is variable/VARIABLE. ingredients[1]: correct;
    preferred_term is empty and concentration is Malt extract/G_PER_L, which is nonnumeric.
    Source component inventory: malt extract 20 g; yeast extract 5 g; sucrose 500
    g; distilled water 1 L; agar 20 g. Every mass belongs to the batch containing
    the specified water addition; none is independently stated as a measured final-volume
    concentration. All five are separately present in the owner, whose G_PER_L normalizations
    require explicit source-basis handling before propagation. Source agar is unconditional,
    unlike optional-agar variants elsewhere.'
- assessment_id: conditions
  area: consistency
  topic: Preparation, classification, and unasserted growth scope
  outcome: concern
  summary: COMPLEX/UNDEFINED is consistent with the malt and yeast extracts, and SOLID_AGAR
    agrees with the specified agar. The generic pH-adjustment and autoclaving statements
    have no support on the inspected recipe page; the autoclaving sentence is also
    assigned action DISSOLVE.
  target_ids:
  - CultureMech:007475
  evidence_ids:
  - record
  - owner-0
  - nbrc
  details: Step 1 is an inferred dissolving instruction, not a quoted source protocol.
    Step 2 says adjust pH if needed although the source gives no pH. Step 3 says sterilize
    by autoclaving but uses DISSOLVE and gives no cycle. The maintained owner has
    an empty preparation list; no independent collection-wide protocol was inspected.
    Absence of species, pH, growth evidence, or storage in the source is a limit,
    not permission to invent values.
findings:
- finding_id: f1
  issue_key: cm-007475-generated-component-collapse
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated ingredient rows collapse the source formulation
  description: The generated target retains a five-component ingredient blob and an
    unnamed row whose G_PER_L value is Malt extract. The source MY50G identity and
    individual amounts are recoverable, and the maintained owner already restores
    five rows and the official name, but the generated target predates those repairs.
  target_ids:
  - CultureMech:007475
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
    path: data/normalized_yaml/bacterial/NBRC_1379.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: cm-007475-unsupported-preparation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generic preparation asserts unsupported pH and sterilization instructions
  description: The inspected NBRC page supplies no pH or autoclaving protocol. Generated
    preparation nevertheless advises pH adjustment and calls an autoclaving sentence
    DISSOLVE. A plausible generic operation is not evidence for this source formulation.
  target_ids:
  - CultureMech:007475
  field_paths:
  - preparation_steps[1]
  - preparation_steps[2]
  evidence_ids:
  - record
  - owner-0
  - nbrc
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1379.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Verify the maintained NBRC 1376 formulation and name against the source,
    then regenerate through the maintained merge path, retaining the stable CultureMech
    ID.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007475
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1379.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Require 5 distinct source components with numerical amounts and appropriate units;
    preserve the stated water batch basis without asserting an unmeasured final volume.
  - Preserve the explicit 500 g sucrose batch amount, 1 L water addition, and mandatory
    20 g agar; do not silently change the formulation or turn added water into measured
    final volume.
  - After separately authorized curation/regeneration, run all four documented target
    recipes, just verify-merges, just audit-merge-freshness, and an explicit source-to-output
    component comparison.
- action_id: a2
  description: Verify any retained procedure against an applicable primary collection
    protocol; otherwise preserve the preparation gap. Ensure action tokens agree with
    source-supported descriptions during regeneration.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007475
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1379.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Do not introduce an arbitrary pH or autoclave cycle.
  - Every retained preparation claim has an inspected supporting source and a matching
    action token.
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- This review certifies only the stated target/source comparisons. Maintained-owner
  ontology mappings and mass-per-liter normalization are not blanket-approved for
  regeneration.
- The NBRC recipe lists a water addition, not an independently measured final preparation
  volume. No density, molar-mass, or final-volume conversion is inferred.
- The recipe page does not establish a species-specific growth result or the bacterial
  category as a biological restriction. No taxon identifier, incubation condition,
  atmosphere, storage period or growth outcome is invented.
tags:
- unreviewed-records
- batch-002
- generated-medium
```
