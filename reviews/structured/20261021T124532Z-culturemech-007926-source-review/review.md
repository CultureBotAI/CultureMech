# Source and formulation review: alkaline_clostridial_nutrient_medium (CultureMech:007926)

- Review: 20261021T124532Z-culturemech-007926-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T12:39:26Z
- Finished UTC: 2026-10-21T12:45:32Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact JCM 1295 and TOGO M1391 sources support the listed solute masses but retain separate A/B stages, volume units and conditional preparation that the local layers lose. Both generic solution identifiers resolve to unrelated stocks. Current provider pH 6.8 is not evidence of an assembled final pH. A completed scientific review identifies owner corrections and a limited supplied-form uncertainty.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 209; batch 021 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty task batches contain 200 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 203 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007926 | data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml | generated | alkaline_clostridial_nutrient_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007926 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007926 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch021/209/strict.tsv |
| validate-terms | passed | True | CultureMech:007926 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007926 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007926 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007926.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:007926.

20 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Yeast extract source mass",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "3 g in Solution A, retaining the source-stage recipe and its listed 900 mL or 100 mL water.",
    "rationale": "The existing number matches the source mass and the provider nominal-litre g/L, but the current direct field loses the A/B scope needed for separate preparation. Restore stage scope without treating water-plus-solutes as measured final volume. No attached amount evidence exists.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Yeast extract\",\n          \"volume\": 3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "NaCl source mass",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "5 g in Solution A, retaining the source-stage recipe and its listed 900 mL or 100 mL water.",
    "rationale": "The existing number matches the source mass and the provider nominal-litre g/L, but the current direct field loses the A/B scope needed for separate preparation. Restore stage scope without treating water-plus-solutes as measured final volume. No attached amount evidence exists.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "Sodium acetate source mass",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "3 g in Solution A, retaining the source-stage recipe and its listed 900 mL or 100 mL water.",
    "rationale": "The existing number matches the source mass and the provider nominal-litre g/L, but the current direct field loses the A/B scope needed for separate preparation. Restore stage scope without treating water-plus-solutes as measured final volume. No attached amount evidence exists.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"Sodium acetate\",\n          \"volume\": 3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "Glucose source mass",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "5 g in Solution A, retaining the source-stage recipe and its listed 900 mL or 100 mL water.",
    "rationale": "The existing number matches the source mass and the provider nominal-litre g/L, but the current direct field loses the A/B scope needed for separate preparation. Restore stage scope without treating water-plus-solutes as measured final volume. No attached amount evidence exists.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"Glucose\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Soluble starch source mass",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "1 g in Solution A, retaining the source-stage recipe and its listed 900 mL or 100 mL water.",
    "rationale": "The existing number matches the source mass and the provider nominal-litre g/L, but the current direct field loses the A/B scope needed for separate preparation. Restore stage scope without treating water-plus-solutes as measured final volume. No attached amount evidence exists.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"Soluble starch\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Beef extract source mass",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "10 g in Solution A, retaining the source-stage recipe and its listed 900 mL or 100 mL water.",
    "rationale": "The existing number matches the source mass and the provider nominal-litre g/L, but the current direct field loses the A/B scope needed for separate preparation. Restore stage scope without treating water-plus-solutes as measured final volume. No attached amount evidence exists.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"Beef extract\",\n          \"volume\": 10,\n          \"unit\": \"g\"",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "L-Cysteine・HCl・H2O source mass",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "0.5 g in Solution A, retaining the source-stage recipe and its listed 900 mL or 100 mL water.",
    "rationale": "The existing number matches the source mass and the provider nominal-litre g/L, but the current direct field loses the A/B scope needed for separate preparation. Restore stage scope without treating water-plus-solutes as measured final volume. No attached amount evidence exists.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"L-Cysteine・HCl・H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Peptone source mass",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "5 g in Solution A, retaining the source-stage recipe and its listed 900 mL or 100 mL water.",
    "rationale": "The existing number matches the source mass and the provider nominal-litre g/L, but the current direct field loses the A/B scope needed for separate preparation. Restore stage scope without treating water-plus-solutes as measured final volume. No attached amount evidence exists.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"Peptone\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "NaHCO3 source mass",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2.9",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2.9",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "2.9 g in Solution B, retaining the source-stage recipe and its listed 900 mL or 100 mL water.",
    "rationale": "The existing number matches the source mass and the provider nominal-litre g/L, but the current direct field loses the A/B scope needed for separate preparation. Restore stage scope without treating water-plus-solutes as measured final volume. No attached amount evidence exists.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"NaHCO3\",\n          \"volume\": 2.9,\n          \"unit\": \"g\"",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Na2CO3 source mass",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "7",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "7",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "7 g in Solution B, retaining the source-stage recipe and its listed 900 mL or 100 mL water.",
    "rationale": "The existing number matches the source mass and the provider nominal-litre g/L, but the current direct field loses the A/B scope needed for separate preparation. Restore stage scope without treating water-plus-solutes as measured final volume. No attached amount evidence exists.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2CO3\",\n          \"volume\": 7,\n          \"unit\": \"g\"",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Solution A water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "900 mL water in its named source stage.",
    "rationale": "The stored sum 1000 G_PER_L is a mass-unit substitution and erases the two preparation stages. Preserve literal volume quantities; 900+100=1000 mL is a nominal liquid-input sum only.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 900,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Solution B water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "100 mL water in its named source stage.",
    "rationale": "The stored sum 1000 G_PER_L is a mass-unit substitution and erases the two preparation stages. Preserve literal volume quantities; 900+100=1000 mL is a nominal liquid-input sum only.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Solution A receiving volume",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "900",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "900",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "900 mL of the exact JCM 1295 solution, not the unrelated 5342/5343 stock.",
    "rationale": "Correct G_PER_L to a source-volume representation and preserve identity. No separate stock ID is invented from the provider flattened main-solution 5449 identifier.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Solution A\",\n          \"volume\": 900,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Solution B receiving volume",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "100 mL of the exact JCM 1295 solution, not the unrelated 5342/5343 stock.",
    "rationale": "Correct G_PER_L to a source-volume representation and preserve identity. No separate stock ID is invented from the provider flattened main-solution 5449 identifier.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Solution B\",\n          \"volume\": 100,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "Nitrogen atmosphere quantity and branch",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      }
    ],
    "proposed_source_representation": "No nitrogen dose or gas ratio is quantified; retain the static-condition OR nitrogen-atmosphere alternative.",
    "rationale": "The existing VARIABLE value does not establish a required nitrogen addition. The source context is conditional, and no independent growth or phenotype assertion is introduced.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"N2\"",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      },
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.comments[1].comment, static OR nitrogen clause",
        "exact_source_quote": "Cultivate under a static culture condition or a N2 atmosphere.",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "Solution A pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "pH 6.5–7.0 for Solution A before combining with B.",
    "rationale": "Both local layers omit the instruction. The provider global 6.8 is not an independently supported final-mixture endpoint; do not install it as ph_value.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.comments[0].comment following Solution A",
        "exact_source_quote": "Adjust pH to 6.5-7.0.",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "Conditional solid-branch gellan mass",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "For the optional solid branch only: 10.0 g gellan gum in Solution A (900 mL).",
    "rationale": "This does not change the current liquid baseline to mandatory solid medium. Keep gellan identity distinct from agar and preserve the source conditional scope.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.comments[1].comment, conditional solid branch",
        "exact_source_quote": "For preparation of solid medium, add 10.0 g gellan gum in Solution A (900 ml).",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "Conditional solid-branch hot mixing range",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "60–70°C for mixing the conditional solid branch after autoclaving.",
    "rationale": "Do not replace the preceding general combine-after-cooling instruction with a universal hot-mixing step; the source places this range in the solid-medium branch.",
    "source_snippets": [
      {
        "source_key": "togoM1391",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391",
        "source_locator": "$.comments[1].comment, following conditional gellan branch",
        "exact_source_quote": "After autoclaving, mix the two solutions while being hot (60 to 70 C) and pour into test tubes or petri dishes.",
        "snapshot_sha256": "892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "Autoclave temperature",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "121°C default applied with the explicit separate A/B sterilization instruction.",
    "rationale": "The exact page supplies this default and no competing cycle. Neither local layer retains the cycle. Keep conditional solid-branch handling separate.",
    "source_snippets": [
      {
        "source_key": "jcm1295",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1295",
        "source_locator": "JCM page header default applying to medium 1295",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "985dbbb8a571948d2b39756928b0a419dc8685b47fe52c75ab733975ab502c99",
        "parsed_text_sha256": "e94f35eb62e657cf07a7582cc5979ff500516fc06a1c3608328ae5ae06b67ea5"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Autoclave duration",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "15 minutes default applied with the explicit separate A/B sterilization instruction.",
    "rationale": "The exact page supplies this default and no competing cycle. Neither local layer retains the cycle. Keep conditional solid-branch handling separate.",
    "source_snippets": [
      {
        "source_key": "jcm1295",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1295",
        "source_locator": "JCM page header default applying to medium 1295",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "985dbbb8a571948d2b39756928b0a419dc8685b47fe52c75ab733975ab502c99",
        "parsed_text_sha256": "e94f35eb62e657cf07a7582cc5979ff500516fc06a1c3608328ae5ae06b67ea5"
      }
    ]
  }
]

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:007926.

9 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 9/12 primary and 6/12 secondary instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form uncertainty is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 12: primary 75.00%; secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Exact accession, stable identity and maintained ownership

identity: supported. Targets: CultureMech:007926.

CM007926 resolves to one exact normalized TOGO M1391 owner; target merge provenance agrees. M1391 explicitly identifies JCM 1295. The source accession is supported, while current generic A/B links fail exact recipe correspondence.

### Claim-level evidence and provider/primary scope

evidence: concern. Targets: CultureMech:007926.

Import URLs and history are provenance, not attached ingredient evidence. Every listed local concentration is covered in the inventory with literal source text, exact locators, original units and scope. Source availability and scientific correctness are assessed separately.

### Preparation stages and missing source conditions

completeness: concern. Targets: CultureMech:007926.

Both layers omit preparation_steps. Recover source A pH 6.5–7.0, separate A/B sterilization and combination after cooling, the static OR nitrogen option, and the separately conditional gellan/hot-mixing branch. The source does not state an assembled final pH 6.8. Preserve the exact default cycle and unquantified nitrogen.

### Composition and physical-state classification

scope: supported. Targets: CultureMech:007926.

Yeast extract, beef extract and peptone support COMPLEX/UNDEFINED. LIQUID is consistent with the baseline. The source describes an optional gellan-solid branch; it does not justify automatically changing the baseline physical state or substituting agar. The title alone is not organism-specific growth evidence.

### Supplied forms and limits of chemical specificity

grounding: concern. Targets: CultureMech:007926.

CHEBI:91248 explicitly defines the L-cysteine hydrochloride monohydrate written in the source. The source sodium acetate name is unqualified, while CHEBI:32954 carries an anhydrous formula and synonyms; exact supplied hydrate remains unresolved. This is not proof that the current salt ID is false, and no replacement or mass conversion is inferred. Generic glucose/starch names do not establish a supplier product.

### Growth, taxonomy and graph claim scope

scope: not_applicable. Targets: CultureMech:007926.

No experimental growth assertion or target-organism evidence is present. The medium title, generic application and provider context do not establish a strain phenotype, current taxonomy identifier or graph membership. No unrelated organism evidence is transferred.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:007926.

25 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Current writers and authoritative correction path

provenance: concern. Targets: CultureMech:007926.

Current TOGO code separates primary and local solution sections, retains comments, maps ml to ML_PER_L and can normalize local batches from liquid/water anchors; those anchors are not measured final volumes. Its bare percent mapping does not independently establish a w/v source basis. Current cleanup no longer sums disagreeing duplicates. The solution migrator resolves generic solution names from a global name index; name equality alone is insufficient source identity. Defaults supply variable values and Unknown solution names without scientific evidence. These current functions do not prove which historical execution produced the stored values. Correct the maintained owner with exact evidence, preserve old events and append clarification, then regenerate through the normal path.

## Findings

### f1: A/B references and volume units misrepresent the source assembly

blocker / open / confirmed; issue key: stock-identity-stage.

Both local layers link A/B to unrelated mediadive.solution:5342/5343 stocks, write the 900/100 mL receiving volumes as G_PER_L and combine source water into 1000 G_PER_L. Solute masses are numerically retained but their separate A/B preparation scope is lost.

### f2: The source preparation and conditional branches are missing

major / open / confirmed; issue key: missing-conditional-preparation.

No preparation steps retain the A-only pH range, separate sterilization, static-or-nitrogen choice or optional gellan-solid branch. The provider global pH 6.8 does not justify a final-pH assertion. The conditionally hot mixing range must not become a universal instruction.

### f3: Exact sodium acetate hydration is not established

minor / open / confirmed; issue key: acetate-form-limit.

The primary and providers name sodium acetate without a hydrate qualifier. The asserted CHEBI:32954 exists with a correct label but represents anhydrous sodium acetate; the inspected sources do not independently establish that precise supplied form.

## Recommended Actions And Acceptance Checks

### a1

Replace the nonmatching stock links with exact source-scoped A/B representation in the normalized owner; preserve all ten solute masses, two water volumes and two receiving volumes with their correct units. Remove unsupported Unknown solution placeholders and attach quantity evidence before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add the exact supported preparation with stage and conditional qualifiers, including the source default cycle. Retain LIQUID baseline unless a separate evidenced solid variant is intentionally represented; do not assert a final pH from midpoint metadata. Preserve old history and append a correction note.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve source wording and explicitly document the unresolved supplied hydration form. Seek exact source/product evidence before changing the identifier or applying a hydrate-dependent mass conversion; do not substitute a guessed hydrate.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch021/209/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch021/209/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml:1:id: CultureMech:007926<br>./data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml:1:id: CultureMech:007926<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch021/source-preflight-bound/209/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 19 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1295; Medium 1295: complete A/B formulation, pH instruction and conditional solid branch | supports | The primary specifies A with 900 mL water, B with 100 mL water, A pH 6.5–7.0, separate sterilization and a static-or-nitrogen alternative. The gellan branch is conditional. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391; meta; components[0..2]; comments[0..1] | supports | TOGO M1391 explicitly identifies JCM_M1295 and retains A/B references, unquantified nitrogen, stage-specific masses/water and the conditional preparation text. |
| mediadive | https://mediadive.dsmz.de/rest/medium/J1295; data.medium; solution 5449 recipe and steps | supports | The provider flattens A/B into a declared 1000 mL recipe while retaining two water rows and section-marker steps. Its medium min_pH/max_pH 6.8 is provider metadata, not an independently stated assembled endpoint in the primary. |
| wrong-a | https://mediadive.dsmz.de/rest/solution/5342; Exact endpoint identity and complete recipe; mismatch only | supports | The asserted generic solution endpoint is an unrelated 500 mL stock. Its ingredients and optional agar procedure do not transfer to JCM 1295. A reused metadata annotation naming JCM142 does not establish current-record identity. |
| wrong-b | https://mediadive.dsmz.de/rest/solution/5343; Exact endpoint identity and complete recipe; mismatch only | supports | The asserted generic solution endpoint is an unrelated 500 mL stock. Its ingredients and optional agar procedure do not transfer to JCM 1295. A reused metadata annotation naming JCM142 does not establish current-record identity. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch021/209/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17234 resolves to glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi28017 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:28017 resolves to starch. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32954 resolves to sodium acetate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32954": [{"label": "Na-acetate", "match_type": "preferred_term", "identifier": "CHEBI:32954", "preferred_term": "Na-acetate", "ontology_id": "CHEBI:32954", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml", "events": 12, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO code separates primary and local solution sections, retains comments, maps ml to ML_PER_L and can normalize local batches from liquid/water anchors; those anchors are not measured final volumes. Its bare percent mapping does not independently establish a w/v source basis. Current cleanup no longer sums disagreeing duplicates. The solution migrator resolves generic solution names from a global name index; name equality alone is insufficient source identity. Defaults supply variable values and Unknown solution names without scientific evidence. These current functions do not prove which historical execution produced the stored values. Correct the maintained owner with exact evidence, preserve old events and append clarification, then regenerate through the normal path. |
| writer-1 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO code separates primary and local solution sections, retains comments, maps ml to ML_PER_L and can normalize local batches from liquid/water anchors; those anchors are not measured final volumes. Its bare percent mapping does not independently establish a w/v source basis. Current cleanup no longer sums disagreeing duplicates. The solution migrator resolves generic solution names from a global name index; name equality alone is insufficient source identity. Defaults supply variable values and Unknown solution names without scientific evidence. These current functions do not prove which historical execution produced the stored values. Correct the maintained owner with exact evidence, preserve old events and append clarification, then regenerate through the normal path. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO code separates primary and local solution sections, retains comments, maps ml to ML_PER_L and can normalize local batches from liquid/water anchors; those anchors are not measured final volumes. Its bare percent mapping does not independently establish a w/v source basis. Current cleanup no longer sums disagreeing duplicates. The solution migrator resolves generic solution names from a global name index; name equality alone is insufficient source identity. Defaults supply variable values and Unknown solution names without scientific evidence. These current functions do not prove which historical execution produced the stored values. Correct the maintained owner with exact evidence, preserve old events and append clarification, then regenerate through the normal path. |
| writer-3 | src/culturemech/validation/schema_defaulter.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO code separates primary and local solution sections, retains comments, maps ml to ML_PER_L and can normalize local batches from liquid/water anchors; those anchors are not measured final volumes. Its bare percent mapping does not independently establish a w/v source basis. Current cleanup no longer sums disagreeing duplicates. The solution migrator resolves generic solution names from a global name index; name equality alone is insufficient source identity. Defaults supply variable values and Unknown solution names without scientific evidence. These current functions do not prove which historical execution produced the stored values. Correct the maintained owner with exact evidence, preserve old events and append clarification, then regenerate through the normal path. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The fresh inspection inputs and exact per-record bound catalog are authoritative. Captures retain original retrieval timestamps and hashes; preflight observations do not replace the current source comparisons. No recipe or saved review has been edited.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T124532Z-culturemech-007926-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkaline_clostridial_nutrient_medium (CultureMech:007926)'
started_at: '2026-10-21T12:39:26Z'
finished_at: '2026-10-21T12:45:32Z'
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
summary: The exact JCM 1295 and TOGO M1391 sources support the listed solute masses
  but retain separate A/B stages, volume units and conditional preparation that the
  local layers lose. Both generic solution identifiers resolve to unrelated stocks.
  Current provider pH 6.8 is not evidence of an assembled final pH. A completed scientific
  review identifies owner corrections and a limited supplied-form uncertainty.
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
  - path: data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml
    sha256: 0c08e55649d76861b8367cda179c26d565b21329284c6b47cb3335b826da67ca
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml
    sha256: 0927d424771e4f5d86929e141052bcf7abf48feb2db85e3092f6982ad2399c89
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml
    sha256: fbc65564968b86b312f7795ff5c4527f199c51d04dc2764452d46bb5ba339566
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml
    sha256: 84a4c07adfb1f11f32159a52f5e575738eb641428074b0958a68b8d5ba265ba5
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
  - path: scripts/enrich_with_chebi.py
    sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 209; batch 021 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty task batches contain
    200 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 203 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007926
targets:
- target_id: CultureMech:007926
  path: data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml
  label: alkaline_clostridial_nutrient_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007926
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch021/209/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch021/209/strict.tsv"
  target_ids:
  - CultureMech:007926
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007926
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007926
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
  - CultureMech:007926
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T12:45:31Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T12:45:31Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:40:48.998923Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch021/209/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T12:40:50.735569Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch021/209/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:40:52.658117Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:40:53.821026Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T12:45:31Z'
  support: supports
  summary: './data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml:1:id:
    CultureMech:007926

    ./data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml:1:id:
    CultureMech:007926

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch021/source-preflight-bound/209/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T12:45:31Z'
  support: supports
  summary: 19 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 552bf2f7af500537af5182b08d2a165d323ec09dfec6e3664e4194a151ff5889
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1295
  locator: 'Medium 1295: complete A/B formulation, pH instruction and conditional
    solid branch'
  accessed_at: '2026-10-21T12:23:44.289299Z'
  support: supports
  summary: The primary specifies A with 900 mL water, B with 100 mL water, A pH 6.5–7.0,
    separate sterilization and a static-or-nitrogen alternative. The gellan branch
    is conditional.
  snapshot_sha256: 985dbbb8a571948d2b39756928b0a419dc8685b47fe52c75ab733975ab502c99
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391
  locator: meta; components[0..2]; comments[0..1]
  accessed_at: '2026-10-21T12:23:42.681351Z'
  support: supports
  summary: TOGO M1391 explicitly identifies JCM_M1295 and retains A/B references,
    unquantified nitrogen, stage-specific masses/water and the conditional preparation
    text.
  snapshot_sha256: 892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0
- evidence_id: mediadive
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1295
  locator: data.medium; solution 5449 recipe and steps
  accessed_at: '2026-10-21T12:23:42.043085Z'
  support: supports
  summary: The provider flattens A/B into a declared 1000 mL recipe while retaining
    two water rows and section-marker steps. Its medium min_pH/max_pH 6.8 is provider
    metadata, not an independently stated assembled endpoint in the primary.
  snapshot_sha256: 6d0560197f3f43cca1ca2971e342ef25bfe3514e72e2be2e6ead744eff599d2d
- evidence_id: wrong-a
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5342
  locator: Exact endpoint identity and complete recipe; mismatch only
  accessed_at: '2026-10-21T07:31:13.269119Z'
  support: supports
  summary: The asserted generic solution endpoint is an unrelated 500 mL stock. Its
    ingredients and optional agar procedure do not transfer to JCM 1295. A reused
    metadata annotation naming JCM142 does not establish current-record identity.
  snapshot_sha256: 4bf262e02d0a83f9d1a24a52d2a14383aa8c6f27384e446d7da6274a05319240
- evidence_id: wrong-b
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5343
  locator: Exact endpoint identity and complete recipe; mismatch only
  accessed_at: '2026-10-21T07:31:13.547266Z'
  support: supports
  summary: The asserted generic solution endpoint is an unrelated 500 mL stock. Its
    ingredients and optional agar procedure do not transfer to JCM 1295. A reused
    metadata annotation naming JCM142 does not establish current-record identity.
  snapshot_sha256: 28c315b1d9cf9a5c19f4d79c639298f5818c06ea87462c84336f66297d20f4c0
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch021/209/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T12:45:31Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: e544a147dc9696d2b2154f65c0cf54c46037d6ecffdc3a740f52a5d3f9b9bdba
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
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.738243Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
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
- evidence_id: chebi28017
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:42.748724Z'
  support: supports
  summary: CHEBI:28017 resolves to starch. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 959b4330165a7ff12d2e464f4a7b44e148376624d04cf7764b6a8671c1c99204
- evidence_id: chebi29377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:31:16.500548Z'
  support: supports
  summary: CHEBI:29377 resolves to sodium carbonate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
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
- evidence_id: chebi32954
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:00:48.206583Z'
  support: supports
  summary: CHEBI:32954 resolves to sodium acetate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 573cba85f57c363463610a20b17be618893d6432ba239604fbd8aa562f98161b
- evidence_id: chebi91248
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:32.136441Z'
  support: supports
  summary: CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T12:45:31Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type":
    "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id":
    "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate
    solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term",
    "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32954": [{"label":
    "Na-acetate", "match_type": "preferred_term", "identifier": "CHEBI:32954", "preferred_term":
    "Na-acetate", "ontology_id": "CHEBI:32954", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T12:45:31Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml",
    "events": 12, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:45:31Z'
  support: context_only
  summary: Current TOGO code separates primary and local solution sections, retains
    comments, maps ml to ML_PER_L and can normalize local batches from liquid/water
    anchors; those anchors are not measured final volumes. Its bare percent mapping
    does not independently establish a w/v source basis. Current cleanup no longer
    sums disagreeing duplicates. The solution migrator resolves generic solution names
    from a global name index; name equality alone is insufficient source identity.
    Defaults supply variable values and Unknown solution names without scientific
    evidence. These current functions do not prove which historical execution produced
    the stored values. Correct the maintained owner with exact evidence, preserve
    old events and append clarification, then regenerate through the normal path.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:45:31Z'
  support: context_only
  summary: Current TOGO code separates primary and local solution sections, retains
    comments, maps ml to ML_PER_L and can normalize local batches from liquid/water
    anchors; those anchors are not measured final volumes. Its bare percent mapping
    does not independently establish a w/v source basis. Current cleanup no longer
    sums disagreeing duplicates. The solution migrator resolves generic solution names
    from a global name index; name equality alone is insufficient source identity.
    Defaults supply variable values and Unknown solution names without scientific
    evidence. These current functions do not prove which historical execution produced
    the stored values. Correct the maintained owner with exact evidence, preserve
    old events and append clarification, then regenerate through the normal path.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:45:31Z'
  support: context_only
  summary: Current TOGO code separates primary and local solution sections, retains
    comments, maps ml to ML_PER_L and can normalize local batches from liquid/water
    anchors; those anchors are not measured final volumes. Its bare percent mapping
    does not independently establish a w/v source basis. Current cleanup no longer
    sums disagreeing duplicates. The solution migrator resolves generic solution names
    from a global name index; name equality alone is insufficient source identity.
    Defaults supply variable values and Unknown solution names without scientific
    evidence. These current functions do not prove which historical execution produced
    the stored values. Correct the maintained owner with exact evidence, preserve
    old events and append clarification, then regenerate through the normal path.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/validation/schema_defaulter.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:45:31Z'
  support: context_only
  summary: Current TOGO code separates primary and local solution sections, retains
    comments, maps ml to ML_PER_L and can normalize local batches from liquid/water
    anchors; those anchors are not measured final volumes. Its bare percent mapping
    does not independently establish a w/v source basis. Current cleanup no longer
    sums disagreeing duplicates. The solution migrator resolves generic solution names
    from a global name index; name equality alone is insufficient source identity.
    Defaults supply variable values and Unknown solution names without scientific
    evidence. These current functions do not prove which historical execution produced
    the stored values. Correct the maintained owner with exact evidence, preserve
    old events and append clarification, then regenerate through the normal path.
  snapshot_sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007926
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 20 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:007926
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Yeast extract source mass\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"3 g in Solution A, retaining the source-stage recipe and its listed 900 mL\
    \ or 100 mL water.\",\n    \"rationale\": \"The existing number matches the source\
    \ mass and the provider nominal-litre g/L, but the current direct field loses\
    \ the A/B scope needed for separate preparation. Restore stage scope without treating\
    \ water-plus-solutes as measured final volume. No attached amount evidence exists.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1391\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract\\\",\\n          \\\"volume\\\"\
    : 3,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"NaCl source mass\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"5 g in Solution A, retaining the source-stage recipe and its listed 900 mL\
    \ or 100 mL water.\",\n    \"rationale\": \"The existing number matches the source\
    \ mass and the provider nominal-litre g/L, but the current direct field loses\
    \ the A/B scope needed for separate preparation. Restore stage scope without treating\
    \ water-plus-solutes as measured final volume. No attached amount evidence exists.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1391\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 5,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"Sodium acetate source mass\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"3 g in Solution A, retaining the source-stage recipe and its listed 900 mL\
    \ or 100 mL water.\",\n    \"rationale\": \"The existing number matches the source\
    \ mass and the provider nominal-litre g/L, but the current direct field loses\
    \ the A/B scope needed for separate preparation. Restore stage scope without treating\
    \ water-plus-solutes as measured final volume. No attached amount evidence exists.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1391\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Sodium acetate\\\",\\n          \\\"volume\\\"\
    : 3,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"Glucose source mass\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"5 g in Solution A, retaining the source-stage recipe and its listed 900 mL\
    \ or 100 mL water.\",\n    \"rationale\": \"The existing number matches the source\
    \ mass and the provider nominal-litre g/L, but the current direct field loses\
    \ the A/B scope needed for separate preparation. Restore stage scope without treating\
    \ water-plus-solutes as measured final volume. No attached amount evidence exists.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1391\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Glucose\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"Soluble starch source mass\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"1 g in Solution A, retaining the source-stage recipe and its listed 900 mL\
    \ or 100 mL water.\",\n    \"rationale\": \"The existing number matches the source\
    \ mass and the provider nominal-litre g/L, but the current direct field loses\
    \ the A/B scope needed for separate preparation. Restore stage scope without treating\
    \ water-plus-solutes as measured final volume. No attached amount evidence exists.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1391\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Soluble starch\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"Beef extract source mass\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"10 g in Solution A, retaining the source-stage recipe and its listed 900 mL\
    \ or 100 mL water.\",\n    \"rationale\": \"The existing number matches the source\
    \ mass and the provider nominal-litre g/L, but the current direct field loses\
    \ the A/B scope needed for separate preparation. Restore stage scope without treating\
    \ water-plus-solutes as measured final volume. No attached amount evidence exists.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1391\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Beef extract\\\",\\n          \\\"volume\\\":\
    \ 10,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"L-Cysteine・HCl・H2O source mass\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"0.5 g in Solution A, retaining the source-stage recipe and its listed 900\
    \ mL or 100 mL water.\",\n    \"rationale\": \"The existing number matches the\
    \ source mass and the provider nominal-litre g/L, but the current direct field\
    \ loses the A/B scope needed for separate preparation. Restore stage scope without\
    \ treating water-plus-solutes as measured final volume. No attached amount evidence\
    \ exists.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM1391\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"L-Cysteine・HCl・H2O\\\",\\n          \\\"volume\\\
    \": 0.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Peptone source mass\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"5 g in Solution A, retaining the source-stage recipe and its listed 900 mL\
    \ or 100 mL water.\",\n    \"rationale\": \"The existing number matches the source\
    \ mass and the provider nominal-litre g/L, but the current direct field loses\
    \ the A/B scope needed for separate preparation. Restore stage scope without treating\
    \ water-plus-solutes as measured final volume. No attached amount evidence exists.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1391\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Peptone\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"NaHCO3 source mass\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.9\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.9\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"2.9 g in Solution B, retaining the source-stage recipe and its listed 900\
    \ mL or 100 mL water.\",\n    \"rationale\": \"The existing number matches the\
    \ source mass and the provider nominal-litre g/L, but the current direct field\
    \ loses the A/B scope needed for separate preparation. Restore stage scope without\
    \ treating water-plus-solutes as measured final volume. No attached amount evidence\
    \ exists.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM1391\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaHCO3\\\",\\n          \\\"volume\\\": 2.9,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Na2CO3 source mass\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"7 g in Solution B, retaining the source-stage recipe and its listed 900 mL\
    \ or 100 mL water.\",\n    \"rationale\": \"The existing number matches the source\
    \ mass and the provider nominal-litre g/L, but the current direct field loses\
    \ the A/B scope needed for separate preparation. Restore stage scope without treating\
    \ water-plus-solutes as measured final volume. No attached amount evidence exists.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1391\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2CO3\\\",\\n          \\\"volume\\\": 7,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"Solution A water\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"900 mL water in its named source stage.\",\n    \"rationale\": \"The stored\
    \ sum 1000 G_PER_L is a mass-unit substitution and erases the two preparation\
    \ stages. Preserve literal volume quantities; 900+100=1000 mL is a nominal liquid-input\
    \ sum only.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM1391\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 900,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"Solution B water\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"100 mL water in its named source stage.\",\n    \"rationale\": \"The stored\
    \ sum 1000 G_PER_L is a mass-unit substitution and erases the two preparation\
    \ stages. Preserve literal volume quantities; 900+100=1000 mL is a nominal liquid-input\
    \ sum only.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM1391\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 100,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"Solution A receiving volume\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"900\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"900\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"900 mL of the exact JCM 1295 solution, not the unrelated 5342/5343 stock.\"\
    ,\n    \"rationale\": \"Correct G_PER_L to a source-volume representation and\
    \ preserve identity. No separate stock ID is invented from the provider flattened\
    \ main-solution 5449 identifier.\",\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"togoM1391\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution A\\\",\\n          \\\"volume\\\": 900,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"Solution B receiving volume\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"100 mL of the exact JCM 1295 solution, not the unrelated 5342/5343 stock.\"\
    ,\n    \"rationale\": \"Correct G_PER_L to a source-volume representation and\
    \ preserve identity. No separate stock ID is invented from the provider flattened\
    \ main-solution 5449 identifier.\",\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"togoM1391\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution B\\\",\\n          \\\"volume\\\": 100,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"Nitrogen atmosphere quantity and branch\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"No nitrogen dose or gas ratio is quantified; retain the static-condition OR\
    \ nitrogen-atmosphere alternative.\",\n    \"rationale\": \"The existing VARIABLE\
    \ value does not establish a required nitrogen addition. The source context is\
    \ conditional, and no independent growth or phenotype assertion is introduced.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1391\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"N2\\\"\",\n        \"snapshot_sha256\": \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\
    \n      },\n      {\n        \"source_key\": \"togoM1391\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\",\n\
    \        \"source_locator\": \"$.comments[1].comment, static OR nitrogen clause\"\
    ,\n        \"exact_source_quote\": \"Cultivate under a static culture condition\
    \ or a N2 atmosphere.\",\n        \"snapshot_sha256\": \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"Solution A pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"pH 6.5–7.0 for Solution A before combining with B.\",\n    \"rationale\":\
    \ \"Both local layers omit the instruction. The provider global 6.8 is not an\
    \ independently supported final-mixture endpoint; do not install it as ph_value.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1391\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.comments[0].comment following Solution A\"\
    ,\n        \"exact_source_quote\": \"Adjust pH to 6.5-7.0.\",\n        \"snapshot_sha256\"\
    : \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\"\
    : \"Conditional solid-branch gellan mass\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"For the optional solid branch only: 10.0 g gellan gum in Solution A (900 mL).\"\
    ,\n    \"rationale\": \"This does not change the current liquid baseline to mandatory\
    \ solid medium. Keep gellan identity distinct from agar and preserve the source\
    \ conditional scope.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1391\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.comments[1].comment, conditional solid branch\"\
    ,\n        \"exact_source_quote\": \"For preparation of solid medium, add 10.0\
    \ g gellan gum in Solution A (900 ml).\",\n        \"snapshot_sha256\": \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"Conditional solid-branch hot mixing range\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"60–70°C for mixing the conditional solid branch after autoclaving.\",\n  \
    \  \"rationale\": \"Do not replace the preceding general combine-after-cooling\
    \ instruction with a universal hot-mixing step; the source places this range in\
    \ the solid-medium branch.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"togoM1391\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1391\"\
    ,\n        \"source_locator\": \"$.comments[1].comment, following conditional\
    \ gellan branch\",\n        \"exact_source_quote\": \"After autoclaving, mix the\
    \ two solutions while being hot (60 to 70 C) and pour into test tubes or petri\
    \ dishes.\",\n        \"snapshot_sha256\": \"892141fec8c4d8b4fc5648010b994cf0bbf3814ae4b3931c5847e3e6303641e0\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\"\
    : \"Autoclave temperature\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"121°C default applied with the explicit separate A/B sterilization instruction.\"\
    ,\n    \"rationale\": \"The exact page supplies this default and no competing\
    \ cycle. Neither local layer retains the cycle. Keep conditional solid-branch\
    \ handling separate.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1295\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1295\"\
    ,\n        \"source_locator\": \"JCM page header default applying to medium 1295\"\
    ,\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize media\
    \ by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"985dbbb8a571948d2b39756928b0a419dc8685b47fe52c75ab733975ab502c99\"\
    ,\n        \"parsed_text_sha256\": \"e94f35eb62e657cf07a7582cc5979ff500516fc06a1c3608328ae5ae06b67ea5\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"Autoclave duration\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_CLOSTRIDIAL_NUTRIENT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"15 minutes default applied with the explicit separate A/B sterilization instruction.\"\
    ,\n    \"rationale\": \"The exact page supplies this default and no competing\
    \ cycle. Neither local layer retains the cycle. Keep conditional solid-branch\
    \ handling separate.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1295\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1295\"\
    ,\n        \"source_locator\": \"JCM page header default applying to medium 1295\"\
    ,\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize media\
    \ by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"985dbbb8a571948d2b39756928b0a419dc8685b47fe52c75ab733975ab502c99\"\
    ,\n        \"parsed_text_sha256\": \"e94f35eb62e657cf07a7582cc5979ff500516fc06a1c3608328ae5ae06b67ea5\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '9 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 9/12 primary and 6/12 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form
    uncertainty is addressed separately; valid IDs and labels do not establish correct
    source grounding.'
  target_ids:
  - CultureMech:007926
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi17234
  - chebi17997
  - chebi26710
  - chebi28017
  - chebi29377
  - chebi32139
  - chebi32954
  - chebi91248
  details: 'Instance coverage on a 0–100 percent scale, denominator 12: primary 75.00%;
    secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: identity
  area: identity
  topic: Exact accession, stable identity and maintained ownership
  outcome: supported
  summary: CM007926 resolves to one exact normalized TOGO M1391 owner; target merge
    provenance agrees. M1391 explicitly identifies JCM 1295. The source accession
    is supported, while current generic A/B links fail exact recipe correspondence.
  target_ids:
  - CultureMech:007926
  evidence_ids:
  - record
  - id-search
  - owner-0
  - primary
  - provider
  - mediadive
- assessment_id: source-evidence
  area: evidence
  topic: Claim-level evidence and provider/primary scope
  outcome: concern
  summary: Import URLs and history are provenance, not attached ingredient evidence.
    Every listed local concentration is covered in the inventory with literal source
    text, exact locators, original units and scope. Source availability and scientific
    correctness are assessed separately.
  target_ids:
  - CultureMech:007926
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - mediadive
- assessment_id: preparation
  area: completeness
  topic: Preparation stages and missing source conditions
  outcome: concern
  summary: Both layers omit preparation_steps. Recover source A pH 6.5–7.0, separate
    A/B sterilization and combination after cooling, the static OR nitrogen option,
    and the separately conditional gellan/hot-mixing branch. The source does not state
    an assembled final pH 6.8. Preserve the exact default cycle and unquantified nitrogen.
  target_ids:
  - CultureMech:007926
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - mediadive
- assessment_id: classification
  area: scope
  topic: Composition and physical-state classification
  outcome: supported
  summary: Yeast extract, beef extract and peptone support COMPLEX/UNDEFINED. LIQUID
    is consistent with the baseline. The source describes an optional gellan-solid
    branch; it does not justify automatically changing the baseline physical state
    or substituting agar. The title alone is not organism-specific growth evidence.
  target_ids:
  - CultureMech:007926
  evidence_ids:
  - record
  - primary
  - provider
  - mediadive
- assessment_id: forms
  area: grounding
  topic: Supplied forms and limits of chemical specificity
  outcome: concern
  summary: CHEBI:91248 explicitly defines the L-cysteine hydrochloride monohydrate
    written in the source. The source sodium acetate name is unqualified, while CHEBI:32954
    carries an anhydrous formula and synonyms; exact supplied hydrate remains unresolved.
    This is not proof that the current salt ID is false, and no replacement or mass
    conversion is inferred. Generic glucose/starch names do not establish a supplier
    product.
  target_ids:
  - CultureMech:007926
  evidence_ids:
  - record
  - primary
  - provider
  - mediadive
- assessment_id: growth
  area: scope
  topic: Growth, taxonomy and graph claim scope
  outcome: not_applicable
  summary: No experimental growth assertion or target-organism evidence is present.
    The medium title, generic application and provider context do not establish a
    strain phenotype, current taxonomy identifier or graph membership. No unrelated
    organism evidence is transferred.
  target_ids:
  - CultureMech:007926
  evidence_ids:
  - record
  - primary
  - provider
  - mediadive
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 25 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:007926
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: writer
  area: provenance
  topic: Current writers and authoritative correction path
  outcome: concern
  summary: Current TOGO code separates primary and local solution sections, retains
    comments, maps ml to ML_PER_L and can normalize local batches from liquid/water
    anchors; those anchors are not measured final volumes. Its bare percent mapping
    does not independently establish a w/v source basis. Current cleanup no longer
    sums disagreeing duplicates. The solution migrator resolves generic solution names
    from a global name index; name equality alone is insufficient source identity.
    Defaults supply variable values and Unknown solution names without scientific
    evidence. These current functions do not prove which historical execution produced
    the stored values. Correct the maintained owner with exact evidence, preserve
    old events and append clarification, then regenerate through the normal path.
  target_ids:
  - CultureMech:007926
  evidence_ids:
  - record
  - writer-0
  - writer-1
  - writer-2
  - writer-3
findings:
- finding_id: f1
  issue_key: stock-identity-stage
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: A/B references and volume units misrepresent the source assembly
  description: Both local layers link A/B to unrelated mediadive.solution:5342/5343
    stocks, write the 900/100 mL receiving volumes as G_PER_L and combine source water
    into 1000 G_PER_L. Solute masses are numerically retained but their separate A/B
    preparation scope is lost.
  target_ids:
  - CultureMech:007926
  field_paths:
  - solutions
  - ingredients
  evidence_ids:
  - record
  - primary
  - provider
  - mediadive
  - wrong-a
  - wrong-b
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml
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
  issue_key: missing-conditional-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The source preparation and conditional branches are missing
  description: No preparation steps retain the A-only pH range, separate sterilization,
    static-or-nitrogen choice or optional gellan-solid branch. The provider global
    pH 6.8 does not justify a final-pH assertion. The conditionally hot mixing range
    must not become a universal instruction.
  target_ids:
  - CultureMech:007926
  field_paths:
  - preparation_steps
  - ingredients[0]
  - physical_state
  evidence_ids:
  - record
  - primary
  - provider
  - mediadive
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3.5
  normalization_reason: P3.5 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: acetate-form-limit
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Exact sodium acetate hydration is not established
  description: The primary and providers name sodium acetate without a hydrate qualifier.
    The asserted CHEBI:32954 exists with a correct label but represents anhydrous
    sodium acetate; the inspected sources do not independently establish that precise
    supplied form.
  target_ids:
  - CultureMech:007926
  field_paths:
  - ingredients[4].term
  - ingredients[4].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - primary
  - provider
  - chebi32954
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml
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
  description: Replace the nonmatching stock links with exact source-scoped A/B representation
    in the normalized owner; preserve all ten solute masses, two water volumes and
    two receiving volumes with their correct units. Remove unsupported Unknown solution
    placeholders and attach quantity evidence before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007926
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml
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
  description: Add the exact supported preparation with stage and conditional qualifiers,
    including the source default cycle. Retain LIQUID baseline unless a separate evidenced
    solid variant is intentionally represented; do not assert a final pH from midpoint
    metadata. Preserve old history and append a correction note.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007926
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml
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
  description: Preserve source wording and explicitly document the unresolved supplied
    hydration form. Seek exact source/product evidence before changing the identifier
    or applying a hydrate-dependent mass conversion; do not substitute a guessed hydrate.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007926
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1391_Alkaline_Clostridial_Nutrient_Medium.yaml
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
- The fresh inspection inputs and exact per-record bound catalog are authoritative.
  Captures retain original retrieval timestamps and hashes; preflight observations
  do not replace the current source comparisons. No recipe or saved review has been
  edited.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-021
- generated-medium
```
