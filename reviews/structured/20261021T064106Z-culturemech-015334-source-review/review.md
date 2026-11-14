# Source and formulation review: 1_2_tryptic_soy_broth_anaerobic (CultureMech:015334)

- Review: 20261021T064106Z-culturemech-015334-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T06:36:39Z
- Finished UTC: 2026-10-21T06:41:06Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 1205 identity, all five direct amounts, pH and complete preparation are supported. The commercial premix is correctly preserved. Source supplier and water/batch context are omitted; three maintained concentration evidence objects and their later provenance are absent from the generated target.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 53 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 006 selects ordinals 51-60 after five validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:015334 | data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml | generated | 1_2_tryptic_soy_broth_anaerobic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:015334 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:015334 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch006/053/strict.tsv |
| validate-terms | passed | True | CultureMech:015334 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:015334 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:015334 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:015334.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:015334.

3 primary CHEBI identities resolve with matching labels; 3 of 3 current secondary keys have live pinned-index rows. Unresolved keys: [].

5 direct ingredient instances; primary coverage 3/5 (60.00%), verified secondary coverage 3/5 (60.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Source accession and maintained owner

identity: supported. Targets: CultureMech:015334.

CultureMech:015334 identifies DSMZ1205 through mediadive.medium:1205 and one specialized normalized owner. The source is a liquid broth with an intact commercial product boundary. No sibling constituent expansion is imported.

### ingredients[0].concentration

quantity: supported. Targets: CultureMech:015334.

verified: exact source row, original gram amount and provider-declared per-liter value agree. The commercial product is retained as a mixture; no unverified internal constituent calculation is required.

### ingredients[1].concentration

quantity: supported. Targets: CultureMech:015334.

verified: exact source row, original gram amount and provider-declared per-liter value agree. The commercial product is retained as a mixture; no unverified internal constituent calculation is required.

### ingredients[2].concentration

quantity: supported. Targets: CultureMech:015334.

verified: exact source row, original gram amount and provider-declared per-liter value agree. The commercial product is retained as a mixture; no unverified internal constituent calculation is required.

### ingredients[3].concentration

quantity: supported. Targets: CultureMech:015334.

verified: exact source row, original gram amount and provider-declared per-liter value agree. The commercial product is retained as a mixture; no unverified internal constituent calculation is required.

### ingredients[4].concentration

quantity: supported. Targets: CultureMech:015334.

verified: exact source row, original gram amount and provider-declared per-liter value agree. The commercial product is retained as a mixture; no unverified internal constituent calculation is required.

### Preparation, gas, stocks and pH

completeness: supported. Targets: CultureMech:015334.

The full preparation text equals the provider text and preserves source staging, acid adjustment, gas and separately sterilized stock-addition context. The numeric pH matches the source. Stock strengths, stock volumes and acid dose are not supplied, and the record does not invent them.

### Product supplier and water basis

completeness: concern. Targets: CultureMech:015334.

The source product has a BD BACTO qualifier, and the water volume and declared main volume are explicit upstream. The local product name and per-liter values omit those formulation details. A precise catalog is not needed to retain the source product as supplied; it must not be guessed.

### Chemical identity and undefined mixtures

grounding: supported. Targets: CultureMech:015334.

NaCl, D-glucose and DL-dithiothreitol resolve with matching labels and live secondary keys. The two undefined mixture ingredients remain ungrounded rather than being forced into pure-chemical identities. Primary and secondary linkage are each 3/5 (60%) on a 0–100 scale; this is not a scientific-accuracy score.

### Composition, physical state and category

scope: supported. Targets: CultureMech:015334.

COMPLEX/UNDEFINED and LIQUID agree with the source premix/extract and absence of gelling agent. Specialized is a broad organizational category for this anaerobic formulation; no specific organism claim creates a taxonomic conflict. Generic cultivation is not evidence of strain-specific performance.

### Maintained evidence versus generated target

evidence: concern. Targets: CultureMech:015334.

Three owner ingredient evidence objects match the current provider rows exactly after JSON parsing, and correctly limit their amount claims to the provider-declared main-recipe basis. They and the later owner curation event/reference are missing from the older generated output. Premix and DTT amounts still lack narrow owner evidence. The target reference gate checked zero excerpts.

## Findings

### f1: Supplier and water/batch context are omitted

major / open / confirmed; issue key: CM015334-source-product-context.

The source product qualifier and original water volume are missing from both local records, limiting faithful interpretation of the correctly retained commercial ingredient and per-liter amounts.

### f2: Generated record omits maintained concentration evidence

minor / open / confirmed; issue key: CM015334-generated-evidence-gap.

The owner contains three verified concentration evidence objects and a later provenance event absent from the target; the other two direct amounts lack narrow owner evidence.

## Recommended Actions And Acceptance Checks

### a1

Retain the verified BD BACTO qualifier and source water/batch context in the maintained owner. Preserve the premix boundary and do not infer a catalog or internal formula.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve verified owner evidence during separately authorized regeneration and add narrow support for the remaining product and DTT amounts. Check the resulting target contains the intended evidence and later provenance.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch006/053/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch006/053/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml:1:id: CultureMech:015334<br>./data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml:1:id: CultureMech:015334<br> |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17634 resolves to D-glucose and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi18320 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18320; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:18320 resolves to 1,4-dithiothreitol and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17634": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:18320": [{"label": "DL-Dithiothreitol", "match_type": "preferred_term", "identifier": "CHEBI:18320", "preferred_term": "DL-Dithiothreitol", "ontology_id": "CHEBI:18320", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| dsmz | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1205.pdf; Page 1 formulation and preparation | supports | Full primary collection formula and preparation inspected; source product remains a premix. |
| api | https://mediadive.dsmz.de/rest/medium/1205; data.medium; data.solutions[0] | supports | All five non-water source rows, declared main volume, pH and preparation inspected. |
| render | https://bacmedia.dsmz.de/pdf/1205; Page 1 | supports | Source rendering confirms declared volume, pH and preparation context. |
| trace | Target, maintained owner and live provider comparison; All five quantities; exact preparation text; all three maintained evidence snippets parsed as JSON | supports | {"accessed_at": "2026-10-21T06:40:43.849832+00:00", "all_five_amounts": [{"index": 0, "concentration_matches_provider": true, "maintained_evidence_objects": 0, "generated_evidence_objects": 0}, {"index": 1, "concentration_matches_provider": true, "maintained_evidence_objects": 1, "generated_evidence_objects": 0}, {"index": 2, "concentration_matches_provider": true, "maintained_evidence_objects": 1, "generated_evidence_objects": 0}, {"index": 3, "concentration_matches_provider": true, "maintained_evidence_objects": 1, "generated_evidence_objects": 0}, {"index": 4, "concentration_matches_provider": true, "maintained_evidence_objects": 0, "generated_evidence_objects": 0}], "preparation_equal_to_provider": true, "ph_equal_to_provider": true, "source_product_attribute": "BD BACTO", "provider_main_volume_ml": 1000, "source_water_row": {"recipe_order": 6, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "owner_evidence_json_equal_to_current_provider": 3} |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No exact commercial-product catalog or constituent composition is claimed or required for this source-faithful premix representation. Manufacturer details remain a bounded follow-up only if an expansion is later proposed.
- No record edits, source protocol optimization, organism-specific growth assertion or experimental final-volume measurement was performed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T064106Z-culturemech-015334-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_2_tryptic_soy_broth_anaerobic (CultureMech:015334)'
started_at: '2026-10-21T06:36:39Z'
finished_at: '2026-10-21T06:41:06Z'
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
summary: DSMZ 1205 identity, all five direct amounts, pH and complete preparation
  are supported. The commercial premix is correctly preserved. Source supplier and
  water/batch context are omitted; three maintained concentration evidence objects
  and their later provenance are absent from the generated target.
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
  - path: data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml
    sha256: 2fd0b2aa40f92a4bd9eb50b098150ccdfeea4c2aec6834bdab874e9c03c3ae8d
    role: target
  - path: data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml
    sha256: d3041ad09664b0d80df60a2ffb47804e70a55889212257797e967cdb1be3db4d
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
  selection: Record 53 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 006 selects ordinals 51-60 after five
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:015334
targets:
- target_id: CultureMech:015334
  path: data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml
  label: 1_2_tryptic_soy_broth_anaerobic
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:015334
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch006/053/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch006/053/strict.tsv"
  target_ids:
  - CultureMech:015334
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:015334
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:015334
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
  - CultureMech:015334
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T06:41:05Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T06:41:05Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:37:33.530805Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch006/053/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T06:37:36.337255Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch006/053/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:37:42.344465Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:37:49.837441Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T06:41:05Z'
  support: supports
  summary: './data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml:1:id:
    CultureMech:015334

    ./data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml:1:id:
    CultureMech:015334

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: chebi17634
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:14:38.075522Z'
  support: supports
  summary: CHEBI:17634 resolves to D-glucose and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: d11b31a8e91c3fffe7744f612dab69cdb4e02f42068cd2eb1458acee4503a62f
- evidence_id: chebi18320
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18320
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:37:24.678779Z'
  support: supports
  summary: CHEBI:18320 resolves to 1,4-dithiothreitol and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 475ff3beab5570f7c37e9627477a11b45f76f0be7b4d04d07c310416b58c5e54
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
  accessed_at: '2026-10-21T06:41:05Z'
  support: supports
  summary: '{"CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier":
    "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17634": [{"label": "D-Glucose", "match_type":
    "preferred_term", "identifier": "CHEBI:17634", "preferred_term": "D-Glucose",
    "ontology_id": "CHEBI:17634", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}],
    "CHEBI:18320": [{"label": "DL-Dithiothreitol", "match_type": "preferred_term",
    "identifier": "CHEBI:18320", "preferred_term": "DL-Dithiothreitol", "ontology_id":
    "CHEBI:18320", "mapping_status": "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: dsmz
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1205.pdf
  locator: Page 1 formulation and preparation
  accessed_at: '2026-10-20T07:37:13.684844Z'
  support: supports
  summary: Full primary collection formula and preparation inspected; source product
    remains a premix.
  quote: Trypticase soy broth (BD BACTO) 13.75 g
  snapshot_sha256: 192dc12c9d2d5be2aa9baae12bbd7acf5bb6da94cbac17128bcfa1e1958234be
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1205
  locator: data.medium; data.solutions[0]
  accessed_at: '2026-10-20T07:38:16.669937Z'
  support: supports
  summary: All five non-water source rows, declared main volume, pH and preparation
    inspected.
  snapshot_sha256: 711e2a48c1ba46c9a988d5070cdb8f76f3a389f2f3b2837a20562caa65fd48dd
- evidence_id: render
  kind: database
  reference: https://bacmedia.dsmz.de/pdf/1205
  locator: Page 1
  accessed_at: '2026-10-20T07:37:19.790784Z'
  support: supports
  summary: Source rendering confirms declared volume, pH and preparation context.
  snapshot_sha256: eb07b4a706bafc255d4b8b2e9456da28785d8028ac353bf6070ff6f6db6be7a2
- evidence_id: trace
  kind: validation
  reference: Target, maintained owner and live provider comparison
  locator: All five quantities; exact preparation text; all three maintained evidence
    snippets parsed as JSON
  accessed_at: '2026-10-21T06:40:43.849832Z'
  support: supports
  summary: '{"accessed_at": "2026-10-21T06:40:43.849832+00:00", "all_five_amounts":
    [{"index": 0, "concentration_matches_provider": true, "maintained_evidence_objects":
    0, "generated_evidence_objects": 0}, {"index": 1, "concentration_matches_provider":
    true, "maintained_evidence_objects": 1, "generated_evidence_objects": 0}, {"index":
    2, "concentration_matches_provider": true, "maintained_evidence_objects": 1, "generated_evidence_objects":
    0}, {"index": 3, "concentration_matches_provider": true, "maintained_evidence_objects":
    1, "generated_evidence_objects": 0}, {"index": 4, "concentration_matches_provider":
    true, "maintained_evidence_objects": 0, "generated_evidence_objects": 0}], "preparation_equal_to_provider":
    true, "ph_equal_to_provider": true, "source_product_attribute": "BD BACTO", "provider_main_volume_ml":
    1000, "source_water_row": {"recipe_order": 6, "compound": "Distilled water", "compound_id":
    4, "amount": 1000, "unit": "ml", "optional": 0}, "owner_evidence_json_equal_to_current_provider":
    3}'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:015334
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
  - CultureMech:015334
  evidence_ids:
  - record
  - mim
  - chebi17634
  - chebi18320
  - chebi26710
  details: 5 direct ingredient instances; primary coverage 3/5 (60.00%), verified
    secondary coverage 3/5 (60.00%). Percentages use a 0–100 linkage scale, not a
    scientific correctness score. Complex mixtures without asserted IDs remain ungrounded
    rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Source accession and maintained owner
  outcome: supported
  summary: CultureMech:015334 identifies DSMZ1205 through mediadive.medium:1205 and
    one specialized normalized owner. The source is a liquid broth with an intact
    commercial product boundary. No sibling constituent expansion is imported.
  target_ids:
  - CultureMech:015334
  evidence_ids:
  - record
  - owner-0
  - id-search
  - dsmz
  - api
- assessment_id: amount-0
  area: quantity
  topic: ingredients[0].concentration
  outcome: supported
  summary: 'verified: exact source row, original gram amount and provider-declared
    per-liter value agree. The commercial product is retained as a mixture; no unverified
    internal constituent calculation is required.'
  target_ids:
  - CultureMech:015334
  evidence_ids:
  - record
  - dsmz
  - api
  - trace
- assessment_id: amount-1
  area: quantity
  topic: ingredients[1].concentration
  outcome: supported
  summary: 'verified: exact source row, original gram amount and provider-declared
    per-liter value agree. The commercial product is retained as a mixture; no unverified
    internal constituent calculation is required.'
  target_ids:
  - CultureMech:015334
  evidence_ids:
  - record
  - dsmz
  - api
  - trace
- assessment_id: amount-2
  area: quantity
  topic: ingredients[2].concentration
  outcome: supported
  summary: 'verified: exact source row, original gram amount and provider-declared
    per-liter value agree. The commercial product is retained as a mixture; no unverified
    internal constituent calculation is required.'
  target_ids:
  - CultureMech:015334
  evidence_ids:
  - record
  - dsmz
  - api
  - trace
- assessment_id: amount-3
  area: quantity
  topic: ingredients[3].concentration
  outcome: supported
  summary: 'verified: exact source row, original gram amount and provider-declared
    per-liter value agree. The commercial product is retained as a mixture; no unverified
    internal constituent calculation is required.'
  target_ids:
  - CultureMech:015334
  evidence_ids:
  - record
  - dsmz
  - api
  - trace
- assessment_id: amount-4
  area: quantity
  topic: ingredients[4].concentration
  outcome: supported
  summary: 'verified: exact source row, original gram amount and provider-declared
    per-liter value agree. The commercial product is retained as a mixture; no unverified
    internal constituent calculation is required.'
  target_ids:
  - CultureMech:015334
  evidence_ids:
  - record
  - dsmz
  - api
  - trace
- assessment_id: preparation
  area: completeness
  topic: Preparation, gas, stocks and pH
  outcome: supported
  summary: The full preparation text equals the provider text and preserves source
    staging, acid adjustment, gas and separately sterilized stock-addition context.
    The numeric pH matches the source. Stock strengths, stock volumes and acid dose
    are not supplied, and the record does not invent them.
  target_ids:
  - CultureMech:015334
  evidence_ids:
  - record
  - owner-0
  - dsmz
  - api
  - trace
- assessment_id: source-detail
  area: completeness
  topic: Product supplier and water basis
  outcome: concern
  summary: The source product has a BD BACTO qualifier, and the water volume and declared
    main volume are explicit upstream. The local product name and per-liter values
    omit those formulation details. A precise catalog is not needed to retain the
    source product as supplied; it must not be guessed.
  target_ids:
  - CultureMech:015334
  evidence_ids:
  - record
  - owner-0
  - dsmz
  - api
  - render
  - trace
- assessment_id: forms
  area: grounding
  topic: Chemical identity and undefined mixtures
  outcome: supported
  summary: NaCl, D-glucose and DL-dithiothreitol resolve with matching labels and
    live secondary keys. The two undefined mixture ingredients remain ungrounded rather
    than being forced into pure-chemical identities. Primary and secondary linkage
    are each 3/5 (60%) on a 0–100 scale; this is not a scientific-accuracy score.
  target_ids:
  - CultureMech:015334
  evidence_ids:
  - record
  - mim
  - chebi26710
  - chebi17634
  - chebi18320
  - dsmz
- assessment_id: classification
  area: scope
  topic: Composition, physical state and category
  outcome: supported
  summary: COMPLEX/UNDEFINED and LIQUID agree with the source premix/extract and absence
    of gelling agent. Specialized is a broad organizational category for this anaerobic
    formulation; no specific organism claim creates a taxonomic conflict. Generic
    cultivation is not evidence of strain-specific performance.
  target_ids:
  - CultureMech:015334
  evidence_ids:
  - record
  - dsmz
  - api
- assessment_id: evidence
  area: evidence
  topic: Maintained evidence versus generated target
  outcome: concern
  summary: Three owner ingredient evidence objects match the current provider rows
    exactly after JSON parsing, and correctly limit their amount claims to the provider-declared
    main-recipe basis. They and the later owner curation event/reference are missing
    from the older generated output. Premix and DTT amounts still lack narrow owner
    evidence. The target reference gate checked zero excerpts.
  target_ids:
  - CultureMech:015334
  evidence_ids:
  - record
  - owner-0
  - api
  - trace
  - validate-references
findings:
- finding_id: f1
  issue_key: CM015334-source-product-context
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Supplier and water/batch context are omitted
  description: The source product qualifier and original water volume are missing
    from both local records, limiting faithful interpretation of the correctly retained
    commercial ingredient and per-liter amounts.
  target_ids:
  - CultureMech:015334
  field_paths:
  - ingredients[0].supplier_catalog
  - notes
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - dsmz
  - api
  - render
  - trace
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM015334-generated-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Generated record omits maintained concentration evidence
  description: The owner contains three verified concentration evidence objects and
    a later provenance event absent from the target; the other two direct amounts
    lack narrow owner evidence.
  target_ids:
  - CultureMech:015334
  field_paths:
  - ingredients[*].evidence
  - curation_history
  - references
  evidence_ids:
  - record
  - owner-0
  - api
  - trace
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Retain the verified BD BACTO qualifier and source water/batch context
    in the maintained owner. Preserve the premix boundary and do not infer a catalog
    or internal formula.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:015334
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml
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
  description: Preserve verified owner evidence during separately authorized regeneration
    and add narrow support for the remaining product and DTT amounts. Check the resulting
    target contains the intended evidence and later provenance.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:015334
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml
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
- No exact commercial-product catalog or constituent composition is claimed or required
  for this source-faithful premix representation. Manufacturer details remain a bounded
  follow-up only if an expansion is later proposed.
- No record edits, source protocol optimization, organism-specific growth assertion
  or experimental final-volume measurement was performed.
tags:
- unreviewed-records
- batch-006
- generated-medium
```
