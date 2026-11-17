# Source and formulation review: antarctic_bacterial_medium (CultureMech:009689)

- Review: 20261021T162345Z-culturemech-009689-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T16:17:55Z
- Finished UTC: 2026-10-21T16:23:45Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Antarctic Bacterial Medium preserves the four ingredient names from TOGO M326 but encodes 1 L water as 1 g/L and omits the provider’s pH 6.9. The three solid amounts remain source-batch masses without an independently established final-volume denominator. Exact JCM331 returns no formulation, so primary confirmation remains unavailable and this review is partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 288; batch 029 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-eight task batches contain 280 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 283 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009689 | data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml | generated | antarctic_bacterial_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009689 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009689 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch029/288/strict.tsv |
| validate-terms | passed | True | CultureMech:009689 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009689 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009689 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: jcm331 | unavailable | True | CultureMech:009689 | The exact JCM331 page returned HTTP200 but says Nothing found and provides no formulation. Required primary content is unavailable; no default sterilization or current collection confirmation can be inferred. |
| Exact source content access: mediadiveJ331api | unavailable | False | CultureMech:009689 | mediadiveJ331api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| Exact source content access: mediadiveJ331retry | unavailable | False | CultureMech:009689 | mediadiveJ331retry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009689.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:009689.

2 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 2/4 primary and 2/4 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 4: primary 50.00%; secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009689.

13 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### TOGO M326 and original JCM331 identity

identity: supported. Targets: CultureMech:009689.

The target and sole maintained owner share CultureMech:009689. The exact provider metadata links M326 to JCM_M331 and its original URL, matching local provenance. The current collection endpoint is empty, so the accession relationship is provider-supported without primary formulation confirmation.

### Source quantities and solvent representation

consistency: concern. Targets: CultureMech:009689.

All four local ingredient names agree with the secondary source and retain the BD-Difco product qualifiers. Water is explicitly1 L in the provider and cannot be represented as1 g/L. Agar15 g, yeast1 g and peptone5 g are source batch quantities; the source lists water1 L without a measured final-volume or make-up declaration. No density or final denominator is invented.

### Explicit secondary-source pH and unavailable primary procedure

completeness: concern. Targets: CultureMech:009689.

The provider says Adjust pH to6.9, but both local layers lack pH and preparation fields. This bounded omission is supported by the available source. The empty JCM page and failed MediaDive requests cannot establish additional sterilization conditions, stock handling or incubation requirements.

### Composition, physical state and biological scope

scope: supported. Targets: CultureMech:009689.

COMPLEX/UNDEFINED is consistent with yeast extract and peptone; SOLID_AGAR agrees with the explicit nonoptional agar row. Bacterial filing, generic cultivation application and title do not establish a named strain, Antarctic growth phenotype or optimum. No organism, DOI, PMID, taxonomy or genome identifier is asserted. The two complex ingredients remain ungrounded rather than being assigned invented pure-chemical identities.

### Current TOGO import and merge behavior

provenance: supported. Targets: CultureMech:009689.

Current TOGO parsing recognizes litre and mass units, separates primary and stock sections and extracts comments as preparation. The maintained historical record nevertheless has the water mass unit and missing pH. Current source code is context, not proof of the exact historical execution. Correct the sole normalized owner before regenerating the target.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009689.

5 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "Distilled water",
    "field_path": "ingredients[0].concentration",
    "decision": "correct",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM326",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M326",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "d3944a1290e40479028a280f761499e8a87bfd2379faecf529269b7f1d0d7fca"
      }
    ],
    "rationale": "Preserve the explicit1 L solvent input in preparation with volume units. The current1 G_PER_L is a mass-concentration representation of a source volume; do not apply an assumed density or infer final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Agar",
    "field_path": "ingredients[1].concentration",
    "decision": "unsupported",
    "local": {
      "value": "15",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM326",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M326",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Agar\",\n          \"volume\": 15,\n          \"unit\": \"g\"",
        "snapshot_sha256": "d3944a1290e40479028a280f761499e8a87bfd2379faecf529269b7f1d0d7fca"
      }
    ],
    "rationale": "The secondary source verifies the listed batch mass, but does not independently establish the final-volume denominator of the stored g/L. Preserve the source amount/product qualifier and unresolved basis; no primary recipe is available to close the gap.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "Yeast extract (BD-Difco)",
    "field_path": "ingredients[2].concentration",
    "decision": "unsupported",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM326",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M326",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "d3944a1290e40479028a280f761499e8a87bfd2379faecf529269b7f1d0d7fca"
      }
    ],
    "rationale": "The secondary source verifies the listed batch mass, but does not independently establish the final-volume denominator of the stored g/L. Preserve the source amount/product qualifier and unresolved basis; no primary recipe is available to close the gap.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "Bacto peptone (BD-Difco)",
    "field_path": "ingredients[3].concentration",
    "decision": "unsupported",
    "local": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM326",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M326",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"Bacto peptone (BD-Difco)\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "d3944a1290e40479028a280f761499e8a87bfd2379faecf529269b7f1d0d7fca"
      }
    ],
    "rationale": "The secondary source verifies the listed batch mass, but does not independently establish the final-volume denominator of the stored g/L. Preserve the source amount/product qualifier and unresolved basis; no primary recipe is available to close the gap.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "Source pH 6.9",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "togoM326",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M326",
        "source_locator": "$.comments[0].comment; also $.meta.ph",
        "exact_source_quote": "\"comment\": \"Adjust pH to 6.9.\"",
        "snapshot_sha256": "d3944a1290e40479028a280f761499e8a87bfd2379faecf529269b7f1d0d7fca"
      }
    ],
    "rationale": "Add the explicit provider pH with exact secondary evidence and its limit. The source gives no titrant identity, dose or sterilization cycle.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  }
]

## Findings

### f1: A solvent volume is represented as a mass concentration

major / open / confirmed; issue key: antarctic-bacterial-water-unit.

Both local layers encode distilled water1 G_PER_L, while the exact provider lists1 L. The other three g/L values correspond numerically to source batch masses but lack an independently established final-volume basis. This is a source-unit and representation defect; primary availability remains a separate limitation.

### f2: Available source pH is omitted

minor / open / confirmed; issue key: antarctic-bacterial-ph-omission.

The provider explicitly says Adjust pH to6.9. Neither target nor owner represents that pH or preparation instruction. No additional procedure is inferred from the inaccessible primary.

## Recommended Actions And Acceptance Checks

### a1

Represent water as a preparation-volume input and preserve the three original source masses with their stated basis. Obtain exact collection confirmation when available; do not invent density or final volume. Correct the maintained owner before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add the provider-supported pH6.9 with a narrow exact excerpt and clearly labeled secondary provenance, while retaining the required primary-access limitation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch029/288/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch029/288/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml:1:id: CultureMech:009689<br>./data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml:1:id: CultureMech:009689<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch029/source-preflight-bound/288/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 7 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch029/source-preflight-bound/288/evidence-context-original.json; Complete frozen source context rebound to every fresh native input | context_only | All context input hashes match the fresh native inspection. The preflight remains historical preparation; this assessment uses the current bound record catalog and native input hashes. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-3 | src/culturemech/import/togo_importer.py; _ingredient_from_item lines 273–339; _assembled_solution_sections lines 341–411; _extract_assembled_solutions lines 413–461; _is_primary_section lines 464–466; _looks_like_solution_item lines 469–478; _local_batch_volume_ml lines 480–507; _local_solution_composition lines 509–531; _solution_from_item lines 533–585; _extract_primary_components lines 587–641; _extract_preparation_steps lines 644–668; _parse_unit lines 713–746 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| togoM326 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M326; $.meta, $.components[0].items[0:4] and $.comments[0] | supports | The full exact TOGO payload was read. It identifies JCM_M331 and lists water1 L, agar15 g, BD-Difco yeast extract1 g and Bacto peptone5 g, with pH6.9. This is secondary provider support, not a recovered primary recipe. |
| jcm331-attempt | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=331; Preserved exact public retrieval result | context_only | The exact JCM331 page returned HTTP200 but says Nothing found and provides no formulation. Required primary content is unavailable; no default sterilization or current collection confirmation can be inferred. |
| mediadiveJ331api-attempt | https://mediadive.dsmz.de/rest/medium/J331; Preserved exact public retrieval result | context_only | mediadiveJ331api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| mediadiveJ331retry-attempt | https://mediadive.dsmz.de/rest/medium/J331; Preserved exact public retrieval result | context_only | mediadiveJ331retry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml", "events": 6, "timestamp_issues": []}] |
| quantity-inventory | /private/tmp/culturemech-review-work-batch029/288/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| quantity-local-fields | /private/tmp/culturemech-review-work-batch029/288/quantity-local-field-audit.json; All quantity layer paths and exact stored values against full inspected YAML | context_only | Every local concentration is covered; every layer locator resolves to its exact stored value or explicitly absent intended container. Source locators remain in source_snippets. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact JCM331 page returned HTTP200 but says Nothing found and provides no formulation. Required primary content is unavailable; no default sterilization or current collection confirmation can be inferred.
- mediadiveJ331api: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- mediadiveJ331retry: exact public request returned HTTP 503; original access time, response bytes and any separately recorded retry are retained. Error bytes do not establish formulation or historical absence.
- JCM331 required primary content is unavailable despite HTTP200. Both separate MediaDiveJ331 attempts returned503; their error bodies do not support formulation or prove a historical recipe absent. The TOGO page shell adds no recipe evidence beyond the separately captured JSON.
- No later stock, generic autoclave cycle, organism growth or incubation requirement is supplied by the available exact source. Final-volume uncertainty remains explicit.
- This scientific assessment preceded formal review validation and saving; their results are recorded separately.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T162345Z-culturemech-009689-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: antarctic_bacterial_medium (CultureMech:009689)'
started_at: '2026-10-21T16:17:55Z'
finished_at: '2026-10-21T16:23:45Z'
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
summary: Antarctic Bacterial Medium preserves the four ingredient names from TOGO
  M326 but encodes 1 L water as 1 g/L and omits the provider’s pH 6.9. The three solid
  amounts remain source-batch masses without an independently established final-volume
  denominator. Exact JCM331 returns no formulation, so primary confirmation remains
  unavailable and this review is partial.
source:
  git_revision: 033ef56966c19f8948d84a579b3f280e3e94e9e3
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
  - path: data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml
    sha256: 7f4873f29a2e49211a56f01e2d5ac25a902b5fd754cc8ce5a8ef4fc57db3e7b8
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml
    sha256: caa1b98b5caed680dc783e127fcdb61cd71b3fc2c890735b587283952a049f84
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
    sha256: 60a2ad5d759b91ea153f23d8b3ae4bc7ead87f38accac1219fe4806fd5272ab0
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/fetch_medium_concentration_sources.py
    sha256: 746c2828863e6ee409d88409a540ea0a8d01ffad3e38be4a4a47f47bec5bbeb5
    role: context
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
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
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
    role: context
  - path: src/culturemech/fetch/togo_fetcher.py
    sha256: 7aac40fe1d47e30810ae0be02f6e369ddb9bf657d630072595c62f46fb0bf339
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
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
    sha256: 64a778108fd3197a8cc08082f80c1de3ec33eda58350cee5df612ab61d23cea1
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 288; batch 029 item 8 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-eight task batches
    contain 280 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 283 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009689
targets:
- target_id: CultureMech:009689
  path: data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml
  label: antarctic_bacterial_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009689
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch029/288/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch029/288/strict.tsv"
  target_ids:
  - CultureMech:009689
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009689
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009689
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
  - CultureMech:009689
- check_id: jcm331-source-access
  name: 'Exact source content access: jcm331'
  required: true
  status: unavailable
  summary: The exact JCM331 page returned HTTP200 but says Nothing found and provides
    no formulation. Required primary content is unavailable; no default sterilization
    or current collection confirmation can be inferred.
  target_ids:
  - CultureMech:009689
  evidence_ids:
  - jcm331-attempt
- check_id: mediadiveJ331api-source-access
  name: 'Exact source content access: mediadiveJ331api'
  required: false
  status: unavailable
  summary: 'mediadiveJ331api: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:009689
  evidence_ids:
  - mediadiveJ331api-attempt
- check_id: mediadiveJ331retry-source-access
  name: 'Exact source content access: mediadiveJ331retry'
  required: false
  status: unavailable
  summary: 'mediadiveJ331retry: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  target_ids:
  - CultureMech:009689
  evidence_ids:
  - mediadiveJ331retry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T16:23:43Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T16:23:43Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:34.311179Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch029/288/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:35.736609Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch029/288/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:37.236411Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:38.087658Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T16:23:43Z'
  support: supports
  summary: './data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml:1:id: CultureMech:009689

    ./data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml:1:id:
    CultureMech:009689

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/source-preflight-bound/288/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T16:23:43Z'
  support: supports
  summary: 7 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: b0b6246ad444a15ce53cfe7823c0aa29a84803601f6db13e9d0b28145fef9a46
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/source-preflight-bound/288/evidence-context-original.json
  locator: Complete frozen source context rebound to every fresh native input
  accessed_at: '2026-10-21T16:23:43Z'
  support: context_only
  summary: All context input hashes match the fresh native inspection. The preflight
    remains historical preparation; this assessment uses the current bound record
    catalog and native input hashes.
  snapshot_sha256: 21ed0641e7c9c0ef03c950a1af814256a26e3bed14fe51951a0bd8dc65b6751f
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T16:23:43Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-context-1
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570;
    _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps
    lines 653–721
  accessed_at: '2026-10-21T16:23:43Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T16:23:43Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-context-3
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item lines 273–339; _assembled_solution_sections lines
    341–411; _extract_assembled_solutions lines 413–461; _is_primary_section lines
    464–466; _looks_like_solution_item lines 469–478; _local_batch_volume_ml lines
    480–507; _local_solution_composition lines 509–531; _solution_from_item lines
    533–585; _extract_primary_components lines 587–641; _extract_preparation_steps
    lines 644–668; _parse_unit lines 713–746
  accessed_at: '2026-10-21T16:23:43Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: togoM326
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M326
  locator: $.meta, $.components[0].items[0:4] and $.comments[0]
  accessed_at: '2026-10-21T16:01:40.096218Z'
  support: supports
  summary: The full exact TOGO payload was read. It identifies JCM_M331 and lists
    water1 L, agar15 g, BD-Difco yeast extract1 g and Bacto peptone5 g, with pH6.9.
    This is secondary provider support, not a recovered primary recipe.
  snapshot_sha256: d3944a1290e40479028a280f761499e8a87bfd2379faecf529269b7f1d0d7fca
- evidence_id: jcm331-attempt
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=331
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:01:41.376232Z'
  support: context_only
  summary: The exact JCM331 page returned HTTP200 but says Nothing found and provides
    no formulation. Required primary content is unavailable; no default sterilization
    or current collection confirmation can be inferred.
  snapshot_sha256: e6b9130bccd3c0da8e695c943f249cd1ccf7b284b02f4b57f7f34a49390e0aa4
- evidence_id: mediadiveJ331api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J331
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:01:39.566102Z'
  support: context_only
  summary: 'mediadiveJ331api: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ331retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J331
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:03:01.045585Z'
  support: context_only
  summary: 'mediadiveJ331retry: exact public request returned HTTP 503; original access
    time, response bytes and any separately recorded retry are retained. Error bytes
    do not establish formulation or historical absence.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: CHEBI:15377 resolves to water. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: CHEBI:2509 resolves to agar. Identifier existence and label metadata do
    not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T16:23:43Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type":
    "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id":
    "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T16:23:43Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/288/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T16:23:43Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 6ffa8694143ce70fa1d22bf285692d9466b9053afbf149a3e0dd71d34545e435
- evidence_id: quantity-local-fields
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/288/quantity-local-field-audit.json
  locator: All quantity layer paths and exact stored values against full inspected
    YAML
  accessed_at: '2026-10-21T16:23:43Z'
  support: context_only
  summary: Every local concentration is covered; every layer locator resolves to its
    exact stored value or explicitly absent intended container. Source locators remain
    in source_snippets.
  snapshot_sha256: 21b96a6a8e1060632867d0d2a632074037b678be05c5bd41e9f6597f8d5e481f
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009689
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '2 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 2/4 primary
    and 2/4 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:009689
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi2509
  details: 'Instance coverage on a 0–100 percent scale, denominator 4: primary 50.00%;
    secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 13 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:009689
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: TOGO M326 and original JCM331 identity
  outcome: supported
  summary: The target and sole maintained owner share CultureMech:009689. The exact
    provider metadata links M326 to JCM_M331 and its original URL, matching local
    provenance. The current collection endpoint is empty, so the accession relationship
    is provider-supported without primary formulation confirmation.
  target_ids:
  - CultureMech:009689
  evidence_ids:
  - record
  - owner-0
  - id-search
  - togoM326
  - jcm331-attempt
- assessment_id: formulation
  area: consistency
  topic: Source quantities and solvent representation
  outcome: concern
  summary: All four local ingredient names agree with the secondary source and retain
    the BD-Difco product qualifiers. Water is explicitly1 L in the provider and cannot
    be represented as1 g/L. Agar15 g, yeast1 g and peptone5 g are source batch quantities;
    the source lists water1 L without a measured final-volume or make-up declaration.
    No density or final denominator is invented.
  target_ids:
  - CultureMech:009689
  evidence_ids:
  - record
  - owner-0
  - togoM326
- assessment_id: preparation
  area: completeness
  topic: Explicit secondary-source pH and unavailable primary procedure
  outcome: concern
  summary: The provider says Adjust pH to6.9, but both local layers lack pH and preparation
    fields. This bounded omission is supported by the available source. The empty
    JCM page and failed MediaDive requests cannot establish additional sterilization
    conditions, stock handling or incubation requirements.
  target_ids:
  - CultureMech:009689
  evidence_ids:
  - record
  - owner-0
  - togoM326
  - jcm331-attempt
- assessment_id: classification
  area: scope
  topic: Composition, physical state and biological scope
  outcome: supported
  summary: COMPLEX/UNDEFINED is consistent with yeast extract and peptone; SOLID_AGAR
    agrees with the explicit nonoptional agar row. Bacterial filing, generic cultivation
    application and title do not establish a named strain, Antarctic growth phenotype
    or optimum. No organism, DOI, PMID, taxonomy or genome identifier is asserted.
    The two complex ingredients remain ungrounded rather than being assigned invented
    pure-chemical identities.
  target_ids:
  - CultureMech:009689
  evidence_ids:
  - record
  - togoM326
- assessment_id: writer-context
  area: provenance
  topic: Current TOGO import and merge behavior
  outcome: supported
  summary: Current TOGO parsing recognizes litre and mass units, separates primary
    and stock sections and extracts comments as preparation. The maintained historical
    record nevertheless has the water mass unit and missing pH. Current source code
    is context, not proof of the exact historical execution. Correct the sole normalized
    owner before regenerating the target.
  target_ids:
  - CultureMech:009689
  evidence_ids:
  - record
  - owner-0
  - writer-context-0
  - writer-context-1
  - writer-context-2
  - writer-context-3
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 5 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:009689
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"Distilled water\",\n    \"field_path\"\
    : \"ingredients[0].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : {\n      \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM326\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M326\",\n     \
    \   \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"d3944a1290e40479028a280f761499e8a87bfd2379faecf529269b7f1d0d7fca\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the explicit1 L solvent input\
    \ in preparation with volume units. The current1 G_PER_L is a mass-concentration\
    \ representation of a source volume; do not apply an assumed density or infer\
    \ final volume.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Agar\",\n    \"field_path\": \"ingredients[1].concentration\",\n    \"decision\"\
    : \"unsupported\",\n    \"local\": {\n      \"value\": \"15\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM326\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M326\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Agar\\\",\\n          \\\"volume\\\": 15,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"d3944a1290e40479028a280f761499e8a87bfd2379faecf529269b7f1d0d7fca\"\
    \n      }\n    ],\n    \"rationale\": \"The secondary source verifies the listed\
    \ batch mass, but does not independently establish the final-volume denominator\
    \ of the stored g/L. Preserve the source amount/product qualifier and unresolved\
    \ basis; no primary recipe is available to close the gap.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"15\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"unsupported\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Yeast extract (BD-Difco)\",\n    \"field_path\": \"ingredients[2].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"1\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM326\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M326\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract (BD-Difco)\\\",\\n          \\\"\
    volume\\\": 1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"d3944a1290e40479028a280f761499e8a87bfd2379faecf529269b7f1d0d7fca\"\n     \
    \ }\n    ],\n    \"rationale\": \"The secondary source verifies the listed batch\
    \ mass, but does not independently establish the final-volume denominator of the\
    \ stored g/L. Preserve the source amount/product qualifier and unresolved basis;\
    \ no primary recipe is available to close the gap.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"unsupported\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Bacto peptone (BD-Difco)\",\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM326\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M326\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Bacto peptone (BD-Difco)\\\",\\n          \\\"\
    volume\\\": 5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"d3944a1290e40479028a280f761499e8a87bfd2379faecf529269b7f1d0d7fca\"\n     \
    \ }\n    ],\n    \"rationale\": \"The secondary source verifies the listed batch\
    \ mass, but does not independently establish the final-volume denominator of the\
    \ stored g/L. Preserve the source amount/product qualifier and unresolved basis;\
    \ no primary recipe is available to close the gap.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"unsupported\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Source pH 6.9\",\n    \"field_path\": \"preparation_steps\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"togoM326\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M326\"\
    ,\n        \"source_locator\": \"$.comments[0].comment; also $.meta.ph\",\n  \
    \      \"exact_source_quote\": \"\\\"comment\\\": \\\"Adjust pH to 6.9.\\\"\"\
    ,\n        \"snapshot_sha256\": \"d3944a1290e40479028a280f761499e8a87bfd2379faecf529269b7f1d0d7fca\"\
    \n      }\n    ],\n    \"rationale\": \"Add the explicit provider pH with exact\
    \ secondary evidence and its limit. The source gives no titrant identity, dose\
    \ or sterilization cycle.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n      \
    \  \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  }\n]"
findings:
- finding_id: f1
  issue_key: antarctic-bacterial-water-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: A solvent volume is represented as a mass concentration
  description: Both local layers encode distilled water1 G_PER_L, while the exact
    provider lists1 L. The other three g/L values correspond numerically to source
    batch masses but lack an independently established final-volume basis. This is
    a source-unit and representation defect; primary availability remains a separate
    limitation.
  target_ids:
  - CultureMech:009689
  field_paths:
  - ingredients[0].concentration
  - ingredients[1].concentration
  - ingredients[2].concentration
  - ingredients[3].concentration
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - togoM326
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: antarctic-bacterial-ph-omission
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Available source pH is omitted
  description: The provider explicitly says Adjust pH to6.9. Neither target nor owner
    represents that pH or preparation instruction. No additional procedure is inferred
    from the inaccessible primary.
  target_ids:
  - CultureMech:009689
  field_paths:
  - ph_value
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - togoM326
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3.4
  normalization_reason: P3.4 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Represent water as a preparation-volume input and preserve the three
    original source masses with their stated basis. Obtain exact collection confirmation
    when available; do not invent density or final volume. Correct the maintained
    owner before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009689
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml
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
  description: Add the provider-supported pH6.9 with a narrow exact excerpt and clearly
    labeled secondary provenance, while retaining the required primary-access limitation.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009689
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml
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
- The exact JCM331 page returned HTTP200 but says Nothing found and provides no formulation.
  Required primary content is unavailable; no default sterilization or current collection
  confirmation can be inferred.
- 'mediadiveJ331api: exact public request returned HTTP 503; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- 'mediadiveJ331retry: exact public request returned HTTP 503; original access time,
  response bytes and any separately recorded retry are retained. Error bytes do not
  establish formulation or historical absence.'
- JCM331 required primary content is unavailable despite HTTP200. Both separate MediaDiveJ331
  attempts returned503; their error bodies do not support formulation or prove a historical
  recipe absent. The TOGO page shell adds no recipe evidence beyond the separately
  captured JSON.
- No later stock, generic autoclave cycle, organism growth or incubation requirement
  is supplied by the available exact source. Final-volume uncertainty remains explicit.
- This scientific assessment preceded formal review validation and saving; their results
  are recorded separately.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-029
- generated-medium
```
