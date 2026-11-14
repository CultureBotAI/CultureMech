# Source and formulation review: 2_mh_medium (CultureMech:001751)

- Review: 20261021T075408Z-culturemech-001751-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T07:45:22Z
- Finished UTC: 2026-10-21T07:54:08Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 620 and MediaDive support the seven named solutes and provider-declared concentrations, but methanol 20 g/L suppresses the primary recipe's unresolved 2% basis. Glucose/methanol filtration and the water instruction are omitted. Five verified concentration excerpts present in the maintained DSMZ owner have not reached the generated target. Both maintained owners and their reciprocal source-duplicate links were inspected; exact KOMODO source verification remains limited by HTTP 403.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 85; batch 009 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding eight task batches contain 80 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 82 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001751 | data/merge_yaml/merged/2_mh_medium.yaml | generated | 2_mh_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001751 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001751 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-009/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch009/085/strict.tsv |
| validate-terms | passed | True | CultureMech:001751 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001751 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001751 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact KOMODO provider-row verification | unavailable | True | CultureMech:001751 | Captured exact MediaList request returned HTTP 403; no exact medium-620 row was available for source comparison. This is an HTTP outcome, not a command exit code. The successful DSMZ PDF/API reads support DSMZ formulation only. |
| Asserted KG-Microbe correspondence applicability | not_applicable | False | CultureMech:001751 | The target and both owners assert no kg_microbe_match. The documented exact graph-set check was not run and no graph identity claim is made. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001751.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:001751.

7 primary CHEBI identities resolve with matching labels; 7 of 7 current secondary keys have live pinned-index rows. Unresolved keys: [].

7 direct ingredient instances; CHEBI-primary instance linkage 7/7 (100.00%), verified secondary coverage 7/7 (100.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### DSMZ source identity and both maintained owners

identity: supported. Targets: CultureMech:001751.

DSMZ PDF 620 and the MediaDive medium/solution response identify this formulation. Both maintained owners have the same seven names, concentrations and chemical IDs. Reciprocal source-duplicate descriptors resolve to the two actual stable IDs and paths; the KOMODO ingredients were explicitly copied from DSMZ, not an independent experimental confirmation.

### Every ingredient amount and source-only water

quantity: concern. Targets: CultureMech:001751.

All seven stored values equal provider g_l; the six non-methanol mass amounts and hydrate forms also agree with the primary PDF. Iron sulfate 2 mg correctly corresponds to 0.002 g/L under the API-declared 1000 ml basis. Methanol 20 g/L retains only the provider normalization and loses the unqualified primary 2% amount. Water 1000 ml is a preparation instruction, not an extra solute concentration.

[{"field_path": "ingredients[0].concentration", "ingredient": "Glucose", "current": {"value": "1.5", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[0]", "source_amount": 1.5, "source_unit": "g", "provider_g_l": 1.5, "source_attribute": "filter-sterilized", "same_value_in_target_and_both_owners": true, "assessment": "Supported as the provider-declared main-solution concentration; primary PDF confirms amount and chemical form.", "arithmetic": "1.5 g × 1 g/g / (1000 ml / 1000 ml per L) = 1.5 g/L; denominator comes from the API solution-volume field, not from water addition alone."}, {"field_path": "ingredients[1].concentration", "ingredient": "KH2PO4", "current": {"value": "2", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[1]", "source_amount": 2, "source_unit": "g", "provider_g_l": 2, "source_attribute": null, "same_value_in_target_and_both_owners": true, "assessment": "Supported as the provider-declared main-solution concentration; primary PDF confirms amount and chemical form.", "arithmetic": "2 g × 1 g/g / (1000 ml / 1000 ml per L) = 2 g/L; denominator comes from the API solution-volume field, not from water addition alone."}, {"field_path": "ingredients[2].concentration", "ingredient": "(NH4)2SO4", "current": {"value": "2", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[2]", "source_amount": 2, "source_unit": "g", "provider_g_l": 2, "source_attribute": null, "same_value_in_target_and_both_owners": true, "assessment": "Supported as the provider-declared main-solution concentration; primary PDF confirms amount and chemical form.", "arithmetic": "2 g × 1 g/g / (1000 ml / 1000 ml per L) = 2 g/L; denominator comes from the API solution-volume field, not from water addition alone."}, {"field_path": "ingredients[3].concentration", "ingredient": "MgSO4 x 7 H2O", "current": {"value": "0.025", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[3]", "source_amount": 0.025, "source_unit": "g", "provider_g_l": 0.025, "source_attribute": null, "same_value_in_target_and_both_owners": true, "assessment": "Supported as the provider-declared main-solution concentration; primary PDF confirms amount and chemical form.", "arithmetic": "0.025 g × 1 g/g / (1000 ml / 1000 ml per L) = 0.025 g/L; denominator comes from the API solution-volume field, not from water addition alone."}, {"field_path": "ingredients[4].concentration", "ingredient": "NaCl", "current": {"value": "0.5", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[4]", "source_amount": 0.5, "source_unit": "g", "provider_g_l": 0.5, "source_attribute": null, "same_value_in_target_and_both_owners": true, "assessment": "Supported as the provider-declared main-solution concentration; primary PDF confirms amount and chemical form.", "arithmetic": "0.5 g × 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L; denominator comes from the API solution-volume field, not from water addition alone."}, {"field_path": "ingredients[5].concentration", "ingredient": "FeSO4 x 7 H2O", "current": {"value": "0.002", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[5]", "source_amount": 2, "source_unit": "mg", "provider_g_l": 0.002, "source_attribute": null, "same_value_in_target_and_both_owners": true, "assessment": "Supported as the provider-declared main-solution concentration; primary PDF confirms amount and chemical form.", "arithmetic": "2 mg × 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.002 g/L; denominator comes from the API solution-volume field, not from water addition alone."}, {"field_path": "ingredients[6].concentration", "ingredient": "Methanol", "current": {"value": "20", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[7]", "source_amount": 2, "source_unit": "%", "provider_g_l": 20, "source_attribute": "filter-sterilized", "same_value_in_target_and_both_owners": true, "assessment": "Local 20 g/L exactly follows the provider g_l field; original PDF/API 2% lacks w/v, v/v or w/w qualification, so its primary-source basis is unresolved.", "conditional_arithmetic": "If 2% means w/v, 2 g per 100 ml gives 20 g/L. If it means v/v, it describes a different quantity basis; no density conversion or final receiving-volume assumption is made. Neither interpretation is independently selected here."}, {"field_path": "preparation_steps", "source_only_component": "Distilled water", "source_locator": "$.data.solutions[0].recipe[6]; DSMZ PDF water row", "source_amount": 1000, "source_unit": "ml", "assessment": "Source water instruction is absent from target and both owners. Preserve it in preparation context; it is not a missing gram-per-litre solute or independent proof of an exact final volume after methanol addition."}]

### Filtration, water instruction and pH

completeness: concern. Targets: CultureMech:001751.

The pH range 7.0–7.5 is retained correctly, though the target/DSMZ preparation step is merely a MIX-labelled pH note. Both sources mark glucose and methanol as filter-sterilized and list water 1000 ml; these instructions are absent from all local layers. The source supplies no filtration pore size, time/temperature, autoclave regimen, addition timing or explicit final-volume closure, so none should be invented.

### Existing owner excerpts and generated evidence drift

evidence: concern. Targets: CultureMech:001751.

All five parent excerpts at ingredients[1:6] are exact substrings of the current raw response and match their JSON rows, source URL and reported hash. They support only KH2PO4, ammonium sulfate, MgSO4 heptahydrate, NaCl and FeSO4 heptahydrate provider concentrations. Neither glucose nor methanol has an existing excerpt. The generated target has no excerpts or reference list, so its zero reference checks do not assess the maintained parent evidence.

### Defined liquid medium, duplicate scope and growth limits

scope: supported. Targets: CultureMech:001751.

The seven named pure compounds, no complex ingredients, no solidifier, and provider complex_medium=no support DEFINED/DEFINED and LIQUID. Bacterial placement and generic microbial-cultivation application supply no organism or strain-specific growth evidence. SOURCE_DUPLICATE describes the documented local copied composition, not a distinct biological variant. No CHEBI ingredient-set match to KG-Microbe is asserted or inferred.

### Unavailable exact KOMODO row and oxygen annotation

provenance: unknown. Targets: CultureMech:001751.

The maintained KOMODO owner names accession 620, DSMZ 620 and Aerobic: No. Its exact MediaList source is unavailable with HTTP 403. The local DSMZ-copy event and reciprocal duplicate links are readable, but accession correspondence and the oxygen flag remain unverified at the upstream row. Neither the DSMZ recipe nor the boolean import code establishes anaerobic growth or obligate physiology.

### All target and owner history timestamps

provenance: concern. Targets: CultureMech:001751.

Target and DSMZ-owner history timestamps are timezone-aware. The KOMODO owner has a malformed .fZ timestamp at event 0 and an otherwise parseable timezone-free timestamp at event 1. Preserve those original events and document any correction with independent timing evidence; do not guess a timezone or rewrite the append-only history.

## Findings

### f1: Methanol percent basis is hidden by provider normalization

major / open / confirmed; issue key: CM001751-methanol-basis.

All three local files assert methanol 20 g/L. This matches MediaDive g_l=20, but the same provider row and DSMZ PDF give original amount 2 with an unqualified percent unit. The records preserve neither that original amount nor the unresolved basis. The value is provider-backed, not independently established as a primary-source w/v concentration.

### f2: Ingredient-specific filtration and water instruction are omitted

major / open / confirmed; issue key: CM001751-source-preparation.

The PDF and API mark glucose and methanol as filter-sterilized and list distilled water 1000 ml. None of the target or two owners retains these instructions. The pH-only MIX note in the target and DSMZ owner is not a complete preparation representation.

### f3: Generated record predates five verified owner evidence additions

major / open / confirmed; issue key: CM001751-owner-evidence-drift.

The maintained DSMZ owner contains five exact API excerpts for ingredients[1:6], one reference and the 2026-10-07 evidence-curation event. The generated target last merged on 2026-08-06 and lacks all five excerpts and the reference. Its reference check examined zero excerpts, despite the maintained evidence now being available.

### f4: KOMODO contributor history contains malformed and timezone-free times

minor / open / confirmed; issue key: CM001751-contributor-history.

The KOMODO maintained input has 2026-01-27T01:15:03.fZ at curation_history[0] and 2026-02-03T11:19:00.544807 without a timezone at curation_history[1]. The target and DSMZ owner do not share these two timestamp defects; their successful target-only schema check does not validate this contributor history.

## Recommended Actions And Acceptance Checks

### a1

Retain the exact original 2% source amount and the separate provider g_l=20 assertion with claim-level provenance and explicit basis uncertainty. Resolve the percentage basis before asserting a conversion; do not substitute v/v, use an assumed density, or declare 20 g/L numerically false without new evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore glucose/methanol filtration qualifiers and the literal water instruction at maintained-input preparation scope, preserving the correct pH range. Do not turn water addition into an asserted final-volume closure, or invent filtration pore size, sterilization timing, autoclaving or adjustment reagents.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the verified parent evidence and refresh the generated record only after maintained-input review and separately authorized regeneration. Verify the five exact excerpts, reference and source-history provenance survive. Add narrow evidence for glucose and qualified methanol separately; do not treat these five excerpts as validating all ingredients or proving methanol percent basis.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Retain the original events and append a corrective provenance note supported by an actual source log if available. Correct future KOMODO timestamp generation without inventing historical fractional seconds or timezone; leave unresolved timing explicit.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/2_mh_medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/2_mh_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/2_mh_medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/2_mh_medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch009/085/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-009/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch009/085/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/2_mh_medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/2_mh_medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/2_mh_medium.yaml:1:id: CultureMech:001751<br>./data/normalized_yaml/bacterial/2_mh_medium.yaml:1:id: CultureMech:001751<br> |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17234 resolves to glucose and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17790 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17790; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17790 resolves to methanol and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:62946 resolves to ammonium sulfate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17790": [{"label": "Methanol", "match_type": "preferred_term", "identifier": "CHEBI:17790", "preferred_term": "Methanol", "ontology_id": "CHEBI:17790", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| dsmz | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium620.pdf; Page 1, heading 620. 2% MH MEDIUM; complete ingredient table and pH line | supports | The complete one-page DSMZ 620 recipe lists glucose 1.500 g, KH2PO4 2.000 g, ammonium sulfate 2.000 g, magnesium sulfate heptahydrate 0.025 g, NaCl 0.500 g, iron(II) sulfate heptahydrate 2.000 mg, distilled water 1000.000 ml, and methanol 2.000 percent. Glucose and methanol carry filter-sterilized qualifiers. The pH is 7–7.5. The PDF does not specify the percent basis, final-volume closure, a filtration pore size, a methanol density, or an autoclaving procedure. |
| mediadive | https://mediadive.dsmz.de/rest/medium/620; $.data.medium; $.data.solutions[0].id, volume, recipe[0:8], steps | supports | The captured response identifies DSMZ medium 620 and one main solution, ID 1329, with declared volume 1000 ml. Its eight rows include six solute mass amounts, water 1000 ml, and methanol amount 2 with unit percent while separately declaring g_l=20. Glucose and methanol attributes retain filter-sterilized. Medium min_pH/max_pH and the sole step specify 7–7.5; complex_medium is no. These are provider-declared amounts, not independent experimental concentration measurements. |
| komodo-access | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact MediaList endpoint used by the checked-in KOMODO web fetcher; captured response and HTTP metadata | context_only | The exact endpoint returned HTTP 403 with a JavaScript/cookie challenge. This is evidence of unavailable source access, not evidence that KOMODO medium 620 or its metadata is absent or false. The original access time and failed-response hash are retained. |
| amount-trace | data/merge_yaml/merged/2_mh_medium.yaml; All seven ingredient concentration nodes in target and both owners; source-only water instruction | supports | [{"field_path": "ingredients[0].concentration", "ingredient": "Glucose", "current": {"value": "1.5", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[0]", "source_amount": 1.5, "source_unit": "g", "provider_g_l": 1.5, "source_attribute": "filter-sterilized", "same_value_in_target_and_both_owners": true, "assessment": "Supported as the provider-declared main-solution concentration; primary PDF confirms amount and chemical form.", "arithmetic": "1.5 g × 1 g/g / (1000 ml / 1000 ml per L) = 1.5 g/L; denominator comes from the API solution-volume field, not from water addition alone."}, {"field_path": "ingredients[1].concentration", "ingredient": "KH2PO4", "current": {"value": "2", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[1]", "source_amount": 2, "source_unit": "g", "provider_g_l": 2, "source_attribute": null, "same_value_in_target_and_both_owners": true, "assessment": "Supported as the provider-declared main-solution concentration; primary PDF confirms amount and chemical form.", "arithmetic": "2 g × 1 g/g / (1000 ml / 1000 ml per L) = 2 g/L; denominator comes from the API solution-volume field, not from water addition alone."}, {"field_path": "ingredients[2].concentration", "ingredient": "(NH4)2SO4", "current": {"value": "2", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[2]", "source_amount": 2, "source_unit": "g", "provider_g_l": 2, "source_attribute": null, "same_value_in_target_and_both_owners": true, "assessment": "Supported as the provider-declared main-solution concentration; primary PDF confirms amount and chemical form.", "arithmetic": "2 g × 1 g/g / (1000 ml / 1000 ml per L) = 2 g/L; denominator comes from the API solution-volume field, not from water addition alone."}, {"field_path": "ingredients[3].concentration", "ingredient": "MgSO4 x 7 H2O", "current": {"value": "0.025", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[3]", "source_amount": 0.025, "source_unit": "g", "provider_g_l": 0.025, "source_attribute": null, "same_value_in_target_and_both_owners": true, "assessment": "Supported as the provider-declared main-solution concentration; primary PDF confirms amount and chemical form.", "arithmetic": "0.025 g × 1 g/g / (1000 ml / 1000 ml per L) = 0.025 g/L; denominator comes from the API solution-volume field, not from water addition alone."}, {"field_path": "ingredients[4].concentration", "ingredient": "NaCl", "current": {"value": "0.5", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[4]", "source_amount": 0.5, "source_unit": "g", "provider_g_l": 0.5, "source_attribute": null, "same_value_in_target_and_both_owners": true, "assessment": "Supported as the provider-declared main-solution concentration; primary PDF confirms amount and chemical form.", "arithmetic": "0.5 g × 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L; denominator comes from the API solution-volume field, not from water addition alone."}, {"field_path": "ingredients[5].concentration", "ingredient": "FeSO4 x 7 H2O", "current": {"value": "0.002", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[5]", "source_amount": 2, "source_unit": "mg", "provider_g_l": 0.002, "source_attribute": null, "same_value_in_target_and_both_owners": true, "assessment": "Supported as the provider-declared main-solution concentration; primary PDF confirms amount and chemical form.", "arithmetic": "2 mg × 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.002 g/L; denominator comes from the API solution-volume field, not from water addition alone."}, {"field_path": "ingredients[6].concentration", "ingredient": "Methanol", "current": {"value": "20", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[7]", "source_amount": 2, "source_unit": "%", "provider_g_l": 20, "source_attribute": "filter-sterilized", "same_value_in_target_and_both_owners": true, "assessment": "Local 20 g/L exactly follows the provider g_l field; original PDF/API 2% lacks w/v, v/v or w/w qualification, so its primary-source basis is unresolved.", "conditional_arithmetic": "If 2% means w/v, 2 g per 100 ml gives 20 g/L. If it means v/v, it describes a different quantity basis; no density conversion or final receiving-volume assumption is made. Neither interpretation is independently selected here."}, {"field_path": "preparation_steps", "source_only_component": "Distilled water", "source_locator": "$.data.solutions[0].recipe[6]; DSMZ PDF water row", "source_amount": 1000, "source_unit": "ml", "assessment": "Source water instruction is absent from target and both owners. Preserve it in preparation context; it is not a missing gram-per-litre solute or independent proof of an exact final volume after methanol addition."}] |
| existing-evidence | data/normalized_yaml/bacterial/2_mh_medium.yaml; ingredients[1:6].evidence[0]; references[0]; curation_history[7]; comparison with target | supports | {"verified_excerpts": [{"owner_path": "data/normalized_yaml/bacterial/2_mh_medium.yaml", "field_path": "ingredients[1].evidence[0]", "source_locator": "$.data.solutions[0].recipe[1]", "literal_snippet_matches_current_capture": true, "current_capture_sha256": "1f063fe21456c04e7a448ee3bfd14ca43e3e33db209ebebd1c4e078f89d45263", "scope": "Exact provider row and declared main-solution concentration only; does not verify the ingredient ontology mapping or methanol percent basis."}, {"owner_path": "data/normalized_yaml/bacterial/2_mh_medium.yaml", "field_path": "ingredients[2].evidence[0]", "source_locator": "$.data.solutions[0].recipe[2]", "literal_snippet_matches_current_capture": true, "current_capture_sha256": "1f063fe21456c04e7a448ee3bfd14ca43e3e33db209ebebd1c4e078f89d45263", "scope": "Exact provider row and declared main-solution concentration only; does not verify the ingredient ontology mapping or methanol percent basis."}, {"owner_path": "data/normalized_yaml/bacterial/2_mh_medium.yaml", "field_path": "ingredients[3].evidence[0]", "source_locator": "$.data.solutions[0].recipe[3]", "literal_snippet_matches_current_capture": true, "current_capture_sha256": "1f063fe21456c04e7a448ee3bfd14ca43e3e33db209ebebd1c4e078f89d45263", "scope": "Exact provider row and declared main-solution concentration only; does not verify the ingredient ontology mapping or methanol percent basis."}, {"owner_path": "data/normalized_yaml/bacterial/2_mh_medium.yaml", "field_path": "ingredients[4].evidence[0]", "source_locator": "$.data.solutions[0].recipe[4]", "literal_snippet_matches_current_capture": true, "current_capture_sha256": "1f063fe21456c04e7a448ee3bfd14ca43e3e33db209ebebd1c4e078f89d45263", "scope": "Exact provider row and declared main-solution concentration only; does not verify the ingredient ontology mapping or methanol percent basis."}, {"owner_path": "data/normalized_yaml/bacterial/2_mh_medium.yaml", "field_path": "ingredients[5].evidence[0]", "source_locator": "$.data.solutions[0].recipe[5]", "literal_snippet_matches_current_capture": true, "current_capture_sha256": "1f063fe21456c04e7a448ee3bfd14ca43e3e33db209ebebd1c4e078f89d45263", "scope": "Exact provider row and declared main-solution concentration only; does not verify the ingredient ontology mapping or methanol percent basis."}], "source_reference_matches": true, "target_excerpts": 0, "target_references": 0, "chronology": "The target merge event is 2026-08-06; the maintained parent added these five excerpts and reference on 2026-10-07. The artifact is stale relative to this evidence addition; no claim is made that the current merger would discard it."} |
| history | data/merge_yaml/merged/2_mh_medium.yaml; data/normalized_yaml/bacterial/2_mh_medium.yaml; data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml; All history events: target 9, DSMZ owner 8, KOMODO owner 8; reciprocal parent/child descriptors | supports | {"events": [{"layer": "target", "index": 0, "timestamp": "2026-01-26T17:53:11.754287Z", "assessment": "timezone-aware ISO timestamp"}, {"layer": "target", "index": 1, "timestamp": "2026-03-13T06:19:06.949204Z", "assessment": "timezone-aware ISO timestamp"}, {"layer": "target", "index": 2, "timestamp": "2026-03-17T06:30:53.000000Z", "assessment": "timezone-aware ISO timestamp"}, {"layer": "target", "index": 3, "timestamp": "2026-03-17T19:45:19.189976+00:00", "assessment": "timezone-aware ISO timestamp"}, {"layer": "target", "index": 4, "timestamp": "2026-05-20T06:00:46.876250+00:00", "assessment": "timezone-aware ISO timestamp"}, {"layer": "target", "index": 5, "timestamp": "2026-06-05T07:40:15.758614+00:00", "assessment": "timezone-aware ISO timestamp"}, {"layer": "target", "index": 6, "timestamp": "2026-06-10T07:46:42.537571+00:00", "assessment": "timezone-aware ISO timestamp"}, {"layer": "target", "index": 7, "timestamp": "2026-08-06T03:04:34.040528+00:00", "assessment": "timezone-aware ISO timestamp"}, {"layer": "target", "index": 8, "timestamp": "2026-08-06T03:04:34.040563+00:00", "assessment": "timezone-aware ISO timestamp"}, {"layer": "DSMZ owner", "index": 0, "timestamp": "2026-01-26T17:53:11.754287Z", "assessment": "timezone-aware ISO timestamp"}, {"layer": "DSMZ owner", "index": 1, "timestamp": "2026-03-13T06:19:06.949204Z", "assessment": "timezone-aware ISO timestamp"}, {"layer": "DSMZ owner", "index": 2, "timestamp": "2026-03-17T06:30:53.000000Z", "assessment": "timezone-aware ISO timestamp"}, {"layer": "DSMZ owner", "index": 3, "timestamp": "2026-03-17T19:45:19.189976+00:00", "assessment": "timezone-aware ISO timestamp"}, {"layer": "DSMZ owner", "index": 4, "timestamp": "2026-05-20T06:00:46.876250+00:00", "assessment": "timezone-aware ISO timestamp"}, {"layer": "DSMZ owner", "index": 5, "timestamp": "2026-06-05T07:40:15.758614+00:00", "assessment": "timezone-aware ISO timestamp"}, {"layer": "DSMZ owner", "index": 6, "timestamp": "2026-06-10T07:46:42.537571+00:00", "assessment": "timezone-aware ISO timestamp"}, {"layer": "DSMZ owner", "index": 7, "timestamp": "2026-10-07T12:21:30.028294+00:00", "assessment": "timezone-aware ISO timestamp"}, {"layer": "KOMODO owner", "index": 0, "timestamp": "2026-01-27T01:15:03.fZ", "assessment": "malformed ISO timestamp"}, {"layer": "KOMODO owner", "index": 1, "timestamp": "2026-02-03T11:19:00.544807", "assessment": "timezone missing"}, {"layer": "KOMODO owner", "index": 2, "timestamp": "2026-03-13T06:19:38.383361Z", "assessment": "timezone-aware ISO timestamp"}, {"layer": "KOMODO owner", "index": 3, "timestamp": "2026-03-17T06:29:57.000000Z", "assessment": "timezone-aware ISO timestamp"}, {"layer": "KOMODO owner", "index": 4, "timestamp": "2026-03-17T19:45:55.293612+00:00", "assessment": "timezone-aware ISO timestamp"}, {"layer": "KOMODO owner", "index": 5, "timestamp": "2026-05-20T06:00:52.913576+00:00", "assessment": "timezone-aware ISO timestamp"}, {"layer": "KOMODO owner", "index": 6, "timestamp": "2026-06-05T07:40:24.987579+00:00", "assessment": "timezone-aware ISO timestamp"}, {"layer": "KOMODO owner", "index": 7, "timestamp": "2026-06-10T07:46:45.406270+00:00", "assessment": "timezone-aware ISO timestamp"}], "relationships": {"parent_variant_child": {"path": "data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml", "relationship": "SOURCE_DUPLICATE", "id": "CultureMech:006115", "name": "2_mh_medium", "notes": "Same ingredient and concentration signature; KOMODO record copied from the matching DSMZ medium source."}, "komodo_parent": {"path": "data/normalized_yaml/bacterial/2_mh_medium.yaml", "relationship": "SOURCE_DUPLICATE", "id": "CultureMech:001751", "name": "2_mh_medium", "notes": "KOMODO record states DSMZ Medium 620 provenance and exactly matches the single same-category DSMZ parent signature."}}, "interpretation": "Matching ingredient signatures and the explicit DSMZ-copy event support the local source-duplicate lineage. They do not independently establish the inaccessible KOMODO row or a biological recipe variant."} |
| transform | src/culturemech/import/mediadive_importer.py; src/culturemech/import/komodo_web_importer.py; src/culturemech/fetch/komodo_web_fetcher.py; src/culturemech/merge/merger.py; MediaDiveImporter._parse_api_composition; KomodoWebImporter._convert_to_culturemech; MediaList BASE_URL and HTML boolean parsing; RecipeMerger.merge_group | supports | The inspected current MediaDive path selects the first solution, skips water, prefers g_l, and copies optional/condition notes without copying ingredient attribute qualifiers in that loop. The current KOMODO writer formats a time.strftime pattern containing %f and records the imported is_aerobic boolean as Yes/No. These code observations contextualize the existing artifacts; no importer, fetcher or merger was run, and they are not a reconstructed execution trace. The current merger delegates formulation/evidence consolidation, so missing evidence in an older generated file is not proof of a current dropping bug. |
| kg-scope | rg --no-ignore --hidden -n 'kg_microbe_match&#124;kg_microbe' data/merge_yaml/merged/2_mh_medium.yaml data/normalized_yaml/bacterial/2_mh_medium.yaml data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml; Exact generated target and both maintained owners; complete ignored-inclusive text search | context_only | No kg_microbe_match or other kg_microbe field occurs in the three inspected records. Exact graph correspondence is therefore not an asserted claim of this target. No graph match was inferred from the DSMZ/MediaDive accession, and no graph-availability or matching execution was required. |

## Limits And Additional Notes

- The captured exact KOMODO MediaList endpoint returned HTTP 403. Its medium-620 row, declared DSMZ correspondence and Aerobic: No metadata could not be independently reread from the provider; local copied-composition history and matching signatures are not independent upstream confirmation.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Only CultureMech:001751 is the review target; CultureMech:006115 is inspected as a maintained contributor. No second review target, new growth assertion or independent KOMODO recipe validation is implied.
- No density-based methanol conversion, primary-source percent basis, measured final volume, filtration pore size or organism-specific cultivation result was established. Provider g_l and declared solution volume remain explicitly provider assertions.
- No kg_microbe_match is asserted in the target or either owner. KG graph availability was not assessed and no ingredient-set correspondence was claimed.
- The four supplied diagnostics were read without rerunning them. No importer, merger, corpus regeneration, source repair or saved-bundle write was executed by this draft generation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T075408Z-culturemech-001751-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 2_mh_medium (CultureMech:001751)'
started_at: '2026-10-21T07:45:22Z'
finished_at: '2026-10-21T07:54:08Z'
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
summary: DSMZ 620 and MediaDive support the seven named solutes and provider-declared
  concentrations, but methanol 20 g/L suppresses the primary recipe's unresolved 2%
  basis. Glucose/methanol filtration and the water instruction are omitted. Five verified
  concentration excerpts present in the maintained DSMZ owner have not reached the
  generated target. Both maintained owners and their reciprocal source-duplicate links
  were inspected; exact KOMODO source verification remains limited by HTTP 403.
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
  - path: data/merge_yaml/merged/2_mh_medium.yaml
    sha256: a977cc8eb05f9c669fad424a33022e423a70863e43a5a1d98fc270bc93574e3a
    role: target
  - path: data/normalized_yaml/bacterial/2_mh_medium.yaml
    sha256: 82e40d26e191afbf270d5bd795056cbdcedcdc8c7644a9986a660951f4676b5b
    role: context
  - path: data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml
    sha256: 5b4ac9f20ac57cad92af06c8c88733696fae5554a38ac2f3b0bf614c1a50bb5b
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
  - path: src/culturemech/fetch/komodo_web_fetcher.py
    sha256: 89c510caa08d989b7ec6cee9ac17cc2f0faab606fe8a29ca435df476e52ff004
    role: context
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
    role: context
  - path: src/culturemech/import/komodo_importer.py
    sha256: 702733bd580e4ba28f77e183e1e8268f17ea2c1041cf7b3addd92919624f2706
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
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
  selection: Task review 85; batch 009 item 5 of 10, selected in Python lexicographic
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
  - CultureMech:001751
targets:
- target_id: CultureMech:001751
  path: data/merge_yaml/merged/2_mh_medium.yaml
  label: 2_mh_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/2_mh_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001751
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/2_mh_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch009/085/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-009/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch009/085/strict.tsv"
  target_ids:
  - CultureMech:001751
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/2_mh_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001751
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/2_mh_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001751
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
  - CultureMech:001751
- check_id: komodo-source-access
  name: Exact KOMODO provider-row verification
  required: true
  status: unavailable
  summary: Captured exact MediaList request returned HTTP 403; no exact medium-620
    row was available for source comparison. This is an HTTP outcome, not a command
    exit code. The successful DSMZ PDF/API reads support DSMZ formulation only.
  target_ids:
  - CultureMech:001751
  evidence_ids:
  - komodo-access
- check_id: kg-match-applicability
  name: Asserted KG-Microbe correspondence applicability
  required: false
  status: not_applicable
  summary: The target and both owners assert no kg_microbe_match. The documented exact
    graph-set check was not run and no graph identity claim is made.
  target_ids:
  - CultureMech:001751
  evidence_ids:
  - kg-scope
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/2_mh_medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T07:54:07Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/2_mh_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T07:54:07Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T07:54:07Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/2_mh_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:47:50.427727Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/2_mh_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch009/085/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T07:47:52.637833Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-009/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch009/085/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/2_mh_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:47:56.218023Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/2_mh_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:47:57.702327Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T07:54:07Z'
  support: supports
  summary: './data/merge_yaml/merged/2_mh_medium.yaml:1:id: CultureMech:001751

    ./data/normalized_yaml/bacterial/2_mh_medium.yaml:1:id: CultureMech:001751

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
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
- evidence_id: chebi17790
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17790
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:31:15.825913Z'
  support: supports
  summary: CHEBI:17790 resolves to methanol and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 9954cafff5982d415d5fbed82fa4630ac9958247ed636b3c770976752ebd50de
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
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:31:16.624783Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:31:17.768734Z'
  support: supports
  summary: CHEBI:62946 resolves to ammonium sulfate and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:31:17.924011Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:31:18.402233Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T07:54:07Z'
  support: supports
  summary: '{"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label":
    "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O",
    "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:17790": [{"label": "Methanol", "match_type": "preferred_term", "identifier":
    "CHEBI:17790", "preferred_term": "Methanol", "ontology_id": "CHEBI:17790", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: dsmz
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium620.pdf
  locator: Page 1, heading 620. 2% MH MEDIUM; complete ingredient table and pH line
  accessed_at: '2026-10-21T07:31:14.593716Z'
  support: supports
  summary: The complete one-page DSMZ 620 recipe lists glucose 1.500 g, KH2PO4 2.000
    g, ammonium sulfate 2.000 g, magnesium sulfate heptahydrate 0.025 g, NaCl 0.500
    g, iron(II) sulfate heptahydrate 2.000 mg, distilled water 1000.000 ml, and methanol
    2.000 percent. Glucose and methanol carry filter-sterilized qualifiers. The pH
    is 7–7.5. The PDF does not specify the percent basis, final-volume closure, a
    filtration pore size, a methanol density, or an autoclaving procedure.
  quote: Methanol (filter-sterilized) 2.000 %
  snapshot_sha256: 4c372dc6b62e723a2ba4a0ae4cf29ddb175ce9f4eea94e2311e66830bb99f019
- evidence_id: mediadive
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/620
  locator: $.data.medium; $.data.solutions[0].id, volume, recipe[0:8], steps
  accessed_at: '2026-10-21T07:31:13.265041Z'
  support: supports
  summary: The captured response identifies DSMZ medium 620 and one main solution,
    ID 1329, with declared volume 1000 ml. Its eight rows include six solute mass
    amounts, water 1000 ml, and methanol amount 2 with unit percent while separately
    declaring g_l=20. Glucose and methanol attributes retain filter-sterilized. Medium
    min_pH/max_pH and the sole step specify 7–7.5; complex_medium is no. These are
    provider-declared amounts, not independent experimental concentration measurements.
  snapshot_sha256: 1f063fe21456c04e7a448ee3bfd14ca43e3e33db209ebebd1c4e078f89d45263
- evidence_id: komodo-access
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact MediaList endpoint used by the checked-in KOMODO web fetcher; captured
    response and HTTP metadata
  accessed_at: '2026-10-21T07:31:13.263705Z'
  support: context_only
  summary: The exact endpoint returned HTTP 403 with a JavaScript/cookie challenge.
    This is evidence of unavailable source access, not evidence that KOMODO medium
    620 or its metadata is absent or false. The original access time and failed-response
    hash are retained.
  snapshot_sha256: 29b422fe5f39bc51b93073f1881bde02395a1b1cc40a86f8238bde510663f000
- evidence_id: amount-trace
  kind: record_content
  reference: data/merge_yaml/merged/2_mh_medium.yaml
  locator: All seven ingredient concentration nodes in target and both owners; source-only
    water instruction
  accessed_at: '2026-10-21T07:54:07Z'
  support: supports
  summary: '[{"field_path": "ingredients[0].concentration", "ingredient": "Glucose",
    "current": {"value": "1.5", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[0]",
    "source_amount": 1.5, "source_unit": "g", "provider_g_l": 1.5, "source_attribute":
    "filter-sterilized", "same_value_in_target_and_both_owners": true, "assessment":
    "Supported as the provider-declared main-solution concentration; primary PDF confirms
    amount and chemical form.", "arithmetic": "1.5 g × 1 g/g / (1000 ml / 1000 ml
    per L) = 1.5 g/L; denominator comes from the API solution-volume field, not from
    water addition alone."}, {"field_path": "ingredients[1].concentration", "ingredient":
    "KH2PO4", "current": {"value": "2", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[1]",
    "source_amount": 2, "source_unit": "g", "provider_g_l": 2, "source_attribute":
    null, "same_value_in_target_and_both_owners": true, "assessment": "Supported as
    the provider-declared main-solution concentration; primary PDF confirms amount
    and chemical form.", "arithmetic": "2 g × 1 g/g / (1000 ml / 1000 ml per L) =
    2 g/L; denominator comes from the API solution-volume field, not from water addition
    alone."}, {"field_path": "ingredients[2].concentration", "ingredient": "(NH4)2SO4",
    "current": {"value": "2", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[2]",
    "source_amount": 2, "source_unit": "g", "provider_g_l": 2, "source_attribute":
    null, "same_value_in_target_and_both_owners": true, "assessment": "Supported as
    the provider-declared main-solution concentration; primary PDF confirms amount
    and chemical form.", "arithmetic": "2 g × 1 g/g / (1000 ml / 1000 ml per L) =
    2 g/L; denominator comes from the API solution-volume field, not from water addition
    alone."}, {"field_path": "ingredients[3].concentration", "ingredient": "MgSO4
    x 7 H2O", "current": {"value": "0.025", "unit": "G_PER_L"}, "source_locator":
    "$.data.solutions[0].recipe[3]", "source_amount": 0.025, "source_unit": "g", "provider_g_l":
    0.025, "source_attribute": null, "same_value_in_target_and_both_owners": true,
    "assessment": "Supported as the provider-declared main-solution concentration;
    primary PDF confirms amount and chemical form.", "arithmetic": "0.025 g × 1 g/g
    / (1000 ml / 1000 ml per L) = 0.025 g/L; denominator comes from the API solution-volume
    field, not from water addition alone."}, {"field_path": "ingredients[4].concentration",
    "ingredient": "NaCl", "current": {"value": "0.5", "unit": "G_PER_L"}, "source_locator":
    "$.data.solutions[0].recipe[4]", "source_amount": 0.5, "source_unit": "g", "provider_g_l":
    0.5, "source_attribute": null, "same_value_in_target_and_both_owners": true, "assessment":
    "Supported as the provider-declared main-solution concentration; primary PDF confirms
    amount and chemical form.", "arithmetic": "0.5 g × 1 g/g / (1000 ml / 1000 ml
    per L) = 0.5 g/L; denominator comes from the API solution-volume field, not from
    water addition alone."}, {"field_path": "ingredients[5].concentration", "ingredient":
    "FeSO4 x 7 H2O", "current": {"value": "0.002", "unit": "G_PER_L"}, "source_locator":
    "$.data.solutions[0].recipe[5]", "source_amount": 2, "source_unit": "mg", "provider_g_l":
    0.002, "source_attribute": null, "same_value_in_target_and_both_owners": true,
    "assessment": "Supported as the provider-declared main-solution concentration;
    primary PDF confirms amount and chemical form.", "arithmetic": "2 mg × 0.001 g/mg
    / (1000 ml / 1000 ml per L) = 0.002 g/L; denominator comes from the API solution-volume
    field, not from water addition alone."}, {"field_path": "ingredients[6].concentration",
    "ingredient": "Methanol", "current": {"value": "20", "unit": "G_PER_L"}, "source_locator":
    "$.data.solutions[0].recipe[7]", "source_amount": 2, "source_unit": "%", "provider_g_l":
    20, "source_attribute": "filter-sterilized", "same_value_in_target_and_both_owners":
    true, "assessment": "Local 20 g/L exactly follows the provider g_l field; original
    PDF/API 2% lacks w/v, v/v or w/w qualification, so its primary-source basis is
    unresolved.", "conditional_arithmetic": "If 2% means w/v, 2 g per 100 ml gives
    20 g/L. If it means v/v, it describes a different quantity basis; no density conversion
    or final receiving-volume assumption is made. Neither interpretation is independently
    selected here."}, {"field_path": "preparation_steps", "source_only_component":
    "Distilled water", "source_locator": "$.data.solutions[0].recipe[6]; DSMZ PDF
    water row", "source_amount": 1000, "source_unit": "ml", "assessment": "Source
    water instruction is absent from target and both owners. Preserve it in preparation
    context; it is not a missing gram-per-litre solute or independent proof of an
    exact final volume after methanol addition."}]'
- evidence_id: existing-evidence
  kind: record_content
  reference: data/normalized_yaml/bacterial/2_mh_medium.yaml
  locator: ingredients[1:6].evidence[0]; references[0]; curation_history[7]; comparison
    with target
  accessed_at: '2026-10-21T07:54:07Z'
  support: supports
  summary: '{"verified_excerpts": [{"owner_path": "data/normalized_yaml/bacterial/2_mh_medium.yaml",
    "field_path": "ingredients[1].evidence[0]", "source_locator": "$.data.solutions[0].recipe[1]",
    "literal_snippet_matches_current_capture": true, "current_capture_sha256": "1f063fe21456c04e7a448ee3bfd14ca43e3e33db209ebebd1c4e078f89d45263",
    "scope": "Exact provider row and declared main-solution concentration only; does
    not verify the ingredient ontology mapping or methanol percent basis."}, {"owner_path":
    "data/normalized_yaml/bacterial/2_mh_medium.yaml", "field_path": "ingredients[2].evidence[0]",
    "source_locator": "$.data.solutions[0].recipe[2]", "literal_snippet_matches_current_capture":
    true, "current_capture_sha256": "1f063fe21456c04e7a448ee3bfd14ca43e3e33db209ebebd1c4e078f89d45263",
    "scope": "Exact provider row and declared main-solution concentration only; does
    not verify the ingredient ontology mapping or methanol percent basis."}, {"owner_path":
    "data/normalized_yaml/bacterial/2_mh_medium.yaml", "field_path": "ingredients[3].evidence[0]",
    "source_locator": "$.data.solutions[0].recipe[3]", "literal_snippet_matches_current_capture":
    true, "current_capture_sha256": "1f063fe21456c04e7a448ee3bfd14ca43e3e33db209ebebd1c4e078f89d45263",
    "scope": "Exact provider row and declared main-solution concentration only; does
    not verify the ingredient ontology mapping or methanol percent basis."}, {"owner_path":
    "data/normalized_yaml/bacterial/2_mh_medium.yaml", "field_path": "ingredients[4].evidence[0]",
    "source_locator": "$.data.solutions[0].recipe[4]", "literal_snippet_matches_current_capture":
    true, "current_capture_sha256": "1f063fe21456c04e7a448ee3bfd14ca43e3e33db209ebebd1c4e078f89d45263",
    "scope": "Exact provider row and declared main-solution concentration only; does
    not verify the ingredient ontology mapping or methanol percent basis."}, {"owner_path":
    "data/normalized_yaml/bacterial/2_mh_medium.yaml", "field_path": "ingredients[5].evidence[0]",
    "source_locator": "$.data.solutions[0].recipe[5]", "literal_snippet_matches_current_capture":
    true, "current_capture_sha256": "1f063fe21456c04e7a448ee3bfd14ca43e3e33db209ebebd1c4e078f89d45263",
    "scope": "Exact provider row and declared main-solution concentration only; does
    not verify the ingredient ontology mapping or methanol percent basis."}], "source_reference_matches":
    true, "target_excerpts": 0, "target_references": 0, "chronology": "The target
    merge event is 2026-08-06; the maintained parent added these five excerpts and
    reference on 2026-10-07. The artifact is stale relative to this evidence addition;
    no claim is made that the current merger would discard it."}'
- evidence_id: history
  kind: record_content
  reference: data/merge_yaml/merged/2_mh_medium.yaml; data/normalized_yaml/bacterial/2_mh_medium.yaml;
    data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml
  locator: 'All history events: target 9, DSMZ owner 8, KOMODO owner 8; reciprocal
    parent/child descriptors'
  accessed_at: '2026-10-21T07:54:07Z'
  support: supports
  summary: '{"events": [{"layer": "target", "index": 0, "timestamp": "2026-01-26T17:53:11.754287Z",
    "assessment": "timezone-aware ISO timestamp"}, {"layer": "target", "index": 1,
    "timestamp": "2026-03-13T06:19:06.949204Z", "assessment": "timezone-aware ISO
    timestamp"}, {"layer": "target", "index": 2, "timestamp": "2026-03-17T06:30:53.000000Z",
    "assessment": "timezone-aware ISO timestamp"}, {"layer": "target", "index": 3,
    "timestamp": "2026-03-17T19:45:19.189976+00:00", "assessment": "timezone-aware
    ISO timestamp"}, {"layer": "target", "index": 4, "timestamp": "2026-05-20T06:00:46.876250+00:00",
    "assessment": "timezone-aware ISO timestamp"}, {"layer": "target", "index": 5,
    "timestamp": "2026-06-05T07:40:15.758614+00:00", "assessment": "timezone-aware
    ISO timestamp"}, {"layer": "target", "index": 6, "timestamp": "2026-06-10T07:46:42.537571+00:00",
    "assessment": "timezone-aware ISO timestamp"}, {"layer": "target", "index": 7,
    "timestamp": "2026-08-06T03:04:34.040528+00:00", "assessment": "timezone-aware
    ISO timestamp"}, {"layer": "target", "index": 8, "timestamp": "2026-08-06T03:04:34.040563+00:00",
    "assessment": "timezone-aware ISO timestamp"}, {"layer": "DSMZ owner", "index":
    0, "timestamp": "2026-01-26T17:53:11.754287Z", "assessment": "timezone-aware ISO
    timestamp"}, {"layer": "DSMZ owner", "index": 1, "timestamp": "2026-03-13T06:19:06.949204Z",
    "assessment": "timezone-aware ISO timestamp"}, {"layer": "DSMZ owner", "index":
    2, "timestamp": "2026-03-17T06:30:53.000000Z", "assessment": "timezone-aware ISO
    timestamp"}, {"layer": "DSMZ owner", "index": 3, "timestamp": "2026-03-17T19:45:19.189976+00:00",
    "assessment": "timezone-aware ISO timestamp"}, {"layer": "DSMZ owner", "index":
    4, "timestamp": "2026-05-20T06:00:46.876250+00:00", "assessment": "timezone-aware
    ISO timestamp"}, {"layer": "DSMZ owner", "index": 5, "timestamp": "2026-06-05T07:40:15.758614+00:00",
    "assessment": "timezone-aware ISO timestamp"}, {"layer": "DSMZ owner", "index":
    6, "timestamp": "2026-06-10T07:46:42.537571+00:00", "assessment": "timezone-aware
    ISO timestamp"}, {"layer": "DSMZ owner", "index": 7, "timestamp": "2026-10-07T12:21:30.028294+00:00",
    "assessment": "timezone-aware ISO timestamp"}, {"layer": "KOMODO owner", "index":
    0, "timestamp": "2026-01-27T01:15:03.fZ", "assessment": "malformed ISO timestamp"},
    {"layer": "KOMODO owner", "index": 1, "timestamp": "2026-02-03T11:19:00.544807",
    "assessment": "timezone missing"}, {"layer": "KOMODO owner", "index": 2, "timestamp":
    "2026-03-13T06:19:38.383361Z", "assessment": "timezone-aware ISO timestamp"},
    {"layer": "KOMODO owner", "index": 3, "timestamp": "2026-03-17T06:29:57.000000Z",
    "assessment": "timezone-aware ISO timestamp"}, {"layer": "KOMODO owner", "index":
    4, "timestamp": "2026-03-17T19:45:55.293612+00:00", "assessment": "timezone-aware
    ISO timestamp"}, {"layer": "KOMODO owner", "index": 5, "timestamp": "2026-05-20T06:00:52.913576+00:00",
    "assessment": "timezone-aware ISO timestamp"}, {"layer": "KOMODO owner", "index":
    6, "timestamp": "2026-06-05T07:40:24.987579+00:00", "assessment": "timezone-aware
    ISO timestamp"}, {"layer": "KOMODO owner", "index": 7, "timestamp": "2026-06-10T07:46:45.406270+00:00",
    "assessment": "timezone-aware ISO timestamp"}], "relationships": {"parent_variant_child":
    {"path": "data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml", "relationship":
    "SOURCE_DUPLICATE", "id": "CultureMech:006115", "name": "2_mh_medium", "notes":
    "Same ingredient and concentration signature; KOMODO record copied from the matching
    DSMZ medium source."}, "komodo_parent": {"path": "data/normalized_yaml/bacterial/2_mh_medium.yaml",
    "relationship": "SOURCE_DUPLICATE", "id": "CultureMech:001751", "name": "2_mh_medium",
    "notes": "KOMODO record states DSMZ Medium 620 provenance and exactly matches
    the single same-category DSMZ parent signature."}}, "interpretation": "Matching
    ingredient signatures and the explicit DSMZ-copy event support the local source-duplicate
    lineage. They do not independently establish the inaccessible KOMODO row or a
    biological recipe variant."}'
- evidence_id: transform
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py; src/culturemech/import/komodo_web_importer.py;
    src/culturemech/fetch/komodo_web_fetcher.py; src/culturemech/merge/merger.py
  locator: MediaDiveImporter._parse_api_composition; KomodoWebImporter._convert_to_culturemech;
    MediaList BASE_URL and HTML boolean parsing; RecipeMerger.merge_group
  accessed_at: '2026-10-21T07:54:07Z'
  support: supports
  summary: The inspected current MediaDive path selects the first solution, skips
    water, prefers g_l, and copies optional/condition notes without copying ingredient
    attribute qualifiers in that loop. The current KOMODO writer formats a time.strftime
    pattern containing %f and records the imported is_aerobic boolean as Yes/No. These
    code observations contextualize the existing artifacts; no importer, fetcher or
    merger was run, and they are not a reconstructed execution trace. The current
    merger delegates formulation/evidence consolidation, so missing evidence in an
    older generated file is not proof of a current dropping bug.
- evidence_id: kg-scope
  kind: record_content
  reference: rg --no-ignore --hidden -n 'kg_microbe_match|kg_microbe' data/merge_yaml/merged/2_mh_medium.yaml
    data/normalized_yaml/bacterial/2_mh_medium.yaml data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml
  locator: Exact generated target and both maintained owners; complete ignored-inclusive
    text search
  accessed_at: '2026-10-21T07:54:07Z'
  support: context_only
  summary: No kg_microbe_match or other kg_microbe field occurs in the three inspected
    records. Exact graph correspondence is therefore not an asserted claim of this
    target. No graph match was inferred from the DSMZ/MediaDive accession, and no
    graph-availability or matching execution was required.
  search_scope: rg --no-ignore --hidden over the three fully read target/owner paths;
    ignored files were included.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001751
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '7 primary CHEBI identities resolve with matching labels; 7 of 7 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:001751
  evidence_ids:
  - record
  - mim
  - chebi17234
  - chebi17790
  - chebi26710
  - chebi31795
  - chebi62946
  - chebi63036
  - chebi75836
  details: 7 direct ingredient instances; CHEBI-primary instance linkage 7/7 (100.00%),
    verified secondary coverage 7/7 (100.00%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: DSMZ source identity and both maintained owners
  outcome: supported
  summary: DSMZ PDF 620 and the MediaDive medium/solution response identify this formulation.
    Both maintained owners have the same seven names, concentrations and chemical
    IDs. Reciprocal source-duplicate descriptors resolve to the two actual stable
    IDs and paths; the KOMODO ingredients were explicitly copied from DSMZ, not an
    independent experimental confirmation.
  target_ids:
  - CultureMech:001751
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - id-search
  - dsmz
  - mediadive
  - history
- assessment_id: quantities
  area: quantity
  topic: Every ingredient amount and source-only water
  outcome: concern
  summary: All seven stored values equal provider g_l; the six non-methanol mass amounts
    and hydrate forms also agree with the primary PDF. Iron sulfate 2 mg correctly
    corresponds to 0.002 g/L under the API-declared 1000 ml basis. Methanol 20 g/L
    retains only the provider normalization and loses the unqualified primary 2% amount.
    Water 1000 ml is a preparation instruction, not an extra solute concentration.
  target_ids:
  - CultureMech:001751
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz
  - mediadive
  - amount-trace
  details: '[{"field_path": "ingredients[0].concentration", "ingredient": "Glucose",
    "current": {"value": "1.5", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[0]",
    "source_amount": 1.5, "source_unit": "g", "provider_g_l": 1.5, "source_attribute":
    "filter-sterilized", "same_value_in_target_and_both_owners": true, "assessment":
    "Supported as the provider-declared main-solution concentration; primary PDF confirms
    amount and chemical form.", "arithmetic": "1.5 g × 1 g/g / (1000 ml / 1000 ml
    per L) = 1.5 g/L; denominator comes from the API solution-volume field, not from
    water addition alone."}, {"field_path": "ingredients[1].concentration", "ingredient":
    "KH2PO4", "current": {"value": "2", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[1]",
    "source_amount": 2, "source_unit": "g", "provider_g_l": 2, "source_attribute":
    null, "same_value_in_target_and_both_owners": true, "assessment": "Supported as
    the provider-declared main-solution concentration; primary PDF confirms amount
    and chemical form.", "arithmetic": "2 g × 1 g/g / (1000 ml / 1000 ml per L) =
    2 g/L; denominator comes from the API solution-volume field, not from water addition
    alone."}, {"field_path": "ingredients[2].concentration", "ingredient": "(NH4)2SO4",
    "current": {"value": "2", "unit": "G_PER_L"}, "source_locator": "$.data.solutions[0].recipe[2]",
    "source_amount": 2, "source_unit": "g", "provider_g_l": 2, "source_attribute":
    null, "same_value_in_target_and_both_owners": true, "assessment": "Supported as
    the provider-declared main-solution concentration; primary PDF confirms amount
    and chemical form.", "arithmetic": "2 g × 1 g/g / (1000 ml / 1000 ml per L) =
    2 g/L; denominator comes from the API solution-volume field, not from water addition
    alone."}, {"field_path": "ingredients[3].concentration", "ingredient": "MgSO4
    x 7 H2O", "current": {"value": "0.025", "unit": "G_PER_L"}, "source_locator":
    "$.data.solutions[0].recipe[3]", "source_amount": 0.025, "source_unit": "g", "provider_g_l":
    0.025, "source_attribute": null, "same_value_in_target_and_both_owners": true,
    "assessment": "Supported as the provider-declared main-solution concentration;
    primary PDF confirms amount and chemical form.", "arithmetic": "0.025 g × 1 g/g
    / (1000 ml / 1000 ml per L) = 0.025 g/L; denominator comes from the API solution-volume
    field, not from water addition alone."}, {"field_path": "ingredients[4].concentration",
    "ingredient": "NaCl", "current": {"value": "0.5", "unit": "G_PER_L"}, "source_locator":
    "$.data.solutions[0].recipe[4]", "source_amount": 0.5, "source_unit": "g", "provider_g_l":
    0.5, "source_attribute": null, "same_value_in_target_and_both_owners": true, "assessment":
    "Supported as the provider-declared main-solution concentration; primary PDF confirms
    amount and chemical form.", "arithmetic": "0.5 g × 1 g/g / (1000 ml / 1000 ml
    per L) = 0.5 g/L; denominator comes from the API solution-volume field, not from
    water addition alone."}, {"field_path": "ingredients[5].concentration", "ingredient":
    "FeSO4 x 7 H2O", "current": {"value": "0.002", "unit": "G_PER_L"}, "source_locator":
    "$.data.solutions[0].recipe[5]", "source_amount": 2, "source_unit": "mg", "provider_g_l":
    0.002, "source_attribute": null, "same_value_in_target_and_both_owners": true,
    "assessment": "Supported as the provider-declared main-solution concentration;
    primary PDF confirms amount and chemical form.", "arithmetic": "2 mg × 0.001 g/mg
    / (1000 ml / 1000 ml per L) = 0.002 g/L; denominator comes from the API solution-volume
    field, not from water addition alone."}, {"field_path": "ingredients[6].concentration",
    "ingredient": "Methanol", "current": {"value": "20", "unit": "G_PER_L"}, "source_locator":
    "$.data.solutions[0].recipe[7]", "source_amount": 2, "source_unit": "%", "provider_g_l":
    20, "source_attribute": "filter-sterilized", "same_value_in_target_and_both_owners":
    true, "assessment": "Local 20 g/L exactly follows the provider g_l field; original
    PDF/API 2% lacks w/v, v/v or w/w qualification, so its primary-source basis is
    unresolved.", "conditional_arithmetic": "If 2% means w/v, 2 g per 100 ml gives
    20 g/L. If it means v/v, it describes a different quantity basis; no density conversion
    or final receiving-volume assumption is made. Neither interpretation is independently
    selected here."}, {"field_path": "preparation_steps", "source_only_component":
    "Distilled water", "source_locator": "$.data.solutions[0].recipe[6]; DSMZ PDF
    water row", "source_amount": 1000, "source_unit": "ml", "assessment": "Source
    water instruction is absent from target and both owners. Preserve it in preparation
    context; it is not a missing gram-per-litre solute or independent proof of an
    exact final volume after methanol addition."}]'
- assessment_id: preparation
  area: completeness
  topic: Filtration, water instruction and pH
  outcome: concern
  summary: The pH range 7.0–7.5 is retained correctly, though the target/DSMZ preparation
    step is merely a MIX-labelled pH note. Both sources mark glucose and methanol
    as filter-sterilized and list water 1000 ml; these instructions are absent from
    all local layers. The source supplies no filtration pore size, time/temperature,
    autoclave regimen, addition timing or explicit final-volume closure, so none should
    be invented.
  target_ids:
  - CultureMech:001751
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz
  - mediadive
  - transform
- assessment_id: evidence-placement
  area: evidence
  topic: Existing owner excerpts and generated evidence drift
  outcome: concern
  summary: All five parent excerpts at ingredients[1:6] are exact substrings of the
    current raw response and match their JSON rows, source URL and reported hash.
    They support only KH2PO4, ammonium sulfate, MgSO4 heptahydrate, NaCl and FeSO4
    heptahydrate provider concentrations. Neither glucose nor methanol has an existing
    excerpt. The generated target has no excerpts or reference list, so its zero reference
    checks do not assess the maintained parent evidence.
  target_ids:
  - CultureMech:001751
  evidence_ids:
  - record
  - owner-0
  - existing-evidence
  - mediadive
  - validate-references
- assessment_id: classification
  area: scope
  topic: Defined liquid medium, duplicate scope and growth limits
  outcome: supported
  summary: The seven named pure compounds, no complex ingredients, no solidifier,
    and provider complex_medium=no support DEFINED/DEFINED and LIQUID. Bacterial placement
    and generic microbial-cultivation application supply no organism or strain-specific
    growth evidence. SOURCE_DUPLICATE describes the documented local copied composition,
    not a distinct biological variant. No CHEBI ingredient-set match to KG-Microbe
    is asserted or inferred.
  target_ids:
  - CultureMech:001751
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz
  - mediadive
  - history
  - kg-scope
- assessment_id: komodo-boundary
  area: provenance
  topic: Unavailable exact KOMODO row and oxygen annotation
  outcome: unknown
  summary: 'The maintained KOMODO owner names accession 620, DSMZ 620 and Aerobic:
    No. Its exact MediaList source is unavailable with HTTP 403. The local DSMZ-copy
    event and reciprocal duplicate links are readable, but accession correspondence
    and the oxygen flag remain unverified at the upstream row. Neither the DSMZ recipe
    nor the boolean import code establishes anaerobic growth or obligate physiology.'
  target_ids:
  - CultureMech:001751
  evidence_ids:
  - owner-1
  - komodo-access
  - history
  - transform
- assessment_id: history-quality
  area: provenance
  topic: All target and owner history timestamps
  outcome: concern
  summary: Target and DSMZ-owner history timestamps are timezone-aware. The KOMODO
    owner has a malformed .fZ timestamp at event 0 and an otherwise parseable timezone-free
    timestamp at event 1. Preserve those original events and document any correction
    with independent timing evidence; do not guess a timezone or rewrite the append-only
    history.
  target_ids:
  - CultureMech:001751
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - history
  - transform
findings:
- finding_id: f1
  issue_key: CM001751-methanol-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Methanol percent basis is hidden by provider normalization
  description: All three local files assert methanol 20 g/L. This matches MediaDive
    g_l=20, but the same provider row and DSMZ PDF give original amount 2 with an
    unqualified percent unit. The records preserve neither that original amount nor
    the unresolved basis. The value is provider-backed, not independently established
    as a primary-source w/v concentration.
  target_ids:
  - CultureMech:001751
  field_paths:
  - ingredients[6].concentration
  - ingredients[6].notes
  - ingredients[6].evidence
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz
  - mediadive
  - amount-trace
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM001751-source-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Ingredient-specific filtration and water instruction are omitted
  description: The PDF and API mark glucose and methanol as filter-sterilized and
    list distilled water 1000 ml. None of the target or two owners retains these instructions.
    The pH-only MIX note in the target and DSMZ owner is not a complete preparation
    representation.
  target_ids:
  - CultureMech:001751
  field_paths:
  - ingredients[0].notes
  - ingredients[6].notes
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz
  - mediadive
  - amount-trace
  - transform
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml
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
  issue_key: CM001751-owner-evidence-drift
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generated record predates five verified owner evidence additions
  description: The maintained DSMZ owner contains five exact API excerpts for ingredients[1:6],
    one reference and the 2026-10-07 evidence-curation event. The generated target
    last merged on 2026-08-06 and lacks all five excerpts and the reference. Its reference
    check examined zero excerpts, despite the maintained evidence now being available.
  target_ids:
  - CultureMech:001751
  field_paths:
  - ingredients[1:6].evidence
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - existing-evidence
  - mediadive
  - history
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: CM001751-contributor-history
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: KOMODO contributor history contains malformed and timezone-free times
  description: The KOMODO maintained input has 2026-01-27T01:15:03.fZ at curation_history[0]
    and 2026-02-03T11:19:00.544807 without a timezone at curation_history[1]. The
    target and DSMZ owner do not share these two timestamp defects; their successful
    target-only schema check does not validate this contributor history.
  target_ids:
  - CultureMech:001751
  field_paths:
  - data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml::curation_history[1].timestamp
  evidence_ids:
  - owner-1
  - history
  - transform
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Retain the exact original 2% source amount and the separate provider
    g_l=20 assertion with claim-level provenance and explicit basis uncertainty. Resolve
    the percentage basis before asserting a conversion; do not substitute v/v, use
    an assumed density, or declare 20 g/L numerically false without new evidence.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001751
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml
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
  description: Restore glucose/methanol filtration qualifiers and the literal water
    instruction at maintained-input preparation scope, preserving the correct pH range.
    Do not turn water addition into an asserted final-volume closure, or invent filtration
    pore size, sterilization timing, autoclaving or adjustment reagents.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001751
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml
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
  description: Preserve the verified parent evidence and refresh the generated record
    only after maintained-input review and separately authorized regeneration. Verify
    the five exact excerpts, reference and source-history provenance survive. Add
    narrow evidence for glucose and qualified methanol separately; do not treat these
    five excerpts as validating all ingredients or proving methanol percent basis.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001751
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml
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
  description: Retain the original events and append a corrective provenance note
    supported by an actual source log if available. Correct future KOMODO timestamp
    generation without inventing historical fractional seconds or timezone; leave
    unresolved timing explicit.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001751
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml
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
- 'The captured exact KOMODO MediaList endpoint returned HTTP 403. Its medium-620
  row, declared DSMZ correspondence and Aerobic: No metadata could not be independently
  reread from the provider; local copied-composition history and matching signatures
  are not independent upstream confirmation.'
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- Only CultureMech:001751 is the review target; CultureMech:006115 is inspected as
  a maintained contributor. No second review target, new growth assertion or independent
  KOMODO recipe validation is implied.
- No density-based methanol conversion, primary-source percent basis, measured final
  volume, filtration pore size or organism-specific cultivation result was established.
  Provider g_l and declared solution volume remain explicitly provider assertions.
- No kg_microbe_match is asserted in the target or either owner. KG graph availability
  was not assessed and no ingredient-set correspondence was claimed.
- The four supplied diagnostics were read without rerunning them. No importer, merger,
  corpus regeneration, source repair or saved-bundle write was executed by this draft
  generation.
tags:
- unreviewed-records
- batch-009
- generated-medium
```
