# Source and formulation review: 9k_medium (CultureMech:010265)

- Review: 20261021T091840Z-culturemech-010265-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T09:12:09Z
- Finished UTC: 2026-10-21T09:18:40Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M84 explicitly identifies JCM92. The exact collection recipe and provider agree, but both local layers encode stock and solvent volumes as mass concentrations, lose the calcium-nitrate milligram scale, omit pH/sterilization context, and retain an unexplained complex/undefined classification. All eight quantities were reviewed without assuming a final-volume denominator.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 128; batch 013 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twelve task batches contain 120 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 122 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010265 | data/merge_yaml/merged/9k_medium__4af6025b.yaml | generated | 9k_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010265 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010265 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch013/128/strict.tsv |
| validate-terms | passed | True | CultureMech:010265 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010265 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010265 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact JCM92 primary source | passed | True | CultureMech:010265 | The cited JCM GRMD=92 page was inspected in full and agrees with the exact TOGO accession and literal table values. Unstated final-volume basis is retained as a source limitation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010265.

The four documented recipes completed; interpret the scope of each separately.

### Exact collection/provider accession and owner

identity: supported. Targets: CultureMech:010265.

TOGO M84, original JCM_M92 and the cited collection URL identify one source formulation. The generated target and sole maintained owner share a stable ID and identical maintained content. Other 9 K names and the distinct sulfur variant are outside this review.

### Every listed amount, unit and denominator

quantity: concern. Targets: CultureMech:010265.

All eight rows are inventoried: acid addition, solvent volume and calcium-nitrate scale require correction; five other mass literals match the exact table but their final-volume denominator is unsupported. The only arithmetic is 10 mg = 0.010 g at the unchanged source batch level. No sum of nominal liquid volumes is asserted as measured final volume.

[{"field_path": "ingredients[0].concentration", "name": "10 N H2SO4", "stored": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "source_context": "The source is a 1 ml addition of 10 N sulfuric-acid stock, not 1 G_PER_L. Normality is stock strength; no density, molarity conversion or final-medium acid concentration is inferred.", "source_snippets": [{"source_key": "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84", "source_locator": "$.components[0].items[0]", "exact_source_quote": "          \"component_name\": \"10 N H2SO4\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"N\","}]}, {"field_path": "ingredients[1].concentration", "name": "Distilled water", "stored": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "source_context": "The source gives 1 L distilled water as solvent volume, not 1 G_PER_L. Additional acid volume does not establish a measured final-volume denominator.", "source_snippets": [{"source_key": "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84", "source_locator": "$.components[0].items[1]", "exact_source_quote": "          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\","}]}, {"field_path": "ingredients[2].concentration", "name": "MgSO4・7H2O", "stored": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "source_context": "The numerical mass literal matches the source table in grams, but the stored G_PER_L final-concentration basis is not independently established by a 1 L water amount plus an acid addition. Preserve the reported batch mass; do not assume a final denominator or silently rescale.", "source_snippets": [{"source_key": "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84", "source_locator": "$.components[0].items[2]", "exact_source_quote": "          \"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\","}]}, {"field_path": "ingredients[3].concentration", "name": "K2HPO4", "stored": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "source_context": "The numerical mass literal matches the source table in grams, but the stored G_PER_L final-concentration basis is not independently established by a 1 L water amount plus an acid addition. Preserve the reported batch mass; do not assume a final denominator or silently rescale.", "source_snippets": [{"source_key": "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84", "source_locator": "$.components[0].items[3]", "exact_source_quote": "          \"component_name\": \"K2HPO4\",\n          \"volume\": 0.5,\n          \"unit\": \"g\","}]}, {"field_path": "ingredients[4].concentration", "name": "FeSO4・7H2O", "stored": {"value": "50", "unit": "G_PER_L"}, "decision": "unsupported", "source_context": "The numerical mass literal matches the source table in grams, but the stored G_PER_L final-concentration basis is not independently established by a 1 L water amount plus an acid addition. Preserve the reported batch mass; do not assume a final denominator or silently rescale.", "source_snippets": [{"source_key": "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84", "source_locator": "$.components[0].items[4]", "exact_source_quote": "          \"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 50,\n          \"unit\": \"g\","}]}, {"field_path": "ingredients[5].concentration", "name": "KCl", "stored": {"value": "0.1", "unit": "G_PER_L"}, "decision": "unsupported", "source_context": "The numerical mass literal matches the source table in grams, but the stored G_PER_L final-concentration basis is not independently established by a 1 L water amount plus an acid addition. Preserve the reported batch mass; do not assume a final denominator or silently rescale.", "source_snippets": [{"source_key": "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84", "source_locator": "$.components[0].items[5]", "exact_source_quote": "          \"component_name\": \"KCl\",\n          \"volume\": 0.1,\n          \"unit\": \"g\","}]}, {"field_path": "ingredients[6].concentration", "name": "(NH4)2SO4", "stored": {"value": "3", "unit": "G_PER_L"}, "decision": "unsupported", "source_context": "The numerical mass literal matches the source table in grams, but the stored G_PER_L final-concentration basis is not independently established by a 1 L water amount plus an acid addition. Preserve the reported batch mass; do not assume a final denominator or silently rescale.", "source_snippets": [{"source_key": "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84", "source_locator": "$.components[0].items[6]", "exact_source_quote": "          \"component_name\": \"(NH4)2SO4\",\n          \"volume\": 3,\n          \"unit\": \"g\","}]}, {"field_path": "ingredients[7].concentration", "name": "Ca(NO3)2", "stored": {"value": "10", "unit": "G_PER_L"}, "decision": "correct", "source_context": "Source calcium nitrate is 10 mg per listed preparation, equal to 0.010 g in that same source batch. Stored 10 G_PER_L loses the mg/g scale (1000-fold numerator difference) and adds an unverified final-volume denominator. No 0.010 G_PER_L final value is assumed.", "source_snippets": [{"source_key": "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84", "source_locator": "$.components[0].items[7]", "exact_source_quote": "          \"component_name\": \"Ca(NO3)2\",\n          \"volume\": 10,\n          \"unit\": \"mg\","}]}]

### Collection pH and sterilization context

completeness: concern. Targets: CultureMech:010265.

The collection page states pH 3.0 and a default of autoclaving at 121°C for 15 min unless otherwise stated; this medium provides no exception. Both local layers omit pH and preparation/sterilization. This is medium preparation context, not incubation temperature or an organism optimum.

### Quantified acid-stock addition

representation: concern. Targets: CultureMech:010265.

The acid has an explicitly specified stock strength and addition volume in both sources, but the local ingredient concentration treats it as mass per volume. No solution ID is asserted, so no replacement stock identity is invented. Preserve stock strength and addition amount separately from final-medium concentration.

### Every target/owner primary and secondary identifier

grounding: supported. Targets: CultureMech:010265.

7/8 target ingredient instances have primary CHEBI IDs; 5/8 have current secondary keys. All asserted target and owner IDs resolve to matching nonobsolete OLS labels; every secondary key has a live preferred-term row in the pinned MIM index.

Linkage metrics use 8 direct ingredient instances as each denominator and a 0–100 percent scale: primary 87.50%; secondary 62.50%. They are not scientific correctness scores. Missing optional links are not wrong IDs; no replacement term is invented.

### Exact supplied forms and ontology limits

grounding: supported. Targets: CultureMech:010265.

All seven asserted chemical IDs match the exact named salts or water, including magnesium and iron sulfate heptahydrates. Source calcium nitrate has no additional hydrate specification to infer. The acid stock is ungrounded rather than assigned an unsupported molecule/mixture identity. Five current secondary keys resolve; missing links for the two hydrated sulfates remain optional linkage opportunities.

### Whole history and maintained-input correspondence

provenance: supported. Targets: CultureMech:010265.

Target 10 and owner 9 history entries (19 timestamp instances) are timezone-aware. All maintained content matches; the generated target adds only merge metadata and its merge event. Existing import/default/migration/enrichment history is provenance, not scientific confirmation. Preserve every old event; append any later authorized curation clarification.

### Maintained owner and generator boundaries

ownership: supported. Targets: CultureMech:010265.

Corrections belong in the exact normalized owner, with narrowly scoped transformation changes only if necessary after source assessment. Merged output is generated; concentration-independent fingerprints do not establish equivalence between other 9 K formulations. No importer, merger, or exporter was executed.

### Organism, growth and application scope

scope: supported. Targets: CultureMech:010265.

The local application is generic microbial cultivation. Neither exact recipe supplies a target organism or direct growth result in this bounded source scope. No taxonomy, incubation optimum, ecological assignment or new growth claim is added.

### Role/property annotations and claim-level evidence

evidence: concern. Targets: CultureMech:010265.

Ingredient notes preserve provider role/property labels as source annotations; they are not experimentally demonstrated functions or growth claims. Both local layers lack claim-level formulation excerpts, and the reference command reports zero checked references. Cite exact amount/form/stage claims at their narrowest field; source URLs in notes remain useful provenance.

### Composition and physical-state classification

scope: concern. Targets: CultureMech:010265.

LIQUID is compatible with the inspected formula, and no contrary organism filing evidence was found within scope. COMPLEX/UNDEFINED lacks a source-specific explanation. The exact primary formula contains specified inorganic salts and an acid stock with stated strength; no undefined organic mixture is listed.

## Findings

### f1: Liquid units, milligram scale and final-volume basis are lost

major / open / confirmed; issue key: CM010265-units-and-final-basis.

Both local layers encode 1 ml of 10 N acid and 1 L water as 1 G_PER_L each, and calcium nitrate 10 mg as 10 G_PER_L. Five other numerical gram amounts match the table but acquire an unstated final-volume denominator. The calcium numerator difference is 1000-fold; it is not a verified final concentration ratio.

### f2: Exact collection pH and sterilization are absent

major / open / confirmed; issue key: CM010265-preparation-and-evidence-omitted.

The exact JCM92 page supplies pH and its applicable default sterilization statement. Neither local layer retains those instructions or claim-level formulation/preparation excerpts. Source URLs in notes remain valid provenance, but the reference diagnostic checks zero reference excerpts.

### f3: Complex/undefined classification lacks formulation support

minor / open / confirmed; issue key: CM010265-composition-classification.

The exact primary formula contains specified inorganic salts and an acid stock with stated strength; no undefined organic mixture is listed. Both local layers retain COMPLEX/UNDEFINED without explaining an undefined constituent; this metadata should be reassessed against the complete source-scoped formulation.

## Recommended Actions And Acceptance Checks

### a1

Restore original batch amounts and unit scale, solvent volume, stock strength and stock addition volume in the maintained owner, with exact source evidence. Normalize final concentrations only if a source-supported final-volume basis is established; keep unsupported denominators explicit.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the exact collection pH and default preparation statement with narrow evidence and source scope. Do not convert sterilization temperature into incubation temperature or infer organism performance; attach exact source snippets to the separately represented amount claims.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

After resolving the exact formulation and its units, assess DEFINED versus any evidenced undefined component and document the classification in the maintained owner. Preserve bacterial filing unless separate organism evidence supports a change.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/9k_medium__4af6025b.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M84_9K_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/9k_medium__4af6025b.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/9k_medium__4af6025b.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch013/128/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch013/128/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/9k_medium__4af6025b.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/9k_medium__4af6025b.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/9k_medium__4af6025b.yaml:1:id: CultureMech:010265<br>./data/normalized_yaml/bacterial/TOGO_M84_9K_Medium.yaml:1:id: CultureMech:010265<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch013/source-preflight-bound/128/source-catalog.json; Entire authoritative per-record bound catalog; all raw, parsed-text and metadata hashes rechecked | supports | 9 bound source captures verified without new retrieval. Original source access times are retained; no capture from another record is silently substituted. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84; $.meta; all eight $.components[0].items; $.comments | supports | M84 identifies original_media_id JCM_M92 and the exact JCM GRMD=92 URL. The provider preserves ingredient masses, a specified acid-stock volume/strength, water volume, and pH context. |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=92; Complete heading 92 9K MEDIUM, ingredient table, pH note and collection-wide sterilization default | supports | The exact collection table agrees with TOGO amounts and units, including calcium nitrate in milligrams and acid/water in volume units. The page supplies a pH note and a default sterilization statement. A solvent amount plus an acid addition is not an explicit measured final volume. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch013/128/quantity-inventory.json; Every listed concentration and separately identified provider-only missing component | context_only | Each decision retains exact source quote(s), stable URL, source locator, original basis, and rationale. Quotations remain separate from conversion or interpretation. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, preferred label, definition, synonyms and obsolete flag | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate; all asserted primary and secondary labels in target and owner match. Chemical source form is separately assessed; existence does not prove every source condition. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, preferred label, definition, synonyms and obsolete flag | supports | CHEBI:15377 resolves to water; all asserted primary and secondary labels in target and owner match. Chemical source form is separately assessed; existence does not prove every source condition. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, preferred label, definition, synonyms and obsolete flag | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate; all asserted primary and secondary labels in target and owner match. Chemical source form is separately assessed; existence does not prove every source condition. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, preferred label, definition, synonyms and obsolete flag | supports | CHEBI:32588 resolves to potassium chloride; all asserted primary and secondary labels in target and owner match. Chemical source form is separately assessed; existence does not prove every source condition. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, preferred label, definition, synonyms and obsolete flag | supports | CHEBI:62946 resolves to ammonium sulfate; all asserted primary and secondary labels in target and owner match. Chemical source form is separately assessed; existence does not prove every source condition. |
| chebi64205 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64205; Exact OLS obo_id, preferred label, definition, synonyms and obsolete flag | supports | CHEBI:64205 resolves to calcium nitrate; all asserted primary and secondary labels in target and owner match. Chemical source form is separately assessed; existence does not prove every source condition. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, preferred label, definition, synonyms and obsolete flag | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate; all asserted primary and secondary labels in target and owner match. Chemical source form is separately assessed; existence does not prove every source condition. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned preferred-term rows for every asserted secondary key; adjacent snapshot metadata | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:64205": [{"label": "Ca(NO3)2", "match_type": "preferred_term", "identifier": "CHEBI:64205", "preferred_term": "Ca(NO3)2", "ontology_id": "CHEBI:64205", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| current-importer | src/culturemech/import/togo_importer.py; _extract_source_info; _is_primary_section; _ingredient_from_item; _extract_preparation_steps; _extract_ph; _convert_to_culturemech; _parse_unit | context_only | Current code recognizes mg/ml/L and preserves comments in recognized primary sections; it defaults medium_type to COMPLEX. _extract_ph reads outer ph while these provider payloads, when pH is present, place it in meta. This is read-time code context, not execution or a historical replay. Source strength, batch basis and final concentration still need explicit review; regeneration alone is not asserted to repair these owner bytes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No exhaustive organism-growth or cross-corpus synonym search was performed. Missing optional taxonomy/solution links are not automatically errors. No source stock strength is treated as a final-medium concentration, and no density, purity, hydrated form, or final-volume denominator is invented.
- The primary source is available and assessed, but it does not make the final-volume denominator explicit. Completed review means the record and this limitation were assessed, not that the recipe has been corrected or scientifically approved.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T091840Z-culturemech-010265-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 9k_medium (CultureMech:010265)'
started_at: '2026-10-21T09:12:09Z'
finished_at: '2026-10-21T09:18:40Z'
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
summary: TOGO M84 explicitly identifies JCM92. The exact collection recipe and provider
  agree, but both local layers encode stock and solvent volumes as mass concentrations,
  lose the calcium-nitrate milligram scale, omit pH/sterilization context, and retain
  an unexplained complex/undefined classification. All eight quantities were reviewed
  without assuming a final-volume denominator.
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
  - path: data/merge_yaml/merged/9k_medium__4af6025b.yaml
    sha256: 2d948c7aa9adb3dcc0cc045af95be207c3ab50b1ae91b198a7f0de32e6021847
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M84_9K_Medium.yaml
    sha256: 1a648d91304a347fd64d4b50f8f8219b5d136b376ed22cc1ced16a9a40220770
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
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
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
  selection: Task review 128; batch 013 item 8 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twelve task batches contain
    120 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 122 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010265
targets:
- target_id: CultureMech:010265
  path: data/merge_yaml/merged/9k_medium__4af6025b.yaml
  label: 9k_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M84_9K_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/9k_medium__4af6025b.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/9k_medium__4af6025b.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch013/128/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch013/128/strict.tsv"
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/9k_medium__4af6025b.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/9k_medium__4af6025b.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010265
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
  - CultureMech:010265
- check_id: upstream-primary-source
  name: Exact JCM92 primary source
  required: true
  status: passed
  summary: The cited JCM GRMD=92 page was inspected in full and agrees with the exact
    TOGO accession and literal table values. Unstated final-volume basis is retained
    as a source limitation.
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - jcm
  - togo
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/9k_medium__4af6025b.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T09:18:39Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M84_9K_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T09:18:39Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/9k_medium__4af6025b.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:01.714236Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/9k_medium__4af6025b.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch013/128/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:03.370838Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch013/128/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/9k_medium__4af6025b.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:07.731398Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/9k_medium__4af6025b.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:11.321044Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T09:18:39Z'
  support: supports
  summary: './data/merge_yaml/merged/9k_medium__4af6025b.yaml:1:id: CultureMech:010265

    ./data/normalized_yaml/bacterial/TOGO_M84_9K_Medium.yaml:1:id: CultureMech:010265

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch013/source-preflight-bound/128/source-catalog.json
  locator: Entire authoritative per-record bound catalog; all raw, parsed-text and
    metadata hashes rechecked
  accessed_at: '2026-10-21T09:18:39Z'
  support: supports
  summary: 9 bound source captures verified without new retrieval. Original source
    access times are retained; no capture from another record is silently substituted.
  snapshot_sha256: db86f79012d468b0ebf2858750060e19db17ee622cbfb9a0185b7fef8b565363
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84
  locator: $.meta; all eight $.components[0].items; $.comments
  accessed_at: '2026-10-21T09:01:28.211799Z'
  support: supports
  summary: M84 identifies original_media_id JCM_M92 and the exact JCM GRMD=92 URL.
    The provider preserves ingredient masses, a specified acid-stock volume/strength,
    water volume, and pH context.
  snapshot_sha256: bb7c44fe48126fab7e68d41a48fa6f7fe5df1f8ccaf862ebcf832253f9a8c77b
- evidence_id: jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=92
  locator: Complete heading 92 9K MEDIUM, ingredient table, pH note and collection-wide
    sterilization default
  accessed_at: '2026-10-21T09:00:12.131955Z'
  support: supports
  summary: The exact collection table agrees with TOGO amounts and units, including
    calcium nitrate in milligrams and acid/water in volume units. The page supplies
    a pH note and a default sterilization statement. A solvent amount plus an acid
    addition is not an explicit measured final volume.
  snapshot_sha256: 3d608a40d0c3ac9e54aef695416957a54497252d2da61c1b12a481b88455bc2d
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch013/128/quantity-inventory.json
  locator: Every listed concentration and separately identified provider-only missing
    component
  accessed_at: '2026-10-21T09:18:39Z'
  support: context_only
  summary: Each decision retains exact source quote(s), stable URL, source locator,
    original basis, and rationale. Quotations remain separate from conversion or interpretation.
  snapshot_sha256: 33ce17db3c627e598468708c18ef38b202e5222910c395325ca63995fac73feb
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS obo_id, preferred label, definition, synonyms and obsolete flag
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate; all asserted primary
    and secondary labels in target and owner match. Chemical source form is separately
    assessed; existence does not prove every source condition.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS obo_id, preferred label, definition, synonyms and obsolete flag
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: CHEBI:15377 resolves to water; all asserted primary and secondary labels
    in target and owner match. Chemical source form is separately assessed; existence
    does not prove every source condition.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS obo_id, preferred label, definition, synonyms and obsolete flag
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate; all asserted primary
    and secondary labels in target and owner match. Chemical source form is separately
    assessed; existence does not prove every source condition.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS obo_id, preferred label, definition, synonyms and obsolete flag
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: CHEBI:32588 resolves to potassium chloride; all asserted primary and secondary
    labels in target and owner match. Chemical source form is separately assessed;
    existence does not prove every source condition.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS obo_id, preferred label, definition, synonyms and obsolete flag
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: CHEBI:62946 resolves to ammonium sulfate; all asserted primary and secondary
    labels in target and owner match. Chemical source form is separately assessed;
    existence does not prove every source condition.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi64205
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64205
  locator: Exact OLS obo_id, preferred label, definition, synonyms and obsolete flag
  accessed_at: '2026-10-21T09:00:12.945373Z'
  support: supports
  summary: CHEBI:64205 resolves to calcium nitrate; all asserted primary and secondary
    labels in target and owner match. Chemical source form is separately assessed;
    existence does not prove every source condition.
  snapshot_sha256: cf808711c3d8005562d7cb492a9da7abcb7a9ae6334934a1f4c5bafd1bd86062
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS obo_id, preferred label, definition, synonyms and obsolete flag
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate; all asserted primary
    and secondary labels in target and owner match. Chemical source form is separately
    assessed; existence does not prove every source condition.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned preferred-term rows for every asserted secondary key; adjacent snapshot
    metadata
  accessed_at: '2026-10-21T09:18:39Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588":
    [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588",
    "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type":
    "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4",
    "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:64205": [{"label": "Ca(NO3)2", "match_type": "preferred_term", "identifier":
    "CHEBI:64205", "preferred_term": "Ca(NO3)2", "ontology_id": "CHEBI:64205", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: current-importer
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_source_info; _is_primary_section; _ingredient_from_item; _extract_preparation_steps;
    _extract_ph; _convert_to_culturemech; _parse_unit
  accessed_at: '2026-10-21T09:18:39Z'
  support: context_only
  summary: Current code recognizes mg/ml/L and preserves comments in recognized primary
    sections; it defaults medium_type to COMPLEX. _extract_ph reads outer ph while
    these provider payloads, when pH is present, place it in meta. This is read-time
    code context, not execution or a historical replay. Source strength, batch basis
    and final concentration still need explicit review; regeneration alone is not
    asserted to repair these owner bytes.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact collection/provider accession and owner
  outcome: supported
  summary: TOGO M84, original JCM_M92 and the cited collection URL identify one source
    formulation. The generated target and sole maintained owner share a stable ID
    and identical maintained content. Other 9 K names and the distinct sulfur variant
    are outside this review.
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - record
  - owner-0
  - id-search
  - togo
  - jcm
- assessment_id: quantities
  area: quantity
  topic: Every listed amount, unit and denominator
  outcome: concern
  summary: 'All eight rows are inventoried: acid addition, solvent volume and calcium-nitrate
    scale require correction; five other mass literals match the exact table but their
    final-volume denominator is unsupported. The only arithmetic is 10 mg = 0.010
    g at the unchanged source batch level. No sum of nominal liquid volumes is asserted
    as measured final volume.'
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  - quantity-inventory
  details: '[{"field_path": "ingredients[0].concentration", "name": "10 N H2SO4",
    "stored": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "source_context":
    "The source is a 1 ml addition of 10 N sulfuric-acid stock, not 1 G_PER_L. Normality
    is stock strength; no density, molarity conversion or final-medium acid concentration
    is inferred.", "source_snippets": [{"source_key": "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84",
    "source_locator": "$.components[0].items[0]", "exact_source_quote": "          \"component_name\":
    \"10 N H2SO4\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"conc_value\":
    10,\n          \"conc_unit\": \"N\","}]}, {"field_path": "ingredients[1].concentration",
    "name": "Distilled water", "stored": {"value": "1", "unit": "G_PER_L"}, "decision":
    "correct", "source_context": "The source gives 1 L distilled water as solvent
    volume, not 1 G_PER_L. Additional acid volume does not establish a measured final-volume
    denominator.", "source_snippets": [{"source_key": "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84",
    "source_locator": "$.components[0].items[1]", "exact_source_quote": "          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\","}]},
    {"field_path": "ingredients[2].concentration", "name": "MgSO4・7H2O", "stored":
    {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "source_context":
    "The numerical mass literal matches the source table in grams, but the stored
    G_PER_L final-concentration basis is not independently established by a 1 L water
    amount plus an acid addition. Preserve the reported batch mass; do not assume
    a final denominator or silently rescale.", "source_snippets": [{"source_key":
    "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84",
    "source_locator": "$.components[0].items[2]", "exact_source_quote": "          \"component_name\":
    \"MgSO4・7H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\","}]}, {"field_path":
    "ingredients[3].concentration", "name": "K2HPO4", "stored": {"value": "0.5", "unit":
    "G_PER_L"}, "decision": "unsupported", "source_context": "The numerical mass literal
    matches the source table in grams, but the stored G_PER_L final-concentration
    basis is not independently established by a 1 L water amount plus an acid addition.
    Preserve the reported batch mass; do not assume a final denominator or silently
    rescale.", "source_snippets": [{"source_key": "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84",
    "source_locator": "$.components[0].items[3]", "exact_source_quote": "          \"component_name\":
    \"K2HPO4\",\n          \"volume\": 0.5,\n          \"unit\": \"g\","}]}, {"field_path":
    "ingredients[4].concentration", "name": "FeSO4・7H2O", "stored": {"value": "50",
    "unit": "G_PER_L"}, "decision": "unsupported", "source_context": "The numerical
    mass literal matches the source table in grams, but the stored G_PER_L final-concentration
    basis is not independently established by a 1 L water amount plus an acid addition.
    Preserve the reported batch mass; do not assume a final denominator or silently
    rescale.", "source_snippets": [{"source_key": "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84",
    "source_locator": "$.components[0].items[4]", "exact_source_quote": "          \"component_name\":
    \"FeSO4・7H2O\",\n          \"volume\": 50,\n          \"unit\": \"g\","}]}, {"field_path":
    "ingredients[5].concentration", "name": "KCl", "stored": {"value": "0.1", "unit":
    "G_PER_L"}, "decision": "unsupported", "source_context": "The numerical mass literal
    matches the source table in grams, but the stored G_PER_L final-concentration
    basis is not independently established by a 1 L water amount plus an acid addition.
    Preserve the reported batch mass; do not assume a final denominator or silently
    rescale.", "source_snippets": [{"source_key": "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84",
    "source_locator": "$.components[0].items[5]", "exact_source_quote": "          \"component_name\":
    \"KCl\",\n          \"volume\": 0.1,\n          \"unit\": \"g\","}]}, {"field_path":
    "ingredients[6].concentration", "name": "(NH4)2SO4", "stored": {"value": "3",
    "unit": "G_PER_L"}, "decision": "unsupported", "source_context": "The numerical
    mass literal matches the source table in grams, but the stored G_PER_L final-concentration
    basis is not independently established by a 1 L water amount plus an acid addition.
    Preserve the reported batch mass; do not assume a final denominator or silently
    rescale.", "source_snippets": [{"source_key": "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84",
    "source_locator": "$.components[0].items[6]", "exact_source_quote": "          \"component_name\":
    \"(NH4)2SO4\",\n          \"volume\": 3,\n          \"unit\": \"g\","}]}, {"field_path":
    "ingredients[7].concentration", "name": "Ca(NO3)2", "stored": {"value": "10",
    "unit": "G_PER_L"}, "decision": "correct", "source_context": "Source calcium nitrate
    is 10 mg per listed preparation, equal to 0.010 g in that same source batch. Stored
    10 G_PER_L loses the mg/g scale (1000-fold numerator difference) and adds an unverified
    final-volume denominator. No 0.010 G_PER_L final value is assumed.", "source_snippets":
    [{"source_key": "togoM84", "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M84",
    "source_locator": "$.components[0].items[7]", "exact_source_quote": "          \"component_name\":
    \"Ca(NO3)2\",\n          \"volume\": 10,\n          \"unit\": \"mg\","}]}]'
- assessment_id: preparation
  area: completeness
  topic: Collection pH and sterilization context
  outcome: concern
  summary: The collection page states pH 3.0 and a default of autoclaving at 121°C
    for 15 min unless otherwise stated; this medium provides no exception. Both local
    layers omit pH and preparation/sterilization. This is medium preparation context,
    not incubation temperature or an organism optimum.
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
- assessment_id: solutions
  area: representation
  topic: Quantified acid-stock addition
  outcome: concern
  summary: The acid has an explicitly specified stock strength and addition volume
    in both sources, but the local ingredient concentration treats it as mass per
    volume. No solution ID is asserted, so no replacement stock identity is invented.
    Preserve stock strength and addition amount separately from final-medium concentration.
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
- assessment_id: grounding
  area: grounding
  topic: Every target/owner primary and secondary identifier
  outcome: supported
  summary: 7/8 target ingredient instances have primary CHEBI IDs; 5/8 have current
    secondary keys. All asserted target and owner IDs resolve to matching nonobsolete
    OLS labels; every secondary key has a live preferred-term row in the pinned MIM
    index.
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - record
  - owner-0
  - mim
  - chebi131527
  - chebi15377
  - chebi31795
  - chebi32588
  - chebi62946
  - chebi64205
  - chebi75836
  details: 'Linkage metrics use 8 direct ingredient instances as each denominator
    and a 0–100 percent scale: primary 87.50%; secondary 62.50%. They are not scientific
    correctness scores. Missing optional links are not wrong IDs; no replacement term
    is invented.'
- assessment_id: forms
  area: grounding
  topic: Exact supplied forms and ontology limits
  outcome: supported
  summary: All seven asserted chemical IDs match the exact named salts or water, including
    magnesium and iron sulfate heptahydrates. Source calcium nitrate has no additional
    hydrate specification to infer. The acid stock is ungrounded rather than assigned
    an unsupported molecule/mixture identity. Five current secondary keys resolve;
    missing links for the two hydrated sulfates remain optional linkage opportunities.
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
  - chebi131527
  - chebi15377
  - chebi31795
  - chebi32588
  - chebi62946
  - chebi64205
  - chebi75836
- assessment_id: history
  area: provenance
  topic: Whole history and maintained-input correspondence
  outcome: supported
  summary: Target 10 and owner 9 history entries (19 timestamp instances) are timezone-aware.
    All maintained content matches; the generated target adds only merge metadata
    and its merge event. Existing import/default/migration/enrichment history is provenance,
    not scientific confirmation. Preserve every old event; append any later authorized
    curation clarification.
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - record
  - owner-0
  - id-search
- assessment_id: process
  area: ownership
  topic: Maintained owner and generator boundaries
  outcome: supported
  summary: Corrections belong in the exact normalized owner, with narrowly scoped
    transformation changes only if necessary after source assessment. Merged output
    is generated; concentration-independent fingerprints do not establish equivalence
    between other 9 K formulations. No importer, merger, or exporter was executed.
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - record
  - owner-0
  - id-search
  - current-importer
  - bound-source-integrity
- assessment_id: organisms
  area: scope
  topic: Organism, growth and application scope
  outcome: supported
  summary: The local application is generic microbial cultivation. Neither exact recipe
    supplies a target organism or direct growth result in this bounded source scope.
    No taxonomy, incubation optimum, ecological assignment or new growth claim is
    added.
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - record
  - owner-0
  - togo
  - jcm
- assessment_id: annotations
  area: evidence
  topic: Role/property annotations and claim-level evidence
  outcome: concern
  summary: Ingredient notes preserve provider role/property labels as source annotations;
    they are not experimentally demonstrated functions or growth claims. Both local
    layers lack claim-level formulation excerpts, and the reference command reports
    zero checked references. Cite exact amount/form/stage claims at their narrowest
    field; source URLs in notes remain useful provenance.
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - record
  - owner-0
  - togo
  - validate-references
- assessment_id: classification
  area: scope
  topic: Composition and physical-state classification
  outcome: concern
  summary: LIQUID is compatible with the inspected formula, and no contrary organism
    filing evidence was found within scope. COMPLEX/UNDEFINED lacks a source-specific
    explanation. The exact primary formula contains specified inorganic salts and
    an acid stock with stated strength; no undefined organic mixture is listed.
  target_ids:
  - CultureMech:010265
  evidence_ids:
  - record
  - owner-0
  - togo
  - current-importer
  - jcm
findings:
- finding_id: f1
  issue_key: CM010265-units-and-final-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Liquid units, milligram scale and final-volume basis are lost
  description: Both local layers encode 1 ml of 10 N acid and 1 L water as 1 G_PER_L
    each, and calcium nitrate 10 mg as 10 G_PER_L. Five other numerical gram amounts
    match the table but acquire an unstated final-volume denominator. The calcium
    numerator difference is 1000-fold; it is not a verified final concentration ratio.
  target_ids:
  - CultureMech:010265
  field_paths:
  - ingredients[*].concentration
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M84_9K_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CM010265-preparation-and-evidence-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Exact collection pH and sterilization are absent
  description: The exact JCM92 page supplies pH and its applicable default sterilization
    statement. Neither local layer retains those instructions or claim-level formulation/preparation
    excerpts. Source URLs in notes remain valid provenance, but the reference diagnostic
    checks zero reference excerpts.
  target_ids:
  - CultureMech:010265
  field_paths:
  - ph_value
  - preparation_steps
  - sterilization
  - evidence
  - references
  - ingredients[*].evidence
  evidence_ids:
  - record
  - owner-0
  - jcm
  - togo
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M84_9K_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3.5 is promoted from usual minor to major because explicit
    applicable sterilization and pH context are entirely absent from both local representations,
    materially reducing faithful preparation completeness.
- finding_id: f3
  issue_key: CM010265-composition-classification
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Complex/undefined classification lacks formulation support
  description: The exact primary formula contains specified inorganic salts and an
    acid stock with stated strength; no undefined organic mixture is listed. Both
    local layers retain COMPLEX/UNDEFINED without explaining an undefined constituent;
    this metadata should be reassessed against the complete source-scoped formulation.
  target_ids:
  - CultureMech:010265
  field_paths:
  - medium_type
  - composition_type
  evidence_ids:
  - record
  - owner-0
  - togo
  - current-importer
  - jcm
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M84_9K_Medium.yaml
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
  description: Restore original batch amounts and unit scale, solvent volume, stock
    strength and stock addition volume in the maintained owner, with exact source
    evidence. Normalize final concentrations only if a source-supported final-volume
    basis is established; keep unsupported denominators explicit.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010265
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M84_9K_Medium.yaml
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
  description: Preserve the exact collection pH and default preparation statement
    with narrow evidence and source scope. Do not convert sterilization temperature
    into incubation temperature or infer organism performance; attach exact source
    snippets to the separately represented amount claims.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010265
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M84_9K_Medium.yaml
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
  description: After resolving the exact formulation and its units, assess DEFINED
    versus any evidenced undefined component and document the classification in the
    maintained owner. Preserve bacterial filing unless separate organism evidence
    supports a change.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010265
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M84_9K_Medium.yaml
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
- No exhaustive organism-growth or cross-corpus synonym search was performed. Missing
  optional taxonomy/solution links are not automatically errors. No source stock strength
  is treated as a final-medium concentration, and no density, purity, hydrated form,
  or final-volume denominator is invented.
- The primary source is available and assessed, but it does not make the final-volume
  denominator explicit. Completed review means the record and this limitation were
  assessed, not that the recipe has been corrected or scientifically approved.
tags:
- unreviewed-records
- batch-013
- generated-medium
```
