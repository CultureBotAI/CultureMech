# Source and formulation review: alicycliphius_denitrificans_medium (CultureMech:009570)

- Review: 20261021T191725Z-culturemech-009570-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T19:13:55Z
- Finished UTC: 2026-10-21T19:17:25Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact NBRC1619 and TOGO M3056 agree on three dry additions and 1 L water. Both local layers incorrectly encode water as 1 g/L; the other numerals match batch masses but lack an explicit final-volume denominator and attached evidence. No source preparation or organism-specific growth claim is invented.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 345; batch 035 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-four task batches contain 340 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 343 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009570 | data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml | generated | alicycliphius_denitrificans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009570 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009570 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch035/345/strict.tsv |
| validate-terms | passed | True | CultureMech:009570 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009570 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009570 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009570.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009570.

5 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "ingredient_or_context": "Distilled water",
    "field_path": "ingredients[0].concentration",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_amount": 1,
    "source_unit": "L",
    "source_stage": "NBRC1619 single recipe batch",
    "primary_source_evidence_id": "nbrc1619",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "nbrc1619",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1619",
        "source_locator": "Composition table",
        "exact_source_quote": "Distilled water 1 L",
        "snapshot_sha256": "d53ff2b83a2b0e4bfeb519dbd7e62b4fb828b07d04efd30b6908c8dbd2638a56",
        "parsed_text_sha256": "d44ba9b83b170a4a2ad24f0b8b2f30fca8dbafb7299879da212fcf7d794d5b66"
      },
      {
        "source_key": "togoM3056original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3056",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "ca5b9d4e5fc3280b56d4158521a8a0984131d4eefbe8427a444302fe863cb888"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore the literal water input of 1 L. It is not a 1 g/L concentration; no density conversion or measured final volume is assumed."
      },
      {
        "input": "data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Restore the literal water input of 1 L. It is not a 1 g/L concentration; no density conversion or measured final volume is assumed."
      }
    ],
    "arithmetic_and_scope": "Restore the literal water input of 1 L. It is not a 1 g/L concentration; no density conversion or measured final volume is assumed."
  },
  {
    "quantity_id": "q2",
    "ingredient_or_context": "NaCl",
    "field_path": "ingredients[1].concentration",
    "local": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_amount": 5,
    "source_unit": "g",
    "source_stage": "NBRC1619 single recipe batch",
    "primary_source_evidence_id": "nbrc1619",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "nbrc1619",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1619",
        "source_locator": "Composition table",
        "exact_source_quote": "NaCl 5 g",
        "snapshot_sha256": "d53ff2b83a2b0e4bfeb519dbd7e62b4fb828b07d04efd30b6908c8dbd2638a56",
        "parsed_text_sha256": "d44ba9b83b170a4a2ad24f0b8b2f30fca8dbafb7299879da212fcf7d794d5b66"
      },
      {
        "source_key": "togoM3056original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3056",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ca5b9d4e5fc3280b56d4158521a8a0984131d4eefbe8427a444302fe863cb888"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The stored numeral matches the exact dry amount per source batch. The source states 1 L water, not makeup to a final litre, so its G_PER_L denominator is not independently supported. Preserve the batch amount and attach the exact evidence without inventing a final concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The stored numeral matches the exact dry amount per source batch. The source states 1 L water, not makeup to a final litre, so its G_PER_L denominator is not independently supported. Preserve the batch amount and attach the exact evidence without inventing a final concentration."
      }
    ],
    "arithmetic_and_scope": "The stored numeral matches the exact dry amount per source batch. The source states 1 L water, not makeup to a final litre, so its G_PER_L denominator is not independently supported. Preserve the batch amount and attach the exact evidence without inventing a final concentration."
  },
  {
    "quantity_id": "q3",
    "ingredient_or_context": "Beef extract",
    "field_path": "ingredients[2].concentration",
    "local": {
      "value": "3",
      "unit": "G_PER_L"
    },
    "source_amount": 3,
    "source_unit": "g",
    "source_stage": "NBRC1619 single recipe batch",
    "primary_source_evidence_id": "nbrc1619",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "nbrc1619",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1619",
        "source_locator": "Composition table",
        "exact_source_quote": "Beef extract 3 g",
        "snapshot_sha256": "d53ff2b83a2b0e4bfeb519dbd7e62b4fb828b07d04efd30b6908c8dbd2638a56",
        "parsed_text_sha256": "d44ba9b83b170a4a2ad24f0b8b2f30fca8dbafb7299879da212fcf7d794d5b66"
      },
      {
        "source_key": "togoM3056original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3056",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Beef extract\",\n          \"volume\": 3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ca5b9d4e5fc3280b56d4158521a8a0984131d4eefbe8427a444302fe863cb888"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The stored numeral matches the exact dry amount per source batch. The source states 1 L water, not makeup to a final litre, so its G_PER_L denominator is not independently supported. Preserve the batch amount and attach the exact evidence without inventing a final concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The stored numeral matches the exact dry amount per source batch. The source states 1 L water, not makeup to a final litre, so its G_PER_L denominator is not independently supported. Preserve the batch amount and attach the exact evidence without inventing a final concentration."
      }
    ],
    "arithmetic_and_scope": "The stored numeral matches the exact dry amount per source batch. The source states 1 L water, not makeup to a final litre, so its G_PER_L denominator is not independently supported. Preserve the batch amount and attach the exact evidence without inventing a final concentration."
  },
  {
    "quantity_id": "q4",
    "ingredient_or_context": "Bacto peptone",
    "field_path": "ingredients[3].concentration",
    "local": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_amount": 5,
    "source_unit": "g",
    "source_stage": "NBRC1619 single recipe batch",
    "primary_source_evidence_id": "nbrc1619",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "nbrc1619",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1619",
        "source_locator": "Composition table",
        "exact_source_quote": "Bacto peptone 5 g",
        "snapshot_sha256": "d53ff2b83a2b0e4bfeb519dbd7e62b4fb828b07d04efd30b6908c8dbd2638a56",
        "parsed_text_sha256": "d44ba9b83b170a4a2ad24f0b8b2f30fca8dbafb7299879da212fcf7d794d5b66"
      },
      {
        "source_key": "togoM3056original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3056",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"Bacto peptone\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ca5b9d4e5fc3280b56d4158521a8a0984131d4eefbe8427a444302fe863cb888"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The stored numeral matches the exact dry amount per source batch. The source states 1 L water, not makeup to a final litre, so its G_PER_L denominator is not independently supported. Preserve the batch amount and attach the exact evidence without inventing a final concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported",
        "rationale": "The stored numeral matches the exact dry amount per source batch. The source states 1 L water, not makeup to a final litre, so its G_PER_L denominator is not independently supported. Preserve the batch amount and attach the exact evidence without inventing a final concentration."
      }
    ],
    "arithmetic_and_scope": "The stored numeral matches the exact dry amount per source batch. The source states 1 L water, not makeup to a final litre, so its G_PER_L denominator is not independently supported. Preserve the batch amount and attach the exact evidence without inventing a final concentration."
  },
  {
    "quantity_id": "q5",
    "ingredient_or_context": "Unresolved measured final volume",
    "field_path": "preparation_steps",
    "local": null,
    "source_amount": null,
    "source_unit": "not declared",
    "source_stage": "After adding the three dry ingredients",
    "primary_source_evidence_id": "nbrc1619",
    "decision": "unsupported",
    "source_snippets": [
      {
        "source_key": "nbrc1619",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1619",
        "source_locator": "Composition table",
        "exact_source_quote": "Distilled water 1 L",
        "snapshot_sha256": "d53ff2b83a2b0e4bfeb519dbd7e62b4fb828b07d04efd30b6908c8dbd2638a56",
        "parsed_text_sha256": "d44ba9b83b170a4a2ad24f0b8b2f30fca8dbafb7299879da212fcf7d794d5b66"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "unsupported",
        "rationale": "Water input alone does not establish measured final volume; leave the denominator unresolved unless another exact source supplies it."
      },
      {
        "input": "data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "unsupported",
        "rationale": "Water input alone does not establish measured final volume; leave the denominator unresolved unless another exact source supplies it."
      }
    ],
    "arithmetic_and_scope": "No final-volume conversion is performed. Missing pH, sterilization cycle, temperature, gas and vessel parameters are not filled from common practice."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:009570.

2 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 2/4 primary and 2/4 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 4: primary 50.00%; secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009570.

13 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact collection accession and maintained ownership

identity: supported. Targets: CultureMech:009570.

TOGO M3056 explicitly identifies NBRC_M1619 and its exact primary URL. Both titles retain the same source spelling. One maintained bacterial owner and the generated target carry CultureMech:009570 and the same formulation; no namesake substitution is used.

### Batch masses, water and unresolved final volume

consistency: concern. Targets: CultureMech:009570.

All eight local concentration occurrences are covered. Water is a source volume, not mass concentration. The three dry numerals agree with source batch masses but no source makes the final-volume denominator explicit. There are no stock references, nested recipes, alternatives or extra quantitative preparation claims in these records.

### Pure salts versus complex products

grounding: supported. Targets: CultureMech:009570.

Water and sodium chloride have matching nonobsolete canonical labels and exact current MIM preferred rows. Beef extract and Bacto peptone remain ungrounded complex products; the source brand qualifier is retained and no pure-compound identity or supplier composition is invented. The 50% linkage scores describe coverage, not a chemical correctness estimate.

### Conditions absent from both local and inspected source

completeness: unknown. Targets: CultureMech:009570.

Both layers omit preparation, pH, atmosphere, sterilization and incubation conditions. The NBRC Comment fields and TOGO comments array supply no such instructions. This is a source limit rather than evidence for an invented default cycle or a claim that a particular cycle was omitted from the primary.

### Complex liquid medium and taxonomic restraint

scope: supported. Targets: CultureMech:009570.

COMPLEX/UNDEFINED is supported by peptone and beef extract; LIQUID is consistent with the source recipe without a gelling agent. Bacterial filing and the cultivation application are broad context. The source title is not evidence of strain-level growth or a verified taxonomy accession. Neither layer asserts target organisms, organism IDs, DOI/PMID, high_metal or KG match requiring a separate scoped test.

### Amount evidence and historical annotations

evidence: concern. Targets: CultureMech:009570.

Both records lack attached ingredient evidence and a formal reference list. Source URLs in notes establish accession provenance but do not meet the amount-evidence contract. Provider roles/properties are traceable annotations, not independent experiments or grounds for new growth assertions.

### Maintained source and append-only history

provenance: supported. Targets: CultureMech:009570.

The normalized TOGO owner owns future corrections; regenerate the target after reconciliation. All 13 timestamp instances are timezone-aware. Existing ID and MIM migration history is retained as historical provenance; no legacy MIM identifier is currently asserted. The generated layer adds only merge metadata/history to the maintained scientific content.

## Findings

### f1: One litre of water is encoded as 1 g/L

major / open / confirmed; issue key: cm009570-water-volume-as-mass.

Target and owner both represent the exact source water input, 1 L, as a concentration of 1 G_PER_L. Their dry numerals match source batch masses, but no measured final-volume instruction supports converting those masses into final g/L values.

### f2: Source quantities lack claim-linked evidence

minor / open / confirmed; issue key: cm009570-amount-evidence-gap.

The primary URL and source accession are retained in notes, but all eight concentration occurrences lack supporting snippets or scoped explanations. Passing references checked zero excerpts.

## Recommended Actions And Acceptance Checks

### a1

Restore the literal water volume and retain all three source batch masses with their units and scope. Record the unresolved final-volume basis explicitly instead of assuming water input equals final volume. Correct the maintained owner before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Attach exact NBRC1619 and supporting M3056 amount rows to the maintained claims, preserving original units and the final-volume limitation. Do not add unprinted pH, cycle, temperature or organism assertions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch035/345/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch035/345/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml:1:id: CultureMech:009570<br>./data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml:1:id: CultureMech:009570<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch035/source-preflight-bound/345/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 7 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| nbrc1619 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1619; Medium No.1619, complete Composition table and empty Comment fields | supports | Exact primary lists Bacto peptone 5 g, beef extract 3 g, NaCl 5 g and distilled water 1 L. No numerical preparation, final-volume or incubation condition is printed. |
| togoM3056original | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3056; $.meta; $.components[0].items; $.comments | supports | Exact M3056 metadata resolves to NBRC_M1619. All four rows agree with the primary and comments is empty; roles/properties are attributed provider annotations. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch035/345/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml; data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml", "events": 6, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO parsing retains primary sections, reads preparation from explicit comments and recognizes L separately from G_PER_L. Current exact formulation grouping does not certify quantities. This is current writer context, not proof of which historical execution produced the incorrect water unit. |
| writer-1 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO parsing retains primary sections, reads preparation from explicit comments and recognizes L separately from G_PER_L. Current exact formulation grouping does not certify quantities. This is current writer context, not proof of which historical execution produced the incorrect water unit. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- This scientific assessment preceded formal review validation and saving; their actual results are recorded separately.
- Completion means the available exact sources and local claims were assessed, not that the unsupported quantity representation is endorsed. No absent source condition or taxonomy fact was guessed.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T191725Z-culturemech-009570-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alicycliphius_denitrificans_medium (CultureMech:009570)'
started_at: '2026-10-21T19:13:55Z'
finished_at: '2026-10-21T19:17:25Z'
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
summary: Exact NBRC1619 and TOGO M3056 agree on three dry additions and 1 L water.
  Both local layers incorrectly encode water as 1 g/L; the other numerals match batch
  masses but lack an explicit final-volume denominator and attached evidence. No source
  preparation or organism-specific growth claim is invented.
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
  - path: data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml
    sha256: 91e7ac0f871faef2a7a734bfca92ed3a14930c3445e140062774cd0fa3de6df6
    role: target
  - path: data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml
    sha256: 1191bb856995a1c6fe386bff2e092313e0484ee8ab23cb40440ca4173235eaa4
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
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
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
    sha256: 64a778108fd3197a8cc08082f80c1de3ec33eda58350cee5df612ab61d23cea1
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 345; batch 035 item 5 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-four task batches
    contain 340 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 343 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009570
targets:
- target_id: CultureMech:009570
  path: data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml
  label: alicycliphius_denitrificans_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009570
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch035/345/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch035/345/strict.tsv"
  target_ids:
  - CultureMech:009570
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009570
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009570
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
  - CultureMech:009570
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T19:17:24Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T19:17:24Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:28.234877Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch035/345/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:29.441030Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch035/345/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:30.774288Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:31.614061Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T19:17:24Z'
  support: supports
  summary: './data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml:1:id:
    CultureMech:009570

    ./data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml:1:id:
    CultureMech:009570

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch035/source-preflight-bound/345/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T19:17:24Z'
  support: supports
  summary: 7 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: b4a224af7c1998faf8cb2e6e1dab1222556ff25528d861948478d15344c45d5b
- evidence_id: nbrc1619
  kind: database
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1619
  locator: Medium No.1619, complete Composition table and empty Comment fields
  accessed_at: '2026-10-21T18:58:51.729255Z'
  support: supports
  summary: Exact primary lists Bacto peptone 5 g, beef extract 3 g, NaCl 5 g and distilled
    water 1 L. No numerical preparation, final-volume or incubation condition is printed.
  quote: Bacto peptone 5 g Beef extract 3 g NaCl 5 g Distilled water 1 L
  snapshot_sha256: d53ff2b83a2b0e4bfeb519dbd7e62b4fb828b07d04efd30b6908c8dbd2638a56
- evidence_id: togoM3056original
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3056
  locator: $.meta; $.components[0].items; $.comments
  accessed_at: '2026-10-21T18:58:50.839495Z'
  support: supports
  summary: Exact M3056 metadata resolves to NBRC_M1619. All four rows agree with the
    primary and comments is empty; roles/properties are attributed provider annotations.
  quote: '"original_media_id": "NBRC_M1619"'
  snapshot_sha256: ca5b9d4e5fc3280b56d4158521a8a0984131d4eefbe8427a444302fe863cb888
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch035/345/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T19:17:24Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 92150913562d1ce7fa95413e1bfa4986b41c0a6ed07ac8e5b5ef3f51835ad54a
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
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T19:17:24Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/Alicycliphius_denitrificans_Medium.yaml; data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T19:17:24Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:17:24Z'
  support: context_only
  summary: Current TOGO parsing retains primary sections, reads preparation from explicit
    comments and recognizes L separately from G_PER_L. Current exact formulation grouping
    does not certify quantities. This is current writer context, not proof of which
    historical execution produced the incorrect water unit.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:17:24Z'
  support: context_only
  summary: Current TOGO parsing retains primary sections, reads preparation from explicit
    comments and recognizes L separately from G_PER_L. Current exact formulation grouping
    does not certify quantities. This is current writer context, not proof of which
    historical execution produced the incorrect water unit.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009570
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 5 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:009570
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"ingredient_or_context\": \"\
    Distilled water\",\n    \"field_path\": \"ingredients[0].concentration\",\n  \
    \  \"local\": {\n      \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_amount\": 1,\n    \"source_unit\": \"L\",\n    \"source_stage\"\
    : \"NBRC1619 single recipe batch\",\n    \"primary_source_evidence_id\": \"nbrc1619\"\
    ,\n    \"decision\": \"correct\",\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"nbrc1619\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1619\"\
    ,\n        \"source_locator\": \"Composition table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1 L\",\n        \"snapshot_sha256\": \"d53ff2b83a2b0e4bfeb519dbd7e62b4fb828b07d04efd30b6908c8dbd2638a56\"\
    ,\n        \"parsed_text_sha256\": \"d44ba9b83b170a4a2ad24f0b8b2f30fca8dbafb7299879da212fcf7d794d5b66\"\
    \n      },\n      {\n        \"source_key\": \"togoM3056original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3056\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"ca5b9d4e5fc3280b56d4158521a8a0984131d4eefbe8427a444302fe863cb888\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[0].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Restore\
    \ the literal water input of 1 L. It is not a 1 g/L concentration; no density\
    \ conversion or measured final volume is assumed.\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Restore the literal\
    \ water input of 1 L. It is not a 1 g/L concentration; no density conversion or\
    \ measured final volume is assumed.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"Restore the literal water input of 1 L. It is not a 1 g/L concentration; no\
    \ density conversion or measured final volume is assumed.\"\n  },\n  {\n    \"\
    quantity_id\": \"q2\",\n    \"ingredient_or_context\": \"NaCl\",\n    \"field_path\"\
    : \"ingredients[1].concentration\",\n    \"local\": {\n      \"value\": \"5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 5,\n    \"source_unit\"\
    : \"g\",\n    \"source_stage\": \"NBRC1619 single recipe batch\",\n    \"primary_source_evidence_id\"\
    : \"nbrc1619\",\n    \"decision\": \"unsupported\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"nbrc1619\",\n        \"source_url\": \"\
    https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1619\",\n   \
    \     \"source_locator\": \"Composition table\",\n        \"exact_source_quote\"\
    : \"NaCl 5 g\",\n        \"snapshot_sha256\": \"d53ff2b83a2b0e4bfeb519dbd7e62b4fb828b07d04efd30b6908c8dbd2638a56\"\
    ,\n        \"parsed_text_sha256\": \"d44ba9b83b170a4a2ad24f0b8b2f30fca8dbafb7299879da212fcf7d794d5b66\"\
    \n      },\n      {\n        \"source_key\": \"togoM3056original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3056\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 5,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ca5b9d4e5fc3280b56d4158521a8a0984131d4eefbe8427a444302fe863cb888\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[1].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"unsupported\",\n        \"rationale\": \"\
    The stored numeral matches the exact dry amount per source batch. The source states\
    \ 1 L water, not makeup to a final litre, so its G_PER_L denominator is not independently\
    \ supported. Preserve the batch amount and attach the exact evidence without inventing\
    \ a final concentration.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The stored numeral\
    \ matches the exact dry amount per source batch. The source states 1 L water,\
    \ not makeup to a final litre, so its G_PER_L denominator is not independently\
    \ supported. Preserve the batch amount and attach the exact evidence without inventing\
    \ a final concentration.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"\
    The stored numeral matches the exact dry amount per source batch. The source states\
    \ 1 L water, not makeup to a final litre, so its G_PER_L denominator is not independently\
    \ supported. Preserve the batch amount and attach the exact evidence without inventing\
    \ a final concentration.\"\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"ingredient_or_context\"\
    : \"Beef extract\",\n    \"field_path\": \"ingredients[2].concentration\",\n \
    \   \"local\": {\n      \"value\": \"3\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_amount\": 3,\n    \"source_unit\": \"g\",\n    \"source_stage\"\
    : \"NBRC1619 single recipe batch\",\n    \"primary_source_evidence_id\": \"nbrc1619\"\
    ,\n    \"decision\": \"unsupported\",\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"nbrc1619\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1619\"\
    ,\n        \"source_locator\": \"Composition table\",\n        \"exact_source_quote\"\
    : \"Beef extract 3 g\",\n        \"snapshot_sha256\": \"d53ff2b83a2b0e4bfeb519dbd7e62b4fb828b07d04efd30b6908c8dbd2638a56\"\
    ,\n        \"parsed_text_sha256\": \"d44ba9b83b170a4a2ad24f0b8b2f30fca8dbafb7299879da212fcf7d794d5b66\"\
    \n      },\n      {\n        \"source_key\": \"togoM3056original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3056\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Beef extract\\\",\\n          \\\"volume\\\":\
    \ 3,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ca5b9d4e5fc3280b56d4158521a8a0984131d4eefbe8427a444302fe863cb888\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[2].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"unsupported\",\n        \"rationale\": \"\
    The stored numeral matches the exact dry amount per source batch. The source states\
    \ 1 L water, not makeup to a final litre, so its G_PER_L denominator is not independently\
    \ supported. Preserve the batch amount and attach the exact evidence without inventing\
    \ a final concentration.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The stored numeral\
    \ matches the exact dry amount per source batch. The source states 1 L water,\
    \ not makeup to a final litre, so its G_PER_L denominator is not independently\
    \ supported. Preserve the batch amount and attach the exact evidence without inventing\
    \ a final concentration.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"\
    The stored numeral matches the exact dry amount per source batch. The source states\
    \ 1 L water, not makeup to a final litre, so its G_PER_L denominator is not independently\
    \ supported. Preserve the batch amount and attach the exact evidence without inventing\
    \ a final concentration.\"\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"ingredient_or_context\"\
    : \"Bacto peptone\",\n    \"field_path\": \"ingredients[3].concentration\",\n\
    \    \"local\": {\n      \"value\": \"5\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_amount\": 5,\n    \"source_unit\": \"g\",\n    \"source_stage\"\
    : \"NBRC1619 single recipe batch\",\n    \"primary_source_evidence_id\": \"nbrc1619\"\
    ,\n    \"decision\": \"unsupported\",\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"nbrc1619\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1619\"\
    ,\n        \"source_locator\": \"Composition table\",\n        \"exact_source_quote\"\
    : \"Bacto peptone 5 g\",\n        \"snapshot_sha256\": \"d53ff2b83a2b0e4bfeb519dbd7e62b4fb828b07d04efd30b6908c8dbd2638a56\"\
    ,\n        \"parsed_text_sha256\": \"d44ba9b83b170a4a2ad24f0b8b2f30fca8dbafb7299879da212fcf7d794d5b66\"\
    \n      },\n      {\n        \"source_key\": \"togoM3056original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3056\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Bacto peptone\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ca5b9d4e5fc3280b56d4158521a8a0984131d4eefbe8427a444302fe863cb888\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[3].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"unsupported\",\n        \"rationale\": \"\
    The stored numeral matches the exact dry amount per source batch. The source states\
    \ 1 L water, not makeup to a final litre, so its G_PER_L denominator is not independently\
    \ supported. Preserve the batch amount and attach the exact evidence without inventing\
    \ a final concentration.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"The stored numeral\
    \ matches the exact dry amount per source batch. The source states 1 L water,\
    \ not makeup to a final litre, so its G_PER_L denominator is not independently\
    \ supported. Preserve the batch amount and attach the exact evidence without inventing\
    \ a final concentration.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"\
    The stored numeral matches the exact dry amount per source batch. The source states\
    \ 1 L water, not makeup to a final litre, so its G_PER_L denominator is not independently\
    \ supported. Preserve the batch amount and attach the exact evidence without inventing\
    \ a final concentration.\"\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"ingredient_or_context\"\
    : \"Unresolved measured final volume\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"local\": null,\n    \"source_amount\": null,\n    \"source_unit\": \"\
    not declared\",\n    \"source_stage\": \"After adding the three dry ingredients\"\
    ,\n    \"primary_source_evidence_id\": \"nbrc1619\",\n    \"decision\": \"unsupported\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"nbrc1619\",\n\
    \        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1619\"\
    ,\n        \"source_locator\": \"Composition table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1 L\",\n        \"snapshot_sha256\": \"d53ff2b83a2b0e4bfeb519dbd7e62b4fb828b07d04efd30b6908c8dbd2638a56\"\
    ,\n        \"parsed_text_sha256\": \"d44ba9b83b170a4a2ad24f0b8b2f30fca8dbafb7299879da212fcf7d794d5b66\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : null,\n        \"decision\": \"unsupported\",\n        \"rationale\": \"Water\
    \ input alone does not establish measured final volume; leave the denominator\
    \ unresolved unless another exact source supplies it.\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"unsupported\",\n        \"rationale\": \"Water input\
    \ alone does not establish measured final volume; leave the denominator unresolved\
    \ unless another exact source supplies it.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"No final-volume conversion is performed. Missing pH, sterilization cycle,\
    \ temperature, gas and vessel parameters are not filled from common practice.\"\
    \n  }\n]"
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
  - CultureMech:009570
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi26710
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
  - CultureMech:009570
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact collection accession and maintained ownership
  outcome: supported
  summary: TOGO M3056 explicitly identifies NBRC_M1619 and its exact primary URL.
    Both titles retain the same source spelling. One maintained bacterial owner and
    the generated target carry CultureMech:009570 and the same formulation; no namesake
    substitution is used.
  target_ids:
  - CultureMech:009570
  evidence_ids:
  - record
  - nbrc1619
  - togoM3056original
  - owner-0
- assessment_id: source-stage-consistency
  area: consistency
  topic: Batch masses, water and unresolved final volume
  outcome: concern
  summary: All eight local concentration occurrences are covered. Water is a source
    volume, not mass concentration. The three dry numerals agree with source batch
    masses but no source makes the final-volume denominator explicit. There are no
    stock references, nested recipes, alternatives or extra quantitative preparation
    claims in these records.
  target_ids:
  - CultureMech:009570
  evidence_ids:
  - quantity-inventory
  - nbrc1619
  - togoM3056original
  - owner-0
- assessment_id: chemical-forms
  area: grounding
  topic: Pure salts versus complex products
  outcome: supported
  summary: Water and sodium chloride have matching nonobsolete canonical labels and
    exact current MIM preferred rows. Beef extract and Bacto peptone remain ungrounded
    complex products; the source brand qualifier is retained and no pure-compound
    identity or supplier composition is invented. The 50% linkage scores describe
    coverage, not a chemical correctness estimate.
  target_ids:
  - CultureMech:009570
  evidence_ids:
  - record
  - nbrc1619
  - chebi15377
  - chebi26710
  - mim
- assessment_id: preparation
  area: completeness
  topic: Conditions absent from both local and inspected source
  outcome: unknown
  summary: Both layers omit preparation, pH, atmosphere, sterilization and incubation
    conditions. The NBRC Comment fields and TOGO comments array supply no such instructions.
    This is a source limit rather than evidence for an invented default cycle or a
    claim that a particular cycle was omitted from the primary.
  target_ids:
  - CultureMech:009570
  evidence_ids:
  - record
  - nbrc1619
  - togoM3056original
  - owner-0
- assessment_id: classification
  area: scope
  topic: Complex liquid medium and taxonomic restraint
  outcome: supported
  summary: COMPLEX/UNDEFINED is supported by peptone and beef extract; LIQUID is consistent
    with the source recipe without a gelling agent. Bacterial filing and the cultivation
    application are broad context. The source title is not evidence of strain-level
    growth or a verified taxonomy accession. Neither layer asserts target organisms,
    organism IDs, DOI/PMID, high_metal or KG match requiring a separate scoped test.
  target_ids:
  - CultureMech:009570
  evidence_ids:
  - record
  - nbrc1619
  - togoM3056original
- assessment_id: evidence-placement
  area: evidence
  topic: Amount evidence and historical annotations
  outcome: concern
  summary: Both records lack attached ingredient evidence and a formal reference list.
    Source URLs in notes establish accession provenance but do not meet the amount-evidence
    contract. Provider roles/properties are traceable annotations, not independent
    experiments or grounds for new growth assertions.
  target_ids:
  - CultureMech:009570
  evidence_ids:
  - record
  - nbrc1619
  - togoM3056original
  - quantity-inventory
  - owner-0
- assessment_id: ownership
  area: provenance
  topic: Maintained source and append-only history
  outcome: supported
  summary: The normalized TOGO owner owns future corrections; regenerate the target
    after reconciliation. All 13 timestamp instances are timezone-aware. Existing
    ID and MIM migration history is retained as historical provenance; no legacy MIM
    identifier is currently asserted. The generated layer adds only merge metadata/history
    to the maintained scientific content.
  target_ids:
  - CultureMech:009570
  evidence_ids:
  - record
  - history-metadata
  - writer-0
  - writer-1
  - owner-0
findings:
- finding_id: f1
  issue_key: cm009570-water-volume-as-mass
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: One litre of water is encoded as 1 g/L
  description: Target and owner both represent the exact source water input, 1 L,
    as a concentration of 1 G_PER_L. Their dry numerals match source batch masses,
    but no measured final-volume instruction supports converting those masses into
    final g/L values.
  target_ids:
  - CultureMech:009570
  field_paths:
  - ingredients
  evidence_ids:
  - nbrc1619
  - togoM3056original
  - quantity-inventory
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml
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
  issue_key: cm009570-amount-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source quantities lack claim-linked evidence
  description: The primary URL and source accession are retained in notes, but all
    eight concentration occurrences lack supporting snippets or scoped explanations.
    Passing references checked zero excerpts.
  target_ids:
  - CultureMech:009570
  field_paths:
  - ingredients
  - references
  evidence_ids:
  - nbrc1619
  - togoM3056original
  - quantity-inventory
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml
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
  description: Restore the literal water volume and retain all three source batch
    masses with their units and scope. Record the unresolved final-volume basis explicitly
    instead of assuming water input equals final volume. Correct the maintained owner
    before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009570
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml
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
  description: Attach exact NBRC1619 and supporting M3056 amount rows to the maintained
    claims, preserving original units and the final-volume limitation. Do not add
    unprinted pH, cycle, temperature or organism assertions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009570
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alicycliphius_denitrificans_medium.yaml
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
- This scientific assessment preceded formal review validation and saving; their actual
  results are recorded separately.
- Completion means the available exact sources and local claims were assessed, not
  that the unsupported quantity representation is endorsed. No absent source condition
  or taxonomy fact was guessed.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-035
- generated-medium
```
