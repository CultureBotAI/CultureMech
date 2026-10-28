# Source and formulation review: 25_glucose_medium (CultureMech:003216)

- Review: 20261021T072145Z-culturemech-003216-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T07:17:48Z
- Finished UTC: 2026-10-21T07:21:45Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM86 and MediaDiveJ86 support all five solute concentrations in this agar medium. The generated record omits source-specific Polypepton, solvent and mapping/reference corrections already present in its owner. Both layers omit the primary collection sterilization instruction and narrow formulation evidence.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 72; batch 008 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding seven task batches contain 70 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 72 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003216 | data/merge_yaml/merged/25_glucose_medium.yaml | generated | 25_glucose_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003216 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003216 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/072/strict.tsv |
| validate-terms | passed | True | CultureMech:003216 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003216 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003216 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003216.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:003216.

2 primary CHEBI identities resolve with matching labels; 2 of 2 current secondary keys have live pinned-index rows. Unresolved keys: [].

5 direct ingredient instances; CHEBI-primary instance linkage 2/5 (40.00%), verified secondary coverage 2/5 (40.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### JCM86 agar formulation

identity: supported. Targets: CultureMech:003216.

Stable ID, original25% GLUCOSE title, J86 and the JCM86 URL identify the same formulation. The numerical title is preserved without inventing a mass/volume percentage basis. No stock or organism reference is asserted.

### Every direct target concentration

quantity: supported. Targets: CultureMech:003216.

verified: all five gram-per-liter values match explicit provider g_l fields, including glucose250 and agar25. The primary source lists gram amounts with1L water, while the API declares a main-solution volume; support is for provider concentrations, not an independently measured final volume. No agar molarity or mixture molecular weight is adopted from provider metadata.

[{"field_path": "ingredients[0].concentration", "ingredient": "Glucose", "target": {"value": "250", "unit": "G_PER_L"}, "source_amount_g": 250, "provider_g_l": 250, "decision": "verified provider-declared concentration", "source_attribute": null}, {"field_path": "ingredients[1].concentration", "ingredient": "Polypeptone", "target": {"value": "5", "unit": "G_PER_L"}, "source_amount_g": 5, "provider_g_l": 5, "decision": "verified provider-declared concentration", "source_attribute": "Nihon Pharm. Co."}, {"field_path": "ingredients[2].concentration", "ingredient": "Malt extract", "target": {"value": "3", "unit": "G_PER_L"}, "source_amount_g": 3, "provider_g_l": 3, "decision": "verified provider-declared concentration", "source_attribute": null}, {"field_path": "ingredients[3].concentration", "ingredient": "Yeast extract", "target": {"value": "3", "unit": "G_PER_L"}, "source_amount_g": 3, "provider_g_l": 3, "decision": "verified provider-declared concentration", "source_attribute": null}, {"field_path": "ingredients[4].concentration", "ingredient": "Agar", "target": {"value": "25", "unit": "G_PER_L"}, "source_amount_g": 25, "provider_g_l": 25, "decision": "verified provider-declared concentration", "source_attribute": null}]

### Supplied material, water and source metadata

completeness: concern. Targets: CultureMech:003216.

The owner restores source Polypepton manufacturer wording, a water row, a yeast-extract FOODON identity and references absent from the target. The owner water1000ML_PER_L is a nominal formulation representation; preserve the literal1L solvent-batch input and review its denominator context before regeneration. A mass concentration or measured final volume is not established for water.

### Generated and maintained linkage scope

grounding: supported. Targets: CultureMech:003216.

Target primary and secondary CHEBI linkage are each2/5(40%) of direct ingredient instances. The owner has4/6 primary identifiers across CHEBI/FOODON, including3 CHEBI identities, and3 secondary fields. All asserted material IDs resolve; supplied Polypepton and malt extract remain ungrounded rather than receiving invented pure-molecule identifiers. These percentages measure linkage only.

### Source default sterilization and condition limits

completeness: concern. Targets: CultureMech:003216.

Both full local records omit the collection default autoclave instruction available on the primary page. No source pH, incubation condition or strain-specific growth evidence was found in the inspected recipe; those values are not invented.

### Undefined agar formulation

scope: supported. Targets: CultureMech:003216.

COMPLEX/UNDEFINED agrees with supplied digests/extracts and SOLID_AGAR with25g source agar. Generic microbial cultivation establishes no organism-specific growth result or taxonomic exclusivity.

### History and exact evidence placement

provenance: concern. Targets: CultureMech:003216.

All target/owner history timestamps parse with timezones. The owner has later source repair metadata and a reachable reference, but no exact narrow quantity/preparation excerpts. The target reference gate examined zero excerpts.

## Findings

### f1: Generated record lacks source-backed owner corrections

major / open / confirmed; issue key: CM003216-stale-source-material-solvent.

The target retains generic Polypeptone, omits source water and lacks the later yeast mapping/reference context available in its owner.

### f2: JCM sterilization instruction is missing in both layers

major / open / confirmed; issue key: CM003216-source-sterilization-missing.

The primary collection header specifies autoclaving at121 degrees C for15minutes unless otherwise stated; this recipe provides no override and both local records lack preparation instructions.

### f3: Source notes lack narrow claim excerpts

minor / open / confirmed; issue key: CM003216-claim-evidence-gap.

Source URLs and maintained annotations identify the formulation but do not attach exact excerpt support to its quantities, supplied materials or sterilization.

## Recommended Actions And Acceptance Checks

### a1

Verify owner supplied forms and solvent-batch semantics against JCM86, then regenerate and confirm corrected material, quantity context and provenance survive.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add the source-scoped collection instruction and exact supporting evidence in the maintained owner before regeneration; do not invent pH or growth conditions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Add verified metadata and short exact claim-scoped excerpts, preserving provider concentration scope and separating calculations from quotation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/25_glucose_medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/25_glucose_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/25_glucose_medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/25_glucose_medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch008/072/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/072/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/25_glucose_medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/25_glucose_medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/25_glucose_medium.yaml:1:id: CultureMech:003216<br>./data/merge_yaml/merged/25_glucose_medium.yaml:1:id: CultureMech:003216<br> |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17234 resolves to glucose and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:2509 resolves to agar and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=86; GRMD86; complete recipe; collection header | supports | Complete primary six-row recipe and collection header inspected. Glucose250g, Polypepton5g, malt and yeast extracts3g each, agar25g and distilled water1.0L are explicit. The header supplies autoclaving at121 degrees C for15 minutes unless otherwise stated. No pH is specified. |
| mediadive | https://mediadive.dsmz.de/rest/medium/J86; data.medium; solutions[0].volume and recipe[0:6] | supports | J86 resolves to the same JCM title and primary URL. All five solutes carry explicit g_l values; the main solution declares1000mL and a separate distilled-water1000mL row. The Polypeptone row retains the source manufacturer attribute. |
| owner-foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426; Exact maintained-only ingredient identifier, canonical label and obsolete status | supports | FOODON:03315426 resolves to yeast extract; owner term and label match. |
| owner-chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact maintained-only ingredient identifier, canonical label and obsolete status | supports | CHEBI:15377 resolves to water; owner term and label match. |
| context | Full target, owner and captured MediaDive response; All five solutes, separate source water row and history timestamps | supports | {"quantities": [{"field_path": "ingredients[0].concentration", "ingredient": "Glucose", "target": {"value": "250", "unit": "G_PER_L"}, "source_amount_g": 250, "provider_g_l": 250, "decision": "verified provider-declared concentration", "source_attribute": null}, {"field_path": "ingredients[1].concentration", "ingredient": "Polypeptone", "target": {"value": "5", "unit": "G_PER_L"}, "source_amount_g": 5, "provider_g_l": 5, "decision": "verified provider-declared concentration", "source_attribute": "Nihon Pharm. Co."}, {"field_path": "ingredients[2].concentration", "ingredient": "Malt extract", "target": {"value": "3", "unit": "G_PER_L"}, "source_amount_g": 3, "provider_g_l": 3, "decision": "verified provider-declared concentration", "source_attribute": null}, {"field_path": "ingredients[3].concentration", "ingredient": "Yeast extract", "target": {"value": "3", "unit": "G_PER_L"}, "source_amount_g": 3, "provider_g_l": 3, "decision": "verified provider-declared concentration", "source_attribute": null}, {"field_path": "ingredients[4].concentration", "ingredient": "Agar", "target": {"value": "25", "unit": "G_PER_L"}, "source_amount_g": 25, "provider_g_l": 25, "decision": "verified provider-declared concentration", "source_attribute": null}], "source_water_row": {"recipe_order": 6, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "timezone_bearing_history_counts": [6, 6]} |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No organism-specific paper or experiment was assessed. The primary solvent amount is not proof of measured final volume; the source name25% does not license an unstated percent-basis conversion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T072145Z-culturemech-003216-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 25_glucose_medium (CultureMech:003216)'
started_at: '2026-10-21T07:17:48Z'
finished_at: '2026-10-21T07:21:45Z'
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
summary: JCM86 and MediaDiveJ86 support all five solute concentrations in this agar
  medium. The generated record omits source-specific Polypepton, solvent and mapping/reference
  corrections already present in its owner. Both layers omit the primary collection
  sterilization instruction and narrow formulation evidence.
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
  - path: data/merge_yaml/merged/25_glucose_medium.yaml
    sha256: 99ab8afab482d2dc01b64fb606ae410abc9b8954891c20d5e649e24d8ac7a5e2
    role: target
  - path: data/normalized_yaml/bacterial/25_glucose_medium.yaml
    sha256: 9b9b93167c7cc0b617b0dec417bc0bd52b7f0a5b756b976959ea66b92928c8a6
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
  selection: Task review 72; batch 008 item 2 of 10, selected in Python lexicographic
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
  - CultureMech:003216
targets:
- target_id: CultureMech:003216
  path: data/merge_yaml/merged/25_glucose_medium.yaml
  label: 25_glucose_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/25_glucose_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/25_glucose_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003216
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/25_glucose_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch008/072/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/072/strict.tsv"
  target_ids:
  - CultureMech:003216
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/25_glucose_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003216
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/25_glucose_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003216
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
  - CultureMech:003216
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/25_glucose_medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T07:21:44Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/25_glucose_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T07:21:44Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/25_glucose_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:18:15.503386Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/25_glucose_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch008/072/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T07:18:21.204606Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/072/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/25_glucose_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:18:28.298648Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/25_glucose_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:18:31.982443Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T07:21:44Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/25_glucose_medium.yaml:1:id: CultureMech:003216

    ./data/merge_yaml/merged/25_glucose_medium.yaml:1:id: CultureMech:003216

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
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
  accessed_at: '2026-10-21T07:21:44Z'
  support: supports
  summary: '{"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label":
    "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term":
    "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}'
- evidence_id: jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=86
  locator: GRMD86; complete recipe; collection header
  accessed_at: '2026-10-21T07:15:14.983727Z'
  support: supports
  summary: Complete primary six-row recipe and collection header inspected. Glucose250g,
    Polypepton5g, malt and yeast extracts3g each, agar25g and distilled water1.0L
    are explicit. The header supplies autoclaving at121 degrees C for15 minutes unless
    otherwise stated. No pH is specified.
  quote: Polypepton (Nihon Pharm. Co.) 5.0 g
  snapshot_sha256: fd786fbbbd5624f0eec2c80191c5596878fe86ba56315aaccbb7fc6d88652bd3
- evidence_id: mediadive
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J86
  locator: data.medium; solutions[0].volume and recipe[0:6]
  accessed_at: '2026-10-21T07:15:12.400616Z'
  support: supports
  summary: J86 resolves to the same JCM title and primary URL. All five solutes carry
    explicit g_l values; the main solution declares1000mL and a separate distilled-water1000mL
    row. The Polypeptone row retains the source manufacturer attribute.
  snapshot_sha256: 8a316173a59f91f180dc59ca7222665280119a2f8d1a91d6838da48d9370b9e9
- evidence_id: owner-foodon03315426
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426
  locator: Exact maintained-only ingredient identifier, canonical label and obsolete
    status
  accessed_at: '2026-10-21T07:15:14.683592Z'
  support: supports
  summary: FOODON:03315426 resolves to yeast extract; owner term and label match.
  snapshot_sha256: cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44
- evidence_id: owner-chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact maintained-only ingredient identifier, canonical label and obsolete
    status
  accessed_at: '2026-10-21T07:15:13.683527Z'
  support: supports
  summary: CHEBI:15377 resolves to water; owner term and label match.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: context
  kind: validation
  reference: Full target, owner and captured MediaDive response
  locator: All five solutes, separate source water row and history timestamps
  accessed_at: '2026-10-21T07:21:44Z'
  support: supports
  summary: '{"quantities": [{"field_path": "ingredients[0].concentration", "ingredient":
    "Glucose", "target": {"value": "250", "unit": "G_PER_L"}, "source_amount_g": 250,
    "provider_g_l": 250, "decision": "verified provider-declared concentration", "source_attribute":
    null}, {"field_path": "ingredients[1].concentration", "ingredient": "Polypeptone",
    "target": {"value": "5", "unit": "G_PER_L"}, "source_amount_g": 5, "provider_g_l":
    5, "decision": "verified provider-declared concentration", "source_attribute":
    "Nihon Pharm. Co."}, {"field_path": "ingredients[2].concentration", "ingredient":
    "Malt extract", "target": {"value": "3", "unit": "G_PER_L"}, "source_amount_g":
    3, "provider_g_l": 3, "decision": "verified provider-declared concentration",
    "source_attribute": null}, {"field_path": "ingredients[3].concentration", "ingredient":
    "Yeast extract", "target": {"value": "3", "unit": "G_PER_L"}, "source_amount_g":
    3, "provider_g_l": 3, "decision": "verified provider-declared concentration",
    "source_attribute": null}, {"field_path": "ingredients[4].concentration", "ingredient":
    "Agar", "target": {"value": "25", "unit": "G_PER_L"}, "source_amount_g": 25, "provider_g_l":
    25, "decision": "verified provider-declared concentration", "source_attribute":
    null}], "source_water_row": {"recipe_order": 6, "compound": "Distilled water",
    "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "timezone_bearing_history_counts":
    [6, 6]}'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003216
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '2 primary CHEBI identities resolve with matching labels; 2 of 2 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:003216
  evidence_ids:
  - record
  - mim
  - chebi17234
  - chebi2509
  details: 5 direct ingredient instances; CHEBI-primary instance linkage 2/5 (40.00%),
    verified secondary coverage 2/5 (40.00%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: JCM86 agar formulation
  outcome: supported
  summary: Stable ID, original25% GLUCOSE title, J86 and the JCM86 URL identify the
    same formulation. The numerical title is preserved without inventing a mass/volume
    percentage basis. No stock or organism reference is asserted.
  target_ids:
  - CultureMech:003216
  evidence_ids:
  - record
  - owner-0
  - id-search
  - jcm
  - mediadive
- assessment_id: amounts
  area: quantity
  topic: Every direct target concentration
  outcome: supported
  summary: 'verified: all five gram-per-liter values match explicit provider g_l fields,
    including glucose250 and agar25. The primary source lists gram amounts with1L
    water, while the API declares a main-solution volume; support is for provider
    concentrations, not an independently measured final volume. No agar molarity or
    mixture molecular weight is adopted from provider metadata.'
  target_ids:
  - CultureMech:003216
  evidence_ids:
  - record
  - jcm
  - mediadive
  - context
  details: '[{"field_path": "ingredients[0].concentration", "ingredient": "Glucose",
    "target": {"value": "250", "unit": "G_PER_L"}, "source_amount_g": 250, "provider_g_l":
    250, "decision": "verified provider-declared concentration", "source_attribute":
    null}, {"field_path": "ingredients[1].concentration", "ingredient": "Polypeptone",
    "target": {"value": "5", "unit": "G_PER_L"}, "source_amount_g": 5, "provider_g_l":
    5, "decision": "verified provider-declared concentration", "source_attribute":
    "Nihon Pharm. Co."}, {"field_path": "ingredients[2].concentration", "ingredient":
    "Malt extract", "target": {"value": "3", "unit": "G_PER_L"}, "source_amount_g":
    3, "provider_g_l": 3, "decision": "verified provider-declared concentration",
    "source_attribute": null}, {"field_path": "ingredients[3].concentration", "ingredient":
    "Yeast extract", "target": {"value": "3", "unit": "G_PER_L"}, "source_amount_g":
    3, "provider_g_l": 3, "decision": "verified provider-declared concentration",
    "source_attribute": null}, {"field_path": "ingredients[4].concentration", "ingredient":
    "Agar", "target": {"value": "25", "unit": "G_PER_L"}, "source_amount_g": 25, "provider_g_l":
    25, "decision": "verified provider-declared concentration", "source_attribute":
    null}]'
- assessment_id: owner-corrections
  area: completeness
  topic: Supplied material, water and source metadata
  outcome: concern
  summary: The owner restores source Polypepton manufacturer wording, a water row,
    a yeast-extract FOODON identity and references absent from the target. The owner
    water1000ML_PER_L is a nominal formulation representation; preserve the literal1L
    solvent-batch input and review its denominator context before regeneration. A
    mass concentration or measured final volume is not established for water.
  target_ids:
  - CultureMech:003216
  evidence_ids:
  - record
  - owner-0
  - jcm
  - mediadive
  - context
  - owner-foodon03315426
  - owner-chebi15377
- assessment_id: grounding-scope
  area: grounding
  topic: Generated and maintained linkage scope
  outcome: supported
  summary: Target primary and secondary CHEBI linkage are each2/5(40%) of direct ingredient
    instances. The owner has4/6 primary identifiers across CHEBI/FOODON, including3
    CHEBI identities, and3 secondary fields. All asserted material IDs resolve; supplied
    Polypepton and malt extract remain ungrounded rather than receiving invented pure-molecule
    identifiers. These percentages measure linkage only.
  target_ids:
  - CultureMech:003216
  evidence_ids:
  - record
  - owner-0
  - mim
  - chebi17234
  - chebi2509
  - owner-foodon03315426
  - owner-chebi15377
- assessment_id: preparation
  area: completeness
  topic: Source default sterilization and condition limits
  outcome: concern
  summary: Both full local records omit the collection default autoclave instruction
    available on the primary page. No source pH, incubation condition or strain-specific
    growth evidence was found in the inspected recipe; those values are not invented.
  target_ids:
  - CultureMech:003216
  evidence_ids:
  - record
  - owner-0
  - jcm
- assessment_id: classification
  area: scope
  topic: Undefined agar formulation
  outcome: supported
  summary: COMPLEX/UNDEFINED agrees with supplied digests/extracts and SOLID_AGAR
    with25g source agar. Generic microbial cultivation establishes no organism-specific
    growth result or taxonomic exclusivity.
  target_ids:
  - CultureMech:003216
  evidence_ids:
  - record
  - jcm
  - mediadive
- assessment_id: audit
  area: provenance
  topic: History and exact evidence placement
  outcome: concern
  summary: All target/owner history timestamps parse with timezones. The owner has
    later source repair metadata and a reachable reference, but no exact narrow quantity/preparation
    excerpts. The target reference gate examined zero excerpts.
  target_ids:
  - CultureMech:003216
  evidence_ids:
  - record
  - owner-0
  - context
  - validate-references
findings:
- finding_id: f1
  issue_key: CM003216-stale-source-material-solvent
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated record lacks source-backed owner corrections
  description: The target retains generic Polypeptone, omits source water and lacks
    the later yeast mapping/reference context available in its owner.
  target_ids:
  - CultureMech:003216
  field_paths:
  - ingredients[1].preferred_term
  - ingredients
  - ingredients[3].term
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - jcm
  - mediadive
  - context
  - owner-foodon03315426
  - owner-chebi15377
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/25_glucose_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM003216-source-sterilization-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: JCM sterilization instruction is missing in both layers
  description: The primary collection header specifies autoclaving at121 degrees C
    for15minutes unless otherwise stated; this recipe provides no override and both
    local records lack preparation instructions.
  target_ids:
  - CultureMech:003216
  field_paths:
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/25_glucose_medium.yaml
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
  issue_key: CM003216-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source notes lack narrow claim excerpts
  description: Source URLs and maintained annotations identify the formulation but
    do not attach exact excerpt support to its quantities, supplied materials or sterilization.
  target_ids:
  - CultureMech:003216
  field_paths:
  - references
  - ingredients[*].evidence
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm
  - mediadive
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/25_glucose_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Verify owner supplied forms and solvent-batch semantics against JCM86,
    then regenerate and confirm corrected material, quantity context and provenance
    survive.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003216
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/25_glucose_medium.yaml
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
  description: Add the source-scoped collection instruction and exact supporting evidence
    in the maintained owner before regeneration; do not invent pH or growth conditions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003216
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/25_glucose_medium.yaml
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
  description: Add verified metadata and short exact claim-scoped excerpts, preserving
    provider concentration scope and separating calculations from quotation.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003216
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/25_glucose_medium.yaml
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
- No organism-specific paper or experiment was assessed. The primary solvent amount
  is not proof of measured final volume; the source name25% does not license an unstated
  percent-basis conversion.
tags:
- unreviewed-records
- batch-008
- generated-medium
```
