# Source and formulation review: bn3_medium (CultureMech:009817)

- Review: 20261022T012507Z-culturemech-009817-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-22T01:04:30Z
- Finished UTC: 2026-10-22T01:25:07Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

BN3 retains a flattened transcription of the main batch and three separate stock preparations. Resazurin mg, vitamin B12 µg, trace-stock mg and liquid doses were stored as g/L; mixed water and empty stock wrappers obscure the stages. JCM431 and TOGO agree on the quantities and anaerobic preparation. The M190 vitamin dependency is correctly identified with JCM197 and already preserves batch-only evidence. Cobalt/nickel hydrate mappings and the unresolved historical legacy sulfur link require separate curation. Review is partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 439; batch 044 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-three task batches contain 430 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 433 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009817 | data/merge_yaml/merged/BN3_MEDIUM.yaml | generated | bn3_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009817 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009817 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch044/439/strict.tsv |
| validate-terms | passed | True | CultureMech:009817 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009817 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009817 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Historical MediaIngredientMech:001072 correspondence | unavailable | True | CultureMech:009817 | Current-negative index/catalogue/tree lookup completed; historical identity evidence is not available in the bound captures. No historical invalidity or replacement is inferred. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009817.

The four documented recipes completed; interpret the scope of each separately.

### Exact TOGO M431 owner and scoped vitamin dependency

identity: supported. Targets: CultureMech:009817.

The generated target has exactly one maintained owner, TOGO_M431_BN3_Medium.yaml, with identical scientific quantities. The separate normalized bn3_medium.yaml is excluded from merge ownership. The M190 vitamin stock is a dependency, not a second owner, and JCM197 is its correct source identity.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:009817.

26 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 26/30 primary and 11/30 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 30: primary 86.67%; secondary 36.67%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Source chemical forms versus asserted concepts

grounding: concern. Targets: CultureMech:009817.

Primary and provider explicitly name cobalt chloride hexahydrate and nickel chloride hexahydrate; target/owner CHEBI35696 and CHEBI34887 describe anhydrous chlorides despite correct canonical labels. The other named sulfide, magnesium/calcium/manganese/copper chloride, iron/zinc sulfate, molybdate, selenite and tungstate hydrates match their asserted concepts. Resazurin is unqualified here, so no sodium-salt mismatch is inferred. Unqualified glucose, sulfur, bicarbonate and simple salts are compatible; undefined BD-Difco extracts are not assigned invented pure identities. The ten scoped vitamin-stock concepts were separately checked: hydrochloride names are preserved, calcium pantothenate has D-specific synonym/structure but no contrary source stereochemistry, and lipoic acid CHEBI16494 is stereo-unspecified. Valid label/index correspondence is not chemical-form evidence.

### Historical sulfur secondary identity

grounding: unknown. Targets: CultureMech:009817.

The active target and TOGO owner sulfur row asserts MediaIngredientMech:001072. The pinned current index, catalogue and tree have no exact match. Historical validity and migration remain unresolved; CHEBI33403 sulfur is a separate asserted primary identifier, not proof of legacy equivalence.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009817.

27 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Source-specific reduction, gas and sterilization sequence

completeness: concern. Targets: CultureMech:009817.

Both selected layers lack preparation steps and pH, although the exact source specifies basal/trace/SeW/resazurin autoclaving under N2–CO2 4:1 v/v; separately autoclaved glucose/yeast/tryptone stocks; filter-sterilized vitamins and bicarbonate; sulfur steaming; butyl-stopper distribution; and N2-autoclaved sulfide reduction before inoculation. All percent bases remain unknown. The current high_metal annotation is not established by flattened stock concentrations. No strain growth, culture temperature, pressure or incubation time is claimed.

### Attached dependency evidence and historical reports

evidence: supported. Targets: CultureMech:009817.

All eleven transferred M190 vitamin batch claims have exact matching cited raw bytes and literal snippets. The source was later captured with distinct actual access times; no historical retrieval timestamp is fabricated. The excluded M190 sulfide quotation has exact recovered cited JCM197 raw but nonliteral formatted snippet, and remains outside vitamin transfer. October inventory reports performed no source checks; the September report is derivative context only.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009817.

53 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "name": "Resazurin",
    "stage": "Main receiving batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 0.5,
      "unit": "mg",
      "stage": "Main receiving batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 0, row 10 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Resazurin                                               ",
          " 0.5    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Resazurin\",\n          \"volume\": 0.5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. Resazurin is 0.5 mg = 0.0005 g per printed receiving batch, not 0.5 g; the milligram correction is separate from the unresolved final-volume denominator. Exact batch unit conversion is 0.5 mg = 0.0005 g, before any unsupported stock dilution."
  },
  {
    "decision_id": "q2",
    "name": "Na2S・9H2O",
    "stage": "Main receiving batch",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.36",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.36",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 0.36,
      "unit": "g",
      "stage": "Main receiving batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 0, row 11 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Na2S·9H2O                                   ",
          " 0.36   ",
          " g  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2S・9H2O\",\n          \"volume\": 0.36,\n          \"unit\": \"g\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "The primary and provider agree on the printed main-batch mass. The local g/L denominator is not established: 1 L basal medium plus supplements is not a measured final volume. No attached quantity evidence is present."
  },
  {
    "decision_id": "q3",
    "name": "NaHCO3",
    "stage": "Main receiving batch",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "3.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "3.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 3.4,
      "unit": "g",
      "stage": "Main receiving batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 0, row 9 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " NaHCO3 ",
          " 3.4    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"NaHCO3\",\n          \"volume\": 3.4,\n          \"unit\": \"g\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "The primary and provider agree on the printed main-batch mass. The local g/L denominator is not established: 1 L basal medium plus supplements is not a measured final volume. No attached quantity evidence is present."
  },
  {
    "decision_id": "q4",
    "name": "Vitamin B12",
    "stage": "Main receiving batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 5,
      "unit": "ug",
      "stage": "Main receiving batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 0, row 4 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Vitamin B12 ",
          " 5.0    ",
          " µg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"Vitamin B12\",\n          \"volume\": 5,\n          \"unit\": \"ug\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. Main B12 is 5 µg = 0.000005 g per printed batch, not 5 g. This is separate from B12 in the vitamin stock; their delivered contributions must not be silently combined."
  },
  {
    "decision_id": "q5",
    "name": "Sulfur (powder)",
    "stage": "Main receiving batch",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 20,
      "unit": "g",
      "stage": "Main receiving batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 0, row 8 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Sulfur (powder)                                        ",
          " 20.0    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"Sulfur (powder)\",\n          \"volume\": 20,\n          \"unit\": \"g\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "The primary and provider agree on the printed main-batch mass. The local g/L denominator is not established: 1 L basal medium plus supplements is not a measured final volume. No attached quantity evidence is present."
  },
  {
    "decision_id": "q6",
    "name": "Glucose",
    "stage": "Main receiving batch",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "3.6",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "3.6",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 3.6,
      "unit": "g",
      "stage": "Main receiving batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 0, row 5 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Glucose                                                 ",
          " 3.6    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"Glucose\",\n          \"volume\": 3.6,\n          \"unit\": \"g\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "The primary and provider agree on the printed main-batch mass. The local g/L denominator is not established: 1 L basal medium plus supplements is not a measured final volume. No attached quantity evidence is present."
  },
  {
    "decision_id": "q7",
    "name": "Yeast extract (BD-Difco)",
    "stage": "Main receiving batch",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 0.5,
      "unit": "g",
      "stage": "Main receiving batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 0, row 6 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Yeast extract (BD-Difco)                                ",
          " 0.5    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "The primary and provider agree on the printed main-batch mass. The local g/L denominator is not established: 1 L basal medium plus supplements is not a measured final volume. No attached quantity evidence is present."
  },
  {
    "decision_id": "q8",
    "name": "Tryptone (BD-Difco)",
    "stage": "Main receiving batch",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 1.5,
      "unit": "g",
      "stage": "Main receiving batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 0, row 7 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Tryptone (BD-Difco)                                     ",
          " 1.5    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"Tryptone (BD-Difco)\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "The primary and provider agree on the printed main-batch mass. The local g/L denominator is not established: 1 L basal medium plus supplements is not a measured final volume. No attached quantity evidence is present."
  },
  {
    "decision_id": "q9",
    "name": "Basal medium (see below)",
    "stage": "Main receiving batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 1,
      "unit": "L",
      "stage": "Main receiving batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 0, row 0 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Basal medium (see below)                                ",
          " 1.0    ",
          " L  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"Basal medium (see below)\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed."
  },
  {
    "decision_id": "q10",
    "name": "Carbon dioxide gas",
    "stage": "Preparation atmosphere, not a dissolved ingredient rate",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "gas_mixture": "N2:CO2 4:1",
      "basis": "v/v"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Preparation paragraph or global default; exact parsed text",
        "exact_source_quote": "(4:1, v/v)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[0].items[12]",
        "exact_source_quote": "\"component_name\": \"Carbon dioxide gas\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "The local variable token does not represent the source ratio. Preserve the explicit 4:1 v/v preparation/distribution atmosphere and the separate N2-only sulfide-stock sterilization; no dissolved concentration, pressure or culture gas flow is specified."
  },
  {
    "decision_id": "q11",
    "name": "Nitrogen gas",
    "stage": "Preparation atmosphere, not a dissolved ingredient rate",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "gas_mixture": "N2:CO2 4:1",
      "basis": "v/v"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Preparation paragraph or global default; exact parsed text",
        "exact_source_quote": "(4:1, v/v)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[0].items[13]",
        "exact_source_quote": "\"component_name\": \"Nitrogen gas\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "The local variable token does not represent the source ratio. Preserve the explicit 4:1 v/v preparation/distribution atmosphere and the separate N2-only sulfide-stock sterilization; no dissolved concentration, pressure or culture gas flow is specified."
  },
  {
    "decision_id": "q12",
    "name": "Distilled water",
    "stage": "Three distinct solvent preparations incorrectly collapsed",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "989.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "989.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[11].notes",
        "stored": "Role: Solvating media; Properties: Inorganic compound, Defined component, Simple component [Merged 3 duplicates: 1.0, 987.0, 1.0]"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[11].notes",
        "stored": "Role: Solvating media; Properties: Inorganic compound, Defined component, Simple component [Merged 3 duplicates: 1.0, 987.0, 1.0]"
      }
    ],
    "desired": {
      "basal_water": {
        "value": 1,
        "unit": "L"
      },
      "trace_stock_water": {
        "value": 987,
        "unit": "ml"
      },
      "selenium_tungsten_stock_water": {
        "value": 1,
        "unit": "L"
      }
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 1, row 6 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Distilled water                                         ",
          " 1.0    ",
          " L  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 2, row 0 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Distilled water                                       ",
          " 987.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 3, row 3 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Distilled water                                         ",
          " 1.0    ",
          " L        "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      }
    ],
    "interpretation": "The local 989 g/L is accompanied by a note merging numeric values 1, 987 and 1 from different units/stages. Those three source water inputs must be restored separately; neither 989 g/L, a cross-stock volume sum, nor any final-medium volume is source-established. The note documents the local collapse but does not prove execution of a particular current writer."
  },
  {
    "decision_id": "q13",
    "name": "NaCl",
    "stage": "Basal medium preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 1,
      "unit": "g",
      "stage": "Basal medium preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 1, row 0 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " NaCl                                                    ",
          " 1.0    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. These salts belong to the separately defined basal preparation used as a 1 L input, not an independently established final-medium concentration."
  },
  {
    "decision_id": "q14",
    "name": "CaCl2・2H2O",
    "stage": "Basal medium preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.075",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.075",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 0.075,
      "unit": "g",
      "stage": "Basal medium preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 1, row 2 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " CaCl2·2H2O                                  ",
          " 0.075  ",
          " g  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.075,\n          \"unit\": \"g\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. These salts belong to the separately defined basal preparation used as a 1 L input, not an independently established final-medium concentration."
  },
  {
    "decision_id": "q15",
    "name": "KH2PO4",
    "stage": "Basal medium preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 0.2,
      "unit": "g",
      "stage": "Basal medium preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 1, row 4 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " KH2PO4 ",
          " 0.2    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. These salts belong to the separately defined basal preparation used as a 1 L input, not an independently established final-medium concentration."
  },
  {
    "decision_id": "q16",
    "name": "NH4Cl",
    "stage": "Basal medium preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 0.25,
      "unit": "g",
      "stage": "Basal medium preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 1, row 3 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " NH4Cl                                                ",
          " 0.25   ",
          " g  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 0.25,\n          \"unit\": \"g\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. These salts belong to the separately defined basal preparation used as a 1 L input, not an independently established final-medium concentration."
  },
  {
    "decision_id": "q17",
    "name": "MgCl2・6H2O",
    "stage": "Basal medium preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 0.4,
      "unit": "g",
      "stage": "Basal medium preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 1, row 1 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " MgCl2·6H2O                                  ",
          " 0.4    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.4,\n          \"unit\": \"g\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. These salts belong to the separately defined basal preparation used as a 1 L input, not an independently established final-medium concentration."
  },
  {
    "decision_id": "q18",
    "name": "KCl",
    "stage": "Basal medium preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 0.5,
      "unit": "g",
      "stage": "Basal medium preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 1, row 5 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " KCl                                                     ",
          " 0.5    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"KCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. These salts belong to the separately defined basal preparation used as a 1 L input, not an independently established final-medium concentration."
  },
  {
    "decision_id": "q19",
    "name": "25% HCl",
    "stage": "Trace element stock preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "12.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "12.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 12.5,
      "unit": "ml",
      "stage": "Trace element stock preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 2, row 1 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " 25% HCl                                               ",
          " 12.5    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"25% HCl\",\n          \"volume\": 12.5,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. Only 1 ml of this prepared stock is specified for the receiving batch. Listed solvent volumes do not establish final stock volume, so an exact 1/1000 delivered-mass fraction is not asserted. The 25% label has no stated w/v, v/v or mass-fraction basis; retain it as source text and keep the 12.5 ml liquid dose separate. No generic PERCENT enum or acid mass conversion is invented."
  },
  {
    "decision_id": "q20",
    "name": "Na2MoO4・2H2O",
    "stage": "Trace element stock preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "36",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "36",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 36,
      "unit": "mg",
      "stage": "Trace element stock preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 2, row 9 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Na2MoO4·2H2O                            ",
          " 36.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. Only 1 ml of this prepared stock is specified for the receiving batch. Listed solvent volumes do not establish final stock volume, so an exact 1/1000 delivered-mass fraction is not asserted. Exact batch unit conversion is 36 mg = 0.036 g, before any unsupported stock dilution."
  },
  {
    "decision_id": "q21",
    "name": "H3BO3",
    "stage": "Trace element stock preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 30,
      "unit": "mg",
      "stage": "Trace element stock preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 2, row 3 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " H3BO3 ",
          " 30.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 30,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. Only 1 ml of this prepared stock is specified for the receiving batch. Listed solvent volumes do not establish final stock volume, so an exact 1/1000 delivered-mass fraction is not asserted. Exact batch unit conversion is 30 mg = 0.03 g, before any unsupported stock dilution."
  },
  {
    "decision_id": "q22",
    "name": "FeSO4・7H2O",
    "stage": "Trace element stock preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "2.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "2.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 2.1,
      "unit": "g",
      "stage": "Trace element stock preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 2, row 2 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " FeSO4·7H2O                                  ",
          " 2.1    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[2].items[4]",
        "exact_source_quote": "\"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 2.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. Only 1 ml of this prepared stock is specified for the receiving batch. Listed solvent volumes do not establish final stock volume, so an exact 1/1000 delivered-mass fraction is not asserted."
  },
  {
    "decision_id": "q23",
    "name": "MnCl2・4H2O",
    "stage": "Trace element stock preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 100,
      "unit": "mg",
      "stage": "Trace element stock preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 2, row 4 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " MnCl2·4H2O                                ",
          " 100.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[2].items[5]",
        "exact_source_quote": "\"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. Only 1 ml of this prepared stock is specified for the receiving batch. Listed solvent volumes do not establish final stock volume, so an exact 1/1000 delivered-mass fraction is not asserted. Exact batch unit conversion is 100 mg = 0.1 g, before any unsupported stock dilution."
  },
  {
    "decision_id": "q24",
    "name": "CoCl2・6H2O",
    "stage": "Trace element stock preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "190",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "190",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 190,
      "unit": "mg",
      "stage": "Trace element stock preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 2, row 5 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " CoCl2·6H2O                                ",
          " 190.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[2].items[6]",
        "exact_source_quote": "\"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. Only 1 ml of this prepared stock is specified for the receiving batch. Listed solvent volumes do not establish final stock volume, so an exact 1/1000 delivered-mass fraction is not asserted. Exact batch unit conversion is 190 mg = 0.19 g, before any unsupported stock dilution."
  },
  {
    "decision_id": "q25",
    "name": "NiCl2・6H2O",
    "stage": "Trace element stock preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "24",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "24",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 24,
      "unit": "mg",
      "stage": "Trace element stock preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 2, row 6 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " NiCl2·6H2O                                 ",
          " 24.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[2].items[7]",
        "exact_source_quote": "\"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. Only 1 ml of this prepared stock is specified for the receiving batch. Listed solvent volumes do not establish final stock volume, so an exact 1/1000 delivered-mass fraction is not asserted. Exact batch unit conversion is 24 mg = 0.024 g, before any unsupported stock dilution."
  },
  {
    "decision_id": "q26",
    "name": "ZnSO4・7H2O",
    "stage": "Trace element stock preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "144",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "144",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 144,
      "unit": "mg",
      "stage": "Trace element stock preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 2, row 8 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " ZnSO4·7H2O                                ",
          " 144.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[2].items[8]",
        "exact_source_quote": "\"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 144,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. Only 1 ml of this prepared stock is specified for the receiving batch. Listed solvent volumes do not establish final stock volume, so an exact 1/1000 delivered-mass fraction is not asserted. Exact batch unit conversion is 144 mg = 0.144 g, before any unsupported stock dilution."
  },
  {
    "decision_id": "q27",
    "name": "CuCl2・2H2O",
    "stage": "Trace element stock preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 2,
      "unit": "mg",
      "stage": "Trace element stock preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 2, row 7 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " CuCl2·2H2O                                  ",
          " 2.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[2].items[9]",
        "exact_source_quote": "\"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. Only 1 ml of this prepared stock is specified for the receiving batch. Listed solvent volumes do not establish final stock volume, so an exact 1/1000 delivered-mass fraction is not asserted. Exact batch unit conversion is 2 mg = 0.002 g, before any unsupported stock dilution."
  },
  {
    "decision_id": "q28",
    "name": "Na2SeO3・5H2O",
    "stage": "Selenium/tungsten stock preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 6,
      "unit": "mg",
      "stage": "Selenium/tungsten stock preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 3, row 1 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Na2SeO3·5H2O                             ",
          " 6.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2SeO3・5H2O\",\n          \"volume\": 6,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. Only 1 ml of this prepared stock is specified for the receiving batch. Listed solvent volumes do not establish final stock volume, so an exact 1/1000 delivered-mass fraction is not asserted. Exact batch unit conversion is 6 mg = 0.006 g, before any unsupported stock dilution."
  },
  {
    "decision_id": "q29",
    "name": "Na2WO4・2H2O",
    "stage": "Selenium/tungsten stock preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "8",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "8",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 8,
      "unit": "mg",
      "stage": "Selenium/tungsten stock preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 3, row 2 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Na2WO4·2H2O                              ",
          " 8.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[3].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2WO4・2H2O\",\n          \"volume\": 8,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. Only 1 ml of this prepared stock is specified for the receiving batch. Listed solvent volumes do not establish final stock volume, so an exact 1/1000 delivered-mass fraction is not asserted. Exact batch unit conversion is 8 mg = 0.008 g, before any unsupported stock dilution."
  },
  {
    "decision_id": "q30",
    "name": "NaOH",
    "stage": "Selenium/tungsten stock preparation",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "printed_batch_amount": 0.4,
      "unit": "g",
      "stage": "Selenium/tungsten stock preparation"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 3, row 0 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " NaOH                                                    ",
          " 0.4    ",
          " g  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[3].items[3]",
        "exact_source_quote": "\"component_name\": \"NaOH\",\n          \"volume\": 0.4,\n          \"unit\": \"g\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Restore the printed unit and exact source stage shown here; the current direct-medium g/L field is not a representation of this source batch amount or stock dose. Final medium and stock volumes are not independently established, so no replacement final g/L is proposed. Only 1 ml of this prepared stock is specified for the receiving batch. Listed solvent volumes do not establish final stock volume, so an exact 1/1000 delivered-mass fraction is not asserted."
  },
  {
    "decision_id": "q31",
    "name": "Trace element solution (see below)",
    "stage": "Receiving stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "solutions[0].preferred_term",
        "stored": "Trace element solution (see below)"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "solutions[0].preferred_term",
        "stored": "Trace element solution (see below)"
      }
    ],
    "desired": {
      "batch_dose": 1,
      "unit": "ml"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 0, row 1 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Trace element solution (see below)                      ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"Trace element solution (see below)\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Both layers retain an empty Unknown solution wrapper with a mass-per-litre field. The source gives this named stock as a liquid addition. Connect only the appropriate stock composition and receiving dose; M190 is the correct JCM197 vitamin identity. Do not substitute unrelated same-name standalone stocks or invent final-volume fractions."
  },
  {
    "decision_id": "q32",
    "name": "Selenite--tungstate solution (see below)",
    "stage": "Receiving stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "solutions[1].preferred_term",
        "stored": "Selenite--tungstate solution (see below)"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "solutions[1].preferred_term",
        "stored": "Selenite--tungstate solution (see below)"
      }
    ],
    "desired": {
      "batch_dose": 1,
      "unit": "ml"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 0, row 2 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Selenite-tungstate solution (see below)                ",
          " 1.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[0].items[10]",
        "exact_source_quote": "\"component_name\": \"Selenite--tungstate solution (see below)\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Both layers retain an empty Unknown solution wrapper with a mass-per-litre field. The source gives this named stock as a liquid addition. Connect only the appropriate stock composition and receiving dose; M190 is the correct JCM197 vitamin identity. Do not substitute unrelated same-name standalone stocks or invent final-volume fractions."
  },
  {
    "decision_id": "q33",
    "name": "Trace vitamins (see Medium [M190])",
    "stage": "Receiving stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/BN3_MEDIUM.yaml",
        "field_path": "solutions[2].preferred_term",
        "stored": "Trace vitamins (see Medium [M190])"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "solutions[2].preferred_term",
        "stored": "Trace vitamins (see Medium [M190])"
      }
    ],
    "desired": {
      "batch_dose": 10,
      "unit": "ml"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 0, row 3 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " Trace vitamins (see Medium No. 197)                  ",
          " 10.0    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[0].items[11]",
        "exact_source_quote": "\"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "Both layers retain an empty Unknown solution wrapper with a mass-per-litre field. The source gives this named stock as a liquid addition. Connect only the appropriate stock composition and receiving dose; M190 is the correct JCM197 vitamin identity. Do not substitute unrelated same-name standalone stocks or invent final-volume fractions."
  },
  {
    "decision_id": "q34",
    "name": "Distilled water",
    "stage": "External M190/JCM197 trace-vitamin stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[0].evidence[0]",
        "stored": {
          "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
          "supports": "SUPPORT",
          "snippet": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\"",
          "explanation": "solutions[1].composition[0].concentration: Source water batch input: 1 L = 1 L. This is not a measured final volume. Prior duplicate-collapse notes describe the superseded flattened record. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[0]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528."
        }
      }
    ],
    "desired": {
      "preserve_batch_input": 1,
      "unit": "L"
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table 1, row 10 (zero based)",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_primary_cells": [
          " Distilled water                                         ",
          " 1.0    ",
          " L  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Verified narrowly for this existing dependent-stock batch water concentration and its attached exact raw evidence. The cited October 8 raw digest matches the separately captured raw bytes; original cited and later retrieval times remain distinct. The ten vitamin notes intentionally withdraw unsupported g/L rates. This does not verify a final stock volume, a delivered mass in BN3, or unrelated M190 parent ingredients."
  },
  {
    "decision_id": "q35",
    "name": "Biotin",
    "stage": "External M190/JCM197 trace-vitamin stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[1].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[1].evidence[0]",
        "stored": {
          "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
          "supports": "SUPPORT",
          "snippet": "{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\"",
          "explanation": "solutions[1].composition[1].concentration: Source batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[1]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528."
        }
      }
    ],
    "desired": {
      "preserve_batch_input": 2,
      "unit": "mg"
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table 1, row 0 (zero based)",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_primary_cells": [
          " Biotin                                                  ",
          " 2.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Verified narrowly for this existing dependent-stock batch amount note and its attached exact raw evidence. The cited October 8 raw digest matches the separately captured raw bytes; original cited and later retrieval times remain distinct. The ten vitamin notes intentionally withdraw unsupported g/L rates. This does not verify a final stock volume, a delivered mass in BN3, or unrelated M190 parent ingredients."
  },
  {
    "decision_id": "q36",
    "name": "p--Aminobenzoic acid",
    "stage": "External M190/JCM197 trace-vitamin stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[2].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[2].evidence[0]",
        "stored": {
          "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
          "supports": "SUPPORT",
          "snippet": "{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\"",
          "explanation": "solutions[1].composition[2].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[2]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528."
        }
      }
    ],
    "desired": {
      "preserve_batch_input": 5,
      "unit": "mg"
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table 1, row 8 (zero based)",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_primary_cells": [
          " p-Aminobenzoic acid                             ",
          " 5.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Verified narrowly for this existing dependent-stock batch amount note and its attached exact raw evidence. The cited October 8 raw digest matches the separately captured raw bytes; original cited and later retrieval times remain distinct. The ten vitamin notes intentionally withdraw unsupported g/L rates. This does not verify a final stock volume, a delivered mass in BN3, or unrelated M190 parent ingredients."
  },
  {
    "decision_id": "q37",
    "name": "Thiamine・HCl",
    "stage": "External M190/JCM197 trace-vitamin stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[3].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[3].evidence[0]",
        "stored": {
          "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
          "supports": "SUPPORT",
          "snippet": "{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\"",
          "explanation": "solutions[1].composition[3].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[3]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528."
        }
      }
    ],
    "desired": {
      "preserve_batch_input": 5,
      "unit": "mg"
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table 1, row 3 (zero based)",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_primary_cells": [
          " Thiamine·HCl                                      ",
          " 5.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Verified narrowly for this existing dependent-stock batch amount note and its attached exact raw evidence. The cited October 8 raw digest matches the separately captured raw bytes; original cited and later retrieval times remain distinct. The ten vitamin notes intentionally withdraw unsupported g/L rates. This does not verify a final stock volume, a delivered mass in BN3, or unrelated M190 parent ingredients."
  },
  {
    "decision_id": "q38",
    "name": "Calcium pantothenate",
    "stage": "External M190/JCM197 trace-vitamin stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[4].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[4].evidence[0]",
        "stored": {
          "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
          "supports": "SUPPORT",
          "snippet": "{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\"",
          "explanation": "solutions[1].composition[4].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[4]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528."
        }
      }
    ],
    "desired": {
      "preserve_batch_input": 5,
      "unit": "mg"
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table 1, row 6 (zero based)",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_primary_cells": [
          " Calcium pantothenate                                    ",
          " 5.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Verified narrowly for this existing dependent-stock batch amount note and its attached exact raw evidence. The cited October 8 raw digest matches the separately captured raw bytes; original cited and later retrieval times remain distinct. The ten vitamin notes intentionally withdraw unsupported g/L rates. This does not verify a final stock volume, a delivered mass in BN3, or unrelated M190 parent ingredients."
  },
  {
    "decision_id": "q39",
    "name": "Pyridoxine・HCl",
    "stage": "External M190/JCM197 trace-vitamin stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[5].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[5].evidence[0]",
        "stored": {
          "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
          "supports": "SUPPORT",
          "snippet": "{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\"",
          "explanation": "solutions[1].composition[5].concentration: Source batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[5]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528."
        }
      }
    ],
    "desired": {
      "preserve_batch_input": 10,
      "unit": "mg"
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table 1, row 2 (zero based)",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_primary_cells": [
          " Pyridoxine·HCl                                   ",
          " 10.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Verified narrowly for this existing dependent-stock batch amount note and its attached exact raw evidence. The cited October 8 raw digest matches the separately captured raw bytes; original cited and later retrieval times remain distinct. The ten vitamin notes intentionally withdraw unsupported g/L rates. This does not verify a final stock volume, a delivered mass in BN3, or unrelated M190 parent ingredients."
  },
  {
    "decision_id": "q40",
    "name": "Folic acid",
    "stage": "External M190/JCM197 trace-vitamin stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[6].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[6].evidence[0]",
        "stored": {
          "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
          "supports": "SUPPORT",
          "snippet": "{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\"",
          "explanation": "solutions[1].composition[6].concentration: Source batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[6]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528."
        }
      }
    ],
    "desired": {
      "preserve_batch_input": 2,
      "unit": "mg"
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table 1, row 1 (zero based)",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_primary_cells": [
          " Folic acid                                              ",
          " 2.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Verified narrowly for this existing dependent-stock batch amount note and its attached exact raw evidence. The cited October 8 raw digest matches the separately captured raw bytes; original cited and later retrieval times remain distinct. The ten vitamin notes intentionally withdraw unsupported g/L rates. This does not verify a final stock volume, a delivered mass in BN3, or unrelated M190 parent ingredients."
  },
  {
    "decision_id": "q41",
    "name": "Vitamin B12",
    "stage": "External M190/JCM197 trace-vitamin stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[7].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[7].evidence[0]",
        "stored": {
          "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
          "supports": "SUPPORT",
          "snippet": "{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\"",
          "explanation": "solutions[1].composition[7].concentration: Source batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[7]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528."
        }
      }
    ],
    "desired": {
      "preserve_batch_input": 0.1,
      "unit": "mg"
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table 1, row 7 (zero based)",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_primary_cells": [
          " Vitamin B12 ",
          " 0.1    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Verified narrowly for this existing dependent-stock batch amount note and its attached exact raw evidence. The cited October 8 raw digest matches the separately captured raw bytes; original cited and later retrieval times remain distinct. The ten vitamin notes intentionally withdraw unsupported g/L rates. This does not verify a final stock volume, a delivered mass in BN3, or unrelated M190 parent ingredients."
  },
  {
    "decision_id": "q42",
    "name": "Riboflavin",
    "stage": "External M190/JCM197 trace-vitamin stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[8].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[8].evidence[0]",
        "stored": {
          "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
          "supports": "SUPPORT",
          "snippet": "{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\"",
          "explanation": "solutions[1].composition[8].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[8]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528."
        }
      }
    ],
    "desired": {
      "preserve_batch_input": 5,
      "unit": "mg"
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table 1, row 4 (zero based)",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_primary_cells": [
          " Riboflavin                                              ",
          " 5.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Verified narrowly for this existing dependent-stock batch amount note and its attached exact raw evidence. The cited October 8 raw digest matches the separately captured raw bytes; original cited and later retrieval times remain distinct. The ten vitamin notes intentionally withdraw unsupported g/L rates. This does not verify a final stock volume, a delivered mass in BN3, or unrelated M190 parent ingredients."
  },
  {
    "decision_id": "q43",
    "name": "Nicotinic acid",
    "stage": "External M190/JCM197 trace-vitamin stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[9].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[9].evidence[0]",
        "stored": {
          "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
          "supports": "SUPPORT",
          "snippet": "{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\"",
          "explanation": "solutions[1].composition[9].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[9]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528."
        }
      }
    ],
    "desired": {
      "preserve_batch_input": 5,
      "unit": "mg"
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table 1, row 5 (zero based)",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_primary_cells": [
          " Nicotinic acid                                          ",
          " 5.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[9]",
        "exact_source_quote": "\"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Verified narrowly for this existing dependent-stock batch amount note and its attached exact raw evidence. The cited October 8 raw digest matches the separately captured raw bytes; original cited and later retrieval times remain distinct. The ten vitamin notes intentionally withdraw unsupported g/L rates. This does not verify a final stock volume, a delivered mass in BN3, or unrelated M190 parent ingredients."
  },
  {
    "decision_id": "q44",
    "name": "Lipoic acid",
    "stage": "External M190/JCM197 trace-vitamin stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[10].notes",
        "stored": "Role: Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[10].evidence[0]",
        "stored": {
          "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
          "supports": "SUPPORT",
          "snippet": "{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\"",
          "explanation": "solutions[1].composition[10].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[10]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528."
        }
      }
    ],
    "desired": {
      "preserve_batch_input": 5,
      "unit": "mg"
    },
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "HTML table 1, row 9 (zero based)",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "decoded_primary_cells": [
          " Lipoic acid                                             ",
          " 5.0    ",
          " mg  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[10]",
        "exact_source_quote": "\"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Verified narrowly for this existing dependent-stock batch amount note and its attached exact raw evidence. The cited October 8 raw digest matches the separately captured raw bytes; original cited and later retrieval times remain distinct. The ten vitamin notes intentionally withdraw unsupported g/L rates. This does not verify a final stock volume, a delivered mass in BN3, or unrelated M190 parent ingredients."
  },
  {
    "decision_id": "q45",
    "name": "Conditional pH adjustment",
    "stage": "Completed reducing preparation",
    "decision": "add",
    "local_fields": [],
    "desired": {
      "pH": 7.2,
      "condition": "readjust if necessary"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Preparation paragraph or global default; exact parsed text",
        "exact_source_quote": "Readjust pH to 7.2, if necessary.",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      }
    ],
    "interpretation": "Neither selected layer has a pH or preparation array. Add the source condition, not a measured culture pH or an unconditional preset for each separate stock."
  },
  {
    "decision_id": "q46",
    "name": "Global autoclave default",
    "stage": "Applicable autoclaved preparations unless otherwise stated",
    "decision": "add",
    "local_fields": [],
    "desired": {
      "temperature_C": 121,
      "duration_min": 15
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Preparation paragraph or global default; exact parsed text",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      }
    ],
    "interpretation": "This is the actual JCM page default. It applies only to source-designated autoclaved preparations where no exception is stated; do not apply it to filter-sterilized vitamins/bicarbonate or sulfur steaming."
  },
  {
    "decision_id": "q47",
    "name": "Glucose stock",
    "stage": "Separately prepared addition",
    "decision": "schema_gap",
    "local_fields": [],
    "desired": {
      "source_percent_text": "10%",
      "basis": "unspecified",
      "delivered_volume": "not stated"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Preparation paragraph or global default; exact parsed text",
        "exact_source_quote": "Separately autoclave glucose, yeast extract and tryptone (10% each)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      }
    ],
    "interpretation": "Preserve the exact unqualified percent. Its w/v, v/v or mass-fraction basis is not supplied, and a generic PERCENT concentration enum is unavailable. Do not infer a stock dose from the separate batch mass; record the preparation text and unresolved basis explicitly."
  },
  {
    "decision_id": "q48",
    "name": "Yeast extract stock",
    "stage": "Separately prepared addition",
    "decision": "schema_gap",
    "local_fields": [],
    "desired": {
      "source_percent_text": "10%",
      "basis": "unspecified",
      "delivered_volume": "not stated"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Preparation paragraph or global default; exact parsed text",
        "exact_source_quote": "Separately autoclave glucose, yeast extract and tryptone (10% each)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      }
    ],
    "interpretation": "Preserve the exact unqualified percent. Its w/v, v/v or mass-fraction basis is not supplied, and a generic PERCENT concentration enum is unavailable. Do not infer a stock dose from the separate batch mass; record the preparation text and unresolved basis explicitly."
  },
  {
    "decision_id": "q49",
    "name": "Tryptone stock",
    "stage": "Separately prepared addition",
    "decision": "schema_gap",
    "local_fields": [],
    "desired": {
      "source_percent_text": "10%",
      "basis": "unspecified",
      "delivered_volume": "not stated"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Preparation paragraph or global default; exact parsed text",
        "exact_source_quote": "Separately autoclave glucose, yeast extract and tryptone (10% each)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      }
    ],
    "interpretation": "Preserve the exact unqualified percent. Its w/v, v/v or mass-fraction basis is not supplied, and a generic PERCENT concentration enum is unavailable. Do not infer a stock dose from the separate batch mass; record the preparation text and unresolved basis explicitly."
  },
  {
    "decision_id": "q50",
    "name": "Bicarbonate stock",
    "stage": "Separately prepared addition",
    "decision": "schema_gap",
    "local_fields": [],
    "desired": {
      "source_percent_text": "8%",
      "basis": "unspecified",
      "delivered_volume": "not stated"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Preparation paragraph or global default; exact parsed text",
        "exact_source_quote": "(8%) solution",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      }
    ],
    "interpretation": "Preserve the exact unqualified percent. Its w/v, v/v or mass-fraction basis is not supplied, and a generic PERCENT concentration enum is unavailable. Do not infer a stock dose from the separate batch mass; record the preparation text and unresolved basis explicitly."
  },
  {
    "decision_id": "q51",
    "name": "Sulfide stock",
    "stage": "Separately prepared addition",
    "decision": "schema_gap",
    "local_fields": [],
    "desired": {
      "source_percent_text": "5%",
      "basis": "unspecified",
      "delivered_volume": "not stated"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Preparation paragraph or global default; exact parsed text",
        "exact_source_quote": "5% Na 2 S·9H 2 O solution",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      }
    ],
    "interpretation": "Preserve the exact unqualified percent. Its w/v, v/v or mass-fraction basis is not supplied, and a generic PERCENT concentration enum is unavailable. Do not infer a stock dose from the separate batch mass; record the preparation text and unresolved basis explicitly."
  },
  {
    "decision_id": "q52",
    "name": "Hydrochloric acid stock strength",
    "stage": "Trace element stock",
    "decision": "schema_gap",
    "local_fields": [],
    "desired": {
      "source_percent_text": "25%",
      "basis": "unspecified"
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "HTML table 2, row 1 (zero based)",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "decoded_primary_cells": [
          " 25% HCl                                               ",
          " 12.5    ",
          " ml  "
        ],
        "representation": "Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML substring."
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"25% HCl\",\n          \"volume\": 12.5,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "interpretation": "The source separately supplies a 12.5 ml addition of 25% HCl. The percent basis remains unspecified; no density or equivalent acid mass is inferred."
  },
  {
    "decision_id": "q53",
    "name": "Sulfur steaming",
    "stage": "Only sulfur before assembly/distribution",
    "decision": "add",
    "local_fields": [],
    "desired": {
      "duration_each_h": 3,
      "successive_days": 3
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Preparation paragraph or global default; exact parsed text",
        "exact_source_quote": "Steam sulfur for 3 hr on each of 3 successive days.",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      }
    ],
    "interpretation": "This is three hours on each of three successive days, not a culture incubation duration or three-day autoclave cycle. Steam temperature and pressure are not stated."
  }
]

## Findings

### f1: Stock recipes and solvent stages are flattened into the receiving medium

major / open / confirmed; issue key: culturemech.009817.stock-stage-and-solvent.

Basal salts, trace-stock ingredients and selenium/tungsten stock ingredients appear as direct-medium g/L fields. Water 989 g/L collapses 1 L, 987 ml and 1 L from separate preparations; empty Unknown solution wrappers retain liquid additions as g/L. No source final-volume declaration supports these rates.

### f2: Microgram and milligram source quantities are encoded as gram rates

major / open / confirmed; issue key: culturemech.009817.micro-milli-units.

Resazurin 0.5 mg and main B12 5 µg became 0.5 and 5 g/L. Nine trace/selenium-tungsten mg rows likewise retain their numeric values in g/L, in addition to the wrong stock stage. Correct batch unit arithmetic does not establish delivered final-medium rates.

### f3: Two explicitly supplied hexahydrates map to anhydrous concepts

major / open / confirmed; issue key: culturemech.009817.hydrate-identities.

Cobalt chloride hexahydrate and nickel chloride hexahydrate are explicitly supplied in the trace stock, but both selected layers assert CHEBI35696 and CHEBI34887 respectively. These are valid anhydrous concepts with matching labels, not the named source hydrates.

### f4: The required staged reducing preparation is absent

major / open / confirmed; issue key: culturemech.009817.preparation-and-conditions.

Neither selected layer represents the source gas ratio, selective sterilization, sulfur timing, reducing sequence or conditional pH 7.2. This prevents reproduction of the intended medium even after quantity corrections.

### f5: The active legacy sulfur link lacks current and historical correspondence

minor / open / confirmed; issue key: culturemech.009817.legacy-sulfur-correspondence.

MediaIngredientMech:001072 is absent from the pinned current index/catalogue/tree. This establishes a current lookup gap only; its historical identity remains unresolved.

### f6: Selected receiving ingredients and stock wrappers lack attached quantity evidence

minor / open / confirmed; issue key: culturemech.009817.receiving-claim-evidence.

The selected target and owner have no claim evidence for their 33 concentration objects. The separate repaired M190 vitamin stock already has exact batch evidence and should be credited rather than recurred as missing.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct the four source stages and exact liquid additions in the maintained TOGO owner, using only scoped M190 vitamins. Preserve original batch units and separately resolve stock/final-medium denominators before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore the exact printed mg/µg batch units and proper stocks; verify every affected local field against its individual source row. Do not use assumed final litres or bare-percent stock strengths to derive delivered amounts.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Select and independently verify the exact supplied hydrate concepts before updating the maintained owner and regenerating; do not repair only the canonical labels or infer a mass conversion.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Add only the exact source preparation stages and conditional pH, retain all unspecified percent bases, and reassess high_metal against the properly scoped delivered formulation. Do not invent culture incubation, pressure or dose denominators.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Recover exact historical identifier evidence or document the unresolved link before any authorized migration; preserve the independently asserted sulfur CHEBI concept without claiming equivalence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

After stage and unit curation, attach short exact source snippets with source hashes and locators to the appropriate receiving or stock fields; preserve the existing scoped vitamin evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BN3_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BN3_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BN3_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch044/439/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch044/439/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BN3_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BN3_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BN3_MEDIUM.yaml:1:id: CultureMech:009817<br>./data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml:1:id: CultureMech:009817<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch044/source-preflight-bound/439/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 62 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431; Entire JCM431 recipe, all four tables, preparation paragraph and global autoclave default | supports | Main batch, basal medium, trace elements and selenium/tungsten stock are separate. The page explicitly specifies a 4:1 v/v N2–CO2 gas mixture, staged sterilization, sulfur steaming and conditional pH 7.2. Listed stock water is not a final-volume declaration. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431; Full meta, components[0:4] and comments[0] | supports | TOGO identifies JCM431 and transcribes all source stages; its M190 vitamin reference resolves to JCM197. No final-volume measurement or bare-percent basis is supplied. |
| vitamins | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Trace vitamins table only; parent main medium and mineral solution excluded | supports | The named vitamin stock contains ten vitamins and 1 L listed water. Its recipe is transferred only as the stock referred to by JCM431; unrelated parent ingredients and mixed parent water are excluded. |
| vitamin-provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; meta source JCM197 and components[1] only | supports | The M190/JCM197 mapping is explicit. Exact cited raw 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528 is recovered; the maintained stock has removed unsupported final-volume rates and retained batch quantities in notes with attached evidence. |
| vitamin-owner | data/normalized_yaml/bacterial/togo_medium_m190.yaml; solutions[1].composition[0:11] and their exact attached evidence only | supports | The scoped vitamin water concentration and ten batch-amount notes were inspected. The receiving dose elsewhere in this parent does not supply BN3 authority; JCM431 independently specifies 10 ml. Other parent stocks and main ingredients are outside this review transfer. |
| report-0 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BN3_MEDIUM.md; Full exact-identity historical derivative report | context_only | Full October 5 exact-identity inventory read: 0/33 quantity rows source-checked, so it provides no independent formula support. |
| report-1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.md; Full exact-identity historical derivative report | context_only | Full October 5 exact-identity inventory read: 0/33 quantity rows source-checked, so it provides no independent formula support. |
| report-2 | reports/yaml_record_review/20260921T230801Z-BN3_MEDIUM.md; Full exact-identity historical derivative report | context_only | Full September ad hoc review read. Its stock/unit/hydrate observations were reassessed against current captures; its claimed M190/JCM197 mismatch and final g/L assumptions are not adopted. Current source identity resolves M190 to JCM197, and listed stock water does not establish final volume. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16526 resolves to carbon dioxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17234 resolves to glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33403 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33403; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33403 resolves to elemental sulfur. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:35696 resolves to cobalt dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| mimPinnedCatalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Complete pinned current object searched for exact legacy identifier MediaIngredientMech:001072 | context_only | The exact current catalogue/tree at commit 6643131b0f12ab40b66f98135245fca04027e0e9 has no MediaIngredientMech:001072. This current-negative result does not establish historical invalidity or identify a replacement. |
| mimPinnedTree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Complete pinned current object searched for exact legacy identifier MediaIngredientMech:001072 | context_only | The exact current catalogue/tree at commit 6643131b0f12ab40b66f98135245fca04027e0e9 has no MediaIngredientMech:001072. This current-negative result does not establish historical invalidity or identify a replacement. |
| history-metadata | data/merge_yaml/merged/BN3_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 14, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml", "events": 13, "timestamp_issues": []}] |
| writer-0 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The full formulation equality guard and relevant merge_group functions were read. Identical current target/owner scientific fields and historical notes do not prove that the current guarded merger executed the older flattening or unit conversion. |
| writer-1 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The full formulation equality guard and relevant merge_group functions were read. Identical current target/owner scientific fields and historical notes do not prove that the current guarded merger executed the older flattening or unit conversion. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch044/439/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Completion is partial because the active legacy sulfur identifier historical correspondence remains unresolved despite complete current-negative lookups. No new legacy network request was made.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T012507Z-culturemech-009817-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bn3_medium (CultureMech:009817)'
started_at: '2026-10-22T01:04:30Z'
finished_at: '2026-10-22T01:25:07Z'
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
summary: BN3 retains a flattened transcription of the main batch and three separate
  stock preparations. Resazurin mg, vitamin B12 µg, trace-stock mg and liquid doses
  were stored as g/L; mixed water and empty stock wrappers obscure the stages. JCM431
  and TOGO agree on the quantities and anaerobic preparation. The M190 vitamin dependency
  is correctly identified with JCM197 and already preserves batch-only evidence. Cobalt/nickel
  hydrate mappings and the unresolved historical legacy sulfur link require separate
  curation. Review is partial.
source:
  git_revision: 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
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
  - path: data/merge_yaml/merged/BN3_MEDIUM.yaml
    sha256: 79959dc8a30eddb9bdcfeec32bacf6fdea142f837826edacd10e0ddadd402619
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    sha256: 35c2b3264b82cf435135a02583fb7e004fe58bc46d6c0906db454950ea333cdc
    role: context
  - path: data/normalized_yaml/bacterial/bn3_medium.yaml
    sha256: 9713c64779e2e198171f04cb5eaf782c0423ede7348179ab59e09e93291a394d
    role: context
  - path: data/normalized_yaml/bacterial/togo_medium_m190.yaml
    sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BN3_MEDIUM.md
    sha256: fe4feab50de92089379d903e0b47e6e7a2e92dc6f4822f4f7a81297f177c8dc4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.md
    sha256: 1601590034c9aa40373c939b94267fbeddc72ae5b0f15de48f380cba97d1b965
    role: context
  - path: reports/yaml_record_review/20260921T230801Z-BN3_MEDIUM.md
    sha256: f7b264f4b7f3aa84c40ec049d8d89f48d67f8bd0cb7f723e250de0ecdc068b0a
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_jcm_missing_from_togo.py
    sha256: 3e7c9547e5fceda8ced6b556de50b6a0af17e0805be021af6b3e5a6b8eb70570
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
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
  selection: Task review 439; batch 044 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding forty-three task batches
    contain 430 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 433 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009817
targets:
- target_id: CultureMech:009817
  path: data/merge_yaml/merged/BN3_MEDIUM.yaml
  label: bn3_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BN3_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009817
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BN3_MEDIUM.yaml --workers 1
    --out /private/tmp/culturemech-review-work-batch044/439/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch044/439/strict.tsv"
  target_ids:
  - CultureMech:009817
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BN3_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009817
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BN3_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009817
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
  - CultureMech:009817
- check_id: legacy-historical-correspondence
  name: Historical MediaIngredientMech:001072 correspondence
  required: true
  status: unavailable
  summary: Current-negative index/catalogue/tree lookup completed; historical identity
    evidence is not available in the bound captures. No historical invalidity or replacement
    is inferred.
  target_ids:
  - CultureMech:009817
  evidence_ids:
  - mim
  - mimPinnedCatalog
  - mimPinnedTree
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BN3_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-22T01:22:08Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-22T01:22:08Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BN3_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T01:08:18.690981Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BN3_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch044/439/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-22T01:08:20.051769Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-044/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch044/439/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BN3_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T01:08:21.620036Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BN3_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-22T01:08:22.637467Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-22T01:22:08Z'
  support: supports
  summary: './data/merge_yaml/merged/BN3_MEDIUM.yaml:1:id: CultureMech:009817

    ./data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml:1:id: CultureMech:009817

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch044/source-preflight-bound/439/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-22T01:22:08Z'
  support: supports
  summary: 62 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 8dd614c8420d0b2ca47cc5db05f493b4cb8f870ea1e7f1fc2da03a505af1922e
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431
  locator: Entire JCM431 recipe, all four tables, preparation paragraph and global
    autoclave default
  accessed_at: '2026-10-21T12:23:19.260180Z'
  support: supports
  summary: Main batch, basal medium, trace elements and selenium/tungsten stock are
    separate. The page explicitly specifies a 4:1 v/v N2–CO2 gas mixture, staged sterilization,
    sulfur steaming and conditional pH 7.2. Listed stock water is not a final-volume
    declaration.
  snapshot_sha256: cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431
  locator: Full meta, components[0:4] and comments[0]
  accessed_at: '2026-10-21T12:23:17.822513Z'
  support: supports
  summary: TOGO identifies JCM431 and transcribes all source stages; its M190 vitamin
    reference resolves to JCM197. No final-volume measurement or bare-percent basis
    is supplied.
  snapshot_sha256: e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570
- evidence_id: vitamins
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: Trace vitamins table only; parent main medium and mineral solution excluded
  accessed_at: '2026-10-20T06:58:05.867253Z'
  support: supports
  summary: The named vitamin stock contains ten vitamins and 1 L listed water. Its
    recipe is transferred only as the stock referred to by JCM431; unrelated parent
    ingredients and mixed parent water are excluded.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: vitamin-provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  locator: meta source JCM197 and components[1] only
  accessed_at: '2026-10-21T09:28:25.418127Z'
  support: supports
  summary: The M190/JCM197 mapping is explicit. Exact cited raw 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
    is recovered; the maintained stock has removed unsupported final-volume rates
    and retained batch quantities in notes with attached evidence.
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: vitamin-owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/togo_medium_m190.yaml
  locator: solutions[1].composition[0:11] and their exact attached evidence only
  accessed_at: '2026-10-22T01:22:08Z'
  support: supports
  summary: The scoped vitamin water concentration and ten batch-amount notes were
    inspected. The receiving dose elsewhere in this parent does not supply BN3 authority;
    JCM431 independently specifies 10 ml. Other parent stocks and main ingredients
    are outside this review transfer.
  snapshot_sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
- evidence_id: report-0
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BN3_MEDIUM.md
  locator: Full exact-identity historical derivative report
  accessed_at: '2026-10-22T01:22:08Z'
  support: context_only
  summary: 'Full October 5 exact-identity inventory read: 0/33 quantity rows source-checked,
    so it provides no independent formula support.'
  snapshot_sha256: fe4feab50de92089379d903e0b47e6e7a2e92dc6f4822f4f7a81297f177c8dc4
- evidence_id: report-1
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.md
  locator: Full exact-identity historical derivative report
  accessed_at: '2026-10-22T01:22:08Z'
  support: context_only
  summary: 'Full October 5 exact-identity inventory read: 0/33 quantity rows source-checked,
    so it provides no independent formula support.'
  snapshot_sha256: 1601590034c9aa40373c939b94267fbeddc72ae5b0f15de48f380cba97d1b965
- evidence_id: report-2
  kind: record_content
  reference: reports/yaml_record_review/20260921T230801Z-BN3_MEDIUM.md
  locator: Full exact-identity historical derivative report
  accessed_at: '2026-10-22T01:22:08Z'
  support: context_only
  summary: Full September ad hoc review read. Its stock/unit/hydrate observations
    were reassessed against current captures; its claimed M190/JCM197 mismatch and
    final g/L assumptions are not adopted. Current source identity resolves M190 to
    JCM197, and listed stock water does not establish final volume.
  snapshot_sha256: f7b264f4b7f3aa84c40ec049d8d89f48d67f8bd0cb7f723e250de0ecdc068b0a
- evidence_id: chebi131361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:27.980786Z'
  support: supports
  summary: CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:30.346522Z'
  support: supports
  summary: CHEBI:15377 resolves to water. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi16526
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.337128Z'
  support: supports
  summary: CHEBI:16526 resolves to carbon dioxide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:31.535358Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi17997
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:27.385647Z'
  support: supports
  summary: CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
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
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: CHEBI:31206 resolves to ammonium chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32145
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:28.263004Z'
  support: supports
  summary: CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: CHEBI:32588 resolves to potassium chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi33403
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33403
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:26:28.748668Z'
  support: supports
  summary: CHEBI:33403 resolves to elemental sulfur. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: b349493be5d8cb371d1e71751510f9205880ab9d0a14f560191e05606c127a60
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: CHEBI:34887 resolves to nickel dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi35696
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: CHEBI:35696 resolves to cobalt dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:08.324907Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:00:48.784931Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:09.378884Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-22T01:22:08Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type":
    "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id":
    "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843":
    [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843",
    "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status":
    "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term",
    "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label":
    "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term":
    "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type":
    "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036":
    [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036",
    "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term",
    "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mimPinnedCatalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Complete pinned current object searched for exact legacy identifier MediaIngredientMech:001072
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: context_only
  summary: The exact current catalogue/tree at commit 6643131b0f12ab40b66f98135245fca04027e0e9
    has no MediaIngredientMech:001072. This current-negative result does not establish
    historical invalidity or identify a replacement.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: mimPinnedTree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Complete pinned current object searched for exact legacy identifier MediaIngredientMech:001072
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: context_only
  summary: The exact current catalogue/tree at commit 6643131b0f12ab40b66f98135245fca04027e0e9
    has no MediaIngredientMech:001072. This current-negative result does not establish
    historical invalidity or identify a replacement.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BN3_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-22T01:22:08Z'
  support: context_only
  summary: '[{"input": "target", "events": 14, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml", "events": 13, "timestamp_issues":
    []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T01:22:08Z'
  support: context_only
  summary: The full formulation equality guard and relevant merge_group functions
    were read. Identical current target/owner scientific fields and historical notes
    do not prove that the current guarded merger executed the older flattening or
    unit conversion.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-22T01:22:08Z'
  support: context_only
  summary: The full formulation equality guard and relevant merge_group functions
    were read. Identical current target/owner scientific fields and historical notes
    do not prove that the current guarded merger executed the older flattening or
    unit conversion.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch044/439/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-22T01:22:08Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 91554e3ef4c1d269bd6b7462e6eaeee2432b4b4f902b06d930bd9e5be38a67a9
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009817
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact TOGO M431 owner and scoped vitamin dependency
  outcome: supported
  summary: The generated target has exactly one maintained owner, TOGO_M431_BN3_Medium.yaml,
    with identical scientific quantities. The separate normalized bn3_medium.yaml
    is excluded from merge ownership. The M190 vitamin stock is a dependency, not
    a second owner, and JCM197 is its correct source identity.
  target_ids:
  - CultureMech:009817
  evidence_ids:
  - record
  - owner-0
  - id-search
  - primary
  - provider
  - vitamins
  - vitamin-provider
  - vitamin-owner
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '26 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 26/30
    primary and 11/30 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:009817
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131361
  - chebi15377
  - chebi16526
  - chebi17234
  - chebi176843
  - chebi17997
  - chebi26710
  - chebi31206
  - chebi32139
  - chebi32145
  - chebi32312
  - chebi32588
  - chebi33118
  - chebi33403
  - chebi34887
  - chebi35696
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi75836
  - chebi76209
  - chebi86158
  - chebi86318
  - chebi86345
  - chebi86368
  - chebi8806
  details: 'Instance coverage on a 0–100 percent scale, denominator 30: primary 86.67%;
    secondary 36.67%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: forms
  area: grounding
  topic: Source chemical forms versus asserted concepts
  outcome: concern
  summary: 'Primary and provider explicitly name cobalt chloride hexahydrate and nickel
    chloride hexahydrate; target/owner CHEBI35696 and CHEBI34887 describe anhydrous
    chlorides despite correct canonical labels. The other named sulfide, magnesium/calcium/manganese/copper
    chloride, iron/zinc sulfate, molybdate, selenite and tungstate hydrates match
    their asserted concepts. Resazurin is unqualified here, so no sodium-salt mismatch
    is inferred. Unqualified glucose, sulfur, bicarbonate and simple salts are compatible;
    undefined BD-Difco extracts are not assigned invented pure identities. The ten
    scoped vitamin-stock concepts were separately checked: hydrochloride names are
    preserved, calcium pantothenate has D-specific synonym/structure but no contrary
    source stereochemistry, and lipoic acid CHEBI16494 is stereo-unspecified. Valid
    label/index correspondence is not chemical-form evidence.'
  target_ids:
  - CultureMech:009817
  evidence_ids:
  - primary
  - provider
  - vitamins
  - vitamin-owner
  - chebi131361
  - chebi15377
  - chebi16526
  - chebi17234
  - chebi176843
  - chebi17997
  - chebi26710
  - chebi31206
  - chebi32139
  - chebi32145
  - chebi32312
  - chebi32588
  - chebi33118
  - chebi33403
  - chebi34887
  - chebi35696
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi75836
  - chebi76209
  - chebi86158
  - chebi86318
  - chebi86345
  - chebi86368
  - chebi8806
- assessment_id: legacy
  area: grounding
  topic: Historical sulfur secondary identity
  outcome: unknown
  summary: The active target and TOGO owner sulfur row asserts MediaIngredientMech:001072.
    The pinned current index, catalogue and tree have no exact match. Historical validity
    and migration remain unresolved; CHEBI33403 sulfur is a separate asserted primary
    identifier, not proof of legacy equivalence.
  target_ids:
  - CultureMech:009817
  evidence_ids:
  - record
  - owner-0
  - mim
  - mimPinnedCatalog
  - mimPinnedTree
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 27 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:009817
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: preparation
  area: completeness
  topic: Source-specific reduction, gas and sterilization sequence
  outcome: concern
  summary: Both selected layers lack preparation steps and pH, although the exact
    source specifies basal/trace/SeW/resazurin autoclaving under N2–CO2 4:1 v/v; separately
    autoclaved glucose/yeast/tryptone stocks; filter-sterilized vitamins and bicarbonate;
    sulfur steaming; butyl-stopper distribution; and N2-autoclaved sulfide reduction
    before inoculation. All percent bases remain unknown. The current high_metal annotation
    is not established by flattened stock concentrations. No strain growth, culture
    temperature, pressure or incubation time is claimed.
  target_ids:
  - CultureMech:009817
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
- assessment_id: history-auth
  area: evidence
  topic: Attached dependency evidence and historical reports
  outcome: supported
  summary: All eleven transferred M190 vitamin batch claims have exact matching cited
    raw bytes and literal snippets. The source was later captured with distinct actual
    access times; no historical retrieval timestamp is fabricated. The excluded M190
    sulfide quotation has exact recovered cited JCM197 raw but nonliteral formatted
    snippet, and remains outside vitamin transfer. October inventory reports performed
    no source checks; the September report is derivative context only.
  target_ids:
  - CultureMech:009817
  evidence_ids:
  - vitamin-owner
  - vitamin-provider
  - vitamins
  - report-0
  - report-1
  - report-2
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 53 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:009817
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"Resazurin\",\n \
    \   \"stage\": \"Main receiving batch\",\n    \"decision\": \"correct\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 0.5,\n \
    \     \"unit\": \"mg\",\n      \"stage\": \"Main receiving batch\"\n    },\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\",\n   \
    \     \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 0, row 10 (zero based)\",\n      \
    \  \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Resazurin              \
    \                                 \",\n          \" 0.5    \",\n          \" mg\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Resazurin\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. Resazurin\
    \ is 0.5 mg = 0.0005 g per printed receiving batch, not 0.5 g; the milligram correction\
    \ is separate from the unresolved final-volume denominator. Exact batch unit conversion\
    \ is 0.5 mg = 0.0005 g, before any unsupported stock dilution.\"\n  },\n  {\n\
    \    \"decision_id\": \"q2\",\n    \"name\": \"Na2S・9H2O\",\n    \"stage\": \"\
    Main receiving batch\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.36\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.36\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 0.36,\n\
    \      \"unit\": \"g\",\n      \"stage\": \"Main receiving batch\"\n    },\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\",\n   \
    \     \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 0, row 11 (zero based)\",\n      \
    \  \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Na2S·9H2O              \
    \                     \",\n          \" 0.36   \",\n          \" g  \"\n     \
    \   ],\n        \"representation\": \"Exact decoded DOM cells independently rejoined\
    \ to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n      \
    \  \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2S・9H2O\\\",\\n          \\\"volume\\\": 0.36,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary and provider agree on\
    \ the printed main-batch mass. The local g/L denominator is not established: 1\
    \ L basal medium plus supplements is not a measured final volume. No attached\
    \ quantity evidence is present.\"\n  },\n  {\n    \"decision_id\": \"q3\",\n \
    \   \"name\": \"NaHCO3\",\n    \"stage\": \"Main receiving batch\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 3.4,\n \
    \     \"unit\": \"g\",\n      \"stage\": \"Main receiving batch\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 0, row 9 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" NaHCO3 \",\n          \"\
     3.4    \",\n          \" g  \"\n        ],\n        \"representation\": \"Exact\
    \ decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML\
    \ substring.\"\n      },\n      {\n        \"source_key\": \"togoM431original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaHCO3\\\",\\n          \\\"volume\\\": 3.4,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary and provider agree on\
    \ the printed main-batch mass. The local g/L denominator is not established: 1\
    \ L basal medium plus supplements is not a measured final volume. No attached\
    \ quantity evidence is present.\"\n  },\n  {\n    \"decision_id\": \"q4\",\n \
    \   \"name\": \"Vitamin B12\",\n    \"stage\": \"Main receiving batch\",\n   \
    \ \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 5,\n   \
    \   \"unit\": \"ug\",\n      \"stage\": \"Main receiving batch\"\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 0, row 4 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Vitamin B12 \",\n      \
    \    \" 5.0    \",\n          \" µg  \"\n        ],\n        \"representation\"\
    : \"Exact decoded DOM cells independently rejoined to raw HTML; not claimed as\
    \ an HTML substring.\"\n      },\n      {\n        \"source_key\": \"togoM431original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin B12\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"ug\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. Main\
    \ B12 is 5 µg = 0.000005 g per printed batch, not 5 g. This is separate from B12\
    \ in the vitamin stock; their delivered contributions must not be silently combined.\"\
    \n  },\n  {\n    \"decision_id\": \"q5\",\n    \"name\": \"Sulfur (powder)\",\n\
    \    \"stage\": \"Main receiving batch\",\n    \"decision\": \"unsupported\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 20,\n  \
    \    \"unit\": \"g\",\n      \"stage\": \"Main receiving batch\"\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 0, row 8 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Sulfur (powder)        \
    \                                \",\n          \" 20.0    \",\n          \" g\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Sulfur (powder)\\\",\\n          \\\"volume\\\"\
    : 20,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\n      }\n\
    \    ],\n    \"interpretation\": \"The primary and provider agree on the printed\
    \ main-batch mass. The local g/L denominator is not established: 1 L basal medium\
    \ plus supplements is not a measured final volume. No attached quantity evidence\
    \ is present.\"\n  },\n  {\n    \"decision_id\": \"q6\",\n    \"name\": \"Glucose\"\
    ,\n    \"stage\": \"Main receiving batch\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 3.6,\n \
    \     \"unit\": \"g\",\n      \"stage\": \"Main receiving batch\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 0, row 5 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Glucose                \
    \                                 \",\n          \" 3.6    \",\n          \" g\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Glucose\\\",\\n          \\\"volume\\\": 3.6,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"The primary and provider agree on\
    \ the printed main-batch mass. The local g/L denominator is not established: 1\
    \ L basal medium plus supplements is not a measured final volume. No attached\
    \ quantity evidence is present.\"\n  },\n  {\n    \"decision_id\": \"q7\",\n \
    \   \"name\": \"Yeast extract (BD-Difco)\",\n    \"stage\": \"Main receiving batch\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 0.5,\n \
    \     \"unit\": \"g\",\n      \"stage\": \"Main receiving batch\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 0, row 6 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Yeast extract (BD-Difco)\
    \                                \",\n          \" 0.5    \",\n          \" g\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract (BD-Difco)\\\",\\n          \\\"\
    volume\\\": 0.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The primary and provider agree on the printed\
    \ main-batch mass. The local g/L denominator is not established: 1 L basal medium\
    \ plus supplements is not a measured final volume. No attached quantity evidence\
    \ is present.\"\n  },\n  {\n    \"decision_id\": \"q8\",\n    \"name\": \"Tryptone\
    \ (BD-Difco)\",\n    \"stage\": \"Main receiving batch\",\n    \"decision\": \"\
    unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 1.5,\n \
    \     \"unit\": \"g\",\n      \"stage\": \"Main receiving batch\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 0, row 7 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Tryptone (BD-Difco)    \
    \                                 \",\n          \" 1.5    \",\n          \" g\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Tryptone (BD-Difco)\\\",\\n          \\\"volume\\\
    \": 1.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The primary and provider agree on the printed\
    \ main-batch mass. The local g/L denominator is not established: 1 L basal medium\
    \ plus supplements is not a measured final volume. No attached quantity evidence\
    \ is present.\"\n  },\n  {\n    \"decision_id\": \"q9\",\n    \"name\": \"Basal\
    \ medium (see below)\",\n    \"stage\": \"Main receiving batch\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 1,\n   \
    \   \"unit\": \"L\",\n      \"stage\": \"Main receiving batch\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm431\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\",\n  \
    \      \"source_locator\": \"HTML table 0, row 0 (zero based)\",\n        \"snapshot_sha256\"\
    : \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\",\n    \
    \    \"decoded_primary_cells\": [\n          \" Basal medium (see below)     \
    \                           \",\n          \" 1.0    \",\n          \" L  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Basal medium (see below)\\\",\\n          \\\"\
    volume\\\": 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\"\
    : \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact source\
    \ stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed.\"\n\
    \  },\n  {\n    \"decision_id\": \"q10\",\n    \"name\": \"Carbon dioxide gas\"\
    ,\n    \"stage\": \"Preparation atmosphere, not a dissolved ingredient rate\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[9].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"variable\",\n          \"unit\": \"VARIABLE\"\n        }\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"gas_mixture\": \"N2:CO2\
    \ 4:1\",\n      \"basis\": \"v/v\"\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Preparation paragraph or global default; exact\
    \ parsed text\",\n        \"exact_source_quote\": \"(4:1, v/v)\",\n        \"\
    snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      },\n      {\n        \"source_key\": \"togoM431original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[0].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Carbon dioxide gas\\\"\",\n        \"snapshot_sha256\"\
    : \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The local variable token does not represent\
    \ the source ratio. Preserve the explicit 4:1 v/v preparation/distribution atmosphere\
    \ and the separate N2-only sulfide-stock sterilization; no dissolved concentration,\
    \ pressure or culture gas flow is specified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q11\",\n    \"name\": \"Nitrogen gas\",\n    \"stage\": \"Preparation atmosphere,\
    \ not a dissolved ingredient rate\",\n    \"decision\": \"not_quantified\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"gas_mixture\": \"N2:CO2\
    \ 4:1\",\n      \"basis\": \"v/v\"\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Preparation paragraph or global default; exact\
    \ parsed text\",\n        \"exact_source_quote\": \"(4:1, v/v)\",\n        \"\
    snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      },\n      {\n        \"source_key\": \"togoM431original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[0].items[13]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nitrogen gas\\\"\",\n        \"snapshot_sha256\"\
    : \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The local variable token does not represent\
    \ the source ratio. Preserve the explicit 4:1 v/v preparation/distribution atmosphere\
    \ and the separate N2-only sulfide-stock sterilization; no dissolved concentration,\
    \ pressure or culture gas flow is specified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q12\",\n    \"name\": \"Distilled water\",\n    \"stage\": \"Three distinct\
    \ solvent preparations incorrectly collapsed\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"989.0\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"989.0\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].notes\",\n        \"stored\": \"\
    Role: Solvating media; Properties: Inorganic compound, Defined component, Simple\
    \ component [Merged 3 duplicates: 1.0, 987.0, 1.0]\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[11].notes\",\n        \"stored\": \"Role:\
    \ Solvating media; Properties: Inorganic compound, Defined component, Simple component\
    \ [Merged 3 duplicates: 1.0, 987.0, 1.0]\"\n      }\n    ],\n    \"desired\":\
    \ {\n      \"basal_water\": {\n        \"value\": 1,\n        \"unit\": \"L\"\n\
    \      },\n      \"trace_stock_water\": {\n        \"value\": 987,\n        \"\
    unit\": \"ml\"\n      },\n      \"selenium_tungsten_stock_water\": {\n       \
    \ \"value\": 1,\n        \"unit\": \"L\"\n      }\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm431\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\",\n        \"source_locator\"\
    : \"HTML table 1, row 6 (zero based)\",\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Distilled water        \
    \                                 \",\n          \" 1.0    \",\n          \" L\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 2, row 0 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Distilled water        \
    \                               \",\n          \" 987.0    \",\n          \" ml\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 3, row 3 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Distilled water        \
    \                                 \",\n          \" 1.0    \",\n          \" L\
    \        \"\n        ],\n        \"representation\": \"Exact decoded DOM cells\
    \ independently rejoined to raw HTML; not claimed as an HTML substring.\"\n  \
    \    }\n    ],\n    \"interpretation\": \"The local 989 g/L is accompanied by\
    \ a note merging numeric values 1, 987 and 1 from different units/stages. Those\
    \ three source water inputs must be restored separately; neither 989 g/L, a cross-stock\
    \ volume sum, nor any final-medium volume is source-established. The note documents\
    \ the local collapse but does not prove execution of a particular current writer.\"\
    \n  },\n  {\n    \"decision_id\": \"q13\",\n    \"name\": \"NaCl\",\n    \"stage\"\
    : \"Basal medium preparation\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 1,\n   \
    \   \"unit\": \"g\",\n      \"stage\": \"Basal medium preparation\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 1, row 0 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" NaCl                   \
    \                                 \",\n          \" 1.0    \",\n          \" g\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 1,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. These\
    \ salts belong to the separately defined basal preparation used as a 1 L input,\
    \ not an independently established final-medium concentration.\"\n  },\n  {\n\
    \    \"decision_id\": \"q14\",\n    \"name\": \"CaCl2・2H2O\",\n    \"stage\":\
    \ \"Basal medium preparation\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.075\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.075\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 0.075,\n\
    \      \"unit\": \"g\",\n      \"stage\": \"Basal medium preparation\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 1, row 2 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" CaCl2·2H2O             \
    \                     \",\n          \" 0.075  \",\n          \" g  \"\n     \
    \   ],\n        \"representation\": \"Exact decoded DOM cells independently rejoined\
    \ to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n      \
    \  \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2・2H2O\\\",\\n          \\\"volume\\\": 0.075,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. These\
    \ salts belong to the separately defined basal preparation used as a 1 L input,\
    \ not an independently established final-medium concentration.\"\n  },\n  {\n\
    \    \"decision_id\": \"q15\",\n    \"name\": \"KH2PO4\",\n    \"stage\": \"Basal\
    \ medium preparation\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 0.2,\n \
    \     \"unit\": \"g\",\n      \"stage\": \"Basal medium preparation\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 1, row 4 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" KH2PO4 \",\n          \"\
     0.2    \",\n          \" g  \"\n        ],\n        \"representation\": \"Exact\
    \ decoded DOM cells independently rejoined to raw HTML; not claimed as an HTML\
    \ substring.\"\n      },\n      {\n        \"source_key\": \"togoM431original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. These\
    \ salts belong to the separately defined basal preparation used as a 1 L input,\
    \ not an independently established final-medium concentration.\"\n  },\n  {\n\
    \    \"decision_id\": \"q16\",\n    \"name\": \"NH4Cl\",\n    \"stage\": \"Basal\
    \ medium preparation\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 0.25,\n\
    \      \"unit\": \"g\",\n      \"stage\": \"Basal medium preparation\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 1, row 3 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" NH4Cl                  \
    \                              \",\n          \" 0.25   \",\n          \" g  \"\
    \n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 0.25,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. These\
    \ salts belong to the separately defined basal preparation used as a 1 L input,\
    \ not an independently established final-medium concentration.\"\n  },\n  {\n\
    \    \"decision_id\": \"q17\",\n    \"name\": \"MgCl2・6H2O\",\n    \"stage\":\
    \ \"Basal medium preparation\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 0.4,\n \
    \     \"unit\": \"g\",\n      \"stage\": \"Basal medium preparation\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 1, row 1 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" MgCl2·6H2O             \
    \                     \",\n          \" 0.4    \",\n          \" g  \"\n     \
    \   ],\n        \"representation\": \"Exact decoded DOM cells independently rejoined\
    \ to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n      \
    \  \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgCl2・6H2O\\\",\\n          \\\"volume\\\": 0.4,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. These\
    \ salts belong to the separately defined basal preparation used as a 1 L input,\
    \ not an independently established final-medium concentration.\"\n  },\n  {\n\
    \    \"decision_id\": \"q18\",\n    \"name\": \"KCl\",\n    \"stage\": \"Basal\
    \ medium preparation\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 0.5,\n \
    \     \"unit\": \"g\",\n      \"stage\": \"Basal medium preparation\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 1, row 5 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" KCl                    \
    \                                 \",\n          \" 0.5    \",\n          \" g\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KCl\\\",\\n          \\\"volume\\\": 0.5,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. These\
    \ salts belong to the separately defined basal preparation used as a 1 L input,\
    \ not an independently established final-medium concentration.\"\n  },\n  {\n\
    \    \"decision_id\": \"q19\",\n    \"name\": \"25% HCl\",\n    \"stage\": \"\
    Trace element stock preparation\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.5\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.5\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 12.5,\n\
    \      \"unit\": \"ml\",\n      \"stage\": \"Trace element stock preparation\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 2, row 1 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" 25% HCl                \
    \                               \",\n          \" 12.5    \",\n          \" ml\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"25% HCl\\\",\\n          \\\"volume\\\": 12.5,\\\
    n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 25,\\n  \
    \        \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. Only\
    \ 1 ml of this prepared stock is specified for the receiving batch. Listed solvent\
    \ volumes do not establish final stock volume, so an exact 1/1000 delivered-mass\
    \ fraction is not asserted. The 25% label has no stated w/v, v/v or mass-fraction\
    \ basis; retain it as source text and keep the 12.5 ml liquid dose separate. No\
    \ generic PERCENT enum or acid mass conversion is invented.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q20\",\n    \"name\": \"Na2MoO4・2H2O\",\n    \"stage\": \"\
    Trace element stock preparation\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"36\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"36\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 36,\n  \
    \    \"unit\": \"mg\",\n      \"stage\": \"Trace element stock preparation\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 2, row 9 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Na2MoO4·2H2O           \
    \                 \",\n          \" 36.0    \",\n          \" mg  \"\n       \
    \ ],\n        \"representation\": \"Exact decoded DOM cells independently rejoined\
    \ to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n      \
    \  \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 36,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\n      }\n\
    \    ],\n    \"interpretation\": \"Restore the printed unit and exact source stage\
    \ shown here; the current direct-medium g/L field is not a representation of this\
    \ source batch amount or stock dose. Final medium and stock volumes are not independently\
    \ established, so no replacement final g/L is proposed. Only 1 ml of this prepared\
    \ stock is specified for the receiving batch. Listed solvent volumes do not establish\
    \ final stock volume, so an exact 1/1000 delivered-mass fraction is not asserted.\
    \ Exact batch unit conversion is 36 mg = 0.036 g, before any unsupported stock\
    \ dilution.\"\n  },\n  {\n    \"decision_id\": \"q21\",\n    \"name\": \"H3BO3\"\
    ,\n    \"stage\": \"Trace element stock preparation\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 30,\n  \
    \    \"unit\": \"mg\",\n      \"stage\": \"Trace element stock preparation\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 2, row 3 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" H3BO3 \",\n          \"\
     30.0    \",\n          \" mg  \"\n        ],\n        \"representation\": \"\
    Exact decoded DOM cells independently rejoined to raw HTML; not claimed as an\
    \ HTML substring.\"\n      },\n      {\n        \"source_key\": \"togoM431original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 30,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. Only\
    \ 1 ml of this prepared stock is specified for the receiving batch. Listed solvent\
    \ volumes do not establish final stock volume, so an exact 1/1000 delivered-mass\
    \ fraction is not asserted. Exact batch unit conversion is 30 mg = 0.03 g, before\
    \ any unsupported stock dilution.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n\
    \    \"name\": \"FeSO4・7H2O\",\n    \"stage\": \"Trace element stock preparation\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n        \"field_path\":\
    \ \"ingredients[21].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"2.1\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 2.1,\n \
    \     \"unit\": \"g\",\n      \"stage\": \"Trace element stock preparation\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 2, row 2 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" FeSO4·7H2O             \
    \                     \",\n          \" 2.1    \",\n          \" g  \"\n     \
    \   ],\n        \"representation\": \"Exact decoded DOM cells independently rejoined\
    \ to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n      \
    \  \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[2].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4・7H2O\\\",\\n          \\\"volume\\\": 2.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. Only\
    \ 1 ml of this prepared stock is specified for the receiving batch. Listed solvent\
    \ volumes do not establish final stock volume, so an exact 1/1000 delivered-mass\
    \ fraction is not asserted.\"\n  },\n  {\n    \"decision_id\": \"q23\",\n    \"\
    name\": \"MnCl2・4H2O\",\n    \"stage\": \"Trace element stock preparation\",\n\
    \    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n        \"field_path\":\
    \ \"ingredients[22].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"100\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 100,\n \
    \     \"unit\": \"mg\",\n      \"stage\": \"Trace element stock preparation\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 2, row 4 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" MnCl2·4H2O             \
    \                   \",\n          \" 100.0    \",\n          \" mg  \"\n    \
    \    ],\n        \"representation\": \"Exact decoded DOM cells independently rejoined\
    \ to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n      \
    \  \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[2].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2・4H2O\\\",\\n          \\\"volume\\\": 100,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. Only\
    \ 1 ml of this prepared stock is specified for the receiving batch. Listed solvent\
    \ volumes do not establish final stock volume, so an exact 1/1000 delivered-mass\
    \ fraction is not asserted. Exact batch unit conversion is 100 mg = 0.1 g, before\
    \ any unsupported stock dilution.\"\n  },\n  {\n    \"decision_id\": \"q24\",\n\
    \    \"name\": \"CoCl2・6H2O\",\n    \"stage\": \"Trace element stock preparation\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n        \"field_path\":\
    \ \"ingredients[23].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"190\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"190\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 190,\n \
    \     \"unit\": \"mg\",\n      \"stage\": \"Trace element stock preparation\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 2, row 5 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" CoCl2·6H2O             \
    \                   \",\n          \" 190.0    \",\n          \" mg  \"\n    \
    \    ],\n        \"representation\": \"Exact decoded DOM cells independently rejoined\
    \ to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n      \
    \  \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[2].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2・6H2O\\\",\\n          \\\"volume\\\": 190,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. Only\
    \ 1 ml of this prepared stock is specified for the receiving batch. Listed solvent\
    \ volumes do not establish final stock volume, so an exact 1/1000 delivered-mass\
    \ fraction is not asserted. Exact batch unit conversion is 190 mg = 0.19 g, before\
    \ any unsupported stock dilution.\"\n  },\n  {\n    \"decision_id\": \"q25\",\n\
    \    \"name\": \"NiCl2・6H2O\",\n    \"stage\": \"Trace element stock preparation\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n        \"field_path\":\
    \ \"ingredients[24].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"24\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"24\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 24,\n  \
    \    \"unit\": \"mg\",\n      \"stage\": \"Trace element stock preparation\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 2, row 6 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" NiCl2·6H2O             \
    \                    \",\n          \" 24.0    \",\n          \" mg  \"\n    \
    \    ],\n        \"representation\": \"Exact decoded DOM cells independently rejoined\
    \ to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n      \
    \  \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[2].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2・6H2O\\\",\\n          \\\"volume\\\": 24,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. Only\
    \ 1 ml of this prepared stock is specified for the receiving batch. Listed solvent\
    \ volumes do not establish final stock volume, so an exact 1/1000 delivered-mass\
    \ fraction is not asserted. Exact batch unit conversion is 24 mg = 0.024 g, before\
    \ any unsupported stock dilution.\"\n  },\n  {\n    \"decision_id\": \"q26\",\n\
    \    \"name\": \"ZnSO4・7H2O\",\n    \"stage\": \"Trace element stock preparation\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n        \"field_path\":\
    \ \"ingredients[25].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"144\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"144\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 144,\n \
    \     \"unit\": \"mg\",\n      \"stage\": \"Trace element stock preparation\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 2, row 8 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" ZnSO4·7H2O             \
    \                   \",\n          \" 144.0    \",\n          \" mg  \"\n    \
    \    ],\n        \"representation\": \"Exact decoded DOM cells independently rejoined\
    \ to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n      \
    \  \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[2].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4・7H2O\\\",\\n          \\\"volume\\\": 144,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. Only\
    \ 1 ml of this prepared stock is specified for the receiving batch. Listed solvent\
    \ volumes do not establish final stock volume, so an exact 1/1000 delivered-mass\
    \ fraction is not asserted. Exact batch unit conversion is 144 mg = 0.144 g, before\
    \ any unsupported stock dilution.\"\n  },\n  {\n    \"decision_id\": \"q27\",\n\
    \    \"name\": \"CuCl2・2H2O\",\n    \"stage\": \"Trace element stock preparation\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n        \"field_path\":\
    \ \"ingredients[26].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 2,\n   \
    \   \"unit\": \"mg\",\n      \"stage\": \"Trace element stock preparation\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 2, row 7 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" CuCl2·2H2O             \
    \                     \",\n          \" 2.0    \",\n          \" mg  \"\n    \
    \    ],\n        \"representation\": \"Exact decoded DOM cells independently rejoined\
    \ to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n      \
    \  \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[2].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuCl2・2H2O\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. Only\
    \ 1 ml of this prepared stock is specified for the receiving batch. Listed solvent\
    \ volumes do not establish final stock volume, so an exact 1/1000 delivered-mass\
    \ fraction is not asserted. Exact batch unit conversion is 2 mg = 0.002 g, before\
    \ any unsupported stock dilution.\"\n  },\n  {\n    \"decision_id\": \"q28\",\n\
    \    \"name\": \"Na2SeO3・5H2O\",\n    \"stage\": \"Selenium/tungsten stock preparation\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n        \"field_path\":\
    \ \"ingredients[27].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 6,\n   \
    \   \"unit\": \"mg\",\n      \"stage\": \"Selenium/tungsten stock preparation\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 3, row 1 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Na2SeO3·5H2O           \
    \                  \",\n          \" 6.0    \",\n          \" mg  \"\n       \
    \ ],\n        \"representation\": \"Exact decoded DOM cells independently rejoined\
    \ to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n      \
    \  \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2SeO3・5H2O\\\",\\n          \\\"volume\\\":\
    \ 6,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\n      }\n\
    \    ],\n    \"interpretation\": \"Restore the printed unit and exact source stage\
    \ shown here; the current direct-medium g/L field is not a representation of this\
    \ source batch amount or stock dose. Final medium and stock volumes are not independently\
    \ established, so no replacement final g/L is proposed. Only 1 ml of this prepared\
    \ stock is specified for the receiving batch. Listed solvent volumes do not establish\
    \ final stock volume, so an exact 1/1000 delivered-mass fraction is not asserted.\
    \ Exact batch unit conversion is 6 mg = 0.006 g, before any unsupported stock\
    \ dilution.\"\n  },\n  {\n    \"decision_id\": \"q29\",\n    \"name\": \"Na2WO4・2H2O\"\
    ,\n    \"stage\": \"Selenium/tungsten stock preparation\",\n    \"decision\":\
    \ \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 8,\n   \
    \   \"unit\": \"mg\",\n      \"stage\": \"Selenium/tungsten stock preparation\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 3, row 2 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Na2WO4·2H2O            \
    \                  \",\n          \" 8.0    \",\n          \" mg  \"\n       \
    \ ],\n        \"representation\": \"Exact decoded DOM cells independently rejoined\
    \ to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n      \
    \  \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[3].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2WO4・2H2O\\\",\\n          \\\"volume\\\": 8,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. Only\
    \ 1 ml of this prepared stock is specified for the receiving batch. Listed solvent\
    \ volumes do not establish final stock volume, so an exact 1/1000 delivered-mass\
    \ fraction is not asserted. Exact batch unit conversion is 8 mg = 0.008 g, before\
    \ any unsupported stock dilution.\"\n  },\n  {\n    \"decision_id\": \"q30\",\n\
    \    \"name\": \"NaOH\",\n    \"stage\": \"Selenium/tungsten stock preparation\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n        \"field_path\":\
    \ \"ingredients[29].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"printed_batch_amount\": 0.4,\n \
    \     \"unit\": \"g\",\n      \"stage\": \"Selenium/tungsten stock preparation\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 3, row 0 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" NaOH                   \
    \                                 \",\n          \" 0.4    \",\n          \" g\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[3].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaOH\\\",\\n          \\\"volume\\\": 0.4,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the printed unit and exact\
    \ source stage shown here; the current direct-medium g/L field is not a representation\
    \ of this source batch amount or stock dose. Final medium and stock volumes are\
    \ not independently established, so no replacement final g/L is proposed. Only\
    \ 1 ml of this prepared stock is specified for the receiving batch. Listed solvent\
    \ volumes do not establish final stock volume, so an exact 1/1000 delivered-mass\
    \ fraction is not asserted.\"\n  },\n  {\n    \"decision_id\": \"q31\",\n    \"\
    name\": \"Trace element solution (see below)\",\n    \"stage\": \"Receiving stock\
    \ addition\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\",\n        \"\
    field_path\": \"solutions[0].concentration\",\n        \"stored\": {\n       \
    \   \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preferred_term\",\n        \"stored\"\
    : \"Trace element solution (see below)\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\",\n        \"field_path\"\
    : \"solutions[0].preferred_term\",\n        \"stored\": \"Trace element solution\
    \ (see below)\"\n      }\n    ],\n    \"desired\": {\n      \"batch_dose\": 1,\n\
    \      \"unit\": \"ml\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 0, row 1 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Trace element solution (see\
    \ below)                      \",\n          \" 1.0    \",\n          \" ml  \"\
    \n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution (see below)\\\",\\n   \
    \       \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers retain an empty Unknown\
    \ solution wrapper with a mass-per-litre field. The source gives this named stock\
    \ as a liquid addition. Connect only the appropriate stock composition and receiving\
    \ dose; M190 is the correct JCM197 vitamin identity. Do not substitute unrelated\
    \ same-name standalone stocks or invent final-volume fractions.\"\n  },\n  {\n\
    \    \"decision_id\": \"q32\",\n    \"name\": \"Selenite--tungstate solution (see\
    \ below)\",\n    \"stage\": \"Receiving stock addition\",\n    \"decision\": \"\
    correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].preferred_term\",\n        \"stored\"\
    : \"Selenite--tungstate solution (see below)\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\",\n     \
    \   \"field_path\": \"solutions[1].preferred_term\",\n        \"stored\": \"Selenite--tungstate\
    \ solution (see below)\"\n      }\n    ],\n    \"desired\": {\n      \"batch_dose\"\
    : 1,\n      \"unit\": \"ml\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 0, row 2 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Selenite-tungstate solution\
    \ (see below)                \",\n          \" 1.0    \",\n          \" ml  \"\
    \n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[0].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Selenite--tungstate solution (see below)\\\",\\\
    n          \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n      \
    \  \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers retain an empty Unknown\
    \ solution wrapper with a mass-per-litre field. The source gives this named stock\
    \ as a liquid addition. Connect only the appropriate stock composition and receiving\
    \ dose; M190 is the correct JCM197 vitamin identity. Do not substitute unrelated\
    \ same-name standalone stocks or invent final-volume fractions.\"\n  },\n  {\n\
    \    \"decision_id\": \"q33\",\n    \"name\": \"Trace vitamins (see Medium [M190])\"\
    ,\n    \"stage\": \"Receiving stock addition\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BN3_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[2].preferred_term\",\n        \"stored\"\
    : \"Trace vitamins (see Medium [M190])\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\",\n        \"field_path\"\
    : \"solutions[2].preferred_term\",\n        \"stored\": \"Trace vitamins (see\
    \ Medium [M190])\"\n      }\n    ],\n    \"desired\": {\n      \"batch_dose\"\
    : 10,\n      \"unit\": \"ml\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"HTML table 0, row 3 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Trace vitamins (see Medium\
    \ No. 197)                  \",\n          \" 10.0    \",\n          \" ml  \"\
    \n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[0].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace vitamins (see Medium [M190])\\\",\\n   \
    \       \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers retain an empty Unknown\
    \ solution wrapper with a mass-per-litre field. The source gives this named stock\
    \ as a liquid addition. Connect only the appropriate stock composition and receiving\
    \ dose; M190 is the correct JCM197 vitamin identity. Do not substitute unrelated\
    \ same-name standalone stocks or invent final-volume fractions.\"\n  },\n  {\n\
    \    \"decision_id\": \"q34\",\n    \"name\": \"Distilled water\",\n    \"stage\"\
    : \"External M190/JCM197 trace-vitamin stock only\",\n    \"decision\": \"verified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n\
    \        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[0].evidence[0]\",\n    \
    \    \"stored\": {\n          \"reference\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n          \"supports\": \"SUPPORT\",\n          \"snippet\": \"{\\n       \
    \   \\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\",\\n          \\\"gmo\\\": \\\"http://purl.jp/bio/10/gmo/GMO_001001\\\
    \"\",\n          \"explanation\": \"solutions[1].composition[0].concentration:\
    \ Source water batch input: 1 L = 1 L. This is not a measured final volume. Prior\
    \ duplicate-collapse notes describe the superseded flattened record. No final-medium\
    \ volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[0];\
    \ accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"preserve_batch_input\"\
    : 1,\n      \"unit\": \"L\"\n    },\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table 1, row 10 (zero based)\",\n      \
    \  \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Distilled water        \
    \                                 \",\n          \" 1.0    \",\n          \" L\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM190original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Verified narrowly for this existing\
    \ dependent-stock batch water concentration and its attached exact raw evidence.\
    \ The cited October 8 raw digest matches the separately captured raw bytes; original\
    \ cited and later retrieval times remain distinct. The ten vitamin notes intentionally\
    \ withdraw unsupported g/L rates. This does not verify a final stock volume, a\
    \ delivered mass in BN3, or unrelated M190 parent ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q35\",\n    \"name\": \"Biotin\",\n    \"stage\": \"External\
    \ M190/JCM197 trace-vitamin stock only\",\n    \"decision\": \"verified\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[1].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 2 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[1].evidence[0]\",\n        \"stored\": {\n      \
    \    \"reference\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n          \"supports\": \"SUPPORT\",\n          \"snippet\": \"{\\n       \
    \   \\\"component_name\\\": \\\"Biotin\\\",\\n          \\\"volume\\\": 2,\\n\
    \          \\\"unit\\\": \\\"mg\\\",\\n          \\\"gmo\\\": \\\"http://purl.jp/bio/10/gmo/GMO_001025\\\
    \"\",\n          \"explanation\": \"solutions[1].composition[1].concentration:\
    \ Source batch input: 2 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration. No final-medium volume, percentage basis, density or chemical\
    \ grounding is inferred. Locator=components[1].items[1]; accessed=2026-10-08T13:22:46.432534+00:00;\
    \ capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"preserve_batch_input\"\
    : 2,\n      \"unit\": \"mg\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table 1, row 0 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Biotin                 \
    \                                 \",\n          \" 2.0    \",\n          \" mg\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM190original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Biotin\\\",\\n          \\\"volume\\\": 2,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Verified narrowly for this existing\
    \ dependent-stock batch amount note and its attached exact raw evidence. The cited\
    \ October 8 raw digest matches the separately captured raw bytes; original cited\
    \ and later retrieval times remain distinct. The ten vitamin notes intentionally\
    \ withdraw unsupported g/L rates. This does not verify a final stock volume, a\
    \ delivered mass in BN3, or unrelated M190 parent ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q36\",\n    \"name\": \"p--Aminobenzoic acid\",\n    \"\
    stage\": \"External M190/JCM197 trace-vitamin stock only\",\n    \"decision\"\
    : \"verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[2].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[2].evidence[0]\",\n        \"stored\": {\n      \
    \    \"reference\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n          \"supports\": \"SUPPORT\",\n          \"snippet\": \"{\\n       \
    \   \\\"component_name\\\": \\\"p--Aminobenzoic acid\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\",\\n          \\\"gmo\\\": \\\"http://purl.jp/bio/10/gmo/GMO_001026\\\
    \"\",\n          \"explanation\": \"solutions[1].composition[2].concentration:\
    \ Source batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration. No final-medium volume, percentage basis, density or chemical\
    \ grounding is inferred. Locator=components[1].items[2]; accessed=2026-10-08T13:22:46.432534+00:00;\
    \ capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"preserve_batch_input\"\
    : 5,\n      \"unit\": \"mg\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table 1, row 8 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"decoded_primary_cells\": [\n          \" p-Aminobenzoic acid    \
    \                         \",\n          \" 5.0    \",\n          \" mg  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM190original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"p--Aminobenzoic acid\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"interpretation\": \"Verified narrowly for this existing dependent-stock\
    \ batch amount note and its attached exact raw evidence. The cited October 8 raw\
    \ digest matches the separately captured raw bytes; original cited and later retrieval\
    \ times remain distinct. The ten vitamin notes intentionally withdraw unsupported\
    \ g/L rates. This does not verify a final stock volume, a delivered mass in BN3,\
    \ or unrelated M190 parent ingredients.\"\n  },\n  {\n    \"decision_id\": \"\
    q37\",\n    \"name\": \"Thiamine・HCl\",\n    \"stage\": \"External M190/JCM197\
    \ trace-vitamin stock only\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[3].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[3].evidence[0]\",\n        \"stored\": {\n      \
    \    \"reference\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n          \"supports\": \"SUPPORT\",\n          \"snippet\": \"{\\n       \
    \   \\\"component_name\\\": \\\"Thiamine・HCl\\\",\\n          \\\"volume\\\":\
    \ 5,\\n          \\\"unit\\\": \\\"mg\\\",\\n          \\\"gmo\\\": \\\"http://purl.jp/bio/10/gmo/GMO_001027\\\
    \"\",\n          \"explanation\": \"solutions[1].composition[3].concentration:\
    \ Source batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration. No final-medium volume, percentage basis, density or chemical\
    \ grounding is inferred. Locator=components[1].items[3]; accessed=2026-10-08T13:22:46.432534+00:00;\
    \ capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"preserve_batch_input\"\
    : 5,\n      \"unit\": \"mg\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table 1, row 3 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Thiamine·HCl           \
    \                           \",\n          \" 5.0    \",\n          \" mg  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM190original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Thiamine・HCl\\\",\\n          \\\"volume\\\":\
    \ 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"interpretation\": \"Verified narrowly for this existing dependent-stock\
    \ batch amount note and its attached exact raw evidence. The cited October 8 raw\
    \ digest matches the separately captured raw bytes; original cited and later retrieval\
    \ times remain distinct. The ten vitamin notes intentionally withdraw unsupported\
    \ g/L rates. This does not verify a final stock volume, a delivered mass in BN3,\
    \ or unrelated M190 parent ingredients.\"\n  },\n  {\n    \"decision_id\": \"\
    q38\",\n    \"name\": \"Calcium pantothenate\",\n    \"stage\": \"External M190/JCM197\
    \ trace-vitamin stock only\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[4].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[4].evidence[0]\",\n        \"stored\": {\n      \
    \    \"reference\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n          \"supports\": \"SUPPORT\",\n          \"snippet\": \"{\\n       \
    \   \\\"component_name\\\": \\\"Calcium pantothenate\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\",\\n          \\\"gmo\\\": \\\"http://purl.jp/bio/10/gmo/GMO_001028\\\
    \"\",\n          \"explanation\": \"solutions[1].composition[4].concentration:\
    \ Source batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration. No final-medium volume, percentage basis, density or chemical\
    \ grounding is inferred. Locator=components[1].items[4]; accessed=2026-10-08T13:22:46.432534+00:00;\
    \ capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"preserve_batch_input\"\
    : 5,\n      \"unit\": \"mg\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table 1, row 6 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Calcium pantothenate   \
    \                                 \",\n          \" 5.0    \",\n          \" mg\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM190original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Calcium pantothenate\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"interpretation\": \"Verified narrowly for this existing dependent-stock\
    \ batch amount note and its attached exact raw evidence. The cited October 8 raw\
    \ digest matches the separately captured raw bytes; original cited and later retrieval\
    \ times remain distinct. The ten vitamin notes intentionally withdraw unsupported\
    \ g/L rates. This does not verify a final stock volume, a delivered mass in BN3,\
    \ or unrelated M190 parent ingredients.\"\n  },\n  {\n    \"decision_id\": \"\
    q39\",\n    \"name\": \"Pyridoxine・HCl\",\n    \"stage\": \"External M190/JCM197\
    \ trace-vitamin stock only\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[5].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 10 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[5].evidence[0]\",\n        \"stored\": {\n      \
    \    \"reference\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n          \"supports\": \"SUPPORT\",\n          \"snippet\": \"{\\n       \
    \   \\\"component_name\\\": \\\"Pyridoxine・HCl\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"mg\\\",\\n          \\\"gmo\\\": \\\"http://purl.jp/bio/10/gmo/GMO_001029\\\
    \"\",\n          \"explanation\": \"solutions[1].composition[5].concentration:\
    \ Source batch input: 10 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration. No final-medium volume, percentage basis, density or chemical\
    \ grounding is inferred. Locator=components[1].items[5]; accessed=2026-10-08T13:22:46.432534+00:00;\
    \ capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"preserve_batch_input\"\
    : 10,\n      \"unit\": \"mg\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table 1, row 2 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Pyridoxine·HCl         \
    \                          \",\n          \" 10.0    \",\n          \" mg  \"\n\
    \        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM190original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Pyridoxine・HCl\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"interpretation\": \"Verified narrowly for this existing dependent-stock\
    \ batch amount note and its attached exact raw evidence. The cited October 8 raw\
    \ digest matches the separately captured raw bytes; original cited and later retrieval\
    \ times remain distinct. The ten vitamin notes intentionally withdraw unsupported\
    \ g/L rates. This does not verify a final stock volume, a delivered mass in BN3,\
    \ or unrelated M190 parent ingredients.\"\n  },\n  {\n    \"decision_id\": \"\
    q40\",\n    \"name\": \"Folic acid\",\n    \"stage\": \"External M190/JCM197 trace-vitamin\
    \ stock only\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[6].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 2 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[6].evidence[0]\",\n        \"stored\": {\n      \
    \    \"reference\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n          \"supports\": \"SUPPORT\",\n          \"snippet\": \"{\\n       \
    \   \\\"component_name\\\": \\\"Folic acid\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\",\\n          \\\"gmo\\\": \\\"http://purl.jp/bio/10/gmo/GMO_001033\\\
    \"\",\n          \"explanation\": \"solutions[1].composition[6].concentration:\
    \ Source batch input: 2 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration. No final-medium volume, percentage basis, density or chemical\
    \ grounding is inferred. Locator=components[1].items[6]; accessed=2026-10-08T13:22:46.432534+00:00;\
    \ capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"preserve_batch_input\"\
    : 2,\n      \"unit\": \"mg\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table 1, row 1 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Folic acid             \
    \                                 \",\n          \" 2.0    \",\n          \" mg\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM190original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Folic acid\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Verified narrowly for this existing\
    \ dependent-stock batch amount note and its attached exact raw evidence. The cited\
    \ October 8 raw digest matches the separately captured raw bytes; original cited\
    \ and later retrieval times remain distinct. The ten vitamin notes intentionally\
    \ withdraw unsupported g/L rates. This does not verify a final stock volume, a\
    \ delivered mass in BN3, or unrelated M190 parent ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q41\",\n    \"name\": \"Vitamin B12\",\n    \"stage\"\
    : \"External M190/JCM197 trace-vitamin stock only\",\n    \"decision\": \"verified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[7].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 0.1 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[7].evidence[0]\",\n        \"stored\": {\n      \
    \    \"reference\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n          \"supports\": \"SUPPORT\",\n          \"snippet\": \"{\\n       \
    \   \\\"component_name\\\": \\\"Vitamin B12\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"mg\\\",\\n          \\\"gmo\\\": \\\"http://purl.jp/bio/10/gmo/GMO_001034\\\
    \"\",\n          \"explanation\": \"solutions[1].composition[7].concentration:\
    \ Source batch input: 0.1 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration. No final-medium volume, percentage basis, density or chemical\
    \ grounding is inferred. Locator=components[1].items[7]; accessed=2026-10-08T13:22:46.432534+00:00;\
    \ capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"preserve_batch_input\"\
    : 0.1,\n      \"unit\": \"mg\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table 1, row 7 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Vitamin B12 \",\n      \
    \    \" 0.1    \",\n          \" mg  \"\n        ],\n        \"representation\"\
    : \"Exact decoded DOM cells independently rejoined to raw HTML; not claimed as\
    \ an HTML substring.\"\n      },\n      {\n        \"source_key\": \"togoM190original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin B12\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Verified narrowly for this existing\
    \ dependent-stock batch amount note and its attached exact raw evidence. The cited\
    \ October 8 raw digest matches the separately captured raw bytes; original cited\
    \ and later retrieval times remain distinct. The ten vitamin notes intentionally\
    \ withdraw unsupported g/L rates. This does not verify a final stock volume, a\
    \ delivered mass in BN3, or unrelated M190 parent ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q42\",\n    \"name\": \"Riboflavin\",\n    \"stage\":\
    \ \"External M190/JCM197 trace-vitamin stock only\",\n    \"decision\": \"verified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[8].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[8].evidence[0]\",\n        \"stored\": {\n      \
    \    \"reference\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n          \"supports\": \"SUPPORT\",\n          \"snippet\": \"{\\n       \
    \   \\\"component_name\\\": \\\"Riboflavin\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\",\\n          \\\"gmo\\\": \\\"http://purl.jp/bio/10/gmo/GMO_001037\\\
    \"\",\n          \"explanation\": \"solutions[1].composition[8].concentration:\
    \ Source batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration. No final-medium volume, percentage basis, density or chemical\
    \ grounding is inferred. Locator=components[1].items[8]; accessed=2026-10-08T13:22:46.432534+00:00;\
    \ capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"preserve_batch_input\"\
    : 5,\n      \"unit\": \"mg\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table 1, row 4 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Riboflavin             \
    \                                 \",\n          \" 5.0    \",\n          \" mg\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM190original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Riboflavin\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Verified narrowly for this existing\
    \ dependent-stock batch amount note and its attached exact raw evidence. The cited\
    \ October 8 raw digest matches the separately captured raw bytes; original cited\
    \ and later retrieval times remain distinct. The ten vitamin notes intentionally\
    \ withdraw unsupported g/L rates. This does not verify a final stock volume, a\
    \ delivered mass in BN3, or unrelated M190 parent ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q43\",\n    \"name\": \"Nicotinic acid\",\n    \"stage\"\
    : \"External M190/JCM197 trace-vitamin stock only\",\n    \"decision\": \"verified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[9].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[9].evidence[0]\",\n        \"stored\": {\n      \
    \    \"reference\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n          \"supports\": \"SUPPORT\",\n          \"snippet\": \"{\\n       \
    \   \\\"component_name\\\": \\\"Nicotinic acid\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"mg\\\",\\n          \\\"gmo\\\": \\\"http://purl.jp/bio/10/gmo/GMO_001038\\\
    \"\",\n          \"explanation\": \"solutions[1].composition[9].concentration:\
    \ Source batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration. No final-medium volume, percentage basis, density or chemical\
    \ grounding is inferred. Locator=components[1].items[9]; accessed=2026-10-08T13:22:46.432534+00:00;\
    \ capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"preserve_batch_input\"\
    : 5,\n      \"unit\": \"mg\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table 1, row 5 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Nicotinic acid         \
    \                                 \",\n          \" 5.0    \",\n          \" mg\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM190original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nicotinic acid\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"interpretation\": \"Verified narrowly for this existing dependent-stock\
    \ batch amount note and its attached exact raw evidence. The cited October 8 raw\
    \ digest matches the separately captured raw bytes; original cited and later retrieval\
    \ times remain distinct. The ten vitamin notes intentionally withdraw unsupported\
    \ g/L rates. This does not verify a final stock volume, a delivered mass in BN3,\
    \ or unrelated M190 parent ingredients.\"\n  },\n  {\n    \"decision_id\": \"\
    q44\",\n    \"name\": \"Lipoic acid\",\n    \"stage\": \"External M190/JCM197\
    \ trace-vitamin stock only\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[10].notes\",\n        \"\
    stored\": \"Role: Growth factor; Properties: Organic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 5 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n   \
    \     \"field_path\": \"solutions[1].composition[10].evidence[0]\",\n        \"\
    stored\": {\n          \"reference\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n          \"supports\": \"SUPPORT\",\n          \"snippet\": \"{\\n       \
    \   \\\"component_name\\\": \\\"Lipoic acid\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\",\\n          \\\"gmo\\\": \\\"http://purl.jp/bio/10/gmo/GMO_001699\\\
    \"\",\n          \"explanation\": \"solutions[1].composition[10].concentration:\
    \ Source batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration. No final-medium volume, percentage basis, density or chemical\
    \ grounding is inferred. Locator=components[1].items[10]; accessed=2026-10-08T13:22:46.432534+00:00;\
    \ capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"preserve_batch_input\"\
    : 5,\n      \"unit\": \"mg\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"HTML table 1, row 9 (zero based)\",\n       \
    \ \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"decoded_primary_cells\": [\n          \" Lipoic acid            \
    \                                 \",\n          \" 5.0    \",\n          \" mg\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM190original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Lipoic acid\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Verified narrowly for this existing\
    \ dependent-stock batch amount note and its attached exact raw evidence. The cited\
    \ October 8 raw digest matches the separately captured raw bytes; original cited\
    \ and later retrieval times remain distinct. The ten vitamin notes intentionally\
    \ withdraw unsupported g/L rates. This does not verify a final stock volume, a\
    \ delivered mass in BN3, or unrelated M190 parent ingredients.\"\n  },\n  {\n\
    \    \"decision_id\": \"q45\",\n    \"name\": \"Conditional pH adjustment\",\n\
    \    \"stage\": \"Completed reducing preparation\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [],\n    \"desired\": {\n      \"pH\": 7.2,\n      \"\
    condition\": \"readjust if necessary\"\n    },\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Preparation paragraph or global default; exact\
    \ parsed text\",\n        \"exact_source_quote\": \"Readjust pH to 7.2, if necessary.\"\
    ,\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      }\n    ],\n    \"interpretation\": \"Neither selected layer has a pH or\
    \ preparation array. Add the source condition, not a measured culture pH or an\
    \ unconditional preset for each separate stock.\"\n  },\n  {\n    \"decision_id\"\
    : \"q46\",\n    \"name\": \"Global autoclave default\",\n    \"stage\": \"Applicable\
    \ autoclaved preparations unless otherwise stated\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [],\n    \"desired\": {\n      \"temperature_C\": 121,\n\
    \      \"duration_min\": 15\n    },\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Preparation paragraph or global default; exact\
    \ parsed text\",\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize\
    \ media by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"\
    cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\",\n        \"\
    parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      }\n    ],\n    \"interpretation\": \"This is the actual JCM page default.\
    \ It applies only to source-designated autoclaved preparations where no exception\
    \ is stated; do not apply it to filter-sterilized vitamins/bicarbonate or sulfur\
    \ steaming.\"\n  },\n  {\n    \"decision_id\": \"q47\",\n    \"name\": \"Glucose\
    \ stock\",\n    \"stage\": \"Separately prepared addition\",\n    \"decision\"\
    : \"schema_gap\",\n    \"local_fields\": [],\n    \"desired\": {\n      \"source_percent_text\"\
    : \"10%\",\n      \"basis\": \"unspecified\",\n      \"delivered_volume\": \"\
    not stated\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Preparation paragraph or global default; exact\
    \ parsed text\",\n        \"exact_source_quote\": \"Separately autoclave glucose,\
    \ yeast extract and tryptone (10% each)\",\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact unqualified percent.\
    \ Its w/v, v/v or mass-fraction basis is not supplied, and a generic PERCENT concentration\
    \ enum is unavailable. Do not infer a stock dose from the separate batch mass;\
    \ record the preparation text and unresolved basis explicitly.\"\n  },\n  {\n\
    \    \"decision_id\": \"q48\",\n    \"name\": \"Yeast extract stock\",\n    \"\
    stage\": \"Separately prepared addition\",\n    \"decision\": \"schema_gap\",\n\
    \    \"local_fields\": [],\n    \"desired\": {\n      \"source_percent_text\"\
    : \"10%\",\n      \"basis\": \"unspecified\",\n      \"delivered_volume\": \"\
    not stated\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Preparation paragraph or global default; exact\
    \ parsed text\",\n        \"exact_source_quote\": \"Separately autoclave glucose,\
    \ yeast extract and tryptone (10% each)\",\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact unqualified percent.\
    \ Its w/v, v/v or mass-fraction basis is not supplied, and a generic PERCENT concentration\
    \ enum is unavailable. Do not infer a stock dose from the separate batch mass;\
    \ record the preparation text and unresolved basis explicitly.\"\n  },\n  {\n\
    \    \"decision_id\": \"q49\",\n    \"name\": \"Tryptone stock\",\n    \"stage\"\
    : \"Separately prepared addition\",\n    \"decision\": \"schema_gap\",\n    \"\
    local_fields\": [],\n    \"desired\": {\n      \"source_percent_text\": \"10%\"\
    ,\n      \"basis\": \"unspecified\",\n      \"delivered_volume\": \"not stated\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Preparation paragraph or global default; exact\
    \ parsed text\",\n        \"exact_source_quote\": \"Separately autoclave glucose,\
    \ yeast extract and tryptone (10% each)\",\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact unqualified percent.\
    \ Its w/v, v/v or mass-fraction basis is not supplied, and a generic PERCENT concentration\
    \ enum is unavailable. Do not infer a stock dose from the separate batch mass;\
    \ record the preparation text and unresolved basis explicitly.\"\n  },\n  {\n\
    \    \"decision_id\": \"q50\",\n    \"name\": \"Bicarbonate stock\",\n    \"stage\"\
    : \"Separately prepared addition\",\n    \"decision\": \"schema_gap\",\n    \"\
    local_fields\": [],\n    \"desired\": {\n      \"source_percent_text\": \"8%\"\
    ,\n      \"basis\": \"unspecified\",\n      \"delivered_volume\": \"not stated\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Preparation paragraph or global default; exact\
    \ parsed text\",\n        \"exact_source_quote\": \"(8%) solution\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact unqualified percent.\
    \ Its w/v, v/v or mass-fraction basis is not supplied, and a generic PERCENT concentration\
    \ enum is unavailable. Do not infer a stock dose from the separate batch mass;\
    \ record the preparation text and unresolved basis explicitly.\"\n  },\n  {\n\
    \    \"decision_id\": \"q51\",\n    \"name\": \"Sulfide stock\",\n    \"stage\"\
    : \"Separately prepared addition\",\n    \"decision\": \"schema_gap\",\n    \"\
    local_fields\": [],\n    \"desired\": {\n      \"source_percent_text\": \"5%\"\
    ,\n      \"basis\": \"unspecified\",\n      \"delivered_volume\": \"not stated\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Preparation paragraph or global default; exact\
    \ parsed text\",\n        \"exact_source_quote\": \"5% Na 2 S·9H 2 O solution\"\
    ,\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact unqualified percent.\
    \ Its w/v, v/v or mass-fraction basis is not supplied, and a generic PERCENT concentration\
    \ enum is unavailable. Do not infer a stock dose from the separate batch mass;\
    \ record the preparation text and unresolved basis explicitly.\"\n  },\n  {\n\
    \    \"decision_id\": \"q52\",\n    \"name\": \"Hydrochloric acid stock strength\"\
    ,\n    \"stage\": \"Trace element stock\",\n    \"decision\": \"schema_gap\",\n\
    \    \"local_fields\": [],\n    \"desired\": {\n      \"source_percent_text\"\
    : \"25%\",\n      \"basis\": \"unspecified\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm431\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\",\n        \"source_locator\"\
    : \"HTML table 2, row 1 (zero based)\",\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"decoded_primary_cells\": [\n          \" 25% HCl                \
    \                               \",\n          \" 12.5    \",\n          \" ml\
    \  \"\n        ],\n        \"representation\": \"Exact decoded DOM cells independently\
    \ rejoined to raw HTML; not claimed as an HTML substring.\"\n      },\n      {\n\
    \        \"source_key\": \"togoM431original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"25% HCl\\\",\\n          \\\"volume\\\": 12.5,\\\
    n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 25,\\n  \
    \        \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"interpretation\": \"The source separately supplies a\
    \ 12.5 ml addition of 25% HCl. The percent basis remains unspecified; no density\
    \ or equivalent acid mass is inferred.\"\n  },\n  {\n    \"decision_id\": \"q53\"\
    ,\n    \"name\": \"Sulfur steaming\",\n    \"stage\": \"Only sulfur before assembly/distribution\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [],\n    \"desired\": {\n\
    \      \"duration_each_h\": 3,\n      \"successive_days\": 3\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm431\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\",\n        \"source_locator\"\
    : \"Preparation paragraph or global default; exact parsed text\",\n        \"\
    exact_source_quote\": \"Steam sulfur for 3 hr on each of 3 successive days.\"\
    ,\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      }\n    ],\n    \"interpretation\": \"This is three hours on each of three\
    \ successive days, not a culture incubation duration or three-day autoclave cycle.\
    \ Steam temperature and pressure are not stated.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.009817.stock-stage-and-solvent
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Stock recipes and solvent stages are flattened into the receiving medium
  description: Basal salts, trace-stock ingredients and selenium/tungsten stock ingredients
    appear as direct-medium g/L fields. Water 989 g/L collapses 1 L, 987 ml and 1
    L from separate preparations; empty Unknown solution wrappers retain liquid additions
    as g/L. No source final-volume declaration supports these rates.
  target_ids:
  - CultureMech:009817
  field_paths:
  - ingredients[8]
  - ingredients[11]
  - ingredients[12]
  - ingredients[18]
  - ingredients[27]
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
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
  issue_key: culturemech.009817.micro-milli-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Microgram and milligram source quantities are encoded as gram rates
  description: Resazurin 0.5 mg and main B12 5 µg became 0.5 and 5 g/L. Nine trace/selenium-tungsten
    mg rows likewise retain their numeric values in g/L, in addition to the wrong
    stock stage. Correct batch unit arithmetic does not establish delivered final-medium
    rates.
  target_ids:
  - CultureMech:009817
  field_paths:
  - ingredients[0].concentration
  - ingredients[3].concentration
  - ingredients[19].concentration
  - ingredients[20].concentration
  - ingredients[22].concentration
  - ingredients[23].concentration
  - ingredients[24].concentration
  - ingredients[25].concentration
  - ingredients[26].concentration
  - ingredients[27].concentration
  - ingredients[28].concentration
  evidence_ids:
  - primary
  - provider
  - record
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
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
  issue_key: culturemech.009817.hydrate-identities
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two explicitly supplied hexahydrates map to anhydrous concepts
  description: Cobalt chloride hexahydrate and nickel chloride hexahydrate are explicitly
    supplied in the trace stock, but both selected layers assert CHEBI35696 and CHEBI34887
    respectively. These are valid anhydrous concepts with matching labels, not the
    named source hydrates.
  target_ids:
  - CultureMech:009817
  field_paths:
  - ingredients[23].term
  - ingredients[24].term
  evidence_ids:
  - primary
  - provider
  - chebi35696
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.009817.preparation-and-conditions
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The required staged reducing preparation is absent
  description: Neither selected layer represents the source gas ratio, selective sterilization,
    sulfur timing, reducing sequence or conditional pH 7.2. This prevents reproduction
    of the intended medium even after quantity corrections.
  target_ids:
  - CultureMech:009817
  field_paths:
  - preparation_steps
  - ph_value
  - high_metal
  evidence_ids:
  - primary
  - provider
  - record
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3
  normalization_reason: P3.4 is escalated to major because the missing redox and sterilization
    sequence changes reproducibility; it is not merely optional narrative or a culture-growth
    assertion.
- finding_id: f5
  issue_key: culturemech.009817.legacy-sulfur-correspondence
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: The active legacy sulfur link lacks current and historical correspondence
  description: MediaIngredientMech:001072 is absent from the pinned current index/catalogue/tree.
    This establishes a current lookup gap only; its historical identity remains unresolved.
  target_ids:
  - CultureMech:009817
  field_paths:
  - ingredients[4].mediaingredientmech_term
  evidence_ids:
  - mim
  - mimPinnedCatalog
  - mimPinnedTree
  - record
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.2
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: culturemech.009817.receiving-claim-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Selected receiving ingredients and stock wrappers lack attached quantity
    evidence
  description: The selected target and owner have no claim evidence for their 33 concentration
    objects. The separate repaired M190 vitamin stock already has exact batch evidence
    and should be credited rather than recurred as missing.
  target_ids:
  - CultureMech:009817
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - vitamin-owner
  - primary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: P4.3 is a minor traceability exception distinct from the confirmed
    major stage/unit defects; linkage alone does not validate the unresolved final-volume
    basis.
actions:
- action_id: a1
  description: Reconstruct the four source stages and exact liquid additions in the
    maintained TOGO owner, using only scoped M190 vitamins. Preserve original batch
    units and separately resolve stock/final-medium denominators before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009817
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
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
  description: Restore the exact printed mg/µg batch units and proper stocks; verify
    every affected local field against its individual source row. Do not use assumed
    final litres or bare-percent stock strengths to derive delivered amounts.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009817
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
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
  description: Select and independently verify the exact supplied hydrate concepts
    before updating the maintained owner and regenerating; do not repair only the
    canonical labels or infer a mass conversion.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009817
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
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
  description: Add only the exact source preparation stages and conditional pH, retain
    all unspecified percent bases, and reassess high_metal against the properly scoped
    delivered formulation. Do not invent culture incubation, pressure or dose denominators.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009817
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
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
  description: Recover exact historical identifier evidence or document the unresolved
    link before any authorized migration; preserve the independently asserted sulfur
    CHEBI concept without claiming equivalence.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009817
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
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
  description: After stage and unit curation, attach short exact source snippets with
    source hashes and locators to the appropriate receiving or stock fields; preserve
    the existing scoped vitamin evidence.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:009817
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
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
- Completion is partial because the active legacy sulfur identifier historical correspondence
  remains unresolved despite complete current-negative lookups. No new legacy network
  request was made.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-044
- generated-medium
```
