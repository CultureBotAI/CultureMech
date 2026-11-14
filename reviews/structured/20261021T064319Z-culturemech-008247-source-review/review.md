# Source and formulation review: 1_5_lbm_medium (CultureMech:008247)

- Review: 20261021T064319Z-culturemech-008247-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T06:36:41Z
- Finished UTC: 2026-10-21T06:43:19Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M1688 resolves to NBRC893. Direct amounts and source brand names are retained, but seawater volume is encoded as mass and its link to a generic salt solution is not supported by the source alternatives. Generated output also omits maintained pH and agar grounding corrections.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 55 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 006 selects ordinals 51-60 after five validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008247 | data/merge_yaml/merged/1_5_LBM_medium.yaml | generated | 1_5_lbm_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008247 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008247 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch006/055/strict.tsv |
| validate-terms | passed | True | CultureMech:008247 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008247 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008247 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008247.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:008247.

0 primary CHEBI identities resolve with matching labels; 0 of 0 current secondary keys have live pinned-index rows. Unresolved keys: [].

3 direct ingredient instances; primary coverage 0/3 (0.00%), verified secondary coverage 0/3 (0.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Medium accession and seawater alternatives

identity: concern. Targets: CultureMech:008247.

The medium accession resolves correctly. The source allows filtered aged seawater or a named commercial artificial seawater; it does not establish equivalence to the linked generic MediaDive sea-salt solution. A matching broad name cannot verify a stock substitution.

### ingredients[0].concentration

quantity: supported. Targets: CultureMech:008247.

verified nominal recipe amount: source gram mass agrees on the stated one-liter seawater basis. Source brand qualifiers remain present; the agar amount is conditional. No final measured volume is inferred.

### ingredients[1].concentration

quantity: supported. Targets: CultureMech:008247.

verified nominal recipe amount: source gram mass agrees on the stated one-liter seawater basis. Source brand qualifiers remain present; the agar amount is conditional. No final measured volume is inferred.

### ingredients[2].concentration

quantity: supported. Targets: CultureMech:008247.

verified nominal recipe amount: source gram mass agrees on the stated one-liter seawater basis. Source brand qualifiers remain present; the agar amount is conditional. No final measured volume is inferred.

### solutions[0].concentration

quantity: concern. Targets: CultureMech:008247.

correct: the source liter volume is recast as G_PER_L. No seawater density or justification for a mass conversion is provided.

### Referenced stock composition and evidence

quantity: concern. Targets: CultureMech:008247.

The generic stock salt amount matches the provider within that stock. Its water value represents milliliters upstream, not the local percentage encoding. These facts do not establish any concentration in NBRC893 because the link itself lacks source support. No inherited salt contribution is calculated.

### Maintained pH, agar grounding and provenance

completeness: concern. Targets: CultureMech:008247.

The owner now preserves source pH, agar grounding, source notes and later curation provenance that the generated record omits. These corrections are supported by source text and the ontology response. Other stock-unit and stock-identity problems remain in both layers.

### Conditional agar, mixtures and biological claims

scope: supported. Targets: CultureMech:008247.

COMPLEX/UNDEFINED is supported by undefined extracts and seawater. SOLID_AGAR is compatible with choosing the source optional-agar branch; preserve that branch condition and do not assert every preparation is solid. No organism-specific growth assertion is made.

### Placeholder name and source evidence

evidence: concern. Targets: CultureMech:008247.

Unknown solution is a placeholder despite a preferred term. Source notes/references and curation events do not provide narrow quantity evidence. Target reference validation inspected zero excerpts.

## Findings

### f1: Generic seawater stock is not verified as the source material

blocker / open / confirmed; issue key: CM008247-unsupported-seawater-link.

The resolvable generic salt solution is not established as either source-prescribed seawater alternative. Its broad label cannot justify replacing the original material.

### f2: Seawater volume is encoded as a mass concentration

major / open / confirmed; issue key: CM008247-seawater-volume-unit.

The source liter value is labeled G_PER_L in target and owner without density evidence.

### f3: Generated output lacks maintained source corrections

major / open / confirmed; issue key: CM008247-generated-corrections-missing.

Supported owner pH, agar grounding and later curation provenance are absent from the generated target.

### f4: Solution placeholder and narrow evidence need follow-up

minor / open / confirmed; issue key: CM008247-placeholder-and-evidence.

The placeholder solution name and lack of scoped source evidence obscure an otherwise recoverable provenance chain.

## Recommended Actions And Acceptance Checks

### a1

Reconcile the seawater descriptor with the original alternatives and retain their preparation/product qualifiers. Remove or replace the unsupported link only through evidence-backed curation; do not transfer generic-stock quantities.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the original volume and batch basis, with no assumed seawater density or inherited stock dilution.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Retain verified owner corrections during separately authorized regeneration, then recheck that all intended fields and provenance survive.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Resolve the descriptor name consistently with the verified material and attach narrow quantity/alternative-condition evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_5_LBM_medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/1_5_lbm_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_5_LBM_medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_5_LBM_medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch006/055/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch006/055/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_5_LBM_medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_5_LBM_medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/1_5_LBM_medium.yaml:1:id: CultureMech:008247<br>./data/normalized_yaml/bacterial/1_5_lbm_medium.yaml:1:id: CultureMech:008247<br> |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {} |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=893; Medium893 composition, pH and footnotes | supports | Whole recipe and seawater footnote inspected; natural and named commercial artificial alternatives remain distinct. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1688; meta; components[0]; comments | supports | Complete source entry retains original NBRC accession, pH and seawater footnotes. |
| stock-api | https://mediadive.dsmz.de/rest/solution/1801; data.id; data.name; data.recipe; data.steps | supports | Linked solution identity resolves, but its generic salt preparation is not identified by the NBRC source as the prescribed seawater alternative. |
| stock-local | data/normalized_yaml/bacterial/mediadive_1801_Seawater.yaml; Whole referenced stock and index entry; source hash captured | context_only | The index resolves solution1801 to CultureMech:011231. Salt-row evidence matches the live provider JSON exactly; the water row is incorrectly encoded as a percentage and the placeholder ingredients field is present. This bounded dependency check does not constitute a separate stock review. |
| owner-agar | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Owner-added CHEBI:2509 label and obsolete status | supports | The maintained owner agar identifier resolves with a matching label; it is absent from the generated target. |
| trace | NBRC893/TOGO M1688 and maintained comparison; Three direct amounts; seawater addition; corrected owner fields | context_only | {"direct": [{"index": 0, "source": {"amount": 15, "unit": "g"}, "target": {"value": "15", "unit": "G_PER_L"}}, {"index": 1, "source": {"amount": 1, "unit": "g"}, "target": {"value": "1", "unit": "G_PER_L"}}, {"index": 2, "source": {"amount": 2, "unit": "g"}, "target": {"value": "2", "unit": "G_PER_L"}}], "source_seawater": {"amount": 1, "unit": "L"}, "target_solution": {"preferred_term": "Seawater*", "term": {"id": "mediadive.solution:1801", "label": "Seawater"}, "concentration": {"value": "1", "unit": "G_PER_L"}, "notes": "See mediadive_1801_Seawater.yaml for composition", "name": "Unknown solution"}, "owner_ph": 7.0, "owner_agar_term": {"id": "CHEBI:2509", "label": "agar"}, "stock_salt_evidence_matches_live_provider": true} |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Referenced stock was read for identity, relevant quantity evidence and dependency risk; it was not independently reviewed as a second target.
- No complete natural-seawater composition, commercial artificial-seawater formula, density, stock dilution, final-volume measurement or experimental growth is inferred.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T064319Z-culturemech-008247-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_5_lbm_medium (CultureMech:008247)'
started_at: '2026-10-21T06:36:41Z'
finished_at: '2026-10-21T06:43:19Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify the assessed recipe bytes.
    This is an independent agent review of captured local inputs and inspected primary/database
    sources, not experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: TOGO M1688 resolves to NBRC893. Direct amounts and source brand names are
  retained, but seawater volume is encoded as mass and its link to a generic salt
  solution is not supported by the source alternatives. Generated output also omits
  maintained pH and agar grounding corrections.
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
  - path: data/merge_yaml/merged/1_5_LBM_medium.yaml
    sha256: 92e9ffcdcf59b50c29c5ac8013bc78dfb8de6e1dffece02e214e650d12958b2b
    role: target
  - path: data/normalized_yaml/bacterial/1_5_lbm_medium.yaml
    sha256: 2441d5a6b2f80b8822710674c0dda323f7836b5772ed0684559defef908d3f04
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_1801_Seawater.yaml
    sha256: 5f065e84ba52fd60223785bbca506de054f7b4767ba54fb36263e3276bbb9454
    role: context
  - path: data/normalized_yaml/solutions/mediadive_solution_index.json
    sha256: 2e43ed2391d0113480837e0756120d71a8dad8a4490010054e67bfb90c66d381
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
  - path: src/culturemech/convert/mediadive_raw_yaml.py
    sha256: 70ba720001705c315f2c5bd40871e08f6f429b6229c78255e6c94dfdcc482432
    role: context
  - path: src/culturemech/convert/togo_raw_yaml.py
    sha256: ce5e73545c9ecde54724259d2fd475676c0f3cb44dcfd283950e89fd49c10993
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
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
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
  selection: Record 55 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 006 selects ordinals 51-60 after five
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008247
targets:
- target_id: CultureMech:008247
  path: data/merge_yaml/merged/1_5_LBM_medium.yaml
  label: 1_5_lbm_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_5_lbm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_5_LBM_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008247
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_5_LBM_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch006/055/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch006/055/strict.tsv"
  target_ids:
  - CultureMech:008247
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_5_LBM_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008247
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_5_LBM_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008247
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
  - CultureMech:008247
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_5_LBM_medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T06:43:17Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_5_lbm_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T06:43:17Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_5_LBM_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:38:15.036322Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_5_LBM_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch006/055/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T06:38:17.217550Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch006/055/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_5_LBM_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:38:19.862367Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_5_LBM_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:38:21.421480Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T06:43:17Z'
  support: supports
  summary: './data/merge_yaml/merged/1_5_LBM_medium.yaml:1:id: CultureMech:008247

    ./data/normalized_yaml/bacterial/1_5_lbm_medium.yaml:1:id: CultureMech:008247

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T06:43:17Z'
  support: supports
  summary: '{}'
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=893
  locator: Medium893 composition, pH and footnotes
  accessed_at: '2026-10-21T06:41:16.605634Z'
  support: supports
  summary: Whole recipe and seawater footnote inspected; natural and named commercial
    artificial alternatives remain distinct.
  quote: Filtered, aged seawater or artificial seawater (Daigo's Artificial Seawater
    SP**).
  snapshot_sha256: a3552963074145b47ce9c758e07e58c31ba225bd3ec2c0ae92cb53f97f282cf9
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1688
  locator: meta; components[0]; comments
  accessed_at: '2026-10-21T06:41:11.830457Z'
  support: supports
  summary: Complete source entry retains original NBRC accession, pH and seawater
    footnotes.
  snapshot_sha256: ff80c0cae39bc7cab0533dd087a7b2648c5e2724a0edf41ab4f1fef4310aca8b
- evidence_id: stock-api
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/1801
  locator: data.id; data.name; data.recipe; data.steps
  accessed_at: '2026-10-21T06:41:11.067691Z'
  support: supports
  summary: Linked solution identity resolves, but its generic salt preparation is
    not identified by the NBRC source as the prescribed seawater alternative.
  snapshot_sha256: d1269f65c0917a49e9c707b4f2032533a4e059139a2353fd7e43e37b0a28bbbc
- evidence_id: stock-local
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_1801_Seawater.yaml
  locator: Whole referenced stock and index entry; source hash captured
  accessed_at: '2026-10-21T06:43:17Z'
  support: context_only
  summary: The index resolves solution1801 to CultureMech:011231. Salt-row evidence
    matches the live provider JSON exactly; the water row is incorrectly encoded as
    a percentage and the placeholder ingredients field is present. This bounded dependency
    check does not constitute a separate stock review.
- evidence_id: owner-agar
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Owner-added CHEBI:2509 label and obsolete status
  accessed_at: '2026-10-20T07:07:41.448510Z'
  support: supports
  summary: The maintained owner agar identifier resolves with a matching label; it
    is absent from the generated target.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: trace
  kind: validation
  reference: NBRC893/TOGO M1688 and maintained comparison
  locator: Three direct amounts; seawater addition; corrected owner fields
  accessed_at: '2026-10-21T06:43:17Z'
  support: context_only
  summary: '{"direct": [{"index": 0, "source": {"amount": 15, "unit": "g"}, "target":
    {"value": "15", "unit": "G_PER_L"}}, {"index": 1, "source": {"amount": 1, "unit":
    "g"}, "target": {"value": "1", "unit": "G_PER_L"}}, {"index": 2, "source": {"amount":
    2, "unit": "g"}, "target": {"value": "2", "unit": "G_PER_L"}}], "source_seawater":
    {"amount": 1, "unit": "L"}, "target_solution": {"preferred_term": "Seawater*",
    "term": {"id": "mediadive.solution:1801", "label": "Seawater"}, "concentration":
    {"value": "1", "unit": "G_PER_L"}, "notes": "See mediadive_1801_Seawater.yaml
    for composition", "name": "Unknown solution"}, "owner_ph": 7.0, "owner_agar_term":
    {"id": "CHEBI:2509", "label": "agar"}, "stock_salt_evidence_matches_live_provider":
    true}'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008247
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '0 primary CHEBI identities resolve with matching labels; 0 of 0 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:008247
  evidence_ids:
  - record
  - mim
  details: 3 direct ingredient instances; primary coverage 0/3 (0.00%), verified secondary
    coverage 0/3 (0.00%). Percentages use a 0–100 linkage scale, not a scientific
    correctness score. Complex mixtures without asserted IDs remain ungrounded rather
    than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Medium accession and seawater alternatives
  outcome: concern
  summary: The medium accession resolves correctly. The source allows filtered aged
    seawater or a named commercial artificial seawater; it does not establish equivalence
    to the linked generic MediaDive sea-salt solution. A matching broad name cannot
    verify a stock substitution.
  target_ids:
  - CultureMech:008247
  evidence_ids:
  - record
  - owner-0
  - id-search
  - nbrc
  - togo
  - stock-api
  - stock-local
- assessment_id: amount-0
  area: quantity
  topic: ingredients[0].concentration
  outcome: supported
  summary: 'verified nominal recipe amount: source gram mass agrees on the stated
    one-liter seawater basis. Source brand qualifiers remain present; the agar amount
    is conditional. No final measured volume is inferred.'
  target_ids:
  - CultureMech:008247
  evidence_ids:
  - record
  - nbrc
  - togo
  - trace
- assessment_id: amount-1
  area: quantity
  topic: ingredients[1].concentration
  outcome: supported
  summary: 'verified nominal recipe amount: source gram mass agrees on the stated
    one-liter seawater basis. Source brand qualifiers remain present; the agar amount
    is conditional. No final measured volume is inferred.'
  target_ids:
  - CultureMech:008247
  evidence_ids:
  - record
  - nbrc
  - togo
  - trace
- assessment_id: amount-2
  area: quantity
  topic: ingredients[2].concentration
  outcome: supported
  summary: 'verified nominal recipe amount: source gram mass agrees on the stated
    one-liter seawater basis. Source brand qualifiers remain present; the agar amount
    is conditional. No final measured volume is inferred.'
  target_ids:
  - CultureMech:008247
  evidence_ids:
  - record
  - nbrc
  - togo
  - trace
- assessment_id: seawater-dose
  area: quantity
  topic: solutions[0].concentration
  outcome: concern
  summary: 'correct: the source liter volume is recast as G_PER_L. No seawater density
    or justification for a mass conversion is provided.'
  target_ids:
  - CultureMech:008247
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - trace
- assessment_id: nested-stock
  area: quantity
  topic: Referenced stock composition and evidence
  outcome: concern
  summary: The generic stock salt amount matches the provider within that stock. Its
    water value represents milliliters upstream, not the local percentage encoding.
    These facts do not establish any concentration in NBRC893 because the link itself
    lacks source support. No inherited salt contribution is calculated.
  target_ids:
  - CultureMech:008247
  evidence_ids:
  - stock-api
  - stock-local
  - trace
- assessment_id: generated-drift
  area: completeness
  topic: Maintained pH, agar grounding and provenance
  outcome: concern
  summary: The owner now preserves source pH, agar grounding, source notes and later
    curation provenance that the generated record omits. These corrections are supported
    by source text and the ontology response. Other stock-unit and stock-identity
    problems remain in both layers.
  target_ids:
  - CultureMech:008247
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - owner-agar
  - trace
- assessment_id: classification
  area: scope
  topic: Conditional agar, mixtures and biological claims
  outcome: supported
  summary: COMPLEX/UNDEFINED is supported by undefined extracts and seawater. SOLID_AGAR
    is compatible with choosing the source optional-agar branch; preserve that branch
    condition and do not assert every preparation is solid. No organism-specific growth
    assertion is made.
  target_ids:
  - CultureMech:008247
  evidence_ids:
  - record
  - nbrc
  - togo
- assessment_id: provenance
  area: evidence
  topic: Placeholder name and source evidence
  outcome: concern
  summary: Unknown solution is a placeholder despite a preferred term. Source notes/references
    and curation events do not provide narrow quantity evidence. Target reference
    validation inspected zero excerpts.
  target_ids:
  - CultureMech:008247
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - validate-references
  - trace
findings:
- finding_id: f1
  issue_key: CM008247-unsupported-seawater-link
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Generic seawater stock is not verified as the source material
  description: The resolvable generic salt solution is not established as either source-prescribed
    seawater alternative. Its broad label cannot justify replacing the original material.
  target_ids:
  - CultureMech:008247
  field_paths:
  - solutions[0].term
  - solutions[0].notes
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - stock-api
  - stock-local
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_5_lbm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM008247-seawater-volume-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Seawater volume is encoded as a mass concentration
  description: The source liter value is labeled G_PER_L in target and owner without
    density evidence.
  target_ids:
  - CultureMech:008247
  field_paths:
  - solutions[0].concentration
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - trace
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_5_lbm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM008247-generated-corrections-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated output lacks maintained source corrections
  description: Supported owner pH, agar grounding and later curation provenance are
    absent from the generated target.
  target_ids:
  - CultureMech:008247
  field_paths:
  - ph_value
  - ingredients[0].term
  - ingredients[0].mediaingredientmech_chebi_term
  - curation_history
  - references
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - owner-agar
  - trace
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_5_lbm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: CM008247-placeholder-and-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Solution placeholder and narrow evidence need follow-up
  description: The placeholder solution name and lack of scoped source evidence obscure
    an otherwise recoverable provenance chain.
  target_ids:
  - CultureMech:008247
  field_paths:
  - solutions[0].name
  - ingredients[*].evidence
  - references
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_5_lbm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.1
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Reconcile the seawater descriptor with the original alternatives and
    retain their preparation/product qualifiers. Remove or replace the unsupported
    link only through evidence-backed curation; do not transfer generic-stock quantities.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008247
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_5_lbm_medium.yaml
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
- action_id: a2
  description: Preserve the original volume and batch basis, with no assumed seawater
    density or inherited stock dilution.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008247
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_5_lbm_medium.yaml
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
- action_id: a3
  description: Retain verified owner corrections during separately authorized regeneration,
    then recheck that all intended fields and provenance survive.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008247
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_5_lbm_medium.yaml
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
- action_id: a4
  description: Resolve the descriptor name consistently with the verified material
    and attach narrow quantity/alternative-condition evidence.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008247
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_5_lbm_medium.yaml
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
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- Referenced stock was read for identity, relevant quantity evidence and dependency
  risk; it was not independently reviewed as a second target.
- No complete natural-seawater composition, commercial artificial-seawater formula,
  density, stock dilution, final-volume measurement or experimental growth is inferred.
tags:
- unreviewed-records
- batch-006
- generated-medium
```
