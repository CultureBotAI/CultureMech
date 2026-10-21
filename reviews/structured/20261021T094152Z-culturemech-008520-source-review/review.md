# Source and formulation review: a3 (CultureMech:008520)

- Review: 20261021T094152Z-culturemech-008520-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T09:35:25Z
- Finished UTC: 2026-10-21T09:41:52Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

A3 is NBRC 1210 via TOGO M1941, but both layers change original milligrams and stock doses into g/L, flatten two stock recipes and combine their water amounts. The two referenced MediaDive stocks are different formulations. Calcium and manganese hydrate identities, optional agar scope, pH and provenance need bounded curation.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 132; batch 014 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirteen task batches contain 130 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 132 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008520 | data/merge_yaml/merged/A3.yaml | generated | a3 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008520 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008520 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch014/132/strict.tsv |
| validate-terms | passed | True | CultureMech:008520 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008520 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008520 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008520.

The four documented recipes completed; interpret the scope of each separately.

### Exact primary labels and current secondary linkage coverage

grounding: supported. Targets: CultureMech:008520.

14 unique asserted CHEBI identifiers resolve with exact labels. Primary linkage 14/15 (93.33%); verified current secondary linkage 10/15 (66.67%). This is a 0–100 ingredient-instance linkage scale, not scientific correctness. Missing current secondary keys: []. Legacy links and chemical-form correctness are assessed separately.

### Every direct, stock, stock-addition and preparation quantity

quantity: concern. Targets: CultureMech:008520.

Twenty decisions cover all 19 original source rows across main/Fe/A5 stages and target pH. Every target ingredient and both stock additions are reconciled; quantities and optionality remain source scoped.

[{"field_path": "ingredients[0].concentration", "decision": "correct", "stage": "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "Distilled water 1 L", "source_locator": "NBRC 1210 main medium; exact Distilled water composition/addition entry", "explanation": "Main water is 1 L. The recorded 502 g/L adds this numerical 1 to a separate 500 ml Fe-stock batch and a separate 1 L A5 batch; these are neither common units nor one preparation stage.", "original_source_amount": 1, "original_source_unit": "L", "provider_locator": "$.components[0].items[0]", "provider_paragraph": 1}, {"field_path": "ingredients[1].concentration", "decision": "correct", "stage": "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "MgSO 4 ·7H 2 O 75 mg", "source_locator": "NBRC 1210 main medium; exact MgSO4·7H2O composition/addition entry", "explanation": "Source 75 mg is 0.075 g for this main recipe, not 75 g/L. Preserve its 1 L water basis without claiming a measured final volume.", "original_source_amount": 75, "original_source_unit": "mg", "provider_locator": "$.components[0].items[1]", "provider_paragraph": 1}, {"field_path": "ingredients[2].concentration", "decision": "correct", "stage": "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "NaCl 25 mg", "source_locator": "NBRC 1210 main medium; exact NaCl composition/addition entry", "explanation": "Source 25 mg is 0.025 g for this main recipe, not 25 g/L. Preserve its 1 L water basis without claiming a measured final volume.", "original_source_amount": 25, "original_source_unit": "mg", "provider_locator": "$.components[0].items[2]", "provider_paragraph": 1}, {"field_path": "ingredients[3].concentration", "decision": "correct", "stage": "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "KH 2 PO 4 175 mg", "source_locator": "NBRC 1210 main medium; exact KH2PO4 composition/addition entry", "explanation": "Source 175 mg is 0.175 g for this main recipe, not 175 g/L. Preserve its 1 L water basis without claiming a measured final volume.", "original_source_amount": 175, "original_source_unit": "mg", "provider_locator": "$.components[0].items[3]", "provider_paragraph": 1}, {"field_path": "ingredients[4].concentration", "decision": "correct", "stage": "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "K 2 HPO 4 75 mg", "source_locator": "NBRC 1210 main medium; exact K2HPO4 composition/addition entry", "explanation": "Source 75 mg is 0.075 g for this main recipe, not 75 g/L. Preserve its 1 L water basis without claiming a measured final volume.", "original_source_amount": 75, "original_source_unit": "mg", "provider_locator": "$.components[0].items[4]", "provider_paragraph": 1}, {"field_path": "ingredients[5].concentration", "decision": "correct", "stage": "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "KNO 3 250 mg", "source_locator": "NBRC 1210 main medium; exact KNO3 composition/addition entry", "explanation": "Source 250 mg is 0.25 g for this main recipe, not 250 g/L. Preserve its 1 L water basis without claiming a measured final volume.", "original_source_amount": 250, "original_source_unit": "mg", "provider_locator": "$.components[0].items[5]", "provider_paragraph": 1}, {"field_path": "ingredients[6].concentration", "decision": "correct", "stage": "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "CaCl 2 ·H 2 O 10 mg", "source_locator": "NBRC 1210 main medium; exact CaCl2·H2O composition/addition entry", "explanation": "Source 10 mg is 0.01 g for this main recipe, not 10 g/L. Preserve its 1 L water basis without claiming a measured final volume.", "original_source_amount": 10, "original_source_unit": "mg", "provider_locator": "$.components[0].items[6]", "provider_paragraph": 1}, {"field_path": "ingredients[7].concentration", "decision": "correct", "stage": "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "Agar (if needed) 15 g", "source_locator": "NBRC 1210 main medium; exact Agar (if needed) composition/addition entry", "explanation": "The stated 15 g agar applies only if needed. Its number is preserved but unconditional solid state does not represent the agar-free branch; preserve the conditional family explicitly.", "original_source_amount": 15, "original_source_unit": "g", "provider_locator": "$.components[0].items[7]", "provider_paragraph": 1}, {"field_path": "solutions[0].concentration", "decision": "correct", "stage": "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "Fe Solution* 1 ml", "source_locator": "NBRC 1210 main medium; exact Fe Solution* composition/addition entry", "explanation": "Source addition is 1 ml of the source-specific stock, not 1 g/L. Density is unknown; the currently linked MediaDive stock is a different recipe.", "original_source_amount": 1, "original_source_unit": "ml", "provider_locator": "$.components[0].items[8]", "provider_paragraph": 1}, {"field_path": "solutions[1].concentration", "decision": "correct", "stage": "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "A5 Solution** 1 ml", "source_locator": "NBRC 1210 main medium; exact A5 Solution** composition/addition entry", "explanation": "Source addition is 1 ml of the source-specific stock, not 1 g/L. Density is unknown; the currently linked MediaDive stock is a different recipe.", "original_source_amount": 1, "original_source_unit": "ml", "provider_locator": "$.components[0].items[9]", "provider_paragraph": 1}, {"field_path": "ingredients[0].concentration", "decision": "correct", "stage": "Fe stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "Distilled water 500 ml", "source_locator": "NBRC 1210 Fe stock before its 1 ml addition; exact Distilled water composition/addition entry", "explanation": "Keep the source amount, original unit and stage; do not flatten stock preparation quantities into receiving-medium concentrations.", "original_source_amount": 500, "original_source_unit": "ml", "provider_locator": "$.components[1].items[0]", "provider_paragraph": 5}, {"field_path": "ingredients[8].concentration", "decision": "correct", "stage": "Fe stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "FeSO 4 ·7H 2 O 1.0 g", "source_locator": "NBRC 1210 Fe stock before its 1 ml addition; exact FeSO4·7H2O composition/addition entry", "explanation": "Keep the source amount, original unit and stage; do not flatten stock preparation quantities into receiving-medium concentrations.", "original_source_amount": 1, "original_source_unit": "g", "provider_locator": "$.components[1].items[1]", "provider_paragraph": 5}, {"field_path": "ingredients[9].concentration", "decision": "not_quantified", "stage": "Fe stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "H 2 SO 4 few drops", "source_locator": "NBRC 1210 Fe stock before its 1 ml addition; exact H2SO4 composition/addition entry", "explanation": "Retain few drops within Fe-stock preparation. No fixed volume, mass, strength or final-medium acid concentration is supported.", "original_source_amount": null, "original_source_unit": null, "provider_locator": "$.components[1].items[2]", "provider_paragraph": 5}, {"field_path": "ingredients[0].concentration", "decision": "correct", "stage": "A5 stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "Distilled water 1L", "source_locator": "NBRC 1210 A5 stock before its 1 ml addition; exact Distilled water composition/addition entry", "explanation": "Keep the source amount, original unit and stage; do not flatten stock preparation quantities into receiving-medium concentrations.", "original_source_amount": 1, "original_source_unit": "L", "provider_locator": "$.components[2].items[0]", "provider_paragraph": 8}, {"field_path": "ingredients[10].concentration", "decision": "correct", "stage": "A5 stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "H 3 BO 3 2.86 g", "source_locator": "NBRC 1210 A5 stock before its 1 ml addition; exact H3BO3 composition/addition entry", "explanation": "Keep the source amount, original unit and stage; do not flatten stock preparation quantities into receiving-medium concentrations.", "original_source_amount": 2.86, "original_source_unit": "g", "provider_locator": "$.components[2].items[1]", "provider_paragraph": 8}, {"field_path": "ingredients[11].concentration", "decision": "correct", "stage": "A5 stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "ZnSO 4 ·7H 2 O 222 mg", "source_locator": "NBRC 1210 A5 stock before its 1 ml addition; exact ZnSO4·7H2O composition/addition entry", "explanation": "Keep the source amount, original unit and stage; do not flatten stock preparation quantities into receiving-medium concentrations. Its 222 mg equals 0.222 g within the separately prepared stock; this conversion does not make the stock amount a final-medium concentration.", "original_source_amount": 222, "original_source_unit": "mg", "provider_locator": "$.components[2].items[2]", "provider_paragraph": 8}, {"field_path": "ingredients[12].concentration", "decision": "correct", "stage": "A5 stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "CuSO 4 ·5H 2 O 79 mg", "source_locator": "NBRC 1210 A5 stock before its 1 ml addition; exact CuSO4·5H2O composition/addition entry", "explanation": "Keep the source amount, original unit and stage; do not flatten stock preparation quantities into receiving-medium concentrations. Its 79 mg equals 0.079 g within the separately prepared stock; this conversion does not make the stock amount a final-medium concentration.", "original_source_amount": 79, "original_source_unit": "mg", "provider_locator": "$.components[2].items[3]", "provider_paragraph": 8}, {"field_path": "ingredients[13].concentration", "decision": "correct", "stage": "A5 stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "MnSO 4 ·7H 2 O 2.5 g", "source_locator": "NBRC 1210 A5 stock before its 1 ml addition; exact MnSO4·7H2O composition/addition entry", "explanation": "Keep the source amount, original unit and stage; do not flatten stock preparation quantities into receiving-medium concentrations.", "original_source_amount": 2.5, "original_source_unit": "g", "provider_locator": "$.components[2].items[4]", "provider_paragraph": 8}, {"field_path": "ingredients[14].concentration", "decision": "correct", "stage": "A5 stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "Na 2 MoO 4 21 mg", "source_locator": "NBRC 1210 A5 stock before its 1 ml addition; exact Na2MoO4 composition/addition entry", "explanation": "Keep the source amount, original unit and stage; do not flatten stock preparation quantities into receiving-medium concentrations. Its 21 mg equals 0.021 g within the separately prepared stock; this conversion does not make the stock amount a final-medium concentration.", "original_source_amount": 21, "original_source_unit": "mg", "provider_locator": "$.components[2].items[5]", "provider_paragraph": 8}, {"field_path": "ph_value", "decision": "add", "stage": "main recipe target pH", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210", "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5", "source_quote": "pH 6.0", "source_locator": "NBRC 1210 pH row", "explanation": "Both layers omit the source target pH. Do not infer incubation or post-growth pH."}]

### Exact primary accession and linked stock boundaries

identity: concern. Targets: CultureMech:008520.

TOGO M1941 and NBRC 1210 agree on A3 identity. Both external stock IDs resolve, but their actual recipes conflict with the two explicitly specified NBRC stocks. Generic stock names cannot establish equivalence.

### All source materials and asserted molecular forms

grounding: concern. Targets: CultureMech:008520.

The six main salts and five A5 reagents retain primary formula strings. Calcium monohydrate and manganese sulfate heptahydrate are mapped to formulas Ca.2Cl and Mn.O4S that omit stated waters. Other source-stated sulfate hydrates resolve appropriately. NBRC writes Na2MoO4 without hydrate; do not replace it with the different external stock dihydrate. Its imported Organic compound note conflicts with its inorganic molybdate structure. Agar remains a mixture without an invented molecule ID.

### Conditional agar, classifications and claimed properties

scope: concern. Targets: CultureMech:008520.

The source expressly permits agar omission, while the target declares SOLID_AGAR and retains no separate liquid branch. A chemically specified salt/stock basis does not justify carrying generic COMPLEX/UNDEFINED labels across both branches; reassess those fields after stock and conditional-agar representation. high_metal has no source-backed threshold or separate evidence, and corrupted quantities cannot justify it. No target organism, strain, incubation, parent, native variant or KG match is asserted.

### Source pH and stock qualifiers

completeness: concern. Targets: CultureMech:008520.

pH 6.0 and the Fe-stock few-drops qualifier are absent as usable preparation context. The exact NBRC page provides no sterilization or incubation conditions, so none is supplied by analogy. Main/stock solvent quantities are separate.

### Owner correspondence, current code and claim evidence

provenance: concern. Targets: CultureMech:008520.

The complete 14 target and 13 owner events have timezone-bearing timestamps. Target history extends owner by the merge event; ingredients and stocks currently agree. Dates and fingerprint are lineage metadata, not scientific validation. No claim-level source evidence or references are present in the fully read target/owner; source links remain only in notes. Exact dependency evidence does not transfer across the false stock links.

## Findings

### f1: Original units and distinct stock stages are collapsed

blocker / open / confirmed; issue key: CM008520-source-units-and-stock-stages.

Six main milligram values become numerically identical g/L values. Fe/A5 stock ingredients are flattened into the medium; their milligram rows have the same unit corruption. Two 1 ml stock additions become 1 g/L, and unrelated water batches are summed to 502 g/L. These changes materially replace the source formulation.

### f2: Both linked MediaDive stocks differ from NBRC A3

major / open / confirmed; issue key: CM008520-false-stock-identities.

Fe 5640 uses HCl and conflicting Fe-strength representations rather than NBRC 1 g FeSO4·7H2O in 500 ml water with sulfuric-acid drops. A5 4987 changes manganese salt, molybdate hydration, adds cobalt, and changes boron/copper/zinc amounts. Existing exact dependency excerpts cannot establish identity.

### f3: Two molecular identifiers omit explicit source hydration

major / open / confirmed; issue key: CM008520-hydrate-mapping.

CaCl2·H2O and MnSO4·7H2O names have anhydrous-form ontology structures. Canonical label passes do not reconcile those formulas with the supplied materials.

### f4: The optional-agar family is represented as unconditional solid medium

major / open / confirmed; issue key: CM008520-conditional-family-classification.

NBRC says Agar (if needed); the record declares SOLID_AGAR without a liquid branch. COMPLEX/UNDEFINED and high_metal also lack reconciled source support for the corrected branch-specific composition.

### f5: The primary target pH is omitted

major / open / confirmed; issue key: CM008520-missing-source-ph.

Both NBRC and TOGO specify pH 6.0; neither local layer preserves it. No primary incubation or sterilization instruction was found in the fully inspected exact page.

### f6: Legacy linkage and source claims remain weakly represented

minor / open / confirmed; issue key: CM008520-secondary-link-and-property-provenance.

KNO3 retains legacy MediaIngredientMech:000170 while ten other secondary links use current CHEBI keys. The complete pinned index resolves current potassium nitrate but not the legacy identifier. Sodium molybdate is incorrectly described as organic in imported notes. Source amounts and conditions have no narrow evidence objects.

## Recommended Actions And Acceptance Checks

### a1

Restore original units and main/stock boundaries from exact NBRC sections, preserving conditional agar and unquantified sulfuric acid. Retain solvent amounts as preparation instructions; derive any concentration only from an explicit appropriate basis.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Replace unsupported cross-stock identity assertions with explicitly source-scoped stock representations. Preserve provider internal conflicts and do not edit the different dependency recipes to force a match. Replace Unknown solution placeholders using verified source names.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve exact source hydrate identities without guessing replacements; retain explicit unsupported mapping if a verified exact term is unavailable.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Represent the source agar condition and reconcile each branch’s physical state and composition classification. Require explicit support for high_metal rather than quantities corrupted during import.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Preserve source target pH and stock-preparation qualifiers with exact evidence; do not invent missing sterilization or incubation parameters.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Reconcile the legacy link against the pinned current entry, correct the unsupported property label, and attach exact primary snippets at their claim/stage. Preserve existing history and source dates.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/A3.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/a3.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/A3.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/A3.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch014/132/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch014/132/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/A3.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/A3.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/A3.yaml:1:id: CultureMech:008520<br>./data/normalized_yaml/bacterial/a3.yaml:1:id: CultureMech:008520<br> |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7758-11-4", "kegg.compound:C13197", "kegg.drug:D02403", "metacyc.compound:CPD0-2433", "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"], "generalized_empirical_formula": ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131527"], "inchi_key_string": ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"], "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]} |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:15377 resolves to water; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7732-18-5", "gmelin:117", "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001", "metacyc.compound:WATER", "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"], "generalized_empirical_formula": ["H2O"], "has_alternative_id": ["CHEBI:10743", "CHEBI:13352", "CHEBI:27313", "CHEBI:42043", "CHEBI:42857", "CHEBI:43228", "CHEBI:44292", "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15377"], "inchi_key_string": ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass": ["18.015"], "monoisotopic_mass": ["18.01056"], "smiles_string": ["[H]O[H]"]} |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:26710 resolves to sodium chloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula": ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string": ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]} |
| chebi26836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:26836 resolves to sulfuric acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7664-93-9", "gmelin:2122", "kegg.compound:C00059", "kegg.drug:D05963", "knapsack:C00007530", "molbase:4", "ppdb:606", "pubmed:13568755", "pubmed:16122922", "pubmed:19397353", "pubmed:22047659", "pubmed:22136045", "pubmed:22204399", "pubmed:22267186", "pubmed:22296037", "pubmed:22364556", "pubmed:22435616", "reaxys:2037554", "wikipedia.en:Sulfuric_acid"], "generalized_empirical_formula": ["H2O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26836"], "inchi_key_string": ["QAOWNCQODCNURD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O4S/c1-5(2,3)4/h(H2,1,2,3,4)"], "mass": ["98.079"], "monoisotopic_mass": ["97.96738"], "smiles_string": ["[H]OS(=O)(=O)O[H]"]} |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7758-99-8", "kegg.drug:D03613", "pubmed:11407502", "pubmed:12209195", "pubmed:12484481", "pubmed:15040745", "pubmed:15607472", "pubmed:15824790", "pubmed:19346702", "pubmed:2002460", "pubmed:20132934", "pubmed:2913309", "pubmed:3351847", "pubmed:7615984", "pubmed:8878264", "pubmed:9521458", "pubmed:9776063", "reaxys:16499970", "wikipedia.en:Copper(II)_sulfate"], "generalized_empirical_formula": ["Cu.5H2O.O4S"], "has_alternative_id": ["CHEBI:121741", "CHEBI:370227"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31440"], "inchi_key_string": ["JZCCFEFSEZPSOG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Cu.H2O4S.5H2O/c;1-5(2,3)4;;;;;/h;(H2,1,2,3,4);5*1H2/q+2;;;;;;/p-2"], "mass": ["249.684"], "monoisotopic_mass": ["248.93415"], "smiles_string": ["O=S(=O)([O-])[O-].[Cu+2].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H]"]} |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505", "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222", "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"], "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]} |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7446-20-0", "gmelin:47216", "kegg.drug:D01081", "wikipedia.en:Zinc_Sulfate"], "generalized_empirical_formula": ["7H2O.O4S.Zn"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32312"], "inchi_key_string": ["RZLVQBNCHSJZPX-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/H2O4S.7H2O.Zn/c1-5(2,3)4;;;;;;;;/h(H2,1,2,3,4);7*1H2;/q;;;;;;;;+2/p-2"], "mass": ["287.558"], "monoisotopic_mass": ["285.95482"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Zn+2]"]} |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:33118 resolves to boric acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["bpdb:2136", "cas:10043-35-3", "cas:11113-50-1", "drugcentral:3035", "gmelin:1585", "kegg.compound:C12486", "kegg.drug:D01089", "molbase:1644", "pdb-ccd:BO3", "ppdb:2136"], "generalized_empirical_formula": ["H3BO3"], "has_alternative_id": ["CHEBI:22911", "CHEBI:31299", "CHEBI:41248"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:33118"], "inchi_key_string": ["KGBXLFKZBHKPEV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"], "mass": ["61.833"], "monoisotopic_mass": ["62.01752"], "smiles_string": ["[H]OB(O[H])O[H]"]} |
| chebi3312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:3312 resolves to calcium dichloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["agr:IND607339542", "cas:10043-52-4", "drugbank:DB01164", "foodb.food:FDB015404", "hmdb:HMDB0303526", "kegg.compound:C08130", "metacyc.compound:CPD0-1589", "molbase:1869", "ppdb:109", "pubmed:11057678", "pubmed:13333715", "pubmed:32018153", "pubmed:32441097", "pubmed:34618995", "pubmed:34981086", "pubmed:35159430", "pubmed:35159592", "pubmed:35200459", "pubmed:35260323", "wikipedia.en:Calcium_Chloride"], "generalized_empirical_formula": ["Ca.2Cl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:3312"], "inchi_key_string": ["UXVMQQNJUSDDNG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Ca.2ClH/h;2*1H/q+2;;/p-2"], "mass": ["110.984"], "monoisotopic_mass": ["109.9003"], "smiles_string": ["[Ca+2].[Cl-].[Cl-]"]} |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"], "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"], "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]} |
| chebi63043 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:63043 resolves to potassium nitrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7757-79-1", "kegg.drug:D02051", "pubmed:20062955", "pubmed:21566718", "pubmed:21770249", "pubmed:21905227", "reaxys:16014598", "wikipedia.en:Potassium_nitrate"], "generalized_empirical_formula": ["K.NO3"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63043"], "inchi_key_string": ["FGIUAXJPYTZDNR-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/K.NO3/c;2-1(3)4/q+1;-1"], "mass": ["101.102"], "monoisotopic_mass": ["100.95152"], "smiles_string": ["O=[N+]([O-])[O-].[K+]"]} |
| chebi75215 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75215; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:75215 resolves to sodium molybdate (anhydrous); canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7631-95-0", "kegg.compound:C15455", "reaxys:11323078", "wikipedia.en:Sodium_molybdate"], "generalized_empirical_formula": ["MoO4.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75215"], "inchi_key_string": ["TVXXNOYZHKPKGW-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/Mo.2Na.4O/q;2*+1;;;2*-1"], "mass": ["205.916"], "monoisotopic_mass": ["207.86461"], "smiles_string": ["[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]} |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]} |
| chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:86360 resolves to manganese(II) sulfate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7785-87-7", "metacyc.compound:CPD0-1608", "reaxys:11343137", "reaxys:14270535", "reaxys:28059988", "wikipedia.en:Manganese(II)_sulfate"], "generalized_empirical_formula": ["Mn.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86360"], "inchi_key_string": ["SQQMAOCOWKFBNP-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mn.H2O4S/c;1-5(2,3)4/h;(H2,1,2,3,4)/q+2;/p-2"], "mass": ["151.001"], "monoisotopic_mass": ["150.88977"], "smiles_string": ["O=S(=O)([O-])[O-].[Mn+2]"]} |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned CSV; preferred-term MAPPED rows for every asserted secondary CHEBI key | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26836": [{"label": "H2SO4", "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75215": [{"label": "Na2MoO4", "match_type": "preferred_term", "identifier": "CHEBI:75215", "preferred_term": "Na2MoO4", "ontology_id": "CHEBI:75215", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210; Medium 1210 A3 entire composition, pH and two footnoted stock recipes | supports | Exact NBRC primary identifies A3, gives six main solutes in mg, optional agar, two 1 ml stock additions, pH 6.0 and distinct Fe/A5 stock recipes. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1941; $.meta; all three $.components sections; $.comments | supports | TOGO M1941 identifies NBRC_M1210 and preserves the same source amounts and distinct main, Fe and A5 sections. Its structured sulfuric-acid amount is absent while the comment retains few drops. |
| fe-other | https://mediadive.dsmz.de/rest/solution/5640; $.data.volume/recipe/steps | refutes | MediaDive 5640 is an Fe solution in 0.001 M HCl. Its 10 g FeSO4·7H2O recipe row and 4.98%/10 g Fe preparation text are internally inconsistent; neither supports the NBRC sulfuric-acid stock. |
| a5-other | https://mediadive.dsmz.de/rest/solution/4987; $.data.volume/recipe[0:7] | refutes | MediaDive 4987 adds cobalt nitrate, uses manganese chloride and sodium molybdate dihydrate, and differs in boron/copper/zinc quantities. It is not NBRC A3 A5 stock. |
| dep-solution5640 | https://mediadive.dsmz.de/rest/solution/5640; $.data.recipe; matching data/normalized_yaml/bacterial/mediadive_5640_Fe_solution.yaml composition evidence | supports | 1 local ingredient snippets parse to the exact captured provider rows and retain the same historical response hash; current and historical access times differ. This verifies those dependency sources only, not their use as A3 stocks. |
| dep-solution4987 | https://mediadive.dsmz.de/rest/solution/4987; $.data.recipe; matching data/normalized_yaml/bacterial/mediadive_4987_A5_solution.yaml composition evidence | supports | 7 local ingredient snippets parse to the exact captured provider rows and retain the same historical response hash; current and historical access times differ. This verifies those dependency sources only, not their use as A3 stocks. |
| writer | src/culturemech/import/togo_importer.py; scripts/migrate_solutions_from_ingredients.py; scripts/cleanup_media_quality.py; _extract_primary_components/_solution_from_item/_ingredient_from_item; _resolve_solution; duplicate handling | context_only | Current importer separates named stocks and preserves source units. Current migrator can resolve a stock by cleaned name and copies existing concentrations without formulation comparison. Current duplicate cleanup does not justify summing different stage solvent amounts. These are inspected present-code contexts, not an attributed historical execution. |
| quantities | /private/tmp/culturemech-review-work-batch014/132/quantity-inventory.json; Complete source-linked quantity decision inventory | context_only | Twenty decisions cover all 19 original source rows across main/Fe/A5 stages and target pH. Every target ingredient and both stock additions are reconciled; quantities and optionality remain source scoped. |
| legacy | src/culturemech/data/mediaingredientmech/label_index.csv; Every row for legacy MediaIngredientMech:000170 and CHEBI:63043 | context_only | The complete 9077-row pinned CSV has no legacy identifier row; its current KNO3 preferred-term entry is [{"label": "KNO3", "match_type": "preferred_term", "identifier": "CHEBI:63043", "preferred_term": "KNO3", "ontology_id": "CHEBI:63043", "mapping_status": "MAPPED", "ambiguity": "unique"}]. This is a stale secondary link, not a failed primary potassium-nitrate identity. |

## Limits And Additional Notes

- The two linked MediaDive SolutionRecipe files are dependency context only, not additional reviewed targets. Their exact current source excerpts do not establish equivalence to NBRC A3 stocks.
- NBRC specifies solvent quantities and additions, not independently measured final volumes. Sulfuric-acid strength and drop volume are unreported. No density, final-volume, incubation or sterilization default is invented.
- Current TOGO importer and migration code explain representation mechanisms only; their current contents are not proof of the exact historical code executed.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T094152Z-culturemech-008520-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: a3 (CultureMech:008520)'
started_at: '2026-10-21T09:35:25Z'
finished_at: '2026-10-21T09:41:52Z'
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
summary: A3 is NBRC 1210 via TOGO M1941, but both layers change original milligrams
  and stock doses into g/L, flatten two stock recipes and combine their water amounts.
  The two referenced MediaDive stocks are different formulations. Calcium and manganese
  hydrate identities, optional agar scope, pH and provenance need bounded curation.
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
  - path: data/merge_yaml/merged/A3.yaml
    sha256: 3a60f98be14213b53bfeb09e321f727d500df1020243ef40c8e7daae524ee7ac
    role: target
  - path: data/normalized_yaml/bacterial/a3.yaml
    sha256: fbb7fdf9e1a4f14cde8098afa06899ac0c318feb1e9790c0d1c2c66e24510766
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4987_A5_solution.yaml
    sha256: d74c693e6e7689b7eb9d6af4bbaa3eb657de8b2533c4b5ac47e5d96be83afd12
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5640_Fe_solution.yaml
    sha256: dc6cd183ce920296264597df4d76292074e5fed63621c9673586bf6e2dc6956c
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/audit_merged_duplicates.py
    sha256: f98dd2c9772d8b2f36659ec5ead5a82ff1d00c283c3357de62c32df408e3c913
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/fetch_medium_concentration_sources.py
    sha256: 746c2828863e6ee409d88409a540ea0a8d01ffad3e38be4a4a47f47bec5bbeb5
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
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
  - path: src/culturemech/ingredients/mim_label_index.py
    sha256: e07eb72fe91743859451d1998dfeafe58a40dad43baa82d710a740c47dc4bf61
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
  selection: Task review 132; batch 014 item 2 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirteen task batches
    contain 130 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 132 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008520
targets:
- target_id: CultureMech:008520
  path: data/merge_yaml/merged/A3.yaml
  label: a3
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/a3.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/A3.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008520
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/A3.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch014/132/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch014/132/strict.tsv"
  target_ids:
  - CultureMech:008520
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/A3.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008520
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/A3.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008520
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
  - CultureMech:008520
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/A3.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T09:41:51Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/a3.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T09:41:51Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/A3.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:22.444937Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/A3.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch014/132/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:25.656927Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-014/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch014/132/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/A3.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:28.094326Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/A3.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:36:30.087123Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T09:41:51Z'
  support: supports
  summary: './data/merge_yaml/merged/A3.yaml:1:id: CultureMech:008520

    ./data/normalized_yaml/bacterial/a3.yaml:1:id: CultureMech:008520

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: 'CHEBI:131527 resolves to dipotassium hydrogen phosphate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:7758-11-4", "kegg.compound:C13197", "kegg.drug:D02403", "metacyc.compound:CPD0-2433",
    "reaxys:11343458", "wikipedia.en:Dipotassium_phosphate"], "generalized_empirical_formula":
    ["HO4P.2K"], "has_alternative_id": ["CHEBI:32031"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:131527"], "inchi_key_string": ["ZPWVASYFFYYZEW-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/2K.H3O4P/c;;1-5(2,3)4/h;;(H3,1,2,3,4)/q2*+1;/p-2"], "mass": ["174.174"],
    "monoisotopic_mass": ["173.88866"], "smiles_string": ["O=P([O-])([O-])O.[K+].[K+]"]}'
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: 'CHEBI:15377 resolves to water; canonical label and live status alone do
    not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"charge": [0.0], "database_cross_reference": ["cas:7732-18-5", "gmelin:117",
    "hmdb:HMDB0002111", "kegg.compound:C00001", "kegg.drug:D00001", "metacyc.compound:WATER",
    "molbase:1", "pdb-ccd:HOH", "reaxys:3587155", "wikipedia.en:Water"], "generalized_empirical_formula":
    ["H2O"], "has_alternative_id": ["CHEBI:10743", "CHEBI:13352", "CHEBI:27313", "CHEBI:42043",
    "CHEBI:42857", "CHEBI:43228", "CHEBI:44292", "CHEBI:44701", "CHEBI:44819", "CHEBI:5585"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15377"], "inchi_key_string":
    ["XLYOFNOQVPJJNP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/H2O/h1H2"], "mass":
    ["18.015"], "monoisotopic_mass": ["18.01056"], "smiles_string": ["[H]O[H]"]}'
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: 'CHEBI:26710 resolves to sodium chloride; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5",
    "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL",
    "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula":
    ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string":
    ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"],
    "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]}'
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi26836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T07:29:13.222926Z'
  support: supports
  summary: 'CHEBI:26836 resolves to sulfuric acid; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7664-93-9",
    "gmelin:2122", "kegg.compound:C00059", "kegg.drug:D05963", "knapsack:C00007530",
    "molbase:4", "ppdb:606", "pubmed:13568755", "pubmed:16122922", "pubmed:19397353",
    "pubmed:22047659", "pubmed:22136045", "pubmed:22204399", "pubmed:22267186", "pubmed:22296037",
    "pubmed:22364556", "pubmed:22435616", "reaxys:2037554", "wikipedia.en:Sulfuric_acid"],
    "generalized_empirical_formula": ["H2O4S"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:26836"], "inchi_key_string": ["QAOWNCQODCNURD-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/H2O4S/c1-5(2,3)4/h(H2,1,2,3,4)"], "mass": ["98.079"], "monoisotopic_mass":
    ["97.96738"], "smiles_string": ["[H]OS(=O)(=O)O[H]"]}'
  snapshot_sha256: 19e202cd697eed2be3130d5b0b29cc0c1d18575ad103110877303ee678779737
- evidence_id: chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:28.489501Z'
  support: supports
  summary: 'CHEBI:31440 resolves to copper(II) sulfate pentahydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:7758-99-8", "kegg.drug:D03613", "pubmed:11407502", "pubmed:12209195", "pubmed:12484481",
    "pubmed:15040745", "pubmed:15607472", "pubmed:15824790", "pubmed:19346702", "pubmed:2002460",
    "pubmed:20132934", "pubmed:2913309", "pubmed:3351847", "pubmed:7615984", "pubmed:8878264",
    "pubmed:9521458", "pubmed:9776063", "reaxys:16499970", "wikipedia.en:Copper(II)_sulfate"],
    "generalized_empirical_formula": ["Cu.5H2O.O4S"], "has_alternative_id": ["CHEBI:121741",
    "CHEBI:370227"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31440"],
    "inchi_key_string": ["JZCCFEFSEZPSOG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Cu.H2O4S.5H2O/c;1-5(2,3)4;;;;;/h;(H2,1,2,3,4);5*1H2/q+2;;;;;;/p-2"],
    "mass": ["249.684"], "monoisotopic_mass": ["248.93415"], "smiles_string": ["O=S(=O)([O-])[O-].[Cu+2].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H]"]}'
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: 'CHEBI:31795 resolves to magnesium sulfate heptahydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505",
    "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222",
    "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"],
    "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}'
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: 'CHEBI:32312 resolves to zinc sulfate heptahydrate; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7446-20-0",
    "gmelin:47216", "kegg.drug:D01081", "wikipedia.en:Zinc_Sulfate"], "generalized_empirical_formula":
    ["7H2O.O4S.Zn"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32312"],
    "inchi_key_string": ["RZLVQBNCHSJZPX-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/H2O4S.7H2O.Zn/c1-5(2,3)4;;;;;;;;/h(H2,1,2,3,4);7*1H2;/q;;;;;;;;+2/p-2"],
    "mass": ["287.558"], "monoisotopic_mass": ["285.95482"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Zn+2]"]}'
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: 'CHEBI:33118 resolves to boric acid; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"charge": [0.0], "database_cross_reference": ["bpdb:2136", "cas:10043-35-3",
    "cas:11113-50-1", "drugcentral:3035", "gmelin:1585", "kegg.compound:C12486", "kegg.drug:D01089",
    "molbase:1644", "pdb-ccd:BO3", "ppdb:2136"], "generalized_empirical_formula":
    ["H3BO3"], "has_alternative_id": ["CHEBI:22911", "CHEBI:31299", "CHEBI:41248"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:33118"], "inchi_key_string":
    ["KGBXLFKZBHKPEV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"],
    "mass": ["61.833"], "monoisotopic_mass": ["62.01752"], "smiles_string": ["[H]OB(O[H])O[H]"]}'
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi3312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T07:16:24.822837Z'
  support: supports
  summary: 'CHEBI:3312 resolves to calcium dichloride; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["agr:IND607339542",
    "cas:10043-52-4", "drugbank:DB01164", "foodb.food:FDB015404", "hmdb:HMDB0303526",
    "kegg.compound:C08130", "metacyc.compound:CPD0-1589", "molbase:1869", "ppdb:109",
    "pubmed:11057678", "pubmed:13333715", "pubmed:32018153", "pubmed:32441097", "pubmed:34618995",
    "pubmed:34981086", "pubmed:35159430", "pubmed:35159592", "pubmed:35200459", "pubmed:35260323",
    "wikipedia.en:Calcium_Chloride"], "generalized_empirical_formula": ["Ca.2Cl"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:3312"], "inchi_key_string":
    ["UXVMQQNJUSDDNG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Ca.2ClH/h;2*1H/q+2;;/p-2"],
    "mass": ["110.984"], "monoisotopic_mass": ["109.9003"], "smiles_string": ["[Ca+2].[Cl-].[Cl-]"]}'
  snapshot_sha256: 34ed49d95375c80dcb07576c67d04fa77337bfecf406accb283e8c32253b754b
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: 'CHEBI:63036 resolves to potassium dihydrogen phosphate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"],
    "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string":
    ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"],
    "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]}'
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63043
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T09:27:40.679699Z'
  support: supports
  summary: 'CHEBI:63043 resolves to potassium nitrate; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7757-79-1",
    "kegg.drug:D02051", "pubmed:20062955", "pubmed:21566718", "pubmed:21770249", "pubmed:21905227",
    "reaxys:16014598", "wikipedia.en:Potassium_nitrate"], "generalized_empirical_formula":
    ["K.NO3"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63043"], "inchi_key_string":
    ["FGIUAXJPYTZDNR-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/K.NO3/c;2-1(3)4/q+1;-1"],
    "mass": ["101.102"], "monoisotopic_mass": ["100.95152"], "smiles_string": ["O=[N+]([O-])[O-].[K+]"]}'
  snapshot_sha256: c324450e6330a169c708c32a7908b6df0276f4dc76da413e473b563928f61c13
- evidence_id: chebi75215
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75215
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T09:27:41.268041Z'
  support: supports
  summary: 'CHEBI:75215 resolves to sodium molybdate (anhydrous); canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:7631-95-0", "kegg.compound:C15455", "reaxys:11323078", "wikipedia.en:Sodium_molybdate"],
    "generalized_empirical_formula": ["MoO4.2Na"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:75215"], "inchi_key_string": ["TVXXNOYZHKPKGW-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/Mo.2Na.4O/q;2*+1;;;2*-1"], "mass": ["205.916"], "monoisotopic_mass":
    ["207.86461"], "smiles_string": ["[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]}'
  snapshot_sha256: fc350638c78c930db3b38cb59bd48dc73b408d309f79ada3ee087a8fb207fb0e
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: 'CHEBI:75836 resolves to iron(2+) sulfate heptahydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890",
    "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id":
    ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"],
    "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]}'
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi86360
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:05.958063Z'
  support: supports
  summary: 'CHEBI:86360 resolves to manganese(II) sulfate; canonical label and live
    status alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7785-87-7",
    "metacyc.compound:CPD0-1608", "reaxys:11343137", "reaxys:14270535", "reaxys:28059988",
    "wikipedia.en:Manganese(II)_sulfate"], "generalized_empirical_formula": ["Mn.O4S"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86360"], "inchi_key_string":
    ["SQQMAOCOWKFBNP-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mn.H2O4S/c;1-5(2,3)4/h;(H2,1,2,3,4)/q+2;/p-2"],
    "mass": ["151.001"], "monoisotopic_mass": ["150.88977"], "smiles_string": ["O=S(=O)([O-])[O-].[Mn+2]"]}'
  snapshot_sha256: ee3b60385f389c4eeb301cfe59996112ffa9c3c135268559b79e91810a14932b
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned CSV; preferred-term MAPPED rows for every asserted secondary
    CHEBI key
  accessed_at: '2026-10-21T09:41:51Z'
  support: supports
  summary: '{"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795":
    [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label":
    "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term":
    "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label":
    "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term":
    "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:26836": [{"label": "H2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label":
    "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term":
    "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440":
    [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75215": [{"label": "Na2MoO4", "match_type":
    "preferred_term", "identifier": "CHEBI:75215", "preferred_term": "Na2MoO4", "ontology_id":
    "CHEBI:75215", "mapping_status": "MAPPED", "ambiguity": "unique"}]}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210
  locator: Medium 1210 A3 entire composition, pH and two footnoted stock recipes
  accessed_at: '2026-10-21T09:27:41.962081Z'
  support: supports
  summary: Exact NBRC primary identifies A3, gives six main solutes in mg, optional
    agar, two 1 ml stock additions, pH 6.0 and distinct Fe/A5 stock recipes.
  snapshot_sha256: da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1941
  locator: $.meta; all three $.components sections; $.comments
  accessed_at: '2026-10-21T09:27:38.292316Z'
  support: supports
  summary: TOGO M1941 identifies NBRC_M1210 and preserves the same source amounts
    and distinct main, Fe and A5 sections. Its structured sulfuric-acid amount is
    absent while the comment retains few drops.
  snapshot_sha256: ef7bf3b07871bd8900d73add9f53c7cb776e8f5858a23e67290aa398c7d6dad9
- evidence_id: fe-other
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5640
  locator: $.data.volume/recipe/steps
  accessed_at: '2026-10-21T09:27:38.285848Z'
  support: refutes
  summary: MediaDive 5640 is an Fe solution in 0.001 M HCl. Its 10 g FeSO4·7H2O recipe
    row and 4.98%/10 g Fe preparation text are internally inconsistent; neither supports
    the NBRC sulfuric-acid stock.
  snapshot_sha256: b164e4e00e83b055b294497483c012b6c52ba7e33eb236a1839cf7357a8f4e1c
- evidence_id: a5-other
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4987
  locator: $.data.volume/recipe[0:7]
  accessed_at: '2026-10-21T09:27:37.735110Z'
  support: refutes
  summary: MediaDive 4987 adds cobalt nitrate, uses manganese chloride and sodium
    molybdate dihydrate, and differs in boron/copper/zinc quantities. It is not NBRC
    A3 A5 stock.
  snapshot_sha256: a9d72c787779be737b424d113df6824d5310c92641f2d1cb7510d8172fb2db4a
- evidence_id: dep-solution5640
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5640
  locator: $.data.recipe; matching data/normalized_yaml/bacterial/mediadive_5640_Fe_solution.yaml
    composition evidence
  accessed_at: '2026-10-21T09:27:38.285848Z'
  support: supports
  summary: 1 local ingredient snippets parse to the exact captured provider rows and
    retain the same historical response hash; current and historical access times
    differ. This verifies those dependency sources only, not their use as A3 stocks.
  snapshot_sha256: b164e4e00e83b055b294497483c012b6c52ba7e33eb236a1839cf7357a8f4e1c
- evidence_id: dep-solution4987
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4987
  locator: $.data.recipe; matching data/normalized_yaml/bacterial/mediadive_4987_A5_solution.yaml
    composition evidence
  accessed_at: '2026-10-21T09:27:37.735110Z'
  support: supports
  summary: 7 local ingredient snippets parse to the exact captured provider rows and
    retain the same historical response hash; current and historical access times
    differ. This verifies those dependency sources only, not their use as A3 stocks.
  snapshot_sha256: a9d72c787779be737b424d113df6824d5310c92641f2d1cb7510d8172fb2db4a
- evidence_id: writer
  kind: record_content
  reference: src/culturemech/import/togo_importer.py; scripts/migrate_solutions_from_ingredients.py;
    scripts/cleanup_media_quality.py
  locator: _extract_primary_components/_solution_from_item/_ingredient_from_item;
    _resolve_solution; duplicate handling
  accessed_at: '2026-10-21T09:41:51Z'
  support: context_only
  summary: Current importer separates named stocks and preserves source units. Current
    migrator can resolve a stock by cleaned name and copies existing concentrations
    without formulation comparison. Current duplicate cleanup does not justify summing
    different stage solvent amounts. These are inspected present-code contexts, not
    an attributed historical execution.
- evidence_id: quantities
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch014/132/quantity-inventory.json
  locator: Complete source-linked quantity decision inventory
  accessed_at: '2026-10-21T09:41:51Z'
  support: context_only
  summary: Twenty decisions cover all 19 original source rows across main/Fe/A5 stages
    and target pH. Every target ingredient and both stock additions are reconciled;
    quantities and optionality remain source scoped.
  snapshot_sha256: 5f77b5c8b19da6df8e198d6affc581a0b3a2b660645420236e597bde927ee555
- evidence_id: legacy
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Every row for legacy MediaIngredientMech:000170 and CHEBI:63043
  accessed_at: '2026-10-21T09:41:51Z'
  support: context_only
  summary: 'The complete 9077-row pinned CSV has no legacy identifier row; its current
    KNO3 preferred-term entry is [{"label": "KNO3", "match_type": "preferred_term",
    "identifier": "CHEBI:63043", "preferred_term": "KNO3", "ontology_id": "CHEBI:63043",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]. This is a stale secondary
    link, not a failed primary potassium-nitrate identity.'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008520
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding-coverage
  area: grounding
  topic: Exact primary labels and current secondary linkage coverage
  outcome: supported
  summary: '14 unique asserted CHEBI identifiers resolve with exact labels. Primary
    linkage 14/15 (93.33%); verified current secondary linkage 10/15 (66.67%). This
    is a 0–100 ingredient-instance linkage scale, not scientific correctness. Missing
    current secondary keys: []. Legacy links and chemical-form correctness are assessed
    separately.'
  target_ids:
  - CultureMech:008520
  evidence_ids:
  - record
  - mim
  - chebi131527
  - chebi15377
  - chebi26710
  - chebi26836
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi33118
  - chebi3312
  - chebi63036
  - chebi63043
  - chebi75215
  - chebi75836
  - chebi86360
- assessment_id: quantities
  area: quantity
  topic: Every direct, stock, stock-addition and preparation quantity
  outcome: concern
  summary: Twenty decisions cover all 19 original source rows across main/Fe/A5 stages
    and target pH. Every target ingredient and both stock additions are reconciled;
    quantities and optionality remain source scoped.
  target_ids:
  - CultureMech:008520
  evidence_ids:
  - record
  - owner-0
  - quantities
  details: '[{"field_path": "ingredients[0].concentration", "decision": "correct",
    "stage": "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "Distilled water 1 L", "source_locator": "NBRC 1210 main medium;
    exact Distilled water composition/addition entry", "explanation": "Main water
    is 1 L. The recorded 502 g/L adds this numerical 1 to a separate 500 ml Fe-stock
    batch and a separate 1 L A5 batch; these are neither common units nor one preparation
    stage.", "original_source_amount": 1, "original_source_unit": "L", "provider_locator":
    "$.components[0].items[0]", "provider_paragraph": 1}, {"field_path": "ingredients[1].concentration",
    "decision": "correct", "stage": "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "MgSO 4 ·7H 2 O 75 mg", "source_locator": "NBRC 1210 main medium;
    exact MgSO4·7H2O composition/addition entry", "explanation": "Source 75 mg is
    0.075 g for this main recipe, not 75 g/L. Preserve its 1 L water basis without
    claiming a measured final volume.", "original_source_amount": 75, "original_source_unit":
    "mg", "provider_locator": "$.components[0].items[1]", "provider_paragraph": 1},
    {"field_path": "ingredients[2].concentration", "decision": "correct", "stage":
    "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "NaCl 25 mg", "source_locator": "NBRC 1210 main medium; exact
    NaCl composition/addition entry", "explanation": "Source 25 mg is 0.025 g for
    this main recipe, not 25 g/L. Preserve its 1 L water basis without claiming a
    measured final volume.", "original_source_amount": 25, "original_source_unit":
    "mg", "provider_locator": "$.components[0].items[2]", "provider_paragraph": 1},
    {"field_path": "ingredients[3].concentration", "decision": "correct", "stage":
    "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "KH 2 PO 4 175 mg", "source_locator": "NBRC 1210 main medium;
    exact KH2PO4 composition/addition entry", "explanation": "Source 175 mg is 0.175
    g for this main recipe, not 175 g/L. Preserve its 1 L water basis without claiming
    a measured final volume.", "original_source_amount": 175, "original_source_unit":
    "mg", "provider_locator": "$.components[0].items[3]", "provider_paragraph": 1},
    {"field_path": "ingredients[4].concentration", "decision": "correct", "stage":
    "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "K 2 HPO 4 75 mg", "source_locator": "NBRC 1210 main medium; exact
    K2HPO4 composition/addition entry", "explanation": "Source 75 mg is 0.075 g for
    this main recipe, not 75 g/L. Preserve its 1 L water basis without claiming a
    measured final volume.", "original_source_amount": 75, "original_source_unit":
    "mg", "provider_locator": "$.components[0].items[4]", "provider_paragraph": 1},
    {"field_path": "ingredients[5].concentration", "decision": "correct", "stage":
    "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "KNO 3 250 mg", "source_locator": "NBRC 1210 main medium; exact
    KNO3 composition/addition entry", "explanation": "Source 250 mg is 0.25 g for
    this main recipe, not 250 g/L. Preserve its 1 L water basis without claiming a
    measured final volume.", "original_source_amount": 250, "original_source_unit":
    "mg", "provider_locator": "$.components[0].items[5]", "provider_paragraph": 1},
    {"field_path": "ingredients[6].concentration", "decision": "correct", "stage":
    "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "CaCl 2 ·H 2 O 10 mg", "source_locator": "NBRC 1210 main medium;
    exact CaCl2·H2O composition/addition entry", "explanation": "Source 10 mg is 0.01
    g for this main recipe, not 10 g/L. Preserve its 1 L water basis without claiming
    a measured final volume.", "original_source_amount": 10, "original_source_unit":
    "mg", "provider_locator": "$.components[0].items[6]", "provider_paragraph": 1},
    {"field_path": "ingredients[7].concentration", "decision": "correct", "stage":
    "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "Agar (if needed) 15 g", "source_locator": "NBRC 1210 main medium;
    exact Agar (if needed) composition/addition entry", "explanation": "The stated
    15 g agar applies only if needed. Its number is preserved but unconditional solid
    state does not represent the agar-free branch; preserve the conditional family
    explicitly.", "original_source_amount": 15, "original_source_unit": "g", "provider_locator":
    "$.components[0].items[7]", "provider_paragraph": 1}, {"field_path": "solutions[0].concentration",
    "decision": "correct", "stage": "main medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "Fe Solution* 1 ml", "source_locator": "NBRC 1210 main medium;
    exact Fe Solution* composition/addition entry", "explanation": "Source addition
    is 1 ml of the source-specific stock, not 1 g/L. Density is unknown; the currently
    linked MediaDive stock is a different recipe.", "original_source_amount": 1, "original_source_unit":
    "ml", "provider_locator": "$.components[0].items[8]", "provider_paragraph": 1},
    {"field_path": "solutions[1].concentration", "decision": "correct", "stage": "main
    medium", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "A5 Solution** 1 ml", "source_locator": "NBRC 1210 main medium;
    exact A5 Solution** composition/addition entry", "explanation": "Source addition
    is 1 ml of the source-specific stock, not 1 g/L. Density is unknown; the currently
    linked MediaDive stock is a different recipe.", "original_source_amount": 1, "original_source_unit":
    "ml", "provider_locator": "$.components[0].items[9]", "provider_paragraph": 1},
    {"field_path": "ingredients[0].concentration", "decision": "correct", "stage":
    "Fe stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "Distilled water 500 ml", "source_locator": "NBRC 1210 Fe stock
    before its 1 ml addition; exact Distilled water composition/addition entry", "explanation":
    "Keep the source amount, original unit and stage; do not flatten stock preparation
    quantities into receiving-medium concentrations.", "original_source_amount": 500,
    "original_source_unit": "ml", "provider_locator": "$.components[1].items[0]",
    "provider_paragraph": 5}, {"field_path": "ingredients[8].concentration", "decision":
    "correct", "stage": "Fe stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "FeSO 4 ·7H 2 O 1.0 g", "source_locator": "NBRC 1210 Fe stock
    before its 1 ml addition; exact FeSO4·7H2O composition/addition entry", "explanation":
    "Keep the source amount, original unit and stage; do not flatten stock preparation
    quantities into receiving-medium concentrations.", "original_source_amount": 1,
    "original_source_unit": "g", "provider_locator": "$.components[1].items[1]", "provider_paragraph":
    5}, {"field_path": "ingredients[9].concentration", "decision": "not_quantified",
    "stage": "Fe stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "H 2 SO 4 few drops", "source_locator": "NBRC 1210 Fe stock before
    its 1 ml addition; exact H2SO4 composition/addition entry", "explanation": "Retain
    few drops within Fe-stock preparation. No fixed volume, mass, strength or final-medium
    acid concentration is supported.", "original_source_amount": null, "original_source_unit":
    null, "provider_locator": "$.components[1].items[2]", "provider_paragraph": 5},
    {"field_path": "ingredients[0].concentration", "decision": "correct", "stage":
    "A5 stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "Distilled water 1L", "source_locator": "NBRC 1210 A5 stock before
    its 1 ml addition; exact Distilled water composition/addition entry", "explanation":
    "Keep the source amount, original unit and stage; do not flatten stock preparation
    quantities into receiving-medium concentrations.", "original_source_amount": 1,
    "original_source_unit": "L", "provider_locator": "$.components[2].items[0]", "provider_paragraph":
    8}, {"field_path": "ingredients[10].concentration", "decision": "correct", "stage":
    "A5 stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "H 3 BO 3 2.86 g", "source_locator": "NBRC 1210 A5 stock before
    its 1 ml addition; exact H3BO3 composition/addition entry", "explanation": "Keep
    the source amount, original unit and stage; do not flatten stock preparation quantities
    into receiving-medium concentrations.", "original_source_amount": 2.86, "original_source_unit":
    "g", "provider_locator": "$.components[2].items[1]", "provider_paragraph": 8},
    {"field_path": "ingredients[11].concentration", "decision": "correct", "stage":
    "A5 stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "ZnSO 4 ·7H 2 O 222 mg", "source_locator": "NBRC 1210 A5 stock
    before its 1 ml addition; exact ZnSO4·7H2O composition/addition entry", "explanation":
    "Keep the source amount, original unit and stage; do not flatten stock preparation
    quantities into receiving-medium concentrations. Its 222 mg equals 0.222 g within
    the separately prepared stock; this conversion does not make the stock amount
    a final-medium concentration.", "original_source_amount": 222, "original_source_unit":
    "mg", "provider_locator": "$.components[2].items[2]", "provider_paragraph": 8},
    {"field_path": "ingredients[12].concentration", "decision": "correct", "stage":
    "A5 stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "CuSO 4 ·5H 2 O 79 mg", "source_locator": "NBRC 1210 A5 stock
    before its 1 ml addition; exact CuSO4·5H2O composition/addition entry", "explanation":
    "Keep the source amount, original unit and stage; do not flatten stock preparation
    quantities into receiving-medium concentrations. Its 79 mg equals 0.079 g within
    the separately prepared stock; this conversion does not make the stock amount
    a final-medium concentration.", "original_source_amount": 79, "original_source_unit":
    "mg", "provider_locator": "$.components[2].items[3]", "provider_paragraph": 8},
    {"field_path": "ingredients[13].concentration", "decision": "correct", "stage":
    "A5 stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "MnSO 4 ·7H 2 O 2.5 g", "source_locator": "NBRC 1210 A5 stock
    before its 1 ml addition; exact MnSO4·7H2O composition/addition entry", "explanation":
    "Keep the source amount, original unit and stage; do not flatten stock preparation
    quantities into receiving-medium concentrations.", "original_source_amount": 2.5,
    "original_source_unit": "g", "provider_locator": "$.components[2].items[4]", "provider_paragraph":
    8}, {"field_path": "ingredients[14].concentration", "decision": "correct", "stage":
    "A5 stock before its 1 ml addition", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "Na 2 MoO 4 21 mg", "source_locator": "NBRC 1210 A5 stock before
    its 1 ml addition; exact Na2MoO4 composition/addition entry", "explanation": "Keep
    the source amount, original unit and stage; do not flatten stock preparation quantities
    into receiving-medium concentrations. Its 21 mg equals 0.021 g within the separately
    prepared stock; this conversion does not make the stock amount a final-medium
    concentration.", "original_source_amount": 21, "original_source_unit": "mg", "provider_locator":
    "$.components[2].items[5]", "provider_paragraph": 8}, {"field_path": "ph_value",
    "decision": "add", "stage": "main recipe target pH", "source_reference": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1210",
    "source_sha256": "da300ff95547b2c11c191d079dfc8f8ad186afd72d3229d689b0034b1195d7b5",
    "source_quote": "pH 6.0", "source_locator": "NBRC 1210 pH row", "explanation":
    "Both layers omit the source target pH. Do not infer incubation or post-growth
    pH."}]'
- assessment_id: identity
  area: identity
  topic: Exact primary accession and linked stock boundaries
  outcome: concern
  summary: TOGO M1941 and NBRC 1210 agree on A3 identity. Both external stock IDs
    resolve, but their actual recipes conflict with the two explicitly specified NBRC
    stocks. Generic stock names cannot establish equivalence.
  target_ids:
  - CultureMech:008520
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - fe-other
  - a5-other
  - id-search
- assessment_id: forms
  area: grounding
  topic: All source materials and asserted molecular forms
  outcome: concern
  summary: The six main salts and five A5 reagents retain primary formula strings.
    Calcium monohydrate and manganese sulfate heptahydrate are mapped to formulas
    Ca.2Cl and Mn.O4S that omit stated waters. Other source-stated sulfate hydrates
    resolve appropriately. NBRC writes Na2MoO4 without hydrate; do not replace it
    with the different external stock dihydrate. Its imported Organic compound note
    conflicts with its inorganic molybdate structure. Agar remains a mixture without
    an invented molecule ID.
  target_ids:
  - CultureMech:008520
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - chebi3312
  - chebi86360
  - chebi75215
  - mim
- assessment_id: scope
  area: scope
  topic: Conditional agar, classifications and claimed properties
  outcome: concern
  summary: The source expressly permits agar omission, while the target declares SOLID_AGAR
    and retains no separate liquid branch. A chemically specified salt/stock basis
    does not justify carrying generic COMPLEX/UNDEFINED labels across both branches;
    reassess those fields after stock and conditional-agar representation. high_metal
    has no source-backed threshold or separate evidence, and corrupted quantities
    cannot justify it. No target organism, strain, incubation, parent, native variant
    or KG match is asserted.
  target_ids:
  - CultureMech:008520
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
- assessment_id: preparation
  area: completeness
  topic: Source pH and stock qualifiers
  outcome: concern
  summary: pH 6.0 and the Fe-stock few-drops qualifier are absent as usable preparation
    context. The exact NBRC page provides no sterilization or incubation conditions,
    so none is supplied by analogy. Main/stock solvent quantities are separate.
  target_ids:
  - CultureMech:008520
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - quantities
- assessment_id: history
  area: provenance
  topic: Owner correspondence, current code and claim evidence
  outcome: concern
  summary: The complete 14 target and 13 owner events have timezone-bearing timestamps.
    Target history extends owner by the merge event; ingredients and stocks currently
    agree. Dates and fingerprint are lineage metadata, not scientific validation.
    No claim-level source evidence or references are present in the fully read target/owner;
    source links remain only in notes. Exact dependency evidence does not transfer
    across the false stock links.
  target_ids:
  - CultureMech:008520
  evidence_ids:
  - record
  - owner-0
  - writer
  - dep-solution5640
  - dep-solution4987
  - validate-references
findings:
- finding_id: f1
  issue_key: CM008520-source-units-and-stock-stages
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Original units and distinct stock stages are collapsed
  description: Six main milligram values become numerically identical g/L values.
    Fe/A5 stock ingredients are flattened into the medium; their milligram rows have
    the same unit corruption. Two 1 ml stock additions become 1 g/L, and unrelated
    water batches are summed to 502 g/L. These changes materially replace the source
    formulation.
  target_ids:
  - CultureMech:008520
  field_paths:
  - ingredients[*].concentration
  - solutions[*].concentration
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - quantities
  - writer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/a3.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CM008520-false-stock-identities
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Both linked MediaDive stocks differ from NBRC A3
  description: Fe 5640 uses HCl and conflicting Fe-strength representations rather
    than NBRC 1 g FeSO4·7H2O in 500 ml water with sulfuric-acid drops. A5 4987 changes
    manganese salt, molybdate hydration, adds cobalt, and changes boron/copper/zinc
    amounts. Existing exact dependency excerpts cannot establish identity.
  target_ids:
  - CultureMech:008520
  field_paths:
  - solutions[0].term
  - solutions[1].term
  - solutions[*].notes
  - solutions[*].name
  evidence_ids:
  - nbrc
  - fe-other
  - a5-other
  - dep-solution5640
  - dep-solution4987
  - writer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/a3.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: CM008520-hydrate-mapping
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two molecular identifiers omit explicit source hydration
  description: CaCl2·H2O and MnSO4·7H2O names have anhydrous-form ontology structures.
    Canonical label passes do not reconcile those formulas with the supplied materials.
  target_ids:
  - CultureMech:008520
  field_paths:
  - ingredients[6].term
  - ingredients[13].term
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - chebi3312
  - chebi86360
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/a3.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: CM008520-conditional-family-classification
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: The optional-agar family is represented as unconditional solid medium
  description: NBRC says Agar (if needed); the record declares SOLID_AGAR without
    a liquid branch. COMPLEX/UNDEFINED and high_metal also lack reconciled source
    support for the corrected branch-specific composition.
  target_ids:
  - CultureMech:008520
  field_paths:
  - physical_state
  - medium_type
  - composition_type
  - high_metal
  - ingredients[7]
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/a3.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: CM008520-missing-source-ph
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The primary target pH is omitted
  description: Both NBRC and TOGO specify pH 6.0; neither local layer preserves it.
    No primary incubation or sterilization instruction was found in the fully inspected
    exact page.
  target_ids:
  - CultureMech:008520
  field_paths:
  - ph_value
  - preparation_steps
  evidence_ids:
  - nbrc
  - togo
  - record
  - owner-0
  - quantities
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/a3.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: CM008520-secondary-link-and-property-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Legacy linkage and source claims remain weakly represented
  description: KNO3 retains legacy MediaIngredientMech:000170 while ten other secondary
    links use current CHEBI keys. The complete pinned index resolves current potassium
    nitrate but not the legacy identifier. Sodium molybdate is incorrectly described
    as organic in imported notes. Source amounts and conditions have no narrow evidence
    objects.
  target_ids:
  - CultureMech:008520
  field_paths:
  - ingredients[5].mediaingredientmech_term
  - ingredients[14].notes
  - ingredients[*].evidence
  - references
  evidence_ids:
  - legacy
  - mim
  - chebi63043
  - chebi75215
  - nbrc
  - record
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/a3.yaml
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
  description: Restore original units and main/stock boundaries from exact NBRC sections,
    preserving conditional agar and unquantified sulfuric acid. Retain solvent amounts
    as preparation instructions; derive any concentration only from an explicit appropriate
    basis.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008520
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/a3.yaml
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
  description: Replace unsupported cross-stock identity assertions with explicitly
    source-scoped stock representations. Preserve provider internal conflicts and
    do not edit the different dependency recipes to force a match. Replace Unknown
    solution placeholders using verified source names.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008520
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/a3.yaml
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
  description: Resolve exact source hydrate identities without guessing replacements;
    retain explicit unsupported mapping if a verified exact term is unavailable.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008520
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/a3.yaml
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
  description: Represent the source agar condition and reconcile each branch’s physical
    state and composition classification. Require explicit support for high_metal
    rather than quantities corrupted during import.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008520
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/a3.yaml
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
  description: Preserve source target pH and stock-preparation qualifiers with exact
    evidence; do not invent missing sterilization or incubation parameters.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:008520
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/a3.yaml
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
- action_id: a6
  description: Reconcile the legacy link against the pinned current entry, correct
    the unsupported property label, and attach exact primary snippets at their claim/stage.
    Preserve existing history and source dates.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:008520
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/a3.yaml
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
- The two linked MediaDive SolutionRecipe files are dependency context only, not additional
  reviewed targets. Their exact current source excerpts do not establish equivalence
  to NBRC A3 stocks.
- NBRC specifies solvent quantities and additions, not independently measured final
  volumes. Sulfuric-acid strength and drop volume are unreported. No density, final-volume,
  incubation or sterilization default is invented.
- Current TOGO importer and migration code explain representation mechanisms only;
  their current contents are not proof of the exact historical code executed.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-014
- generated-medium
```
