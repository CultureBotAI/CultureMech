# Source and formulation review: 1_tryptone_agar (CultureMech:009733)

- Review: 20261021T065959Z-culturemech-009733-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T06:57:05Z
- Finished UTC: 2026-10-21T06:59:59Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M353 and the primary JCM359 recipe agree on supplied products and solute amounts. The target retains a water volume-to-mass error and omits pH, preparation, agar grounding and source-duplicate context already corrected or documented in its maintained owner.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 62; batch 007 item 2 of 10, selected in Python lexicographic repository-relative path order from the current uncovered merged corpus. The prior six validated batch lists contain 60 distinct merged target paths. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c has 40 validated baseline bundles covering 2 current merged paths. The union with prior batches covers 62 of 6320 current merged paths before this batch. This target path occurs in neither set. Task ordinals continue the saved-review sequence, not global path ranks after upstream corpus or coverage changes. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009733 | data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml | generated | 1_tryptone_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009733 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009733 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch007/062/strict.tsv |
| validate-terms | passed | True | CultureMech:009733 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009733 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009733 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009733.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:009733.

1 primary CHEBI identities resolve with matching labels; 1 of 1 current secondary keys have live pinned-index rows. Unresolved keys: [].

3 direct ingredient instances; CHEBI-primary instance linkage 1/3 (33.33%), verified secondary coverage 1/3 (33.33%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Source accession and preserved product specificity

identity: supported. Targets: CultureMech:009733.

The generated record identifies TOGO M353 and its JCM359 original source. Both source-disclosed supplied-product qualifiers survive. The maintained source-duplicate relationship resolves reciprocally to the same collection accession.

### ingredients[1].concentration

quantity: supported. Targets: CultureMech:009733.

verified: source mass amount and provider-declared per-liter value agree; retain the source batch-water context rather than claiming an independently measured final volume.

### ingredients[2].concentration

quantity: supported. Targets: CultureMech:009733.

verified: source mass amount and provider-declared per-liter value agree; retain the source batch-water context rather than claiming an independently measured final volume.

### ingredients[0].concentration

quantity: concern. Targets: CultureMech:009733.

correct: literal source water volume became mass concentration without density support. The maintained owner already restores a literal L amount; regenerate only after source/owner verification.

### Maintained pH, preparation and relationship fields

completeness: concern. Targets: CultureMech:009733.

The owner preserves source pH, adjustment and properly scoped JCM collection default, plus agar mapping and reciprocal source-duplicate context. All are missing from the generated target, which predates the owner curation event.

### Composition and physical state

scope: supported. Targets: CultureMech:009733.

COMPLEX/UNDEFINED and SOLID_AGAR agree with source tryptone and agar. Notes reproduce source annotations without experimental role claims. No organism-specific growth claim or incubation condition is inferred.

### Current direct-ingredient linkage

grounding: supported. Targets: CultureMech:009733.

The target has one verified primary and secondary CHEBI key among three direct instances: 1/3 (33.33%) each, a 0–100 linkage metric. The owner additionally maps agar; the supplied tryptone mixture remains intentionally unmapped. Neither its absence nor a low score justifies assigning a pure molecule.

### History and narrow claim support

evidence: concern. Targets: CultureMech:009733.

Histories parse with timezones. The owner has references and source-specific notes but lacks narrow ingredient evidence; target reference validation examined zero excerpts.

## Findings

### f1: Water volume is still represented as mass concentration

major / open / confirmed; issue key: CM009733-water-volume-unit.

The generated water field asserts G_PER_L for a source liter amount; the maintained owner has already changed it to a literal batch-volume unit.

### f2: Generated record lacks maintained source-backed fields

major / open / confirmed; issue key: CM009733-stale-curated-fields.

Source pH, preparation context, agar mapping, references and the reciprocal source-duplicate relationship are present in the owner but absent from the target.

### f3: Formulation claims lack narrow evidence

minor / open / confirmed; issue key: CM009733-narrow-evidence-gap.

References and history alone do not attach support to individual quantities, supplied products, water basis or preparation context.

## Recommended Actions And Acceptance Checks

### a1

Verify the owner correction against the original source and regenerate the derived record with the literal volume and batch scope preserved.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Review the maintained fields and regenerate the derived record. Preserve the collection-default exception and source-duplicate meaning without promoting unassessed growth claims.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Add scoped primary/provider evidence to supported claims in the owner before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch007/062/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch007/062/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml:1:id: CultureMech:009733<br>./data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml:1:id: CultureMech:009733<br> |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15377 resolves to water and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=359; GRMD359 table and default | supports | Entire original recipe and page default inspected, including product qualifiers, amounts, water basis, pH and collection-scoped default. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M353; meta; components[0]; comments | supports | Source identity, all three amounts/units, annotations and pH inspected. |
| api | https://mediadive.dsmz.de/rest/medium/J359; data.medium; data.solutions[0] | supports | Source identity, provider-declared solute concentrations, water and pH checked. |
| parent | data/normalized_yaml/bacterial/1_tryptone_agar.yaml; Entire maintained parent; reciprocal variant_children | supports | Parent ID/path resolves and its reciprocal child is this maintained TOGO record. Source-specific accession comparison supports the documented duplicate relationship; no new merge is proposed. |
| owner-agar | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Owner agar identity | supports | The owner agar ID resolves with its canonical label and nonobsolete status. This mapping is missing from the generated target. |
| context | Complete target, owner, parent and TOGO source; Three row comparisons; all history timestamp checks; reciprocal variant IDs | supports | {"row_trace": [{"field_path": "ingredients[0]", "source_amount": 1, "source_unit": "L", "local_concentration": {"value": "1", "unit": "G_PER_L"}, "annotations_retained": true}, {"field_path": "ingredients[1]", "source_amount": 15, "source_unit": "g", "local_concentration": {"value": "15", "unit": "G_PER_L"}, "annotations_retained": true}, {"field_path": "ingredients[2]", "source_amount": 10, "source_unit": "g", "local_concentration": {"value": "10", "unit": "G_PER_L"}, "annotations_retained": true}], "timezone_bearing_history_counts": [7, 7, 7], "reciprocal_variant_ids_verified": true} |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- This review is complete for the declared source/formulation scope; no experimental verification or exhaustive literature search is implied.
- The related maintained JCM parent is context only. Its separate KG assertion is outside this target, which asserts no kg_microbe_match.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T065959Z-culturemech-009733-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_tryptone_agar (CultureMech:009733)'
started_at: '2026-10-21T06:57:05Z'
finished_at: '2026-10-21T06:59:59Z'
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
summary: TOGO M353 and the primary JCM359 recipe agree on supplied products and solute
  amounts. The target retains a water volume-to-mass error and omits pH, preparation,
  agar grounding and source-duplicate context already corrected or documented in its
  maintained owner.
source:
  git_revision: 24a1d277eb7f0437af53af0d178a30f9bfa6374c
  state: working_tree
  inputs:
  - path: .claude/skills/audit-schema-gaps/SKILL.md
    sha256: 86467f280ecdd2d60531d3b2a9249d7a38efa4cfeab714d55421b9a62cfabb7d
    role: context
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
  - path: .claude/skills/schema-gap-analysis/SKILL.md
    sha256: 09665fe53584559e776f75ab41dfabd997eff0cac10bafcca0a721b678ccee93
    role: context
  - path: AGENTS.md
    sha256: 72737a531548de8636bcf70b972e71a7630a0e579215b6ded392d88d1b51a4fc
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
  - path: data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml
    sha256: 3018098e914cc924334ca7fd47757e11ca31430d71b8968f491dcfede7ac3ec6
    role: target
  - path: data/normalized_yaml/bacterial/1_tryptone_agar.yaml
    sha256: 8154c5ad1e1d8e2a57c1290de8ea388a035d7c13b0683b3e4f45557010eafa96
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml
    sha256: 60aabf4b95bba1107fd3f5ce00195b8b0dc413cfbaabe1dda1c9cc0bad8ddcd8
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
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
  - path: src/culturemech/fetch/togo_fetcher.py
    sha256: 7aac40fe1d47e30810ae0be02f6e369ddb9bf657d630072595c62f46fb0bf339
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
  selection: Task review 62; batch 007 item 2 of 10, selected in Python lexicographic
    repository-relative path order from the current uncovered merged corpus. The prior
    six validated batch lists contain 60 distinct merged target paths. Fresh origin/main
    at 24a1d277eb7f0437af53af0d178a30f9bfa6374c has 40 validated baseline bundles
    covering 2 current merged paths. The union with prior batches covers 62 of 6320
    current merged paths before this batch. This target path occurs in neither set.
    Task ordinals continue the saved-review sequence, not global path ranks after
    upstream corpus or coverage changes. This bundle selects only the named record;
    no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009733
targets:
- target_id: CultureMech:009733
  path: data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml
  label: 1_tryptone_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009733
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch007/062/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch007/062/strict.tsv"
  target_ids:
  - CultureMech:009733
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009733
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009733
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
  - CultureMech:009733
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T06:59:57Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T06:59:57Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:57:25.416880Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch007/062/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T06:57:28.806129Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch007/062/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:57:32.556638Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:57:35.010973Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T06:59:57Z'
  support: supports
  summary: './data/merge_yaml/merged/1_tryptone_agar__551e7d77.yaml:1:id: CultureMech:009733

    ./data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml:1:id: CultureMech:009733

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T04:00:00.223561Z'
  support: supports
  summary: CHEBI:15377 resolves to water and is not obsolete. This verifies the asserted
    generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond
    the record is inferred.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T06:59:57Z'
  support: supports
  summary: '{"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=359
  locator: GRMD359 table and default
  accessed_at: '2026-10-21T06:55:22.658404Z'
  support: supports
  summary: Entire original recipe and page default inspected, including product qualifiers,
    amounts, water basis, pH and collection-scoped default.
  quote: Distilled water 1.0 L Adjust pH to 7.0.
  snapshot_sha256: 362fd82527ba83f62033b006490d2649a8f1faaf821c4a7cdaa35bbc2556a18f
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M353
  locator: meta; components[0]; comments
  accessed_at: '2026-10-21T06:55:22.017802Z'
  support: supports
  summary: Source identity, all three amounts/units, annotations and pH inspected.
  snapshot_sha256: 3402b01ce7d43932f86d1064af40142a8eab74d6daf04202b9ea6b4c470ba495
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J359
  locator: data.medium; data.solutions[0]
  accessed_at: '2026-10-21T06:55:22.017539Z'
  support: supports
  summary: Source identity, provider-declared solute concentrations, water and pH
    checked.
  snapshot_sha256: d7f656d2212421f891224e8f26f7e7fa8ecc45365f0ec8b5d4a04f88450a3a7a
- evidence_id: parent
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_tryptone_agar.yaml
  locator: Entire maintained parent; reciprocal variant_children
  accessed_at: '2026-10-21T06:59:57Z'
  support: supports
  summary: Parent ID/path resolves and its reciprocal child is this maintained TOGO
    record. Source-specific accession comparison supports the documented duplicate
    relationship; no new merge is proposed.
- evidence_id: owner-agar
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Owner agar identity
  accessed_at: '2026-10-20T07:07:41.448510Z'
  support: supports
  summary: The owner agar ID resolves with its canonical label and nonobsolete status.
    This mapping is missing from the generated target.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: context
  kind: validation
  reference: Complete target, owner, parent and TOGO source
  locator: Three row comparisons; all history timestamp checks; reciprocal variant
    IDs
  accessed_at: '2026-10-21T06:59:57Z'
  support: supports
  summary: '{"row_trace": [{"field_path": "ingredients[0]", "source_amount": 1, "source_unit":
    "L", "local_concentration": {"value": "1", "unit": "G_PER_L"}, "annotations_retained":
    true}, {"field_path": "ingredients[1]", "source_amount": 15, "source_unit": "g",
    "local_concentration": {"value": "15", "unit": "G_PER_L"}, "annotations_retained":
    true}, {"field_path": "ingredients[2]", "source_amount": 10, "source_unit": "g",
    "local_concentration": {"value": "10", "unit": "G_PER_L"}, "annotations_retained":
    true}], "timezone_bearing_history_counts": [7, 7, 7], "reciprocal_variant_ids_verified":
    true}'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009733
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '1 primary CHEBI identities resolve with matching labels; 1 of 1 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:009733
  evidence_ids:
  - record
  - mim
  - chebi15377
  details: 3 direct ingredient instances; CHEBI-primary instance linkage 1/3 (33.33%),
    verified secondary coverage 1/3 (33.33%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Source accession and preserved product specificity
  outcome: supported
  summary: The generated record identifies TOGO M353 and its JCM359 original source.
    Both source-disclosed supplied-product qualifiers survive. The maintained source-duplicate
    relationship resolves reciprocally to the same collection accession.
  target_ids:
  - CultureMech:009733
  evidence_ids:
  - record
  - owner-0
  - id-search
  - jcm
  - togo
  - api
  - parent
  - context
- assessment_id: amount-1
  area: quantity
  topic: ingredients[1].concentration
  outcome: supported
  summary: 'verified: source mass amount and provider-declared per-liter value agree;
    retain the source batch-water context rather than claiming an independently measured
    final volume.'
  target_ids:
  - CultureMech:009733
  evidence_ids:
  - record
  - jcm
  - togo
  - api
  - context
- assessment_id: amount-2
  area: quantity
  topic: ingredients[2].concentration
  outcome: supported
  summary: 'verified: source mass amount and provider-declared per-liter value agree;
    retain the source batch-water context rather than claiming an independently measured
    final volume.'
  target_ids:
  - CultureMech:009733
  evidence_ids:
  - record
  - jcm
  - togo
  - api
  - context
- assessment_id: water
  area: quantity
  topic: ingredients[0].concentration
  outcome: concern
  summary: 'correct: literal source water volume became mass concentration without
    density support. The maintained owner already restores a literal L amount; regenerate
    only after source/owner verification.'
  target_ids:
  - CultureMech:009733
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - context
- assessment_id: freshness
  area: completeness
  topic: Maintained pH, preparation and relationship fields
  outcome: concern
  summary: The owner preserves source pH, adjustment and properly scoped JCM collection
    default, plus agar mapping and reciprocal source-duplicate context. All are missing
    from the generated target, which predates the owner curation event.
  target_ids:
  - CultureMech:009733
  evidence_ids:
  - record
  - owner-0
  - parent
  - jcm
  - togo
  - api
  - context
  - owner-agar
- assessment_id: classification
  area: scope
  topic: Composition and physical state
  outcome: supported
  summary: COMPLEX/UNDEFINED and SOLID_AGAR agree with source tryptone and agar. Notes
    reproduce source annotations without experimental role claims. No organism-specific
    growth claim or incubation condition is inferred.
  target_ids:
  - CultureMech:009733
  evidence_ids:
  - record
  - jcm
  - togo
  - context
- assessment_id: linkage
  area: grounding
  topic: Current direct-ingredient linkage
  outcome: supported
  summary: 'The target has one verified primary and secondary CHEBI key among three
    direct instances: 1/3 (33.33%) each, a 0–100 linkage metric. The owner additionally
    maps agar; the supplied tryptone mixture remains intentionally unmapped. Neither
    its absence nor a low score justifies assigning a pure molecule.'
  target_ids:
  - CultureMech:009733
  evidence_ids:
  - record
  - owner-0
  - mim
  - chebi15377
  - owner-agar
- assessment_id: evidence
  area: evidence
  topic: History and narrow claim support
  outcome: concern
  summary: Histories parse with timezones. The owner has references and source-specific
    notes but lacks narrow ingredient evidence; target reference validation examined
    zero excerpts.
  target_ids:
  - CultureMech:009733
  evidence_ids:
  - record
  - owner-0
  - context
  - validate-references
findings:
- finding_id: f1
  issue_key: CM009733-water-volume-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water volume is still represented as mass concentration
  description: The generated water field asserts G_PER_L for a source liter amount;
    the maintained owner has already changed it to a literal batch-volume unit.
  target_ids:
  - CultureMech:009733
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM009733-stale-curated-fields
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated record lacks maintained source-backed fields
  description: Source pH, preparation context, agar mapping, references and the reciprocal
    source-duplicate relationship are present in the owner but absent from the target.
  target_ids:
  - CultureMech:009733
  field_paths:
  - ph_value
  - preparation_steps
  - sterilization
  - ingredients[1].term
  - parent_media
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - parent
  - jcm
  - togo
  - api
  - context
  - owner-agar
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM009733-narrow-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Formulation claims lack narrow evidence
  description: References and history alone do not attach support to individual quantities,
    supplied products, water basis or preparation context.
  target_ids:
  - CultureMech:009733
  field_paths:
  - ingredients[*].evidence
  - evidence
  - references
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - api
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Verify the owner correction against the original source and regenerate
    the derived record with the literal volume and batch scope preserved.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009733
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml
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
  description: Review the maintained fields and regenerate the derived record. Preserve
    the collection-default exception and source-duplicate meaning without promoting
    unassessed growth claims.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009733
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml
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
  description: Add scoped primary/provider evidence to supported claims in the owner
    before regeneration.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009733
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml
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
- This review is complete for the declared source/formulation scope; no experimental
  verification or exhaustive literature search is implied.
- The related maintained JCM parent is context only. Its separate KG assertion is
  outside this target, which asserts no kg_microbe_match.
tags:
- unreviewed-records
- batch-007
- generated-medium
```
