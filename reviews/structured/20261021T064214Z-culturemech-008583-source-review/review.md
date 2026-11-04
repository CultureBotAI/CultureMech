# Source and formulation review: 1_3_diluted_lb_medium_with_biphenyl (CultureMech:008583)

- Review: 20261021T064214Z-culturemech-008583-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T06:36:40Z
- Finished UTC: 2026-10-21T06:42:14Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M1999 resolves to NBRC1286. The four non-water ingredient amounts agree with the source nominal recipe, but water volume is encoded as mass. The defining biphenyl vapor-phase context and source pH are absent; claim-level evidence is missing.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 54 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 006 selects ordinals 51-60 after five validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008583 | data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml | generated | 1_3_diluted_lb_medium_with_biphenyl |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008583 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008583 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch006/054/strict.tsv |
| validate-terms | passed | True | CultureMech:008583 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008583 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008583 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008583.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:008583.

3 primary CHEBI identities resolve with matching labels; 3 of 3 current secondary keys have live pinned-index rows. Unresolved keys: [].

5 direct ingredient instances; primary coverage 3/5 (60.00%), verified secondary coverage 3/5 (60.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Source accession and defining medium context

identity: concern. Targets: CultureMech:008583.

The accession identifies the intended NBRC1286 formulation. Its defining biphenyl condition survives only in the label, not the formulation or preparation; the represented recipe therefore lacks a named component of the source identity.

### ingredients[0].concentration

quantity: concern. Targets: CultureMech:008583.

correct: original liter water volume is recast as a mass concentration without density evidence.

### ingredients[1].concentration

quantity: supported. Targets: CultureMech:008583.

verified nominal recipe amount: the original gram quantity agrees with the source batch containing one liter water. This supports the nominal preparation basis, not an independently measured final solution volume; keep the source rounding.

### ingredients[2].concentration

quantity: supported. Targets: CultureMech:008583.

verified nominal recipe amount: the original gram quantity agrees with the source batch containing one liter water. This supports the nominal preparation basis, not an independently measured final solution volume; keep the source rounding.

### ingredients[3].concentration

quantity: supported. Targets: CultureMech:008583.

verified nominal recipe amount: the original gram quantity agrees with the source batch containing one liter water. This supports the nominal preparation basis, not an independently measured final solution volume; keep the source rounding.

### ingredients[4].concentration

quantity: supported. Targets: CultureMech:008583.

verified nominal recipe amount: the original gram quantity agrees with the source batch containing one liter water. This supports the nominal preparation basis, not an independently measured final solution volume; keep the source rounding.

### Source-only biphenyl context

quantity: concern. Targets: CultureMech:008583.

not_quantified: the collection names crystalline biphenyl delivered as vapor-phase context, without a mass dose or bulk-medium concentration. The omission can be corrected faithfully without inventing an amount or treating it as a dissolved addition.

### pH and source preparation

completeness: concern. Targets: CultureMech:008583.

The source pH is present in both upstream entries but absent locally. The source gives no complete sterilization or incubation protocol for this record, so none should be inferred from other LB formulations.

### Supplied materials and mixture scope

grounding: supported. Targets: CultureMech:008583.

Water, sodium chloride and agar resolve with correct labels and current secondary keys. Yeast extract and Bacto tryptone remain named mixtures; the source brand qualifier is retained in the ingredient name. No exact product catalog or pure-molecule identity is inferred.

### Classification and biological claims

scope: supported. Targets: CultureMech:008583.

COMPLEX/UNDEFINED and SOLID_AGAR agree with the source extracts and gelling material. The bacterial category and generic cultivation application make no specific organism growth assertion. Ingredient-role notes reproduce database annotations, not mechanistic experiments.

### Evidence and history

evidence: concern. Targets: CultureMech:008583.

Source identifiers and import/merge provenance are present, but there are no narrow quantity or preparation evidence objects in target or owner. Reference validation checked zero excerpts; it cannot certify missing context.

## Findings

### f1: Defining biphenyl condition is absent from the formulation

blocker / open / confirmed; issue key: CM008583-biphenyl-context-missing.

The label identifies a biphenyl medium, but the source-only biphenyl phase/context is missing from ingredients and preparation. This changes the represented formulation.

### f2: Water volume is encoded as mass concentration

major / open / confirmed; issue key: CM008583-water-volume-unit.

The source liter value is retained numerically but labeled G_PER_L.

### f3: Source pH is missing

major / open / confirmed; issue key: CM008583-ph-omitted.

Both source records specify pH, but neither local record preserves it.

### f4: Quantity and preparation evidence is absent

minor / open / confirmed; issue key: CM008583-claim-evidence-gap.

Source notes and history do not supply claim-level amount or phase support.

## Recommended Actions And Acceptance Checks

### a1

Retain the source biphenyl context and phase in the maintained owner, leaving dose/concentration unspecified. Do not invent a dissolved concentration or extrapolate an incubation protocol.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Represent the original water volume and nominal batch basis without a guessed density conversion.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Retain source pH with a narrow citation and preserve any unknown adjustment procedure as unknown.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach narrow evidence to unchanged supported amounts and corrected context; verify it survives regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/1_3_diluted_lb_medium_with_biphenyl.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch006/054/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch006/054/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml:1:id: CultureMech:008583<br>./data/normalized_yaml/bacterial/1_3_diluted_lb_medium_with_biphenyl.yaml:1:id: CultureMech:008583<br> |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15377 resolves to water and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:2509 resolves to agar and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1999; meta; components[0]; comments | supports | Complete entry and preparation comments inspected, including original NBRC accession and pH. |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1286; Medium1286 composition and following comment | supports | Full collection recipe identifies five listed ingredients plus a distinct biphenyl vapor-phase condition and pH. |
| trace | TOGO M1999 component and owner comparison; All five direct rows and notes; whole target and owner read | context_only | [{"index": 0, "name": "Distilled water", "source_unit": "L", "source_amount": 1, "target": {"value": "1", "unit": "G_PER_L"}}, {"index": 1, "name": "Yeast extract", "source_unit": "g", "source_amount": 1.6, "target": {"value": "1.6", "unit": "G_PER_L"}}, {"index": 2, "name": "NaCl", "source_unit": "g", "source_amount": 3.3, "target": {"value": "3.3", "unit": "G_PER_L"}}, {"index": 3, "name": "Agar", "source_unit": "g", "source_amount": 15, "target": {"value": "15", "unit": "G_PER_L"}}, {"index": 4, "name": "Bacto tryptone", "source_unit": "g", "source_amount": 3.3, "target": {"value": "3.3", "unit": "G_PER_L"}}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No exact biphenyl amount, dissolved concentration, measured final volume, incubation condition, sterilization method or organism-specific growth is inferred.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T064214Z-culturemech-008583-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_3_diluted_lb_medium_with_biphenyl (CultureMech:008583)'
started_at: '2026-10-21T06:36:40Z'
finished_at: '2026-10-21T06:42:14Z'
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
summary: TOGO M1999 resolves to NBRC1286. The four non-water ingredient amounts agree
  with the source nominal recipe, but water volume is encoded as mass. The defining
  biphenyl vapor-phase context and source pH are absent; claim-level evidence is missing.
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
  - path: data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml
    sha256: 73c92d1b348831eee32b5c77a487d989048b9d4a0e84901c76c337c6994de2f9
    role: target
  - path: data/normalized_yaml/bacterial/1_3_diluted_lb_medium_with_biphenyl.yaml
    sha256: 06c045720af93f16d3298bea90fca8d4bbd7da24ad3aa090491080c5b62d1b07
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
  selection: Record 54 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 006 selects ordinals 51-60 after five
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008583
targets:
- target_id: CultureMech:008583
  path: data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml
  label: 1_3_diluted_lb_medium_with_biphenyl
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_3_diluted_lb_medium_with_biphenyl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008583
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch006/054/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch006/054/strict.tsv"
  target_ids:
  - CultureMech:008583
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008583
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008583
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
  - CultureMech:008583
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T06:42:12Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_3_diluted_lb_medium_with_biphenyl.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T06:42:12Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:37:56.976646Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch006/054/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T06:38:05.867247Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch006/054/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:38:10.415208Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:38:13.505286Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T06:42:12Z'
  support: supports
  summary: './data/merge_yaml/merged/1_3_Diluted_LB_Medium_with_Biphenyl.yaml:1:id:
    CultureMech:008583

    ./data/normalized_yaml/bacterial/1_3_diluted_lb_medium_with_biphenyl.yaml:1:id:
    CultureMech:008583

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
  accessed_at: '2026-10-21T06:42:12Z'
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
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1999
  locator: meta; components[0]; comments
  accessed_at: '2026-10-21T06:41:12.054964Z'
  support: supports
  summary: Complete entry and preparation comments inspected, including original NBRC
    accession and pH.
  snapshot_sha256: 745171ae36ab1a7a055d138589ad0da7e0bb6ae81140228d49d624559ba5948d
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1286
  locator: Medium1286 composition and following comment
  accessed_at: '2026-10-21T06:41:16.604863Z'
  support: supports
  summary: Full collection recipe identifies five listed ingredients plus a distinct
    biphenyl vapor-phase condition and pH.
  quote: Biphenyl crystal is supplied on a lid of petri dish as vapor phase.
  snapshot_sha256: 9896d9499c009fff27e883be8117a84b4ac836c95b232d9a6834ec25e3a21da3
- evidence_id: trace
  kind: validation
  reference: TOGO M1999 component and owner comparison
  locator: All five direct rows and notes; whole target and owner read
  accessed_at: '2026-10-21T06:42:12Z'
  support: context_only
  summary: '[{"index": 0, "name": "Distilled water", "source_unit": "L", "source_amount":
    1, "target": {"value": "1", "unit": "G_PER_L"}}, {"index": 1, "name": "Yeast extract",
    "source_unit": "g", "source_amount": 1.6, "target": {"value": "1.6", "unit": "G_PER_L"}},
    {"index": 2, "name": "NaCl", "source_unit": "g", "source_amount": 3.3, "target":
    {"value": "3.3", "unit": "G_PER_L"}}, {"index": 3, "name": "Agar", "source_unit":
    "g", "source_amount": 15, "target": {"value": "15", "unit": "G_PER_L"}}, {"index":
    4, "name": "Bacto tryptone", "source_unit": "g", "source_amount": 3.3, "target":
    {"value": "3.3", "unit": "G_PER_L"}}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008583
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
  - CultureMech:008583
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
  topic: Source accession and defining medium context
  outcome: concern
  summary: The accession identifies the intended NBRC1286 formulation. Its defining
    biphenyl condition survives only in the label, not the formulation or preparation;
    the represented recipe therefore lacks a named component of the source identity.
  target_ids:
  - CultureMech:008583
  evidence_ids:
  - record
  - owner-0
  - id-search
  - nbrc
  - togo
- assessment_id: amount-0
  area: quantity
  topic: ingredients[0].concentration
  outcome: concern
  summary: 'correct: original liter water volume is recast as a mass concentration
    without density evidence.'
  target_ids:
  - CultureMech:008583
  evidence_ids:
  - record
  - nbrc
  - togo
  - trace
- assessment_id: amount-1
  area: quantity
  topic: ingredients[1].concentration
  outcome: supported
  summary: 'verified nominal recipe amount: the original gram quantity agrees with
    the source batch containing one liter water. This supports the nominal preparation
    basis, not an independently measured final solution volume; keep the source rounding.'
  target_ids:
  - CultureMech:008583
  evidence_ids:
  - record
  - nbrc
  - togo
  - trace
- assessment_id: amount-2
  area: quantity
  topic: ingredients[2].concentration
  outcome: supported
  summary: 'verified nominal recipe amount: the original gram quantity agrees with
    the source batch containing one liter water. This supports the nominal preparation
    basis, not an independently measured final solution volume; keep the source rounding.'
  target_ids:
  - CultureMech:008583
  evidence_ids:
  - record
  - nbrc
  - togo
  - trace
- assessment_id: amount-3
  area: quantity
  topic: ingredients[3].concentration
  outcome: supported
  summary: 'verified nominal recipe amount: the original gram quantity agrees with
    the source batch containing one liter water. This supports the nominal preparation
    basis, not an independently measured final solution volume; keep the source rounding.'
  target_ids:
  - CultureMech:008583
  evidence_ids:
  - record
  - nbrc
  - togo
  - trace
- assessment_id: amount-4
  area: quantity
  topic: ingredients[4].concentration
  outcome: supported
  summary: 'verified nominal recipe amount: the original gram quantity agrees with
    the source batch containing one liter water. This supports the nominal preparation
    basis, not an independently measured final solution volume; keep the source rounding.'
  target_ids:
  - CultureMech:008583
  evidence_ids:
  - record
  - nbrc
  - togo
  - trace
- assessment_id: biphenyl
  area: quantity
  topic: Source-only biphenyl context
  outcome: concern
  summary: 'not_quantified: the collection names crystalline biphenyl delivered as
    vapor-phase context, without a mass dose or bulk-medium concentration. The omission
    can be corrected faithfully without inventing an amount or treating it as a dissolved
    addition.'
  target_ids:
  - CultureMech:008583
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
- assessment_id: preparation
  area: completeness
  topic: pH and source preparation
  outcome: concern
  summary: The source pH is present in both upstream entries but absent locally. The
    source gives no complete sterilization or incubation protocol for this record,
    so none should be inferred from other LB formulations.
  target_ids:
  - CultureMech:008583
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
- assessment_id: grounding-forms
  area: grounding
  topic: Supplied materials and mixture scope
  outcome: supported
  summary: Water, sodium chloride and agar resolve with correct labels and current
    secondary keys. Yeast extract and Bacto tryptone remain named mixtures; the source
    brand qualifier is retained in the ingredient name. No exact product catalog or
    pure-molecule identity is inferred.
  target_ids:
  - CultureMech:008583
  evidence_ids:
  - record
  - mim
  - chebi15377
  - chebi26710
  - chebi2509
  - nbrc
- assessment_id: classification
  area: scope
  topic: Classification and biological claims
  outcome: supported
  summary: COMPLEX/UNDEFINED and SOLID_AGAR agree with the source extracts and gelling
    material. The bacterial category and generic cultivation application make no specific
    organism growth assertion. Ingredient-role notes reproduce database annotations,
    not mechanistic experiments.
  target_ids:
  - CultureMech:008583
  evidence_ids:
  - record
  - nbrc
  - togo
  - trace
- assessment_id: evidence
  area: evidence
  topic: Evidence and history
  outcome: concern
  summary: Source identifiers and import/merge provenance are present, but there are
    no narrow quantity or preparation evidence objects in target or owner. Reference
    validation checked zero excerpts; it cannot certify missing context.
  target_ids:
  - CultureMech:008583
  evidence_ids:
  - record
  - owner-0
  - validate-references
  - togo
  - nbrc
findings:
- finding_id: f1
  issue_key: CM008583-biphenyl-context-missing
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Defining biphenyl condition is absent from the formulation
  description: The label identifies a biphenyl medium, but the source-only biphenyl
    phase/context is missing from ingredients and preparation. This changes the represented
    formulation.
  target_ids:
  - CultureMech:008583
  field_paths:
  - ingredients
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_3_diluted_lb_medium_with_biphenyl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM008583-water-volume-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water volume is encoded as mass concentration
  description: The source liter value is retained numerically but labeled G_PER_L.
  target_ids:
  - CultureMech:008583
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - trace
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_3_diluted_lb_medium_with_biphenyl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM008583-ph-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source pH is missing
  description: Both source records specify pH, but neither local record preserves
    it.
  target_ids:
  - CultureMech:008583
  field_paths:
  - ph_value
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_3_diluted_lb_medium_with_biphenyl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: CM008583-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Quantity and preparation evidence is absent
  description: Source notes and history do not supply claim-level amount or phase
    support.
  target_ids:
  - CultureMech:008583
  field_paths:
  - ingredients[*].evidence
  - references
  evidence_ids:
  - record
  - owner-0
  - validate-references
  - nbrc
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_3_diluted_lb_medium_with_biphenyl.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Retain the source biphenyl context and phase in the maintained owner,
    leaving dose/concentration unspecified. Do not invent a dissolved concentration
    or extrapolate an incubation protocol.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008583
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_3_diluted_lb_medium_with_biphenyl.yaml
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
  description: Represent the original water volume and nominal batch basis without
    a guessed density conversion.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008583
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_3_diluted_lb_medium_with_biphenyl.yaml
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
  description: Retain source pH with a narrow citation and preserve any unknown adjustment
    procedure as unknown.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008583
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_3_diluted_lb_medium_with_biphenyl.yaml
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
  description: Attach narrow evidence to unchanged supported amounts and corrected
    context; verify it survives regeneration.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008583
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_3_diluted_lb_medium_with_biphenyl.yaml
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
- No exact biphenyl amount, dissolved concentration, measured final volume, incubation
  condition, sterilization method or organism-specific growth is inferred.
tags:
- unreviewed-records
- batch-006
- generated-medium
```
