# Source and formulation review: archaeoglobus_medium (CultureMech:005188)

- Review: 20261021T165630Z-culturemech-005188-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T16:49:42Z
- Finished UTC: 2026-10-21T16:56:30Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact KOMODO 399 catalogue metadata links to DSMZ 399, whose complete primary defines a main medium and Modified Wolin mineral stock. All three local layers flatten stock strengths and sum full-stock magnesium, calcium and sodium with main contributions. Their normalized main numbers have no authenticated current provider denominator or primary-declared final volume. The DSMZ owner retains preparation that the target and KOMODO owner omit. Nickel hydrate and resazurin salt mismatches, broken category-specific relation paths and unattached source evidence require curation; current source access is sufficient for this bounded formulation review.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 298; batch 030 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-nine task batches contain 290 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 293 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:005188 | data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml | generated | archaeoglobus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:005188 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:005188 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-030/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch030/298/strict.tsv |
| validate-terms | passed | True | CultureMech:005188 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:005188 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:005188 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive399api | unavailable | False | CultureMech:005188 | Optional mediadive399api request returned 503. Current base formulation can be assessed from the exact catalogue link and primary sources; historical byte equivalence and a distinct KOMODO variant are not inferred. |
| Exact source content access: komodo399detail | unavailable | False | CultureMech:005188 | Optional komodo399detail request returned 403. Current base formulation can be assessed from the exact catalogue link and primary sources; historical byte equivalence and a distinct KOMODO variant are not inferred. |
| Exact source content access: komodo399actual | unavailable | False | CultureMech:005188 | Optional komodo399actual request returned 403. Current base formulation can be assessed from the exact catalogue link and primary sources; historical byte equivalence and a distinct KOMODO variant are not inferred. |
| Exact source content access: mediadive399retry | unavailable | False | CultureMech:005188 | Optional mediadive399retry request returned 503. Current base formulation can be assessed from the exact catalogue link and primary sources; historical byte equivalence and a distinct KOMODO variant are not inferred. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:005188.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary chemical identifiers

grounding: concern. Targets: CultureMech:005188.

24 distinct primary/current-secondary IDs have matching nonobsolete labels. Target direct-ingredient linkage is 24/25 primary (96.00%) and 23/25 current CHEBI-based secondary (92.00%), on a 0–100 linkage scale, not an accuracy score. Current secondary keys without pinned index rows: []. Legacy slot count 0 is separate and does not enter that current-key claim. Supplied-form correspondence is assessed separately.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:005188.

26 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Explicit catalogue linkage and maintained contributors

identity: supported. Targets: CultureMech:005188.

KOMODO399 links directly to DSMZ399; both maintained source contributors resolve to exact stable IDs and actual archaea paths. Historical KOMODO detail bytes and current API are unavailable, but no distinct historical variant or byte equivalence is inferred. Exact current primary formulation is assessed directly.

### Mixture state and organism boundaries

scope: supported. Targets: CultureMech:005188.

Liquid and complex with SEMI_DEFINED composition is compatible with specified salts plus undefined yeast extract, without agar. Catalogue no-aerobic metadata aligns with the primary anoxic procedure but does not independently prove physiology. No organism-specific growth, optimum, taxonomy, DOI or PMID is asserted by this review.

### Source hydrate and salt correspondence

grounding: concern. Targets: CultureMech:005188.

Nickel chloride hexahydrate is linked to anhydrous CHEBI:34887; sodium resazurin is linked to neutral CHEBI:8806. Printed ferrous ammonium sulfate heptahydrate agrees with CHEBI:131378, and explicit sodium L-lactate agrees with its L-specific term. Other named hydrates were compared with captured structures; current MIM matches cannot substitute for source-form evidence.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:005188.

60 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "label": "KCl",
    "decision": "correct",
    "source_stage": "Main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.335968",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.335968",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.335968",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main table: exact named row",
        "exact_source_quote": "KCl 0.34 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the original main amount/unit and its source batch context. The primary lists 1000 ml water plus stock additions, without an explicit final-volume denominator; do not authenticate the existing G_PER_L basis by reverse-engineering its number."
  },
  {
    "decision_id": "q2",
    "label": "MgCl2 x 6 H2O",
    "decision": "correct",
    "source_stage": "Main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3.95257",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3.95257",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3.95257",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main table: exact named row",
        "exact_source_quote": "MgCl2 x 6 H2O 4.00 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the original main amount/unit and its source batch context. The primary lists 1000 ml water plus stock additions, without an explicit final-volume denominator; do not authenticate the existing G_PER_L basis by reverse-engineering its number."
  },
  {
    "decision_id": "q3",
    "label": "MgSO4 x 7 H2O",
    "decision": "correct",
    "source_stage": "Main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "6.40909",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "6.40909",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "6.40909",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main table: exact named row",
        "exact_source_quote": "MgSO4 x 7 H2O 3.45 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the original main amount/unit and its source batch context. The primary lists 1000 ml water plus stock additions, without an explicit final-volume denominator; do not authenticate the existing G_PER_L basis by reverse-engineering its number. This local value also sums a main contribution with an undiluted full-stock concentration; separate both stages."
  },
  {
    "decision_id": "q4",
    "label": "NH4Cl",
    "decision": "correct",
    "source_stage": "Main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.247036",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.247036",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.247036",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main table: exact named row",
        "exact_source_quote": "NH4Cl 0.25 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the original main amount/unit and its source batch context. The primary lists 1000 ml water plus stock additions, without an explicit final-volume denominator; do not authenticate the existing G_PER_L basis by reverse-engineering its number."
  },
  {
    "decision_id": "q5",
    "label": "CaCl2 x 2 H2O",
    "decision": "correct",
    "source_stage": "Main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.23834",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.23834",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.23834",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main table: exact named row",
        "exact_source_quote": "CaCl2 x 2 H2O 0.14 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the original main amount/unit and its source batch context. The primary lists 1000 ml water plus stock additions, without an explicit final-volume denominator; do not authenticate the existing G_PER_L basis by reverse-engineering its number. This local value also sums a main contribution with an undiluted full-stock concentration; separate both stages."
  },
  {
    "decision_id": "q6",
    "label": "K2HPO4",
    "decision": "correct",
    "source_stage": "Main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.13834",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.13834",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.13834",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main table: exact named row",
        "exact_source_quote": "K2HPO4 0.14 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the original main amount/unit and its source batch context. The primary lists 1000 ml water plus stock additions, without an explicit final-volume denominator; do not authenticate the existing G_PER_L basis by reverse-engineering its number."
  },
  {
    "decision_id": "q7",
    "label": "NaCl",
    "decision": "correct",
    "source_stage": "Main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "18.7866",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "18.7866",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "18.7866",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main table: exact named row",
        "exact_source_quote": "NaCl 18.00 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the original main amount/unit and its source batch context. The primary lists 1000 ml water plus stock additions, without an explicit final-volume denominator; do not authenticate the existing G_PER_L basis by reverse-engineering its number. This local value also sums a main contribution with an undiluted full-stock concentration; separate both stages."
  },
  {
    "decision_id": "q8",
    "label": "Yeast extract",
    "decision": "correct",
    "source_stage": "Main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.494071",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.494071",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.494071",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main table: exact named row",
        "exact_source_quote": "Yeast extract (OXOID) 0.50 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the original main amount/unit and its source batch context. The primary lists 1000 ml water plus stock additions, without an explicit final-volume denominator; do not authenticate the existing G_PER_L basis by reverse-engineering its number."
  },
  {
    "decision_id": "q9",
    "label": "Na-L-lactate",
    "decision": "correct",
    "source_stage": "Main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.48221",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.48221",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.48221",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main table: exact named row",
        "exact_source_quote": "Na-L-lactate 1.50 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the original main amount/unit and its source batch context. The primary lists 1000 ml water plus stock additions, without an explicit final-volume denominator; do not authenticate the existing G_PER_L basis by reverse-engineering its number."
  },
  {
    "decision_id": "q10",
    "label": "Fe(NH4)2(SO4)2 x 7 H2O",
    "decision": "correct",
    "source_stage": "Main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.00197628",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.00197628",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.00197628",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main table: exact named row",
        "exact_source_quote": "Fe(NH4)2(SO4)2 x 7 H2O (0.1% w/v) 2.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the original main amount/unit and its source batch context. The primary lists 1000 ml water plus stock additions, without an explicit final-volume denominator; do not authenticate the existing G_PER_L basis by reverse-engineering its number. Preserve the explicit 0.1% w/v stock strength and its separate volume dose. That supports a delivered mass calculation but not the existing final concentration without a final-volume basis."
  },
  {
    "decision_id": "q11",
    "label": "Sodium resazurin",
    "decision": "correct",
    "source_stage": "Main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.000494071",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.000494071",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.000494071",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main table: exact named row",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the original main amount/unit and its source batch context. The primary lists 1000 ml water plus stock additions, without an explicit final-volume denominator; do not authenticate the existing G_PER_L basis by reverse-engineering its number. Preserve the explicit 0.1% w/v stock strength and its separate volume dose. That supports a delivered mass calculation but not the existing final concentration without a final-volume basis."
  },
  {
    "decision_id": "q12",
    "label": "NaHCO3",
    "decision": "correct",
    "source_stage": "Main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.96443",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.96443",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.96443",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main table: exact named row",
        "exact_source_quote": "NaHCO3 3.00 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the original main amount/unit and its source batch context. The primary lists 1000 ml water plus stock additions, without an explicit final-volume denominator; do not authenticate the existing G_PER_L basis by reverse-engineering its number."
  },
  {
    "decision_id": "q13",
    "label": "Na2S x 9 H2O",
    "decision": "correct",
    "source_stage": "Main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.494071",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.494071",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.494071",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main table: exact named row",
        "exact_source_quote": "Na2S x 9 H2O 0.50 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the original main amount/unit and its source batch context. The primary lists 1000 ml water plus stock additions, without an explicit final-volume denominator; do not authenticate the existing G_PER_L basis by reverse-engineering its number."
  },
  {
    "decision_id": "q14",
    "label": "Nitrilotriacetic acid stock amount",
    "decision": "correct",
    "source_stage": "Modified Wolin mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Pages1–2 Modified Wolin mineral subsection: exact row",
        "exact_source_quote": "Nitrilotriacetic acid 1.50 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin stock water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "This original amount is in a separately prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate and water basis; only the 10 ml main dose transfers. Do not sum the full stock with main contributions."
  },
  {
    "decision_id": "q15",
    "label": "MgSO4 x 7 H2O stock amount",
    "decision": "correct",
    "source_stage": "Modified Wolin mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "6.40909",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "6.40909",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "6.40909",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Pages1–2 Modified Wolin mineral subsection: exact row",
        "exact_source_quote": "MgSO4 x 7 H2O 3.00 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin stock water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "This original amount is in a separately prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate and water basis; only the 10 ml main dose transfers. Do not sum the full stock with main contributions."
  },
  {
    "decision_id": "q16",
    "label": "MnSO4 x H2O stock amount",
    "decision": "correct",
    "source_stage": "Modified Wolin mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Pages1–2 Modified Wolin mineral subsection: exact row",
        "exact_source_quote": "MnSO4 x H2O 0.50 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin stock water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "This original amount is in a separately prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate and water basis; only the 10 ml main dose transfers. Do not sum the full stock with main contributions."
  },
  {
    "decision_id": "q17",
    "label": "NaCl stock amount",
    "decision": "correct",
    "source_stage": "Modified Wolin mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "18.7866",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "18.7866",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "18.7866",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Pages1–2 Modified Wolin mineral subsection: exact row",
        "exact_source_quote": "NaCl 1.00 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin stock water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "This original amount is in a separately prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate and water basis; only the 10 ml main dose transfers. Do not sum the full stock with main contributions."
  },
  {
    "decision_id": "q18",
    "label": "FeSO4 x 7 H2O stock amount",
    "decision": "correct",
    "source_stage": "Modified Wolin mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Pages1–2 Modified Wolin mineral subsection: exact row",
        "exact_source_quote": "FeSO4 x 7 H2O 0.10 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin stock water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "This original amount is in a separately prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate and water basis; only the 10 ml main dose transfers. Do not sum the full stock with main contributions."
  },
  {
    "decision_id": "q19",
    "label": "CoSO4 x 7 H2O stock amount",
    "decision": "correct",
    "source_stage": "Modified Wolin mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Pages1–2 Modified Wolin mineral subsection: exact row",
        "exact_source_quote": "CoSO4 x 7 H2O 0.18 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin stock water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "This original amount is in a separately prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate and water basis; only the 10 ml main dose transfers. Do not sum the full stock with main contributions."
  },
  {
    "decision_id": "q20",
    "label": "CaCl2 x 2 H2O stock amount",
    "decision": "correct",
    "source_stage": "Modified Wolin mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.23834",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.23834",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.23834",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Pages1–2 Modified Wolin mineral subsection: exact row",
        "exact_source_quote": "CaCl2 x 2 H2O 0.10 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin stock water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "This original amount is in a separately prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate and water basis; only the 10 ml main dose transfers. Do not sum the full stock with main contributions."
  },
  {
    "decision_id": "q21",
    "label": "ZnSO4 x 7 H2O stock amount",
    "decision": "correct",
    "source_stage": "Modified Wolin mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Pages1–2 Modified Wolin mineral subsection: exact row",
        "exact_source_quote": "ZnSO4 x 7 H2O 0.18 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin stock water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "This original amount is in a separately prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate and water basis; only the 10 ml main dose transfers. Do not sum the full stock with main contributions."
  },
  {
    "decision_id": "q22",
    "label": "CuSO4 x 5 H2O stock amount",
    "decision": "correct",
    "source_stage": "Modified Wolin mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Pages1–2 Modified Wolin mineral subsection: exact row",
        "exact_source_quote": "CuSO4 x 5 H2O 0.01 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin stock water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "This original amount is in a separately prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate and water basis; only the 10 ml main dose transfers. Do not sum the full stock with main contributions."
  },
  {
    "decision_id": "q23",
    "label": "AlK(SO4)2 x 12 H2O stock amount",
    "decision": "correct",
    "source_stage": "Modified Wolin mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Pages1–2 Modified Wolin mineral subsection: exact row",
        "exact_source_quote": "AlK(SO4)2 x 12 H2O 0.02 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin stock water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "This original amount is in a separately prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate and water basis; only the 10 ml main dose transfers. Do not sum the full stock with main contributions."
  },
  {
    "decision_id": "q24",
    "label": "H3BO3 stock amount",
    "decision": "correct",
    "source_stage": "Modified Wolin mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Pages1–2 Modified Wolin mineral subsection: exact row",
        "exact_source_quote": "H3BO3 0.01 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin stock water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "This original amount is in a separately prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate and water basis; only the 10 ml main dose transfers. Do not sum the full stock with main contributions."
  },
  {
    "decision_id": "q25",
    "label": "Na2MoO4 x 2 H2O stock amount",
    "decision": "correct",
    "source_stage": "Modified Wolin mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Pages1–2 Modified Wolin mineral subsection: exact row",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.01 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin stock water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "This original amount is in a separately prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate and water basis; only the 10 ml main dose transfers. Do not sum the full stock with main contributions."
  },
  {
    "decision_id": "q26",
    "label": "NiCl2 x 6 H2O stock amount",
    "decision": "correct",
    "source_stage": "Modified Wolin mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Pages1–2 Modified Wolin mineral subsection: exact row",
        "exact_source_quote": "NiCl2 x 6 H2O 0.03 g",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin stock water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "This original amount is in a separately prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate and water basis; only the 10 ml main dose transfers. Do not sum the full stock with main contributions."
  },
  {
    "decision_id": "q27",
    "label": "Na2SeO3 x 5 H2O stock amount",
    "decision": "correct",
    "source_stage": "Modified Wolin mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Pages1–2 Modified Wolin mineral subsection: exact row",
        "exact_source_quote": "Na2SeO3 x 5 H2O 0.30 mg",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin stock water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "This original amount is in a separately prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate and water basis; only the 10 ml main dose transfers. Do not sum the full stock with main contributions."
  },
  {
    "decision_id": "q28",
    "label": "Na2WO4 x 2 H2O stock amount",
    "decision": "correct",
    "source_stage": "Modified Wolin mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Pages1–2 Modified Wolin mineral subsection: exact row",
        "exact_source_quote": "Na2WO4 x 2 H2O 0.40 mg",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin stock water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "This original amount is in a separately prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate and water basis; only the 10 ml main dose transfers. Do not sum the full stock with main contributions."
  },
  {
    "decision_id": "q29",
    "label": "Mineral stock dose",
    "decision": "add",
    "source_stage": "Main stock addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main table stock dose",
        "exact_source_quote": "Modified Wolin's mineral solution 10.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "All layers lack solutions; represent the exact complete stock and its 10 ml source batch dose without inventing a per-liter denominator."
  },
  {
    "decision_id": "q30",
    "label": "Main water",
    "decision": "add",
    "source_stage": "Main batch",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page1 main table water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain 1000 ml main water independently of stock preparation water; water is absent as a named ingredient."
  },
  {
    "decision_id": "q31",
    "label": "Mineral stock water",
    "decision": "add",
    "source_stage": "Mineral stock",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Modified Wolin subsection water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain 1000 ml water within mineral stock only; it is not another main liter or a verified measured stock volume."
  },
  {
    "decision_id": "q32",
    "label": "Unknown final volume",
    "decision": "not_quantified",
    "source_stage": "Main denominator limit",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main table",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main table",
        "exact_source_quote": "Modified Wolin's mineral solution 10.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main table",
        "exact_source_quote": "Fe(NH4)2(SO4)2 x 7 H2O (0.1% w/v) 2.00 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main table",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "The known listed liquid additions sum to 1012.5 ml before unspecified sulfide stock volume. This sum is not a measured final volume; a 1012 ml-like local normalization is neither a declaration in this primary nor verified current API evidence."
  },
  {
    "decision_id": "q33",
    "label": "Main pH",
    "decision": "evidence_only",
    "source_stage": "Main pH",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 6.9
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ph_value",
        "stored": 6.9
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ph_value",
        "stored": 6.9
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "pH to 6.9",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Stored 6.9 agrees with source main adjustment, but no attached same-layer evidence exists."
  },
  {
    "decision_id": "q34",
    "label": "Main gas mixture",
    "decision": "add",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "80% H2\nand 20% CO2 gas mixture",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the exact source preparation quantity and its stated stage; this layer lacks preparation_steps."
  },
  {
    "decision_id": "q35",
    "label": "Main gas mixture",
    "decision": "add",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "80% H2\nand 20% CO2 gas mixture",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the exact source preparation quantity and its stated stage; this layer lacks preparation_steps."
  },
  {
    "decision_id": "q36",
    "label": "Main gas mixture",
    "decision": "evidence_only",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients except bicarbonate and sulfide, then sparge medium with 80% H2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add bicarbonate and adjust pH to 6.9, then dispense medium under 80% H2 and 20% CO2 gas atmosphere into serum vials (e.g., 20 ml per 100 ml bottle), seal and autoclave. Before use reduce the medium with sodium sulfide from a sterile anoxic stock solution prepared under 100% N2 gas."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "80% H2\nand 20% CO2 gas mixture",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Existing DSMZ-owner description retains this exact numeric preparation context without attached evidence. Do not turn vessel example, gas ratio or overpressure into a nutrient concentration."
  },
  {
    "decision_id": "q37",
    "label": "Sparging duration",
    "decision": "add",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "30 - 45 min",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the exact source preparation quantity and its stated stage; this layer lacks preparation_steps."
  },
  {
    "decision_id": "q38",
    "label": "Sparging duration",
    "decision": "add",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "30 - 45 min",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the exact source preparation quantity and its stated stage; this layer lacks preparation_steps."
  },
  {
    "decision_id": "q39",
    "label": "Sparging duration",
    "decision": "evidence_only",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients except bicarbonate and sulfide, then sparge medium with 80% H2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add bicarbonate and adjust pH to 6.9, then dispense medium under 80% H2 and 20% CO2 gas atmosphere into serum vials (e.g., 20 ml per 100 ml bottle), seal and autoclave. Before use reduce the medium with sodium sulfide from a sterile anoxic stock solution prepared under 100% N2 gas."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "30 - 45 min",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Existing DSMZ-owner description retains this exact numeric preparation context without attached evidence. Do not turn vessel example, gas ratio or overpressure into a nutrient concentration."
  },
  {
    "decision_id": "q40",
    "label": "Dispensing atmosphere",
    "decision": "add",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "80% H2 and 20% CO2 gas atmosphere",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the exact source preparation quantity and its stated stage; this layer lacks preparation_steps."
  },
  {
    "decision_id": "q41",
    "label": "Dispensing atmosphere",
    "decision": "add",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "80% H2 and 20% CO2 gas atmosphere",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the exact source preparation quantity and its stated stage; this layer lacks preparation_steps."
  },
  {
    "decision_id": "q42",
    "label": "Dispensing atmosphere",
    "decision": "evidence_only",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients except bicarbonate and sulfide, then sparge medium with 80% H2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add bicarbonate and adjust pH to 6.9, then dispense medium under 80% H2 and 20% CO2 gas atmosphere into serum vials (e.g., 20 ml per 100 ml bottle), seal and autoclave. Before use reduce the medium with sodium sulfide from a sterile anoxic stock solution prepared under 100% N2 gas."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "80% H2 and 20% CO2 gas atmosphere",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Existing DSMZ-owner description retains this exact numeric preparation context without attached evidence. Do not turn vessel example, gas ratio or overpressure into a nutrient concentration."
  },
  {
    "decision_id": "q43",
    "label": "Vessel example",
    "decision": "add",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "20 ml per 100 ml bottle",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the exact source preparation quantity and its stated stage; this layer lacks preparation_steps."
  },
  {
    "decision_id": "q44",
    "label": "Vessel example",
    "decision": "add",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "20 ml per 100 ml bottle",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the exact source preparation quantity and its stated stage; this layer lacks preparation_steps."
  },
  {
    "decision_id": "q45",
    "label": "Vessel example",
    "decision": "evidence_only",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients except bicarbonate and sulfide, then sparge medium with 80% H2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add bicarbonate and adjust pH to 6.9, then dispense medium under 80% H2 and 20% CO2 gas atmosphere into serum vials (e.g., 20 ml per 100 ml bottle), seal and autoclave. Before use reduce the medium with sodium sulfide from a sterile anoxic stock solution prepared under 100% N2 gas."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "20 ml per 100 ml bottle",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Existing DSMZ-owner description retains this exact numeric preparation context without attached evidence. Do not turn vessel example, gas ratio or overpressure into a nutrient concentration."
  },
  {
    "decision_id": "q46",
    "label": "Sulfide-stock atmosphere",
    "decision": "add",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "100% N2 gas",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the exact source preparation quantity and its stated stage; this layer lacks preparation_steps."
  },
  {
    "decision_id": "q47",
    "label": "Sulfide-stock atmosphere",
    "decision": "add",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "100% N2 gas",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the exact source preparation quantity and its stated stage; this layer lacks preparation_steps."
  },
  {
    "decision_id": "q48",
    "label": "Sulfide-stock atmosphere",
    "decision": "evidence_only",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients except bicarbonate and sulfide, then sparge medium with 80% H2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add bicarbonate and adjust pH to 6.9, then dispense medium under 80% H2 and 20% CO2 gas atmosphere into serum vials (e.g., 20 ml per 100 ml bottle), seal and autoclave. Before use reduce the medium with sodium sulfide from a sterile anoxic stock solution prepared under 100% N2 gas."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "100% N2 gas",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Existing DSMZ-owner description retains this exact numeric preparation context without attached evidence. Do not turn vessel example, gas ratio or overpressure into a nutrient concentration."
  },
  {
    "decision_id": "q49",
    "label": "Overpressure and gas",
    "decision": "add",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation2",
        "exact_source_quote": "2 bar overpressure of sterile 80% H2 and 20% CO2 gas mixture.",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the exact source preparation quantity and its stated stage; this layer lacks preparation_steps."
  },
  {
    "decision_id": "q50",
    "label": "Overpressure and gas",
    "decision": "add",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation2",
        "exact_source_quote": "2 bar overpressure of sterile 80% H2 and 20% CO2 gas mixture.",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Retain the exact source preparation quantity and its stated stage; this layer lacks preparation_steps."
  },
  {
    "decision_id": "q51",
    "label": "Overpressure and gas",
    "decision": "evidence_only",
    "source_stage": "Named main/stock procedure",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "After inoculation, add 2 bar overpressure of sterile 80% H2 and 20% CO2 gas mixture."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation2",
        "exact_source_quote": "2 bar overpressure of sterile 80% H2 and 20% CO2 gas mixture.",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Existing DSMZ-owner description retains this exact numeric preparation context without attached evidence. Do not turn vessel example, gas ratio or overpressure into a nutrient concentration."
  },
  {
    "decision_id": "q52",
    "label": "Initial mineral pH",
    "decision": "add",
    "source_stage": "Mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page2 mineral preparation",
        "exact_source_quote": "adjust pH to 6.5 with KOH",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Add only within mineral stock, not as main-medium pH."
  },
  {
    "decision_id": "q53",
    "label": "Initial mineral pH",
    "decision": "add",
    "source_stage": "Mineral stock",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page2 mineral preparation",
        "exact_source_quote": "adjust pH to 6.5 with KOH",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Add only within mineral stock, not as main-medium pH."
  },
  {
    "decision_id": "q54",
    "label": "Initial mineral pH",
    "decision": "correct",
    "source_stage": "Mineral stock",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page2 mineral preparation",
        "exact_source_quote": "adjust pH to 6.5 with KOH",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "The numeric text is retained but needs explicit mineral-stock scope; it is not a main-medium pH step."
  },
  {
    "decision_id": "q55",
    "label": "Final mineral pH",
    "decision": "add",
    "source_stage": "Mineral stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page2 mineral preparation",
        "exact_source_quote": "final to pH 7.0 with KOH.",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Add only within mineral stock, not as main-medium pH."
  },
  {
    "decision_id": "q56",
    "label": "Final mineral pH",
    "decision": "add",
    "source_stage": "Mineral stock",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page2 mineral preparation",
        "exact_source_quote": "final to pH 7.0 with KOH.",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Add only within mineral stock, not as main-medium pH."
  },
  {
    "decision_id": "q57",
    "label": "Final mineral pH",
    "decision": "correct",
    "source_stage": "Mineral stock",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Page2 mineral preparation",
        "exact_source_quote": "final to pH 7.0 with KOH.",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "The numeric text is retained but needs explicit mineral-stock scope; it is not a main-medium pH step."
  },
  {
    "decision_id": "q58",
    "label": "KOH strength and dose",
    "decision": "not_quantified",
    "source_stage": "Mineral stock",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Mineral stock initial adjustment",
        "exact_source_quote": "adjust pH to 6.5 with KOH",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      },
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Mineral stock final adjustment",
        "exact_source_quote": "final to pH 7.0 with KOH.",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Neither acid/base amount nor concentration follows from the pH targets; do not guess."
  },
  {
    "decision_id": "q59",
    "label": "Late sulfide stock strength and volume",
    "decision": "not_quantified",
    "source_stage": "Sulfide stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.494071",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.494071",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.494071",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "with sodium sulfide from a sterile anoxic stock solution prepared under 100% N2 gas.",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "The source gives a main sulfide mass but no separate stock strength or volume dose; retain the distinct late-addition step."
  },
  {
    "decision_id": "q60",
    "label": "Sterilization method and absent cycle",
    "decision": "not_quantified",
    "source_stage": "Main preparation",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz399",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf",
        "source_locator": "Main preparation1",
        "exact_source_quote": "seal and autoclave.",
        "snapshot_sha256": "29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0",
        "parsed_text_sha256": "4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22"
      }
    ],
    "interpretation": "Autoclaving is explicit, but no cycle time/temperature is supplied. Restore the method where absent and retain unknown cycle numbers rather than borrowing defaults."
  }
]

### Two maintained owners and generated boundary

ownership: supported. Targets: CultureMech:005188.

Both exact archaea owners own future correction. Complete source bytes and their different preparation/history fields were compared; the target must be regenerated only after maintained-input repair. No recipe, history or generated artifact was changed.

## Findings

### f1: Full-stock concentrations and main ingredients have been combined

blocker / open / confirmed; issue key: cm005188-stocks-sums.

Modified Wolin constituents remain flat in all three layers; magnesium sulfate 6.40909, calcium chloride 0.23834 and sodium chloride 18.7866 sum main values with undiluted stock strengths. The exact 10 ml stock dose and both water contexts are missing. Existing normalized main numbers cannot establish their own denominator.

### f2: Nickel hydrate and resazurin salt are misgrounded

major / open / confirmed; issue key: cm005188-forms.

NiCl2 hexahydrate is assigned anhydrous nickel dichloride; sodium resazurin is assigned the neutral molecule. Canonical labels and current MIM membership do not resolve these supplied-form mismatches.

### f3: Generated and KOMODO layers omit source preparation

major / open / confirmed; issue key: cm005188-preparation.

DSMZ owner retains gas ratios, timing, vessel example, late sulfide, 2 bar overpressure and pH instructions; target and KOMODO owner omit them. Mineral initial pH 6.5 and final 7.0 also require explicit stock placement in the DSMZ owner.

### f4: Both relation directions name absent bacterial paths

major / open / confirmed; issue key: cm005188-broken-relations.

Target/KOMODO parent points to bacterial/archaeoglobus_medium.yaml; DSMZ child points to bacterial/KOMODO_399_ARCHAEOGLOBUS_medium.yaml. Ignored-inclusive exact stable-ID search resolves both owners under archaea instead. This path defect is distinct from historical source-equivalence uncertainty.

### f5: Source claims lack attachments and historical timestamps need qualification

minor / open / confirmed; issue key: cm005188-evidence-history.

No main/stock/preparation claim has attached evidence. KOMODO and target each retain a malformed timestamp and a timezone-naive event; their copied-source history cannot authenticate current API payloads. Preserve those historical bytes and qualify them separately.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct the full mineral stock and its dose, split contributions and retain original main amounts/stock units and water stages. Resolve volume evidence before asserting final concentrations.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Use exact source and structural evidence to reconcile salt/hydrate grounding without guessed IDs or unsupported molecular-weight conversions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve exact source preparation in maintained contributors and ensure regenerated target retains it, with stock pH separate from main 6.9 and unknown cycle numbers left unresolved.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Correct maintained locators only after exact ID verification, recheck both directions and preserve the evidence scope of SOURCE_DUPLICATE rather than treating a signature as historical proof.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Attach narrow exact-source evidence after correction, append rather than rewrite historical clarification, and distinguish source linkage from historical byte equivalence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/archaea/archaeoglobus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch030/298/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-030/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch030/298/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml:1:id: CultureMech:005188<br>./data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml:1:id: CultureMech:005188<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch030/source-preflight-bound/298/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 33 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf; Complete two-page primary: main table, preparation and Modified Wolin mineral subsection | supports | Exact main recipe and named stock are available. Main water, stock doses and stock water remain separate; no measured final-volume declaration is printed. |
| mineral | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf; Modified Wolin mineral solution only | supports | Only the named mineral stock and its pH adjustment transfer. Parent basal, vitamin and organism-specific instructions are excluded. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact MediaInfo=399 accession row | supports | Current catalogue explicitly links this accession to DSMZ399; Is Aerobic=false is metadata, not an independent physiological experiment. |
| catalog-header | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact header row | supports | Column labels distinguish Is Complex from Is Aerobic. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Exact label validity is separate from source chemical-form support. |
| chebi131378 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131378; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:131378 resolves to ferrous ammonium sulfate heptahydrate. Exact label validity is separate from source chemical-form support. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Exact label validity is separate from source chemical-form support. |
| chebi232798 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_232798; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:232798 resolves to sodium L-lactate. Exact label validity is separate from source chemical-form support. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:26710 resolves to sodium chloride. Exact label validity is separate from source chemical-form support. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:31206 resolves to ammonium chloride. Exact label validity is separate from source chemical-form support. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Exact label validity is separate from source chemical-form support. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Exact label validity is separate from source chemical-form support. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Exact label validity is separate from source chemical-form support. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Exact label validity is separate from source chemical-form support. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:32588 resolves to potassium chloride. Exact label validity is separate from source chemical-form support. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:33118 resolves to boric acid. Exact label validity is separate from source chemical-form support. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:34887 resolves to nickel dichloride. Exact label validity is separate from source chemical-form support. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:44557 resolves to nitrilotriacetic acid. Exact label validity is separate from source chemical-form support. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Exact label validity is separate from source chemical-form support. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Exact label validity is separate from source chemical-form support. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Exact label validity is separate from source chemical-form support. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Exact label validity is separate from source chemical-form support. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Exact label validity is separate from source chemical-form support. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Exact label validity is separate from source chemical-form support. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Exact label validity is separate from source chemical-form support. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Exact label validity is separate from source chemical-form support. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:8806 resolves to Resazurin. Exact label validity is separate from source chemical-form support. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. Exact label validity is separate from source chemical-form support. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned index exact identifier lookup; adjacent snapshot metadata | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131378": [{"label": "Fe(NH4)2(SO4)2 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131378", "preferred_term": "Fe(NH4)2(SO4)2 x 7 H2O", "ontology_id": "CHEBI:131378", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:232798": [{"label": "Na-L-lactate", "match_type": "preferred_term", "identifier": "CHEBI:232798", "preferred_term": "Na-L-lactate", "ontology_id": "CHEBI:232798", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "missing_current_keys": []} |
| history-metadata | data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml; data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml; data/normalized_yaml/archaea/archaeoglobus_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:59.241479"}]}, {"input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:59.241479"}]}, {"input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml", "events": 8, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer and cleanup/merge functions are scoped context. Current duplicate code does not prove historical summation; the observed source differences and historical notes supply separate evidence. |
| writer-1 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer and cleanup/merge functions are scoped context. Current duplicate code does not prove historical summation; the observed source differences and historical notes supply separate evidence. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer and cleanup/merge functions are scoped context. Current duplicate code does not prove historical summation; the observed source differences and historical notes supply separate evidence. |
| relations | /private/tmp/culturemech-review-work-batch030/source-preflight-bound/298/evidence-context-original.json; Ignored-inclusive exact path/basename/stable-ID lookup | context_only | [{"record_path": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml", "field_path": "$.parent_media", "assertion": {"path": "data/normalized_yaml/bacterial/archaeoglobus_medium.yaml", "relationship": "SOURCE_DUPLICATE", "id": "CultureMech:001508", "name": "archaeoglobus_medium", "notes": "KOMODO record explicitly cites DSMZ Medium 399; one unlinked DSMZ parent record exists and the local physical state, pH, ingredient, and concentration signatures match exactly."}, "declared_path_in_ignored_inclusive_listing": false, "resolved_exact_id_and_basename": [{"path": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml", "id": "CultureMech:001508", "sha256": "fd1e708c4811c9f1f6112549a8d9761574622785a0e9978b896b072a6a3cab3f"}], "search_scope": "All normalized files, ignored/hidden included; exact case and parsed stableID; no link repair inferred."}, {"record_path": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml", "field_path": "$.parent_media", "assertion": {"path": "data/normalized_yaml/bacterial/archaeoglobus_medium.yaml", "relationship": "SOURCE_DUPLICATE", "id": "CultureMech:001508", "name": "archaeoglobus_medium", "notes": "KOMODO record explicitly cites DSMZ Medium 399; one unlinked DSMZ parent record exists and the local physical state, pH, ingredient, and concentration signatures match exactly."}, "declared_path_in_ignored_inclusive_listing": false, "resolved_exact_id_and_basename": [{"path": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml", "id": "CultureMech:001508", "sha256": "fd1e708c4811c9f1f6112549a8d9761574622785a0e9978b896b072a6a3cab3f"}], "search_scope": "All normalized files, ignored/hidden included; exact case and parsed stableID; no link repair inferred."}, {"record_path": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml", "field_path": "$.variant_children[0]", "assertion": {"path": "data/normalized_yaml/bacterial/KOMODO_399_ARCHAEOGLOBUS_medium.yaml", "relationship": "SOURCE_DUPLICATE", "id": "CultureMech:005188", "name": "archaeoglobus_medium", "notes": "KOMODO record is an exact source duplicate of DSMZ Medium 399; local ingredient and concentration signatures match."}, "declared_path_in_ignored_inclusive_listing": false, "resolved_exact_id_and_basename": [{"path": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml", "id": "CultureMech:005188", "sha256": "9ad78be620171c5b6c8161cf4593a421ba6b423486ac9bb5a739239bfbd53683"}], "search_scope": "All normalized files, ignored/hidden included; exact case and parsed stableID; no link repair inferred."}] |
| quantity-inventory | /private/tmp/culturemech-review-work-batch030/298/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| mediadive399api-attempt | https://mediadive.dsmz.de/rest/medium/399; Preserved exact public retrieval result | context_only | Optional mediadive399api request returned 503. Current base formulation can be assessed from the exact catalogue link and primary sources; historical byte equivalence and a distinct KOMODO variant are not inferred. |
| komodo399detail-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaInfo=399; Preserved exact public retrieval result | context_only | Optional komodo399detail request returned 403. Current base formulation can be assessed from the exact catalogue link and primary sources; historical byte equivalence and a distinct KOMODO variant are not inferred. |
| komodo399actual-attempt | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=399; Preserved exact public retrieval result | context_only | Optional komodo399actual request returned 403. Current base formulation can be assessed from the exact catalogue link and primary sources; historical byte equivalence and a distinct KOMODO variant are not inferred. |
| mediadive399retry-attempt | https://mediadive.dsmz.de/rest/medium/399; Preserved exact public retrieval result | context_only | Optional mediadive399retry request returned 503. Current base formulation can be assessed from the exact catalogue link and primary sources; historical byte equivalence and a distinct KOMODO variant are not inferred. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Optional mediadive399api request returned 503. Current base formulation can be assessed from the exact catalogue link and primary sources; historical byte equivalence and a distinct KOMODO variant are not inferred.
- Optional komodo399detail request returned 403. Current base formulation can be assessed from the exact catalogue link and primary sources; historical byte equivalence and a distinct KOMODO variant are not inferred.
- Optional komodo399actual request returned 403. Current base formulation can be assessed from the exact catalogue link and primary sources; historical byte equivalence and a distinct KOMODO variant are not inferred.
- Optional mediadive399retry request returned 503. Current base formulation can be assessed from the exact catalogue link and primary sources; historical byte equivalence and a distinct KOMODO variant are not inferred.
- No required identifier remains unresolved in this bounded current-source review. Parent DSMZ141 transfers only the named mineral subsection and its pH, not parent vitamins, basal medium, organisms or other conditions. All source batch quantities remain separate from unknown measured final volume and current API normalization.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T165630Z-culturemech-005188-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: archaeoglobus_medium (CultureMech:005188)'
started_at: '2026-10-21T16:49:42Z'
finished_at: '2026-10-21T16:56:30Z'
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
summary: Exact KOMODO 399 catalogue metadata links to DSMZ 399, whose complete primary
  defines a main medium and Modified Wolin mineral stock. All three local layers flatten
  stock strengths and sum full-stock magnesium, calcium and sodium with main contributions.
  Their normalized main numbers have no authenticated current provider denominator
  or primary-declared final volume. The DSMZ owner retains preparation that the target
  and KOMODO owner omit. Nickel hydrate and resazurin salt mismatches, broken category-specific
  relation paths and unattached source evidence require curation; current source access
  is sufficient for this bounded formulation review.
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
  - path: data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml
    sha256: e78b7f6a7ec9fd188478ce58edc4e1401a1ac81f65e6f94f8a2a8dd7136361cb
    role: target
  - path: data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml
    sha256: 9ad78be620171c5b6c8161cf4593a421ba6b423486ac9bb5a739239bfbd53683
    role: context
  - path: data/normalized_yaml/archaea/archaeoglobus_medium.yaml
    sha256: fd1e708c4811c9f1f6112549a8d9761574622785a0e9978b896b072a6a3cab3f
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml.md
    sha256: 05a51d1357da9d5e2b5e9336137ac1c051691d73dc80ffa5c87ff78eaac81f61
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/archaea/archaeoglobus_medium.yaml.md
    sha256: 3f60d7df0dd728acd7a60e4258da7c3e5defdd08965c10431e0e57186170f3cb
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
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
  - path: scripts/promote_komodo_volume_candidates.py
    sha256: 2423b7e2e04011b31d21eac939714a2db4380f033a69094325dc567e44929cd2
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
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
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
  - path: src/culturemech/convert/komodo_web_raw_yaml.py
    sha256: a1a37015b4e6bac657e49f375b39a319815cc6b02a02135674a858a8b6eab03a
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
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/fetch/komodo_web_fetcher.py
    sha256: 89c510caa08d989b7ec6cee9ac17cc2f0faab606fe8a29ca435df476e52ff004
    role: context
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
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
  selection: Task review 298; batch 030 item 8 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-nine task batches
    contain 290 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 293 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:005188
targets:
- target_id: CultureMech:005188
  path: data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml
  label: archaeoglobus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:005188
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch030/298/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-030/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch030/298/strict.tsv"
  target_ids:
  - CultureMech:005188
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:005188
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:005188
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
  - CultureMech:005188
- check_id: mediadive399api-source-access
  name: 'Exact source content access: mediadive399api'
  required: false
  status: unavailable
  summary: Optional mediadive399api request returned 503. Current base formulation
    can be assessed from the exact catalogue link and primary sources; historical
    byte equivalence and a distinct KOMODO variant are not inferred.
  target_ids:
  - CultureMech:005188
  evidence_ids:
  - mediadive399api-attempt
- check_id: komodo399detail-source-access
  name: 'Exact source content access: komodo399detail'
  required: false
  status: unavailable
  summary: Optional komodo399detail request returned 403. Current base formulation
    can be assessed from the exact catalogue link and primary sources; historical
    byte equivalence and a distinct KOMODO variant are not inferred.
  target_ids:
  - CultureMech:005188
  evidence_ids:
  - komodo399detail-attempt
- check_id: komodo399actual-source-access
  name: 'Exact source content access: komodo399actual'
  required: false
  status: unavailable
  summary: Optional komodo399actual request returned 403. Current base formulation
    can be assessed from the exact catalogue link and primary sources; historical
    byte equivalence and a distinct KOMODO variant are not inferred.
  target_ids:
  - CultureMech:005188
  evidence_ids:
  - komodo399actual-attempt
- check_id: mediadive399retry-source-access
  name: 'Exact source content access: mediadive399retry'
  required: false
  status: unavailable
  summary: Optional mediadive399retry request returned 503. Current base formulation
    can be assessed from the exact catalogue link and primary sources; historical
    byte equivalence and a distinct KOMODO variant are not inferred.
  target_ids:
  - CultureMech:005188
  evidence_ids:
  - mediadive399retry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T16:56:28Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T16:56:28Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/archaea/archaeoglobus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T16:56:28Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:50:05.903191Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch030/298/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T16:50:07.981561Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-030/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch030/298/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:50:10.259561Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:50:11.288576Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T16:56:28Z'
  support: supports
  summary: './data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml:1:id:
    CultureMech:005188

    ./data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml:1:id: CultureMech:005188

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch030/source-preflight-bound/298/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T16:56:28Z'
  support: supports
  summary: 33 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 57c82a19c6754dd42b2480a7521ffb7e7b2908f76630f9ec76c58e4f831d1f63
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf
  locator: 'Complete two-page primary: main table, preparation and Modified Wolin
    mineral subsection'
  accessed_at: '2026-10-21T16:34:00.130965Z'
  support: supports
  summary: Exact main recipe and named stock are available. Main water, stock doses
    and stock water remain separate; no measured final-volume declaration is printed.
  quote: '399: ARCHAEOGLOBUS MEDIUM'
  snapshot_sha256: 29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0
- evidence_id: mineral
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf
  locator: Modified Wolin mineral solution only
  accessed_at: '2026-10-21T10:13:12.306566Z'
  support: supports
  summary: Only the named mineral stock and its pH adjustment transfer. Parent basal,
    vitamin and organism-specific instructions are excluded.
  quote: NiCl2 x 6 H2O 0.03 g
  snapshot_sha256: 8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact MediaInfo=399 accession row
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Current catalogue explicitly links this accession to DSMZ399; Is Aerobic=false
    is metadata, not an independent physiological experiment.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=399'\
    \ >399</a></TD>\n\t\t\t\t\t<TD>ARCHAEOGLOBUS medium</TD>\n\t\t\t\t\t<TD> 6.9</TD>\n\
    \t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n\
    <TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf</a></TD>\n\t\
    \t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: catalog-header
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact header row
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Column labels distinguish Is Complex from Is Aerobic.
  quote: "<TR>\n\t\t\t\t\t<TD valign=\"top\" align=\"left\" width=\"50\">ID</TD>\n\
    \t\t\t\t\t<TD valign=\"top\" align=\"left\">Name</TD>\n\t\t\t\t\t<TD valign=\"\
    top\" align=\"left\">PH Info</TD>\n\t\t\t\t\t<TD valign=\"top\" align=\"left\"\
    >Is Complex</TD>\n\t\t\t\t\t<TD valign=\"top\" align=\"left\">Is Aerobic</TD>\n\
    \t\t\t\t\t<TD valign=\"top\" align=\"left\">Is SubMedium</TD>\n\t\t\t\t\t<TD valign=\"\
    top\" align=\"left\">Instructions</TD>\n\t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: chebi131361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T07:33:27.980786Z'
  support: supports
  summary: CHEBI:131361 resolves to disodium selenite pentahydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi131378
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131378
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T16:34:00.785581Z'
  support: supports
  summary: CHEBI:131378 resolves to ferrous ammonium sulfate heptahydrate. Exact label
    validity is separate from source chemical-form support.
  snapshot_sha256: c7f21c3d5ea0eb206069589ba5b58cbd89b3ed96f796286de9536cbe6cef5337
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi232798
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_232798
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T13:39:29.688460Z'
  support: supports
  summary: CHEBI:232798 resolves to sodium L-lactate. Exact label validity is separate
    from source chemical-form support.
  snapshot_sha256: 9babe942a39eb91a513ec202dbae4289fda9f5586836aaee58192b4795ce7344
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride. Exact label validity is separate
    from source chemical-form support.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: CHEBI:31206 resolves to ammonium chloride. Exact label validity is separate
    from source chemical-form support.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:28.489501Z'
  support: supports
  summary: CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: CHEBI:32139 resolves to sodium hydrogencarbonate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: CHEBI:32312 resolves to zinc sulfate heptahydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: CHEBI:32588 resolves to potassium chloride. Exact label validity is separate
    from source chemical-form support.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid. Exact label validity is separate from
    source chemical-form support.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: CHEBI:34887 resolves to nickel dichloride. Exact label validity is separate
    from source chemical-form support.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi44557
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:46:15.250117Z'
  support: supports
  summary: CHEBI:44557 resolves to nitrilotriacetic acid. Exact label validity is
    separate from source chemical-form support.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: CHEBI:63939 resolves to sodium tungstate dihydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: CHEBI:76209 resolves to sodium sulfide nonahydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: CHEBI:86345 resolves to magnesium dichloride hexahydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86364
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T07:33:35.036768Z'
  support: supports
  summary: CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Exact label
    validity is separate from source chemical-form support.
  snapshot_sha256: f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069
- evidence_id: chebi86465
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:08.054799Z'
  support: supports
  summary: CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Exact
    label validity is separate from source chemical-form support.
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: CHEBI:8806 resolves to Resazurin. Exact label validity is separate from
    source chemical-form support.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi91244
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:07.079384Z'
  support: supports
  summary: CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned index exact identifier lookup; adjacent snapshot metadata
  accessed_at: '2026-10-21T16:56:28Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows":
    {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id":
    "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131378":
    [{"label": "Fe(NH4)2(SO4)2 x 7 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:131378", "preferred_term": "Fe(NH4)2(SO4)2 x 7 H2O", "ontology_id": "CHEBI:131378",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label":
    "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term":
    "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:232798": [{"label": "Na-L-lactate", "match_type": "preferred_term",
    "identifier": "CHEBI:232798", "preferred_term": "Na-L-lactate", "ontology_id":
    "CHEBI:232798", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label":
    "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label":
    "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term":
    "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588":
    [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588",
    "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label":
    "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term":
    "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id":
    "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939":
    [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209":
    [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label":
    "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465",
    "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term":
    "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}, "missing_current_keys": []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml; data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml;
    data/normalized_yaml/archaea/archaeoglobus_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T16:56:28Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:18:59.241479"}]}, {"input": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:18:59.241479"}]}, {"input": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
    "events": 8, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:56:28Z'
  support: context_only
  summary: Current importer and cleanup/merge functions are scoped context. Current
    duplicate code does not prove historical summation; the observed source differences
    and historical notes supply separate evidence.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:56:28Z'
  support: context_only
  summary: Current importer and cleanup/merge functions are scoped context. Current
    duplicate code does not prove historical summation; the observed source differences
    and historical notes supply separate evidence.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:56:28Z'
  support: context_only
  summary: Current importer and cleanup/merge functions are scoped context. Current
    duplicate code does not prove historical summation; the observed source differences
    and historical notes supply separate evidence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: relations
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch030/source-preflight-bound/298/evidence-context-original.json
  locator: Ignored-inclusive exact path/basename/stable-ID lookup
  accessed_at: '2026-10-21T16:56:28Z'
  support: context_only
  summary: '[{"record_path": "data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml", "field_path":
    "$.parent_media", "assertion": {"path": "data/normalized_yaml/bacterial/archaeoglobus_medium.yaml",
    "relationship": "SOURCE_DUPLICATE", "id": "CultureMech:001508", "name": "archaeoglobus_medium",
    "notes": "KOMODO record explicitly cites DSMZ Medium 399; one unlinked DSMZ parent
    record exists and the local physical state, pH, ingredient, and concentration
    signatures match exactly."}, "declared_path_in_ignored_inclusive_listing": false,
    "resolved_exact_id_and_basename": [{"path": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
    "id": "CultureMech:001508", "sha256": "fd1e708c4811c9f1f6112549a8d9761574622785a0e9978b896b072a6a3cab3f"}],
    "search_scope": "All normalized files, ignored/hidden included; exact case and
    parsed stableID; no link repair inferred."}, {"record_path": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
    "field_path": "$.parent_media", "assertion": {"path": "data/normalized_yaml/bacterial/archaeoglobus_medium.yaml",
    "relationship": "SOURCE_DUPLICATE", "id": "CultureMech:001508", "name": "archaeoglobus_medium",
    "notes": "KOMODO record explicitly cites DSMZ Medium 399; one unlinked DSMZ parent
    record exists and the local physical state, pH, ingredient, and concentration
    signatures match exactly."}, "declared_path_in_ignored_inclusive_listing": false,
    "resolved_exact_id_and_basename": [{"path": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
    "id": "CultureMech:001508", "sha256": "fd1e708c4811c9f1f6112549a8d9761574622785a0e9978b896b072a6a3cab3f"}],
    "search_scope": "All normalized files, ignored/hidden included; exact case and
    parsed stableID; no link repair inferred."}, {"record_path": "data/normalized_yaml/archaea/archaeoglobus_medium.yaml",
    "field_path": "$.variant_children[0]", "assertion": {"path": "data/normalized_yaml/bacterial/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
    "relationship": "SOURCE_DUPLICATE", "id": "CultureMech:005188", "name": "archaeoglobus_medium",
    "notes": "KOMODO record is an exact source duplicate of DSMZ Medium 399; local
    ingredient and concentration signatures match."}, "declared_path_in_ignored_inclusive_listing":
    false, "resolved_exact_id_and_basename": [{"path": "data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml",
    "id": "CultureMech:005188", "sha256": "9ad78be620171c5b6c8161cf4593a421ba6b423486ac9bb5a739239bfbd53683"}],
    "search_scope": "All normalized files, ignored/hidden included; exact case and
    parsed stableID; no link repair inferred."}]'
  snapshot_sha256: 5c12b2d77a00d770ee76db7e02895df9f4aeb8d9102770a5e204a33dcdc75c8d
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch030/298/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T16:56:28Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 274f58199baefd9f14406e02a66654aaacd237851c3492b6bd872bf65613a9a7
- evidence_id: mediadive399api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/399
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:33:59.532747Z'
  support: context_only
  summary: Optional mediadive399api request returned 503. Current base formulation
    can be assessed from the exact catalogue link and primary sources; historical
    byte equivalence and a distinct KOMODO variant are not inferred.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo399detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaInfo=399
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:33:59.356552Z'
  support: context_only
  summary: Optional komodo399detail request returned 403. Current base formulation
    can be assessed from the exact catalogue link and primary sources; historical
    byte equivalence and a distinct KOMODO variant are not inferred.
  snapshot_sha256: 81f0eb1b52f75cfabfbd99f2f54e51f5397b492355745c84b79d72ce36462067
- evidence_id: komodo399actual-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=399
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:33:59.356942Z'
  support: context_only
  summary: Optional komodo399actual request returned 403. Current base formulation
    can be assessed from the exact catalogue link and primary sources; historical
    byte equivalence and a distinct KOMODO variant are not inferred.
  snapshot_sha256: 8e4a026a70f5a9106bf4ab55a2fa7425987a99207df5cf9ac2f1893d61ed8186
- evidence_id: mediadive399retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/399
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:38:11.087237Z'
  support: context_only
  summary: Optional mediadive399retry request returned 503. Current base formulation
    can be assessed from the exact catalogue link and primary sources; historical
    byte equivalence and a distinct KOMODO variant are not inferred.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:005188
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary chemical identifiers
  outcome: concern
  summary: '24 distinct primary/current-secondary IDs have matching nonobsolete labels.
    Target direct-ingredient linkage is 24/25 primary (96.00%) and 23/25 current CHEBI-based
    secondary (92.00%), on a 0–100 linkage scale, not an accuracy score. Current secondary
    keys without pinned index rows: []. Legacy slot count 0 is separate and does not
    enter that current-key claim. Supplied-form correspondence is assessed separately.'
  target_ids:
  - CultureMech:005188
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi131361
  - chebi131378
  - chebi131527
  - chebi232798
  - chebi26710
  - chebi31206
  - chebi31440
  - chebi31795
  - chebi32139
  - chebi32312
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi44557
  - chebi63939
  - chebi75213
  - chebi75836
  - chebi76209
  - chebi86158
  - chebi86345
  - chebi86364
  - chebi86465
  - chebi8806
  - chebi91244
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 26 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:005188
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: identity
  area: identity
  topic: Explicit catalogue linkage and maintained contributors
  outcome: supported
  summary: KOMODO399 links directly to DSMZ399; both maintained source contributors
    resolve to exact stable IDs and actual archaea paths. Historical KOMODO detail
    bytes and current API are unavailable, but no distinct historical variant or byte
    equivalence is inferred. Exact current primary formulation is assessed directly.
  target_ids:
  - CultureMech:005188
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - catalog
  - catalog-header
- assessment_id: classification
  area: scope
  topic: Mixture state and organism boundaries
  outcome: supported
  summary: Liquid and complex with SEMI_DEFINED composition is compatible with specified
    salts plus undefined yeast extract, without agar. Catalogue no-aerobic metadata
    aligns with the primary anoxic procedure but does not independently prove physiology.
    No organism-specific growth, optimum, taxonomy, DOI or PMID is asserted by this
    review.
  target_ids:
  - CultureMech:005188
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - catalog
  - catalog-header
- assessment_id: forms
  area: grounding
  topic: Source hydrate and salt correspondence
  outcome: concern
  summary: Nickel chloride hexahydrate is linked to anhydrous CHEBI:34887; sodium
    resazurin is linked to neutral CHEBI:8806. Printed ferrous ammonium sulfate heptahydrate
    agrees with CHEBI:131378, and explicit sodium L-lactate agrees with its L-specific
    term. Other named hydrates were compared with captured structures; current MIM
    matches cannot substitute for source-form evidence.
  target_ids:
  - CultureMech:005188
  evidence_ids:
  - primary
  - mineral
  - chebi34887
  - chebi8806
  - chebi131378
  - chebi232798
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 60 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:005188
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"label\": \"KCl\",\n    \"\
    decision\": \"correct\",\n    \"source_stage\": \"Main batch\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.335968\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.335968\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.335968\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table: exact named row\",\n      \
    \  \"exact_source_quote\": \"KCl 0.34 g\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Page1 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the original main amount/unit\
    \ and its source batch context. The primary lists 1000 ml water plus stock additions,\
    \ without an explicit final-volume denominator; do not authenticate the existing\
    \ G_PER_L basis by reverse-engineering its number.\"\n  },\n  {\n    \"decision_id\"\
    : \"q2\",\n    \"label\": \"MgCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n\
    \    \"source_stage\": \"Main batch\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"3.95257\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.95257\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.95257\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table: exact named row\",\n      \
    \  \"exact_source_quote\": \"MgCl2 x 6 H2O 4.00 g\",\n        \"snapshot_sha256\"\
    : \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\",\n    \
    \    \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Page1 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the original main amount/unit\
    \ and its source batch context. The primary lists 1000 ml water plus stock additions,\
    \ without an explicit final-volume denominator; do not authenticate the existing\
    \ G_PER_L basis by reverse-engineering its number.\"\n  },\n  {\n    \"decision_id\"\
    : \"q3\",\n    \"label\": \"MgSO4 x 7 H2O\",\n    \"decision\": \"correct\",\n\
    \    \"source_stage\": \"Main batch\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"6.40909\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.40909\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.40909\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table: exact named row\",\n      \
    \  \"exact_source_quote\": \"MgSO4 x 7 H2O 3.45 g\",\n        \"snapshot_sha256\"\
    : \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\",\n    \
    \    \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Page1 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the original main amount/unit\
    \ and its source batch context. The primary lists 1000 ml water plus stock additions,\
    \ without an explicit final-volume denominator; do not authenticate the existing\
    \ G_PER_L basis by reverse-engineering its number. This local value also sums\
    \ a main contribution with an undiluted full-stock concentration; separate both\
    \ stages.\"\n  },\n  {\n    \"decision_id\": \"q4\",\n    \"label\": \"NH4Cl\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"Main batch\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.247036\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.247036\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.247036\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table: exact named row\",\n      \
    \  \"exact_source_quote\": \"NH4Cl 0.25 g\",\n        \"snapshot_sha256\": \"\
    29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\",\n        \"\
    parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Page1 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the original main amount/unit\
    \ and its source batch context. The primary lists 1000 ml water plus stock additions,\
    \ without an explicit final-volume denominator; do not authenticate the existing\
    \ G_PER_L basis by reverse-engineering its number.\"\n  },\n  {\n    \"decision_id\"\
    : \"q5\",\n    \"label\": \"CaCl2 x 2 H2O\",\n    \"decision\": \"correct\",\n\
    \    \"source_stage\": \"Main batch\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.23834\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.23834\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.23834\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table: exact named row\",\n      \
    \  \"exact_source_quote\": \"CaCl2 x 2 H2O 0.14 g\",\n        \"snapshot_sha256\"\
    : \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\",\n    \
    \    \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Page1 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the original main amount/unit\
    \ and its source batch context. The primary lists 1000 ml water plus stock additions,\
    \ without an explicit final-volume denominator; do not authenticate the existing\
    \ G_PER_L basis by reverse-engineering its number. This local value also sums\
    \ a main contribution with an undiluted full-stock concentration; separate both\
    \ stages.\"\n  },\n  {\n    \"decision_id\": \"q6\",\n    \"label\": \"K2HPO4\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"Main batch\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.13834\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.13834\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.13834\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table: exact named row\",\n      \
    \  \"exact_source_quote\": \"K2HPO4 0.14 g\",\n        \"snapshot_sha256\": \"\
    29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\",\n        \"\
    parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Page1 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the original main amount/unit\
    \ and its source batch context. The primary lists 1000 ml water plus stock additions,\
    \ without an explicit final-volume denominator; do not authenticate the existing\
    \ G_PER_L basis by reverse-engineering its number.\"\n  },\n  {\n    \"decision_id\"\
    : \"q7\",\n    \"label\": \"NaCl\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Main batch\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"18.7866\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"18.7866\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"18.7866\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table: exact named row\",\n      \
    \  \"exact_source_quote\": \"NaCl 18.00 g\",\n        \"snapshot_sha256\": \"\
    29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\",\n        \"\
    parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Page1 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the original main amount/unit\
    \ and its source batch context. The primary lists 1000 ml water plus stock additions,\
    \ without an explicit final-volume denominator; do not authenticate the existing\
    \ G_PER_L basis by reverse-engineering its number. This local value also sums\
    \ a main contribution with an undiluted full-stock concentration; separate both\
    \ stages.\"\n  },\n  {\n    \"decision_id\": \"q8\",\n    \"label\": \"Yeast extract\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"Main batch\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.494071\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.494071\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.494071\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table: exact named row\",\n      \
    \  \"exact_source_quote\": \"Yeast extract (OXOID) 0.50 g\",\n        \"snapshot_sha256\"\
    : \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\",\n    \
    \    \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Page1 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the original main amount/unit\
    \ and its source batch context. The primary lists 1000 ml water plus stock additions,\
    \ without an explicit final-volume denominator; do not authenticate the existing\
    \ G_PER_L basis by reverse-engineering its number.\"\n  },\n  {\n    \"decision_id\"\
    : \"q9\",\n    \"label\": \"Na-L-lactate\",\n    \"decision\": \"correct\",\n\
    \    \"source_stage\": \"Main batch\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.48221\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.48221\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.48221\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table: exact named row\",\n      \
    \  \"exact_source_quote\": \"Na-L-lactate 1.50 g\",\n        \"snapshot_sha256\"\
    : \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\",\n    \
    \    \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Page1 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the original main amount/unit\
    \ and its source batch context. The primary lists 1000 ml water plus stock additions,\
    \ without an explicit final-volume denominator; do not authenticate the existing\
    \ G_PER_L basis by reverse-engineering its number.\"\n  },\n  {\n    \"decision_id\"\
    : \"q10\",\n    \"label\": \"Fe(NH4)2(SO4)2 x 7 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"source_stage\": \"Main batch\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\",\n   \
    \     \"field_path\": \"ingredients[9].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.00197628\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00197628\",\n          \"unit\": \"G_PER_L\"\n \
    \       }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00197628\",\n          \"unit\": \"G_PER_L\"\n \
    \       }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table: exact named row\",\n      \
    \  \"exact_source_quote\": \"Fe(NH4)2(SO4)2 x 7 H2O (0.1% w/v) 2.00 ml\",\n  \
    \      \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Page1 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the original main amount/unit\
    \ and its source batch context. The primary lists 1000 ml water plus stock additions,\
    \ without an explicit final-volume denominator; do not authenticate the existing\
    \ G_PER_L basis by reverse-engineering its number. Preserve the explicit 0.1%\
    \ w/v stock strength and its separate volume dose. That supports a delivered mass\
    \ calculation but not the existing final concentration without a final-volume\
    \ basis.\"\n  },\n  {\n    \"decision_id\": \"q11\",\n    \"label\": \"Sodium\
    \ resazurin\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Main batch\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000494071\",\n          \"unit\": \"G_PER_L\"\n\
    \        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000494071\",\n          \"unit\": \"G_PER_L\"\n\
    \        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000494071\",\n          \"unit\": \"G_PER_L\"\n\
    \        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table: exact named row\",\n      \
    \  \"exact_source_quote\": \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"\
    snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Page1 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the original main amount/unit\
    \ and its source batch context. The primary lists 1000 ml water plus stock additions,\
    \ without an explicit final-volume denominator; do not authenticate the existing\
    \ G_PER_L basis by reverse-engineering its number. Preserve the explicit 0.1%\
    \ w/v stock strength and its separate volume dose. That supports a delivered mass\
    \ calculation but not the existing final concentration without a final-volume\
    \ basis.\"\n  },\n  {\n    \"decision_id\": \"q12\",\n    \"label\": \"NaHCO3\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"Main batch\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.96443\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.96443\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.96443\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table: exact named row\",\n      \
    \  \"exact_source_quote\": \"NaHCO3 3.00 g\",\n        \"snapshot_sha256\": \"\
    29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\",\n        \"\
    parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Page1 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the original main amount/unit\
    \ and its source batch context. The primary lists 1000 ml water plus stock additions,\
    \ without an explicit final-volume denominator; do not authenticate the existing\
    \ G_PER_L basis by reverse-engineering its number.\"\n  },\n  {\n    \"decision_id\"\
    : \"q13\",\n    \"label\": \"Na2S x 9 H2O\",\n    \"decision\": \"correct\",\n\
    \    \"source_stage\": \"Main batch\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[12].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.494071\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.494071\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.494071\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table: exact named row\",\n      \
    \  \"exact_source_quote\": \"Na2S x 9 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\",\n    \
    \    \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Page1 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the original main amount/unit\
    \ and its source batch context. The primary lists 1000 ml water plus stock additions,\
    \ without an explicit final-volume denominator; do not authenticate the existing\
    \ G_PER_L basis by reverse-engineering its number.\"\n  },\n  {\n    \"decision_id\"\
    : \"q14\",\n    \"label\": \"Nitrilotriacetic acid stock amount\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Modified Wolin mineral stock\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2 Modified Wolin mineral subsection: exact\
    \ row\",\n        \"exact_source_quote\": \"Nitrilotriacetic acid 1.50 g\",\n\
    \        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"This original amount is in a separately\
    \ prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate\
    \ and water basis; only the 10 ml main dose transfers. Do not sum the full stock\
    \ with main contributions.\"\n  },\n  {\n    \"decision_id\": \"q15\",\n    \"\
    label\": \"MgSO4 x 7 H2O stock amount\",\n    \"decision\": \"correct\",\n   \
    \ \"source_stage\": \"Modified Wolin mineral stock\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.40909\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.40909\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.40909\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2 Modified Wolin mineral subsection: exact\
    \ row\",\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 3.00 g\",\n        \"\
    snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"This original amount is in a separately\
    \ prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate\
    \ and water basis; only the 10 ml main dose transfers. Do not sum the full stock\
    \ with main contributions.\"\n  },\n  {\n    \"decision_id\": \"q16\",\n    \"\
    label\": \"MnSO4 x H2O stock amount\",\n    \"decision\": \"correct\",\n    \"\
    source_stage\": \"Modified Wolin mineral stock\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2 Modified Wolin mineral subsection: exact\
    \ row\",\n        \"exact_source_quote\": \"MnSO4 x H2O 0.50 g\",\n        \"\
    snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"This original amount is in a separately\
    \ prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate\
    \ and water basis; only the 10 ml main dose transfers. Do not sum the full stock\
    \ with main contributions.\"\n  },\n  {\n    \"decision_id\": \"q17\",\n    \"\
    label\": \"NaCl stock amount\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Modified Wolin mineral stock\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\",\n        \"\
    field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"18.7866\",\n          \"unit\": \"G_PER_L\"\n        }\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"18.7866\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"18.7866\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2 Modified Wolin mineral subsection: exact\
    \ row\",\n        \"exact_source_quote\": \"NaCl 1.00 g\",\n        \"snapshot_sha256\"\
    : \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\",\n    \
    \    \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"This original amount is in a separately\
    \ prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate\
    \ and water basis; only the 10 ml main dose transfers. Do not sum the full stock\
    \ with main contributions.\"\n  },\n  {\n    \"decision_id\": \"q18\",\n    \"\
    label\": \"FeSO4 x 7 H2O stock amount\",\n    \"decision\": \"correct\",\n   \
    \ \"source_stage\": \"Modified Wolin mineral stock\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2 Modified Wolin mineral subsection: exact\
    \ row\",\n        \"exact_source_quote\": \"FeSO4 x 7 H2O 0.10 g\",\n        \"\
    snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"This original amount is in a separately\
    \ prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate\
    \ and water basis; only the 10 ml main dose transfers. Do not sum the full stock\
    \ with main contributions.\"\n  },\n  {\n    \"decision_id\": \"q19\",\n    \"\
    label\": \"CoSO4 x 7 H2O stock amount\",\n    \"decision\": \"correct\",\n   \
    \ \"source_stage\": \"Modified Wolin mineral stock\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2 Modified Wolin mineral subsection: exact\
    \ row\",\n        \"exact_source_quote\": \"CoSO4 x 7 H2O 0.18 g\",\n        \"\
    snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"This original amount is in a separately\
    \ prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate\
    \ and water basis; only the 10 ml main dose transfers. Do not sum the full stock\
    \ with main contributions.\"\n  },\n  {\n    \"decision_id\": \"q20\",\n    \"\
    label\": \"CaCl2 x 2 H2O stock amount\",\n    \"decision\": \"correct\",\n   \
    \ \"source_stage\": \"Modified Wolin mineral stock\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.23834\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.23834\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.23834\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2 Modified Wolin mineral subsection: exact\
    \ row\",\n        \"exact_source_quote\": \"CaCl2 x 2 H2O 0.10 g\",\n        \"\
    snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"This original amount is in a separately\
    \ prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate\
    \ and water basis; only the 10 ml main dose transfers. Do not sum the full stock\
    \ with main contributions.\"\n  },\n  {\n    \"decision_id\": \"q21\",\n    \"\
    label\": \"ZnSO4 x 7 H2O stock amount\",\n    \"decision\": \"correct\",\n   \
    \ \"source_stage\": \"Modified Wolin mineral stock\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2 Modified Wolin mineral subsection: exact\
    \ row\",\n        \"exact_source_quote\": \"ZnSO4 x 7 H2O 0.18 g\",\n        \"\
    snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"This original amount is in a separately\
    \ prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate\
    \ and water basis; only the 10 ml main dose transfers. Do not sum the full stock\
    \ with main contributions.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n    \"\
    label\": \"CuSO4 x 5 H2O stock amount\",\n    \"decision\": \"correct\",\n   \
    \ \"source_stage\": \"Modified Wolin mineral stock\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2 Modified Wolin mineral subsection: exact\
    \ row\",\n        \"exact_source_quote\": \"CuSO4 x 5 H2O 0.01 g\",\n        \"\
    snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"This original amount is in a separately\
    \ prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate\
    \ and water basis; only the 10 ml main dose transfers. Do not sum the full stock\
    \ with main contributions.\"\n  },\n  {\n    \"decision_id\": \"q23\",\n    \"\
    label\": \"AlK(SO4)2 x 12 H2O stock amount\",\n    \"decision\": \"correct\",\n\
    \    \"source_stage\": \"Modified Wolin mineral stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2 Modified Wolin mineral subsection: exact\
    \ row\",\n        \"exact_source_quote\": \"AlK(SO4)2 x 12 H2O 0.02 g\",\n   \
    \     \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"This original amount is in a separately\
    \ prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate\
    \ and water basis; only the 10 ml main dose transfers. Do not sum the full stock\
    \ with main contributions.\"\n  },\n  {\n    \"decision_id\": \"q24\",\n    \"\
    label\": \"H3BO3 stock amount\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Modified Wolin mineral stock\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\",\n        \"\
    field_path\": \"ingredients[20].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n        }\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2 Modified Wolin mineral subsection: exact\
    \ row\",\n        \"exact_source_quote\": \"H3BO3 0.01 g\",\n        \"snapshot_sha256\"\
    : \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\",\n    \
    \    \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"This original amount is in a separately\
    \ prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate\
    \ and water basis; only the 10 ml main dose transfers. Do not sum the full stock\
    \ with main contributions.\"\n  },\n  {\n    \"decision_id\": \"q25\",\n    \"\
    label\": \"Na2MoO4 x 2 H2O stock amount\",\n    \"decision\": \"correct\",\n \
    \   \"source_stage\": \"Modified Wolin mineral stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2 Modified Wolin mineral subsection: exact\
    \ row\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 0.01 g\",\n      \
    \  \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"This original amount is in a separately\
    \ prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate\
    \ and water basis; only the 10 ml main dose transfers. Do not sum the full stock\
    \ with main contributions.\"\n  },\n  {\n    \"decision_id\": \"q26\",\n    \"\
    label\": \"NiCl2 x 6 H2O stock amount\",\n    \"decision\": \"correct\",\n   \
    \ \"source_stage\": \"Modified Wolin mineral stock\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2 Modified Wolin mineral subsection: exact\
    \ row\",\n        \"exact_source_quote\": \"NiCl2 x 6 H2O 0.03 g\",\n        \"\
    snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"This original amount is in a separately\
    \ prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate\
    \ and water basis; only the 10 ml main dose transfers. Do not sum the full stock\
    \ with main contributions.\"\n  },\n  {\n    \"decision_id\": \"q27\",\n    \"\
    label\": \"Na2SeO3 x 5 H2O stock amount\",\n    \"decision\": \"correct\",\n \
    \   \"source_stage\": \"Modified Wolin mineral stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2 Modified Wolin mineral subsection: exact\
    \ row\",\n        \"exact_source_quote\": \"Na2SeO3 x 5 H2O 0.30 mg\",\n     \
    \   \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"This original amount is in a separately\
    \ prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate\
    \ and water basis; only the 10 ml main dose transfers. Do not sum the full stock\
    \ with main contributions.\"\n  },\n  {\n    \"decision_id\": \"q28\",\n    \"\
    label\": \"Na2WO4 x 2 H2O stock amount\",\n    \"decision\": \"correct\",\n  \
    \  \"source_stage\": \"Modified Wolin mineral stock\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0004\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0004\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0004\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2 Modified Wolin mineral subsection: exact\
    \ row\",\n        \"exact_source_quote\": \"Na2WO4 x 2 H2O 0.40 mg\",\n      \
    \  \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Modified Wolin stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"This original amount is in a separately\
    \ prepared mineral stock, not a direct main concentration. Retain its exact unit/hydrate\
    \ and water basis; only the 10 ml main dose transfers. Do not sum the full stock\
    \ with main contributions.\"\n  },\n  {\n    \"decision_id\": \"q29\",\n    \"\
    label\": \"Mineral stock dose\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"Main stock addition\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": null,\n        \"presence\": \"absent\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main table stock dose\",\n        \"exact_source_quote\"\
    : \"Modified Wolin's mineral solution 10.00 ml\",\n        \"snapshot_sha256\"\
    : \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\",\n    \
    \    \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"All layers lack solutions; represent\
    \ the exact complete stock and its 10 ml source batch dose without inventing a\
    \ per-liter denominator.\"\n  },\n  {\n    \"decision_id\": \"q30\",\n    \"label\"\
    : \"Main water\",\n    \"decision\": \"add\",\n    \"source_stage\": \"Main batch\"\
    ,\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page1 main table water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain 1000 ml main water independently\
    \ of stock preparation water; water is absent as a named ingredient.\"\n  },\n\
    \  {\n    \"decision_id\": \"q31\",\n    \"label\": \"Mineral stock water\",\n\
    \    \"decision\": \"add\",\n    \"source_stage\": \"Mineral stock\",\n    \"\
    local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Modified Wolin subsection water row\",\n    \
    \    \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\"\
    : \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\",\n    \
    \    \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain 1000 ml water within mineral\
    \ stock only; it is not another main liter or a verified measured stock volume.\"\
    \n  },\n  {\n    \"decision_id\": \"q32\",\n    \"label\": \"Unknown final volume\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"source_stage\": \"Main denominator\
    \ limit\",\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Main table\",\n        \"exact_source_quote\": \"Modified\
    \ Wolin's mineral solution 10.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Main table\",\n        \"exact_source_quote\": \"Fe(NH4)2(SO4)2\
    \ x 7 H2O (0.1% w/v) 2.00 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Main table\",\n        \"exact_source_quote\": \"Sodium\
    \ resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"The known listed liquid additions\
    \ sum to 1012.5 ml before unspecified sulfide stock volume. This sum is not a\
    \ measured final volume; a 1012 ml-like local normalization is neither a declaration\
    \ in this primary nor verified current API evidence.\"\n  },\n  {\n    \"decision_id\"\
    : \"q33\",\n    \"label\": \"Main pH\",\n    \"decision\": \"evidence_only\",\n\
    \    \"source_stage\": \"Main pH\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\",\n        \"\
    field_path\": \"ph_value\",\n        \"stored\": 6.9\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.9\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.9\n      }\n \
    \   ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz399\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"pH to 6.9\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Stored 6.9 agrees with source main\
    \ adjustment, but no attached same-layer evidence exists.\"\n  },\n  {\n    \"\
    decision_id\": \"q34\",\n    \"label\": \"Main gas mixture\",\n    \"decision\"\
    : \"add\",\n    \"source_stage\": \"Named main/stock procedure\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"80% H2\\nand 20% CO2 gas mixture\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact source preparation\
    \ quantity and its stated stage; this layer lacks preparation_steps.\"\n  },\n\
    \  {\n    \"decision_id\": \"q35\",\n    \"label\": \"Main gas mixture\",\n  \
    \  \"decision\": \"add\",\n    \"source_stage\": \"Named main/stock procedure\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"80% H2\\nand 20% CO2 gas mixture\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact source preparation\
    \ quantity and its stated stage; this layer lacks preparation_steps.\"\n  },\n\
    \  {\n    \"decision_id\": \"q36\",\n    \"label\": \"Main gas mixture\",\n  \
    \  \"decision\": \"evidence_only\",\n    \"source_stage\": \"Named main/stock\
    \ procedure\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients except bicarbonate and sulfide, then sparge medium with\
    \ 80% H2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add bicarbonate\
    \ and adjust pH to 6.9, then dispense medium under 80% H2 and 20% CO2 gas atmosphere\
    \ into serum vials (e.g., 20 ml per 100 ml bottle), seal and autoclave. Before\
    \ use reduce the medium with sodium sulfide from a sterile anoxic stock solution\
    \ prepared under 100% N2 gas.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"80% H2\\nand 20% CO2 gas mixture\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing DSMZ-owner description retains\
    \ this exact numeric preparation context without attached evidence. Do not turn\
    \ vessel example, gas ratio or overpressure into a nutrient concentration.\"\n\
    \  },\n  {\n    \"decision_id\": \"q37\",\n    \"label\": \"Sparging duration\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"Named main/stock procedure\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"30 - 45 min\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact source preparation\
    \ quantity and its stated stage; this layer lacks preparation_steps.\"\n  },\n\
    \  {\n    \"decision_id\": \"q38\",\n    \"label\": \"Sparging duration\",\n \
    \   \"decision\": \"add\",\n    \"source_stage\": \"Named main/stock procedure\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"30 - 45 min\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact source preparation\
    \ quantity and its stated stage; this layer lacks preparation_steps.\"\n  },\n\
    \  {\n    \"decision_id\": \"q39\",\n    \"label\": \"Sparging duration\",\n \
    \   \"decision\": \"evidence_only\",\n    \"source_stage\": \"Named main/stock\
    \ procedure\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients except bicarbonate and sulfide, then sparge medium with\
    \ 80% H2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add bicarbonate\
    \ and adjust pH to 6.9, then dispense medium under 80% H2 and 20% CO2 gas atmosphere\
    \ into serum vials (e.g., 20 ml per 100 ml bottle), seal and autoclave. Before\
    \ use reduce the medium with sodium sulfide from a sterile anoxic stock solution\
    \ prepared under 100% N2 gas.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"30 - 45 min\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing DSMZ-owner description retains\
    \ this exact numeric preparation context without attached evidence. Do not turn\
    \ vessel example, gas ratio or overpressure into a nutrient concentration.\"\n\
    \  },\n  {\n    \"decision_id\": \"q40\",\n    \"label\": \"Dispensing atmosphere\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"Named main/stock procedure\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"80% H2 and 20% CO2 gas atmosphere\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact source preparation\
    \ quantity and its stated stage; this layer lacks preparation_steps.\"\n  },\n\
    \  {\n    \"decision_id\": \"q41\",\n    \"label\": \"Dispensing atmosphere\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"Named main/stock procedure\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"80% H2 and 20% CO2 gas atmosphere\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact source preparation\
    \ quantity and its stated stage; this layer lacks preparation_steps.\"\n  },\n\
    \  {\n    \"decision_id\": \"q42\",\n    \"label\": \"Dispensing atmosphere\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"source_stage\": \"Named main/stock\
    \ procedure\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients except bicarbonate and sulfide, then sparge medium with\
    \ 80% H2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add bicarbonate\
    \ and adjust pH to 6.9, then dispense medium under 80% H2 and 20% CO2 gas atmosphere\
    \ into serum vials (e.g., 20 ml per 100 ml bottle), seal and autoclave. Before\
    \ use reduce the medium with sodium sulfide from a sterile anoxic stock solution\
    \ prepared under 100% N2 gas.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"80% H2 and 20% CO2 gas atmosphere\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing DSMZ-owner description retains\
    \ this exact numeric preparation context without attached evidence. Do not turn\
    \ vessel example, gas ratio or overpressure into a nutrient concentration.\"\n\
    \  },\n  {\n    \"decision_id\": \"q43\",\n    \"label\": \"Vessel example\",\n\
    \    \"decision\": \"add\",\n    \"source_stage\": \"Named main/stock procedure\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"20 ml per 100 ml bottle\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact source preparation\
    \ quantity and its stated stage; this layer lacks preparation_steps.\"\n  },\n\
    \  {\n    \"decision_id\": \"q44\",\n    \"label\": \"Vessel example\",\n    \"\
    decision\": \"add\",\n    \"source_stage\": \"Named main/stock procedure\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"20 ml per 100 ml bottle\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact source preparation\
    \ quantity and its stated stage; this layer lacks preparation_steps.\"\n  },\n\
    \  {\n    \"decision_id\": \"q45\",\n    \"label\": \"Vessel example\",\n    \"\
    decision\": \"evidence_only\",\n    \"source_stage\": \"Named main/stock procedure\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients except bicarbonate and sulfide, then sparge medium with\
    \ 80% H2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add bicarbonate\
    \ and adjust pH to 6.9, then dispense medium under 80% H2 and 20% CO2 gas atmosphere\
    \ into serum vials (e.g., 20 ml per 100 ml bottle), seal and autoclave. Before\
    \ use reduce the medium with sodium sulfide from a sterile anoxic stock solution\
    \ prepared under 100% N2 gas.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"20 ml per 100 ml bottle\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing DSMZ-owner description retains\
    \ this exact numeric preparation context without attached evidence. Do not turn\
    \ vessel example, gas ratio or overpressure into a nutrient concentration.\"\n\
    \  },\n  {\n    \"decision_id\": \"q46\",\n    \"label\": \"Sulfide-stock atmosphere\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"Named main/stock procedure\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"100% N2 gas\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact source preparation\
    \ quantity and its stated stage; this layer lacks preparation_steps.\"\n  },\n\
    \  {\n    \"decision_id\": \"q47\",\n    \"label\": \"Sulfide-stock atmosphere\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"Named main/stock procedure\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"100% N2 gas\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact source preparation\
    \ quantity and its stated stage; this layer lacks preparation_steps.\"\n  },\n\
    \  {\n    \"decision_id\": \"q48\",\n    \"label\": \"Sulfide-stock atmosphere\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"source_stage\": \"Named main/stock\
    \ procedure\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients except bicarbonate and sulfide, then sparge medium with\
    \ 80% H2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add bicarbonate\
    \ and adjust pH to 6.9, then dispense medium under 80% H2 and 20% CO2 gas atmosphere\
    \ into serum vials (e.g., 20 ml per 100 ml bottle), seal and autoclave. Before\
    \ use reduce the medium with sodium sulfide from a sterile anoxic stock solution\
    \ prepared under 100% N2 gas.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"100% N2 gas\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing DSMZ-owner description retains\
    \ this exact numeric preparation context without attached evidence. Do not turn\
    \ vessel example, gas ratio or overpressure into a nutrient concentration.\"\n\
    \  },\n  {\n    \"decision_id\": \"q49\",\n    \"label\": \"Overpressure and gas\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"Named main/stock procedure\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation2\",\n        \"exact_source_quote\"\
    : \"2 bar overpressure of sterile 80% H2 and 20% CO2 gas mixture.\",\n       \
    \ \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact source preparation\
    \ quantity and its stated stage; this layer lacks preparation_steps.\"\n  },\n\
    \  {\n    \"decision_id\": \"q50\",\n    \"label\": \"Overpressure and gas\",\n\
    \    \"decision\": \"add\",\n    \"source_stage\": \"Named main/stock procedure\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation2\",\n        \"exact_source_quote\"\
    : \"2 bar overpressure of sterile 80% H2 and 20% CO2 gas mixture.\",\n       \
    \ \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact source preparation\
    \ quantity and its stated stage; this layer lacks preparation_steps.\"\n  },\n\
    \  {\n    \"decision_id\": \"q51\",\n    \"label\": \"Overpressure and gas\",\n\
    \    \"decision\": \"evidence_only\",\n    \"source_stage\": \"Named main/stock\
    \ procedure\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"After inoculation, add 2 bar overpressure of sterile 80% H2 and 20% CO2 gas\
    \ mixture.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation2\",\n        \"exact_source_quote\"\
    : \"2 bar overpressure of sterile 80% H2 and 20% CO2 gas mixture.\",\n       \
    \ \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing DSMZ-owner description retains\
    \ this exact numeric preparation context without attached evidence. Do not turn\
    \ vessel example, gas ratio or overpressure into a nutrient concentration.\"\n\
    \  },\n  {\n    \"decision_id\": \"q52\",\n    \"label\": \"Initial mineral pH\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"Mineral stock\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page2 mineral preparation\",\n        \"exact_source_quote\"\
    : \"adjust pH to 6.5 with KOH\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Add only within mineral stock, not\
    \ as main-medium pH.\"\n  },\n  {\n    \"decision_id\": \"q53\",\n    \"label\"\
    : \"Initial mineral pH\",\n    \"decision\": \"add\",\n    \"source_stage\": \"\
    Mineral stock\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page2 mineral preparation\",\n        \"exact_source_quote\"\
    : \"adjust pH to 6.5 with KOH\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Add only within mineral stock, not\
    \ as main-medium pH.\"\n  },\n  {\n    \"decision_id\": \"q54\",\n    \"label\"\
    : \"Initial mineral pH\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Mineral stock\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/archaeoglobus_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[2].description\",\n        \"stored\": \"First dissolve\
    \ nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust\
    \ final to pH 7.0 with KOH.\"\n      }\n    ],\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page2 mineral preparation\",\n        \"exact_source_quote\"\
    : \"adjust pH to 6.5 with KOH\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"The numeric text is retained but\
    \ needs explicit mineral-stock scope; it is not a main-medium pH step.\"\n  },\n\
    \  {\n    \"decision_id\": \"q55\",\n    \"label\": \"Final mineral pH\",\n  \
    \  \"decision\": \"add\",\n    \"source_stage\": \"Mineral stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page2 mineral preparation\",\n        \"exact_source_quote\"\
    : \"final to pH 7.0 with KOH.\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Add only within mineral stock, not\
    \ as main-medium pH.\"\n  },\n  {\n    \"decision_id\": \"q56\",\n    \"label\"\
    : \"Final mineral pH\",\n    \"decision\": \"add\",\n    \"source_stage\": \"\
    Mineral stock\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page2 mineral preparation\",\n        \"exact_source_quote\"\
    : \"final to pH 7.0 with KOH.\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Add only within mineral stock, not\
    \ as main-medium pH.\"\n  },\n  {\n    \"decision_id\": \"q57\",\n    \"label\"\
    : \"Final mineral pH\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Mineral stock\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/archaeoglobus_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[2].description\",\n        \"stored\": \"First dissolve\
    \ nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust\
    \ final to pH 7.0 with KOH.\"\n      }\n    ],\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Page2 mineral preparation\",\n        \"exact_source_quote\"\
    : \"final to pH 7.0 with KOH.\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"The numeric text is retained but\
    \ needs explicit mineral-stock scope; it is not a main-medium pH step.\"\n  },\n\
    \  {\n    \"decision_id\": \"q58\",\n    \"label\": \"KOH strength and dose\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"source_stage\": \"Mineral stock\"\
    ,\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Mineral stock initial adjustment\",\n       \
    \ \"exact_source_quote\": \"adjust pH to 6.5 with KOH\",\n        \"snapshot_sha256\"\
    : \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\",\n    \
    \    \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      },\n      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\",\n    \
    \    \"source_locator\": \"Mineral stock final adjustment\",\n        \"exact_source_quote\"\
    : \"final to pH 7.0 with KOH.\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Neither acid/base amount nor concentration\
    \ follows from the pH targets; do not guess.\"\n  },\n  {\n    \"decision_id\"\
    : \"q59\",\n    \"label\": \"Late sulfide stock strength and volume\",\n    \"\
    decision\": \"not_quantified\",\n    \"source_stage\": \"Sulfide stock\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.494071\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.494071\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.494071\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"with sodium sulfide from a sterile anoxic stock solution prepared under 100%\
    \ N2 gas.\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"The source gives a main sulfide mass\
    \ but no separate stock strength or volume dose; retain the distinct late-addition\
    \ step.\"\n  },\n  {\n    \"decision_id\": \"q60\",\n    \"label\": \"Sterilization\
    \ method and absent cycle\",\n    \"decision\": \"not_quantified\",\n    \"source_stage\"\
    : \"Main preparation\",\n    \"local_fields\": [],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz399\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf\"\
    ,\n        \"source_locator\": \"Main preparation1\",\n        \"exact_source_quote\"\
    : \"seal and autoclave.\",\n        \"snapshot_sha256\": \"29f9f4df24231ba04f8113f3f7b6d8fd82b186c000608627ad02905808ae7ed0\"\
    ,\n        \"parsed_text_sha256\": \"4609acb3cfe2a07415faee2cf9efb50f0530aacaf6eb95951b4e5c06354abb22\"\
    \n      }\n    ],\n    \"interpretation\": \"Autoclaving is explicit, but no cycle\
    \ time/temperature is supplied. Restore the method where absent and retain unknown\
    \ cycle numbers rather than borrowing defaults.\"\n  }\n]"
- assessment_id: ownership
  area: ownership
  topic: Two maintained owners and generated boundary
  outcome: supported
  summary: Both exact archaea owners own future correction. Complete source bytes
    and their different preparation/history fields were compared; the target must
    be regenerated only after maintained-input repair. No recipe, history or generated
    artifact was changed.
  target_ids:
  - CultureMech:005188
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - writer-0
  - writer-1
  - writer-2
findings:
- finding_id: f1
  issue_key: cm005188-stocks-sums
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Full-stock concentrations and main ingredients have been combined
  description: Modified Wolin constituents remain flat in all three layers; magnesium
    sulfate 6.40909, calcium chloride 0.23834 and sodium chloride 18.7866 sum main
    values with undiluted stock strengths. The exact 10 ml stock dose and both water
    contexts are missing. Existing normalized main numbers cannot establish their
    own denominator.
  target_ids:
  - CultureMech:005188
  field_paths:
  - ingredients[*].concentration
  - ingredients[2].notes
  - ingredients[4].notes
  - ingredients[6].notes
  - solutions
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - mineral
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P1
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: cm005188-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydrate and resazurin salt are misgrounded
  description: NiCl2 hexahydrate is assigned anhydrous nickel dichloride; sodium resazurin
    is assigned the neutral molecule. Canonical labels and current MIM membership
    do not resolve these supplied-form mismatches.
  target_ids:
  - CultureMech:005188
  field_paths:
  - ingredients[22].term
  - ingredients[22].mediaingredientmech_chebi_term
  - ingredients[10].term
  evidence_ids:
  - primary
  - mineral
  - chebi34887
  - chebi8806
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: cm005188-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated and KOMODO layers omit source preparation
  description: DSMZ owner retains gas ratios, timing, vessel example, late sulfide,
    2 bar overpressure and pH instructions; target and KOMODO owner omit them. Mineral
    initial pH 6.5 and final 7.0 also require explicit stock placement in the DSMZ
    owner.
  target_ids:
  - CultureMech:005188
  field_paths:
  - preparation_steps
  - solutions
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: cm005188-broken-relations
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Both relation directions name absent bacterial paths
  description: Target/KOMODO parent points to bacterial/archaeoglobus_medium.yaml;
    DSMZ child points to bacterial/KOMODO_399_ARCHAEOGLOBUS_medium.yaml. Ignored-inclusive
    exact stable-ID search resolves both owners under archaea instead. This path defect
    is distinct from historical source-equivalence uncertainty.
  target_ids:
  - CultureMech:005188
  field_paths:
  - parent_media.path
  - variant_children[0].path
  evidence_ids:
  - relations
  - record
  - owner-0
  - owner-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: cm005188-evidence-history
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Source claims lack attachments and historical timestamps need qualification
  description: No main/stock/preparation claim has attached evidence. KOMODO and target
    each retain a malformed timestamp and a timezone-naive event; their copied-source
    history cannot authenticate current API payloads. Preserve those historical bytes
    and qualify them separately.
  target_ids:
  - CultureMech:005188
  field_paths:
  - ingredients[*].evidence
  - curation_history
  - variant_modifications
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - history-metadata
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Reconstruct the full mineral stock and its dose, split contributions
    and retain original main amounts/stock units and water stages. Resolve volume
    evidence before asserting final concentrations.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:005188
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_medium.yaml
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
  description: Use exact source and structural evidence to reconcile salt/hydrate
    grounding without guessed IDs or unsupported molecular-weight conversions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:005188
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_medium.yaml
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
  description: Preserve exact source preparation in maintained contributors and ensure
    regenerated target retains it, with stock pH separate from main 6.9 and unknown
    cycle numbers left unresolved.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:005188
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_medium.yaml
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
  description: Correct maintained locators only after exact ID verification, recheck
    both directions and preserve the evidence scope of SOURCE_DUPLICATE rather than
    treating a signature as historical proof.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:005188
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_medium.yaml
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
  description: Attach narrow exact-source evidence after correction, append rather
    than rewrite historical clarification, and distinguish source linkage from historical
    byte equivalence.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:005188
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_399_ARCHAEOGLOBUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_medium.yaml
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
- Optional mediadive399api request returned 503. Current base formulation can be assessed
  from the exact catalogue link and primary sources; historical byte equivalence and
  a distinct KOMODO variant are not inferred.
- Optional komodo399detail request returned 403. Current base formulation can be assessed
  from the exact catalogue link and primary sources; historical byte equivalence and
  a distinct KOMODO variant are not inferred.
- Optional komodo399actual request returned 403. Current base formulation can be assessed
  from the exact catalogue link and primary sources; historical byte equivalence and
  a distinct KOMODO variant are not inferred.
- Optional mediadive399retry request returned 503. Current base formulation can be
  assessed from the exact catalogue link and primary sources; historical byte equivalence
  and a distinct KOMODO variant are not inferred.
- No required identifier remains unresolved in this bounded current-source review.
  Parent DSMZ141 transfers only the named mineral subsection and its pH, not parent
  vitamins, basal medium, organisms or other conditions. All source batch quantities
  remain separate from unknown measured final volume and current API normalization.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-030
- generated-medium
```
