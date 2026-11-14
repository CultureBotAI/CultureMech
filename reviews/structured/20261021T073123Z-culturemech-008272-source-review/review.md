# Source and formulation review: 2_5_nacl_bpg_agar (CultureMech:008272)

- Review: 20261021T073123Z-culturemech-008272-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T07:20:57Z
- Finished UTC: 2026-10-21T07:31:23Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M170 resolves to JCM177 and preserves all seven supported solute amounts and supplied forms. Both local layers misrepresent source water1L as1g/L and omit pH7.2, the pH-adjustment step and the JCM sterilization default. Chemical mappings resolve, including the corrected magnesium sulfate heptahydrate.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 80; batch 008 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding seven task batches contain 70 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 72 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008272 | data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml | generated | 2_5_nacl_bpg_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008272 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008272 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/080/strict.tsv |
| validate-terms | passed | True | CultureMech:008272 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008272 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008272 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008272.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:008272.

6 primary CHEBI identities resolve with matching labels; 5 of 5 current secondary keys have live pinned-index rows. Unresolved keys: [].

8 direct ingredient instances; CHEBI-primary instance linkage 6/8 (75.00%), verified secondary coverage 5/8 (62.50%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### TOGO M170 from JCM177

identity: supported. Targets: CultureMech:008272.

Stable ID, merge owner and exact provider source metadata establish this formulation. The source preserves BD-Difco Bacto peptone and the seven-water magnesium sulfate form. Similar naming to the separate MediaDive import is not the sole identity evidence.

### Every listed amount and unit

quantity: concern. Targets: CultureMech:008272.

correct: water1G_PER_L conflicts with source1L and provider1000mL. The seven solute values agree with explicit provider g_l and source gram amounts. Preserve literal solvent-batch context; neither the water row nor nominal provider volume establishes an independently measured final volume. No density-based water conversion is warranted.

[{"field": "ingredients[0].concentration", "material": "Distilled water", "target": {"value": "1", "unit": "G_PER_L"}, "togo_amount": 1, "togo_unit": "L", "provider_g_l": null, "provider_locator": "$.data.solutions[0].recipe[7]", "decision": "correct solvent-volume unit"}, {"field": "ingredients[1].concentration", "material": "MgSO4\u30fb7H2O", "target": {"value": "2.5", "unit": "G_PER_L"}, "togo_amount": 2.5, "togo_unit": "g", "provider_g_l": 2.5, "provider_locator": "$.data.solutions[0].recipe[5]", "decision": "verified provider concentration"}, {"field": "ingredients[2].concentration", "material": "NaCl", "target": {"value": "25", "unit": "G_PER_L"}, "togo_amount": 25, "togo_unit": "g", "provider_g_l": 25, "provider_locator": "$.data.solutions[0].recipe[4]", "decision": "verified provider concentration"}, {"field": "ingredients[3].concentration", "material": "KCl", "target": {"value": "1", "unit": "G_PER_L"}, "togo_amount": 1, "togo_unit": "g", "provider_g_l": 1, "provider_locator": "$.data.solutions[0].recipe[6]", "decision": "verified provider concentration"}, {"field": "ingredients[4].concentration", "material": "Glucose", "target": {"value": "1", "unit": "G_PER_L"}, "togo_amount": 1, "togo_unit": "g", "provider_g_l": 1, "provider_locator": "$.data.solutions[0].recipe[2]", "decision": "verified provider concentration"}, {"field": "ingredients[5].concentration", "material": "Agar", "target": {"value": "15", "unit": "G_PER_L"}, "togo_amount": 15, "togo_unit": "g", "provider_g_l": 15, "provider_locator": "$.data.solutions[0].recipe[3]", "decision": "verified provider concentration"}, {"field": "ingredients[6].concentration", "material": "Bacto peptone (BD-Difco)", "target": {"value": "5", "unit": "G_PER_L"}, "togo_amount": 5, "togo_unit": "g", "provider_g_l": 5, "provider_locator": "$.data.solutions[0].recipe[0]", "decision": "verified provider concentration"}, {"field": "ingredients[7].concentration", "material": "Fish meat extract", "target": {"value": "5", "unit": "G_PER_L"}, "togo_amount": 5, "togo_unit": "g", "provider_g_l": 5, "provider_locator": "$.data.solutions[0].recipe[1]", "decision": "verified provider concentration"}]

### Supplied forms and linkage

grounding: supported. Targets: CultureMech:008272.

All six primary CHEBI IDs/labels match captured ontology terms, including CHEBI31795 for MgSO4·7H2O; the historical generic ID is no longer asserted. Five secondary keys have current pinned preferred-term rows. Primary linkage6/8(75%) and secondary5/8(62.5%) are direct-instance metrics, not correctness scores. Peptone and fish extract remain undefined mixtures.

### Source pH and preparation

completeness: concern. Targets: CultureMech:008272.

Both full local files omit the explicit pH7.2 adjustment and the primary collection default autoclaving121 degrees C for15minutes unless otherwise specified. No source exception appears in this recipe. The sources do not establish an acid/base reagent or incubation condition.

### Classification, imported roles and growth limits

scope: supported. Targets: CultureMech:008272.

COMPLEX/UNDEFINED agrees with peptone/fish extract, and agar15g supports SOLID_AGAR. All role/property strings are traceable to provider annotations; these are source metadata rather than experimental functional measurements. Generic microbial cultivation asserts no organism-specific growth. No nested stock or internal organism reference is present.

### History and exact evidence placement

provenance: concern. Targets: CultureMech:008272.

All history timestamps have timezones. Both files retain source URLs in notes but lack a reference list and ingredient evidence objects. The target reference gate examines zero excerpts, which does not validate quantities or preparation.

## Findings

### f1: Source water volume is represented as a mass concentration

major / open / confirmed; issue key: CM008272-water-volume-unit.

Water is1G_PER_L in both target and owner, while TOGO/JCM explicitly say1L and MediaDive1000mL.

### f2: Source pH and adjustment instruction are missing

major / open / confirmed; issue key: CM008272-source-ph-missing.

Both layers omit pH7.2 and its adjustment instruction, although all three inspected sources preserve them.

### f3: JCM sterilization default is omitted

major / open / confirmed; issue key: CM008272-source-sterilization-missing.

The source collection header specifies121 degrees C for15minutes unless otherwise stated; this recipe has no override and both local layers omit preparation.

### f4: Source notes lack narrow reference evidence

minor / open / confirmed; issue key: CM008272-claim-evidence-gap.

Source URLs and imported annotations identify the recipe but no exact excerpts support its quantities, supplied materials or preparation at claim level.

## Recommended Actions And Acceptance Checks

### a1

Correct the maintained water amount/unit with literal source batch-volume evidence; preserve concentration denominator context and regenerate after owner validation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add the source-supported pH and adjustment instruction to the maintained owner without inventing an acid/base reagent, then regenerate.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Represent the collection default and its exception with exact source scope in the owner before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Add verified reference metadata and short exact excerpts at narrow claims, distinguishing provider concentration support from primary batch amounts.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M170_2.5_NaCl-BPG_Agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch008/080/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/080/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml:1:id: CultureMech:008272<br>./data/normalized_yaml/bacterial/TOGO_M170_2.5_NaCl-BPG_Agar.yaml:1:id: CultureMech:008272<br> |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15377 resolves to water and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17234 resolves to glucose and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:2509 resolves to agar and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32588 resolves to potassium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=177; GRMD177; composition; pH instruction; collection header | supports | Complete primary eight-row recipe, pH instruction and collection header inspected: Bacto peptone(BD-Difco)5g, fish meat extract5g, glucose1g, agar15g, NaCl25g, MgSO4·7H2O2.5g, KCl1g and water1L. Adjust pH7.2. General collection default is121 degrees C for15minutes unless otherwise stated. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M170; meta; components[0].items; comments[0] | supports | Complete M170 API identifies JCM_M177 and its primary URL, water1L, seven solute amounts, source roles/properties and pH7.2/comment. |
| api | https://mediadive.dsmz.de/rest/medium/J177; data.medium; solutions[0].recipe and steps | supports | J177 resolves to JCM177. Main solution volume1000mL and seven explicit g_l values support solute concentrations; water is separately1000mL without a g_l field. |
| context | Complete target, owner and captured provider rows; All eight quantities, imported annotation provenance and history timestamps | supports | {"quantity_trace": [{"field": "ingredients[0].concentration", "material": "Distilled water", "target": {"value": "1", "unit": "G_PER_L"}, "togo_amount": 1, "togo_unit": "L", "provider_g_l": null, "provider_locator": "$.data.solutions[0].recipe[7]", "decision": "correct solvent-volume unit"}, {"field": "ingredients[1].concentration", "material": "MgSO4\u30fb7H2O", "target": {"value": "2.5", "unit": "G_PER_L"}, "togo_amount": 2.5, "togo_unit": "g", "provider_g_l": 2.5, "provider_locator": "$.data.solutions[0].recipe[5]", "decision": "verified provider concentration"}, {"field": "ingredients[2].concentration", "material": "NaCl", "target": {"value": "25", "unit": "G_PER_L"}, "togo_amount": 25, "togo_unit": "g", "provider_g_l": 25, "provider_locator": "$.data.solutions[0].recipe[4]", "decision": "verified provider concentration"}, {"field": "ingredients[3].concentration", "material": "KCl", "target": {"value": "1", "unit": "G_PER_L"}, "togo_amount": 1, "togo_unit": "g", "provider_g_l": 1, "provider_locator": "$.data.solutions[0].recipe[6]", "decision": "verified provider concentration"}, {"field": "ingredients[4].concentration", "material": "Glucose", "target": {"value": "1", "unit": "G_PER_L"}, "togo_amount": 1, "togo_unit": "g", "provider_g_l": 1, "provider_locator": "$.data.solutions[0].recipe[2]", "decision": "verified provider concentration"}, {"field": "ingredients[5].concentration", "material": "Agar", "target": {"value": "15", "unit": "G_PER_L"}, "togo_amount": 15, "togo_unit": "g", "provider_g_l": 15, "provider_locator": "$.data.solutions[0].recipe[3]", "decision": "verified provider concentration"}, {"field": "ingredients[6].concentration", "material": "Bacto peptone (BD-Difco)", "target": {"value": "5", "unit": "G_PER_L"}, "togo_amount": 5, "togo_unit": "g", "provider_g_l": 5, "provider_locator": "$.data.solutions[0].recipe[0]", "decision": "verified provider concentration"}, {"field": "ingredients[7].concentration", "material": "Fish meat extract", "target": {"value": "5", "unit": "G_PER_L"}, "togo_amount": 5, "togo_unit": "g", "provider_g_l": 5, "provider_locator": "$.data.solutions[0].recipe[1]", "decision": "verified provider concentration"}], "roles_properties_match_provider": true, "timezone_bearing_history_counts": [8, 7]} |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No organism-specific literature, measured final volume or experimental role validation was performed. No provider agar molarity or mixture molecular weight was adopted.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T073123Z-culturemech-008272-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 2_5_nacl_bpg_agar (CultureMech:008272)'
started_at: '2026-10-21T07:20:57Z'
finished_at: '2026-10-21T07:31:23Z'
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
summary: TOGO M170 resolves to JCM177 and preserves all seven supported solute amounts
  and supplied forms. Both local layers misrepresent source water1L as1g/L and omit
  pH7.2, the pH-adjustment step and the JCM sterilization default. Chemical mappings
  resolve, including the corrected magnesium sulfate heptahydrate.
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
  - path: data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml
    sha256: 029b2b27dee5ccf5bb5715ff48fe5f4b523ac675078ccdb099793f2505022fe6
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M170_2.5_NaCl-BPG_Agar.yaml
    sha256: 8ded2e8685e1a9fde52a06d701cf6470543cdaf8f3ca5f4eeb6931e47665b4a6
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
  selection: Task review 80; batch 008 item 10 of 10, selected in Python lexicographic
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
  - CultureMech:008272
targets:
- target_id: CultureMech:008272
  path: data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml
  label: 2_5_nacl_bpg_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M170_2.5_NaCl-BPG_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008272
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch008/080/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/080/strict.tsv"
  target_ids:
  - CultureMech:008272
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008272
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008272
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
  - CultureMech:008272
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T07:31:20Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M170_2.5_NaCl-BPG_Agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T07:31:20Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:22:37.630910Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch008/080/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T07:22:39.596898Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/080/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:22:41.986955Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:22:43.559443Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T07:31:20Z'
  support: supports
  summary: './data/merge_yaml/merged/2_5_nacl_bpg_agar__bf5a0a80.yaml:1:id: CultureMech:008272

    ./data/normalized_yaml/bacterial/TOGO_M170_2.5_NaCl-BPG_Agar.yaml:1:id: CultureMech:008272

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
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T06:57:46.747221Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T06:57:47.406565Z'
  support: supports
  summary: CHEBI:32588 resolves to potassium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T07:31:20Z'
  support: supports
  summary: '{"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label":
    "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term":
    "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=177
  locator: GRMD177; composition; pH instruction; collection header
  accessed_at: '2026-10-21T07:16:25.682086Z'
  support: supports
  summary: 'Complete primary eight-row recipe, pH instruction and collection header
    inspected: Bacto peptone(BD-Difco)5g, fish meat extract5g, glucose1g, agar15g,
    NaCl25g, MgSO4·7H2O2.5g, KCl1g and water1L. Adjust pH7.2. General collection default
    is121 degrees C for15minutes unless otherwise stated.'
  quote: Adjust pH to 7.2.
  snapshot_sha256: 8fe25920cef282e25e425827d1cbb1d4454bc9bbfa35b8419464b300c8aee601
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M170
  locator: meta; components[0].items; comments[0]
  accessed_at: '2026-10-21T07:16:20.370417Z'
  support: supports
  summary: Complete M170 API identifies JCM_M177 and its primary URL, water1L, seven
    solute amounts, source roles/properties and pH7.2/comment.
  snapshot_sha256: 733d55bee2ef0681bfb86585353351c9131e1688dd2fe356a21c8e6722c9ea15
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J177
  locator: data.medium; solutions[0].recipe and steps
  accessed_at: '2026-10-21T07:16:20.342596Z'
  support: supports
  summary: J177 resolves to JCM177. Main solution volume1000mL and seven explicit
    g_l values support solute concentrations; water is separately1000mL without a
    g_l field.
  snapshot_sha256: de84e819d8156c53750aa71652021bd4d3f9b7a7f7ade55fc8536b6e3da30859
- evidence_id: context
  kind: validation
  reference: Complete target, owner and captured provider rows
  locator: All eight quantities, imported annotation provenance and history timestamps
  accessed_at: '2026-10-21T07:31:20Z'
  support: supports
  summary: '{"quantity_trace": [{"field": "ingredients[0].concentration", "material":
    "Distilled water", "target": {"value": "1", "unit": "G_PER_L"}, "togo_amount":
    1, "togo_unit": "L", "provider_g_l": null, "provider_locator": "$.data.solutions[0].recipe[7]",
    "decision": "correct solvent-volume unit"}, {"field": "ingredients[1].concentration",
    "material": "MgSO4\u30fb7H2O", "target": {"value": "2.5", "unit": "G_PER_L"},
    "togo_amount": 2.5, "togo_unit": "g", "provider_g_l": 2.5, "provider_locator":
    "$.data.solutions[0].recipe[5]", "decision": "verified provider concentration"},
    {"field": "ingredients[2].concentration", "material": "NaCl", "target": {"value":
    "25", "unit": "G_PER_L"}, "togo_amount": 25, "togo_unit": "g", "provider_g_l":
    25, "provider_locator": "$.data.solutions[0].recipe[4]", "decision": "verified
    provider concentration"}, {"field": "ingredients[3].concentration", "material":
    "KCl", "target": {"value": "1", "unit": "G_PER_L"}, "togo_amount": 1, "togo_unit":
    "g", "provider_g_l": 1, "provider_locator": "$.data.solutions[0].recipe[6]", "decision":
    "verified provider concentration"}, {"field": "ingredients[4].concentration",
    "material": "Glucose", "target": {"value": "1", "unit": "G_PER_L"}, "togo_amount":
    1, "togo_unit": "g", "provider_g_l": 1, "provider_locator": "$.data.solutions[0].recipe[2]",
    "decision": "verified provider concentration"}, {"field": "ingredients[5].concentration",
    "material": "Agar", "target": {"value": "15", "unit": "G_PER_L"}, "togo_amount":
    15, "togo_unit": "g", "provider_g_l": 15, "provider_locator": "$.data.solutions[0].recipe[3]",
    "decision": "verified provider concentration"}, {"field": "ingredients[6].concentration",
    "material": "Bacto peptone (BD-Difco)", "target": {"value": "5", "unit": "G_PER_L"},
    "togo_amount": 5, "togo_unit": "g", "provider_g_l": 5, "provider_locator": "$.data.solutions[0].recipe[0]",
    "decision": "verified provider concentration"}, {"field": "ingredients[7].concentration",
    "material": "Fish meat extract", "target": {"value": "5", "unit": "G_PER_L"},
    "togo_amount": 5, "togo_unit": "g", "provider_g_l": 5, "provider_locator": "$.data.solutions[0].recipe[1]",
    "decision": "verified provider concentration"}], "roles_properties_match_provider":
    true, "timezone_bearing_history_counts": [8, 7]}'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008272
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '6 primary CHEBI identities resolve with matching labels; 5 of 5 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:008272
  evidence_ids:
  - record
  - mim
  - chebi15377
  - chebi17234
  - chebi2509
  - chebi26710
  - chebi31795
  - chebi32588
  details: 8 direct ingredient instances; CHEBI-primary instance linkage 6/8 (75.00%),
    verified secondary coverage 5/8 (62.50%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: TOGO M170 from JCM177
  outcome: supported
  summary: Stable ID, merge owner and exact provider source metadata establish this
    formulation. The source preserves BD-Difco Bacto peptone and the seven-water magnesium
    sulfate form. Similar naming to the separate MediaDive import is not the sole
    identity evidence.
  target_ids:
  - CultureMech:008272
  evidence_ids:
  - record
  - owner-0
  - id-search
  - togo
  - jcm
  - api
- assessment_id: amounts
  area: quantity
  topic: Every listed amount and unit
  outcome: concern
  summary: 'correct: water1G_PER_L conflicts with source1L and provider1000mL. The
    seven solute values agree with explicit provider g_l and source gram amounts.
    Preserve literal solvent-batch context; neither the water row nor nominal provider
    volume establishes an independently measured final volume. No density-based water
    conversion is warranted.'
  target_ids:
  - CultureMech:008272
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - api
  - context
  details: '[{"field": "ingredients[0].concentration", "material": "Distilled water",
    "target": {"value": "1", "unit": "G_PER_L"}, "togo_amount": 1, "togo_unit": "L",
    "provider_g_l": null, "provider_locator": "$.data.solutions[0].recipe[7]", "decision":
    "correct solvent-volume unit"}, {"field": "ingredients[1].concentration", "material":
    "MgSO4\u30fb7H2O", "target": {"value": "2.5", "unit": "G_PER_L"}, "togo_amount":
    2.5, "togo_unit": "g", "provider_g_l": 2.5, "provider_locator": "$.data.solutions[0].recipe[5]",
    "decision": "verified provider concentration"}, {"field": "ingredients[2].concentration",
    "material": "NaCl", "target": {"value": "25", "unit": "G_PER_L"}, "togo_amount":
    25, "togo_unit": "g", "provider_g_l": 25, "provider_locator": "$.data.solutions[0].recipe[4]",
    "decision": "verified provider concentration"}, {"field": "ingredients[3].concentration",
    "material": "KCl", "target": {"value": "1", "unit": "G_PER_L"}, "togo_amount":
    1, "togo_unit": "g", "provider_g_l": 1, "provider_locator": "$.data.solutions[0].recipe[6]",
    "decision": "verified provider concentration"}, {"field": "ingredients[4].concentration",
    "material": "Glucose", "target": {"value": "1", "unit": "G_PER_L"}, "togo_amount":
    1, "togo_unit": "g", "provider_g_l": 1, "provider_locator": "$.data.solutions[0].recipe[2]",
    "decision": "verified provider concentration"}, {"field": "ingredients[5].concentration",
    "material": "Agar", "target": {"value": "15", "unit": "G_PER_L"}, "togo_amount":
    15, "togo_unit": "g", "provider_g_l": 15, "provider_locator": "$.data.solutions[0].recipe[3]",
    "decision": "verified provider concentration"}, {"field": "ingredients[6].concentration",
    "material": "Bacto peptone (BD-Difco)", "target": {"value": "5", "unit": "G_PER_L"},
    "togo_amount": 5, "togo_unit": "g", "provider_g_l": 5, "provider_locator": "$.data.solutions[0].recipe[0]",
    "decision": "verified provider concentration"}, {"field": "ingredients[7].concentration",
    "material": "Fish meat extract", "target": {"value": "5", "unit": "G_PER_L"},
    "togo_amount": 5, "togo_unit": "g", "provider_g_l": 5, "provider_locator": "$.data.solutions[0].recipe[1]",
    "decision": "verified provider concentration"}]'
- assessment_id: forms
  area: grounding
  topic: Supplied forms and linkage
  outcome: supported
  summary: All six primary CHEBI IDs/labels match captured ontology terms, including
    CHEBI31795 for MgSO4·7H2O; the historical generic ID is no longer asserted. Five
    secondary keys have current pinned preferred-term rows. Primary linkage6/8(75%)
    and secondary5/8(62.5%) are direct-instance metrics, not correctness scores. Peptone
    and fish extract remain undefined mixtures.
  target_ids:
  - CultureMech:008272
  evidence_ids:
  - record
  - mim
  - chebi31795
  - chebi15377
  - chebi17234
  - chebi2509
  - chebi26710
  - chebi32588
  - jcm
- assessment_id: conditions
  area: completeness
  topic: Source pH and preparation
  outcome: concern
  summary: Both full local files omit the explicit pH7.2 adjustment and the primary
    collection default autoclaving121 degrees C for15minutes unless otherwise specified.
    No source exception appears in this recipe. The sources do not establish an acid/base
    reagent or incubation condition.
  target_ids:
  - CultureMech:008272
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - api
- assessment_id: scope
  area: scope
  topic: Classification, imported roles and growth limits
  outcome: supported
  summary: COMPLEX/UNDEFINED agrees with peptone/fish extract, and agar15g supports
    SOLID_AGAR. All role/property strings are traceable to provider annotations; these
    are source metadata rather than experimental functional measurements. Generic
    microbial cultivation asserts no organism-specific growth. No nested stock or
    internal organism reference is present.
  target_ids:
  - CultureMech:008272
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - context
- assessment_id: provenance
  area: provenance
  topic: History and exact evidence placement
  outcome: concern
  summary: All history timestamps have timezones. Both files retain source URLs in
    notes but lack a reference list and ingredient evidence objects. The target reference
    gate examines zero excerpts, which does not validate quantities or preparation.
  target_ids:
  - CultureMech:008272
  evidence_ids:
  - record
  - owner-0
  - context
  - validate-references
findings:
- finding_id: f1
  issue_key: CM008272-water-volume-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Source water volume is represented as a mass concentration
  description: Water is1G_PER_L in both target and owner, while TOGO/JCM explicitly
    say1L and MediaDive1000mL.
  target_ids:
  - CultureMech:008272
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - api
  - context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M170_2.5_NaCl-BPG_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM008272-source-ph-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source pH and adjustment instruction are missing
  description: Both layers omit pH7.2 and its adjustment instruction, although all
    three inspected sources preserve them.
  target_ids:
  - CultureMech:008272
  field_paths:
  - ph_value
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M170_2.5_NaCl-BPG_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM008272-source-sterilization-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: JCM sterilization default is omitted
  description: The source collection header specifies121 degrees C for15minutes unless
    otherwise stated; this recipe has no override and both local layers omit preparation.
  target_ids:
  - CultureMech:008272
  field_paths:
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M170_2.5_NaCl-BPG_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: CM008272-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source notes lack narrow reference evidence
  description: Source URLs and imported annotations identify the recipe but no exact
    excerpts support its quantities, supplied materials or preparation at claim level.
  target_ids:
  - CultureMech:008272
  field_paths:
  - references
  - ingredients[*].evidence
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - api
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M170_2.5_NaCl-BPG_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Correct the maintained water amount/unit with literal source batch-volume
    evidence; preserve concentration denominator context and regenerate after owner
    validation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008272
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M170_2.5_NaCl-BPG_Agar.yaml
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
  description: Add the source-supported pH and adjustment instruction to the maintained
    owner without inventing an acid/base reagent, then regenerate.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008272
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M170_2.5_NaCl-BPG_Agar.yaml
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
  description: Represent the collection default and its exception with exact source
    scope in the owner before regeneration.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008272
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M170_2.5_NaCl-BPG_Agar.yaml
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
  description: Add verified reference metadata and short exact excerpts at narrow
    claims, distinguishing provider concentration support from primary batch amounts.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008272
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M170_2.5_NaCl-BPG_Agar.yaml
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
- No organism-specific literature, measured final volume or experimental role validation
  was performed. No provider agar molarity or mixture molecular weight was adopted.
tags:
- unreviewed-records
- batch-008
- generated-medium
```
