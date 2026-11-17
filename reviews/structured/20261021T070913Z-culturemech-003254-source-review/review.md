# Source and formulation review: 225m1_medium (CultureMech:003254)

- Review: 20261021T070913Z-culturemech-003254-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T06:57:09Z
- Finished UTC: 2026-10-21T07:09:13Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The JCM905 liquid formulation and all eight solute concentrations are supported, including 300 g/L magnesium chloride hexahydrate. The target and its maintained owner omit source material qualifiers and the collection sterilization instruction, and have no narrow formulation evidence.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 66; batch 007 item 6 of 10, selected in Python lexicographic repository-relative path order from the current uncovered merged corpus. The prior six validated batch lists contain 60 distinct merged target paths. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c has 40 validated baseline bundles covering 2 current merged paths. The union with prior batches covers 62 of 6320 current merged paths before this batch. This target path occurs in neither set. Task ordinals continue the saved-review sequence, not global path ranks after upstream corpus or coverage changes. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003254 | data/merge_yaml/merged/225M1_MEDIUM.yaml | generated | 225m1_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003254 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003254 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch007/066/strict.tsv |
| validate-terms | passed | True | CultureMech:003254 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003254 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003254 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003254.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:003254.

6 primary CHEBI identities resolve with matching labels; 6 of 6 current secondary keys have live pinned-index rows. Unresolved keys: [].

8 direct ingredient instances; CHEBI-primary instance linkage 6/8 (75.00%), verified secondary coverage 6/8 (75.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### JCM905 liquid formulation

identity: supported. Targets: CultureMech:003254.

Stable ID, J905 accession and original name identify the liquid basal formulation. The source explicitly describes agar addition as a solid-medium option; it is correctly conditional in target prose. No stock or organism identifier is asserted.

### All eight direct ingredients and final-volume basis

quantity: supported. Targets: CultureMech:003254.

verified: every solute mass is directly supported for an explicit final 1.0 L. The 300 g/L magnesium chloride hexahydrate value is source-supported, not a magnitude-based error. No stock/density/molar conversion is required.

[{"field_path": "ingredients[0].concentration", "ingredient": "Casamino acids", "source_mass_g": 1, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": "BD-Difco", "target_amount": {"value": "1", "unit": "G_PER_L"}}, {"field_path": "ingredients[1].concentration", "ingredient": "Yeast extract", "source_mass_g": 1, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": "BD-Difco", "target_amount": {"value": "1", "unit": "G_PER_L"}}, {"field_path": "ingredients[2].concentration", "ingredient": "Starch", "source_mass_g": 2, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": "soluble", "target_amount": {"value": "2", "unit": "G_PER_L"}}, {"field_path": "ingredients[3].concentration", "ingredient": "NaCl", "source_mass_g": 20, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": null, "target_amount": {"value": "20", "unit": "G_PER_L"}}, {"field_path": "ingredients[4].concentration", "ingredient": "MgCl2 x 6 H2O", "source_mass_g": 300, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": null, "target_amount": {"value": "300", "unit": "G_PER_L"}}, {"field_path": "ingredients[5].concentration", "ingredient": "CaCl2 x 2 H2O", "source_mass_g": 0.13, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": null, "target_amount": {"value": "0.13", "unit": "G_PER_L"}}, {"field_path": "ingredients[6].concentration", "ingredient": "K2SO4", "source_mass_g": 5, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": null, "target_amount": {"value": "5", "unit": "G_PER_L"}}, {"field_path": "ingredients[7].concentration", "ingredient": "Sodium pyruvate", "source_mass_g": 0.13, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": null, "target_amount": {"value": "0.13", "unit": "G_PER_L"}}]

### Water, KOH and conditional agar in preparation prose

quantity: supported. Targets: CultureMech:003254.

Water makes up the final volume; it is not a measured fixed dose. KOH solution is stated as 25%, but the source does not identify its percentage basis or addition volume; not_quantified for a final KOH concentration. Retain that ambiguity. The 23.0 g/L agar dose is verified only for the optional solid preparation, not a basal liquid ingredient.

### Generic identities versus supplied materials

grounding: concern. Targets: CultureMech:003254.

All six asserted chemical IDs and current secondary links resolve; hydrate formulas agree with the primary source. Generic starch does not preserve the explicit soluble-starch material. Casamino acids and yeast extract also lose their BD-Difco qualifiers, present in both inspected providers. Coverage is 6/8 (75%) for each linkage class, not a correctness score.

### Source instructions and conditions

completeness: concern. Targets: CultureMech:003254.

Final volume, pH and adjustment/agar instructions survive, but the collection default sterilization time and temperature are absent from the entire target and owner. The source provides no incubation condition or strain-specific growth assertion to transfer.

### Composition and physical state

scope: supported. Targets: CultureMech:003254.

COMPLEX/UNDEFINED is supported by the two supplied undefined nutrient mixtures, and LIQUID matches the basal recipe. The bacterial folder is a repository filing choice; no source organism or taxonomic exclusivity is established by this recipe page. No claim of universal or optimized growth is supported.

### History and narrow source evidence

evidence: concern. Targets: CultureMech:003254.

All target and owner history timestamps parse with timezones. Source provenance is recoverable, but narrow ingredient/preparation evidence and bibliographic entries are absent in these full files; the reference validator checked zero excerpts.

## Findings

### f1: Source material qualifiers were dropped

major / open / confirmed; issue key: CM003254-source-material-qualifiers.

The target and owner retain generic starch instead of explicit soluble starch, and omit the supplied BD-Difco qualifiers on casamino acids and yeast extract. A generic ontology match does not preserve supplied material identity.

### f2: JCM sterilization instruction is missing

major / open / confirmed; issue key: CM003254-source-sterilization-missing.

The inspected primary page supplies a default autoclave instruction of 121 degrees C for 15 minutes unless otherwise stated. Neither full recipe carries it; the media-specific preparation paragraph does not override it.

### f3: Recoverable provenance lacks narrow claim evidence

minor / open / confirmed; issue key: CM003254-claim-evidence-gap.

A source link and import history identify the provider, but do not attach the inspected source to individual quantities, supplied forms or preparation claims.

## Recommended Actions And Acceptance Checks

### a1

Restore source material qualifiers in the maintained owner without inventing product identifiers or forcing pure-molecule IDs for mixtures; verify importer attribute handling before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add a source-scoped preparation step with narrow evidence in the owner, preserving order and collection-default scope; then regenerate.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Add verified source metadata and short exact claim-scoped excerpts to the maintained owner; keep curator arithmetic outside quotation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/225M1_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/225m1_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/225M1_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/225M1_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch007/066/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch007/066/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/225M1_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/225M1_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/225M1_MEDIUM.yaml:1:id: CultureMech:003254<br>./data/normalized_yaml/bacterial/225m1_medium.yaml:1:id: CultureMech:003254<br> |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi28017 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:28017 resolves to starch and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32036; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32036 resolves to potassium sulfate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:50144 resolves to sodium pyruvate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86158 resolves to calcium chloride dihydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:28017": [{"label": "Starch", "match_type": "preferred_term", "identifier": "CHEBI:28017", "preferred_term": "Starch", "ontology_id": "CHEBI:28017", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32036": [{"label": "K2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32036", "preferred_term": "K2SO4", "ontology_id": "CHEBI:32036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=905; GRMD905; complete ingredient list; preparation paragraph; collection header | supports | Complete eight-component primary recipe, preparation paragraph and collection default inspected. Source explicitly makes the final volume 1.0 L; pH 6.8 is adjusted with 25% KOH. Agar is conditional on preparation of solid medium. The header supplies autoclaving at 121 degrees C for 15 minutes unless otherwise stated. |
| mediadive | https://mediadive.dsmz.de/rest/medium/J905; data.medium; solutions[0].recipe and steps | supports | J905 resolves to JCM225M1 and the exact primary link. All eight numeric rows, supplier/form attributes and preparation paragraph were inspected. |
| context | Full target, maintained owner and MediaDive source; Eight row comparisons and full history timestamps | supports | {"quantities": [{"field_path": "ingredients[0].concentration", "ingredient": "Casamino acids", "source_mass_g": 1, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": "BD-Difco", "target_amount": {"value": "1", "unit": "G_PER_L"}}, {"field_path": "ingredients[1].concentration", "ingredient": "Yeast extract", "source_mass_g": 1, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": "BD-Difco", "target_amount": {"value": "1", "unit": "G_PER_L"}}, {"field_path": "ingredients[2].concentration", "ingredient": "Starch", "source_mass_g": 2, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": "soluble", "target_amount": {"value": "2", "unit": "G_PER_L"}}, {"field_path": "ingredients[3].concentration", "ingredient": "NaCl", "source_mass_g": 20, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": null, "target_amount": {"value": "20", "unit": "G_PER_L"}}, {"field_path": "ingredients[4].concentration", "ingredient": "MgCl2 x 6 H2O", "source_mass_g": 300, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": null, "target_amount": {"value": "300", "unit": "G_PER_L"}}, {"field_path": "ingredients[5].concentration", "ingredient": "CaCl2 x 2 H2O", "source_mass_g": 0.13, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": null, "target_amount": {"value": "0.13", "unit": "G_PER_L"}}, {"field_path": "ingredients[6].concentration", "ingredient": "K2SO4", "source_mass_g": 5, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": null, "target_amount": {"value": "5", "unit": "G_PER_L"}}, {"field_path": "ingredients[7].concentration", "ingredient": "Sodium pyruvate", "source_mass_g": 0.13, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": null, "target_amount": {"value": "0.13", "unit": "G_PER_L"}}], "timezone_bearing_history_counts": [9, 8], "target_owner_formulation_equal": true} |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Review is confined to the primary collection recipe and its MediaDive representation. No primary research paper or organism-specific growth experiment was assessed; the recipe does not identify a tested strain.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T070913Z-culturemech-003254-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 225m1_medium (CultureMech:003254)'
started_at: '2026-10-21T06:57:09Z'
finished_at: '2026-10-21T07:09:13Z'
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
summary: The JCM905 liquid formulation and all eight solute concentrations are supported,
  including 300 g/L magnesium chloride hexahydrate. The target and its maintained
  owner omit source material qualifiers and the collection sterilization instruction,
  and have no narrow formulation evidence.
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
  - path: data/merge_yaml/merged/225M1_MEDIUM.yaml
    sha256: 082aea3dace122ec50c6e1e31b774d0db9e0f758570424bc915167ff596338c1
    role: target
  - path: data/normalized_yaml/bacterial/225m1_medium.yaml
    sha256: 414221e7fea5349f2abc192971c147e72d83fd3c6e53d356d5eb3407a38ca3ed
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
  selection: Task review 66; batch 007 item 6 of 10, selected in Python lexicographic
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
  - CultureMech:003254
targets:
- target_id: CultureMech:003254
  path: data/merge_yaml/merged/225M1_MEDIUM.yaml
  label: 225m1_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/225m1_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/225M1_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003254
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/225M1_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch007/066/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch007/066/strict.tsv"
  target_ids:
  - CultureMech:003254
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/225M1_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003254
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/225M1_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003254
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
  - CultureMech:003254
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/225M1_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T07:09:11Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/225m1_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T07:09:11Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/225M1_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:58:28.711049Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/225M1_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch007/066/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T06:58:33.693664Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-007/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch007/066/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/225M1_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:58:40.626026Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/225M1_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:58:43.409140Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T07:09:11Z'
  support: supports
  summary: './data/merge_yaml/merged/225M1_MEDIUM.yaml:1:id: CultureMech:003254

    ./data/normalized_yaml/bacterial/225m1_medium.yaml:1:id: CultureMech:003254

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:11:31.325976Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi28017
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T06:57:46.408993Z'
  support: supports
  summary: CHEBI:28017 resolves to starch and is not obsolete. This verifies the asserted
    generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond
    the record is inferred.
  snapshot_sha256: 959b4330165a7ff12d2e464f4a7b44e148376624d04cf7764b6a8671c1c99204
- evidence_id: chebi32036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32036
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T06:57:47.376553Z'
  support: supports
  summary: CHEBI:32036 resolves to potassium sulfate and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 0e2a526c994d512b314d090b5acbd8acbc65a9f998ac0d292d8756f2b97de777
- evidence_id: chebi50144
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T06:57:48.079595Z'
  support: supports
  summary: CHEBI:50144 resolves to sodium pyruvate and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 457ed29adfdea68c420ea0c094d7d75593958fc70f908f6809348e4e12e7e15d
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T06:57:48.767939Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T06:57:48.885937Z'
  support: supports
  summary: CHEBI:86345 resolves to magnesium dichloride hexahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T07:09:11Z'
  support: supports
  summary: '{"CHEBI:28017": [{"label": "Starch", "match_type": "preferred_term", "identifier":
    "CHEBI:28017", "preferred_term": "Starch", "ontology_id": "CHEBI:28017", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345":
    [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier":
    "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32036":
    [{"label": "K2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32036",
    "preferred_term": "K2SO4", "ontology_id": "CHEBI:32036", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type":
    "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate",
    "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=905
  locator: GRMD905; complete ingredient list; preparation paragraph; collection header
  accessed_at: '2026-10-21T06:57:49.372218Z'
  support: supports
  summary: Complete eight-component primary recipe, preparation paragraph and collection
    default inspected. Source explicitly makes the final volume 1.0 L; pH 6.8 is adjusted
    with 25% KOH. Agar is conditional on preparation of solid medium. The header supplies
    autoclaving at 121 degrees C for 15 minutes unless otherwise stated.
  quote: Soluble starch 2.0 g
  snapshot_sha256: b1ce4606c289fc217c49dbd787d456c17efa2c9a23b49092f71d7d819a77ccb3
- evidence_id: mediadive
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J905
  locator: data.medium; solutions[0].recipe and steps
  accessed_at: '2026-10-21T06:57:44.865200Z'
  support: supports
  summary: J905 resolves to JCM225M1 and the exact primary link. All eight numeric
    rows, supplier/form attributes and preparation paragraph were inspected.
  snapshot_sha256: 8cf53461fd0e7e9cad82bd0036ac9a910f031bc6c8f480a48b40d2e61022ad18
- evidence_id: context
  kind: validation
  reference: Full target, maintained owner and MediaDive source
  locator: Eight row comparisons and full history timestamps
  accessed_at: '2026-10-21T07:09:11Z'
  support: supports
  summary: '{"quantities": [{"field_path": "ingredients[0].concentration", "ingredient":
    "Casamino acids", "source_mass_g": 1, "explicit_final_volume_L": 1, "decision":
    "verified", "source_attribute": "BD-Difco", "target_amount": {"value": "1", "unit":
    "G_PER_L"}}, {"field_path": "ingredients[1].concentration", "ingredient": "Yeast
    extract", "source_mass_g": 1, "explicit_final_volume_L": 1, "decision": "verified",
    "source_attribute": "BD-Difco", "target_amount": {"value": "1", "unit": "G_PER_L"}},
    {"field_path": "ingredients[2].concentration", "ingredient": "Starch", "source_mass_g":
    2, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute": "soluble",
    "target_amount": {"value": "2", "unit": "G_PER_L"}}, {"field_path": "ingredients[3].concentration",
    "ingredient": "NaCl", "source_mass_g": 20, "explicit_final_volume_L": 1, "decision":
    "verified", "source_attribute": null, "target_amount": {"value": "20", "unit":
    "G_PER_L"}}, {"field_path": "ingredients[4].concentration", "ingredient": "MgCl2
    x 6 H2O", "source_mass_g": 300, "explicit_final_volume_L": 1, "decision": "verified",
    "source_attribute": null, "target_amount": {"value": "300", "unit": "G_PER_L"}},
    {"field_path": "ingredients[5].concentration", "ingredient": "CaCl2 x 2 H2O",
    "source_mass_g": 0.13, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute":
    null, "target_amount": {"value": "0.13", "unit": "G_PER_L"}}, {"field_path": "ingredients[6].concentration",
    "ingredient": "K2SO4", "source_mass_g": 5, "explicit_final_volume_L": 1, "decision":
    "verified", "source_attribute": null, "target_amount": {"value": "5", "unit":
    "G_PER_L"}}, {"field_path": "ingredients[7].concentration", "ingredient": "Sodium
    pyruvate", "source_mass_g": 0.13, "explicit_final_volume_L": 1, "decision": "verified",
    "source_attribute": null, "target_amount": {"value": "0.13", "unit": "G_PER_L"}}],
    "timezone_bearing_history_counts": [9, 8], "target_owner_formulation_equal": true}'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003254
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '6 primary CHEBI identities resolve with matching labels; 6 of 6 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:003254
  evidence_ids:
  - record
  - mim
  - chebi26710
  - chebi28017
  - chebi32036
  - chebi50144
  - chebi86158
  - chebi86345
  details: 8 direct ingredient instances; CHEBI-primary instance linkage 6/8 (75.00%),
    verified secondary coverage 6/8 (75.00%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: JCM905 liquid formulation
  outcome: supported
  summary: Stable ID, J905 accession and original name identify the liquid basal formulation.
    The source explicitly describes agar addition as a solid-medium option; it is
    correctly conditional in target prose. No stock or organism identifier is asserted.
  target_ids:
  - CultureMech:003254
  evidence_ids:
  - record
  - owner-0
  - id-search
  - jcm
  - mediadive
- assessment_id: amounts
  area: quantity
  topic: All eight direct ingredients and final-volume basis
  outcome: supported
  summary: 'verified: every solute mass is directly supported for an explicit final
    1.0 L. The 300 g/L magnesium chloride hexahydrate value is source-supported, not
    a magnitude-based error. No stock/density/molar conversion is required.'
  target_ids:
  - CultureMech:003254
  evidence_ids:
  - record
  - jcm
  - mediadive
  - context
  details: '[{"field_path": "ingredients[0].concentration", "ingredient": "Casamino
    acids", "source_mass_g": 1, "explicit_final_volume_L": 1, "decision": "verified",
    "source_attribute": "BD-Difco", "target_amount": {"value": "1", "unit": "G_PER_L"}},
    {"field_path": "ingredients[1].concentration", "ingredient": "Yeast extract",
    "source_mass_g": 1, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute":
    "BD-Difco", "target_amount": {"value": "1", "unit": "G_PER_L"}}, {"field_path":
    "ingredients[2].concentration", "ingredient": "Starch", "source_mass_g": 2, "explicit_final_volume_L":
    1, "decision": "verified", "source_attribute": "soluble", "target_amount": {"value":
    "2", "unit": "G_PER_L"}}, {"field_path": "ingredients[3].concentration", "ingredient":
    "NaCl", "source_mass_g": 20, "explicit_final_volume_L": 1, "decision": "verified",
    "source_attribute": null, "target_amount": {"value": "20", "unit": "G_PER_L"}},
    {"field_path": "ingredients[4].concentration", "ingredient": "MgCl2 x 6 H2O",
    "source_mass_g": 300, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute":
    null, "target_amount": {"value": "300", "unit": "G_PER_L"}}, {"field_path": "ingredients[5].concentration",
    "ingredient": "CaCl2 x 2 H2O", "source_mass_g": 0.13, "explicit_final_volume_L":
    1, "decision": "verified", "source_attribute": null, "target_amount": {"value":
    "0.13", "unit": "G_PER_L"}}, {"field_path": "ingredients[6].concentration", "ingredient":
    "K2SO4", "source_mass_g": 5, "explicit_final_volume_L": 1, "decision": "verified",
    "source_attribute": null, "target_amount": {"value": "5", "unit": "G_PER_L"}},
    {"field_path": "ingredients[7].concentration", "ingredient": "Sodium pyruvate",
    "source_mass_g": 0.13, "explicit_final_volume_L": 1, "decision": "verified", "source_attribute":
    null, "target_amount": {"value": "0.13", "unit": "G_PER_L"}}]'
- assessment_id: adjustment
  area: quantity
  topic: Water, KOH and conditional agar in preparation prose
  outcome: supported
  summary: Water makes up the final volume; it is not a measured fixed dose. KOH solution
    is stated as 25%, but the source does not identify its percentage basis or addition
    volume; not_quantified for a final KOH concentration. Retain that ambiguity. The
    23.0 g/L agar dose is verified only for the optional solid preparation, not a
    basal liquid ingredient.
  target_ids:
  - CultureMech:003254
  evidence_ids:
  - record
  - jcm
  - mediadive
- assessment_id: forms
  area: grounding
  topic: Generic identities versus supplied materials
  outcome: concern
  summary: All six asserted chemical IDs and current secondary links resolve; hydrate
    formulas agree with the primary source. Generic starch does not preserve the explicit
    soluble-starch material. Casamino acids and yeast extract also lose their BD-Difco
    qualifiers, present in both inspected providers. Coverage is 6/8 (75%) for each
    linkage class, not a correctness score.
  target_ids:
  - CultureMech:003254
  evidence_ids:
  - record
  - owner-0
  - jcm
  - mediadive
  - mim
  - chebi28017
  - chebi86345
  - chebi86158
- assessment_id: preparation
  area: completeness
  topic: Source instructions and conditions
  outcome: concern
  summary: Final volume, pH and adjustment/agar instructions survive, but the collection
    default sterilization time and temperature are absent from the entire target and
    owner. The source provides no incubation condition or strain-specific growth assertion
    to transfer.
  target_ids:
  - CultureMech:003254
  evidence_ids:
  - record
  - owner-0
  - jcm
  - mediadive
- assessment_id: classification
  area: scope
  topic: Composition and physical state
  outcome: supported
  summary: COMPLEX/UNDEFINED is supported by the two supplied undefined nutrient mixtures,
    and LIQUID matches the basal recipe. The bacterial folder is a repository filing
    choice; no source organism or taxonomic exclusivity is established by this recipe
    page. No claim of universal or optimized growth is supported.
  target_ids:
  - CultureMech:003254
  evidence_ids:
  - record
  - jcm
- assessment_id: audit
  area: evidence
  topic: History and narrow source evidence
  outcome: concern
  summary: All target and owner history timestamps parse with timezones. Source provenance
    is recoverable, but narrow ingredient/preparation evidence and bibliographic entries
    are absent in these full files; the reference validator checked zero excerpts.
  target_ids:
  - CultureMech:003254
  evidence_ids:
  - record
  - owner-0
  - context
  - validate-references
findings:
- finding_id: f1
  issue_key: CM003254-source-material-qualifiers
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Source material qualifiers were dropped
  description: The target and owner retain generic starch instead of explicit soluble
    starch, and omit the supplied BD-Difco qualifiers on casamino acids and yeast
    extract. A generic ontology match does not preserve supplied material identity.
  target_ids:
  - CultureMech:003254
  field_paths:
  - ingredients[0].preferred_term
  - ingredients[1].preferred_term
  - ingredients[2].preferred_term
  evidence_ids:
  - record
  - owner-0
  - jcm
  - mediadive
  - chebi28017
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/225m1_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM003254-source-sterilization-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: JCM sterilization instruction is missing
  description: The inspected primary page supplies a default autoclave instruction
    of 121 degrees C for 15 minutes unless otherwise stated. Neither full recipe carries
    it; the media-specific preparation paragraph does not override it.
  target_ids:
  - CultureMech:003254
  field_paths:
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/225m1_medium.yaml
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
  issue_key: CM003254-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Recoverable provenance lacks narrow claim evidence
  description: A source link and import history identify the provider, but do not
    attach the inspected source to individual quantities, supplied forms or preparation
    claims.
  target_ids:
  - CultureMech:003254
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
    path: data/normalized_yaml/bacterial/225m1_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Restore source material qualifiers in the maintained owner without
    inventing product identifiers or forcing pure-molecule IDs for mixtures; verify
    importer attribute handling before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003254
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/225m1_medium.yaml
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
  description: Add a source-scoped preparation step with narrow evidence in the owner,
    preserving order and collection-default scope; then regenerate.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003254
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/225m1_medium.yaml
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
  description: Add verified source metadata and short exact claim-scoped excerpts
    to the maintained owner; keep curator arithmetic outside quotation.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003254
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/225m1_medium.yaml
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
- Review is confined to the primary collection recipe and its MediaDive representation.
  No primary research paper or organism-specific growth experiment was assessed; the
  recipe does not identify a tested strain.
tags:
- unreviewed-records
- batch-007
- generated-medium
```
