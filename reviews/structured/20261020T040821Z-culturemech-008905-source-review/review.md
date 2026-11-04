# Source and formulation review: 1_10_strength_ytss_agar (CultureMech:008905)

- Review: 20261020T040821Z-culturemech-008905-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-20T04:06:26Z
- Finished UTC: 2026-10-20T04:08:21Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The target correctly identifies TOGO M2318 but conflates its named diluted agar variant with the full-strength formulation described in source prose. It also retains an obsolete water mass unit, despite a maintained correction, and lacks agar/solid-state representation. Percent basis and the exact diluted formulation remain unresolved; no numerical replacement is inferred.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 35 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008905 | data/merge_yaml/merged/1_10_strength_ytss_agar.yaml | generated | 1_10_strength_ytss_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008905 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008905 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/035/strict.tsv |
| validate-terms | passed | True | CultureMech:008905 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008905 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008905 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008905.

The four documented recipes completed; interpret the scope of each separately.

### Accession, medium variant and source scope

identity: concern. Targets: CultureMech:008905.

The selected target and owner resolve to M2318, but source-comment scope contradicts the formulation attribution used by the record and repair script.

The review target is unambiguous even though its scientific formulation is inconsistent. No arbitrary replacement identity, calculated diluted recipe or duplicate merge is proposed. The complete source comment must be carried into future curation rather than relying on component rows alone.

### ingredients[0].concentration

quantity: concern. Targets: CultureMech:008905.

correct: the target has 1 G_PER_L while TOGO supplies 1 L water. The maintained owner already has a volume-based representation; regeneration must not restore the old mass unit.

### ingredients[1].concentration: yeast extract

quantity: concern. Targets: CultureMech:008905.

conflict: the numeric component entry agrees with the record, but its applicability to the named variant and its PERCENT_W_V basis are not supported.

Do not compute a final replacement from the name alone. Resolve both variant scope and percentage basis in source-specific evidence before changing an amount.

### ingredients[3].concentration: tryptone

quantity: concern. Targets: CultureMech:008905.

conflict: the numeric component entry agrees with the record, but its applicability to the named variant and its PERCENT_W_V basis are not supported.

Do not compute a final replacement from the name alone. Resolve both variant scope and percentage basis in source-specific evidence before changing an amount.

### ingredients[2].concentration

quantity: concern. Targets: CultureMech:008905.

conflict: 20 G_PER_L reproduces the database row and parent-formulation prose, but its applicability to the diluted named variant is not established.

Do not assume either that sea salts are diluted with organic nutrients or that salt strength is held constant. Sea salts are an undefined commercial/mineral mixture here; no exact salt composition, supplier or alternative ontology identity is inferred.

### Ingredient identities and linkage

grounding: supported. Targets: CultureMech:008905.

The target water CHEBI identity and secondary MIM key resolve. The three complex mixtures remain ungrounded, rather than assigned invented single-molecule IDs. The owner’s added FoodOn yeast identity is valid.

Four direct ingredient instances; one primary CHEBI and one secondary MIM CHEBI link give 1/4 or 25% coverage each, on a 0–100 linkage scale. Owner mapping coverage is separate from target coverage. Current schema/term passes do not establish the missing formulation details.

### Physical state and missing solidifier

representation: concern. Targets: CultureMech:008905.

The target and owner say LIQUID and list no solidifier despite the source-specific name identifying an agar medium. An actual agar amount is not supplied in the inspected passage.

Report missing representation and unresolved dose together; do not infer a typical agar concentration. There are no stock solution descriptors, internal recipe links, nested amounts or asserted incubation conditions. Empty preparation/pH fields cannot be populated from this passage. Missing data is not a basis to invent sterilization, storage or growth conditions.

### Growth, classifications and annotations

scope: supported. Targets: CultureMech:008905.

COMPLEX/UNDEFINED fits the mixture ingredients. The target carries only a generic cultivation application and database role/property notes, with no taxon, strain identifier, mechanistic or transcriptomic assertion.

The article’s relevant isolation context is not promoted into new target-organism or universal growth assertions. No taxonomy identifier is guessed. Annotation-only role text remains scoped as a database statement; no unrelated literature organism is treated as evidence for the target.

### Current owner versus generated snapshot

provenance: concern. Targets: CultureMech:008905.

The owner includes later water correction, FoodOn mapping and source notes that the generated target lacks; it still preserves the central source-scope problem. Neither local record has scoped concentration excerpts.

Data-quality flags and the completed repair event are provenance, not scientific approval. The target reference check examined zero excerpts. All absence observations concern the complete target/owner objects; the whole-checkout search included ignored files. No publication, recipe mutation or status promotion is performed.

## Findings

### f1: Parent formulation is attributed to the diluted variant

blocker / open / confirmed; issue key: culturemech-008905-full-strength-variant-conflation.

The source explicitly labels the quoted formulation full strength; the target and repair specification apply it to the diluted name. The percentage basis is also unstated. A matching numeric database row cannot resolve that contextual contradiction.

### f2: Generated water unit remains wrong after owner correction

major / open / confirmed; issue key: culturemech-008905-generated-water-unit-stale.

The target retains 1 G_PER_L for source water given in liters. The maintained owner already records the volume, so this specific correction is stale in the derived artifact.

### f3: Agar medium is represented as liquid without a solidifier

major / open / confirmed; issue key: culturemech-008905-agar-state-incomplete.

The source-specific agar identity conflicts with LIQUID and the complete four-component ingredient list. The source passage does not quantify agar, so the missing amount remains unresolved.

### f4: Source context is not retained as claim-level evidence

minor / open / confirmed; issue key: culturemech-008905-source-evidence-placement-gap.

The generated target has only a source URL. Owner source notes reproduce amounts but lack the decisive surrounding variant context; the target reference validator checked zero excerpts.

## Recommended Actions And Acceptance Checks

### a1

Correct the maintained variant attribution and owning repair specification from the full source context. Preserve unresolved dilution/percentage scope rather than inferring replacement numbers.

- Reconcile structured TOGO rows with their full source comment and the exact primary-publication variant before asserting replacement values.
- Use source-specific evidence for percentage basis, dilution scope and any solidifier amount; unresolved quantities must remain explicit.
- Run focused schema, strict, term and reference validators after separately authorized maintained-input edits; then regenerate and run just verify-merges and just audit-merge-freshness.

### a2

Preserve the owner’s source-volume correction and regenerate after resolving remaining owner issues; do not convert water to a guessed mass.

- Reconcile structured TOGO rows with their full source comment and the exact primary-publication variant before asserting replacement values.
- Use source-specific evidence for percentage basis, dilution scope and any solidifier amount; unresolved quantities must remain explicit.
- Run focused schema, strict, term and reference validators after separately authorized maintained-input edits; then regenerate and run just verify-merges and just audit-merge-freshness.

### a3

Resolve the intended physical-state representation and obtain exact variant-specific solidifier evidence. Do not substitute a customary agar amount.

- Reconcile structured TOGO rows with their full source comment and the exact primary-publication variant before asserting replacement values.
- Use source-specific evidence for percentage basis, dilution scope and any solidifier amount; unresolved quantities must remain explicit.
- Run focused schema, strict, term and reference validators after separately authorized maintained-input edits; then regenerate and run just verify-merges and just audit-merge-freshness.

### a4

Attach short exact excerpts and source locators at the narrowest relevant claims, including contrary context, before regeneration. Retain historical repairs as append-only provenance.

- Reconcile structured TOGO rows with their full source comment and the exact primary-publication variant before asserting replacement values.
- Use source-specific evidence for percentage basis, dilution scope and any solidifier amount; unresolved quantities must remain explicit.
- Run focused schema, strict, term and reference validators after separately authorized maintained-input edits; then regenerate and run just verify-merges and just audit-merge-freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_10_strength_ytss_agar.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_10_strength_ytss_agar.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_10_strength_ytss_agar.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch004/035/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/035/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_10_strength_ytss_agar.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_10_strength_ytss_agar.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2318; meta; complete components[0].items; comments[0] | supports | M2318 has four numeric component rows and a comment explicitly distinguishing a diluted agar isolation medium from a full-strength parenthetical formulation. Metadata has no original-source URL. The structured percentages lack an explicit mass/volume basis. |
| paper | https://userpages.umbc.edu/~belas/Documents/070724%20AEM%20Moran%20et%20al%20published.pdf; Published page 4559: title/DOI and Materials and Methods, Organisms paragraph | supports | Moran et al., Ecological Genomics of Marine Roseobacters, Applied and Environmental Microbiology 73 (2007), 4559–4569; DOI 10.1128/AEM.02580-06 is printed in the PDF. The medium passage matches the TOGO comment and distinguishes the named diluted agar variant from its full-strength parent. |
| repair | scripts/repair_sparse_top_score15.py; TARGETS entry for CultureMech:008905, lines 95–133 | context_only | The maintained repair specification corrects water and adds yeast identity/source notes, but retains the two percentages and labels them as the diluted medium. Its comment extraction misses the parenthetical scope; current owner history reflects this repair. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS identifier, label, definition/annotation and obsolete flag | supports | CHEBI:15377 resolves to water. This is the sole target primary term. |
| foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426; Exact OLS identifier, label, definition/annotation and obsolete flag | supports | FOODON:03315426 resolves to yeast extract. This valid FoodOn mapping occurs only in the maintained owner, not the generated target; no promotion into target is implied. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Live preferred-term rows for target secondary CHEBI:15377; pinned metadata captured | supports | [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}] |
| id-search | repository checkout; Exact top-level CultureMech:008905 lookup with rg --no-ignore --hidden | supports | Exactly one maintained owner and its generated copy were found. Both complete files were read; all four ingredients and history/source fields compared. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact one-tenth-strength formulation, dilution scope, percentage basis and agar amount are not established by the inspected source passage. No customary recipe values are substituted.
- Only the original article metadata and relevant medium description were used; unrelated genomic, pathogenicity and other-organism content does not support this medium. No new growth assertion or organism mapping is added.
- TOGO HTML is a JavaScript shell. Its inspected API retains the relevant source prose; the publication was read through the author-hosted published PDF after publisher/PMC access was inconsistent.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T040821Z-culturemech-008905-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_10_strength_ytss_agar (CultureMech:008905)'
started_at: '2026-10-20T04:06:26Z'
finished_at: '2026-10-20T04:08:21Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or alter these assessed recipe bytes.
    This is an independent source-based agent review, not experimental verification.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The target correctly identifies TOGO M2318 but conflates its named diluted
  agar variant with the full-strength formulation described in source prose. It also
  retains an obsolete water mass unit, despite a maintained correction, and lacks
  agar/solid-state representation. Percent basis and the exact diluted formulation
  remain unresolved; no numerical replacement is inferred.
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
  - path: data/merge_yaml/merged/1_10_strength_ytss_agar.yaml
    sha256: 2be91ce624ae7cb77c6b789e24e2f7a93755b63068e3d763a505734544e4e068
    role: target
  - path: data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml
    sha256: ea46e2fc620b4f8a18a14ea9a94737f5762318f0e36f34919987af4fce58b051
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
  - path: scripts/repair_sparse_top_score15.py
    sha256: eb1ade260b2866a213ede49213e8b394b65b0409e86eac6810cbd5700dbec6eb
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
  selection: Record 35 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008905
targets:
- target_id: CultureMech:008905
  path: data/merge_yaml/merged/1_10_strength_ytss_agar.yaml
  label: 1_10_strength_ytss_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_10_strength_ytss_agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008905
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_10_strength_ytss_agar.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch004/035/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/035/strict.tsv"
  target_ids:
  - CultureMech:008905
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_10_strength_ytss_agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008905
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_10_strength_ytss_agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008905
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
  - CultureMech:008905
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_10_strength_ytss_agar.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-20T04:08:21Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T04:08:21Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_10_strength_ytss_agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T04:06:27.754949Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_10_strength_ytss_agar.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch004/035/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-20T04:06:29.151226Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/035/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_10_strength_ytss_agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T04:06:31.174965Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_10_strength_ytss_agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T04:06:32.232327Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2318
  locator: meta; complete components[0].items; comments[0]
  accessed_at: '2026-10-20T04:06:34.458123Z'
  support: supports
  summary: M2318 has four numeric component rows and a comment explicitly distinguishing
    a diluted agar isolation medium from a full-strength parenthetical formulation.
    Metadata has no original-source URL. The structured percentages lack an explicit
    mass/volume basis.
  snapshot_sha256: 59b31da56d34d26486d7d3b4f5ce8ef596718a59b2d66eb803a06cad06fef7cc
- evidence_id: paper
  kind: primary_source
  reference: https://userpages.umbc.edu/~belas/Documents/070724%20AEM%20Moran%20et%20al%20published.pdf
  locator: 'Published page 4559: title/DOI and Materials and Methods, Organisms paragraph'
  accessed_at: '2026-10-20T04:08:21Z'
  support: supports
  summary: Moran et al., Ecological Genomics of Marine Roseobacters, Applied and Environmental
    Microbiology 73 (2007), 4559–4569; DOI 10.1128/AEM.02580-06 is printed in the
    PDF. The medium passage matches the TOGO comment and distinguishes the named diluted
    agar variant from its full-strength parent.
  quote: full strength YTSS is 0.4% yeast extract plus 0.25% tryptone
- evidence_id: repair
  kind: record_content
  reference: scripts/repair_sparse_top_score15.py
  locator: TARGETS entry for CultureMech:008905, lines 95–133
  accessed_at: '2026-10-20T04:08:21Z'
  support: context_only
  summary: The maintained repair specification corrects water and adds yeast identity/source
    notes, but retains the two percentages and labels them as the diluted medium.
    Its comment extraction misses the parenthetical scope; current owner history reflects
    this repair.
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS identifier, label, definition/annotation and obsolete flag
  accessed_at: '2026-10-20T04:00:00.223561Z'
  support: supports
  summary: CHEBI:15377 resolves to water. This is the sole target primary term.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: foodon03315426
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426
  locator: Exact OLS identifier, label, definition/annotation and obsolete flag
  accessed_at: '2026-10-20T04:06:35.111654Z'
  support: supports
  summary: FOODON:03315426 resolves to yeast extract. This valid FoodOn mapping occurs
    only in the maintained owner, not the generated target; no promotion into target
    is implied.
  snapshot_sha256: cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Live preferred-term rows for target secondary CHEBI:15377; pinned metadata
    captured
  accessed_at: '2026-10-20T04:08:21Z'
  support: supports
  summary: '[{"label": "Distilled water", "match_type": "preferred_term", "identifier":
    "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level CultureMech:008905 lookup with rg --no-ignore --hidden
  accessed_at: '2026-10-20T04:08:21Z'
  support: supports
  summary: Exactly one maintained owner and its generated copy were found. Both complete
    files were read; all four ingredients and history/source fields compared.
  search_scope: Whole checkout including ignored and hidden files; identical ID across
    normalized/generated layers is expected.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008905
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Accession, medium variant and source scope
  outcome: concern
  summary: The selected target and owner resolve to M2318, but source-comment scope
    contradicts the formulation attribution used by the record and repair script.
  target_ids:
  - CultureMech:008905
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper
  - repair
  - id-search
  details: The review target is unambiguous even though its scientific formulation
    is inconsistent. No arbitrary replacement identity, calculated diluted recipe
    or duplicate merge is proposed. The complete source comment must be carried into
    future curation rather than relying on component rows alone.
- assessment_id: water
  area: quantity
  topic: ingredients[0].concentration
  outcome: concern
  summary: 'correct: the target has 1 G_PER_L while TOGO supplies 1 L water. The maintained
    owner already has a volume-based representation; regeneration must not restore
    the old mass unit.'
  target_ids:
  - CultureMech:008905
  evidence_ids:
  - record
  - owner-0
  - togo
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Water volume must not be represented as a guessed mass concentration
    evidence_ids:
    - togo
- assessment_id: amount-1
  area: quantity
  topic: 'ingredients[1].concentration: yeast extract'
  outcome: concern
  summary: 'conflict: the numeric component entry agrees with the record, but its
    applicability to the named variant and its PERCENT_W_V basis are not supported.'
  target_ids:
  - CultureMech:008905
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper
  details: Do not compute a final replacement from the name alone. Resolve both variant
    scope and percentage basis in source-specific evidence before changing an amount.
  dimensions:
  - name: concentration_decision
    value: conflict
    definition: Structured database row and surrounding source scope disagree; percent
      basis is unspecified
    evidence_ids:
    - togo
    - paper
- assessment_id: amount-3
  area: quantity
  topic: 'ingredients[3].concentration: tryptone'
  outcome: concern
  summary: 'conflict: the numeric component entry agrees with the record, but its
    applicability to the named variant and its PERCENT_W_V basis are not supported.'
  target_ids:
  - CultureMech:008905
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper
  details: Do not compute a final replacement from the name alone. Resolve both variant
    scope and percentage basis in source-specific evidence before changing an amount.
  dimensions:
  - name: concentration_decision
    value: conflict
    definition: Structured database row and surrounding source scope disagree; percent
      basis is unspecified
    evidence_ids:
    - togo
    - paper
- assessment_id: salt
  area: quantity
  topic: ingredients[2].concentration
  outcome: concern
  summary: 'conflict: 20 G_PER_L reproduces the database row and parent-formulation
    prose, but its applicability to the diluted named variant is not established.'
  target_ids:
  - CultureMech:008905
  evidence_ids:
  - record
  - togo
  - paper
  details: Do not assume either that sea salts are diluted with organic nutrients
    or that salt strength is held constant. Sea salts are an undefined commercial/mineral
    mixture here; no exact salt composition, supplier or alternative ontology identity
    is inferred.
  dimensions:
  - name: concentration_decision
    value: conflict
    definition: Source value exists but its variant applicability remains unresolved
    evidence_ids:
    - togo
    - paper
- assessment_id: chemistry
  area: grounding
  topic: Ingredient identities and linkage
  outcome: supported
  summary: The target water CHEBI identity and secondary MIM key resolve. The three
    complex mixtures remain ungrounded, rather than assigned invented single-molecule
    IDs. The owner’s added FoodOn yeast identity is valid.
  target_ids:
  - CultureMech:008905
  evidence_ids:
  - record
  - owner-0
  - chebi15377
  - foodon03315426
  - mim
  details: Four direct ingredient instances; one primary CHEBI and one secondary MIM
    CHEBI link give 1/4 or 25% coverage each, on a 0–100 linkage scale. Owner mapping
    coverage is separate from target coverage. Current schema/term passes do not establish
    the missing formulation details.
- assessment_id: state
  area: representation
  topic: Physical state and missing solidifier
  outcome: concern
  summary: The target and owner say LIQUID and list no solidifier despite the source-specific
    name identifying an agar medium. An actual agar amount is not supplied in the
    inspected passage.
  target_ids:
  - CultureMech:008905
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper
  details: Report missing representation and unresolved dose together; do not infer
    a typical agar concentration. There are no stock solution descriptors, internal
    recipe links, nested amounts or asserted incubation conditions. Empty preparation/pH
    fields cannot be populated from this passage. Missing data is not a basis to invent
    sterilization, storage or growth conditions.
- assessment_id: scope
  area: scope
  topic: Growth, classifications and annotations
  outcome: supported
  summary: COMPLEX/UNDEFINED fits the mixture ingredients. The target carries only
    a generic cultivation application and database role/property notes, with no taxon,
    strain identifier, mechanistic or transcriptomic assertion.
  target_ids:
  - CultureMech:008905
  evidence_ids:
  - record
  - togo
  details: The article’s relevant isolation context is not promoted into new target-organism
    or universal growth assertions. No taxonomy identifier is guessed. Annotation-only
    role text remains scoped as a database statement; no unrelated literature organism
    is treated as evidence for the target.
- assessment_id: provenance
  area: provenance
  topic: Current owner versus generated snapshot
  outcome: concern
  summary: The owner includes later water correction, FoodOn mapping and source notes
    that the generated target lacks; it still preserves the central source-scope problem.
    Neither local record has scoped concentration excerpts.
  target_ids:
  - CultureMech:008905
  evidence_ids:
  - record
  - owner-0
  - repair
  - togo
  - validate-references
  details: Data-quality flags and the completed repair event are provenance, not scientific
    approval. The target reference check examined zero excerpts. All absence observations
    concern the complete target/owner objects; the whole-checkout search included
    ignored files. No publication, recipe mutation or status promotion is performed.
findings:
- finding_id: f1
  issue_key: culturemech-008905-full-strength-variant-conflation
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Parent formulation is attributed to the diluted variant
  description: The source explicitly labels the quoted formulation full strength;
    the target and repair specification apply it to the diluted name. The percentage
    basis is also unstated. A matching numeric database row cannot resolve that contextual
    contradiction.
  target_ids:
  - CultureMech:008905
  field_paths:
  - name
  - ingredients[1].concentration
  - ingredients[2].concentration
  - ingredients[3].concentration
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper
  - repair
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: culturemech-008905-generated-water-unit-stale
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Generated water unit remains wrong after owner correction
  description: The target retains 1 G_PER_L for source water given in liters. The
    maintained owner already records the volume, so this specific correction is stale
    in the derived artifact.
  target_ids:
  - CultureMech:008905
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: culturemech-008905-agar-state-incomplete
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Agar medium is represented as liquid without a solidifier
  description: The source-specific agar identity conflicts with LIQUID and the complete
    four-component ingredient list. The source passage does not quantify agar, so
    the missing amount remains unresolved.
  target_ids:
  - CultureMech:008905
  field_paths:
  - physical_state
  - ingredients
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: culturemech-008905-source-evidence-placement-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source context is not retained as claim-level evidence
  description: The generated target has only a source URL. Owner source notes reproduce
    amounts but lack the decisive surrounding variant context; the target reference
    validator checked zero excerpts.
  target_ids:
  - CultureMech:008905
  field_paths:
  - ingredients[*].evidence
  - references
  - notes
  evidence_ids:
  - record
  - owner-0
  - togo
  - repair
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Correct the maintained variant attribution and owning repair specification
    from the full source context. Preserve unresolved dilution/percentage scope rather
    than inferring replacement numbers.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008905
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Reconcile structured TOGO rows with their full source comment and the exact primary-publication
    variant before asserting replacement values.
  - Use source-specific evidence for percentage basis, dilution scope and any solidifier
    amount; unresolved quantities must remain explicit.
  - Run focused schema, strict, term and reference validators after separately authorized
    maintained-input edits; then regenerate and run just verify-merges and just audit-merge-freshness.
- action_id: a2
  description: Preserve the owner’s source-volume correction and regenerate after
    resolving remaining owner issues; do not convert water to a guessed mass.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008905
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Reconcile structured TOGO rows with their full source comment and the exact primary-publication
    variant before asserting replacement values.
  - Use source-specific evidence for percentage basis, dilution scope and any solidifier
    amount; unresolved quantities must remain explicit.
  - Run focused schema, strict, term and reference validators after separately authorized
    maintained-input edits; then regenerate and run just verify-merges and just audit-merge-freshness.
- action_id: a3
  description: Resolve the intended physical-state representation and obtain exact
    variant-specific solidifier evidence. Do not substitute a customary agar amount.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008905
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Reconcile structured TOGO rows with their full source comment and the exact primary-publication
    variant before asserting replacement values.
  - Use source-specific evidence for percentage basis, dilution scope and any solidifier
    amount; unresolved quantities must remain explicit.
  - Run focused schema, strict, term and reference validators after separately authorized
    maintained-input edits; then regenerate and run just verify-merges and just audit-merge-freshness.
- action_id: a4
  description: Attach short exact excerpts and source locators at the narrowest relevant
    claims, including contrary context, before regeneration. Retain historical repairs
    as append-only provenance.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008905
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_strength_ytss_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Reconcile structured TOGO rows with their full source comment and the exact primary-publication
    variant before asserting replacement values.
  - Use source-specific evidence for percentage basis, dilution scope and any solidifier
    amount; unresolved quantities must remain explicit.
  - Run focused schema, strict, term and reference validators after separately authorized
    maintained-input edits; then regenerate and run just verify-merges and just audit-merge-freshness.
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- The exact one-tenth-strength formulation, dilution scope, percentage basis and agar
  amount are not established by the inspected source passage. No customary recipe
  values are substituted.
- Only the original article metadata and relevant medium description were used; unrelated
  genomic, pathogenicity and other-organism content does not support this medium.
  No new growth assertion or organism mapping is added.
- TOGO HTML is a JavaScript shell. Its inspected API retains the relevant source prose;
  the publication was read through the author-hosted published PDF after publisher/PMC
  access was inconsistent.
tags:
- unreviewed-records
- batch-004
- generated-medium
```
