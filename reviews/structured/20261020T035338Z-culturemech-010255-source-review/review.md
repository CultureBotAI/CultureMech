# Source and formulation review: 1_10_r2a_broth (CultureMech:010255)

- Review: 20261020T035338Z-culturemech-010255-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-19T23:41:12Z
- Finished UTC: 2026-10-20T03:53:38Z
- Reviewer: OpenAI Codex with delegated source and validator checks (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M840/JCM805 identity and the commercial broth concentration are supported. Two major findings concern source water volume represented as mass concentration and omitted source preparation context. Both are already corrected in the maintained owner but absent from this generated snapshot.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 30 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 003 selects ordinals 21-30 after the first two reserved batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010255 | data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml | generated | 1_10_r2a_broth |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010255 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010255 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-003/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch003/030/strict.tsv |
| validate-terms | passed | True | CultureMech:010255 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010255 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010255 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010255.

The four documented recipes completed; interpret the scope of each separately.

### Exact source and commercial formulation

identity: supported. Targets: CultureMech:010255.

CultureMech:010255 identifies M840, explicitly derived from JCM805. Named commercial broth identity is retained in target. No additional tenfold dilution should be inferred from the recipe name.

### Both direct quantities

quantity: concern. Targets: CultureMech:010255.

ingredients[0] water1G_PER_L is incorrect: source gives1L or1000mL preparation water, correctly represented in owner. ingredients[1] commercial broth0.32G_PER_L is verified:0.32g/(1000mL/1000)=0.32g/L using explicit PDF final-volume heading, corroborated by API g_l. No constituent decomposition, density inference or stock calculation is needed.

### All asserted primary and secondary IDs

grounding: supported. Targets: CultureMech:010255.

Target water primary CHEBI and matching secondary MIM CHEBI key resolve. Commercial mixture remains ungrounded to a pure chemical. Primary and secondary linkage each1/2 ingredient instances (50%); these measure link presence, not accuracy.

### Source preparation context

completeness: concern. Targets: CultureMech:010255.

JCM page-level default sterilization applies to805 and is represented in owner but absent in target. Owner water-dissolution context and literal amount evidence also are absent. Source805 supplies no pH or incubation conditions; do not import parent839 pH.

### Complex liquid formulation and growth scope

scope: supported. Targets: CultureMech:010255.

COMPLEX/UNDEFINED/LIQUID matches source mixture and API complex flag. TOGO water-role and mixture-property notes are reproduced accurately, not experimental growth evidence. No organism, strain, yield or phenotype is asserted.

### Generated freshness and owner-only graph context

provenance: concern. Targets: CultureMech:010255.

Target August merge predates maintained September repair and October evidence curation. Owner literal PDF excerpts match inspected source. Source-duplicate parent003150 resolves, but exact full-strength parent equivalence is not established by this review; do not blindly transfer that interpretation. Correct source-supported regeneration is needed, not an unsupported current-generator blame.

## Findings

### f1: Generated water quantity retains the old dimensional error

major / open / confirmed; issue key: culturemech-010255-generated-water-unit-error.

Target water1G_PER_L contradicts source1L and the maintained owner volume correction. No density conversion supports the target value.

### f2: Generated record omits maintained source preparation context

major / open / confirmed; issue key: culturemech-010255-generated-preparation-omission.

Target lacks JCM source sterilization and preparation context restored in the owner. It also omits the scoped evidence and later curation provenance. The retained source URL does not replace these material preparation details.

## Recommended Actions And Acceptance Checks

### a1

During separately authorized regeneration retain the verified owner water volume and source evidence. Do not turn the volume addition into mass concentration or alter the supported premix concentration.

- Compare regenerated fields with source scope and verified owner evidence.
- Run all four documented target recipes and inspect actual excerpt checks.
- After authorized regeneration run merge freshness and verification gates.

### a2

During authorized regeneration retain source-supported preparation and evidence, while independently assessing owner-only parent graph semantics. Do not invent pH, incubation conditions or premix expansion.

- Compare regenerated fields with source scope and verified owner evidence.
- Run all four documented target recipes and inspect actual excerpt checks.
- After authorized regeneration run merge freshness and verification gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M840_1_10_R2A_Broth.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch003/030/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-003/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch003/030/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M840; $.meta and $.components[0].items | supports | M840 explicitly maps to JCM_M805, named DAIGO/Nihon Pharm. broth and water volume. |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=805; Complete GRMD805 page | supports | JCM805 confirms the named commercial powder amount and1L water, plus page-level default sterilization with no recipe exception. |
| pdf | https://www.bacmedia.dsmz.de/pdf/J805; Page1 table and volume heading | supports | JCM-attributed PDF gives premix0.32g, water1000mL and explicit final volume1000mL. |
| api | https://mediadive.dsmz.de/rest/medium/J805; $.data.medium and $.data.solutions[0] | supports | MediaDive J805 resolves and declares g_l0.32 on main volume1000mL with product attribute. |
| parent-source | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=839; GRMD839 recipe and premix comment | supports | Parent-source formulation names DAIGO availability but its listed component masses do not establish exact3.2g premix mass. |
| water-id | https://www.ebi.ac.uk/chebi/CHEBI:15377; ChEBI ID/name/formula | supports | CHEBI:15377 resolves to water. It supports identity, not the target unit conversion. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; CHEBI:15377 exact Distilled water row and companion metadata | supports | Single secondary key has a MAPPED Distilled water row. Packaged source commit6643131b0f12ab40b66f98135245fca04027e0e9; CSV SHA2564765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5. |
| parent | data/normalized_yaml/bacterial/1_10_r2a_broth.yaml; Complete source-duplicate context record read earlier in this batch, unchanged captured bytes | supports | CultureMech:003150 resolves to J805 and reciprocally identifies010255 as its TOGO source duplicate. Its maintained broth and water formulation matches this owner; that equality does not certify owner-only full-strength parent/premix semantics. |

## Limits And Additional Notes

- Owner-only quantitative parent equivalence to JCM839 is not automatically certified: its listed masses total3.15g versus3.2g implied by ten times the J805 dose. Preserve nominal source naming without inferring exact premix constituents.
- No supplier catalog/version or chemical expansion of the commercial DAIGO mixture is established. Context records are not additional reviewed targets.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T035338Z-culturemech-010255-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_10_r2a_broth (CultureMech:010255)'
started_at: '2026-10-19T23:41:12Z'
finished_at: '2026-10-20T03:53:38Z'
reviewer:
  identity: OpenAI Codex with delegated source and validator checks
  kind: agent
  independence: independent
  independence_basis: Review team did not author or edit the assessed recipe bytes;
    findings were assessed against the frozen checkout and inspected source documents.
    This is an agent review, not experimental verification.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: TOGO M840/JCM805 identity and the commercial broth concentration are supported.
  Two major findings concern source water volume represented as mass concentration
  and omitted source preparation context. Both are already corrected in the maintained
  owner but absent from this generated snapshot.
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
  - path: data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml
    sha256: 1f61472a3a3b38459e29efdcaae18c1f5235b7d3f5c78bb02379eb3c8059eb3d
    role: target
  - path: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
    sha256: 199ec4c42f3e624cad33b581c95fd5ffef8deda69f66b19443684b543a6c2c1b
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M840_1_10_R2A_Broth.yaml
    sha256: 63cc467886a9d69742df552b1cb986a3791259fa41a131a94c9a468303697453
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4754_Main_sol_J805.yaml
    sha256: 683388ceb96249761c3a916880b0808ef2087db68d2356497ddd188f814ff2af
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4803_Main_sol_J839.yaml
    sha256: ee706828e768ede3d43750ebc69c337ef81cf01574f1d7752cc682436aa4f33a
    role: context
  - path: data/normalized_yaml/bacterial/r2a_broth.yaml
    sha256: fbc213871f26e5a3a66dbd96376daf12451e31dac6be99d2d001258aba651aac
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
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/fetch_mediadive_solution_volumes.py
    sha256: 408cdfa3f5c446e8f9c32ac98d7ea8a3a36553b23c032f3b7551f6a1661fd39a
    role: context
  - path: scripts/import_mediadive_solutions.py
    sha256: f97db7607d76c46b75d2d2428e8a425a5735e52beb3a9c28fd0af03ab5b31aa8
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
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
  selection: Record 30 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 003 selects ordinals 21-30 after the
    first two reserved batches; saved bundles are published locally in path order.
    On fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010255
targets:
- target_id: CultureMech:010255
  path: data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml
  label: 1_10_r2a_broth
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M840_1_10_R2A_Broth.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010255
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch003/030/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-003/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch003/030/strict.tsv"
  target_ids:
  - CultureMech:010255
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010255
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010255
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
  - CultureMech:010255
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-20T03:53:38Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M840_1_10_R2A_Broth.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T03:53:38Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:42:36.741168Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch003/030/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-19T23:42:38.516568Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-003/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch003/030/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:42:40.921943Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_10_r2a_broth__effd6b5a.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:42:42.173478Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M840
  locator: $.meta and $.components[0].items
  accessed_at: '2026-10-19T23:37:55.497440Z'
  support: supports
  summary: M840 explicitly maps to JCM_M805, named DAIGO/Nihon Pharm. broth and water
    volume.
  snapshot_sha256: 1396b41438ffec14102cf65382cfc773c9f0bf935ad435454a2925841510c2d8
- evidence_id: jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=805
  locator: Complete GRMD805 page
  accessed_at: '2026-10-19T23:37:51.303327Z'
  support: supports
  summary: JCM805 confirms the named commercial powder amount and1L water, plus page-level
    default sterilization with no recipe exception.
  snapshot_sha256: 07e46ecb47ae02b5389216b4e58bb45c86aaa4f0404f242a5cc608b1db879c78
- evidence_id: pdf
  kind: primary_source
  reference: https://www.bacmedia.dsmz.de/pdf/J805
  locator: Page1 table and volume heading
  accessed_at: '2026-10-19T23:37:52.082619Z'
  support: supports
  summary: JCM-attributed PDF gives premix0.32g, water1000mL and explicit final volume1000mL.
  snapshot_sha256: d2ed0e24210fd6098a96168a5551c3f46492f9d4fda5140f8a29e0de8df98d54
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J805
  locator: $.data.medium and $.data.solutions[0]
  accessed_at: '2026-10-19T23:37:51.360159Z'
  support: supports
  summary: MediaDive J805 resolves and declares g_l0.32 on main volume1000mL with
    product attribute.
  snapshot_sha256: abf22ecf20c08b0bac5bc7adf608fa4f737c068ac9c317b795acfd7aea181ff7
- evidence_id: parent-source
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=839
  locator: GRMD839 recipe and premix comment
  accessed_at: '2026-10-19T23:37:52.053703Z'
  support: supports
  summary: Parent-source formulation names DAIGO availability but its listed component
    masses do not establish exact3.2g premix mass.
  snapshot_sha256: f5a394752fe5f901f82116bedd28e137e3bb097668a38b7102f233e90834b09a
- evidence_id: water-id
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:15377
  locator: ChEBI ID/name/formula
  accessed_at: '2026-10-19T23:32:48.413412Z'
  support: supports
  summary: CHEBI:15377 resolves to water. It supports identity, not the target unit
    conversion.
  snapshot_sha256: 1a98a50fba3aa8ec10dc2fd5c355cd22bc1a955252adbd43f4042fd2f1a3ee5d
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: CHEBI:15377 exact Distilled water row and companion metadata
  accessed_at: '2026-10-20T03:53:38Z'
  support: supports
  summary: Single secondary key has a MAPPED Distilled water row. Packaged source
    commit6643131b0f12ab40b66f98135245fca04027e0e9; CSV SHA2564765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5.
- evidence_id: parent
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
  locator: Complete source-duplicate context record read earlier in this batch, unchanged
    captured bytes
  accessed_at: '2026-10-20T03:53:38Z'
  support: supports
  summary: CultureMech:003150 resolves to J805 and reciprocally identifies010255 as
    its TOGO source duplicate. Its maintained broth and water formulation matches
    this owner; that equality does not certify owner-only full-strength parent/premix
    semantics.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010255
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact source and commercial formulation
  outcome: supported
  summary: CultureMech:010255 identifies M840, explicitly derived from JCM805. Named
    commercial broth identity is retained in target. No additional tenfold dilution
    should be inferred from the recipe name.
  target_ids:
  - CultureMech:010255
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  - pdf
- assessment_id: quantity
  area: quantity
  topic: Both direct quantities
  outcome: concern
  summary: 'ingredients[0] water1G_PER_L is incorrect: source gives1L or1000mL preparation
    water, correctly represented in owner. ingredients[1] commercial broth0.32G_PER_L
    is verified:0.32g/(1000mL/1000)=0.32g/L using explicit PDF final-volume heading,
    corroborated by API g_l. No constituent decomposition, density inference or stock
    calculation is needed.'
  target_ids:
  - CultureMech:010255
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  - pdf
  - api
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and secondary IDs
  outcome: supported
  summary: Target water primary CHEBI and matching secondary MIM CHEBI key resolve.
    Commercial mixture remains ungrounded to a pure chemical. Primary and secondary
    linkage each1/2 ingredient instances (50%); these measure link presence, not accuracy.
  target_ids:
  - CultureMech:010255
  evidence_ids:
  - record
  - water-id
  - mim
- assessment_id: preparation
  area: completeness
  topic: Source preparation context
  outcome: concern
  summary: JCM page-level default sterilization applies to805 and is represented in
    owner but absent in target. Owner water-dissolution context and literal amount
    evidence also are absent. Source805 supplies no pH or incubation conditions; do
    not import parent839 pH.
  target_ids:
  - CultureMech:010255
  evidence_ids:
  - record
  - owner-0
  - jcm
  - pdf
- assessment_id: classification
  area: scope
  topic: Complex liquid formulation and growth scope
  outcome: supported
  summary: COMPLEX/UNDEFINED/LIQUID matches source mixture and API complex flag. TOGO
    water-role and mixture-property notes are reproduced accurately, not experimental
    growth evidence. No organism, strain, yield or phenotype is asserted.
  target_ids:
  - CultureMech:010255
  evidence_ids:
  - record
  - togo
  - jcm
  - api
- assessment_id: ownership
  area: provenance
  topic: Generated freshness and owner-only graph context
  outcome: concern
  summary: Target August merge predates maintained September repair and October evidence
    curation. Owner literal PDF excerpts match inspected source. Source-duplicate
    parent003150 resolves, but exact full-strength parent equivalence is not established
    by this review; do not blindly transfer that interpretation. Correct source-supported
    regeneration is needed, not an unsupported current-generator blame.
  target_ids:
  - CultureMech:010255
  evidence_ids:
  - record
  - owner-0
  - parent
  - parent-source
  - pdf
findings:
- finding_id: f1
  issue_key: culturemech-010255-generated-water-unit-error
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Generated water quantity retains the old dimensional error
  description: Target water1G_PER_L contradicts source1L and the maintained owner
    volume correction. No density conversion supports the target value.
  target_ids:
  - CultureMech:010255
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  - pdf
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M840_1_10_R2A_Broth.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: culturemech-010255-generated-preparation-omission
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated record omits maintained source preparation context
  description: Target lacks JCM source sterilization and preparation context restored
    in the owner. It also omits the scoped evidence and later curation provenance.
    The retained source URL does not replace these material preparation details.
  target_ids:
  - CultureMech:010255
  field_paths:
  - preparation_steps
  - sterilization
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - jcm
  - pdf
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M840_1_10_R2A_Broth.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: During separately authorized regeneration retain the verified owner
    water volume and source evidence. Do not turn the volume addition into mass concentration
    or alter the supported premix concentration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010255
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M840_1_10_R2A_Broth.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Compare regenerated fields with source scope and verified owner evidence.
  - Run all four documented target recipes and inspect actual excerpt checks.
  - After authorized regeneration run merge freshness and verification gates.
- action_id: a2
  description: During authorized regeneration retain source-supported preparation
    and evidence, while independently assessing owner-only parent graph semantics.
    Do not invent pH, incubation conditions or premix expansion.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010255
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M840_1_10_R2A_Broth.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Compare regenerated fields with source scope and verified owner evidence.
  - Run all four documented target recipes and inspect actual excerpt checks.
  - After authorized regeneration run merge freshness and verification gates.
limitations:
- 'Owner-only quantitative parent equivalence to JCM839 is not automatically certified:
  its listed masses total3.15g versus3.2g implied by ten times the J805 dose. Preserve
  nominal source naming without inferring exact premix constituents.'
- No supplier catalog/version or chemical expansion of the commercial DAIGO mixture
  is established. Context records are not additional reviewed targets.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-003
- generated-medium
```
