# Source and formulation review: 245 (CultureMech:007480)

- Review: 20261021T072000Z-culturemech-007480-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T07:17:45Z
- Finished UTC: 2026-10-21T07:20:00Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated local record245 identifies NBRC244 but contains two malformed ingredient rows. The maintained owner has recovered the source formulation, pH and a reciprocal TOGO source-duplicate link and removed unsupported preparation defaults. These corrections have not reached the generated record, and several owner ontology labels need canonicalization.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 71; batch 008 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding seven task batches contain 70 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 72 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007480 | data/merge_yaml/merged/245.yaml | generated | 245 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007480 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007480 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/071/strict.tsv |
| validate-terms | passed | True | CultureMech:007480 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007480 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007480 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007480.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:007480.

0 primary CHEBI identities resolve with matching labels; 0 of 0 current secondary keys have live pinned-index rows. Unresolved keys: [].

2 direct ingredient instances; CHEBI-primary instance linkage 0/2 (0.00%), verified secondary coverage 0/2 (0.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Exact NBRC244 record and source-duplicate context

identity: supported. Targets: CultureMech:007480.

The local numeric record245 is resolved by stable ID, merge owner and explicit NBRC244 history. The primary page has no official title, so none is invented. The maintained reciprocal TOGO M1466 link resolves and shares the actual source formulation; it is not a reason to merge distinct source records solely by a fingerprint.

### Both malformed target rows and six recovered owner quantities

quantity: concern. Targets: CultureMech:007480.

correct: the target combines the full source table and pH into one ingredient name with VARIABLE quantity, plus a blank ingredient with textual concentration. The owner and child recover all six source numerals and volume units. Source seawater750mL plus water250mL describes a nominal one-liter liquid-input batch; it does not independently measure final volume after solutes. Preserve that basis and optional agar when verifying per-liter representations.

[["Yeast extract", "4", "G_PER_L"], ["Malt extract", "10", "G_PER_L"], ["Glucose", "4", "G_PER_L"], ["Seawater", "750", "ML_PER_L"], ["Distilled water", "250", "ML_PER_L"], ["Agar (if needed)", "20", "G_PER_L"]]

### pH, source term, mappings and reciprocal link

completeness: concern. Targets: CultureMech:007480.

The owner retains pH7.6, source identity, ingredient mappings, references and later reciprocal-link history missing from the generated target. The owner also removes the unsupported generic preparation list that remains in the target.

### Source scope and generated fallback protocol

evidence: concern. Targets: CultureMech:007480.

unsupported: neither inspected source supplies an autoclave protocol. The target fallback also says dissolve in distilled water, omitting the seawater context, and labels autoclaving DISSOLVE. Owner empty preparation is not proof that no preparation is possible; it avoids asserting these unsupported defaults. Source pH7.6 remains supported.

### Owner identity support versus canonical labels

grounding: concern. Targets: CultureMech:007480.

All six owner IDs resolve to the supplied general material classes: three CHEBI IDs, two FOODON extract terms and the ENVO sea-water term. Four labels differ from canonical labels (yeast extract, malt extract, sea water, agar). These are bounded label discrepancies, not wrong chemical identities. Seawater does not establish an exact salinity or artificial-seawater composition.

[{"owner_field": "ingredients[0].term", "id": "FOODON:03315426", "asserted_label": "Yeast extract", "canonical_label": "yeast extract", "matches": false}, {"owner_field": "ingredients[1].term", "id": "FOODON:03301056", "asserted_label": "Malt extract", "canonical_label": "malt extract", "matches": false}, {"owner_field": "ingredients[2].term", "id": "CHEBI:17234", "asserted_label": "glucose", "canonical_label": "glucose", "matches": true}, {"owner_field": "ingredients[3].term", "id": "ENVO:00002149", "asserted_label": "Seawater", "canonical_label": "sea water", "matches": false}, {"owner_field": "ingredients[4].term", "id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "matches": true}, {"owner_field": "ingredients[5].term", "id": "CHEBI:2509", "asserted_label": "Agar", "canonical_label": "agar", "matches": false}]

### Linkage denominators

grounding: concern. Targets: CultureMech:007480.

Target primary and secondary linkage are0/2 (0%) of malformed rows, not two valid ingredient identities. The owner has6/6 asserted primary identifiers (100% across ontologies), including3/6 CHEBI identities (50%), and0/6 secondary fields (0%). These linkage percentages are not scientific accuracy scores.

### Undefined marine formulation and optional solid state

scope: supported. Targets: CultureMech:007480.

COMPLEX/UNDEFINED agrees with extracts and seawater. SOLID_AGAR is consistent with the optional agar preparation, but must not erase the explicit if-needed qualifier. No organism-specific growth, temperature, salinity value or stock composition is asserted.

### History and narrow source evidence

provenance: concern. Targets: CultureMech:007480.

Every target/owner/child timestamp parses with a timezone. Source references and owner metadata recover provenance, but these files lack narrow ingredient evidence with exact excerpts; the target reference validator checked zero excerpts. Child links and source content were checked separately above.

## Findings

### f1: Generated recipe is still a concatenated source table

blocker / open / confirmed; issue key: CM007480-malformed-generated-formulation.

The two ingredient rows consist of a whole recipe blob and a blank name with a nonnumeric concentration, rather than the six source components.

### f2: Source-backed owner corrections have not reached the target

major / open / confirmed; issue key: CM007480-stale-ph-source-linkage.

The generated record lacks the owner pH, source term, ingredient identities, source-duplicate relationship, references and subsequent history.

### f3: Unsupported importer preparation survives in the generated record

major / open / confirmed; issue key: CM007480-unsupported-generated-preparation.

The target retains the generic fallback protocol removed from the owner, including an autoclave instruction absent from the sources and misclassified as DISSOLVE.

### f4: Four owner labels differ from canonical ontology labels

minor / open / confirmed; issue key: CM007480-owner-canonical-labels.

The future regeneration owner uses Yeast extract, Malt extract, Seawater and Agar where the inspected canonical labels are yeast extract, malt extract, sea water and agar. IDs and material classes resolve.

### f5: Source provenance lacks narrow claim excerpts

minor / open / confirmed; issue key: CM007480-claim-evidence-gap.

The primary reference and maintained notes identify the source but do not provide exact excerpt support for quantities, optionality and pH.

## Recommended Actions And Acceptance Checks

### a1

Verify the recovered owner formulation, nominal batch-volume basis and agar optionality, then regenerate the merged record. Preserve source and stable identity.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Verify owner label correspondence and reciprocal references, then regenerate and confirm all source-backed corrections survive. Do not invent a medium title.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Regenerate from the verified maintained preparation and inspect importer fallback behavior; add protocol claims only with source-specific evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Canonicalize the owner term labels while retaining preferred source names and supported IDs before regeneration. Check the corresponding child/context labels separately.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Attach short exact source excerpts to the narrow claims, preserving literal batch quantities and keeping per-liter interpretation separate from quotation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/245.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_245.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/245.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/245.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch008/071/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/071/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/245.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/245.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/NBRC_245.yaml:1:id: CultureMech:007480<br>./data/merge_yaml/merged/245.yaml:1:id: CultureMech:007480<br> |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {} |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=244; Medium No.244; blank Medium title; Composition; pH; Comment | supports | Complete official medium244 table inspected: yeast extract4g, malt extract10g, glucose4g, seawater750mL, distilled water250mL, optional agar20g and pH7.6. The medium-title and Comment fields are blank. No measured final-volume statement or sterilization protocol is supplied. |
| legacy | http://www.nbrc.nite.go.jp/NBRC2/NBRCMediumDetailServlet?NO=244; Legacy redirect and complete medium detail | supports | The import-history legacy servlet resolves to the same current medium244 page and composition. The local filename245 does not establish a provider accession245. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1466; meta; components[0].items; comments | supports | Complete structured provider record inspected: accession NBRC_M244, same six ingredients and quantities, pH7.6 and unnamed title. This supports source-duplicate context for the maintained child. |
| togo-page | https://togomedium.org/medium/M1466; Canonical page HTTP200 application shell | context_only | Canonical reference URL returned an application shell; recipe content was obtained from the separately inspected public API. The shell alone is not formulation evidence. |
| owner-foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426; Exact owner identifier, canonical label, definition and obsolete status | supports | FOODON:03315426 resolves to yeast extract. The material identity is supported; asserted owner label is Yeast extract. |
| owner-foodon03301056 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03301056; Exact owner identifier, canonical label, definition and obsolete status | supports | FOODON:03301056 resolves to malt extract. The material identity is supported; asserted owner label is Malt extract. |
| owner-chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact owner identifier, canonical label, definition and obsolete status | supports | CHEBI:17234 resolves to glucose. The material identity is supported; asserted owner label is glucose. |
| owner-envo00002149 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_00002149; Exact owner identifier, canonical label, definition and obsolete status | supports | ENVO:00002149 resolves to sea water. The material identity is supported; asserted owner label is Seawater. |
| owner-chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact owner identifier, canonical label, definition and obsolete status | supports | CHEBI:15377 resolves to water. The material identity is supported; asserted owner label is water. |
| owner-chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact owner identifier, canonical label, definition and obsolete status | supports | CHEBI:2509 resolves to agar. The material identity is supported; asserted owner label is Agar. |
| child | data/normalized_yaml/bacterial/togo_medium_m1466.yaml; Entire maintained child; reciprocal source-duplicate fields; all ingredient rows and history | supports | Full child read as owner context, not a second reviewed target. Its ID/path/name and parent ID/path agree with the owner, and its source accession is NBRC244. The six numeric rows agree, with agar retained as optional. |
| child-id | repository checkout; Exact top-level child ID lookup | supports | ./data/merge_yaml/merged/togo_medium_m1466.yaml:1:id: CultureMech:008008<br>./data/normalized_yaml/bacterial/togo_medium_m1466.yaml:1:id: CultureMech:008008<br> |
| context | Complete target, owner, child and captured ontology terms; All six recovered quantities, reciprocal link, canonical labels and every history timestamp | supports | {"owner_child_quantity_signature": [["Yeast extract", "4", "G_PER_L"], ["Malt extract", "10", "G_PER_L"], ["Glucose", "4", "G_PER_L"], ["Seawater", "750", "ML_PER_L"], ["Distilled water", "250", "ML_PER_L"], ["Agar (if needed)", "20", "G_PER_L"]], "owner_labels": [{"owner_field": "ingredients[0].term", "id": "FOODON:03315426", "asserted_label": "Yeast extract", "canonical_label": "yeast extract", "matches": false}, {"owner_field": "ingredients[1].term", "id": "FOODON:03301056", "asserted_label": "Malt extract", "canonical_label": "malt extract", "matches": false}, {"owner_field": "ingredients[2].term", "id": "CHEBI:17234", "asserted_label": "glucose", "canonical_label": "glucose", "matches": true}, {"owner_field": "ingredients[3].term", "id": "ENVO:00002149", "asserted_label": "Seawater", "canonical_label": "sea water", "matches": false}, {"owner_field": "ingredients[4].term", "id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "matches": true}, {"owner_field": "ingredients[5].term", "id": "CHEBI:2509", "asserted_label": "Agar", "canonical_label": "agar", "matches": false}], "reciprocal_reference_verified": true, "timezone_bearing_history_counts": [6, 9, 7]} |
| importer | src/culturemech/import/nbrc_importer.py; _map_preparation_steps | supports | The current importer synthesizes the same dissolve/conditional-pH/autoclave fallback descriptions when preparation text is absent. The autoclave substring misses autoclaving and leaves DISSOLVE. Code inspection supports a current failure mode, not a reconstruction of historical execution. |
| repair | scripts/repair_nbrc_244_score15.py; Entire script; parent/child guards, fixed source, ingredients, grounding table and reciprocal references | supports | The inspected repair script distinguishes parent CultureMech007480 from child008008, pins the NBRC244 source and writes reciprocal SOURCE_DUPLICATE references. Its explicit material-label table also retains noncanonical FOODON/ENVO capitalization/spacing. Read only; not executed. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The maintained child was inspected only to resolve the asserted source-duplicate context, not counted as a second reviewed target. Historical scraper execution and measured final volume were not reconstructed; TOGO canonical HTML alone was an application shell, with recipe content verified through its public API.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T072000Z-culturemech-007480-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 245 (CultureMech:007480)'
started_at: '2026-10-21T07:17:45Z'
finished_at: '2026-10-21T07:20:00Z'
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
summary: The generated local record245 identifies NBRC244 but contains two malformed
  ingredient rows. The maintained owner has recovered the source formulation, pH and
  a reciprocal TOGO source-duplicate link and removed unsupported preparation defaults.
  These corrections have not reached the generated record, and several owner ontology
  labels need canonicalization.
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
  - path: data/merge_yaml/merged/245.yaml
    sha256: fc06b462495de029acbd423629f90e63778508e3758d02eac29e79bb3333dc3c
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_245.yaml
    sha256: 5621c55df32a098a312aa1fbf79f2d09a950b80278dbb3ca26bd40de5fefb53e
    role: context
  - path: data/normalized_yaml/bacterial/togo_medium_m1466.yaml
    sha256: 9062433baed8c0d72db8a6c905179750b875dc8a99fe9cd565dd8afc5d1959dd
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
  - path: scripts/repair_nbrc_244_score15.py
    sha256: 71336734bad3bfedebf995d395a2ea103891f691565bb41cd6c8461827104ac3
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
  selection: Task review 71; batch 008 item 1 of 10, selected in Python lexicographic
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
  - CultureMech:007480
targets:
- target_id: CultureMech:007480
  path: data/merge_yaml/merged/245.yaml
  label: '245'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_245.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/245.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007480
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/245.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch008/071/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/071/strict.tsv"
  target_ids:
  - CultureMech:007480
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/245.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007480
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/245.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007480
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
  - CultureMech:007480
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/245.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T07:19:57Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_245.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T07:19:57Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/245.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:18:05.863855Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/245.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch008/071/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T07:18:11.942383Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/071/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/245.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:18:18.921875Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/245.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:18:22.987153Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T07:19:57Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/NBRC_245.yaml:1:id: CultureMech:007480

    ./data/merge_yaml/merged/245.yaml:1:id: CultureMech:007480

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T07:19:57Z'
  support: supports
  summary: '{}'
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=244
  locator: Medium No.244; blank Medium title; Composition; pH; Comment
  accessed_at: '2026-10-21T07:15:15.047368Z'
  support: supports
  summary: 'Complete official medium244 table inspected: yeast extract4g, malt extract10g,
    glucose4g, seawater750mL, distilled water250mL, optional agar20g and pH7.6. The
    medium-title and Comment fields are blank. No measured final-volume statement
    or sterilization protocol is supplied.'
  quote: Agar (if needed) 20 g
  snapshot_sha256: 4a76a8ca869ac4ddbfc5778ff16ec5318f4929605d2c76aa878a12a12d6d85e2
- evidence_id: legacy
  kind: primary_source
  reference: http://www.nbrc.nite.go.jp/NBRC2/NBRCMediumDetailServlet?NO=244
  locator: Legacy redirect and complete medium detail
  accessed_at: '2026-10-21T07:15:12.396883Z'
  support: supports
  summary: The import-history legacy servlet resolves to the same current medium244
    page and composition. The local filename245 does not establish a provider accession245.
  snapshot_sha256: 4a76a8ca869ac4ddbfc5778ff16ec5318f4929605d2c76aa878a12a12d6d85e2
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1466
  locator: meta; components[0].items; comments
  accessed_at: '2026-10-21T07:15:13.437436Z'
  support: supports
  summary: 'Complete structured provider record inspected: accession NBRC_M244, same
    six ingredients and quantities, pH7.6 and unnamed title. This supports source-duplicate
    context for the maintained child.'
  snapshot_sha256: 5ca53bbfdf7509ac9f332a409d7486b42302ac72ba11e65941db3a277f9fb4b3
- evidence_id: togo-page
  kind: database
  reference: https://togomedium.org/medium/M1466
  locator: Canonical page HTTP200 application shell
  accessed_at: '2026-10-21T07:15:13.148687Z'
  support: context_only
  summary: Canonical reference URL returned an application shell; recipe content was
    obtained from the separately inspected public API. The shell alone is not formulation
    evidence.
  snapshot_sha256: 78669d85db93e40276577aaf5073aa0bc2420fe5b7be6212de5619e445da93aa
- evidence_id: owner-foodon03315426
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426
  locator: Exact owner identifier, canonical label, definition and obsolete status
  accessed_at: '2026-10-21T07:15:14.683592Z'
  support: supports
  summary: FOODON:03315426 resolves to yeast extract. The material identity is supported;
    asserted owner label is Yeast extract.
  snapshot_sha256: cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44
- evidence_id: owner-foodon03301056
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03301056
  locator: Exact owner identifier, canonical label, definition and obsolete status
  accessed_at: '2026-10-21T07:15:14.356800Z'
  support: supports
  summary: FOODON:03301056 resolves to malt extract. The material identity is supported;
    asserted owner label is Malt extract.
  snapshot_sha256: e2b38be76bc2c1ae54dfa8591ea52da8ab44a9e59a1fc7d4d9e1a16338fc8fd8
- evidence_id: owner-chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact owner identifier, canonical label, definition and obsolete status
  accessed_at: '2026-10-21T07:15:14.054540Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose. The material identity is supported; asserted
    owner label is glucose.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: owner-envo00002149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_00002149
  locator: Exact owner identifier, canonical label, definition and obsolete status
  accessed_at: '2026-10-21T07:15:14.257665Z'
  support: supports
  summary: ENVO:00002149 resolves to sea water. The material identity is supported;
    asserted owner label is Seawater.
  snapshot_sha256: 606e3d069458b6f4d637bc9515fdd9947f1a5d2bca36043729825e643d7211d2
- evidence_id: owner-chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact owner identifier, canonical label, definition and obsolete status
  accessed_at: '2026-10-21T07:15:13.683527Z'
  support: supports
  summary: CHEBI:15377 resolves to water. The material identity is supported; asserted
    owner label is water.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: owner-chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact owner identifier, canonical label, definition and obsolete status
  accessed_at: '2026-10-21T07:15:14.241118Z'
  support: supports
  summary: CHEBI:2509 resolves to agar. The material identity is supported; asserted
    owner label is Agar.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: child
  kind: record_content
  reference: data/normalized_yaml/bacterial/togo_medium_m1466.yaml
  locator: Entire maintained child; reciprocal source-duplicate fields; all ingredient
    rows and history
  accessed_at: '2026-10-21T07:19:57Z'
  support: supports
  summary: Full child read as owner context, not a second reviewed target. Its ID/path/name
    and parent ID/path agree with the owner, and its source accession is NBRC244.
    The six numeric rows agree, with agar retained as optional.
- evidence_id: child-id
  kind: record_content
  reference: repository checkout
  locator: Exact top-level child ID lookup
  accessed_at: '2026-10-21T07:19:57Z'
  support: supports
  summary: './data/merge_yaml/merged/togo_medium_m1466.yaml:1:id: CultureMech:008008

    ./data/normalized_yaml/bacterial/togo_medium_m1466.yaml:1:id: CultureMech:008008

    '
  search_scope: Whole isolated checkout with rg --no-ignore --hidden, including ignored
    paths; normalized and generated layers distinguished.
- evidence_id: context
  kind: validation
  reference: Complete target, owner, child and captured ontology terms
  locator: All six recovered quantities, reciprocal link, canonical labels and every
    history timestamp
  accessed_at: '2026-10-21T07:19:57Z'
  support: supports
  summary: '{"owner_child_quantity_signature": [["Yeast extract", "4", "G_PER_L"],
    ["Malt extract", "10", "G_PER_L"], ["Glucose", "4", "G_PER_L"], ["Seawater", "750",
    "ML_PER_L"], ["Distilled water", "250", "ML_PER_L"], ["Agar (if needed)", "20",
    "G_PER_L"]], "owner_labels": [{"owner_field": "ingredients[0].term", "id": "FOODON:03315426",
    "asserted_label": "Yeast extract", "canonical_label": "yeast extract", "matches":
    false}, {"owner_field": "ingredients[1].term", "id": "FOODON:03301056", "asserted_label":
    "Malt extract", "canonical_label": "malt extract", "matches": false}, {"owner_field":
    "ingredients[2].term", "id": "CHEBI:17234", "asserted_label": "glucose", "canonical_label":
    "glucose", "matches": true}, {"owner_field": "ingredients[3].term", "id": "ENVO:00002149",
    "asserted_label": "Seawater", "canonical_label": "sea water", "matches": false},
    {"owner_field": "ingredients[4].term", "id": "CHEBI:15377", "asserted_label":
    "water", "canonical_label": "water", "matches": true}, {"owner_field": "ingredients[5].term",
    "id": "CHEBI:2509", "asserted_label": "Agar", "canonical_label": "agar", "matches":
    false}], "reciprocal_reference_verified": true, "timezone_bearing_history_counts":
    [6, 9, 7]}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/nbrc_importer.py
  locator: _map_preparation_steps
  accessed_at: '2026-10-21T07:19:57Z'
  support: supports
  summary: The current importer synthesizes the same dissolve/conditional-pH/autoclave
    fallback descriptions when preparation text is absent. The autoclave substring
    misses autoclaving and leaves DISSOLVE. Code inspection supports a current failure
    mode, not a reconstruction of historical execution.
- evidence_id: repair
  kind: record_content
  reference: scripts/repair_nbrc_244_score15.py
  locator: Entire script; parent/child guards, fixed source, ingredients, grounding
    table and reciprocal references
  accessed_at: '2026-10-21T07:19:57Z'
  support: supports
  summary: The inspected repair script distinguishes parent CultureMech007480 from
    child008008, pins the NBRC244 source and writes reciprocal SOURCE_DUPLICATE references.
    Its explicit material-label table also retains noncanonical FOODON/ENVO capitalization/spacing.
    Read only; not executed.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007480
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
  - CultureMech:007480
  evidence_ids:
  - record
  - mim
  details: 2 direct ingredient instances; CHEBI-primary instance linkage 0/2 (0.00%),
    verified secondary coverage 0/2 (0.00%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Exact NBRC244 record and source-duplicate context
  outcome: supported
  summary: The local numeric record245 is resolved by stable ID, merge owner and explicit
    NBRC244 history. The primary page has no official title, so none is invented.
    The maintained reciprocal TOGO M1466 link resolves and shares the actual source
    formulation; it is not a reason to merge distinct source records solely by a fingerprint.
  target_ids:
  - CultureMech:007480
  evidence_ids:
  - record
  - owner-0
  - id-search
  - nbrc
  - legacy
  - togo
  - child
  - child-id
  - repair
- assessment_id: formulation
  area: quantity
  topic: Both malformed target rows and six recovered owner quantities
  outcome: concern
  summary: 'correct: the target combines the full source table and pH into one ingredient
    name with VARIABLE quantity, plus a blank ingredient with textual concentration.
    The owner and child recover all six source numerals and volume units. Source seawater750mL
    plus water250mL describes a nominal one-liter liquid-input batch; it does not
    independently measure final volume after solutes. Preserve that basis and optional
    agar when verifying per-liter representations.'
  target_ids:
  - CultureMech:007480
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - child
  - context
  details: '[["Yeast extract", "4", "G_PER_L"], ["Malt extract", "10", "G_PER_L"],
    ["Glucose", "4", "G_PER_L"], ["Seawater", "750", "ML_PER_L"], ["Distilled water",
    "250", "ML_PER_L"], ["Agar (if needed)", "20", "G_PER_L"]]'
- assessment_id: freshness
  area: completeness
  topic: pH, source term, mappings and reciprocal link
  outcome: concern
  summary: The owner retains pH7.6, source identity, ingredient mappings, references
    and later reciprocal-link history missing from the generated target. The owner
    also removes the unsupported generic preparation list that remains in the target.
  target_ids:
  - CultureMech:007480
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - child
  - context
- assessment_id: preparation
  area: evidence
  topic: Source scope and generated fallback protocol
  outcome: concern
  summary: 'unsupported: neither inspected source supplies an autoclave protocol.
    The target fallback also says dissolve in distilled water, omitting the seawater
    context, and labels autoclaving DISSOLVE. Owner empty preparation is not proof
    that no preparation is possible; it avoids asserting these unsupported defaults.
    Source pH7.6 remains supported.'
  target_ids:
  - CultureMech:007480
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - importer
- assessment_id: owner-grounding
  area: grounding
  topic: Owner identity support versus canonical labels
  outcome: concern
  summary: 'All six owner IDs resolve to the supplied general material classes: three
    CHEBI IDs, two FOODON extract terms and the ENVO sea-water term. Four labels differ
    from canonical labels (yeast extract, malt extract, sea water, agar). These are
    bounded label discrepancies, not wrong chemical identities. Seawater does not
    establish an exact salinity or artificial-seawater composition.'
  target_ids:
  - CultureMech:007480
  evidence_ids:
  - owner-0
  - context
  - owner-foodon03315426
  - owner-foodon03301056
  - owner-chebi17234
  - owner-envo00002149
  - owner-chebi15377
  - owner-chebi2509
  details: '[{"owner_field": "ingredients[0].term", "id": "FOODON:03315426", "asserted_label":
    "Yeast extract", "canonical_label": "yeast extract", "matches": false}, {"owner_field":
    "ingredients[1].term", "id": "FOODON:03301056", "asserted_label": "Malt extract",
    "canonical_label": "malt extract", "matches": false}, {"owner_field": "ingredients[2].term",
    "id": "CHEBI:17234", "asserted_label": "glucose", "canonical_label": "glucose",
    "matches": true}, {"owner_field": "ingredients[3].term", "id": "ENVO:00002149",
    "asserted_label": "Seawater", "canonical_label": "sea water", "matches": false},
    {"owner_field": "ingredients[4].term", "id": "CHEBI:15377", "asserted_label":
    "water", "canonical_label": "water", "matches": true}, {"owner_field": "ingredients[5].term",
    "id": "CHEBI:2509", "asserted_label": "Agar", "canonical_label": "agar", "matches":
    false}]'
- assessment_id: mapping-scope
  area: grounding
  topic: Linkage denominators
  outcome: concern
  summary: Target primary and secondary linkage are0/2 (0%) of malformed rows, not
    two valid ingredient identities. The owner has6/6 asserted primary identifiers
    (100% across ontologies), including3/6 CHEBI identities (50%), and0/6 secondary
    fields (0%). These linkage percentages are not scientific accuracy scores.
  target_ids:
  - CultureMech:007480
  evidence_ids:
  - record
  - owner-0
  - mim
  - context
- assessment_id: classification
  area: scope
  topic: Undefined marine formulation and optional solid state
  outcome: supported
  summary: COMPLEX/UNDEFINED agrees with extracts and seawater. SOLID_AGAR is consistent
    with the optional agar preparation, but must not erase the explicit if-needed
    qualifier. No organism-specific growth, temperature, salinity value or stock composition
    is asserted.
  target_ids:
  - CultureMech:007480
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - child
- assessment_id: audit
  area: provenance
  topic: History and narrow source evidence
  outcome: concern
  summary: Every target/owner/child timestamp parses with a timezone. Source references
    and owner metadata recover provenance, but these files lack narrow ingredient
    evidence with exact excerpts; the target reference validator checked zero excerpts.
    Child links and source content were checked separately above.
  target_ids:
  - CultureMech:007480
  evidence_ids:
  - record
  - owner-0
  - child
  - context
  - validate-references
findings:
- finding_id: f1
  issue_key: CM007480-malformed-generated-formulation
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated recipe is still a concatenated source table
  description: The two ingredient rows consist of a whole recipe blob and a blank
    name with a nonnumeric concentration, rather than the six source components.
  target_ids:
  - CultureMech:007480
  field_paths:
  - ingredients[0]
  - ingredients[1]
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_245.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM007480-stale-ph-source-linkage
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source-backed owner corrections have not reached the target
  description: The generated record lacks the owner pH, source term, ingredient identities,
    source-duplicate relationship, references and subsequent history.
  target_ids:
  - CultureMech:007480
  field_paths:
  - ph_value
  - media_term
  - ingredients[*].term
  - variant_children
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - child
  - context
  - repair
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_245.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM007480-unsupported-generated-preparation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Unsupported importer preparation survives in the generated record
  description: The target retains the generic fallback protocol removed from the owner,
    including an autoclave instruction absent from the sources and misclassified as
    DISSOLVE.
  target_ids:
  - CultureMech:007480
  field_paths:
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - importer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_245.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: CM007480-owner-canonical-labels
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Four owner labels differ from canonical ontology labels
  description: The future regeneration owner uses Yeast extract, Malt extract, Seawater
    and Agar where the inspected canonical labels are yeast extract, malt extract,
    sea water and agar. IDs and material classes resolve.
  target_ids:
  - CultureMech:007480
  field_paths:
  - data/normalized_yaml/bacterial/NBRC_245.yaml:ingredients[0].term.label
  - data/normalized_yaml/bacterial/NBRC_245.yaml:ingredients[1].term.label
  - data/normalized_yaml/bacterial/NBRC_245.yaml:ingredients[3].term.label
  - data/normalized_yaml/bacterial/NBRC_245.yaml:ingredients[5].term.label
  evidence_ids:
  - owner-0
  - context
  - owner-foodon03315426
  - owner-foodon03301056
  - owner-envo00002149
  - owner-chebi2509
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_245.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f5
  issue_key: CM007480-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source provenance lacks narrow claim excerpts
  description: The primary reference and maintained notes identify the source but
    do not provide exact excerpt support for quantities, optionality and pH.
  target_ids:
  - CultureMech:007480
  field_paths:
  - references
  - ingredients[*].evidence
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_245.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Verify the recovered owner formulation, nominal batch-volume basis
    and agar optionality, then regenerate the merged record. Preserve source and stable
    identity.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007480
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_245.yaml
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
  description: Verify owner label correspondence and reciprocal references, then regenerate
    and confirm all source-backed corrections survive. Do not invent a medium title.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007480
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_245.yaml
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
  description: Regenerate from the verified maintained preparation and inspect importer
    fallback behavior; add protocol claims only with source-specific evidence.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007480
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_245.yaml
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
  description: Canonicalize the owner term labels while retaining preferred source
    names and supported IDs before regeneration. Check the corresponding child/context
    labels separately.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007480
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_245.yaml
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
- action_id: a5
  description: Attach short exact source excerpts to the narrow claims, preserving
    literal batch quantities and keeping per-liter interpretation separate from quotation.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:007480
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_245.yaml
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
- The maintained child was inspected only to resolve the asserted source-duplicate
  context, not counted as a second reviewed target. Historical scraper execution and
  measured final volume were not reconstructed; TOGO canonical HTML alone was an application
  shell, with recipe content verified through its public API.
tags:
- unreviewed-records
- batch-008
- generated-medium
```
