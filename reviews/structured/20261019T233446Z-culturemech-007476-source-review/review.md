# Source and formulation review: 14 (CultureMech:007476)

- Review: 20261019T233446Z-culturemech-007476-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-19T23:30:30Z
- Finished UTC: 2026-10-19T23:34:46Z
- Reviewer: OpenAI Codex with delegated source and validator checks (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Generated record 14 is an unusable rendering of NBRC 13 Seawater Starch Agar. Its source amounts, salinity instruction and pH survive only in a concatenated ingredient descriptor; generic preparation instead names distilled water, and DEFINED annotations conflict with the source Soytone/seawater formulation. The maintained owner repairs several fields but still needs verified source identity and preparation handling before regeneration.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 18 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; batch002 covers ordinals11-20 after batch001. On fresh origin/main at this batch base, scripts/record_review.py list validated34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007476 | data/merge_yaml/merged/14.yaml | generated | 14 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007476 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007476 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch002/018/strict.tsv |
| validate-terms | passed | True | CultureMech:007476 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007476 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007476 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007476.

The four documented recipes completed; interpret the scope of each separately.

### Source accession, stable ID, and generated ownership

identity: supported. Targets: CultureMech:007476.

The import history and maintained owner identify NBRC 13, Seawater Starch Agar (SWS). The numeric local filename/name is not the source accession. The stable CultureMech identifier and merge-event owner agree; the source identity is recoverable despite the uninformative generated name.

### Asserted ingredient identifiers, MIM linkage, and solution references

grounding: concern. Targets: CultureMech:007476.

Neither of the two generated ingredient descriptors carries a chemical CURIE, MIM link, or stock-solution reference. No nonexistent ontology identifier or broken internal link is asserted. The malformed descriptor and empty name must be repaired before ingredient grounding can be assessed meaningfully.

Primary term presence=0/2 encoded descriptors; MIM-link presence=0/2. Those denominators describe encoded rows, not the 4 source components. Owner-only chemical identifiers are not certified by this generated-target review. No replacement ontology identifier is proposed without independent verification.

### History, evidence placement, and source-to-output freshness

provenance: concern. Targets: CultureMech:007476.

The generated August 6 merge predates the maintained August composition recovery and September metadata updates. The later owner history and references are absent from generated output. The historical import source remains recoverable, but there is no scoped ingredient evidence in the target.

The reference validator performed zero excerpt checks. Inline curation history is part of the recipe, not a standalone HistoryRecord. Preserve historical events; do not backdate or rewrite them to imply a generated repair occurred. Follow-up curation belongs in the maintained owner and generation path. The inspected merger code, schema and source-owner bytes are included in the frozen input capture.

### All encoded quantities and source preparation compartments

quantity: concern. Targets: CultureMech:007476.

Both generated quantity rows require reconstruction. The source seawater salinity is a retained formulation condition, not a basis for inventing its individual ion concentrations.

ingredients[0]: correct; the full four-component recipe, pH and seawater footnote are concatenated under a variable/VARIABLE quantity. ingredients[1]: correct; unnamed descriptor with nonnumeric Soytone/G_PER_L. Source amounts: Soytone 1 g, soluble starch 10 g, seawater at 2% salinity 1 L, agar 15 g. The maintained owner preserves all four rows, water as volume, and pH 8.2. Source masses belong to this water-addition batch, not an independently measured final volume. Preserve the source 2% salinity wording; its mass/volume convention is unspecified. No saline density, artificial seawater formula, or seawater-ion expansion is verified.

### Preparation and classification correspondence

consistency: concern. Targets: CultureMech:007476.

The pH 8.2 and seawater-dilution text survive in the ingredient blob but are absent from operative structured preparation. Step 1 instead dissolves in distilled water. Both DEFINED classifications contradict the source mixture character; the owner already uses COMPLEX/UNDEFINED.

Source specifies diluted artificial or natural seawater at 2% salinity, not substitution with distilled water alone. Source agar supports SOLID_AGAR. The autoclaving description is assigned DISSOLVE and no sterilization protocol is given on the inspected page. The maintained name remains 14 even though its media_term identifies NBRC 13. No source culture result or organism identifier is asserted by the target.

## Findings

### f1: Generated ingredient rows collapse the source formulation

blocker / open / confirmed; issue key: cm-007476-generated-component-collapse.

A concatenated ingredient/protocol blob and an unnamed Soytone/G_PER_L row replace the four source ingredients. Source identity resolves to NBRC 13 SWS, while both the target name and maintained name remain numeric local labels.

### f2: Operative preparation loses seawater and specified pH context

major / open / confirmed; issue key: cm-007476-preparation-solvent-and-ph.

The source requires diluted seawater at 2% salinity and pH 8.2. Those instructions are stranded in ingredients[0], while preparation says dissolve in distilled water and adjust pH if needed. Its autoclaving sentence is miscoded as DISSOLVE and lacks inspected source support.

### f3: Defined annotations conflict with the source mixture

major / open / confirmed; issue key: cm-007476-defined-classification.

medium_type and composition_type are both DEFINED although the formulation includes Soytone and incompletely specified natural/artificial seawater. Soytone is an enzymatic soy digest, not a fully enumerated chemical composition. The maintained owner already classifies the formulation as COMPLEX/UNDEFINED.

## Recommended Actions And Acceptance Checks

### a1

Reconcile the maintained source name/accession and four-component formulation, then regenerate this target. Preserve the stable CultureMech identifier and the seawater preparation boundary.

- Require 4 distinct source components with numerical amounts and appropriate units; preserve the stated water batch basis without asserting an unmeasured final volume.
- Represent the exact source medium name and NBRC 13 accession without confusing them with the historical filename 14.
- Retain 1 L seawater at the stated 2% salinity rather than a mass unit or an invented defined seawater composition.
- After separately authorized curation/regeneration, run all four documented target recipes, just verify-merges, just audit-merge-freshness, and an explicit source-to-output component comparison.

### a2

Preserve the source seawater preparation and pH in maintained structured fields, distinguish source instructions from inferred operations, and verify any sterilization assertion before regeneration.

- The operative recipe retains pH 8.2 and seawater diluted to the stated 2% salinity.
- Distilled water is not substituted for the entire seawater medium.
- No unsupported autoclave method/cycle or action-token mismatch remains.

### a3

Verify and propagate the source-consistent COMPLEX/UNDEFINED classification through the maintained generation path.

- Both classification axes agree with the schema definitions and source mixture character.
- Do not expand the Soytone or unspecified seawater into guessed chemicals to preserve a DEFINED flag.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/14.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_14.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/14.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/14.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch002/018/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch002/018/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/14.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/14.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=13; Medium Detail Information; four Composition rows; pH statement; seawater footnote | supports | NBRC 13 identifies Seawater Starch Agar (SWS): Soytone 1 g, soluble starch 10 g, seawater at 2% salinity 1 L and agar 15 g; pH 8.2. It permits artificial or natural seawater diluted with distilled water. |
| soytone | https://www.thermofisher.com/order/catalog/product/212488; Difco Soytone product description and Features | supports | The manufacturer describes Soytone as an enzymatic soy digest containing vitamins and carbohydrates. This supports its chemically undefined mixture character, not exact catalog equivalence, supplier choice, animal-origin status, or a complete chemical expansion of the unspecified NBRC ingredient. |
| schema-classification | src/culturemech/schema/culturemech.yaml; MediumTypeEnum and MediumCompositionTypeEnum | supports | DEFINED requires known exact chemical composition; COMPLEX/UNDEFINED includes peptones and plant extracts. These definitions govern the target classification. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- This review certifies only the stated target/source comparisons. Maintained-owner ontology mappings and mass-per-liter normalization are not blanket-approved for regeneration.
- The NBRC recipe lists a water addition, not an independently measured final preparation volume. No density, molar-mass, or final-volume conversion is inferred.
- The recipe page does not establish a species-specific growth result or the bacterial category as a biological restriction. No taxon identifier, incubation condition, atmosphere, storage period or growth outcome is invented.
- A historical BD manual URL failed direct retrieval; the current manufacturer Soytone page was inspected instead. That page supports mixture classification only and does not identify the exact catalog used by NBRC.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T233446Z-culturemech-007476-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 14 (CultureMech:007476)'
started_at: '2026-10-19T23:30:30Z'
finished_at: '2026-10-19T23:34:46Z'
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
summary: Generated record 14 is an unusable rendering of NBRC 13 Seawater Starch Agar.
  Its source amounts, salinity instruction and pH survive only in a concatenated ingredient
  descriptor; generic preparation instead names distilled water, and DEFINED annotations
  conflict with the source Soytone/seawater formulation. The maintained owner repairs
  several fields but still needs verified source identity and preparation handling
  before regeneration.
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
  - path: data/merge_yaml/merged/14.yaml
    sha256: b28c23018127792ed2c3fd912b85abb5da6d90faae6ba6f7864984984e51d85e
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_14.yaml
    sha256: 5c19ac16e0d1ef0e32b41cc5ac599ff429fdd94fbc895af2976a91337e63a12d
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
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/recover_nbrc_composition.py
    sha256: a723e458895350a68ffae3e446006205b2e00cb185bee13976d5047be56405f0
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
  selection: Record 18 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; batch002 covers ordinals11-20 after batch001.
    On fresh origin/main at this batch base, scripts/record_review.py list validated34
    existing bundles and none listed this target path or ID. This bundle selects only
    the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007476
targets:
- target_id: CultureMech:007476
  path: data/merge_yaml/merged/14.yaml
  label: '14'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_14.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/14.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007476
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/14.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch002/018/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch002/018/strict.tsv"
  target_ids:
  - CultureMech:007476
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/14.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007476
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/14.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007476
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
  - CultureMech:007476
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/14.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-19T23:34:46Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_14.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-19T23:34:46Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/14.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:32:02.616443Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/14.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch002/018/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-19T23:32:04.149757Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch002/018/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/14.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:32:06.062994Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/14.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:32:07.073424Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=13
  locator: Medium Detail Information; four Composition rows; pH statement; seawater
    footnote
  accessed_at: '2026-10-19T23:29:38Z'
  support: supports
  summary: 'NBRC 13 identifies Seawater Starch Agar (SWS): Soytone 1 g, soluble starch
    10 g, seawater at 2% salinity 1 L and agar 15 g; pH 8.2. It permits artificial
    or natural seawater diluted with distilled water.'
  snapshot_sha256: 3f69311178eebf7b07fb164252964eb7eefd503170f0b52cb8cb8b66dae042a0
- evidence_id: soytone
  kind: primary_source
  reference: https://www.thermofisher.com/order/catalog/product/212488
  locator: Difco Soytone product description and Features
  accessed_at: '2026-10-19T23:32:13Z'
  support: supports
  summary: The manufacturer describes Soytone as an enzymatic soy digest containing
    vitamins and carbohydrates. This supports its chemically undefined mixture character,
    not exact catalog equivalence, supplier choice, animal-origin status, or a complete
    chemical expansion of the unspecified NBRC ingredient.
  snapshot_sha256: 40176ef4a41db3de3a1d789cf2dbcbfb41931b1ef79c6f87d80f02a5e4202f66
- evidence_id: schema-classification
  kind: authority
  reference: src/culturemech/schema/culturemech.yaml
  locator: MediumTypeEnum and MediumCompositionTypeEnum
  accessed_at: '2026-10-19T23:34:46Z'
  support: supports
  summary: DEFINED requires known exact chemical composition; COMPLEX/UNDEFINED includes
    peptones and plant extracts. These definitions govern the target classification.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007476
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Source accession, stable ID, and generated ownership
  outcome: supported
  summary: The import history and maintained owner identify NBRC 13, Seawater Starch
    Agar (SWS). The numeric local filename/name is not the source accession. The stable
    CultureMech identifier and merge-event owner agree; the source identity is recoverable
    despite the uninformative generated name.
  target_ids:
  - CultureMech:007476
  evidence_ids:
  - record
  - owner-0
  - nbrc
- assessment_id: grounding
  area: grounding
  topic: Asserted ingredient identifiers, MIM linkage, and solution references
  outcome: concern
  summary: Neither of the two generated ingredient descriptors carries a chemical
    CURIE, MIM link, or stock-solution reference. No nonexistent ontology identifier
    or broken internal link is asserted. The malformed descriptor and empty name must
    be repaired before ingredient grounding can be assessed meaningfully.
  target_ids:
  - CultureMech:007476
  evidence_ids:
  - record
  - owner-0
  details: Primary term presence=0/2 encoded descriptors; MIM-link presence=0/2. Those
    denominators describe encoded rows, not the 4 source components. Owner-only chemical
    identifiers are not certified by this generated-target review. No replacement
    ontology identifier is proposed without independent verification.
- assessment_id: provenance
  area: provenance
  topic: History, evidence placement, and source-to-output freshness
  outcome: concern
  summary: The generated August 6 merge predates the maintained August composition
    recovery and September metadata updates. The later owner history and references
    are absent from generated output. The historical import source remains recoverable,
    but there is no scoped ingredient evidence in the target.
  target_ids:
  - CultureMech:007476
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - validate-references
  details: The reference validator performed zero excerpt checks. Inline curation
    history is part of the recipe, not a standalone HistoryRecord. Preserve historical
    events; do not backdate or rewrite them to imply a generated repair occurred.
    Follow-up curation belongs in the maintained owner and generation path. The inspected
    merger code, schema and source-owner bytes are included in the frozen input capture.
- assessment_id: quantities
  area: quantity
  topic: All encoded quantities and source preparation compartments
  outcome: concern
  summary: Both generated quantity rows require reconstruction. The source seawater
    salinity is a retained formulation condition, not a basis for inventing its individual
    ion concentrations.
  target_ids:
  - CultureMech:007476
  evidence_ids:
  - record
  - owner-0
  - nbrc
  details: 'ingredients[0]: correct; the full four-component recipe, pH and seawater
    footnote are concatenated under a variable/VARIABLE quantity. ingredients[1]:
    correct; unnamed descriptor with nonnumeric Soytone/G_PER_L. Source amounts: Soytone
    1 g, soluble starch 10 g, seawater at 2% salinity 1 L, agar 15 g. The maintained
    owner preserves all four rows, water as volume, and pH 8.2. Source masses belong
    to this water-addition batch, not an independently measured final volume. Preserve
    the source 2% salinity wording; its mass/volume convention is unspecified. No
    saline density, artificial seawater formula, or seawater-ion expansion is verified.'
- assessment_id: conditions
  area: consistency
  topic: Preparation and classification correspondence
  outcome: concern
  summary: The pH 8.2 and seawater-dilution text survive in the ingredient blob but
    are absent from operative structured preparation. Step 1 instead dissolves in
    distilled water. Both DEFINED classifications contradict the source mixture character;
    the owner already uses COMPLEX/UNDEFINED.
  target_ids:
  - CultureMech:007476
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - soytone
  - schema-classification
  details: Source specifies diluted artificial or natural seawater at 2% salinity,
    not substitution with distilled water alone. Source agar supports SOLID_AGAR.
    The autoclaving description is assigned DISSOLVE and no sterilization protocol
    is given on the inspected page. The maintained name remains 14 even though its
    media_term identifies NBRC 13. No source culture result or organism identifier
    is asserted by the target.
findings:
- finding_id: f1
  issue_key: cm-007476-generated-component-collapse
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated ingredient rows collapse the source formulation
  description: A concatenated ingredient/protocol blob and an unnamed Soytone/G_PER_L
    row replace the four source ingredients. Source identity resolves to NBRC 13 SWS,
    while both the target name and maintained name remain numeric local labels.
  target_ids:
  - CultureMech:007476
  field_paths:
  - name
  - original_name
  - ingredients[0]
  - ingredients[1]
  - media_term
  evidence_ids:
  - record
  - owner-0
  - nbrc
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_14.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: cm-007476-preparation-solvent-and-ph
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Operative preparation loses seawater and specified pH context
  description: The source requires diluted seawater at 2% salinity and pH 8.2. Those
    instructions are stranded in ingredients[0], while preparation says dissolve in
    distilled water and adjust pH if needed. Its autoclaving sentence is miscoded
    as DISSOLVE and lacks inspected source support.
  target_ids:
  - CultureMech:007476
  field_paths:
  - ph_value
  - preparation_steps[0]
  - preparation_steps[1]
  - preparation_steps[2]
  evidence_ids:
  - record
  - owner-0
  - nbrc
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_14.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: cm-007476-defined-classification
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Defined annotations conflict with the source mixture
  description: medium_type and composition_type are both DEFINED although the formulation
    includes Soytone and incompletely specified natural/artificial seawater. Soytone
    is an enzymatic soy digest, not a fully enumerated chemical composition. The maintained
    owner already classifies the formulation as COMPLEX/UNDEFINED.
  target_ids:
  - CultureMech:007476
  field_paths:
  - medium_type
  - composition_type
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - soytone
  - schema-classification
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_14.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Reconcile the maintained source name/accession and four-component formulation,
    then regenerate this target. Preserve the stable CultureMech identifier and the
    seawater preparation boundary.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007476
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_14.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Require 4 distinct source components with numerical amounts and appropriate units;
    preserve the stated water batch basis without asserting an unmeasured final volume.
  - Represent the exact source medium name and NBRC 13 accession without confusing
    them with the historical filename 14.
  - Retain 1 L seawater at the stated 2% salinity rather than a mass unit or an invented
    defined seawater composition.
  - After separately authorized curation/regeneration, run all four documented target
    recipes, just verify-merges, just audit-merge-freshness, and an explicit source-to-output
    component comparison.
- action_id: a2
  description: Preserve the source seawater preparation and pH in maintained structured
    fields, distinguish source instructions from inferred operations, and verify any
    sterilization assertion before regeneration.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007476
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_14.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - The operative recipe retains pH 8.2 and seawater diluted to the stated 2% salinity.
  - Distilled water is not substituted for the entire seawater medium.
  - No unsupported autoclave method/cycle or action-token mismatch remains.
- action_id: a3
  description: Verify and propagate the source-consistent COMPLEX/UNDEFINED classification
    through the maintained generation path.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007476
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_14.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Both classification axes agree with the schema definitions and source mixture
    character.
  - Do not expand the Soytone or unspecified seawater into guessed chemicals to preserve
    a DEFINED flag.
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- This review certifies only the stated target/source comparisons. Maintained-owner
  ontology mappings and mass-per-liter normalization are not blanket-approved for
  regeneration.
- The NBRC recipe lists a water addition, not an independently measured final preparation
  volume. No density, molar-mass, or final-volume conversion is inferred.
- The recipe page does not establish a species-specific growth result or the bacterial
  category as a biological restriction. No taxon identifier, incubation condition,
  atmosphere, storage period or growth outcome is invented.
- A historical BD manual URL failed direct retrieval; the current manufacturer Soytone
  page was inspected instead. That page supports mixture classification only and does
  not identify the exact catalog used by NBRC.
tags:
- unreviewed-records
- batch-002
- generated-medium
```
