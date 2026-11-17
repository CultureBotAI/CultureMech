# Source and formulation review: 1_2_r2a_medium_with_75_artificial_seawater (CultureMech:010168)

- Review: 20261020T072533Z-culturemech-010168-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-20T07:24:07Z
- Finished UTC: 2026-10-20T07:25:33Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M761 correctly identifies JCM 736 and preserves the eight nutrient amounts and supplied forms. Its generated and maintained records flatten and duplicate the seawater stock, convert source liquid volumes to mass, combine water numerals from different stages, and omit the source preparation/pH context. Current extraction separates the dose but leaves the local stock composition empty.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 48 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 005 selects ordinals 41-50 after four validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010168 | data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml | generated | 1_2_r2a_medium_with_75_artificial_seawater |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010168 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010168 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-005/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch005/048/strict.tsv |
| validate-terms | passed | True | CultureMech:010168 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010168 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010168 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010168.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:010168.

16 primary CHEBI identities resolve with matching labels; 15 of 15 current secondary keys have live pinned-index rows. Unresolved keys: [].

20 direct ingredient instances; primary coverage 16/20 (80.00%), verified secondary coverage 15/20 (75.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Source identity and owner correspondence

identity: supported. Targets: CultureMech:010168.

CultureMech:010168 resolves through TOGO M761 to JCM 736. The entire target and single normalized owner agree in scientific content. Their shared source identity does not validate the altered stock representation.

### ingredients[0].concentration and source stage

quantity: concern. Targets: CultureMech:010168.

correct: 250 ml receiving-stage water and 1 L stock water were combined as bare numerals into 251 G_PER_L. This mixes preparation stages and incompatible units.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[1].concentration and source stage

quantity: supported. Targets: CultureMech:010168.

verified amount: MgSO4·7H2O 0.025 G_PER_L agrees with the source mass and nominal receiving-recipe basis; source supplier/form qualifiers are retained.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[2].concentration and source stage

quantity: supported. Targets: CultureMech:010168.

verified amount: K2HPO4 0.15 G_PER_L agrees with the source mass and nominal receiving-recipe basis; source supplier/form qualifiers are retained.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[3].concentration and source stage

quantity: supported. Targets: CultureMech:010168.

verified amount: Sodium pyruvate 0.15 G_PER_L agrees with the source mass and nominal receiving-recipe basis; source supplier/form qualifiers are retained.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[4].concentration and source stage

quantity: supported. Targets: CultureMech:010168.

verified amount: Glucose 0.25 G_PER_L agrees with the source mass and nominal receiving-recipe basis; source supplier/form qualifiers are retained.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[5].concentration and source stage

quantity: supported. Targets: CultureMech:010168.

verified amount: Soluble starch 0.25 G_PER_L agrees with the source mass and nominal receiving-recipe basis; source supplier/form qualifiers are retained.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[6].concentration and source stage

quantity: supported. Targets: CultureMech:010168.

verified amount: Yeast extract (BD-Difco) 0.25 G_PER_L agrees with the source mass and nominal receiving-recipe basis; source supplier/form qualifiers are retained.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[7].concentration and source stage

quantity: supported. Targets: CultureMech:010168.

verified amount: Proteose peptone No. 3 (BD-Difco) 0.25 G_PER_L agrees with the source mass and nominal receiving-recipe basis; source supplier/form qualifiers are retained.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[8].concentration and source stage

quantity: supported. Targets: CultureMech:010168.

verified amount: Casamino acids (BD-Difco) 0.25 G_PER_L agrees with the source mass and nominal receiving-recipe basis; source supplier/form qualifiers are retained.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[9].concentration and source stage

quantity: concern. Targets: CultureMech:010168.

correct: the source seawater addition is a liquid volume. It is represented as a direct ingredient mass concentration while its stock solutes are also expanded below.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[10].concentration and source stage

quantity: concern. Targets: CultureMech:010168.

correct scope: NaCl 23.5 G_PER_L is a stock-batch value, not a direct receiving-medium concentration. Unlike the volume rows, the stock mass units themselves agree with the source.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[11].concentration and source stage

quantity: concern. Targets: CultureMech:010168.

correct scope: CaCl2·2H2O 1.1 G_PER_L is a stock-batch value, not a direct receiving-medium concentration. Unlike the volume rows, the stock mass units themselves agree with the source.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[12].concentration and source stage

quantity: concern. Targets: CultureMech:010168.

correct scope: MgCl2·6H2O 4.9 G_PER_L is a stock-batch value, not a direct receiving-medium concentration. Unlike the volume rows, the stock mass units themselves agree with the source.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[13].concentration and source stage

quantity: concern. Targets: CultureMech:010168.

correct scope: H3BO3 0.026 G_PER_L is a stock-batch value, not a direct receiving-medium concentration. Unlike the volume rows, the stock mass units themselves agree with the source.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[14].concentration and source stage

quantity: concern. Targets: CultureMech:010168.

correct scope: KCl 0.66 G_PER_L is a stock-batch value, not a direct receiving-medium concentration. Unlike the volume rows, the stock mass units themselves agree with the source.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[15].concentration and source stage

quantity: concern. Targets: CultureMech:010168.

correct scope: NaHCO3 0.19 G_PER_L is a stock-batch value, not a direct receiving-medium concentration. Unlike the volume rows, the stock mass units themselves agree with the source.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[16].concentration and source stage

quantity: concern. Targets: CultureMech:010168.

correct scope: Na2SO4 3.9 G_PER_L is a stock-batch value, not a direct receiving-medium concentration. Unlike the volume rows, the stock mass units themselves agree with the source.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[17].concentration and source stage

quantity: concern. Targets: CultureMech:010168.

correct scope: SrCl2·6H2O 0.024 G_PER_L is a stock-batch value, not a direct receiving-medium concentration. Unlike the volume rows, the stock mass units themselves agree with the source.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[18].concentration and source stage

quantity: concern. Targets: CultureMech:010168.

correct scope: NaF 0.003 G_PER_L is a stock-batch value, not a direct receiving-medium concentration. Unlike the volume rows, the stock mass units themselves agree with the source.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### ingredients[19].concentration and source stage

quantity: concern. Targets: CultureMech:010168.

correct scope: KBr 0.096 G_PER_L is a stock-batch value, not a direct receiving-medium concentration. Unlike the volume rows, the stock mass units themselves agree with the source.

All twenty assertions individually traced. No density conversion, hydration change or new final stock concentration is inferred.

### Stock boundary and current process

consistency: concern. Targets: CultureMech:010168.

The stock addition and ten stock solutes appear together as direct ingredients. Current bounded parsing separates nine main rows and one volume-valued stock addition, and retains the preparation comment, but returns empty stock composition. Regeneration/import alone is not established as a complete repair.

### Source preparation and pH scope

completeness: concern. Targets: CultureMech:010168.

The source specifies separate preparation and later combination, with pH adjustment before the seawater addition. Target and owner retain neither the preparation steps nor this pH context. A provider-wide pH header should not replace the primary source stage.

### Supplied forms and chemical identities

grounding: supported. Targets: CultureMech:010168.

Supplier-qualified nutrients and soluble starch are retained. Generic starch grounding is compatible with that separate supplied-form qualifier. The explicit magnesium sulfate, magnesium chloride, calcium chloride and strontium chloride hydrate labels agree with the source; generic glucose is not narrowed to a stereoisomer. Ontology existence does not certify the amount/stage claims.

### Physical state, role annotations and growth claims

scope: supported. Targets: CultureMech:010168.

No source gelling component supports LIQUID, and complex nutrient mixtures support COMPLEX/UNDEFINED. Imported role/property notes match the TOGO rows, but do not establish organism-specific mechanisms or growth. No taxon, DOI, PMID, strain, incubation or storage assertion is made.

### Source support and history

evidence: concern. Targets: CultureMech:010168.

No amount evidence is attached to the twenty direct claims in target or owner. Import and duplicate-cleanup history explain provenance but do not justify combining stocks or volumes. Reference validation examined zero excerpts.

## Findings

### f1: Seawater stock and its components are duplicated as direct ingredients

blocker / open / confirmed; issue key: CM010168-seawater-stock-flattened.

The stock addition and its ten-solute formulation appear in one direct ingredient list, obscuring the receiving-medium boundary and changing the meaning of the source recipe. Current preview keeps the addition separate but loses its local composition.

### f2: Liquid volumes became masses and water stages were combined

major / open / confirmed; issue key: CM010168-liquid-volume-units.

Both stock-addition volume and main/stock water volumes are encoded as G_PER_L; incompatible water numerals were summed. Source grams for stock solutes are separate from these liquid-unit errors.

### f3: Source preparation and pH stage are omitted

major / open / confirmed; issue key: CM010168-preparation-ph-scope.

Both inspected sources retain the preparation sequence and stage-specific pH adjustment; the local records have no preparation or pH fields.

### f4: Claims lack evidence for units and stage

minor / open / confirmed; issue key: CM010168-stage-evidence-gap.

All twenty claims lack evidence objects, preventing source-stage distinctions from being recovered at the asserted fields.

## Recommended Actions And Acceptance Checks

### a1

Restore separate main and source-defined stock representations in the normalized owner, retaining the exact composition once. Resolve the local stock-section matching gap demonstrated by the empty-composition preview before relying on the importer. Regenerate only after verification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore original liquid units and preparation-stage/batch context without using a density assumption. Keep stock water separate from receiving-medium water and do not infer a measured final volume.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Retain exact source preparation and pH scope with evidence, avoiding an unsupported measured-final-pH assertion.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach narrow evidence to the corrected main ingredients and stock addition/composition; preserve provenance through regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch005/048/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-005/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch005/048/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml:1:id: CultureMech:010168<br>./data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml:1:id: CultureMech:010168<br> |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15377 resolves to water and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17234 resolves to glucose and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi28017 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:28017 resolves to starch and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi28741 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28741; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:28741 resolves to sodium fluoride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32030 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32030; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32030 resolves to potassium bromide and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32139 resolves to sodium hydrogencarbonate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32149 resolves to sodium sulfate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32588 resolves to potassium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:33118 resolves to boric acid and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi36385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_36385; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:36385 resolves to strontium dichloride hexahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:50144 resolves to sodium pyruvate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86158 resolves to calcium chloride dihydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:36385": [{"label": "SrCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:36385", "preferred_term": "SrCl2 x 6 H2O", "ontology_id": "CHEBI:36385", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:28741": [{"label": "NaF", "match_type": "preferred_term", "identifier": "CHEBI:28741", "preferred_term": "NaF", "ontology_id": "CHEBI:28741", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32030": [{"label": "KBr", "match_type": "preferred_term", "identifier": "CHEBI:32030", "preferred_term": "KBr", "ontology_id": "CHEBI:32030", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M761; meta; components[0:2]; comments[0] | supports | Complete two-section source, metadata and preparation comment inspected; main additions and seawater stock remain distinct in the provider. |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=736; GRMD 736 complete formula and preparation paragraph | supports | Collection original supports the TOGO identity, supplied forms, source preparation and distinct stock composition. |
| api | https://mediadive.dsmz.de/rest/medium/J736; data.medium and data.solutions[0:2] | supports | Independent provider representation separates main solution 4666 and seawater stock 4667; numeric comparison is scoped by stage. |
| render | https://bacmedia.dsmz.de/pdf/J736; Page 1 complete recipe and headings | supports | Rendering retains stock separation and a declared volume basis, but its final-pH label abbreviates the collection preparation context. |
| trace | src/culturemech/import/togo_importer.py; Exact input-row trace and bounded primary-component/preparation parsing | supports | {"accessed_at": "2026-10-20T07:24:46.026444+00:00", "amount_trace": [{"index": 0, "name": "Distilled water", "source_rows": [{"section": 0, "amount": 250, "unit": "ml"}, {"section": 1, "amount": 1, "unit": "L"}], "error": "Different-stage water numerals combined with incompatible units."}, {"index": 1, "name": "MgSO4\u00b77H2O", "section": 0, "amount": 0.025, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 2, "name": "K2HPO4", "section": 0, "amount": 0.15, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 3, "name": "Sodium pyruvate", "section": 0, "amount": 0.15, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 4, "name": "Glucose", "section": 0, "amount": 0.25, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 5, "name": "Soluble starch", "section": 0, "amount": 0.25, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 6, "name": "Yeast extract (BD-Difco)", "section": 0, "amount": 0.25, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 7, "name": "Proteose peptone No. 3 (BD-Difco)", "section": 0, "amount": 0.25, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 8, "name": "Casamino acids (BD-Difco)", "section": 0, "amount": 0.25, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 9, "name": "Artificial seawater (see below)", "section": 0, "amount": 750, "unit": "ml", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 10, "name": "NaCl", "section": 1, "amount": 23.5, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 11, "name": "CaCl2\u00b72H2O", "section": 1, "amount": 1.1, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 12, "name": "MgCl2\u00b76H2O", "section": 1, "amount": 4.9, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 13, "name": "H3BO3", "section": 1, "amount": 0.026, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 14, "name": "KCl", "section": 1, "amount": 0.66, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 15, "name": "NaHCO3", "section": 1, "amount": 0.19, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 16, "name": "Na2SO4", "section": 1, "amount": 3.9, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 17, "name": "SrCl2\u00b76H2O", "section": 1, "amount": 0.024, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 18, "name": "NaF", "section": 1, "amount": 0.003, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 19, "name": "KBr", "section": 1, "amount": 0.096, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}], "parser_preview": {"scope": "In-memory primary-section extraction and preparation parsing; no importer write methods called.", "ingredients": [{"preferred_term": "Distilled water", "concentration": {"value": "250", "unit": "ML_PER_L"}, "notes": "Role: Solvating media; Properties: Inorganic compound, Defined component, Simple component"}, {"preferred_term": "MgSO4\u00b77H2O", "concentration": {"value": "0.025", "unit": "G_PER_L"}, "notes": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component"}, {"preferred_term": "K2HPO4", "concentration": {"value": "0.15", "unit": "G_PER_L"}, "notes": "Role: Buffer; Properties: Inorganic compound, Defined component, Simple component"}, {"preferred_term": "Sodium pyruvate", "concentration": {"value": "0.15", "unit": "G_PER_L"}, "notes": "Role: Carbon source; Properties: Organic compound, Defined component, Simple component"}, {"preferred_term": "Glucose", "concentration": {"value": "0.25", "unit": "G_PER_L"}, "notes": "Role: Carbon source; Properties: Organic compound, Defined component, Simple component"}, {"preferred_term": "Soluble starch", "concentration": {"value": "0.25", "unit": "G_PER_L"}, "notes": "Role: Carbon source; Properties: Undefined component"}, {"preferred_term": "Yeast extract (BD-Difco)", "concentration": {"value": "0.25", "unit": "G_PER_L"}, "notes": "Properties: Undefined component"}, {"preferred_term": "Proteose peptone No. 3 (BD-Difco)", "concentration": {"value": "0.25", "unit": "G_PER_L"}, "notes": "Properties: Undefined component"}, {"preferred_term": "Casamino acids (BD-Difco)", "concentration": {"value": "0.25", "unit": "G_PER_L"}, "notes": "Properties: Undefined component"}], "solutions": [{"preferred_term": "Artificial seawater (see below)", "composition": [], "concentration": {"value": "750", "unit": "ML_PER_L"}, "notes": "Defined in TOGO medium M761."}], "preparation": [{"step_number": 1, "action": "AUTOCLAVE", "description": "Mix components except artificial seawater, adjust pH to 7.2, and autoclave. Separately autoclave artificial seawater. After cooling, combine the two solutions."}]}} |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The receiving-medium basis is provider-declared, not physically measured; no new final stock concentrations are calculated.
- Current parser checks are bounded in-memory diagnostics, not full importer execution or corpus validation. Reused primary captures retain their original access timestamps and were inspected for this distinct target.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T072533Z-culturemech-010168-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_2_r2a_medium_with_75_artificial_seawater
  (CultureMech:010168)'
started_at: '2026-10-20T07:24:07Z'
finished_at: '2026-10-20T07:25:33Z'
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
summary: TOGO M761 correctly identifies JCM 736 and preserves the eight nutrient amounts
  and supplied forms. Its generated and maintained records flatten and duplicate the
  seawater stock, convert source liquid volumes to mass, combine water numerals from
  different stages, and omit the source preparation/pH context. Current extraction
  separates the dose but leaves the local stock composition empty.
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
  - path: data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml
    sha256: 919eab78e7f4378effbfd3ce6cf84e36f7af4897f372316995f8fa3b37d2c092
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml
    sha256: 9cc95f22e0caf3417290fefb7fb6090b9907876900d1e91a8b9c0967c2592fd0
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
  - path: src/culturemech/convert/mediadive_raw_yaml.py
    sha256: 70ba720001705c315f2c5bd40871e08f6f429b6229c78255e6c94dfdcc482432
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
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
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
  selection: Record 48 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 005 selects ordinals 41-50 after four
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010168
targets:
- target_id: CultureMech:010168
  path: data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml
  label: 1_2_r2a_medium_with_75_artificial_seawater
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch005/048/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-005/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch005/048/strict.tsv"
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010168
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
  - CultureMech:010168
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-20T07:25:32Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T07:25:32Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T07:24:20.694001Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch005/048/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-20T07:24:23.602545Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-005/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch005/048/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T07:24:26.982606Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T07:24:29.299991Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-20T07:25:32Z'
  support: supports
  summary: './data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml:1:id:
    CultureMech:010168

    ./data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml:1:id:
    CultureMech:010168

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T04:00:00.223561Z'
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
  accessed_at: '2026-10-20T03:57:32.595833Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
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
  accessed_at: '2026-10-20T07:22:06.659998Z'
  support: supports
  summary: CHEBI:28017 resolves to starch and is not obsolete. This verifies the asserted
    generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond
    the record is inferred.
  snapshot_sha256: 959b4330165a7ff12d2e464f4a7b44e148376624d04cf7764b6a8671c1c99204
- evidence_id: chebi28741
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28741
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:18:35.701178Z'
  support: supports
  summary: CHEBI:28741 resolves to sodium fluoride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 436bc7270fe637f5710b32b2b4491f74c41eebdd6337489545fb97ef5c29a9bb
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:22:09.107223Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32030
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32030
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:18:36.747994Z'
  support: supports
  summary: CHEBI:32030 resolves to potassium bromide and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 2dfff20bf274927ceb7d33e95e02fb24aca53828fc68b5fa5b21db63bdb318e6
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:18:31.261112Z'
  support: supports
  summary: CHEBI:32139 resolves to sodium hydrogencarbonate and is not obsolete. This
    verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:18:34.792120Z'
  support: supports
  summary: CHEBI:32149 resolves to sodium sulfate and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:18:29.554272Z'
  support: supports
  summary: CHEBI:32588 resolves to potassium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:18:28.821622Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi36385
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_36385
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:22:12.205299Z'
  support: supports
  summary: CHEBI:36385 resolves to strontium dichloride hexahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: a81397c907aeb36242c9f0a2aa24979df4b9aad2f624e8991ccd87a4ff9428b5
- evidence_id: chebi50144
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:22:07.440767Z'
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
  accessed_at: '2026-10-20T07:18:25.621908Z'
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
  accessed_at: '2026-10-20T07:22:10.944093Z'
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
  accessed_at: '2026-10-20T07:25:32Z'
  support: supports
  summary: '{"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795":
    [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type":
    "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate",
    "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier":
    "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118":
    [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label":
    "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term":
    "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:36385": [{"label":
    "SrCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:36385",
    "preferred_term": "SrCl2 x 6 H2O", "ontology_id": "CHEBI:36385", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:28741": [{"label": "NaF", "match_type":
    "preferred_term", "identifier": "CHEBI:28741", "preferred_term": "NaF", "ontology_id":
    "CHEBI:28741", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32030":
    [{"label": "KBr", "match_type": "preferred_term", "identifier": "CHEBI:32030",
    "preferred_term": "KBr", "ontology_id": "CHEBI:32030", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}'
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M761
  locator: meta; components[0:2]; comments[0]
  accessed_at: '2026-10-20T07:24:21.858785Z'
  support: supports
  summary: Complete two-section source, metadata and preparation comment inspected;
    main additions and seawater stock remain distinct in the provider.
  snapshot_sha256: 5f9c6ad04a09b2688ad5a4c437a960dd5c2d6615c92f47fda0c30eb51de81d74
- evidence_id: jcm
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=736
  locator: GRMD 736 complete formula and preparation paragraph
  accessed_at: '2026-10-20T07:22:03.451753Z'
  support: supports
  summary: Collection original supports the TOGO identity, supplied forms, source
    preparation and distinct stock composition.
  snapshot_sha256: 9540cd428c51db6ee72f1be70d72e7a2424c4fccc89c997b199619d96180d21e
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J736
  locator: data.medium and data.solutions[0:2]
  accessed_at: '2026-10-20T07:22:04.087299Z'
  support: supports
  summary: Independent provider representation separates main solution 4666 and seawater
    stock 4667; numeric comparison is scoped by stage.
  snapshot_sha256: 96cf1781f06e582472584e47769346c36212dea52bd574a9c7708154e84fad20
- evidence_id: render
  kind: database
  reference: https://bacmedia.dsmz.de/pdf/J736
  locator: Page 1 complete recipe and headings
  accessed_at: '2026-10-20T07:22:04.690002Z'
  support: supports
  summary: Rendering retains stock separation and a declared volume basis, but its
    final-pH label abbreviates the collection preparation context.
  snapshot_sha256: 429adcf2df3b7c12476b2ca49d6b318580a3e68bff718dded35632d084e14f2d
- evidence_id: trace
  kind: validation
  reference: src/culturemech/import/togo_importer.py
  locator: Exact input-row trace and bounded primary-component/preparation parsing
  accessed_at: '2026-10-20T07:24:46.026444Z'
  support: supports
  summary: '{"accessed_at": "2026-10-20T07:24:46.026444+00:00", "amount_trace": [{"index":
    0, "name": "Distilled water", "source_rows": [{"section": 0, "amount": 250, "unit":
    "ml"}, {"section": 1, "amount": 1, "unit": "L"}], "error": "Different-stage water
    numerals combined with incompatible units."}, {"index": 1, "name": "MgSO4\u00b77H2O",
    "section": 0, "amount": 0.025, "unit": "g", "target_unit": "G_PER_L", "notes_match_source":
    true}, {"index": 2, "name": "K2HPO4", "section": 0, "amount": 0.15, "unit": "g",
    "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 3, "name": "Sodium
    pyruvate", "section": 0, "amount": 0.15, "unit": "g", "target_unit": "G_PER_L",
    "notes_match_source": true}, {"index": 4, "name": "Glucose", "section": 0, "amount":
    0.25, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index":
    5, "name": "Soluble starch", "section": 0, "amount": 0.25, "unit": "g", "target_unit":
    "G_PER_L", "notes_match_source": true}, {"index": 6, "name": "Yeast extract (BD-Difco)",
    "section": 0, "amount": 0.25, "unit": "g", "target_unit": "G_PER_L", "notes_match_source":
    true}, {"index": 7, "name": "Proteose peptone No. 3 (BD-Difco)", "section": 0,
    "amount": 0.25, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true},
    {"index": 8, "name": "Casamino acids (BD-Difco)", "section": 0, "amount": 0.25,
    "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index":
    9, "name": "Artificial seawater (see below)", "section": 0, "amount": 750, "unit":
    "ml", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 10, "name":
    "NaCl", "section": 1, "amount": 23.5, "unit": "g", "target_unit": "G_PER_L", "notes_match_source":
    true}, {"index": 11, "name": "CaCl2\u00b72H2O", "section": 1, "amount": 1.1, "unit":
    "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 12, "name":
    "MgCl2\u00b76H2O", "section": 1, "amount": 4.9, "unit": "g", "target_unit": "G_PER_L",
    "notes_match_source": true}, {"index": 13, "name": "H3BO3", "section": 1, "amount":
    0.026, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index":
    14, "name": "KCl", "section": 1, "amount": 0.66, "unit": "g", "target_unit": "G_PER_L",
    "notes_match_source": true}, {"index": 15, "name": "NaHCO3", "section": 1, "amount":
    0.19, "unit": "g", "target_unit": "G_PER_L", "notes_match_source": true}, {"index":
    16, "name": "Na2SO4", "section": 1, "amount": 3.9, "unit": "g", "target_unit":
    "G_PER_L", "notes_match_source": true}, {"index": 17, "name": "SrCl2\u00b76H2O",
    "section": 1, "amount": 0.024, "unit": "g", "target_unit": "G_PER_L", "notes_match_source":
    true}, {"index": 18, "name": "NaF", "section": 1, "amount": 0.003, "unit": "g",
    "target_unit": "G_PER_L", "notes_match_source": true}, {"index": 19, "name": "KBr",
    "section": 1, "amount": 0.096, "unit": "g", "target_unit": "G_PER_L", "notes_match_source":
    true}], "parser_preview": {"scope": "In-memory primary-section extraction and
    preparation parsing; no importer write methods called.", "ingredients": [{"preferred_term":
    "Distilled water", "concentration": {"value": "250", "unit": "ML_PER_L"}, "notes":
    "Role: Solvating media; Properties: Inorganic compound, Defined component, Simple
    component"}, {"preferred_term": "MgSO4\u00b77H2O", "concentration": {"value":
    "0.025", "unit": "G_PER_L"}, "notes": "Role: Mineral source; Properties: Inorganic
    compound, Defined component, Simple component"}, {"preferred_term": "K2HPO4",
    "concentration": {"value": "0.15", "unit": "G_PER_L"}, "notes": "Role: Buffer;
    Properties: Inorganic compound, Defined component, Simple component"}, {"preferred_term":
    "Sodium pyruvate", "concentration": {"value": "0.15", "unit": "G_PER_L"}, "notes":
    "Role: Carbon source; Properties: Organic compound, Defined component, Simple
    component"}, {"preferred_term": "Glucose", "concentration": {"value": "0.25",
    "unit": "G_PER_L"}, "notes": "Role: Carbon source; Properties: Organic compound,
    Defined component, Simple component"}, {"preferred_term": "Soluble starch", "concentration":
    {"value": "0.25", "unit": "G_PER_L"}, "notes": "Role: Carbon source; Properties:
    Undefined component"}, {"preferred_term": "Yeast extract (BD-Difco)", "concentration":
    {"value": "0.25", "unit": "G_PER_L"}, "notes": "Properties: Undefined component"},
    {"preferred_term": "Proteose peptone No. 3 (BD-Difco)", "concentration": {"value":
    "0.25", "unit": "G_PER_L"}, "notes": "Properties: Undefined component"}, {"preferred_term":
    "Casamino acids (BD-Difco)", "concentration": {"value": "0.25", "unit": "G_PER_L"},
    "notes": "Properties: Undefined component"}], "solutions": [{"preferred_term":
    "Artificial seawater (see below)", "composition": [], "concentration": {"value":
    "750", "unit": "ML_PER_L"}, "notes": "Defined in TOGO medium M761."}], "preparation":
    [{"step_number": 1, "action": "AUTOCLAVE", "description": "Mix components except
    artificial seawater, adjust pH to 7.2, and autoclave. Separately autoclave artificial
    seawater. After cooling, combine the two solutions."}]}}'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '16 primary CHEBI identities resolve with matching labels; 15 of 15 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - mim
  - chebi131527
  - chebi15377
  - chebi17234
  - chebi26710
  - chebi28017
  - chebi28741
  - chebi31795
  - chebi32030
  - chebi32139
  - chebi32149
  - chebi32588
  - chebi33118
  - chebi36385
  - chebi50144
  - chebi86158
  - chebi86345
  details: 20 direct ingredient instances; primary coverage 16/20 (80.00%), verified
    secondary coverage 15/20 (75.00%). Percentages use a 0–100 linkage scale, not
    a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded
    rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Source identity and owner correspondence
  outcome: supported
  summary: CultureMech:010168 resolves through TOGO M761 to JCM 736. The entire target
    and single normalized owner agree in scientific content. Their shared source identity
    does not validate the altered stock representation.
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - owner-0
  - id-search
  - togo
  - jcm
  - api
- assessment_id: amount-0
  area: quantity
  topic: ingredients[0].concentration and source stage
  outcome: concern
  summary: 'correct: 250 ml receiving-stage water and 1 L stock water were combined
    as bare numerals into 251 G_PER_L. This mixes preparation stages and incompatible
    units.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-1
  area: quantity
  topic: ingredients[1].concentration and source stage
  outcome: supported
  summary: 'verified amount: MgSO4·7H2O 0.025 G_PER_L agrees with the source mass
    and nominal receiving-recipe basis; source supplier/form qualifiers are retained.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-2
  area: quantity
  topic: ingredients[2].concentration and source stage
  outcome: supported
  summary: 'verified amount: K2HPO4 0.15 G_PER_L agrees with the source mass and nominal
    receiving-recipe basis; source supplier/form qualifiers are retained.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-3
  area: quantity
  topic: ingredients[3].concentration and source stage
  outcome: supported
  summary: 'verified amount: Sodium pyruvate 0.15 G_PER_L agrees with the source mass
    and nominal receiving-recipe basis; source supplier/form qualifiers are retained.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-4
  area: quantity
  topic: ingredients[4].concentration and source stage
  outcome: supported
  summary: 'verified amount: Glucose 0.25 G_PER_L agrees with the source mass and
    nominal receiving-recipe basis; source supplier/form qualifiers are retained.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-5
  area: quantity
  topic: ingredients[5].concentration and source stage
  outcome: supported
  summary: 'verified amount: Soluble starch 0.25 G_PER_L agrees with the source mass
    and nominal receiving-recipe basis; source supplier/form qualifiers are retained.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-6
  area: quantity
  topic: ingredients[6].concentration and source stage
  outcome: supported
  summary: 'verified amount: Yeast extract (BD-Difco) 0.25 G_PER_L agrees with the
    source mass and nominal receiving-recipe basis; source supplier/form qualifiers
    are retained.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-7
  area: quantity
  topic: ingredients[7].concentration and source stage
  outcome: supported
  summary: 'verified amount: Proteose peptone No. 3 (BD-Difco) 0.25 G_PER_L agrees
    with the source mass and nominal receiving-recipe basis; source supplier/form
    qualifiers are retained.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-8
  area: quantity
  topic: ingredients[8].concentration and source stage
  outcome: supported
  summary: 'verified amount: Casamino acids (BD-Difco) 0.25 G_PER_L agrees with the
    source mass and nominal receiving-recipe basis; source supplier/form qualifiers
    are retained.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-9
  area: quantity
  topic: ingredients[9].concentration and source stage
  outcome: concern
  summary: 'correct: the source seawater addition is a liquid volume. It is represented
    as a direct ingredient mass concentration while its stock solutes are also expanded
    below.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-10
  area: quantity
  topic: ingredients[10].concentration and source stage
  outcome: concern
  summary: 'correct scope: NaCl 23.5 G_PER_L is a stock-batch value, not a direct
    receiving-medium concentration. Unlike the volume rows, the stock mass units themselves
    agree with the source.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-11
  area: quantity
  topic: ingredients[11].concentration and source stage
  outcome: concern
  summary: 'correct scope: CaCl2·2H2O 1.1 G_PER_L is a stock-batch value, not a direct
    receiving-medium concentration. Unlike the volume rows, the stock mass units themselves
    agree with the source.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-12
  area: quantity
  topic: ingredients[12].concentration and source stage
  outcome: concern
  summary: 'correct scope: MgCl2·6H2O 4.9 G_PER_L is a stock-batch value, not a direct
    receiving-medium concentration. Unlike the volume rows, the stock mass units themselves
    agree with the source.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-13
  area: quantity
  topic: ingredients[13].concentration and source stage
  outcome: concern
  summary: 'correct scope: H3BO3 0.026 G_PER_L is a stock-batch value, not a direct
    receiving-medium concentration. Unlike the volume rows, the stock mass units themselves
    agree with the source.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-14
  area: quantity
  topic: ingredients[14].concentration and source stage
  outcome: concern
  summary: 'correct scope: KCl 0.66 G_PER_L is a stock-batch value, not a direct receiving-medium
    concentration. Unlike the volume rows, the stock mass units themselves agree with
    the source.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-15
  area: quantity
  topic: ingredients[15].concentration and source stage
  outcome: concern
  summary: 'correct scope: NaHCO3 0.19 G_PER_L is a stock-batch value, not a direct
    receiving-medium concentration. Unlike the volume rows, the stock mass units themselves
    agree with the source.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-16
  area: quantity
  topic: ingredients[16].concentration and source stage
  outcome: concern
  summary: 'correct scope: Na2SO4 3.9 G_PER_L is a stock-batch value, not a direct
    receiving-medium concentration. Unlike the volume rows, the stock mass units themselves
    agree with the source.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-17
  area: quantity
  topic: ingredients[17].concentration and source stage
  outcome: concern
  summary: 'correct scope: SrCl2·6H2O 0.024 G_PER_L is a stock-batch value, not a
    direct receiving-medium concentration. Unlike the volume rows, the stock mass
    units themselves agree with the source.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-18
  area: quantity
  topic: ingredients[18].concentration and source stage
  outcome: concern
  summary: 'correct scope: NaF 0.003 G_PER_L is a stock-batch value, not a direct
    receiving-medium concentration. Unlike the volume rows, the stock mass units themselves
    agree with the source.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: amount-19
  area: quantity
  topic: ingredients[19].concentration and source stage
  outcome: concern
  summary: 'correct scope: KBr 0.096 G_PER_L is a stock-batch value, not a direct
    receiving-medium concentration. Unlike the volume rows, the stock mass units themselves
    agree with the source.'
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - api
  - trace
  details: All twenty assertions individually traced. No density conversion, hydration
    change or new final stock concentration is inferred.
- assessment_id: structure
  area: consistency
  topic: Stock boundary and current process
  outcome: concern
  summary: The stock addition and ten stock solutes appear together as direct ingredients.
    Current bounded parsing separates nine main rows and one volume-valued stock addition,
    and retains the preparation comment, but returns empty stock composition. Regeneration/import
    alone is not established as a complete repair.
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  - trace
- assessment_id: preparation
  area: completeness
  topic: Source preparation and pH scope
  outcome: concern
  summary: The source specifies separate preparation and later combination, with pH
    adjustment before the seawater addition. Target and owner retain neither the preparation
    steps nor this pH context. A provider-wide pH header should not replace the primary
    source stage.
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  - api
  - render
- assessment_id: forms
  area: grounding
  topic: Supplied forms and chemical identities
  outcome: supported
  summary: Supplier-qualified nutrients and soluble starch are retained. Generic starch
    grounding is compatible with that separate supplied-form qualifier. The explicit
    magnesium sulfate, magnesium chloride, calcium chloride and strontium chloride
    hydrate labels agree with the source; generic glucose is not narrowed to a stereoisomer.
    Ontology existence does not certify the amount/stage claims.
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - chebi28017
  - chebi31795
  - chebi86345
  - chebi86158
  - chebi36385
  - chebi17234
- assessment_id: scope
  area: scope
  topic: Physical state, role annotations and growth claims
  outcome: supported
  summary: No source gelling component supports LIQUID, and complex nutrient mixtures
    support COMPLEX/UNDEFINED. Imported role/property notes match the TOGO rows, but
    do not establish organism-specific mechanisms or growth. No taxon, DOI, PMID,
    strain, incubation or storage assertion is made.
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - togo
  - jcm
  - trace
- assessment_id: evidence
  area: evidence
  topic: Source support and history
  outcome: concern
  summary: No amount evidence is attached to the twenty direct claims in target or
    owner. Import and duplicate-cleanup history explain provenance but do not justify
    combining stocks or volumes. Reference validation examined zero excerpts.
  target_ids:
  - CultureMech:010168
  evidence_ids:
  - record
  - owner-0
  - validate-references
  - togo
  - jcm
findings:
- finding_id: f1
  issue_key: CM010168-seawater-stock-flattened
  category: consistency
  severity: blocker
  status: open
  certainty: confirmed
  title: Seawater stock and its components are duplicated as direct ingredients
  description: The stock addition and its ten-solute formulation appear in one direct
    ingredient list, obscuring the receiving-medium boundary and changing the meaning
    of the source recipe. Current preview keeps the addition separate but loses its
    local composition.
  target_ids:
  - CultureMech:010168
  field_paths:
  - ingredients[9:20]
  - solutions
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  - api
  - trace
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM010168-liquid-volume-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Liquid volumes became masses and water stages were combined
  description: Both stock-addition volume and main/stock water volumes are encoded
    as G_PER_L; incompatible water numerals were summed. Source grams for stock solutes
    are separate from these liquid-unit errors.
  target_ids:
  - CultureMech:010168
  field_paths:
  - ingredients[0].concentration
  - ingredients[9].concentration
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  - trace
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM010168-preparation-ph-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation and pH stage are omitted
  description: Both inspected sources retain the preparation sequence and stage-specific
    pH adjustment; the local records have no preparation or pH fields.
  target_ids:
  - CultureMech:010168
  field_paths:
  - preparation_steps
  - ph_value
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: CM010168-stage-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Claims lack evidence for units and stage
  description: All twenty claims lack evidence objects, preventing source-stage distinctions
    from being recovered at the asserted fields.
  target_ids:
  - CultureMech:010168
  field_paths:
  - ingredients[*].evidence
  - evidence
  - references
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Restore separate main and source-defined stock representations in the
    normalized owner, retaining the exact composition once. Resolve the local stock-section
    matching gap demonstrated by the empty-composition preview before relying on the
    importer. Regenerate only after verification.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010168
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml
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
  description: Restore original liquid units and preparation-stage/batch context without
    using a density assumption. Keep stock water separate from receiving-medium water
    and do not infer a measured final volume.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010168
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml
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
  description: Retain exact source preparation and pH scope with evidence, avoiding
    an unsupported measured-final-pH assertion.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010168
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml
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
  description: Attach narrow evidence to the corrected main ingredients and stock
    addition/composition; preserve provenance through regeneration.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010168
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml
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
- The receiving-medium basis is provider-declared, not physically measured; no new
  final stock concentrations are calculated.
- Current parser checks are bounded in-memory diagnostics, not full importer execution
  or corpus validation. Reused primary captures retain their original access timestamps
  and were inspected for this distinct target.
tags:
- unreviewed-records
- batch-005
- generated-medium
```
