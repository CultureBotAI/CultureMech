# Source and formulation review: 9k_with_sulfur_medium (CultureMech:002485)

- Review: 20261021T092344Z-culturemech-002485-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T09:12:06Z
- Finished UTC: 2026-10-21T09:23:44Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

All six recorded solute amounts agree with exact JCM 1321 and provider-declared MediaDive concentrations. Both layers omit the preparation solvent and sulfur powder qualifier and incompletely preserve the primary autoclave parameters. Five exact maintained-owner concentration excerpts are absent from the generated target.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 125; batch 013 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twelve task batches contain 120 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 122 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002485 | data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml | generated | 9k_with_sulfur_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002485 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002485 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch013/125/strict.tsv |
| validate-terms | passed | True | CultureMech:002485 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002485 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002485 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002485.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: concern. Targets: CultureMech:002485.

6 primary CHEBI identities resolve with matching labels; 5 of 6 current secondary keys have live pinned-index rows. Unresolved keys: ['CHEBI:26833'].

6 direct ingredient instances; CHEBI-primary instance linkage 6/6 (100.00%), verified secondary coverage 5/6 (83.33%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### JCM recipe identity and MediaDive hosting

identity: supported. Targets: CultureMech:002485.

CultureMech 002485 denotes JCM GRMD 1321, represented by MediaDive J1321. Exact original/source URLs agree and one normalized owner supplies the generated target. DSMZ hosts the dataset; JCM is the original recipe collection. Similar 9K names do not merge the sulfur medium with iron formulations.

### Every ingredient, original unit and preparation quantity

quantity: concern. Targets: CultureMech:002485.

All six solute values match provider g/L and nominal primary masses. The five owner concentration excerpts are exact and appropriately limited to provider-declared volume; the generated target has none. Water is absent as preparation context. Acid strength and dose are intentionally unquantified. The complete quantity inventory separates sulfur treatment and main autoclave parameters.

[{"field_path": "ingredients[0].concentration", "owner_field_path": "data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml:ingredients[0].concentration", "ingredient": "K2HPO4", "record_value": {"value": "0.5", "unit": "G_PER_L"}, "owner_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "evidence_only", "owner_decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321", "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161", "source_quote": "K 2 HPO 4 0.5 g", "source_locator": "JCM 1321 composition row 1", "original_source_amount": 0.5, "original_source_unit": "g", "provider_locator": "$.data.solutions[0].recipe[0]", "provider_g_l": 0.5, "provider_volume_ml": 1000, "stage": "main medium; sulfur is separately sterilized", "explanation": "The provider explicitly reports this main-recipe g/L value; the primary gives the same original mass and 1 L water. Preserve provider normalization separately from measured final volume."}, {"field_path": "ingredients[1].concentration", "owner_field_path": "data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml:ingredients[1].concentration", "ingredient": "(NH4)2SO4", "record_value": {"value": "3", "unit": "G_PER_L"}, "owner_value": {"value": "3", "unit": "G_PER_L"}, "decision": "evidence_only", "owner_decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321", "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161", "source_quote": "(NH 4 ) 2 SO 4 3.0 g", "source_locator": "JCM 1321 composition row 2", "original_source_amount": 3, "original_source_unit": "g", "provider_locator": "$.data.solutions[0].recipe[1]", "provider_g_l": 3, "provider_volume_ml": 1000, "stage": "main medium; sulfur is separately sterilized", "explanation": "The provider explicitly reports this main-recipe g/L value; the primary gives the same original mass and 1 L water. Preserve provider normalization separately from measured final volume."}, {"field_path": "ingredients[2].concentration", "owner_field_path": "data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml:ingredients[2].concentration", "ingredient": "KCl", "record_value": {"value": "0.1", "unit": "G_PER_L"}, "owner_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only", "owner_decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321", "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161", "source_quote": "KCl 0.1 g", "source_locator": "JCM 1321 composition row 3", "original_source_amount": 0.1, "original_source_unit": "g", "provider_locator": "$.data.solutions[0].recipe[2]", "provider_g_l": 0.1, "provider_volume_ml": 1000, "stage": "main medium; sulfur is separately sterilized", "explanation": "The provider explicitly reports this main-recipe g/L value; the primary gives the same original mass and 1 L water. Preserve provider normalization separately from measured final volume."}, {"field_path": "ingredients[3].concentration", "owner_field_path": "data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml:ingredients[3].concentration", "ingredient": "MgSO4 x 7 H2O", "record_value": {"value": "0.5", "unit": "G_PER_L"}, "owner_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "evidence_only", "owner_decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321", "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161", "source_quote": "MgSO 4 ·7H 2 O 0.5 g", "source_locator": "JCM 1321 composition row 4", "original_source_amount": 0.5, "original_source_unit": "g", "provider_locator": "$.data.solutions[0].recipe[3]", "provider_g_l": 0.5, "provider_volume_ml": 1000, "stage": "main medium; sulfur is separately sterilized", "explanation": "The provider explicitly reports this main-recipe g/L value; the primary gives the same original mass and 1 L water. Preserve provider normalization separately from measured final volume."}, {"field_path": "ingredients[4].concentration", "owner_field_path": "data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml:ingredients[4].concentration", "ingredient": "Ca(NO3)2", "record_value": {"value": "0.01", "unit": "G_PER_L"}, "owner_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "evidence_only", "owner_decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321", "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161", "source_quote": "Ca(NO 3 ) 2 10.0 mg", "source_locator": "JCM 1321 composition row 5", "original_source_amount": 10, "original_source_unit": "mg", "provider_locator": "$.data.solutions[0].recipe[4]", "provider_g_l": 0.01, "provider_volume_ml": 1000, "stage": "main medium; sulfur is separately sterilized", "explanation": "The provider explicitly reports this main-recipe g/L value; the primary gives the same original mass and 1 L water. Preserve provider normalization separately from measured final volume. Exact conversion: 10 mg × 0.001 g/mg = 0.01 g, consistent with provider 0.01 g/L on its declared 1000 ml basis."}, {"field_path": "ingredients[5].concentration", "owner_field_path": "data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml:ingredients[5].concentration", "ingredient": "Sulfur", "record_value": {"value": "5", "unit": "G_PER_L"}, "owner_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "owner_decision": "correct", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321", "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161", "source_quote": "Sulfur (powder) 5.0 g", "source_locator": "JCM 1321 composition row 6", "original_source_amount": 5, "original_source_unit": "g", "provider_locator": "$.data.solutions[0].recipe[5]", "provider_g_l": 5, "provider_volume_ml": 1000, "stage": "main medium; sulfur is separately sterilized", "explanation": "The provider explicitly reports this main-recipe g/L value; the primary gives the same original mass and 1 L water. Preserve provider normalization separately from measured final volume. The numerical value is supported, but the exact source material is sulfur powder and that qualifier is absent from both layers. No molecular allotrope is inferred from the word powder."}, {"field_path": "preparation_steps (source-only solvent)", "decision": "add", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321", "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161", "source_quote": "Distilled water 1.0 L", "source_locator": "JCM 1321 composition water row", "stage": "main preparation solvent", "explanation": "Preserve the literal 1 L water instruction in preparation context. Avoiding a water composition edge does not justify omitting the solvent basis; do not claim measured final volume."}, {"field_path": "preparation_steps[0] acid addition", "decision": "not_quantified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321", "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161", "source_quote": "adjust pH to 2.5 with H 2 SO 4", "source_locator": "JCM 1321 preparation sentence", "stage": "pH adjustment before main-component autoclaving", "explanation": "The acid identity and endpoint are explicit but its strength and fixed dose are not. Retain endpoint-controlled addition without borrowing a strength or dose from another 9K recipe."}, {"field_path": "ph_value; preparation_steps[0]", "decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321", "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161", "source_quote": "adjust pH to 2.5", "source_locator": "JCM 1321 preparation sentence", "stage": "preparation endpoint", "explanation": "Target and owner preserve 2.5 at the documented adjustment stage. This is not an incubation optimum or measured post-growth pH."}, {"field_path": "preparation_steps[0] sulfur treatment", "decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321", "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161", "source_quote": "steaming for 3 hr on each of 3 successive days", "source_locator": "JCM 1321 separate sulfur preparation sentence", "stage": "sulfur stock material treatment", "explanation": "Both layers preserve the duration and repeated-day instruction. Keep it separate from the main-medium autoclave default."}, {"field_path": "preparation_steps[0] main autoclaving", "decision": "add", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321", "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161", "source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.", "source_locator": "JCM page-wide instruction before medium 1321 heading", "stage": "main mixture excluding sulfur", "explanation": "Both layers name autoclaving but omit these source temperature/time parameters. The source-specific separate sulfur treatment remains an explicit exception; do not replace it with this default."}]

### All six chemical identities, hydration and sulfur material

grounding: concern. Targets: CultureMech:002485.

Every asserted CHEBI label resolves. Source K2HPO4, ammonium sulfate, KCl, magnesium sulfate heptahydrate and calcium nitrate agree at their stated forms. Calcium nitrate is not silently converted to a hydrate. Sulfur-atom ontology metadata includes Elemental sulfur as a synonym, so atom wording alone is not evidence of a wrong ID; the separately asserted primary powder form is missing. No unasserted allotrope or molarity is introduced.

### Solvent, main autoclaving and separate sulfur treatment

completeness: concern. Targets: CultureMech:002485.

Both layers preserve pH 2.5 with H2SO4, autoclaving of the other components and separate sulfur steaming for 3 hours on each of 3 days. They omit 1 L water and the primary page-wide 121 C/15 min parameters for main autoclaving. This is incomplete source context, not an absence of all sterilization or a reason to overwrite the sulfur exception.

### Defined composition and liquid-medium boundaries

scope: supported. Targets: CultureMech:002485.

The stated constituents are defined chemicals, and LIQUID describes the non-agar medium without claiming every material is dissolved; sulfur powder may remain a distinct material phase. No organism, strain, native variant, parent, external KG match or measured growth claim is present. General cultivation and bacterial filing do not establish a specific growth outcome.

### Exact owner support and generated evidence omission

evidence: concern. Targets: CultureMech:002485.

The owner carries five source-linked ingredient snippets and a reference absent from the generated target. Sulfur and solvent/preparation claims still need narrow evidence in the owner. The reference accurately distinguishes JCM origin from DSMZ dataset hosting and leaves unknown author/year unset. Target reference checks examined zero excerpts; canonical passes are not a substitute for these source comparisons.

### Historical evidence curation and generated timestamp

provenance: supported. Targets: CultureMech:002485.

All 9 target and 9 owner timestamps include timezones. Their shared prior events agree; target ends in the August merge and owner in the October 7 evidence-only event. All six current amounts agree across layers, consistent with the event retaining existing concentrations. No historical event, target or owner was rewritten.

## Findings

### f1: The source solvent instruction is missing

major / open / confirmed; issue key: CM002485-solvent-preparation-context.

JCM specifies distilled water 1 L and MediaDive retains 1000 ml water. Neither layer preserves that solvent quantity in preparation. Supported provider g/L values do not replace the missing preparation basis.

### f2: Main autoclave parameters are incompletely retained

major / open / confirmed; issue key: CM002485-autoclave-parameters.

Both layers state autoclave but omit JCM’s page-wide 121 C for 15 min parameters. The sulfur-specific steaming exception is already present and must remain separate. A claim that sterilization is wholly absent would be inaccurate.

### f3: Sulfur powder is reduced to an unspecified sulfur material

major / open / confirmed; issue key: CM002485-sulfur-powder-qualifier.

The primary source and provider attribute specify powder. Both layers retain only Sulfur and a broad sulfur-atom identifier. That ontology term is not itself refuted, but it cannot encode the omitted material specification.

### f4: Five exact owner excerpts are absent from the generated target

minor / open / confirmed; issue key: CM002485-generated-evidence-gap.

The owner has five verified concentration snippets and the corresponding source reference; the generated target lacks them. Sulfur, solvent and preparation need additional narrow owner evidence. The current exact response agrees byte-for-byte with the owner’s historical response hash, while access times remain distinct.

### f5: The secondary sulfur key is absent from the pinned MIM index

minor / open / confirmed; issue key: CM002485-secondary-sulfur-link-unresolved.

Both layers assert mediaingredientmech_chebi_term CHEBI:26833 for sulfur. The complete pinned index has no row for that identifier, including alternate matching modes. Five other secondary keys have verified live preferred-term rows. OLS resolves the primary CHEBI:26833 sulfur term, so this finding concerns only the secondary linkage.

## Recommended Actions And Acceptance Checks

### a1

Preserve the exact solvent instruction with evidence in maintained preparation context; keep nominal solvent quantity distinct from measured final volume and avoid an unnecessary solvent chemical edge.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the primary default for the main mixture while retaining the explicitly separate sulfur treatment and pH-adjustment order, with exact source quotation and scope.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve powder as the exact source material qualifier with evidence; do not invent an allotrope or replace the valid canonical term label solely because it says atom.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve the five exact owner excerpts, add source-supported missing claims and ensure reference/provenance survive separately authorized regeneration without rewriting earlier history.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Reconcile the secondary sulfur linkage against a versioned authoritative MIM source; preserve the five verified links and valid primary CHEBI term. Record the unresolved link explicitly and do not invent or guess a replacement identifier.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch013/125/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch013/125/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml:1:id: CultureMech:002485<br>./data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml:1:id: CultureMech:002485<br> |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:131527 resolves to canonical label dipotassium hydrogen phosphate; term-label correspondence alone does not verify source grade, salt form or stereochemistry. |
| chebi26833 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26833; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26833 resolves to canonical label sulfur atom; term-label correspondence alone does not verify source grade, salt form or stereochemistry. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31795 resolves to canonical label magnesium sulfate heptahydrate; term-label correspondence alone does not verify source grade, salt form or stereochemistry. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32588 resolves to canonical label potassium chloride; term-label correspondence alone does not verify source grade, salt form or stereochemistry. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:62946 resolves to canonical label ammonium sulfate; term-label correspondence alone does not verify source grade, salt form or stereochemistry. |
| chebi64205 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64205; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:64205 resolves to canonical label calcium nitrate; term-label correspondence alone does not verify source grade, salt form or stereochemistry. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | context_only | {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:64205": [{"label": "Ca(NO3)2", "match_type": "preferred_term", "identifier": "CHEBI:64205", "preferred_term": "Ca(NO3)2", "ontology_id": "CHEBI:64205", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26833": []}; Unresolved current secondary keys: ['CHEBI:26833'] |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321; JCM 1321 full composition, recipe preparation and page-wide sterilization default | supports | The exact source specifies six mass components, distilled water 1 L, sulfur as powder, pH adjustment to 2.5 with H2SO4, main-component autoclaving and separate sulfur steaming. The page default gives 121 C for 15 min unless otherwise stated; the sulfur exception is explicitly separate. |
| provider | https://mediadive.dsmz.de/rest/medium/J1321; $.data.medium; $.data.solutions[0].volume/recipe/steps | supports | MediaDive J1321 names JCM GRMD 1321 as its original source, declares 1000 ml and six g/L values. Calcium nitrate is 10 mg with g_l 0.01; sulfur has attribute powder. Its preparation sentence retains the separate sulfur treatment, but not the primary page-wide autoclave parameters. |
| quantities | /private/tmp/culturemech-review-work-batch013/125/quantity-inventory.json; Six target/owner solute amounts plus solvent, acid, pH and two sterilization quantity contexts | context_only | Eleven source-linked decisions preserve literal quotations, exact locators, native vocabulary, original units and distinct preparation stages. Interpretations and conversion arithmetic are outside source quotations. |
| owner-excerpts | data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml; ingredients[0:5].evidence[0]; references[0]; final October 7 curation event | supports | All five owner snippets are literal substrings of the captured exact response and parse to the matching recipe rows. The current response hash equals the historical hash recorded by the owner. This confirms byte agreement, not a new observation of the historical request. Historical and current access times remain distinct. Sulfur lacks corresponding ingredient evidence. |
| writer | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _parse_preparation_steps | context_only | Current importer skips water from chemical composition, reads primary API g_l and only condition/optional qualifiers for direct ingredients, and reads the provider preparation text. Non-stock powder attributes and primary page-wide instructions therefore require separate preservation. This is current-code context, not proof of historical execution. |
| mim-sulfur-absence | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned CSV; every row checked for identifier CHEBI:26833 | refutes | All 9077 CSV rows were read without applying preferred-term or mapping-status filters. No row carries CHEBI:26833. This is an unresolved secondary MIM linkage; the independently resolved primary CHEBI sulfur term remains valid. |

## Limits And Additional Notes

- MediaDive declares a 1000 ml main-solution volume and six g/L values. Primary water 1 L is a solvent instruction, not independent proof of measured final volume after acid adjustment.
- No sulfur allotrope, sulfuric-acid strength or dose, incubation condition, organism-specific growth or density-based conversion is inferred. The JCM 92 iron formulation is a separate source and supplies no replacement quantities here.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T092344Z-culturemech-002485-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 9k_with_sulfur_medium (CultureMech:002485)'
started_at: '2026-10-21T09:12:06Z'
finished_at: '2026-10-21T09:23:44Z'
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
summary: All six recorded solute amounts agree with exact JCM 1321 and provider-declared
  MediaDive concentrations. Both layers omit the preparation solvent and sulfur powder
  qualifier and incompletely preserve the primary autoclave parameters. Five exact
  maintained-owner concentration excerpts are absent from the generated target.
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
  - path: data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml
    sha256: 39734b4bd3b9de47d34b0b8ca4b1daed33abe1896cf1ac3760894a7999bff27d
    role: target
  - path: data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml
    sha256: b3dcc3b6df1240d0abd649afae8750047e3ac85bb0d0120b1503d6aeea2b3ba7
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
  - path: scripts/fetch_medium_concentration_sources.py
    sha256: 746c2828863e6ee409d88409a540ea0a8d01ffad3e38be4a4a47f47bec5bbeb5
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: scripts/review_solution_concentration_evidence.py
    sha256: 40a5bb439caf0791caff746a1eac8d5069525f381c7f3b52556c26937741f65a
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
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
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
  selection: Task review 125; batch 013 item 5 of 10, selected in Python lexicographic
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
  - CultureMech:002485
targets:
- target_id: CultureMech:002485
  path: data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml
  label: 9k_with_sulfur_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002485
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch013/125/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch013/125/strict.tsv"
  target_ids:
  - CultureMech:002485
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002485
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002485
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
  - CultureMech:002485
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T09:23:42Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T09:23:42Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:11.108612Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch013/125/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:14.313850Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-013/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch013/125/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:22.794642Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:13:25.450638Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T09:23:42Z'
  support: supports
  summary: './data/merge_yaml/merged/9K_WITH_SULFUR_MEDIUM.yaml:1:id: CultureMech:002485

    ./data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml:1:id: CultureMech:002485

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
  summary: CHEBI:131527 resolves to canonical label dipotassium hydrogen phosphate;
    term-label correspondence alone does not verify source grade, salt form or stereochemistry.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi26833
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26833
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:04.114839Z'
  support: supports
  summary: CHEBI:26833 resolves to canonical label sulfur atom; term-label correspondence
    alone does not verify source grade, salt form or stereochemistry.
  snapshot_sha256: 34952547270a6bcbbfa3a3699082c8d5359e51d0f90518ab9ca5400494a8ae33
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to canonical label magnesium sulfate heptahydrate;
    term-label correspondence alone does not verify source grade, salt form or stereochemistry.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: CHEBI:32588 resolves to canonical label potassium chloride; term-label
    correspondence alone does not verify source grade, salt form or stereochemistry.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: CHEBI:62946 resolves to canonical label ammonium sulfate; term-label correspondence
    alone does not verify source grade, salt form or stereochemistry.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi64205
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64205
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T09:00:12.945373Z'
  support: supports
  summary: CHEBI:64205 resolves to canonical label calcium nitrate; term-label correspondence
    alone does not verify source grade, salt form or stereochemistry.
  snapshot_sha256: cf808711c3d8005562d7cb492a9da7abcb7a9ae6334934a1f4c5bafd1bd86062
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T09:23:42Z'
  support: context_only
  summary: '{"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label":
    "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term":
    "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:64205": [{"label":
    "Ca(NO3)2", "match_type": "preferred_term", "identifier": "CHEBI:64205", "preferred_term":
    "Ca(NO3)2", "ontology_id": "CHEBI:64205", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:26833": []}; Unresolved current secondary keys: [''CHEBI:26833'']'
- evidence_id: jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321
  locator: JCM 1321 full composition, recipe preparation and page-wide sterilization
    default
  accessed_at: '2026-10-21T09:00:12.947467Z'
  support: supports
  summary: The exact source specifies six mass components, distilled water 1 L, sulfur
    as powder, pH adjustment to 2.5 with H2SO4, main-component autoclaving and separate
    sulfur steaming. The page default gives 121 C for 15 min unless otherwise stated;
    the sulfur exception is explicitly separate.
  snapshot_sha256: 4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1321
  locator: $.data.medium; $.data.solutions[0].volume/recipe/steps
  accessed_at: '2026-10-21T09:00:12.945150Z'
  support: supports
  summary: MediaDive J1321 names JCM GRMD 1321 as its original source, declares 1000
    ml and six g/L values. Calcium nitrate is 10 mg with g_l 0.01; sulfur has attribute
    powder. Its preparation sentence retains the separate sulfur treatment, but not
    the primary page-wide autoclave parameters.
  snapshot_sha256: 3f8c2d333ba84c1ca7f667855b08954eb4b0a0cd5437536e73960484b8c98279
- evidence_id: quantities
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch013/125/quantity-inventory.json
  locator: Six target/owner solute amounts plus solvent, acid, pH and two sterilization
    quantity contexts
  accessed_at: '2026-10-21T09:23:42Z'
  support: context_only
  summary: Eleven source-linked decisions preserve literal quotations, exact locators,
    native vocabulary, original units and distinct preparation stages. Interpretations
    and conversion arithmetic are outside source quotations.
  snapshot_sha256: 81372ba504c7ecb33dc8786d9dc1e12f599ae0c69c7ebc221e2e86953c46d805
- evidence_id: owner-excerpts
  kind: record_content
  reference: data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml
  locator: ingredients[0:5].evidence[0]; references[0]; final October 7 curation event
  accessed_at: '2026-10-21T09:23:42Z'
  support: supports
  summary: All five owner snippets are literal substrings of the captured exact response
    and parse to the matching recipe rows. The current response hash equals the historical
    hash recorded by the owner. This confirms byte agreement, not a new observation
    of the historical request. Historical and current access times remain distinct.
    Sulfur lacks corresponding ingredient evidence.
- evidence_id: writer
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _parse_preparation_steps
  accessed_at: '2026-10-21T09:23:42Z'
  support: context_only
  summary: Current importer skips water from chemical composition, reads primary API
    g_l and only condition/optional qualifiers for direct ingredients, and reads the
    provider preparation text. Non-stock powder attributes and primary page-wide instructions
    therefore require separate preservation. This is current-code context, not proof
    of historical execution.
- evidence_id: mim-sulfur-absence
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned CSV; every row checked for identifier CHEBI:26833
  accessed_at: '2026-10-21T09:23:42Z'
  support: refutes
  summary: All 9077 CSV rows were read without applying preferred-term or mapping-status
    filters. No row carries CHEBI:26833. This is an unresolved secondary MIM linkage;
    the independently resolved primary CHEBI sulfur term remains valid.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002485
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: concern
  summary: '6 primary CHEBI identities resolve with matching labels; 5 of 6 current
    secondary keys have live pinned-index rows. Unresolved keys: [''CHEBI:26833''].'
  target_ids:
  - CultureMech:002485
  evidence_ids:
  - record
  - mim
  - chebi131527
  - chebi26833
  - chebi31795
  - chebi32588
  - chebi62946
  - chebi64205
  details: 6 direct ingredient instances; CHEBI-primary instance linkage 6/6 (100.00%),
    verified secondary coverage 5/6 (83.33%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: JCM recipe identity and MediaDive hosting
  outcome: supported
  summary: CultureMech 002485 denotes JCM GRMD 1321, represented by MediaDive J1321.
    Exact original/source URLs agree and one normalized owner supplies the generated
    target. DSMZ hosts the dataset; JCM is the original recipe collection. Similar
    9K names do not merge the sulfur medium with iron formulations.
  target_ids:
  - CultureMech:002485
  evidence_ids:
  - record
  - owner-0
  - id-search
  - jcm
  - provider
- assessment_id: amounts
  area: quantity
  topic: Every ingredient, original unit and preparation quantity
  outcome: concern
  summary: All six solute values match provider g/L and nominal primary masses. The
    five owner concentration excerpts are exact and appropriately limited to provider-declared
    volume; the generated target has none. Water is absent as preparation context.
    Acid strength and dose are intentionally unquantified. The complete quantity inventory
    separates sulfur treatment and main autoclave parameters.
  target_ids:
  - CultureMech:002485
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - quantities
  - owner-excerpts
  details: '[{"field_path": "ingredients[0].concentration", "owner_field_path": "data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml:ingredients[0].concentration",
    "ingredient": "K2HPO4", "record_value": {"value": "0.5", "unit": "G_PER_L"}, "owner_value":
    {"value": "0.5", "unit": "G_PER_L"}, "decision": "evidence_only", "owner_decision":
    "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321",
    "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161",
    "source_quote": "K 2 HPO 4 0.5 g", "source_locator": "JCM 1321 composition row
    1", "original_source_amount": 0.5, "original_source_unit": "g", "provider_locator":
    "$.data.solutions[0].recipe[0]", "provider_g_l": 0.5, "provider_volume_ml": 1000,
    "stage": "main medium; sulfur is separately sterilized", "explanation": "The provider
    explicitly reports this main-recipe g/L value; the primary gives the same original
    mass and 1 L water. Preserve provider normalization separately from measured final
    volume."}, {"field_path": "ingredients[1].concentration", "owner_field_path":
    "data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml:ingredients[1].concentration",
    "ingredient": "(NH4)2SO4", "record_value": {"value": "3", "unit": "G_PER_L"},
    "owner_value": {"value": "3", "unit": "G_PER_L"}, "decision": "evidence_only",
    "owner_decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321",
    "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161",
    "source_quote": "(NH 4 ) 2 SO 4 3.0 g", "source_locator": "JCM 1321 composition
    row 2", "original_source_amount": 3, "original_source_unit": "g", "provider_locator":
    "$.data.solutions[0].recipe[1]", "provider_g_l": 3, "provider_volume_ml": 1000,
    "stage": "main medium; sulfur is separately sterilized", "explanation": "The provider
    explicitly reports this main-recipe g/L value; the primary gives the same original
    mass and 1 L water. Preserve provider normalization separately from measured final
    volume."}, {"field_path": "ingredients[2].concentration", "owner_field_path":
    "data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml:ingredients[2].concentration",
    "ingredient": "KCl", "record_value": {"value": "0.1", "unit": "G_PER_L"}, "owner_value":
    {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only", "owner_decision":
    "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321",
    "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161",
    "source_quote": "KCl 0.1 g", "source_locator": "JCM 1321 composition row 3", "original_source_amount":
    0.1, "original_source_unit": "g", "provider_locator": "$.data.solutions[0].recipe[2]",
    "provider_g_l": 0.1, "provider_volume_ml": 1000, "stage": "main medium; sulfur
    is separately sterilized", "explanation": "The provider explicitly reports this
    main-recipe g/L value; the primary gives the same original mass and 1 L water.
    Preserve provider normalization separately from measured final volume."}, {"field_path":
    "ingredients[3].concentration", "owner_field_path": "data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml:ingredients[3].concentration",
    "ingredient": "MgSO4 x 7 H2O", "record_value": {"value": "0.5", "unit": "G_PER_L"},
    "owner_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "evidence_only",
    "owner_decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321",
    "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161",
    "source_quote": "MgSO 4 ·7H 2 O 0.5 g", "source_locator": "JCM 1321 composition
    row 4", "original_source_amount": 0.5, "original_source_unit": "g", "provider_locator":
    "$.data.solutions[0].recipe[3]", "provider_g_l": 0.5, "provider_volume_ml": 1000,
    "stage": "main medium; sulfur is separately sterilized", "explanation": "The provider
    explicitly reports this main-recipe g/L value; the primary gives the same original
    mass and 1 L water. Preserve provider normalization separately from measured final
    volume."}, {"field_path": "ingredients[4].concentration", "owner_field_path":
    "data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml:ingredients[4].concentration",
    "ingredient": "Ca(NO3)2", "record_value": {"value": "0.01", "unit": "G_PER_L"},
    "owner_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "evidence_only",
    "owner_decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321",
    "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161",
    "source_quote": "Ca(NO 3 ) 2 10.0 mg", "source_locator": "JCM 1321 composition
    row 5", "original_source_amount": 10, "original_source_unit": "mg", "provider_locator":
    "$.data.solutions[0].recipe[4]", "provider_g_l": 0.01, "provider_volume_ml": 1000,
    "stage": "main medium; sulfur is separately sterilized", "explanation": "The provider
    explicitly reports this main-recipe g/L value; the primary gives the same original
    mass and 1 L water. Preserve provider normalization separately from measured final
    volume. Exact conversion: 10 mg × 0.001 g/mg = 0.01 g, consistent with provider
    0.01 g/L on its declared 1000 ml basis."}, {"field_path": "ingredients[5].concentration",
    "owner_field_path": "data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml:ingredients[5].concentration",
    "ingredient": "Sulfur", "record_value": {"value": "5", "unit": "G_PER_L"}, "owner_value":
    {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "owner_decision": "correct",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321",
    "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161",
    "source_quote": "Sulfur (powder) 5.0 g", "source_locator": "JCM 1321 composition
    row 6", "original_source_amount": 5, "original_source_unit": "g", "provider_locator":
    "$.data.solutions[0].recipe[5]", "provider_g_l": 5, "provider_volume_ml": 1000,
    "stage": "main medium; sulfur is separately sterilized", "explanation": "The provider
    explicitly reports this main-recipe g/L value; the primary gives the same original
    mass and 1 L water. Preserve provider normalization separately from measured final
    volume. The numerical value is supported, but the exact source material is sulfur
    powder and that qualifier is absent from both layers. No molecular allotrope is
    inferred from the word powder."}, {"field_path": "preparation_steps (source-only
    solvent)", "decision": "add", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321",
    "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161",
    "source_quote": "Distilled water 1.0 L", "source_locator": "JCM 1321 composition
    water row", "stage": "main preparation solvent", "explanation": "Preserve the
    literal 1 L water instruction in preparation context. Avoiding a water composition
    edge does not justify omitting the solvent basis; do not claim measured final
    volume."}, {"field_path": "preparation_steps[0] acid addition", "decision": "not_quantified",
    "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321",
    "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161",
    "source_quote": "adjust pH to 2.5 with H 2 SO 4", "source_locator": "JCM 1321
    preparation sentence", "stage": "pH adjustment before main-component autoclaving",
    "explanation": "The acid identity and endpoint are explicit but its strength and
    fixed dose are not. Retain endpoint-controlled addition without borrowing a strength
    or dose from another 9K recipe."}, {"field_path": "ph_value; preparation_steps[0]",
    "decision": "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321",
    "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161",
    "source_quote": "adjust pH to 2.5", "source_locator": "JCM 1321 preparation sentence",
    "stage": "preparation endpoint", "explanation": "Target and owner preserve 2.5
    at the documented adjustment stage. This is not an incubation optimum or measured
    post-growth pH."}, {"field_path": "preparation_steps[0] sulfur treatment", "decision":
    "verified", "source_reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321",
    "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161",
    "source_quote": "steaming for 3 hr on each of 3 successive days", "source_locator":
    "JCM 1321 separate sulfur preparation sentence", "stage": "sulfur stock material
    treatment", "explanation": "Both layers preserve the duration and repeated-day
    instruction. Keep it separate from the main-medium autoclave default."}, {"field_path":
    "preparation_steps[0] main autoclaving", "decision": "add", "source_reference":
    "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1321", "source_sha256": "4c874cc1a74c8fa629cf6d18ef5d816dc7239120c07037e92edfdf2862855161",
    "source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C
    for 15 min.", "source_locator": "JCM page-wide instruction before medium 1321
    heading", "stage": "main mixture excluding sulfur", "explanation": "Both layers
    name autoclaving but omit these source temperature/time parameters. The source-specific
    separate sulfur treatment remains an explicit exception; do not replace it with
    this default."}]'
- assessment_id: forms
  area: grounding
  topic: All six chemical identities, hydration and sulfur material
  outcome: concern
  summary: Every asserted CHEBI label resolves. Source K2HPO4, ammonium sulfate, KCl,
    magnesium sulfate heptahydrate and calcium nitrate agree at their stated forms.
    Calcium nitrate is not silently converted to a hydrate. Sulfur-atom ontology metadata
    includes Elemental sulfur as a synonym, so atom wording alone is not evidence
    of a wrong ID; the separately asserted primary powder form is missing. No unasserted
    allotrope or molarity is introduced.
  target_ids:
  - CultureMech:002485
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - mim
  - chebi131527
  - chebi62946
  - chebi32588
  - chebi31795
  - chebi64205
  - chebi26833
- assessment_id: preparation
  area: completeness
  topic: Solvent, main autoclaving and separate sulfur treatment
  outcome: concern
  summary: Both layers preserve pH 2.5 with H2SO4, autoclaving of the other components
    and separate sulfur steaming for 3 hours on each of 3 days. They omit 1 L water
    and the primary page-wide 121 C/15 min parameters for main autoclaving. This is
    incomplete source context, not an absence of all sterilization or a reason to
    overwrite the sulfur exception.
  target_ids:
  - CultureMech:002485
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - writer
  - quantities
- assessment_id: classification
  area: scope
  topic: Defined composition and liquid-medium boundaries
  outcome: supported
  summary: The stated constituents are defined chemicals, and LIQUID describes the
    non-agar medium without claiming every material is dissolved; sulfur powder may
    remain a distinct material phase. No organism, strain, native variant, parent,
    external KG match or measured growth claim is present. General cultivation and
    bacterial filing do not establish a specific growth outcome.
  target_ids:
  - CultureMech:002485
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
- assessment_id: evidence
  area: evidence
  topic: Exact owner support and generated evidence omission
  outcome: concern
  summary: The owner carries five source-linked ingredient snippets and a reference
    absent from the generated target. Sulfur and solvent/preparation claims still
    need narrow evidence in the owner. The reference accurately distinguishes JCM
    origin from DSMZ dataset hosting and leaves unknown author/year unset. Target
    reference checks examined zero excerpts; canonical passes are not a substitute
    for these source comparisons.
  target_ids:
  - CultureMech:002485
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - owner-excerpts
  - validate-references
- assessment_id: history
  area: provenance
  topic: Historical evidence curation and generated timestamp
  outcome: supported
  summary: All 9 target and 9 owner timestamps include timezones. Their shared prior
    events agree; target ends in the August merge and owner in the October 7 evidence-only
    event. All six current amounts agree across layers, consistent with the event
    retaining existing concentrations. No historical event, target or owner was rewritten.
  target_ids:
  - CultureMech:002485
  evidence_ids:
  - record
  - owner-0
  - owner-excerpts
findings:
- finding_id: f1
  issue_key: CM002485-solvent-preparation-context
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The source solvent instruction is missing
  description: JCM specifies distilled water 1 L and MediaDive retains 1000 ml water.
    Neither layer preserves that solvent quantity in preparation. Supported provider
    g/L values do not replace the missing preparation basis.
  target_ids:
  - CultureMech:002485
  field_paths:
  - preparation_steps
  - notes
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - quantities
  - writer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CM002485-autoclave-parameters
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Main autoclave parameters are incompletely retained
  description: Both layers state autoclave but omit JCM’s page-wide 121 C for 15 min
    parameters. The sulfur-specific steaming exception is already present and must
    remain separate. A claim that sterilization is wholly absent would be inaccurate.
  target_ids:
  - CultureMech:002485
  field_paths:
  - preparation_steps[0]
  - sterilization
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: CM002485-sulfur-powder-qualifier
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Sulfur powder is reduced to an unspecified sulfur material
  description: The primary source and provider attribute specify powder. Both layers
    retain only Sulfur and a broad sulfur-atom identifier. That ontology term is not
    itself refuted, but it cannot encode the omitted material specification.
  target_ids:
  - CultureMech:002485
  field_paths:
  - ingredients[5].preferred_term
  - ingredients[5].notes
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - chebi26833
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: CM002485-generated-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Five exact owner excerpts are absent from the generated target
  description: The owner has five verified concentration snippets and the corresponding
    source reference; the generated target lacks them. Sulfur, solvent and preparation
    need additional narrow owner evidence. The current exact response agrees byte-for-byte
    with the owner’s historical response hash, while access times remain distinct.
  target_ids:
  - CultureMech:002485
  field_paths:
  - ingredients[*].evidence
  - references
  - evidence
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - owner-excerpts
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: CM002485-secondary-sulfur-link-unresolved
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: The secondary sulfur key is absent from the pinned MIM index
  description: Both layers assert mediaingredientmech_chebi_term CHEBI:26833 for sulfur.
    The complete pinned index has no row for that identifier, including alternate
    matching modes. Five other secondary keys have verified live preferred-term rows.
    OLS resolves the primary CHEBI:26833 sulfur term, so this finding concerns only
    the secondary linkage.
  target_ids:
  - CultureMech:002485
  field_paths:
  - ingredients[5].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - mim
  - mim-sulfur-absence
  - chebi26833
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml
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
  description: Preserve the exact solvent instruction with evidence in maintained
    preparation context; keep nominal solvent quantity distinct from measured final
    volume and avoid an unnecessary solvent chemical edge.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml
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
  description: Preserve the primary default for the main mixture while retaining the
    explicitly separate sulfur treatment and pH-adjustment order, with exact source
    quotation and scope.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml
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
  description: Preserve powder as the exact source material qualifier with evidence;
    do not invent an allotrope or replace the valid canonical term label solely because
    it says atom.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml
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
  description: Preserve the five exact owner excerpts, add source-supported missing
    claims and ensure reference/provenance survive separately authorized regeneration
    without rewriting earlier history.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml
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
  description: Reconcile the secondary sulfur linkage against a versioned authoritative
    MIM source; preserve the five verified links and valid primary CHEBI term. Record
    the unresolved link explicitly and do not invent or guess a replacement identifier.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:002485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/9k_with_sulfur_medium.yaml
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
- MediaDive declares a 1000 ml main-solution volume and six g/L values. Primary water
  1 L is a solvent instruction, not independent proof of measured final volume after
  acid adjustment.
- No sulfur allotrope, sulfuric-acid strength or dose, incubation condition, organism-specific
  growth or density-based conversion is inferred. The JCM 92 iron formulation is a
  separate source and supplies no replacement quantities here.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-013
- generated-medium
```
