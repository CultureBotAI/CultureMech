# Scientific review: CHM

- Review: 20261028T085607Z-culturemech-000060-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T08:34:00.836116Z
- Finished UTC: 2026-10-28T08:56:07.861406Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

CHM has source-supported nominal solutes but missing source preparation, unsupported algae defaults and an unrelated KG identifier. Existing owner source repair is lost from generated output. The unselected bacterial namesake remains comparison context only.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch061 index 07
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000060 | data/merge_yaml/merged/CHM.yaml | generated | chm |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:000060 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:000060 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:000060 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:000060 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Stable identity and namesake resolution

identity: concern. Targets: CultureMech:000060.

The selected stable ID resolves to the algae CHM owner; the bacterial namesake has another ID. C78 is a confirmed unrelated provider identity; CCAP source and C23 identify CHM.

### Once-only native diagnostics

schema: supported. Targets: CultureMech:000060.

All four canonical checks pass; references performs zero checks. This establishes encoded shape/term diagnostics only.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:000060.

7 current concentration fields are covered by 8 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b061-quantity-inventory-v1","target":"data/merge_yaml/merged/CHM.yaml","quantity_field_count":7,"decisions":[{"quantity_id":"q1","label":"Sodium acetate trihydrate","local_fields":[{"path":"data/merge_yaml/merged/CHM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/algae/chm.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chm.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Existing nominal 1 g/L is supported by the primary table explicitly headed Medium per litre and the exact C23 provider g_l. No attached claim exists, so this is not verified. The instruction adds constituents to one litre of solvent; no measured final-volume claim is invented.","source_stage":"CCAP stated per-litre recipe; C23 declared normalization","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt lines 11-13","quote":"Medium                                                                   per litre\n\n           Sodium acetate trihydrate                                     1.0 g","quote_basis":"derivative text"},{"evidence_id":"apiC23","reference":"https://mediadive.dsmz.de/rest/medium/C23","raw_path":"REVIEW_WORK/batch061/source07-09/apiC23.raw","raw_sha256":"c7b83dc0172b62a6b3c48b5d6a6d01ea942e3d8369c3437b0344ba239c017823","text_sha256":"c7b83dc0172b62a6b3c48b5d6a6d01ea942e3d8369c3437b0344ba239c017823","accessed_at":"2026-10-28T08:34:07.947738Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Sodium acetate x 3 H2O\",\n                        \"compound_id\": 1817,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Lab-Lemco powder","local_fields":[{"path":"data/merge_yaml/merged/CHM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/algae/chm.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chm.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Existing nominal 1 g/L is supported by the primary table explicitly headed Medium per litre and the exact C23 provider g_l. No attached claim exists, so this is not verified. The instruction adds constituents to one litre of solvent; no measured final-volume claim is invented.","source_stage":"CCAP stated per-litre recipe; C23 declared normalization","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt lines 11-14","quote":"Medium                                                                   per litre\n\n           Sodium acetate trihydrate                                     1.0 g\n           Lab-Lemco powder                                              1.0 g","quote_basis":"derivative text"},{"evidence_id":"apiC23","reference":"https://mediadive.dsmz.de/rest/medium/C23","raw_path":"REVIEW_WORK/batch061/source07-09/apiC23.raw","raw_sha256":"c7b83dc0172b62a6b3c48b5d6a6d01ea942e3d8369c3437b0344ba239c017823","text_sha256":"c7b83dc0172b62a6b3c48b5d6a6d01ea942e3d8369c3437b0344ba239c017823","accessed_at":"2026-10-28T08:34:07.947738Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Lab Lemco powder\",\n                        \"compound_id\": 2136,\n                        \"attribute\": \"Oxoid L29\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"Input deionised water","local_fields":[{"path":"data/normalized_yaml/bacterial/chm.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1000","unit":"ML_PER_L"}}],"decision":"correct","rationale":"Comparison owner encodes input solvent as ML_PER_L. Primary says add to one litre of water, not make up to a final litre; represent the input volume and its preparation role. The selected target/owner omit it.","source_stage":"Input solvent, not final-medium fraction","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt lines 17-17","quote":"Add the above constituents to 1 litre of deionised water. Autoclave at 15 psi for 15 minutes.","quote_basis":"derivative text"},{"evidence_id":"apiC23","reference":"https://mediadive.dsmz.de/rest/medium/C23","raw_path":"REVIEW_WORK/batch061/source07-09/apiC23.raw","raw_sha256":"c7b83dc0172b62a6b3c48b5d6a6d01ea942e3d8369c3437b0344ba239c017823","text_sha256":"c7b83dc0172b62a6b3c48b5d6a6d01ea942e3d8369c3437b0344ba239c017823","accessed_at":"2026-10-28T08:34:07.947738Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Deionized water\",\n                        \"compound_id\": 418,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"Autoclave pressure/time","local_fields":[{"path":"data/normalized_yaml/bacterial/chm.yaml","field_path":"preparation_steps[1].description","stored":"Autoclave at 15 psi for 15 min."}],"decision":"evidence_only","rationale":"The comparison owner already preserves the literal pressure and duration. These controls are absent from selected owner/target; no temperature is inferred from pressure.","source_stage":"Primary preparation","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt lines 17-17","quote":"Add the above constituents to 1 litre of deionised water. Autoclave at 15 psi for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q5","label":"Unsubstantiated light_intensity","local_fields":[{"path":"data/merge_yaml/merged/CHM.yaml","field_path":"light_intensity","stored":"Varies by species; typically 50-100 µmol photons m⁻² s⁻¹"},{"path":"data/normalized_yaml/algae/chm.yaml","field_path":"light_intensity","stored":"Varies by species; typically 50-100 µmol photons m⁻² s⁻¹"}],"decision":"unsupported","rationale":"These are current importer defaults, not instructions in the complete exact CHM source. Retain no asserted cultivation ranges from generic algae boilerplate.","source_stage":"Unsupported record-level defaults","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt lines 6-17","quote":"CHM (Chilomonas Medium)\n                                         Freshwater Protozoa\n\n\n\nMedium                                                                   per litre\n\n           Sodium acetate trihydrate                                     1.0 g\n           Lab-Lemco powder                                              1.0 g\n\n\nAdd the above constituents to 1 litre of deionised water. Autoclave at 15 psi for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q6","label":"Unsubstantiated light_cycle","local_fields":[{"path":"data/merge_yaml/merged/CHM.yaml","field_path":"light_cycle","stored":"Varies by species; commonly 12:12 or 16:8 light:dark"},{"path":"data/normalized_yaml/algae/chm.yaml","field_path":"light_cycle","stored":"Varies by species; commonly 12:12 or 16:8 light:dark"}],"decision":"unsupported","rationale":"These are current importer defaults, not instructions in the complete exact CHM source. Retain no asserted cultivation ranges from generic algae boilerplate.","source_stage":"Unsupported record-level defaults","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt lines 6-17","quote":"CHM (Chilomonas Medium)\n                                         Freshwater Protozoa\n\n\n\nMedium                                                                   per litre\n\n           Sodium acetate trihydrate                                     1.0 g\n           Lab-Lemco powder                                              1.0 g\n\n\nAdd the above constituents to 1 litre of deionised water. Autoclave at 15 psi for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q7","label":"Unsubstantiated temperature_range","local_fields":[{"path":"data/merge_yaml/merged/CHM.yaml","field_path":"temperature_range","stored":"15-30°C depending on species"},{"path":"data/normalized_yaml/algae/chm.yaml","field_path":"temperature_range","stored":"15-30°C depending on species"}],"decision":"unsupported","rationale":"These are current importer defaults, not instructions in the complete exact CHM source. Retain no asserted cultivation ranges from generic algae boilerplate.","source_stage":"Unsupported record-level defaults","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt lines 6-17","quote":"CHM (Chilomonas Medium)\n                                         Freshwater Protozoa\n\n\n\nMedium                                                                   per litre\n\n           Sodium acetate trihydrate                                     1.0 g\n           Lab-Lemco powder                                              1.0 g\n\n\nAdd the above constituents to 1 litre of deionised water. Autoclave at 15 psi for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q8","label":"Primary revision/date","local_fields":[],"decision":"evidence_only","rationale":"Fresh directly captured PDF is revision002, approved29May2026. No claim that this is the version used in past curation; source retrieval timestamps are preserved.","source_stage":"Source version metadata","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt lines 1-2","quote":"QF 09                                         Revision: 002\n                                     Media Preparation Recipe Template                   Approved: 29 MAY 26","quote_basis":"derivative text"},{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt lines 24-24","quote":"Reviewed: 29th May 2026","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/CHM.yaml":null,"data/normalized_yaml/algae/chm.yaml":null,"data/normalized_yaml/bacterial/chm.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:000060.

Selected sodium acetate trihydrate CHEBI32138 is chemically and canonically supported; Lab-Lemco is an unresolved mixture, not a missing single-compound identity by definition. The scoped comparison has confirmed anhydrous-versus-trihydrate mismatch despite correct canonical labels. Exact current MIM rows and preferred-term lookups remain snapshot-only. Selected secondary-link presence is0/4 ingredient instances; validity among existing selected secondary slots has an empty population, not a percentage.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:000060.

All five inspected historical reports were read completely: three selected target/algae-owner reports and two bacterial-comparison reports. Fresh C23 raw bytes exactly match the October7 report digest and its three literal recipe objects plus step; this authenticates content only, not an original retrieval event. Earlier unresolved source identity is now narrowed by the exact source link. The September suggestion to encode solvent per litre is not adopted. Existing owner source repair is credited and current writers are not claimed as historical execution proof.

### Unselected namesake comparison boundary

grounding: not_applicable. Targets: CultureMech:000060.

The separately scoped CultureMech000331 namesake explicitly supplies sodium acetate trihydrate but uses anhydrous CHEBI32954 in both primary and secondary slots. OLS formula/InChI and primary source distinguish it from CHEBI32138, already correct in selected000060. Reconcile the named comparison owner separately; do not duplicate a finding against the correct selected slot. This context-only observation is not an open finding against selected CultureMech000060 and is not an authorized repair target in this review.

## Findings

### f1: Selected owner omits source water and preparation

major / open / confirmed; issue key: culturemech-000060-missing-source-preparation.

The two selected records retain the solutes but omit the explicitly stated deionised-water input and autoclave step. Preserve input volume as such, without inventing a final-volume denominator or a temperature derived from pressure. The separately identified bacterial namesake already has preparation and is comparison evidence, not this target's generation owner.

### f2: Generic algae and cultivation defaults exceed the CHM source

major / open / confirmed; issue key: culturemech-000060-unsupported-algae-defaults.

The source identifies CHM as Chilomonas Medium for Freshwater Protozoa. The current algae description, applications, light ranges/cycles and temperature range are generic import defaults unsupported by this exact source. Reconcile the biological scope and remove unsupported defaults without inferring a strain-growth claim or choosing an unverified taxonomic category.

### f3: Asserted C78 resolves to a different medium

major / open / confirmed; issue key: culturemech-000060-wrong-kg-identity.

Fresh MediaDive C78 identifies PM and links MR_PM.pdf; it is not CHM. C23 independently identifies CHM and links the exact CCAP source, but correcting the KG association still requires scoped identity provenance, not identifier-set similarity alone. Do not import C78 formulation or treat C23 as an additional generation owner.

### f4: Generated output omits existing owner source provenance

minor / open / confirmed; issue key: culturemech-000060-generated-source-staleness.

The maintained algae owner already carries structured CCAP sources and its September repair event, while generated CHM omits them. Credit that repair. Current singleton merge copies the owner, so this is generated staleness rather than evidence of a current merge implementation that necessarily drops sources. Preserve earlier history and append future events.

## Recommended Actions And Acceptance Checks

### a1

The two selected records retain the solutes but omit the explicitly stated deionised-water input and autoclave step. Preserve input volume as such, without inventing a final-volume denominator or a temperature derived from pressure. The separately identified bacterial namesake already has preparation and is comparison evidence, not this target's generation owner.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The source identifies CHM as Chilomonas Medium for Freshwater Protozoa. The current algae description, applications, light ranges/cycles and temperature range are generic import defaults unsupported by this exact source. Reconcile the biological scope and remove unsupported defaults without inferring a strain-growth claim or choosing an unverified taxonomic category.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Fresh MediaDive C78 identifies PM and links MR_PM.pdf; it is not CHM. C23 independently identifies CHM and links the exact CCAP source, but correcting the KG association still requires scoped identity provenance, not identifier-set similarity alone. Do not import C78 formulation or treat C23 as an additional generation owner.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The maintained algae owner already carries structured CCAP sources and its September repair event, while generated CHM omits them. Credit that repair. Current singleton merge copies the owner, so this is generated staleness rather than evidence of a current merge implementation that necessarily drops sources. Preserve earlier history and append future events.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ccapCHM | https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf; REVIEW_WORK/batch061/source07-09/ccapCHM.json; exact original raw/text/hash/time metadata | context_only | Exact CHM primary recipe, organism-category and instructions. No strain growth inference. |
| apiC23 | https://mediadive.dsmz.de/rest/medium/C23; REVIEW_WORK/batch061/source07-09/apiC23.json; exact original raw/text/hash/time metadata | context_only | Exact namesake CHM provider identity comparison; not an additional generation owner. |
| apiC78 | https://mediadive.dsmz.de/rest/medium/C78; REVIEW_WORK/batch061/source07-09/apiC78.json; exact original raw/text/hash/time metadata | context_only | Identity-only comparison for asserted KG C78; no formulation transfer. |
| chebi32138 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32138; REVIEW_WORK/batch061/source07-09/chebi32138.json; exact original raw/text/hash/time metadata | context_only | Exact supplied-form and canonical identity for ordinary CHM source review. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954; REVIEW_WORK/batch061/source07-09/chebi32954.json; exact original raw/text/hash/time metadata | context_only | Exact supplied-form and canonical identity for ordinary CHM source review. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch061/source07-09/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Exact supplied-form and canonical identity for ordinary CHM source review. |
| target | data/merge_yaml/merged/CHM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/algae/chm.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-18 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-19 | reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/chm.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-20 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/chm.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-22 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chm.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/yaml_record_review/20260922T072255Z-CHM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| comparison | data/normalized_yaml/bacterial/chm.yaml; Complete comparison file | context_only | Separate CultureMech000331 namesake from the same CCAP source; not the generation owner of selected000060. Its existing fields are compared explicitly and not silently transferred. |
| writer-ccap | src/culturemech/import/ccap_importer.py; convert_recipe, ingredient/preparation extraction | context_only | Current CCAP importer hardcodes algae category and generic light, temperature and applications. This current behavior explains a risk, not proof of the historical run. |
| writer-ccap-sources | scripts/repair_ccap_sources_score10.py; repair_record and source/history guards | context_only | Current guarded repair adds structured CCAP source provenance; the exact maintained owner already has it. Existing matching repair events can be replaced by this implementation, so future curation must separately preserve append-only history. |
| writer-kg | src/culturemech/match/kg_media_matcher.py; extract_recipe_ingredients, find_exact_match, find_matches | context_only | Current matcher compares CHEBI/FOODON identifier sets, ignoring concentrations and source preparation. This does not authenticate medium identity, mixture coverage or growth. |
| writer-simple | scripts/repair_official_simple_score20.py; CHM target block, _ingredient, repair_record | context_only | Exact CHM target is bacterial/chm.yaml (CultureMech000331/C23), not selected algae/chm.yaml. Its existing trihydrate descriptor is paired with anhydrous CHEBI32954; preserve source and owner boundaries. |
| quantities | REVIEW_WORK/batch061/record07/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch061/record07/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch061/record07/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch061/record07/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch061/record07/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch061/record07/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch061/record07/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch061/record07/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch061/record07/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch061/record07/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch061/record07/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- The scope includes all four selected concentration fields and three fields of the explicitly separate namesake comparison. Neither that comparison nor its historical API review becomes generation ownership.
- No current or archived KG graph was used to reconstruct the historical C78 assignment. Current API identity contradicts the local assertion; the historical graph mapping itself remains unrecovered.
- The fresh direct PDF revision002 differs from an older web-tool cached revision001. Only the directly captured current raw/text/visual bytes support this review.
- No exact original October7 raw event archive was recovered; fresh C23 equal bytes only authenticate report content.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T085607Z-culturemech-000060-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: CHM'
started_at: '2026-10-28T08:34:00.836116Z'
finished_at: '2026-10-28T08:56:07.861406Z'
reviewer:
  identity: Codex tsb_source_check
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Read-only independent review of maintained source records, fresh
    sources and original diagnostics.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: CHM has source-supported nominal solutes but missing source preparation,
  unsupported algae defaults and an unrelated KG identifier. Existing owner source
  repair is lost from generated output. The unselected bacterial namesake remains
  comparison context only.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
    role: context
  - path: .claude/skills/review-ingredient-concentrations/SKILL.md
    sha256: a67993ef11cf374ac579c53252bc603f9894ebd69cad711b11f293714c76621e
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
    sha256: c0ef0808662f57dc2f57ce9b405485830503653aceee1451c9e1dae42f9e7021
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/CHM.yaml
    sha256: 3c92655a6f36f064e6533888a77fc5ce1d39b941d9864d16cbf00e7df8047ab0
    role: target
  - path: data/normalized_yaml/algae/chm.yaml
    sha256: 0256f685790c514727001a5291742bf7be02bdfc3289fe52accacb094570dffc
    role: context
  - path: data/normalized_yaml/bacterial/chm.yaml
    sha256: 27a6a1e81da7b9514136a240d06c2855886b6e7f8406d220e9e6d2591a28ea76
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
    sha256: 8cb892e67e1d94bc93c77f3a03d8d4ced32d8d31aa8e5b0346853cbc05077d6f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
    sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/chm.yaml.md
    sha256: e87106ffa386d908d078f88378dab9d3bc3c98095a80a22112e4560935f07127
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHM.md
    sha256: 2bb9560190fe2754aac225888dd8e9a940b473d99143fe6ccea80d4559be5bd6
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/chm.md
    sha256: 37f26d113c15640821e0efe9589dd8fcad48129916ff319e9e8ef8608b51de7f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chm.md
    sha256: 929fb73d3bef5a499749d591433a32aa3a468a5bc3fd0466250b22371f731176
    role: context
  - path: reports/yaml_record_review/20260922T072255Z-CHM.md
    sha256: 6bb5e944d8203fc114d93d1dcbefc8ee01bfbe8395c647b9e533e65da36b4d0e
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/assign_culturemech_ids.py
    sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/enrich_with_chebi.py
    sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
    role: context
  - path: scripts/enrich_with_kg_microbe_matches.py
    sha256: 61351f99ef2cb0cef03e74ad92d21dcf3b38df77a06602bdac814974e7728eeb
    role: context
  - path: scripts/enrich_with_mediaingredientmech.py
    sha256: 6357c9d621c3d6e32b28b2982afedfaed384830cea1602a775b0a5f0852c015e
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/promote_komodo_volume_candidates.py
    sha256: 2423b7e2e04011b31d21eac939714a2db4380f033a69094325dc567e44929cd2
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/remove_invalid_chebi_ids.py
    sha256: a6c2f7577812081230fd5fe008182c09eace4ef7818857f8026ec8d5e0b760e0
    role: context
  - path: scripts/repair_ccap_instruction_rows.py
    sha256: eb1a4c8c46eb45dcdde6a5d2f0f6833792dd0802c45603eefa1b63a3ff96fca5
    role: context
  - path: scripts/repair_ccap_sources_score10.py
    sha256: f518688ae99e154f490af337dab30b9038657a814db72861e0b53658a2541ae6
    role: context
  - path: scripts/repair_mediadive_jcm_structure.py
    sha256: 5bff4c2d1900051bdea1b8e0f655049147c85cc9c61da4c348a6d60a8d0fd509
    role: context
  - path: scripts/repair_official_simple_score20.py
    sha256: 689ef1b008090eba5ce1ef4083ef25245565ba2f3ff8b9a34372c049590e75f1
    role: context
  - path: scripts/repair_togo_commercial_score20.py
    sha256: d5e34df82098bf7558fcdd103d24d00218513488ea860952881c73240596c822
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/import/ccap_importer.py
    sha256: c579c1d8fb62b96e739e5ee5c963453753ebca0bbf50996fb0f0d6eedd75c9ac
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
    role: context
  - path: src/culturemech/match/kg_media_matcher.py
    sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
    role: context
  - path: src/culturemech/merge/formulation.py
    sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
    role: context
  - path: src/culturemech/merge/matcher.py
    sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
    role: context
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: Whole exact target/owner with explicit scoped dependencies, current
    sources and historical claims.
  selection: Authoritative batch061 index 07
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000060
targets:
- target_id: CultureMech:000060
  path: data/merge_yaml/merged/CHM.yaml
  label: chm
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/chm.yaml
    role: maintained source
  ownership_note: Exact declared maintained contributors resolved against stable identity;
    stocks and other source variants remain scoped comparisons.
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:000060
  command: just validate-schema data/merge_yaml/merged/CHM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-schema
- check_id: strict
  name: Canonical strict
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:000060
  command: just validate-strict data/merge_yaml/merged/CHM.yaml --out REVIEW_WORK/batch061/record07/strict.tsv
    --workers 1 --quiet
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-strict
- check_id: terms
  name: Canonical terms
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:000060
  command: just validate-terms data/merge_yaml/merged/CHM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-terms
- check_id: references
  name: Canonical references
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:000060
  command: just validate-references data/merge_yaml/merged/CHM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: ccapCHM
  kind: primary_source
  reference: https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf
  accessed_at: '2026-10-28T08:34:08.750100Z'
  locator: REVIEW_WORK/batch061/source07-09/ccapCHM.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact CHM primary recipe, organism-category and instructions. No strain
    growth inference.
  snapshot_sha256: 5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041
- evidence_id: apiC23
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/C23
  accessed_at: '2026-10-28T08:34:07.947738Z'
  locator: REVIEW_WORK/batch061/source07-09/apiC23.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact namesake CHM provider identity comparison; not an additional generation
    owner.
  snapshot_sha256: c7b83dc0172b62a6b3c48b5d6a6d01ea942e3d8369c3437b0344ba239c017823
- evidence_id: apiC78
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/C78
  accessed_at: '2026-10-28T08:34:07.961053Z'
  locator: REVIEW_WORK/batch061/source07-09/apiC78.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Identity-only comparison for asserted KG C78; no formulation transfer.
  snapshot_sha256: 4b31301fdfddf71fe6ffab40e214d8e1690345d67fea02e55a90eac55c4ea660
- evidence_id: chebi32138
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32138
  accessed_at: '2026-10-28T08:34:08.656227Z'
  locator: REVIEW_WORK/batch061/source07-09/chebi32138.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact supplied-form and canonical identity for ordinary CHM source review.
  snapshot_sha256: a85623bd501ec509db74e3ec861994a6e2b3c99b2542468162f19ec72891787d
- evidence_id: chebi32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954
  accessed_at: '2026-10-28T08:34:08.664428Z'
  locator: REVIEW_WORK/batch061/source07-09/chebi32954.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact supplied-form and canonical identity for ordinary CHM source review.
  snapshot_sha256: 6718762e0aceec57316f70ff5a6264c973f1f2b235e6d5bbe077a9c349394fb8
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T08:34:09.085725Z'
  locator: REVIEW_WORK/batch061/source07-09/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact supplied-form and canonical identity for ordinary CHM source review.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CHM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T08:42:01.977517Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 3c92655a6f36f064e6533888a77fc5ce1d39b941d9864d16cbf00e7df8047ab0
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/algae/chm.yaml
  locator: Complete file
  accessed_at: '2026-10-28T08:42:01.977690Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 0256f685790c514727001a5291742bf7be02bdfc3289fe52accacb094570dffc
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T08:42:01.977722Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T08:42:01.978046Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T08:42:01.978072Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T08:42:01.978095Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T08:42:01.978132Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/chm.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T08:42:01.984086Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: e87106ffa386d908d078f88378dab9d3bc3c98095a80a22112e4560935f07127
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHM.md
  locator: Complete report
  accessed_at: '2026-10-28T08:42:01.984139Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 2bb9560190fe2754aac225888dd8e9a940b473d99143fe6ccea80d4559be5bd6
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/chm.md
  locator: Complete report
  accessed_at: '2026-10-28T08:42:01.984167Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 37f26d113c15640821e0efe9589dd8fcad48129916ff319e9e8ef8608b51de7f
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chm.md
  locator: Complete report
  accessed_at: '2026-10-28T08:42:01.984190Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 929fb73d3bef5a499749d591433a32aa3a468a5bc3fd0466250b22371f731176
- evidence_id: report-23
  kind: prior_review
  reference: reports/yaml_record_review/20260922T072255Z-CHM.md
  locator: Complete report
  accessed_at: '2026-10-28T08:42:01.984212Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 6bb5e944d8203fc114d93d1dcbefc8ee01bfbe8395c647b9e533e65da36b4d0e
- evidence_id: comparison
  kind: record_content
  reference: data/normalized_yaml/bacterial/chm.yaml
  locator: Complete comparison file
  accessed_at: '2026-10-28T08:42:01.985805Z'
  support: context_only
  summary: Separate CultureMech000331 namesake from the same CCAP source; not the
    generation owner of selected000060. Its existing fields are compared explicitly
    and not silently transferred.
  snapshot_sha256: 27a6a1e81da7b9514136a240d06c2855886b6e7f8406d220e9e6d2591a28ea76
- evidence_id: writer-ccap
  kind: record_content
  reference: src/culturemech/import/ccap_importer.py
  locator: convert_recipe, ingredient/preparation extraction
  accessed_at: '2026-10-28T08:42:01.985834Z'
  support: context_only
  summary: Current CCAP importer hardcodes algae category and generic light, temperature
    and applications. This current behavior explains a risk, not proof of the historical
    run.
  snapshot_sha256: c579c1d8fb62b96e739e5ee5c963453753ebca0bbf50996fb0f0d6eedd75c9ac
- evidence_id: writer-ccap-sources
  kind: record_content
  reference: scripts/repair_ccap_sources_score10.py
  locator: repair_record and source/history guards
  accessed_at: '2026-10-28T08:42:01.985862Z'
  support: context_only
  summary: Current guarded repair adds structured CCAP source provenance; the exact
    maintained owner already has it. Existing matching repair events can be replaced
    by this implementation, so future curation must separately preserve append-only
    history.
  snapshot_sha256: f518688ae99e154f490af337dab30b9038657a814db72861e0b53658a2541ae6
- evidence_id: writer-kg
  kind: record_content
  reference: src/culturemech/match/kg_media_matcher.py
  locator: extract_recipe_ingredients, find_exact_match, find_matches
  accessed_at: '2026-10-28T08:42:01.985889Z'
  support: context_only
  summary: Current matcher compares CHEBI/FOODON identifier sets, ignoring concentrations
    and source preparation. This does not authenticate medium identity, mixture coverage
    or growth.
  snapshot_sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
- evidence_id: writer-simple
  kind: record_content
  reference: scripts/repair_official_simple_score20.py
  locator: CHM target block, _ingredient, repair_record
  accessed_at: '2026-10-28T08:42:01.985916Z'
  support: context_only
  summary: Exact CHM target is bacterial/chm.yaml (CultureMech000331/C23), not selected
    algae/chm.yaml. Its existing trihydrate descriptor is paired with anhydrous CHEBI32954;
    preserve source and owner boundaries.
  snapshot_sha256: 689ef1b008090eba5ce1ef4083ef25245565ba2f3ff8b9a34372c049590e75f1
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch061/record07/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T08:42:02.067242Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: ee11d3d45edd4cbdd416ddee54071137cf127730583523bc90f029af7b8f5a73
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch061/record07/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T08:42:02.067282Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 82014e381479061aa63d8f1a6537306d9c8243fcc688d276a01c4ec0536c5067
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch061/record07/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T08:42:02.067344Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 6943034d15d5d9bdcb026621d64e888945b5d66419a3988228724a0d46b16b84
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch061/record07/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T08:42:02.067390Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: a76fee80b203e9928fb6e5725ccc29ce432dc7d3ab5768626bee2f15a2636f23
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch061/record07/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T08:42:02.067430Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: ecc58b9cfa47dd6f3175112e9450306ce6ef0958466b2800ca46ac30746fc823
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch061/record07/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T08:42:02.067468Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 73220577e473c3f0d832ed794764cf133421646dc7b3ba3fb15772c32df1e45a
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch061/record07/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T08:42:02.067501Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch061/record07/schema-result.json
  accessed_at: '2026-10-28T08:34:02.747605Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 453972253a99ee58e8d7fec0a5bc637839fccf8ea756012d104ca05e30b95af2
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch061/record07/strict-result.json
  accessed_at: '2026-10-28T08:34:04.489979Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 8461ceb15f5bc770064a80f3d92e175da3c48e118b3ca4e379b9caa97a803bf5
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch061/record07/terms-result.json
  accessed_at: '2026-10-28T08:34:06.792383Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 1ab36fdfee16f18356fa610155b08f677166a2ab6756595e3afd64a9549ae8ed
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch061/record07/references-result.json
  accessed_at: '2026-10-28T08:34:08.138739Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: a23ffb0fb75656c0754377a2517034cddea90a283782f2ac5348066eca162049
assessments:
- assessment_id: identity
  area: identity
  topic: Stable identity and namesake resolution
  outcome: concern
  summary: The selected stable ID resolves to the algae CHM owner; the bacterial namesake
    has another ID. C78 is a confirmed unrelated provider identity; CCAP source and
    C23 identify CHM.
  target_ids:
  - CultureMech:000060
  evidence_ids:
  - target
  - owner
  - comparison
  - ccapCHM
  - apiC78
  - apiC23
- assessment_id: schema
  area: schema
  topic: Once-only native diagnostics
  outcome: supported
  summary: All four canonical checks pass; references performs zero checks. This establishes
    encoded shape/term diagnostics only.
  target_ids:
  - CultureMech:000060
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 7 current concentration fields are covered by 8 decisions, including unchanged
    support and explicit source-only conditions.
  target_ids:
  - CultureMech:000060
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b061-quantity-inventory-v1","target":"data/merge_yaml/merged/CHM.yaml","quantity_field_count":7,"decisions":[{"quantity_id":"q1","label":"Sodium
    acetate trihydrate","local_fields":[{"path":"data/merge_yaml/merged/CHM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/algae/chm.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chm.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Existing
    nominal 1 g/L is supported by the primary table explicitly headed Medium per litre
    and the exact C23 provider g_l. No attached claim exists, so this is not verified.
    The instruction adds constituents to one litre of solvent; no measured final-volume
    claim is invented.","source_stage":"CCAP stated per-litre recipe; C23 declared
    normalization","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt
    lines 11-13","quote":"Medium                                                                   per
    litre\n\n           Sodium acetate trihydrate                                     1.0
    g","quote_basis":"derivative text"},{"evidence_id":"apiC23","reference":"https://mediadive.dsmz.de/rest/medium/C23","raw_path":"REVIEW_WORK/batch061/source07-09/apiC23.raw","raw_sha256":"c7b83dc0172b62a6b3c48b5d6a6d01ea942e3d8369c3437b0344ba239c017823","text_sha256":"c7b83dc0172b62a6b3c48b5d6a6d01ea942e3d8369c3437b0344ba239c017823","accessed_at":"2026-10-28T08:34:07.947738Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Sodium acetate x 3 H2O\",\n                        \"compound_id\":
    1817,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Lab-Lemco
    powder","local_fields":[{"path":"data/merge_yaml/merged/CHM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/algae/chm.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chm.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1.0","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Existing
    nominal 1 g/L is supported by the primary table explicitly headed Medium per litre
    and the exact C23 provider g_l. No attached claim exists, so this is not verified.
    The instruction adds constituents to one litre of solvent; no measured final-volume
    claim is invented.","source_stage":"CCAP stated per-litre recipe; C23 declared
    normalization","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt
    lines 11-14","quote":"Medium                                                                   per
    litre\n\n           Sodium acetate trihydrate                                     1.0
    g\n           Lab-Lemco powder                                              1.0
    g","quote_basis":"derivative text"},{"evidence_id":"apiC23","reference":"https://mediadive.dsmz.de/rest/medium/C23","raw_path":"REVIEW_WORK/batch061/source07-09/apiC23.raw","raw_sha256":"c7b83dc0172b62a6b3c48b5d6a6d01ea942e3d8369c3437b0344ba239c017823","text_sha256":"c7b83dc0172b62a6b3c48b5d6a6d01ea942e3d8369c3437b0344ba239c017823","accessed_at":"2026-10-28T08:34:07.947738Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Lab Lemco powder\",\n                        \"compound_id\":
    2136,\n                        \"attribute\": \"Oxoid L29\",\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q3","label":"Input deionised water","local_fields":[{"path":"data/normalized_yaml/bacterial/chm.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1000","unit":"ML_PER_L"}}],"decision":"correct","rationale":"Comparison
    owner encodes input solvent as ML_PER_L. Primary says add to one litre of water,
    not make up to a final litre; represent the input volume and its preparation role.
    The selected target/owner omit it.","source_stage":"Input solvent, not final-medium
    fraction","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt
    lines 17-17","quote":"Add the above constituents to 1 litre of deionised water.
    Autoclave at 15 psi for 15 minutes.","quote_basis":"derivative text"},{"evidence_id":"apiC23","reference":"https://mediadive.dsmz.de/rest/medium/C23","raw_path":"REVIEW_WORK/batch061/source07-09/apiC23.raw","raw_sha256":"c7b83dc0172b62a6b3c48b5d6a6d01ea942e3d8369c3437b0344ba239c017823","text_sha256":"c7b83dc0172b62a6b3c48b5d6a6d01ea942e3d8369c3437b0344ba239c017823","accessed_at":"2026-10-28T08:34:07.947738Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Deionized water\",\n                        \"compound_id\":
    418,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"Autoclave pressure/time","local_fields":[{"path":"data/normalized_yaml/bacterial/chm.yaml","field_path":"preparation_steps[1].description","stored":"Autoclave
    at 15 psi for 15 min."}],"decision":"evidence_only","rationale":"The comparison
    owner already preserves the literal pressure and duration. These controls are
    absent from selected owner/target; no temperature is inferred from pressure.","source_stage":"Primary
    preparation","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt
    lines 17-17","quote":"Add the above constituents to 1 litre of deionised water.
    Autoclave at 15 psi for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q5","label":"Unsubstantiated
    light_intensity","local_fields":[{"path":"data/merge_yaml/merged/CHM.yaml","field_path":"light_intensity","stored":"Varies
    by species; typically 50-100 µmol photons m⁻² s⁻¹"},{"path":"data/normalized_yaml/algae/chm.yaml","field_path":"light_intensity","stored":"Varies
    by species; typically 50-100 µmol photons m⁻² s⁻¹"}],"decision":"unsupported","rationale":"These
    are current importer defaults, not instructions in the complete exact CHM source.
    Retain no asserted cultivation ranges from generic algae boilerplate.","source_stage":"Unsupported
    record-level defaults","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt
    lines 6-17","quote":"CHM (Chilomonas Medium)\n                                         Freshwater
    Protozoa\n\n\n\nMedium                                                                   per
    litre\n\n           Sodium acetate trihydrate                                     1.0
    g\n           Lab-Lemco powder                                              1.0
    g\n\n\nAdd the above constituents to 1 litre of deionised water. Autoclave at
    15 psi for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q6","label":"Unsubstantiated
    light_cycle","local_fields":[{"path":"data/merge_yaml/merged/CHM.yaml","field_path":"light_cycle","stored":"Varies
    by species; commonly 12:12 or 16:8 light:dark"},{"path":"data/normalized_yaml/algae/chm.yaml","field_path":"light_cycle","stored":"Varies
    by species; commonly 12:12 or 16:8 light:dark"}],"decision":"unsupported","rationale":"These
    are current importer defaults, not instructions in the complete exact CHM source.
    Retain no asserted cultivation ranges from generic algae boilerplate.","source_stage":"Unsupported
    record-level defaults","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt
    lines 6-17","quote":"CHM (Chilomonas Medium)\n                                         Freshwater
    Protozoa\n\n\n\nMedium                                                                   per
    litre\n\n           Sodium acetate trihydrate                                     1.0
    g\n           Lab-Lemco powder                                              1.0
    g\n\n\nAdd the above constituents to 1 litre of deionised water. Autoclave at
    15 psi for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q7","label":"Unsubstantiated
    temperature_range","local_fields":[{"path":"data/merge_yaml/merged/CHM.yaml","field_path":"temperature_range","stored":"15-30°C
    depending on species"},{"path":"data/normalized_yaml/algae/chm.yaml","field_path":"temperature_range","stored":"15-30°C
    depending on species"}],"decision":"unsupported","rationale":"These are current
    importer defaults, not instructions in the complete exact CHM source. Retain no
    asserted cultivation ranges from generic algae boilerplate.","source_stage":"Unsupported
    record-level defaults","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt
    lines 6-17","quote":"CHM (Chilomonas Medium)\n                                         Freshwater
    Protozoa\n\n\n\nMedium                                                                   per
    litre\n\n           Sodium acetate trihydrate                                     1.0
    g\n           Lab-Lemco powder                                              1.0
    g\n\n\nAdd the above constituents to 1 litre of deionised water. Autoclave at
    15 psi for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q8","label":"Primary
    revision/date","local_fields":[],"decision":"evidence_only","rationale":"Fresh
    directly captured PDF is revision002, approved29May2026. No claim that this is
    the version used in past curation; source retrieval timestamps are preserved.","source_stage":"Source
    version metadata","sources":[{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt
    lines 1-2","quote":"QF 09                                         Revision: 002\n                                     Media
    Preparation Recipe Template                   Approved: 29 MAY 26","quote_basis":"derivative
    text"},{"evidence_id":"ccapCHM","reference":"https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf","raw_path":"REVIEW_WORK/batch061/source07-09/ccapCHM.raw","raw_sha256":"5326758a405cc692c2938b755e6896e729cdd675b410fcd001a6acf4de1a4041","text_sha256":"7eb6963b04ac945c26e757ef25b7b93bc292c95c6b08f441236650d3dab80748","accessed_at":"2026-10-28T08:34:08.750100Z","locator":"ccapCHM.txt
    lines 24-24","quote":"Reviewed: 29th May 2026","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/CHM.yaml":null,"data/normalized_yaml/algae/chm.yaml":null,"data/normalized_yaml/bacterial/chm.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: Selected sodium acetate trihydrate CHEBI32138 is chemically and canonically
    supported; Lab-Lemco is an unresolved mixture, not a missing single-compound identity
    by definition. The scoped comparison has confirmed anhydrous-versus-trihydrate
    mismatch despite correct canonical labels. Exact current MIM rows and preferred-term
    lookups remain snapshot-only. Selected secondary-link presence is0/4 ingredient
    instances; validity among existing selected secondary slots has an empty population,
    not a percentage.
  target_ids:
  - CultureMech:000060
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: 'All five inspected historical reports were read completely: three selected
    target/algae-owner reports and two bacterial-comparison reports. Fresh C23 raw
    bytes exactly match the October7 report digest and its three literal recipe objects
    plus step; this authenticates content only, not an original retrieval event. Earlier
    unresolved source identity is now narrowed by the exact source link. The September
    suggestion to encode solvent per litre is not adopted. Existing owner source repair
    is credited and current writers are not claimed as historical execution proof.'
  target_ids:
  - CultureMech:000060
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
- assessment_id: comparison-form
  area: grounding
  topic: Unselected namesake comparison boundary
  outcome: not_applicable
  summary: The separately scoped CultureMech000331 namesake explicitly supplies sodium
    acetate trihydrate but uses anhydrous CHEBI32954 in both primary and secondary
    slots. OLS formula/InChI and primary source distinguish it from CHEBI32138, already
    correct in selected000060. Reconcile the named comparison owner separately; do
    not duplicate a finding against the correct selected slot. This context-only observation
    is not an open finding against selected CultureMech000060 and is not an authorized
    repair target in this review.
  target_ids:
  - CultureMech:000060
  evidence_ids:
  - comparison
  - chebi32138
  - chebi32954
  - ccapCHM
  - writer-simple
findings:
- finding_id: f1
  issue_key: culturemech-000060-missing-source-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Selected owner omits source water and preparation
  description: The two selected records retain the solutes but omit the explicitly
    stated deionised-water input and autoclave step. Preserve input volume as such,
    without inventing a final-volume denominator or a temperature derived from pressure.
    The separately identified bacterial namesake already has preparation and is comparison
    evidence, not this target's generation owner.
  target_ids:
  - CultureMech:000060
  field_paths:
  - ingredients
  - preparation_steps
  - sterilization
  evidence_ids:
  - ccapCHM
  - target
  - owner
  - comparison
  - quantities
  rule_id: review-yaml-record/completeness
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/chm.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-000060-unsupported-algae-defaults
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Generic algae and cultivation defaults exceed the CHM source
  description: The source identifies CHM as Chilomonas Medium for Freshwater Protozoa.
    The current algae description, applications, light ranges/cycles and temperature
    range are generic import defaults unsupported by this exact source. Reconcile
    the biological scope and remove unsupported defaults without inferring a strain-growth
    claim or choosing an unverified taxonomic category.
  target_ids:
  - CultureMech:000060
  field_paths:
  - category
  - description
  - applications
  - light_intensity
  - light_cycle
  - temperature_range
  evidence_ids:
  - ccapCHM
  - target
  - owner
  - writer-ccap
  - quantities
  rule_id: review-yaml-record/scope
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/chm.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-000060-wrong-kg-identity
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Asserted C78 resolves to a different medium
  description: Fresh MediaDive C78 identifies PM and links MR_PM.pdf; it is not CHM.
    C23 independently identifies CHM and links the exact CCAP source, but correcting
    the KG association still requires scoped identity provenance, not identifier-set
    similarity alone. Do not import C78 formulation or treat C23 as an additional
    generation owner.
  target_ids:
  - CultureMech:000060
  field_paths:
  - kg_microbe_match
  evidence_ids:
  - apiC78
  - apiC23
  - ccapCHM
  - writer-kg
  rule_id: review-yaml-record/identity
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/chm.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-000060-generated-source-staleness
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated output omits existing owner source provenance
  description: The maintained algae owner already carries structured CCAP sources
    and its September repair event, while generated CHM omits them. Credit that repair.
    Current singleton merge copies the owner, so this is generated staleness rather
    than evidence of a current merge implementation that necessarily drops sources.
    Preserve earlier history and append future events.
  target_ids:
  - CultureMech:000060
  field_paths:
  - sources
  - curation_history
  evidence_ids:
  - target
  - owner
  - writer-ccap-sources
  - writer-merger
  rule_id: review-yaml-record/provenance
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/chm.yaml
    role: maintained source
actions:
- action_id: a1
  description: The two selected records retain the solutes but omit the explicitly
    stated deionised-water input and autoclave step. Preserve input volume as such,
    without inventing a final-volume denominator or a temperature derived from pressure.
    The separately identified bacterial namesake already has preparation and is comparison
    evidence, not this target's generation owner.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000060
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/chm.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a2
  description: The source identifies CHM as Chilomonas Medium for Freshwater Protozoa.
    The current algae description, applications, light ranges/cycles and temperature
    range are generic import defaults unsupported by this exact source. Reconcile
    the biological scope and remove unsupported defaults without inferring a strain-growth
    claim or choosing an unverified taxonomic category.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000060
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/chm.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a3
  description: Fresh MediaDive C78 identifies PM and links MR_PM.pdf; it is not CHM.
    C23 independently identifies CHM and links the exact CCAP source, but correcting
    the KG association still requires scoped identity provenance, not identifier-set
    similarity alone. Do not import C78 formulation or treat C23 as an additional
    generation owner.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000060
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/chm.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a4
  description: The maintained algae owner already carries structured CCAP sources
    and its September repair event, while generated CHM omits them. Credit that repair.
    Current singleton merge copies the owner, so this is generated staleness rather
    than evidence of a current merge implementation that necessarily drops sources.
    Preserve earlier history and append future events.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000060
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/chm.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- The scope includes all four selected concentration fields and three fields of the
  explicitly separate namesake comparison. Neither that comparison nor its historical
  API review becomes generation ownership.
- No current or archived KG graph was used to reconstruct the historical C78 assignment.
  Current API identity contradicts the local assertion; the historical graph mapping
  itself remains unrecovered.
- The fresh direct PDF revision002 differs from an older web-tool cached revision001.
  Only the directly captured current raw/text/visual bytes support this review.
- No exact original October7 raw event archive was recovered; fresh C23 equal bytes
  only authenticate report content.
- No strain-growth claim, optimization or experimental recommendation is inferred
  from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent
  rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed
  only on their declared normalization basis; unspecified percent bases and hydrate
  numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was
  performed by this author.
```
