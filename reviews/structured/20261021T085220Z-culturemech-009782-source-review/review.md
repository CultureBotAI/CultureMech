# Source and formulation review: 6_b_medium (CultureMech:009782)

- Review: 20261021T085220Z-culturemech-009782-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T08:48:56Z
- Finished UTC: 2026-10-21T08:52:20Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The seven non-water amounts and ingredient identities agree with TOGO M39 and JCM 47, but both layers turn the source 1 L of distilled water into 1 g/L. The unadjusted-pH instruction and primary sterilization default are absent, and no narrow formulation evidence or reference has been attached.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 112; batch 012 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding eleven task batches contain 110 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 112 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009782 | data/merge_yaml/merged/6_b_medium__990e4708.yaml | generated | 6_b_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009782 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009782 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch012/112/strict.tsv |
| validate-terms | passed | True | CultureMech:009782 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009782 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009782 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009782.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:009782.

6 primary CHEBI identities resolve with matching labels; 5 of 5 current secondary keys have live pinned-index rows. Unresolved keys: [].

8 direct ingredient instances; CHEBI-primary instance linkage 6/8 (75.00%), verified secondary coverage 5/8 (62.50%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Single target and exact original recipe accession

identity: supported. Targets: CultureMech:009782.

CM009782 resolves to one maintained TOGO M39 owner and one generated target. The explicit source metadata maps M39 to JCM 47; name similarity alone is not used. MediaDive J47 is a separate dataset representation of that explicitly linked source.

### Every concentration and original source unit

quantity: concern. Targets: CultureMech:009782.

Seven non-water values match the primary masses and provider-declared concentrations. Water 1 L has been changed into 1 g/L in both layers; no dimensional conversion supports that representation. All eight fields, including stock/final-volume boundaries, are documented individually.

[{"field_path": "ingredients[0].concentration", "ingredient": "Distilled water", "target_and_owner_value": {"value": "1", "unit": "G_PER_L"}, "source_key": "togoM39api", "source_locator": "$.components[0].items[0]", "original_amount": 1, "original_unit": "L", "provider_source_locator": "$.data.solutions[0].recipe[7]", "provider_volume_ml": 1000, "provider_g_l": null, "stage": "main-medium preparation, not stock or assay", "decision": "correct", "explanation": "The source amount is a 1 L preparation solvent volume, not 1 g/L. Preserve the volume in preparation context without inferring density, water mass or measured final volume."}, {"field_path": "ingredients[1].concentration", "ingredient": "CaCO3", "target_and_owner_value": {"value": "1", "unit": "G_PER_L"}, "source_key": "togoM39api", "source_locator": "$.components[0].items[1]", "original_amount": 1, "original_unit": "g", "provider_source_locator": "$.data.solutions[0].recipe[5]", "provider_volume_ml": 1000, "provider_g_l": 1, "stage": "main-medium preparation, not stock or assay", "decision": "verified", "explanation": "The source mass is retained nominally with 1 L water, and the exact MediaDive J47 representation independently reports this g/L number on its declared 1000 ml basis. No measured final volume or stock dilution is inferred."}, {"field_path": "ingredients[2].concentration", "ingredient": "Glycerol", "target_and_owner_value": {"value": "50", "unit": "G_PER_L"}, "source_key": "togoM39api", "source_locator": "$.components[0].items[2]", "original_amount": 50, "original_unit": "g", "provider_source_locator": "$.data.solutions[0].recipe[1]", "provider_volume_ml": 1000, "provider_g_l": 50, "stage": "main-medium preparation, not stock or assay", "decision": "verified", "explanation": "The source mass is retained nominally with 1 L water, and the exact MediaDive J47 representation independently reports this g/L number on its declared 1000 ml basis. No measured final volume or stock dilution is inferred."}, {"field_path": "ingredients[3].concentration", "ingredient": "Glucose", "target_and_owner_value": {"value": "10", "unit": "G_PER_L"}, "source_key": "togoM39api", "source_locator": "$.components[0].items[3]", "original_amount": 10, "original_unit": "g", "provider_source_locator": "$.data.solutions[0].recipe[3]", "provider_volume_ml": 1000, "provider_g_l": 10, "stage": "main-medium preparation, not stock or assay", "decision": "verified", "explanation": "The source mass is retained nominally with 1 L water, and the exact MediaDive J47 representation independently reports this g/L number on its declared 1000 ml basis. No measured final volume or stock dilution is inferred."}, {"field_path": "ingredients[4].concentration", "ingredient": "Soluble starch", "target_and_owner_value": {"value": "20", "unit": "G_PER_L"}, "source_key": "togoM39api", "source_locator": "$.components[0].items[4]", "original_amount": 20, "original_unit": "g", "provider_source_locator": "$.data.solutions[0].recipe[4]", "provider_volume_ml": 1000, "provider_g_l": 20, "stage": "main-medium preparation, not stock or assay", "decision": "verified", "explanation": "The source mass is retained nominally with 1 L water, and the exact MediaDive J47 representation independently reports this g/L number on its declared 1000 ml basis. No measured final volume or stock dilution is inferred."}, {"field_path": "ingredients[5].concentration", "ingredient": "Agar", "target_and_owner_value": {"value": "15", "unit": "G_PER_L"}, "source_key": "togoM39api", "source_locator": "$.components[0].items[5]", "original_amount": 15, "original_unit": "g", "provider_source_locator": "$.data.solutions[0].recipe[6]", "provider_volume_ml": 1000, "provider_g_l": 15, "stage": "main-medium preparation, not stock or assay", "decision": "verified", "explanation": "The source mass is retained nominally with 1 L water, and the exact MediaDive J47 representation independently reports this g/L number on its declared 1000 ml basis. No measured final volume or stock dilution is inferred."}, {"field_path": "ingredients[6].concentration", "ingredient": "Yeast extract (BD-Difco)", "target_and_owner_value": {"value": "5", "unit": "G_PER_L"}, "source_key": "togoM39api", "source_locator": "$.components[0].items[6]", "original_amount": 5, "original_unit": "g", "provider_source_locator": "$.data.solutions[0].recipe[0]", "provider_volume_ml": 1000, "provider_g_l": 5, "stage": "main-medium preparation, not stock or assay", "decision": "verified", "explanation": "The source mass is retained nominally with 1 L water, and the exact MediaDive J47 representation independently reports this g/L number on its declared 1000 ml basis. No measured final volume or stock dilution is inferred."}, {"field_path": "ingredients[7].concentration", "ingredient": "N--Z amine, type A (Sheffield)", "target_and_owner_value": {"value": "5", "unit": "G_PER_L"}, "source_key": "togoM39api", "source_locator": "$.components[0].items[7]", "original_amount": 5, "original_unit": "g", "provider_source_locator": "$.data.solutions[0].recipe[2]", "provider_volume_ml": 1000, "provider_g_l": 5, "stage": "main-medium preparation, not stock or assay", "decision": "verified", "explanation": "The source mass is retained nominally with 1 L water, and the exact MediaDive J47 representation independently reports this g/L number on its declared 1000 ml basis. No measured final volume or stock dilution is inferred."}]

### Exact source materials versus ontology metadata

grounding: supported. Targets: CultureMech:009782.

Source soluble starch is explicitly retained in the ingredient name while CHEBI gives the generic starch class. BD-Difco yeast extract and Sheffield N-Z amine type A qualifiers are retained. Glycerol, glucose without an added stereochemical restriction, calcium carbonate and agar match the stated source materials; water identity is valid even though its unit is wrong. Six primary CHEBI IDs and five current secondary keys are separately checked; undefined mixtures are not assigned invented molecules.

### Source pH instruction and sterilization default

completeness: concern. Targets: CultureMech:009782.

Both layers lack preparation steps. JCM and TOGO retain pH unadjusted, which is not a numeric pH target. The JCM page also supplies a default 121 C for 15 min autoclaving requirement; no recipe-specific exception is stated. No extra incubation, storage or cooling conditions are inferred.

### Physical state, complex ingredients and organism scope

scope: supported. Targets: CultureMech:009782.

The source agar addition supports solid-agar classification, and yeast extract/N-Z amine support complex undefined composition. Neither layer asserts stocks, variants, parent relationships, KG correspondence or organism-specific growth. Bacterial filing and a generic cultivation application are not strain-level evidence.

### Recoverable source links versus claim-level evidence

evidence: concern. Targets: CultureMech:009782.

Notes and media_term preserve exact TOGO/JCM source identity, but neither layer has a bibliography or narrow ingredient/preparation evidence. The reference diagnostic performed zero checks. Evidence should retain catalogue/dataset type, actual access time, exact source locator and missing author/year metadata without inventing a publication.

### Timezone-aware events and generated ownership

provenance: supported. Targets: CultureMech:009782.

All 8 target and 7 owner timestamps parse with timezones. The generated record preserves the seven owner events and appends its August merge event. Current target ingredient content equals its maintained owner; no historical process was rerun and no event was rewritten.

## Findings

### f1: The source water volume is represented as a mass concentration

major / open / confirmed; issue key: CM009782-water-volume-unit.

Both target and owner encode distilled water as 1 G_PER_L, while exact TOGO M39 and JCM 47 specify 1 L water. The unit change is dimensionally unsupported; the valid water ontology term and schema pass do not correct it.

### f2: Unadjusted pH and source sterilization were omitted

major / open / confirmed; issue key: CM009782-source-preparation-omitted.

The complex medium has no preparation steps in either layer. The source pH-unadjusted instruction and JCM default sterilization are available but absent, materially limiting faithful preparation. Native P3.4 is normalized to major for these source-supported omissions.

### f3: Recoverable source links are not attached to formulation claims

minor / open / confirmed; issue key: CM009782-formulation-evidence-gap.

Exact source URLs survive only as notes and accession metadata. Neither layer attaches narrow evidence or bibliographic context to the eight quantities or preparation claims; the zero-check reference pass does not verify them.

## Recommended Actions And Acceptance Checks

### a1

Preserve 1 L distilled water as source preparation-volume context in the maintained owner. Do not infer water density, mass concentration or measured final volume; verify the current importer and regenerate only after owner correction.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain pH unadjusted and the exact JCM page-wide sterilization default with scoped evidence. Preserve the source wording and do not invent a numeric pH, incubation or storage condition.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Attach exact claim-level primary/provider evidence with original units, preparation stage, source type and actual access metadata; preserve append-only provenance and regenerate after owner verification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/6_b_medium__990e4708.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M39_6_B_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/6_b_medium__990e4708.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/6_b_medium__990e4708.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch012/112/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch012/112/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/6_b_medium__990e4708.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/6_b_medium__990e4708.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/6_b_medium__990e4708.yaml:1:id: CultureMech:009782<br>./data/normalized_yaml/bacterial/TOGO_M39_6_B_Medium.yaml:1:id: CultureMech:009782<br> |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15377 resolves to water and is not obsolete. Exact ontology-label metadata is verified; source material form and formulation are assessed separately. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17234 resolves to glucose and is not obsolete. Exact ontology-label metadata is verified; source material form and formulation are assessed separately. |
| chebi17754 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17754; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17754 resolves to glycerol and is not obsolete. Exact ontology-label metadata is verified; source material form and formulation are assessed separately. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:2509 resolves to agar and is not obsolete. Exact ontology-label metadata is verified; source material form and formulation are assessed separately. |
| chebi28017 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:28017 resolves to starch and is not obsolete. Exact ontology-label metadata is verified; source material form and formulation are assessed separately. |
| chebi3311 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3311; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:3311 resolves to calcium carbonate and is not obsolete. Exact ontology-label metadata is verified; source material form and formulation are assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3311": [{"label": "CaCO3", "match_type": "preferred_term", "identifier": "CHEBI:3311", "preferred_term": "CaCO3", "ontology_id": "CHEBI:3311", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17754": [{"label": "Glycerol", "match_type": "preferred_term", "identifier": "CHEBI:17754", "preferred_term": "Glycerol", "ontology_id": "CHEBI:17754", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M39; $.meta; $.components[0].items[0:8]; $.comments[0] | supports | TOGO M39 explicitly identifies JCM_M47 and its original URL. Eight rows retain water 1 L, CaCO3 1 g, glycerol 50 g, glucose 10 g, soluble starch 20 g, agar 15 g, BD-Difco yeast extract 5 g and Sheffield N-Z amine type A 5 g. The comment says pH unadjusted. |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=47; JCM 47 entire composition, pH text and shared sterilization instruction | supports | The exact original JCM page independently confirms all eight component amounts and material qualifiers, unadjusted pH, and the default autoclaving requirement of 121 C for 15 min unless otherwise stated. |
| mediadive | https://mediadive.dsmz.de/rest/medium/J47; $.data.medium; $.data.solutions[0] | supports | MediaDive J47 explicitly links JCM 47. It separately reports seven solute g/L values on provider volume 1000 ml and water 1000 ml. Supplier/material attributes remain separate fields; this provider view is not an independent measurement of final volume. |
| quantities | /private/tmp/culturemech-review-work-batch012/112/quantity-inventory.json; All eight target/owner quantity fields against original source units and exact provider rows | context_only | Eight explicit decisions: seven solute values have source/provider support; the water entry is dimensionally wrong. Original units and the preparation-volume boundary are preserved. |
| writer | src/culturemech/import/togo_importer.py; _ingredient_from_item; _parse_unit; _extract_preparation_steps | context_only | Current code recognizes source L separately from G_PER_L and retains nonempty source comments as preparation steps. It was inspected only; this does not reconstruct which historical implementation produced the current wrong water unit or omitted comment. |

## Limits And Additional Notes

- JCM specifies nominal masses with 1 L distilled water. MediaDive J47 independently reports a 1000 ml solution and g/L fields; this supports the provider normalization, not a measured final volume or a water-density conversion.
- No stock formulation, organism-specific growth, incubation optimum, molarity for undefined ingredients or supplier equivalence is inferred. The reviewed target is CM009782; the separate MediaDive-derived CM002829 record is not another reviewed target.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T085220Z-culturemech-009782-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 6_b_medium (CultureMech:009782)'
started_at: '2026-10-21T08:48:56Z'
finished_at: '2026-10-21T08:52:20Z'
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
summary: The seven non-water amounts and ingredient identities agree with TOGO M39
  and JCM 47, but both layers turn the source 1 L of distilled water into 1 g/L. The
  unadjusted-pH instruction and primary sterilization default are absent, and no narrow
  formulation evidence or reference has been attached.
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
  - path: data/merge_yaml/merged/6_b_medium__990e4708.yaml
    sha256: aa5719da79004a9810e62abd2b9bcfe51ce3f3d77102641244fce1dc220c0dee
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M39_6_B_Medium.yaml
    sha256: cd251550fd1340605b2b14422f6e812afee2b086b835a2912603600528e68bf7
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
  selection: Task review 112; batch 012 item 2 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding eleven task batches contain
    110 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 112 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009782
targets:
- target_id: CultureMech:009782
  path: data/merge_yaml/merged/6_b_medium__990e4708.yaml
  label: 6_b_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M39_6_B_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/6_b_medium__990e4708.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009782
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/6_b_medium__990e4708.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch012/112/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch012/112/strict.tsv"
  target_ids:
  - CultureMech:009782
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/6_b_medium__990e4708.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009782
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/6_b_medium__990e4708.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009782
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
  - CultureMech:009782
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/6_b_medium__990e4708.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T08:52:19Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M39_6_B_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T08:52:19Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/6_b_medium__990e4708.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:49:36.420124Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/6_b_medium__990e4708.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch012/112/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T08:49:37.964821Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-012/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch012/112/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/6_b_medium__990e4708.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:49:39.652383Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/6_b_medium__990e4708.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:49:40.728090Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T08:52:19Z'
  support: supports
  summary: './data/merge_yaml/merged/6_b_medium__990e4708.yaml:1:id: CultureMech:009782

    ./data/normalized_yaml/bacterial/TOGO_M39_6_B_Medium.yaml:1:id: CultureMech:009782

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:42:30.346522Z'
  support: supports
  summary: CHEBI:15377 resolves to water and is not obsolete. Exact ontology-label
    metadata is verified; source material form and formulation are assessed separately.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:42:31.535358Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose and is not obsolete. Exact ontology-label
    metadata is verified; source material form and formulation are assessed separately.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi17754
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17754
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:42:35.442871Z'
  support: supports
  summary: CHEBI:17754 resolves to glycerol and is not obsolete. Exact ontology-label
    metadata is verified; source material form and formulation are assessed separately.
  snapshot_sha256: 0231975176416cbaad3ad04c9efeedbe9bef0b826645e592a4a2f511e8d1db95
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:42:37.629610Z'
  support: supports
  summary: CHEBI:2509 resolves to agar and is not obsolete. Exact ontology-label metadata
    is verified; source material form and formulation are assessed separately.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi28017
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:42:42.748724Z'
  support: supports
  summary: CHEBI:28017 resolves to starch and is not obsolete. Exact ontology-label
    metadata is verified; source material form and formulation are assessed separately.
  snapshot_sha256: 959b4330165a7ff12d2e464f4a7b44e148376624d04cf7764b6a8671c1c99204
- evidence_id: chebi3311
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3311
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:42:45.903210Z'
  support: supports
  summary: CHEBI:3311 resolves to calcium carbonate and is not obsolete. Exact ontology-label
    metadata is verified; source material form and formulation are assessed separately.
  snapshot_sha256: 5413cec912ec253d62ba7a3f4ce7f0a9312ba8d1cb756713003f77a6e849d4b2
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T08:52:19Z'
  support: supports
  summary: '{"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3311":
    [{"label": "CaCO3", "match_type": "preferred_term", "identifier": "CHEBI:3311",
    "preferred_term": "CaCO3", "ontology_id": "CHEBI:3311", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17754": [{"label": "Glycerol", "match_type": "preferred_term",
    "identifier": "CHEBI:17754", "preferred_term": "Glycerol", "ontology_id": "CHEBI:17754",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label":
    "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term":
    "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M39
  locator: $.meta; $.components[0].items[0:8]; $.comments[0]
  accessed_at: '2026-10-21T08:42:29.769045Z'
  support: supports
  summary: TOGO M39 explicitly identifies JCM_M47 and its original URL. Eight rows
    retain water 1 L, CaCO3 1 g, glycerol 50 g, glucose 10 g, soluble starch 20 g,
    agar 15 g, BD-Difco yeast extract 5 g and Sheffield N-Z amine type A 5 g. The
    comment says pH unadjusted.
  snapshot_sha256: 92a6425322fe40baef9db697368c06d77bebed6b44a57be073ecb8be26e12fc6
- evidence_id: jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=47
  locator: JCM 47 entire composition, pH text and shared sterilization instruction
  accessed_at: '2026-10-21T08:43:25.576837Z'
  support: supports
  summary: The exact original JCM page independently confirms all eight component
    amounts and material qualifiers, unadjusted pH, and the default autoclaving requirement
    of 121 C for 15 min unless otherwise stated.
  snapshot_sha256: 2e4fdba2a6199af856888505dcc744bcf5094e88f09000755c1e48874e4df73a
- evidence_id: mediadive
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J47
  locator: $.data.medium; $.data.solutions[0]
  accessed_at: '2026-10-21T08:42:27.862338Z'
  support: supports
  summary: MediaDive J47 explicitly links JCM 47. It separately reports seven solute
    g/L values on provider volume 1000 ml and water 1000 ml. Supplier/material attributes
    remain separate fields; this provider view is not an independent measurement of
    final volume.
  snapshot_sha256: 09e2d1296555fcfa80f1c1d51702b2e1684dcdacc51bffc09e8e034002399b2d
- evidence_id: quantities
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch012/112/quantity-inventory.json
  locator: All eight target/owner quantity fields against original source units and
    exact provider rows
  accessed_at: '2026-10-21T08:52:19Z'
  support: context_only
  summary: 'Eight explicit decisions: seven solute values have source/provider support;
    the water entry is dimensionally wrong. Original units and the preparation-volume
    boundary are preserved.'
  snapshot_sha256: b78eb24b5829018dd17b09b6b17905258bb9b3f9ed179c3ae9fda34d5dd67f49
- evidence_id: writer
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item; _parse_unit; _extract_preparation_steps
  accessed_at: '2026-10-21T08:52:19Z'
  support: context_only
  summary: Current code recognizes source L separately from G_PER_L and retains nonempty
    source comments as preparation steps. It was inspected only; this does not reconstruct
    which historical implementation produced the current wrong water unit or omitted
    comment.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009782
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
  - CultureMech:009782
  evidence_ids:
  - record
  - mim
  - chebi15377
  - chebi17234
  - chebi17754
  - chebi2509
  - chebi28017
  - chebi3311
  details: 8 direct ingredient instances; CHEBI-primary instance linkage 6/8 (75.00%),
    verified secondary coverage 5/8 (62.50%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Single target and exact original recipe accession
  outcome: supported
  summary: CM009782 resolves to one maintained TOGO M39 owner and one generated target.
    The explicit source metadata maps M39 to JCM 47; name similarity alone is not
    used. MediaDive J47 is a separate dataset representation of that explicitly linked
    source.
  target_ids:
  - CultureMech:009782
  evidence_ids:
  - record
  - owner-0
  - id-search
  - togo
  - jcm
  - mediadive
- assessment_id: amounts
  area: quantity
  topic: Every concentration and original source unit
  outcome: concern
  summary: Seven non-water values match the primary masses and provider-declared concentrations.
    Water 1 L has been changed into 1 g/L in both layers; no dimensional conversion
    supports that representation. All eight fields, including stock/final-volume boundaries,
    are documented individually.
  target_ids:
  - CultureMech:009782
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  - mediadive
  - quantities
  details: '[{"field_path": "ingredients[0].concentration", "ingredient": "Distilled
    water", "target_and_owner_value": {"value": "1", "unit": "G_PER_L"}, "source_key":
    "togoM39api", "source_locator": "$.components[0].items[0]", "original_amount":
    1, "original_unit": "L", "provider_source_locator": "$.data.solutions[0].recipe[7]",
    "provider_volume_ml": 1000, "provider_g_l": null, "stage": "main-medium preparation,
    not stock or assay", "decision": "correct", "explanation": "The source amount
    is a 1 L preparation solvent volume, not 1 g/L. Preserve the volume in preparation
    context without inferring density, water mass or measured final volume."}, {"field_path":
    "ingredients[1].concentration", "ingredient": "CaCO3", "target_and_owner_value":
    {"value": "1", "unit": "G_PER_L"}, "source_key": "togoM39api", "source_locator":
    "$.components[0].items[1]", "original_amount": 1, "original_unit": "g", "provider_source_locator":
    "$.data.solutions[0].recipe[5]", "provider_volume_ml": 1000, "provider_g_l": 1,
    "stage": "main-medium preparation, not stock or assay", "decision": "verified",
    "explanation": "The source mass is retained nominally with 1 L water, and the
    exact MediaDive J47 representation independently reports this g/L number on its
    declared 1000 ml basis. No measured final volume or stock dilution is inferred."},
    {"field_path": "ingredients[2].concentration", "ingredient": "Glycerol", "target_and_owner_value":
    {"value": "50", "unit": "G_PER_L"}, "source_key": "togoM39api", "source_locator":
    "$.components[0].items[2]", "original_amount": 50, "original_unit": "g", "provider_source_locator":
    "$.data.solutions[0].recipe[1]", "provider_volume_ml": 1000, "provider_g_l": 50,
    "stage": "main-medium preparation, not stock or assay", "decision": "verified",
    "explanation": "The source mass is retained nominally with 1 L water, and the
    exact MediaDive J47 representation independently reports this g/L number on its
    declared 1000 ml basis. No measured final volume or stock dilution is inferred."},
    {"field_path": "ingredients[3].concentration", "ingredient": "Glucose", "target_and_owner_value":
    {"value": "10", "unit": "G_PER_L"}, "source_key": "togoM39api", "source_locator":
    "$.components[0].items[3]", "original_amount": 10, "original_unit": "g", "provider_source_locator":
    "$.data.solutions[0].recipe[3]", "provider_volume_ml": 1000, "provider_g_l": 10,
    "stage": "main-medium preparation, not stock or assay", "decision": "verified",
    "explanation": "The source mass is retained nominally with 1 L water, and the
    exact MediaDive J47 representation independently reports this g/L number on its
    declared 1000 ml basis. No measured final volume or stock dilution is inferred."},
    {"field_path": "ingredients[4].concentration", "ingredient": "Soluble starch",
    "target_and_owner_value": {"value": "20", "unit": "G_PER_L"}, "source_key": "togoM39api",
    "source_locator": "$.components[0].items[4]", "original_amount": 20, "original_unit":
    "g", "provider_source_locator": "$.data.solutions[0].recipe[4]", "provider_volume_ml":
    1000, "provider_g_l": 20, "stage": "main-medium preparation, not stock or assay",
    "decision": "verified", "explanation": "The source mass is retained nominally
    with 1 L water, and the exact MediaDive J47 representation independently reports
    this g/L number on its declared 1000 ml basis. No measured final volume or stock
    dilution is inferred."}, {"field_path": "ingredients[5].concentration", "ingredient":
    "Agar", "target_and_owner_value": {"value": "15", "unit": "G_PER_L"}, "source_key":
    "togoM39api", "source_locator": "$.components[0].items[5]", "original_amount":
    15, "original_unit": "g", "provider_source_locator": "$.data.solutions[0].recipe[6]",
    "provider_volume_ml": 1000, "provider_g_l": 15, "stage": "main-medium preparation,
    not stock or assay", "decision": "verified", "explanation": "The source mass is
    retained nominally with 1 L water, and the exact MediaDive J47 representation
    independently reports this g/L number on its declared 1000 ml basis. No measured
    final volume or stock dilution is inferred."}, {"field_path": "ingredients[6].concentration",
    "ingredient": "Yeast extract (BD-Difco)", "target_and_owner_value": {"value":
    "5", "unit": "G_PER_L"}, "source_key": "togoM39api", "source_locator": "$.components[0].items[6]",
    "original_amount": 5, "original_unit": "g", "provider_source_locator": "$.data.solutions[0].recipe[0]",
    "provider_volume_ml": 1000, "provider_g_l": 5, "stage": "main-medium preparation,
    not stock or assay", "decision": "verified", "explanation": "The source mass is
    retained nominally with 1 L water, and the exact MediaDive J47 representation
    independently reports this g/L number on its declared 1000 ml basis. No measured
    final volume or stock dilution is inferred."}, {"field_path": "ingredients[7].concentration",
    "ingredient": "N--Z amine, type A (Sheffield)", "target_and_owner_value": {"value":
    "5", "unit": "G_PER_L"}, "source_key": "togoM39api", "source_locator": "$.components[0].items[7]",
    "original_amount": 5, "original_unit": "g", "provider_source_locator": "$.data.solutions[0].recipe[2]",
    "provider_volume_ml": 1000, "provider_g_l": 5, "stage": "main-medium preparation,
    not stock or assay", "decision": "verified", "explanation": "The source mass is
    retained nominally with 1 L water, and the exact MediaDive J47 representation
    independently reports this g/L number on its declared 1000 ml basis. No measured
    final volume or stock dilution is inferred."}]'
- assessment_id: forms
  area: grounding
  topic: Exact source materials versus ontology metadata
  outcome: supported
  summary: Source soluble starch is explicitly retained in the ingredient name while
    CHEBI gives the generic starch class. BD-Difco yeast extract and Sheffield N-Z
    amine type A qualifiers are retained. Glycerol, glucose without an added stereochemical
    restriction, calcium carbonate and agar match the stated source materials; water
    identity is valid even though its unit is wrong. Six primary CHEBI IDs and five
    current secondary keys are separately checked; undefined mixtures are not assigned
    invented molecules.
  target_ids:
  - CultureMech:009782
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  - mim
  - chebi15377
  - chebi3311
  - chebi17754
  - chebi17234
  - chebi28017
  - chebi2509
- assessment_id: preparation
  area: completeness
  topic: Source pH instruction and sterilization default
  outcome: concern
  summary: Both layers lack preparation steps. JCM and TOGO retain pH unadjusted,
    which is not a numeric pH target. The JCM page also supplies a default 121 C for
    15 min autoclaving requirement; no recipe-specific exception is stated. No extra
    incubation, storage or cooling conditions are inferred.
  target_ids:
  - CultureMech:009782
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - writer
- assessment_id: classification
  area: scope
  topic: Physical state, complex ingredients and organism scope
  outcome: supported
  summary: The source agar addition supports solid-agar classification, and yeast
    extract/N-Z amine support complex undefined composition. Neither layer asserts
    stocks, variants, parent relationships, KG correspondence or organism-specific
    growth. Bacterial filing and a generic cultivation application are not strain-level
    evidence.
  target_ids:
  - CultureMech:009782
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
- assessment_id: provenance
  area: evidence
  topic: Recoverable source links versus claim-level evidence
  outcome: concern
  summary: Notes and media_term preserve exact TOGO/JCM source identity, but neither
    layer has a bibliography or narrow ingredient/preparation evidence. The reference
    diagnostic performed zero checks. Evidence should retain catalogue/dataset type,
    actual access time, exact source locator and missing author/year metadata without
    inventing a publication.
  target_ids:
  - CultureMech:009782
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  - mediadive
  - validate-references
- assessment_id: history
  area: provenance
  topic: Timezone-aware events and generated ownership
  outcome: supported
  summary: All 8 target and 7 owner timestamps parse with timezones. The generated
    record preserves the seven owner events and appends its August merge event. Current
    target ingredient content equals its maintained owner; no historical process was
    rerun and no event was rewritten.
  target_ids:
  - CultureMech:009782
  evidence_ids:
  - record
  - owner-0
findings:
- finding_id: f1
  issue_key: CM009782-water-volume-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: The source water volume is represented as a mass concentration
  description: Both target and owner encode distilled water as 1 G_PER_L, while exact
    TOGO M39 and JCM 47 specify 1 L water. The unit change is dimensionally unsupported;
    the valid water ontology term and schema pass do not correct it.
  target_ids:
  - CultureMech:009782
  field_paths:
  - ingredients[0].concentration
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  - mediadive
  - quantities
  - writer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M39_6_B_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CM009782-source-preparation-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Unadjusted pH and source sterilization were omitted
  description: The complex medium has no preparation steps in either layer. The source
    pH-unadjusted instruction and JCM default sterilization are available but absent,
    materially limiting faithful preparation. Native P3.4 is normalized to major for
    these source-supported omissions.
  target_ids:
  - CultureMech:009782
  field_paths:
  - preparation_steps
  - sterilization
  - notes
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - writer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M39_6_B_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: CM009782-formulation-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Recoverable source links are not attached to formulation claims
  description: Exact source URLs survive only as notes and accession metadata. Neither
    layer attaches narrow evidence or bibliographic context to the eight quantities
    or preparation claims; the zero-check reference pass does not verify them.
  target_ids:
  - CultureMech:009782
  field_paths:
  - ingredients[*].evidence
  - references
  - evidence
  - notes
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  - mediadive
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M39_6_B_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Preserve 1 L distilled water as source preparation-volume context in
    the maintained owner. Do not infer water density, mass concentration or measured
    final volume; verify the current importer and regenerate only after owner correction.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009782
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M39_6_B_Medium.yaml
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
  description: Retain pH unadjusted and the exact JCM page-wide sterilization default
    with scoped evidence. Preserve the source wording and do not invent a numeric
    pH, incubation or storage condition.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009782
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M39_6_B_Medium.yaml
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
  description: Attach exact claim-level primary/provider evidence with original units,
    preparation stage, source type and actual access metadata; preserve append-only
    provenance and regenerate after owner verification.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009782
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M39_6_B_Medium.yaml
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
- JCM specifies nominal masses with 1 L distilled water. MediaDive J47 independently
  reports a 1000 ml solution and g/L fields; this supports the provider normalization,
  not a measured final volume or a water-density conversion.
- No stock formulation, organism-specific growth, incubation optimum, molarity for
  undefined ingredients or supplier equivalence is inferred. The reviewed target is
  CM009782; the separate MediaDive-derived CM002829 record is not another reviewed
  target.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-012
- generated-medium
```
