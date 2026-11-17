# Source and formulation review: 229 (CultureMech:007479)

- Review: 20261021T071156Z-culturemech-007479-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T06:57:12Z
- Finished UTC: 2026-10-21T07:11:56Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The target is the generated NBRC228 Bennett's Agar record under local name229. Its two malformed ingredient rows cannot represent the six-component source recipe. The maintained owner has recovered formulation, title and pH, but unsupported importer preparation defaults remain in both layers.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 69; batch 007 item 9 of 10, selected in Python lexicographic repository-relative path order from the current uncovered merged corpus. The prior six validated batch lists contain 60 distinct merged target paths. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c has 40 validated baseline bundles covering 2 current merged paths. The union with prior batches covers 62 of 6320 current merged paths before this batch. This target path occurs in neither set. Task ordinals continue the saved-review sequence, not global path ranks after upstream corpus or coverage changes. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007479 | data/merge_yaml/merged/229.yaml | generated | 229 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007479 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007479 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch007/069/strict.tsv |
| validate-terms | passed | True | CultureMech:007479 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007479 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007479 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007479.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:007479.

0 primary CHEBI identities resolve with matching labels; 0 of 0 current secondary keys have live pinned-index rows. Unresolved keys: [].

2 direct ingredient instances; CHEBI-primary instance linkage 0/2 (0.00%), verified secondary coverage 0/2 (0.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Stable record versus local numeric display name

identity: supported. Targets: CultureMech:007479.

The exact target and merge owner resolve the intended NBRC228 medium. Current primary title is Bennett's Agar. Local229 is a historical filename/name, not the provider accession; the history correctly names228.

### Every target row and all six recovered owner ingredients

quantity: concern. Targets: CultureMech:007479.

correct: row0 concatenates the entire recipe and pH into a preferred_term with VARIABLE amount; row1 has an empty name and nonnumeric Yeast extract concentration. Neither row is a valid ingredient assertion despite schema success. The six owner quantities agree with the source numerals; retain source grams plus1L water as their nominal batch basis, not an independently measured final volume. No stock dose is asserted.

[["Yeast extract", "1", "G_PER_L"], ["Beef extract", "1", "G_PER_L"], ["N-Z-Amine A", "2", "G_PER_L"], ["Glucose", "10", "G_PER_L"], ["Distilled water", "1", "L"], ["Agar", "20", "G_PER_L"]]

### Title, pH, mappings, references and later history

completeness: concern. Targets: CultureMech:007479.

Source-supported title, pH7.3, medium term, three ingredient identities and references exist in the owner after the target merge event, but are absent from the target. The owner retains the three undefined nutrient mixtures without invented pure-molecule IDs.

### Imported generic preparation defaults

evidence: concern. Targets: CultureMech:007479.

unsupported: the primary table has a blank Comment; it provides no dissolve/autoclave protocol. pH7.3 is source-supported, but the conditional phrase adjust pH if needed is a fallback rather than the source instruction. Both files retain autoclaving mislabeled DISSOLVE. Do not fill absent time/temperature from convention.

### Complex agar medium and growth limits

scope: supported. Targets: CultureMech:007479.

COMPLEX/UNDEFINED and SOLID_AGAR agree with the six-component source recipe. No organism, growth experiment, solution reference or incubation conditions are asserted; generic cultivation supplies no strain-specific evidence.

### Malformed target versus recovered owner linkage

grounding: concern. Targets: CultureMech:007479.

The target has0/2 primary and0/2 secondary links (0% of two malformed rows, not a denominator of valid ingredient identities). The owner has3/6 primary and3/6 secondary CHEBI keys, all matching the inspected chemical identities; mixtures remain ungrounded. Linkage is not a scientific accuracy metric.

### History and narrow evidence

evidence: concern. Targets: CultureMech:007479.

All target/owner timestamps parse with timezones and the owner records later recovery/repair. Its source reference is reachable but lacks exact narrow evidence for amounts/preparation. Target reference validation examined zero excerpts.

## Findings

### f1: Generated formulation consists of malformed rows

blocker / open / confirmed; issue key: CM007479-malformed-generated-formulation.

A whole recipe blob and an empty ingredient carrying a textual concentration replace the actual six source ingredients. This invalid scientific representation survives deterministic schema checks.

### f2: Source-supported identity and pH corrections have not reached the target

major / open / confirmed; issue key: CM007479-stale-identity-ph-mappings.

The owner contains the official Bennett's Agar title, NBRC228 source term, pH7.3, three mappings and reference context that the generated target lacks.

### f3: Importer fallback preparation is presented without source support

major / open / confirmed; issue key: CM007479-unsupported-preparation-defaults.

Both layers retain generic instructions absent from the inspected primary record. The autoclaving description is also categorized as DISSOLVE.

### f4: Recovered source provenance lacks narrow claim excerpts

minor / open / confirmed; issue key: CM007479-claim-evidence-gap.

The maintained owner links the correct primary page but does not attach exact support to quantities or preparation, and the generated record lacks the later reference.

## Recommended Actions And Acceptance Checks

### a1

Verify every recovered owner ingredient and source batch basis, resolve retained preparation defaults, then regenerate the derived formulation; do not hand-edit the merged YAML.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Verify the maintained corrections against NBRC228 and current ontology labels, then regenerate and confirm retention. Keep the stable CultureMech ID and source accession228.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Remove unsupported protocol assertions or replace them only with verified source-specific evidence. Preserve the supported pH while resolving the importer default/action-classification behavior.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Add source metadata and short exact claim-scoped excerpts after owner verification, then regenerate without rewriting previous history.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/229.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_229.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/229.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/229.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch007/069/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch007/069/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/229.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/229.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/229.yaml:1:id: CultureMech:007479<br>./data/normalized_yaml/bacterial/NBRC_229.yaml:1:id: CultureMech:007479<br> |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {} |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=228; Medium No.228; Medium; Composition; pH; Comment | supports | Complete official medium228 table inspected: Bennett's Agar; yeast extract1g, beef extract1g, N-Z-Amine A2g, glucose10g, water1L and agar20g; pH7.3. The Comment field supplies no preparation instruction or final-volume measurement. |
| legacy | http://www.nbrc.nite.go.jp/NBRC2/NBRCMediumDetailServlet?NO=228; Legacy servlet redirect; complete current medium detail | supports | The legacy URL retained in import history resolves to the current medium228 page with the same name, formulation and pH. A local filename229 is not evidence that the source accession should change to229. |
| owner-chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact maintained ingredient identifier, canonical label and obsolete status | supports | CHEBI:17234 resolves to glucose; the maintained identity and canonical label match. |
| owner-chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact maintained ingredient identifier, canonical label and obsolete status | supports | CHEBI:15377 resolves to water; the maintained identity and canonical label match. |
| owner-chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact maintained ingredient identifier, canonical label and obsolete status | supports | CHEBI:2509 resolves to agar; the maintained identity and canonical label match. |
| context | Complete target and maintained owner; All ingredient rows, pH, source term and timestamps | supports | {"owner_six_row_signature": [["Yeast extract", "1", "G_PER_L"], ["Beef extract", "1", "G_PER_L"], ["N-Z-Amine A", "2", "G_PER_L"], ["Glucose", "10", "G_PER_L"], ["Distilled water", "1", "L"], ["Agar", "20", "G_PER_L"]], "target_rows": [{"preferred_term": "Yeast extract1gBeef extract1gN-Z-Amine A2gGlucose10gDistilled water1LAgar20gpH 7.3", "concentration": {"value": "variable", "unit": "VARIABLE"}}, {"preferred_term": "", "concentration": {"value": "Yeast extract", "unit": "G_PER_L"}}], "target_history_count": 6, "owner_history_count": 8, "all_history_timestamps_timezone_bearing": true} |
| importer | src/culturemech/import/nbrc_importer.py; _map_preparation_steps, lines260-305 | supports | The inspected current importer supplies these same three fallback instructions when preparation is absent. Its autoclave substring does not match autoclaving, leaving that fallback action DISSOLVE. Code inspection explains a current failure mode; it is not a reconstruction of the historical execution. |
| repair | scripts/repair_nbrc_229_score15.py; Entire script; fixed target/source identity, six-row guard, title/pH/reference/mapping updates | supports | The maintained repair script is restricted to CultureMech007479 in NBRC_229.yaml and NBRC228. Its required six-row signature and added title/pH/mappings agree with the maintained owner and current primary table. It does not supply primary evidence for the retained preparation defaults. Script was read, not executed. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Current NBRC pages and retained code/history were inspected; the historical scraper execution was not reconstructed. Source gram amounts are assessed on their literal water-batch basis, with no inferred measured final volume.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T071156Z-culturemech-007479-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 229 (CultureMech:007479)'
started_at: '2026-10-21T06:57:12Z'
finished_at: '2026-10-21T07:11:56Z'
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
summary: The target is the generated NBRC228 Bennett's Agar record under local name229.
  Its two malformed ingredient rows cannot represent the six-component source recipe.
  The maintained owner has recovered formulation, title and pH, but unsupported importer
  preparation defaults remain in both layers.
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
  - path: data/merge_yaml/merged/229.yaml
    sha256: edded140affa25d4e44699b07350e4ffcda9e934c8300252c8a0ea325b37bae1
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_229.yaml
    sha256: d9526eac3fc95d4d14d74761d1475cb4d07ec1b4488636392d459b12ca277e93
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
  - path: scripts/repair_nbrc_229_score15.py
    sha256: 67b5a6d71e56c999f98b524089c3782f4bd3f80bfc76f126784bddb6d6665708
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
  selection: Task review 69; batch 007 item 9 of 10, selected in Python lexicographic
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
  - CultureMech:007479
targets:
- target_id: CultureMech:007479
  path: data/merge_yaml/merged/229.yaml
  label: '229'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_229.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/229.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007479
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/229.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch007/069/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch007/069/strict.tsv"
  target_ids:
  - CultureMech:007479
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/229.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007479
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/229.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007479
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
  - CultureMech:007479
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/229.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T07:11:55Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_229.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T07:11:55Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/229.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:59:15.990735Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/229.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch007/069/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T06:59:20.559737Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch007/069/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/229.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:59:25.847043Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/229.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:59:29.154987Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T07:11:55Z'
  support: supports
  summary: './data/merge_yaml/merged/229.yaml:1:id: CultureMech:007479

    ./data/normalized_yaml/bacterial/NBRC_229.yaml:1:id: CultureMech:007479

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T07:11:55Z'
  support: supports
  summary: '{}'
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=228
  locator: Medium No.228; Medium; Composition; pH; Comment
  accessed_at: '2026-10-21T06:57:49.936491Z'
  support: supports
  summary: 'Complete official medium228 table inspected: Bennett''s Agar; yeast extract1g,
    beef extract1g, N-Z-Amine A2g, glucose10g, water1L and agar20g; pH7.3. The Comment
    field supplies no preparation instruction or final-volume measurement.'
  quote: Medium Bennett's Agar
  snapshot_sha256: d8ad6f7c2cc5374d3fc8d99f10d233a4ce288859f70769d6730adf379e879117
- evidence_id: legacy
  kind: primary_source
  reference: http://www.nbrc.nite.go.jp/NBRC2/NBRCMediumDetailServlet?NO=228
  locator: Legacy servlet redirect; complete current medium detail
  accessed_at: '2026-10-21T06:57:44.861051Z'
  support: supports
  summary: The legacy URL retained in import history resolves to the current medium228
    page with the same name, formulation and pH. A local filename229 is not evidence
    that the source accession should change to229.
  snapshot_sha256: d8ad6f7c2cc5374d3fc8d99f10d233a4ce288859f70769d6730adf379e879117
- evidence_id: owner-chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact maintained ingredient identifier, canonical label and obsolete status
  accessed_at: '2026-10-20T03:57:32.595833Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose; the maintained identity and canonical
    label match.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: owner-chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact maintained ingredient identifier, canonical label and obsolete status
  accessed_at: '2026-10-20T04:00:00.223561Z'
  support: supports
  summary: CHEBI:15377 resolves to water; the maintained identity and canonical label
    match.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: owner-chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact maintained ingredient identifier, canonical label and obsolete status
  accessed_at: '2026-10-20T07:07:41.448510Z'
  support: supports
  summary: CHEBI:2509 resolves to agar; the maintained identity and canonical label
    match.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: context
  kind: validation
  reference: Complete target and maintained owner
  locator: All ingredient rows, pH, source term and timestamps
  accessed_at: '2026-10-21T07:11:55Z'
  support: supports
  summary: '{"owner_six_row_signature": [["Yeast extract", "1", "G_PER_L"], ["Beef
    extract", "1", "G_PER_L"], ["N-Z-Amine A", "2", "G_PER_L"], ["Glucose", "10",
    "G_PER_L"], ["Distilled water", "1", "L"], ["Agar", "20", "G_PER_L"]], "target_rows":
    [{"preferred_term": "Yeast extract1gBeef extract1gN-Z-Amine A2gGlucose10gDistilled
    water1LAgar20gpH 7.3", "concentration": {"value": "variable", "unit": "VARIABLE"}},
    {"preferred_term": "", "concentration": {"value": "Yeast extract", "unit": "G_PER_L"}}],
    "target_history_count": 6, "owner_history_count": 8, "all_history_timestamps_timezone_bearing":
    true}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/nbrc_importer.py
  locator: _map_preparation_steps, lines260-305
  accessed_at: '2026-10-21T07:11:55Z'
  support: supports
  summary: The inspected current importer supplies these same three fallback instructions
    when preparation is absent. Its autoclave substring does not match autoclaving,
    leaving that fallback action DISSOLVE. Code inspection explains a current failure
    mode; it is not a reconstruction of the historical execution.
- evidence_id: repair
  kind: record_content
  reference: scripts/repair_nbrc_229_score15.py
  locator: Entire script; fixed target/source identity, six-row guard, title/pH/reference/mapping
    updates
  accessed_at: '2026-10-21T07:11:55Z'
  support: supports
  summary: The maintained repair script is restricted to CultureMech007479 in NBRC_229.yaml
    and NBRC228. Its required six-row signature and added title/pH/mappings agree
    with the maintained owner and current primary table. It does not supply primary
    evidence for the retained preparation defaults. Script was read, not executed.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007479
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
  - CultureMech:007479
  evidence_ids:
  - record
  - mim
  details: 2 direct ingredient instances; CHEBI-primary instance linkage 0/2 (0.00%),
    verified secondary coverage 0/2 (0.00%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Stable record versus local numeric display name
  outcome: supported
  summary: The exact target and merge owner resolve the intended NBRC228 medium. Current
    primary title is Bennett's Agar. Local229 is a historical filename/name, not the
    provider accession; the history correctly names228.
  target_ids:
  - CultureMech:007479
  evidence_ids:
  - record
  - owner-0
  - id-search
  - nbrc
  - legacy
  - repair
- assessment_id: formulation
  area: quantity
  topic: Every target row and all six recovered owner ingredients
  outcome: concern
  summary: 'correct: row0 concatenates the entire recipe and pH into a preferred_term
    with VARIABLE amount; row1 has an empty name and nonnumeric Yeast extract concentration.
    Neither row is a valid ingredient assertion despite schema success. The six owner
    quantities agree with the source numerals; retain source grams plus1L water as
    their nominal batch basis, not an independently measured final volume. No stock
    dose is asserted.'
  target_ids:
  - CultureMech:007479
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - context
  details: '[["Yeast extract", "1", "G_PER_L"], ["Beef extract", "1", "G_PER_L"],
    ["N-Z-Amine A", "2", "G_PER_L"], ["Glucose", "10", "G_PER_L"], ["Distilled water",
    "1", "L"], ["Agar", "20", "G_PER_L"]]'
- assessment_id: freshness
  area: completeness
  topic: Title, pH, mappings, references and later history
  outcome: concern
  summary: Source-supported title, pH7.3, medium term, three ingredient identities
    and references exist in the owner after the target merge event, but are absent
    from the target. The owner retains the three undefined nutrient mixtures without
    invented pure-molecule IDs.
  target_ids:
  - CultureMech:007479
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - context
  - repair
  - owner-chebi17234
  - owner-chebi15377
  - owner-chebi2509
- assessment_id: preparation
  area: evidence
  topic: Imported generic preparation defaults
  outcome: concern
  summary: 'unsupported: the primary table has a blank Comment; it provides no dissolve/autoclave
    protocol. pH7.3 is source-supported, but the conditional phrase adjust pH if needed
    is a fallback rather than the source instruction. Both files retain autoclaving
    mislabeled DISSOLVE. Do not fill absent time/temperature from convention.'
  target_ids:
  - CultureMech:007479
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - legacy
  - importer
- assessment_id: classification
  area: scope
  topic: Complex agar medium and growth limits
  outcome: supported
  summary: COMPLEX/UNDEFINED and SOLID_AGAR agree with the six-component source recipe.
    No organism, growth experiment, solution reference or incubation conditions are
    asserted; generic cultivation supplies no strain-specific evidence.
  target_ids:
  - CultureMech:007479
  evidence_ids:
  - record
  - nbrc
- assessment_id: mapping-scope
  area: grounding
  topic: Malformed target versus recovered owner linkage
  outcome: concern
  summary: The target has0/2 primary and0/2 secondary links (0% of two malformed rows,
    not a denominator of valid ingredient identities). The owner has3/6 primary and3/6
    secondary CHEBI keys, all matching the inspected chemical identities; mixtures
    remain ungrounded. Linkage is not a scientific accuracy metric.
  target_ids:
  - CultureMech:007479
  evidence_ids:
  - record
  - owner-0
  - mim
  - owner-chebi17234
  - owner-chebi15377
  - owner-chebi2509
- assessment_id: audit
  area: evidence
  topic: History and narrow evidence
  outcome: concern
  summary: All target/owner timestamps parse with timezones and the owner records
    later recovery/repair. Its source reference is reachable but lacks exact narrow
    evidence for amounts/preparation. Target reference validation examined zero excerpts.
  target_ids:
  - CultureMech:007479
  evidence_ids:
  - record
  - owner-0
  - context
  - validate-references
  - nbrc
findings:
- finding_id: f1
  issue_key: CM007479-malformed-generated-formulation
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated formulation consists of malformed rows
  description: A whole recipe blob and an empty ingredient carrying a textual concentration
    replace the actual six source ingredients. This invalid scientific representation
    survives deterministic schema checks.
  target_ids:
  - CultureMech:007479
  field_paths:
  - ingredients[0]
  - ingredients[1]
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_229.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM007479-stale-identity-ph-mappings
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source-supported identity and pH corrections have not reached the target
  description: The owner contains the official Bennett's Agar title, NBRC228 source
    term, pH7.3, three mappings and reference context that the generated target lacks.
  target_ids:
  - CultureMech:007479
  field_paths:
  - name
  - original_name
  - media_term
  - ph_value
  - ingredients[*].term
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - context
  - repair
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_229.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM007479-unsupported-preparation-defaults
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Importer fallback preparation is presented without source support
  description: Both layers retain generic instructions absent from the inspected primary
    record. The autoclaving description is also categorized as DISSOLVE.
  target_ids:
  - CultureMech:007479
  field_paths:
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - legacy
  - importer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_229.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: CM007479-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Recovered source provenance lacks narrow claim excerpts
  description: The maintained owner links the correct primary page but does not attach
    exact support to quantities or preparation, and the generated record lacks the
    later reference.
  target_ids:
  - CultureMech:007479
  field_paths:
  - references
  - ingredients[*].evidence
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_229.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Verify every recovered owner ingredient and source batch basis, resolve
    retained preparation defaults, then regenerate the derived formulation; do not
    hand-edit the merged YAML.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007479
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_229.yaml
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
  description: Verify the maintained corrections against NBRC228 and current ontology
    labels, then regenerate and confirm retention. Keep the stable CultureMech ID
    and source accession228.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007479
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_229.yaml
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
  description: Remove unsupported protocol assertions or replace them only with verified
    source-specific evidence. Preserve the supported pH while resolving the importer
    default/action-classification behavior.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007479
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_229.yaml
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
  description: Add source metadata and short exact claim-scoped excerpts after owner
    verification, then regenerate without rewriting previous history.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007479
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_229.yaml
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
- Current NBRC pages and retained code/history were inspected; the historical scraper
  execution was not reconstructed. Source gram amounts are assessed on their literal
  water-batch basis, with no inferred measured final volume.
tags:
- unreviewed-records
- batch-007
- generated-medium
```
