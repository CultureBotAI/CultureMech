# Source and formulation review: 4_yaco_media (CultureMech:009318)

- Review: 20261021T083523Z-culturemech-009318-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T08:29:12Z
- Finished UTC: 2026-10-21T08:35:23Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated 4-YACo record flattens supplement headings and molecular alternatives into 16 ingredients with 15 unspecified amounts, while its later eight-row maintained owner prescribes a combined supplement treatment that the cited study does not establish as the basal recipe. Source quantities can be compared only with their experimental context: the captured maltose unit is unresolved, the yeast percentage has no stated mass/volume basis, and the B6 dose allocation between named forms is unclear. Several chemical assertions exceed source specificity, and the generated record omits later conditions and references. The available paper supports bounded findings, but exact original typography and the complete referenced basal formulation remain unresolved.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 103; batch 011 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding ten task batches contain 100 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 102 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009318 | data/merge_yaml/merged/4_yaco_media.yaml | generated | 4_yaco_media |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009318 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009318 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-011/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch011/103/strict.tsv |
| validate-terms | passed | True | CultureMech:009318 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009318 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009318 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Original unit typography and complete basal formulation | unavailable | True | CultureMech:009318 | Primary HTML is available, but exact maltose-unit typography remains unresolved after the retained publisher/XML/PDF routes. The separately cited basal formulation was not independently recovered; no claim is made that its endpoint is inaccessible. Review is partial for these required source questions. |
| Target and owner history timestamp syntax | passed | False | CultureMech:009318 | 18 timestamp values across both full records parse with explicit timezones; provenance syntax only. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009318.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: concern. Targets: CultureMech:009318.

7 primary CHEBI identities resolve with matching labels; 2 of 3 current secondary keys have live pinned-index rows. Unresolved keys: ['CHEBI:18167']. Resolution does not validate the source-level pyridoxine assignment, maltose anomer or owner-only L-tryptophan label; these are assessed separately.

16 direct ingredient instances; CHEBI-primary instance linkage 7/16 (43.75%), verified secondary coverage 2/16 (12.50%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Source identity and exact maintained owner

identity: supported. Targets: CultureMech:009318.

Stable ID CultureMech:009318 and TOGO:M2770 identify the same named medium in both layers. The merge event identifies one maintained bacterial owner. The current provider retains its supplement hierarchy; publication identity is independently corroborated. Correct accession identity does not make every flattened ingredient or later repair assertion source-supported.

### All 16 target rows and all eight owner rows

quantity: concern. Targets: CultureMech:009318.

Every row is traced below. Fifteen target amounts are VARIABLE. Some source quantities are recoverable with nominal culture-volume context, but the maltose unit, yeast percentage basis and B6 amount allocation remain unresolved. No stock solutions or external stock references are asserted, and the main-section self references are headings rather than independent stock recipes.

[{"target_field": "ingredients[0]", "material": "yeast autolysate", "target_concentration": {"value": "4", "unit": "PERCENT_W_V"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[0]", "owner_concentration": {"value": "4", "unit": "PERCENT_W_V"}, "source_quantity_or_relation": "4%; percentage basis not specified", "source_locator": "$.components[0].items[0]; $.comments[0]; sec3 p1", "assessment": "The numerical 4 is supported; PERCENT_W_V is more specific than either capture."}, {"target_field": "ingredients[1]", "material": "maltose", "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[1]", "owner_concentration": {"value": "20", "unit": "MILLIMOLAR"}, "source_quantity_or_relation": "literal 20 m; unit unresolved", "source_locator": "$.components[0].items[1]; $.comments[0]; sec3 p1", "assessment": "Target VARIABLE preserves no amount; owner 20 MILLIMOLAR is not verified by this typography. Alpha form is not specified."}, {"target_field": "ingredients[2]", "material": "carbon dioxide", "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[3]", "owner_concentration": {"value": "20", "unit": "PERCENT_V_V"}, "source_quantity_or_relation": "20% of headspace", "source_locator": "$.components[0].items[2]; $.comments[0]; sec3 p1", "assessment": "Source gas-phase proportion; owner records headspace. Do not treat as dissolved concentration or infer pressure."}, {"target_field": "ingredients[3]", "material": "hydrogen", "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[2]", "owner_concentration": {"value": "80", "unit": "PERCENT_V_V"}, "source_quantity_or_relation": "80% of headspace", "source_locator": "$.components[0].items[3]; $.comments[0]; sec3 p1", "assessment": "Source gas-phase proportion; owner records headspace. Do not derive a liquid concentration."}, {"target_field": "ingredients[4]", "material": "B7 heading", "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[4]", "owner_concentration": {"value": "60-100", "unit": "MICROG_PER_L"}, "source_quantity_or_relation": "same biotin supplement as target row8", "source_locator": "$.components[0].items[4]; $.components[1]; sec3 p2", "assessment": "Heading is not a second biotin dose."}, {"target_field": "ingredients[5]", "material": "B6 heading", "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[5]", "owner_concentration": {"value": "24-40", "unit": "MG_PER_L"}, "source_quantity_or_relation": "120–200 micrograms per tube names two forms with unresolved allocation", "source_locator": "$.components[0].items[5]; $.comments[2]; sec3 p3", "assessment": "24–40 mg/L is arithmetic for the stated mass per nominal 5 mL only; not established as combined-family total or independent dose for each. Pyridoxine is not named."}, {"target_field": "ingredients[6]", "material": "B12/corrinoid heading", "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[6]", "owner_concentration": {"value": "6-10", "unit": "MG_PER_L"}, "source_quantity_or_relation": "30–50 micrograms per tube of one selected named form", "source_locator": "$.components[0].items[6]; $.comments[3]; sec3 p4", "assessment": "6–10 mg/L conditional on nominal 5 mL applies to one chosen form; not a sum of four forms plus heading."}, {"target_field": "ingredients[7]", "material": "tryptophan heading", "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[7]", "owner_concentration": {"value": "12-20", "unit": "MG_PER_L"}, "source_quantity_or_relation": "same supplement as target row15", "source_locator": "$.components[0].items[7]; $.components[4]; sec3 p5", "assessment": "Heading is not a second dose; owner L specificity is unsupported."}, {"target_field": "ingredients[8]", "material": "biotin (supplier named)", "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[4]", "owner_concentration": {"value": "60-100", "unit": "MICROG_PER_L"}, "source_quantity_or_relation": "0.3–0.5 micrograms per tube", "source_locator": "$.components[1].items[0]; $.comments[1]; sec3 p2", "assessment": "0.3–0.5 micrograms /0.005 L = 60–100 micrograms/L conditionally; owner arithmetic agrees. Inclusion depends on treatment."}, {"target_field": "ingredients[9]", "material": "pyridoxal-phosphate", "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[5]", "owner_concentration": {"value": "24-40", "unit": "MG_PER_L"}, "source_quantity_or_relation": "one of the two B6 forms named together", "source_locator": "$.components[2].items[0]; $.comments[2]; sec3 p3", "assessment": "Source uses and between forms; no exclusive alternative, each-dose allocation or combined total is verified."}, {"target_field": "ingredients[10]", "material": "pyridoxal-HCl", "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[5]", "owner_concentration": {"value": "24-40", "unit": "MG_PER_L"}, "source_quantity_or_relation": "other B6 form named together", "source_locator": "$.components[2].items[1]; $.comments[2]; sec3 p3", "assessment": "Preserve hydrochloride identity and unresolved allocation; do not equate with pyridoxine."}, {"target_field": "ingredients[11]", "material": "hydroxocobalamin acetate salt", "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[6]", "owner_concentration": {"value": "6-10", "unit": "MG_PER_L"}, "source_quantity_or_relation": "one of four corrinoid alternatives", "source_locator": "$.components[3].items[0]; $.comments[3]; sec3 p4", "assessment": "6–10 mg/L conditional dose applies only if this form is chosen; preserve salt form."}, {"target_field": "ingredients[12]", "material": "hydroxocobalamin hydrochloride", "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[6]", "owner_concentration": {"value": "6-10", "unit": "MG_PER_L"}, "source_quantity_or_relation": "one of four corrinoid alternatives", "source_locator": "$.components[3].items[1]; $.comments[3]; sec3 p4", "assessment": "6–10 mg/L conditional dose applies only if this form is chosen; preserve hydrochloride."}, {"target_field": "ingredients[13]", "material": "methylcobalamin", "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[6]", "owner_concentration": {"value": "6-10", "unit": "MG_PER_L"}, "source_quantity_or_relation": "one of four corrinoid alternatives", "source_locator": "$.components[3].items[2]; $.comments[3]; sec3 p4", "assessment": "6–10 mg/L conditional dose applies only if this form is chosen."}, {"target_field": "ingredients[14]", "material": "cyanocobalamin (supplier named)", "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[6]", "owner_concentration": {"value": "6-10", "unit": "MG_PER_L"}, "source_quantity_or_relation": "one of four corrinoid alternatives", "source_locator": "$.components[3].items[3]; $.comments[3]; sec3 p4", "assessment": "6–10 mg/L conditional dose applies only if this form is chosen."}, {"target_field": "ingredients[15]", "material": "tryptophan (supplier named)", "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[7]", "owner_concentration": {"value": "12-20", "unit": "MG_PER_L"}, "source_quantity_or_relation": "60–100 micrograms per tube", "source_locator": "$.components[4].items[0]; $.comments[4]; sec3 p5", "assessment": "60–100 micrograms /0.005 L = 12–20 mg/L conditionally; owner arithmetic agrees but L form is not established."}]

### Basal medium versus experimental supplement treatments

representation: concern. Targets: CultureMech:009318.

The generated list duplicates B7 and tryptophan headings with named ingredients, retains B6 forms alongside an unsupported pyridoxine heading, and flattens four explicitly alternative corrinoids. The later owner improves the hierarchy and preserves the corrinoid choice in notes, but its preparation_steps[1] commands all four supplement families together. The study distinguishes base cultures and supplementation experiments; no single universal combined treatment is established.

### Molecular forms, source specificity and owner linkages

grounding: concern. Targets: CultureMech:009318.

All seven asserted target primary CHEBI IDs have matching current canonical labels. This does not establish source suitability: pyridoxine is not either named pyridoxal form, alpha-maltose exceeds the source anomer scope, and owner L-tryptophan exceeds both the generic source name and its generic term. Vitamin B12 is a family term and must not become an extra molecular dose. Owner B6/B12 families deliberately lack IDs; no pure-molecule replacement is inferred. The maltose secondary key is unresolved in both local layers.

Primary target linkage: 7/16 ingredients (43.75%). Target live secondary linkage: 2/16 (12.50%), from 3 asserted keys. Owner primary linkage: 5/8 (62.50%); owner live secondary linkage: 4/8 (50.00%), from 5 asserted keys. Linkage percentages measure index presence, not chemical/source correctness.

### Culture context and preparation provenance

completeness: concern. Targets: CultureMech:009318.

The owner retains gas headspace, nominal culture/vessel volumes, darkness and room-temperature wording from the methods. The generated target omits those conditions and all preparation steps, leaving gases as unspecified ingredient rows. Source headspace context supports an oxygen-free atmosphere but not an invented dissolved dose, pressure or numeric incubation temperature. No source pH or sterilization instruction is established in the captured media subsection. The owner initial preparation and universal-supplement steps also require the unresolved source and treatment qualifications above.

### Mixtures, physical state and organism-claim boundary

scope: supported. Targets: CultureMech:009318.

Yeast autolysate supports COMPLEX/UNDEFINED classification and the described liquid cultures support LIQUID. The paper names Treponema primitia ZAS-2 and Treponema azotonutricium ZAS-9 in this study; these are publication-era contextual names, not newly assigned taxonomy IDs or broader species-growth claims. Background organisms, transcriptomic pathways and response comparisons are not transferred into recipe assertions. Neither local layer currently asserts a named target organism.

### Later maintained repair versus stale generated representation

ownership: concern. Targets: CultureMech:009318.

The target preserves the older sixteen-row representation, whereas the owner and its documented September repair use eight rows, conditions and two references. The owner is the maintained correction surface, but its unit, molecular-scope and treatment assertions must be reviewed before regeneration. Do not copy the later owner wholesale as an approved recipe or infer a defect in unexecuted current merging.

### Citation placement and source-access limits

evidence: concern. Targets: CultureMech:009318.

The generated record has no structured references; its passing reference command checked zero references. The owner has TOGO and DOI references and per-ingredient source prose, but no claim-level excerpts or variant-specific evidence for its inferred unit, stereochemistry or combined treatment. The PMC capture verifies publication content while the unavailable alternate representations and unrecovered basal recipe bound completion.

## Findings

### f1: Supplement headings and treatment alternatives are presented as one formula

blocker / open / confirmed; issue key: cm009318-supplement-treatments-flattened.

The target lists self-referential supplement headings alongside their named forms, duplicates biotin and tryptophan, and presents four explicitly alternative corrinoids as independent ingredients. The later owner collapses these entries, but its preparation_steps[1] instructs a combined B7/B6/B12/tryptophan treatment for every culture. The article distinguishes the base medium and experimental supplementation; no single formulation corresponding to either all listed rows or that universal combined instruction is established. This blocks faithful recipe interpretation and export under one formulation.

### f2: Percentage, maltose unit and B6 allocation exceed the captured evidence

major / open / confirmed; issue key: cm009318-unverified-unit-and-dose-bases.

Both layers assert PERCENT_W_V for yeast autolysate although the sources specify only 4%. The owner ingredients[1], notes and preparation_steps[0] assert 20 MILLIMOLAR even though both captured source representations leave a literal lowercase m. That unit is unverified, not proven false. Owner ingredients[5] assigns 24–40 mg/L to an opaque B6 family even though the 120–200 microgram wording does not resolve allocation between its two named forms. Other per-liter supplement arithmetic is valid only on the reported nominal 5 mL culture basis and within the relevant treatment.

### f3: Chemical assertions are more specific than the named source materials

major / open / confirmed; issue key: cm009318-source-molecular-scope-mismatches.

Target ingredients[5] identifies the B6 heading as pyridoxine CHEBI:16709, while the source names pyridoxal-HCl and pyridoxal-phosphate. Both layers identify generic source maltose as alpha-maltose CHEBI:18167 without anomer evidence. The maintained owner ingredients[7].preferred_term further asserts L-tryptophan although the source and CHEBI:27897 term are generic. Canonical labels resolve, but these source-form assertions are unsupported.

### f4: The maltose secondary key has no current pinned MIM row

major / open / confirmed; issue key: cm009318-unresolved-maltose-secondary-key.

Both local layers assert CHEBI:18167 as a MediaIngredientMech secondary link. A complete read of the pinned index finds no row with that exact identifier, although the ontology term itself resolves. Only two of three target secondary keys and four of five owner keys have live preferred-term rows. This is a linkage defect independent of the source anomer question.

### f5: The generated target omits documented gas and culture context

major / open / confirmed; issue key: cm009318-generated-conditions-absent.

The generated target has unspecified gas ingredient amounts and no aeration, vessel, temperature or preparation fields. The current owner retains the source 80% H2/20% CO2 headspace, nominal 5 mL cultures in 25 mL vessels, darkness and room-temperature context. These fields help distinguish gas-phase supply and source-specific conditions, but must be preserved alongside correction of the owner unit/treatment assumptions.

### f6: Generated references and claim-level qualifications are missing

minor / open / confirmed; issue key: cm009318-source-evidence-not-retained.

The generated target retains a TOGO note but omits the owner two references and per-ingredient source prose. The owner references alone do not support every inferred quantity, form or treatment. The target reference check passes with zero references; neither that result nor historical curated flags provide scientific validation.

## Recommended Actions And Acceptance Checks

### a1

Review the maintained owner and represent the basal medium and supported supplementation variants separately. Remove heading/material double counting, preserve the explicit one-form corrinoid choice, and retain B6 allocation uncertainty. Correct owner preparation_steps[1]; do not infer an exclusive B6 alternative or universally required cocktail. Recover the referenced basal formulation before claiming a complete recipe, then regenerate the target.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the source 4% without an unsupported mass/volume basis; independently recover original maltose typography before retaining or changing 20 mM. Resolve or explicitly retain B6 allocation uncertainty rather than treating the family dose as a known total. Keep original per-tube amounts and the conditional nominal-volume calculations as separate evidence. Amend owner notes and preparation text, append a clarification to provenance, and regenerate after source review.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Correct the maintained molecular scope using independently supported forms, retaining named hydrochloride/phosphate distinctions and uncertain stereochemistry. Do not add pyridoxine as another source ingredient or silently invent replacement IDs. Resolve target-only stale assertions through verified owner correction and regeneration; owner-only L naming requires explicit source support or qualification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Reconcile the maintained maltose secondary link against the pinned MIM release after establishing source chemical scope. Verify the exact accepted key and canonical label or retain the link as unresolved; do not replace it solely from a similar label. Regenerate and check exact secondary-key availability.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

After correcting and verifying the maintained formulation, regenerate to preserve source-scoped headspace, culture/vessel volume and qualitative conditions. Keep gas proportions in their headspace context; do not infer liquid concentrations, pressure, numeric temperature, pH or sterilization. Ensure the revised preparation does not prescribe an unsupported combined treatment.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Add concise claim-level support for the exact source recipe/treatment, original amounts, conditional calculations, chemical-form limits and unavailable source questions in the maintained owner; preserve and propagate appropriate references. Append a correction event while retaining every historical event unchanged.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/4_yaco_media.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/4_yaco_media.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/4_yaco_media.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/4_yaco_media.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch011/103/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-011/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch011/103/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/4_yaco_media.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/4_yaco_media.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/4_yaco_media.yaml:1:id: CultureMech:009318<br>./data/normalized_yaml/bacterial/4_yaco_media.yaml:1:id: CultureMech:009318<br> |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2770; $.meta; $.components[0:5]; $.comments[0:5] | supports | M2770 identifies 4-YACo media with an empty original-source URL. It has eight main entries, including four self-referential supplement headings, followed by four named supplement sections. Comments retain the methods quantities and context; most component rows themselves have no numerical amount. This hierarchy is not a list of 16 independently dosed ingredients. |
| paper-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fismej.2011.3&amp;format=json&amp;resultType=core; $.resultList.result[0] | supports | The DOI identifies Rosenthal, Matson, Eldar and Leadbetter (2011), RNA-seq reveals cooperative metabolic interactions between two termite-gut spirochete species in co-culture; PMID 21326336 and PMCID PMC3146290. This identifies the publication, not a unique supplement treatment. |
| paper-methods | https://pmc.ncbi.nlm.nih.gov/articles/PMC3146290/; section#sec3, direct paragraphs 1–5 | supports | The culture-media methods distinguish the named base and gas headspace from vitamin/amino-acid/cofactor preparations. They give nominal 5 mL cultures, 25 mL vessels, darkness and room temperature. Supplement amounts are specified per culture tube; the B12/corrinoid paragraph selects one of four named forms. |
| paper-treatment-scope | https://pmc.ncbi.nlm.nih.gov/articles/PMC3146290/; section#sec8, direct paragraphs 3 and 8; figure#fig2 caption; section#sec3 | supports | The results describe the base-medium cultures separately from later candidate-factor supplementation experiments. Figure 2 discusses particular supplement combinations. This does not support requiring all four supplement families in every culture. The coenzyme-A discussion supplies no dose in the captured culture-media methods, so no missing universal ingredient or quantity is inferred. |
| paper-basal-limit | https://pmc.ncbi.nlm.nih.gov/articles/PMC3146290/; section#sec8, direct paragraph 3; reference#bib15; section#sec3 | partial | The base-medium context cites Graber et al. 2004. The captured 2011 methods identify the medium and supplements but do not independently establish every basal constituent, its preparation or a final-volume basis. The separate cited basal recipe was not recovered in this review. |
| maltose-typography | https://pmc.ncbi.nlm.nih.gov/articles/PMC3146290/; section#sec3 &gt; p:first-of-type, first sentence; raw UTF-8 byte offset 58725 | partial | Raw HTML and its text node contain the number 20, U+2009 thin space, and lowercase m before maltose. The literal unit is not expanded by tags, hidden M, entity, superscript or MathML in that passage; the TOGO comment likewise leaves lowercase m. The maintained 20 MILLIMOLAR assertion is therefore unverified, not demonstrated false. |
| publisher-unavailable | https://doi.org/10.1038/ismej.2011.3; Exact retained response body | unknown | The DOI route resolved to the publisher but returned HTTP403; no primary page body was recovered by this request. |
| xml-unavailable | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3146290/fullTextXML; Exact retained response body | unknown | The Europe PMC full-text XML request returned HTTP500; no source XML was recovered. |
| pdf-unavailable | https://pmc.ncbi.nlm.nih.gov/articles/PMC3146290/pdf/ismej20113a.pdf; Exact retained response body | unknown | The nominal article-PDF URL returned HTTP200 with an HTML download interstitial, not PDF bytes. Original PDF typography was not recovered. |
| supplement-unavailable | https://pmc.ncbi.nlm.nih.gov/articles/instance/3146290/bin/ismej20113x1.pdf; Exact retained response body | unknown | The nominal supplementary-PDF URL returned HTTP200 with an HTML download interstitial, not the supplement contents. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15956 resolves to biotin and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:16526 resolves to carbon dioxide and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi16709 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16709; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:16709 resolves to pyridoxine and is not obsolete. This verifies identifier/label correspondence only; source chemical form and stereochemical scope require the separate comparison in this review. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:176843 resolves to vitamin B12 and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi18167 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18167; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:18167 resolves to alpha-maltose and is not obsolete. This verifies identifier/label correspondence only; source chemical form and stereochemical scope require the separate comparison in this review. |
| chebi18276 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18276; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:18276 resolves to dihydrogen and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi27897 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27897; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:27897 resolves to tryptophan and is not obsolete. This verifies identifier/label correspondence only; source chemical form and stereochemical scope require the separate comparison in this review. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | context_only | {"CHEBI:18167": [], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:27897": [{"label": "Tryptophan", "match_type": "preferred_term", "identifier": "CHEBI:27897", "preferred_term": "Tryptophan", "ontology_id": "CHEBI:27897", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}; Unresolved current secondary keys: ['CHEBI:18167'] |
| owner-mim | src/culturemech/data/mediaingredientmech/label_index.csv; All owner secondary keys; complete CSV read including ignored file; pinned metadata in source.inputs | supports | Four of five owner secondary keys have live preferred-term rows; CHEBI:18167 has no exact identifier row in the pinned index. Target linkage is two of three asserted secondary keys. This is a local MIM linkage defect, not evidence that CHEBI:18167 is an invalid ontology term. No nearby maltose key is silently substituted. {"CHEBI:18167": [], "CHEBI:18276": [{"label": "Hydrogen gas", "match_type": "preferred_term", "identifier": "CHEBI:18276", "preferred_term": "Hydrogen gas", "ontology_id": "CHEBI:18276", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16526": [{"label": "Carbon dioxide gas", "match_type": "preferred_term", "identifier": "CHEBI:16526", "preferred_term": "Carbon dioxide gas", "ontology_id": "CHEBI:16526", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27897": [{"label": "Tryptophan", "match_type": "preferred_term", "identifier": "CHEBI:27897", "preferred_term": "Tryptophan", "ontology_id": "CHEBI:27897", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]} |
| chemical-forms | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16709; Exact term description and molecular annotations | supports | CHEBI:16709 is pyridoxine, the methanol form of B6. The source names pyridoxal-HCl and pyridoxal-phosphate, so its generic B6 heading does not justify pyridoxine as another ingredient. |
| maltose-form | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18167; Exact term description and stereochemical annotations | supports | CHEBI:18167 specifically asserts the alpha configuration at the reducing-end anomeric centre. The paper and provider name maltose without that specification. Neither a different replacement ID nor a hydrate is verified here. |
| tryptophan-form | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27897; Exact term description, InChI and SMILES | supports | CHEBI:27897 is the generic tryptophan term. Its annotations do not specify the owner-only L designation, and the captured methods likewise name generic tryptophan. The source does not establish the enantiomer. |
| repair-context | scripts/repair_togo_m2770_4_yaco_score15.py; INGREDIENTS; PREPARATION_STEPS; NOTES; repair_record; _append_curation_event | supports | Read the complete current repair script without running it. It explicitly supplies 20 MILLIMOLAR, the combined supplementation instruction, L-tryptophan and condition/reference fields seen in the later owner. This establishes those maintained assertions and their local repair context, not independent source verification. No current generic importer or merge path was replayed. |
| history | data/merge_yaml/merged/4_yaco_media.yaml; All nine target and nine owner curation_history timestamps; owner September repair event | supports | All 18 scoped timestamps parse with explicit timezone offsets. The owner history records a past repair interpretation and must remain preserved as provenance; later correction requires an appended clarification, not rewriting that event. Syntax and a curated flag do not establish scientific approval. |

## Limits And Additional Notes

- The primary PMC HTML for DOI 10.1038/ismej.2011.3 is available and was inspected. Its maltose text literally says 20 m, with a thin space and lowercase m; no hidden capital M or unit markup was recovered. The publisher DOI route returned 403, Europe PMC full-text XML returned 500, and purported PDF/supplement routes returned HTML interstitials. Neither 20 mM nor another molarity is verified; this does not prove 20 mM false.
- The article refers to Graber et al. 2004 for the 4YACo basal-medium context. That cited basal formulation was not independently recovered in this bounded review, and no access attempt or remote unavailability claim is made for that separate article. The available methods do not justify treating yeast autolysate and maltose as a complete independently reconstructed basal recipe.
- Per-liter supplement arithmetic is conditional on the reported nominal 5 mL culture volume, not a measured post-addition final volume. B6 wording does not resolve whether its stated amount applies to each form or a combined amount. Corrinoids are explicitly one chosen form. These conversions do not establish universal inclusion or an optimized recipe.
- Publication-era species names and strain designations are contextual only. No current taxonomy identifier, strain accession, new growth assertion, preferred supplement choice, or experimental optimization is proposed. No pH, numeric room-temperature value, gas pressure, unreported stock recipe or sterilization step is inferred.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T083523Z-culturemech-009318-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 4_yaco_media (CultureMech:009318)'
started_at: '2026-10-21T08:29:12Z'
finished_at: '2026-10-21T08:35:23Z'
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
summary: 'The generated 4-YACo record flattens supplement headings and molecular alternatives
  into 16 ingredients with 15 unspecified amounts, while its later eight-row maintained
  owner prescribes a combined supplement treatment that the cited study does not establish
  as the basal recipe. Source quantities can be compared only with their experimental
  context: the captured maltose unit is unresolved, the yeast percentage has no stated
  mass/volume basis, and the B6 dose allocation between named forms is unclear. Several
  chemical assertions exceed source specificity, and the generated record omits later
  conditions and references. The available paper supports bounded findings, but exact
  original typography and the complete referenced basal formulation remain unresolved.'
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
  - path: data/merge_yaml/merged/4_yaco_media.yaml
    sha256: e7f0dfe49059ad2dcf92002d5e19338762a30c3780b66373a175894081b70424
    role: target
  - path: data/normalized_yaml/bacterial/4_yaco_media.yaml
    sha256: 5e97be36ddd81738729b8b941d98e1d29acd42a61ab3fb661971c0baff01727e
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
  - path: scripts/repair_togo_m2770_4_yaco_score15.py
    sha256: 82754336ca05790a1bdb2378cd3cbac8e3c27b5ae0412ba2c6af34dd82ec59ef
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
  selection: Task review 103; batch 011 item 3 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding ten task batches contain
    100 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 102 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009318
targets:
- target_id: CultureMech:009318
  path: data/merge_yaml/merged/4_yaco_media.yaml
  label: 4_yaco_media
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/4_yaco_media.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/4_yaco_media.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009318
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/4_yaco_media.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch011/103/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-011/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch011/103/strict.tsv"
  target_ids:
  - CultureMech:009318
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/4_yaco_media.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009318
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/4_yaco_media.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009318
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
  - CultureMech:009318
- check_id: source-typography-and-basal-scope
  name: Original unit typography and complete basal formulation
  required: true
  status: unavailable
  summary: Primary HTML is available, but exact maltose-unit typography remains unresolved
    after the retained publisher/XML/PDF routes. The separately cited basal formulation
    was not independently recovered; no claim is made that its endpoint is inaccessible.
    Review is partial for these required source questions.
  target_ids:
  - CultureMech:009318
  evidence_ids:
  - paper-methods
  - maltose-typography
  - paper-basal-limit
  - publisher-unavailable
  - xml-unavailable
  - pdf-unavailable
  - supplement-unavailable
- check_id: scoped-history-timestamps
  name: Target and owner history timestamp syntax
  required: false
  status: passed
  summary: 18 timestamp values across both full records parse with explicit timezones;
    provenance syntax only.
  target_ids:
  - CultureMech:009318
  evidence_ids:
  - history
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/4_yaco_media.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T08:35:22Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/4_yaco_media.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T08:35:22Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/4_yaco_media.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:30:47.919628Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/4_yaco_media.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch011/103/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T08:30:53.112895Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-011/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch011/103/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/4_yaco_media.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:30:59.183036Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/4_yaco_media.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T08:31:02.435319Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T08:35:22Z'
  support: supports
  summary: './data/merge_yaml/merged/4_yaco_media.yaml:1:id: CultureMech:009318

    ./data/normalized_yaml/bacterial/4_yaco_media.yaml:1:id: CultureMech:009318

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2770
  locator: $.meta; $.components[0:5]; $.comments[0:5]
  accessed_at: '2026-10-21T08:17:25.525614Z'
  support: supports
  summary: M2770 identifies 4-YACo media with an empty original-source URL. It has
    eight main entries, including four self-referential supplement headings, followed
    by four named supplement sections. Comments retain the methods quantities and
    context; most component rows themselves have no numerical amount. This hierarchy
    is not a list of 16 independently dosed ingredients.
  snapshot_sha256: f1813929222eb545facde1e1ea634e68b498ea29441b9051978e4223bc69f850
- evidence_id: paper-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fismej.2011.3&format=json&resultType=core
  locator: $.resultList.result[0]
  accessed_at: '2026-10-21T08:17:25.770932Z'
  support: supports
  summary: The DOI identifies Rosenthal, Matson, Eldar and Leadbetter (2011), RNA-seq
    reveals cooperative metabolic interactions between two termite-gut spirochete
    species in co-culture; PMID 21326336 and PMCID PMC3146290. This identifies the
    publication, not a unique supplement treatment.
  snapshot_sha256: db58a8a55da2ef515e4476cba6103825052b5aedc990de112bf56b147af62b9c
- evidence_id: paper-methods
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3146290/
  locator: section#sec3, direct paragraphs 1–5
  accessed_at: '2026-10-21T08:19:33.044238Z'
  support: supports
  summary: The culture-media methods distinguish the named base and gas headspace
    from vitamin/amino-acid/cofactor preparations. They give nominal 5 mL cultures,
    25 mL vessels, darkness and room temperature. Supplement amounts are specified
    per culture tube; the B12/corrinoid paragraph selects one of four named forms.
  snapshot_sha256: 2c76242665dc90f5e7336505b7354b374a5b083ef6eac51a2213a5e747bb076c
- evidence_id: paper-treatment-scope
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3146290/
  locator: section#sec8, direct paragraphs 3 and 8; figure#fig2 caption; section#sec3
  accessed_at: '2026-10-21T08:19:33.044238Z'
  support: supports
  summary: The results describe the base-medium cultures separately from later candidate-factor
    supplementation experiments. Figure 2 discusses particular supplement combinations.
    This does not support requiring all four supplement families in every culture.
    The coenzyme-A discussion supplies no dose in the captured culture-media methods,
    so no missing universal ingredient or quantity is inferred.
  snapshot_sha256: 2c76242665dc90f5e7336505b7354b374a5b083ef6eac51a2213a5e747bb076c
- evidence_id: paper-basal-limit
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3146290/
  locator: section#sec8, direct paragraph 3; reference#bib15; section#sec3
  accessed_at: '2026-10-21T08:19:33.044238Z'
  support: partial
  summary: The base-medium context cites Graber et al. 2004. The captured 2011 methods
    identify the medium and supplements but do not independently establish every basal
    constituent, its preparation or a final-volume basis. The separate cited basal
    recipe was not recovered in this review.
  snapshot_sha256: 2c76242665dc90f5e7336505b7354b374a5b083ef6eac51a2213a5e747bb076c
- evidence_id: maltose-typography
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3146290/
  locator: section#sec3 > p:first-of-type, first sentence; raw UTF-8 byte offset 58725
  accessed_at: '2026-10-21T08:19:33.044238Z'
  support: partial
  summary: Raw HTML and its text node contain the number 20, U+2009 thin space, and
    lowercase m before maltose. The literal unit is not expanded by tags, hidden M,
    entity, superscript or MathML in that passage; the TOGO comment likewise leaves
    lowercase m. The maintained 20 MILLIMOLAR assertion is therefore unverified, not
    demonstrated false.
  quote: 20 m maltose
  snapshot_sha256: 2c76242665dc90f5e7336505b7354b374a5b083ef6eac51a2213a5e747bb076c
- evidence_id: publisher-unavailable
  kind: search
  reference: https://doi.org/10.1038/ismej.2011.3
  locator: Exact retained response body
  accessed_at: '2026-10-21T08:17:23.768571Z'
  support: unknown
  summary: The DOI route resolved to the publisher but returned HTTP403; no primary
    page body was recovered by this request.
  snapshot_sha256: 02bab7856bce7edf2c67d1b7db412eb188a91218ea021eb34e27ba193e18b820
  search_scope: Exact public request and retained response body at the stated access
    time; no exhaustive absence claim or local-file search is implied.
- evidence_id: xml-unavailable
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3146290/fullTextXML
  locator: Exact retained response body
  accessed_at: '2026-10-21T08:19:33.557657Z'
  support: unknown
  summary: The Europe PMC full-text XML request returned HTTP500; no source XML was
    recovered.
  snapshot_sha256: 2750418adec882053390accd5c73d48b1dfa93852d6ecb5d61060c71d7968dbd
  search_scope: Exact public request and retained response body at the stated access
    time; no exhaustive absence claim or local-file search is implied.
- evidence_id: pdf-unavailable
  kind: search
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3146290/pdf/ismej20113a.pdf
  locator: Exact retained response body
  accessed_at: '2026-10-21T08:20:10.849205Z'
  support: unknown
  summary: The nominal article-PDF URL returned HTTP200 with an HTML download interstitial,
    not PDF bytes. Original PDF typography was not recovered.
  snapshot_sha256: 88793046ee918a31ef187170a3bf5a637d99073270c3192d7df6c489ec9bede2
  search_scope: Exact public request and retained response body at the stated access
    time; no exhaustive absence claim or local-file search is implied.
- evidence_id: supplement-unavailable
  kind: search
  reference: https://pmc.ncbi.nlm.nih.gov/articles/instance/3146290/bin/ismej20113x1.pdf
  locator: Exact retained response body
  accessed_at: '2026-10-21T08:20:11.099629Z'
  support: unknown
  summary: The nominal supplementary-PDF URL returned HTTP200 with an HTML download
    interstitial, not the supplement contents.
  snapshot_sha256: fb01cdc1f74c59ea6e75009a469b5a7ac079f94abf555f17b32ec21df41fde8d
  search_scope: Exact public request and retained response body at the stated access
    time; no exhaustive absence claim or local-file search is implied.
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:26.163642Z'
  support: supports
  summary: CHEBI:15956 resolves to biotin and is not obsolete. This verifies the asserted
    generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond
    the record is inferred.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16526
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:26.337128Z'
  support: supports
  summary: CHEBI:16526 resolves to carbon dioxide and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi16709
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16709
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:26.473529Z'
  support: supports
  summary: CHEBI:16709 resolves to pyridoxine and is not obsolete. This verifies identifier/label
    correspondence only; source chemical form and stereochemical scope require the
    separate comparison in this review.
  snapshot_sha256: 520ccaa52464e36a60d2a7f103f96537c2ab4915c9e10dc40817a76db6469e29
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: CHEBI:176843 resolves to vitamin B12 and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi18167
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18167
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:27.439061Z'
  support: supports
  summary: CHEBI:18167 resolves to alpha-maltose and is not obsolete. This verifies
    identifier/label correspondence only; source chemical form and stereochemical
    scope require the separate comparison in this review.
  snapshot_sha256: e5f8ffe560badeedcb0ca1b3895a1cbb9913d56e11224fa91ffb77fa8a383199
- evidence_id: chebi18276
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18276
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:27.615173Z'
  support: supports
  summary: CHEBI:18276 resolves to dihydrogen and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 47a32d9cfe41e3759385a0e4e002e9fa208fe1511d84e3d0d1f9f1ca9ce6e86d
- evidence_id: chebi27897
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27897
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T08:17:28.236728Z'
  support: supports
  summary: CHEBI:27897 resolves to tryptophan and is not obsolete. This verifies identifier/label
    correspondence only; source chemical form and stereochemical scope require the
    separate comparison in this review.
  snapshot_sha256: 78f04ac852c2983fb22754bc69247270d164db0c867a4e05c0f9e1faf82445dc
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T08:35:22Z'
  support: context_only
  summary: '{"CHEBI:18167": [], "CHEBI:176843": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}],
    "CHEBI:27897": [{"label": "Tryptophan", "match_type": "preferred_term", "identifier":
    "CHEBI:27897", "preferred_term": "Tryptophan", "ontology_id": "CHEBI:27897", "mapping_status":
    "MAPPED", "ambiguity": "resolved:owned"}]}; Unresolved current secondary keys:
    [''CHEBI:18167'']'
- evidence_id: owner-mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All owner secondary keys; complete CSV read including ignored file; pinned
    metadata in source.inputs
  accessed_at: '2026-10-21T08:35:22Z'
  support: supports
  summary: 'Four of five owner secondary keys have live preferred-term rows; CHEBI:18167
    has no exact identifier row in the pinned index. Target linkage is two of three
    asserted secondary keys. This is a local MIM linkage defect, not evidence that
    CHEBI:18167 is an invalid ontology term. No nearby maltose key is silently substituted.
    {"CHEBI:18167": [], "CHEBI:18276": [{"label": "Hydrogen gas", "match_type": "preferred_term",
    "identifier": "CHEBI:18276", "preferred_term": "Hydrogen gas", "ontology_id":
    "CHEBI:18276", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16526":
    [{"label": "Carbon dioxide gas", "match_type": "preferred_term", "identifier":
    "CHEBI:16526", "preferred_term": "Carbon dioxide gas", "ontology_id": "CHEBI:16526",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label":
    "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term":
    "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:27897": [{"label": "Tryptophan", "match_type": "preferred_term",
    "identifier": "CHEBI:27897", "preferred_term": "Tryptophan", "ontology_id": "CHEBI:27897",
    "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}]}'
- evidence_id: chemical-forms
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16709
  locator: Exact term description and molecular annotations
  accessed_at: '2026-10-21T08:17:26.473529Z'
  support: supports
  summary: CHEBI:16709 is pyridoxine, the methanol form of B6. The source names pyridoxal-HCl
    and pyridoxal-phosphate, so its generic B6 heading does not justify pyridoxine
    as another ingredient.
  snapshot_sha256: 520ccaa52464e36a60d2a7f103f96537c2ab4915c9e10dc40817a76db6469e29
- evidence_id: maltose-form
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18167
  locator: Exact term description and stereochemical annotations
  accessed_at: '2026-10-21T08:17:27.439061Z'
  support: supports
  summary: CHEBI:18167 specifically asserts the alpha configuration at the reducing-end
    anomeric centre. The paper and provider name maltose without that specification.
    Neither a different replacement ID nor a hydrate is verified here.
  snapshot_sha256: e5f8ffe560badeedcb0ca1b3895a1cbb9913d56e11224fa91ffb77fa8a383199
- evidence_id: tryptophan-form
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27897
  locator: Exact term description, InChI and SMILES
  accessed_at: '2026-10-21T08:17:28.236728Z'
  support: supports
  summary: CHEBI:27897 is the generic tryptophan term. Its annotations do not specify
    the owner-only L designation, and the captured methods likewise name generic tryptophan.
    The source does not establish the enantiomer.
  snapshot_sha256: 78f04ac852c2983fb22754bc69247270d164db0c867a4e05c0f9e1faf82445dc
- evidence_id: repair-context
  kind: record_content
  reference: scripts/repair_togo_m2770_4_yaco_score15.py
  locator: INGREDIENTS; PREPARATION_STEPS; NOTES; repair_record; _append_curation_event
  accessed_at: '2026-10-21T08:35:22Z'
  support: supports
  summary: Read the complete current repair script without running it. It explicitly
    supplies 20 MILLIMOLAR, the combined supplementation instruction, L-tryptophan
    and condition/reference fields seen in the later owner. This establishes those
    maintained assertions and their local repair context, not independent source verification.
    No current generic importer or merge path was replayed.
- evidence_id: history
  kind: record_content
  reference: data/merge_yaml/merged/4_yaco_media.yaml
  locator: All nine target and nine owner curation_history timestamps; owner September
    repair event
  accessed_at: '2026-10-21T08:35:22Z'
  support: supports
  summary: All 18 scoped timestamps parse with explicit timezone offsets. The owner
    history records a past repair interpretation and must remain preserved as provenance;
    later correction requires an appended clarification, not rewriting that event.
    Syntax and a curated flag do not establish scientific approval.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009318
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: concern
  summary: '7 primary CHEBI identities resolve with matching labels; 2 of 3 current
    secondary keys have live pinned-index rows. Unresolved keys: [''CHEBI:18167''].
    Resolution does not validate the source-level pyridoxine assignment, maltose anomer
    or owner-only L-tryptophan label; these are assessed separately.'
  target_ids:
  - CultureMech:009318
  evidence_ids:
  - record
  - mim
  - chebi15956
  - chebi16526
  - chebi16709
  - chebi176843
  - chebi18167
  - chebi18276
  - chebi27897
  details: 16 direct ingredient instances; CHEBI-primary instance linkage 7/16 (43.75%),
    verified secondary coverage 2/16 (12.50%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Source identity and exact maintained owner
  outcome: supported
  summary: Stable ID CultureMech:009318 and TOGO:M2770 identify the same named medium
    in both layers. The merge event identifies one maintained bacterial owner. The
    current provider retains its supplement hierarchy; publication identity is independently
    corroborated. Correct accession identity does not make every flattened ingredient
    or later repair assertion source-supported.
  target_ids:
  - CultureMech:009318
  evidence_ids:
  - record
  - owner-0
  - id-search
  - togo
  - paper-metadata
- assessment_id: amounts
  area: quantity
  topic: All 16 target rows and all eight owner rows
  outcome: concern
  summary: Every row is traced below. Fifteen target amounts are VARIABLE. Some source
    quantities are recoverable with nominal culture-volume context, but the maltose
    unit, yeast percentage basis and B6 amount allocation remain unresolved. No stock
    solutions or external stock references are asserted, and the main-section self
    references are headings rather than independent stock recipes.
  target_ids:
  - CultureMech:009318
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper-methods
  - maltose-typography
  details: '[{"target_field": "ingredients[0]", "material": "yeast autolysate", "target_concentration":
    {"value": "4", "unit": "PERCENT_W_V"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[0]",
    "owner_concentration": {"value": "4", "unit": "PERCENT_W_V"}, "source_quantity_or_relation":
    "4%; percentage basis not specified", "source_locator": "$.components[0].items[0];
    $.comments[0]; sec3 p1", "assessment": "The numerical 4 is supported; PERCENT_W_V
    is more specific than either capture."}, {"target_field": "ingredients[1]", "material":
    "maltose", "target_concentration": {"value": "variable", "unit": "VARIABLE"},
    "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[1]",
    "owner_concentration": {"value": "20", "unit": "MILLIMOLAR"}, "source_quantity_or_relation":
    "literal 20 m; unit unresolved", "source_locator": "$.components[0].items[1];
    $.comments[0]; sec3 p1", "assessment": "Target VARIABLE preserves no amount; owner
    20 MILLIMOLAR is not verified by this typography. Alpha form is not specified."},
    {"target_field": "ingredients[2]", "material": "carbon dioxide", "target_concentration":
    {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[3]",
    "owner_concentration": {"value": "20", "unit": "PERCENT_V_V"}, "source_quantity_or_relation":
    "20% of headspace", "source_locator": "$.components[0].items[2]; $.comments[0];
    sec3 p1", "assessment": "Source gas-phase proportion; owner records headspace.
    Do not treat as dissolved concentration or infer pressure."}, {"target_field":
    "ingredients[3]", "material": "hydrogen", "target_concentration": {"value": "variable",
    "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[2]",
    "owner_concentration": {"value": "80", "unit": "PERCENT_V_V"}, "source_quantity_or_relation":
    "80% of headspace", "source_locator": "$.components[0].items[3]; $.comments[0];
    sec3 p1", "assessment": "Source gas-phase proportion; owner records headspace.
    Do not derive a liquid concentration."}, {"target_field": "ingredients[4]", "material":
    "B7 heading", "target_concentration": {"value": "variable", "unit": "VARIABLE"},
    "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[4]",
    "owner_concentration": {"value": "60-100", "unit": "MICROG_PER_L"}, "source_quantity_or_relation":
    "same biotin supplement as target row8", "source_locator": "$.components[0].items[4];
    $.components[1]; sec3 p2", "assessment": "Heading is not a second biotin dose."},
    {"target_field": "ingredients[5]", "material": "B6 heading", "target_concentration":
    {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[5]",
    "owner_concentration": {"value": "24-40", "unit": "MG_PER_L"}, "source_quantity_or_relation":
    "120–200 micrograms per tube names two forms with unresolved allocation", "source_locator":
    "$.components[0].items[5]; $.comments[2]; sec3 p3", "assessment": "24–40 mg/L
    is arithmetic for the stated mass per nominal 5 mL only; not established as combined-family
    total or independent dose for each. Pyridoxine is not named."}, {"target_field":
    "ingredients[6]", "material": "B12/corrinoid heading", "target_concentration":
    {"value": "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[6]",
    "owner_concentration": {"value": "6-10", "unit": "MG_PER_L"}, "source_quantity_or_relation":
    "30–50 micrograms per tube of one selected named form", "source_locator": "$.components[0].items[6];
    $.comments[3]; sec3 p4", "assessment": "6–10 mg/L conditional on nominal 5 mL
    applies to one chosen form; not a sum of four forms plus heading."}, {"target_field":
    "ingredients[7]", "material": "tryptophan heading", "target_concentration": {"value":
    "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[7]",
    "owner_concentration": {"value": "12-20", "unit": "MG_PER_L"}, "source_quantity_or_relation":
    "same supplement as target row15", "source_locator": "$.components[0].items[7];
    $.components[4]; sec3 p5", "assessment": "Heading is not a second dose; owner
    L specificity is unsupported."}, {"target_field": "ingredients[8]", "material":
    "biotin (supplier named)", "target_concentration": {"value": "variable", "unit":
    "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[4]",
    "owner_concentration": {"value": "60-100", "unit": "MICROG_PER_L"}, "source_quantity_or_relation":
    "0.3–0.5 micrograms per tube", "source_locator": "$.components[1].items[0]; $.comments[1];
    sec3 p2", "assessment": "0.3–0.5 micrograms /0.005 L = 60–100 micrograms/L conditionally;
    owner arithmetic agrees. Inclusion depends on treatment."}, {"target_field": "ingredients[9]",
    "material": "pyridoxal-phosphate", "target_concentration": {"value": "variable",
    "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[5]",
    "owner_concentration": {"value": "24-40", "unit": "MG_PER_L"}, "source_quantity_or_relation":
    "one of the two B6 forms named together", "source_locator": "$.components[2].items[0];
    $.comments[2]; sec3 p3", "assessment": "Source uses and between forms; no exclusive
    alternative, each-dose allocation or combined total is verified."}, {"target_field":
    "ingredients[10]", "material": "pyridoxal-HCl", "target_concentration": {"value":
    "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[5]",
    "owner_concentration": {"value": "24-40", "unit": "MG_PER_L"}, "source_quantity_or_relation":
    "other B6 form named together", "source_locator": "$.components[2].items[1]; $.comments[2];
    sec3 p3", "assessment": "Preserve hydrochloride identity and unresolved allocation;
    do not equate with pyridoxine."}, {"target_field": "ingredients[11]", "material":
    "hydroxocobalamin acetate salt", "target_concentration": {"value": "variable",
    "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[6]",
    "owner_concentration": {"value": "6-10", "unit": "MG_PER_L"}, "source_quantity_or_relation":
    "one of four corrinoid alternatives", "source_locator": "$.components[3].items[0];
    $.comments[3]; sec3 p4", "assessment": "6–10 mg/L conditional dose applies only
    if this form is chosen; preserve salt form."}, {"target_field": "ingredients[12]",
    "material": "hydroxocobalamin hydrochloride", "target_concentration": {"value":
    "variable", "unit": "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[6]",
    "owner_concentration": {"value": "6-10", "unit": "MG_PER_L"}, "source_quantity_or_relation":
    "one of four corrinoid alternatives", "source_locator": "$.components[3].items[1];
    $.comments[3]; sec3 p4", "assessment": "6–10 mg/L conditional dose applies only
    if this form is chosen; preserve hydrochloride."}, {"target_field": "ingredients[13]",
    "material": "methylcobalamin", "target_concentration": {"value": "variable", "unit":
    "VARIABLE"}, "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[6]",
    "owner_concentration": {"value": "6-10", "unit": "MG_PER_L"}, "source_quantity_or_relation":
    "one of four corrinoid alternatives", "source_locator": "$.components[3].items[2];
    $.comments[3]; sec3 p4", "assessment": "6–10 mg/L conditional dose applies only
    if this form is chosen."}, {"target_field": "ingredients[14]", "material": "cyanocobalamin
    (supplier named)", "target_concentration": {"value": "variable", "unit": "VARIABLE"},
    "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[6]",
    "owner_concentration": {"value": "6-10", "unit": "MG_PER_L"}, "source_quantity_or_relation":
    "one of four corrinoid alternatives", "source_locator": "$.components[3].items[3];
    $.comments[3]; sec3 p4", "assessment": "6–10 mg/L conditional dose applies only
    if this form is chosen."}, {"target_field": "ingredients[15]", "material": "tryptophan
    (supplier named)", "target_concentration": {"value": "variable", "unit": "VARIABLE"},
    "owner_field": "data/normalized_yaml/bacterial/4_yaco_media.yaml:ingredients[7]",
    "owner_concentration": {"value": "12-20", "unit": "MG_PER_L"}, "source_quantity_or_relation":
    "60–100 micrograms per tube", "source_locator": "$.components[4].items[0]; $.comments[4];
    sec3 p5", "assessment": "60–100 micrograms /0.005 L = 12–20 mg/L conditionally;
    owner arithmetic agrees but L form is not established."}]'
- assessment_id: variants
  area: representation
  topic: Basal medium versus experimental supplement treatments
  outcome: concern
  summary: The generated list duplicates B7 and tryptophan headings with named ingredients,
    retains B6 forms alongside an unsupported pyridoxine heading, and flattens four
    explicitly alternative corrinoids. The later owner improves the hierarchy and
    preserves the corrinoid choice in notes, but its preparation_steps[1] commands
    all four supplement families together. The study distinguishes base cultures and
    supplementation experiments; no single universal combined treatment is established.
  target_ids:
  - CultureMech:009318
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper-methods
  - paper-treatment-scope
  - paper-basal-limit
- assessment_id: source-chemical-scope
  area: grounding
  topic: Molecular forms, source specificity and owner linkages
  outcome: concern
  summary: 'All seven asserted target primary CHEBI IDs have matching current canonical
    labels. This does not establish source suitability: pyridoxine is not either named
    pyridoxal form, alpha-maltose exceeds the source anomer scope, and owner L-tryptophan
    exceeds both the generic source name and its generic term. Vitamin B12 is a family
    term and must not become an extra molecular dose. Owner B6/B12 families deliberately
    lack IDs; no pure-molecule replacement is inferred. The maltose secondary key
    is unresolved in both local layers.'
  target_ids:
  - CultureMech:009318
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper-methods
  - chemical-forms
  - maltose-form
  - tryptophan-form
  - chebi176843
  - owner-mim
  details: 'Primary target linkage: 7/16 ingredients (43.75%). Target live secondary
    linkage: 2/16 (12.50%), from 3 asserted keys. Owner primary linkage: 5/8 (62.50%);
    owner live secondary linkage: 4/8 (50.00%), from 5 asserted keys. Linkage percentages
    measure index presence, not chemical/source correctness.'
- assessment_id: conditions
  area: completeness
  topic: Culture context and preparation provenance
  outcome: concern
  summary: The owner retains gas headspace, nominal culture/vessel volumes, darkness
    and room-temperature wording from the methods. The generated target omits those
    conditions and all preparation steps, leaving gases as unspecified ingredient
    rows. Source headspace context supports an oxygen-free atmosphere but not an invented
    dissolved dose, pressure or numeric incubation temperature. No source pH or sterilization
    instruction is established in the captured media subsection. The owner initial
    preparation and universal-supplement steps also require the unresolved source
    and treatment qualifications above.
  target_ids:
  - CultureMech:009318
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper-methods
  - paper-basal-limit
- assessment_id: classification
  area: scope
  topic: Mixtures, physical state and organism-claim boundary
  outcome: supported
  summary: Yeast autolysate supports COMPLEX/UNDEFINED classification and the described
    liquid cultures support LIQUID. The paper names Treponema primitia ZAS-2 and Treponema
    azotonutricium ZAS-9 in this study; these are publication-era contextual names,
    not newly assigned taxonomy IDs or broader species-growth claims. Background organisms,
    transcriptomic pathways and response comparisons are not transferred into recipe
    assertions. Neither local layer currently asserts a named target organism.
  target_ids:
  - CultureMech:009318
  evidence_ids:
  - record
  - owner-0
  - paper-methods
  - paper-treatment-scope
- assessment_id: ownership
  area: ownership
  topic: Later maintained repair versus stale generated representation
  outcome: concern
  summary: The target preserves the older sixteen-row representation, whereas the
    owner and its documented September repair use eight rows, conditions and two references.
    The owner is the maintained correction surface, but its unit, molecular-scope
    and treatment assertions must be reviewed before regeneration. Do not copy the
    later owner wholesale as an approved recipe or infer a defect in unexecuted current
    merging.
  target_ids:
  - CultureMech:009318
  evidence_ids:
  - record
  - owner-0
  - repair-context
- assessment_id: evidence
  area: evidence
  topic: Citation placement and source-access limits
  outcome: concern
  summary: The generated record has no structured references; its passing reference
    command checked zero references. The owner has TOGO and DOI references and per-ingredient
    source prose, but no claim-level excerpts or variant-specific evidence for its
    inferred unit, stereochemistry or combined treatment. The PMC capture verifies
    publication content while the unavailable alternate representations and unrecovered
    basal recipe bound completion.
  target_ids:
  - CultureMech:009318
  evidence_ids:
  - record
  - owner-0
  - validate-references
  - togo
  - paper-metadata
  - paper-methods
  - paper-basal-limit
  - maltose-typography
  - history
findings:
- finding_id: f1
  issue_key: cm009318-supplement-treatments-flattened
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Supplement headings and treatment alternatives are presented as one formula
  description: The target lists self-referential supplement headings alongside their
    named forms, duplicates biotin and tryptophan, and presents four explicitly alternative
    corrinoids as independent ingredients. The later owner collapses these entries,
    but its preparation_steps[1] instructs a combined B7/B6/B12/tryptophan treatment
    for every culture. The article distinguishes the base medium and experimental
    supplementation; no single formulation corresponding to either all listed rows
    or that universal combined instruction is established. This blocks faithful recipe
    interpretation and export under one formulation.
  target_ids:
  - CultureMech:009318
  field_paths:
  - ingredients
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper-methods
  - paper-treatment-scope
  - paper-basal-limit
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/4_yaco_media.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: cm009318-unverified-unit-and-dose-bases
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Percentage, maltose unit and B6 allocation exceed the captured evidence
  description: Both layers assert PERCENT_W_V for yeast autolysate although the sources
    specify only 4%. The owner ingredients[1], notes and preparation_steps[0] assert
    20 MILLIMOLAR even though both captured source representations leave a literal
    lowercase m. That unit is unverified, not proven false. Owner ingredients[5] assigns
    24–40 mg/L to an opaque B6 family even though the 120–200 microgram wording does
    not resolve allocation between its two named forms. Other per-liter supplement
    arithmetic is valid only on the reported nominal 5 mL culture basis and within
    the relevant treatment.
  target_ids:
  - CultureMech:009318
  field_paths:
  - ingredients[0].concentration
  - ingredients[1].concentration
  - ingredients[5].concentration
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper-methods
  - maltose-typography
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/4_yaco_media.yaml
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
  issue_key: cm009318-source-molecular-scope-mismatches
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Chemical assertions are more specific than the named source materials
  description: Target ingredients[5] identifies the B6 heading as pyridoxine CHEBI:16709,
    while the source names pyridoxal-HCl and pyridoxal-phosphate. Both layers identify
    generic source maltose as alpha-maltose CHEBI:18167 without anomer evidence. The
    maintained owner ingredients[7].preferred_term further asserts L-tryptophan although
    the source and CHEBI:27897 term are generic. Canonical labels resolve, but these
    source-form assertions are unsupported.
  target_ids:
  - CultureMech:009318
  field_paths:
  - ingredients[1].term
  - ingredients[1].mediaingredientmech_chebi_term
  - ingredients[5].term
  - ingredients[7].preferred_term
  evidence_ids:
  - record
  - owner-0
  - paper-methods
  - togo
  - chemical-forms
  - maltose-form
  - tryptophan-form
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/4_yaco_media.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: cm009318-unresolved-maltose-secondary-key
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The maltose secondary key has no current pinned MIM row
  description: Both local layers assert CHEBI:18167 as a MediaIngredientMech secondary
    link. A complete read of the pinned index finds no row with that exact identifier,
    although the ontology term itself resolves. Only two of three target secondary
    keys and four of five owner keys have live preferred-term rows. This is a linkage
    defect independent of the source anomer question.
  target_ids:
  - CultureMech:009318
  field_paths:
  - ingredients[1].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - mim
  - owner-mim
  - maltose-form
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/4_yaco_media.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.1
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: cm009318-generated-conditions-absent
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The generated target omits documented gas and culture context
  description: The generated target has unspecified gas ingredient amounts and no
    aeration, vessel, temperature or preparation fields. The current owner retains
    the source 80% H2/20% CO2 headspace, nominal 5 mL cultures in 25 mL vessels, darkness
    and room-temperature context. These fields help distinguish gas-phase supply and
    source-specific conditions, but must be preserved alongside correction of the
    owner unit/treatment assumptions.
  target_ids:
  - CultureMech:009318
  field_paths:
  - ingredients[2].concentration
  - ingredients[3].concentration
  - aeration
  - culture_vessel
  - temperature_range
  - incubation_atmosphere
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - paper-methods
  - togo
  - repair-context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/4_yaco_media.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: cm009318-source-evidence-not-retained
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Generated references and claim-level qualifications are missing
  description: The generated target retains a TOGO note but omits the owner two references
    and per-ingredient source prose. The owner references alone do not support every
    inferred quantity, form or treatment. The target reference check passes with zero
    references; neither that result nor historical curated flags provide scientific
    validation.
  target_ids:
  - CultureMech:009318
  field_paths:
  - references
  - evidence
  - ingredients
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - validate-references
  - paper-metadata
  - paper-methods
  - paper-basal-limit
  - history
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/4_yaco_media.yaml
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
  description: Review the maintained owner and represent the basal medium and supported
    supplementation variants separately. Remove heading/material double counting,
    preserve the explicit one-form corrinoid choice, and retain B6 allocation uncertainty.
    Correct owner preparation_steps[1]; do not infer an exclusive B6 alternative or
    universally required cocktail. Recover the referenced basal formulation before
    claiming a complete recipe, then regenerate the target.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009318
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/4_yaco_media.yaml
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
  description: Preserve the source 4% without an unsupported mass/volume basis; independently
    recover original maltose typography before retaining or changing 20 mM. Resolve
    or explicitly retain B6 allocation uncertainty rather than treating the family
    dose as a known total. Keep original per-tube amounts and the conditional nominal-volume
    calculations as separate evidence. Amend owner notes and preparation text, append
    a clarification to provenance, and regenerate after source review.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009318
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/4_yaco_media.yaml
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
  description: Correct the maintained molecular scope using independently supported
    forms, retaining named hydrochloride/phosphate distinctions and uncertain stereochemistry.
    Do not add pyridoxine as another source ingredient or silently invent replacement
    IDs. Resolve target-only stale assertions through verified owner correction and
    regeneration; owner-only L naming requires explicit source support or qualification.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009318
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/4_yaco_media.yaml
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
  description: Reconcile the maintained maltose secondary link against the pinned
    MIM release after establishing source chemical scope. Verify the exact accepted
    key and canonical label or retain the link as unresolved; do not replace it solely
    from a similar label. Regenerate and check exact secondary-key availability.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009318
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/4_yaco_media.yaml
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
  description: After correcting and verifying the maintained formulation, regenerate
    to preserve source-scoped headspace, culture/vessel volume and qualitative conditions.
    Keep gas proportions in their headspace context; do not infer liquid concentrations,
    pressure, numeric temperature, pH or sterilization. Ensure the revised preparation
    does not prescribe an unsupported combined treatment.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009318
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/4_yaco_media.yaml
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
  description: Add concise claim-level support for the exact source recipe/treatment,
    original amounts, conditional calculations, chemical-form limits and unavailable
    source questions in the maintained owner; preserve and propagate appropriate references.
    Append a correction event while retaining every historical event unchanged.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:009318
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/4_yaco_media.yaml
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
- The primary PMC HTML for DOI 10.1038/ismej.2011.3 is available and was inspected.
  Its maltose text literally says 20 m, with a thin space and lowercase m; no hidden
  capital M or unit markup was recovered. The publisher DOI route returned 403, Europe
  PMC full-text XML returned 500, and purported PDF/supplement routes returned HTML
  interstitials. Neither 20 mM nor another molarity is verified; this does not prove
  20 mM false.
- The article refers to Graber et al. 2004 for the 4YACo basal-medium context. That
  cited basal formulation was not independently recovered in this bounded review,
  and no access attempt or remote unavailability claim is made for that separate article.
  The available methods do not justify treating yeast autolysate and maltose as a
  complete independently reconstructed basal recipe.
- Per-liter supplement arithmetic is conditional on the reported nominal 5 mL culture
  volume, not a measured post-addition final volume. B6 wording does not resolve whether
  its stated amount applies to each form or a combined amount. Corrinoids are explicitly
  one chosen form. These conversions do not establish universal inclusion or an optimized
  recipe.
- Publication-era species names and strain designations are contextual only. No current
  taxonomy identifier, strain accession, new growth assertion, preferred supplement
  choice, or experimental optimization is proposed. No pH, numeric room-temperature
  value, gas pressure, unreported stock recipe or sterilization step is inferred.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-011
- generated-medium
```
