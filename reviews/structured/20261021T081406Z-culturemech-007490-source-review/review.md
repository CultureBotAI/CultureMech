# Source and formulation review: 367 (CultureMech:007490)

- Review: 20261021T081406Z-culturemech-007490-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T08:09:13Z
- Finished UTC: 2026-10-21T08:14:06Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated numeric record identifies NBRC366 but still encodes the entire formulation as a concatenated ingredient and a blank ingredient with a chemical name in its concentration. Its maintained owner has recovered 12 source rows, pH and source metadata. These corrections have not reached the target. The official page gives the formula, optional agar and pH5.5 but no preparation or sterilization protocol. The maintained owner removes the generic preparation list (empty preparation_steps), while the target retains the unsupported fallback and labels autoclaving DISSOLVE.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 94; batch 010 item 4 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding nine task batches contain 90 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 92 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007490 | data/merge_yaml/merged/367.yaml | generated | 367 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007490 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007490 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch010/094/strict.tsv |
| validate-terms | passed | True | CultureMech:007490 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007490 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007490 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007490.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:007490.

0 primary CHEBI identities resolve with matching labels; 0 of 0 current secondary keys have live pinned-index rows. Unresolved keys: [].

2 direct ingredient instances; CHEBI-primary instance linkage 0/2 (0.00%), verified secondary coverage 0/2 (0.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Exact NBRC366 source and maintained owner

identity: supported. Targets: CultureMech:007490.

Stable ID CultureMech:007490, the merge contributor NBRC_367.yaml, the explicit import-history accession and both live source routes identify NBRC366. The official title field is blank; no conventional medium name is invented. Normalized/generated appearances of the same stable ID are distinct data layers, not evidence of two maintained IDs.

### Every malformed node, recovered quantity and pH claim

quantity: concern. Targets: CultureMech:007490.

Both target ingredient rows need correction. All 12 owner rows preserve the corresponding source numerals and supplied chemical/product forms. The water-input batch basis, optional agar and any liquid additions remain explicit; there are no source stock groups or target stock references to invent. The full field-by-field inventory records verified batch facts separately from nominal final-concentration interpretations.

[{"target_field": "ingredients[0]", "stored_value": {"preferred_term": "Peptone10gMeat extract10gYeast extract5gGlucose20gTween 801gK2HPO42gSodium acetate5gDiammonium hydrogencitrate2gMgSO4·7H2O0.2gMnSO4·nH2O0.05gDistilled water1LAgar (if needed)15gpH 5.5", "concentration": {"value": "variable", "unit": "VARIABLE"}}, "decision": "correct", "reason": "An entire composition table plus pH/footnotes is not one ingredient. VARIABLE conceals explicit source numerals."}, {"target_field": "ingredients[1]", "stored_value": {"preferred_term": "", "concentration": {"value": "Peptone", "unit": "G_PER_L"}}, "decision": "correct", "reason": "The ingredient name is blank and the concentration value is a chemical/product name, not an amount."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[0]", "source_locator": "#medium-comp table tr[0]", "source_excerpt": "Peptone 10 g", "source_amount": "10", "source_unit": "g", "owner_concentration": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Peptone is an undefined mixture; no supplier or digest substrate inferred.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[1]", "source_locator": "#medium-comp table tr[1]", "source_excerpt": "Meat extract 10 g", "source_amount": "10", "source_unit": "g", "owner_concentration": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Meat extract is left as supplied; no unverified substitution by beef extract.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[2]", "source_locator": "#medium-comp table tr[2]", "source_excerpt": "Yeast extract 5 g", "source_amount": "5", "source_unit": "g", "owner_concentration": {"value": "5", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Yeast extract remains a mixture without a reconstructed internal composition.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[3]", "source_locator": "#medium-comp table tr[3]", "source_excerpt": "Glucose 20 g", "source_amount": "20", "source_unit": "g", "owner_concentration": {"value": "20", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Glucose is generic; do not add an unstated stereochemical or hydrate qualifier.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[4]", "source_locator": "#medium-comp table tr[4]", "source_excerpt": "Tween 80 1 g", "source_amount": "1", "source_unit": "g", "owner_concentration": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Tween 80 is supplied as 1 g, not 1 ml; polysorbate80 class mapping does not establish a product lot or density.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[5]", "source_locator": "#medium-comp table tr[5]", "source_excerpt": "K 2 HPO 4 2 g", "source_amount": "2", "source_unit": "g", "owner_concentration": {"value": "2", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Dipotassium hydrogen phosphate is distinct from monopotassium phosphate.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[6]", "source_locator": "#medium-comp table tr[6]", "source_excerpt": "Sodium acetate 5 g", "source_amount": "5", "source_unit": "g", "owner_concentration": {"value": "5", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Sodium acetate has no explicit hydrate in the source; no hydrate-specific mass conversion.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[7]", "source_locator": "#medium-comp table tr[7]", "source_excerpt": "Diammonium hydrogencitrate 2 g", "source_amount": "2", "source_unit": "g", "owner_concentration": {"value": "2", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Diammonium hydrogencitrate must retain its ammonium counterion count and citrate protonation.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[8]", "source_locator": "#medium-comp table tr[8]", "source_excerpt": "MgSO 4 ·7H 2 O 0.2 g", "source_amount": "0.2", "source_unit": "g", "owner_concentration": {"value": "0.2", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Magnesium sulfate heptahydrate is explicit.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[9]", "source_locator": "#medium-comp table tr[9]", "source_excerpt": "MnSO 4 ·nH 2 O 0.05 g", "source_amount": "0.05", "source_unit": "g", "owner_concentration": {"value": "0.05", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "The hydrate number n is unspecified; do not replace it by monohydrate or calculate molarity.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[10]", "source_locator": "#medium-comp table tr[10]", "source_excerpt": "Distilled water 1 L", "source_amount": "1", "source_unit": "L", "owner_concentration": {"value": "1", "unit": "L"}, "decision": "verified", "reason": "The source directly reports the one-liter water quantity.", "chemical_form_and_scope": "One liter of water is the stated batch input, not a measured final-volume result.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[11]", "source_locator": "#medium-comp table tr[11]", "source_excerpt": "Agar (if needed) 15 g", "source_amount": "15", "source_unit": "g", "owner_concentration": {"value": "15", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Agar is explicitly optional at 15 g; do not infer mandatory solid culture.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"field": "ph_value", "source_excerpt": "pH 5.5", "source_locator": "#medium-comp pH line", "owner_value": 5.5, "target_value": null, "decision": "add", "reason": "Source pH is explicit and maintained but absent as a structured target value; it remains buried in the ingredient blob."}]

### Maintained recovery and later source metadata versus generated bytes

completeness: concern. Targets: CultureMech:007490.

The target retains the pre-recovery composition, lacks structured pH, source term, source reference and recovered mappings, and ends with the August6 merge event. The owner contains August19 recovery, August20 linkage and September source-repair events. These are observed content differences; no generator rerun or causal history reconstruction was performed.

### Source-specific protocol versus generated default steps

evidence: concern. Targets: CultureMech:007490.

The official page gives the formula, optional agar and pH5.5 but no preparation or sterilization protocol. The maintained owner removes the generic preparation list (empty preparation_steps), while the target retains the unsupported fallback and labels autoclaving DISSOLVE.

### Resolved owner identifiers and exact chemical-form scope

grounding: concern. Targets: CultureMech:007490.

All 8 distinct owner ontology IDs resolve and are non-obsolete; 3 asserted labels differ from canonical labels. The quantity inventory separately preserves source hydrate, salt, stereochemical and undefined-mixture limits. Canonical label resolution alone is not proof of supplied chemical form or preparation. No replacement identifiers were invented.

[{"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[0].term", "id": "MICRO:0000178", "asserted_label": "Peptone", "canonical_label": "peptone", "label_matches": false, "definition": [], "source_form_scope": "Peptone is an undefined mixture; no supplier or digest substrate inferred."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[2].term", "id": "FOODON:03315426", "asserted_label": "Yeast extract", "canonical_label": "yeast extract", "label_matches": false, "definition": ["SIREN DB annotation:\n* not heat-treated FOODON:03440003\n* part of algae or fungus FOODON:03420247"], "source_form_scope": "Yeast extract remains a mixture without a reconstructed internal composition."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[3].term", "id": "CHEBI:17234", "asserted_label": "glucose", "canonical_label": "glucose", "label_matches": true, "definition": ["An aldohexose used as a source of energy and metabolic intermediate."], "source_form_scope": "Glucose is generic; do not add an unstated stereochemical or hydrate qualifier."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[4].term", "id": "CHEBI:53426", "asserted_label": "polysorbate 80", "canonical_label": "polysorbate 80", "label_matches": true, "definition": ["A polymer composed of PEG-ylated sorbitan, where the total number of poly(ethylene glycol) units is 20 (&lt;em&gt;w&lt;/em&gt; + &lt;em&gt;x&lt;/em&gt; + &lt;em&gt;y&lt;/em&gt; + &lt;em&gt;z&lt;/em&gt; = 20) and a single terminal is capped by an oleoyl group."], "source_form_scope": "Tween 80 is supplied as 1 g, not 1 ml; polysorbate80 class mapping does not establish a product lot or density."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[5].term", "id": "CHEBI:131527", "asserted_label": "dipotassium hydrogen phosphate", "canonical_label": "dipotassium hydrogen phosphate", "label_matches": true, "definition": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "source_form_scope": "Dipotassium hydrogen phosphate is distinct from monopotassium phosphate."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[6].term", "id": "CHEBI:32954", "asserted_label": "sodium acetate", "canonical_label": "sodium acetate", "label_matches": true, "definition": [], "source_form_scope": "Sodium acetate has no explicit hydrate in the source; no hydrate-specific mass conversion."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[10].term", "id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_matches": true, "definition": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "source_form_scope": "One liter of water is the stated batch input, not a measured final-volume result."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[11].term", "id": "CHEBI:2509", "asserted_label": "Agar", "canonical_label": "agar", "label_matches": false, "definition": ["A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties."], "source_form_scope": "Agar is explicitly optional at 15 g; do not infer mandatory solid culture."}]

### Separate malformed-target and recovered-owner linkage denominators

grounding: concern. Targets: CultureMech:007490.

Target primary and secondary linkage are 0/2 (0%) of malformed rows; this does not mean two legitimate ingredients were checked. Owner all-ontology primary linkage is 8/12 (66.67%), CHEBI linkage is 6/12 (50.00%), and live pinned secondary linkage is 0/12 (0.00%). These are 0–100 linkage percentages, not scientific correctness scores.

### Source classification, optionality and absence of asserted growth claims

scope: supported. Targets: CultureMech:007490.

The official medium-title field is blank; no MRS name or recipe equivalence is inferred. Peptone and extracts support COMPLEX/UNDEFINED. SOLID_AGAR describes only the optional agar preparation; preserve the liquid alternative. The target and owner assert no target-organism IDs, gene/transcriptomic context, native variants, parent links or KG-Microbe match. No organism-specific growth, optimization, incubation or strain identity is inferred from a medium title or bacterial filing category.

### History integrity and narrow claim evidence

provenance: concern. Targets: CultureMech:007490.

All six target and eight owner timestamps parse with timezones; the first five events agree and later entries remain append-only context. The owner primary reference and notes identify the source but contain no narrow ingredient/root evidence excerpts. The target reference validator checked zero excerpts. Source availability and every amount were checked directly above; a zero-issue result did not test them.

## Findings

### f1: Generated formula remains a table blob and an unnamed ingredient

blocker / open / confirmed; issue key: CM007490-malformed-generated-formulation.

The target has two malformed ingredient objects instead of the 12 source rows. One names the complete recipe including pH/footnotes and assigns VARIABLE; the other has a blank preferred term and 'Peptone' as a G_PER_L value. This prevents faithful machine interpretation despite the four documented checks passing; it is a scientific representation blocker, not a P1.1 schema failure.

### f2: Maintained source-backed corrections have not reached the target

major / open / confirmed; issue key: CM007490-stale-source-ph-grounding.

The owner supplies NBRC366 source metadata, structured pH5.5, recovered row identities and later recovery/grounding history missing from the target. Corrected composition is tracked in the separate blocker; this finding covers lost identity, pH and provenance.

### f3: Generated preparation defaults lack the required source scope

major / open / confirmed; issue key: CM007490-unsupported-generated-preparation.

The official page gives the formula, optional agar and pH5.5 but no preparation or sterilization protocol. The maintained owner removes the generic preparation list (empty preparation_steps), while the target retains the unsupported fallback and labels autoclaving DISSOLVE.

### f4: Three maintained-owner labels differ from canonical ontology labels

minor / open / confirmed; issue key: CM007490-owner-canonical-labels.

MICRO:0000178: 'Peptone' versus canonical 'peptone'; FOODON:03315426: 'Yeast extract' versus canonical 'yeast extract'; CHEBI:2509: 'Agar' versus canonical 'agar'. These are case/label discrepancies on resolved identifiers, not demonstrated wrong material IDs.

### f5: Source provenance lacks narrow claim excerpts

minor / open / confirmed; issue key: CM007490-claim-evidence-gap.

The maintained primary reference and notes identify the correct source but do not attach exact excerpt evidence to individual amounts, the water-input basis, pH or source-specific preparation/optionality. The target lacks the maintained reference and its validator checked zero evidence excerpts.

## Recommended Actions And Acceptance Checks

### a1

Verify every recovered maintained-owner row and source batch/optionality boundary, retain the stable source identity, then regenerate the merged record. Do not edit the generated table blob directly.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Verify owner source metadata and canonical labels, then regenerate and confirm that pH, source accession, references, supported mappings and append-only history survive. Keep provider accession separate from the local numeric filename.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the supported pH5.5 and optional-agar scope; do not reintroduce the unsupported importer defaults when regenerating from the maintained owner. Add a sterilization or preparation procedure only if an exact source supports it.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Canonicalize maintained-owner term labels while preserving preferred source names, IDs, exact material forms and concentration evidence before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Attach short exact excerpts and locators to each maintained ingredient amount and other narrow claims using the existing evidence slots. Keep original source units and batch conditions distinct from arithmetic or interpretation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/367.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_367.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/367.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/367.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch010/094/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch010/094/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/367.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/367.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/367.yaml:1:id: CultureMech:007490<br>./data/normalized_yaml/bacterial/NBRC_367.yaml:1:id: CultureMech:007490<br> |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {} |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=366; Medium No.; Medium title; #medium-comp nested composition table, pH, footnotes and Comment | supports | The complete official NBRC366 medium page was read: all 12 composition rows, pH5.5, optionality and any footnotes. The official medium-title field is blank; no MRS name or recipe equivalence is inferred. Peptone and extracts support COMPLEX/UNDEFINED. SOLID_AGAR describes only the optional agar preparation; preserve the liquid alternative. |
| legacy | http://www.nbrc.nite.go.jp/NBRC2/NBRCMediumDetailServlet?NO=366; Historical HTTP servlet redirect; Medium No.; full medium detail | supports | The exact historical servlet URL in the import event resolves to the current NBRC366 record. Preserve the request URL, resolved URL, original timestamp and response hash; the local numeric filename is not the provider accession. |
| owner-micro0000178 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000178; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier MICRO:0000178 resolves to canonical label 'peptone', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier FOODON:03315426 resolves to canonical label 'yeast extract', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier CHEBI:17234 resolves to canonical label 'glucose', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-chebi53426 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53426; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier CHEBI:53426 resolves to canonical label 'polysorbate 80', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier CHEBI:131527 resolves to canonical label 'dipotassium hydrogen phosphate', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier CHEBI:32954 resolves to canonical label 'sodium acetate', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier CHEBI:15377 resolves to canonical label 'water', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier CHEBI:2509 resolves to canonical label 'agar', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-mim | src/culturemech/data/mediaingredientmech/label_index.csv; All pinned live preferred-term rows for current owner secondary identifiers; adjacent snapshot metadata captured | context_only | {"secondary_identifier_instances": [], "matching_rows": {}, "limit": "A key/alias match is linkage evidence, not proof that every alias has the correct chemical form. The source and canonical term separately establish any hydrate correspondence."} |
| quantity-inventory | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=366; Every source table row, pH line, both target ingredient nodes, and exact owner field paths | supports | [{"target_field": "ingredients[0]", "stored_value": {"preferred_term": "Peptone10gMeat extract10gYeast extract5gGlucose20gTween 801gK2HPO42gSodium acetate5gDiammonium hydrogencitrate2gMgSO4·7H2O0.2gMnSO4·nH2O0.05gDistilled water1LAgar (if needed)15gpH 5.5", "concentration": {"value": "variable", "unit": "VARIABLE"}}, "decision": "correct", "reason": "An entire composition table plus pH/footnotes is not one ingredient. VARIABLE conceals explicit source numerals."}, {"target_field": "ingredients[1]", "stored_value": {"preferred_term": "", "concentration": {"value": "Peptone", "unit": "G_PER_L"}}, "decision": "correct", "reason": "The ingredient name is blank and the concentration value is a chemical/product name, not an amount."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[0]", "source_locator": "#medium-comp table tr[0]", "source_excerpt": "Peptone 10 g", "source_amount": "10", "source_unit": "g", "owner_concentration": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Peptone is an undefined mixture; no supplier or digest substrate inferred.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[1]", "source_locator": "#medium-comp table tr[1]", "source_excerpt": "Meat extract 10 g", "source_amount": "10", "source_unit": "g", "owner_concentration": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Meat extract is left as supplied; no unverified substitution by beef extract.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[2]", "source_locator": "#medium-comp table tr[2]", "source_excerpt": "Yeast extract 5 g", "source_amount": "5", "source_unit": "g", "owner_concentration": {"value": "5", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Yeast extract remains a mixture without a reconstructed internal composition.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[3]", "source_locator": "#medium-comp table tr[3]", "source_excerpt": "Glucose 20 g", "source_amount": "20", "source_unit": "g", "owner_concentration": {"value": "20", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Glucose is generic; do not add an unstated stereochemical or hydrate qualifier.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[4]", "source_locator": "#medium-comp table tr[4]", "source_excerpt": "Tween 80 1 g", "source_amount": "1", "source_unit": "g", "owner_concentration": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Tween 80 is supplied as 1 g, not 1 ml; polysorbate80 class mapping does not establish a product lot or density.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[5]", "source_locator": "#medium-comp table tr[5]", "source_excerpt": "K 2 HPO 4 2 g", "source_amount": "2", "source_unit": "g", "owner_concentration": {"value": "2", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Dipotassium hydrogen phosphate is distinct from monopotassium phosphate.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[6]", "source_locator": "#medium-comp table tr[6]", "source_excerpt": "Sodium acetate 5 g", "source_amount": "5", "source_unit": "g", "owner_concentration": {"value": "5", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Sodium acetate has no explicit hydrate in the source; no hydrate-specific mass conversion.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[7]", "source_locator": "#medium-comp table tr[7]", "source_excerpt": "Diammonium hydrogencitrate 2 g", "source_amount": "2", "source_unit": "g", "owner_concentration": {"value": "2", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Diammonium hydrogencitrate must retain its ammonium counterion count and citrate protonation.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[8]", "source_locator": "#medium-comp table tr[8]", "source_excerpt": "MgSO 4 ·7H 2 O 0.2 g", "source_amount": "0.2", "source_unit": "g", "owner_concentration": {"value": "0.2", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Magnesium sulfate heptahydrate is explicit.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[9]", "source_locator": "#medium-comp table tr[9]", "source_excerpt": "MnSO 4 ·nH 2 O 0.05 g", "source_amount": "0.05", "source_unit": "g", "owner_concentration": {"value": "0.05", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "The hydrate number n is unspecified; do not replace it by monohydrate or calculate molarity.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[10]", "source_locator": "#medium-comp table tr[10]", "source_excerpt": "Distilled water 1 L", "source_amount": "1", "source_unit": "L", "owner_concentration": {"value": "1", "unit": "L"}, "decision": "verified", "reason": "The source directly reports the one-liter water quantity.", "chemical_form_and_scope": "One liter of water is the stated batch input, not a measured final-volume result.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[11]", "source_locator": "#medium-comp table tr[11]", "source_excerpt": "Agar (if needed) 15 g", "source_amount": "15", "source_unit": "g", "owner_concentration": {"value": "15", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Agar is explicitly optional at 15 g; do not infer mandatory solid culture.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"field": "ph_value", "source_excerpt": "pH 5.5", "source_locator": "#medium-comp pH line", "owner_value": 5.5, "target_value": null, "decision": "add", "reason": "Source pH is explicit and maintained but absent as a structured target value; it remains buried in the ingredient blob."}] |
| audit-context | data/normalized_yaml/bacterial/NBRC_367.yaml; Entire owner versus generated record; all term labels, source references, later history and timezone fields | context_only | {"owner_identifier_checks": [{"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[0].term", "id": "MICRO:0000178", "asserted_label": "Peptone", "canonical_label": "peptone", "label_matches": false, "definition": [], "source_form_scope": "Peptone is an undefined mixture; no supplier or digest substrate inferred."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[2].term", "id": "FOODON:03315426", "asserted_label": "Yeast extract", "canonical_label": "yeast extract", "label_matches": false, "definition": ["SIREN DB annotation:\n* not heat-treated FOODON:03440003\n* part of algae or fungus FOODON:03420247"], "source_form_scope": "Yeast extract remains a mixture without a reconstructed internal composition."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[3].term", "id": "CHEBI:17234", "asserted_label": "glucose", "canonical_label": "glucose", "label_matches": true, "definition": ["An aldohexose used as a source of energy and metabolic intermediate."], "source_form_scope": "Glucose is generic; do not add an unstated stereochemical or hydrate qualifier."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[4].term", "id": "CHEBI:53426", "asserted_label": "polysorbate 80", "canonical_label": "polysorbate 80", "label_matches": true, "definition": ["A polymer composed of PEG-ylated sorbitan, where the total number of poly(ethylene glycol) units is 20 (&lt;em&gt;w&lt;/em&gt; + &lt;em&gt;x&lt;/em&gt; + &lt;em&gt;y&lt;/em&gt; + &lt;em&gt;z&lt;/em&gt; = 20) and a single terminal is capped by an oleoyl group."], "source_form_scope": "Tween 80 is supplied as 1 g, not 1 ml; polysorbate80 class mapping does not establish a product lot or density."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[5].term", "id": "CHEBI:131527", "asserted_label": "dipotassium hydrogen phosphate", "canonical_label": "dipotassium hydrogen phosphate", "label_matches": true, "definition": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "source_form_scope": "Dipotassium hydrogen phosphate is distinct from monopotassium phosphate."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[6].term", "id": "CHEBI:32954", "asserted_label": "sodium acetate", "canonical_label": "sodium acetate", "label_matches": true, "definition": [], "source_form_scope": "Sodium acetate has no explicit hydrate in the source; no hydrate-specific mass conversion."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[10].term", "id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_matches": true, "definition": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "source_form_scope": "One liter of water is the stated batch input, not a measured final-volume result."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[11].term", "id": "CHEBI:2509", "asserted_label": "Agar", "canonical_label": "agar", "label_matches": false, "definition": ["A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties."], "source_form_scope": "Agar is explicitly optional at 15 g; do not infer mandatory solid culture."}], "history": {"target": {"count": 6, "timezone_bearing_timestamps": ["2026-02-20T00:22:35.953837Z", "2026-03-13T03:09:26.666003Z", "2026-03-13T06:19:49.239630Z", "2026-03-14T00:00:00+00:00", "2026-05-16T09:03:06.694710+00:00", "2026-08-06T03:05:04.676649+00:00"]}, "owner": {"count": 8, "timezone_bearing_timestamps": ["2026-02-20T00:22:35.953837Z", "2026-03-13T03:09:26.666003Z", "2026-03-13T06:19:49.239630Z", "2026-03-14T00:00:00+00:00", "2026-05-16T09:03:06.694710+00:00", "2026-08-19T21:54:22.912825+00:00", "2026-08-20T19:01:16.015082+00:00", "2026-09-07T00:00:00-07:00"]}}, "owner_reference": [{"reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=366"}], "target_reference_count": 0, "owner_narrow_evidence_present": false} |
| importer | src/culturemech/import/nbrc_importer.py; _create_description; _map_ingredients; _infer_physical_state; _map_preparation_steps; _determine_category | supports | Current code maps g/mg/ml to nominal per-liter units, defaults unknown units to G_PER_L, infers SOLID_AGAR from any agar substring without optionality handling, and synthesizes dissolve/conditional-pH/autoclave steps if preparation is empty. The autoclave substring does not match autoclaving, leaving the action DISSOLVE. These inspected current rules explain a reproducible failure mode; historical execution is not reconstructed. |
| scraper | src/culturemech/fetch/nbrc_scraper.py; _extract_ingredients and _extract_preparation | context_only | The current extractor scans nested tables and descendant rows/cells, takes the first two cells as name/amount, and uses unseparated text extraction. The preparation reader looks for a preparation label and a following list. This is current context for collapsed tables and missed composition footnotes, not a rerun or a claim that no historical fixes occurred. |
| recovery | scripts/recover_nbrc_composition.py; Module explanation; parse_composition; _ingredient; media_number_index | supports | The inspected recovery implementation distinguishes three-cell ingredient rows from one-cell prose, retains supplier/filtering footnotes rather than treating them as stock recipes, and maps explicit g/mg/ml/L units. It documents the historical table-blob issue and the distinction between record names and provider medium numbers. The source table and current owner were independently compared; the script was not executed. |
| raw-converter | src/culturemech/convert/nbrc_raw_yaml.py; Module contract and main converter dispatch | context_only | The NBRC raw-YAML converter dispatches a direct JSON-to-YAML conversion without normalization. It is not a maintained scientific curation owner or a remedy for damaged source-JSON ingredient structure. |

## Limits And Additional Notes

- The original historical scrape bytes were not reconstructed. The official pages were captured on their recorded access dates; current importer code is evidence of present behavior, not proof of the exact historical execution.
- The source table states a 1 L distilled-water input. Its nominal per-liter convention is retained without claiming an independently measured final volume after dissolved solids or added liquids. No density, hydrate mass, molarity or exact final-volume conversion is inferred.
- The maintained owner is context for this one generated target, not a second reviewed record. Ontology ID/label resolution and pinned MIM linkage are checked separately from source-supported chemical form, product grade and preparation.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T081406Z-culturemech-007490-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 367 (CultureMech:007490)'
started_at: '2026-10-21T08:09:13Z'
finished_at: '2026-10-21T08:14:06Z'
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
summary: The generated numeric record identifies NBRC366 but still encodes the entire
  formulation as a concatenated ingredient and a blank ingredient with a chemical
  name in its concentration. Its maintained owner has recovered 12 source rows, pH
  and source metadata. These corrections have not reached the target. The official
  page gives the formula, optional agar and pH5.5 but no preparation or sterilization
  protocol. The maintained owner removes the generic preparation list (empty preparation_steps),
  while the target retains the unsupported fallback and labels autoclaving DISSOLVE.
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
  - path: data/merge_yaml/merged/367.yaml
    sha256: 36d9bad9b6f53a2cae1c1eb670549c444136ec272ce5a792ccf363cb2d4d7fc8
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_367.yaml
    sha256: 28b5fd44ef48fd5d963c6111cd891ec6574a194049145d502852e1d9fb518e0c
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
  - path: scripts/recover_nbrc_composition.py
    sha256: a723e458895350a68ffae3e446006205b2e00cb185bee13976d5047be56405f0
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/nbrc_raw_yaml.py
    sha256: de5654d4eed2e01a2383dcf417b7d8e2779dbb622de9351c28373fb691812ec1
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/fetch/nbrc_scraper.py
    sha256: 5c5bbda489abe0b6d000b9318a76913ab5496ee83aff58b530c2b42b5989d1e3
    role: context
  - path: src/culturemech/import/nbrc_importer.py
    sha256: 857b7e0ac88aef783ce4bc9b35c4c6a3d9fc38824a5d463010a6046ac4180924
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
  selection: Task review 94; batch 010 item 4 of 10, selected in Python lexicographic
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
  - CultureMech:007490
targets:
- target_id: CultureMech:007490
  path: data/merge_yaml/merged/367.yaml
  label: '367'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_367.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/367.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007490
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/367.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch010/094/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch010/094/strict.tsv"
  target_ids:
  - CultureMech:007490
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/367.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007490
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/367.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007490
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
  - CultureMech:007490
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/367.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T08:14:05Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_367.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T08:14:05Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/367.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:10:12.510521Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/367.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch010/094/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T08:10:14.166793Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch010/094/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/367.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:10:17.084315Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/367.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:10:20.222351Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T08:14:05Z'
  support: supports
  summary: './data/merge_yaml/merged/367.yaml:1:id: CultureMech:007490

    ./data/normalized_yaml/bacterial/NBRC_367.yaml:1:id: CultureMech:007490

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T08:14:05Z'
  support: supports
  summary: '{}'
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=366
  locator: 'Medium No.; Medium title; #medium-comp nested composition table, pH, footnotes
    and Comment'
  accessed_at: '2026-10-21T08:00:49.998391Z'
  support: supports
  summary: 'The complete official NBRC366 medium page was read: all 12 composition
    rows, pH5.5, optionality and any footnotes. The official medium-title field is
    blank; no MRS name or recipe equivalence is inferred. Peptone and extracts support
    COMPLEX/UNDEFINED. SOLID_AGAR describes only the optional agar preparation; preserve
    the liquid alternative.'
  quote: pH 5.5
  snapshot_sha256: 4837825185e5b052e48ee943f2ccf9fb4088a3eb2baf93fb41c9793ec3b01bf1
- evidence_id: legacy
  kind: primary_source
  reference: http://www.nbrc.nite.go.jp/NBRC2/NBRCMediumDetailServlet?NO=366
  locator: Historical HTTP servlet redirect; Medium No.; full medium detail
  accessed_at: '2026-10-21T08:00:45.622381Z'
  support: supports
  summary: The exact historical servlet URL in the import event resolves to the current
    NBRC366 record. Preserve the request URL, resolved URL, original timestamp and
    response hash; the local numeric filename is not the provider accession.
  snapshot_sha256: 4837825185e5b052e48ee943f2ccf9fb4088a3eb2baf93fb41c9793ec3b01bf1
- evidence_id: owner-micro0000178
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000178
  locator: '$._embedded.terms[0]: obo_id, label, description, is_obsolete'
  accessed_at: '2026-10-21T08:00:49.423450Z'
  support: context_only
  summary: Exact owner identifier MICRO:0000178 resolves to canonical label 'peptone',
    is not obsolete, and has the captured definition. This response verifies identifier/label
    correspondence; source material, hydrate, stereochemistry and product scope are
    assessed separately in the quantity inventory.
  snapshot_sha256: ef45aa186438f91d015280171fde8ccb25740a50cc6f2c6e848de6aad3339b31
- evidence_id: owner-foodon03315426
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426
  locator: '$._embedded.terms[0]: obo_id, label, description, is_obsolete'
  accessed_at: '2026-10-21T08:00:49.388263Z'
  support: context_only
  summary: Exact owner identifier FOODON:03315426 resolves to canonical label 'yeast
    extract', is not obsolete, and has the captured definition. This response verifies
    identifier/label correspondence; source material, hydrate, stereochemistry and
    product scope are assessed separately in the quantity inventory.
  snapshot_sha256: cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44
- evidence_id: owner-chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: '$._embedded.terms[0]: obo_id, label, description, is_obsolete'
  accessed_at: '2026-10-21T08:00:47.394885Z'
  support: context_only
  summary: Exact owner identifier CHEBI:17234 resolves to canonical label 'glucose',
    is not obsolete, and has the captured definition. This response verifies identifier/label
    correspondence; source material, hydrate, stereochemistry and product scope are
    assessed separately in the quantity inventory.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: owner-chebi53426
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53426
  locator: '$._embedded.terms[0]: obo_id, label, description, is_obsolete'
  accessed_at: '2026-10-21T08:00:48.722812Z'
  support: context_only
  summary: Exact owner identifier CHEBI:53426 resolves to canonical label 'polysorbate
    80', is not obsolete, and has the captured definition. This response verifies
    identifier/label correspondence; source material, hydrate, stereochemistry and
    product scope are assessed separately in the quantity inventory.
  snapshot_sha256: d213680c843282430d36cc13a81ee5bfda8029054f6b1482a375c35fd94191a6
- evidence_id: owner-chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: '$._embedded.terms[0]: obo_id, label, description, is_obsolete'
  accessed_at: '2026-10-21T08:00:46.687620Z'
  support: context_only
  summary: Exact owner identifier CHEBI:131527 resolves to canonical label 'dipotassium
    hydrogen phosphate', is not obsolete, and has the captured definition. This response
    verifies identifier/label correspondence; source material, hydrate, stereochemistry
    and product scope are assessed separately in the quantity inventory.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: owner-chebi32954
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954
  locator: '$._embedded.terms[0]: obo_id, label, description, is_obsolete'
  accessed_at: '2026-10-21T08:00:48.206583Z'
  support: context_only
  summary: Exact owner identifier CHEBI:32954 resolves to canonical label 'sodium
    acetate', is not obsolete, and has the captured definition. This response verifies
    identifier/label correspondence; source material, hydrate, stereochemistry and
    product scope are assessed separately in the quantity inventory.
  snapshot_sha256: 573cba85f57c363463610a20b17be618893d6432ba239604fbd8aa562f98161b
- evidence_id: owner-chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: '$._embedded.terms[0]: obo_id, label, description, is_obsolete'
  accessed_at: '2026-10-21T08:00:46.690750Z'
  support: context_only
  summary: Exact owner identifier CHEBI:15377 resolves to canonical label 'water',
    is not obsolete, and has the captured definition. This response verifies identifier/label
    correspondence; source material, hydrate, stereochemistry and product scope are
    assessed separately in the quantity inventory.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: owner-chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: '$._embedded.terms[0]: obo_id, label, description, is_obsolete'
  accessed_at: '2026-10-21T08:00:47.471291Z'
  support: context_only
  summary: Exact owner identifier CHEBI:2509 resolves to canonical label 'agar', is
    not obsolete, and has the captured definition. This response verifies identifier/label
    correspondence; source material, hydrate, stereochemistry and product scope are
    assessed separately in the quantity inventory.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: owner-mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All pinned live preferred-term rows for current owner secondary identifiers;
    adjacent snapshot metadata captured
  accessed_at: '2026-10-21T08:14:05Z'
  support: context_only
  summary: '{"secondary_identifier_instances": [], "matching_rows": {}, "limit": "A
    key/alias match is linkage evidence, not proof that every alias has the correct
    chemical form. The source and canonical term separately establish any hydrate
    correspondence."}'
- evidence_id: quantity-inventory
  kind: record_content
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=366
  locator: Every source table row, pH line, both target ingredient nodes, and exact
    owner field paths
  accessed_at: '2026-10-21T08:14:05Z'
  support: supports
  summary: '[{"target_field": "ingredients[0]", "stored_value": {"preferred_term":
    "Peptone10gMeat extract10gYeast extract5gGlucose20gTween 801gK2HPO42gSodium acetate5gDiammonium
    hydrogencitrate2gMgSO4·7H2O0.2gMnSO4·nH2O0.05gDistilled water1LAgar (if needed)15gpH
    5.5", "concentration": {"value": "variable", "unit": "VARIABLE"}}, "decision":
    "correct", "reason": "An entire composition table plus pH/footnotes is not one
    ingredient. VARIABLE conceals explicit source numerals."}, {"target_field": "ingredients[1]",
    "stored_value": {"preferred_term": "", "concentration": {"value": "Peptone", "unit":
    "G_PER_L"}}, "decision": "correct", "reason": "The ingredient name is blank and
    the concentration value is a chemical/product name, not an amount."}, {"owner_field":
    "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[0]", "source_locator":
    "#medium-comp table tr[0]", "source_excerpt": "Peptone 10 g", "source_amount":
    "10", "source_unit": "g", "owner_concentration": {"value": "10", "unit": "G_PER_L"},
    "decision": "evidence_only", "reason": "The owner preserves the source numeral
    and mass/volume unit on a nominal one-liter water-input basis; this is not an
    independently verified final-volume concentration.", "chemical_form_and_scope":
    "Peptone is an undefined mixture; no supplier or digest substrate inferred.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[1]",
    "source_locator": "#medium-comp table tr[1]", "source_excerpt": "Meat extract
    10 g", "source_amount": "10", "source_unit": "g", "owner_concentration": {"value":
    "10", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Meat extract is left as supplied; no unverified substitution by beef extract.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[2]",
    "source_locator": "#medium-comp table tr[2]", "source_excerpt": "Yeast extract
    5 g", "source_amount": "5", "source_unit": "g", "owner_concentration": {"value":
    "5", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Yeast extract remains a mixture without a reconstructed internal composition.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[3]",
    "source_locator": "#medium-comp table tr[3]", "source_excerpt": "Glucose 20 g",
    "source_amount": "20", "source_unit": "g", "owner_concentration": {"value": "20",
    "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Glucose is generic; do not add an unstated stereochemical or hydrate qualifier.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[4]",
    "source_locator": "#medium-comp table tr[4]", "source_excerpt": "Tween 80 1 g",
    "source_amount": "1", "source_unit": "g", "owner_concentration": {"value": "1",
    "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Tween 80 is supplied as 1 g, not 1 ml; polysorbate80 class mapping does not establish
    a product lot or density.", "target_reconstruction": "Replace the malformed target
    rows only after owner verification and separately authorized regeneration."},
    {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[5]",
    "source_locator": "#medium-comp table tr[5]", "source_excerpt": "K 2 HPO 4 2 g",
    "source_amount": "2", "source_unit": "g", "owner_concentration": {"value": "2",
    "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Dipotassium hydrogen phosphate is distinct from monopotassium phosphate.", "target_reconstruction":
    "Replace the malformed target rows only after owner verification and separately
    authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[6]",
    "source_locator": "#medium-comp table tr[6]", "source_excerpt": "Sodium acetate
    5 g", "source_amount": "5", "source_unit": "g", "owner_concentration": {"value":
    "5", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Sodium acetate has no explicit hydrate in the source; no hydrate-specific mass
    conversion.", "target_reconstruction": "Replace the malformed target rows only
    after owner verification and separately authorized regeneration."}, {"owner_field":
    "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[7]", "source_locator":
    "#medium-comp table tr[7]", "source_excerpt": "Diammonium hydrogencitrate 2 g",
    "source_amount": "2", "source_unit": "g", "owner_concentration": {"value": "2",
    "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Diammonium hydrogencitrate must retain its ammonium counterion count and citrate
    protonation.", "target_reconstruction": "Replace the malformed target rows only
    after owner verification and separately authorized regeneration."}, {"owner_field":
    "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[8]", "source_locator":
    "#medium-comp table tr[8]", "source_excerpt": "MgSO 4 ·7H 2 O 0.2 g", "source_amount":
    "0.2", "source_unit": "g", "owner_concentration": {"value": "0.2", "unit": "G_PER_L"},
    "decision": "evidence_only", "reason": "The owner preserves the source numeral
    and mass/volume unit on a nominal one-liter water-input basis; this is not an
    independently verified final-volume concentration.", "chemical_form_and_scope":
    "Magnesium sulfate heptahydrate is explicit.", "target_reconstruction": "Replace
    the malformed target rows only after owner verification and separately authorized
    regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[9]",
    "source_locator": "#medium-comp table tr[9]", "source_excerpt": "MnSO 4 ·nH 2
    O 0.05 g", "source_amount": "0.05", "source_unit": "g", "owner_concentration":
    {"value": "0.05", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The
    owner preserves the source numeral and mass/volume unit on a nominal one-liter
    water-input basis; this is not an independently verified final-volume concentration.",
    "chemical_form_and_scope": "The hydrate number n is unspecified; do not replace
    it by monohydrate or calculate molarity.", "target_reconstruction": "Replace the
    malformed target rows only after owner verification and separately authorized
    regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[10]",
    "source_locator": "#medium-comp table tr[10]", "source_excerpt": "Distilled water
    1 L", "source_amount": "1", "source_unit": "L", "owner_concentration": {"value":
    "1", "unit": "L"}, "decision": "verified", "reason": "The source directly reports
    the one-liter water quantity.", "chemical_form_and_scope": "One liter of water
    is the stated batch input, not a measured final-volume result.", "target_reconstruction":
    "Replace the malformed target rows only after owner verification and separately
    authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[11]",
    "source_locator": "#medium-comp table tr[11]", "source_excerpt": "Agar (if needed)
    15 g", "source_amount": "15", "source_unit": "g", "owner_concentration": {"value":
    "15", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Agar is explicitly optional at 15 g; do not infer mandatory solid culture.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"field": "ph_value", "source_excerpt":
    "pH 5.5", "source_locator": "#medium-comp pH line", "owner_value": 5.5, "target_value":
    null, "decision": "add", "reason": "Source pH is explicit and maintained but absent
    as a structured target value; it remains buried in the ingredient blob."}]'
- evidence_id: audit-context
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_367.yaml
  locator: Entire owner versus generated record; all term labels, source references,
    later history and timezone fields
  accessed_at: '2026-10-21T08:14:05Z'
  support: context_only
  summary: '{"owner_identifier_checks": [{"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[0].term",
    "id": "MICRO:0000178", "asserted_label": "Peptone", "canonical_label": "peptone",
    "label_matches": false, "definition": [], "source_form_scope": "Peptone is an
    undefined mixture; no supplier or digest substrate inferred."}, {"owner_field":
    "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[2].term", "id": "FOODON:03315426",
    "asserted_label": "Yeast extract", "canonical_label": "yeast extract", "label_matches":
    false, "definition": ["SIREN DB annotation:\n* not heat-treated FOODON:03440003\n*
    part of algae or fungus FOODON:03420247"], "source_form_scope": "Yeast extract
    remains a mixture without a reconstructed internal composition."}, {"owner_field":
    "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[3].term", "id": "CHEBI:17234",
    "asserted_label": "glucose", "canonical_label": "glucose", "label_matches": true,
    "definition": ["An aldohexose used as a source of energy and metabolic intermediate."],
    "source_form_scope": "Glucose is generic; do not add an unstated stereochemical
    or hydrate qualifier."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[4].term",
    "id": "CHEBI:53426", "asserted_label": "polysorbate 80", "canonical_label": "polysorbate
    80", "label_matches": true, "definition": ["A polymer composed of PEG-ylated sorbitan,
    where the total number of poly(ethylene glycol) units is 20 (<em>w</em> + <em>x</em>
    + <em>y</em> + <em>z</em> = 20) and a single terminal is capped by an oleoyl group."],
    "source_form_scope": "Tween 80 is supplied as 1 g, not 1 ml; polysorbate80 class
    mapping does not establish a product lot or density."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[5].term",
    "id": "CHEBI:131527", "asserted_label": "dipotassium hydrogen phosphate", "canonical_label":
    "dipotassium hydrogen phosphate", "label_matches": true, "definition": ["A potassium
    salt that is the dipotassium salt of phosphoric acid."], "source_form_scope":
    "Dipotassium hydrogen phosphate is distinct from monopotassium phosphate."}, {"owner_field":
    "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[6].term", "id": "CHEBI:32954",
    "asserted_label": "sodium acetate", "canonical_label": "sodium acetate", "label_matches":
    true, "definition": [], "source_form_scope": "Sodium acetate has no explicit hydrate
    in the source; no hydrate-specific mass conversion."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[10].term",
    "id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_matches":
    true, "definition": ["An oxygen hydride consisting of an oxygen atom that is covalently
    bonded to two hydrogen atoms"], "source_form_scope": "One liter of water is the
    stated batch input, not a measured final-volume result."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[11].term",
    "id": "CHEBI:2509", "asserted_label": "Agar", "canonical_label": "agar", "label_matches":
    false, "definition": ["A complex mixture of polysaccharides extracted from species
    of red algae. Its two main components are agarose and agaropectin. Agarose is
    the component responsible for the high-strength gelling properties of agar, while
    agaropectin provides the viscous properties."], "source_form_scope": "Agar is
    explicitly optional at 15 g; do not infer mandatory solid culture."}], "history":
    {"target": {"count": 6, "timezone_bearing_timestamps": ["2026-02-20T00:22:35.953837Z",
    "2026-03-13T03:09:26.666003Z", "2026-03-13T06:19:49.239630Z", "2026-03-14T00:00:00+00:00",
    "2026-05-16T09:03:06.694710+00:00", "2026-08-06T03:05:04.676649+00:00"]}, "owner":
    {"count": 8, "timezone_bearing_timestamps": ["2026-02-20T00:22:35.953837Z", "2026-03-13T03:09:26.666003Z",
    "2026-03-13T06:19:49.239630Z", "2026-03-14T00:00:00+00:00", "2026-05-16T09:03:06.694710+00:00",
    "2026-08-19T21:54:22.912825+00:00", "2026-08-20T19:01:16.015082+00:00", "2026-09-07T00:00:00-07:00"]}},
    "owner_reference": [{"reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=366"}],
    "target_reference_count": 0, "owner_narrow_evidence_present": false}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/nbrc_importer.py
  locator: _create_description; _map_ingredients; _infer_physical_state; _map_preparation_steps;
    _determine_category
  accessed_at: '2026-10-21T08:14:05Z'
  support: supports
  summary: Current code maps g/mg/ml to nominal per-liter units, defaults unknown
    units to G_PER_L, infers SOLID_AGAR from any agar substring without optionality
    handling, and synthesizes dissolve/conditional-pH/autoclave steps if preparation
    is empty. The autoclave substring does not match autoclaving, leaving the action
    DISSOLVE. These inspected current rules explain a reproducible failure mode; historical
    execution is not reconstructed.
- evidence_id: scraper
  kind: record_content
  reference: src/culturemech/fetch/nbrc_scraper.py
  locator: _extract_ingredients and _extract_preparation
  accessed_at: '2026-10-21T08:14:05Z'
  support: context_only
  summary: The current extractor scans nested tables and descendant rows/cells, takes
    the first two cells as name/amount, and uses unseparated text extraction. The
    preparation reader looks for a preparation label and a following list. This is
    current context for collapsed tables and missed composition footnotes, not a rerun
    or a claim that no historical fixes occurred.
- evidence_id: recovery
  kind: record_content
  reference: scripts/recover_nbrc_composition.py
  locator: Module explanation; parse_composition; _ingredient; media_number_index
  accessed_at: '2026-10-21T08:14:05Z'
  support: supports
  summary: The inspected recovery implementation distinguishes three-cell ingredient
    rows from one-cell prose, retains supplier/filtering footnotes rather than treating
    them as stock recipes, and maps explicit g/mg/ml/L units. It documents the historical
    table-blob issue and the distinction between record names and provider medium
    numbers. The source table and current owner were independently compared; the script
    was not executed.
- evidence_id: raw-converter
  kind: record_content
  reference: src/culturemech/convert/nbrc_raw_yaml.py
  locator: Module contract and main converter dispatch
  accessed_at: '2026-10-21T08:14:05Z'
  support: context_only
  summary: The NBRC raw-YAML converter dispatches a direct JSON-to-YAML conversion
    without normalization. It is not a maintained scientific curation owner or a remedy
    for damaged source-JSON ingredient structure.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007490
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '0 primary CHEBI identities resolve with matching labels; 0 of 0 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:007490
  evidence_ids:
  - record
  - mim
  details: 2 direct ingredient instances; CHEBI-primary instance linkage 0/2 (0.00%),
    verified secondary coverage 0/2 (0.00%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Exact NBRC366 source and maintained owner
  outcome: supported
  summary: Stable ID CultureMech:007490, the merge contributor NBRC_367.yaml, the
    explicit import-history accession and both live source routes identify NBRC366.
    The official title field is blank; no conventional medium name is invented. Normalized/generated
    appearances of the same stable ID are distinct data layers, not evidence of two
    maintained IDs.
  target_ids:
  - CultureMech:007490
  evidence_ids:
  - record
  - owner-0
  - id-search
  - nbrc
  - legacy
- assessment_id: formulation
  area: quantity
  topic: Every malformed node, recovered quantity and pH claim
  outcome: concern
  summary: Both target ingredient rows need correction. All 12 owner rows preserve
    the corresponding source numerals and supplied chemical/product forms. The water-input
    batch basis, optional agar and any liquid additions remain explicit; there are
    no source stock groups or target stock references to invent. The full field-by-field
    inventory records verified batch facts separately from nominal final-concentration
    interpretations.
  target_ids:
  - CultureMech:007490
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - quantity-inventory
  details: '[{"target_field": "ingredients[0]", "stored_value": {"preferred_term":
    "Peptone10gMeat extract10gYeast extract5gGlucose20gTween 801gK2HPO42gSodium acetate5gDiammonium
    hydrogencitrate2gMgSO4·7H2O0.2gMnSO4·nH2O0.05gDistilled water1LAgar (if needed)15gpH
    5.5", "concentration": {"value": "variable", "unit": "VARIABLE"}}, "decision":
    "correct", "reason": "An entire composition table plus pH/footnotes is not one
    ingredient. VARIABLE conceals explicit source numerals."}, {"target_field": "ingredients[1]",
    "stored_value": {"preferred_term": "", "concentration": {"value": "Peptone", "unit":
    "G_PER_L"}}, "decision": "correct", "reason": "The ingredient name is blank and
    the concentration value is a chemical/product name, not an amount."}, {"owner_field":
    "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[0]", "source_locator":
    "#medium-comp table tr[0]", "source_excerpt": "Peptone 10 g", "source_amount":
    "10", "source_unit": "g", "owner_concentration": {"value": "10", "unit": "G_PER_L"},
    "decision": "evidence_only", "reason": "The owner preserves the source numeral
    and mass/volume unit on a nominal one-liter water-input basis; this is not an
    independently verified final-volume concentration.", "chemical_form_and_scope":
    "Peptone is an undefined mixture; no supplier or digest substrate inferred.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[1]",
    "source_locator": "#medium-comp table tr[1]", "source_excerpt": "Meat extract
    10 g", "source_amount": "10", "source_unit": "g", "owner_concentration": {"value":
    "10", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Meat extract is left as supplied; no unverified substitution by beef extract.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[2]",
    "source_locator": "#medium-comp table tr[2]", "source_excerpt": "Yeast extract
    5 g", "source_amount": "5", "source_unit": "g", "owner_concentration": {"value":
    "5", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Yeast extract remains a mixture without a reconstructed internal composition.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[3]",
    "source_locator": "#medium-comp table tr[3]", "source_excerpt": "Glucose 20 g",
    "source_amount": "20", "source_unit": "g", "owner_concentration": {"value": "20",
    "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Glucose is generic; do not add an unstated stereochemical or hydrate qualifier.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[4]",
    "source_locator": "#medium-comp table tr[4]", "source_excerpt": "Tween 80 1 g",
    "source_amount": "1", "source_unit": "g", "owner_concentration": {"value": "1",
    "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Tween 80 is supplied as 1 g, not 1 ml; polysorbate80 class mapping does not establish
    a product lot or density.", "target_reconstruction": "Replace the malformed target
    rows only after owner verification and separately authorized regeneration."},
    {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[5]",
    "source_locator": "#medium-comp table tr[5]", "source_excerpt": "K 2 HPO 4 2 g",
    "source_amount": "2", "source_unit": "g", "owner_concentration": {"value": "2",
    "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Dipotassium hydrogen phosphate is distinct from monopotassium phosphate.", "target_reconstruction":
    "Replace the malformed target rows only after owner verification and separately
    authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[6]",
    "source_locator": "#medium-comp table tr[6]", "source_excerpt": "Sodium acetate
    5 g", "source_amount": "5", "source_unit": "g", "owner_concentration": {"value":
    "5", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Sodium acetate has no explicit hydrate in the source; no hydrate-specific mass
    conversion.", "target_reconstruction": "Replace the malformed target rows only
    after owner verification and separately authorized regeneration."}, {"owner_field":
    "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[7]", "source_locator":
    "#medium-comp table tr[7]", "source_excerpt": "Diammonium hydrogencitrate 2 g",
    "source_amount": "2", "source_unit": "g", "owner_concentration": {"value": "2",
    "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Diammonium hydrogencitrate must retain its ammonium counterion count and citrate
    protonation.", "target_reconstruction": "Replace the malformed target rows only
    after owner verification and separately authorized regeneration."}, {"owner_field":
    "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[8]", "source_locator":
    "#medium-comp table tr[8]", "source_excerpt": "MgSO 4 ·7H 2 O 0.2 g", "source_amount":
    "0.2", "source_unit": "g", "owner_concentration": {"value": "0.2", "unit": "G_PER_L"},
    "decision": "evidence_only", "reason": "The owner preserves the source numeral
    and mass/volume unit on a nominal one-liter water-input basis; this is not an
    independently verified final-volume concentration.", "chemical_form_and_scope":
    "Magnesium sulfate heptahydrate is explicit.", "target_reconstruction": "Replace
    the malformed target rows only after owner verification and separately authorized
    regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[9]",
    "source_locator": "#medium-comp table tr[9]", "source_excerpt": "MnSO 4 ·nH 2
    O 0.05 g", "source_amount": "0.05", "source_unit": "g", "owner_concentration":
    {"value": "0.05", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The
    owner preserves the source numeral and mass/volume unit on a nominal one-liter
    water-input basis; this is not an independently verified final-volume concentration.",
    "chemical_form_and_scope": "The hydrate number n is unspecified; do not replace
    it by monohydrate or calculate molarity.", "target_reconstruction": "Replace the
    malformed target rows only after owner verification and separately authorized
    regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[10]",
    "source_locator": "#medium-comp table tr[10]", "source_excerpt": "Distilled water
    1 L", "source_amount": "1", "source_unit": "L", "owner_concentration": {"value":
    "1", "unit": "L"}, "decision": "verified", "reason": "The source directly reports
    the one-liter water quantity.", "chemical_form_and_scope": "One liter of water
    is the stated batch input, not a measured final-volume result.", "target_reconstruction":
    "Replace the malformed target rows only after owner verification and separately
    authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[11]",
    "source_locator": "#medium-comp table tr[11]", "source_excerpt": "Agar (if needed)
    15 g", "source_amount": "15", "source_unit": "g", "owner_concentration": {"value":
    "15", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Agar is explicitly optional at 15 g; do not infer mandatory solid culture.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"field": "ph_value", "source_excerpt":
    "pH 5.5", "source_locator": "#medium-comp pH line", "owner_value": 5.5, "target_value":
    null, "decision": "add", "reason": "Source pH is explicit and maintained but absent
    as a structured target value; it remains buried in the ingredient blob."}]'
- assessment_id: freshness
  area: completeness
  topic: Maintained recovery and later source metadata versus generated bytes
  outcome: concern
  summary: The target retains the pre-recovery composition, lacks structured pH, source
    term, source reference and recovered mappings, and ends with the August6 merge
    event. The owner contains August19 recovery, August20 linkage and September source-repair
    events. These are observed content differences; no generator rerun or causal history
    reconstruction was performed.
  target_ids:
  - CultureMech:007490
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - audit-context
  - recovery
- assessment_id: preparation
  area: evidence
  topic: Source-specific protocol versus generated default steps
  outcome: concern
  summary: The official page gives the formula, optional agar and pH5.5 but no preparation
    or sterilization protocol. The maintained owner removes the generic preparation
    list (empty preparation_steps), while the target retains the unsupported fallback
    and labels autoclaving DISSOLVE.
  target_ids:
  - CultureMech:007490
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - importer
  - scraper
  - recovery
- assessment_id: owner-grounding
  area: grounding
  topic: Resolved owner identifiers and exact chemical-form scope
  outcome: concern
  summary: All 8 distinct owner ontology IDs resolve and are non-obsolete; 3 asserted
    labels differ from canonical labels. The quantity inventory separately preserves
    source hydrate, salt, stereochemical and undefined-mixture limits. Canonical label
    resolution alone is not proof of supplied chemical form or preparation. No replacement
    identifiers were invented.
  target_ids:
  - CultureMech:007490
  evidence_ids:
  - owner-0
  - nbrc
  - quantity-inventory
  - audit-context
  - owner-mim
  - owner-chebi131527
  - owner-chebi15377
  - owner-chebi17234
  - owner-chebi2509
  - owner-chebi32954
  - owner-chebi53426
  - owner-foodon03315426
  - owner-micro0000178
  details: '[{"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[0].term",
    "id": "MICRO:0000178", "asserted_label": "Peptone", "canonical_label": "peptone",
    "label_matches": false, "definition": [], "source_form_scope": "Peptone is an
    undefined mixture; no supplier or digest substrate inferred."}, {"owner_field":
    "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[2].term", "id": "FOODON:03315426",
    "asserted_label": "Yeast extract", "canonical_label": "yeast extract", "label_matches":
    false, "definition": ["SIREN DB annotation:\n* not heat-treated FOODON:03440003\n*
    part of algae or fungus FOODON:03420247"], "source_form_scope": "Yeast extract
    remains a mixture without a reconstructed internal composition."}, {"owner_field":
    "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[3].term", "id": "CHEBI:17234",
    "asserted_label": "glucose", "canonical_label": "glucose", "label_matches": true,
    "definition": ["An aldohexose used as a source of energy and metabolic intermediate."],
    "source_form_scope": "Glucose is generic; do not add an unstated stereochemical
    or hydrate qualifier."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[4].term",
    "id": "CHEBI:53426", "asserted_label": "polysorbate 80", "canonical_label": "polysorbate
    80", "label_matches": true, "definition": ["A polymer composed of PEG-ylated sorbitan,
    where the total number of poly(ethylene glycol) units is 20 (<em>w</em> + <em>x</em>
    + <em>y</em> + <em>z</em> = 20) and a single terminal is capped by an oleoyl group."],
    "source_form_scope": "Tween 80 is supplied as 1 g, not 1 ml; polysorbate80 class
    mapping does not establish a product lot or density."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[5].term",
    "id": "CHEBI:131527", "asserted_label": "dipotassium hydrogen phosphate", "canonical_label":
    "dipotassium hydrogen phosphate", "label_matches": true, "definition": ["A potassium
    salt that is the dipotassium salt of phosphoric acid."], "source_form_scope":
    "Dipotassium hydrogen phosphate is distinct from monopotassium phosphate."}, {"owner_field":
    "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[6].term", "id": "CHEBI:32954",
    "asserted_label": "sodium acetate", "canonical_label": "sodium acetate", "label_matches":
    true, "definition": [], "source_form_scope": "Sodium acetate has no explicit hydrate
    in the source; no hydrate-specific mass conversion."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[10].term",
    "id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_matches":
    true, "definition": ["An oxygen hydride consisting of an oxygen atom that is covalently
    bonded to two hydrogen atoms"], "source_form_scope": "One liter of water is the
    stated batch input, not a measured final-volume result."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[11].term",
    "id": "CHEBI:2509", "asserted_label": "Agar", "canonical_label": "agar", "label_matches":
    false, "definition": ["A complex mixture of polysaccharides extracted from species
    of red algae. Its two main components are agarose and agaropectin. Agarose is
    the component responsible for the high-strength gelling properties of agar, while
    agaropectin provides the viscous properties."], "source_form_scope": "Agar is
    explicitly optional at 15 g; do not infer mandatory solid culture."}]'
- assessment_id: mapping-scope
  area: grounding
  topic: Separate malformed-target and recovered-owner linkage denominators
  outcome: concern
  summary: Target primary and secondary linkage are 0/2 (0%) of malformed rows; this
    does not mean two legitimate ingredients were checked. Owner all-ontology primary
    linkage is 8/12 (66.67%), CHEBI linkage is 6/12 (50.00%), and live pinned secondary
    linkage is 0/12 (0.00%). These are 0–100 linkage percentages, not scientific correctness
    scores.
  target_ids:
  - CultureMech:007490
  evidence_ids:
  - record
  - owner-0
  - mim
  - owner-mim
  - audit-context
- assessment_id: classification
  area: scope
  topic: Source classification, optionality and absence of asserted growth claims
  outcome: supported
  summary: The official medium-title field is blank; no MRS name or recipe equivalence
    is inferred. Peptone and extracts support COMPLEX/UNDEFINED. SOLID_AGAR describes
    only the optional agar preparation; preserve the liquid alternative. The target
    and owner assert no target-organism IDs, gene/transcriptomic context, native variants,
    parent links or KG-Microbe match. No organism-specific growth, optimization, incubation
    or strain identity is inferred from a medium title or bacterial filing category.
  target_ids:
  - CultureMech:007490
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - quantity-inventory
- assessment_id: audit
  area: provenance
  topic: History integrity and narrow claim evidence
  outcome: concern
  summary: All six target and eight owner timestamps parse with timezones; the first
    five events agree and later entries remain append-only context. The owner primary
    reference and notes identify the source but contain no narrow ingredient/root
    evidence excerpts. The target reference validator checked zero excerpts. Source
    availability and every amount were checked directly above; a zero-issue result
    did not test them.
  target_ids:
  - CultureMech:007490
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - legacy
  - audit-context
  - validate-references
findings:
- finding_id: f1
  issue_key: CM007490-malformed-generated-formulation
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated formula remains a table blob and an unnamed ingredient
  description: The target has two malformed ingredient objects instead of the 12 source
    rows. One names the complete recipe including pH/footnotes and assigns VARIABLE;
    the other has a blank preferred term and 'Peptone' as a G_PER_L value. This prevents
    faithful machine interpretation despite the four documented checks passing; it
    is a scientific representation blocker, not a P1.1 schema failure.
  target_ids:
  - CultureMech:007490
  field_paths:
  - ingredients[0]
  - ingredients[1]
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - quantity-inventory
  - recovery
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_367.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CM007490-stale-source-ph-grounding
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Maintained source-backed corrections have not reached the target
  description: The owner supplies NBRC366 source metadata, structured pH5.5, recovered
    row identities and later recovery/grounding history missing from the target. Corrected
    composition is tracked in the separate blocker; this finding covers lost identity,
    pH and provenance.
  target_ids:
  - CultureMech:007490
  field_paths:
  - ph_value
  - media_term
  - references
  - ingredients[*].term
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - audit-context
  - recovery
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_367.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: CM007490-unsupported-generated-preparation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generated preparation defaults lack the required source scope
  description: The official page gives the formula, optional agar and pH5.5 but no
    preparation or sterilization protocol. The maintained owner removes the generic
    preparation list (empty preparation_steps), while the target retains the unsupported
    fallback and labels autoclaving DISSOLVE.
  target_ids:
  - CultureMech:007490
  field_paths:
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - importer
  - scraper
  - recovery
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_367.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: CM007490-owner-canonical-labels
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Three maintained-owner labels differ from canonical ontology labels
  description: 'MICRO:0000178: ''Peptone'' versus canonical ''peptone''; FOODON:03315426:
    ''Yeast extract'' versus canonical ''yeast extract''; CHEBI:2509: ''Agar'' versus
    canonical ''agar''. These are case/label discrepancies on resolved identifiers,
    not demonstrated wrong material IDs.'
  target_ids:
  - CultureMech:007490
  field_paths:
  - data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[0].term.label
  - data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[2].term.label
  - data/normalized_yaml/bacterial/NBRC_367.yaml:ingredients[11].term.label
  evidence_ids:
  - owner-0
  - audit-context
  - owner-chebi2509
  - owner-foodon03315426
  - owner-micro0000178
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_367.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: CM007490-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source provenance lacks narrow claim excerpts
  description: The maintained primary reference and notes identify the correct source
    but do not attach exact excerpt evidence to individual amounts, the water-input
    basis, pH or source-specific preparation/optionality. The target lacks the maintained
    reference and its validator checked zero evidence excerpts.
  target_ids:
  - CultureMech:007490
  field_paths:
  - references
  - ingredients[*].evidence
  - evidence
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - quantity-inventory
  - audit-context
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_367.yaml
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
  description: Verify every recovered maintained-owner row and source batch/optionality
    boundary, retain the stable source identity, then regenerate the merged record.
    Do not edit the generated table blob directly.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007490
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_367.yaml
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
  description: Verify owner source metadata and canonical labels, then regenerate
    and confirm that pH, source accession, references, supported mappings and append-only
    history survive. Keep provider accession separate from the local numeric filename.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007490
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_367.yaml
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
  description: Preserve the supported pH5.5 and optional-agar scope; do not reintroduce
    the unsupported importer defaults when regenerating from the maintained owner.
    Add a sterilization or preparation procedure only if an exact source supports
    it.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007490
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_367.yaml
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
  description: Canonicalize maintained-owner term labels while preserving preferred
    source names, IDs, exact material forms and concentration evidence before regeneration.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007490
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_367.yaml
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
  description: Attach short exact excerpts and locators to each maintained ingredient
    amount and other narrow claims using the existing evidence slots. Keep original
    source units and batch conditions distinct from arithmetic or interpretation.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:007490
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_367.yaml
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
- The original historical scrape bytes were not reconstructed. The official pages
  were captured on their recorded access dates; current importer code is evidence
  of present behavior, not proof of the exact historical execution.
- The source table states a 1 L distilled-water input. Its nominal per-liter convention
  is retained without claiming an independently measured final volume after dissolved
  solids or added liquids. No density, hydrate mass, molarity or exact final-volume
  conversion is inferred.
- The maintained owner is context for this one generated target, not a second reviewed
  record. Ontology ID/label resolution and pinned MIM linkage are checked separately
  from source-supported chemical form, product grade and preparation.
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
