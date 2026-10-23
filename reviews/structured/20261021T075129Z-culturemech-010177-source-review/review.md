# Source and formulation review: 2_nacl_ypg_agar (CultureMech:010177)

- Review: 20261021T075129Z-culturemech-010177-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T07:45:24Z
- Finished UTC: 2026-10-21T07:51:29Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M76 identifies JCM 85 and all five solute concentrations are supported. Both local layers encode water 1 L as 1 g/L and omit the source pH range and JCM sterilization default. Four primary and four secondary chemical identifiers resolve, but source notes lack claim-level evidence.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 86; batch 009 item 6 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding eight task batches contain 80 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 82 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010177 | data/merge_yaml/merged/2_nacl_ypg_agar.yaml | generated | 2_nacl_ypg_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010177 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010177 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-009/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch009/086/strict.tsv |
| validate-terms | passed | True | CultureMech:010177 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010177 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010177 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010177.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:010177.

4 primary CHEBI identities resolve with matching labels; 4 of 4 current secondary keys have live pinned-index rows. Unresolved keys: [].

6 direct ingredient instances; CHEBI-primary instance linkage 4/6 (66.67%), verified secondary coverage 4/6 (66.67%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### TOGO M76 from JCM GRMD 85

identity: supported. Targets: CultureMech:010177.

Stable ID and merge event resolve the maintained owner. Both providers explicitly identify the same primary JCM accession and recipe; generic naming is not used as sole identity evidence.

### Every direct amount and unit

quantity: concern. Targets: CultureMech:010177.

The five solutes agree with explicit provider g_l and primary gram amounts. Water 1 g/L conflicts with source 1 L / provider 1000 ml. Preserve literal source water input and provider concentration basis without claiming an independently measured final volume, water density or mixture molarity. No stock or nested dilution appears in the complete source.

[{"field": "ingredients[0].concentration", "material": "Distilled water", "record": {"value": "1", "unit": "G_PER_L"}, "source_amount": 1, "source_unit": "L", "provider_g_l": null, "provider_locator": "$.data.solutions[0].recipe[5]", "decision": "correct volume unit"}, {"field": "ingredients[1].concentration", "material": "Yeast extract", "record": {"value": "10", "unit": "G_PER_L"}, "source_amount": 10, "source_unit": "g", "provider_g_l": 10, "provider_locator": "$.data.solutions[0].recipe[3]", "decision": "verified provider concentration"}, {"field": "ingredients[2].concentration", "material": "NaCl", "record": {"value": "20", "unit": "G_PER_L"}, "source_amount": 20, "source_unit": "g", "provider_g_l": 20, "provider_locator": "$.data.solutions[0].recipe[0]", "decision": "verified provider concentration"}, {"field": "ingredients[3].concentration", "material": "Glucose", "record": {"value": "20", "unit": "G_PER_L"}, "source_amount": 20, "source_unit": "g", "provider_g_l": 20, "provider_locator": "$.data.solutions[0].recipe[1]", "decision": "verified provider concentration"}, {"field": "ingredients[4].concentration", "material": "Agar", "record": {"value": "20", "unit": "G_PER_L"}, "source_amount": 20, "source_unit": "g", "provider_g_l": 20, "provider_locator": "$.data.solutions[0].recipe[4]", "decision": "verified provider concentration"}, {"field": "ingredients[5].concentration", "material": "Peptone", "record": {"value": "10", "unit": "G_PER_L"}, "source_amount": 10, "source_unit": "g", "provider_g_l": 10, "provider_locator": "$.data.solutions[0].recipe[2]", "decision": "verified provider concentration"}]

### Chemical forms and linkage

grounding: supported. Targets: CultureMech:010177.

All four primary CHEBI IDs have matching canonical labels; all four secondary keys have live pinned-index rows. Both linkage measures are 4/6 direct instances. Peptone and yeast are undefined mixtures. These are linkage metrics, not scientific accuracy scores.

### Exact pH range and collection default

completeness: concern. Targets: CultureMech:010177.

Both local layers omit pH 5.2-5.4 and its adjustment instruction as well as the JCM 121 C/15 min sterilization default. The provider scalar midpoint 5.3 must not replace the primary range. No titrant identity, strength, dose or incubation condition is supplied.

### Classification, roles and cultivation limits

scope: supported. Targets: CultureMech:010177.

Mandatory agar 20 g supports SOLID_AGAR; peptone and yeast support COMPLEX/UNDEFINED. Every imported role/property string is traceable to TOGO metadata, not experimental role evidence. Generic microbial cultivation establishes no strain-specific growth or exclusive taxonomic range.

### History and source-evidence placement

provenance: concern. Targets: CultureMech:010177.

All history timestamps have timezones. Source notes preserve exact accessions/URLs, but neither file has claim-level ingredient evidence or a reference list; the reference gate examined zero excerpts.

## Findings

### f1: Source water volume is represented as mass concentration

major / open / confirmed; issue key: CM010177-water-unit.

Both layers assert 1 g/L water instead of the source 1 L input.

### f2: Source pH range and adjustment are missing

major / open / confirmed; issue key: CM010177-ph-range-missing.

Primary JCM, TOGO and provider preparation retain 5.2-5.4; both local files omit it.

### f3: JCM sterilization default is omitted

major / open / confirmed; issue key: CM010177-sterilization-missing.

Both local files omit the source default 121 C for 15 min unless otherwise stated, with no recipe override.

### f4: Source notes lack narrow formulation evidence

minor / open / confirmed; issue key: CM010177-claim-evidence-gap.

No exact excerpts or bibliographic metadata support the formulation at claim level.

## Recommended Actions And Acceptance Checks

### a1

Restore literal solvent-volume preparation context with source evidence, without assuming density or final volume.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add the exact source range and adjustment instruction. Do not substitute midpoint 5.3 or invent a titrant.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the exact collection default and its exception scope before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Add verified source metadata and short exact excerpts for amounts, units and preparation, separating primary batch amounts from provider g_l.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/2_nacl_ypg_agar.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M76_2_NaCl-YPG_Agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/2_nacl_ypg_agar.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/2_nacl_ypg_agar.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch009/086/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-009/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch009/086/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/2_nacl_ypg_agar.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/2_nacl_ypg_agar.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/2_nacl_ypg_agar.yaml:1:id: CultureMech:010177<br>./data/normalized_yaml/bacterial/TOGO_M76_2_NaCl-YPG_Agar.yaml:1:id: CultureMech:010177<br> |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15377 resolves to water and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17234 resolves to glucose and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:2509 resolves to agar and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=85; Heading; six-row formulation; pH instruction; collection header | supports | Complete GRMD 85 page inspected: NaCl 20 g, glucose 20 g, peptone 10 g, yeast extract 10 g, agar 20 g and distilled water 1 L. The exact pH range is retained in the primary instruction. The page-wide default is 121 C/15 min autoclaving unless otherwise stated; this recipe has no exception. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M76; meta; components[0].items; comments[0] | supports | M76 explicitly identifies JCM_M85 and the primary URL. It preserves six original amounts/units, pH range 5.2-5.4 in metadata and the same range in the comment (double hyphen). |
| api | https://mediadive.dsmz.de/rest/medium/J85; data.medium; solutions[0].volume, recipe and steps | supports | J85 supplies five explicit g_l values, declared main volume 1000 ml and water 1000 ml. Its preparation preserves pH 5.2-5.4 although scalar min/max metadata is 5.3. Use the primary range, not the provider midpoint. |
| trace | Entire target, maintained owner and captured provider rows; All six quantities, role/property provenance and history timestamps | supports | [{"field": "ingredients[0].concentration", "material": "Distilled water", "record": {"value": "1", "unit": "G_PER_L"}, "source_amount": 1, "source_unit": "L", "provider_g_l": null, "provider_locator": "$.data.solutions[0].recipe[5]", "decision": "correct volume unit"}, {"field": "ingredients[1].concentration", "material": "Yeast extract", "record": {"value": "10", "unit": "G_PER_L"}, "source_amount": 10, "source_unit": "g", "provider_g_l": 10, "provider_locator": "$.data.solutions[0].recipe[3]", "decision": "verified provider concentration"}, {"field": "ingredients[2].concentration", "material": "NaCl", "record": {"value": "20", "unit": "G_PER_L"}, "source_amount": 20, "source_unit": "g", "provider_g_l": 20, "provider_locator": "$.data.solutions[0].recipe[0]", "decision": "verified provider concentration"}, {"field": "ingredients[3].concentration", "material": "Glucose", "record": {"value": "20", "unit": "G_PER_L"}, "source_amount": 20, "source_unit": "g", "provider_g_l": 20, "provider_locator": "$.data.solutions[0].recipe[1]", "decision": "verified provider concentration"}, {"field": "ingredients[4].concentration", "material": "Agar", "record": {"value": "20", "unit": "G_PER_L"}, "source_amount": 20, "source_unit": "g", "provider_g_l": 20, "provider_locator": "$.data.solutions[0].recipe[4]", "decision": "verified provider concentration"}, {"field": "ingredients[5].concentration", "material": "Peptone", "record": {"value": "10", "unit": "G_PER_L"}, "source_amount": 10, "source_unit": "g", "provider_g_l": 10, "provider_locator": "$.data.solutions[0].recipe[2]", "decision": "verified provider concentration"}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No measured final volume, organism-specific growth, experimental ingredient roles or historical importer execution was established. Current sources and original capture timestamps were retained; no corpus or generator was modified.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T075129Z-culturemech-010177-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 2_nacl_ypg_agar (CultureMech:010177)'
started_at: '2026-10-21T07:45:24Z'
finished_at: '2026-10-21T07:51:29Z'
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
summary: TOGO M76 identifies JCM 85 and all five solute concentrations are supported.
  Both local layers encode water 1 L as 1 g/L and omit the source pH range and JCM
  sterilization default. Four primary and four secondary chemical identifiers resolve,
  but source notes lack claim-level evidence.
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
  - path: data/merge_yaml/merged/2_nacl_ypg_agar.yaml
    sha256: bfd1922a22b72ba554150f21ad729b4d887da7767acf3064d2ceecb82fc03103
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M76_2_NaCl-YPG_Agar.yaml
    sha256: 94ceafa60b660facdaffa665abe28b44e07104129dc6b5d0b6cb3392642f0272
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
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
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
  selection: Task review 86; batch 009 item 6 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding eight task batches contain
    80 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 82 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010177
targets:
- target_id: CultureMech:010177
  path: data/merge_yaml/merged/2_nacl_ypg_agar.yaml
  label: 2_nacl_ypg_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M76_2_NaCl-YPG_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/2_nacl_ypg_agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010177
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/2_nacl_ypg_agar.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch009/086/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-009/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch009/086/strict.tsv"
  target_ids:
  - CultureMech:010177
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/2_nacl_ypg_agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010177
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/2_nacl_ypg_agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010177
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
  - CultureMech:010177
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/2_nacl_ypg_agar.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T07:51:16Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M76_2_NaCl-YPG_Agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T07:51:16Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/2_nacl_ypg_agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:47:59.033885Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/2_nacl_ypg_agar.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch009/086/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T07:48:01.414746Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-009/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch009/086/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/2_nacl_ypg_agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:48:05.567466Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/2_nacl_ypg_agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:48:07.429032Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T07:51:16Z'
  support: supports
  summary: './data/merge_yaml/merged/2_nacl_ypg_agar.yaml:1:id: CultureMech:010177

    ./data/normalized_yaml/bacterial/TOGO_M76_2_NaCl-YPG_Agar.yaml:1:id: CultureMech:010177

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:31:15.205780Z'
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
  accessed_at: '2026-10-21T07:31:15.211005Z'
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
  accessed_at: '2026-10-21T07:31:15.863758Z'
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
  accessed_at: '2026-10-21T07:31:15.881003Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T07:51:16Z'
  support: supports
  summary: '{"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label":
    "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term":
    "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}'
- evidence_id: jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=85
  locator: Heading; six-row formulation; pH instruction; collection header
  accessed_at: '2026-10-21T07:33:35.640291Z'
  support: supports
  summary: 'Complete GRMD 85 page inspected: NaCl 20 g, glucose 20 g, peptone 10 g,
    yeast extract 10 g, agar 20 g and distilled water 1 L. The exact pH range is retained
    in the primary instruction. The page-wide default is 121 C/15 min autoclaving
    unless otherwise stated; this recipe has no exception.'
  quote: Adjust pH to 5.2-5.4.
  snapshot_sha256: f71a7b87f9e1c694643621a0ab490eed5df5818002a54ec1afec1db971fd11e0
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M76
  locator: meta; components[0].items; comments[0]
  accessed_at: '2026-10-21T07:33:27.978460Z'
  support: supports
  summary: M76 explicitly identifies JCM_M85 and the primary URL. It preserves six
    original amounts/units, pH range 5.2-5.4 in metadata and the same range in the
    comment (double hyphen).
  snapshot_sha256: 9d9eb1dfa9f381ff0715c904178a3351e89da327897c2320280063702461de1d
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J85
  locator: data.medium; solutions[0].volume, recipe and steps
  accessed_at: '2026-10-21T07:33:27.333398Z'
  support: supports
  summary: J85 supplies five explicit g_l values, declared main volume 1000 ml and
    water 1000 ml. Its preparation preserves pH 5.2-5.4 although scalar min/max metadata
    is 5.3. Use the primary range, not the provider midpoint.
  snapshot_sha256: 15379a401762b61d7cf03c43f924503e757445b1516883280cbb0df738de0a65
- evidence_id: trace
  kind: validation
  reference: Entire target, maintained owner and captured provider rows
  locator: All six quantities, role/property provenance and history timestamps
  accessed_at: '2026-10-21T07:51:16Z'
  support: supports
  summary: '[{"field": "ingredients[0].concentration", "material": "Distilled water",
    "record": {"value": "1", "unit": "G_PER_L"}, "source_amount": 1, "source_unit":
    "L", "provider_g_l": null, "provider_locator": "$.data.solutions[0].recipe[5]",
    "decision": "correct volume unit"}, {"field": "ingredients[1].concentration",
    "material": "Yeast extract", "record": {"value": "10", "unit": "G_PER_L"}, "source_amount":
    10, "source_unit": "g", "provider_g_l": 10, "provider_locator": "$.data.solutions[0].recipe[3]",
    "decision": "verified provider concentration"}, {"field": "ingredients[2].concentration",
    "material": "NaCl", "record": {"value": "20", "unit": "G_PER_L"}, "source_amount":
    20, "source_unit": "g", "provider_g_l": 20, "provider_locator": "$.data.solutions[0].recipe[0]",
    "decision": "verified provider concentration"}, {"field": "ingredients[3].concentration",
    "material": "Glucose", "record": {"value": "20", "unit": "G_PER_L"}, "source_amount":
    20, "source_unit": "g", "provider_g_l": 20, "provider_locator": "$.data.solutions[0].recipe[1]",
    "decision": "verified provider concentration"}, {"field": "ingredients[4].concentration",
    "material": "Agar", "record": {"value": "20", "unit": "G_PER_L"}, "source_amount":
    20, "source_unit": "g", "provider_g_l": 20, "provider_locator": "$.data.solutions[0].recipe[4]",
    "decision": "verified provider concentration"}, {"field": "ingredients[5].concentration",
    "material": "Peptone", "record": {"value": "10", "unit": "G_PER_L"}, "source_amount":
    10, "source_unit": "g", "provider_g_l": 10, "provider_locator": "$.data.solutions[0].recipe[2]",
    "decision": "verified provider concentration"}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010177
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '4 primary CHEBI identities resolve with matching labels; 4 of 4 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:010177
  evidence_ids:
  - record
  - mim
  - chebi15377
  - chebi17234
  - chebi2509
  - chebi26710
  details: 6 direct ingredient instances; CHEBI-primary instance linkage 4/6 (66.67%),
    verified secondary coverage 4/6 (66.67%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: TOGO M76 from JCM GRMD 85
  outcome: supported
  summary: Stable ID and merge event resolve the maintained owner. Both providers
    explicitly identify the same primary JCM accession and recipe; generic naming
    is not used as sole identity evidence.
  target_ids:
  - CultureMech:010177
  evidence_ids:
  - record
  - owner-0
  - id-search
  - jcm
  - togo
  - api
- assessment_id: amounts
  area: quantity
  topic: Every direct amount and unit
  outcome: concern
  summary: The five solutes agree with explicit provider g_l and primary gram amounts.
    Water 1 g/L conflicts with source 1 L / provider 1000 ml. Preserve literal source
    water input and provider concentration basis without claiming an independently
    measured final volume, water density or mixture molarity. No stock or nested dilution
    appears in the complete source.
  target_ids:
  - CultureMech:010177
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - api
  - trace
  details: '[{"field": "ingredients[0].concentration", "material": "Distilled water",
    "record": {"value": "1", "unit": "G_PER_L"}, "source_amount": 1, "source_unit":
    "L", "provider_g_l": null, "provider_locator": "$.data.solutions[0].recipe[5]",
    "decision": "correct volume unit"}, {"field": "ingredients[1].concentration",
    "material": "Yeast extract", "record": {"value": "10", "unit": "G_PER_L"}, "source_amount":
    10, "source_unit": "g", "provider_g_l": 10, "provider_locator": "$.data.solutions[0].recipe[3]",
    "decision": "verified provider concentration"}, {"field": "ingredients[2].concentration",
    "material": "NaCl", "record": {"value": "20", "unit": "G_PER_L"}, "source_amount":
    20, "source_unit": "g", "provider_g_l": 20, "provider_locator": "$.data.solutions[0].recipe[0]",
    "decision": "verified provider concentration"}, {"field": "ingredients[3].concentration",
    "material": "Glucose", "record": {"value": "20", "unit": "G_PER_L"}, "source_amount":
    20, "source_unit": "g", "provider_g_l": 20, "provider_locator": "$.data.solutions[0].recipe[1]",
    "decision": "verified provider concentration"}, {"field": "ingredients[4].concentration",
    "material": "Agar", "record": {"value": "20", "unit": "G_PER_L"}, "source_amount":
    20, "source_unit": "g", "provider_g_l": 20, "provider_locator": "$.data.solutions[0].recipe[4]",
    "decision": "verified provider concentration"}, {"field": "ingredients[5].concentration",
    "material": "Peptone", "record": {"value": "10", "unit": "G_PER_L"}, "source_amount":
    10, "source_unit": "g", "provider_g_l": 10, "provider_locator": "$.data.solutions[0].recipe[2]",
    "decision": "verified provider concentration"}]'
- assessment_id: grounding-detail
  area: grounding
  topic: Chemical forms and linkage
  outcome: supported
  summary: All four primary CHEBI IDs have matching canonical labels; all four secondary
    keys have live pinned-index rows. Both linkage measures are 4/6 direct instances.
    Peptone and yeast are undefined mixtures. These are linkage metrics, not scientific
    accuracy scores.
  target_ids:
  - CultureMech:010177
  evidence_ids:
  - record
  - mim
  - jcm
  - chebi15377
  - chebi17234
  - chebi2509
  - chebi26710
- assessment_id: preparation
  area: completeness
  topic: Exact pH range and collection default
  outcome: concern
  summary: Both local layers omit pH 5.2-5.4 and its adjustment instruction as well
    as the JCM 121 C/15 min sterilization default. The provider scalar midpoint 5.3
    must not replace the primary range. No titrant identity, strength, dose or incubation
    condition is supplied.
  target_ids:
  - CultureMech:010177
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - api
- assessment_id: scope
  area: scope
  topic: Classification, roles and cultivation limits
  outcome: supported
  summary: Mandatory agar 20 g supports SOLID_AGAR; peptone and yeast support COMPLEX/UNDEFINED.
    Every imported role/property string is traceable to TOGO metadata, not experimental
    role evidence. Generic microbial cultivation establishes no strain-specific growth
    or exclusive taxonomic range.
  target_ids:
  - CultureMech:010177
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - trace
- assessment_id: provenance
  area: provenance
  topic: History and source-evidence placement
  outcome: concern
  summary: All history timestamps have timezones. Source notes preserve exact accessions/URLs,
    but neither file has claim-level ingredient evidence or a reference list; the
    reference gate examined zero excerpts.
  target_ids:
  - CultureMech:010177
  evidence_ids:
  - record
  - owner-0
  - trace
  - validate-references
findings:
- finding_id: f1
  issue_key: CM010177-water-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Source water volume is represented as mass concentration
  description: Both layers assert 1 g/L water instead of the source 1 L input.
  target_ids:
  - CultureMech:010177
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M76_2_NaCl-YPG_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM010177-ph-range-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source pH range and adjustment are missing
  description: Primary JCM, TOGO and provider preparation retain 5.2-5.4; both local
    files omit it.
  target_ids:
  - CultureMech:010177
  field_paths:
  - ph_range
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M76_2_NaCl-YPG_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM010177-sterilization-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: JCM sterilization default is omitted
  description: Both local files omit the source default 121 C for 15 min unless otherwise
    stated, with no recipe override.
  target_ids:
  - CultureMech:010177
  field_paths:
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M76_2_NaCl-YPG_Agar.yaml
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
  issue_key: CM010177-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source notes lack narrow formulation evidence
  description: No exact excerpts or bibliographic metadata support the formulation
    at claim level.
  target_ids:
  - CultureMech:010177
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
    path: data/normalized_yaml/bacterial/TOGO_M76_2_NaCl-YPG_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Restore literal solvent-volume preparation context with source evidence,
    without assuming density or final volume.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010177
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M76_2_NaCl-YPG_Agar.yaml
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
  description: Add the exact source range and adjustment instruction. Do not substitute
    midpoint 5.3 or invent a titrant.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010177
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M76_2_NaCl-YPG_Agar.yaml
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
  description: Preserve the exact collection default and its exception scope before
    regeneration.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010177
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M76_2_NaCl-YPG_Agar.yaml
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
  description: Add verified source metadata and short exact excerpts for amounts,
    units and preparation, separating primary batch amounts from provider g_l.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010177
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M76_2_NaCl-YPG_Agar.yaml
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
- No measured final volume, organism-specific growth, experimental ingredient roles
  or historical importer execution was established. Current sources and original capture
  timestamps were retained; no corpus or generator was modified.
tags:
- unreviewed-records
- batch-009
- generated-medium
```
