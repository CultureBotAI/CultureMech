# Provenance-only partial review: 7H9 (CultureMech:015481)

- Review: 20261021T085327Z-culturemech-015481-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T08:48:57Z
- Finished UTC: 2026-10-21T08:53:27Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Partial provenance-only review. The generated target and normalized owner correspond and mechanical checks pass. Authenticated GitHub repository metadata confirms the cited CultureBotHT repository exists and is private, despite earlier unauthenticated 404 responses. The citation is a repository-root locator without a pinned historical source-file version; exact upstream contents and all operational or biological claims remain unexamined.

## Scope And Provenance

One generated record, reviewed only for record/owner identity, source and citation metadata, ontology ID/label metadata, field structure and timestamp provenance. Literature support for formulation or biological claims was not reassessed.

Selection: Task review 114; batch 012 item 4 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding eleven task batches contain 110 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 112 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:015481 | data/merge_yaml/merged/7H9.yaml | generated | 7H9 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:015481 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:015481 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch012/114/strict.tsv |
| validate-terms | passed | True | CultureMech:015481 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:015481 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:015481 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Required formulation and operational scientific assessment | skipped | True | CultureMech:015481 | The local description explicitly names Mycobacterium tuberculosis H37Rv. Actionable cultivation, formulation and procedure assessment is outside the permitted safety scope. Ingredient/stock, concentration, preparation, culture-condition and biological-performance assessments were deliberately not performed. This is a safety scope boundary, not a failed source download or a finding that those values are wrong. |
| Exact historical upstream source-file version | skipped | True | CultureMech:015481 | Repository identity/access was checked, but the exact historical file, revision and upstream contents were deliberately not retrieved or assessed in this provenance-only safety scope. Marked skipped rather than universally unavailable; authenticated metadata access succeeded. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:015481.

The four documented recipes completed; interpret the scope of each separately.

### Operational and biological claims excluded from this review

scope: unknown. Targets: CultureMech:015481.

The local description explicitly names Mycobacterium tuberculosis H37Rv. Actionable cultivation, formulation and procedure assessment is outside the permitted safety scope. No concentration decisions or procedural corrections are supplied; literature support for those claims was not reassessed.

### Exact generated target and maintained source

ownership: supported. Targets: CultureMech:015481.

The target and data/normalized_yaml/specialized/7h9.yaml share stable ID CultureMech:015481. The explicit merged_from entry and final merge-event source name the maintained file. Apart from merge metadata and the appended merge event, parsed record fields agree. This is representation/provenance correspondence, not scientific equivalence to an upstream formulation.

### History shape and append-only ownership

provenance: supported. Targets: CultureMech:015481.

The 9 timestamp instances are timezone-aware; owner history is retained by the generated target. Any later metadata clarification must append an honest current event rather than rewriting earlier events.

### Asserted identifier and label metadata only

grounding: supported. Targets: CultureMech:015481.

All 15 distinct asserted primary ontology identifiers resolve to matching non-obsolete labels in the captured OLS responses. This is not a source-to-ingredient grounding assessment and does not recommend any substitution or correction.

### Repository and import metadata identity

identity: supported. Targets: CultureMech:015481.

The records name CultureBotHT and the original 7H9.yaml basename. Authenticated metadata verifies the exact repository identity. Public 404 attempts and later authenticated success retain their distinct access contexts; neither response verifies the imported historical file.

### Historical source-file locator and version

provenance: concern. Targets: CultureMech:015481.

sources[0] identifies a repository root and database key; curation_history[0] names an imported basename. Neither layer records an exact upstream file locator, commit or blob hash. The notes mention FEBA without a versioned primary source citation. The historical contents remain unexamined and are not declared absent.

### Organism-specific description and metadata limits

scope: unknown. Targets: CultureMech:015481.

The organism and strain in the local description are recorded context only. This review neither validates the completeness wording nor supplies growth evidence, taxonomy replacements, chemical corrections or cultivation instructions. The specialized category and quality flag are preserved as local metadata, not treated as evidence of performance.

## Findings

### f1: Repository-root citation does not pin the imported source version

minor / open / confirmed; issue key: CM015481-historical-source-version-provenance.

The maintained owner and target identify CultureBotHT through a repository-root URL and an import-event basename, but do not provide an exact historical source-file revision or blob identity. The FEBA note likewise lacks a versioned source locator. Authenticated metadata access confirms the repository exists; exact historical contents were not retrieved. This bounded traceability gap is separate from any unassessed scientific or operational claim.

## Recommended Actions And Acceptance Checks

### a1

Clarify maintained provenance metadata so the repository identity, access context and known historical-source limits are explicit. Add a source-file/version locator only when it is actually established through an authorized metadata process; otherwise preserve it as unresolved. Keep private contents out of public evidence, retain existing historical events, and append an honest metadata clarification only after an authorized edit. No formulation or cultivation corrections are proposed.

- Limit any follow-up to source identity, access context, citation/version locators and honest provenance wording; do not alter formulation or operational fields under this review.
- Preserve earlier history; append a dated metadata clarification only if a separately authorized maintained-input change is made.
- After an authorized metadata edit, run the four documented target validators. If derived output is regenerated, run the documented merge checks; neither mechanical step certifies scientific validity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/7H9.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Entire local YAML read for record identity, provenance and field structure. Operational content was not assessed or reproduced in this review. |
| owner-0 | data/normalized_yaml/specialized/7h9.yaml; Entire maintained YAML | context_only | Entire local YAML read for record identity, provenance and field structure. Operational content was not assessed or reproduced in this review. |
| validate-schema | just validate-schema data/merge_yaml/merged/7H9.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/7H9.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch012/114/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch012/114/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/7H9.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/7H9.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| scope-contract | docs/record-reviews.md; Verdict And Severity; provenance-only inspection and scientific_review flag | supports | The native contract distinguishes provenance-only inspection from scientific review and requires literature support not reassessed to be explicit. |
| history-metadata | data/merge_yaml/merged/7H9.yaml; data/normalized_yaml/specialized/7h9.yaml; curation_history[*].timestamp; final generated MERGED_RECIPES event | supports | All 9 timestamp instances are parseable and timezone-aware: 5 target events and 4 maintained-owner events. The generated record preserves the owner history and appends its merge event. This checks timestamp shape and preservation, not the scientific truth of historical actions. |
| ontology-chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; $._embedded.terms[0].obo_id, label, is_obsolete | supports | The asserted ID CHEBI:15956 resolves with the record's canonical label and is not obsolete. This is metadata verification only; suitability of that term for the medium ingredient or source chemical form was not assessed. |
| ontology-chebi16015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16015; $._embedded.terms[0].obo_id, label, is_obsolete | supports | The asserted ID CHEBI:16015 resolves with the record's canonical label and is not obsolete. This is metadata verification only; suitability of that term for the medium ingredient or source chemical form was not assessed. |
| ontology-chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; $._embedded.terms[0].obo_id, label, is_obsolete | supports | The asserted ID CHEBI:17634 resolves with the record's canonical label and is not obsolete. This is metadata verification only; suitability of that term for the medium ingredient or source chemical form was not assessed. |
| ontology-chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0].obo_id, label, is_obsolete | supports | The asserted ID CHEBI:26710 resolves with the record's canonical label and is not obsolete. This is metadata verification only; suitability of that term for the medium ingredient or source chemical form was not assessed. |
| ontology-chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; $._embedded.terms[0].obo_id, label, is_obsolete | supports | The asserted ID CHEBI:30961 resolves with the record's canonical label and is not obsolete. This is metadata verification only; suitability of that term for the medium ingredient or source chemical form was not assessed. |
| ontology-chebi31604 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31604; $._embedded.terms[0].obo_id, label, is_obsolete | supports | The asserted ID CHEBI:31604 resolves with the record's canonical label and is not obsolete. This is metadata verification only; suitability of that term for the medium ingredient or source chemical form was not assessed. |
| ontology-chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; $._embedded.terms[0].obo_id, label, is_obsolete | supports | The asserted ID CHEBI:32599 resolves with the record's canonical label and is not obsolete. This is metadata verification only; suitability of that term for the medium ingredient or source chemical form was not assessed. |
| ontology-chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; $._embedded.terms[0].obo_id, label, is_obsolete | supports | The asserted ID CHEBI:34683 resolves with the record's canonical label and is not obsolete. This is metadata verification only; suitability of that term for the medium ingredient or source chemical form was not assessed. |
| ontology-chebi35176 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35176; $._embedded.terms[0].obo_id, label, is_obsolete | supports | The asserted ID CHEBI:35176 resolves with the record's canonical label and is not obsolete. This is metadata verification only; suitability of that term for the medium ingredient or source chemical form was not assessed. |
| ontology-chebi53258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258; $._embedded.terms[0].obo_id, label, is_obsolete | supports | The asserted ID CHEBI:53258 resolves with the record's canonical label and is not obsolete. This is metadata verification only; suitability of that term for the medium ingredient or source chemical form was not assessed. |
| ontology-chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; $._embedded.terms[0].obo_id, label, is_obsolete | supports | The asserted ID CHEBI:62946 resolves with the record's canonical label and is not obsolete. This is metadata verification only; suitability of that term for the medium ingredient or source chemical form was not assessed. |
| ontology-chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0].obo_id, label, is_obsolete | supports | The asserted ID CHEBI:63036 resolves with the record's canonical label and is not obsolete. This is metadata verification only; suitability of that term for the medium ingredient or source chemical form was not assessed. |
| ontology-chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0].obo_id, label, is_obsolete | supports | The asserted ID CHEBI:86158 resolves with the record's canonical label and is not obsolete. This is metadata verification only; suitability of that term for the medium ingredient or source chemical form was not assessed. |
| ontology-chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; $._embedded.terms[0].obo_id, label, is_obsolete | supports | The asserted ID CHEBI:86318 resolves with the record's canonical label and is not obsolete. This is metadata verification only; suitability of that term for the medium ingredient or source chemical form was not assessed. |
| ontology-chebi53426retry | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53426; $._embedded.terms[0].obo_id, label, is_obsolete | supports | The asserted ID CHEBI:53426 resolves with the record's canonical label and is not obsolete. This is metadata verification only; suitability of that term for the medium ingredient or source chemical form was not assessed. |
| access-culturebothtPublicRepository | https://github.com/CultureBotAI/CultureBotHT; Unauthenticated response metadata | context_only | The exact public request returned HTTP 404. This records that access context only; the subsequent authenticated metadata response confirms the repository exists, so the 404 cannot support universal unavailability or nonexistence. |
| access-culturebothtPublicMetadata | https://api.github.com/repos/CultureBotAI/CultureBotHT; Unauthenticated response metadata | context_only | The exact public request returned HTTP 404. This records that access context only; the subsequent authenticated metadata response confirms the repository exists, so the 404 cannot support universal unavailability or nonexistence. |
| repository-authenticated | https://api.github.com/repos/CultureBotAI/CultureBotHT; Authenticated repository metadata only: full_name, html_url, default_branch, private, archived, id | supports | The exact cited repository resolves through configured authenticated gh access. Repository metadata confirms its identity and private access context. No repository contents, historical source file or commit, formulation, or protocol was retrieved. This supersedes any inference of nonexistence from the earlier public 404; it does not establish historical-source content. |
| importer-provenance | scripts/import_from_culturebotht.py; CultureBotHTImporter.transform_medium source tracking and import history; import_file passes yaml_file.name | supports | The current importer appends the repository-root URL and medium name, and records the input basename in an import event. These fields do not pin a source commit or historical blob. The current code is read as metadata-generation context, not proof that an unchanged historical implementation or upstream content was used. |

## Limits And Additional Notes

- The local description explicitly names Mycobacterium tuberculosis H37Rv. Actionable cultivation, formulation and procedure assessment is outside the permitted safety scope.
- This is a provenance-only observation, not a complete scientific review. Literature support for the formulation and biological claims was not reassessed. Required operational assessments are explicitly skipped; partial completion does not certify that the recipe is correct, complete or suitable for use.
- The four documented diagnostic commands passed. The reference checker examined zero excerpts, so its pass does not validate a paper, supplier attribution, source version, or any biological claim.
- Ontology checks here are limited to identifier, canonical-label and obsolete-flag metadata. No ingredient replacement, chemical-form correction, CAS or molecular-weight correction, or secondary-link scientific assessment is made.
- No record, source capture, history, derived output, or scientific status was changed. No additional diagnostic, native review validation, save, or corpus-wide gate was run by this draft author.
- The authenticated follow-up retrieved only selected repository metadata. No private source contents were retrieved or published. Exact historical source-file and FEBA identity/version remain unexamined, not proven unavailable or nonexistent.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T085327Z-culturemech-015481-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Provenance-only partial review: 7H9 (CultureMech:015481)'
started_at: '2026-10-21T08:48:57Z'
finished_at: '2026-10-21T08:53:27Z'
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
scientific_review: false
summary: Partial provenance-only review. The generated target and normalized owner
  correspond and mechanical checks pass. Authenticated GitHub repository metadata
  confirms the cited CultureBotHT repository exists and is private, despite earlier
  unauthenticated 404 responses. The citation is a repository-root locator without
  a pinned historical source-file version; exact upstream contents and all operational
  or biological claims remain unexamined.
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
  - path: data/merge_yaml/merged/7H9.yaml
    sha256: 7ebcde7b30a7e6cd777d8123868424e0541666777b6316dd6c80f673d8e94b92
    role: target
  - path: data/normalized_yaml/specialized/7h9.yaml
    sha256: a6327097f51faf6a0a3759530b3fe5e039afed8cf100f39ea2197fa49f0cbf17
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
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
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
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
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
  description: One generated record, reviewed only for record/owner identity, source
    and citation metadata, ontology ID/label metadata, field structure and timestamp
    provenance. Literature support for formulation or biological claims was not reassessed.
  selection: Task review 114; batch 012 item 4 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding eleven task batches contain
    110 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 112 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:015481
  exclusions:
  - target: CultureMech:015481
    reason: 'The local description explicitly names Mycobacterium tuberculosis H37Rv.
      Actionable cultivation, formulation and procedure assessment is outside the
      permitted safety scope. Excluded: ingredient selection or chemical-form correction,
      amounts, stock arithmetic, preparation, cultivation or sporulation procedures,
      culture conditions, performance, and growth evidence.'
targets:
- target_id: CultureMech:015481
  path: data/merge_yaml/merged/7H9.yaml
  label: 7H9
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/7h9.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/7H9.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:015481
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/7H9.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch012/114/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch012/114/strict.tsv"
  target_ids:
  - CultureMech:015481
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/7H9.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:015481
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/7H9.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:015481
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
  - CultureMech:015481
- check_id: operational-formulation-review
  name: Required formulation and operational scientific assessment
  required: true
  status: skipped
  target_ids:
  - CultureMech:015481
  evidence_ids:
  - record
  - scope-contract
  summary: The local description explicitly names Mycobacterium tuberculosis H37Rv.
    Actionable cultivation, formulation and procedure assessment is outside the permitted
    safety scope. Ingredient/stock, concentration, preparation, culture-condition
    and biological-performance assessments were deliberately not performed. This is
    a safety scope boundary, not a failed source download or a finding that those
    values are wrong.
- check_id: historical-source-version
  name: Exact historical upstream source-file version
  required: true
  status: skipped
  target_ids:
  - CultureMech:015481
  evidence_ids:
  - record
  - owner-0
  - repository-authenticated
  - importer-provenance
  summary: Repository identity/access was checked, but the exact historical file,
    revision and upstream contents were deliberately not retrieved or assessed in
    this provenance-only safety scope. Marked skipped rather than universally unavailable;
    authenticated metadata access succeeded.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/7H9.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T08:53:27Z'
  support: context_only
  summary: Entire local YAML read for record identity, provenance and field structure.
    Operational content was not assessed or reproduced in this review.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/specialized/7h9.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T08:53:27Z'
  support: context_only
  summary: Entire local YAML read for record identity, provenance and field structure.
    Operational content was not assessed or reproduced in this review.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/7H9.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:49:47.039850Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/7H9.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch012/114/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T08:49:48.511950Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch012/114/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/7H9.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:49:50.108802Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/7H9.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:49:51.102301Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: scope-contract
  kind: record_content
  reference: docs/record-reviews.md
  locator: Verdict And Severity; provenance-only inspection and scientific_review
    flag
  accessed_at: '2026-10-21T08:53:27Z'
  support: supports
  summary: The native contract distinguishes provenance-only inspection from scientific
    review and requires literature support not reassessed to be explicit.
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/7H9.yaml; data/normalized_yaml/specialized/7h9.yaml
  locator: curation_history[*].timestamp; final generated MERGED_RECIPES event
  accessed_at: '2026-10-21T08:53:27Z'
  support: supports
  summary: 'All 9 timestamp instances are parseable and timezone-aware: 5 target events
    and 4 maintained-owner events. The generated record preserves the owner history
    and appends its merge event. This checks timestamp shape and preservation, not
    the scientific truth of historical actions.'
- evidence_id: ontology-chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: $._embedded.terms[0].obo_id, label, is_obsolete
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: The asserted ID CHEBI:15956 resolves with the record's canonical label
    and is not obsolete. This is metadata verification only; suitability of that term
    for the medium ingredient or source chemical form was not assessed.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: ontology-chebi16015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16015
  locator: $._embedded.terms[0].obo_id, label, is_obsolete
  accessed_at: '2026-10-21T08:42:30.847456Z'
  support: supports
  summary: The asserted ID CHEBI:16015 resolves with the record's canonical label
    and is not obsolete. This is metadata verification only; suitability of that term
    for the medium ingredient or source chemical form was not assessed.
  snapshot_sha256: d4c039ee9f11823d174df5fa637b67506440f658c3492afcdf8032f0316f77d3
- evidence_id: ontology-chebi17634
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634
  locator: $._embedded.terms[0].obo_id, label, is_obsolete
  accessed_at: '2026-10-21T08:42:33.425023Z'
  support: supports
  summary: The asserted ID CHEBI:17634 resolves with the record's canonical label
    and is not obsolete. This is metadata verification only; suitability of that term
    for the medium ingredient or source chemical form was not assessed.
  snapshot_sha256: d11b31a8e91c3fffe7744f612dab69cdb4e02f42068cd2eb1458acee4503a62f
- evidence_id: ontology-chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: $._embedded.terms[0].obo_id, label, is_obsolete
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: The asserted ID CHEBI:26710 resolves with the record's canonical label
    and is not obsolete. This is metadata verification only; suitability of that term
    for the medium ingredient or source chemical form was not assessed.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: ontology-chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: $._embedded.terms[0].obo_id, label, is_obsolete
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: The asserted ID CHEBI:30961 resolves with the record's canonical label
    and is not obsolete. This is metadata verification only; suitability of that term
    for the medium ingredient or source chemical form was not assessed.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: ontology-chebi31604
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31604
  locator: $._embedded.terms[0].obo_id, label, is_obsolete
  accessed_at: '2026-10-21T08:42:44.987529Z'
  support: supports
  summary: The asserted ID CHEBI:31604 resolves with the record's canonical label
    and is not obsolete. This is metadata verification only; suitability of that term
    for the medium ingredient or source chemical form was not assessed.
  snapshot_sha256: 31acf125b469ffd64e2de503550d29336a7a0f99c8a3ea24b80b53bdb715e7f8
- evidence_id: ontology-chebi32599
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: $._embedded.terms[0].obo_id, label, is_obsolete
  accessed_at: '2026-10-21T08:42:45.640268Z'
  support: supports
  summary: The asserted ID CHEBI:32599 resolves with the record's canonical label
    and is not obsolete. This is metadata verification only; suitability of that term
    for the medium ingredient or source chemical form was not assessed.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: ontology-chebi34683
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: $._embedded.terms[0].obo_id, label, is_obsolete
  accessed_at: '2026-10-21T08:42:46.851695Z'
  support: supports
  summary: The asserted ID CHEBI:34683 resolves with the record's canonical label
    and is not obsolete. This is metadata verification only; suitability of that term
    for the medium ingredient or source chemical form was not assessed.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: ontology-chebi35176
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35176
  locator: $._embedded.terms[0].obo_id, label, is_obsolete
  accessed_at: '2026-10-21T08:42:49.940050Z'
  support: supports
  summary: The asserted ID CHEBI:35176 resolves with the record's canonical label
    and is not obsolete. This is metadata verification only; suitability of that term
    for the medium ingredient or source chemical form was not assessed.
  snapshot_sha256: 81ec7a8870c22cb4add111b8bd75e37886d7c96c9fc402a01f384c4cd4b6b746
- evidence_id: ontology-chebi53258
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258
  locator: $._embedded.terms[0].obo_id, label, is_obsolete
  accessed_at: '2026-10-21T08:42:54.823692Z'
  support: supports
  summary: The asserted ID CHEBI:53258 resolves with the record's canonical label
    and is not obsolete. This is metadata verification only; suitability of that term
    for the medium ingredient or source chemical form was not assessed.
  snapshot_sha256: 2a35c6dc3532c2276c6b19aef0992260e14b1fc36423fa3eb812bb94f63c4371
- evidence_id: ontology-chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: $._embedded.terms[0].obo_id, label, is_obsolete
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: The asserted ID CHEBI:62946 resolves with the record's canonical label
    and is not obsolete. This is metadata verification only; suitability of that term
    for the medium ingredient or source chemical form was not assessed.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: ontology-chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: $._embedded.terms[0].obo_id, label, is_obsolete
  accessed_at: '2026-10-21T08:43:08.324907Z'
  support: supports
  summary: The asserted ID CHEBI:63036 resolves with the record's canonical label
    and is not obsolete. This is metadata verification only; suitability of that term
    for the medium ingredient or source chemical form was not assessed.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: ontology-chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: $._embedded.terms[0].obo_id, label, is_obsolete
  accessed_at: '2026-10-21T08:43:09.378884Z'
  support: supports
  summary: The asserted ID CHEBI:86158 resolves with the record's canonical label
    and is not obsolete. This is metadata verification only; suitability of that term
    for the medium ingredient or source chemical form was not assessed.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: ontology-chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: $._embedded.terms[0].obo_id, label, is_obsolete
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: The asserted ID CHEBI:86318 resolves with the record's canonical label
    and is not obsolete. This is metadata verification only; suitability of that term
    for the medium ingredient or source chemical form was not assessed.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: ontology-chebi53426retry
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53426
  locator: $._embedded.terms[0].obo_id, label, is_obsolete
  accessed_at: '2026-10-21T08:44:30.953651Z'
  support: supports
  summary: The asserted ID CHEBI:53426 resolves with the record's canonical label
    and is not obsolete. This is metadata verification only; suitability of that term
    for the medium ingredient or source chemical form was not assessed.
  snapshot_sha256: d213680c843282430d36cc13a81ee5bfda8029054f6b1482a375c35fd94191a6
- evidence_id: access-culturebothtPublicRepository
  kind: database
  reference: https://github.com/CultureBotAI/CultureBotHT
  locator: Unauthenticated response metadata
  accessed_at: '2026-10-21T08:42:27.408212Z'
  support: context_only
  summary: The exact public request returned HTTP 404. This records that access context
    only; the subsequent authenticated metadata response confirms the repository exists,
    so the 404 cannot support universal unavailability or nonexistence.
  snapshot_sha256: d138b6df8db0c251e6e74bd187fa5c28e18c7f9cfd8497b37be0f8fe3edef5ea
- evidence_id: access-culturebothtPublicMetadata
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/CultureBotHT
  locator: Unauthenticated response metadata
  accessed_at: '2026-10-21T08:42:27.405156Z'
  support: context_only
  summary: The exact public request returned HTTP 404. This records that access context
    only; the subsequent authenticated metadata response confirms the repository exists,
    so the 404 cannot support universal unavailability or nonexistence.
  snapshot_sha256: 4f50e254a719a6b1b06b529bdaa08980e4acf0878aad0090cba7771f6ebdf0b9
- evidence_id: repository-authenticated
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/CultureBotHT
  locator: 'Authenticated repository metadata only: full_name, html_url, default_branch,
    private, archived, id'
  accessed_at: '2026-10-21T08:48:43.685545Z'
  support: supports
  summary: The exact cited repository resolves through configured authenticated gh
    access. Repository metadata confirms its identity and private access context.
    No repository contents, historical source file or commit, formulation, or protocol
    was retrieved. This supersedes any inference of nonexistence from the earlier
    public 404; it does not establish historical-source content.
  snapshot_sha256: d386c84c817c0d715aad1d1f0f21e1faced5fc4e26114883d8b65bc4056e03d5
- evidence_id: importer-provenance
  kind: record_content
  reference: scripts/import_from_culturebotht.py
  locator: CultureBotHTImporter.transform_medium source tracking and import history;
    import_file passes yaml_file.name
  accessed_at: '2026-10-21T08:53:27Z'
  support: supports
  summary: The current importer appends the repository-root URL and medium name, and
    records the input basename in an import event. These fields do not pin a source
    commit or historical blob. The current code is read as metadata-generation context,
    not proof that an unchanged historical implementation or upstream content was
    used.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:015481
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: scientific-scope
  area: scope
  topic: Operational and biological claims excluded from this review
  outcome: unknown
  summary: The local description explicitly names Mycobacterium tuberculosis H37Rv.
    Actionable cultivation, formulation and procedure assessment is outside the permitted
    safety scope. No concentration decisions or procedural corrections are supplied;
    literature support for those claims was not reassessed.
  target_ids:
  - CultureMech:015481
  evidence_ids:
  - record
  - scope-contract
- assessment_id: identity-owner
  area: ownership
  topic: Exact generated target and maintained source
  outcome: supported
  summary: The target and data/normalized_yaml/specialized/7h9.yaml share stable ID
    CultureMech:015481. The explicit merged_from entry and final merge-event source
    name the maintained file. Apart from merge metadata and the appended merge event,
    parsed record fields agree. This is representation/provenance correspondence,
    not scientific equivalence to an upstream formulation.
  target_ids:
  - CultureMech:015481
  evidence_ids:
  - record
  - owner-0
- assessment_id: history
  area: provenance
  topic: History shape and append-only ownership
  outcome: supported
  summary: The 9 timestamp instances are timezone-aware; owner history is retained
    by the generated target. Any later metadata clarification must append an honest
    current event rather than rewriting earlier events.
  target_ids:
  - CultureMech:015481
  evidence_ids:
  - history-metadata
- assessment_id: ontology-metadata
  area: grounding
  topic: Asserted identifier and label metadata only
  outcome: supported
  summary: All 15 distinct asserted primary ontology identifiers resolve to matching
    non-obsolete labels in the captured OLS responses. This is not a source-to-ingredient
    grounding assessment and does not recommend any substitution or correction.
  target_ids:
  - CultureMech:015481
  evidence_ids:
  - record
  - ontology-chebi15956
  - ontology-chebi16015
  - ontology-chebi17634
  - ontology-chebi26710
  - ontology-chebi30961
  - ontology-chebi31604
  - ontology-chebi32599
  - ontology-chebi34683
  - ontology-chebi35176
  - ontology-chebi53258
  - ontology-chebi62946
  - ontology-chebi63036
  - ontology-chebi86158
  - ontology-chebi86318
  - ontology-chebi53426retry
- assessment_id: source-access
  area: identity
  topic: Repository and import metadata identity
  outcome: supported
  summary: The records name CultureBotHT and the original 7H9.yaml basename. Authenticated
    metadata verifies the exact repository identity. Public 404 attempts and later
    authenticated success retain their distinct access contexts; neither response
    verifies the imported historical file.
  target_ids:
  - CultureMech:015481
  evidence_ids:
  - record
  - owner-0
  - repository-authenticated
  - access-culturebothtPublicRepository
  - access-culturebothtPublicMetadata
  - importer-provenance
- assessment_id: source-version
  area: provenance
  topic: Historical source-file locator and version
  outcome: concern
  summary: sources[0] identifies a repository root and database key; curation_history[0]
    names an imported basename. Neither layer records an exact upstream file locator,
    commit or blob hash. The notes mention FEBA without a versioned primary source
    citation. The historical contents remain unexamined and are not declared absent.
  target_ids:
  - CultureMech:015481
  evidence_ids:
  - record
  - owner-0
  - repository-authenticated
  - importer-provenance
- assessment_id: description-scope
  area: scope
  topic: Organism-specific description and metadata limits
  outcome: unknown
  summary: The organism and strain in the local description are recorded context only.
    This review neither validates the completeness wording nor supplies growth evidence,
    taxonomy replacements, chemical corrections or cultivation instructions. The specialized
    category and quality flag are preserved as local metadata, not treated as evidence
    of performance.
  target_ids:
  - CultureMech:015481
  evidence_ids:
  - record
  - owner-0
  - scope-contract
findings:
- finding_id: f1
  issue_key: CM015481-historical-source-version-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Repository-root citation does not pin the imported source version
  description: The maintained owner and target identify CultureBotHT through a repository-root
    URL and an import-event basename, but do not provide an exact historical source-file
    revision or blob identity. The FEBA note likewise lacks a versioned source locator.
    Authenticated metadata access confirms the repository exists; exact historical
    contents were not retrieved. This bounded traceability gap is separate from any
    unassessed scientific or operational claim.
  target_ids:
  - CultureMech:015481
  field_paths:
  - sources[0].url
  - sources[0].database_id
  - notes
  - curation_history[0].notes
  evidence_ids:
  - record
  - owner-0
  - repository-authenticated
  - importer-provenance
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/7h9.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P3
  normalization_reason: Native P3 normalized to minor because this is a bounded historical-source
    locator/version gap; no assertion is made that the source or formulation is wrong.
actions:
- action_id: a1
  description: Clarify maintained provenance metadata so the repository identity,
    access context and known historical-source limits are explicit. Add a source-file/version
    locator only when it is actually established through an authorized metadata process;
    otherwise preserve it as unresolved. Keep private contents out of public evidence,
    retain existing historical events, and append an honest metadata clarification
    only after an authorized edit. No formulation or cultivation corrections are proposed.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:015481
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/7h9.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Limit any follow-up to source identity, access context, citation/version locators
    and honest provenance wording; do not alter formulation or operational fields
    under this review.
  - Preserve earlier history; append a dated metadata clarification only if a separately
    authorized maintained-input change is made.
  - After an authorized metadata edit, run the four documented target validators.
    If derived output is regenerated, run the documented merge checks; neither mechanical
    step certifies scientific validity.
limitations:
- The local description explicitly names Mycobacterium tuberculosis H37Rv. Actionable
  cultivation, formulation and procedure assessment is outside the permitted safety
  scope.
- This is a provenance-only observation, not a complete scientific review. Literature
  support for the formulation and biological claims was not reassessed. Required operational
  assessments are explicitly skipped; partial completion does not certify that the
  recipe is correct, complete or suitable for use.
- The four documented diagnostic commands passed. The reference checker examined zero
  excerpts, so its pass does not validate a paper, supplier attribution, source version,
  or any biological claim.
- Ontology checks here are limited to identifier, canonical-label and obsolete-flag
  metadata. No ingredient replacement, chemical-form correction, CAS or molecular-weight
  correction, or secondary-link scientific assessment is made.
- No record, source capture, history, derived output, or scientific status was changed.
  No additional diagnostic, native review validation, save, or corpus-wide gate was
  run by this draft author.
- The authenticated follow-up retrieved only selected repository metadata. No private
  source contents were retrieved or published. Exact historical source-file and FEBA
  identity/version remain unexamined, not proven unavailable or nonexistent.
tags:
- unreviewed-records
- batch-012
- generated-medium
```
