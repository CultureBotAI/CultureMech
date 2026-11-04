# Source and formulation review: 1_2_gy_agar (CultureMech:002253)

- Review: 20261020T041031Z-culturemech-002253-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-20T04:08:44Z
- Finished UTC: 2026-10-20T04:10:31Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The target and maintained owner correctly represent JCM 1072 and all four listed solute concentrations. They omit the source yeast-extract supplier qualifier, water-batch context and applicable collection-default sterilization, and provide no scoped concentration evidence. No further halving or invented pH is justified.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 37 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002253 | data/merge_yaml/merged/1_2_GY_AGAR.yaml | generated | 1_2_gy_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002253 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002253 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/037/strict.tsv |
| validate-terms | passed | True | CultureMech:002253 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002253 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002253 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002253.

The four documented recipes completed; interpret the scope of each separately.

### Accession, generated target and owner

identity: supported. Targets: CultureMech:002253.

CultureMech:002253 and the single normalized owner both resolve to JCM J1072 / GRMD 1072. No sibling or alternate formulation is conflated.

The uppercase filename and normalized lowercase stored name denote the same stable target. The source describes a complete medium; its API main-solution label is not a separate stock requiring a dilution reference.

### ingredients[0].concentration (Glucose)

quantity: supported. Targets: CultureMech:002253.

verified: 10 G_PER_L agrees with the primary source mass, explicit API g_l and provider volume 1000 mL.

All four direct solute quantities were checked individually. The source already specifies 1/2 GY; no additional twofold dilution is inferred. No stock, nested dose, percent basis or mass-to-molar conversion is involved.

### ingredients[1].concentration (KH2PO4)

quantity: supported. Targets: CultureMech:002253.

verified: 0.5 G_PER_L agrees with the primary source mass, explicit API g_l and provider volume 1000 mL.

All four direct solute quantities were checked individually. The source already specifies 1/2 GY; no additional twofold dilution is inferred. No stock, nested dose, percent basis or mass-to-molar conversion is involved.

### ingredients[2].concentration (Yeast extract)

quantity: supported. Targets: CultureMech:002253.

verified: 1 G_PER_L agrees with the primary source mass, explicit API g_l and provider volume 1000 mL.

All four direct solute quantities were checked individually. The source already specifies 1/2 GY; no additional twofold dilution is inferred. No stock, nested dose, percent basis or mass-to-molar conversion is involved.

### ingredients[3].concentration (Agar)

quantity: supported. Targets: CultureMech:002253.

verified: 15 G_PER_L agrees with the primary source mass, explicit API g_l and provider volume 1000 mL.

All four direct solute quantities were checked individually. The source already specifies 1/2 GY; no additional twofold dilution is inferred. No stock, nested dose, percent basis or mass-to-molar conversion is involved.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:002253.

3 primary CHEBI identities and 3 secondary keys resolve with matching labels.

4 direct ingredient instances; primary coverage 3/4 (75.00%), secondary coverage 3/4 (75.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Source supplied form and solvent/preparation context

completeness: concern. Targets: CultureMech:002253.

The generic yeast-extract label omits the BD-Difco qualifier present in both collection and API. Target and owner also omit the source water-batch context and collection-default sterilization.

The yeast mixture is correctly left without an invented pure-chemical term. Supplier identity is a source attribute rather than proof of a specific catalog SKU. The primary phosphate term correctly denotes potassium dihydrogen phosphate; generic glucose is not narrowed to a stereoisomer. Missing water context is not the same as an incorrect water concentration: the target has no water row.

### Physical state and unsupported optional conditions

consistency: supported. Targets: CultureMech:002253.

Required agar supports SOLID_AGAR. COMPLEX/UNDEFINED is consistent with yeast extract. Neither source states a pH, so no numerical pH is inferred.

No incubation, atmosphere, storage, shelf life, light or vessel condition is asserted. The collection default is the explicit preparation information requiring retention; no extra protocol is supplied. Source amount units remain valid for a solidified medium.

### Organisms, roles and classifications

scope: supported. Targets: CultureMech:002253.

The generic cultivation application and bacterial filing do not make strain-level growth claims. No ontology role, taxon, strain, DOI, PMID or transcriptomics identifier is asserted.

All asserted ingredient and source identifiers have been checked; optional absent fields are not filled from unrelated examples. No iModulonDB query is applicable to the target medium.

### Source recoverability and evidence placement

evidence: concern. Targets: CultureMech:002253.

The exact collection URL, accession and chronological history are recoverable, but all four amount assertions lack scoped evidence in target and owner. The reference gate examined zero excerpts.

The entire target and owner were read. Absence observations are bounded to those complete files; identifier searches included ignored files. The generated copy matches owner scientific fields, so missing details require maintained-input curation rather than editing the generated YAML. Historical change logs are provenance, not independent source certification.

## Findings

### f1: Source preparation, water basis and supplied yeast qualifier are missing

major / open / confirmed; issue key: culturemech-002253-source-preparation-and-form-omissions.

Owner and target omit the applicable collection-default sterilization, source water-batch context and yeast-extract supplier qualifier. These are recoverable source details needed to preserve formulation/preparation specificity.

### f2: Four supported concentrations lack scoped evidence entries

minor / open / confirmed; issue key: culturemech-002253-concentration-evidence-gap.

The four mass-per-liter assertions match inspected source data but have no ingredient-level supporting excerpts in owner or generated target.

## Recommended Actions And Acceptance Checks

### a1

Retain these exact source details with claim-level evidence in the normalized owner. Preserve correct concentrations and source-unspecified pH; inspect source attribute/preparation handling before authorized regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add concise exact source excerpts, supplied-form context and provider volume at schema-supported claim locations in the maintained owner, then preserve them through regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_2_GY_AGAR.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/1_2_gy_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_2_GY_AGAR.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_2_GY_AGAR.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch004/037/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/037/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_2_GY_AGAR.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_2_GY_AGAR.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/1_2_GY_AGAR.yaml:1:id: CultureMech:002253<br>./data/normalized_yaml/bacterial/1_2_gy_agar.yaml:1:id: CultureMech:002253<br> |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1072; Complete recipe plus applicable page default | supports | JCM 1072 lists four solutes and a one-liter water batch. The yeast extract is supplier-qualified; the page specifies default sterilization unless an entry states otherwise, and this entry has no exception. |
| api | https://mediadive.dsmz.de/rest/medium/J1072; data.medium; complete data.solutions[0] | supports | J1072 identifies JCM 1072 and gives main solution 5137, volume 1000 mL, four explicit g_l values, a supplier attribute for yeast extract and a water row. |
| bacmedia | https://bacmedia.dsmz.de/pdf/J1072; Page 1, title, volume header and complete formulation | supports | The J1072 rendering confirms the four masses, supplier qualifier and explicit final volume of 1000 mL. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17234 resolves to glucose and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:2509 resolves to agar and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Collection recipe support is not experimental growth evidence. No organism-specific or mechanistic assertion is added.
- Provider-declared volume supports mass-per-liter normalization; physical final volume was not independently measured.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T041031Z-culturemech-002253-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_2_gy_agar (CultureMech:002253)'
started_at: '2026-10-20T04:08:44Z'
finished_at: '2026-10-20T04:10:31Z'
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
summary: The target and maintained owner correctly represent JCM 1072 and all four
  listed solute concentrations. They omit the source yeast-extract supplier qualifier,
  water-batch context and applicable collection-default sterilization, and provide
  no scoped concentration evidence. No further halving or invented pH is justified.
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
  - path: data/merge_yaml/merged/1_2_GY_AGAR.yaml
    sha256: e5e8ad2822f4747e39608ba0a969df149be6301ec8cb07ce7d188aa5d0d8af4d
    role: target
  - path: data/normalized_yaml/bacterial/1_2_gy_agar.yaml
    sha256: d03145b43b63c3bd353e3410447b86a142444f0e54761479f186dd4c6a899328
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
  selection: Record 37 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002253
targets:
- target_id: CultureMech:002253
  path: data/merge_yaml/merged/1_2_GY_AGAR.yaml
  label: 1_2_gy_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_gy_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_2_GY_AGAR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002253
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_2_GY_AGAR.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch004/037/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/037/strict.tsv"
  target_ids:
  - CultureMech:002253
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_2_GY_AGAR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002253
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_2_GY_AGAR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002253
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
  - CultureMech:002253
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_2_GY_AGAR.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-20T04:10:30Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_2_gy_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T04:10:30Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_2_GY_AGAR.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T04:09:00.643981Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_2_GY_AGAR.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch004/037/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-20T04:09:04.349330Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/037/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_2_GY_AGAR.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T04:09:08.034340Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_2_GY_AGAR.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T04:09:10.033322Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-20T04:10:30Z'
  support: supports
  summary: './data/merge_yaml/merged/1_2_GY_AGAR.yaml:1:id: CultureMech:002253

    ./data/normalized_yaml/bacterial/1_2_gy_agar.yaml:1:id: CultureMech:002253

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: jcm
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1072
  locator: Complete recipe plus applicable page default
  accessed_at: '2026-10-20T04:08:58.889390Z'
  support: supports
  summary: JCM 1072 lists four solutes and a one-liter water batch. The yeast extract
    is supplier-qualified; the page specifies default sterilization unless an entry
    states otherwise, and this entry has no exception.
  snapshot_sha256: 012b29e2ed4e13d1ee7d02f8f041383251020cda38ce6780385677f410589d72
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1072
  locator: data.medium; complete data.solutions[0]
  accessed_at: '2026-10-20T04:08:59.439189Z'
  support: supports
  summary: J1072 identifies JCM 1072 and gives main solution 5137, volume 1000 mL,
    four explicit g_l values, a supplier attribute for yeast extract and a water row.
  snapshot_sha256: ee25dbf5fd0fcd64818a2fb5979cda597a2a66efc3034272d564f6e85ee3c353
- evidence_id: bacmedia
  kind: database
  reference: https://bacmedia.dsmz.de/pdf/J1072
  locator: Page 1, title, volume header and complete formulation
  accessed_at: '2026-10-20T04:09:00.016636Z'
  support: supports
  summary: The J1072 rendering confirms the four masses, supplier qualifier and explicit
    final volume of 1000 mL.
  quote: 'Final volume: 1000 ml'
  snapshot_sha256: b8012610e56c7a5b915f03ee0f81f62b3bb0a9133acf0e249c0abe6316f4b9e1
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T03:57:32.595833Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T03:57:34.697126Z'
  support: supports
  summary: CHEBI:2509 resolves to agar and is not obsolete. This verifies the asserted
    generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond
    the record is inferred.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T04:02:35.727546Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-20T04:10:30Z'
  support: supports
  summary: '{"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002253
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Accession, generated target and owner
  outcome: supported
  summary: CultureMech:002253 and the single normalized owner both resolve to JCM
    J1072 / GRMD 1072. No sibling or alternate formulation is conflated.
  target_ids:
  - CultureMech:002253
  evidence_ids:
  - record
  - owner-0
  - id-search
  - jcm
  - api
  details: The uppercase filename and normalized lowercase stored name denote the
    same stable target. The source describes a complete medium; its API main-solution
    label is not a separate stock requiring a dilution reference.
- assessment_id: amount-0
  area: quantity
  topic: ingredients[0].concentration (Glucose)
  outcome: supported
  summary: 'verified: 10 G_PER_L agrees with the primary source mass, explicit API
    g_l and provider volume 1000 mL.'
  target_ids:
  - CultureMech:002253
  evidence_ids:
  - record
  - jcm
  - api
  - bacmedia
  details: All four direct solute quantities were checked individually. The source
    already specifies 1/2 GY; no additional twofold dilution is inferred. No stock,
    nested dose, percent basis or mass-to-molar conversion is involved.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Exact source solute mass and provider-declared mass-per-liter normalization
      agree
    evidence_ids:
    - jcm
    - api
    - bacmedia
- assessment_id: amount-1
  area: quantity
  topic: ingredients[1].concentration (KH2PO4)
  outcome: supported
  summary: 'verified: 0.5 G_PER_L agrees with the primary source mass, explicit API
    g_l and provider volume 1000 mL.'
  target_ids:
  - CultureMech:002253
  evidence_ids:
  - record
  - jcm
  - api
  - bacmedia
  details: All four direct solute quantities were checked individually. The source
    already specifies 1/2 GY; no additional twofold dilution is inferred. No stock,
    nested dose, percent basis or mass-to-molar conversion is involved.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Exact source solute mass and provider-declared mass-per-liter normalization
      agree
    evidence_ids:
    - jcm
    - api
    - bacmedia
- assessment_id: amount-2
  area: quantity
  topic: ingredients[2].concentration (Yeast extract)
  outcome: supported
  summary: 'verified: 1 G_PER_L agrees with the primary source mass, explicit API
    g_l and provider volume 1000 mL.'
  target_ids:
  - CultureMech:002253
  evidence_ids:
  - record
  - jcm
  - api
  - bacmedia
  details: All four direct solute quantities were checked individually. The source
    already specifies 1/2 GY; no additional twofold dilution is inferred. No stock,
    nested dose, percent basis or mass-to-molar conversion is involved.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Exact source solute mass and provider-declared mass-per-liter normalization
      agree
    evidence_ids:
    - jcm
    - api
    - bacmedia
- assessment_id: amount-3
  area: quantity
  topic: ingredients[3].concentration (Agar)
  outcome: supported
  summary: 'verified: 15 G_PER_L agrees with the primary source mass, explicit API
    g_l and provider volume 1000 mL.'
  target_ids:
  - CultureMech:002253
  evidence_ids:
  - record
  - jcm
  - api
  - bacmedia
  details: All four direct solute quantities were checked individually. The source
    already specifies 1/2 GY; no additional twofold dilution is inferred. No stock,
    nested dose, percent basis or mass-to-molar conversion is involved.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Exact source solute mass and provider-declared mass-per-liter normalization
      agree
    evidence_ids:
    - jcm
    - api
    - bacmedia
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: 3 primary CHEBI identities and 3 secondary keys resolve with matching labels.
  target_ids:
  - CultureMech:002253
  evidence_ids:
  - record
  - mim
  - chebi17234
  - chebi2509
  - chebi63036
  details: 4 direct ingredient instances; primary coverage 3/4 (75.00%), secondary
    coverage 3/4 (75.00%). Percentages use a 0–100 linkage scale, not a scientific
    correctness score. Complex mixtures without asserted IDs remain ungrounded rather
    than receiving invented pure-molecule identities.
- assessment_id: forms
  area: completeness
  topic: Source supplied form and solvent/preparation context
  outcome: concern
  summary: The generic yeast-extract label omits the BD-Difco qualifier present in
    both collection and API. Target and owner also omit the source water-batch context
    and collection-default sterilization.
  target_ids:
  - CultureMech:002253
  evidence_ids:
  - record
  - owner-0
  - jcm
  - api
  - bacmedia
  details: 'The yeast mixture is correctly left without an invented pure-chemical
    term. Supplier identity is a source attribute rather than proof of a specific
    catalog SKU. The primary phosphate term correctly denotes potassium dihydrogen
    phosphate; generic glucose is not narrowed to a stereoisomer. Missing water context
    is not the same as an incorrect water concentration: the target has no water row.'
- assessment_id: conditions
  area: consistency
  topic: Physical state and unsupported optional conditions
  outcome: supported
  summary: Required agar supports SOLID_AGAR. COMPLEX/UNDEFINED is consistent with
    yeast extract. Neither source states a pH, so no numerical pH is inferred.
  target_ids:
  - CultureMech:002253
  evidence_ids:
  - record
  - jcm
  - api
  - bacmedia
  details: No incubation, atmosphere, storage, shelf life, light or vessel condition
    is asserted. The collection default is the explicit preparation information requiring
    retention; no extra protocol is supplied. Source amount units remain valid for
    a solidified medium.
- assessment_id: scope
  area: scope
  topic: Organisms, roles and classifications
  outcome: supported
  summary: The generic cultivation application and bacterial filing do not make strain-level
    growth claims. No ontology role, taxon, strain, DOI, PMID or transcriptomics identifier
    is asserted.
  target_ids:
  - CultureMech:002253
  evidence_ids:
  - record
  - jcm
  details: All asserted ingredient and source identifiers have been checked; optional
    absent fields are not filled from unrelated examples. No iModulonDB query is applicable
    to the target medium.
- assessment_id: provenance
  area: evidence
  topic: Source recoverability and evidence placement
  outcome: concern
  summary: The exact collection URL, accession and chronological history are recoverable,
    but all four amount assertions lack scoped evidence in target and owner. The reference
    gate examined zero excerpts.
  target_ids:
  - CultureMech:002253
  evidence_ids:
  - record
  - owner-0
  - validate-references
  - jcm
  - api
  details: The entire target and owner were read. Absence observations are bounded
    to those complete files; identifier searches included ignored files. The generated
    copy matches owner scientific fields, so missing details require maintained-input
    curation rather than editing the generated YAML. Historical change logs are provenance,
    not independent source certification.
findings:
- finding_id: f1
  issue_key: culturemech-002253-source-preparation-and-form-omissions
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation, water basis and supplied yeast qualifier are missing
  description: Owner and target omit the applicable collection-default sterilization,
    source water-batch context and yeast-extract supplier qualifier. These are recoverable
    source details needed to preserve formulation/preparation specificity.
  target_ids:
  - CultureMech:002253
  field_paths:
  - ingredients[2].preferred_term
  - ingredients
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm
  - api
  - bacmedia
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_gy_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: culturemech-002253-concentration-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Four supported concentrations lack scoped evidence entries
  description: The four mass-per-liter assertions match inspected source data but
    have no ingredient-level supporting excerpts in owner or generated target.
  target_ids:
  - CultureMech:002253
  field_paths:
  - ingredients[*].evidence
  - references
  evidence_ids:
  - record
  - owner-0
  - jcm
  - api
  - bacmedia
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_gy_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Retain these exact source details with claim-level evidence in the
    normalized owner. Preserve correct concentrations and source-unspecified pH; inspect
    source attribute/preparation handling before authorized regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002253
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_gy_agar.yaml
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
  description: Add concise exact source excerpts, supplied-form context and provider
    volume at schema-supported claim locations in the maintained owner, then preserve
    them through regeneration.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002253
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_gy_agar.yaml
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
- Collection recipe support is not experimental growth evidence. No organism-specific
  or mechanistic assertion is added.
- Provider-declared volume supports mass-per-liter normalization; physical final volume
  was not independently measured.
tags:
- unreviewed-records
- batch-004
- generated-medium
```
