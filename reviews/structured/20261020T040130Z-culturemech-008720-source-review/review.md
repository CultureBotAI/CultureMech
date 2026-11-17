# Source and formulation review: 1_10_r2a_with_mes_ph6 (CultureMech:008720)

- Review: 20261020T040130Z-culturemech-008720-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-20T03:59:41Z
- Finished UTC: 2026-10-20T04:01:30Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The target resolves to TOGO M2127 / NBRC 1459. Its water amount uses a mass unit in place of the source volume; explicit pH is omitted; and a named commercial R2A premix is represented as an empty unknown solution without its supplier footnote. Other listed masses and optional-agar wording match the source. The same issues are present in the maintained owner.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 32 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008720 | data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml | generated | 1_10_r2a_with_mes_ph6 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008720 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008720 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/032/strict.tsv |
| validate-terms | passed | True | CultureMech:008720 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008720 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008720 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008720.

The four documented recipes completed; interpret the scope of each separately.

### Source identity and maintained ownership

identity: supported. Targets: CultureMech:008720.

The target ID/path and single normalized owner resolve. TOGO M2127 and NBRC 1459 identify the same medium; the generated scientific fields match the owner, so these defects are not created solely by a later multi-source merge.

The supplied original_name, accession and URLs correspond to the inspected source. No distinct source accessions are merged. CultureMech:008720 occurs as the same record across normalized/generated layers, not as an independent duplicate within the maintained corpus.

### ingredients[0].concentration

quantity: concern. Targets: CultureMech:008720.

correct: target 1 G_PER_L cannot encode the source 1 L water batch. This is a dimension error, not a density conversion to be guessed.

### ingredients[1].concentration

quantity: supported. Targets: CultureMech:008720.

verified source mass: MES 3.9 g in the source batch containing 1 L water; target 3.9 G_PER_L agrees numerically with nominal batch normalization.

Exact final volume after dissolution is not specified; do not invent density, a stock strength, further tenfold dilution, or a prepared-stock addition volume. The 1/10 name does not authorize dividing the source dose again.

### ingredients[2].concentration

quantity: supported. Targets: CultureMech:008720.

verified source mass: optional agar 15 g in the source batch containing 1 L water; target 15 G_PER_L agrees numerically with nominal batch normalization.

Exact final volume after dissolution is not specified; do not invent density, a stock strength, further tenfold dilution, or a prepared-stock addition volume. The 1/10 name does not authorize dividing the source dose again.

### solutions[0].concentration

quantity: supported. Targets: CultureMech:008720.

verified source mass: R2A Broth DAIGO 0.32 g in the source batch containing 1 L water; target 0.32 G_PER_L agrees numerically with nominal batch normalization.

Exact final volume after dissolution is not specified; do not invent density, a stock strength, further tenfold dilution, or a prepared-stock addition volume. The 1/10 name does not authorize dividing the source dose again.

### Named premix versus unknown solution

representation: concern. Targets: CultureMech:008720.

The source premix identity is retained only in preferred_term, while name says Unknown solution and composition is empty. No prepared stock, dilution or recipe link is supplied by the source. The omitted footnote gives a recoverable commercial product identity.

Three direct ingredient instances plus one solution descriptor are the four asserted source components. There are no inline composition amounts, nested stocks or internal CultureMech solution IDs to resolve. Empty composition does not prove a missing local stock exists: this is an opaque premix representation problem. A new generic R2A expansion would require its own exact product evidence and must not be inferred from a similarly named parent medium. The source footnote is present on the inspected page/API but not in either complete local record; this is a bounded field-level absence observation.

### Ontology identities, role annotations and linkage

grounding: supported. Targets: CultureMech:008720.

Both primary CHEBI IDs and both secondary MIM CHEBI keys resolve. Water and MES labels are supported at their asserted level of specificity; no salt or stereochemical form is invented.

Primary/secondary linkage covers 2/3 direct ingredients (66.67%, scale 0–100 percent); counting the unlinked opaque premix as a source component gives 2/4 (50%). These are linkage metrics, not correctness scores. Agar remains ungrounded, not wrongly grounded. TOGO annotations support the copied buffer/solvent/solidifying and defined/undefined notes as database annotations, not independent mechanistic or growth findings.

### pH, optional agar and missing protocol fields

completeness: concern. Targets: CultureMech:008720.

The title retains pH6 but neither local record has a structured pH value despite an explicit source value. SOLID_AGAR is consistent with the optional-agar branch and the optional wording remains present.

The source provides no detailed sterilization, incubation, storage or vessel procedure; do not synthesize one or treat absent optional protocol fields as established errors. Source pH is a distinct recoverable condition. There is no experimental growth result, taxon, strain, DOI or PMID to verify. Bacterial filing and generic cultivation application are not organism-level growth evidence.

### Provenance and concentration support placement

evidence: concern. Targets: CultureMech:008720.

Source URLs and accession are recoverable, and history records import, solution migration and generated merge. None of the four quantity assertions has scoped evidence in the complete local records; the reference gate examined zero excerpts.

History is reviewed as provenance, not proof that old mutators were correct. Actual historical execution was not replayed. No discussion flag or existing evidence object is being deleted or closed. Required deterministic checks passed; semantic defects survive those checks.

## Findings

### f1: Water volume is represented as a mass concentration

major / open / confirmed; issue key: culturemech-008720-water-unit-error.

The source specifies 1 L distilled water. Target and maintained owner instead assert 1 G_PER_L. No source density or mass conversion supports this representation.

### f2: Named commercial premix became an empty unknown solution

major / open / confirmed; issue key: culturemech-008720-premix-placeholder-and-identity-gap.

The mass-dosed R2A Broth DAIGO product is wrapped in a solution descriptor with an Unknown solution name and no composition or reference. The source supplier/product footnote is omitted. This does not identify a separately prepared stock or establish its composition.

### f3: Explicit source pH is missing from structured conditions

major / open / confirmed; issue key: culturemech-008720-source-ph-omitted.

Both primary collection page and structured API specify pH 6.0; the local name carries that cue but the schema condition field is absent in target and owner.

### f4: Quantity assertions have no scoped source evidence

minor / open / confirmed; issue key: culturemech-008720-quantity-evidence-gap.

All three direct amounts and the premix mass dose lack claim-level excerpts. Sources are recoverable, but a notes URL alone does not document each unit, optionality and batch basis.

## Recommended Actions And Acceptance Checks

### a1

Correct the maintained water representation to preserve its source volume/batch basis using schema-supported fields; inspect the source unit transform and regenerate derived records after authorized curation.

- Verify source units and batch context against NBRC 1459 and TOGO M2127.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on the maintained correction.
- After separately authorized regeneration, run just verify-merges and just audit-merge-freshness; confirm the corrected fields survive in this generated target.

### a2

Retain the exact named commercial premix and source product-code provenance in the maintained record. Use an appropriate opaque ingredient representation or explicitly justified solution model; remove the placeholder without inventing a generic R2A recipe or stock dose.

- Verify source units and batch context against NBRC 1459 and TOGO M2127.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on the maintained correction.
- After separately authorized regeneration, run just verify-merges and just audit-merge-freshness; confirm the corrected fields survive in this generated target.
- Verify product code 395-01681 against the source footnote and vendor listing, preserving source-era attribution separately from current manufacturer metadata.

### a3

Populate the source-supported pH using the maintained schema field and attach exact source evidence; do not infer additional preparation conditions.

- Verify source units and batch context against NBRC 1459 and TOGO M2127.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on the maintained correction.
- After separately authorized regeneration, run just verify-merges and just audit-merge-freshness; confirm the corrected fields survive in this generated target.

### a4

Add short exact supporting excerpts at schema-supported claim locations in the maintained input, with the source water-batch limitation explicit.

- Verify source units and batch context against NBRC 1459 and TOGO M2127.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on the maintained correction.
- After separately authorized regeneration, run just verify-merges and just audit-merge-freshness; confirm the corrected fields survive in this generated target.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/1_10_r2a_with_mes_ph6.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch004/032/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/032/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1459; Medium number/title, complete composition table and footnote | supports | NBRC 1459 names this medium and lists four components, pH and a supplier/product-code footnote. The water uses a volume unit, the agar is optional and the premix is identified by product name. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2127; meta; components[0].items[0:4]; comments[0:4] | supports | TOGO M2127 points to NBRC_M1459 and the same official URL. All four components, original units, component-role annotations, pH and supplier footnote were inspected. |
| product | https://labchem-wako.fujifilm.com/asia/product/detail/W01N0139-0168.html; Product title and number table, lines 29 and 60–67 of inspected page | supports | Official product page pairs R2A Broth DAIGO with code 395-01681 and a 300G package. It confirms a mass-packaged named commercial medium; it does not establish the identity of an arbitrary prepared R2A stock or the source-era manufacturer. |
| chebi-15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; OLS exact IRI response: identifier, preferred label, obsolete flag and available annotation | supports | CHEBI:15377 resolves to water and is not obsolete. The water definition supports the generic chemical identity; distilled grade remains in the ingredient label. |
| chebi-39010 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_39010; OLS exact IRI response: identifier, preferred label, obsolete flag and available annotation | supports | CHEBI:39010 resolves to MES and is not obsolete. MES has no definition/form annotation in this response. Label correspondence is verified, but a particular salt, hydrate, molarity or preparation grade is not inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact identifier matches and pinned metadata | supports | {"15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "39010": [{"label": "MES", "match_type": "preferred_term", "identifier": "CHEBI:39010", "preferred_term": "MES", "ontology_id": "CHEBI:39010", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| ids | repository checkout; Top-level exact CultureMech ID search | supports | ./data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml:1:id: CultureMech:008720<br>./data/normalized_yaml/bacterial/1_10_r2a_with_mes_ph6.yaml:1:id: CultureMech:008720<br> |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Collection sources specify a one-liter water batch, not a measured final solution volume. Solute G_PER_L values are assessed as nominal source-batch normalization; exact final-volume concentrations are not independently certified.
- The inspected TOGO HTML is only a JavaScript shell; evidence comes from its structured API and the inspected primary NBRC page.
- The product page confirms the name/code pairing only. Supplier/manufacturer naming varies across source eras; no historical production continuity or exact premix composition is inferred.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T040130Z-culturemech-008720-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_10_r2a_with_mes_ph6 (CultureMech:008720)'
started_at: '2026-10-20T03:59:41Z'
finished_at: '2026-10-20T04:01:30Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or edit the assessed recipe bytes. Source
    comparison and identifier checks are independent agent review, not experimental
    validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The target resolves to TOGO M2127 / NBRC 1459. Its water amount uses a mass
  unit in place of the source volume; explicit pH is omitted; and a named commercial
  R2A premix is represented as an empty unknown solution without its supplier footnote.
  Other listed masses and optional-agar wording match the source. The same issues
  are present in the maintained owner.
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
  - path: data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml
    sha256: c2357be0acdeee220c5af83025040433aacb255a910808ef71c5212b49dea717
    role: target
  - path: data/normalized_yaml/bacterial/1_10_r2a_with_mes_ph6.yaml
    sha256: 6eb715cd41a23504937c2b16514fe2ecb78aad3c8a3d55d672c1aab3e0661ecd
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
  selection: Record 32 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008720
targets:
- target_id: CultureMech:008720
  path: data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml
  label: 1_10_r2a_with_mes_ph6
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_with_mes_ph6.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008720
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch004/032/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/032/strict.tsv"
  target_ids:
  - CultureMech:008720
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008720
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008720
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
  - CultureMech:008720
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-20T04:01:29Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_10_r2a_with_mes_ph6.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T04:01:29Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T03:59:45.164912Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch004/032/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-20T03:59:46.760916Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/032/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T03:59:48.657619Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T03:59:49.640467Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1459
  locator: Medium number/title, complete composition table and footnote
  accessed_at: '2026-10-20T03:59:58.139415Z'
  support: supports
  summary: NBRC 1459 names this medium and lists four components, pH and a supplier/product-code
    footnote. The water uses a volume unit, the agar is optional and the premix is
    identified by product name.
  quote: Distilled water 1 L
  snapshot_sha256: 82123848f08a2a1ac63b2acc5ff15c040dd0cfd05beb4467b1e524ea243030c7
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2127
  locator: meta; components[0].items[0:4]; comments[0:4]
  accessed_at: '2026-10-20T03:59:59.526456Z'
  support: supports
  summary: TOGO M2127 points to NBRC_M1459 and the same official URL. All four components,
    original units, component-role annotations, pH and supplier footnote were inspected.
  snapshot_sha256: d96eef90e30187478343d83fe6785323f890015c1a9f700ec662100b5b611c92
- evidence_id: product
  kind: primary_source
  reference: https://labchem-wako.fujifilm.com/asia/product/detail/W01N0139-0168.html
  locator: Product title and number table, lines 29 and 60–67 of inspected page
  accessed_at: '2026-10-20T04:01:29Z'
  support: supports
  summary: Official product page pairs R2A Broth DAIGO with code 395-01681 and a 300G
    package. It confirms a mass-packaged named commercial medium; it does not establish
    the identity of an arbitrary prepared R2A stock or the source-era manufacturer.
- evidence_id: chebi-15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: 'OLS exact IRI response: identifier, preferred label, obsolete flag and
    available annotation'
  accessed_at: '2026-10-20T04:00:00.223561Z'
  support: supports
  summary: CHEBI:15377 resolves to water and is not obsolete. The water definition
    supports the generic chemical identity; distilled grade remains in the ingredient
    label.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi-39010
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_39010
  locator: 'OLS exact IRI response: identifier, preferred label, obsolete flag and
    available annotation'
  accessed_at: '2026-10-20T04:00:00.835716Z'
  support: supports
  summary: CHEBI:39010 resolves to MES and is not obsolete. MES has no definition/form
    annotation in this response. Label correspondence is verified, but a particular
    salt, hydrate, molarity or preparation grade is not inferred.
  snapshot_sha256: 66ff3b91a811729048d6f9d0452f6f2f951a50012862a413baae9c3a149cb096
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact identifier matches and pinned metadata
  accessed_at: '2026-10-20T04:01:29Z'
  support: supports
  summary: '{"15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "39010": [{"label":
    "MES", "match_type": "preferred_term", "identifier": "CHEBI:39010", "preferred_term":
    "MES", "ontology_id": "CHEBI:39010", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}'
- evidence_id: ids
  kind: record_content
  reference: repository checkout
  locator: Top-level exact CultureMech ID search
  accessed_at: '2026-10-20T04:01:29Z'
  support: supports
  summary: './data/merge_yaml/merged/1_10_r2a_with_mes_ph6.yaml:1:id: CultureMech:008720

    ./data/normalized_yaml/bacterial/1_10_r2a_with_mes_ph6.yaml:1:id: CultureMech:008720

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; normalized and generated
    layers distinguished.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008720
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Source identity and maintained ownership
  outcome: supported
  summary: The target ID/path and single normalized owner resolve. TOGO M2127 and
    NBRC 1459 identify the same medium; the generated scientific fields match the
    owner, so these defects are not created solely by a later multi-source merge.
  target_ids:
  - CultureMech:008720
  evidence_ids:
  - record
  - owner-0
  - ids
  - nbrc
  - togo
  details: The supplied original_name, accession and URLs correspond to the inspected
    source. No distinct source accessions are merged. CultureMech:008720 occurs as
    the same record across normalized/generated layers, not as an independent duplicate
    within the maintained corpus.
- assessment_id: water
  area: quantity
  topic: ingredients[0].concentration
  outcome: concern
  summary: 'correct: target 1 G_PER_L cannot encode the source 1 L water batch. This
    is a dimension error, not a density conversion to be guessed.'
  target_ids:
  - CultureMech:008720
  evidence_ids:
  - record
  - nbrc
  - togo
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for the water quantity/unit relative to its original batch
      representation
    evidence_ids:
    - nbrc
    - togo
- assessment_id: amount-mes
  area: quantity
  topic: ingredients[1].concentration
  outcome: supported
  summary: 'verified source mass: MES 3.9 g in the source batch containing 1 L water;
    target 3.9 G_PER_L agrees numerically with nominal batch normalization.'
  target_ids:
  - CultureMech:008720
  evidence_ids:
  - record
  - nbrc
  - togo
  details: Exact final volume after dissolution is not specified; do not invent density,
    a stock strength, further tenfold dilution, or a prepared-stock addition volume.
    The 1/10 name does not authorize dividing the source dose again.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Original source mass verified; nominal G_PER_L normalization only,
      with exact final-volume limitation explicit
    evidence_ids:
    - nbrc
    - togo
- assessment_id: amount-agar
  area: quantity
  topic: ingredients[2].concentration
  outcome: supported
  summary: 'verified source mass: optional agar 15 g in the source batch containing
    1 L water; target 15 G_PER_L agrees numerically with nominal batch normalization.'
  target_ids:
  - CultureMech:008720
  evidence_ids:
  - record
  - nbrc
  - togo
  details: Exact final volume after dissolution is not specified; do not invent density,
    a stock strength, further tenfold dilution, or a prepared-stock addition volume.
    The 1/10 name does not authorize dividing the source dose again.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Original source mass verified; nominal G_PER_L normalization only,
      with exact final-volume limitation explicit
    evidence_ids:
    - nbrc
    - togo
- assessment_id: amount-premix
  area: quantity
  topic: solutions[0].concentration
  outcome: supported
  summary: 'verified source mass: R2A Broth DAIGO 0.32 g in the source batch containing
    1 L water; target 0.32 G_PER_L agrees numerically with nominal batch normalization.'
  target_ids:
  - CultureMech:008720
  evidence_ids:
  - record
  - nbrc
  - togo
  details: Exact final volume after dissolution is not specified; do not invent density,
    a stock strength, further tenfold dilution, or a prepared-stock addition volume.
    The 1/10 name does not authorize dividing the source dose again.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Original source mass verified; nominal G_PER_L normalization only,
      with exact final-volume limitation explicit
    evidence_ids:
    - nbrc
    - togo
- assessment_id: stock
  area: representation
  topic: Named premix versus unknown solution
  outcome: concern
  summary: The source premix identity is retained only in preferred_term, while name
    says Unknown solution and composition is empty. No prepared stock, dilution or
    recipe link is supplied by the source. The omitted footnote gives a recoverable
    commercial product identity.
  target_ids:
  - CultureMech:008720
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - product
  details: 'Three direct ingredient instances plus one solution descriptor are the
    four asserted source components. There are no inline composition amounts, nested
    stocks or internal CultureMech solution IDs to resolve. Empty composition does
    not prove a missing local stock exists: this is an opaque premix representation
    problem. A new generic R2A expansion would require its own exact product evidence
    and must not be inferred from a similarly named parent medium. The source footnote
    is present on the inspected page/API but not in either complete local record;
    this is a bounded field-level absence observation.'
- assessment_id: chemistry
  area: grounding
  topic: Ontology identities, role annotations and linkage
  outcome: supported
  summary: Both primary CHEBI IDs and both secondary MIM CHEBI keys resolve. Water
    and MES labels are supported at their asserted level of specificity; no salt or
    stereochemical form is invented.
  target_ids:
  - CultureMech:008720
  evidence_ids:
  - record
  - chebi-15377
  - chebi-39010
  - mim
  - togo
  details: Primary/secondary linkage covers 2/3 direct ingredients (66.67%, scale
    0–100 percent); counting the unlinked opaque premix as a source component gives
    2/4 (50%). These are linkage metrics, not correctness scores. Agar remains ungrounded,
    not wrongly grounded. TOGO annotations support the copied buffer/solvent/solidifying
    and defined/undefined notes as database annotations, not independent mechanistic
    or growth findings.
- assessment_id: conditions
  area: completeness
  topic: pH, optional agar and missing protocol fields
  outcome: concern
  summary: The title retains pH6 but neither local record has a structured pH value
    despite an explicit source value. SOLID_AGAR is consistent with the optional-agar
    branch and the optional wording remains present.
  target_ids:
  - CultureMech:008720
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  details: The source provides no detailed sterilization, incubation, storage or vessel
    procedure; do not synthesize one or treat absent optional protocol fields as established
    errors. Source pH is a distinct recoverable condition. There is no experimental
    growth result, taxon, strain, DOI or PMID to verify. Bacterial filing and generic
    cultivation application are not organism-level growth evidence.
- assessment_id: evidence
  area: evidence
  topic: Provenance and concentration support placement
  outcome: concern
  summary: Source URLs and accession are recoverable, and history records import,
    solution migration and generated merge. None of the four quantity assertions has
    scoped evidence in the complete local records; the reference gate examined zero
    excerpts.
  target_ids:
  - CultureMech:008720
  evidence_ids:
  - record
  - owner-0
  - validate-references
  - nbrc
  - togo
  details: History is reviewed as provenance, not proof that old mutators were correct.
    Actual historical execution was not replayed. No discussion flag or existing evidence
    object is being deleted or closed. Required deterministic checks passed; semantic
    defects survive those checks.
findings:
- finding_id: f1
  issue_key: culturemech-008720-water-unit-error
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water volume is represented as a mass concentration
  description: The source specifies 1 L distilled water. Target and maintained owner
    instead assert 1 G_PER_L. No source density or mass conversion supports this representation.
  target_ids:
  - CultureMech:008720
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_with_mes_ph6.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: culturemech-008720-premix-placeholder-and-identity-gap
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Named commercial premix became an empty unknown solution
  description: The mass-dosed R2A Broth DAIGO product is wrapped in a solution descriptor
    with an Unknown solution name and no composition or reference. The source supplier/product
    footnote is omitted. This does not identify a separately prepared stock or establish
    its composition.
  target_ids:
  - CultureMech:008720
  field_paths:
  - solutions[0].name
  - solutions[0].composition
  - solutions[0].preferred_term
  - solutions[0].notes
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - product
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_with_mes_ph6.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.1
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech-008720-source-ph-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Explicit source pH is missing from structured conditions
  description: Both primary collection page and structured API specify pH 6.0; the
    local name carries that cue but the schema condition field is absent in target
    and owner.
  target_ids:
  - CultureMech:008720
  field_paths:
  - ph_value
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_with_mes_ph6.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: culturemech-008720-quantity-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Quantity assertions have no scoped source evidence
  description: All three direct amounts and the premix mass dose lack claim-level
    excerpts. Sources are recoverable, but a notes URL alone does not document each
    unit, optionality and batch basis.
  target_ids:
  - CultureMech:008720
  field_paths:
  - ingredients[*].evidence
  - evidence
  - references
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_with_mes_ph6.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Correct the maintained water representation to preserve its source
    volume/batch basis using schema-supported fields; inspect the source unit transform
    and regenerate derived records after authorized curation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008720
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_with_mes_ph6.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify source units and batch context against NBRC 1459 and TOGO M2127.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on the maintained correction.
  - After separately authorized regeneration, run just verify-merges and just audit-merge-freshness;
    confirm the corrected fields survive in this generated target.
- action_id: a2
  description: Retain the exact named commercial premix and source product-code provenance
    in the maintained record. Use an appropriate opaque ingredient representation
    or explicitly justified solution model; remove the placeholder without inventing
    a generic R2A recipe or stock dose.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008720
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_with_mes_ph6.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify source units and batch context against NBRC 1459 and TOGO M2127.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on the maintained correction.
  - After separately authorized regeneration, run just verify-merges and just audit-merge-freshness;
    confirm the corrected fields survive in this generated target.
  - Verify product code 395-01681 against the source footnote and vendor listing,
    preserving source-era attribution separately from current manufacturer metadata.
- action_id: a3
  description: Populate the source-supported pH using the maintained schema field
    and attach exact source evidence; do not infer additional preparation conditions.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008720
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_with_mes_ph6.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify source units and batch context against NBRC 1459 and TOGO M2127.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on the maintained correction.
  - After separately authorized regeneration, run just verify-merges and just audit-merge-freshness;
    confirm the corrected fields survive in this generated target.
- action_id: a4
  description: Add short exact supporting excerpts at schema-supported claim locations
    in the maintained input, with the source water-batch limitation explicit.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008720
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_with_mes_ph6.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify source units and batch context against NBRC 1459 and TOGO M2127.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on the maintained correction.
  - After separately authorized regeneration, run just verify-merges and just audit-merge-freshness;
    confirm the corrected fields survive in this generated target.
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- Collection sources specify a one-liter water batch, not a measured final solution
  volume. Solute G_PER_L values are assessed as nominal source-batch normalization;
  exact final-volume concentrations are not independently certified.
- The inspected TOGO HTML is only a JavaScript shell; evidence comes from its structured
  API and the inspected primary NBRC page.
- The product page confirms the name/code pairing only. Supplier/manufacturer naming
  varies across source eras; no historical production continuity or exact premix composition
  is inferred.
tags:
- unreviewed-records
- batch-004
- generated-medium
```
