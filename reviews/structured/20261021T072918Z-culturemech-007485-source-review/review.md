# Source and formulation review: 296 (CultureMech:007485)

- Review: 20261021T072918Z-culturemech-007485-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T07:20:51Z
- Finished UTC: 2026-10-21T07:29:18Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated local296 record denotes unnamed NBRC294 but has two malformed ingredient rows and generic preparation. The owner restores Bacto Yeast Extract(Difco), water1L, pH5.0 and adjustment with1N HCl while removing unsupported autoclaving; these source-backed corrections have not reached the generated target.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 77; batch 008 item 7 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding seven task batches contain 70 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 72 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007485 | data/merge_yaml/merged/296.yaml | generated | 296 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007485 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007485 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/077/strict.tsv |
| validate-terms | passed | True | CultureMech:007485 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007485 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007485 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007485.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:007485.

0 primary CHEBI identities resolve with matching labels; 0 of 0 current secondary keys have live pinned-index rows. Unresolved keys: [].

2 direct ingredient instances; CHEBI-primary instance linkage 0/2 (0.00%), verified secondary coverage 0/2 (0.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Unnamed NBRC294 and local import296

identity: supported. Targets: CultureMech:007485.

Stable ID, merge owner and explicit import history identify NBRC294. The primary Medium title is blank, so no official name is invented. Owner nbrc.medium:294 and its reference match the live accession.

### Both malformed rows and complete source formulation

quantity: concern. Targets: CultureMech:007485.

correct: the target embeds the recipe and adjustment instruction in a VARIABLE ingredient plus a blank row with a textual concentration. The owner recovers the supplied yeast-extract amount and literal water1L. Its5g/L denotes a nominal one-liter-water batch, not independently measured final volume.

[["Bacto Yeast Extract (Difco)", "5", "G_PER_L"], ["Distilled water", "1", "L"]]

### Acid strength, amount and endpoint

quantity: supported. Targets: CultureMech:007485.

verified/not_quantified: source1N HCl is the strength of the pH-adjustment reagent; pH5.0 is the endpoint. Neither is a final-medium HCl concentration. No added volume is supplied, so final acid amount, chloride contribution and dilution cannot be calculated. Owner preparation preserves the correct source scope.

### Recovered source metadata and preparation

completeness: concern. Targets: CultureMech:007485.

The generated target omits owner source term, water mapping, pH5.0, exact acid-adjustment procedure, reference and later repair history. It retains unsupported autoclaving and vague conditional pH rather than the source-specific procedure.

### Source mixture and owner water identity

grounding: supported. Targets: CultureMech:007485.

Target primary/secondary linkage is0/2 malformed rows. The owner has1/2 primary CHEBI links(50%) and0/2 secondary links. Water identity resolves; branded yeast extract remains an ungrounded mixture without a guessed pure-molecule identity. Linkage is not a scientific accuracy score.

### Liquid undefined formulation and biological scope

scope: supported. Targets: CultureMech:007485.

LIQUID agrees with the source absence of gelling material, and COMPLEX/UNDEFINED with yeast extract. No organism, stock record, experiment or incubation condition is asserted. Bacterial category is organizational context, not exclusive biological applicability.

### History and narrow evidence

provenance: concern. Targets: CultureMech:007485.

Every target/owner timestamp has a timezone. Source notes and URL identify the formulation but omit exact narrow claim excerpts. The target reference gate examined zero excerpts; it cannot certify source formulation or preparation.

## Findings

### f1: Generated ingredient rows do not represent the source formulation

blocker / open / confirmed; issue key: CM007485-malformed-ingredient-table.

The target contains one full-recipe/acid-instruction text blob with VARIABLE concentration and one blank row with Bacto Yeast Extract(Difco) as the amount.

### f2: Generated target lacks structured source identity and pH

major / open / confirmed; issue key: CM007485-stale-source-ph-metadata.

The source term, water identity, pH5.0, official reference and source-recovery history present in the owner are absent from the target.

### f3: Generated preparation omits the exact acid procedure and asserts unsupported autoclaving

major / open / confirmed; issue key: CM007485-stale-preparation.

The source and owner specify adjustment to pH5.0 with1N HCl. The target instead retains generic fallback text, including unsubstantiated autoclaving classified DISSOLVE.

### f4: Source claims lack narrow excerpts

minor / open / confirmed; issue key: CM007485-claim-evidence-gap.

Owner notes/reference supply provenance but no exact field-level support for quantities, supplied product or acid-adjustment scope.

## Recommended Actions And Acceptance Checks

### a1

Verify the recovered two-component owner against NBRC294 and preserve literal solvent-batch context, then regenerate.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Verify maintained source metadata and batch semantics before regeneration; do not invent an official title for the blank source field.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Regenerate the verified owner preparation and inspect importer fallback behavior. Preserve reagent strength and endpoint without fabricating acid volume or final concentration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach short exact source excerpts to the narrow formulation and preparation claims, separating interpretation from quotation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/296.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_296.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/296.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/296.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch008/077/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/077/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/296.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/296.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/296.yaml:1:id: CultureMech:007485<br>./data/normalized_yaml/bacterial/NBRC_296.yaml:1:id: CultureMech:007485<br> |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {} |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=294; Medium No.294; blank title; complete Composition; adjustment text; Comment | supports | Complete official medium294 page inspected: blank Medium title; Bacto Yeast Extract(Difco)5g, distilled water1L, and adjustment to pH5.0 with1N HCl. Comment is blank. No sterilization protocol or acid addition amount is supplied. |
| legacy | http://www.nbrc.nite.go.jp/NBRC2/NBRCMediumDetailServlet?NO=294; Redirect and complete medium detail | supports | The historical servlet resolves to the same current source294 page and quantities. Local296 does not establish provider accession296. |
| owner-water | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact owner water identifier, canonical label and obsolete flag | supports | CHEBI15377 resolves to water with matching owner label. This validates identity, not final-volume semantics. |
| context | Complete target and maintained owner; Every recovered quantity, preparation instruction, pH and history timestamp | supports | {"owner_quantity_signature": [["Bacto Yeast Extract (Difco)", "5", "G_PER_L"], ["Distilled water", "1", "L"]], "owner_ph": 5.0, "owner_preparation": [{"step_number": 1, "action": "ADJUST_PH", "description": "Adjust pH to 5.0 with 1 N HCl."}], "timezone_bearing_history_counts": [6, 8]} |
| importer | src/culturemech/import/nbrc_importer.py; _map_preparation_steps | supports | Current importer fallback supplies the same generic dissolve/conditional-pH/autoclaving text; its substring handling leaves autoclaving classified DISSOLVE. This current code behavior is not a reconstruction of historical execution. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No source sterilization protocol, acid addition volume, measured final volume or strain-specific growth was established. Historical scraper execution was not reconstructed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T072918Z-culturemech-007485-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 296 (CultureMech:007485)'
started_at: '2026-10-21T07:20:51Z'
finished_at: '2026-10-21T07:29:18Z'
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
summary: The generated local296 record denotes unnamed NBRC294 but has two malformed
  ingredient rows and generic preparation. The owner restores Bacto Yeast Extract(Difco),
  water1L, pH5.0 and adjustment with1N HCl while removing unsupported autoclaving;
  these source-backed corrections have not reached the generated target.
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
  - path: data/merge_yaml/merged/296.yaml
    sha256: cb2184157e480a3ec591be8db9610f9b6e32ea5e66ab08b95a99fd5e644945e5
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_296.yaml
    sha256: ec19e81a78c34f4e2b2ba4a3c547ac30da17766a10bf81798ffdfc122cfa014e
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
  selection: Task review 77; batch 008 item 7 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding seven task batches contain
    70 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 72 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007485
targets:
- target_id: CultureMech:007485
  path: data/merge_yaml/merged/296.yaml
  label: '296'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_296.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/296.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007485
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/296.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch008/077/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/077/strict.tsv"
  target_ids:
  - CultureMech:007485
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/296.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007485
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/296.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007485
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
  - CultureMech:007485
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/296.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T07:29:16Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_296.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T07:29:16Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/296.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:22:11.651538Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/296.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch008/077/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T07:22:15.794729Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/077/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/296.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:22:21.413442Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/296.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:22:22.897687Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T07:29:16Z'
  support: supports
  summary: './data/merge_yaml/merged/296.yaml:1:id: CultureMech:007485

    ./data/normalized_yaml/bacterial/NBRC_296.yaml:1:id: CultureMech:007485

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T07:29:16Z'
  support: supports
  summary: '{}'
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=294
  locator: Medium No.294; blank title; complete Composition; adjustment text; Comment
  accessed_at: '2026-10-21T07:16:26.141020Z'
  support: supports
  summary: 'Complete official medium294 page inspected: blank Medium title; Bacto
    Yeast Extract(Difco)5g, distilled water1L, and adjustment to pH5.0 with1N HCl.
    Comment is blank. No sterilization protocol or acid addition amount is supplied.'
  quote: Adjust pH to 5.0 with 1 N HCl
  snapshot_sha256: 595fca1eaa1bb0001e82b5c733556633f0072f7c1e9f854b96c6b2889ba4dfa7
- evidence_id: legacy
  kind: primary_source
  reference: http://www.nbrc.nite.go.jp/NBRC2/NBRCMediumDetailServlet?NO=294
  locator: Redirect and complete medium detail
  accessed_at: '2026-10-21T07:16:19.829334Z'
  support: supports
  summary: The historical servlet resolves to the same current source294 page and
    quantities. Local296 does not establish provider accession296.
  snapshot_sha256: 595fca1eaa1bb0001e82b5c733556633f0072f7c1e9f854b96c6b2889ba4dfa7
- evidence_id: owner-water
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact owner water identifier, canonical label and obsolete flag
  accessed_at: '2026-10-21T07:15:13.683527Z'
  support: supports
  summary: CHEBI15377 resolves to water with matching owner label. This validates
    identity, not final-volume semantics.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: context
  kind: validation
  reference: Complete target and maintained owner
  locator: Every recovered quantity, preparation instruction, pH and history timestamp
  accessed_at: '2026-10-21T07:29:16Z'
  support: supports
  summary: '{"owner_quantity_signature": [["Bacto Yeast Extract (Difco)", "5", "G_PER_L"],
    ["Distilled water", "1", "L"]], "owner_ph": 5.0, "owner_preparation": [{"step_number":
    1, "action": "ADJUST_PH", "description": "Adjust pH to 5.0 with 1 N HCl."}], "timezone_bearing_history_counts":
    [6, 8]}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/nbrc_importer.py
  locator: _map_preparation_steps
  accessed_at: '2026-10-21T07:29:16Z'
  support: supports
  summary: Current importer fallback supplies the same generic dissolve/conditional-pH/autoclaving
    text; its substring handling leaves autoclaving classified DISSOLVE. This current
    code behavior is not a reconstruction of historical execution.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007485
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
  - CultureMech:007485
  evidence_ids:
  - record
  - mim
  details: 2 direct ingredient instances; CHEBI-primary instance linkage 0/2 (0.00%),
    verified secondary coverage 0/2 (0.00%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Unnamed NBRC294 and local import296
  outcome: supported
  summary: Stable ID, merge owner and explicit import history identify NBRC294. The
    primary Medium title is blank, so no official name is invented. Owner nbrc.medium:294
    and its reference match the live accession.
  target_ids:
  - CultureMech:007485
  evidence_ids:
  - record
  - owner-0
  - id-search
  - nbrc
  - legacy
- assessment_id: quantities
  area: quantity
  topic: Both malformed rows and complete source formulation
  outcome: concern
  summary: 'correct: the target embeds the recipe and adjustment instruction in a
    VARIABLE ingredient plus a blank row with a textual concentration. The owner recovers
    the supplied yeast-extract amount and literal water1L. Its5g/L denotes a nominal
    one-liter-water batch, not independently measured final volume.'
  target_ids:
  - CultureMech:007485
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - context
  details: '[["Bacto Yeast Extract (Difco)", "5", "G_PER_L"], ["Distilled water",
    "1", "L"]]'
- assessment_id: acid
  area: quantity
  topic: Acid strength, amount and endpoint
  outcome: supported
  summary: 'verified/not_quantified: source1N HCl is the strength of the pH-adjustment
    reagent; pH5.0 is the endpoint. Neither is a final-medium HCl concentration. No
    added volume is supplied, so final acid amount, chloride contribution and dilution
    cannot be calculated. Owner preparation preserves the correct source scope.'
  target_ids:
  - CultureMech:007485
  evidence_ids:
  - owner-0
  - nbrc
  - context
- assessment_id: freshness
  area: completeness
  topic: Recovered source metadata and preparation
  outcome: concern
  summary: The generated target omits owner source term, water mapping, pH5.0, exact
    acid-adjustment procedure, reference and later repair history. It retains unsupported
    autoclaving and vague conditional pH rather than the source-specific procedure.
  target_ids:
  - CultureMech:007485
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - context
  - importer
- assessment_id: grounding-scope
  area: grounding
  topic: Source mixture and owner water identity
  outcome: supported
  summary: Target primary/secondary linkage is0/2 malformed rows. The owner has1/2
    primary CHEBI links(50%) and0/2 secondary links. Water identity resolves; branded
    yeast extract remains an ungrounded mixture without a guessed pure-molecule identity.
    Linkage is not a scientific accuracy score.
  target_ids:
  - CultureMech:007485
  evidence_ids:
  - record
  - owner-0
  - owner-water
  - context
- assessment_id: classification
  area: scope
  topic: Liquid undefined formulation and biological scope
  outcome: supported
  summary: LIQUID agrees with the source absence of gelling material, and COMPLEX/UNDEFINED
    with yeast extract. No organism, stock record, experiment or incubation condition
    is asserted. Bacterial category is organizational context, not exclusive biological
    applicability.
  target_ids:
  - CultureMech:007485
  evidence_ids:
  - record
  - owner-0
  - nbrc
- assessment_id: provenance
  area: provenance
  topic: History and narrow evidence
  outcome: concern
  summary: Every target/owner timestamp has a timezone. Source notes and URL identify
    the formulation but omit exact narrow claim excerpts. The target reference gate
    examined zero excerpts; it cannot certify source formulation or preparation.
  target_ids:
  - CultureMech:007485
  evidence_ids:
  - record
  - owner-0
  - context
  - validate-references
findings:
- finding_id: f1
  issue_key: CM007485-malformed-ingredient-table
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated ingredient rows do not represent the source formulation
  description: The target contains one full-recipe/acid-instruction text blob with
    VARIABLE concentration and one blank row with Bacto Yeast Extract(Difco) as the
    amount.
  target_ids:
  - CultureMech:007485
  field_paths:
  - ingredients
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_296.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P1.1
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CM007485-stale-source-ph-metadata
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated target lacks structured source identity and pH
  description: The source term, water identity, pH5.0, official reference and source-recovery
    history present in the owner are absent from the target.
  target_ids:
  - CultureMech:007485
  field_paths:
  - media_term
  - ingredients
  - ph_value
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_296.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM007485-stale-preparation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generated preparation omits the exact acid procedure and asserts unsupported
    autoclaving
  description: The source and owner specify adjustment to pH5.0 with1N HCl. The target
    instead retains generic fallback text, including unsubstantiated autoclaving classified
    DISSOLVE.
  target_ids:
  - CultureMech:007485
  field_paths:
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - context
  - importer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_296.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: CM007485-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source claims lack narrow excerpts
  description: Owner notes/reference supply provenance but no exact field-level support
    for quantities, supplied product or acid-adjustment scope.
  target_ids:
  - CultureMech:007485
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
    path: data/normalized_yaml/bacterial/NBRC_296.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Verify the recovered two-component owner against NBRC294 and preserve
    literal solvent-batch context, then regenerate.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_296.yaml
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
  description: Verify maintained source metadata and batch semantics before regeneration;
    do not invent an official title for the blank source field.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_296.yaml
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
  description: Regenerate the verified owner preparation and inspect importer fallback
    behavior. Preserve reagent strength and endpoint without fabricating acid volume
    or final concentration.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_296.yaml
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
  description: Attach short exact source excerpts to the narrow formulation and preparation
    claims, separating interpretation from quotation.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_296.yaml
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
- No source sterilization protocol, acid addition volume, measured final volume or
  strain-specific growth was established. Historical scraper execution was not reconstructed.
tags:
- unreviewed-records
- batch-008
- generated-medium
```
