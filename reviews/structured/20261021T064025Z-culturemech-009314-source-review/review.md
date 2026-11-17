# Source and formulation review: 1_2_tryptic_soy_broth_anaerobic (CultureMech:009314)

- Review: 20261021T064025Z-culturemech-009314-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T06:36:38Z
- Finished UTC: 2026-10-21T06:40:25Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M2766 resolves to DSMZ 1205. The commercial broth is replaced by unsupported direct constituents and agar; water volume becomes mass, and source preparation and pH are omitted. The exact historic commercial product remains unresolved.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 52 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 006 selects ordinals 51-60 after five validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009314 | data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml | generated | 1_2_tryptic_soy_broth_anaerobic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009314 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009314 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch006/052/strict.tsv |
| validate-terms | passed | True | CultureMech:009314 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009314 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009314 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Verify historic BD product and composition | unavailable | True | CultureMech:009314 | The source gives BD BACTO without a catalog; current catalog metadata and Sigma composition do not resolve the historic BD formula. Manufacturer manual access failed. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009314.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:009314.

Eight distinct CHEBI identifiers across nine ingredient instances and two additional MICRO/FOODON instances resolve. Four secondary keys have live index rows.

13 direct ingredient instances; primary linkage 11/13 (84.62%); secondary linkage 4/13 (30.77%), both on a 0–100 scale. Yeast extract and DTT have no asserted primary ID. Identifier existence is not composition validation.

### Database accession and owner

identity: supported. Targets: CultureMech:009314.

TOGO M2766 explicitly links DSMZ1205; target and sole owner have identical ingredients. The source product remains a premix, not a list of free-standing constituents.

### ingredients[0].concentration

quantity: concern. Targets: CultureMech:009314.

correct: original water volume is encoded as G_PER_L without a justified density conversion.

### ingredients[1].concentration

quantity: supported. Targets: CultureMech:009314.

verified: source supplement numeric amount and original gram unit agree with the primary source and provider per-liter representation.

### ingredients[2].concentration

quantity: supported. Targets: CultureMech:009314.

verified: source supplement numeric amount and original gram unit agree with the primary source and provider per-liter representation.

### ingredients[3].concentration

quantity: supported. Targets: CultureMech:009314.

verified: source supplement numeric amount and original gram unit agree with the primary source and provider per-liter representation.

### ingredients[4].concentration

quantity: concern. Targets: CultureMech:009314.

unsupported: this is an expanded product constituent, not a separately dosed source ingredient; agar is absent from the primary broth recipe.

### ingredients[5].concentration

quantity: concern. Targets: CultureMech:009314.

unsupported: this is an expanded product constituent, not a separately dosed source ingredient; agar is absent from the primary broth recipe.

### ingredients[6].concentration

quantity: concern. Targets: CultureMech:009314.

unsupported: this is an expanded product constituent, not a separately dosed source ingredient; agar is absent from the primary broth recipe.

### ingredients[7].concentration

quantity: concern. Targets: CultureMech:009314.

unsupported: this is an expanded product constituent, not a separately dosed source ingredient; agar is absent from the primary broth recipe.

### ingredients[8].concentration

quantity: concern. Targets: CultureMech:009314.

unsupported: this is an expanded product constituent, not a separately dosed source ingredient; agar is absent from the primary broth recipe.

### ingredients[9].concentration

quantity: concern. Targets: CultureMech:009314.

unsupported: this is an expanded product constituent, not a separately dosed source ingredient; agar is absent from the primary broth recipe.

### ingredients[10].concentration

quantity: supported. Targets: CultureMech:009314.

verified: source supplement numeric amount and original gram unit agree with the primary source and provider per-liter representation.

### ingredients[11].concentration

quantity: concern. Targets: CultureMech:009314.

not_quantified as a mass addition: source gas composition and acid adjustment context must be retained separately; VARIABLE alone loses source scope.

### ingredients[12].concentration

quantity: concern. Targets: CultureMech:009314.

not_quantified as a mass addition: source gas composition and acid adjustment context must be retained separately; VARIABLE alone loses source scope.

### Ontology specificity and source annotations

grounding: concern. Targets: CultureMech:009314.

The hydrolyzed vegetable-protein term is broader than a particular soy digest; supplier synonyms do not establish exact commercial identity. DTT is ungrounded and its copied inorganic annotation conflicts with the named organic dithiol. Source acid annotation is generic while preparation identifies an adjustment role. Preserve those differences rather than promote annotations as mechanisms.

### pH, gas and stock-addition context

completeness: concern. Targets: CultureMech:009314.

Source pH and preparation are absent locally. Gas composition, separate addition stages and unspecified stock strengths require scoped representation, not inferred dose values.

### Composition and physical state

scope: concern. Targets: CultureMech:009314.

COMPLEX/UNDEFINED agrees with source premix and yeast extract. LIQUID agrees with the intended broth but conflicts with the unsupported local agar addition; correct the recipe identity before changing state. No organism-specific growth claim is asserted.

### Source support and history

evidence: concern. Targets: CultureMech:009314.

The source accession resolves and timestamps parse normally; the generic product page and import history do not support the substituted formulation. Reference checking examined zero excerpts.

## Findings

### f1: Expanded product and agar change the source broth

blocker / open / confirmed; issue key: CM009314-premix-expansion.

The source commercial product dose is replaced by six direct components totaling 45 g/L, including agar absent from the source.

### f2: Water volume is represented as mass

major / open / confirmed; issue key: CM009314-water-volume-unit.

The numeric water volume is retained but its milliliter unit becomes G_PER_L without density evidence.

### f3: Preparation and pH are omitted

major / open / confirmed; issue key: CM009314-preparation-omitted.

The original pH and preparation stages are lost, including gas and separate-addition scope.

### f4: Supplier and exact-product equivalence are unsupported

major / open / confirmed; issue key: CM009314-product-provenance.

Multi-vendor TSB/TSA identity, catalog attribution and exact digest/brand synonyms are not verified for the source BD BACTO product.

### f5: Imported annotation and missing evidence need curation

minor / open / confirmed; issue key: CM009314-source-annotation-and-evidence.

DTT retains an inorganic annotation from the source, while claim-level quantities and preparation have no evidence objects. Import history is not validation of these claims.

## Recommended Actions And Acceptance Checks

### a1

Restore the source product boundary and its supplier context. Keep separately added supplements; do not calculate constituent substitutions until exact product composition is verified.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the original water volume and batch basis; do not assume density to justify the imported unit.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Retain the source context with stage-specific evidence and leave unspecified stock strengths or acid doses unresolved.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Constrain product assertions to verified supplier/source claims and document uncertainty until historic product identity is established.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Review copied annotations against verified chemistry and attach narrow evidence to corrected claims; preserve the original source wording as provenance where necessary.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch006/052/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch006/052/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml:1:id: CultureMech:009314<br>./data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml:1:id: CultureMech:009314<br> |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15377 resolves to water and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17234 resolves to glucose and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17634 resolves to D-glucose and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17883 resolves to hydrogen chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17997 resolves to dinitrogen and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:2509 resolves to agar and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17634": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| micro0000182 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182; Exact asserted identifier, label, definition and obsolete flag | supports | MICRO:0000182 resolves to tryptone. Term existence does not verify the actual commercial ingredient or digest method. |
| foodon03315720 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315720; Exact asserted identifier, label, definition and obsolete flag | supports | FOODON:03315720 resolves to vegetable protein, hydrolyzed. Term existence does not verify the actual commercial ingredient or digest method. |
| dsmz | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1205.pdf; Page 1 formulation and preparation | supports | Complete original collection formula and preparation inspected. Its product boundary and separate supplements are explicit. |
| api | https://mediadive.dsmz.de/rest/medium/1205; data.medium; data.solutions[0] | supports | Exact medium identity, compound rows, declared main volume and preparation match the primary collection source. |
| render | https://bacmedia.dsmz.de/pdf/1205; Page 1 | supports | Collection rendering confirms pH, declared volume and preparation context. |
| sigma | https://www.sigmaaldrich.com/deepweb/assets/sigmaaldrich/product/documents/288/904/22092dat.pdf; Page 1 product title and composition table | context_only | The cited Sigma catalog denotes TSB. Its standard formula has five constituents and no agar in the base composition; the soy component is a papain digest. This specification does not identify the BD product used by DSMZ or establish interchangeability. |
| cited-page | https://en.wikipedia.org/wiki/Tryptic_soy_broth; Preparation list, inspected current page | context_only | The cited secondary page describes a generic formulation, not the exact DSMZ premix or a vendor-specific certificate. It is insufficient to justify the expanded recipe or combined TSB/TSA product identity. |
| bd-catalog | https://www.bd.com/en-us/products-and-solutions/products/product-page.211825; Title, catalog and packaging metadata | context_only | BD catalog 211825 resolves to Tryptic Soy Broth, 500 g, GTIN 00382902118251. No formula is supplied on the inspected page. Catalog existence does not establish which historic BD BACTO broth DSMZ1205 used. |
| bd-formula-access | https://static.bd.com/assets/product/Documents/Integrated%20Diagnostic%20Solutions%20%28IDS%29/DS_CM_Difco-and-BBL-culture-media-manual_UG_EN.pdf; Bounded manufacturer-document retrieval | context_only | The indexed official manual URL returned HTTP 404. No BD formula was inspected; neither search snippets nor retailer formulas were accepted. This is an access limitation, not proof that documentation does not exist. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2766; meta; components[0]; comments | supports | Full eight-component source entry, original accession, pH and preparation comment inspected. |
| trace | TOGO M2766 and maintained-owner comparison; All unexpanded rows and annotations; expanded product mass sum | context_only | {"rows": [{"target_index": 0, "source_index": 0, "source_unit": "ml", "source_amount": 1000, "source_gas_fraction": null, "target_concentration": {"value": "1000", "unit": "G_PER_L"}, "notes_match": true}, {"target_index": 1, "source_index": 1, "source_unit": "g", "source_amount": 1, "source_gas_fraction": null, "target_concentration": {"value": "1", "unit": "G_PER_L"}, "notes_match": true}, {"target_index": 2, "source_index": 2, "source_unit": "g", "source_amount": 2.5, "source_gas_fraction": null, "target_concentration": {"value": "2.5", "unit": "G_PER_L"}, "notes_match": true}, {"target_index": 3, "source_index": 3, "source_unit": "g", "source_amount": 3.6, "source_gas_fraction": null, "target_concentration": {"value": "3.6", "unit": "G_PER_L"}, "notes_match": true}, {"target_index": 10, "source_index": 5, "source_unit": "g", "source_amount": 0.15, "source_gas_fraction": null, "target_concentration": {"value": "0.15", "unit": "G_PER_L"}, "notes_match": true}, {"target_index": 11, "source_index": 6, "source_unit": null, "source_amount": null, "source_gas_fraction": 100, "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "notes_match": true}, {"target_index": 12, "source_index": 7, "source_unit": null, "source_amount": null, "source_gas_fraction": null, "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "notes_match": true}], "expanded_product_sum_g_per_l": 45, "source_premix_g": 13.75, "owner_ingredients_identical": true} |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Commercial product identity/composition is unresolved; completion is partial. Source captures and reused web evidence preserve their original access times.
- No source-specific organism application, experimental growth, optimization or inferred stock/gas concentration is added.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T064025Z-culturemech-009314-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_2_tryptic_soy_broth_anaerobic (CultureMech:009314)'
started_at: '2026-10-21T06:36:38Z'
finished_at: '2026-10-21T06:40:25Z'
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
summary: TOGO M2766 resolves to DSMZ 1205. The commercial broth is replaced by unsupported
  direct constituents and agar; water volume becomes mass, and source preparation
  and pH are omitted. The exact historic commercial product remains unresolved.
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
  - path: data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml
    sha256: c2adbf9a83df7c913a69772b8f07029e36b172809f5b78ef0d04ba0678ecc583
    role: target
  - path: data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml
    sha256: 10b86d7e6253fedcfab784b5cc16d2c9abc67fd069cd6b1cc7fb75f716863008
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
  selection: Record 52 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 006 selects ordinals 51-60 after five
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009314
targets:
- target_id: CultureMech:009314
  path: data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml
  label: 1_2_tryptic_soy_broth_anaerobic
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch006/052/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch006/052/strict.tsv"
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009314
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
  - CultureMech:009314
- check_id: commercial-product-identity
  name: Verify historic BD product and composition
  required: true
  status: unavailable
  summary: The source gives BD BACTO without a catalog; current catalog metadata and
    Sigma composition do not resolve the historic BD formula. Manufacturer manual
    access failed.
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - dsmz
  - togo
  - bd-catalog
  - bd-formula-access
  - sigma
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T06:40:23Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T06:40:23Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:36:59.043181Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch006/052/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T06:37:10.574944Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-006/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch006/052/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:37:13.419120Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T06:37:23.168034Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T06:40:23Z'
  support: supports
  summary: './data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml:1:id: CultureMech:009314

    ./data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml:1:id: CultureMech:009314

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
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
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
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T03:57:32.595833Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi17634
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:14:38.075522Z'
  support: supports
  summary: CHEBI:17634 resolves to D-glucose and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: d11b31a8e91c3fffe7744f612dab69cdb4e02f42068cd2eb1458acee4503a62f
- evidence_id: chebi17883
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:37:25.439020Z'
  support: supports
  summary: CHEBI:17883 resolves to hydrogen chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: chebi17997
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:26:34.033078Z'
  support: supports
  summary: CHEBI:17997 resolves to dinitrogen and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:07:41.448510Z'
  support: supports
  summary: CHEBI:2509 resolves to agar and is not obsolete. This verifies the asserted
    generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond
    the record is inferred.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:11:31.325976Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T06:40:23Z'
  support: supports
  summary: '{"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17634": [{"label": "D-Glucose", "match_type":
    "preferred_term", "identifier": "CHEBI:17634", "preferred_term": "D-Glucose",
    "ontology_id": "CHEBI:17634", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}],
    "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier":
    "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: micro0000182
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182
  locator: Exact asserted identifier, label, definition and obsolete flag
  accessed_at: '2026-10-20T07:37:21.973857Z'
  support: supports
  summary: MICRO:0000182 resolves to tryptone. Term existence does not verify the
    actual commercial ingredient or digest method.
  snapshot_sha256: 01875997c482a49e4d41eb35c6c697e190afd236a8527625e94b6f96df3872b0
- evidence_id: foodon03315720
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315720
  locator: Exact asserted identifier, label, definition and obsolete flag
  accessed_at: '2026-10-20T07:37:22.786983Z'
  support: supports
  summary: FOODON:03315720 resolves to vegetable protein, hydrolyzed. Term existence
    does not verify the actual commercial ingredient or digest method.
  snapshot_sha256: aa063e8b88177611aba640828e84d3982b1b3b1c65b11647d89c9efbf6274c25
- evidence_id: dsmz
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1205.pdf
  locator: Page 1 formulation and preparation
  accessed_at: '2026-10-20T07:37:13.684844Z'
  support: supports
  summary: Complete original collection formula and preparation inspected. Its product
    boundary and separate supplements are explicit.
  quote: Trypticase soy broth (BD BACTO) 13.75 g
  snapshot_sha256: 192dc12c9d2d5be2aa9baae12bbd7acf5bb6da94cbac17128bcfa1e1958234be
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1205
  locator: data.medium; data.solutions[0]
  accessed_at: '2026-10-20T07:38:16.669937Z'
  support: supports
  summary: Exact medium identity, compound rows, declared main volume and preparation
    match the primary collection source.
  snapshot_sha256: 711e2a48c1ba46c9a988d5070cdb8f76f3a389f2f3b2837a20562caa65fd48dd
- evidence_id: render
  kind: database
  reference: https://bacmedia.dsmz.de/pdf/1205
  locator: Page 1
  accessed_at: '2026-10-20T07:37:19.790784Z'
  support: supports
  summary: Collection rendering confirms pH, declared volume and preparation context.
  snapshot_sha256: eb07b4a706bafc255d4b8b2e9456da28785d8028ac353bf6070ff6f6db6be7a2
- evidence_id: sigma
  kind: primary_source
  reference: https://www.sigmaaldrich.com/deepweb/assets/sigmaaldrich/product/documents/288/904/22092dat.pdf
  locator: Page 1 product title and composition table
  accessed_at: '2026-10-21T06:37:51Z'
  support: context_only
  summary: The cited Sigma catalog denotes TSB. Its standard formula has five constituents
    and no agar in the base composition; the soy component is a papain digest. This
    specification does not identify the BD product used by DSMZ or establish interchangeability.
- evidence_id: cited-page
  kind: database
  reference: https://en.wikipedia.org/wiki/Tryptic_soy_broth
  locator: Preparation list, inspected current page
  accessed_at: '2026-10-21T06:37:51Z'
  support: context_only
  summary: The cited secondary page describes a generic formulation, not the exact
    DSMZ premix or a vendor-specific certificate. It is insufficient to justify the
    expanded recipe or combined TSB/TSA product identity.
- evidence_id: bd-catalog
  kind: primary_source
  reference: https://www.bd.com/en-us/products-and-solutions/products/product-page.211825
  locator: Title, catalog and packaging metadata
  accessed_at: '2026-10-21T06:37:51Z'
  support: context_only
  summary: BD catalog 211825 resolves to Tryptic Soy Broth, 500 g, GTIN 00382902118251.
    No formula is supplied on the inspected page. Catalog existence does not establish
    which historic BD BACTO broth DSMZ1205 used.
- evidence_id: bd-formula-access
  kind: primary_source
  reference: https://static.bd.com/assets/product/Documents/Integrated%20Diagnostic%20Solutions%20%28IDS%29/DS_CM_Difco-and-BBL-culture-media-manual_UG_EN.pdf
  locator: Bounded manufacturer-document retrieval
  accessed_at: '2026-10-21T06:36:35.781064Z'
  support: context_only
  summary: The indexed official manual URL returned HTTP 404. No BD formula was inspected;
    neither search snippets nor retailer formulas were accepted. This is an access
    limitation, not proof that documentation does not exist.
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2766
  locator: meta; components[0]; comments
  accessed_at: '2026-10-21T06:38:46.457660Z'
  support: supports
  summary: Full eight-component source entry, original accession, pH and preparation
    comment inspected.
  snapshot_sha256: d2cf8cedc32554c6411adc997594a9a983b109f695d04e0338cc59e02b5ac675
- evidence_id: trace
  kind: validation
  reference: TOGO M2766 and maintained-owner comparison
  locator: All unexpanded rows and annotations; expanded product mass sum
  accessed_at: '2026-10-21T06:40:23Z'
  support: context_only
  summary: '{"rows": [{"target_index": 0, "source_index": 0, "source_unit": "ml",
    "source_amount": 1000, "source_gas_fraction": null, "target_concentration": {"value":
    "1000", "unit": "G_PER_L"}, "notes_match": true}, {"target_index": 1, "source_index":
    1, "source_unit": "g", "source_amount": 1, "source_gas_fraction": null, "target_concentration":
    {"value": "1", "unit": "G_PER_L"}, "notes_match": true}, {"target_index": 2, "source_index":
    2, "source_unit": "g", "source_amount": 2.5, "source_gas_fraction": null, "target_concentration":
    {"value": "2.5", "unit": "G_PER_L"}, "notes_match": true}, {"target_index": 3,
    "source_index": 3, "source_unit": "g", "source_amount": 3.6, "source_gas_fraction":
    null, "target_concentration": {"value": "3.6", "unit": "G_PER_L"}, "notes_match":
    true}, {"target_index": 10, "source_index": 5, "source_unit": "g", "source_amount":
    0.15, "source_gas_fraction": null, "target_concentration": {"value": "0.15", "unit":
    "G_PER_L"}, "notes_match": true}, {"target_index": 11, "source_index": 6, "source_unit":
    null, "source_amount": null, "source_gas_fraction": 100, "target_concentration":
    {"value": "variable", "unit": "VARIABLE"}, "notes_match": true}, {"target_index":
    12, "source_index": 7, "source_unit": null, "source_amount": null, "source_gas_fraction":
    null, "target_concentration": {"value": "variable", "unit": "VARIABLE"}, "notes_match":
    true}], "expanded_product_sum_g_per_l": 45, "source_premix_g": 13.75, "owner_ingredients_identical":
    true}'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: Eight distinct CHEBI identifiers across nine ingredient instances and two
    additional MICRO/FOODON instances resolve. Four secondary keys have live index
    rows.
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - mim
  - chebi131527
  - chebi15377
  - chebi17234
  - chebi17634
  - chebi17883
  - chebi17997
  - chebi2509
  - chebi26710
  - micro0000182
  - foodon03315720
  details: 13 direct ingredient instances; primary linkage 11/13 (84.62%); secondary
    linkage 4/13 (30.77%), both on a 0–100 scale. Yeast extract and DTT have no asserted
    primary ID. Identifier existence is not composition validation.
- assessment_id: identity
  area: identity
  topic: Database accession and owner
  outcome: supported
  summary: TOGO M2766 explicitly links DSMZ1205; target and sole owner have identical
    ingredients. The source product remains a premix, not a list of free-standing
    constituents.
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - owner-0
  - id-search
  - togo
  - dsmz
  - trace
- assessment_id: amount-0
  area: quantity
  topic: ingredients[0].concentration
  outcome: concern
  summary: 'correct: original water volume is encoded as G_PER_L without a justified
    density conversion.'
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - togo
  - dsmz
  - api
  - trace
- assessment_id: amount-1
  area: quantity
  topic: ingredients[1].concentration
  outcome: supported
  summary: 'verified: source supplement numeric amount and original gram unit agree
    with the primary source and provider per-liter representation.'
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - togo
  - dsmz
  - api
  - trace
- assessment_id: amount-2
  area: quantity
  topic: ingredients[2].concentration
  outcome: supported
  summary: 'verified: source supplement numeric amount and original gram unit agree
    with the primary source and provider per-liter representation.'
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - togo
  - dsmz
  - api
  - trace
- assessment_id: amount-3
  area: quantity
  topic: ingredients[3].concentration
  outcome: supported
  summary: 'verified: source supplement numeric amount and original gram unit agree
    with the primary source and provider per-liter representation.'
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - togo
  - dsmz
  - api
  - trace
- assessment_id: amount-4
  area: quantity
  topic: ingredients[4].concentration
  outcome: concern
  summary: 'unsupported: this is an expanded product constituent, not a separately
    dosed source ingredient; agar is absent from the primary broth recipe.'
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - togo
  - dsmz
  - api
  - trace
- assessment_id: amount-5
  area: quantity
  topic: ingredients[5].concentration
  outcome: concern
  summary: 'unsupported: this is an expanded product constituent, not a separately
    dosed source ingredient; agar is absent from the primary broth recipe.'
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - togo
  - dsmz
  - api
  - trace
- assessment_id: amount-6
  area: quantity
  topic: ingredients[6].concentration
  outcome: concern
  summary: 'unsupported: this is an expanded product constituent, not a separately
    dosed source ingredient; agar is absent from the primary broth recipe.'
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - togo
  - dsmz
  - api
  - trace
- assessment_id: amount-7
  area: quantity
  topic: ingredients[7].concentration
  outcome: concern
  summary: 'unsupported: this is an expanded product constituent, not a separately
    dosed source ingredient; agar is absent from the primary broth recipe.'
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - togo
  - dsmz
  - api
  - trace
- assessment_id: amount-8
  area: quantity
  topic: ingredients[8].concentration
  outcome: concern
  summary: 'unsupported: this is an expanded product constituent, not a separately
    dosed source ingredient; agar is absent from the primary broth recipe.'
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - togo
  - dsmz
  - api
  - trace
- assessment_id: amount-9
  area: quantity
  topic: ingredients[9].concentration
  outcome: concern
  summary: 'unsupported: this is an expanded product constituent, not a separately
    dosed source ingredient; agar is absent from the primary broth recipe.'
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - togo
  - dsmz
  - api
  - trace
- assessment_id: amount-10
  area: quantity
  topic: ingredients[10].concentration
  outcome: supported
  summary: 'verified: source supplement numeric amount and original gram unit agree
    with the primary source and provider per-liter representation.'
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - togo
  - dsmz
  - api
  - trace
- assessment_id: amount-11
  area: quantity
  topic: ingredients[11].concentration
  outcome: concern
  summary: 'not_quantified as a mass addition: source gas composition and acid adjustment
    context must be retained separately; VARIABLE alone loses source scope.'
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - togo
  - dsmz
  - api
  - trace
- assessment_id: amount-12
  area: quantity
  topic: ingredients[12].concentration
  outcome: concern
  summary: 'not_quantified as a mass addition: source gas composition and acid adjustment
    context must be retained separately; VARIABLE alone loses source scope.'
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - togo
  - dsmz
  - api
  - trace
- assessment_id: chemistry
  area: grounding
  topic: Ontology specificity and source annotations
  outcome: concern
  summary: The hydrolyzed vegetable-protein term is broader than a particular soy
    digest; supplier synonyms do not establish exact commercial identity. DTT is ungrounded
    and its copied inorganic annotation conflicts with the named organic dithiol.
    Source acid annotation is generic while preparation identifies an adjustment role.
    Preserve those differences rather than promote annotations as mechanisms.
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - micro0000182
  - foodon03315720
  - togo
  - dsmz
- assessment_id: preparation
  area: completeness
  topic: pH, gas and stock-addition context
  outcome: concern
  summary: Source pH and preparation are absent locally. Gas composition, separate
    addition stages and unspecified stock strengths require scoped representation,
    not inferred dose values.
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - owner-0
  - togo
  - dsmz
  - api
- assessment_id: classification
  area: scope
  topic: Composition and physical state
  outcome: concern
  summary: COMPLEX/UNDEFINED agrees with source premix and yeast extract. LIQUID agrees
    with the intended broth but conflicts with the unsupported local agar addition;
    correct the recipe identity before changing state. No organism-specific growth
    claim is asserted.
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - togo
  - dsmz
- assessment_id: provenance
  area: evidence
  topic: Source support and history
  outcome: concern
  summary: The source accession resolves and timestamps parse normally; the generic
    product page and import history do not support the substituted formulation. Reference
    checking examined zero excerpts.
  target_ids:
  - CultureMech:009314
  evidence_ids:
  - record
  - owner-0
  - togo
  - cited-page
  - validate-references
findings:
- finding_id: f1
  issue_key: CM009314-premix-expansion
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Expanded product and agar change the source broth
  description: The source commercial product dose is replaced by six direct components
    totaling 45 g/L, including agar absent from the source.
  target_ids:
  - CultureMech:009314
  field_paths:
  - ingredients[4:10]
  - physical_state
  evidence_ids:
  - record
  - owner-0
  - togo
  - dsmz
  - api
  - trace
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM009314-water-volume-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water volume is represented as mass
  description: The numeric water volume is retained but its milliliter unit becomes
    G_PER_L without density evidence.
  target_ids:
  - CultureMech:009314
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - togo
  - dsmz
  - trace
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM009314-preparation-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation and pH are omitted
  description: The original pH and preparation stages are lost, including gas and
    separate-addition scope.
  target_ids:
  - CultureMech:009314
  field_paths:
  - ph_value
  - preparation_steps
  - ingredients[11:13]
  evidence_ids:
  - record
  - owner-0
  - togo
  - dsmz
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: CM009314-product-provenance
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Supplier and exact-product equivalence are unsupported
  description: Multi-vendor TSB/TSA identity, catalog attribution and exact digest/brand
    synonyms are not verified for the source BD BACTO product.
  target_ids:
  - CultureMech:009314
  field_paths:
  - ingredients[4:10].supplier_catalog
  - ingredients[4:9].synonyms
  - notes
  evidence_ids:
  - record
  - owner-0
  - togo
  - dsmz
  - sigma
  - bd-catalog
  - foodon03315720
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f5
  issue_key: CM009314-source-annotation-and-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Imported annotation and missing evidence need curation
  description: DTT retains an inorganic annotation from the source, while claim-level
    quantities and preparation have no evidence objects. Import history is not validation
    of these claims.
  target_ids:
  - CultureMech:009314
  field_paths:
  - ingredients[10].notes
  - ingredients[*].evidence
  - references
  evidence_ids:
  - record
  - owner-0
  - togo
  - dsmz
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Restore the source product boundary and its supplier context. Keep
    separately added supplements; do not calculate constituent substitutions until
    exact product composition is verified.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009314
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml
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
  description: Preserve the original water volume and batch basis; do not assume density
    to justify the imported unit.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009314
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml
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
  description: Retain the source context with stage-specific evidence and leave unspecified
    stock strengths or acid doses unresolved.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009314
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml
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
  description: Constrain product assertions to verified supplier/source claims and
    document uncertainty until historic product identity is established.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009314
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml
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
  description: Review copied annotations against verified chemistry and attach narrow
    evidence to corrected claims; preserve the original source wording as provenance
    where necessary.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009314
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml
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
- Commercial product identity/composition is unresolved; completion is partial. Source
  captures and reused web evidence preserve their original access times.
- No source-specific organism application, experimental growth, optimization or inferred
  stock/gas concentration is added.
tags:
- unreviewed-records
- batch-006
- generated-medium
```
