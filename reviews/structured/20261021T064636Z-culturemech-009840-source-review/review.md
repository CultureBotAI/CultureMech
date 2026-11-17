# Source and formulation review: 1_5_nutrient_agar_no_2 (CultureMech:009840)

- Review: 20261021T064636Z-culturemech-009840-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T06:36:44Z
- Finished UTC: 2026-10-21T06:46:36Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M453 and MediaDive J453 agree on the collection accession and the four solute amounts. Water volume is encoded as mass, and the source pH range is omitted. Supplier qualifiers are preserved. The original JCM endpoint does not provide the recipe, so collection verification remains incomplete.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 58 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 006 selects ordinals 51-60 after five validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009840 | data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml | generated | 1_5_nutrient_agar_no_2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009840 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009840 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch006/058/strict.tsv |
| validate-terms | passed | True | CultureMech:009840 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009840 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009840 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Inspect original JCM453 recipe | unavailable | True | CultureMech:009840 | Original collection endpoint returns no recipe; two provider representations remain available for bounded comparison. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009840.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:009840.

3 primary CHEBI identities resolve with matching labels; 3 of 3 current secondary keys have live pinned-index rows. Unresolved keys: [].

5 direct ingredient instances; primary coverage 3/5 (60.00%), verified secondary coverage 3/5 (60.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Accession and owner

identity: supported. Targets: CultureMech:009840.

The target and one normalized owner identify TOGO M453, explicitly linked to JCM453. MediaDive corroborates that accession; direct original-collection verification is unavailable. No similarly named medium is substituted.

### ingredients[0].concentration

quantity: concern. Targets: CultureMech:009840.

correct: source water volume is represented as mass concentration without density evidence.

### ingredients[1].concentration

quantity: supported. Targets: CultureMech:009840.

verified against providers: numeric gram amount agrees with TOGO and the provider-declared per-liter basis in MediaDive. This is not original-collection or experimental final-volume confirmation.

### ingredients[2].concentration

quantity: supported. Targets: CultureMech:009840.

verified against providers: numeric gram amount agrees with TOGO and the provider-declared per-liter basis in MediaDive. This is not original-collection or experimental final-volume confirmation.

### ingredients[3].concentration

quantity: supported. Targets: CultureMech:009840.

verified against providers: numeric gram amount agrees with TOGO and the provider-declared per-liter basis in MediaDive. This is not original-collection or experimental final-volume confirmation.

### ingredients[4].concentration

quantity: supported. Targets: CultureMech:009840.

verified against providers: numeric gram amount agrees with TOGO and the provider-declared per-liter basis in MediaDive. This is not original-collection or experimental final-volume confirmation.

### Source pH range

completeness: concern. Targets: CultureMech:009840.

TOGO supplies a pH range and adjustment instruction, matching the MediaDive preparation. Neither local record preserves it. MediaDive also carries a scalar metadata value; preserve the original range context rather than choosing a midpoint as a new precise claim.

### Ingredient identities and supplier qualifiers

grounding: supported. Targets: CultureMech:009840.

Three asserted chemical/material IDs and secondary keys resolve. The two undefined ingredients remain named mixtures with BD-Difco qualifiers retained; no exact product catalog or pure-molecule identity is inferred. Direct-instance primary and secondary linkage are each 3/5 (60%), not scientific-accuracy metrics.

### Composition, state and biological scope

scope: supported. Targets: CultureMech:009840.

COMPLEX/UNDEFINED and SOLID_AGAR agree with provider extracts and gelling agent. Imported notes are source annotations rather than experimental role evidence. Generic bacterial cultivation makes no strain-specific growth claim.

### History and narrow evidence

evidence: concern. Targets: CultureMech:009840.

Import and merge histories trace provenance, but neither record carries claim-level quantity or preparation evidence. Target reference validation checked zero excerpts.

## Findings

### f1: Water volume is encoded as mass concentration

major / open / confirmed; issue key: CM009840-water-volume-unit.

The source liter amount has been given G_PER_L units without density evidence.

### f2: Source pH range is absent

major / open / confirmed; issue key: CM009840-ph-range-omitted.

Both provider representations preserve a pH adjustment range that is missing locally.

### f3: Quantity and preparation evidence is missing

minor / open / confirmed; issue key: CM009840-claim-evidence-gap.

Source notes and history do not provide narrow support for individual quantities or pH context.

## Recommended Actions And Acceptance Checks

### a1

Retain original water volume and batch basis; do not justify the import with a guessed density.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Represent the verified range and its preparation scope with provider attribution. Do not replace it with a newly inferred exact value.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Attach scoped evidence to supported provider claims and corrected units, explicitly preserving the original-collection access limitation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M453_1_5_Nutrient_Agar_NO._2.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch006/058/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch006/058/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml:1:id: CultureMech:009840<br>./data/normalized_yaml/bacterial/TOGO_M453_1_5_Nutrient_Agar_NO._2.yaml:1:id: CultureMech:009840<br> |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15377 resolves to water and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:2509 resolves to agar and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M453; meta; components[0]; comments | supports | Complete source identity, five components, pH range and adjustment comment inspected. |
| api | https://mediadive.dsmz.de/rest/medium/J453; data.medium; data.solutions[0] | supports | Provider accession, ingredient attributes, declared volume and amounts inspected; its preparation preserves the pH range. |
| jcm-access | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=453; Body returned for exact GRMD453 lookup | context_only | HTTP200 response says Nothing found; no original collection recipe was inspected. This is bounded endpoint unavailability, not proof that the historical recipe did not exist. |
| trace | Whole target/owner and TOGO source comparison; All five direct rows and source annotations | supports | [{"index": 0, "source_unit": "L", "source_amount": 1, "target_concentration": {"value": "1", "unit": "G_PER_L"}, "annotations_match": true}, {"index": 1, "source_unit": "g", "source_amount": 1, "target_concentration": {"value": "1", "unit": "G_PER_L"}, "annotations_match": true}, {"index": 2, "source_unit": "g", "source_amount": 15, "target_concentration": {"value": "15", "unit": "G_PER_L"}, "annotations_match": true}, {"index": 3, "source_unit": "g", "source_amount": 2, "target_concentration": {"value": "2", "unit": "G_PER_L"}, "annotations_match": true}, {"index": 4, "source_unit": "g", "source_amount": 2, "target_concentration": {"value": "2", "unit": "G_PER_L"}, "annotations_match": true}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Completion is partial because original JCM453 recipe access was unavailable. Agreement between database providers is not independent inspection of that primary recipe.
- No additional sterilization procedure, adjustment dose, measured final volume, organism growth claim or optimization is inferred.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T064636Z-culturemech-009840-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_5_nutrient_agar_no_2 (CultureMech:009840)'
started_at: '2026-10-21T06:36:44Z'
finished_at: '2026-10-21T06:46:36Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify the assessed recipe bytes.
    This is an independent agent review of captured local inputs and inspected primary/database
    sources, not experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: TOGO M453 and MediaDive J453 agree on the collection accession and the four
  solute amounts. Water volume is encoded as mass, and the source pH range is omitted.
  Supplier qualifiers are preserved. The original JCM endpoint does not provide the
  recipe, so collection verification remains incomplete.
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
  - path: data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml
    sha256: a67d39b7ed23595bfdc85d89113a32d4e9fe227bdff272cf2d79496d10fecb8e
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M453_1_5_Nutrient_Agar_NO._2.yaml
    sha256: 7eb3c917c5926edeeab430f95a195eec031cc8bcdb7ed6bd8c29c9938e9fdb30
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
  selection: Record 58 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 006 selects ordinals 51-60 after five
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009840
targets:
- target_id: CultureMech:009840
  path: data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml
  label: 1_5_nutrient_agar_no_2
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M453_1_5_Nutrient_Agar_NO._2.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch006/058/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch006/058/strict.tsv"
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009840
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
  - CultureMech:009840
- check_id: original-collection
  name: Inspect original JCM453 recipe
  required: true
  status: unavailable
  summary: Original collection endpoint returns no recipe; two provider representations
    remain available for bounded comparison.
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - jcm-access
  - togo
  - api
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T06:46:34Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M453_1_5_Nutrient_Agar_NO._2.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T06:46:34Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:38:39.131766Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch006/058/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T06:38:40.879389Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch006/058/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:38:42.855395Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:38:44.031120Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T06:46:34Z'
  support: supports
  summary: './data/merge_yaml/merged/1_5_nutrient_agar_no_2__b809c568.yaml:1:id: CultureMech:009840

    ./data/normalized_yaml/bacterial/TOGO_M453_1_5_Nutrient_Agar_NO._2.yaml:1:id:
    CultureMech:009840

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
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:07:41.448510Z'
  support: supports
  summary: CHEBI:2509 resolves to agar and is not obsolete. This verifies the asserted
    generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond
    the record is inferred.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:11:31.325976Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T06:46:34Z'
  support: supports
  summary: '{"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M453
  locator: meta; components[0]; comments
  accessed_at: '2026-10-21T06:41:12.059714Z'
  support: supports
  summary: Complete source identity, five components, pH range and adjustment comment
    inspected.
  snapshot_sha256: dfe84d7b0188c0572e7c4c3a11e05d4f5872af80fd465ce63a60de926978d5e7
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J453
  locator: data.medium; data.solutions[0]
  accessed_at: '2026-10-21T06:41:11.066663Z'
  support: supports
  summary: Provider accession, ingredient attributes, declared volume and amounts
    inspected; its preparation preserves the pH range.
  snapshot_sha256: 26d3aa0b8a3590ae37a442a1913d4b67156fe41622ef586c8f5d7c4933db9132
- evidence_id: jcm-access
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=453
  locator: Body returned for exact GRMD453 lookup
  accessed_at: '2026-10-21T06:41:16.059704Z'
  support: context_only
  summary: HTTP200 response says Nothing found; no original collection recipe was
    inspected. This is bounded endpoint unavailability, not proof that the historical
    recipe did not exist.
  snapshot_sha256: 642eb54c6ca393babc22fc835b9f06cb42d5d7c8b50eb60058861030fb4ffeea
- evidence_id: trace
  kind: validation
  reference: Whole target/owner and TOGO source comparison
  locator: All five direct rows and source annotations
  accessed_at: '2026-10-21T06:46:34Z'
  support: supports
  summary: '[{"index": 0, "source_unit": "L", "source_amount": 1, "target_concentration":
    {"value": "1", "unit": "G_PER_L"}, "annotations_match": true}, {"index": 1, "source_unit":
    "g", "source_amount": 1, "target_concentration": {"value": "1", "unit": "G_PER_L"},
    "annotations_match": true}, {"index": 2, "source_unit": "g", "source_amount":
    15, "target_concentration": {"value": "15", "unit": "G_PER_L"}, "annotations_match":
    true}, {"index": 3, "source_unit": "g", "source_amount": 2, "target_concentration":
    {"value": "2", "unit": "G_PER_L"}, "annotations_match": true}, {"index": 4, "source_unit":
    "g", "source_amount": 2, "target_concentration": {"value": "2", "unit": "G_PER_L"},
    "annotations_match": true}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '3 primary CHEBI identities resolve with matching labels; 3 of 3 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - record
  - mim
  - chebi15377
  - chebi2509
  - chebi26710
  details: 5 direct ingredient instances; primary coverage 3/5 (60.00%), verified
    secondary coverage 3/5 (60.00%). Percentages use a 0–100 linkage scale, not a
    scientific correctness score. Complex mixtures without asserted IDs remain ungrounded
    rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Accession and owner
  outcome: supported
  summary: The target and one normalized owner identify TOGO M453, explicitly linked
    to JCM453. MediaDive corroborates that accession; direct original-collection verification
    is unavailable. No similarly named medium is substituted.
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - record
  - owner-0
  - id-search
  - togo
  - api
  - jcm-access
- assessment_id: amount-0
  area: quantity
  topic: ingredients[0].concentration
  outcome: concern
  summary: 'correct: source water volume is represented as mass concentration without
    density evidence.'
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - record
  - togo
  - api
  - trace
- assessment_id: amount-1
  area: quantity
  topic: ingredients[1].concentration
  outcome: supported
  summary: 'verified against providers: numeric gram amount agrees with TOGO and the
    provider-declared per-liter basis in MediaDive. This is not original-collection
    or experimental final-volume confirmation.'
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - record
  - togo
  - api
  - trace
- assessment_id: amount-2
  area: quantity
  topic: ingredients[2].concentration
  outcome: supported
  summary: 'verified against providers: numeric gram amount agrees with TOGO and the
    provider-declared per-liter basis in MediaDive. This is not original-collection
    or experimental final-volume confirmation.'
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - record
  - togo
  - api
  - trace
- assessment_id: amount-3
  area: quantity
  topic: ingredients[3].concentration
  outcome: supported
  summary: 'verified against providers: numeric gram amount agrees with TOGO and the
    provider-declared per-liter basis in MediaDive. This is not original-collection
    or experimental final-volume confirmation.'
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - record
  - togo
  - api
  - trace
- assessment_id: amount-4
  area: quantity
  topic: ingredients[4].concentration
  outcome: supported
  summary: 'verified against providers: numeric gram amount agrees with TOGO and the
    provider-declared per-liter basis in MediaDive. This is not original-collection
    or experimental final-volume confirmation.'
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - record
  - togo
  - api
  - trace
- assessment_id: pH
  area: completeness
  topic: Source pH range
  outcome: concern
  summary: TOGO supplies a pH range and adjustment instruction, matching the MediaDive
    preparation. Neither local record preserves it. MediaDive also carries a scalar
    metadata value; preserve the original range context rather than choosing a midpoint
    as a new precise claim.
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
- assessment_id: materials
  area: grounding
  topic: Ingredient identities and supplier qualifiers
  outcome: supported
  summary: Three asserted chemical/material IDs and secondary keys resolve. The two
    undefined ingredients remain named mixtures with BD-Difco qualifiers retained;
    no exact product catalog or pure-molecule identity is inferred. Direct-instance
    primary and secondary linkage are each 3/5 (60%), not scientific-accuracy metrics.
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - record
  - mim
  - chebi15377
  - chebi26710
  - chebi2509
  - togo
  - api
- assessment_id: classification
  area: scope
  topic: Composition, state and biological scope
  outcome: supported
  summary: COMPLEX/UNDEFINED and SOLID_AGAR agree with provider extracts and gelling
    agent. Imported notes are source annotations rather than experimental role evidence.
    Generic bacterial cultivation makes no strain-specific growth claim.
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - record
  - togo
  - api
  - trace
- assessment_id: evidence
  area: evidence
  topic: History and narrow evidence
  outcome: concern
  summary: Import and merge histories trace provenance, but neither record carries
    claim-level quantity or preparation evidence. Target reference validation checked
    zero excerpts.
  target_ids:
  - CultureMech:009840
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  - validate-references
findings:
- finding_id: f1
  issue_key: CM009840-water-volume-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water volume is encoded as mass concentration
  description: The source liter amount has been given G_PER_L units without density
    evidence.
  target_ids:
  - CultureMech:009840
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  - trace
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M453_1_5_Nutrient_Agar_NO._2.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM009840-ph-range-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source pH range is absent
  description: Both provider representations preserve a pH adjustment range that is
    missing locally.
  target_ids:
  - CultureMech:009840
  field_paths:
  - ph_value
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M453_1_5_Nutrient_Agar_NO._2.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM009840-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Quantity and preparation evidence is missing
  description: Source notes and history do not provide narrow support for individual
    quantities or pH context.
  target_ids:
  - CultureMech:009840
  field_paths:
  - ingredients[*].evidence
  - references
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M453_1_5_Nutrient_Agar_NO._2.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Retain original water volume and batch basis; do not justify the import
    with a guessed density.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009840
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M453_1_5_Nutrient_Agar_NO._2.yaml
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
  description: Represent the verified range and its preparation scope with provider
    attribution. Do not replace it with a newly inferred exact value.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009840
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M453_1_5_Nutrient_Agar_NO._2.yaml
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
  description: Attach scoped evidence to supported provider claims and corrected units,
    explicitly preserving the original-collection access limitation.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009840
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M453_1_5_Nutrient_Agar_NO._2.yaml
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
- Completion is partial because original JCM453 recipe access was unavailable. Agreement
  between database providers is not independent inspection of that primary recipe.
- No additional sterilization procedure, adjustment dose, measured final volume, organism
  growth claim or optimization is inferred.
tags:
- unreviewed-records
- batch-006
- generated-medium
```
