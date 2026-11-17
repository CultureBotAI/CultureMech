# Source and formulation review: 1_10_sabourauds_agar (CultureMech:009437)

- Review: 20261020T040348Z-culturemech-009437-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-20T04:02:02Z
- Finished UTC: 2026-10-20T04:03:48Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The TOGO-derived target is JCM medium 35. All six non-water ingredient masses and their supplied chemical forms match the collection recipe. Water is incorrectly represented as 1 G_PER_L, while source pH adjustment and the collection default sterilization are omitted. Source-linked concentration evidence is absent in this owner and target. The similarly named MediaDive owner is contextual evidence, not an additional reviewed target.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 33 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009437 | data/merge_yaml/merged/1_10_sabourauds_agar.yaml | generated | 1_10_sabourauds_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009437 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009437 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/033/strict.tsv |
| validate-terms | passed | True | CultureMech:009437 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009437 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009437 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009437.

The four documented recipes completed; interpret the scope of each separately.

### Source accession and duplicate boundary

identity: supported. Targets: CultureMech:009437.

The selected target 009437 and its sole bacterial normalized owner resolve to TOGO M28 / JCM 35. The fungal MediaDive owner 010521 is a source-corresponding sibling, not a second target in this bundle.

All six non-water source components agree between provider routes. Differences in represented water, pH, evidence and linkage require reconciliation before any lossless consolidation. Do not merge merely from name similarity or copy the sibling’s midpoint as if the primary source had no range. The target has one merged_from entry; its fields reproduce its own owner rather than conflating these two records.

### ingredients[0].concentration (Distilled water)

quantity: concern. Targets: CultureMech:009437.

correct: 1 G_PER_L water is incompatible with the original 1 L water quantity.

The six source solute masses are glucose 4 g, peptone 1 g, KH2PO4 1.5 g, magnesium sulfate heptahydrate 1 g, sodium nitrate 1 g and agar 20 g. The API explicitly encodes those g_l values; no further tenfold reduction is justified by the name. Water is a source volume, not a guessed mass concentration. No stock addition or nested dilution is present.

### ingredients[1].concentration (MgSO4・7H2O)

quantity: supported. Targets: CultureMech:009437.

verified: 1 G_PER_L agrees with the source mass and explicit provider volume of 1000 mL.

The six source solute masses are glucose 4 g, peptone 1 g, KH2PO4 1.5 g, magnesium sulfate heptahydrate 1 g, sodium nitrate 1 g and agar 20 g. The API explicitly encodes those g_l values; no further tenfold reduction is justified by the name. Water is a source volume, not a guessed mass concentration. No stock addition or nested dilution is present.

### ingredients[2].concentration (KH2PO4)

quantity: supported. Targets: CultureMech:009437.

verified: 1.5 G_PER_L agrees with the source mass and explicit provider volume of 1000 mL.

The six source solute masses are glucose 4 g, peptone 1 g, KH2PO4 1.5 g, magnesium sulfate heptahydrate 1 g, sodium nitrate 1 g and agar 20 g. The API explicitly encodes those g_l values; no further tenfold reduction is justified by the name. Water is a source volume, not a guessed mass concentration. No stock addition or nested dilution is present.

### ingredients[3].concentration (NaNO3)

quantity: supported. Targets: CultureMech:009437.

verified: 1 G_PER_L agrees with the source mass and explicit provider volume of 1000 mL.

The six source solute masses are glucose 4 g, peptone 1 g, KH2PO4 1.5 g, magnesium sulfate heptahydrate 1 g, sodium nitrate 1 g and agar 20 g. The API explicitly encodes those g_l values; no further tenfold reduction is justified by the name. Water is a source volume, not a guessed mass concentration. No stock addition or nested dilution is present.

### ingredients[4].concentration (Glucose)

quantity: supported. Targets: CultureMech:009437.

verified: 4 G_PER_L agrees with the source mass and explicit provider volume of 1000 mL.

The six source solute masses are glucose 4 g, peptone 1 g, KH2PO4 1.5 g, magnesium sulfate heptahydrate 1 g, sodium nitrate 1 g and agar 20 g. The API explicitly encodes those g_l values; no further tenfold reduction is justified by the name. Water is a source volume, not a guessed mass concentration. No stock addition or nested dilution is present.

### ingredients[5].concentration (Agar)

quantity: supported. Targets: CultureMech:009437.

verified: 20 G_PER_L agrees with the source mass and explicit provider volume of 1000 mL.

The six source solute masses are glucose 4 g, peptone 1 g, KH2PO4 1.5 g, magnesium sulfate heptahydrate 1 g, sodium nitrate 1 g and agar 20 g. The API explicitly encodes those g_l values; no further tenfold reduction is justified by the name. Water is a source volume, not a guessed mass concentration. No stock addition or nested dilution is present.

### ingredients[6].concentration (Peptone)

quantity: supported. Targets: CultureMech:009437.

verified: 1 G_PER_L agrees with the source mass and explicit provider volume of 1000 mL.

The six source solute masses are glucose 4 g, peptone 1 g, KH2PO4 1.5 g, magnesium sulfate heptahydrate 1 g, sodium nitrate 1 g and agar 20 g. The API explicitly encodes those g_l values; no further tenfold reduction is justified by the name. Water is a source volume, not a guessed mass concentration. No stock addition or nested dilution is present.

### All supplied forms and asserted identifiers

grounding: supported. Targets: CultureMech:009437.

Six primary CHEBI IDs resolve with matching labels. Five secondary CHEBI keys have live MIM index rows. The magnesium heptahydrate is correctly grounded; absence of a secondary link on that row is not a wrong primary mapping.

Seven direct ingredient instances: 6/7 primary CHEBI coverage (85.71%) and 5/7 secondary MIM CHEBI coverage (71.43%), percentages on a 0–100 scale measuring linkage only. Peptone remains an undefined mixture without an invented pure-chemical identity. Generic glucose does not assert stereochemistry. Source KH2PO4 is the dihydrogen salt, not dipotassium hydrogen phosphate. No current legacy numeric MIM ID is asserted by this target. Historical curator text describes previous changes, not active identifiers.

### Source pH, preparation and physical state

completeness: concern. Targets: CultureMech:009437.

The source pH adjustment range and JCM page-default sterilization are omitted entirely from the target and its owner. SOLID_AGAR matches the required agar row.

Preserve the primary range rather than replacing it with the provider header midpoint. The source specifies no additional incubation, atmosphere, storage, light or vessel conditions. Do not infer any. G_PER_L mass normalization remains valid for a medium solidified with agar. No recipe-specific exception negates the collection default.

### Roles, classification and growth scope

scope: supported. Targets: CultureMech:009437.

COMPLEX/UNDEFINED is compatible with peptone and the provider annotation. Ingredient-role notes reproduce TOGO annotations; they are not experimental growth or mechanistic evidence.

No target organism, taxon identifier, DOI, PMID, growth result, role ontology CURIE or transcriptomic assertion is present. The bacterial filing category does not prove exclusive bacterial use or conflict with the similarly named fungal-filed sibling. No unreported growth claim is added.

### Evidence placement and history

evidence: concern. Targets: CultureMech:009437.

Source URLs, accession and complete history are recoverable, but no target/owner ingredient has scoped quantity evidence. The reference gate examined zero excerpts. The contextual sibling’s evidence cannot certify this target automatically.

Complete local target and both contextual owner files were read, not just projections. Absence of pH, preparation and evidence is bounded to these complete target/owner objects; no global absence is asserted. No discussion flags or stock references require resolution. Full ID/product/merge gates are follow-up acceptance checks, not executed during this read-only review.

## Findings

### f1: Water batch volume is encoded as a mass concentration

major / open / confirmed; issue key: culturemech-009437-water-unit-error.

Target and owner assert 1 G_PER_L distilled water where the original source specifies 1 L. No density conversion or source mass supports this unit.

### f2: Source pH range and default sterilization are missing

major / open / confirmed; issue key: culturemech-009437-source-conditions-omitted.

The JCM source states a pH adjustment range and a default sterilization instruction. Neither is present in the target or maintained owner. The provider midpoint does not replace the source range.

### f3: Quantity claims lack scoped supporting excerpts

minor / open / confirmed; issue key: culturemech-009437-concentration-evidence-gap.

All seven direct quantity assertions lack claim-level evidence in this owner/target. Six numerical concentrations are corroborated by explicit provider normalization; the water unit defect is separate.

## Recommended Actions And Acceptance Checks

### a1

Correct the maintained water representation to preserve original volume and batch basis in schema-supported fields; inspect the importer unit path, then regenerate derived output under separate curation authorization.

- Check the exact JCM 35 formulation and TOGO M28 source units and conditions.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references after maintained-input corrections.
- After separately authorized regeneration, run just verify-merges and just audit-merge-freshness and verify this target reflects its owner.

### a2

Preserve the source pH range and applicable collection default preparation in the maintained input with precise supporting evidence. Avoid additional inferred protocol steps.

- Check the exact JCM 35 formulation and TOGO M28 source units and conditions.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references after maintained-input corrections.
- After separately authorized regeneration, run just verify-merges and just audit-merge-freshness and verify this target reflects its owner.

### a3

Attach source-specific short excerpts and quantity/batch context in the maintained owner, preserving exact supplied forms and separating provider normalization from original water volume.

- Check the exact JCM 35 formulation and TOGO M28 source units and conditions.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references after maintained-input corrections.
- After separately authorized regeneration, run just verify-merges and just audit-merge-freshness and verify this target reflects its owner.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_10_sabourauds_agar.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_10_sabourauds_agar.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_10_sabourauds_agar.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch004/033/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/033/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_10_sabourauds_agar.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_10_sabourauds_agar.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=35; Entire medium 35 entry plus page default above it | supports | JCM 35 identifies the medium and specifies seven components, a pH range and a page-level default sterilization condition. The latter applies because this recipe states no alternative. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M28; meta; complete components[0].items; comments | supports | M28 resolves to JCM_M35 and its exact primary URL. Every component and original unit, pH metadata, adjustment comment and copied role/property annotation inspected. |
| api | https://mediadive.dsmz.de/rest/medium/J35; data.medium and complete data.solutions[0] | supports | J35 resolves to JCM 35. Main solution 3658 has volume 1000 mL, six explicit g_l entries, a water row and pH adjustment. Medium pH metadata uses 6.9 although the step retains the range. |
| bacmedia | https://bacmedia.dsmz.de/pdf/J35; Page 1, title, final-volume header, composition and adjustment | supports | The rendering identifies J35, gives explicit final volume 1000 mL, lists all seven ingredient amounts and preserves the pH adjustment range while its header gives 6.9. |
| sibling | data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml; Complete contextual maintained record, including all six evidence entries and history | context_only | Context owner CultureMech:010521 has the same source-specific six solute amounts and names J35. Its existing amount evidence does not automatically belong to the distinct TOGO target. It retains pH adjustment, unlike the target, but has its own scope limitations. |
| chebi-15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term: identifier, label, definition, obsolete flag and chemical annotation | supports | CHEBI:15377 = water; nonobsolete. Form checked against the ingredient label: water, heptahydrate, monopotassium dihydrogen phosphate, sodium nitrate, generic glucose or agar as applicable. No molarity or unstated hydrate is inferred. |
| chebi-31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS term: identifier, label, definition, obsolete flag and chemical annotation | supports | CHEBI:31795 = magnesium sulfate heptahydrate; nonobsolete. Form checked against the ingredient label: water, heptahydrate, monopotassium dihydrogen phosphate, sodium nitrate, generic glucose or agar as applicable. No molarity or unstated hydrate is inferred. |
| chebi-63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS term: identifier, label, definition, obsolete flag and chemical annotation | supports | CHEBI:63036 = potassium dihydrogen phosphate; nonobsolete. Form checked against the ingredient label: water, heptahydrate, monopotassium dihydrogen phosphate, sodium nitrate, generic glucose or agar as applicable. No molarity or unstated hydrate is inferred. |
| chebi-63005 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63005; Exact OLS term: identifier, label, definition, obsolete flag and chemical annotation | supports | CHEBI:63005 = sodium nitrate; nonobsolete. Form checked against the ingredient label: water, heptahydrate, monopotassium dihydrogen phosphate, sodium nitrate, generic glucose or agar as applicable. No molarity or unstated hydrate is inferred. |
| chebi-17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS term: identifier, label, definition, obsolete flag and chemical annotation | supports | CHEBI:17234 = glucose; nonobsolete. Form checked against the ingredient label: water, heptahydrate, monopotassium dihydrogen phosphate, sodium nitrate, generic glucose or agar as applicable. No molarity or unstated hydrate is inferred. |
| chebi-2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS term: identifier, label, definition, obsolete flag and chemical annotation | supports | CHEBI:2509 = agar; nonobsolete. Form checked against the ingredient label: water, heptahydrate, monopotassium dihydrogen phosphate, sodium nitrate, generic glucose or agar as applicable. No molarity or unstated hydrate is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for the five asserted secondary keys; metadata pinned in source inputs | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63005": [{"label": "NaNO3", "match_type": "preferred_term", "identifier": "CHEBI:63005", "preferred_term": "NaNO3", "ontology_id": "CHEBI:63005", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| ids | repository checkout; Whole-checkout exact top-level ID lookup | supports | ./data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml:1:id: CultureMech:010521<br>./data/merge_yaml/merged/1_10_sabourauds_agar.yaml:1:id: CultureMech:009437<br>./data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml:1:id: CultureMech:010521<br>./data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml:1:id: CultureMech:009437<br> |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The JCM page specifies the source water batch; the BacMedia rendering and MediaDive API independently supply a 1000 mL normalization volume. Provider-declared concentrations are not independently measured final volumes.
- The contextual MediaDive owner contains a historical MIM link requiring its own review. It is not asserted by this target and is not certified here.
- The TOGO HTML is only a JavaScript shell; the structured TOGO API and primary JCM page supply the inspected content.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T040348Z-culturemech-009437-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_10_sabourauds_agar (CultureMech:009437)'
started_at: '2026-10-20T04:02:02Z'
finished_at: '2026-10-20T04:03:48Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: The reviewer did not author or change these recipe bytes. This
    is an independent agent source review with deterministic diagnostics, not experimental
    verification.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The TOGO-derived target is JCM medium 35. All six non-water ingredient masses
  and their supplied chemical forms match the collection recipe. Water is incorrectly
  represented as 1 G_PER_L, while source pH adjustment and the collection default
  sterilization are omitted. Source-linked concentration evidence is absent in this
  owner and target. The similarly named MediaDive owner is contextual evidence, not
  an additional reviewed target.
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
  - path: data/merge_yaml/merged/1_10_sabourauds_agar.yaml
    sha256: 30ac3d89c5039124b5b67724fa221d86036c9c4b20c7f9407a7ee5fd6eb3e7d2
    role: target
  - path: data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml
    sha256: 95f60e7f47f5d288b7b2dc4feeaeec6ece9ab505dde09ca080192af2277afedb
    role: context
  - path: data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml
    sha256: 1f5ddfb7899c262e248e89912b7c2e78e8c6f0ccda5fa903a80b116c8c860515
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
  selection: Record 33 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009437
targets:
- target_id: CultureMech:009437
  path: data/merge_yaml/merged/1_10_sabourauds_agar.yaml
  label: 1_10_sabourauds_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_10_sabourauds_agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_10_sabourauds_agar.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch004/033/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/033/strict.tsv"
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_10_sabourauds_agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_10_sabourauds_agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009437
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
  - CultureMech:009437
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_10_sabourauds_agar.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-20T04:03:46Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T04:03:46Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_10_sabourauds_agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T04:02:04.892136Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_10_sabourauds_agar.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch004/033/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-20T04:02:06.076409Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/033/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_10_sabourauds_agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T04:02:08.036675Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_10_sabourauds_agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T04:02:08.961769Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: jcm
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=35
  locator: Entire medium 35 entry plus page default above it
  accessed_at: '2026-10-20T04:02:31.634174Z'
  support: supports
  summary: JCM 35 identifies the medium and specifies seven components, a pH range
    and a page-level default sterilization condition. The latter applies because this
    recipe states no alternative.
  quote: Adjust pH to 6.8-7.0.
  snapshot_sha256: eeaba7bc7ca708cf1a08321f2c3e46942ea17aea622b28287515a3eb53f41bf5
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M28
  locator: meta; complete components[0].items; comments
  accessed_at: '2026-10-20T04:02:33.126259Z'
  support: supports
  summary: M28 resolves to JCM_M35 and its exact primary URL. Every component and
    original unit, pH metadata, adjustment comment and copied role/property annotation
    inspected.
  snapshot_sha256: d339cc9771a6b674263da0d8f6a135d2d49aa6567ee8a3e327407f114b057b22
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J35
  locator: data.medium and complete data.solutions[0]
  accessed_at: '2026-10-20T04:02:33.781202Z'
  support: supports
  summary: J35 resolves to JCM 35. Main solution 3658 has volume 1000 mL, six explicit
    g_l entries, a water row and pH adjustment. Medium pH metadata uses 6.9 although
    the step retains the range.
  snapshot_sha256: c9db6996d60d6c0fe9b2b5fedc6b94baebf1daf35b0b26fa8280fc5045b25f27
- evidence_id: bacmedia
  kind: database
  reference: https://bacmedia.dsmz.de/pdf/J35
  locator: Page 1, title, final-volume header, composition and adjustment
  accessed_at: '2026-10-20T04:02:34.311188Z'
  support: supports
  summary: The rendering identifies J35, gives explicit final volume 1000 mL, lists
    all seven ingredient amounts and preserves the pH adjustment range while its header
    gives 6.9.
  quote: 'Final volume: 1000 ml'
  snapshot_sha256: 548719824d623168addd562310f09dfae0bd6d4ac0308dbe0af3efd8edef6daa
- evidence_id: sibling
  kind: record_content
  reference: data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml
  locator: Complete contextual maintained record, including all six evidence entries
    and history
  accessed_at: '2026-10-20T04:03:46Z'
  support: context_only
  summary: Context owner CultureMech:010521 has the same source-specific six solute
    amounts and names J35. Its existing amount evidence does not automatically belong
    to the distinct TOGO target. It retains pH adjustment, unlike the target, but
    has its own scope limitations.
- evidence_id: chebi-15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: 'Exact OLS term: identifier, label, definition, obsolete flag and chemical
    annotation'
  accessed_at: '2026-10-20T04:00:00.223561Z'
  support: supports
  summary: 'CHEBI:15377 = water; nonobsolete. Form checked against the ingredient
    label: water, heptahydrate, monopotassium dihydrogen phosphate, sodium nitrate,
    generic glucose or agar as applicable. No molarity or unstated hydrate is inferred.'
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi-31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: 'Exact OLS term: identifier, label, definition, obsolete flag and chemical
    annotation'
  accessed_at: '2026-10-20T03:57:34.006322Z'
  support: supports
  summary: 'CHEBI:31795 = magnesium sulfate heptahydrate; nonobsolete. Form checked
    against the ingredient label: water, heptahydrate, monopotassium dihydrogen phosphate,
    sodium nitrate, generic glucose or agar as applicable. No molarity or unstated
    hydrate is inferred.'
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi-63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: 'Exact OLS term: identifier, label, definition, obsolete flag and chemical
    annotation'
  accessed_at: '2026-10-20T04:02:35.727546Z'
  support: supports
  summary: 'CHEBI:63036 = potassium dihydrogen phosphate; nonobsolete. Form checked
    against the ingredient label: water, heptahydrate, monopotassium dihydrogen phosphate,
    sodium nitrate, generic glucose or agar as applicable. No molarity or unstated
    hydrate is inferred.'
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi-63005
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63005
  locator: 'Exact OLS term: identifier, label, definition, obsolete flag and chemical
    annotation'
  accessed_at: '2026-10-20T04:02:36.443517Z'
  support: supports
  summary: 'CHEBI:63005 = sodium nitrate; nonobsolete. Form checked against the ingredient
    label: water, heptahydrate, monopotassium dihydrogen phosphate, sodium nitrate,
    generic glucose or agar as applicable. No molarity or unstated hydrate is inferred.'
  snapshot_sha256: 1ec6a815a0e22ba0d12f84ad998bef39b9e6b80cf90c25cd1ab51903bbb54da3
- evidence_id: chebi-17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: 'Exact OLS term: identifier, label, definition, obsolete flag and chemical
    annotation'
  accessed_at: '2026-10-20T03:57:32.595833Z'
  support: supports
  summary: 'CHEBI:17234 = glucose; nonobsolete. Form checked against the ingredient
    label: water, heptahydrate, monopotassium dihydrogen phosphate, sodium nitrate,
    generic glucose or agar as applicable. No molarity or unstated hydrate is inferred.'
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi-2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: 'Exact OLS term: identifier, label, definition, obsolete flag and chemical
    annotation'
  accessed_at: '2026-10-20T03:57:34.697126Z'
  support: supports
  summary: 'CHEBI:2509 = agar; nonobsolete. Form checked against the ingredient label:
    water, heptahydrate, monopotassium dihydrogen phosphate, sodium nitrate, generic
    glucose or agar as applicable. No molarity or unstated hydrate is inferred.'
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for the five asserted secondary keys; metadata
    pinned in source inputs
  accessed_at: '2026-10-20T04:03:46Z'
  support: supports
  summary: '{"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036":
    [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036",
    "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:63005": [{"label": "NaNO3", "match_type": "preferred_term",
    "identifier": "CHEBI:63005", "preferred_term": "NaNO3", "ontology_id": "CHEBI:63005",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label":
    "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term":
    "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: ids
  kind: record_content
  reference: repository checkout
  locator: Whole-checkout exact top-level ID lookup
  accessed_at: '2026-10-20T04:03:46Z'
  support: supports
  summary: './data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml:1:id: CultureMech:010521

    ./data/merge_yaml/merged/1_10_sabourauds_agar.yaml:1:id: CultureMech:009437

    ./data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml:1:id: CultureMech:010521

    ./data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml:1:id: CultureMech:009437

    '
  search_scope: rg --no-ignore --hidden across all checkout files, including ignored
    files; maintained and generated layers distinguished.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Source accession and duplicate boundary
  outcome: supported
  summary: The selected target 009437 and its sole bacterial normalized owner resolve
    to TOGO M28 / JCM 35. The fungal MediaDive owner 010521 is a source-corresponding
    sibling, not a second target in this bundle.
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - api
  - sibling
  - ids
  details: All six non-water source components agree between provider routes. Differences
    in represented water, pH, evidence and linkage require reconciliation before any
    lossless consolidation. Do not merge merely from name similarity or copy the sibling’s
    midpoint as if the primary source had no range. The target has one merged_from
    entry; its fields reproduce its own owner rather than conflating these two records.
- assessment_id: quantity-0
  area: quantity
  topic: ingredients[0].concentration (Distilled water)
  outcome: concern
  summary: 'correct: 1 G_PER_L water is incompatible with the original 1 L water quantity.'
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - record
  - jcm
  - togo
  - api
  - bacmedia
  details: The six source solute masses are glucose 4 g, peptone 1 g, KH2PO4 1.5 g,
    magnesium sulfate heptahydrate 1 g, sodium nitrate 1 g and agar 20 g. The API
    explicitly encodes those g_l values; no further tenfold reduction is justified
    by the name. Water is a source volume, not a guessed mass concentration. No stock
    addition or nested dilution is present.
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact ingredient assertion, with provider volume
      distinguished from source water volume
    evidence_ids:
    - jcm
    - togo
    - api
    - bacmedia
- assessment_id: quantity-1
  area: quantity
  topic: ingredients[1].concentration (MgSO4・7H2O)
  outcome: supported
  summary: 'verified: 1 G_PER_L agrees with the source mass and explicit provider
    volume of 1000 mL.'
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - record
  - jcm
  - togo
  - api
  - bacmedia
  details: The six source solute masses are glucose 4 g, peptone 1 g, KH2PO4 1.5 g,
    magnesium sulfate heptahydrate 1 g, sodium nitrate 1 g and agar 20 g. The API
    explicitly encodes those g_l values; no further tenfold reduction is justified
    by the name. Water is a source volume, not a guessed mass concentration. No stock
    addition or nested dilution is present.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Decision for this exact ingredient assertion, with provider volume
      distinguished from source water volume
    evidence_ids:
    - jcm
    - togo
    - api
    - bacmedia
- assessment_id: quantity-2
  area: quantity
  topic: ingredients[2].concentration (KH2PO4)
  outcome: supported
  summary: 'verified: 1.5 G_PER_L agrees with the source mass and explicit provider
    volume of 1000 mL.'
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - record
  - jcm
  - togo
  - api
  - bacmedia
  details: The six source solute masses are glucose 4 g, peptone 1 g, KH2PO4 1.5 g,
    magnesium sulfate heptahydrate 1 g, sodium nitrate 1 g and agar 20 g. The API
    explicitly encodes those g_l values; no further tenfold reduction is justified
    by the name. Water is a source volume, not a guessed mass concentration. No stock
    addition or nested dilution is present.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Decision for this exact ingredient assertion, with provider volume
      distinguished from source water volume
    evidence_ids:
    - jcm
    - togo
    - api
    - bacmedia
- assessment_id: quantity-3
  area: quantity
  topic: ingredients[3].concentration (NaNO3)
  outcome: supported
  summary: 'verified: 1 G_PER_L agrees with the source mass and explicit provider
    volume of 1000 mL.'
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - record
  - jcm
  - togo
  - api
  - bacmedia
  details: The six source solute masses are glucose 4 g, peptone 1 g, KH2PO4 1.5 g,
    magnesium sulfate heptahydrate 1 g, sodium nitrate 1 g and agar 20 g. The API
    explicitly encodes those g_l values; no further tenfold reduction is justified
    by the name. Water is a source volume, not a guessed mass concentration. No stock
    addition or nested dilution is present.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Decision for this exact ingredient assertion, with provider volume
      distinguished from source water volume
    evidence_ids:
    - jcm
    - togo
    - api
    - bacmedia
- assessment_id: quantity-4
  area: quantity
  topic: ingredients[4].concentration (Glucose)
  outcome: supported
  summary: 'verified: 4 G_PER_L agrees with the source mass and explicit provider
    volume of 1000 mL.'
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - record
  - jcm
  - togo
  - api
  - bacmedia
  details: The six source solute masses are glucose 4 g, peptone 1 g, KH2PO4 1.5 g,
    magnesium sulfate heptahydrate 1 g, sodium nitrate 1 g and agar 20 g. The API
    explicitly encodes those g_l values; no further tenfold reduction is justified
    by the name. Water is a source volume, not a guessed mass concentration. No stock
    addition or nested dilution is present.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Decision for this exact ingredient assertion, with provider volume
      distinguished from source water volume
    evidence_ids:
    - jcm
    - togo
    - api
    - bacmedia
- assessment_id: quantity-5
  area: quantity
  topic: ingredients[5].concentration (Agar)
  outcome: supported
  summary: 'verified: 20 G_PER_L agrees with the source mass and explicit provider
    volume of 1000 mL.'
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - record
  - jcm
  - togo
  - api
  - bacmedia
  details: The six source solute masses are glucose 4 g, peptone 1 g, KH2PO4 1.5 g,
    magnesium sulfate heptahydrate 1 g, sodium nitrate 1 g and agar 20 g. The API
    explicitly encodes those g_l values; no further tenfold reduction is justified
    by the name. Water is a source volume, not a guessed mass concentration. No stock
    addition or nested dilution is present.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Decision for this exact ingredient assertion, with provider volume
      distinguished from source water volume
    evidence_ids:
    - jcm
    - togo
    - api
    - bacmedia
- assessment_id: quantity-6
  area: quantity
  topic: ingredients[6].concentration (Peptone)
  outcome: supported
  summary: 'verified: 1 G_PER_L agrees with the source mass and explicit provider
    volume of 1000 mL.'
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - record
  - jcm
  - togo
  - api
  - bacmedia
  details: The six source solute masses are glucose 4 g, peptone 1 g, KH2PO4 1.5 g,
    magnesium sulfate heptahydrate 1 g, sodium nitrate 1 g and agar 20 g. The API
    explicitly encodes those g_l values; no further tenfold reduction is justified
    by the name. Water is a source volume, not a guessed mass concentration. No stock
    addition or nested dilution is present.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Decision for this exact ingredient assertion, with provider volume
      distinguished from source water volume
    evidence_ids:
    - jcm
    - togo
    - api
    - bacmedia
- assessment_id: forms
  area: grounding
  topic: All supplied forms and asserted identifiers
  outcome: supported
  summary: Six primary CHEBI IDs resolve with matching labels. Five secondary CHEBI
    keys have live MIM index rows. The magnesium heptahydrate is correctly grounded;
    absence of a secondary link on that row is not a wrong primary mapping.
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - record
  - mim
  - chebi-15377
  - chebi-31795
  - chebi-63036
  - chebi-63005
  - chebi-17234
  - chebi-2509
  details: 'Seven direct ingredient instances: 6/7 primary CHEBI coverage (85.71%)
    and 5/7 secondary MIM CHEBI coverage (71.43%), percentages on a 0–100 scale measuring
    linkage only. Peptone remains an undefined mixture without an invented pure-chemical
    identity. Generic glucose does not assert stereochemistry. Source KH2PO4 is the
    dihydrogen salt, not dipotassium hydrogen phosphate. No current legacy numeric
    MIM ID is asserted by this target. Historical curator text describes previous
    changes, not active identifiers.'
- assessment_id: conditions
  area: completeness
  topic: Source pH, preparation and physical state
  outcome: concern
  summary: The source pH adjustment range and JCM page-default sterilization are omitted
    entirely from the target and its owner. SOLID_AGAR matches the required agar row.
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - api
  - bacmedia
  details: Preserve the primary range rather than replacing it with the provider header
    midpoint. The source specifies no additional incubation, atmosphere, storage,
    light or vessel conditions. Do not infer any. G_PER_L mass normalization remains
    valid for a medium solidified with agar. No recipe-specific exception negates
    the collection default.
- assessment_id: classification
  area: scope
  topic: Roles, classification and growth scope
  outcome: supported
  summary: COMPLEX/UNDEFINED is compatible with peptone and the provider annotation.
    Ingredient-role notes reproduce TOGO annotations; they are not experimental growth
    or mechanistic evidence.
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - record
  - togo
  - api
  details: No target organism, taxon identifier, DOI, PMID, growth result, role ontology
    CURIE or transcriptomic assertion is present. The bacterial filing category does
    not prove exclusive bacterial use or conflict with the similarly named fungal-filed
    sibling. No unreported growth claim is added.
- assessment_id: provenance
  area: evidence
  topic: Evidence placement and history
  outcome: concern
  summary: Source URLs, accession and complete history are recoverable, but no target/owner
    ingredient has scoped quantity evidence. The reference gate examined zero excerpts.
    The contextual sibling’s evidence cannot certify this target automatically.
  target_ids:
  - CultureMech:009437
  evidence_ids:
  - record
  - owner-0
  - validate-references
  - sibling
  - jcm
  details: Complete local target and both contextual owner files were read, not just
    projections. Absence of pH, preparation and evidence is bounded to these complete
    target/owner objects; no global absence is asserted. No discussion flags or stock
    references require resolution. Full ID/product/merge gates are follow-up acceptance
    checks, not executed during this read-only review.
findings:
- finding_id: f1
  issue_key: culturemech-009437-water-unit-error
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water batch volume is encoded as a mass concentration
  description: Target and owner assert 1 G_PER_L distilled water where the original
    source specifies 1 L. No density conversion or source mass supports this unit.
  target_ids:
  - CultureMech:009437
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: culturemech-009437-source-conditions-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source pH range and default sterilization are missing
  description: The JCM source states a pH adjustment range and a default sterilization
    instruction. Neither is present in the target or maintained owner. The provider
    midpoint does not replace the source range.
  target_ids:
  - CultureMech:009437
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
    path: data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: culturemech-009437-concentration-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Quantity claims lack scoped supporting excerpts
  description: All seven direct quantity assertions lack claim-level evidence in this
    owner/target. Six numerical concentrations are corroborated by explicit provider
    normalization; the water unit defect is separate.
  target_ids:
  - CultureMech:009437
  field_paths:
  - ingredients[*].evidence
  - references
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - api
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Correct the maintained water representation to preserve original volume
    and batch basis in schema-supported fields; inspect the importer unit path, then
    regenerate derived output under separate curation authorization.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009437
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Check the exact JCM 35 formulation and TOGO M28 source units and conditions.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    after maintained-input corrections.
  - After separately authorized regeneration, run just verify-merges and just audit-merge-freshness
    and verify this target reflects its owner.
- action_id: a2
  description: Preserve the source pH range and applicable collection default preparation
    in the maintained input with precise supporting evidence. Avoid additional inferred
    protocol steps.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009437
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Check the exact JCM 35 formulation and TOGO M28 source units and conditions.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    after maintained-input corrections.
  - After separately authorized regeneration, run just verify-merges and just audit-merge-freshness
    and verify this target reflects its owner.
- action_id: a3
  description: Attach source-specific short excerpts and quantity/batch context in
    the maintained owner, preserving exact supplied forms and separating provider
    normalization from original water volume.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009437
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Check the exact JCM 35 formulation and TOGO M28 source units and conditions.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    after maintained-input corrections.
  - After separately authorized regeneration, run just verify-merges and just audit-merge-freshness
    and verify this target reflects its owner.
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- The JCM page specifies the source water batch; the BacMedia rendering and MediaDive
  API independently supply a 1000 mL normalization volume. Provider-declared concentrations
  are not independently measured final volumes.
- The contextual MediaDive owner contains a historical MIM link requiring its own
  review. It is not asserted by this target and is not certified here.
- The TOGO HTML is only a JavaScript shell; the structured TOGO API and primary JCM
  page supply the inspected content.
tags:
- unreviewed-records
- batch-004
- generated-medium
```
