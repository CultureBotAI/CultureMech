# Source and formulation review: 1_2_r2a_medium_with_75_artificial_seawater (CultureMech:003079)

- Review: 20261020T072349Z-culturemech-003079-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-20T07:21:54Z
- Finished UTC: 2026-10-20T07:23:49Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM 736 identity and the eight nutrient quantities are supported, but ten artificial-seawater stock concentrations have been flattened into direct medium ingredients with the stock dose omitted. Source preparation stages and supplied-form qualifiers are missing. Current API parsing separates the stock; this does not certify the existing normalized record or its preparation evidence.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 47 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 005 selects ordinals 41-50 after four validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003079 | data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml | generated | 1_2_r2a_medium_with_75_artificial_seawater |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003079 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003079 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-005/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch005/047/strict.tsv |
| validate-terms | passed | True | CultureMech:003079 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003079 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003079 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003079.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:003079.

15 primary CHEBI identities resolve with matching labels; 15 of 15 current secondary keys have live pinned-index rows. Unresolved keys: [].

18 direct ingredient instances; primary coverage 15/18 (83.33%), verified secondary coverage 15/18 (83.33%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Medium identity and maintained owner

identity: supported. Targets: CultureMech:003079.

CultureMech:003079 and its single normalized owner resolve to JCM 736 / MediaDive J736. The source describes a complete medium assembled using a separately prepared stock; the stock name is not a separate synonym for the whole medium.

### ingredients[0].concentration

quantity: supported. Targets: CultureMech:003079.

verified amount: Yeast extract 0.25 G_PER_L matches the exact main-recipe g_l and provider-declared 1000 ml basis. Original powder mass and supplied form must remain distinguishable from preparation-stage concentration.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[1].concentration

quantity: supported. Targets: CultureMech:003079.

verified amount: Proteose peptone no. 3 0.25 G_PER_L matches the exact main-recipe g_l and provider-declared 1000 ml basis. Original powder mass and supplied form must remain distinguishable from preparation-stage concentration.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[2].concentration

quantity: supported. Targets: CultureMech:003079.

verified amount: Casamino acids 0.25 G_PER_L matches the exact main-recipe g_l and provider-declared 1000 ml basis. Original powder mass and supplied form must remain distinguishable from preparation-stage concentration.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[3].concentration

quantity: supported. Targets: CultureMech:003079.

verified amount: Glucose 0.25 G_PER_L matches the exact main-recipe g_l and provider-declared 1000 ml basis. Original powder mass and supplied form must remain distinguishable from preparation-stage concentration.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[4].concentration

quantity: supported. Targets: CultureMech:003079.

verified amount: Starch 0.25 G_PER_L matches the exact main-recipe g_l and provider-declared 1000 ml basis. Original powder mass and supplied form must remain distinguishable from preparation-stage concentration.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[5].concentration

quantity: supported. Targets: CultureMech:003079.

verified amount: Sodium pyruvate 0.15 G_PER_L matches the exact main-recipe g_l and provider-declared 1000 ml basis. Original powder mass and supplied form must remain distinguishable from preparation-stage concentration.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[6].concentration

quantity: supported. Targets: CultureMech:003079.

verified amount: K2HPO4 0.15 G_PER_L matches the exact main-recipe g_l and provider-declared 1000 ml basis. Original powder mass and supplied form must remain distinguishable from preparation-stage concentration.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[7].concentration

quantity: supported. Targets: CultureMech:003079.

verified amount: MgSO4 x 7 H2O 0.025 G_PER_L matches the exact main-recipe g_l and provider-declared 1000 ml basis. Original powder mass and supplied form must remain distinguishable from preparation-stage concentration.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[8].concentration

quantity: concern. Targets: CultureMech:003079.

correct scope: NaCl 23.5 G_PER_L matches a stock-only concentration in solution 4667, not a direct receiving-medium addition. The stock dose/boundary is missing.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[9].concentration

quantity: concern. Targets: CultureMech:003079.

correct scope: MgCl2 x 6 H2O 4.9 G_PER_L matches a stock-only concentration in solution 4667, not a direct receiving-medium addition. The stock dose/boundary is missing.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[10].concentration

quantity: concern. Targets: CultureMech:003079.

correct scope: Na2SO4 3.9 G_PER_L matches a stock-only concentration in solution 4667, not a direct receiving-medium addition. The stock dose/boundary is missing.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[11].concentration

quantity: concern. Targets: CultureMech:003079.

correct scope: CaCl2 x 2 H2O 1.1 G_PER_L matches a stock-only concentration in solution 4667, not a direct receiving-medium addition. The stock dose/boundary is missing.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[12].concentration

quantity: concern. Targets: CultureMech:003079.

correct scope: KCl 0.66 G_PER_L matches a stock-only concentration in solution 4667, not a direct receiving-medium addition. The stock dose/boundary is missing.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[13].concentration

quantity: concern. Targets: CultureMech:003079.

correct scope: NaHCO3 0.19 G_PER_L matches a stock-only concentration in solution 4667, not a direct receiving-medium addition. The stock dose/boundary is missing.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[14].concentration

quantity: concern. Targets: CultureMech:003079.

correct scope: KBr 0.096 G_PER_L matches a stock-only concentration in solution 4667, not a direct receiving-medium addition. The stock dose/boundary is missing.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[15].concentration

quantity: concern. Targets: CultureMech:003079.

correct scope: H3BO3 0.026 G_PER_L matches a stock-only concentration in solution 4667, not a direct receiving-medium addition. The stock dose/boundary is missing.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[16].concentration

quantity: concern. Targets: CultureMech:003079.

correct scope: SrCl2 x 6 H2O 0.024 G_PER_L matches a stock-only concentration in solution 4667, not a direct receiving-medium addition. The stock dose/boundary is missing.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### ingredients[17].concentration

quantity: concern. Targets: CultureMech:003079.

correct scope: NaF 0.003 G_PER_L matches a stock-only concentration in solution 4667, not a direct receiving-medium addition. The stock dose/boundary is missing.

Every direct amount was traced to its exact source section. Numeric agreement with stock g_l does not validate a final-medium claim. No replacement final stock concentrations or density conversions were calculated.

### Omitted stock dose and representation

consistency: concern. Targets: CultureMech:003079.

The source main recipe adds artificial seawater by volume. Target and owner omit that solution addition and instead place its ten solutes in the direct ingredient list. Current in-memory API parsing returns eight direct nutrients plus the source stock reference/dose, so the observed flattening is not evidence that the current API parser still behaves that way.

### Preparation stages and pH scope

completeness: concern. Targets: CultureMech:003079.

The collection pH adjustment applies to the non-seawater mixture before separate sterilization and later combination. Target retains only an unscoped pH step; the API/rendering also abbreviate this preparation and describe pH broadly. Preserve the primary-source stage rather than infer a measured final-mixture pH.

### Supplier qualifiers and starch form

completeness: concern. Targets: CultureMech:003079.

The source qualifies yeast extract, proteose peptone No.3 and Casamino acids by supplier, and specifies soluble starch. Those qualifiers are absent from the local target/owner. Generic CHEBI starch is not itself invalid, but it cannot replace the supplied-form qualifier.

### Hydrate and salt correspondence

grounding: supported. Targets: CultureMech:003079.

Asserted phosphate and sodium-pyruvate identities are consistent with the source labels. Explicit magnesium sulfate, magnesium chloride, calcium chloride and strontium chloride hydrates are preserved. Generic glucose is not narrowed to an unsupported stereoisomer; complex nutrient mixtures remain ungrounded rather than receiving invented molecule IDs.

### Physical state, classification and growth claims

scope: supported. Targets: CultureMech:003079.

The source has no gelling ingredient, consistent with LIQUID. Complex extracts support COMPLEX/UNDEFINED. Bacterial filing and generic cultivation make no strain-level growth claim. No incubation, atmosphere, storage, DOI, PMID or taxon assertion needs to be imported from unrelated sources.

### Formulation evidence and maintained-input ownership

evidence: concern. Targets: CultureMech:003079.

All 18 direct ingredients lack source evidence in the target and owner. Import/merge histories identify provenance but do not support the flattened formulation; reference validation examined zero excerpts. Maintained-input correction must precede regeneration.

## Findings

### f1: Stock concentrations are represented as direct medium additions

blocker / open / confirmed; issue key: CM003079-stock-concentrations-flattened.

The ten solutes in source artificial-seawater stock 4667 appear at stock strength as direct medium ingredients, while the specified stock addition and its boundary are absent. This changes the meaning of the recipe.

### f2: Separate preparation and pH context are lost

major / open / confirmed; issue key: CM003079-preparation-stage-omissions.

The source specifies separate preparation followed by combination; the local record retains only an unscoped pH adjustment. Provider abbreviations and a final-pH heading do not replace the primary-source stage.

### f3: Supplier and soluble-starch qualifiers are omitted

major / open / confirmed; issue key: CM003079-source-form-qualifiers.

Three supplied nutrient qualifiers and the soluble-starch form are dropped in target and owner although the source/API preserve them.

### f4: Amounts lack evidence for their preparation stage

minor / open / confirmed; issue key: CM003079-stage-evidence-gap.

The target and owner have no scoped ingredient or stock-addition evidence to distinguish main recipe amounts from stock concentrations.

## Recommended Actions And Acceptance Checks

### a1

Restore a separate source-defined stock and its receiving-medium dose in the normalized owner; verify exact candidate stock identity before reuse. Current API parsing already separates this boundary, but source-form and preparation omissions still need review before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain the primary-source step sequence and scope pH to the named preparation stage with evidence. Do not infer a measured final-mixture pH.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Retain exact source supplied-form qualifiers without inventing catalog numbers or replacing generic chemical identity with an unsupported narrower term.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Add narrow evidence after correcting stock boundaries and preparation scope; verify it survives generation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch005/047/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-005/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch005/047/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml:1:id: CultureMech:003079<br>./data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml:1:id: CultureMech:003079<br> |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
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
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:28017": [{"label": "Starch", "match_type": "preferred_term", "identifier": "CHEBI:28017", "preferred_term": "Starch", "ontology_id": "CHEBI:28017", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32030": [{"label": "KBr", "match_type": "preferred_term", "identifier": "CHEBI:32030", "preferred_term": "KBr", "ontology_id": "CHEBI:32030", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:36385": [{"label": "SrCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:36385", "preferred_term": "SrCl2 x 6 H2O", "ontology_id": "CHEBI:36385", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:28741": [{"label": "NaF", "match_type": "preferred_term", "identifier": "CHEBI:28741", "preferred_term": "NaF", "ontology_id": "CHEBI:28741", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=736; JCM GRMD 736, full recipe and preparation paragraph | supports | Complete primary recipe and separate seawater formulation inspected, including supplied forms and preparation-stage order. |
| api | https://mediadive.dsmz.de/rest/medium/J736; data.medium; complete data.solutions[0:2] | supports | J736 explicitly separates main solution 4666 from stock 4667 and supplies the stock dose, volumes and source attributes. Its abbreviated preparation loses collection-stage detail. |
| render | https://bacmedia.dsmz.de/pdf/J736; Page 1 main recipe, stock section and headers | supports | Rendering retains distinct main/stock sections and a declared final-volume header but abbreviates the preparation and describes pH as final. |
| trace | src/culturemech/import/mediadive_importer.py; Bounded API composition and stock parsing; individual source-row trace | supports | {"accessed_at": "2026-10-20T07:22:56.978248+00:00", "amount_trace": [{"index": 0, "name": "Yeast extract", "source_solution": 4666, "source_amount": 0.25, "source_unit": "g", "source_g_l": 0.25, "scope": "main-recipe"}, {"index": 1, "name": "Proteose peptone no. 3", "source_solution": 4666, "source_amount": 0.25, "source_unit": "g", "source_g_l": 0.25, "scope": "main-recipe"}, {"index": 2, "name": "Casamino acids", "source_solution": 4666, "source_amount": 0.25, "source_unit": "g", "source_g_l": 0.25, "scope": "main-recipe"}, {"index": 3, "name": "Glucose", "source_solution": 4666, "source_amount": 0.25, "source_unit": "g", "source_g_l": 0.25, "scope": "main-recipe"}, {"index": 4, "name": "Starch", "source_solution": 4666, "source_amount": 0.25, "source_unit": "g", "source_g_l": 0.25, "scope": "main-recipe"}, {"index": 5, "name": "Sodium pyruvate", "source_solution": 4666, "source_amount": 0.15, "source_unit": "g", "source_g_l": 0.15, "scope": "main-recipe"}, {"index": 6, "name": "K2HPO4", "source_solution": 4666, "source_amount": 0.15, "source_unit": "g", "source_g_l": 0.15, "scope": "main-recipe"}, {"index": 7, "name": "MgSO4 x 7 H2O", "source_solution": 4666, "source_amount": 0.025, "source_unit": "g", "source_g_l": 0.025, "scope": "main-recipe"}, {"index": 8, "name": "NaCl", "source_solution": 4667, "source_amount": 23.5, "source_unit": "g", "source_g_l": 23.5, "scope": "stock-only"}, {"index": 9, "name": "MgCl2 x 6 H2O", "source_solution": 4667, "source_amount": 4.9, "source_unit": "g", "source_g_l": 4.9, "scope": "stock-only"}, {"index": 10, "name": "Na2SO4", "source_solution": 4667, "source_amount": 3.9, "source_unit": "g", "source_g_l": 3.9, "scope": "stock-only"}, {"index": 11, "name": "CaCl2 x 2 H2O", "source_solution": 4667, "source_amount": 1.1, "source_unit": "g", "source_g_l": 1.1, "scope": "stock-only"}, {"index": 12, "name": "KCl", "source_solution": 4667, "source_amount": 0.66, "source_unit": "g", "source_g_l": 0.66, "scope": "stock-only"}, {"index": 13, "name": "NaHCO3", "source_solution": 4667, "source_amount": 0.19, "source_unit": "g", "source_g_l": 0.19, "scope": "stock-only"}, {"index": 14, "name": "KBr", "source_solution": 4667, "source_amount": 0.096, "source_unit": "g", "source_g_l": 0.096, "scope": "stock-only"}, {"index": 15, "name": "H3BO3", "source_solution": 4667, "source_amount": 0.026, "source_unit": "g", "source_g_l": 0.026, "scope": "stock-only"}, {"index": 16, "name": "SrCl2 x 6 H2O", "source_solution": 4667, "source_amount": 0.024, "source_unit": "g", "source_g_l": 0.024, "scope": "stock-only"}, {"index": 17, "name": "NaF", "source_solution": 4667, "source_amount": 3, "source_unit": "mg", "source_g_l": 0.003, "scope": "stock-only"}], "local_stock_candidate": {"path": "data/normalized_yaml/bacterial/mediadive_4667_Artificial_seawater.yaml", "id": "CultureMech:013624", "term": {"id": "mediadive.solution:4667", "label": "Artificial seawater"}, "composition_count": 11, "scope": "Root identity and all composition fields compared, not full evidence/history review."}, "current_parser_preview": {"scope": "In-memory API composition and stock-addition parsing with empty ontology lookup; no importer writes or full pipeline execution.", "ingredients": [{"preferred_term": "Yeast extract", "concentration": {"value": "0.25", "unit": "G_PER_L"}}, {"preferred_term": "Proteose peptone no. 3", "concentration": {"value": "0.25", "unit": "G_PER_L"}}, {"preferred_term": "Casamino acids", "concentration": {"value": "0.25", "unit": "G_PER_L"}}, {"preferred_term": "Glucose", "concentration": {"value": "0.25", "unit": "G_PER_L"}}, {"preferred_term": "Starch", "concentration": {"value": "0.25", "unit": "G_PER_L"}}, {"preferred_term": "Sodium pyruvate", "concentration": {"value": "0.15", "unit": "G_PER_L"}}, {"preferred_term": "K2HPO4", "concentration": {"value": "0.15", "unit": "G_PER_L"}}, {"preferred_term": "MgSO4 x 7 H2O", "concentration": {"value": "0.025", "unit": "G_PER_L"}}], "solutions": [{"preferred_term": "Artificial seawater", "term": {"id": "mediadive.solution:4667", "label": "Artificial seawater"}, "concentration": {"value": "750", "unit": "ML_PER_L"}}]}} |
| stock-candidate | data/normalized_yaml/bacterial/mediadive_4667_Artificial_seawater.yaml; Root identity and complete composition projection | context_only | CultureMech:013624 identifies source solution 4667 and its eleven composition rows agree with the source stock. This is a reuse candidate, not an asserted link in the target or a full stock-review verdict; local evidence/history and quality flags are not certified. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Provider-declared volume was not physically measured; no final concentration of stock-derived components was calculated.
- The stock reuse candidate was examined for root identity/composition only; its complete evidence, history, identifiers and quality flags require separate review before any curation decision.
- Bounded parser calls used an empty ontology lookup and do not certify the full importer or corpus.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T072349Z-culturemech-003079-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_2_r2a_medium_with_75_artificial_seawater
  (CultureMech:003079)'
started_at: '2026-10-20T07:21:54Z'
finished_at: '2026-10-20T07:23:49Z'
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
summary: JCM 736 identity and the eight nutrient quantities are supported, but ten
  artificial-seawater stock concentrations have been flattened into direct medium
  ingredients with the stock dose omitted. Source preparation stages and supplied-form
  qualifiers are missing. Current API parsing separates the stock; this does not certify
  the existing normalized record or its preparation evidence.
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
  - path: data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml
    sha256: 557d15b5a57556bc61986198fc0750b6f6b7e7742cbe5a19316a7c03ebfa8761
    role: target
  - path: data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml
    sha256: a1457064cee9aba0533c782fdcc4ca0b03caaf83ca0e5c985a02e7f02bf3a23c
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4667_Artificial_seawater.yaml
    sha256: 645840faae6d9ba113f1e22cd63a3555a0eb3e1d95fce49aea7fcde57c280031
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
  selection: Record 47 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 005 selects ordinals 41-50 after four
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003079
targets:
- target_id: CultureMech:003079
  path: data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml
  label: 1_2_r2a_medium_with_75_artificial_seawater
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch005/047/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-005/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch005/047/strict.tsv"
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003079
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
  - CultureMech:003079
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-20T07:23:48Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T07:23:48Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T07:22:01.585966Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch005/047/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-20T07:22:03.139144Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-005/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch005/047/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T07:22:05.702459Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T07:22:06.845132Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-20T07:23:48Z'
  support: supports
  summary: './data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml:1:id:
    CultureMech:003079

    ./data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml:1:id:
    CultureMech:003079

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
  accessed_at: '2026-10-20T07:23:48Z'
  support: supports
  summary: '{"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:28017": [{"label":
    "Starch", "match_type": "preferred_term", "identifier": "CHEBI:28017", "preferred_term":
    "Starch", "ontology_id": "CHEBI:28017", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type": "preferred_term",
    "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label":
    "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term":
    "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label":
    "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345",
    "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149":
    [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149",
    "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O",
    "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type":
    "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id":
    "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32030":
    [{"label": "KBr", "match_type": "preferred_term", "identifier": "CHEBI:32030",
    "preferred_term": "KBr", "ontology_id": "CHEBI:32030", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:36385": [{"label":
    "SrCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:36385",
    "preferred_term": "SrCl2 x 6 H2O", "ontology_id": "CHEBI:36385", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:28741": [{"label": "NaF", "match_type":
    "preferred_term", "identifier": "CHEBI:28741", "preferred_term": "NaF", "ontology_id":
    "CHEBI:28741", "mapping_status": "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: jcm
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=736
  locator: JCM GRMD 736, full recipe and preparation paragraph
  accessed_at: '2026-10-20T07:22:03.451753Z'
  support: supports
  summary: Complete primary recipe and separate seawater formulation inspected, including
    supplied forms and preparation-stage order.
  snapshot_sha256: 9540cd428c51db6ee72f1be70d72e7a2424c4fccc89c997b199619d96180d21e
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J736
  locator: data.medium; complete data.solutions[0:2]
  accessed_at: '2026-10-20T07:22:04.087299Z'
  support: supports
  summary: J736 explicitly separates main solution 4666 from stock 4667 and supplies
    the stock dose, volumes and source attributes. Its abbreviated preparation loses
    collection-stage detail.
  snapshot_sha256: 96cf1781f06e582472584e47769346c36212dea52bd574a9c7708154e84fad20
- evidence_id: render
  kind: database
  reference: https://bacmedia.dsmz.de/pdf/J736
  locator: Page 1 main recipe, stock section and headers
  accessed_at: '2026-10-20T07:22:04.690002Z'
  support: supports
  summary: Rendering retains distinct main/stock sections and a declared final-volume
    header but abbreviates the preparation and describes pH as final.
  snapshot_sha256: 429adcf2df3b7c12476b2ca49d6b318580a3e68bff718dded35632d084e14f2d
- evidence_id: trace
  kind: validation
  reference: src/culturemech/import/mediadive_importer.py
  locator: Bounded API composition and stock parsing; individual source-row trace
  accessed_at: '2026-10-20T07:22:56.978248Z'
  support: supports
  summary: '{"accessed_at": "2026-10-20T07:22:56.978248+00:00", "amount_trace": [{"index":
    0, "name": "Yeast extract", "source_solution": 4666, "source_amount": 0.25, "source_unit":
    "g", "source_g_l": 0.25, "scope": "main-recipe"}, {"index": 1, "name": "Proteose
    peptone no. 3", "source_solution": 4666, "source_amount": 0.25, "source_unit":
    "g", "source_g_l": 0.25, "scope": "main-recipe"}, {"index": 2, "name": "Casamino
    acids", "source_solution": 4666, "source_amount": 0.25, "source_unit": "g", "source_g_l":
    0.25, "scope": "main-recipe"}, {"index": 3, "name": "Glucose", "source_solution":
    4666, "source_amount": 0.25, "source_unit": "g", "source_g_l": 0.25, "scope":
    "main-recipe"}, {"index": 4, "name": "Starch", "source_solution": 4666, "source_amount":
    0.25, "source_unit": "g", "source_g_l": 0.25, "scope": "main-recipe"}, {"index":
    5, "name": "Sodium pyruvate", "source_solution": 4666, "source_amount": 0.15,
    "source_unit": "g", "source_g_l": 0.15, "scope": "main-recipe"}, {"index": 6,
    "name": "K2HPO4", "source_solution": 4666, "source_amount": 0.15, "source_unit":
    "g", "source_g_l": 0.15, "scope": "main-recipe"}, {"index": 7, "name": "MgSO4
    x 7 H2O", "source_solution": 4666, "source_amount": 0.025, "source_unit": "g",
    "source_g_l": 0.025, "scope": "main-recipe"}, {"index": 8, "name": "NaCl", "source_solution":
    4667, "source_amount": 23.5, "source_unit": "g", "source_g_l": 23.5, "scope":
    "stock-only"}, {"index": 9, "name": "MgCl2 x 6 H2O", "source_solution": 4667,
    "source_amount": 4.9, "source_unit": "g", "source_g_l": 4.9, "scope": "stock-only"},
    {"index": 10, "name": "Na2SO4", "source_solution": 4667, "source_amount": 3.9,
    "source_unit": "g", "source_g_l": 3.9, "scope": "stock-only"}, {"index": 11, "name":
    "CaCl2 x 2 H2O", "source_solution": 4667, "source_amount": 1.1, "source_unit":
    "g", "source_g_l": 1.1, "scope": "stock-only"}, {"index": 12, "name": "KCl", "source_solution":
    4667, "source_amount": 0.66, "source_unit": "g", "source_g_l": 0.66, "scope":
    "stock-only"}, {"index": 13, "name": "NaHCO3", "source_solution": 4667, "source_amount":
    0.19, "source_unit": "g", "source_g_l": 0.19, "scope": "stock-only"}, {"index":
    14, "name": "KBr", "source_solution": 4667, "source_amount": 0.096, "source_unit":
    "g", "source_g_l": 0.096, "scope": "stock-only"}, {"index": 15, "name": "H3BO3",
    "source_solution": 4667, "source_amount": 0.026, "source_unit": "g", "source_g_l":
    0.026, "scope": "stock-only"}, {"index": 16, "name": "SrCl2 x 6 H2O", "source_solution":
    4667, "source_amount": 0.024, "source_unit": "g", "source_g_l": 0.024, "scope":
    "stock-only"}, {"index": 17, "name": "NaF", "source_solution": 4667, "source_amount":
    3, "source_unit": "mg", "source_g_l": 0.003, "scope": "stock-only"}], "local_stock_candidate":
    {"path": "data/normalized_yaml/bacterial/mediadive_4667_Artificial_seawater.yaml",
    "id": "CultureMech:013624", "term": {"id": "mediadive.solution:4667", "label":
    "Artificial seawater"}, "composition_count": 11, "scope": "Root identity and all
    composition fields compared, not full evidence/history review."}, "current_parser_preview":
    {"scope": "In-memory API composition and stock-addition parsing with empty ontology
    lookup; no importer writes or full pipeline execution.", "ingredients": [{"preferred_term":
    "Yeast extract", "concentration": {"value": "0.25", "unit": "G_PER_L"}}, {"preferred_term":
    "Proteose peptone no. 3", "concentration": {"value": "0.25", "unit": "G_PER_L"}},
    {"preferred_term": "Casamino acids", "concentration": {"value": "0.25", "unit":
    "G_PER_L"}}, {"preferred_term": "Glucose", "concentration": {"value": "0.25",
    "unit": "G_PER_L"}}, {"preferred_term": "Starch", "concentration": {"value": "0.25",
    "unit": "G_PER_L"}}, {"preferred_term": "Sodium pyruvate", "concentration": {"value":
    "0.15", "unit": "G_PER_L"}}, {"preferred_term": "K2HPO4", "concentration": {"value":
    "0.15", "unit": "G_PER_L"}}, {"preferred_term": "MgSO4 x 7 H2O", "concentration":
    {"value": "0.025", "unit": "G_PER_L"}}], "solutions": [{"preferred_term": "Artificial
    seawater", "term": {"id": "mediadive.solution:4667", "label": "Artificial seawater"},
    "concentration": {"value": "750", "unit": "ML_PER_L"}}]}}'
- evidence_id: stock-candidate
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_4667_Artificial_seawater.yaml
  locator: Root identity and complete composition projection
  accessed_at: '2026-10-20T07:23:48Z'
  support: context_only
  summary: CultureMech:013624 identifies source solution 4667 and its eleven composition
    rows agree with the source stock. This is a reuse candidate, not an asserted link
    in the target or a full stock-review verdict; local evidence/history and quality
    flags are not certified.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '15 primary CHEBI identities resolve with matching labels; 15 of 15 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - mim
  - chebi131527
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
  details: 18 direct ingredient instances; primary coverage 15/18 (83.33%), verified
    secondary coverage 15/18 (83.33%). Percentages use a 0–100 linkage scale, not
    a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded
    rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Medium identity and maintained owner
  outcome: supported
  summary: CultureMech:003079 and its single normalized owner resolve to JCM 736 /
    MediaDive J736. The source describes a complete medium assembled using a separately
    prepared stock; the stock name is not a separate synonym for the whole medium.
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - owner-0
  - id-search
  - jcm
  - api
- assessment_id: amount-0
  area: quantity
  topic: ingredients[0].concentration
  outcome: supported
  summary: 'verified amount: Yeast extract 0.25 G_PER_L matches the exact main-recipe
    g_l and provider-declared 1000 ml basis. Original powder mass and supplied form
    must remain distinguishable from preparation-stage concentration.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-1
  area: quantity
  topic: ingredients[1].concentration
  outcome: supported
  summary: 'verified amount: Proteose peptone no. 3 0.25 G_PER_L matches the exact
    main-recipe g_l and provider-declared 1000 ml basis. Original powder mass and
    supplied form must remain distinguishable from preparation-stage concentration.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-2
  area: quantity
  topic: ingredients[2].concentration
  outcome: supported
  summary: 'verified amount: Casamino acids 0.25 G_PER_L matches the exact main-recipe
    g_l and provider-declared 1000 ml basis. Original powder mass and supplied form
    must remain distinguishable from preparation-stage concentration.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-3
  area: quantity
  topic: ingredients[3].concentration
  outcome: supported
  summary: 'verified amount: Glucose 0.25 G_PER_L matches the exact main-recipe g_l
    and provider-declared 1000 ml basis. Original powder mass and supplied form must
    remain distinguishable from preparation-stage concentration.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-4
  area: quantity
  topic: ingredients[4].concentration
  outcome: supported
  summary: 'verified amount: Starch 0.25 G_PER_L matches the exact main-recipe g_l
    and provider-declared 1000 ml basis. Original powder mass and supplied form must
    remain distinguishable from preparation-stage concentration.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-5
  area: quantity
  topic: ingredients[5].concentration
  outcome: supported
  summary: 'verified amount: Sodium pyruvate 0.15 G_PER_L matches the exact main-recipe
    g_l and provider-declared 1000 ml basis. Original powder mass and supplied form
    must remain distinguishable from preparation-stage concentration.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-6
  area: quantity
  topic: ingredients[6].concentration
  outcome: supported
  summary: 'verified amount: K2HPO4 0.15 G_PER_L matches the exact main-recipe g_l
    and provider-declared 1000 ml basis. Original powder mass and supplied form must
    remain distinguishable from preparation-stage concentration.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-7
  area: quantity
  topic: ingredients[7].concentration
  outcome: supported
  summary: 'verified amount: MgSO4 x 7 H2O 0.025 G_PER_L matches the exact main-recipe
    g_l and provider-declared 1000 ml basis. Original powder mass and supplied form
    must remain distinguishable from preparation-stage concentration.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-8
  area: quantity
  topic: ingredients[8].concentration
  outcome: concern
  summary: 'correct scope: NaCl 23.5 G_PER_L matches a stock-only concentration in
    solution 4667, not a direct receiving-medium addition. The stock dose/boundary
    is missing.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-9
  area: quantity
  topic: ingredients[9].concentration
  outcome: concern
  summary: 'correct scope: MgCl2 x 6 H2O 4.9 G_PER_L matches a stock-only concentration
    in solution 4667, not a direct receiving-medium addition. The stock dose/boundary
    is missing.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-10
  area: quantity
  topic: ingredients[10].concentration
  outcome: concern
  summary: 'correct scope: Na2SO4 3.9 G_PER_L matches a stock-only concentration in
    solution 4667, not a direct receiving-medium addition. The stock dose/boundary
    is missing.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-11
  area: quantity
  topic: ingredients[11].concentration
  outcome: concern
  summary: 'correct scope: CaCl2 x 2 H2O 1.1 G_PER_L matches a stock-only concentration
    in solution 4667, not a direct receiving-medium addition. The stock dose/boundary
    is missing.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-12
  area: quantity
  topic: ingredients[12].concentration
  outcome: concern
  summary: 'correct scope: KCl 0.66 G_PER_L matches a stock-only concentration in
    solution 4667, not a direct receiving-medium addition. The stock dose/boundary
    is missing.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-13
  area: quantity
  topic: ingredients[13].concentration
  outcome: concern
  summary: 'correct scope: NaHCO3 0.19 G_PER_L matches a stock-only concentration
    in solution 4667, not a direct receiving-medium addition. The stock dose/boundary
    is missing.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-14
  area: quantity
  topic: ingredients[14].concentration
  outcome: concern
  summary: 'correct scope: KBr 0.096 G_PER_L matches a stock-only concentration in
    solution 4667, not a direct receiving-medium addition. The stock dose/boundary
    is missing.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-15
  area: quantity
  topic: ingredients[15].concentration
  outcome: concern
  summary: 'correct scope: H3BO3 0.026 G_PER_L matches a stock-only concentration
    in solution 4667, not a direct receiving-medium addition. The stock dose/boundary
    is missing.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-16
  area: quantity
  topic: ingredients[16].concentration
  outcome: concern
  summary: 'correct scope: SrCl2 x 6 H2O 0.024 G_PER_L matches a stock-only concentration
    in solution 4667, not a direct receiving-medium addition. The stock dose/boundary
    is missing.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: amount-17
  area: quantity
  topic: ingredients[17].concentration
  outcome: concern
  summary: 'correct scope: NaF 0.003 G_PER_L matches a stock-only concentration in
    solution 4667, not a direct receiving-medium addition. The stock dose/boundary
    is missing.'
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - render
  - trace
  details: Every direct amount was traced to its exact source section. Numeric agreement
    with stock g_l does not validate a final-medium claim. No replacement final stock
    concentrations or density conversions were calculated.
- assessment_id: stock
  area: consistency
  topic: Omitted stock dose and representation
  outcome: concern
  summary: The source main recipe adds artificial seawater by volume. Target and owner
    omit that solution addition and instead place its ten solutes in the direct ingredient
    list. Current in-memory API parsing returns eight direct nutrients plus the source
    stock reference/dose, so the observed flattening is not evidence that the current
    API parser still behaves that way.
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - owner-0
  - jcm
  - api
  - trace
  - stock-candidate
- assessment_id: preparation
  area: completeness
  topic: Preparation stages and pH scope
  outcome: concern
  summary: The collection pH adjustment applies to the non-seawater mixture before
    separate sterilization and later combination. Target retains only an unscoped
    pH step; the API/rendering also abbreviate this preparation and describe pH broadly.
    Preserve the primary-source stage rather than infer a measured final-mixture pH.
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - owner-0
  - jcm
  - api
  - render
- assessment_id: forms
  area: completeness
  topic: Supplier qualifiers and starch form
  outcome: concern
  summary: The source qualifies yeast extract, proteose peptone No.3 and Casamino
    acids by supplier, and specifies soluble starch. Those qualifiers are absent from
    the local target/owner. Generic CHEBI starch is not itself invalid, but it cannot
    replace the supplied-form qualifier.
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - owner-0
  - jcm
  - api
  - chebi28017
- assessment_id: chemistry
  area: grounding
  topic: Hydrate and salt correspondence
  outcome: supported
  summary: Asserted phosphate and sodium-pyruvate identities are consistent with the
    source labels. Explicit magnesium sulfate, magnesium chloride, calcium chloride
    and strontium chloride hydrates are preserved. Generic glucose is not narrowed
    to an unsupported stereoisomer; complex nutrient mixtures remain ungrounded rather
    than receiving invented molecule IDs.
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
  - chebi131527
  - chebi50144
  - chebi31795
  - chebi86345
  - chebi86158
  - chebi36385
  - chebi17234
- assessment_id: scope
  area: scope
  topic: Physical state, classification and growth claims
  outcome: supported
  summary: The source has no gelling ingredient, consistent with LIQUID. Complex extracts
    support COMPLEX/UNDEFINED. Bacterial filing and generic cultivation make no strain-level
    growth claim. No incubation, atmosphere, storage, DOI, PMID or taxon assertion
    needs to be imported from unrelated sources.
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - jcm
  - api
- assessment_id: evidence
  area: evidence
  topic: Formulation evidence and maintained-input ownership
  outcome: concern
  summary: All 18 direct ingredients lack source evidence in the target and owner.
    Import/merge histories identify provenance but do not support the flattened formulation;
    reference validation examined zero excerpts. Maintained-input correction must
    precede regeneration.
  target_ids:
  - CultureMech:003079
  evidence_ids:
  - record
  - owner-0
  - validate-references
  - jcm
  - api
findings:
- finding_id: f1
  issue_key: CM003079-stock-concentrations-flattened
  category: consistency
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock concentrations are represented as direct medium additions
  description: The ten solutes in source artificial-seawater stock 4667 appear at
    stock strength as direct medium ingredients, while the specified stock addition
    and its boundary are absent. This changes the meaning of the recipe.
  target_ids:
  - CultureMech:003079
  field_paths:
  - ingredients[8:18]
  - solutions
  evidence_ids:
  - record
  - owner-0
  - jcm
  - api
  - trace
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM003079-preparation-stage-omissions
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Separate preparation and pH context are lost
  description: The source specifies separate preparation followed by combination;
    the local record retains only an unscoped pH adjustment. Provider abbreviations
    and a final-pH heading do not replace the primary-source stage.
  target_ids:
  - CultureMech:003079
  field_paths:
  - preparation_steps
  - ph_value
  evidence_ids:
  - record
  - owner-0
  - jcm
  - api
  - render
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM003079-source-form-qualifiers
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Supplier and soluble-starch qualifiers are omitted
  description: Three supplied nutrient qualifiers and the soluble-starch form are
    dropped in target and owner although the source/API preserve them.
  target_ids:
  - CultureMech:003079
  field_paths:
  - ingredients[0:3].preferred_term
  - ingredients[4].preferred_term
  evidence_ids:
  - record
  - owner-0
  - jcm
  - api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: CM003079-stage-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Amounts lack evidence for their preparation stage
  description: The target and owner have no scoped ingredient or stock-addition evidence
    to distinguish main recipe amounts from stock concentrations.
  target_ids:
  - CultureMech:003079
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
    path: data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Restore a separate source-defined stock and its receiving-medium dose
    in the normalized owner; verify exact candidate stock identity before reuse. Current
    API parsing already separates this boundary, but source-form and preparation omissions
    still need review before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003079
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml
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
  description: Retain the primary-source step sequence and scope pH to the named preparation
    stage with evidence. Do not infer a measured final-mixture pH.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003079
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml
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
  description: Retain exact source supplied-form qualifiers without inventing catalog
    numbers or replacing generic chemical identity with an unsupported narrower term.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003079
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml
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
  description: Add narrow evidence after correcting stock boundaries and preparation
    scope; verify it survives generation.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003079
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml
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
- Provider-declared volume was not physically measured; no final concentration of
  stock-derived components was calculated.
- The stock reuse candidate was examined for root identity/composition only; its complete
  evidence, history, identifiers and quality flags require separate review before
  any curation decision.
- Bounded parser calls used an empty ontology lookup and do not certify the full importer
  or corpus.
tags:
- unreviewed-records
- batch-005
- generated-medium
```
