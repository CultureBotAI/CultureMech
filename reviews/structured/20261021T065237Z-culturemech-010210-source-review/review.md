# Source and formulation review: 1_ogawa_medium (CultureMech:010210)

- Review: 20261021T065237Z-culturemech-010210-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T06:36:46Z
- Finished UTC: 2026-10-21T06:52:37Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M79 identifies JCM88, but its local solution references point to unrelated stocks selected by generic names. Source stock ingredients were also flattened into the receiving medium; volumes became mass concentrations and source preparation context was omitted. Original collection access remains unavailable.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 60 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 006 selects ordinals 51-60 after five validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010210 | data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml | generated | 1_ogawa_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010210 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010210 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch006/060/strict.tsv |
| validate-terms | passed | True | CultureMech:010210 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010210 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010210 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Inspect original JCM88 recipe | unavailable | True | CultureMech:010210 | Original collection endpoint returns no recipe; two provider representations support bounded assessment. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010210.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:010210.

4 primary CHEBI identities resolve with matching labels; 4 of 4 current secondary keys have live pinned-index rows. Unresolved keys: [].

5 direct ingredient instances; primary coverage 4/5 (80.00%), verified secondary coverage 4/5 (80.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### solutions[0] referenced CultureMech:014248.composition[0].concentration

quantity: supported. Targets: CultureMech:010210.

verified within referenced stock only: provider-declared concentration within this stock; no receiving-medium calculation. This quantity does not validate the wrong receiving-medium association.

### solutions[0] referenced CultureMech:014248.composition[1].concentration

quantity: supported. Targets: CultureMech:010210.

verified within referenced stock only: literal batch-volume unit conversion; no final-volume inference. This quantity does not validate the wrong receiving-medium association.

### solutions[1] referenced CultureMech:014249.composition[0].concentration

quantity: supported. Targets: CultureMech:010210.

verified within referenced stock only: provider-declared concentration within this stock; no receiving-medium calculation. This quantity does not validate the wrong receiving-medium association.

### solutions[1] referenced CultureMech:014249.composition[1].concentration

quantity: supported. Targets: CultureMech:010210.

verified within referenced stock only: provider-declared concentration within this stock; no receiving-medium calculation. This quantity does not validate the wrong receiving-medium association.

### solutions[1] referenced CultureMech:014249.composition[2].concentration

quantity: supported. Targets: CultureMech:010210.

verified within referenced stock only: provider-declared concentration within this stock; no receiving-medium calculation. This quantity does not validate the wrong receiving-medium association.

### solutions[1] referenced CultureMech:014249.composition[3].concentration

quantity: supported. Targets: CultureMech:010210.

verified within referenced stock only: provider-declared concentration within this stock; no receiving-medium calculation. This quantity does not validate the wrong receiving-medium association.

### solutions[1] referenced CultureMech:014249.composition[4].concentration

quantity: supported. Targets: CultureMech:010210.

verified within referenced stock only: provider-declared concentration within this stock; no receiving-medium calculation. This quantity does not validate the wrong receiving-medium association.

### solutions[1] referenced CultureMech:014249.composition[5].concentration

quantity: supported. Targets: CultureMech:010210.

verified within referenced stock only: literal batch-volume unit conversion; no final-volume inference. This quantity does not validate the wrong receiving-medium association.

### Source accession and generated owner

identity: supported. Targets: CultureMech:010210.

The target and one normalized owner consistently identify TOGO M79, whose original source is JCM88. MediaDive J88 corroborates that source identity. Equal short stock names do not establish stock identity.

### Referenced stock identity

grounding: concern. Targets: CultureMech:010210.

Both MediaDive solution CURIEs and their unique local SolutionRecipe records resolve. Their compositions are different from the medium-local source stocks. The name-only resolver reproduces these exact wrong associations, but its present behavior alone does not prove the historical executable bytes.

### ingredients[0].concentration

quantity: concern. Targets: CultureMech:010210.

correct: source Solution I water volume is a local preparation amount, not the asserted mass concentration.

### ingredients[1].concentration

quantity: concern. Targets: CultureMech:010210.

correct: phosphate mass belongs inside source Solution I; the direct final-medium concentration loses that boundary.

### ingredients[2].concentration

quantity: concern. Targets: CultureMech:010210.

correct: glutamate mass belongs inside source Solution I; the receiving-medium field does not preserve its local preparation basis.

### ingredients[3].concentration

quantity: concern. Targets: CultureMech:010210.

correct: glycerol is a volume amount inside source Solution II, not an evidenced mass concentration.

### ingredients[4].concentration

quantity: concern. Targets: CultureMech:010210.

correct: whole egg is a volume amount inside source Solution II; density and final-volume support are absent.

### solutions[0].concentration

quantity: concern. Targets: CultureMech:010210.

correct: source Solution I is a volume addition; the mass-concentration unit and associated stock identity are unsupported.

### solutions[1].concentration

quantity: concern. Targets: CultureMech:010210.

correct: source Solution II is a volume addition; the mass-concentration unit and associated stock identity are unsupported.

### solutions[2]

quantity: concern. Targets: CultureMech:010210.

correct/unsupported: the dye stock is a nested addition within source Solution II, promoted locally to the parent. Its source volume became mass concentration; empty composition leaves its exact form and percent basis unresolved.

### Duplicated parent and stock layers

completeness: concern. Targets: CultureMech:010210.

All five direct ingredient entries originate inside source stock sections, while the corresponding stock additions remain at the parent. The third solution likewise belongs within source Solution II. Merely relinking two stock IDs would leave duplicated and mis-scoped formulation claims; no corrected final concentration is calculated.

### Direct ingredient identity and annotations

grounding: supported. Targets: CultureMech:010210.

Four of five direct instances have verified CHEBI primary identifiers and live secondary keys:80% each on a 0–100 linkage scale. Whole egg remains an undefined mixture. Source role/property labels are retained as imported annotations; no experimental role evidence is inferred.

### Source preparation context

completeness: concern. Targets: CultureMech:010210.

Both providers carry a scoped preparation comment that is absent from both local files. A separate commercial-product availability comment is metadata, not an operational mixing instruction. No missing pH or incubation condition is guessed.

### Classification and physical-state limits

scope: unknown. Targets: CultureMech:010210.

COMPLEX/UNDEFINED is consistent with an egg-containing source. The inspected source excerpts do not independently establish final physical state; LIQUID remains unverified. The schema has agar-specific solid categories, so no replacement enum is assumed. Generic cultivation is not a strain-specific growth assertion.

### Provenance, placeholders and evidence

evidence: concern. Targets: CultureMech:010210.

Target/owner histories have timezone-bearing timestamps and explain the migration. Three Unknown solution names remain. No narrow quantity/preparation evidence occurs in the target; reference validation examined zero excerpts. Stock evidence supports only those stock compositions.

## Findings

### f1: Generic solution names resolve to unrelated stocks

blocker / open / confirmed; issue key: CM010210-wrong-solution-identities.

Both asserted stock IDs resolve to real records with different inventories from the source-scoped Solution I and II. Name-only last-entry resolution reproduces this result; reference existence alone does not validate identity.

### f2: Nested stock components are also asserted at the parent

major / open / confirmed; issue key: CM010210-flattened-stock-assembly.

Five direct entries and the dye stock were extracted from nested source sections while parent stock additions remained. This destroys preparation scope and creates a double-counting risk even after correcting stock identity.

### f3: Volume doses and stock-local amounts became final mass concentrations

major / open / confirmed; issue key: CM010210-volume-mass-and-basis.

Water, glycerol, egg and all three stock doses use unsupported G_PER_L units. The two direct solute amounts retain source numerals but lose their stock-local basis. No density, percent basis or measured final volume supports the apparent conversions.

### f4: Provider preparation context is omitted

major / open / confirmed; issue key: CM010210-source-preparation-omitted.

Neither target nor normalized owner retains the preparation comment supplied by both provider representations, leaving the stock assembly description incomplete.

### f5: Solution placeholders and narrow evidence remain unresolved

minor / open / confirmed; issue key: CM010210-placeholders-and-evidence.

Unknown solution display names, an empty dye-stock composition and absent claim-level evidence obscure provenance. The material formulation consequences are separately recorded above; this finding addresses the remaining provenance representation.

## Recommended Actions And Acceptance Checks

### a1

Reconcile exact source-scoped stock identity in the maintained owner and review the legacy resolver against the demonstrated name collision. Independently inspect any candidate replacement stock before linking it.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Confirm that stock identity uses source context and composition rather than an ambiguous name alone.

### a2

Represent each material at its source preparation level; remove duplicate parent assertions only after source reconciliation and separately authorized curation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve source units and stock/batch context. Keep uncertain stock strength, chemical form and final volume explicit; do not turn provider totals into an assumed final concentration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Recover source-scoped preparation evidence after resolving stock identity and hierarchy, preserving semantic differences between filtration, mixing and heating without adding experimental conditions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Replace placeholders with verified source-scoped labels and attach narrow evidence while retaining unresolved stock chemistry and original-source access limits.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch006/060/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch006/060/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml:1:id: CultureMech:010210<br>./data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml:1:id: CultureMech:010210<br> |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15377 resolves to water and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17754 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17754; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17754 resolves to glycerol and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi64220 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64220; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:64220 resolves to monosodium glutamate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:64220": [{"label": "Na glutamate", "match_type": "preferred_term", "identifier": "CHEBI:64220", "preferred_term": "Na glutamate", "ontology_id": "CHEBI:64220", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17754": [{"label": "Glycerol", "match_type": "preferred_term", "identifier": "CHEBI:17754", "preferred_term": "Glycerol", "ontology_id": "CHEBI:17754", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M79; meta; components[0:3]; comments | supports | Complete identity, three component sections, all amounts/units, source-local references, annotations and comments inspected. Source references explicitly point back to M79. |
| api | https://mediadive.dsmz.de/rest/medium/J88; data.medium; data.solutions | supports | Complete provider medium and solution sections inspected. Its source-local stocks have IDs3716 and3717; these are contextual identifiers, not independently verified replacement local records. |
| jcm-access | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=88; Exact GRMD88 response | context_only | HTTP200 says Nothing found; original collection recipe unavailable. This does not establish historical absence. |
| dependency-check | Captured normalized stock files, solution index, current provider APIs and scripts/migrate_solutions_from_ingredients.py; Bounded identity, eight stock rows, source-section traces and in-memory resolver reproduction | supports | {"scope": "Read-only dependency identity, schema association and source-section representation checks for record60; no mutation, save, stock-review bundle or experimental recommendation. External responses reused from already completed bounded preflight and ontology captures.", "representation_observation": "All five direct target ingredients originate in the two named source stock sections, while the source stock additions remain present and the third solution is promoted from within Solution II to the parent. This is a source-boundary flattening problem; do not infer a corrected final concentration, sum current wrong-stock compositions, or silently replace a stock from its generic name.", "legacy_resolver": {"source": "scripts/migrate_solutions_from_ingredients.py", "method": "SolutionMigrator(..., dry_run=True)._resolve_solution on three in-memory name-only descriptors; no migrate_all or file mutation invoked", "observed_rule": "Constructor assigns solutions_by_name[lowercase_name] repeatedly, retaining the last index entry. _resolve_solution uses that name map without checking source medium or composition.", "reproductions": [{"name": "Solution I", "same_name_candidates_in_index_order": [{"id": "mediadive.solution:461", "name": "Solution I"}, {"id": "mediadive.solution:1207", "name": "Solution I"}, {"id": "mediadive.solution:1720", "name": "Solution I"}, {"id": "mediadive.solution:2614", "name": "Solution I"}, {"id": "mediadive.solution:3073", "name": "Solution I"}, {"id": "mediadive.solution:3316", "name": "Solution I"}, {"id": "mediadive.solution:3329", "name": "Solution I"}, {"id": "mediadive.solution:3716", "name": "Solution I"}, {"id": "mediadive.solution:3856", "name": "Solution I"}, {"id": "mediadive.solution:4815", "name": "Solution I"}, {"id": "mediadive.solution:5335", "name": "Solution I"}], "candidate_count": 11, "in_memory_resolution": {"preferred_term": "Solution I", "term": {"id": "mediadive.solution:5335", "label": "Solution I"}, "notes": "See mediadive_5335_Solution_I.yaml for composition"}}, {"name": "Solution II", "same_name_candidates_in_index_order": [{"id": "mediadive.solution:1208", "name": "Solution II"}, {"id": "mediadive.solution:1721", "name": "Solution II"}, {"id": "mediadive.solution:2615", "name": "Solution II"}, {"id": "mediadive.solution:3717", "name": "Solution II"}, {"id": "mediadive.solution:3857", "name": "Solution II"}, {"id": "mediadive.solution:4816", "name": "Solution II"}, {"id": "mediadive.solution:5336", "name": "Solution II"}], "candidate_count": 7, "in_memory_resolution": {"preferred_term": "Solution II", "term": {"id": "mediadive.solution:5336", "label": "Solution II"}, "notes": "See mediadive_5336_Solution_II.yaml for composition"}}, {"name": "2% Malachite green solution", "same_name_candidates_in_index_order": [], "candidate_count": 0, "in_memory_resolution": {"preferred_term": "2% Malachite green solution", "composition": []}}], "historical_limit": "The present code/index reproduce the target IDs and filename notes. This is evidence of the mechanism, not proof that the currently inspected bytes were exactly the historical executable/index at import time."}, "actual_checks": {"dependency_root_ids_unique_within_normalized_corpus": true, "lookup_included_ignored_files": true, "resolved_local_dependencies": 2, "record_class_commands_exit_zero": true, "stock_composition_rows_checked_against_fresh_api": 8, "embedded_evidence_rows_equal_api_json": 8, "distinct_chebi_ids_resolved_nonobsolete_with_matching_labels": 7, "all_inspection_input_hashes_reverified": true, "full_stock_validator_suite_run": false, "external_fetches_by_this_agent": 0}, "limitations": ["The source-section observations establish representation and association errors, not a repaired preparation protocol.", "No density, total final volume, missing percent basis, or stock-dilution arithmetic was inferred.", "Candidate source-associated stock records3716/3717 were not reviewed as independent targets.", "No organism applicability or pathogen-specific culture claim was sought or assessed."]} |
| stock-0 | data/normalized_yaml/bacterial/mediadive_5335_Solution_I.yaml; Entire SolutionRecipe; composition, evidence, reference and history | context_only | Resolved CultureMech:014248 / mediadive.solution:5335. The asserted reference exists, but its inventory differs from this medium source. Legacy placeholder ingredients and incomplete flags coexist with the populated composition; dependency checks do not promote stock scientific status. |
| stock-0-api | https://mediadive.dsmz.de/rest/solution/5335; data.id; data.recipe; data.volume | supports | Exact stock identity and all composition rows inspected; embedded local evidence JSON equals current provider rows. These are statements about the referenced stock, not support for adding it to this medium. |
| stock-1 | data/normalized_yaml/bacterial/mediadive_5336_Solution_II.yaml; Entire SolutionRecipe; composition, evidence, reference and history | context_only | Resolved CultureMech:014249 / mediadive.solution:5336. The asserted reference exists, but its inventory differs from this medium source. Legacy placeholder ingredients and incomplete flags coexist with the populated composition; dependency checks do not promote stock scientific status. |
| stock-1-api | https://mediadive.dsmz.de/rest/solution/5336; data.id; data.recipe; data.volume | supports | Exact stock identity and all composition rows inspected; embedded local evidence JSON equals current provider rows. These are statements about the referenced stock, not support for adding it to this medium. |
| dependency-CHEBI-131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS identifier, canonical label and obsolete status | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate and is nonobsolete. This checks the referenced stock label only; it does not support its use in this medium. |
| dependency-CHEBI-15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS identifier, canonical label and obsolete status | supports | CHEBI:15377 resolves to water and is nonobsolete. This checks the referenced stock label only; it does not support its use in this medium. |
| dependency-CHEBI-63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS identifier, canonical label and obsolete status | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate and is nonobsolete. This checks the referenced stock label only; it does not support its use in this medium. |
| dependency-CHEBI-62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS identifier, canonical label and obsolete status | supports | CHEBI:62946 resolves to ammonium sulfate and is nonobsolete. This checks the referenced stock label only; it does not support its use in this medium. |
| dependency-CHEBI-26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS identifier, canonical label and obsolete status | supports | CHEBI:26710 resolves to sodium chloride and is nonobsolete. This checks the referenced stock label only; it does not support its use in this medium. |
| dependency-CHEBI-31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS identifier, canonical label and obsolete status | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate and is nonobsolete. This checks the referenced stock label only; it does not support its use in this medium. |
| dependency-CHEBI-86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS identifier, canonical label and obsolete status | supports | CHEBI:86158 resolves to calcium chloride dihydrate and is nonobsolete. This checks the referenced stock label only; it does not support its use in this medium. |
| history | Entire target and maintained-owner histories; All history timestamps parsed with timezone | supports | {"checked_at": "2026-10-21T06:49:34.444925+00:00", "records": [{"path": "data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml", "history": [{"timestamp": "2026-01-27T06:35:55.717444Z", "curator": "togo-import", "parseable_with_timezone": true}, {"timestamp": "2026-01-28T19:48:13.186315Z", "curator": "chebi-enrichment", "parseable_with_timezone": true}, {"timestamp": "2026-03-09T08:04:21.873268+00:00", "curator": "solution-migrator-v1.0", "parseable_with_timezone": true}, {"timestamp": "2026-03-13T06:20:12.133987Z", "curator": "culturemech-id-assigner-v1.0", "parseable_with_timezone": true}, {"timestamp": "2026-03-14T00:00:00+00:00", "curator": "schema-defaulter-v1.0", "parseable_with_timezone": true}, {"timestamp": "2026-03-17T06:29:53.000000Z", "curator": "mediaingredientmech-enrichment-v1.0", "parseable_with_timezone": true}, {"timestamp": "2026-03-17T19:46:31.075337+00:00", "curator": "normalize_media_names_to_snake_case.py", "parseable_with_timezone": true}, {"timestamp": "2026-05-16T09:03:20.972238+00:00", "curator": "migrate_legacy_fields.py", "parseable_with_timezone": true}, {"timestamp": "2026-06-05T07:40:44.553474+00:00", "curator": "mim-legacy-to-chebi-migration-v1.0", "parseable_with_timezone": true}, {"timestamp": "2026-06-08T23:19:35.002124+00:00", "curator": "chebi-regrounding-v1.0", "parseable_with_timezone": true}, {"timestamp": "2026-06-10T07:46:51.676725+00:00", "curator": "primary-term-label-canonicalization-v1.0", "parseable_with_timezone": true}, {"timestamp": "2026-08-06T03:05:19.407111+00:00", "curator": "merge_recipes.py", "parseable_with_timezone": true}]}, {"path": "data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml", "history": [{"timestamp": "2026-01-27T06:35:55.717444Z", "curator": "togo-import", "parseable_with_timezone": true}, {"timestamp": "2026-01-28T19:48:13.186315Z", "curator": "chebi-enrichment", "parseable_with_timezone": true}, {"timestamp": "2026-03-09T08:04:21.873268+00:00", "curator": "solution-migrator-v1.0", "parseable_with_timezone": true}, {"timestamp": "2026-03-13T06:20:12.133987Z", "curator": "culturemech-id-assigner-v1.0", "parseable_with_timezone": true}, {"timestamp": "2026-03-14T00:00:00+00:00", "curator": "schema-defaulter-v1.0", "parseable_with_timezone": true}, {"timestamp": "2026-03-17T06:29:53.000000Z", "curator": "mediaingredientmech-enrichment-v1.0", "parseable_with_timezone": true}, {"timestamp": "2026-03-17T19:46:31.075337+00:00", "curator": "normalize_media_names_to_snake_case.py", "parseable_with_timezone": true}, {"timestamp": "2026-05-16T09:03:20.972238+00:00", "curator": "migrate_legacy_fields.py", "parseable_with_timezone": true}, {"timestamp": "2026-06-05T07:40:44.553474+00:00", "curator": "mim-legacy-to-chebi-migration-v1.0", "parseable_with_timezone": true}, {"timestamp": "2026-06-08T23:19:35.002124+00:00", "curator": "chebi-regrounding-v1.0", "parseable_with_timezone": true}, {"timestamp": "2026-06-10T07:46:51.676725+00:00", "curator": "primary-term-label-canonicalization-v1.0", "parseable_with_timezone": true}]}]} |
| schema-state | src/culturemech/schema/culturemech.yaml; PhysicalStateEnum; solutions and SolutionDescriptor concentration definitions | context_only | Solution entries represent pre-prepared stocks added to the receiving medium. Physical-state options describe broth, agar-solidified, reduced-agar and biphasic media; source stock material alone does not prove a final state. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Original JCM88 verification is unavailable, so this review is partial. Provider agreement does not substitute for that primary inspection.
- The two referenced stocks were read and bounded identity/quantity evidence checked; neither receives a standalone complete scientific review here. Replacement stock records were not assessed.
- No density, percent basis, additive final volume, replacement formulation, organism growth claim or experimental optimization is inferred.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T065237Z-culturemech-010210-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_ogawa_medium (CultureMech:010210)'
started_at: '2026-10-21T06:36:46Z'
finished_at: '2026-10-21T06:52:37Z'
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
summary: TOGO M79 identifies JCM88, but its local solution references point to unrelated
  stocks selected by generic names. Source stock ingredients were also flattened into
  the receiving medium; volumes became mass concentrations and source preparation
  context was omitted. Original collection access remains unavailable.
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
  - path: data/culturemech_recipe_catalog.tsv
    sha256: 0be6a7574e35e4a19cd5f30338d47e1c2cdac0d00152528850a676476394d378
    role: context
  - path: data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml
    sha256: d21d2e1d254e3b944d134f57f943b76a4614f2525e63d7ec259fd129499f7efe
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml
    sha256: cb4f373cee82c5757a697aacf59662d25c822bc21dfd7baa3d26769a144acad6
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5335_Solution_I.yaml
    sha256: 473a8e55f73394b6f3a1347cf04bc6eeb30b6d4a70926ea4fb81bba7c85253be
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5336_Solution_II.yaml
    sha256: 68af0d947a23aa586253be1ffc02555dfc467b063bb9524291d6130a4825d8c4
    role: context
  - path: data/normalized_yaml/recipe_index.json
    sha256: dd2b482ef24092540340b8f444a673e7ab92d1982b519b57bc7a9461222377b2
    role: context
  - path: data/normalized_yaml/solutions/mediadive_solution_index.json
    sha256: 2e43ed2391d0113480837e0756120d71a8dad8a4490010054e67bfb90c66d381
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
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/record_kinds.py
    sha256: 2d9e26cc1e58fddfa9cb215d2adb5ca67abba51639404039f3c6d4c09f436652
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
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
  selection: Record 60 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 006 selects ordinals 51-60 after five
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010210
targets:
- target_id: CultureMech:010210
  path: data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml
  label: 1_ogawa_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch006/060/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch006/060/strict.tsv"
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010210
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
  - CultureMech:010210
- check_id: original-collection
  name: Inspect original JCM88 recipe
  required: true
  status: unavailable
  summary: Original collection endpoint returns no recipe; two provider representations
    support bounded assessment.
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - jcm-access
  - togo
  - api
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T06:52:35Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T06:52:35Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:38:55.050148Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch006/060/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T06:39:00.044152Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch006/060/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:39:05.839613Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:39:11.245990Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T06:52:35Z'
  support: supports
  summary: './data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml:1:id: CultureMech:010210

    ./data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml:1:id: CultureMech:010210

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
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
- evidence_id: chebi17754
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17754
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T06:49:18.571418Z'
  support: supports
  summary: CHEBI:17754 resolves to glycerol and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 0231975176416cbaad3ad04c9efeedbe9bef0b826645e592a4a2f511e8d1db95
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T06:49:18.575865Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi64220
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64220
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T06:49:18.590575Z'
  support: supports
  summary: CHEBI:64220 resolves to monosodium glutamate and is not obsolete. This
    verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: f365c8a94dc3b7bb63e10235e8728f2333b34fb60943ea59c357ebd3456fb25b
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T06:52:35Z'
  support: supports
  summary: '{"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036":
    [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036",
    "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:64220": [{"label": "Na glutamate", "match_type":
    "preferred_term", "identifier": "CHEBI:64220", "preferred_term": "Na glutamate",
    "ontology_id": "CHEBI:64220", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:17754": [{"label": "Glycerol", "match_type": "preferred_term", "identifier":
    "CHEBI:17754", "preferred_term": "Glycerol", "ontology_id": "CHEBI:17754", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M79
  locator: meta; components[0:3]; comments
  accessed_at: '2026-10-21T06:49:17.791422Z'
  support: supports
  summary: Complete identity, three component sections, all amounts/units, source-local
    references, annotations and comments inspected. Source references explicitly point
    back to M79.
  quote: '"reference_media_id": "M79"'
  snapshot_sha256: 89714d95c18660e62fa29c3f4edae54e7477872fb6219b8d39f8ef6ff414ec1d
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J88
  locator: data.medium; data.solutions
  accessed_at: '2026-10-21T06:49:17.767665Z'
  support: supports
  summary: Complete provider medium and solution sections inspected. Its source-local
    stocks have IDs3716 and3717; these are contextual identifiers, not independently
    verified replacement local records.
  snapshot_sha256: 13bf4ba4878aa5af41e9bd6a17ea0b1571b2a45391b7866c6b43b8fbc9311c45
- evidence_id: jcm-access
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=88
  locator: Exact GRMD88 response
  accessed_at: '2026-10-21T06:49:19.225068Z'
  support: context_only
  summary: HTTP200 says Nothing found; original collection recipe unavailable. This
    does not establish historical absence.
  snapshot_sha256: 30987abed7918c73b7eac11a9236d07eae101d3648ca4f28b11ff387c6ef94c9
- evidence_id: dependency-check
  kind: validation
  reference: Captured normalized stock files, solution index, current provider APIs
    and scripts/migrate_solutions_from_ingredients.py
  locator: Bounded identity, eight stock rows, source-section traces and in-memory
    resolver reproduction
  accessed_at: '2026-10-21T06:51:32.634185Z'
  support: supports
  summary: '{"scope": "Read-only dependency identity, schema association and source-section
    representation checks for record60; no mutation, save, stock-review bundle or
    experimental recommendation. External responses reused from already completed
    bounded preflight and ontology captures.", "representation_observation": "All
    five direct target ingredients originate in the two named source stock sections,
    while the source stock additions remain present and the third solution is promoted
    from within Solution II to the parent. This is a source-boundary flattening problem;
    do not infer a corrected final concentration, sum current wrong-stock compositions,
    or silently replace a stock from its generic name.", "legacy_resolver": {"source":
    "scripts/migrate_solutions_from_ingredients.py", "method": "SolutionMigrator(...,
    dry_run=True)._resolve_solution on three in-memory name-only descriptors; no migrate_all
    or file mutation invoked", "observed_rule": "Constructor assigns solutions_by_name[lowercase_name]
    repeatedly, retaining the last index entry. _resolve_solution uses that name map
    without checking source medium or composition.", "reproductions": [{"name": "Solution
    I", "same_name_candidates_in_index_order": [{"id": "mediadive.solution:461", "name":
    "Solution I"}, {"id": "mediadive.solution:1207", "name": "Solution I"}, {"id":
    "mediadive.solution:1720", "name": "Solution I"}, {"id": "mediadive.solution:2614",
    "name": "Solution I"}, {"id": "mediadive.solution:3073", "name": "Solution I"},
    {"id": "mediadive.solution:3316", "name": "Solution I"}, {"id": "mediadive.solution:3329",
    "name": "Solution I"}, {"id": "mediadive.solution:3716", "name": "Solution I"},
    {"id": "mediadive.solution:3856", "name": "Solution I"}, {"id": "mediadive.solution:4815",
    "name": "Solution I"}, {"id": "mediadive.solution:5335", "name": "Solution I"}],
    "candidate_count": 11, "in_memory_resolution": {"preferred_term": "Solution I",
    "term": {"id": "mediadive.solution:5335", "label": "Solution I"}, "notes": "See
    mediadive_5335_Solution_I.yaml for composition"}}, {"name": "Solution II", "same_name_candidates_in_index_order":
    [{"id": "mediadive.solution:1208", "name": "Solution II"}, {"id": "mediadive.solution:1721",
    "name": "Solution II"}, {"id": "mediadive.solution:2615", "name": "Solution II"},
    {"id": "mediadive.solution:3717", "name": "Solution II"}, {"id": "mediadive.solution:3857",
    "name": "Solution II"}, {"id": "mediadive.solution:4816", "name": "Solution II"},
    {"id": "mediadive.solution:5336", "name": "Solution II"}], "candidate_count":
    7, "in_memory_resolution": {"preferred_term": "Solution II", "term": {"id": "mediadive.solution:5336",
    "label": "Solution II"}, "notes": "See mediadive_5336_Solution_II.yaml for composition"}},
    {"name": "2% Malachite green solution", "same_name_candidates_in_index_order":
    [], "candidate_count": 0, "in_memory_resolution": {"preferred_term": "2% Malachite
    green solution", "composition": []}}], "historical_limit": "The present code/index
    reproduce the target IDs and filename notes. This is evidence of the mechanism,
    not proof that the currently inspected bytes were exactly the historical executable/index
    at import time."}, "actual_checks": {"dependency_root_ids_unique_within_normalized_corpus":
    true, "lookup_included_ignored_files": true, "resolved_local_dependencies": 2,
    "record_class_commands_exit_zero": true, "stock_composition_rows_checked_against_fresh_api":
    8, "embedded_evidence_rows_equal_api_json": 8, "distinct_chebi_ids_resolved_nonobsolete_with_matching_labels":
    7, "all_inspection_input_hashes_reverified": true, "full_stock_validator_suite_run":
    false, "external_fetches_by_this_agent": 0}, "limitations": ["The source-section
    observations establish representation and association errors, not a repaired preparation
    protocol.", "No density, total final volume, missing percent basis, or stock-dilution
    arithmetic was inferred.", "Candidate source-associated stock records3716/3717
    were not reviewed as independent targets.", "No organism applicability or pathogen-specific
    culture claim was sought or assessed."]}'
  search_scope: Ignored-inclusive rg lookup across data/normalized_yaml for exact
    stock root IDs; entire stock files read. Full stock validator suite not run.
- evidence_id: stock-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5335_Solution_I.yaml
  locator: Entire SolutionRecipe; composition, evidence, reference and history
  accessed_at: '2026-10-21T06:52:35Z'
  support: context_only
  summary: Resolved CultureMech:014248 / mediadive.solution:5335. The asserted reference
    exists, but its inventory differs from this medium source. Legacy placeholder
    ingredients and incomplete flags coexist with the populated composition; dependency
    checks do not promote stock scientific status.
  snapshot_sha256: 473a8e55f73394b6f3a1347cf04bc6eeb30b6d4a70926ea4fb81bba7c85253be
- evidence_id: stock-0-api
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5335
  locator: data.id; data.recipe; data.volume
  accessed_at: '2026-10-21T06:49:17.772598Z'
  support: supports
  summary: Exact stock identity and all composition rows inspected; embedded local
    evidence JSON equals current provider rows. These are statements about the referenced
    stock, not support for adding it to this medium.
  snapshot_sha256: aee5a511e53e8c67289cabed61f3da1031e0665e8e299d70d2c27216898fe138
- evidence_id: stock-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5336_Solution_II.yaml
  locator: Entire SolutionRecipe; composition, evidence, reference and history
  accessed_at: '2026-10-21T06:52:35Z'
  support: context_only
  summary: Resolved CultureMech:014249 / mediadive.solution:5336. The asserted reference
    exists, but its inventory differs from this medium source. Legacy placeholder
    ingredients and incomplete flags coexist with the populated composition; dependency
    checks do not promote stock scientific status.
  snapshot_sha256: 68af0d947a23aa586253be1ffc02555dfc467b063bb9524291d6130a4825d8c4
- evidence_id: stock-1-api
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5336
  locator: data.id; data.recipe; data.volume
  accessed_at: '2026-10-21T06:49:17.783079Z'
  support: supports
  summary: Exact stock identity and all composition rows inspected; embedded local
    evidence JSON equals current provider rows. These are statements about the referenced
    stock, not support for adding it to this medium.
  snapshot_sha256: 72a48eb3bc63e3cc3b25ee23581dfe6563ddde69c8dc024efd1077fa8e9b6cc1
- evidence_id: dependency-CHEBI-131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS identifier, canonical label and obsolete status
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate and is nonobsolete.
    This checks the referenced stock label only; it does not support its use in this
    medium.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: dependency-CHEBI-15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS identifier, canonical label and obsolete status
  accessed_at: '2026-10-20T04:00:00.223561Z'
  support: supports
  summary: CHEBI:15377 resolves to water and is nonobsolete. This checks the referenced
    stock label only; it does not support its use in this medium.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: dependency-CHEBI-63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS identifier, canonical label and obsolete status
  accessed_at: '2026-10-21T06:49:18.575865Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate and is nonobsolete.
    This checks the referenced stock label only; it does not support its use in this
    medium.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: dependency-CHEBI-62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS identifier, canonical label and obsolete status
  accessed_at: '2026-10-20T07:26:27.571684Z'
  support: supports
  summary: CHEBI:62946 resolves to ammonium sulfate and is nonobsolete. This checks
    the referenced stock label only; it does not support its use in this medium.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: dependency-CHEBI-26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS identifier, canonical label and obsolete status
  accessed_at: '2026-10-20T07:11:31.325976Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride and is nonobsolete. This checks
    the referenced stock label only; it does not support its use in this medium.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: dependency-CHEBI-31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS identifier, canonical label and obsolete status
  accessed_at: '2026-10-20T07:22:09.107223Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate and is nonobsolete.
    This checks the referenced stock label only; it does not support its use in this
    medium.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: dependency-CHEBI-86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS identifier, canonical label and obsolete status
  accessed_at: '2026-10-20T07:18:25.621908Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate and is nonobsolete.
    This checks the referenced stock label only; it does not support its use in this
    medium.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: history
  kind: validation
  reference: Entire target and maintained-owner histories
  locator: All history timestamps parsed with timezone
  accessed_at: '2026-10-21T06:49:34.444925Z'
  support: supports
  summary: '{"checked_at": "2026-10-21T06:49:34.444925+00:00", "records": [{"path":
    "data/merge_yaml/merged/1_ogawa_medium__65d0ae34.yaml", "history": [{"timestamp":
    "2026-01-27T06:35:55.717444Z", "curator": "togo-import", "parseable_with_timezone":
    true}, {"timestamp": "2026-01-28T19:48:13.186315Z", "curator": "chebi-enrichment",
    "parseable_with_timezone": true}, {"timestamp": "2026-03-09T08:04:21.873268+00:00",
    "curator": "solution-migrator-v1.0", "parseable_with_timezone": true}, {"timestamp":
    "2026-03-13T06:20:12.133987Z", "curator": "culturemech-id-assigner-v1.0", "parseable_with_timezone":
    true}, {"timestamp": "2026-03-14T00:00:00+00:00", "curator": "schema-defaulter-v1.0",
    "parseable_with_timezone": true}, {"timestamp": "2026-03-17T06:29:53.000000Z",
    "curator": "mediaingredientmech-enrichment-v1.0", "parseable_with_timezone": true},
    {"timestamp": "2026-03-17T19:46:31.075337+00:00", "curator": "normalize_media_names_to_snake_case.py",
    "parseable_with_timezone": true}, {"timestamp": "2026-05-16T09:03:20.972238+00:00",
    "curator": "migrate_legacy_fields.py", "parseable_with_timezone": true}, {"timestamp":
    "2026-06-05T07:40:44.553474+00:00", "curator": "mim-legacy-to-chebi-migration-v1.0",
    "parseable_with_timezone": true}, {"timestamp": "2026-06-08T23:19:35.002124+00:00",
    "curator": "chebi-regrounding-v1.0", "parseable_with_timezone": true}, {"timestamp":
    "2026-06-10T07:46:51.676725+00:00", "curator": "primary-term-label-canonicalization-v1.0",
    "parseable_with_timezone": true}, {"timestamp": "2026-08-06T03:05:19.407111+00:00",
    "curator": "merge_recipes.py", "parseable_with_timezone": true}]}, {"path": "data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml",
    "history": [{"timestamp": "2026-01-27T06:35:55.717444Z", "curator": "togo-import",
    "parseable_with_timezone": true}, {"timestamp": "2026-01-28T19:48:13.186315Z",
    "curator": "chebi-enrichment", "parseable_with_timezone": true}, {"timestamp":
    "2026-03-09T08:04:21.873268+00:00", "curator": "solution-migrator-v1.0", "parseable_with_timezone":
    true}, {"timestamp": "2026-03-13T06:20:12.133987Z", "curator": "culturemech-id-assigner-v1.0",
    "parseable_with_timezone": true}, {"timestamp": "2026-03-14T00:00:00+00:00", "curator":
    "schema-defaulter-v1.0", "parseable_with_timezone": true}, {"timestamp": "2026-03-17T06:29:53.000000Z",
    "curator": "mediaingredientmech-enrichment-v1.0", "parseable_with_timezone": true},
    {"timestamp": "2026-03-17T19:46:31.075337+00:00", "curator": "normalize_media_names_to_snake_case.py",
    "parseable_with_timezone": true}, {"timestamp": "2026-05-16T09:03:20.972238+00:00",
    "curator": "migrate_legacy_fields.py", "parseable_with_timezone": true}, {"timestamp":
    "2026-06-05T07:40:44.553474+00:00", "curator": "mim-legacy-to-chebi-migration-v1.0",
    "parseable_with_timezone": true}, {"timestamp": "2026-06-08T23:19:35.002124+00:00",
    "curator": "chebi-regrounding-v1.0", "parseable_with_timezone": true}, {"timestamp":
    "2026-06-10T07:46:51.676725+00:00", "curator": "primary-term-label-canonicalization-v1.0",
    "parseable_with_timezone": true}]}]}'
- evidence_id: schema-state
  kind: record_content
  reference: src/culturemech/schema/culturemech.yaml
  locator: PhysicalStateEnum; solutions and SolutionDescriptor concentration definitions
  accessed_at: '2026-10-21T06:52:35Z'
  support: context_only
  summary: Solution entries represent pre-prepared stocks added to the receiving medium.
    Physical-state options describe broth, agar-solidified, reduced-agar and biphasic
    media; source stock material alone does not prove a final state.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010210
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
  - CultureMech:010210
  evidence_ids:
  - record
  - mim
  - chebi15377
  - chebi17754
  - chebi63036
  - chebi64220
  details: 5 direct ingredient instances; primary coverage 4/5 (80.00%), verified
    secondary coverage 4/5 (80.00%). Percentages use a 0–100 linkage scale, not a
    scientific correctness score. Complex mixtures without asserted IDs remain ungrounded
    rather than receiving invented pure-molecule identities.
- assessment_id: stock-0-amount-0
  area: quantity
  topic: solutions[0] referenced CultureMech:014248.composition[0].concentration
  outcome: supported
  summary: 'verified within referenced stock only: provider-declared concentration
    within this stock; no receiving-medium calculation. This quantity does not validate
    the wrong receiving-medium association.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - stock-0
  - stock-0-api
  - dependency-check
- assessment_id: stock-0-amount-1
  area: quantity
  topic: solutions[0] referenced CultureMech:014248.composition[1].concentration
  outcome: supported
  summary: 'verified within referenced stock only: literal batch-volume unit conversion;
    no final-volume inference. This quantity does not validate the wrong receiving-medium
    association.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - stock-0
  - stock-0-api
  - dependency-check
- assessment_id: stock-1-amount-0
  area: quantity
  topic: solutions[1] referenced CultureMech:014249.composition[0].concentration
  outcome: supported
  summary: 'verified within referenced stock only: provider-declared concentration
    within this stock; no receiving-medium calculation. This quantity does not validate
    the wrong receiving-medium association.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - stock-1
  - stock-1-api
  - dependency-check
- assessment_id: stock-1-amount-1
  area: quantity
  topic: solutions[1] referenced CultureMech:014249.composition[1].concentration
  outcome: supported
  summary: 'verified within referenced stock only: provider-declared concentration
    within this stock; no receiving-medium calculation. This quantity does not validate
    the wrong receiving-medium association.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - stock-1
  - stock-1-api
  - dependency-check
- assessment_id: stock-1-amount-2
  area: quantity
  topic: solutions[1] referenced CultureMech:014249.composition[2].concentration
  outcome: supported
  summary: 'verified within referenced stock only: provider-declared concentration
    within this stock; no receiving-medium calculation. This quantity does not validate
    the wrong receiving-medium association.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - stock-1
  - stock-1-api
  - dependency-check
- assessment_id: stock-1-amount-3
  area: quantity
  topic: solutions[1] referenced CultureMech:014249.composition[3].concentration
  outcome: supported
  summary: 'verified within referenced stock only: provider-declared concentration
    within this stock; no receiving-medium calculation. This quantity does not validate
    the wrong receiving-medium association.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - stock-1
  - stock-1-api
  - dependency-check
- assessment_id: stock-1-amount-4
  area: quantity
  topic: solutions[1] referenced CultureMech:014249.composition[4].concentration
  outcome: supported
  summary: 'verified within referenced stock only: provider-declared concentration
    within this stock; no receiving-medium calculation. This quantity does not validate
    the wrong receiving-medium association.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - stock-1
  - stock-1-api
  - dependency-check
- assessment_id: stock-1-amount-5
  area: quantity
  topic: solutions[1] referenced CultureMech:014249.composition[5].concentration
  outcome: supported
  summary: 'verified within referenced stock only: literal batch-volume unit conversion;
    no final-volume inference. This quantity does not validate the wrong receiving-medium
    association.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - stock-1
  - stock-1-api
  - dependency-check
- assessment_id: identity
  area: identity
  topic: Source accession and generated owner
  outcome: supported
  summary: The target and one normalized owner consistently identify TOGO M79, whose
    original source is JCM88. MediaDive J88 corroborates that source identity. Equal
    short stock names do not establish stock identity.
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - record
  - owner-0
  - id-search
  - togo
  - api
- assessment_id: references
  area: grounding
  topic: Referenced stock identity
  outcome: concern
  summary: Both MediaDive solution CURIEs and their unique local SolutionRecipe records
    resolve. Their compositions are different from the medium-local source stocks.
    The name-only resolver reproduces these exact wrong associations, but its present
    behavior alone does not prove the historical executable bytes.
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - record
  - stock-0
  - stock-1
  - stock-0-api
  - stock-1-api
  - togo
  - api
  - dependency-check
- assessment_id: amount-0
  area: quantity
  topic: ingredients[0].concentration
  outcome: concern
  summary: 'correct: source Solution I water volume is a local preparation amount,
    not the asserted mass concentration.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  - dependency-check
- assessment_id: amount-1
  area: quantity
  topic: ingredients[1].concentration
  outcome: concern
  summary: 'correct: phosphate mass belongs inside source Solution I; the direct final-medium
    concentration loses that boundary.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  - dependency-check
- assessment_id: amount-2
  area: quantity
  topic: ingredients[2].concentration
  outcome: concern
  summary: 'correct: glutamate mass belongs inside source Solution I; the receiving-medium
    field does not preserve its local preparation basis.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  - dependency-check
- assessment_id: amount-3
  area: quantity
  topic: ingredients[3].concentration
  outcome: concern
  summary: 'correct: glycerol is a volume amount inside source Solution II, not an
    evidenced mass concentration.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  - dependency-check
- assessment_id: amount-4
  area: quantity
  topic: ingredients[4].concentration
  outcome: concern
  summary: 'correct: whole egg is a volume amount inside source Solution II; density
    and final-volume support are absent.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  - dependency-check
- assessment_id: amount-5
  area: quantity
  topic: solutions[0].concentration
  outcome: concern
  summary: 'correct: source Solution I is a volume addition; the mass-concentration
    unit and associated stock identity are unsupported.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  - dependency-check
- assessment_id: amount-6
  area: quantity
  topic: solutions[1].concentration
  outcome: concern
  summary: 'correct: source Solution II is a volume addition; the mass-concentration
    unit and associated stock identity are unsupported.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  - dependency-check
- assessment_id: amount-7
  area: quantity
  topic: solutions[2]
  outcome: concern
  summary: 'correct/unsupported: the dye stock is a nested addition within source
    Solution II, promoted locally to the parent. Its source volume became mass concentration;
    empty composition leaves its exact form and percent basis unresolved.'
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  - dependency-check
- assessment_id: assembly
  area: completeness
  topic: Duplicated parent and stock layers
  outcome: concern
  summary: All five direct ingredient entries originate inside source stock sections,
    while the corresponding stock additions remain at the parent. The third solution
    likewise belongs within source Solution II. Merely relinking two stock IDs would
    leave duplicated and mis-scoped formulation claims; no corrected final concentration
    is calculated.
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - record
  - togo
  - api
  - dependency-check
  - schema-state
- assessment_id: grounding-scope
  area: grounding
  topic: Direct ingredient identity and annotations
  outcome: supported
  summary: Four of five direct instances have verified CHEBI primary identifiers and
    live secondary keys:80% each on a 0–100 linkage scale. Whole egg remains an undefined
    mixture. Source role/property labels are retained as imported annotations; no
    experimental role evidence is inferred.
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - record
  - mim
  - chebi15377
  - chebi63036
  - chebi64220
  - chebi17754
  - togo
- assessment_id: preparation
  area: completeness
  topic: Source preparation context
  outcome: concern
  summary: Both providers carry a scoped preparation comment that is absent from both
    local files. A separate commercial-product availability comment is metadata, not
    an operational mixing instruction. No missing pH or incubation condition is guessed.
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
- assessment_id: state
  area: scope
  topic: Classification and physical-state limits
  outcome: unknown
  summary: COMPLEX/UNDEFINED is consistent with an egg-containing source. The inspected
    source excerpts do not independently establish final physical state; LIQUID remains
    unverified. The schema has agar-specific solid categories, so no replacement enum
    is assumed. Generic cultivation is not a strain-specific growth assertion.
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - record
  - togo
  - api
  - schema-state
- assessment_id: audit
  area: evidence
  topic: Provenance, placeholders and evidence
  outcome: concern
  summary: Target/owner histories have timezone-bearing timestamps and explain the
    migration. Three Unknown solution names remain. No narrow quantity/preparation
    evidence occurs in the target; reference validation examined zero excerpts. Stock
    evidence supports only those stock compositions.
  target_ids:
  - CultureMech:010210
  evidence_ids:
  - record
  - owner-0
  - history
  - validate-references
  - stock-0
  - stock-1
findings:
- finding_id: f1
  issue_key: CM010210-wrong-solution-identities
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Generic solution names resolve to unrelated stocks
  description: Both asserted stock IDs resolve to real records with different inventories
    from the source-scoped Solution I and II. Name-only last-entry resolution reproduces
    this result; reference existence alone does not validate identity.
  target_ids:
  - CultureMech:010210
  field_paths:
  - solutions[0].term
  - solutions[1].term
  - solutions[0].notes
  - solutions[1].notes
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  - stock-0
  - stock-1
  - stock-0-api
  - stock-1-api
  - dependency-check
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P1.5
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CM010210-flattened-stock-assembly
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Nested stock components are also asserted at the parent
  description: Five direct entries and the dye stock were extracted from nested source
    sections while parent stock additions remained. This destroys preparation scope
    and creates a double-counting risk even after correcting stock identity.
  target_ids:
  - CultureMech:010210
  field_paths:
  - ingredients
  - solutions[2]
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  - dependency-check
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM010210-volume-mass-and-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Volume doses and stock-local amounts became final mass concentrations
  description: Water, glycerol, egg and all three stock doses use unsupported G_PER_L
    units. The two direct solute amounts retain source numerals but lose their stock-local
    basis. No density, percent basis or measured final volume supports the apparent
    conversions.
  target_ids:
  - CultureMech:010210
  field_paths:
  - ingredients[*].concentration
  - solutions[*].concentration
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  - dependency-check
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: CM010210-source-preparation-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Provider preparation context is omitted
  description: Neither target nor normalized owner retains the preparation comment
    supplied by both provider representations, leaving the stock assembly description
    incomplete.
  target_ids:
  - CultureMech:010210
  field_paths:
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: CM010210-placeholders-and-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Solution placeholders and narrow evidence remain unresolved
  description: Unknown solution display names, an empty dye-stock composition and
    absent claim-level evidence obscure provenance. The material formulation consequences
    are separately recorded above; this finding addresses the remaining provenance
    representation.
  target_ids:
  - CultureMech:010210
  field_paths:
  - solutions[*].name
  - solutions[2].composition
  - evidence
  - references
  evidence_ids:
  - record
  - owner-0
  - togo
  - api
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.1
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Reconcile exact source-scoped stock identity in the maintained owner
    and review the legacy resolver against the demonstrated name collision. Independently
    inspect any candidate replacement stock before linking it.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010210
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml
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
  - Confirm that stock identity uses source context and composition rather than an
    ambiguous name alone.
- action_id: a2
  description: Represent each material at its source preparation level; remove duplicate
    parent assertions only after source reconciliation and separately authorized curation.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010210
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml
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
  description: Preserve source units and stock/batch context. Keep uncertain stock
    strength, chemical form and final volume explicit; do not turn provider totals
    into an assumed final concentration.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010210
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml
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
  description: Recover source-scoped preparation evidence after resolving stock identity
    and hierarchy, preserving semantic differences between filtration, mixing and
    heating without adding experimental conditions.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010210
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml
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
  description: Replace placeholders with verified source-scoped labels and attach
    narrow evidence while retaining unresolved stock chemistry and original-source
    access limits.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:010210
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M79_1_Ogawa_Medium.yaml
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
- Original JCM88 verification is unavailable, so this review is partial. Provider
  agreement does not substitute for that primary inspection.
- The two referenced stocks were read and bounded identity/quantity evidence checked;
  neither receives a standalone complete scientific review here. Replacement stock
  records were not assessed.
- No density, percent basis, additive final volume, replacement formulation, organism
  growth claim or experimental optimization is inferred.
tags:
- unreviewed-records
- batch-006
- generated-medium
```
