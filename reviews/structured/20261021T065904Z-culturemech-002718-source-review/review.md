# Source and formulation review: 1_tryptone_agar (CultureMech:002718)

- Review: 20261021T065904Z-culturemech-002718-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T06:56:47Z
- Finished UTC: 2026-10-21T06:59:04Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The two direct mass concentrations and pH agree with JCM359 and MediaDive. The generated record omits maintained supplier, water/batch and source-duplicate context, and lacks the collection-wide sterilization instruction. The asserted KG ingredient-set match cannot be revalidated without its graph snapshot.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 61; batch 007 item 1 of 10, selected in Python lexicographic repository-relative path order from the current uncovered merged corpus. The prior six validated batch lists contain 60 distinct merged target paths. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c has 40 validated baseline bundles covering 2 current merged paths. The union with prior batches covers 62 of 6320 current merged paths before this batch. This target path occurs in neither set. Task ordinals continue the saved-review sequence, not global path ranks after upstream corpus or coverage changes. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002718 | data/merge_yaml/merged/1_tryptone_agar.yaml | generated | 1_tryptone_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002718 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002718 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch007/061/strict.tsv |
| validate-terms | passed | True | CultureMech:002718 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002718 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002718 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Revalidate asserted KG projected ingredient-set match | unavailable | True | CultureMech:002718 | No graph nodes/edges (including compressed candidates) were found by hidden/ignored-inclusive inventory of this isolated checkout; matcher loading raises FileNotFoundError. Accession lookup and local projection were checked, but neither proves the graph match. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002718.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:002718.

1 primary CHEBI identities resolve with matching labels; 1 of 1 current secondary keys have live pinned-index rows. Unresolved keys: [].

2 direct ingredient instances; CHEBI-primary instance linkage 1/2 (50.00%), verified secondary coverage 1/2 (50.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Primary accession and maintained ownership

identity: supported. Targets: CultureMech:002718.

The generated target and normalized owner identify JCM359 via MediaDive J359. TOGO M353 is a verified source duplicate in the maintained layer; the similarly named NBRC record is not assumed equivalent.

### ingredients[0].concentration

quantity: supported. Targets: CultureMech:002718.

verified: the source mass numeral agrees with the primary recipe and the provider explicitly reports the same per-liter value. Preserve the collection water/batch context rather than claiming an independently measured final volume.

### ingredients[1].concentration

quantity: supported. Targets: CultureMech:002718.

verified: the source mass numeral agrees with the primary recipe and the provider explicitly reports the same per-liter value. Preserve the collection water/batch context rather than claiming an independently measured final volume.

### Missing solvent context and owner water representation

quantity: concern. Targets: CultureMech:002718.

add/evidence_only: the primary recipe gives a distilled-water batch amount that the target omits. The owner now includes water, but its ML_PER_L value should not be mistaken for a source-declared measured final volume; retain the literal batch-volume evidence during any authorized correction.

### pH and collection-scoped preparation default

completeness: concern. Targets: CultureMech:002718.

The scalar pH and adjustment step match both primary and provider sources. The live JCM page also states a general sterilization default unless a recipe overrides it; the target and its owner omit that context. The maintained TOGO sibling has captured it with proper collection scope.

### Ingredients and partial graph projection

grounding: supported. Targets: CultureMech:002718.

Agar identity and secondary key resolve; tryptone is an intentionally unresolved mixture, not a pure-molecule mapping gap requiring a guess. Direct target primary and secondary linkage are each 1/2 (50%, a 0–100 instance-linkage metric). The owner has added water and retains two verified CHEBI entries among three ingredients; coverage and graph matches need reevaluation after regeneration.

### Composition, state and applications

scope: supported. Targets: CultureMech:002718.

COMPLEX/UNDEFINED and SOLID_AGAR agree with the recipe ingredients. Generic microbial cultivation adds no strain-level growth assertion. JCM preparation metadata is source scoped; no incubation protocol or additional organism claim is inferred.

### Maintained versus generated representation

completeness: concern. Targets: CultureMech:002718.

Later maintained curation records supplier labels, water, source references and a reciprocal source-duplicate relationship that the generated target lacks. Input hashes and append-only histories identify the exact snapshot; no merge rerun was performed.

### History and narrow support

evidence: concern. Targets: CultureMech:002718.

All inspected history timestamps parse with timezones. The target reference check examined zero excerpts; the owner carries a source URL but lacks narrow ingredient/preparation evidence.

## Findings

### f1: Generated recipe omits maintained source context

major / open / confirmed; issue key: CM002718-stale-supplier-batch-context.

The target lacks the source-disclosed BD-Difco/Bacto qualifiers, solvent batch context and later source-duplicate linkage now present in its normalized owner.

### f2: Collection preparation default is missing

major / open / confirmed; issue key: CM002718-collection-preparation-default.

The live original-collection page states a sterilization default whose scope applies unless otherwise specified. The target and its maintained owner preserve only pH adjustment.

### f3: Source claims lack narrow evidence

minor / open / confirmed; issue key: CM002718-claim-evidence-gap.

Import history and a URL do not provide field-level evidence for amounts, supplied products, batch basis and preparation context.

## Recommended Actions And Acceptance Checks

### a1

Verify remaining owner quantity semantics, then regenerate the derived record from maintained inputs. Retain source product specificity and literal water/batch evidence, and reassess the projected KG link after ingredient changes.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Represent the verified collection-default instruction with its exception and source scope in the owner, then regenerate; do not imply a record-specific experimental determination.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Attach bounded primary/provider evidence to each supported formulation claim and distinguish batch quantities from derived concentration arithmetic.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_tryptone_agar.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/1_tryptone_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_tryptone_agar.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_tryptone_agar.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch007/061/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch007/061/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_tryptone_agar.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_tryptone_agar.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/1_tryptone_agar.yaml:1:id: CultureMech:002718<br>./data/normalized_yaml/bacterial/1_tryptone_agar.yaml:1:id: CultureMech:002718<br> |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:2509 resolves to agar and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| owner-water | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact owner/variant water identifier, label and obsolete flag | supports | The maintained water identifier resolves with the canonical water label; identity does not validate its batch/final-volume denominator. |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=359; GRMD359 recipe table and page default | supports | Complete primary recipe and collection default inspected: two named product amounts, distilled-water batch volume, pH adjustment and collection-scoped preparation default. |
| api | https://mediadive.dsmz.de/rest/medium/J359; data.medium; data.solutions[0] | supports | Source accession, both solute g_l values, product attributes, water volume and pH statement agree with the primary recipe. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M353; meta; components[0]; comments | supports | Source identity and all three rows inspected solely to verify the maintained source-duplicate link. |
| kg-accession | https://mediadive.dsmz.de/rest/medium/12; data.medium; data.solutions[0] | supports | Asserted medium12 accession resolves to Soil Extract Medium. Its name/formulation differs, but the local field means projected ontology ingredient-set equality, not full recipe identity. |
| context | Exact target and owner, reciprocal variant link, KG matcher and isolated-checkout inventory; Pure ingredient extraction; FileNotFoundError on graph loading; ignored-inclusive inventory; timestamp parsing | context_only | {"checked_at": "2026-10-21T06:57:22.192409+00:00", "projection": {"data/merge_yaml/merged/1_tryptone_agar.yaml": ["CHEBI:2509"], "data/normalized_yaml/bacterial/1_tryptone_agar.yaml": ["CHEBI:15377", "CHEBI:2509"]}, "graph_check": {"status": "unavailable", "error": "KG-Microbe mediadive data not found at /private/tmp/culturemech-record-review-20261019-batch-007/data/transformed/mediadive. Expected edges.tsv and nodes.tsv. Please ensure kg-microbe repository is cloned and data is transformed."}, "inventory_command": ["rg", "--files", "--no-ignore", "--hidden", "."], "inventory_count": 64836, "inventory_sha256": "6c1dacb627a1cf31d00456c34010afbf3ef4b95b955faf382ae042a2ec087f5b", "graph_candidates": [], "inventory_scope": "Entire isolated batch007 checkout, hidden and ignored files included; not a whole-machine absence claim.", "variant_reference": {"child": "data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml", "id": "CultureMech:009733", "reciprocal": true, "source_scope": "TOGO M353 and JCM359 accession; not a new equivalence inferred from names"}, "history": [{"path": "data/merge_yaml/merged/1_tryptone_agar.yaml", "timezone_bearing_history_count": 6}, {"path": "data/normalized_yaml/bacterial/1_tryptone_agar.yaml", "timezone_bearing_history_count": 7}, {"path": "data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml", "timezone_bearing_history_count": 7}]} |
| kg-semantics | src/culturemech/match/kg_media_matcher.py; extract_recipe_ingredients, find_matches, find_exact_match; schema kg_microbe_match | context_only | The matcher compares projected CHEBI/FOODON sets and ignores concentrations and unmapped tryptone. Target projection is agar only; the maintained owner also includes water. The graph files needed to test the stored association are unavailable in the isolated checkout. |
| variant | data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml; Entire maintained variant; reciprocal parent_media and source references | supports | Reciprocal IDs and paths resolve. This maintained TOGO import preserves the same collection accession and discloses the supplier, water basis and collection default. It is contextual evidence, not a second target review. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The primary JCM recipe is available. Partial completion is specifically due to the unavailable KG graph, not a primary-source access failure.
- The KG field is not a whole-recipe equivalence assertion. A different provider title does not establish a wrong ingredient-set match, and no replacement link is guessed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T065904Z-culturemech-002718-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_tryptone_agar (CultureMech:002718)'
started_at: '2026-10-21T06:56:47Z'
finished_at: '2026-10-21T06:59:04Z'
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
scientific_review: true
summary: The two direct mass concentrations and pH agree with JCM359 and MediaDive.
  The generated record omits maintained supplier, water/batch and source-duplicate
  context, and lacks the collection-wide sterilization instruction. The asserted KG
  ingredient-set match cannot be revalidated without its graph snapshot.
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
  - path: .claude/skills/match-kg-microbe/SKILL.md
    sha256: add85aafc1e18164de2a9717cc9d63e5e20f34a1d597568a0c6d8b039c574a99
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
  - path: data/merge_yaml/merged/1_tryptone_agar.yaml
    sha256: 6c03260d5262a1057751229a66b928d75b9da0871a6207bed9778ae4328efea4
    role: target
  - path: data/normalized_yaml/bacterial/1_tryptone_agar.yaml
    sha256: 8154c5ad1e1d8e2a57c1290de8ea388a035d7c13b0683b3e4f45557010eafa96
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml
    sha256: 60aabf4b95bba1107fd3f5ce00195b8b0dc413cfbaabe1dda1c9cc0bad8ddcd8
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
  - path: scripts/enrich_with_kg_microbe_matches.py
    sha256: 61351f99ef2cb0cef03e74ad92d21dcf3b38df77a06602bdac814974e7728eeb
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
  - path: src/culturemech/match/kg_media_matcher.py
    sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
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
  selection: Task review 61; batch 007 item 1 of 10, selected in Python lexicographic
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
  - CultureMech:002718
targets:
- target_id: CultureMech:002718
  path: data/merge_yaml/merged/1_tryptone_agar.yaml
  label: 1_tryptone_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_tryptone_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_tryptone_agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002718
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_tryptone_agar.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch007/061/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch007/061/strict.tsv"
  target_ids:
  - CultureMech:002718
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_tryptone_agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002718
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_tryptone_agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002718
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
  - CultureMech:002718
- check_id: kg-graph
  name: Revalidate asserted KG projected ingredient-set match
  required: true
  status: unavailable
  summary: No graph nodes/edges (including compressed candidates) were found by hidden/ignored-inclusive
    inventory of this isolated checkout; matcher loading raises FileNotFoundError.
    Accession lookup and local projection were checked, but neither proves the graph
    match.
  target_ids:
  - CultureMech:002718
  evidence_ids:
  - context
  - kg-semantics
  - kg-accession
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_tryptone_agar.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T06:59:02Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_tryptone_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T06:59:02Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_tryptone_agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:57:25.586106Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_tryptone_agar.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch007/061/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T06:57:28.949232Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch007/061/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_tryptone_agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:57:32.594514Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_tryptone_agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:57:34.963184Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T06:59:02Z'
  support: supports
  summary: './data/merge_yaml/merged/1_tryptone_agar.yaml:1:id: CultureMech:002718

    ./data/normalized_yaml/bacterial/1_tryptone_agar.yaml:1:id: CultureMech:002718

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:07:41.448510Z'
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
  accessed_at: '2026-10-21T06:59:02Z'
  support: supports
  summary: '{"CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: owner-water
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact owner/variant water identifier, label and obsolete flag
  accessed_at: '2026-10-20T04:00:00.223561Z'
  support: supports
  summary: The maintained water identifier resolves with the canonical water label;
    identity does not validate its batch/final-volume denominator.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=359
  locator: GRMD359 recipe table and page default
  accessed_at: '2026-10-21T06:55:22.658404Z'
  support: supports
  summary: 'Complete primary recipe and collection default inspected: two named product
    amounts, distilled-water batch volume, pH adjustment and collection-scoped preparation
    default.'
  quote: Tryptone (BD-Difco) 10.0 g Bacto agar (BD-Difco) 15.0 g Distilled water 1.0
    L
  snapshot_sha256: 362fd82527ba83f62033b006490d2649a8f1faaf821c4a7cdaa35bbc2556a18f
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J359
  locator: data.medium; data.solutions[0]
  accessed_at: '2026-10-21T06:55:22.017539Z'
  support: supports
  summary: Source accession, both solute g_l values, product attributes, water volume
    and pH statement agree with the primary recipe.
  snapshot_sha256: d7f656d2212421f891224e8f26f7e7fa8ecc45365f0ec8b5d4a04f88450a3a7a
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M353
  locator: meta; components[0]; comments
  accessed_at: '2026-10-21T06:55:22.017802Z'
  support: supports
  summary: Source identity and all three rows inspected solely to verify the maintained
    source-duplicate link.
  snapshot_sha256: 3402b01ce7d43932f86d1064af40142a8eab74d6daf04202b9ea6b4c470ba495
- evidence_id: kg-accession
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/12
  locator: data.medium; data.solutions[0]
  accessed_at: '2026-10-21T06:55:22.017167Z'
  support: supports
  summary: Asserted medium12 accession resolves to Soil Extract Medium. Its name/formulation
    differs, but the local field means projected ontology ingredient-set equality,
    not full recipe identity.
  snapshot_sha256: aae1357e31d914ca483bea213eafb7d4a462aa252fc9008b483e42791202bd8b
- evidence_id: context
  kind: validation
  reference: Exact target and owner, reciprocal variant link, KG matcher and isolated-checkout
    inventory
  locator: Pure ingredient extraction; FileNotFoundError on graph loading; ignored-inclusive
    inventory; timestamp parsing
  accessed_at: '2026-10-21T06:57:22.192409Z'
  support: context_only
  summary: '{"checked_at": "2026-10-21T06:57:22.192409+00:00", "projection": {"data/merge_yaml/merged/1_tryptone_agar.yaml":
    ["CHEBI:2509"], "data/normalized_yaml/bacterial/1_tryptone_agar.yaml": ["CHEBI:15377",
    "CHEBI:2509"]}, "graph_check": {"status": "unavailable", "error": "KG-Microbe
    mediadive data not found at /private/tmp/culturemech-record-review-20261019-batch-007/data/transformed/mediadive.
    Expected edges.tsv and nodes.tsv. Please ensure kg-microbe repository is cloned
    and data is transformed."}, "inventory_command": ["rg", "--files", "--no-ignore",
    "--hidden", "."], "inventory_count": 64836, "inventory_sha256": "6c1dacb627a1cf31d00456c34010afbf3ef4b95b955faf382ae042a2ec087f5b",
    "graph_candidates": [], "inventory_scope": "Entire isolated batch007 checkout,
    hidden and ignored files included; not a whole-machine absence claim.", "variant_reference":
    {"child": "data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml", "id":
    "CultureMech:009733", "reciprocal": true, "source_scope": "TOGO M353 and JCM359
    accession; not a new equivalence inferred from names"}, "history": [{"path": "data/merge_yaml/merged/1_tryptone_agar.yaml",
    "timezone_bearing_history_count": 6}, {"path": "data/normalized_yaml/bacterial/1_tryptone_agar.yaml",
    "timezone_bearing_history_count": 7}, {"path": "data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml",
    "timezone_bearing_history_count": 7}]}'
  search_scope: Entire isolated batch007 checkout, hidden and ignored files included;
    not a whole-machine absence claim.
- evidence_id: kg-semantics
  kind: record_content
  reference: src/culturemech/match/kg_media_matcher.py
  locator: extract_recipe_ingredients, find_matches, find_exact_match; schema kg_microbe_match
  accessed_at: '2026-10-21T06:59:02Z'
  support: context_only
  summary: The matcher compares projected CHEBI/FOODON sets and ignores concentrations
    and unmapped tryptone. Target projection is agar only; the maintained owner also
    includes water. The graph files needed to test the stored association are unavailable
    in the isolated checkout.
- evidence_id: variant
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M353_1_Tryptone_Agar.yaml
  locator: Entire maintained variant; reciprocal parent_media and source references
  accessed_at: '2026-10-21T06:59:02Z'
  support: supports
  summary: Reciprocal IDs and paths resolve. This maintained TOGO import preserves
    the same collection accession and discloses the supplier, water basis and collection
    default. It is contextual evidence, not a second target review.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002718
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '1 primary CHEBI identities resolve with matching labels; 1 of 1 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:002718
  evidence_ids:
  - record
  - mim
  - chebi2509
  details: 2 direct ingredient instances; CHEBI-primary instance linkage 1/2 (50.00%),
    verified secondary coverage 1/2 (50.00%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Primary accession and maintained ownership
  outcome: supported
  summary: The generated target and normalized owner identify JCM359 via MediaDive
    J359. TOGO M353 is a verified source duplicate in the maintained layer; the similarly
    named NBRC record is not assumed equivalent.
  target_ids:
  - CultureMech:002718
  evidence_ids:
  - record
  - owner-0
  - id-search
  - jcm
  - api
  - togo
  - variant
- assessment_id: amount-0
  area: quantity
  topic: ingredients[0].concentration
  outcome: supported
  summary: 'verified: the source mass numeral agrees with the primary recipe and the
    provider explicitly reports the same per-liter value. Preserve the collection
    water/batch context rather than claiming an independently measured final volume.'
  target_ids:
  - CultureMech:002718
  evidence_ids:
  - record
  - jcm
  - api
- assessment_id: amount-1
  area: quantity
  topic: ingredients[1].concentration
  outcome: supported
  summary: 'verified: the source mass numeral agrees with the primary recipe and the
    provider explicitly reports the same per-liter value. Preserve the collection
    water/batch context rather than claiming an independently measured final volume.'
  target_ids:
  - CultureMech:002718
  evidence_ids:
  - record
  - jcm
  - api
- assessment_id: batch
  area: quantity
  topic: Missing solvent context and owner water representation
  outcome: concern
  summary: 'add/evidence_only: the primary recipe gives a distilled-water batch amount
    that the target omits. The owner now includes water, but its ML_PER_L value should
    not be mistaken for a source-declared measured final volume; retain the literal
    batch-volume evidence during any authorized correction.'
  target_ids:
  - CultureMech:002718
  evidence_ids:
  - record
  - owner-0
  - jcm
  - api
- assessment_id: preparation
  area: completeness
  topic: pH and collection-scoped preparation default
  outcome: concern
  summary: The scalar pH and adjustment step match both primary and provider sources.
    The live JCM page also states a general sterilization default unless a recipe
    overrides it; the target and its owner omit that context. The maintained TOGO
    sibling has captured it with proper collection scope.
  target_ids:
  - CultureMech:002718
  evidence_ids:
  - record
  - owner-0
  - jcm
  - api
  - variant
- assessment_id: mapping
  area: grounding
  topic: Ingredients and partial graph projection
  outcome: supported
  summary: Agar identity and secondary key resolve; tryptone is an intentionally unresolved
    mixture, not a pure-molecule mapping gap requiring a guess. Direct target primary
    and secondary linkage are each 1/2 (50%, a 0–100 instance-linkage metric). The
    owner has added water and retains two verified CHEBI entries among three ingredients;
    coverage and graph matches need reevaluation after regeneration.
  target_ids:
  - CultureMech:002718
  evidence_ids:
  - record
  - mim
  - chebi2509
  - owner-water
  - jcm
  - context
  - kg-semantics
- assessment_id: class
  area: scope
  topic: Composition, state and applications
  outcome: supported
  summary: COMPLEX/UNDEFINED and SOLID_AGAR agree with the recipe ingredients. Generic
    microbial cultivation adds no strain-level growth assertion. JCM preparation metadata
    is source scoped; no incubation protocol or additional organism claim is inferred.
  target_ids:
  - CultureMech:002718
  evidence_ids:
  - record
  - jcm
  - api
- assessment_id: freshness
  area: completeness
  topic: Maintained versus generated representation
  outcome: concern
  summary: Later maintained curation records supplier labels, water, source references
    and a reciprocal source-duplicate relationship that the generated target lacks.
    Input hashes and append-only histories identify the exact snapshot; no merge rerun
    was performed.
  target_ids:
  - CultureMech:002718
  evidence_ids:
  - record
  - owner-0
  - variant
  - context
- assessment_id: evidence
  area: evidence
  topic: History and narrow support
  outcome: concern
  summary: All inspected history timestamps parse with timezones. The target reference
    check examined zero excerpts; the owner carries a source URL but lacks narrow
    ingredient/preparation evidence.
  target_ids:
  - CultureMech:002718
  evidence_ids:
  - record
  - owner-0
  - context
  - validate-references
findings:
- finding_id: f1
  issue_key: CM002718-stale-supplier-batch-context
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated recipe omits maintained source context
  description: The target lacks the source-disclosed BD-Difco/Bacto qualifiers, solvent
    batch context and later source-duplicate linkage now present in its normalized
    owner.
  target_ids:
  - CultureMech:002718
  field_paths:
  - ingredients
  - references
  - variant_children
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - jcm
  - api
  - variant
  - context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_tryptone_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM002718-collection-preparation-default
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Collection preparation default is missing
  description: The live original-collection page states a sterilization default whose
    scope applies unless otherwise specified. The target and its maintained owner
    preserve only pH adjustment.
  target_ids:
  - CultureMech:002718
  field_paths:
  - preparation_steps
  - sterilization
  evidence_ids:
  - record
  - owner-0
  - jcm
  - variant
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_tryptone_agar.yaml
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
  issue_key: CM002718-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source claims lack narrow evidence
  description: Import history and a URL do not provide field-level evidence for amounts,
    supplied products, batch basis and preparation context.
  target_ids:
  - CultureMech:002718
  field_paths:
  - ingredients[*].evidence
  - evidence
  - references
  evidence_ids:
  - record
  - owner-0
  - jcm
  - api
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_tryptone_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Verify remaining owner quantity semantics, then regenerate the derived
    record from maintained inputs. Retain source product specificity and literal water/batch
    evidence, and reassess the projected KG link after ingredient changes.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002718
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_tryptone_agar.yaml
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
  description: Represent the verified collection-default instruction with its exception
    and source scope in the owner, then regenerate; do not imply a record-specific
    experimental determination.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002718
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_tryptone_agar.yaml
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
  description: Attach bounded primary/provider evidence to each supported formulation
    claim and distinguish batch quantities from derived concentration arithmetic.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002718
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_tryptone_agar.yaml
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
- The primary JCM recipe is available. Partial completion is specifically due to the
  unavailable KG graph, not a primary-source access failure.
- The KG field is not a whole-recipe equivalence assertion. A different provider title
  does not establish a wrong ingredient-set match, and no replacement link is guessed.
tags:
- unreviewed-records
- batch-007
- generated-medium
```
