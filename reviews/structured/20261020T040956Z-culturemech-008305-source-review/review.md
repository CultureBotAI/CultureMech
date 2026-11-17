# Source and formulation review: 1_2my (CultureMech:008305)

- Review: 20261020T040956Z-culturemech-008305-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-20T04:08:42Z
- Finished UTC: 2026-10-20T04:09:56Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M1742 correctly resolves to NBRC 951 and retains all five non-water source masses and supplier labels. Water is encoded with the wrong dimension, and the explicit unadjusted-pH instruction is omitted. The same gaps occur in the maintained owner. No additional dilution, premix expansion or arbitrary pH is justified.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 36 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008305 | data/merge_yaml/merged/1_2MY.yaml | generated | 1_2my |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008305 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008305 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/036/strict.tsv |
| validate-terms | passed | True | CultureMech:008305 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008305 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008305 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008305.

The four documented recipes completed; interpret the scope of each separately.

### Medium accession, owner and supplied-product labels

identity: supported. Targets: CultureMech:008305.

The target ID/path and sole normalized owner resolve to TOGO M1742 / NBRC 951. The distinct uppercase filename and lowercase stored name do not change its identity.

Five non-water components match the source including Bacto Peptone (Difco) and Malt Extract Agar (Nissui). The latter is a premixed ingredient, not a claim that all its mass is pure malt extract or a ready-made stock solution. No source sibling is silently substituted.

### ingredients[0].concentration (Distilled water)

quantity: concern. Targets: CultureMech:008305.

correct: source water 1 L is misrepresented as 1 G_PER_L.

The source is already named 1/2MY; no extra halving is supported. The unusual direct agar amount and separate malt-extract-agar premix are both explicitly listed, so neither is corrected based on intuition. Exact final volume is not independently established; no density or stock conversion is performed.

### ingredients[1].concentration (Yeast extract)

quantity: supported. Targets: CultureMech:008305.

verified source mass: 1.5 g; the same numerical G_PER_L value is a nominal one-liter batch normalization.

The source is already named 1/2MY; no extra halving is supported. The unusual direct agar amount and separate malt-extract-agar premix are both explicitly listed, so neither is corrected based on intuition. Exact final volume is not independently established; no density or stock conversion is performed.

### ingredients[2].concentration (Glucose)

quantity: supported. Targets: CultureMech:008305.

verified source mass: 5 g; the same numerical G_PER_L value is a nominal one-liter batch normalization.

The source is already named 1/2MY; no extra halving is supported. The unusual direct agar amount and separate malt-extract-agar premix are both explicitly listed, so neither is corrected based on intuition. Exact final volume is not independently established; no density or stock conversion is performed.

### ingredients[3].concentration (Agar)

quantity: supported. Targets: CultureMech:008305.

verified source mass: 18.8 g; the same numerical G_PER_L value is a nominal one-liter batch normalization.

The source is already named 1/2MY; no extra halving is supported. The unusual direct agar amount and separate malt-extract-agar premix are both explicitly listed, so neither is corrected based on intuition. Exact final volume is not independently established; no density or stock conversion is performed.

### ingredients[4].concentration (Bacto Peptone (Difco))

quantity: supported. Targets: CultureMech:008305.

verified source mass: 2.5 g; the same numerical G_PER_L value is a nominal one-liter batch normalization.

The source is already named 1/2MY; no extra halving is supported. The unusual direct agar amount and separate malt-extract-agar premix are both explicitly listed, so neither is corrected based on intuition. Exact final volume is not independently established; no density or stock conversion is performed.

### ingredients[5].concentration (Malt Extract Agar (Nissui))

quantity: supported. Targets: CultureMech:008305.

verified source mass: 2.7 g; the same numerical G_PER_L value is a nominal one-liter batch normalization.

The source is already named 1/2MY; no extra halving is supported. The unusual direct agar amount and separate malt-extract-agar premix are both explicitly listed, so neither is corrected based on intuition. Exact final volume is not independently established; no density or stock conversion is performed.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:008305.

3 primary CHEBI identities and 3 secondary keys resolve with matching labels.

6 direct ingredient instances; primary coverage 3/6 (50.00%), secondary coverage 3/6 (50.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Unadjusted pH, physical state and absent optional protocols

completeness: concern. Targets: CultureMech:008305.

The source explicitly leaves pH unadjusted, but this instruction is absent from target and owner. SOLID_AGAR matches the required agar-containing formulation.

The missing datum is an instruction, not a numeric pH. Do not fill in a typical pH. The inspected collection entry supplies no sterilization, incubation, storage, vessel or shelf-life procedure; those are not inferred. No stocks, nested additions or internal solution references are asserted.

### Classification, roles and growth

scope: supported. Targets: CultureMech:008305.

COMPLEX/UNDEFINED is supported by the extracts and peptone. Copied role/property notes correspond to the TOGO database annotations.

No organism, strain, DOI, PMID, taxonomy ID, mechanistic pathway or transcriptomics assertion is present. Generic cultivation application and bacterial filing are not organism-specific experimental evidence. Three source ingredients have no primary chemical ID; that is not an invalid mapping.

### History, source recoverability and evidence placement

provenance: concern. Targets: CultureMech:008305.

The source accession and URLs are recoverable and the full owner matches target scientific fields. Six quantity assertions lack scoped excerpts; the reference gate examined zero excerpts.

The complete target and owner, including history, were read. Ingredient/source-field absence is bounded to those objects; no global absence claim is made. Historical events describe prior transformations, not completed scientific verification. No recipe content or history is changed by this review.

## Findings

### f1: Source water volume is represented as mass concentration

major / open / confirmed; issue key: culturemech-008305-water-unit-error.

Both target and owner encode source 1 L water as 1 G_PER_L, an unsupported dimension change.

### f2: Explicit unadjusted-pH instruction is omitted

major / open / confirmed; issue key: culturemech-008305-unadjusted-ph-instruction-omitted.

The primary collection entry and TOGO comment specify unadjusted pH. Neither local record retains that preparation constraint.

### f3: Six quantity assertions lack scoped source excerpts

minor / open / confirmed; issue key: culturemech-008305-quantity-evidence-gap.

No ingredient-level amount evidence is present in owner or target. Five non-water masses are corroborated; the water dimension defect is separately recorded.

## Recommended Actions And Acceptance Checks

### a1

Preserve the source water volume/batch basis in maintained schema-supported fields and inspect the importer unit path before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain the nonnumeric source instruction with evidence in the maintained record; do not invent a pH value.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Add concise exact source excerpts with original units, supplier-qualified labels and batch basis at schema-supported claim locations.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_2MY.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/1_2my.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_2MY.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_2MY.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch004/036/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/036/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_2MY.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_2MY.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/1_2MY.yaml:1:id: CultureMech:008305<br>./data/normalized_yaml/bacterial/1_2my.yaml:1:id: CultureMech:008305<br> |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=951; Complete medium entry: identity, composition and final pH line | supports | NBRC 951 identifies 1/2MY, lists the exact six source components and states that pH is unadjusted. Both supplier-qualified ingredients are retained in the local record. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1742; meta; components[0].items; comments[0] | supports | M1742 points to NBRC_M951 and the exact collection URL. The complete six-row component list, original units, role/property annotations and pH comment were inspected. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15377 resolves to water and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17234 resolves to glucose and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:2509 resolves to agar and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The source gives a one-liter water batch, not an independently measured final solution volume. Non-water amounts are supported as source masses and nominal batch-normalized G_PER_L values.
- Opaque commercial ingredients are retained as named mixtures. Their exact internal composition and product-line continuity are not asserted or inferred; the source supplies no product codes.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T040956Z-culturemech-008305-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_2my (CultureMech:008305)'
started_at: '2026-10-20T04:08:42Z'
finished_at: '2026-10-20T04:09:56Z'
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
summary: TOGO M1742 correctly resolves to NBRC 951 and retains all five non-water
  source masses and supplier labels. Water is encoded with the wrong dimension, and
  the explicit unadjusted-pH instruction is omitted. The same gaps occur in the maintained
  owner. No additional dilution, premix expansion or arbitrary pH is justified.
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
  - path: data/merge_yaml/merged/1_2MY.yaml
    sha256: e84c7441e00045be3e734f135c94345270a877cfec9322aa2117efdc6e9fe795
    role: target
  - path: data/normalized_yaml/bacterial/1_2my.yaml
    sha256: 0ca34f074ea88c4411e4a0c96a610f65fe44ae94a657c89ef76c2266422129b4
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
  selection: Record 36 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008305
targets:
- target_id: CultureMech:008305
  path: data/merge_yaml/merged/1_2MY.yaml
  label: 1_2my
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2my.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_2MY.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008305
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_2MY.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch004/036/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/036/strict.tsv"
  target_ids:
  - CultureMech:008305
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_2MY.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008305
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_2MY.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008305
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
  - CultureMech:008305
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_2MY.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-20T04:09:54Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_2my.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T04:09:54Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_2MY.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T04:08:47.791943Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_2MY.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch004/036/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-20T04:08:51.391165Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/036/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_2MY.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T04:08:56.168140Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_2MY.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T04:08:58.397488Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-20T04:09:54Z'
  support: supports
  summary: './data/merge_yaml/merged/1_2MY.yaml:1:id: CultureMech:008305

    ./data/normalized_yaml/bacterial/1_2my.yaml:1:id: CultureMech:008305

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=951
  locator: 'Complete medium entry: identity, composition and final pH line'
  accessed_at: '2026-10-20T04:08:57.505158Z'
  support: supports
  summary: NBRC 951 identifies 1/2MY, lists the exact six source components and states
    that pH is unadjusted. Both supplier-qualified ingredients are retained in the
    local record.
  quote: pH unadjusted
  snapshot_sha256: 291ee5f99c8d74534d8b1f5d1bb3249480136faf7835f76200512ea00272cf8c
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1742
  locator: meta; components[0].items; comments[0]
  accessed_at: '2026-10-20T04:08:58.227809Z'
  support: supports
  summary: M1742 points to NBRC_M951 and the exact collection URL. The complete six-row
    component list, original units, role/property annotations and pH comment were
    inspected.
  snapshot_sha256: fbda74d2c21cf19c5349e1bff965a7004e700af7c4ee6117bfb1b4a8843e8ac2
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-20T04:09:54Z'
  support: supports
  summary: '{"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234":
    [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234",
    "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008305
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Medium accession, owner and supplied-product labels
  outcome: supported
  summary: The target ID/path and sole normalized owner resolve to TOGO M1742 / NBRC
    951. The distinct uppercase filename and lowercase stored name do not change its
    identity.
  target_ids:
  - CultureMech:008305
  evidence_ids:
  - record
  - owner-0
  - id-search
  - nbrc
  - togo
  details: Five non-water components match the source including Bacto Peptone (Difco)
    and Malt Extract Agar (Nissui). The latter is a premixed ingredient, not a claim
    that all its mass is pure malt extract or a ready-made stock solution. No source
    sibling is silently substituted.
- assessment_id: amount-0
  area: quantity
  topic: ingredients[0].concentration (Distilled water)
  outcome: concern
  summary: 'correct: source water 1 L is misrepresented as 1 G_PER_L.'
  target_ids:
  - CultureMech:008305
  evidence_ids:
  - record
  - nbrc
  - togo
  details: The source is already named 1/2MY; no extra halving is supported. The unusual
    direct agar amount and separate malt-extract-agar premix are both explicitly listed,
    so neither is corrected based on intuition. Exact final volume is not independently
    established; no density or stock conversion is performed.
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Source amount verified or dimensional correction required, with nominal
      batch normalization distinguished from measured final volume
    evidence_ids:
    - nbrc
    - togo
- assessment_id: amount-1
  area: quantity
  topic: ingredients[1].concentration (Yeast extract)
  outcome: supported
  summary: 'verified source mass: 1.5 g; the same numerical G_PER_L value is a nominal
    one-liter batch normalization.'
  target_ids:
  - CultureMech:008305
  evidence_ids:
  - record
  - nbrc
  - togo
  details: The source is already named 1/2MY; no extra halving is supported. The unusual
    direct agar amount and separate malt-extract-agar premix are both explicitly listed,
    so neither is corrected based on intuition. Exact final volume is not independently
    established; no density or stock conversion is performed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Source amount verified or dimensional correction required, with nominal
      batch normalization distinguished from measured final volume
    evidence_ids:
    - nbrc
    - togo
- assessment_id: amount-2
  area: quantity
  topic: ingredients[2].concentration (Glucose)
  outcome: supported
  summary: 'verified source mass: 5 g; the same numerical G_PER_L value is a nominal
    one-liter batch normalization.'
  target_ids:
  - CultureMech:008305
  evidence_ids:
  - record
  - nbrc
  - togo
  details: The source is already named 1/2MY; no extra halving is supported. The unusual
    direct agar amount and separate malt-extract-agar premix are both explicitly listed,
    so neither is corrected based on intuition. Exact final volume is not independently
    established; no density or stock conversion is performed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Source amount verified or dimensional correction required, with nominal
      batch normalization distinguished from measured final volume
    evidence_ids:
    - nbrc
    - togo
- assessment_id: amount-3
  area: quantity
  topic: ingredients[3].concentration (Agar)
  outcome: supported
  summary: 'verified source mass: 18.8 g; the same numerical G_PER_L value is a nominal
    one-liter batch normalization.'
  target_ids:
  - CultureMech:008305
  evidence_ids:
  - record
  - nbrc
  - togo
  details: The source is already named 1/2MY; no extra halving is supported. The unusual
    direct agar amount and separate malt-extract-agar premix are both explicitly listed,
    so neither is corrected based on intuition. Exact final volume is not independently
    established; no density or stock conversion is performed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Source amount verified or dimensional correction required, with nominal
      batch normalization distinguished from measured final volume
    evidence_ids:
    - nbrc
    - togo
- assessment_id: amount-4
  area: quantity
  topic: ingredients[4].concentration (Bacto Peptone (Difco))
  outcome: supported
  summary: 'verified source mass: 2.5 g; the same numerical G_PER_L value is a nominal
    one-liter batch normalization.'
  target_ids:
  - CultureMech:008305
  evidence_ids:
  - record
  - nbrc
  - togo
  details: The source is already named 1/2MY; no extra halving is supported. The unusual
    direct agar amount and separate malt-extract-agar premix are both explicitly listed,
    so neither is corrected based on intuition. Exact final volume is not independently
    established; no density or stock conversion is performed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Source amount verified or dimensional correction required, with nominal
      batch normalization distinguished from measured final volume
    evidence_ids:
    - nbrc
    - togo
- assessment_id: amount-5
  area: quantity
  topic: ingredients[5].concentration (Malt Extract Agar (Nissui))
  outcome: supported
  summary: 'verified source mass: 2.7 g; the same numerical G_PER_L value is a nominal
    one-liter batch normalization.'
  target_ids:
  - CultureMech:008305
  evidence_ids:
  - record
  - nbrc
  - togo
  details: The source is already named 1/2MY; no extra halving is supported. The unusual
    direct agar amount and separate malt-extract-agar premix are both explicitly listed,
    so neither is corrected based on intuition. Exact final volume is not independently
    established; no density or stock conversion is performed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Source amount verified or dimensional correction required, with nominal
      batch normalization distinguished from measured final volume
    evidence_ids:
    - nbrc
    - togo
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: 3 primary CHEBI identities and 3 secondary keys resolve with matching labels.
  target_ids:
  - CultureMech:008305
  evidence_ids:
  - record
  - mim
  - chebi15377
  - chebi17234
  - chebi2509
  details: 6 direct ingredient instances; primary coverage 3/6 (50.00%), secondary
    coverage 3/6 (50.00%). Percentages use a 0–100 linkage scale, not a scientific
    correctness score. Complex mixtures without asserted IDs remain ungrounded rather
    than receiving invented pure-molecule identities.
- assessment_id: conditions
  area: completeness
  topic: Unadjusted pH, physical state and absent optional protocols
  outcome: concern
  summary: The source explicitly leaves pH unadjusted, but this instruction is absent
    from target and owner. SOLID_AGAR matches the required agar-containing formulation.
  target_ids:
  - CultureMech:008305
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  details: The missing datum is an instruction, not a numeric pH. Do not fill in a
    typical pH. The inspected collection entry supplies no sterilization, incubation,
    storage, vessel or shelf-life procedure; those are not inferred. No stocks, nested
    additions or internal solution references are asserted.
- assessment_id: scope
  area: scope
  topic: Classification, roles and growth
  outcome: supported
  summary: COMPLEX/UNDEFINED is supported by the extracts and peptone. Copied role/property
    notes correspond to the TOGO database annotations.
  target_ids:
  - CultureMech:008305
  evidence_ids:
  - record
  - togo
  - nbrc
  details: No organism, strain, DOI, PMID, taxonomy ID, mechanistic pathway or transcriptomics
    assertion is present. Generic cultivation application and bacterial filing are
    not organism-specific experimental evidence. Three source ingredients have no
    primary chemical ID; that is not an invalid mapping.
- assessment_id: provenance
  area: provenance
  topic: History, source recoverability and evidence placement
  outcome: concern
  summary: The source accession and URLs are recoverable and the full owner matches
    target scientific fields. Six quantity assertions lack scoped excerpts; the reference
    gate examined zero excerpts.
  target_ids:
  - CultureMech:008305
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - validate-references
  details: The complete target and owner, including history, were read. Ingredient/source-field
    absence is bounded to those objects; no global absence claim is made. Historical
    events describe prior transformations, not completed scientific verification.
    No recipe content or history is changed by this review.
findings:
- finding_id: f1
  issue_key: culturemech-008305-water-unit-error
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Source water volume is represented as mass concentration
  description: Both target and owner encode source 1 L water as 1 G_PER_L, an unsupported
    dimension change.
  target_ids:
  - CultureMech:008305
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2my.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: culturemech-008305-unadjusted-ph-instruction-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Explicit unadjusted-pH instruction is omitted
  description: The primary collection entry and TOGO comment specify unadjusted pH.
    Neither local record retains that preparation constraint.
  target_ids:
  - CultureMech:008305
  field_paths:
  - preparation_steps
  - notes
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2my.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: culturemech-008305-quantity-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Six quantity assertions lack scoped source excerpts
  description: No ingredient-level amount evidence is present in owner or target.
    Five non-water masses are corroborated; the water dimension defect is separately
    recorded.
  target_ids:
  - CultureMech:008305
  field_paths:
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
    path: data/normalized_yaml/bacterial/1_2my.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Preserve the source water volume/batch basis in maintained schema-supported
    fields and inspect the importer unit path before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008305
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2my.yaml
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
  description: Retain the nonnumeric source instruction with evidence in the maintained
    record; do not invent a pH value.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008305
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2my.yaml
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
  description: Add concise exact source excerpts with original units, supplier-qualified
    labels and batch basis at schema-supported claim locations.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008305
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2my.yaml
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
- The source gives a one-liter water batch, not an independently measured final solution
  volume. Non-water amounts are supported as source masses and nominal batch-normalized
  G_PER_L values.
- Opaque commercial ingredients are retained as named mixtures. Their exact internal
  composition and product-line continuity are not asserted or inferred; the source
  supplies no product codes.
tags:
- unreviewed-records
- batch-004
- generated-medium
```
