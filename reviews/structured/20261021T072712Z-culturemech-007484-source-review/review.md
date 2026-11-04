# Source and formulation review: 280 (CultureMech:007484)

- Review: 20261021T072712Z-culturemech-007484-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T07:17:57Z
- Finished UTC: 2026-10-21T07:27:12Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated local280 record denotes NBRC279 Tryptone Yeast Extract Agar but has malformed ingredient rows. Its owner recovers the five source components, official identity and pH7.0. Both layers retain an unsupported generic autoclave protocol, so owner curation must precede regeneration.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 75; batch 008 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding seven task batches contain 70 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 72 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007484 | data/merge_yaml/merged/280.yaml | generated | 280 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007484 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007484 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/075/strict.tsv |
| validate-terms | passed | True | CultureMech:007484 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007484 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007484 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007484.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:007484.

0 primary CHEBI identities resolve with matching labels; 0 of 0 current secondary keys have live pinned-index rows. Unresolved keys: [].

2 direct ingredient instances; CHEBI-primary instance linkage 0/2 (0.00%), verified secondary coverage 0/2 (0.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### NBRC279 TYG and maintained owner

identity: supported. Targets: CultureMech:007484.

Stable ID, explicit source history and merge owner resolve local280 to NBRC279. The official title and source term in the maintained owner match the primary page. Difco supplied-material wording is retained in the owner.

### Two malformed target rows and all five owner quantities

quantity: concern. Targets: CultureMech:007484.

correct: the target contains a whole-recipe text blob with VARIABLE concentration and a blank row with textual amount. The owner recovers every source numeral, water1L and pH7.0. Solute G_PER_L values reflect the nominal one-liter-water batch; the source does not establish measured final volume. Preserve manufacturer, batch quantities and denominator scope.

[["Bacto Tryptone (Difco)", "3", "G_PER_L"], ["Yeast extract", "5", "G_PER_L"], ["Glucose", "5", "G_PER_L"], ["Distilled water", "1", "L"], ["Agar", "20", "G_PER_L"]]

### Generated and maintained ingredient identities

grounding: supported. Targets: CultureMech:007484.

Target primary/secondary linkage is0/2 malformed direct rows; the owner has3/5 primary and3/5 secondary CHEBI links(60% each). Glucose, water and agar IDs/labels resolve and all three secondary keys have live pinned preferred-term rows. Tryptone and yeast extract remain ungrounded rather than receiving invented pure-molecule identities. Coverage is a linkage metric only.

### Official title, pH and source-backed owner corrections

completeness: concern. Targets: CultureMech:007484.

The generated target lacks the owner official title, source term, structured pH, recovered component mappings, reference and later history. Regeneration alone cannot fix its preparation because the same unsupported list remains in the owner.

### Unsupported fallback and exact condition scope

evidence: concern. Targets: CultureMech:007484.

unsupported: source pH7.0 supports a target condition but does not establish a particular adjustment procedure or sterilization method. Both local layers retain an unqualified autoclave step classified DISSOLVE. No stock, incubation condition or organism-specific growth claim is supplied by this recipe.

### Undefined solid agar medium

scope: supported. Targets: CultureMech:007484.

COMPLEX/UNDEFINED is compatible with tryptone and yeast extract; source agar20g supports SOLID_AGAR. Bacterial category is organizational context, not an exclusive growth-range claim. No organism or internal stock reference is asserted.

### History and claim-level support

provenance: concern. Targets: CultureMech:007484.

All target/owner history timestamps parse with timezones. Source notes and reference identify the formulation but lack exact narrow amount/pH excerpts. The target reference gate checked zero excerpts and does not establish preparation support.

## Findings

### f1: Generated rows do not represent the five-component formulation

blocker / open / confirmed; issue key: CM007484-malformed-ingredient-table.

The full source recipe and pH are embedded in one VARIABLE ingredient, followed by a blank ingredient with Bacto Tryptone (Difco) as its concentration value.

### f2: Official source identity and structured pH are missing

major / open / confirmed; issue key: CM007484-stale-source-corrections.

The target label280 and absent structured source/pH/mappings/reference omit corrections already present in the maintained NBRC279 owner.

### f3: Both layers retain unsupported generic autoclaving

major / open / confirmed; issue key: CM007484-unsupported-preparation-both-layers.

The official source gives no sterilization protocol, but both target and owner assert autoclaving and label it DISSOLVE. An owner correction is required before regeneration.

### f4: Formulation and pH lack narrow source excerpts

minor / open / confirmed; issue key: CM007484-claim-evidence-gap.

The maintained URL and source notes provide provenance but do not attach exact support to each supplied material, quantity and pH.

## Recommended Actions And Acceptance Checks

### a1

Verify the recovered five-component owner and source batch basis, then regenerate after the separate preparation correction.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Verify the owner official title, exact accession, supplied materials and pH7.0, then regenerate and verify these fields survive.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Remove or qualify unsupported preparation in the maintained owner; retain source pH as a condition and add protocol details only with exact supporting evidence. Inspect importer fallback generation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach short verified source excerpts to the narrow claims, retaining literal batch quantities and separating concentration interpretation from quotation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/280.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_280.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/280.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/280.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch008/075/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/075/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/280.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/280.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/NBRC_280.yaml:1:id: CultureMech:007484<br>./data/merge_yaml/merged/280.yaml:1:id: CultureMech:007484<br> |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {} |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=279; Medium No.279; complete Composition; pH; Comment | supports | Complete official NBRC279 recipe inspected: Tryptone Yeast Extract Agar (TYG); Bacto Tryptone (Difco)3g, yeast extract5g, glucose5g, distilled water1L, agar20g and pH7.0. Comment is blank; no sterilization procedure is supplied. |
| legacy | http://www.nbrc.nite.go.jp/NBRC2/NBRCMediumDetailServlet?NO=279; Redirect and complete medium detail | supports | The import-history servlet resolves to the same official medium279 page. Local280 is not source accession280. |
| owner-chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact owner identifier, canonical label and obsolete flag | supports | CHEBI:17234 resolves to glucose; primary and secondary labels match. |
| owner-chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact owner identifier, canonical label and obsolete flag | supports | CHEBI:15377 resolves to water; primary and secondary labels match. |
| owner-chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact owner identifier, canonical label and obsolete flag | supports | CHEBI:2509 resolves to agar; primary and secondary labels match. |
| context | Whole target, owner and pinned MIM index; All recovered amounts, pH, secondary keys and history timestamps | supports | {"owner_quantities": [["Bacto Tryptone (Difco)", "3", "G_PER_L"], ["Yeast extract", "5", "G_PER_L"], ["Glucose", "5", "G_PER_L"], ["Distilled water", "1", "L"], ["Agar", "20", "G_PER_L"]], "owner_ph": 7.0, "owner_secondary_rows": {"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "timezone_bearing_history_counts": [6, 8]} |
| importer | src/culturemech/import/nbrc_importer.py; _map_preparation_steps | supports | Current code emits these generic dissolve/conditional-pH/autoclaving defaults when source preparation is absent. Its autoclave substring does not match autoclaving, leaving action DISSOLVE. This verifies a current code failure mode rather than proving historical execution. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No source sterilization method, measured final volume or strain-specific growth result was established. Historical scraper execution was not reconstructed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T072712Z-culturemech-007484-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 280 (CultureMech:007484)'
started_at: '2026-10-21T07:17:57Z'
finished_at: '2026-10-21T07:27:12Z'
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
summary: The generated local280 record denotes NBRC279 Tryptone Yeast Extract Agar
  but has malformed ingredient rows. Its owner recovers the five source components,
  official identity and pH7.0. Both layers retain an unsupported generic autoclave
  protocol, so owner curation must precede regeneration.
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
  - path: data/merge_yaml/merged/280.yaml
    sha256: 338ac5795c3516a89dff066beab83109e15d79e16439b7926554701643e43781
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_280.yaml
    sha256: 8eae64a371d512a9194afafefa1097a5621acf5d9c6ab624940123a94417e10f
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
  selection: Task review 75; batch 008 item 5 of 10, selected in Python lexicographic
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
  - CultureMech:007484
targets:
- target_id: CultureMech:007484
  path: data/merge_yaml/merged/280.yaml
  label: '280'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_280.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/280.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007484
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/280.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch008/075/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/075/strict.tsv"
  target_ids:
  - CultureMech:007484
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/280.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007484
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/280.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007484
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
  - CultureMech:007484
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/280.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T07:27:10Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_280.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T07:27:10Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/280.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:19:11.923237Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/280.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch008/075/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T07:19:15.961425Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/075/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/280.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:19:20.839124Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/280.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:19:23.116593Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T07:27:10Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/NBRC_280.yaml:1:id: CultureMech:007484

    ./data/merge_yaml/merged/280.yaml:1:id: CultureMech:007484

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T07:27:10Z'
  support: supports
  summary: '{}'
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=279
  locator: Medium No.279; complete Composition; pH; Comment
  accessed_at: '2026-10-21T07:15:15.578497Z'
  support: supports
  summary: 'Complete official NBRC279 recipe inspected: Tryptone Yeast Extract Agar
    (TYG); Bacto Tryptone (Difco)3g, yeast extract5g, glucose5g, distilled water1L,
    agar20g and pH7.0. Comment is blank; no sterilization procedure is supplied.'
  quote: Bacto Tryptone (Difco) 3 g
  snapshot_sha256: 95e468a64055db5f6ce9bc83d75e735ad7c2a6cdd3cee35f829214aeb2f4301d
- evidence_id: legacy
  kind: primary_source
  reference: http://www.nbrc.nite.go.jp/NBRC2/NBRCMediumDetailServlet?NO=279
  locator: Redirect and complete medium detail
  accessed_at: '2026-10-21T07:15:12.399771Z'
  support: supports
  summary: The import-history servlet resolves to the same official medium279 page.
    Local280 is not source accession280.
  snapshot_sha256: 95e468a64055db5f6ce9bc83d75e735ad7c2a6cdd3cee35f829214aeb2f4301d
- evidence_id: owner-chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact owner identifier, canonical label and obsolete flag
  accessed_at: '2026-10-21T07:15:14.054540Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose; primary and secondary labels match.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: owner-chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact owner identifier, canonical label and obsolete flag
  accessed_at: '2026-10-21T07:15:13.683527Z'
  support: supports
  summary: CHEBI:15377 resolves to water; primary and secondary labels match.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: owner-chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact owner identifier, canonical label and obsolete flag
  accessed_at: '2026-10-21T07:15:14.241118Z'
  support: supports
  summary: CHEBI:2509 resolves to agar; primary and secondary labels match.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: context
  kind: validation
  reference: Whole target, owner and pinned MIM index
  locator: All recovered amounts, pH, secondary keys and history timestamps
  accessed_at: '2026-10-21T07:27:10Z'
  support: supports
  summary: '{"owner_quantities": [["Bacto Tryptone (Difco)", "3", "G_PER_L"], ["Yeast
    extract", "5", "G_PER_L"], ["Glucose", "5", "G_PER_L"], ["Distilled water", "1",
    "L"], ["Agar", "20", "G_PER_L"]], "owner_ph": 7.0, "owner_secondary_rows": {"CHEBI:17234":
    [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234",
    "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type":
    "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water",
    "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, "timezone_bearing_history_counts": [6, 8]}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/nbrc_importer.py
  locator: _map_preparation_steps
  accessed_at: '2026-10-21T07:27:10Z'
  support: supports
  summary: Current code emits these generic dissolve/conditional-pH/autoclaving defaults
    when source preparation is absent. Its autoclave substring does not match autoclaving,
    leaving action DISSOLVE. This verifies a current code failure mode rather than
    proving historical execution.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007484
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
  - CultureMech:007484
  evidence_ids:
  - record
  - mim
  details: 2 direct ingredient instances; CHEBI-primary instance linkage 0/2 (0.00%),
    verified secondary coverage 0/2 (0.00%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: NBRC279 TYG and maintained owner
  outcome: supported
  summary: Stable ID, explicit source history and merge owner resolve local280 to
    NBRC279. The official title and source term in the maintained owner match the
    primary page. Difco supplied-material wording is retained in the owner.
  target_ids:
  - CultureMech:007484
  evidence_ids:
  - record
  - owner-0
  - id-search
  - nbrc
  - legacy
- assessment_id: quantities
  area: quantity
  topic: Two malformed target rows and all five owner quantities
  outcome: concern
  summary: 'correct: the target contains a whole-recipe text blob with VARIABLE concentration
    and a blank row with textual amount. The owner recovers every source numeral,
    water1L and pH7.0. Solute G_PER_L values reflect the nominal one-liter-water batch;
    the source does not establish measured final volume. Preserve manufacturer, batch
    quantities and denominator scope.'
  target_ids:
  - CultureMech:007484
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - context
  details: '[["Bacto Tryptone (Difco)", "3", "G_PER_L"], ["Yeast extract", "5", "G_PER_L"],
    ["Glucose", "5", "G_PER_L"], ["Distilled water", "1", "L"], ["Agar", "20", "G_PER_L"]]'
- assessment_id: grounding-scope
  area: grounding
  topic: Generated and maintained ingredient identities
  outcome: supported
  summary: Target primary/secondary linkage is0/2 malformed direct rows; the owner
    has3/5 primary and3/5 secondary CHEBI links(60% each). Glucose, water and agar
    IDs/labels resolve and all three secondary keys have live pinned preferred-term
    rows. Tryptone and yeast extract remain ungrounded rather than receiving invented
    pure-molecule identities. Coverage is a linkage metric only.
  target_ids:
  - CultureMech:007484
  evidence_ids:
  - record
  - owner-0
  - context
  - owner-chebi17234
  - owner-chebi15377
  - owner-chebi2509
- assessment_id: freshness
  area: completeness
  topic: Official title, pH and source-backed owner corrections
  outcome: concern
  summary: The generated target lacks the owner official title, source term, structured
    pH, recovered component mappings, reference and later history. Regeneration alone
    cannot fix its preparation because the same unsupported list remains in the owner.
  target_ids:
  - CultureMech:007484
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - context
- assessment_id: preparation
  area: evidence
  topic: Unsupported fallback and exact condition scope
  outcome: concern
  summary: 'unsupported: source pH7.0 supports a target condition but does not establish
    a particular adjustment procedure or sterilization method. Both local layers retain
    an unqualified autoclave step classified DISSOLVE. No stock, incubation condition
    or organism-specific growth claim is supplied by this recipe.'
  target_ids:
  - CultureMech:007484
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - importer
- assessment_id: classification
  area: scope
  topic: Undefined solid agar medium
  outcome: supported
  summary: COMPLEX/UNDEFINED is compatible with tryptone and yeast extract; source
    agar20g supports SOLID_AGAR. Bacterial category is organizational context, not
    an exclusive growth-range claim. No organism or internal stock reference is asserted.
  target_ids:
  - CultureMech:007484
  evidence_ids:
  - record
  - owner-0
  - nbrc
- assessment_id: provenance
  area: provenance
  topic: History and claim-level support
  outcome: concern
  summary: All target/owner history timestamps parse with timezones. Source notes
    and reference identify the formulation but lack exact narrow amount/pH excerpts.
    The target reference gate checked zero excerpts and does not establish preparation
    support.
  target_ids:
  - CultureMech:007484
  evidence_ids:
  - record
  - owner-0
  - context
  - validate-references
findings:
- finding_id: f1
  issue_key: CM007484-malformed-ingredient-table
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated rows do not represent the five-component formulation
  description: The full source recipe and pH are embedded in one VARIABLE ingredient,
    followed by a blank ingredient with Bacto Tryptone (Difco) as its concentration
    value.
  target_ids:
  - CultureMech:007484
  field_paths:
  - ingredients
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_280.yaml
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
  issue_key: CM007484-stale-source-corrections
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Official source identity and structured pH are missing
  description: The target label280 and absent structured source/pH/mappings/reference
    omit corrections already present in the maintained NBRC279 owner.
  target_ids:
  - CultureMech:007484
  field_paths:
  - name
  - original_name
  - media_term
  - ph_value
  - ingredients
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_280.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM007484-unsupported-preparation-both-layers
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Both layers retain unsupported generic autoclaving
  description: The official source gives no sterilization protocol, but both target
    and owner assert autoclaving and label it DISSOLVE. An owner correction is required
    before regeneration.
  target_ids:
  - CultureMech:007484
  field_paths:
  - preparation_steps
  - data/normalized_yaml/bacterial/NBRC_280.yaml:preparation_steps
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - importer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_280.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: CM007484-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Formulation and pH lack narrow source excerpts
  description: The maintained URL and source notes provide provenance but do not attach
    exact support to each supplied material, quantity and pH.
  target_ids:
  - CultureMech:007484
  field_paths:
  - references
  - ingredients[*].evidence
  - ph_value
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_280.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Verify the recovered five-component owner and source batch basis, then
    regenerate after the separate preparation correction.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007484
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_280.yaml
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
  description: Verify the owner official title, exact accession, supplied materials
    and pH7.0, then regenerate and verify these fields survive.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007484
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_280.yaml
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
  description: Remove or qualify unsupported preparation in the maintained owner;
    retain source pH as a condition and add protocol details only with exact supporting
    evidence. Inspect importer fallback generation.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007484
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_280.yaml
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
  description: Attach short verified source excerpts to the narrow claims, retaining
    literal batch quantities and separating concentration interpretation from quotation.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007484
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_280.yaml
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
- No source sterilization method, measured final volume or strain-specific growth
  result was established. Historical scraper execution was not reconstructed.
tags:
- unreviewed-records
- batch-008
- generated-medium
```
