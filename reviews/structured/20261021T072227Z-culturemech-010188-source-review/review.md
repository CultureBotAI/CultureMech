# Source and formulation review: 25_glucose_medium (CultureMech:010188)

- Review: 20261021T072227Z-culturemech-010188-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T07:17:51Z
- Finished UTC: 2026-10-21T07:22:27Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M77 identifies the JCM86 agar formulation and retains all supplied solute names and numerals. Water1L was encoded as1G_PER_L in both target and owner, and the available primary sterilization instruction is missing. All asserted ingredient IDs resolve; narrow source evidence is still absent.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 73; batch 008 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding seven task batches contain 70 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 72 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010188 | data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml | generated | 25_glucose_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010188 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010188 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/073/strict.tsv |
| validate-terms | passed | True | CultureMech:010188 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010188 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010188 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010188.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:010188.

3 primary CHEBI identities resolve with matching labels; 3 of 3 current secondary keys have live pinned-index rows. Unresolved keys: [].

6 direct ingredient instances; CHEBI-primary instance linkage 3/6 (50.00%), verified secondary coverage 3/6 (50.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Exact TOGO M77 and JCM86 source

identity: supported. Targets: CultureMech:010188.

The stable record identifies M77/JCM_M86, matching the inspected original recipe. The supplied Polypepton manufacturer qualifier is retained. No stock, sibling reference, tested organism or alternate source accession is asserted.

### All five solute concentrations

quantity: supported. Targets: CultureMech:010188.

verified: the solute numerals and exact source materials agree with JCM86 and TOGO; MediaDiveJ86 separately declares the same g_l values. Primary grams plus1L water are a nominal batch, not independent measurement of final volume. Agar at25g/L is consistent with the source preparation, and no conversion to percent or molarity is justified by physical state alone.

[{"field_path": "ingredients[0].concentration", "ingredient": "Distilled water", "source_amount": 1, "source_unit": "L", "target": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "source_annotations_retained": true}, {"field_path": "ingredients[1].concentration", "ingredient": "Yeast extract", "source_amount": 3, "source_unit": "g", "target": {"value": "3", "unit": "G_PER_L"}, "decision": "verified at source nominal batch/provider basis", "source_annotations_retained": true}, {"field_path": "ingredients[2].concentration", "ingredient": "Glucose", "source_amount": 250, "source_unit": "g", "target": {"value": "250", "unit": "G_PER_L"}, "decision": "verified at source nominal batch/provider basis", "source_annotations_retained": true}, {"field_path": "ingredients[3].concentration", "ingredient": "Agar", "source_amount": 25, "source_unit": "g", "target": {"value": "25", "unit": "G_PER_L"}, "decision": "verified at source nominal batch/provider basis", "source_annotations_retained": true}, {"field_path": "ingredients[4].concentration", "ingredient": "Malt extract", "source_amount": 3, "source_unit": "g", "target": {"value": "3", "unit": "G_PER_L"}, "decision": "verified at source nominal batch/provider basis", "source_annotations_retained": true}, {"field_path": "ingredients[5].concentration", "ingredient": "Polypepton (Nihon Pharm. Co.)", "source_amount": 5, "source_unit": "g", "target": {"value": "5", "unit": "G_PER_L"}, "decision": "verified at source nominal batch/provider basis", "source_annotations_retained": true}]

### ingredients[0].concentration

quantity: concern. Targets: CultureMech:010188.

correct: source water1L is recorded as1G_PER_L in both full local files. Restore the literal solvent volume with its preparation/batch context; neither density nor measured final volume is established by this row.

### Primary collection sterilization context

completeness: concern. Targets: CultureMech:010188.

The primary JCM header supplies an applicable default autoclave instruction absent from both target and owner. TOGO omits that collection header but does not override it. The primary recipe supplies no pH, strain-specific incubation or growth experiment to add.

### Verified mappings and undefined material scope

grounding: supported. Targets: CultureMech:010188.

Water, glucose and agar IDs/labels resolve and their three current secondary keys are supported by the pinned index. Primary and secondary linkage are each3/6(50%) of direct ingredient instances, not a correctness score. The three supplied digest/extract ingredients remain unmapped rather than receiving pure-molecule IDs.

### Undefined agar recipe and imported annotations

scope: supported. Targets: CultureMech:010188.

COMPLEX/UNDEFINED and SOLID_AGAR agree with the supplied ingredients. Role/property notes exactly retain the source database annotations; those annotations and generic cultivation are not experimental evidence of organism growth. The source25% title is not used to infer an unstated percentage basis.

### History and claim-level evidence

provenance: concern. Targets: CultureMech:010188.

All target/owner history timestamps parse with timezones. Source notes resolve to the correct provider and collection, but no narrow quantity or preparation evidence is present in either full file. The reference gate checked zero excerpts.

## Findings

### f1: Source water volume is represented as mass concentration

major / open / confirmed; issue key: CM010188-water-volume-unit.

The source1L distilled-water row is encoded as1G_PER_L in both layers, despite correct solute numerals.

### f2: Primary JCM sterilization instruction is absent

major / open / confirmed; issue key: CM010188-source-sterilization-missing.

Both full records lack the applicable primary collection default of autoclaving at121 degrees C for15minutes; no recipe-specific override is stated.

### f3: Source notes lack exact claim-scoped evidence

minor / open / confirmed; issue key: CM010188-claim-evidence-gap.

Provider links and import history identify the formulation but do not attach exact supporting excerpts to quantities, supplied forms and preparation.

## Recommended Actions And Acceptance Checks

### a1

Correct the maintained solvent-volume representation and inspect TOGO unit handling; preserve source batch context without a density or final-volume assumption before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add source-scoped sterilization and narrow evidence to the owner, then regenerate; leave unspecified pH and incubation conditions unresolved.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Add verified source metadata and short exact excerpts in the appropriate evidence slots, keeping nominal-batch interpretation separate from quotation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M77_25_Glucose_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch008/073/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/073/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml:1:id: CultureMech:010188<br>./data/normalized_yaml/bacterial/TOGO_M77_25_Glucose_Medium.yaml:1:id: CultureMech:010188<br> |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15377 resolves to water and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17234 resolves to glucose and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:2509 resolves to agar and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=86; GRMD86; full recipe and collection header | supports | Complete official JCM86 ingredient list and collection header inspected. Five solute masses, including source-specific Polypepton and25g agar, accompany distilled water1.0L. Collection default sterilization is121 degrees C for15minutes unless otherwise stated. No pH or incubation conditions are specified. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M77; meta; components[0].items; comments | supports | Complete M77 structured recipe inspected: source accession JCM_M86, exact primary URL, six ingredients, original units and role/property annotations. No preparation comment is supplied by TOGO. |
| mediadive | https://mediadive.dsmz.de/rest/medium/J86; data.medium; solutions[0].volume and recipe | supports | Independent database representation of the same primary JCM86 source explicitly provides g_l values for all five solutes. This corroborates the nominal provider concentrations without establishing a measured final volume from the primary water amount. |
| context | Full target and owner versus captured TOGO recipe; All six quantities/units/annotations and complete history timestamps | supports | {"rows": [{"field_path": "ingredients[0].concentration", "ingredient": "Distilled water", "source_amount": 1, "source_unit": "L", "target": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "source_annotations_retained": true}, {"field_path": "ingredients[1].concentration", "ingredient": "Yeast extract", "source_amount": 3, "source_unit": "g", "target": {"value": "3", "unit": "G_PER_L"}, "decision": "verified at source nominal batch/provider basis", "source_annotations_retained": true}, {"field_path": "ingredients[2].concentration", "ingredient": "Glucose", "source_amount": 250, "source_unit": "g", "target": {"value": "250", "unit": "G_PER_L"}, "decision": "verified at source nominal batch/provider basis", "source_annotations_retained": true}, {"field_path": "ingredients[3].concentration", "ingredient": "Agar", "source_amount": 25, "source_unit": "g", "target": {"value": "25", "unit": "G_PER_L"}, "decision": "verified at source nominal batch/provider basis", "source_annotations_retained": true}, {"field_path": "ingredients[4].concentration", "ingredient": "Malt extract", "source_amount": 3, "source_unit": "g", "target": {"value": "3", "unit": "G_PER_L"}, "decision": "verified at source nominal batch/provider basis", "source_annotations_retained": true}, {"field_path": "ingredients[5].concentration", "ingredient": "Polypepton (Nihon Pharm. Co.)", "source_amount": 5, "source_unit": "g", "target": {"value": "5", "unit": "G_PER_L"}, "decision": "verified at source nominal batch/provider basis", "source_annotations_retained": true}], "target_owner_ingredients_equal": true, "timezone_bearing_history_counts": [7, 6]} |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The review concerns one source-derived formulation, not organism-specific growth. Provider-declared g_l values corroborate concentrations but do not prove a measured final volume after solute addition.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T072227Z-culturemech-010188-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 25_glucose_medium (CultureMech:010188)'
started_at: '2026-10-21T07:17:51Z'
finished_at: '2026-10-21T07:22:27Z'
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
summary: TOGO M77 identifies the JCM86 agar formulation and retains all supplied solute
  names and numerals. Water1L was encoded as1G_PER_L in both target and owner, and
  the available primary sterilization instruction is missing. All asserted ingredient
  IDs resolve; narrow source evidence is still absent.
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
  - path: data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml
    sha256: 7cc08ff7635552371594f7f89a812f4729c3f505214e137ad8911850ca5dad5f
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M77_25_Glucose_Medium.yaml
    sha256: ce7914bde839ecc3e8c3b7efa85bbc42eff97c9f1b0ae834eeaf7705347a1b6d
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
  selection: Task review 73; batch 008 item 3 of 10, selected in Python lexicographic
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
  - CultureMech:010188
targets:
- target_id: CultureMech:010188
  path: data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml
  label: 25_glucose_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M77_25_Glucose_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010188
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch008/073/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/073/strict.tsv"
  target_ids:
  - CultureMech:010188
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010188
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010188
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
  - CultureMech:010188
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T07:22:26Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M77_25_Glucose_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T07:22:26Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:18:35.939187Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch008/073/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T07:18:41.222465Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/073/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:18:47.008213Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:18:50.266960Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T07:22:26Z'
  support: supports
  summary: './data/merge_yaml/merged/25_glucose_medium__2c0720bc.yaml:1:id: CultureMech:010188

    ./data/normalized_yaml/bacterial/TOGO_M77_25_Glucose_Medium.yaml:1:id: CultureMech:010188

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:15:13.683527Z'
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
  accessed_at: '2026-10-21T07:15:14.054540Z'
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
  accessed_at: '2026-10-21T07:15:14.241118Z'
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
  accessed_at: '2026-10-21T07:22:26Z'
  support: supports
  summary: '{"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234":
    [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234",
    "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=86
  locator: GRMD86; full recipe and collection header
  accessed_at: '2026-10-21T07:15:14.983727Z'
  support: supports
  summary: Complete official JCM86 ingredient list and collection header inspected.
    Five solute masses, including source-specific Polypepton and25g agar, accompany
    distilled water1.0L. Collection default sterilization is121 degrees C for15minutes
    unless otherwise stated. No pH or incubation conditions are specified.
  quote: Distilled water 1.0 L
  snapshot_sha256: fd786fbbbd5624f0eec2c80191c5596878fe86ba56315aaccbb7fc6d88652bd3
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M77
  locator: meta; components[0].items; comments
  accessed_at: '2026-10-21T07:15:13.439473Z'
  support: supports
  summary: 'Complete M77 structured recipe inspected: source accession JCM_M86, exact
    primary URL, six ingredients, original units and role/property annotations. No
    preparation comment is supplied by TOGO.'
  snapshot_sha256: 3229bf6d0744ce2285ecb06ca42a8e26ec9ac313c0a3b7b66d44a741f2906639
- evidence_id: mediadive
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J86
  locator: data.medium; solutions[0].volume and recipe
  accessed_at: '2026-10-21T07:15:12.400616Z'
  support: supports
  summary: Independent database representation of the same primary JCM86 source explicitly
    provides g_l values for all five solutes. This corroborates the nominal provider
    concentrations without establishing a measured final volume from the primary water
    amount.
  snapshot_sha256: 8a316173a59f91f180dc59ca7222665280119a2f8d1a91d6838da48d9370b9e9
- evidence_id: context
  kind: validation
  reference: Full target and owner versus captured TOGO recipe
  locator: All six quantities/units/annotations and complete history timestamps
  accessed_at: '2026-10-21T07:22:26Z'
  support: supports
  summary: '{"rows": [{"field_path": "ingredients[0].concentration", "ingredient":
    "Distilled water", "source_amount": 1, "source_unit": "L", "target": {"value":
    "1", "unit": "G_PER_L"}, "decision": "correct", "source_annotations_retained":
    true}, {"field_path": "ingredients[1].concentration", "ingredient": "Yeast extract",
    "source_amount": 3, "source_unit": "g", "target": {"value": "3", "unit": "G_PER_L"},
    "decision": "verified at source nominal batch/provider basis", "source_annotations_retained":
    true}, {"field_path": "ingredients[2].concentration", "ingredient": "Glucose",
    "source_amount": 250, "source_unit": "g", "target": {"value": "250", "unit": "G_PER_L"},
    "decision": "verified at source nominal batch/provider basis", "source_annotations_retained":
    true}, {"field_path": "ingredients[3].concentration", "ingredient": "Agar", "source_amount":
    25, "source_unit": "g", "target": {"value": "25", "unit": "G_PER_L"}, "decision":
    "verified at source nominal batch/provider basis", "source_annotations_retained":
    true}, {"field_path": "ingredients[4].concentration", "ingredient": "Malt extract",
    "source_amount": 3, "source_unit": "g", "target": {"value": "3", "unit": "G_PER_L"},
    "decision": "verified at source nominal batch/provider basis", "source_annotations_retained":
    true}, {"field_path": "ingredients[5].concentration", "ingredient": "Polypepton
    (Nihon Pharm. Co.)", "source_amount": 5, "source_unit": "g", "target": {"value":
    "5", "unit": "G_PER_L"}, "decision": "verified at source nominal batch/provider
    basis", "source_annotations_retained": true}], "target_owner_ingredients_equal":
    true, "timezone_bearing_history_counts": [7, 6]}'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010188
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
  - CultureMech:010188
  evidence_ids:
  - record
  - mim
  - chebi15377
  - chebi17234
  - chebi2509
  details: 6 direct ingredient instances; CHEBI-primary instance linkage 3/6 (50.00%),
    verified secondary coverage 3/6 (50.00%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Exact TOGO M77 and JCM86 source
  outcome: supported
  summary: The stable record identifies M77/JCM_M86, matching the inspected original
    recipe. The supplied Polypepton manufacturer qualifier is retained. No stock,
    sibling reference, tested organism or alternate source accession is asserted.
  target_ids:
  - CultureMech:010188
  evidence_ids:
  - record
  - owner-0
  - id-search
  - jcm
  - togo
  - mediadive
- assessment_id: solute-amounts
  area: quantity
  topic: All five solute concentrations
  outcome: supported
  summary: 'verified: the solute numerals and exact source materials agree with JCM86
    and TOGO; MediaDiveJ86 separately declares the same g_l values. Primary grams
    plus1L water are a nominal batch, not independent measurement of final volume.
    Agar at25g/L is consistent with the source preparation, and no conversion to percent
    or molarity is justified by physical state alone.'
  target_ids:
  - CultureMech:010188
  evidence_ids:
  - record
  - jcm
  - togo
  - mediadive
  - context
  details: '[{"field_path": "ingredients[0].concentration", "ingredient": "Distilled
    water", "source_amount": 1, "source_unit": "L", "target": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "source_annotations_retained": true}, {"field_path":
    "ingredients[1].concentration", "ingredient": "Yeast extract", "source_amount":
    3, "source_unit": "g", "target": {"value": "3", "unit": "G_PER_L"}, "decision":
    "verified at source nominal batch/provider basis", "source_annotations_retained":
    true}, {"field_path": "ingredients[2].concentration", "ingredient": "Glucose",
    "source_amount": 250, "source_unit": "g", "target": {"value": "250", "unit": "G_PER_L"},
    "decision": "verified at source nominal batch/provider basis", "source_annotations_retained":
    true}, {"field_path": "ingredients[3].concentration", "ingredient": "Agar", "source_amount":
    25, "source_unit": "g", "target": {"value": "25", "unit": "G_PER_L"}, "decision":
    "verified at source nominal batch/provider basis", "source_annotations_retained":
    true}, {"field_path": "ingredients[4].concentration", "ingredient": "Malt extract",
    "source_amount": 3, "source_unit": "g", "target": {"value": "3", "unit": "G_PER_L"},
    "decision": "verified at source nominal batch/provider basis", "source_annotations_retained":
    true}, {"field_path": "ingredients[5].concentration", "ingredient": "Polypepton
    (Nihon Pharm. Co.)", "source_amount": 5, "source_unit": "g", "target": {"value":
    "5", "unit": "G_PER_L"}, "decision": "verified at source nominal batch/provider
    basis", "source_annotations_retained": true}]'
- assessment_id: water
  area: quantity
  topic: ingredients[0].concentration
  outcome: concern
  summary: 'correct: source water1L is recorded as1G_PER_L in both full local files.
    Restore the literal solvent volume with its preparation/batch context; neither
    density nor measured final volume is established by this row.'
  target_ids:
  - CultureMech:010188
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - context
- assessment_id: preparation
  area: completeness
  topic: Primary collection sterilization context
  outcome: concern
  summary: The primary JCM header supplies an applicable default autoclave instruction
    absent from both target and owner. TOGO omits that collection header but does
    not override it. The primary recipe supplies no pH, strain-specific incubation
    or growth experiment to add.
  target_ids:
  - CultureMech:010188
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
- assessment_id: grounding-scope
  area: grounding
  topic: Verified mappings and undefined material scope
  outcome: supported
  summary: Water, glucose and agar IDs/labels resolve and their three current secondary
    keys are supported by the pinned index. Primary and secondary linkage are each3/6(50%)
    of direct ingredient instances, not a correctness score. The three supplied digest/extract
    ingredients remain unmapped rather than receiving pure-molecule IDs.
  target_ids:
  - CultureMech:010188
  evidence_ids:
  - record
  - jcm
  - togo
  - mim
  - chebi15377
  - chebi17234
  - chebi2509
- assessment_id: classification
  area: scope
  topic: Undefined agar recipe and imported annotations
  outcome: supported
  summary: COMPLEX/UNDEFINED and SOLID_AGAR agree with the supplied ingredients. Role/property
    notes exactly retain the source database annotations; those annotations and generic
    cultivation are not experimental evidence of organism growth. The source25% title
    is not used to infer an unstated percentage basis.
  target_ids:
  - CultureMech:010188
  evidence_ids:
  - record
  - jcm
  - togo
  - context
- assessment_id: audit
  area: provenance
  topic: History and claim-level evidence
  outcome: concern
  summary: All target/owner history timestamps parse with timezones. Source notes
    resolve to the correct provider and collection, but no narrow quantity or preparation
    evidence is present in either full file. The reference gate checked zero excerpts.
  target_ids:
  - CultureMech:010188
  evidence_ids:
  - record
  - owner-0
  - context
  - validate-references
findings:
- finding_id: f1
  issue_key: CM010188-water-volume-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Source water volume is represented as mass concentration
  description: The source1L distilled-water row is encoded as1G_PER_L in both layers,
    despite correct solute numerals.
  target_ids:
  - CultureMech:010188
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M77_25_Glucose_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM010188-source-sterilization-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Primary JCM sterilization instruction is absent
  description: Both full records lack the applicable primary collection default of
    autoclaving at121 degrees C for15minutes; no recipe-specific override is stated.
  target_ids:
  - CultureMech:010188
  field_paths:
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M77_25_Glucose_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: CM010188-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source notes lack exact claim-scoped evidence
  description: Provider links and import history identify the formulation but do not
    attach exact supporting excerpts to quantities, supplied forms and preparation.
  target_ids:
  - CultureMech:010188
  field_paths:
  - references
  - ingredients[*].evidence
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M77_25_Glucose_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Correct the maintained solvent-volume representation and inspect TOGO
    unit handling; preserve source batch context without a density or final-volume
    assumption before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010188
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M77_25_Glucose_Medium.yaml
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
  description: Add source-scoped sterilization and narrow evidence to the owner, then
    regenerate; leave unspecified pH and incubation conditions unresolved.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010188
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M77_25_Glucose_Medium.yaml
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
  description: Add verified source metadata and short exact excerpts in the appropriate
    evidence slots, keeping nominal-batch interpretation separate from quotation.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010188
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M77_25_Glucose_Medium.yaml
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
- The review concerns one source-derived formulation, not organism-specific growth.
  Provider-declared g_l values corroborate concentrations but do not prove a measured
  final volume after solute addition.
tags:
- unreviewed-records
- batch-008
- generated-medium
```
