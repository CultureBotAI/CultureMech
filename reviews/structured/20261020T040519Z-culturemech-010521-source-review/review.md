# Source and formulation review: 1_10_sabourauds_agar (CultureMech:010521)

- Review: 20261020T040519Z-culturemech-010521-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-20T04:02:03Z
- Finished UTC: 2026-10-20T04:05:19Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated J35 record preserves all six source ingredient amounts and forms, including the primary sodium-nitrate identity. It lacks the JCM default sterilization/water-batch context and omits claim-level evidence already present in its maintained owner. The legacy secondary identifier MediaIngredientMech:000171 cannot be verified against an available historical registry, so scientific completion is partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 34 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010521 | data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml | generated | 1_10_sabourauds_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010521 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010521 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/034/strict.tsv |
| validate-terms | passed | True | CultureMech:010521 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010521 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010521 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Historical MIM identifier identity | unavailable | True | CultureMech:010521 | The available pinned registry no longer resolves MediaIngredientMech:000171. Whole-checkout ignored-inclusive discovery did not provide the historical mapping required to verify it. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010521.

The four documented recipes completed; interpret the scope of each separately.

### Target, accession and input ownership

identity: supported. Targets: CultureMech:010521.

CultureMech:010521 resolves to the generated suffixed path and fungal normalized owner. The J35 accession, title and source URL correspond to JCM 35.

The suffix distinguishes a second generated record with the same normalized name; it is not an invented source accession. The source-related TOGO sibling remains a separate contextual record. The selected target has one owner and no asserted internal CultureMech recipe link requiring resolution.

### ingredients[0].concentration: Glucose

quantity: supported. Targets: CultureMech:010521.

verified: 4 G_PER_L agrees with the explicit provider g_l and 1000 mL volume; the primary collection lists the corresponding ingredient mass.

The exact owner evidence row also matches the current parsed API recipe row. These are direct full-medium components, not stock composition or dilution. The source name does not authorize further tenfold dilution. No mass/molar conversion is needed.

### ingredients[1].concentration: Peptone

quantity: supported. Targets: CultureMech:010521.

verified: 1 G_PER_L agrees with the explicit provider g_l and 1000 mL volume; the primary collection lists the corresponding ingredient mass.

The exact owner evidence row also matches the current parsed API recipe row. These are direct full-medium components, not stock composition or dilution. The source name does not authorize further tenfold dilution. No mass/molar conversion is needed.

### ingredients[2].concentration: KH2PO4

quantity: supported. Targets: CultureMech:010521.

verified: 1.5 G_PER_L agrees with the explicit provider g_l and 1000 mL volume; the primary collection lists the corresponding ingredient mass.

The exact owner evidence row also matches the current parsed API recipe row. These are direct full-medium components, not stock composition or dilution. The source name does not authorize further tenfold dilution. No mass/molar conversion is needed.

### ingredients[3].concentration: MgSO4 x 7 H2O

quantity: supported. Targets: CultureMech:010521.

verified: 1 G_PER_L agrees with the explicit provider g_l and 1000 mL volume; the primary collection lists the corresponding ingredient mass.

The exact owner evidence row also matches the current parsed API recipe row. These are direct full-medium components, not stock composition or dilution. The source name does not authorize further tenfold dilution. No mass/molar conversion is needed.

### ingredients[4].concentration: NaNO3

quantity: supported. Targets: CultureMech:010521.

verified: 1 G_PER_L agrees with the explicit provider g_l and 1000 mL volume; the primary collection lists the corresponding ingredient mass.

The exact owner evidence row also matches the current parsed API recipe row. These are direct full-medium components, not stock composition or dilution. The source name does not authorize further tenfold dilution. No mass/molar conversion is needed.

### ingredients[5].concentration: Agar

quantity: supported. Targets: CultureMech:010521.

verified: 20 G_PER_L agrees with the explicit provider g_l and 1000 mL volume; the primary collection lists the corresponding ingredient mass.

The exact owner evidence row also matches the current parsed API recipe row. These are direct full-medium components, not stock composition or dilution. The source name does not authorize further tenfold dilution. No mass/molar conversion is needed.

### Supplied forms and current ontology keys

grounding: supported. Targets: CultureMech:010521.

All five primary CHEBI IDs and four current secondary CHEBI keys resolve. The source heptahydrate and monopotassium dihydrogen phosphate forms agree with their mappings. Peptone is not assigned an invented pure-chemical identity.

Six direct ingredient instances; five have primary CHEBI terms (83.33% linkage), four have verified current secondary keys (66.67%), and one additional secondary link is unresolved historical MIM. All percentages use denominator six, 0–100 scale and measure linkage only. The valid primary sodium-nitrate CHEBI term does not resolve the separate legacy MIM link.

### Historical sodium-nitrate secondary link

grounding: unknown. Targets: CultureMech:010521.

The required identity of MediaIngredientMech:000171 remains unresolved. Its label is plausible but repetition and the independent primary CHEBI term do not prove its historical registry meaning.

This is an unavailable identity check, not a confirmed wrong-ID allegation. Follow-up requires an authoritative historical mapping or separately reviewed migration to a supported current key. No ID replacement or removal is performed, and no successful schema/term check is taken as that historical verification.

### pH and physical-state scope

consistency: supported. Targets: CultureMech:010521.

The provider explicitly reports pH 6.9, while the target preparation retains the primary adjustment range. Agar supports SOLID_AGAR, and the formulation is COMPLEX/UNDEFINED because of peptone.

The 6.9 value is provider metadata, not an independent measurement. The source range remains explicit in preparation and should be preserved in any curation. No incubation, organism, atmosphere, storage or other growth condition is asserted. Bacterial/fungal filing differences between providers do not establish exclusive growth scope.

### Collection default and solvent-batch context

completeness: concern. Targets: CultureMech:010521.

The target and maintained owner omit JCM page-default sterilization and source distilled-water batch context, despite preserving the pH-adjustment step.

No separately prepared stock is asserted; the API main solution is the complete medium. A missing water row is not a numeric mass error like the TOGO sibling; it is missing preparation/batch context. Represent the source water amount without equating it to a measured final volume.

### Generated evidence versus maintained owner

provenance: concern. Targets: CultureMech:010521.

All six owner ingredient evidence objects, bibliographic reference and later curation event are absent from the generated target. The reference gate examined zero excerpts.

Full target and both owners were read. These absence findings are bounded to exact complete objects; no global missing-artifact claim is made. Current merger preservation means the practical action is controlled regeneration after remaining owner corrections, not editing the derived YAML or blindly changing current merge code. History describes provenance; its old execution is not re-certified.

## Findings

### f1: Collection preparation and water basis are incomplete

major / open / confirmed; issue key: culturemech-010521-preparation-context-omitted.

The existing preparation step preserves pH but omits the applicable collection default sterilization. Source distilled-water batch context is also absent from owner and target.

### f2: Generated record omits six maintained concentration-evidence entries

minor / open / confirmed; issue key: culturemech-010521-generated-evidence-stale.

The normalized owner has six scoped evidence entries and a source reference that are absent from this earlier generated snapshot. The numerical values match current provider data, so this is a nonblocking evidence-currentness defect independent of unresolved legacy identity.

## Recommended Actions And Acceptance Checks

### a1

Add source-supported default preparation and solvent-batch context to the maintained record with evidence; preserve the source pH range and avoid inferred incubation or final-volume precision.

- Verify maintained source details against the complete JCM 35 page, including its default header.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on authorized maintained corrections.
- Regenerate with the maintained merge entrypoint, then run just verify-merges and just audit-merge-freshness.

### a2

Regenerate from the maintained owner after separately authorized curation, retaining all claim-level evidence and append-only history. Do not re-add already present owner evidence or hand-edit the derived file.

- Verify maintained source details against the complete JCM 35 page, including its default header.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on authorized maintained corrections.
- Regenerate with the maintained merge entrypoint, then run just verify-merges and just audit-merge-freshness.
- Confirm all six evidence objects and their reference survive generated output without changed scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch004/034/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/034/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| jcm | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=35; Entire recipe and applicable default at page top | supports | JCM 35 provides the six solute masses, distilled-water batch and pH adjustment range. Its page-level default sterilization applies unless otherwise stated; this entry provides no exception. |
| api | https://mediadive.dsmz.de/rest/medium/J35; data.medium and complete data.solutions[0] | supports | J35 is sourced from JCM 35. Solution 3658 has volume 1000 mL and explicit g_l values for all six solutes. The API pH metadata is 6.9 while the preparation step retains the range. |
| bacmedia | https://bacmedia.dsmz.de/pdf/J35; Page 1, header, composition and adjustment | supports | The rendering gives final volume 1000 mL, all source amounts and pH-adjustment range, with a 6.9 pH header. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M28; meta, components and comments | supports | Contextual cross-check: TOGO M28 points to the same JCM 35 source and retains the original pH range and seven ingredient rows. This does not make its local sibling a reviewed target. |
| sibling | data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml; Complete contextual owner | context_only | This distinct TOGO owner refers to the same collection recipe but differs in water, pH, representation and evidence. It is context only for the selected MediaDive-derived target. |
| chebi-17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact term identifier, label, definition, chemical form and obsolete flag | supports | CHEBI:17234 resolves to glucose, nonobsolete=True. Source supplied form agrees; no extra stereochemistry, hydration or molarity inferred. |
| chebi-63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact term identifier, label, definition, chemical form and obsolete flag | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate, nonobsolete=True. Source supplied form agrees; no extra stereochemistry, hydration or molarity inferred. |
| chebi-31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact term identifier, label, definition, chemical form and obsolete flag | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate, nonobsolete=True. Source supplied form agrees; no extra stereochemistry, hydration or molarity inferred. |
| chebi-63005 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63005; Exact term identifier, label, definition, chemical form and obsolete flag | supports | CHEBI:63005 resolves to sodium nitrate, nonobsolete=True. Source supplied form agrees; no extra stereochemistry, hydration or molarity inferred. |
| chebi-2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact term identifier, label, definition, chemical form and obsolete flag | supports | CHEBI:2509 resolves to agar, nonobsolete=True. Source supplied form agrees; no extra stereochemistry, hydration or molarity inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Current pinned index, exact identifier searches and live preferred-term rows | context_only | {"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}; exact legacy key matches=0 |
| legacy-search | repository checkout; Whole-checkout ignored-inclusive file and identifier discovery | context_only | MediaIngredientMech:000171 occurs in 476 files, but the current pinned index has no matching legacy key. File discovery found the packaged current index and code/schema/docs, not a historical mapped-ingredient registry resolving this key. Occurrence frequency is not identity evidence. Registry candidates: ["docs/unmapped_ingredients_guide.md", "docs/archive/UNMAPPED_INGREDIENTS_SUMMARY.md", "src/culturemech/data/mediaingredientmech/label_index.csv", "src/culturemech/data/mediaingredientmech/label_index.metadata.json", "src/culturemech/schema/unmapped_ingredients_schema.yaml", "src/culturemech/schema/mapped_ingredients_schema.yaml", "src/culturemech/ingredients/mim_label_index.py", "tests/test_mim_label_index.py", "tests/test_refresh_mim_label_index.py", "scripts/refresh_mim_label_index.py", "scripts/aggregate_unmapped_ingredients.py", "scripts/aggregate_mapped_ingredients.py", "scripts/check_mim_label_index.py", "scripts/unmapped_ingredients_stats.py"] |
| ids | repository checkout; Whole-checkout exact top-level CultureMech ID search | supports | ./data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml:1:id: CultureMech:010521<br>./data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml:1:id: CultureMech:010521<br>./data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml:1:id: CultureMech:009437<br>./data/merge_yaml/merged/1_10_sabourauds_agar.yaml:1:id: CultureMech:009437<br> |
| owner-evidence | data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml; All six ingredient evidence entries, root reference, October curation event and API row comparisons | supports | Six parsed evidence objects match the live corresponding API recipe rows; their amount values, units, names, g_l and optional flags agree. The owner documents the provider volume and limitations. The generated target has none of those evidence entries or that later reference/history. Comparisons: [{"ingredient": "Glucose", "snippet_json_matches_current_api_row": true, "g_l": 4, "target_mass": {"value": "4", "unit": "G_PER_L"}, "volume": 1000}, {"ingredient": "Peptone", "snippet_json_matches_current_api_row": true, "g_l": 1, "target_mass": {"value": "1", "unit": "G_PER_L"}, "volume": 1000}, {"ingredient": "KH2PO4", "snippet_json_matches_current_api_row": true, "g_l": 1.5, "target_mass": {"value": "1.5", "unit": "G_PER_L"}, "volume": 1000}, {"ingredient": "MgSO4 x 7 H2O", "snippet_json_matches_current_api_row": true, "g_l": 1, "target_mass": {"value": "1", "unit": "G_PER_L"}, "volume": 1000}, {"ingredient": "NaNO3", "snippet_json_matches_current_api_row": true, "g_l": 1, "target_mass": {"value": "1", "unit": "G_PER_L"}, "volume": 1000}, {"ingredient": "Agar", "snippet_json_matches_current_api_row": true, "g_l": 20, "target_mass": {"value": "20", "unit": "G_PER_L"}, "volume": 1000}] |
| merge-code | src/culturemech/merge/merger.py; merge_group singleton branch and formulation evidence-preservation helper | supports | Current singleton merge returns the loaded record including its evidence; formulation-aware multiple-record merging also retains scoped evidence. The target is an earlier generated snapshot with one owner. Missing owner evidence is output freshness, not evidence that current code necessarily strips it. |

## Limits And Additional Notes

- Historical identity verification for MediaIngredientMech:000171 is unavailable. Current CHEBI identity verification does not establish the meaning of a retired MIM numeric identifier.
- Owner evidence was compared as parsed JSON with live API rows; this does not claim byte-for-byte whitespace matching or a retrospective certification of the earlier source download.
- BacMedia/API explicitly provide normalization volume. No physical final-volume measurement, unspecified stock dilution or organism-specific growth inference is made.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Required historical-identifier verification is unavailable, so this valid saved bundle must not be read as a completed scientific review. The unverified legacy link is recorded as unknown rather than asserted erroneous.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T040519Z-culturemech-010521-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_10_sabourauds_agar (CultureMech:010521)'
started_at: '2026-10-20T04:02:03Z'
finished_at: '2026-10-20T04:05:19Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or edit these assessed recipe bytes;
    an independent agent review of frozen inputs and inspected collection sources,
    not experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The generated J35 record preserves all six source ingredient amounts and
  forms, including the primary sodium-nitrate identity. It lacks the JCM default sterilization/water-batch
  context and omits claim-level evidence already present in its maintained owner.
  The legacy secondary identifier MediaIngredientMech:000171 cannot be verified against
  an available historical registry, so scientific completion is partial.
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
  - path: data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml
    sha256: 428a2adc6ee884b1358ed6ff458ab12c2c399fd49200ad1bc15026ec0cf924b5
    role: target
  - path: data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml
    sha256: 95f60e7f47f5d288b7b2dc4feeaeec6ece9ab505dde09ca080192af2277afedb
    role: context
  - path: data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml
    sha256: 1f5ddfb7899c262e248e89912b7c2e78e8c6f0ccda5fa903a80b116c8c860515
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
  selection: Record 34 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010521
targets:
- target_id: CultureMech:010521
  path: data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml
  label: 1_10_sabourauds_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch004/034/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/034/strict.tsv"
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010521
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
  - CultureMech:010521
- check_id: legacy-mim-identity
  name: Historical MIM identifier identity
  required: true
  status: unavailable
  summary: The available pinned registry no longer resolves MediaIngredientMech:000171.
    Whole-checkout ignored-inclusive discovery did not provide the historical mapping
    required to verify it.
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - legacy-search
  - mim
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-20T04:05:19Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T04:05:19Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T04:02:09.795625Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch004/034/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-20T04:02:11.040768Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/034/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T04:02:12.426968Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T04:02:13.267218Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: jcm
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=35
  locator: Entire recipe and applicable default at page top
  accessed_at: '2026-10-20T04:02:31.634174Z'
  support: supports
  summary: JCM 35 provides the six solute masses, distilled-water batch and pH adjustment
    range. Its page-level default sterilization applies unless otherwise stated; this
    entry provides no exception.
  quote: Adjust pH to 6.8-7.0.
  snapshot_sha256: eeaba7bc7ca708cf1a08321f2c3e46942ea17aea622b28287515a3eb53f41bf5
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J35
  locator: data.medium and complete data.solutions[0]
  accessed_at: '2026-10-20T04:02:33.781202Z'
  support: supports
  summary: J35 is sourced from JCM 35. Solution 3658 has volume 1000 mL and explicit
    g_l values for all six solutes. The API pH metadata is 6.9 while the preparation
    step retains the range.
  snapshot_sha256: c9db6996d60d6c0fe9b2b5fedc6b94baebf1daf35b0b26fa8280fc5045b25f27
- evidence_id: bacmedia
  kind: database
  reference: https://bacmedia.dsmz.de/pdf/J35
  locator: Page 1, header, composition and adjustment
  accessed_at: '2026-10-20T04:02:34.311188Z'
  support: supports
  summary: The rendering gives final volume 1000 mL, all source amounts and pH-adjustment
    range, with a 6.9 pH header.
  quote: 'Final volume: 1000 ml'
  snapshot_sha256: 548719824d623168addd562310f09dfae0bd6d4ac0308dbe0af3efd8edef6daa
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M28
  locator: meta, components and comments
  accessed_at: '2026-10-20T04:02:33.126259Z'
  support: supports
  summary: 'Contextual cross-check: TOGO M28 points to the same JCM 35 source and
    retains the original pH range and seven ingredient rows. This does not make its
    local sibling a reviewed target.'
  snapshot_sha256: d339cc9771a6b674263da0d8f6a135d2d49aa6567ee8a3e327407f114b057b22
- evidence_id: sibling
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml
  locator: Complete contextual owner
  accessed_at: '2026-10-20T04:05:19Z'
  support: context_only
  summary: This distinct TOGO owner refers to the same collection recipe but differs
    in water, pH, representation and evidence. It is context only for the selected
    MediaDive-derived target.
- evidence_id: chebi-17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact term identifier, label, definition, chemical form and obsolete flag
  accessed_at: '2026-10-20T03:57:32.595833Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose, nonobsolete=True. Source supplied form
    agrees; no extra stereochemistry, hydration or molarity inferred.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi-63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact term identifier, label, definition, chemical form and obsolete flag
  accessed_at: '2026-10-20T04:02:35.727546Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate, nonobsolete=True.
    Source supplied form agrees; no extra stereochemistry, hydration or molarity inferred.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi-31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact term identifier, label, definition, chemical form and obsolete flag
  accessed_at: '2026-10-20T03:57:34.006322Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate, nonobsolete=True.
    Source supplied form agrees; no extra stereochemistry, hydration or molarity inferred.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi-63005
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63005
  locator: Exact term identifier, label, definition, chemical form and obsolete flag
  accessed_at: '2026-10-20T04:02:36.443517Z'
  support: supports
  summary: CHEBI:63005 resolves to sodium nitrate, nonobsolete=True. Source supplied
    form agrees; no extra stereochemistry, hydration or molarity inferred.
  snapshot_sha256: 1ec6a815a0e22ba0d12f84ad998bef39b9e6b80cf90c25cd1ab51903bbb54da3
- evidence_id: chebi-2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact term identifier, label, definition, chemical form and obsolete flag
  accessed_at: '2026-10-20T03:57:34.697126Z'
  support: supports
  summary: CHEBI:2509 resolves to agar, nonobsolete=True. Source supplied form agrees;
    no extra stereochemistry, hydration or molarity inferred.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Current pinned index, exact identifier searches and live preferred-term
    rows
  accessed_at: '2026-10-20T04:05:19Z'
  support: context_only
  summary: '{"CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}; exact legacy key matches=0'
- evidence_id: legacy-search
  kind: record_content
  reference: repository checkout
  locator: Whole-checkout ignored-inclusive file and identifier discovery
  accessed_at: '2026-10-20T04:04:07.104805Z'
  support: context_only
  summary: 'MediaIngredientMech:000171 occurs in 476 files, but the current pinned
    index has no matching legacy key. File discovery found the packaged current index
    and code/schema/docs, not a historical mapped-ingredient registry resolving this
    key. Occurrence frequency is not identity evidence. Registry candidates: ["docs/unmapped_ingredients_guide.md",
    "docs/archive/UNMAPPED_INGREDIENTS_SUMMARY.md", "src/culturemech/data/mediaingredientmech/label_index.csv",
    "src/culturemech/data/mediaingredientmech/label_index.metadata.json", "src/culturemech/schema/unmapped_ingredients_schema.yaml",
    "src/culturemech/schema/mapped_ingredients_schema.yaml", "src/culturemech/ingredients/mim_label_index.py",
    "tests/test_mim_label_index.py", "tests/test_refresh_mim_label_index.py", "scripts/refresh_mim_label_index.py",
    "scripts/aggregate_unmapped_ingredients.py", "scripts/aggregate_mapped_ingredients.py",
    "scripts/check_mim_label_index.py", "scripts/unmapped_ingredients_stats.py"]'
  search_scope: rg --no-ignore --hidden -l for the exact legacy ID; rg --files --no-ignore
    --hidden for whole-checkout filenames; all exact values inspected in packaged
    index. No claim that an external historical registry never existed.
- evidence_id: ids
  kind: record_content
  reference: repository checkout
  locator: Whole-checkout exact top-level CultureMech ID search
  accessed_at: '2026-10-20T04:04:07.104805Z'
  support: supports
  summary: './data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml:1:id: CultureMech:010521

    ./data/merge_yaml/merged/1_10_sabourauds_agar__6d784de4.yaml:1:id: CultureMech:010521

    ./data/normalized_yaml/bacterial/1_10_sabourauds_agar.yaml:1:id: CultureMech:009437

    ./data/merge_yaml/merged/1_10_sabourauds_agar.yaml:1:id: CultureMech:009437

    '
  search_scope: Ignored and hidden files included, normalized/generated layers distinguished.
- evidence_id: owner-evidence
  kind: record_content
  reference: data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml
  locator: All six ingredient evidence entries, root reference, October curation event
    and API row comparisons
  accessed_at: '2026-10-20T04:04:07.104805Z'
  support: supports
  summary: 'Six parsed evidence objects match the live corresponding API recipe rows;
    their amount values, units, names, g_l and optional flags agree. The owner documents
    the provider volume and limitations. The generated target has none of those evidence
    entries or that later reference/history. Comparisons: [{"ingredient": "Glucose",
    "snippet_json_matches_current_api_row": true, "g_l": 4, "target_mass": {"value":
    "4", "unit": "G_PER_L"}, "volume": 1000}, {"ingredient": "Peptone", "snippet_json_matches_current_api_row":
    true, "g_l": 1, "target_mass": {"value": "1", "unit": "G_PER_L"}, "volume": 1000},
    {"ingredient": "KH2PO4", "snippet_json_matches_current_api_row": true, "g_l":
    1.5, "target_mass": {"value": "1.5", "unit": "G_PER_L"}, "volume": 1000}, {"ingredient":
    "MgSO4 x 7 H2O", "snippet_json_matches_current_api_row": true, "g_l": 1, "target_mass":
    {"value": "1", "unit": "G_PER_L"}, "volume": 1000}, {"ingredient": "NaNO3", "snippet_json_matches_current_api_row":
    true, "g_l": 1, "target_mass": {"value": "1", "unit": "G_PER_L"}, "volume": 1000},
    {"ingredient": "Agar", "snippet_json_matches_current_api_row": true, "g_l": 20,
    "target_mass": {"value": "20", "unit": "G_PER_L"}, "volume": 1000}]'
- evidence_id: merge-code
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group singleton branch and formulation evidence-preservation helper
  accessed_at: '2026-10-20T04:05:19Z'
  support: supports
  summary: Current singleton merge returns the loaded record including its evidence;
    formulation-aware multiple-record merging also retains scoped evidence. The target
    is an earlier generated snapshot with one owner. Missing owner evidence is output
    freshness, not evidence that current code necessarily strips it.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Target, accession and input ownership
  outcome: supported
  summary: CultureMech:010521 resolves to the generated suffixed path and fungal normalized
    owner. The J35 accession, title and source URL correspond to JCM 35.
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - record
  - owner-0
  - ids
  - jcm
  - api
  details: The suffix distinguishes a second generated record with the same normalized
    name; it is not an invented source accession. The source-related TOGO sibling
    remains a separate contextual record. The selected target has one owner and no
    asserted internal CultureMech recipe link requiring resolution.
- assessment_id: amount-0
  area: quantity
  topic: 'ingredients[0].concentration: Glucose'
  outcome: supported
  summary: 'verified: 4 G_PER_L agrees with the explicit provider g_l and 1000 mL
    volume; the primary collection lists the corresponding ingredient mass.'
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - record
  - jcm
  - api
  - bacmedia
  - owner-evidence
  details: The exact owner evidence row also matches the current parsed API recipe
    row. These are direct full-medium components, not stock composition or dilution.
    The source name does not authorize further tenfold dilution. No mass/molar conversion
    is needed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Provider-declared mass-per-liter concentration verified; primary recipe
      mass and provider volume are distinguished
    evidence_ids:
    - api
    - bacmedia
    - jcm
- assessment_id: amount-1
  area: quantity
  topic: 'ingredients[1].concentration: Peptone'
  outcome: supported
  summary: 'verified: 1 G_PER_L agrees with the explicit provider g_l and 1000 mL
    volume; the primary collection lists the corresponding ingredient mass.'
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - record
  - jcm
  - api
  - bacmedia
  - owner-evidence
  details: The exact owner evidence row also matches the current parsed API recipe
    row. These are direct full-medium components, not stock composition or dilution.
    The source name does not authorize further tenfold dilution. No mass/molar conversion
    is needed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Provider-declared mass-per-liter concentration verified; primary recipe
      mass and provider volume are distinguished
    evidence_ids:
    - api
    - bacmedia
    - jcm
- assessment_id: amount-2
  area: quantity
  topic: 'ingredients[2].concentration: KH2PO4'
  outcome: supported
  summary: 'verified: 1.5 G_PER_L agrees with the explicit provider g_l and 1000 mL
    volume; the primary collection lists the corresponding ingredient mass.'
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - record
  - jcm
  - api
  - bacmedia
  - owner-evidence
  details: The exact owner evidence row also matches the current parsed API recipe
    row. These are direct full-medium components, not stock composition or dilution.
    The source name does not authorize further tenfold dilution. No mass/molar conversion
    is needed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Provider-declared mass-per-liter concentration verified; primary recipe
      mass and provider volume are distinguished
    evidence_ids:
    - api
    - bacmedia
    - jcm
- assessment_id: amount-3
  area: quantity
  topic: 'ingredients[3].concentration: MgSO4 x 7 H2O'
  outcome: supported
  summary: 'verified: 1 G_PER_L agrees with the explicit provider g_l and 1000 mL
    volume; the primary collection lists the corresponding ingredient mass.'
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - record
  - jcm
  - api
  - bacmedia
  - owner-evidence
  details: The exact owner evidence row also matches the current parsed API recipe
    row. These are direct full-medium components, not stock composition or dilution.
    The source name does not authorize further tenfold dilution. No mass/molar conversion
    is needed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Provider-declared mass-per-liter concentration verified; primary recipe
      mass and provider volume are distinguished
    evidence_ids:
    - api
    - bacmedia
    - jcm
- assessment_id: amount-4
  area: quantity
  topic: 'ingredients[4].concentration: NaNO3'
  outcome: supported
  summary: 'verified: 1 G_PER_L agrees with the explicit provider g_l and 1000 mL
    volume; the primary collection lists the corresponding ingredient mass.'
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - record
  - jcm
  - api
  - bacmedia
  - owner-evidence
  details: The exact owner evidence row also matches the current parsed API recipe
    row. These are direct full-medium components, not stock composition or dilution.
    The source name does not authorize further tenfold dilution. No mass/molar conversion
    is needed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Provider-declared mass-per-liter concentration verified; primary recipe
      mass and provider volume are distinguished
    evidence_ids:
    - api
    - bacmedia
    - jcm
- assessment_id: amount-5
  area: quantity
  topic: 'ingredients[5].concentration: Agar'
  outcome: supported
  summary: 'verified: 20 G_PER_L agrees with the explicit provider g_l and 1000 mL
    volume; the primary collection lists the corresponding ingredient mass.'
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - record
  - jcm
  - api
  - bacmedia
  - owner-evidence
  details: The exact owner evidence row also matches the current parsed API recipe
    row. These are direct full-medium components, not stock composition or dilution.
    The source name does not authorize further tenfold dilution. No mass/molar conversion
    is needed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Provider-declared mass-per-liter concentration verified; primary recipe
      mass and provider volume are distinguished
    evidence_ids:
    - api
    - bacmedia
    - jcm
- assessment_id: chemistry
  area: grounding
  topic: Supplied forms and current ontology keys
  outcome: supported
  summary: All five primary CHEBI IDs and four current secondary CHEBI keys resolve.
    The source heptahydrate and monopotassium dihydrogen phosphate forms agree with
    their mappings. Peptone is not assigned an invented pure-chemical identity.
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - record
  - mim
  - chebi-17234
  - chebi-63036
  - chebi-31795
  - chebi-63005
  - chebi-2509
  details: Six direct ingredient instances; five have primary CHEBI terms (83.33%
    linkage), four have verified current secondary keys (66.67%), and one additional
    secondary link is unresolved historical MIM. All percentages use denominator six,
    0–100 scale and measure linkage only. The valid primary sodium-nitrate CHEBI term
    does not resolve the separate legacy MIM link.
- assessment_id: legacy
  area: grounding
  topic: Historical sodium-nitrate secondary link
  outcome: unknown
  summary: The required identity of MediaIngredientMech:000171 remains unresolved.
    Its label is plausible but repetition and the independent primary CHEBI term do
    not prove its historical registry meaning.
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - record
  - mim
  - legacy-search
  details: This is an unavailable identity check, not a confirmed wrong-ID allegation.
    Follow-up requires an authoritative historical mapping or separately reviewed
    migration to a supported current key. No ID replacement or removal is performed,
    and no successful schema/term check is taken as that historical verification.
- assessment_id: conditions
  area: consistency
  topic: pH and physical-state scope
  outcome: supported
  summary: The provider explicitly reports pH 6.9, while the target preparation retains
    the primary adjustment range. Agar supports SOLID_AGAR, and the formulation is
    COMPLEX/UNDEFINED because of peptone.
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - record
  - jcm
  - api
  - bacmedia
  details: The 6.9 value is provider metadata, not an independent measurement. The
    source range remains explicit in preparation and should be preserved in any curation.
    No incubation, organism, atmosphere, storage or other growth condition is asserted.
    Bacterial/fungal filing differences between providers do not establish exclusive
    growth scope.
- assessment_id: preparation
  area: completeness
  topic: Collection default and solvent-batch context
  outcome: concern
  summary: The target and maintained owner omit JCM page-default sterilization and
    source distilled-water batch context, despite preserving the pH-adjustment step.
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - record
  - owner-0
  - jcm
  - api
  - bacmedia
  details: No separately prepared stock is asserted; the API main solution is the
    complete medium. A missing water row is not a numeric mass error like the TOGO
    sibling; it is missing preparation/batch context. Represent the source water amount
    without equating it to a measured final volume.
- assessment_id: freshness
  area: provenance
  topic: Generated evidence versus maintained owner
  outcome: concern
  summary: All six owner ingredient evidence objects, bibliographic reference and
    later curation event are absent from the generated target. The reference gate
    examined zero excerpts.
  target_ids:
  - CultureMech:010521
  evidence_ids:
  - record
  - owner-0
  - owner-evidence
  - merge-code
  - validate-references
  details: Full target and both owners were read. These absence findings are bounded
    to exact complete objects; no global missing-artifact claim is made. Current merger
    preservation means the practical action is controlled regeneration after remaining
    owner corrections, not editing the derived YAML or blindly changing current merge
    code. History describes provenance; its old execution is not re-certified.
findings:
- finding_id: f1
  issue_key: culturemech-010521-preparation-context-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Collection preparation and water basis are incomplete
  description: The existing preparation step preserves pH but omits the applicable
    collection default sterilization. Source distilled-water batch context is also
    absent from owner and target.
  target_ids:
  - CultureMech:010521
  field_paths:
  - preparation_steps
  - ingredients
  evidence_ids:
  - record
  - owner-0
  - jcm
  - api
  - bacmedia
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: culturemech-010521-generated-evidence-stale
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated record omits six maintained concentration-evidence entries
  description: The normalized owner has six scoped evidence entries and a source reference
    that are absent from this earlier generated snapshot. The numerical values match
    current provider data, so this is a nonblocking evidence-currentness defect independent
    of unresolved legacy identity.
  target_ids:
  - CultureMech:010521
  field_paths:
  - ingredients[*].evidence
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - owner-evidence
  - merge-code
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Add source-supported default preparation and solvent-batch context
    to the maintained record with evidence; preserve the source pH range and avoid
    inferred incubation or final-volume precision.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010521
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify maintained source details against the complete JCM 35 page, including its
    default header.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on authorized maintained corrections.
  - Regenerate with the maintained merge entrypoint, then run just verify-merges and
    just audit-merge-freshness.
- action_id: a2
  description: Regenerate from the maintained owner after separately authorized curation,
    retaining all claim-level evidence and append-only history. Do not re-add already
    present owner evidence or hand-edit the derived file.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010521
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/1_10_sabourauds_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify maintained source details against the complete JCM 35 page, including its
    default header.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on authorized maintained corrections.
  - Regenerate with the maintained merge entrypoint, then run just verify-merges and
    just audit-merge-freshness.
  - Confirm all six evidence objects and their reference survive generated output
    without changed scope.
limitations:
- Historical identity verification for MediaIngredientMech:000171 is unavailable.
  Current CHEBI identity verification does not establish the meaning of a retired
  MIM numeric identifier.
- Owner evidence was compared as parsed JSON with live API rows; this does not claim
  byte-for-byte whitespace matching or a retrospective certification of the earlier
  source download.
- BacMedia/API explicitly provide normalization volume. No physical final-volume measurement,
  unspecified stock dilution or organism-specific growth inference is made.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-004
- generated-medium
notes:
- Required historical-identifier verification is unavailable, so this valid saved
  bundle must not be read as a completed scientific review. The unverified legacy
  link is recorded as unknown rather than asserted erroneous.
```
