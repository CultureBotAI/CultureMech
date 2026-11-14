# Source and formulation review: 28_mh_medium (CultureMech:000926)

- Review: 20261021T072907Z-culturemech-000926-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T07:20:50Z
- Finished UTC: 2026-10-21T07:29:07Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ1460 and MediaDive support all nine direct solute amounts, supplied salt forms, pH and conditional agar. Both local layers omit source solvent and Difco context; the generated target also lacks eight verified owner evidence objects. The asserted KG ingredient-set match cannot be revalidated without its graph snapshot.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 76; batch 008 item 6 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding seven task batches contain 70 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 72 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000926 | data/merge_yaml/merged/28_mh_medium.yaml | generated | 28_mh_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000926 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:000926 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/076/strict.tsv |
| validate-terms | passed | True | CultureMech:000926 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:000926 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:000926 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Revalidate asserted KG ingredient-set match | unavailable | True | CultureMech:000926 | Graph nodes/edges including compressed candidates were absent from a hidden/ignored-inclusive inventory of this isolated checkout. KGMediaMatcher raises FileNotFoundError. The exact provider accession and local eight-ID projection were checked, but the graph association remains unverified. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:000926.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:000926.

8 primary CHEBI identities resolve with matching labels; 8 of 8 current secondary keys have live pinned-index rows. Unresolved keys: [].

9 direct ingredient instances; CHEBI-primary instance linkage 8/9 (88.89%), verified secondary coverage 8/9 (88.89%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### DSMZ1460 and MediaDive accession

identity: supported. Targets: CultureMech:000926.

The source URL, mediadive.medium:1460 source term and official28% MH MEDIUM title identify the same recipe. Numeric28% is retained as a name; no unstated percent-basis conversion is inferred.

### All nine direct concentrations and supplied forms

quantity: supported. Targets: CultureMech:000926.

verified:195,32.5,50.8,0.8,5,0.16,0.6,5 and20g/L match explicit provider g_l values in order. Primary source forms support the anhydrous salt labels; hydrated substitutions would change the recipe. Agar20g/L is conditional for solid media. Provider volume/amount evidence is not an independent final-volume measurement.

[{"field": "ingredients[0].concentration", "source_locator": "$.data.solutions[0].recipe[0]", "value_g_l": 195, "source_form": "NaCl", "condition": null, "decision": "verified"}, {"field": "ingredients[1].concentration", "source_locator": "$.data.solutions[0].recipe[1]", "value_g_l": 32.5, "source_form": "MgCl2", "condition": null, "decision": "verified"}, {"field": "ingredients[2].concentration", "source_locator": "$.data.solutions[0].recipe[2]", "value_g_l": 50.8, "source_form": "MgSO4", "condition": null, "decision": "verified"}, {"field": "ingredients[3].concentration", "source_locator": "$.data.solutions[0].recipe[3]", "value_g_l": 0.8, "source_form": "CaCl2", "condition": null, "decision": "verified"}, {"field": "ingredients[4].concentration", "source_locator": "$.data.solutions[0].recipe[4]", "value_g_l": 5, "source_form": "KCl", "condition": null, "decision": "verified"}, {"field": "ingredients[5].concentration", "source_locator": "$.data.solutions[0].recipe[5]", "value_g_l": 0.16, "source_form": "NaHCO3", "condition": null, "decision": "verified"}, {"field": "ingredients[6].concentration", "source_locator": "$.data.solutions[0].recipe[6]", "value_g_l": 0.6, "source_form": "NaBr", "condition": null, "decision": "verified"}, {"field": "ingredients[7].concentration", "source_locator": "$.data.solutions[0].recipe[7]", "value_g_l": 5, "source_form": "Yeast extract", "condition": null, "decision": "verified"}, {"field": "ingredients[8].concentration", "source_locator": "$.data.solutions[0].recipe[9]", "value_g_l": 20, "source_form": "Agar", "condition": "for solid medium", "decision": "verified"}]

### Source solvent and supplied yeast-extract grade

completeness: concern. Targets: CultureMech:000926.

Both local layers omit distilled water1000mL and the Difco qualifier on yeast extract. Preserve the primary solvent-batch amount and provider solution context rather than assigning water a mass concentration.

### Bicarbonate stock and addition stage

quantity: supported. Targets: CultureMech:000926.

not_quantified/evidence_only:0.16g/L is the final formulation contribution, while the source separately requires a sterilized NaHCO3 stock added after the autoclaved medium cools. The local preparation retains this instruction. Stock strength, addition volume, sterilization conditions and cooling temperature are not supplied and cannot be calculated. No numeric stock recipe is invented.

### pH, agar condition and preparation representation

scope: supported. Targets: CultureMech:000926.

Final pH7.5 and the compound preparation paragraph agree with sources. The pH statement is stored as MIX, a semantic action mismatch despite correct text. SOLID_AGAR denotes the agar-containing option, which is explicitly retained in ingredient notes and preparation. The source gives no strain-specific incubation or growth claim.

### Complex composition and metal flag

scope: supported. Targets: CultureMech:000926.

COMPLEX/UNDEFINED agrees with yeast extract. Under the inspected schema threshold1049.84mM, NaCl alone contributes provider3336.76mM sodium, so high_metal is supported without estimating metals in yeast extract. This computational flag is not metal-toxicity or bioremediation evidence.

### Eight owner concentration evidence objects

evidence: concern. Targets: CultureMech:000926.

evidence_only: all eight maintained snippets are exact substrings and structurally equal to their provider rows, and the current response hash equals the owner cited capture. Their narrow provider-concentration scope is sound. The generated target omits these evidence objects, source reference and later evidence-only history. Yeast extract and preparation still lack narrow evidence.

### History and linkage limits

provenance: supported. Targets: CultureMech:000926.

All history timestamps have timezones. Primary and secondary linkage are each8/9(88.89%) of direct ingredient instances; all asserted identities and live MIM keys resolve. Unmapped yeast extract is a complex material, not a reason to invent a pure-chemical ID. The KG match remains separately unavailable.

## Findings

### f1: Both layers omit source solvent and supplier context

major / open / confirmed; issue key: CM000926-source-solvent-supplier-gap.

DSMZ specifies distilled water1000mL and yeast extract(Difco); both local layers retain only generic yeast extract and omit the solvent row.

### f2: Generated target omits verified owner evidence

major / open / confirmed; issue key: CM000926-stale-quantity-evidence.

Eight exact owner concentration snippets, the MediaDive reference and later evidence-only history are absent from the target. The owner current source hash and row locators were verified.

### f3: Final pH is stored as a mixing action

minor / open / confirmed; issue key: CM000926-ph-action-classification.

The correct final-pH7.5 statement is classified MIX in both layers. It states a condition rather than a mixing operation.

### f4: Yeast and preparation claims lack narrow support

minor / open / confirmed; issue key: CM000926-remaining-claim-evidence-gap.

The owner evidence covers eight solutes but not yeast extract, pH, conditional agar context or the separate bicarbonate addition instruction.

## Recommended Actions And Acceptance Checks

### a1

Restore source supplied-material and literal solvent/batch context in the maintained owner with narrow evidence; verify the denominator before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

After remaining owner corrections, regenerate and confirm the eight source-scoped concentration evidence objects and metadata survive unchanged.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Represent the source pH condition consistently with the schema without inventing an acid/base adjustment procedure.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach exact short support at the narrowest claim; retain unknown stock strength and volume as unquantified.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/28_mh_medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/28_mh_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/28_mh_medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/28_mh_medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch008/076/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/076/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/28_mh_medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/28_mh_medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/28_mh_medium.yaml:1:id: CultureMech:000926<br>./data/normalized_yaml/bacterial/28_mh_medium.yaml:1:id: CultureMech:000926<br> |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:2509 resolves to agar and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32139 resolves to sodium hydrogencarbonate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32588 resolves to potassium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:32599 resolves to magnesium sulfate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi3312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:3312 resolves to calcium dichloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi63004 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63004; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:63004 resolves to sodium bromide and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi6636 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_6636; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:6636 resolves to magnesium dichloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:6636": [{"label": "MgCl2", "match_type": "preferred_term", "identifier": "CHEBI:6636", "preferred_term": "MgCl2", "ontology_id": "CHEBI:6636", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32599": [{"label": "Magnesium sulfate", "match_type": "preferred_term", "identifier": "CHEBI:32599", "preferred_term": "Magnesium sulfate", "ontology_id": "CHEBI:32599", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3312": [{"label": "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312", "preferred_term": "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63004": [{"label": "NaBr", "match_type": "preferred_term", "identifier": "CHEBI:63004", "preferred_term": "NaBr", "ontology_id": "CHEBI:63004", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| dsmz | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1460.pdf; Entire recipe; final-pH and preparation paragraphs | supports | Complete one-page official recipe inspected, including nine solutes with conditional agar, distilled water1000mL, yeast extract(Difco), pH7.5 and separate sterilized bicarbonate stock addition after cooling. MgCl2, MgSO4 and CaCl2 are specified without hydrate suffixes. |
| api | https://mediadive.dsmz.de/rest/medium/1460; data.medium; data.solutions[0].recipe[0:10]; steps | supports | Complete provider record inspected. Main solution volume1000mL and all nine explicit g_l values support the direct concentrations; water is a separate1000mL row. The yeast attribute is Difco. Agar is conditional for solid medium. |
| context | Complete target, owner and captured MediaDive bytes; Every concentration; all eight literal owner snippets and source hash; history timestamps | supports | {"quantities": [{"field": "ingredients[0].concentration", "source_locator": "$.data.solutions[0].recipe[0]", "value_g_l": 195, "source_form": "NaCl", "condition": null, "decision": "verified"}, {"field": "ingredients[1].concentration", "source_locator": "$.data.solutions[0].recipe[1]", "value_g_l": 32.5, "source_form": "MgCl2", "condition": null, "decision": "verified"}, {"field": "ingredients[2].concentration", "source_locator": "$.data.solutions[0].recipe[2]", "value_g_l": 50.8, "source_form": "MgSO4", "condition": null, "decision": "verified"}, {"field": "ingredients[3].concentration", "source_locator": "$.data.solutions[0].recipe[3]", "value_g_l": 0.8, "source_form": "CaCl2", "condition": null, "decision": "verified"}, {"field": "ingredients[4].concentration", "source_locator": "$.data.solutions[0].recipe[4]", "value_g_l": 5, "source_form": "KCl", "condition": null, "decision": "verified"}, {"field": "ingredients[5].concentration", "source_locator": "$.data.solutions[0].recipe[5]", "value_g_l": 0.16, "source_form": "NaHCO3", "condition": null, "decision": "verified"}, {"field": "ingredients[6].concentration", "source_locator": "$.data.solutions[0].recipe[6]", "value_g_l": 0.6, "source_form": "NaBr", "condition": null, "decision": "verified"}, {"field": "ingredients[7].concentration", "source_locator": "$.data.solutions[0].recipe[7]", "value_g_l": 5, "source_form": "Yeast extract", "condition": null, "decision": "verified"}, {"field": "ingredients[8].concentration", "source_locator": "$.data.solutions[0].recipe[9]", "value_g_l": 20, "source_form": "Agar", "condition": "for solid medium", "decision": "verified"}], "literal_and_structurally_exact_owner_excerpt_indices": [0, 1, 2, 3, 4, 5, 6, 8], "source_sha256_matches_owner_historical_capture": true, "water_row": {"recipe_order": 9, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "timezone_bearing_history_counts": [7, 7], "sodium_chloride_provider_mmol_l": 3336.76, "schema_high_metal_threshold_mM": 1049.84} |
| kg-context | Isolated checkout inventory and KGMediaMatcher; Actual recipe projections; graph constructor error; ignored-inclusive file inventory | context_only | {"checked_at": "2026-10-21T07:27:44.488605+00:00", "projection": {"data/merge_yaml/merged/28_mh_medium.yaml": ["CHEBI:2509", "CHEBI:26710", "CHEBI:32139", "CHEBI:32588", "CHEBI:32599", "CHEBI:3312", "CHEBI:63004", "CHEBI:6636"], "data/normalized_yaml/bacterial/28_mh_medium.yaml": ["CHEBI:2509", "CHEBI:26710", "CHEBI:32139", "CHEBI:32588", "CHEBI:32599", "CHEBI:3312", "CHEBI:63004", "CHEBI:6636"]}, "graph_check": {"status": "unavailable", "error": "KG-Microbe mediadive data not found at /private/tmp/culturemech-record-review-20261019-batch-008/data/transformed/mediadive. Expected edges.tsv and nodes.tsv. Please ensure kg-microbe repository is cloned and data is transformed."}, "inventory_command": ["rg", "--files", "--no-ignore", "--hidden", "."], "inventory_count": 64863, "inventory_sha256": "10520531d91e5646a372f835890b309517223f17ea31593d8b08edc707db3f58", "graph_candidates": [], "inventory_scope": "Whole isolated batch008 checkout including hidden and ignored paths; not a whole-machine absence claim."} |
| kg-semantics | src/culturemech/match/kg_media_matcher.py; extract_recipe_ingredients; find_matches; find_exact_match | context_only | The matcher compares primary CHEBI/FOODON sets while ignoring amounts and ungrounded yeast extract. Target and owner project to the same eight IDs. Provider accession identity does not itself prove a graph set match. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Partial completion concerns unavailable KG graph data; the primary recipe and provider API were available. No whole-machine graph absence is asserted.
- No stock strength, stock addition volume, measured final volume or strain-specific growth result was established.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T072907Z-culturemech-000926-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 28_mh_medium (CultureMech:000926)'
started_at: '2026-10-21T07:20:50Z'
finished_at: '2026-10-21T07:29:07Z'
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
summary: DSMZ1460 and MediaDive support all nine direct solute amounts, supplied salt
  forms, pH and conditional agar. Both local layers omit source solvent and Difco
  context; the generated target also lacks eight verified owner evidence objects.
  The asserted KG ingredient-set match cannot be revalidated without its graph snapshot.
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
  - path: .claude/skills/match-kg-microbe/SKILL.md
    sha256: add85aafc1e18164de2a9717cc9d63e5e20f34a1d597568a0c6d8b039c574a99
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
  - path: data/merge_yaml/merged/28_mh_medium.yaml
    sha256: 6c0220d4e314f1e6d7bfcf30a95957ddbee72979921ac641bf6503f376472715
    role: target
  - path: data/normalized_yaml/bacterial/28_mh_medium.yaml
    sha256: 720c3e6aacecba18c9543aa96b346ef111d1c9f1f32fb56ec1bb7f915b232038
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
  - path: scripts/enrich_with_kg_microbe_matches.py
    sha256: 61351f99ef2cb0cef03e74ad92d21dcf3b38df77a06602bdac814974e7728eeb
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
  - path: src/culturemech/match/kg_media_matcher.py
    sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
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
  selection: Task review 76; batch 008 item 6 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding seven task batches contain
    70 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 72 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000926
targets:
- target_id: CultureMech:000926
  path: data/merge_yaml/merged/28_mh_medium.yaml
  label: 28_mh_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/28_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/28_mh_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:000926
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/28_mh_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch008/076/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/076/strict.tsv"
  target_ids:
  - CultureMech:000926
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/28_mh_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:000926
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/28_mh_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:000926
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
  - CultureMech:000926
- check_id: kg-graph
  name: Revalidate asserted KG ingredient-set match
  required: true
  status: unavailable
  summary: Graph nodes/edges including compressed candidates were absent from a hidden/ignored-inclusive
    inventory of this isolated checkout. KGMediaMatcher raises FileNotFoundError.
    The exact provider accession and local eight-ID projection were checked, but the
    graph association remains unverified.
  target_ids:
  - CultureMech:000926
  evidence_ids:
  - kg-context
  - kg-semantics
  - api
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/28_mh_medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T07:29:05Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/28_mh_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T07:29:05Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/28_mh_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:22:03.517596Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/28_mh_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch008/076/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T07:22:06.781733Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/076/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/28_mh_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:22:09.356756Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/28_mh_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:22:10.548176Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T07:29:05Z'
  support: supports
  summary: './data/merge_yaml/merged/28_mh_medium.yaml:1:id: CultureMech:000926

    ./data/normalized_yaml/bacterial/28_mh_medium.yaml:1:id: CultureMech:000926

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:15:14.241118Z'
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
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: CHEBI:32139 resolves to sodium hydrogencarbonate and is not obsolete. This
    verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T06:57:47.406565Z'
  support: supports
  summary: CHEBI:32588 resolves to potassium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi32599
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:24.745258Z'
  support: supports
  summary: CHEBI:32599 resolves to magnesium sulfate and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: chebi3312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:24.822837Z'
  support: supports
  summary: CHEBI:3312 resolves to calcium dichloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 34ed49d95375c80dcb07576c67d04fa77337bfecf406accb283e8c32253b754b
- evidence_id: chebi63004
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63004
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:25.403149Z'
  support: supports
  summary: CHEBI:63004 resolves to sodium bromide and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 2665f3a4301ab51b67b814a8694bc906c1a13c9b301c85a4416891d3f9412c90
- evidence_id: chebi6636
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_6636
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:25.486015Z'
  support: supports
  summary: CHEBI:6636 resolves to magnesium dichloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 62283ffd3dce5ed835af343e697602b91b9230da436a122769d7821dee39a272
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T07:29:05Z'
  support: supports
  summary: '{"CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier":
    "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:6636": [{"label": "MgCl2", "match_type":
    "preferred_term", "identifier": "CHEBI:6636", "preferred_term": "MgCl2", "ontology_id":
    "CHEBI:6636", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32599":
    [{"label": "Magnesium sulfate", "match_type": "preferred_term", "identifier":
    "CHEBI:32599", "preferred_term": "Magnesium sulfate", "ontology_id": "CHEBI:32599",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3312": [{"label":
    "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312", "preferred_term":
    "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type":
    "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id":
    "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63004":
    [{"label": "NaBr", "match_type": "preferred_term", "identifier": "CHEBI:63004",
    "preferred_term": "NaBr", "ontology_id": "CHEBI:63004", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: dsmz
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1460.pdf
  locator: Entire recipe; final-pH and preparation paragraphs
  accessed_at: '2026-10-21T07:16:20.936140Z'
  support: supports
  summary: Complete one-page official recipe inspected, including nine solutes with
    conditional agar, distilled water1000mL, yeast extract(Difco), pH7.5 and separate
    sterilized bicarbonate stock addition after cooling. MgCl2, MgSO4 and CaCl2 are
    specified without hydrate suffixes.
  quote: Final pH 7.5
  snapshot_sha256: f0d24c9d3ca40598a179bb0cb97b959e3fe093a15d069a51197f7684c6158c25
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1460
  locator: data.medium; data.solutions[0].recipe[0:10]; steps
  accessed_at: '2026-10-21T07:16:20.117653Z'
  support: supports
  summary: Complete provider record inspected. Main solution volume1000mL and all
    nine explicit g_l values support the direct concentrations; water is a separate1000mL
    row. The yeast attribute is Difco. Agar is conditional for solid medium.
  snapshot_sha256: 8571789ab6b2128de351ef43c70855ce6d732e103be52d3c8fc01c340d4c0747
- evidence_id: context
  kind: validation
  reference: Complete target, owner and captured MediaDive bytes
  locator: Every concentration; all eight literal owner snippets and source hash;
    history timestamps
  accessed_at: '2026-10-21T07:29:05Z'
  support: supports
  summary: '{"quantities": [{"field": "ingredients[0].concentration", "source_locator":
    "$.data.solutions[0].recipe[0]", "value_g_l": 195, "source_form": "NaCl", "condition":
    null, "decision": "verified"}, {"field": "ingredients[1].concentration", "source_locator":
    "$.data.solutions[0].recipe[1]", "value_g_l": 32.5, "source_form": "MgCl2", "condition":
    null, "decision": "verified"}, {"field": "ingredients[2].concentration", "source_locator":
    "$.data.solutions[0].recipe[2]", "value_g_l": 50.8, "source_form": "MgSO4", "condition":
    null, "decision": "verified"}, {"field": "ingredients[3].concentration", "source_locator":
    "$.data.solutions[0].recipe[3]", "value_g_l": 0.8, "source_form": "CaCl2", "condition":
    null, "decision": "verified"}, {"field": "ingredients[4].concentration", "source_locator":
    "$.data.solutions[0].recipe[4]", "value_g_l": 5, "source_form": "KCl", "condition":
    null, "decision": "verified"}, {"field": "ingredients[5].concentration", "source_locator":
    "$.data.solutions[0].recipe[5]", "value_g_l": 0.16, "source_form": "NaHCO3", "condition":
    null, "decision": "verified"}, {"field": "ingredients[6].concentration", "source_locator":
    "$.data.solutions[0].recipe[6]", "value_g_l": 0.6, "source_form": "NaBr", "condition":
    null, "decision": "verified"}, {"field": "ingredients[7].concentration", "source_locator":
    "$.data.solutions[0].recipe[7]", "value_g_l": 5, "source_form": "Yeast extract",
    "condition": null, "decision": "verified"}, {"field": "ingredients[8].concentration",
    "source_locator": "$.data.solutions[0].recipe[9]", "value_g_l": 20, "source_form":
    "Agar", "condition": "for solid medium", "decision": "verified"}], "literal_and_structurally_exact_owner_excerpt_indices":
    [0, 1, 2, 3, 4, 5, 6, 8], "source_sha256_matches_owner_historical_capture": true,
    "water_row": {"recipe_order": 9, "compound": "Distilled water", "compound_id":
    4, "amount": 1000, "unit": "ml", "optional": 0}, "timezone_bearing_history_counts":
    [7, 7], "sodium_chloride_provider_mmol_l": 3336.76, "schema_high_metal_threshold_mM":
    1049.84}'
- evidence_id: kg-context
  kind: validation
  reference: Isolated checkout inventory and KGMediaMatcher
  locator: Actual recipe projections; graph constructor error; ignored-inclusive file
    inventory
  accessed_at: '2026-10-21T07:27:44.488605Z'
  support: context_only
  summary: '{"checked_at": "2026-10-21T07:27:44.488605+00:00", "projection": {"data/merge_yaml/merged/28_mh_medium.yaml":
    ["CHEBI:2509", "CHEBI:26710", "CHEBI:32139", "CHEBI:32588", "CHEBI:32599", "CHEBI:3312",
    "CHEBI:63004", "CHEBI:6636"], "data/normalized_yaml/bacterial/28_mh_medium.yaml":
    ["CHEBI:2509", "CHEBI:26710", "CHEBI:32139", "CHEBI:32588", "CHEBI:32599", "CHEBI:3312",
    "CHEBI:63004", "CHEBI:6636"]}, "graph_check": {"status": "unavailable", "error":
    "KG-Microbe mediadive data not found at /private/tmp/culturemech-record-review-20261019-batch-008/data/transformed/mediadive.
    Expected edges.tsv and nodes.tsv. Please ensure kg-microbe repository is cloned
    and data is transformed."}, "inventory_command": ["rg", "--files", "--no-ignore",
    "--hidden", "."], "inventory_count": 64863, "inventory_sha256": "10520531d91e5646a372f835890b309517223f17ea31593d8b08edc707db3f58",
    "graph_candidates": [], "inventory_scope": "Whole isolated batch008 checkout including
    hidden and ignored paths; not a whole-machine absence claim."}'
  search_scope: Whole isolated batch008 checkout including hidden and ignored paths;
    not a whole-machine absence claim.
- evidence_id: kg-semantics
  kind: record_content
  reference: src/culturemech/match/kg_media_matcher.py
  locator: extract_recipe_ingredients; find_matches; find_exact_match
  accessed_at: '2026-10-21T07:29:05Z'
  support: context_only
  summary: The matcher compares primary CHEBI/FOODON sets while ignoring amounts and
    ungrounded yeast extract. Target and owner project to the same eight IDs. Provider
    accession identity does not itself prove a graph set match.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:000926
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '8 primary CHEBI identities resolve with matching labels; 8 of 8 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:000926
  evidence_ids:
  - record
  - mim
  - chebi2509
  - chebi26710
  - chebi32139
  - chebi32588
  - chebi32599
  - chebi3312
  - chebi63004
  - chebi6636
  details: 9 direct ingredient instances; CHEBI-primary instance linkage 8/9 (88.89%),
    verified secondary coverage 8/9 (88.89%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: DSMZ1460 and MediaDive accession
  outcome: supported
  summary: The source URL, mediadive.medium:1460 source term and official28% MH MEDIUM
    title identify the same recipe. Numeric28% is retained as a name; no unstated
    percent-basis conversion is inferred.
  target_ids:
  - CultureMech:000926
  evidence_ids:
  - record
  - owner-0
  - id-search
  - dsmz
  - api
- assessment_id: quantities
  area: quantity
  topic: All nine direct concentrations and supplied forms
  outcome: supported
  summary: verified:195,32.5,50.8,0.8,5,0.16,0.6,5 and20g/L match explicit provider
    g_l values in order. Primary source forms support the anhydrous salt labels; hydrated
    substitutions would change the recipe. Agar20g/L is conditional for solid media.
    Provider volume/amount evidence is not an independent final-volume measurement.
  target_ids:
  - CultureMech:000926
  evidence_ids:
  - record
  - dsmz
  - api
  - context
  details: '[{"field": "ingredients[0].concentration", "source_locator": "$.data.solutions[0].recipe[0]",
    "value_g_l": 195, "source_form": "NaCl", "condition": null, "decision": "verified"},
    {"field": "ingredients[1].concentration", "source_locator": "$.data.solutions[0].recipe[1]",
    "value_g_l": 32.5, "source_form": "MgCl2", "condition": null, "decision": "verified"},
    {"field": "ingredients[2].concentration", "source_locator": "$.data.solutions[0].recipe[2]",
    "value_g_l": 50.8, "source_form": "MgSO4", "condition": null, "decision": "verified"},
    {"field": "ingredients[3].concentration", "source_locator": "$.data.solutions[0].recipe[3]",
    "value_g_l": 0.8, "source_form": "CaCl2", "condition": null, "decision": "verified"},
    {"field": "ingredients[4].concentration", "source_locator": "$.data.solutions[0].recipe[4]",
    "value_g_l": 5, "source_form": "KCl", "condition": null, "decision": "verified"},
    {"field": "ingredients[5].concentration", "source_locator": "$.data.solutions[0].recipe[5]",
    "value_g_l": 0.16, "source_form": "NaHCO3", "condition": null, "decision": "verified"},
    {"field": "ingredients[6].concentration", "source_locator": "$.data.solutions[0].recipe[6]",
    "value_g_l": 0.6, "source_form": "NaBr", "condition": null, "decision": "verified"},
    {"field": "ingredients[7].concentration", "source_locator": "$.data.solutions[0].recipe[7]",
    "value_g_l": 5, "source_form": "Yeast extract", "condition": null, "decision":
    "verified"}, {"field": "ingredients[8].concentration", "source_locator": "$.data.solutions[0].recipe[9]",
    "value_g_l": 20, "source_form": "Agar", "condition": "for solid medium", "decision":
    "verified"}]'
- assessment_id: solvent
  area: completeness
  topic: Source solvent and supplied yeast-extract grade
  outcome: concern
  summary: Both local layers omit distilled water1000mL and the Difco qualifier on
    yeast extract. Preserve the primary solvent-batch amount and provider solution
    context rather than assigning water a mass concentration.
  target_ids:
  - CultureMech:000926
  evidence_ids:
  - record
  - owner-0
  - dsmz
  - api
  - context
- assessment_id: stock
  area: quantity
  topic: Bicarbonate stock and addition stage
  outcome: supported
  summary: not_quantified/evidence_only:0.16g/L is the final formulation contribution,
    while the source separately requires a sterilized NaHCO3 stock added after the
    autoclaved medium cools. The local preparation retains this instruction. Stock
    strength, addition volume, sterilization conditions and cooling temperature are
    not supplied and cannot be calculated. No numeric stock recipe is invented.
  target_ids:
  - CultureMech:000926
  evidence_ids:
  - record
  - owner-0
  - dsmz
  - api
- assessment_id: preparation
  area: scope
  topic: pH, agar condition and preparation representation
  outcome: supported
  summary: Final pH7.5 and the compound preparation paragraph agree with sources.
    The pH statement is stored as MIX, a semantic action mismatch despite correct
    text. SOLID_AGAR denotes the agar-containing option, which is explicitly retained
    in ingredient notes and preparation. The source gives no strain-specific incubation
    or growth claim.
  target_ids:
  - CultureMech:000926
  evidence_ids:
  - record
  - owner-0
  - dsmz
  - api
- assessment_id: flags
  area: scope
  topic: Complex composition and metal flag
  outcome: supported
  summary: COMPLEX/UNDEFINED agrees with yeast extract. Under the inspected schema
    threshold1049.84mM, NaCl alone contributes provider3336.76mM sodium, so high_metal
    is supported without estimating metals in yeast extract. This computational flag
    is not metal-toxicity or bioremediation evidence.
  target_ids:
  - CultureMech:000926
  evidence_ids:
  - record
  - api
  - context
- assessment_id: freshness
  area: evidence
  topic: Eight owner concentration evidence objects
  outcome: concern
  summary: 'evidence_only: all eight maintained snippets are exact substrings and
    structurally equal to their provider rows, and the current response hash equals
    the owner cited capture. Their narrow provider-concentration scope is sound. The
    generated target omits these evidence objects, source reference and later evidence-only
    history. Yeast extract and preparation still lack narrow evidence.'
  target_ids:
  - CultureMech:000926
  evidence_ids:
  - record
  - owner-0
  - api
  - context
  - validate-references
- assessment_id: history
  area: provenance
  topic: History and linkage limits
  outcome: supported
  summary: All history timestamps have timezones. Primary and secondary linkage are
    each8/9(88.89%) of direct ingredient instances; all asserted identities and live
    MIM keys resolve. Unmapped yeast extract is a complex material, not a reason to
    invent a pure-chemical ID. The KG match remains separately unavailable.
  target_ids:
  - CultureMech:000926
  evidence_ids:
  - record
  - owner-0
  - context
  - mim
  - kg-context
findings:
- finding_id: f1
  issue_key: CM000926-source-solvent-supplier-gap
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Both layers omit source solvent and supplier context
  description: DSMZ specifies distilled water1000mL and yeast extract(Difco); both
    local layers retain only generic yeast extract and omit the solvent row.
  target_ids:
  - CultureMech:000926
  field_paths:
  - ingredients
  evidence_ids:
  - record
  - owner-0
  - dsmz
  - api
  - context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/28_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CM000926-stale-quantity-evidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generated target omits verified owner evidence
  description: Eight exact owner concentration snippets, the MediaDive reference and
    later evidence-only history are absent from the target. The owner current source
    hash and row locators were verified.
  target_ids:
  - CultureMech:000926
  field_paths:
  - ingredients[*].evidence
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - api
  - context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/28_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM000926-ph-action-classification
  category: schema
  severity: minor
  status: open
  certainty: confirmed
  title: Final pH is stored as a mixing action
  description: The correct final-pH7.5 statement is classified MIX in both layers.
    It states a condition rather than a mixing operation.
  target_ids:
  - CultureMech:000926
  field_paths:
  - preparation_steps[0]
  evidence_ids:
  - record
  - owner-0
  - dsmz
  - api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/28_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: CM000926-remaining-claim-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Yeast and preparation claims lack narrow support
  description: The owner evidence covers eight solutes but not yeast extract, pH,
    conditional agar context or the separate bicarbonate addition instruction.
  target_ids:
  - CultureMech:000926
  field_paths:
  - ingredients[7].evidence
  - preparation_steps
  - ph_value
  evidence_ids:
  - record
  - owner-0
  - dsmz
  - api
  - context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/28_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Restore source supplied-material and literal solvent/batch context
    in the maintained owner with narrow evidence; verify the denominator before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000926
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/28_mh_medium.yaml
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
  description: After remaining owner corrections, regenerate and confirm the eight
    source-scoped concentration evidence objects and metadata survive unchanged.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000926
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/28_mh_medium.yaml
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
  description: Represent the source pH condition consistently with the schema without
    inventing an acid/base adjustment procedure.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000926
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/28_mh_medium.yaml
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
  description: Attach exact short support at the narrowest claim; retain unknown stock
    strength and volume as unquantified.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000926
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/28_mh_medium.yaml
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
- Partial completion concerns unavailable KG graph data; the primary recipe and provider
  API were available. No whole-machine graph absence is asserted.
- No stock strength, stock addition volume, measured final volume or strain-specific
  growth result was established.
tags:
- unreviewed-records
- batch-008
- generated-medium
```
