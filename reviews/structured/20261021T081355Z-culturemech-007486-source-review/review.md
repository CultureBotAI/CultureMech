# Source and formulation review: 310 (CultureMech:007486)

- Review: 20261021T081355Z-culturemech-007486-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T08:09:09Z
- Finished UTC: 2026-10-21T08:13:55Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated numeric record identifies NBRC309 but still encodes the entire formulation as a concatenated ingredient and a blank ingredient with a chemical name in its concentration. Its maintained owner has recovered 10 source rows, pH and source metadata. These corrections have not reached the target. The current official page supplies the composition and pH 7.0 but no autoclave protocol. All three generic preparation descriptions persist in both target and owner, and the autoclaving description is mislabeled DISSOLVE.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 92; batch 010 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding nine task batches contain 90 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 92 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007486 | data/merge_yaml/merged/310.yaml | generated | 310 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007486 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007486 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch010/092/strict.tsv |
| validate-terms | passed | True | CultureMech:007486 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007486 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007486 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007486.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:007486.

0 primary CHEBI identities resolve with matching labels; 0 of 0 current secondary keys have live pinned-index rows. Unresolved keys: [].

2 direct ingredient instances; CHEBI-primary instance linkage 0/2 (0.00%), verified secondary coverage 0/2 (0.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Exact NBRC309 source and maintained owner

identity: supported. Targets: CultureMech:007486.

Stable ID CultureMech:007486, the merge contributor NBRC_310.yaml, the explicit import-history accession and both live source routes identify NBRC309. The official title is Rhamnose Salt Medium. Normalized/generated appearances of the same stable ID are distinct data layers, not evidence of two maintained IDs.

### Every malformed node, recovered quantity and pH claim

quantity: concern. Targets: CultureMech:007486.

Both target ingredient rows need correction. All 10 owner rows preserve the corresponding source numerals and supplied chemical/product forms. The water-input batch basis, optional agar and any liquid additions remain explicit; there are no source stock groups or target stock references to invent. The full field-by-field inventory records verified batch facts separately from nominal final-concentration interpretations.

[{"target_field": "ingredients[0]", "stored_value": {"preferred_term": "K2HPO42.9gKH2PO42.1gNH4Cl2gMgSO4·7H2O0.4gNaCl30mgCaCl2·2H2O3mgFeSO4·7H2O1mgYeast extract3gRhamnose10gDistilled water1LpH 7.0", "concentration": {"value": "variable", "unit": "VARIABLE"}}, "decision": "correct", "reason": "An entire composition table plus pH/footnotes is not one ingredient. VARIABLE conceals explicit source numerals."}, {"target_field": "ingredients[1]", "stored_value": {"preferred_term": "", "concentration": {"value": "K2HPO4", "unit": "G_PER_L"}}, "decision": "correct", "reason": "The ingredient name is blank and the concentration value is a chemical/product name, not an amount."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[0]", "source_locator": "#medium-comp table tr[0]", "source_excerpt": "K 2 HPO 4 2.9 g", "source_amount": "2.9", "source_unit": "g", "owner_concentration": {"value": "2.9", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Dipotassium hydrogen phosphate; do not replace by monopotassium phosphate.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[1]", "source_locator": "#medium-comp table tr[1]", "source_excerpt": "KH 2 PO 4 2.1 g", "source_amount": "2.1", "source_unit": "g", "owner_concentration": {"value": "2.1", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Potassium dihydrogen phosphate is distinct from the preceding dibasic salt.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[2]", "source_locator": "#medium-comp table tr[2]", "source_excerpt": "NH 4 Cl 2 g", "source_amount": "2", "source_unit": "g", "owner_concentration": {"value": "2", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Ammonium chloride, with no additional hydrate specified.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[3]", "source_locator": "#medium-comp table tr[3]", "source_excerpt": "MgSO 4 ·7H 2 O 0.4 g", "source_amount": "0.4", "source_unit": "g", "owner_concentration": {"value": "0.4", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Heptahydrate is explicit; retain all seven waters.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[4]", "source_locator": "#medium-comp table tr[4]", "source_excerpt": "NaCl 30 mg", "source_amount": "30", "source_unit": "mg", "owner_concentration": {"value": "30", "unit": "MG_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "30 mg is retained as MG_PER_L on the nominal batch basis; no g/mg substitution.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[5]", "source_locator": "#medium-comp table tr[5]", "source_excerpt": "CaCl 2 ·2H 2 O 3 mg", "source_amount": "3", "source_unit": "mg", "owner_concentration": {"value": "3", "unit": "MG_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Dihydrate and 3 mg are explicit; do not use anhydrous mass.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[6]", "source_locator": "#medium-comp table tr[6]", "source_excerpt": "FeSO 4 ·7H 2 O 1 mg", "source_amount": "1", "source_unit": "mg", "owner_concentration": {"value": "1", "unit": "MG_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Iron(II) sulfate heptahydrate and 1 mg are explicit.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[7]", "source_locator": "#medium-comp table tr[7]", "source_excerpt": "Yeast extract 3 g", "source_amount": "3", "source_unit": "g", "owner_concentration": {"value": "3", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Undefined yeast extract; no pure-molecule identity or product grade inferred.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[8]", "source_locator": "#medium-comp table tr[8]", "source_excerpt": "Rhamnose 10 g", "source_amount": "10", "source_unit": "g", "owner_concentration": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Rhamnose without a stated enantiomer or hydrate; no stereochemical refinement.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[9]", "source_locator": "#medium-comp table tr[9]", "source_excerpt": "Distilled water 1 L", "source_amount": "1", "source_unit": "L", "owner_concentration": {"value": "1", "unit": "L"}, "decision": "verified", "reason": "The source directly reports the one-liter water quantity.", "chemical_form_and_scope": "One liter of distilled water is a batch input, not a measurement of final volume after solutes.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"field": "ph_value", "source_excerpt": "pH 7.0", "source_locator": "#medium-comp pH line", "owner_value": 7.0, "target_value": null, "decision": "add", "reason": "Source pH is explicit and maintained but absent as a structured target value; it remains buried in the ingredient blob."}]

### Maintained recovery and later source metadata versus generated bytes

completeness: concern. Targets: CultureMech:007486.

The target retains the pre-recovery composition, lacks structured pH, source term, source reference and recovered mappings, and ends with the August6 merge event. The owner contains August19 recovery, August20 linkage and September source-repair events. These are observed content differences; no generator rerun or causal history reconstruction was performed.

### Source-specific protocol versus generated default steps

evidence: concern. Targets: CultureMech:007486.

The current official page supplies the composition and pH 7.0 but no autoclave protocol. All three generic preparation descriptions persist in both target and owner, and the autoclaving description is mislabeled DISSOLVE.

### Resolved owner identifiers and exact chemical-form scope

grounding: supported. Targets: CultureMech:007486.

All 9 distinct owner ontology IDs resolve and are non-obsolete; 0 asserted labels differ from canonical labels. The quantity inventory separately preserves source hydrate, salt, stereochemical and undefined-mixture limits. Canonical label resolution alone is not proof of supplied chemical form or preparation. No replacement identifiers were invented.

[{"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[0].term", "id": "CHEBI:131527", "asserted_label": "dipotassium hydrogen phosphate", "canonical_label": "dipotassium hydrogen phosphate", "label_matches": true, "definition": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "source_form_scope": "Dipotassium hydrogen phosphate; do not replace by monopotassium phosphate."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[0].mediaingredientmech_chebi_term", "id": "CHEBI:131527", "asserted_label": "dipotassium hydrogen phosphate", "canonical_label": "dipotassium hydrogen phosphate", "label_matches": true, "definition": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "source_form_scope": "Dipotassium hydrogen phosphate; do not replace by monopotassium phosphate."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[1].term", "id": "CHEBI:63036", "asserted_label": "potassium dihydrogen phosphate", "canonical_label": "potassium dihydrogen phosphate", "label_matches": true, "definition": ["A potassium salt in which dihydrogen phosphate(1−) is the counterion."], "source_form_scope": "Potassium dihydrogen phosphate is distinct from the preceding dibasic salt."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[1].mediaingredientmech_chebi_term", "id": "CHEBI:63036", "asserted_label": "potassium dihydrogen phosphate", "canonical_label": "potassium dihydrogen phosphate", "label_matches": true, "definition": ["A potassium salt in which dihydrogen phosphate(1−) is the counterion."], "source_form_scope": "Potassium dihydrogen phosphate is distinct from the preceding dibasic salt."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[2].term", "id": "CHEBI:31206", "asserted_label": "ammonium chloride", "canonical_label": "ammonium chloride", "label_matches": true, "definition": ["An inorganic chloride having ammonium as the counterion."], "source_form_scope": "Ammonium chloride, with no additional hydrate specified."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[2].mediaingredientmech_chebi_term", "id": "CHEBI:31206", "asserted_label": "ammonium chloride", "canonical_label": "ammonium chloride", "label_matches": true, "definition": ["An inorganic chloride having ammonium as the counterion."], "source_form_scope": "Ammonium chloride, with no additional hydrate specified."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[3].term", "id": "CHEBI:31795", "asserted_label": "magnesium sulfate heptahydrate", "canonical_label": "magnesium sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "source_form_scope": "Heptahydrate is explicit; retain all seven waters."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[3].mediaingredientmech_chebi_term", "id": "CHEBI:31795", "asserted_label": "magnesium sulfate heptahydrate", "canonical_label": "magnesium sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "source_form_scope": "Heptahydrate is explicit; retain all seven waters."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[4].term", "id": "CHEBI:26710", "asserted_label": "sodium chloride", "canonical_label": "sodium chloride", "label_matches": true, "definition": ["An inorganic chloride salt having sodium(1+) as the counterion."], "source_form_scope": "30 mg is retained as MG_PER_L on the nominal batch basis; no g/mg substitution."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[4].mediaingredientmech_chebi_term", "id": "CHEBI:26710", "asserted_label": "sodium chloride", "canonical_label": "sodium chloride", "label_matches": true, "definition": ["An inorganic chloride salt having sodium(1+) as the counterion."], "source_form_scope": "30 mg is retained as MG_PER_L on the nominal batch basis; no g/mg substitution."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[5].term", "id": "CHEBI:86158", "asserted_label": "calcium chloride dihydrate", "canonical_label": "calcium chloride dihydrate", "label_matches": true, "definition": ["A hydrate that is the dihydrate form of calcium chloride."], "source_form_scope": "Dihydrate and 3 mg are explicit; do not use anhydrous mass."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[5].mediaingredientmech_chebi_term", "id": "CHEBI:86158", "asserted_label": "calcium chloride dihydrate", "canonical_label": "calcium chloride dihydrate", "label_matches": true, "definition": ["A hydrate that is the dihydrate form of calcium chloride."], "source_form_scope": "Dihydrate and 3 mg are explicit; do not use anhydrous mass."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[6].term", "id": "CHEBI:75836", "asserted_label": "iron(2+) sulfate heptahydrate", "canonical_label": "iron(2+) sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used)."], "source_form_scope": "Iron(II) sulfate heptahydrate and 1 mg are explicit."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[6].mediaingredientmech_chebi_term", "id": "CHEBI:75836", "asserted_label": "iron(2+) sulfate heptahydrate", "canonical_label": "iron(2+) sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used)."], "source_form_scope": "Iron(II) sulfate heptahydrate and 1 mg are explicit."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[8].term", "id": "CHEBI:26546", "asserted_label": "rhamnose", "canonical_label": "rhamnose", "label_matches": true, "definition": ["A deoxymannose sugar that is the 6-deoxy derivative of hexose."], "source_form_scope": "Rhamnose without a stated enantiomer or hydrate; no stereochemical refinement."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[8].mediaingredientmech_chebi_term", "id": "CHEBI:26546", "asserted_label": "rhamnose", "canonical_label": "rhamnose", "label_matches": true, "definition": ["A deoxymannose sugar that is the 6-deoxy derivative of hexose."], "source_form_scope": "Rhamnose without a stated enantiomer or hydrate; no stereochemical refinement."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[9].term", "id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_matches": true, "definition": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "source_form_scope": "One liter of distilled water is a batch input, not a measurement of final volume after solutes."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[9].mediaingredientmech_chebi_term", "id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_matches": true, "definition": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "source_form_scope": "One liter of distilled water is a batch input, not a measurement of final volume after solutes."}]

### Separate malformed-target and recovered-owner linkage denominators

grounding: concern. Targets: CultureMech:007486.

Target primary and secondary linkage are 0/2 (0%) of malformed rows; this does not mean two legitimate ingredients were checked. Owner all-ontology primary linkage is 9/10 (90.00%), CHEBI linkage is 9/10 (90.00%), and live pinned secondary linkage is 9/10 (90.00%). These are 0–100 linkage percentages, not scientific correctness scores.

### Source classification, optionality and absence of asserted growth claims

scope: supported. Targets: CultureMech:007486.

LIQUID is compatible with the source table, which has no agar row. Yeast extract makes COMPLEX/UNDEFINED appropriate despite the salt-based title. Rhamnose Salt Medium is the official title; the numeric filename310 is not NBRC accession310. The target and owner assert no target-organism IDs, gene/transcriptomic context, native variants, parent links or KG-Microbe match. No organism-specific growth, optimization, incubation or strain identity is inferred from a medium title or bacterial filing category.

### History integrity and narrow claim evidence

provenance: concern. Targets: CultureMech:007486.

All six target and eight owner timestamps parse with timezones; the first five events agree and later entries remain append-only context. The owner primary reference and notes identify the source but contain no narrow ingredient/root evidence excerpts. The target reference validator checked zero excerpts. Source availability and every amount were checked directly above; a zero-issue result did not test them.

## Findings

### f1: Generated formula remains a table blob and an unnamed ingredient

blocker / open / confirmed; issue key: CM007486-malformed-generated-formulation.

The target has two malformed ingredient objects instead of the 10 source rows. One names the complete recipe including pH/footnotes and assigns VARIABLE; the other has a blank preferred term and 'K2HPO4' as a G_PER_L value. This prevents faithful machine interpretation despite the four documented checks passing; it is a scientific representation blocker, not a P1.1 schema failure.

### f2: Maintained source-backed corrections have not reached the target

major / open / confirmed; issue key: CM007486-stale-source-ph-grounding.

The owner supplies NBRC309 source metadata, structured pH7.0, recovered row identities and later recovery/grounding history missing from the target. Corrected composition is tracked in the separate blocker; this finding covers lost identity, pH and provenance. The official Rhamnose Salt Medium name is also missing.

### f3: Generated preparation defaults lack the required source scope

major / open / confirmed; issue key: CM007486-unsupported-generated-preparation.

The current official page supplies the composition and pH 7.0 but no autoclave protocol. All three generic preparation descriptions persist in both target and owner, and the autoclaving description is mislabeled DISSOLVE.

### f4: Source provenance lacks narrow claim excerpts

minor / open / confirmed; issue key: CM007486-claim-evidence-gap.

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

Reassess the maintained owner preparation against the exact NBRC309 source; remove or explicitly qualify unsupported defaults, preserve source pH7.0, and use the correct action for any later source-supported sterilization step before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach short exact excerpts and locators to each maintained ingredient amount and other narrow claims using the existing evidence slots. Keep original source units and batch conditions distinct from arithmetic or interpretation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/310.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_310.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/310.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/310.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch010/092/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch010/092/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/310.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/310.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/310.yaml:1:id: CultureMech:007486<br>./data/normalized_yaml/bacterial/NBRC_310.yaml:1:id: CultureMech:007486<br> |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {} |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=309; Medium No.; Medium title; #medium-comp nested composition table, pH, footnotes and Comment | supports | The complete official NBRC309 medium page was read: all 10 composition rows, pH7.0, optionality and any footnotes. LIQUID is compatible with the source table, which has no agar row. Yeast extract makes COMPLEX/UNDEFINED appropriate despite the salt-based title. Rhamnose Salt Medium is the official title; the numeric filename310 is not NBRC accession310. |
| legacy | http://www.nbrc.nite.go.jp/NBRC2/NBRCMediumDetailServlet?NO=309; Historical HTTP servlet redirect; Medium No.; full medium detail | supports | The exact historical servlet URL in the import event resolves to the current NBRC309 record. Preserve the request URL, resolved URL, original timestamp and response hash; the local numeric filename is not the provider accession. |
| owner-chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier CHEBI:131527 resolves to canonical label 'dipotassium hydrogen phosphate', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier CHEBI:63036 resolves to canonical label 'potassium dihydrogen phosphate', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier CHEBI:31206 resolves to canonical label 'ammonium chloride', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier CHEBI:31795 resolves to canonical label 'magnesium sulfate heptahydrate', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier CHEBI:26710 resolves to canonical label 'sodium chloride', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier CHEBI:86158 resolves to canonical label 'calcium chloride dihydrate', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier CHEBI:75836 resolves to canonical label 'iron(2+) sulfate heptahydrate', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-chebi26546 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26546; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier CHEBI:26546 resolves to canonical label 'rhamnose', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id, label, description, is_obsolete | context_only | Exact owner identifier CHEBI:15377 resolves to canonical label 'water', is not obsolete, and has the captured definition. This response verifies identifier/label correspondence; source material, hydrate, stereochemistry and product scope are assessed separately in the quantity inventory. |
| owner-mim | src/culturemech/data/mediaingredientmech/label_index.csv; All pinned live preferred-term rows for current owner secondary identifiers; adjacent snapshot metadata captured | context_only | {"secondary_identifier_instances": ["CHEBI:131527", "CHEBI:63036", "CHEBI:31206", "CHEBI:31795", "CHEBI:26710", "CHEBI:86158", "CHEBI:75836", "CHEBI:26546", "CHEBI:15377"], "matching_rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26546": [{"label": "Rhamnose", "match_type": "preferred_term", "identifier": "CHEBI:26546", "preferred_term": "Rhamnose", "ontology_id": "CHEBI:26546", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "limit": "A key/alias match is linkage evidence, not proof that every alias has the correct chemical form. The source and canonical term separately establish any hydrate correspondence."} |
| quantity-inventory | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=309; Every source table row, pH line, both target ingredient nodes, and exact owner field paths | supports | [{"target_field": "ingredients[0]", "stored_value": {"preferred_term": "K2HPO42.9gKH2PO42.1gNH4Cl2gMgSO4·7H2O0.4gNaCl30mgCaCl2·2H2O3mgFeSO4·7H2O1mgYeast extract3gRhamnose10gDistilled water1LpH 7.0", "concentration": {"value": "variable", "unit": "VARIABLE"}}, "decision": "correct", "reason": "An entire composition table plus pH/footnotes is not one ingredient. VARIABLE conceals explicit source numerals."}, {"target_field": "ingredients[1]", "stored_value": {"preferred_term": "", "concentration": {"value": "K2HPO4", "unit": "G_PER_L"}}, "decision": "correct", "reason": "The ingredient name is blank and the concentration value is a chemical/product name, not an amount."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[0]", "source_locator": "#medium-comp table tr[0]", "source_excerpt": "K 2 HPO 4 2.9 g", "source_amount": "2.9", "source_unit": "g", "owner_concentration": {"value": "2.9", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Dipotassium hydrogen phosphate; do not replace by monopotassium phosphate.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[1]", "source_locator": "#medium-comp table tr[1]", "source_excerpt": "KH 2 PO 4 2.1 g", "source_amount": "2.1", "source_unit": "g", "owner_concentration": {"value": "2.1", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Potassium dihydrogen phosphate is distinct from the preceding dibasic salt.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[2]", "source_locator": "#medium-comp table tr[2]", "source_excerpt": "NH 4 Cl 2 g", "source_amount": "2", "source_unit": "g", "owner_concentration": {"value": "2", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Ammonium chloride, with no additional hydrate specified.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[3]", "source_locator": "#medium-comp table tr[3]", "source_excerpt": "MgSO 4 ·7H 2 O 0.4 g", "source_amount": "0.4", "source_unit": "g", "owner_concentration": {"value": "0.4", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Heptahydrate is explicit; retain all seven waters.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[4]", "source_locator": "#medium-comp table tr[4]", "source_excerpt": "NaCl 30 mg", "source_amount": "30", "source_unit": "mg", "owner_concentration": {"value": "30", "unit": "MG_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "30 mg is retained as MG_PER_L on the nominal batch basis; no g/mg substitution.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[5]", "source_locator": "#medium-comp table tr[5]", "source_excerpt": "CaCl 2 ·2H 2 O 3 mg", "source_amount": "3", "source_unit": "mg", "owner_concentration": {"value": "3", "unit": "MG_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Dihydrate and 3 mg are explicit; do not use anhydrous mass.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[6]", "source_locator": "#medium-comp table tr[6]", "source_excerpt": "FeSO 4 ·7H 2 O 1 mg", "source_amount": "1", "source_unit": "mg", "owner_concentration": {"value": "1", "unit": "MG_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Iron(II) sulfate heptahydrate and 1 mg are explicit.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[7]", "source_locator": "#medium-comp table tr[7]", "source_excerpt": "Yeast extract 3 g", "source_amount": "3", "source_unit": "g", "owner_concentration": {"value": "3", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Undefined yeast extract; no pure-molecule identity or product grade inferred.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[8]", "source_locator": "#medium-comp table tr[8]", "source_excerpt": "Rhamnose 10 g", "source_amount": "10", "source_unit": "g", "owner_concentration": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves the source numeral and mass/volume unit on a nominal one-liter water-input basis; this is not an independently verified final-volume concentration.", "chemical_form_and_scope": "Rhamnose without a stated enantiomer or hydrate; no stereochemical refinement.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[9]", "source_locator": "#medium-comp table tr[9]", "source_excerpt": "Distilled water 1 L", "source_amount": "1", "source_unit": "L", "owner_concentration": {"value": "1", "unit": "L"}, "decision": "verified", "reason": "The source directly reports the one-liter water quantity.", "chemical_form_and_scope": "One liter of distilled water is a batch input, not a measurement of final volume after solutes.", "target_reconstruction": "Replace the malformed target rows only after owner verification and separately authorized regeneration."}, {"field": "ph_value", "source_excerpt": "pH 7.0", "source_locator": "#medium-comp pH line", "owner_value": 7.0, "target_value": null, "decision": "add", "reason": "Source pH is explicit and maintained but absent as a structured target value; it remains buried in the ingredient blob."}] |
| audit-context | data/normalized_yaml/bacterial/NBRC_310.yaml; Entire owner versus generated record; all term labels, source references, later history and timezone fields | context_only | {"owner_identifier_checks": [{"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[0].term", "id": "CHEBI:131527", "asserted_label": "dipotassium hydrogen phosphate", "canonical_label": "dipotassium hydrogen phosphate", "label_matches": true, "definition": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "source_form_scope": "Dipotassium hydrogen phosphate; do not replace by monopotassium phosphate."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[0].mediaingredientmech_chebi_term", "id": "CHEBI:131527", "asserted_label": "dipotassium hydrogen phosphate", "canonical_label": "dipotassium hydrogen phosphate", "label_matches": true, "definition": ["A potassium salt that is the dipotassium salt of phosphoric acid."], "source_form_scope": "Dipotassium hydrogen phosphate; do not replace by monopotassium phosphate."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[1].term", "id": "CHEBI:63036", "asserted_label": "potassium dihydrogen phosphate", "canonical_label": "potassium dihydrogen phosphate", "label_matches": true, "definition": ["A potassium salt in which dihydrogen phosphate(1−) is the counterion."], "source_form_scope": "Potassium dihydrogen phosphate is distinct from the preceding dibasic salt."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[1].mediaingredientmech_chebi_term", "id": "CHEBI:63036", "asserted_label": "potassium dihydrogen phosphate", "canonical_label": "potassium dihydrogen phosphate", "label_matches": true, "definition": ["A potassium salt in which dihydrogen phosphate(1−) is the counterion."], "source_form_scope": "Potassium dihydrogen phosphate is distinct from the preceding dibasic salt."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[2].term", "id": "CHEBI:31206", "asserted_label": "ammonium chloride", "canonical_label": "ammonium chloride", "label_matches": true, "definition": ["An inorganic chloride having ammonium as the counterion."], "source_form_scope": "Ammonium chloride, with no additional hydrate specified."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[2].mediaingredientmech_chebi_term", "id": "CHEBI:31206", "asserted_label": "ammonium chloride", "canonical_label": "ammonium chloride", "label_matches": true, "definition": ["An inorganic chloride having ammonium as the counterion."], "source_form_scope": "Ammonium chloride, with no additional hydrate specified."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[3].term", "id": "CHEBI:31795", "asserted_label": "magnesium sulfate heptahydrate", "canonical_label": "magnesium sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "source_form_scope": "Heptahydrate is explicit; retain all seven waters."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[3].mediaingredientmech_chebi_term", "id": "CHEBI:31795", "asserted_label": "magnesium sulfate heptahydrate", "canonical_label": "magnesium sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate that is the heptahydrate form of magnesium sulfate."], "source_form_scope": "Heptahydrate is explicit; retain all seven waters."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[4].term", "id": "CHEBI:26710", "asserted_label": "sodium chloride", "canonical_label": "sodium chloride", "label_matches": true, "definition": ["An inorganic chloride salt having sodium(1+) as the counterion."], "source_form_scope": "30 mg is retained as MG_PER_L on the nominal batch basis; no g/mg substitution."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[4].mediaingredientmech_chebi_term", "id": "CHEBI:26710", "asserted_label": "sodium chloride", "canonical_label": "sodium chloride", "label_matches": true, "definition": ["An inorganic chloride salt having sodium(1+) as the counterion."], "source_form_scope": "30 mg is retained as MG_PER_L on the nominal batch basis; no g/mg substitution."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[5].term", "id": "CHEBI:86158", "asserted_label": "calcium chloride dihydrate", "canonical_label": "calcium chloride dihydrate", "label_matches": true, "definition": ["A hydrate that is the dihydrate form of calcium chloride."], "source_form_scope": "Dihydrate and 3 mg are explicit; do not use anhydrous mass."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[5].mediaingredientmech_chebi_term", "id": "CHEBI:86158", "asserted_label": "calcium chloride dihydrate", "canonical_label": "calcium chloride dihydrate", "label_matches": true, "definition": ["A hydrate that is the dihydrate form of calcium chloride."], "source_form_scope": "Dihydrate and 3 mg are explicit; do not use anhydrous mass."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[6].term", "id": "CHEBI:75836", "asserted_label": "iron(2+) sulfate heptahydrate", "canonical_label": "iron(2+) sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used)."], "source_form_scope": "Iron(II) sulfate heptahydrate and 1 mg are explicit."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[6].mediaingredientmech_chebi_term", "id": "CHEBI:75836", "asserted_label": "iron(2+) sulfate heptahydrate", "canonical_label": "iron(2+) sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used)."], "source_form_scope": "Iron(II) sulfate heptahydrate and 1 mg are explicit."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[8].term", "id": "CHEBI:26546", "asserted_label": "rhamnose", "canonical_label": "rhamnose", "label_matches": true, "definition": ["A deoxymannose sugar that is the 6-deoxy derivative of hexose."], "source_form_scope": "Rhamnose without a stated enantiomer or hydrate; no stereochemical refinement."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[8].mediaingredientmech_chebi_term", "id": "CHEBI:26546", "asserted_label": "rhamnose", "canonical_label": "rhamnose", "label_matches": true, "definition": ["A deoxymannose sugar that is the 6-deoxy derivative of hexose."], "source_form_scope": "Rhamnose without a stated enantiomer or hydrate; no stereochemical refinement."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[9].term", "id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_matches": true, "definition": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "source_form_scope": "One liter of distilled water is a batch input, not a measurement of final volume after solutes."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[9].mediaingredientmech_chebi_term", "id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_matches": true, "definition": ["An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms"], "source_form_scope": "One liter of distilled water is a batch input, not a measurement of final volume after solutes."}], "history": {"target": {"count": 6, "timezone_bearing_timestamps": ["2026-02-20T00:22:35.948677Z", "2026-03-13T03:09:22.615369Z", "2026-03-13T06:19:49.228531Z", "2026-03-14T00:00:00+00:00", "2026-05-16T09:03:06.682530+00:00", "2026-08-06T03:05:04.669493+00:00"]}, "owner": {"count": 8, "timezone_bearing_timestamps": ["2026-02-20T00:22:35.948677Z", "2026-03-13T03:09:22.615369Z", "2026-03-13T06:19:49.228531Z", "2026-03-14T00:00:00+00:00", "2026-05-16T09:03:06.682530+00:00", "2026-08-19T21:54:22.877838+00:00", "2026-08-20T19:01:15.980273+00:00", "2026-09-11T00:00:00-07:00"]}}, "owner_reference": [{"reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=309"}], "target_reference_count": 0, "owner_narrow_evidence_present": false} |
| importer | src/culturemech/import/nbrc_importer.py; _create_description; _map_ingredients; _infer_physical_state; _map_preparation_steps; _determine_category | supports | Current code maps g/mg/ml to nominal per-liter units, defaults unknown units to G_PER_L, infers SOLID_AGAR from any agar substring without optionality handling, and synthesizes dissolve/conditional-pH/autoclave steps if preparation is empty. The autoclave substring does not match autoclaving, leaving the action DISSOLVE. These inspected current rules explain a reproducible failure mode; historical execution is not reconstructed. |
| scraper | src/culturemech/fetch/nbrc_scraper.py; _extract_ingredients and _extract_preparation | context_only | The current extractor scans nested tables and descendant rows/cells, takes the first two cells as name/amount, and uses unseparated text extraction. The preparation reader looks for a preparation label and a following list. This is current context for collapsed tables and missed composition footnotes, not a rerun or a claim that no historical fixes occurred. |
| recovery | scripts/recover_nbrc_composition.py; Module explanation; parse_composition; _ingredient; media_number_index | supports | The inspected recovery implementation distinguishes three-cell ingredient rows from one-cell prose, retains supplier/filtering footnotes rather than treating them as stock recipes, and maps explicit g/mg/ml/L units. It documents the historical table-blob issue and the distinction between record names and provider medium numbers. The source table and current owner were independently compared; the script was not executed. |
| raw-converter | src/culturemech/convert/nbrc_raw_yaml.py; Module contract and main converter dispatch | context_only | The NBRC raw-YAML converter dispatches a direct JSON-to-YAML conversion without normalization. It is not a maintained scientific curation owner or a remedy for damaged source-JSON ingredient structure. |
| owner-repair | scripts/repair_nbrc_310_score15.py; TARGET_ID/URL/title; imported ingredient signature; grounding table; repair_document | supports | The current bounded repair pins CultureMech007486 to NBRC309, its exact ten recovered rows, official title, pH7.0, nine ingredient identifiers and primary reference. It adds source metadata and history while leaving generic preparation intact. The code was read, not executed. |

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
review_id: 20261021T081355Z-culturemech-007486-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 310 (CultureMech:007486)'
started_at: '2026-10-21T08:09:09Z'
finished_at: '2026-10-21T08:13:55Z'
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
summary: The generated numeric record identifies NBRC309 but still encodes the entire
  formulation as a concatenated ingredient and a blank ingredient with a chemical
  name in its concentration. Its maintained owner has recovered 10 source rows, pH
  and source metadata. These corrections have not reached the target. The current
  official page supplies the composition and pH 7.0 but no autoclave protocol. All
  three generic preparation descriptions persist in both target and owner, and the
  autoclaving description is mislabeled DISSOLVE.
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
  - path: data/merge_yaml/merged/310.yaml
    sha256: 37443c4c053e2f0ea7f41afde4bd50b12a06f77a1e55d51a643c50364742ef65
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_310.yaml
    sha256: 0693675bde9601f81bb00881b2a14cba4089b16d60d25014610d03f03af21b2e
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
  - path: scripts/repair_nbrc_310_score15.py
    sha256: 5b0a919ffad07f7bf26cfa08579bb69cdd35450c6ca945f204604b3b5c087074
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
  selection: Task review 92; batch 010 item 2 of 10, selected in Python lexicographic
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
  - CultureMech:007486
targets:
- target_id: CultureMech:007486
  path: data/merge_yaml/merged/310.yaml
  label: '310'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_310.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/310.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007486
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/310.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch010/092/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch010/092/strict.tsv"
  target_ids:
  - CultureMech:007486
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/310.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007486
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/310.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007486
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
  - CultureMech:007486
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/310.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T08:13:54Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_310.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T08:13:54Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/310.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:10:00.779562Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/310.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch010/092/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T08:10:02.484489Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-010/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch010/092/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/310.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:10:04.435858Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/310.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:10:05.556750Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T08:13:54Z'
  support: supports
  summary: './data/merge_yaml/merged/310.yaml:1:id: CultureMech:007486

    ./data/normalized_yaml/bacterial/NBRC_310.yaml:1:id: CultureMech:007486

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T08:13:54Z'
  support: supports
  summary: '{}'
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=309
  locator: 'Medium No.; Medium title; #medium-comp nested composition table, pH, footnotes
    and Comment'
  accessed_at: '2026-10-21T08:00:49.511364Z'
  support: supports
  summary: 'The complete official NBRC309 medium page was read: all 10 composition
    rows, pH7.0, optionality and any footnotes. LIQUID is compatible with the source
    table, which has no agar row. Yeast extract makes COMPLEX/UNDEFINED appropriate
    despite the salt-based title. Rhamnose Salt Medium is the official title; the
    numeric filename310 is not NBRC accession310.'
  quote: pH 7.0
  snapshot_sha256: 26b883887f94cc6c4946f092fa016251eb6c2a7fbaaddb83d9e1a80b27941ad8
- evidence_id: legacy
  kind: primary_source
  reference: http://www.nbrc.nite.go.jp/NBRC2/NBRCMediumDetailServlet?NO=309
  locator: Historical HTTP servlet redirect; Medium No.; full medium detail
  accessed_at: '2026-10-21T08:00:45.621636Z'
  support: supports
  summary: The exact historical servlet URL in the import event resolves to the current
    NBRC309 record. Preserve the request URL, resolved URL, original timestamp and
    response hash; the local numeric filename is not the provider accession.
  snapshot_sha256: 26b883887f94cc6c4946f092fa016251eb6c2a7fbaaddb83d9e1a80b27941ad8
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
- evidence_id: owner-chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: '$._embedded.terms[0]: obo_id, label, description, is_obsolete'
  accessed_at: '2026-10-21T08:00:48.758019Z'
  support: context_only
  summary: Exact owner identifier CHEBI:63036 resolves to canonical label 'potassium
    dihydrogen phosphate', is not obsolete, and has the captured definition. This
    response verifies identifier/label correspondence; source material, hydrate, stereochemistry
    and product scope are assessed separately in the quantity inventory.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: owner-chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: '$._embedded.terms[0]: obo_id, label, description, is_obsolete'
  accessed_at: '2026-10-21T08:00:48.109537Z'
  support: context_only
  summary: Exact owner identifier CHEBI:31206 resolves to canonical label 'ammonium
    chloride', is not obsolete, and has the captured definition. This response verifies
    identifier/label correspondence; source material, hydrate, stereochemistry and
    product scope are assessed separately in the quantity inventory.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: owner-chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: '$._embedded.terms[0]: obo_id, label, description, is_obsolete'
  accessed_at: '2026-10-21T08:00:48.145370Z'
  support: context_only
  summary: Exact owner identifier CHEBI:31795 resolves to canonical label 'magnesium
    sulfate heptahydrate', is not obsolete, and has the captured definition. This
    response verifies identifier/label correspondence; source material, hydrate, stereochemistry
    and product scope are assessed separately in the quantity inventory.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: owner-chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: '$._embedded.terms[0]: obo_id, label, description, is_obsolete'
  accessed_at: '2026-10-21T08:00:48.036367Z'
  support: context_only
  summary: Exact owner identifier CHEBI:26710 resolves to canonical label 'sodium
    chloride', is not obsolete, and has the captured definition. This response verifies
    identifier/label correspondence; source material, hydrate, stereochemistry and
    product scope are assessed separately in the quantity inventory.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: owner-chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: '$._embedded.terms[0]: obo_id, label, description, is_obsolete'
  accessed_at: '2026-10-21T08:00:48.898092Z'
  support: context_only
  summary: Exact owner identifier CHEBI:86158 resolves to canonical label 'calcium
    chloride dihydrate', is not obsolete, and has the captured definition. This response
    verifies identifier/label correspondence; source material, hydrate, stereochemistry
    and product scope are assessed separately in the quantity inventory.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: owner-chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: '$._embedded.terms[0]: obo_id, label, description, is_obsolete'
  accessed_at: '2026-10-21T08:00:48.784931Z'
  support: context_only
  summary: Exact owner identifier CHEBI:75836 resolves to canonical label 'iron(2+)
    sulfate heptahydrate', is not obsolete, and has the captured definition. This
    response verifies identifier/label correspondence; source material, hydrate, stereochemistry
    and product scope are assessed separately in the quantity inventory.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: owner-chebi26546
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26546
  locator: '$._embedded.terms[0]: obo_id, label, description, is_obsolete'
  accessed_at: '2026-10-21T08:00:47.591756Z'
  support: context_only
  summary: Exact owner identifier CHEBI:26546 resolves to canonical label 'rhamnose',
    is not obsolete, and has the captured definition. This response verifies identifier/label
    correspondence; source material, hydrate, stereochemistry and product scope are
    assessed separately in the quantity inventory.
  snapshot_sha256: 385728d1b3702a7c7e884962cd9c4041965ba8431c1fe2b3966f65b7c4c6180d
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
- evidence_id: owner-mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All pinned live preferred-term rows for current owner secondary identifiers;
    adjacent snapshot metadata captured
  accessed_at: '2026-10-21T08:13:54Z'
  support: context_only
  summary: '{"secondary_identifier_instances": ["CHEBI:131527", "CHEBI:63036", "CHEBI:31206",
    "CHEBI:31795", "CHEBI:26710", "CHEBI:86158", "CHEBI:75836", "CHEBI:26546", "CHEBI:15377"],
    "matching_rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label":
    "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O",
    "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26546": [{"label":
    "Rhamnose", "match_type": "preferred_term", "identifier": "CHEBI:26546", "preferred_term":
    "Rhamnose", "ontology_id": "CHEBI:26546", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "limit":
    "A key/alias match is linkage evidence, not proof that every alias has the correct
    chemical form. The source and canonical term separately establish any hydrate
    correspondence."}'
- evidence_id: quantity-inventory
  kind: record_content
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=309
  locator: Every source table row, pH line, both target ingredient nodes, and exact
    owner field paths
  accessed_at: '2026-10-21T08:13:54Z'
  support: supports
  summary: '[{"target_field": "ingredients[0]", "stored_value": {"preferred_term":
    "K2HPO42.9gKH2PO42.1gNH4Cl2gMgSO4·7H2O0.4gNaCl30mgCaCl2·2H2O3mgFeSO4·7H2O1mgYeast
    extract3gRhamnose10gDistilled water1LpH 7.0", "concentration": {"value": "variable",
    "unit": "VARIABLE"}}, "decision": "correct", "reason": "An entire composition
    table plus pH/footnotes is not one ingredient. VARIABLE conceals explicit source
    numerals."}, {"target_field": "ingredients[1]", "stored_value": {"preferred_term":
    "", "concentration": {"value": "K2HPO4", "unit": "G_PER_L"}}, "decision": "correct",
    "reason": "The ingredient name is blank and the concentration value is a chemical/product
    name, not an amount."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[0]",
    "source_locator": "#medium-comp table tr[0]", "source_excerpt": "K 2 HPO 4 2.9
    g", "source_amount": "2.9", "source_unit": "g", "owner_concentration": {"value":
    "2.9", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Dipotassium hydrogen phosphate; do not replace by monopotassium phosphate.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[1]",
    "source_locator": "#medium-comp table tr[1]", "source_excerpt": "KH 2 PO 4 2.1
    g", "source_amount": "2.1", "source_unit": "g", "owner_concentration": {"value":
    "2.1", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Potassium dihydrogen phosphate is distinct from the preceding dibasic salt.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[2]",
    "source_locator": "#medium-comp table tr[2]", "source_excerpt": "NH 4 Cl 2 g",
    "source_amount": "2", "source_unit": "g", "owner_concentration": {"value": "2",
    "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Ammonium chloride, with no additional hydrate specified.", "target_reconstruction":
    "Replace the malformed target rows only after owner verification and separately
    authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[3]",
    "source_locator": "#medium-comp table tr[3]", "source_excerpt": "MgSO 4 ·7H 2
    O 0.4 g", "source_amount": "0.4", "source_unit": "g", "owner_concentration": {"value":
    "0.4", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Heptahydrate is explicit; retain all seven waters.", "target_reconstruction":
    "Replace the malformed target rows only after owner verification and separately
    authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[4]",
    "source_locator": "#medium-comp table tr[4]", "source_excerpt": "NaCl 30 mg",
    "source_amount": "30", "source_unit": "mg", "owner_concentration": {"value": "30",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "30 mg is retained as MG_PER_L on the nominal batch basis; no g/mg substitution.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[5]",
    "source_locator": "#medium-comp table tr[5]", "source_excerpt": "CaCl 2 ·2H 2
    O 3 mg", "source_amount": "3", "source_unit": "mg", "owner_concentration": {"value":
    "3", "unit": "MG_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Dihydrate and 3 mg are explicit; do not use anhydrous mass.", "target_reconstruction":
    "Replace the malformed target rows only after owner verification and separately
    authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[6]",
    "source_locator": "#medium-comp table tr[6]", "source_excerpt": "FeSO 4 ·7H 2
    O 1 mg", "source_amount": "1", "source_unit": "mg", "owner_concentration": {"value":
    "1", "unit": "MG_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Iron(II) sulfate heptahydrate and 1 mg are explicit.", "target_reconstruction":
    "Replace the malformed target rows only after owner verification and separately
    authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[7]",
    "source_locator": "#medium-comp table tr[7]", "source_excerpt": "Yeast extract
    3 g", "source_amount": "3", "source_unit": "g", "owner_concentration": {"value":
    "3", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Undefined yeast extract; no pure-molecule identity or product grade inferred.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[8]",
    "source_locator": "#medium-comp table tr[8]", "source_excerpt": "Rhamnose 10 g",
    "source_amount": "10", "source_unit": "g", "owner_concentration": {"value": "10",
    "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Rhamnose without a stated enantiomer or hydrate; no stereochemical refinement.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[9]",
    "source_locator": "#medium-comp table tr[9]", "source_excerpt": "Distilled water
    1 L", "source_amount": "1", "source_unit": "L", "owner_concentration": {"value":
    "1", "unit": "L"}, "decision": "verified", "reason": "The source directly reports
    the one-liter water quantity.", "chemical_form_and_scope": "One liter of distilled
    water is a batch input, not a measurement of final volume after solutes.", "target_reconstruction":
    "Replace the malformed target rows only after owner verification and separately
    authorized regeneration."}, {"field": "ph_value", "source_excerpt": "pH 7.0",
    "source_locator": "#medium-comp pH line", "owner_value": 7.0, "target_value":
    null, "decision": "add", "reason": "Source pH is explicit and maintained but absent
    as a structured target value; it remains buried in the ingredient blob."}]'
- evidence_id: audit-context
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_310.yaml
  locator: Entire owner versus generated record; all term labels, source references,
    later history and timezone fields
  accessed_at: '2026-10-21T08:13:54Z'
  support: context_only
  summary: '{"owner_identifier_checks": [{"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[0].term",
    "id": "CHEBI:131527", "asserted_label": "dipotassium hydrogen phosphate", "canonical_label":
    "dipotassium hydrogen phosphate", "label_matches": true, "definition": ["A potassium
    salt that is the dipotassium salt of phosphoric acid."], "source_form_scope":
    "Dipotassium hydrogen phosphate; do not replace by monopotassium phosphate."},
    {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[0].mediaingredientmech_chebi_term",
    "id": "CHEBI:131527", "asserted_label": "dipotassium hydrogen phosphate", "canonical_label":
    "dipotassium hydrogen phosphate", "label_matches": true, "definition": ["A potassium
    salt that is the dipotassium salt of phosphoric acid."], "source_form_scope":
    "Dipotassium hydrogen phosphate; do not replace by monopotassium phosphate."},
    {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[1].term",
    "id": "CHEBI:63036", "asserted_label": "potassium dihydrogen phosphate", "canonical_label":
    "potassium dihydrogen phosphate", "label_matches": true, "definition": ["A potassium
    salt in which dihydrogen phosphate(1−) is the counterion."], "source_form_scope":
    "Potassium dihydrogen phosphate is distinct from the preceding dibasic salt."},
    {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[1].mediaingredientmech_chebi_term",
    "id": "CHEBI:63036", "asserted_label": "potassium dihydrogen phosphate", "canonical_label":
    "potassium dihydrogen phosphate", "label_matches": true, "definition": ["A potassium
    salt in which dihydrogen phosphate(1−) is the counterion."], "source_form_scope":
    "Potassium dihydrogen phosphate is distinct from the preceding dibasic salt."},
    {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[2].term",
    "id": "CHEBI:31206", "asserted_label": "ammonium chloride", "canonical_label":
    "ammonium chloride", "label_matches": true, "definition": ["An inorganic chloride
    having ammonium as the counterion."], "source_form_scope": "Ammonium chloride,
    with no additional hydrate specified."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[2].mediaingredientmech_chebi_term",
    "id": "CHEBI:31206", "asserted_label": "ammonium chloride", "canonical_label":
    "ammonium chloride", "label_matches": true, "definition": ["An inorganic chloride
    having ammonium as the counterion."], "source_form_scope": "Ammonium chloride,
    with no additional hydrate specified."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[3].term",
    "id": "CHEBI:31795", "asserted_label": "magnesium sulfate heptahydrate", "canonical_label":
    "magnesium sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate
    that is the heptahydrate form of magnesium sulfate."], "source_form_scope": "Heptahydrate
    is explicit; retain all seven waters."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[3].mediaingredientmech_chebi_term",
    "id": "CHEBI:31795", "asserted_label": "magnesium sulfate heptahydrate", "canonical_label":
    "magnesium sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate
    that is the heptahydrate form of magnesium sulfate."], "source_form_scope": "Heptahydrate
    is explicit; retain all seven waters."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[4].term",
    "id": "CHEBI:26710", "asserted_label": "sodium chloride", "canonical_label": "sodium
    chloride", "label_matches": true, "definition": ["An inorganic chloride salt having
    sodium(1+) as the counterion."], "source_form_scope": "30 mg is retained as MG_PER_L
    on the nominal batch basis; no g/mg substitution."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[4].mediaingredientmech_chebi_term",
    "id": "CHEBI:26710", "asserted_label": "sodium chloride", "canonical_label": "sodium
    chloride", "label_matches": true, "definition": ["An inorganic chloride salt having
    sodium(1+) as the counterion."], "source_form_scope": "30 mg is retained as MG_PER_L
    on the nominal batch basis; no g/mg substitution."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[5].term",
    "id": "CHEBI:86158", "asserted_label": "calcium chloride dihydrate", "canonical_label":
    "calcium chloride dihydrate", "label_matches": true, "definition": ["A hydrate
    that is the dihydrate form of calcium chloride."], "source_form_scope": "Dihydrate
    and 3 mg are explicit; do not use anhydrous mass."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[5].mediaingredientmech_chebi_term",
    "id": "CHEBI:86158", "asserted_label": "calcium chloride dihydrate", "canonical_label":
    "calcium chloride dihydrate", "label_matches": true, "definition": ["A hydrate
    that is the dihydrate form of calcium chloride."], "source_form_scope": "Dihydrate
    and 3 mg are explicit; do not use anhydrous mass."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[6].term",
    "id": "CHEBI:75836", "asserted_label": "iron(2+) sulfate heptahydrate", "canonical_label":
    "iron(2+) sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate
    that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron
    in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments;
    for solid-dosage treatments, the monohydrate is normally used)."], "source_form_scope":
    "Iron(II) sulfate heptahydrate and 1 mg are explicit."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[6].mediaingredientmech_chebi_term",
    "id": "CHEBI:75836", "asserted_label": "iron(2+) sulfate heptahydrate", "canonical_label":
    "iron(2+) sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate
    that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron
    in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments;
    for solid-dosage treatments, the monohydrate is normally used)."], "source_form_scope":
    "Iron(II) sulfate heptahydrate and 1 mg are explicit."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[8].term",
    "id": "CHEBI:26546", "asserted_label": "rhamnose", "canonical_label": "rhamnose",
    "label_matches": true, "definition": ["A deoxymannose sugar that is the 6-deoxy
    derivative of hexose."], "source_form_scope": "Rhamnose without a stated enantiomer
    or hydrate; no stereochemical refinement."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[8].mediaingredientmech_chebi_term",
    "id": "CHEBI:26546", "asserted_label": "rhamnose", "canonical_label": "rhamnose",
    "label_matches": true, "definition": ["A deoxymannose sugar that is the 6-deoxy
    derivative of hexose."], "source_form_scope": "Rhamnose without a stated enantiomer
    or hydrate; no stereochemical refinement."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[9].term",
    "id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_matches":
    true, "definition": ["An oxygen hydride consisting of an oxygen atom that is covalently
    bonded to two hydrogen atoms"], "source_form_scope": "One liter of distilled water
    is a batch input, not a measurement of final volume after solutes."}, {"owner_field":
    "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[9].mediaingredientmech_chebi_term",
    "id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_matches":
    true, "definition": ["An oxygen hydride consisting of an oxygen atom that is covalently
    bonded to two hydrogen atoms"], "source_form_scope": "One liter of distilled water
    is a batch input, not a measurement of final volume after solutes."}], "history":
    {"target": {"count": 6, "timezone_bearing_timestamps": ["2026-02-20T00:22:35.948677Z",
    "2026-03-13T03:09:22.615369Z", "2026-03-13T06:19:49.228531Z", "2026-03-14T00:00:00+00:00",
    "2026-05-16T09:03:06.682530+00:00", "2026-08-06T03:05:04.669493+00:00"]}, "owner":
    {"count": 8, "timezone_bearing_timestamps": ["2026-02-20T00:22:35.948677Z", "2026-03-13T03:09:22.615369Z",
    "2026-03-13T06:19:49.228531Z", "2026-03-14T00:00:00+00:00", "2026-05-16T09:03:06.682530+00:00",
    "2026-08-19T21:54:22.877838+00:00", "2026-08-20T19:01:15.980273+00:00", "2026-09-11T00:00:00-07:00"]}},
    "owner_reference": [{"reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=309"}],
    "target_reference_count": 0, "owner_narrow_evidence_present": false}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/nbrc_importer.py
  locator: _create_description; _map_ingredients; _infer_physical_state; _map_preparation_steps;
    _determine_category
  accessed_at: '2026-10-21T08:13:54Z'
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
  accessed_at: '2026-10-21T08:13:54Z'
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
  accessed_at: '2026-10-21T08:13:54Z'
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
  accessed_at: '2026-10-21T08:13:54Z'
  support: context_only
  summary: The NBRC raw-YAML converter dispatches a direct JSON-to-YAML conversion
    without normalization. It is not a maintained scientific curation owner or a remedy
    for damaged source-JSON ingredient structure.
- evidence_id: owner-repair
  kind: record_content
  reference: scripts/repair_nbrc_310_score15.py
  locator: TARGET_ID/URL/title; imported ingredient signature; grounding table; repair_document
  accessed_at: '2026-10-21T08:13:54Z'
  support: supports
  summary: The current bounded repair pins CultureMech007486 to NBRC309, its exact
    ten recovered rows, official title, pH7.0, nine ingredient identifiers and primary
    reference. It adds source metadata and history while leaving generic preparation
    intact. The code was read, not executed.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007486
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
  - CultureMech:007486
  evidence_ids:
  - record
  - mim
  details: 2 direct ingredient instances; CHEBI-primary instance linkage 0/2 (0.00%),
    verified secondary coverage 0/2 (0.00%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Exact NBRC309 source and maintained owner
  outcome: supported
  summary: Stable ID CultureMech:007486, the merge contributor NBRC_310.yaml, the
    explicit import-history accession and both live source routes identify NBRC309.
    The official title is Rhamnose Salt Medium. Normalized/generated appearances of
    the same stable ID are distinct data layers, not evidence of two maintained IDs.
  target_ids:
  - CultureMech:007486
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
  summary: Both target ingredient rows need correction. All 10 owner rows preserve
    the corresponding source numerals and supplied chemical/product forms. The water-input
    batch basis, optional agar and any liquid additions remain explicit; there are
    no source stock groups or target stock references to invent. The full field-by-field
    inventory records verified batch facts separately from nominal final-concentration
    interpretations.
  target_ids:
  - CultureMech:007486
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - quantity-inventory
  details: '[{"target_field": "ingredients[0]", "stored_value": {"preferred_term":
    "K2HPO42.9gKH2PO42.1gNH4Cl2gMgSO4·7H2O0.4gNaCl30mgCaCl2·2H2O3mgFeSO4·7H2O1mgYeast
    extract3gRhamnose10gDistilled water1LpH 7.0", "concentration": {"value": "variable",
    "unit": "VARIABLE"}}, "decision": "correct", "reason": "An entire composition
    table plus pH/footnotes is not one ingredient. VARIABLE conceals explicit source
    numerals."}, {"target_field": "ingredients[1]", "stored_value": {"preferred_term":
    "", "concentration": {"value": "K2HPO4", "unit": "G_PER_L"}}, "decision": "correct",
    "reason": "The ingredient name is blank and the concentration value is a chemical/product
    name, not an amount."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[0]",
    "source_locator": "#medium-comp table tr[0]", "source_excerpt": "K 2 HPO 4 2.9
    g", "source_amount": "2.9", "source_unit": "g", "owner_concentration": {"value":
    "2.9", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Dipotassium hydrogen phosphate; do not replace by monopotassium phosphate.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[1]",
    "source_locator": "#medium-comp table tr[1]", "source_excerpt": "KH 2 PO 4 2.1
    g", "source_amount": "2.1", "source_unit": "g", "owner_concentration": {"value":
    "2.1", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Potassium dihydrogen phosphate is distinct from the preceding dibasic salt.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[2]",
    "source_locator": "#medium-comp table tr[2]", "source_excerpt": "NH 4 Cl 2 g",
    "source_amount": "2", "source_unit": "g", "owner_concentration": {"value": "2",
    "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Ammonium chloride, with no additional hydrate specified.", "target_reconstruction":
    "Replace the malformed target rows only after owner verification and separately
    authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[3]",
    "source_locator": "#medium-comp table tr[3]", "source_excerpt": "MgSO 4 ·7H 2
    O 0.4 g", "source_amount": "0.4", "source_unit": "g", "owner_concentration": {"value":
    "0.4", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Heptahydrate is explicit; retain all seven waters.", "target_reconstruction":
    "Replace the malformed target rows only after owner verification and separately
    authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[4]",
    "source_locator": "#medium-comp table tr[4]", "source_excerpt": "NaCl 30 mg",
    "source_amount": "30", "source_unit": "mg", "owner_concentration": {"value": "30",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "30 mg is retained as MG_PER_L on the nominal batch basis; no g/mg substitution.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[5]",
    "source_locator": "#medium-comp table tr[5]", "source_excerpt": "CaCl 2 ·2H 2
    O 3 mg", "source_amount": "3", "source_unit": "mg", "owner_concentration": {"value":
    "3", "unit": "MG_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Dihydrate and 3 mg are explicit; do not use anhydrous mass.", "target_reconstruction":
    "Replace the malformed target rows only after owner verification and separately
    authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[6]",
    "source_locator": "#medium-comp table tr[6]", "source_excerpt": "FeSO 4 ·7H 2
    O 1 mg", "source_amount": "1", "source_unit": "mg", "owner_concentration": {"value":
    "1", "unit": "MG_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Iron(II) sulfate heptahydrate and 1 mg are explicit.", "target_reconstruction":
    "Replace the malformed target rows only after owner verification and separately
    authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[7]",
    "source_locator": "#medium-comp table tr[7]", "source_excerpt": "Yeast extract
    3 g", "source_amount": "3", "source_unit": "g", "owner_concentration": {"value":
    "3", "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Undefined yeast extract; no pure-molecule identity or product grade inferred.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[8]",
    "source_locator": "#medium-comp table tr[8]", "source_excerpt": "Rhamnose 10 g",
    "source_amount": "10", "source_unit": "g", "owner_concentration": {"value": "10",
    "unit": "G_PER_L"}, "decision": "evidence_only", "reason": "The owner preserves
    the source numeral and mass/volume unit on a nominal one-liter water-input basis;
    this is not an independently verified final-volume concentration.", "chemical_form_and_scope":
    "Rhamnose without a stated enantiomer or hydrate; no stereochemical refinement.",
    "target_reconstruction": "Replace the malformed target rows only after owner verification
    and separately authorized regeneration."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[9]",
    "source_locator": "#medium-comp table tr[9]", "source_excerpt": "Distilled water
    1 L", "source_amount": "1", "source_unit": "L", "owner_concentration": {"value":
    "1", "unit": "L"}, "decision": "verified", "reason": "The source directly reports
    the one-liter water quantity.", "chemical_form_and_scope": "One liter of distilled
    water is a batch input, not a measurement of final volume after solutes.", "target_reconstruction":
    "Replace the malformed target rows only after owner verification and separately
    authorized regeneration."}, {"field": "ph_value", "source_excerpt": "pH 7.0",
    "source_locator": "#medium-comp pH line", "owner_value": 7.0, "target_value":
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
  - CultureMech:007486
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - audit-context
  - recovery
  - owner-repair
- assessment_id: preparation
  area: evidence
  topic: Source-specific protocol versus generated default steps
  outcome: concern
  summary: The current official page supplies the composition and pH 7.0 but no autoclave
    protocol. All three generic preparation descriptions persist in both target and
    owner, and the autoclaving description is mislabeled DISSOLVE.
  target_ids:
  - CultureMech:007486
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
  outcome: supported
  summary: All 9 distinct owner ontology IDs resolve and are non-obsolete; 0 asserted
    labels differ from canonical labels. The quantity inventory separately preserves
    source hydrate, salt, stereochemical and undefined-mixture limits. Canonical label
    resolution alone is not proof of supplied chemical form or preparation. No replacement
    identifiers were invented.
  target_ids:
  - CultureMech:007486
  evidence_ids:
  - owner-0
  - nbrc
  - quantity-inventory
  - audit-context
  - owner-mim
  - owner-chebi131527
  - owner-chebi15377
  - owner-chebi26546
  - owner-chebi26710
  - owner-chebi31206
  - owner-chebi31795
  - owner-chebi63036
  - owner-chebi75836
  - owner-chebi86158
  details: '[{"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[0].term",
    "id": "CHEBI:131527", "asserted_label": "dipotassium hydrogen phosphate", "canonical_label":
    "dipotassium hydrogen phosphate", "label_matches": true, "definition": ["A potassium
    salt that is the dipotassium salt of phosphoric acid."], "source_form_scope":
    "Dipotassium hydrogen phosphate; do not replace by monopotassium phosphate."},
    {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[0].mediaingredientmech_chebi_term",
    "id": "CHEBI:131527", "asserted_label": "dipotassium hydrogen phosphate", "canonical_label":
    "dipotassium hydrogen phosphate", "label_matches": true, "definition": ["A potassium
    salt that is the dipotassium salt of phosphoric acid."], "source_form_scope":
    "Dipotassium hydrogen phosphate; do not replace by monopotassium phosphate."},
    {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[1].term",
    "id": "CHEBI:63036", "asserted_label": "potassium dihydrogen phosphate", "canonical_label":
    "potassium dihydrogen phosphate", "label_matches": true, "definition": ["A potassium
    salt in which dihydrogen phosphate(1−) is the counterion."], "source_form_scope":
    "Potassium dihydrogen phosphate is distinct from the preceding dibasic salt."},
    {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[1].mediaingredientmech_chebi_term",
    "id": "CHEBI:63036", "asserted_label": "potassium dihydrogen phosphate", "canonical_label":
    "potassium dihydrogen phosphate", "label_matches": true, "definition": ["A potassium
    salt in which dihydrogen phosphate(1−) is the counterion."], "source_form_scope":
    "Potassium dihydrogen phosphate is distinct from the preceding dibasic salt."},
    {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[2].term",
    "id": "CHEBI:31206", "asserted_label": "ammonium chloride", "canonical_label":
    "ammonium chloride", "label_matches": true, "definition": ["An inorganic chloride
    having ammonium as the counterion."], "source_form_scope": "Ammonium chloride,
    with no additional hydrate specified."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[2].mediaingredientmech_chebi_term",
    "id": "CHEBI:31206", "asserted_label": "ammonium chloride", "canonical_label":
    "ammonium chloride", "label_matches": true, "definition": ["An inorganic chloride
    having ammonium as the counterion."], "source_form_scope": "Ammonium chloride,
    with no additional hydrate specified."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[3].term",
    "id": "CHEBI:31795", "asserted_label": "magnesium sulfate heptahydrate", "canonical_label":
    "magnesium sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate
    that is the heptahydrate form of magnesium sulfate."], "source_form_scope": "Heptahydrate
    is explicit; retain all seven waters."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[3].mediaingredientmech_chebi_term",
    "id": "CHEBI:31795", "asserted_label": "magnesium sulfate heptahydrate", "canonical_label":
    "magnesium sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate
    that is the heptahydrate form of magnesium sulfate."], "source_form_scope": "Heptahydrate
    is explicit; retain all seven waters."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[4].term",
    "id": "CHEBI:26710", "asserted_label": "sodium chloride", "canonical_label": "sodium
    chloride", "label_matches": true, "definition": ["An inorganic chloride salt having
    sodium(1+) as the counterion."], "source_form_scope": "30 mg is retained as MG_PER_L
    on the nominal batch basis; no g/mg substitution."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[4].mediaingredientmech_chebi_term",
    "id": "CHEBI:26710", "asserted_label": "sodium chloride", "canonical_label": "sodium
    chloride", "label_matches": true, "definition": ["An inorganic chloride salt having
    sodium(1+) as the counterion."], "source_form_scope": "30 mg is retained as MG_PER_L
    on the nominal batch basis; no g/mg substitution."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[5].term",
    "id": "CHEBI:86158", "asserted_label": "calcium chloride dihydrate", "canonical_label":
    "calcium chloride dihydrate", "label_matches": true, "definition": ["A hydrate
    that is the dihydrate form of calcium chloride."], "source_form_scope": "Dihydrate
    and 3 mg are explicit; do not use anhydrous mass."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[5].mediaingredientmech_chebi_term",
    "id": "CHEBI:86158", "asserted_label": "calcium chloride dihydrate", "canonical_label":
    "calcium chloride dihydrate", "label_matches": true, "definition": ["A hydrate
    that is the dihydrate form of calcium chloride."], "source_form_scope": "Dihydrate
    and 3 mg are explicit; do not use anhydrous mass."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[6].term",
    "id": "CHEBI:75836", "asserted_label": "iron(2+) sulfate heptahydrate", "canonical_label":
    "iron(2+) sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate
    that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron
    in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments;
    for solid-dosage treatments, the monohydrate is normally used)."], "source_form_scope":
    "Iron(II) sulfate heptahydrate and 1 mg are explicit."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[6].mediaingredientmech_chebi_term",
    "id": "CHEBI:75836", "asserted_label": "iron(2+) sulfate heptahydrate", "canonical_label":
    "iron(2+) sulfate heptahydrate", "label_matches": true, "definition": ["A hydrate
    that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron
    in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments;
    for solid-dosage treatments, the monohydrate is normally used)."], "source_form_scope":
    "Iron(II) sulfate heptahydrate and 1 mg are explicit."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[8].term",
    "id": "CHEBI:26546", "asserted_label": "rhamnose", "canonical_label": "rhamnose",
    "label_matches": true, "definition": ["A deoxymannose sugar that is the 6-deoxy
    derivative of hexose."], "source_form_scope": "Rhamnose without a stated enantiomer
    or hydrate; no stereochemical refinement."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[8].mediaingredientmech_chebi_term",
    "id": "CHEBI:26546", "asserted_label": "rhamnose", "canonical_label": "rhamnose",
    "label_matches": true, "definition": ["A deoxymannose sugar that is the 6-deoxy
    derivative of hexose."], "source_form_scope": "Rhamnose without a stated enantiomer
    or hydrate; no stereochemical refinement."}, {"owner_field": "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[9].term",
    "id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_matches":
    true, "definition": ["An oxygen hydride consisting of an oxygen atom that is covalently
    bonded to two hydrogen atoms"], "source_form_scope": "One liter of distilled water
    is a batch input, not a measurement of final volume after solutes."}, {"owner_field":
    "data/normalized_yaml/bacterial/NBRC_310.yaml:ingredients[9].mediaingredientmech_chebi_term",
    "id": "CHEBI:15377", "asserted_label": "water", "canonical_label": "water", "label_matches":
    true, "definition": ["An oxygen hydride consisting of an oxygen atom that is covalently
    bonded to two hydrogen atoms"], "source_form_scope": "One liter of distilled water
    is a batch input, not a measurement of final volume after solutes."}]'
- assessment_id: mapping-scope
  area: grounding
  topic: Separate malformed-target and recovered-owner linkage denominators
  outcome: concern
  summary: Target primary and secondary linkage are 0/2 (0%) of malformed rows; this
    does not mean two legitimate ingredients were checked. Owner all-ontology primary
    linkage is 9/10 (90.00%), CHEBI linkage is 9/10 (90.00%), and live pinned secondary
    linkage is 9/10 (90.00%). These are 0–100 linkage percentages, not scientific
    correctness scores.
  target_ids:
  - CultureMech:007486
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
  summary: LIQUID is compatible with the source table, which has no agar row. Yeast
    extract makes COMPLEX/UNDEFINED appropriate despite the salt-based title. Rhamnose
    Salt Medium is the official title; the numeric filename310 is not NBRC accession310.
    The target and owner assert no target-organism IDs, gene/transcriptomic context,
    native variants, parent links or KG-Microbe match. No organism-specific growth,
    optimization, incubation or strain identity is inferred from a medium title or
    bacterial filing category.
  target_ids:
  - CultureMech:007486
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
  - CultureMech:007486
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - legacy
  - audit-context
  - validate-references
findings:
- finding_id: f1
  issue_key: CM007486-malformed-generated-formulation
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated formula remains a table blob and an unnamed ingredient
  description: The target has two malformed ingredient objects instead of the 10 source
    rows. One names the complete recipe including pH/footnotes and assigns VARIABLE;
    the other has a blank preferred term and 'K2HPO4' as a G_PER_L value. This prevents
    faithful machine interpretation despite the four documented checks passing; it
    is a scientific representation blocker, not a P1.1 schema failure.
  target_ids:
  - CultureMech:007486
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
    path: data/normalized_yaml/bacterial/NBRC_310.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CM007486-stale-source-ph-grounding
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Maintained source-backed corrections have not reached the target
  description: The owner supplies NBRC309 source metadata, structured pH7.0, recovered
    row identities and later recovery/grounding history missing from the target. Corrected
    composition is tracked in the separate blocker; this finding covers lost identity,
    pH and provenance. The official Rhamnose Salt Medium name is also missing.
  target_ids:
  - CultureMech:007486
  field_paths:
  - ph_value
  - media_term
  - references
  - ingredients[*].term
  - curation_history
  - name
  - original_name
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - audit-context
  - recovery
  - owner-repair
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_310.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: CM007486-unsupported-generated-preparation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generated preparation defaults lack the required source scope
  description: The current official page supplies the composition and pH 7.0 but no
    autoclave protocol. All three generic preparation descriptions persist in both
    target and owner, and the autoclaving description is mislabeled DISSOLVE.
  target_ids:
  - CultureMech:007486
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
    path: data/normalized_yaml/bacterial/NBRC_310.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: CM007486-claim-evidence-gap
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
  - CultureMech:007486
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
    path: data/normalized_yaml/bacterial/NBRC_310.yaml
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
  - CultureMech:007486
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_310.yaml
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
  - CultureMech:007486
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_310.yaml
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
  description: Reassess the maintained owner preparation against the exact NBRC309
    source; remove or explicitly qualify unsupported defaults, preserve source pH7.0,
    and use the correct action for any later source-supported sterilization step before
    regeneration.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007486
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_310.yaml
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
  description: Attach short exact excerpts and locators to each maintained ingredient
    amount and other narrow claims using the existing evidence slots. Keep original
    source units and batch conditions distinct from arithmetic or interpretation.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007486
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_310.yaml
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
