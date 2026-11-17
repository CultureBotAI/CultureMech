# Source and formulation review: 480g_medium (CultureMech:003312)

- Review: 20261021T082326Z-culturemech-003312-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T08:09:21Z
- Finished UTC: 2026-10-21T08:23:26Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The official live JCM964 recipe and MediaDive J964 agree on the 480G medium identity and source masses, but both local layers flatten six A5 stock ingredients into final-medium concentrations and turn a 5 mL addition of 5% sodium sulfide nonahydrate stock into 5 g/L. The source expressly doses A5 as 1 g, so its final trace concentrations cannot be calculated by assuming 1 mL. Nine direct quantities match the provider’s 1005 mL normalization rather than an independently established primary final volume. Preparation loses the stock-addition details; four documented diagnostics pass.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 100; batch 010 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding nine task batches contain 90 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 92 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003312 | data/merge_yaml/merged/480G_MEDIUM.yaml | generated | 480g_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003312 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003312 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch010/100/strict.tsv |
| validate-terms | passed | True | CultureMech:003312 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003312 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003312 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Target and owner timestamp syntax and timezone scope | passed | False | CultureMech:003312 | All 13 target/owner history timestamps parse with explicit timezones; timestamp syntax is not scientific validation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003312.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:003312.

14 primary CHEBI identities resolve with matching labels; 14 of 14 current secondary keys have live pinned-index rows. Unresolved keys: [].

16 direct ingredient instances; CHEBI-primary instance linkage 14/16 (87.50%), verified secondary coverage 14/16 (87.50%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Exact 480G medium and normalized owner

identity: supported. Targets: CultureMech:003312.

Stable CM003312, singleton merge-event source, maintained owner, official JCM964 and provider J964 all identify 480G medium. No similarly named medium or neighboring source accession is substituted.

### Every direct amount and nested stock

quantity: concern. Targets: CultureMech:003312.

All 16 direct rows are traced: nine agree with provider-normalized source masses; sulfide misstates an mL stock dose as g/L; six A5 stock rows are flattened into final-medium concentrations. The primary and provider both explicitly say A5 solution 1 g; unknown density blocks a volume dilution.

[{"field": "ingredients[0].concentration", "material": "NaCl", "local": {"value": "0.497512", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator": "$.data.solutions[0].recipe[0]", "source_row": {"recipe_order": 1, "compound": "NaCl", "compound_id": 43, "amount": 0.5, "unit": "g", "g_l": 0.497512, "mmol_l": 8.51322, "optional": 0}, "decision": "verified as provider-normalized mass; evidence_only for exact primary final-volume claim", "calculation": "0.5g /1.005L = 0.4975124378109452736318407960g/L; provider nominal-volume normalization, subject to primary final-volume limitation."}, {"field": "ingredients[1].concentration", "material": "NH4Cl", "local": {"value": "0.328358", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator": "$.data.solutions[0].recipe[1]", "source_row": {"recipe_order": 2, "compound": "NH4Cl", "compound_id": 42, "amount": 0.33, "unit": "g", "g_l": 0.328358, "mmol_l": 6.13868, "optional": 0}, "decision": "verified as provider-normalized mass; evidence_only for exact primary final-volume claim", "calculation": "0.33g /1.005L = 0.3283582089552238805970149254g/L; provider nominal-volume normalization, subject to primary final-volume limitation."}, {"field": "ingredients[2].concentration", "material": "CaCl2 x 2 H2O", "local": {"value": "0.149254", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator": "$.data.solutions[0].recipe[2]", "source_row": {"recipe_order": 3, "compound": "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.15, "unit": "g", "g_l": 0.149254, "mmol_l": 1.01523, "optional": 0}, "decision": "verified as provider-normalized mass; evidence_only for exact primary final-volume claim", "calculation": "0.15g /1.005L = 0.1492537313432835820895522388g/L; provider nominal-volume normalization, subject to primary final-volume limitation."}, {"field": "ingredients[3].concentration", "material": "MgCl2 x 6 H2O", "local": {"value": "0.348259", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator": "$.data.solutions[0].recipe[3]", "source_row": {"recipe_order": 4, "compound": "MgCl2 x 6 H2O", "compound_id": 79, "amount": 0.35, "unit": "g", "g_l": 0.348259, "mmol_l": 1.713, "optional": 0}, "decision": "verified as provider-normalized mass; evidence_only for exact primary final-volume claim", "calculation": "0.35g /1.005L = 0.3482587064676616915422885572g/L; provider nominal-volume normalization, subject to primary final-volume limitation."}, {"field": "ingredients[4].concentration", "material": "KCl", "local": {"value": "0.298507", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator": "$.data.solutions[0].recipe[4]", "source_row": {"recipe_order": 5, "compound": "KCl", "compound_id": 61, "amount": 0.3, "unit": "g", "g_l": 0.298507, "mmol_l": 4.00412, "optional": 0}, "decision": "verified as provider-normalized mass; evidence_only for exact primary final-volume claim", "calculation": "0.3g /1.005L = 0.2985074626865671641791044776g/L; provider nominal-volume normalization, subject to primary final-volume limitation."}, {"field": "ingredients[5].concentration", "material": "KH2PO4", "local": {"value": "0.298507", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator": "$.data.solutions[0].recipe[5]", "source_row": {"recipe_order": 6, "compound": "KH2PO4", "compound_id": 11, "amount": 0.3, "unit": "g", "g_l": 0.298507, "mmol_l": 2.19352, "optional": 0}, "decision": "verified as provider-normalized mass; evidence_only for exact primary final-volume claim", "calculation": "0.3g /1.005L = 0.2985074626865671641791044776g/L; provider nominal-volume normalization, subject to primary final-volume limitation."}, {"field": "ingredients[6].concentration", "material": "Casitone", "local": {"value": "0.995025", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator": "$.data.solutions[0].recipe[6]", "source_row": {"recipe_order": 7, "compound": "Casitone", "compound_id": 84, "attribute": "BD-Difco", "amount": 1, "unit": "g", "g_l": 0.995025, "optional": 0}, "decision": "verified as provider-normalized mass; evidence_only for exact primary final-volume claim", "calculation": "1g /1.005L = 0.9950248756218905472636815920g/L; provider nominal-volume normalization, subject to primary final-volume limitation."}, {"field": "ingredients[7].concentration", "material": "Yeast extract", "local": {"value": "0.497512", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator": "$.data.solutions[0].recipe[7]", "source_row": {"recipe_order": 8, "compound": "Yeast extract", "compound_id": 16, "amount": 0.5, "unit": "g", "g_l": 0.497512, "optional": 0}, "decision": "verified as provider-normalized mass; evidence_only for exact primary final-volume claim", "calculation": "0.5g /1.005L = 0.4975124378109452736318407960g/L; provider nominal-volume normalization, subject to primary final-volume limitation."}, {"field": "ingredients[8].concentration", "material": "Resazurin", "local": {"value": "0.000995025", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator": "$.data.solutions[0].recipe[9]", "source_row": {"recipe_order": 10, "compound": "Resazurin", "compound_id": 25, "amount": 1, "unit": "mg", "g_l": 0.000995025, "mmol_l": 0.00434148, "optional": 0}, "decision": "verified as provider-normalized mass; evidence_only for exact primary final-volume claim", "calculation": "0.001g /1.005L = 0.0009950248756218905472636815920g/L; provider nominal-volume normalization, subject to primary final-volume limitation."}, {"field": "ingredients[9].concentration", "material": "Na2S x 9 H2O", "local": {"value": "5", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator": "$.data.solutions[0].recipe[11]", "source_row": {"recipe_order": 12, "compound": "Na2S x 9 H2O", "compound_id": 54, "attribute": "5%", "amount": 5, "unit": "ml", "optional": 0}, "decision": "correct: source5mL of5% stock after cooling, not5g/L neat sulfide; percent basis unresolved", "calculation": null}, {"field": "ingredients[10].concentration", "material": "Co(NO3)2 x 6 H2O", "local": {"value": "0.00494", "unit": "G_PER_L"}, "source_solution_id": 4987, "source_locator": "$.data.solutions[1].recipe[0]", "source_row": {"recipe_order": 1, "compound": "Co(NO3)2 x 6 H2O", "compound_id": 541, "amount": 4.94, "unit": "mg", "g_l": 0.00494, "mmol_l": 0.0169739, "optional": 0}, "decision": "correct stock-stage: source A5 stock concentration per1L; final-medium contribution not_quantified because stock addition is1g and density/mass fraction is unknown", "calculation": null}, {"field": "ingredients[11].concentration", "material": "CuSO4 x 5 H2O", "local": {"value": "0.0079", "unit": "G_PER_L"}, "source_solution_id": 4987, "source_locator": "$.data.solutions[1].recipe[1]", "source_row": {"recipe_order": 2, "compound": "CuSO4 x 5 H2O", "compound_id": 121, "amount": 7.9, "unit": "mg", "g_l": 0.0079, "mmol_l": 0.0316397, "optional": 0}, "decision": "correct stock-stage: source A5 stock concentration per1L; final-medium contribution not_quantified because stock addition is1g and density/mass fraction is unknown", "calculation": null}, {"field": "ingredients[12].concentration", "material": "H3BO3", "local": {"value": "0.286", "unit": "G_PER_L"}, "source_solution_id": 4987, "source_locator": "$.data.solutions[1].recipe[2]", "source_row": {"recipe_order": 3, "compound": "H3BO3", "compound_id": 37, "amount": 0.286, "unit": "g", "g_l": 0.286, "mmol_l": 4.62484, "optional": 0}, "decision": "correct stock-stage: source A5 stock concentration per1L; final-medium contribution not_quantified because stock addition is1g and density/mass fraction is unknown", "calculation": null}, {"field": "ingredients[13].concentration", "material": "MnCl2 x 4 H2O", "local": {"value": "0.181", "unit": "G_PER_L"}, "source_solution_id": 4987, "source_locator": "$.data.solutions[1].recipe[3]", "source_row": {"recipe_order": 4, "compound": "MnCl2 x 4 H2O", "compound_id": 36, "amount": 0.181, "unit": "g", "g_l": 0.181, "optional": 0}, "decision": "correct stock-stage: source A5 stock concentration per1L; final-medium contribution not_quantified because stock addition is1g and density/mass fraction is unknown", "calculation": null}, {"field": "ingredients[14].concentration", "material": "Na2MoO4 x 2 H2O", "local": {"value": "0.039", "unit": "G_PER_L"}, "source_solution_id": 4987, "source_locator": "$.data.solutions[1].recipe[4]", "source_row": {"recipe_order": 5, "compound": "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 39, "unit": "mg", "g_l": 0.039, "mmol_l": 0.16119, "optional": 0}, "decision": "correct stock-stage: source A5 stock concentration per1L; final-medium contribution not_quantified because stock addition is1g and density/mass fraction is unknown", "calculation": null}, {"field": "ingredients[15].concentration", "material": "ZnSO4 x 7 H2O", "local": {"value": "0.0222", "unit": "G_PER_L"}, "source_solution_id": 4987, "source_locator": "$.data.solutions[1].recipe[5]", "source_row": {"recipe_order": 6, "compound": "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 22.2, "unit": "mg", "g_l": 0.0222, "mmol_l": 0.077201, "optional": 0}, "decision": "correct stock-stage: source A5 stock concentration per1L; final-medium contribution not_quantified because stock addition is1g and density/mass fraction is unknown", "calculation": null}]

### A5 and sulfide source additions

representation: concern. Targets: CultureMech:003312.

A5 stock per 1 L contains cobalt nitrate hexahydrate 4.94 mg, copper sulfate pentahydrate 7.9 mg, boric acid 0.286 g, manganese chloride tetrahydrate 0.181 g, sodium molybdate dihydrate 39 mg and zinc sulfate heptahydrate 22.2 mg. The receiving medium adds 1 g of that solution; these six stock amounts are not direct final-medium concentrations. Sulfide is a separate 5 mL 5% stock added after cooling. Neither dose is represented as a structured solution addition in either local layer.

### One retained step and source-specific sterilization

completeness: concern. Targets: CultureMech:003312.

The single step correctly preserves N2 autoclaving, post-cooling addition and the parenthetical requirement that the added solution be autoclaved and stored under N2. It ends with following solution without identifying the 5 mL 5% sulfide dose to which that qualifier applies, and does not preserve the A5 stock recipe as a separate preparation. The current primary header supplies 121 °C for 15 min as the default. The record has no pH; neither exact source supplies one, so no pH finding or invented value is added.

### Matching local layers and current import behavior

ownership: concern. Targets: CultureMech:003312.

Target and maintained owner have equal ingredients and preparation; the scientific defects persist in the normalized input. Current importer has stock-preservation logic, but no import/regeneration was run. Correct the owner with exact source evidence and preserve upstream unit ambiguity before regenerating.

### Composition class, growth, variants and history

scope: supported. Targets: CultureMech:003312.

Complex/undefined liquid status is consistent with Casitone and yeast extract and no agar. Generic microbial-cultivation application does not establish a species/strain outcome. There are no target organisms, variants, parent/child links, taxon/assembly identifiers or publications to overgeneralize. Source pH and growth temperature remain unspecified. Import/canonicalization history is provenance rather than scientific approval.

### Source citation and concentration evidence placement

evidence: concern. Targets: CultureMech:003312.

The official JCM URL appears in notes and J964 in media_term, but both local layers lack structured references and claim-level formulation/stock evidence. A repair must retain exact public source, batch basis, source 1 g A5 unit and uncertain percentage basis. The deterministic reference recipe reports 0 reference checks, not external validation of those notes. All target/owner history timestamps were inspected with timezone scope and preserved.

## Findings

### f1: A 5 mL addition of 5% sulfide stock is encoded as 5 g/L

major / open / confirmed; issue key: cm003312-sulfide-stock-dose-as-mass.

ingredients[9] stores sodium sulfide nonahydrate 5 g/L, while official JCM964 and the provider specify 5 mL of 5% solution after cooling. The retained preparation step loses the actual addition it refers to. The percentage basis is not stated, so the remedy is to preserve the stock/dose and resolve its basis rather than invent a replacement final mass concentration.

### f2: Six A5 stock concentrations are misrepresented as final-medium values

major / open / confirmed; issue key: cm003312-a5-stock-flattening.

The last six direct ingredients equal the A5 stock recipe per 1 L. Both sources instead add 1 g of A5 solution to the receiving medium. Omitting that stock/dose relationship makes these final concentration assertions unsupported; replacing 1 g with 1 mL would be an unverified source correction.

### f3: Source quantities and stock-stage limits lack structured evidence

minor / open / confirmed; issue key: cm003312-formulation-evidence-placement.

The official URL exists in notes, but neither layer has structured references or claim-level formulation/stock evidence. In this record the missing stage-specific evidence obscures the provider 1005 mL normalization, source A5 mass dose and percent-basis uncertainty.

## Recommended Actions And Acceptance Checks

### a1

Represent the source 5 mL 5% sulfide stock and its post-cooling, separately autoclaved N2 storage context; preserve the primary 121 °C 15 min default where applicable and resolve percentage basis before mass conversion.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore A5 as the source-defined stock with its six constituent amounts per 1 L and literal 1 g receiving dose. Leave final trace contributions unresolved until density/mass fraction or a corrected authoritative source is verified; do not double-count expanded constituents.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Add the exact JCM and provider versions as structured references and narrow amount/stock evidence with original units, locators and explicit conversion limits; retain notes provenance rather than replace it with an unsupported DOI.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/480G_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/480g_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/480G_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/480G_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch010/100/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch010/100/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/480G_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/480G_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=964; 964 480G MEDIUM; A5 solution section; shared sterilization header | supports | Read complete official JCM964 medium page: nine direct solute masses, A5 solution 1.0 g,1 L water,5 mL 5% sodium sulfide nonahydrate after cooling, anaerobic N2 handling, and the six-constituent A5 recipe per 1 L. The page default is 121 °C 15 min autoclaving unless otherwise stated. |
| provider | https://mediadive.dsmz.de/rest/medium/J964; $.data.medium; $.data.solutions[0:2] | supports | Exact J964 identity and link agree with JCM. Main solution 4986 declares 1005 mL and contains the source doses including A5 solution 4987 amount 1, unit g and sulfide amount 5, unit ml attribute 5%. Nested 4987 is 1000 mL stock with six solutes and water. |
| pdf-unavailable | https://jcm.brc.riken.jp/en/wp-content/uploads/medium/JCM964.pdf; HTTP status | unknown | Candidate official static PDF returned 404; exact live official HTML remains available and supplies the recipe. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31206 resolves to ammonium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32588 resolves to potassium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:33118 resolves to boric acid and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:75213 resolves to sodium molybdate dihydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86158 resolves to calcium chloride dihydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86214 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86214; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86214 resolves to cobalt dinitrate hexahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:8806 resolves to Resazurin and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86214": [{"label": "Co(NO3)2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86214", "preferred_term": "Co(NO3)2 x 6 H2O", "ontology_id": "CHEBI:86214", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| importer | src/culturemech/import/mediadive_importer.py; _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _normalize_unit | context_only | Current importer keeps primary formulation rows separate from later stocks and recognizes explicit solution_id plus percentage-bearing mL additions. It can retain A5 solution_id 4987 with source 1 g and the 5% sulfide addition with 5 mL, instead of flattening later stock rows. This read-only code comparison is not a claim that rerunning an import has repaired these persisted recipes or resolved A5 density. |
| history | data/merge_yaml/merged/480G_MEDIUM.yaml; Every timestamp in target and sole normalized owner | supports | [{"path": "data/merge_yaml/merged/480G_MEDIUM.yaml", "field": "curation_history[0].timestamp", "value": "2026-01-26T17:53:18.150706Z", "timezone_aware": true}, {"path": "data/merge_yaml/merged/480G_MEDIUM.yaml", "field": "curation_history[1].timestamp", "value": "2026-03-13T06:19:19.409471Z", "timezone_aware": true}, {"path": "data/merge_yaml/merged/480G_MEDIUM.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-17T06:30:19.000000Z", "timezone_aware": true}, {"path": "data/merge_yaml/merged/480G_MEDIUM.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-17T19:45:33.363042+00:00", "timezone_aware": true}, {"path": "data/merge_yaml/merged/480G_MEDIUM.yaml", "field": "curation_history[4].timestamp", "value": "2026-06-05T07:40:15.831277+00:00", "timezone_aware": true}, {"path": "data/merge_yaml/merged/480G_MEDIUM.yaml", "field": "curation_history[5].timestamp", "value": "2026-06-10T07:46:42.559880+00:00", "timezone_aware": true}, {"path": "data/merge_yaml/merged/480G_MEDIUM.yaml", "field": "curation_history[6].timestamp", "value": "2026-08-06T03:04:34.119062+00:00", "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/480g_medium.yaml", "field": "curation_history[0].timestamp", "value": "2026-01-26T17:53:18.150706Z", "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/480g_medium.yaml", "field": "curation_history[1].timestamp", "value": "2026-03-13T06:19:19.409471Z", "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/480g_medium.yaml", "field": "curation_history[2].timestamp", "value": "2026-03-17T06:30:19.000000Z", "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/480g_medium.yaml", "field": "curation_history[3].timestamp", "value": "2026-03-17T19:45:33.363042+00:00", "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/480g_medium.yaml", "field": "curation_history[4].timestamp", "value": "2026-06-05T07:40:15.831277+00:00", "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/480g_medium.yaml", "field": "curation_history[5].timestamp", "value": "2026-06-10T07:46:42.559880+00:00", "timezone_aware": true}] |

## Limits And Additional Notes

- JCM explicitly lists A5 solution 1.0 g. No stock density, mass fraction or correction to 1 mL was verified; the final contribution of each A5 constituent remains unquantified. The review preserves the source’s unit rather than silently repairing it.
- JCM says 5% sodium sulfide nonahydrate solution without explicitly naming w/v, w/w or v/v basis. The supported addition is 5 mL after cooling; no fixed final sulfide mass concentration is asserted from the percentage alone.
- The primary recipe uses 1 L distilled water followed by a 5 mL stock addition; MediaDive declares 1005 mL. Its g/L values are identifiable provider normalizations, not independent proof of measured final volume or a primary make-to-volume instruction.
- A bounded official static-PDF candidate returned 404. Exact live official JCM964 HTML and provider API were successfully retrieved; no unavailable PDF text is treated as evidence.
- No target organism, strain, taxonomy identifier, assembly, DOI/PMID or literature-growth claim is asserted. The review does not infer such claims from the medium title or add generic cultivation conditions.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T082326Z-culturemech-003312-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 480g_medium (CultureMech:003312)'
started_at: '2026-10-21T08:09:21Z'
finished_at: '2026-10-21T08:23:26Z'
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
summary: The official live JCM964 recipe and MediaDive J964 agree on the 480G medium
  identity and source masses, but both local layers flatten six A5 stock ingredients
  into final-medium concentrations and turn a 5 mL addition of 5% sodium sulfide nonahydrate
  stock into 5 g/L. The source expressly doses A5 as 1 g, so its final trace concentrations
  cannot be calculated by assuming 1 mL. Nine direct quantities match the provider’s
  1005 mL normalization rather than an independently established primary final volume.
  Preparation loses the stock-addition details; four documented diagnostics pass.
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
  - path: data/merge_yaml/merged/480G_MEDIUM.yaml
    sha256: f677210fee8b93f60acc07de3d72cc6ba90722f5249f87da1bd671f2d6442d2f
    role: target
  - path: data/normalized_yaml/bacterial/480g_medium.yaml
    sha256: c9d9e8d6182eba7f7690daae23b8b0f333887952ac315453b0f39e71276c2848
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
  selection: Task review 100; batch 010 item 10 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding nine task batches contain
    90 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 92 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003312
targets:
- target_id: CultureMech:003312
  path: data/merge_yaml/merged/480G_MEDIUM.yaml
  label: 480g_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/480g_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/480G_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003312
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/480G_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch010/100/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch010/100/strict.tsv"
  target_ids:
  - CultureMech:003312
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/480G_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003312
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/480G_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003312
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
  - CultureMech:003312
- check_id: scoped-history-timestamps
  name: Target and owner timestamp syntax and timezone scope
  required: false
  status: passed
  summary: All 13 target/owner history timestamps parse with explicit timezones; timestamp
    syntax is not scientific validation.
  target_ids:
  - CultureMech:003312
  evidence_ids:
  - history
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/480G_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T08:23:26Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/480g_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T08:23:26Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/480G_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:10:22.570258Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/480G_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch010/100/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T08:10:24.447269Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch010/100/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/480G_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:10:27.735031Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/480G_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:10:30.990864Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: jcm
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=964
  locator: 964 480G MEDIUM; A5 solution section; shared sterilization header
  accessed_at: '2026-10-21T08:04:45.364600Z'
  support: supports
  summary: 'Read complete official JCM964 medium page: nine direct solute masses,
    A5 solution 1.0 g,1 L water,5 mL 5% sodium sulfide nonahydrate after cooling,
    anaerobic N2 handling, and the six-constituent A5 recipe per 1 L. The page default
    is 121 °C 15 min autoclaving unless otherwise stated.'
  snapshot_sha256: 01248513258223a3d112bb88ce29768c2e0c2b5c9bb6931f0464ec871c27497a
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J964
  locator: $.data.medium; $.data.solutions[0:2]
  accessed_at: '2026-10-21T08:04:43.150888Z'
  support: supports
  summary: Exact J964 identity and link agree with JCM. Main solution 4986 declares
    1005 mL and contains the source doses including A5 solution 4987 amount 1, unit
    g and sulfide amount 5, unit ml attribute 5%. Nested 4987 is 1000 mL stock with
    six solutes and water.
  snapshot_sha256: d87f41d44d0e086f2cae9648445e21b1edc76da0e6eb18b535097383cb119529
- evidence_id: pdf-unavailable
  kind: search
  reference: https://jcm.brc.riken.jp/en/wp-content/uploads/medium/JCM964.pdf
  locator: HTTP status
  accessed_at: '2026-10-21T08:05:46.422684Z'
  support: unknown
  summary: Candidate official static PDF returned 404; exact live official HTML remains
    available and supplies the recipe.
  snapshot_sha256: 3b823caf114dbf76ca3f609fc0be6ac2890f5cf3cc549be12bca64b06e6c78ef
  search_scope: Bounded exact public HTTP request to https://jcm.brc.riken.jp/en/wp-content/uploads/medium/JCM964.pdf
    at the recorded access time. The returned body/status is preserved; no neighboring
    accession, inferred formulation, or exhaustive web absence claim is used. This
    is an external endpoint check; ignored local files are not part of this access
    test.
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:00:48.036367Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:00:48.109537Z'
  support: supports
  summary: CHEBI:31206 resolves to ammonium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:07.786285Z'
  support: supports
  summary: CHEBI:31440 resolves to copper(II) sulfate pentahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:07.609898Z'
  support: supports
  summary: CHEBI:32312 resolves to zinc sulfate heptahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:00.737662Z'
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
  accessed_at: '2026-10-20T06:55:02.761234Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:00:48.758019Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:08.404288Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: CHEBI:76209 resolves to sodium sulfide nonahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:00:48.898092Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86214
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86214
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:33:34.945310Z'
  support: supports
  summary: CHEBI:86214 resolves to cobalt dinitrate hexahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 90cf3337643bc22bd3940bfbdee70a144b13af549ea12534184385f036b4633c
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:54:59.898295Z'
  support: supports
  summary: CHEBI:86345 resolves to magnesium dichloride hexahydrate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:04:45.074853Z'
  support: supports
  summary: CHEBI:86368 resolves to manganese(II) chloride tetrahydrate and is not
    obsolete. This verifies the asserted generic chemical identity; no source grade,
    salt, hydrate or stereochemistry beyond the record is inferred.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T06:55:04.324083Z'
  support: supports
  summary: CHEBI:8806 resolves to Resazurin and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T08:23:26Z'
  support: supports
  summary: '{"CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier":
    "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type":
    "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id":
    "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588":
    [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588",
    "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label":
    "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term":
    "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86214":
    [{"label": "Co(NO3)2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86214",
    "preferred_term": "Co(NO3)2 x 6 H2O", "ontology_id": "CHEBI:86214", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label":
    "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _normalize_unit
  accessed_at: '2026-10-21T08:23:26Z'
  support: context_only
  summary: Current importer keeps primary formulation rows separate from later stocks
    and recognizes explicit solution_id plus percentage-bearing mL additions. It can
    retain A5 solution_id 4987 with source 1 g and the 5% sulfide addition with 5
    mL, instead of flattening later stock rows. This read-only code comparison is
    not a claim that rerunning an import has repaired these persisted recipes or resolved
    A5 density.
- evidence_id: history
  kind: record_content
  reference: data/merge_yaml/merged/480G_MEDIUM.yaml
  locator: Every timestamp in target and sole normalized owner
  accessed_at: '2026-10-21T08:23:26Z'
  support: supports
  summary: '[{"path": "data/merge_yaml/merged/480G_MEDIUM.yaml", "field": "curation_history[0].timestamp",
    "value": "2026-01-26T17:53:18.150706Z", "timezone_aware": true}, {"path": "data/merge_yaml/merged/480G_MEDIUM.yaml",
    "field": "curation_history[1].timestamp", "value": "2026-03-13T06:19:19.409471Z",
    "timezone_aware": true}, {"path": "data/merge_yaml/merged/480G_MEDIUM.yaml", "field":
    "curation_history[2].timestamp", "value": "2026-03-17T06:30:19.000000Z", "timezone_aware":
    true}, {"path": "data/merge_yaml/merged/480G_MEDIUM.yaml", "field": "curation_history[3].timestamp",
    "value": "2026-03-17T19:45:33.363042+00:00", "timezone_aware": true}, {"path":
    "data/merge_yaml/merged/480G_MEDIUM.yaml", "field": "curation_history[4].timestamp",
    "value": "2026-06-05T07:40:15.831277+00:00", "timezone_aware": true}, {"path":
    "data/merge_yaml/merged/480G_MEDIUM.yaml", "field": "curation_history[5].timestamp",
    "value": "2026-06-10T07:46:42.559880+00:00", "timezone_aware": true}, {"path":
    "data/merge_yaml/merged/480G_MEDIUM.yaml", "field": "curation_history[6].timestamp",
    "value": "2026-08-06T03:04:34.119062+00:00", "timezone_aware": true}, {"path":
    "data/normalized_yaml/bacterial/480g_medium.yaml", "field": "curation_history[0].timestamp",
    "value": "2026-01-26T17:53:18.150706Z", "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/480g_medium.yaml",
    "field": "curation_history[1].timestamp", "value": "2026-03-13T06:19:19.409471Z",
    "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/480g_medium.yaml",
    "field": "curation_history[2].timestamp", "value": "2026-03-17T06:30:19.000000Z",
    "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/480g_medium.yaml",
    "field": "curation_history[3].timestamp", "value": "2026-03-17T19:45:33.363042+00:00",
    "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/480g_medium.yaml",
    "field": "curation_history[4].timestamp", "value": "2026-06-05T07:40:15.831277+00:00",
    "timezone_aware": true}, {"path": "data/normalized_yaml/bacterial/480g_medium.yaml",
    "field": "curation_history[5].timestamp", "value": "2026-06-10T07:46:42.559880+00:00",
    "timezone_aware": true}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003312
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '14 primary CHEBI identities resolve with matching labels; 14 of 14 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:003312
  evidence_ids:
  - record
  - mim
  - chebi26710
  - chebi31206
  - chebi31440
  - chebi32312
  - chebi32588
  - chebi33118
  - chebi63036
  - chebi75213
  - chebi76209
  - chebi86158
  - chebi86214
  - chebi86345
  - chebi86368
  - chebi8806
  details: 16 direct ingredient instances; CHEBI-primary instance linkage 14/16 (87.50%),
    verified secondary coverage 14/16 (87.50%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Exact 480G medium and normalized owner
  outcome: supported
  summary: Stable CM003312, singleton merge-event source, maintained owner, official
    JCM964 and provider J964 all identify 480G medium. No similarly named medium or
    neighboring source accession is substituted.
  target_ids:
  - CultureMech:003312
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
- assessment_id: amounts
  area: quantity
  topic: Every direct amount and nested stock
  outcome: concern
  summary: 'All 16 direct rows are traced: nine agree with provider-normalized source
    masses; sulfide misstates an mL stock dose as g/L; six A5 stock rows are flattened
    into final-medium concentrations. The primary and provider both explicitly say
    A5 solution 1 g; unknown density blocks a volume dilution.'
  target_ids:
  - CultureMech:003312
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  details: '[{"field": "ingredients[0].concentration", "material": "NaCl", "local":
    {"value": "0.497512", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator":
    "$.data.solutions[0].recipe[0]", "source_row": {"recipe_order": 1, "compound":
    "NaCl", "compound_id": 43, "amount": 0.5, "unit": "g", "g_l": 0.497512, "mmol_l":
    8.51322, "optional": 0}, "decision": "verified as provider-normalized mass; evidence_only
    for exact primary final-volume claim", "calculation": "0.5g /1.005L = 0.4975124378109452736318407960g/L;
    provider nominal-volume normalization, subject to primary final-volume limitation."},
    {"field": "ingredients[1].concentration", "material": "NH4Cl", "local": {"value":
    "0.328358", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator":
    "$.data.solutions[0].recipe[1]", "source_row": {"recipe_order": 2, "compound":
    "NH4Cl", "compound_id": 42, "amount": 0.33, "unit": "g", "g_l": 0.328358, "mmol_l":
    6.13868, "optional": 0}, "decision": "verified as provider-normalized mass; evidence_only
    for exact primary final-volume claim", "calculation": "0.33g /1.005L = 0.3283582089552238805970149254g/L;
    provider nominal-volume normalization, subject to primary final-volume limitation."},
    {"field": "ingredients[2].concentration", "material": "CaCl2 x 2 H2O", "local":
    {"value": "0.149254", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator":
    "$.data.solutions[0].recipe[2]", "source_row": {"recipe_order": 3, "compound":
    "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.15, "unit": "g", "g_l": 0.149254,
    "mmol_l": 1.01523, "optional": 0}, "decision": "verified as provider-normalized
    mass; evidence_only for exact primary final-volume claim", "calculation": "0.15g
    /1.005L = 0.1492537313432835820895522388g/L; provider nominal-volume normalization,
    subject to primary final-volume limitation."}, {"field": "ingredients[3].concentration",
    "material": "MgCl2 x 6 H2O", "local": {"value": "0.348259", "unit": "G_PER_L"},
    "source_solution_id": 4986, "source_locator": "$.data.solutions[0].recipe[3]",
    "source_row": {"recipe_order": 4, "compound": "MgCl2 x 6 H2O", "compound_id":
    79, "amount": 0.35, "unit": "g", "g_l": 0.348259, "mmol_l": 1.713, "optional":
    0}, "decision": "verified as provider-normalized mass; evidence_only for exact
    primary final-volume claim", "calculation": "0.35g /1.005L = 0.3482587064676616915422885572g/L;
    provider nominal-volume normalization, subject to primary final-volume limitation."},
    {"field": "ingredients[4].concentration", "material": "KCl", "local": {"value":
    "0.298507", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator":
    "$.data.solutions[0].recipe[4]", "source_row": {"recipe_order": 5, "compound":
    "KCl", "compound_id": 61, "amount": 0.3, "unit": "g", "g_l": 0.298507, "mmol_l":
    4.00412, "optional": 0}, "decision": "verified as provider-normalized mass; evidence_only
    for exact primary final-volume claim", "calculation": "0.3g /1.005L = 0.2985074626865671641791044776g/L;
    provider nominal-volume normalization, subject to primary final-volume limitation."},
    {"field": "ingredients[5].concentration", "material": "KH2PO4", "local": {"value":
    "0.298507", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator":
    "$.data.solutions[0].recipe[5]", "source_row": {"recipe_order": 6, "compound":
    "KH2PO4", "compound_id": 11, "amount": 0.3, "unit": "g", "g_l": 0.298507, "mmol_l":
    2.19352, "optional": 0}, "decision": "verified as provider-normalized mass; evidence_only
    for exact primary final-volume claim", "calculation": "0.3g /1.005L = 0.2985074626865671641791044776g/L;
    provider nominal-volume normalization, subject to primary final-volume limitation."},
    {"field": "ingredients[6].concentration", "material": "Casitone", "local": {"value":
    "0.995025", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator":
    "$.data.solutions[0].recipe[6]", "source_row": {"recipe_order": 7, "compound":
    "Casitone", "compound_id": 84, "attribute": "BD-Difco", "amount": 1, "unit": "g",
    "g_l": 0.995025, "optional": 0}, "decision": "verified as provider-normalized
    mass; evidence_only for exact primary final-volume claim", "calculation": "1g
    /1.005L = 0.9950248756218905472636815920g/L; provider nominal-volume normalization,
    subject to primary final-volume limitation."}, {"field": "ingredients[7].concentration",
    "material": "Yeast extract", "local": {"value": "0.497512", "unit": "G_PER_L"},
    "source_solution_id": 4986, "source_locator": "$.data.solutions[0].recipe[7]",
    "source_row": {"recipe_order": 8, "compound": "Yeast extract", "compound_id":
    16, "amount": 0.5, "unit": "g", "g_l": 0.497512, "optional": 0}, "decision": "verified
    as provider-normalized mass; evidence_only for exact primary final-volume claim",
    "calculation": "0.5g /1.005L = 0.4975124378109452736318407960g/L; provider nominal-volume
    normalization, subject to primary final-volume limitation."}, {"field": "ingredients[8].concentration",
    "material": "Resazurin", "local": {"value": "0.000995025", "unit": "G_PER_L"},
    "source_solution_id": 4986, "source_locator": "$.data.solutions[0].recipe[9]",
    "source_row": {"recipe_order": 10, "compound": "Resazurin", "compound_id": 25,
    "amount": 1, "unit": "mg", "g_l": 0.000995025, "mmol_l": 0.00434148, "optional":
    0}, "decision": "verified as provider-normalized mass; evidence_only for exact
    primary final-volume claim", "calculation": "0.001g /1.005L = 0.0009950248756218905472636815920g/L;
    provider nominal-volume normalization, subject to primary final-volume limitation."},
    {"field": "ingredients[9].concentration", "material": "Na2S x 9 H2O", "local":
    {"value": "5", "unit": "G_PER_L"}, "source_solution_id": 4986, "source_locator":
    "$.data.solutions[0].recipe[11]", "source_row": {"recipe_order": 12, "compound":
    "Na2S x 9 H2O", "compound_id": 54, "attribute": "5%", "amount": 5, "unit": "ml",
    "optional": 0}, "decision": "correct: source5mL of5% stock after cooling, not5g/L
    neat sulfide; percent basis unresolved", "calculation": null}, {"field": "ingredients[10].concentration",
    "material": "Co(NO3)2 x 6 H2O", "local": {"value": "0.00494", "unit": "G_PER_L"},
    "source_solution_id": 4987, "source_locator": "$.data.solutions[1].recipe[0]",
    "source_row": {"recipe_order": 1, "compound": "Co(NO3)2 x 6 H2O", "compound_id":
    541, "amount": 4.94, "unit": "mg", "g_l": 0.00494, "mmol_l": 0.0169739, "optional":
    0}, "decision": "correct stock-stage: source A5 stock concentration per1L; final-medium
    contribution not_quantified because stock addition is1g and density/mass fraction
    is unknown", "calculation": null}, {"field": "ingredients[11].concentration",
    "material": "CuSO4 x 5 H2O", "local": {"value": "0.0079", "unit": "G_PER_L"},
    "source_solution_id": 4987, "source_locator": "$.data.solutions[1].recipe[1]",
    "source_row": {"recipe_order": 2, "compound": "CuSO4 x 5 H2O", "compound_id":
    121, "amount": 7.9, "unit": "mg", "g_l": 0.0079, "mmol_l": 0.0316397, "optional":
    0}, "decision": "correct stock-stage: source A5 stock concentration per1L; final-medium
    contribution not_quantified because stock addition is1g and density/mass fraction
    is unknown", "calculation": null}, {"field": "ingredients[12].concentration",
    "material": "H3BO3", "local": {"value": "0.286", "unit": "G_PER_L"}, "source_solution_id":
    4987, "source_locator": "$.data.solutions[1].recipe[2]", "source_row": {"recipe_order":
    3, "compound": "H3BO3", "compound_id": 37, "amount": 0.286, "unit": "g", "g_l":
    0.286, "mmol_l": 4.62484, "optional": 0}, "decision": "correct stock-stage: source
    A5 stock concentration per1L; final-medium contribution not_quantified because
    stock addition is1g and density/mass fraction is unknown", "calculation": null},
    {"field": "ingredients[13].concentration", "material": "MnCl2 x 4 H2O", "local":
    {"value": "0.181", "unit": "G_PER_L"}, "source_solution_id": 4987, "source_locator":
    "$.data.solutions[1].recipe[3]", "source_row": {"recipe_order": 4, "compound":
    "MnCl2 x 4 H2O", "compound_id": 36, "amount": 0.181, "unit": "g", "g_l": 0.181,
    "optional": 0}, "decision": "correct stock-stage: source A5 stock concentration
    per1L; final-medium contribution not_quantified because stock addition is1g and
    density/mass fraction is unknown", "calculation": null}, {"field": "ingredients[14].concentration",
    "material": "Na2MoO4 x 2 H2O", "local": {"value": "0.039", "unit": "G_PER_L"},
    "source_solution_id": 4987, "source_locator": "$.data.solutions[1].recipe[4]",
    "source_row": {"recipe_order": 5, "compound": "Na2MoO4 x 2 H2O", "compound_id":
    9, "amount": 39, "unit": "mg", "g_l": 0.039, "mmol_l": 0.16119, "optional": 0},
    "decision": "correct stock-stage: source A5 stock concentration per1L; final-medium
    contribution not_quantified because stock addition is1g and density/mass fraction
    is unknown", "calculation": null}, {"field": "ingredients[15].concentration",
    "material": "ZnSO4 x 7 H2O", "local": {"value": "0.0222", "unit": "G_PER_L"},
    "source_solution_id": 4987, "source_locator": "$.data.solutions[1].recipe[5]",
    "source_row": {"recipe_order": 6, "compound": "ZnSO4 x 7 H2O", "compound_id":
    35, "amount": 22.2, "unit": "mg", "g_l": 0.0222, "mmol_l": 0.077201, "optional":
    0}, "decision": "correct stock-stage: source A5 stock concentration per1L; final-medium
    contribution not_quantified because stock addition is1g and density/mass fraction
    is unknown", "calculation": null}]'
- assessment_id: dose-hierarchy
  area: representation
  topic: A5 and sulfide source additions
  outcome: concern
  summary: A5 stock per 1 L contains cobalt nitrate hexahydrate 4.94 mg, copper sulfate
    pentahydrate 7.9 mg, boric acid 0.286 g, manganese chloride tetrahydrate 0.181
    g, sodium molybdate dihydrate 39 mg and zinc sulfate heptahydrate 22.2 mg. The
    receiving medium adds 1 g of that solution; these six stock amounts are not direct
    final-medium concentrations. Sulfide is a separate 5 mL 5% stock added after cooling.
    Neither dose is represented as a structured solution addition in either local
    layer.
  target_ids:
  - CultureMech:003312
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
- assessment_id: preparation
  area: completeness
  topic: One retained step and source-specific sterilization
  outcome: concern
  summary: The single step correctly preserves N2 autoclaving, post-cooling addition
    and the parenthetical requirement that the added solution be autoclaved and stored
    under N2. It ends with following solution without identifying the 5 mL 5% sulfide
    dose to which that qualifier applies, and does not preserve the A5 stock recipe
    as a separate preparation. The current primary header supplies 121 °C for 15 min
    as the default. The record has no pH; neither exact source supplies one, so no
    pH finding or invented value is added.
  target_ids:
  - CultureMech:003312
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
- assessment_id: ownership
  area: ownership
  topic: Matching local layers and current import behavior
  outcome: concern
  summary: Target and maintained owner have equal ingredients and preparation; the
    scientific defects persist in the normalized input. Current importer has stock-preservation
    logic, but no import/regeneration was run. Correct the owner with exact source
    evidence and preserve upstream unit ambiguity before regenerating.
  target_ids:
  - CultureMech:003312
  evidence_ids:
  - record
  - owner-0
  - importer
- assessment_id: scope
  area: scope
  topic: Composition class, growth, variants and history
  outcome: supported
  summary: Complex/undefined liquid status is consistent with Casitone and yeast extract
    and no agar. Generic microbial-cultivation application does not establish a species/strain
    outcome. There are no target organisms, variants, parent/child links, taxon/assembly
    identifiers or publications to overgeneralize. Source pH and growth temperature
    remain unspecified. Import/canonicalization history is provenance rather than
    scientific approval.
  target_ids:
  - CultureMech:003312
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
- assessment_id: evidence
  area: evidence
  topic: Source citation and concentration evidence placement
  outcome: concern
  summary: The official JCM URL appears in notes and J964 in media_term, but both
    local layers lack structured references and claim-level formulation/stock evidence.
    A repair must retain exact public source, batch basis, source 1 g A5 unit and
    uncertain percentage basis. The deterministic reference recipe reports 0 reference
    checks, not external validation of those notes. All target/owner history timestamps
    were inspected with timezone scope and preserved.
  target_ids:
  - CultureMech:003312
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - validate-references
  - history
findings:
- finding_id: f1
  issue_key: cm003312-sulfide-stock-dose-as-mass
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: A 5 mL addition of 5% sulfide stock is encoded as 5 g/L
  description: ingredients[9] stores sodium sulfide nonahydrate 5 g/L, while official
    JCM964 and the provider specify 5 mL of 5% solution after cooling. The retained
    preparation step loses the actual addition it refers to. The percentage basis
    is not stated, so the remedy is to preserve the stock/dose and resolve its basis
    rather than invent a replacement final mass concentration.
  target_ids:
  - CultureMech:003312
  field_paths:
  - ingredients[9].concentration
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/480g_medium.yaml
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
  issue_key: cm003312-a5-stock-flattening
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Six A5 stock concentrations are misrepresented as final-medium values
  description: The last six direct ingredients equal the A5 stock recipe per 1 L.
    Both sources instead add 1 g of A5 solution to the receiving medium. Omitting
    that stock/dose relationship makes these final concentration assertions unsupported;
    replacing 1 g with 1 mL would be an unverified source correction.
  target_ids:
  - CultureMech:003312
  field_paths:
  - ingredients[10].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  - ingredients[13].concentration
  - ingredients[14].concentration
  - ingredients[15].concentration
  - solutions
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - importer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/480g_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: cm003312-formulation-evidence-placement
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source quantities and stock-stage limits lack structured evidence
  description: The official URL exists in notes, but neither layer has structured
    references or claim-level formulation/stock evidence. In this record the missing
    stage-specific evidence obscures the provider 1005 mL normalization, source A5
    mass dose and percent-basis uncertainty.
  target_ids:
  - CultureMech:003312
  field_paths:
  - references
  - evidence
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - jcm
  - provider
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/480g_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: P4 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Represent the source 5 mL 5% sulfide stock and its post-cooling, separately
    autoclaved N2 storage context; preserve the primary 121 °C 15 min default where
    applicable and resolve percentage basis before mass conversion.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003312
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/480g_medium.yaml
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
  description: Restore A5 as the source-defined stock with its six constituent amounts
    per 1 L and literal 1 g receiving dose. Leave final trace contributions unresolved
    until density/mass fraction or a corrected authoritative source is verified; do
    not double-count expanded constituents.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003312
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/480g_medium.yaml
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
  description: Add the exact JCM and provider versions as structured references and
    narrow amount/stock evidence with original units, locators and explicit conversion
    limits; retain notes provenance rather than replace it with an unsupported DOI.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003312
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/480g_medium.yaml
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
- JCM explicitly lists A5 solution 1.0 g. No stock density, mass fraction or correction
  to 1 mL was verified; the final contribution of each A5 constituent remains unquantified.
  The review preserves the source’s unit rather than silently repairing it.
- JCM says 5% sodium sulfide nonahydrate solution without explicitly naming w/v, w/w
  or v/v basis. The supported addition is 5 mL after cooling; no fixed final sulfide
  mass concentration is asserted from the percentage alone.
- The primary recipe uses 1 L distilled water followed by a 5 mL stock addition; MediaDive
  declares 1005 mL. Its g/L values are identifiable provider normalizations, not independent
  proof of measured final volume or a primary make-to-volume instruction.
- A bounded official static-PDF candidate returned 404. Exact live official JCM964
  HTML and provider API were successfully retrieved; no unavailable PDF text is treated
  as evidence.
- No target organism, strain, taxonomy identifier, assembly, DOI/PMID or literature-growth
  claim is asserted. The review does not infer such claims from the medium title or
  add generic cultivation conditions.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-010
- generated-medium
```
