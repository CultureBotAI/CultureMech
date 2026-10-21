# Source and formulation review: algoriphagus_alkaliphilus_medium (CultureMech:003999)

- Review: 20261021T122011Z-culturemech-003999-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T12:11:57Z
- Finished UTC: 2026-10-21T12:20:11Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The two maintained owners and generated target flatten mineral and trace stocks into direct concentrations, combine magnesium sulfate across incompatible stages, and lose the Tris solution specification. The DSMZ source supports a complete staged correction, but exact KOMODO detail and historical legacy MIM correspondence remain unresolved; the review is partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 199; batch 020 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding nineteen task batches contain 190 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 193 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003999 | data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml | generated | algoriphagus_alkaliphilus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003999 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003999 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch020/199/strict.tsv |
| validate-terms | passed | True | CultureMech:003999 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003999 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003999 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodo1242detail | unavailable | False | CultureMech:003999 | The exact KOMODO 1242 detail request returned HTTP 403. The live DSMZ primary and MediaDive recipe are usable, but the historical contributing KOMODO formulation cannot be independently confirmed from its inaccessible detail page. |
| Exact historical MIM 000170/000171 correspondence | unavailable | True | CultureMech:003999 | Complete current pinned catalog/tree searches finished successfully, but the required historical legacy objects or an exact crosswalk are unavailable. Current CHEBI-based mappings cannot authenticate those historical identifiers. This is not a current-source access failure. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003999.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:003999.

32 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Main: Yeast extract",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Main batch: 1 g; preserve source stage.",
    "rationale": "No attached amount evidence exists. The value matches the declared nominal litre; attach exact evidence without claiming measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "Main: Proteose peptone no. 3",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Main batch: 1 g; preserve source stage.",
    "rationale": "No attached amount evidence exists. The value matches the declared nominal litre; attach exact evidence without claiming measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Proteose peptone no. 3\",\n                        \"compound_id\": 316,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "Main: Casamino acids",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Main batch: 1 g; preserve source stage.",
    "rationale": "No attached amount evidence exists. The value matches the declared nominal litre; attach exact evidence without claiming measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Casamino acids\",\n                        \"compound_id\": 101,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "Main: Glucose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Main batch: 1 g; preserve source stage.",
    "rationale": "No attached amount evidence exists. The value matches the declared nominal litre; attach exact evidence without claiming measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.55062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Main: Pyruvic acid",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Main batch: 0.05 g; preserve source stage.",
    "rationale": "No attached amount evidence exists. The value matches the declared nominal litre; attach exact evidence without claiming measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Pyruvic acid\",\n                        \"compound_id\": 540,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.567795,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Main: MgSO4 x 7 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Main batch: 0.1 g; preserve source stage.",
    "rationale": "No attached amount evidence exists. Restore direct magnesium sulfate 0.10 g separately from the mineral-stock magnesium; 1.1 g/L is not supported.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.405719,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Main: K2HPO4",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.6",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.6",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.6",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Main batch: 0.6 g; preserve source stage.",
    "rationale": "No attached amount evidence exists. The value matches the declared nominal litre; attach exact evidence without claiming measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.6,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.6,\n                        \"mmol_l\": 3.44479,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Main: Agar",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Main batch: 15 g; preserve source stage.",
    "rationale": "No attached amount evidence exists. The value matches the declared nominal litre; attach exact evidence without claiming measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Mineralsolution 1: Nitrilotriacetic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Stock recipe: 1000 mg with 1000 mL listed water; provider declares stock volume 1000 mL. Dose 50 mL per main batch.",
    "rationale": "The current direct concentration belongs to the mineral-stock stage. On the provider nominal litre stock basis, multiply stock g/L by 0.050 L for its listed main-batch mass. Magnesium contributes 0.050 g in addition to the direct 0.10 g, conditionally totaling 0.15 g; never add 0.10 and 1.0 as same-stage concentrations.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1000,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.23177,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Mineralsolution 1: CaSO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.6",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.6",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.6",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Stock recipe: 600 mg with 1000 mL listed water; provider declares stock volume 1000 mL. Dose 50 mL per main batch.",
    "rationale": "The current direct concentration belongs to the mineral-stock stage. On the provider nominal litre stock basis, multiply stock g/L by 0.050 L for its listed main-batch mass. Magnesium contributes 0.050 g in addition to the direct 0.10 g, conditionally totaling 0.15 g; never add 0.10 and 1.0 as same-stage concentrations.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CaSO4 x 2 H2O\",\n                        \"compound_id\": 190,\n                        \"amount\": 600,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.6,\n                        \"mmol_l\": 3.48489,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Mineralsolution 1: MgSO4 x 7 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Stock recipe: 1000 mg with 1000 mL listed water; provider declares stock volume 1000 mL. Dose 50 mL per main batch.",
    "rationale": "The current direct concentration belongs to the mineral-stock stage. On the provider nominal litre stock basis, multiply stock g/L by 0.050 L for its listed main-batch mass. Magnesium contributes 0.050 g in addition to the direct 0.10 g, conditionally totaling 0.15 g; never add 0.10 and 1.0 as same-stage concentrations.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 1000,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 4.05719,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Mineralsolution 1: NaCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.8",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.8",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.8",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Stock recipe: 800 mg with 1000 mL listed water; provider declares stock volume 1000 mL. Dose 50 mL per main batch.",
    "rationale": "The current direct concentration belongs to the mineral-stock stage. On the provider nominal litre stock basis, multiply stock g/L by 0.050 L for its listed main-batch mass. Magnesium contributes 0.050 g in addition to the direct 0.10 g, conditionally totaling 0.15 g; never add 0.10 and 1.0 as same-stage concentrations.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 800,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.8,\n                        \"mmol_l\": 13.6893,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Mineralsolution 1: KNO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.03",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.03",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.03",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Stock recipe: 1030 mg with 1000 mL listed water; provider declares stock volume 1000 mL. Dose 50 mL per main batch.",
    "rationale": "The current direct concentration belongs to the mineral-stock stage. On the provider nominal litre stock basis, multiply stock g/L by 0.050 L for its listed main-batch mass. Magnesium contributes 0.050 g in addition to the direct 0.10 g, conditionally totaling 0.15 g; never add 0.10 and 1.0 as same-stage concentrations.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\": 191,\n                        \"amount\": 1030,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1.03,\n                        \"mmol_l\": 10.1876,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Mineralsolution 1: NaNO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "6.89",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "6.89",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "6.89",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Stock recipe: 6890 mg with 1000 mL listed water; provider declares stock volume 1000 mL. Dose 50 mL per main batch.",
    "rationale": "The current direct concentration belongs to the mineral-stock stage. On the provider nominal litre stock basis, multiply stock g/L by 0.050 L for its listed main-batch mass. Magnesium contributes 0.050 g in addition to the direct 0.10 g, conditionally totaling 0.15 g; never add 0.10 and 1.0 as same-stage concentrations.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaNO3\",\n                        \"compound_id\": 187,\n                        \"amount\": 6890,\n                        \"unit\": \"mg\",\n                        \"g_l\": 6.89,\n                        \"mmol_l\": 81.0636,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "Mineralsolution 1: Na2HPO4",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "1.11",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "1.11",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "1.11",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Stock recipe: 1110 mg with 1000 mL listed water; provider declares stock volume 1000 mL. Dose 50 mL per main batch.",
    "rationale": "The current direct concentration belongs to the mineral-stock stage. On the provider nominal litre stock basis, multiply stock g/L by 0.050 L for its listed main-batch mass. Magnesium contributes 0.050 g in addition to the direct 0.10 g, conditionally totaling 0.15 g; never add 0.10 and 1.0 as same-stage concentrations.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2HPO4\",\n                        \"compound_id\": 233,\n                        \"amount\": 1110,\n                        \"unit\": \"mg\",\n                        \"g_l\": 1.11,\n                        \"mmol_l\": 7.81916,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "Traceelements Solution: MnSO4 x H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.22",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.22",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.22",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Stock recipe: 0.22 g; 1000 mL water; add 5 mL stock to the main batch.",
    "rationale": "The 1033 trace subsection is the dependency, not the 1033 basal medium. Provider milligram rows equal the primary gram rows. On its declared litre stock basis, multiply stock g/L by 0.005 L; do not retain undiluted stock concentrations as direct medium amounts.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[2].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.22,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.22,\n                        \"mmol_l\": 1.30165,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "Traceelements Solution: ZnSO4 x 7 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Stock recipe: 0.05 g; 1000 mL water; add 5 mL stock to the main batch.",
    "rationale": "The 1033 trace subsection is the dependency, not the 1033 basal medium. Provider milligram rows equal the primary gram rows. On its declared litre stock basis, multiply stock g/L by 0.005 L; do not retain undiluted stock concentrations as direct medium amounts.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[2].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.173876,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "Traceelements Solution: H3BO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Stock recipe: 0.05 g; 1000 mL water; add 5 mL stock to the main batch.",
    "rationale": "The 1033 trace subsection is the dependency, not the 1033 basal medium. Provider milligram rows equal the primary gram rows. On its declared litre stock basis, multiply stock g/L by 0.005 L; do not retain undiluted stock concentrations as direct medium amounts.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[2].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.808538,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "Traceelements Solution: CuSO4 x 5 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.0025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.0025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.0025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Stock recipe: 2.5 mg; 1000 mL water; add 5 mL stock to the main batch.",
    "rationale": "The 1033 trace subsection is the dependency, not the 1033 basal medium. Provider milligram rows equal the primary gram rows. On its declared litre stock basis, multiply stock g/L by 0.005 L; do not retain undiluted stock concentrations as direct medium amounts.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[2].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 2.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0025,\n                        \"mmol_l\": 0.0100126,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Traceelements Solution: Na2MoO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.0025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.0025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.0025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Stock recipe: 2.5 mg; 1000 mL water; add 5 mL stock to the main batch.",
    "rationale": "The 1033 trace subsection is the dependency, not the 1033 basal medium. Provider milligram rows equal the primary gram rows. On its declared litre stock basis, multiply stock g/L by 0.005 L; do not retain undiluted stock concentrations as direct medium amounts.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[2].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 2.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0025,\n                        \"mmol_l\": 0.0103327,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "Traceelements Solution: CoCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.0046",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.0046",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.0046",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Stock recipe: 4.6 mg; 1000 mL water; add 5 mL stock to the main batch.",
    "rationale": "The 1033 trace subsection is the dependency, not the 1033 basal medium. Provider milligram rows equal the primary gram rows. On its declared litre stock basis, multiply stock g/L by 0.005 L; do not retain undiluted stock concentrations as direct medium amounts.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[2].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 4.6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0046,\n                        \"mmol_l\": 0.0354285,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "Mineralsolution 1 dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "50 mL of the named stock in the main batch.",
    "rationale": "All current layers omit stock-addition descriptors. Retain the explicit receiving dose and source recipe separately.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Mineralsolution 1\",\n                        \"solution_id\": 2465,\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "Traceelements Solution dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "solutions[1].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "5 mL of the named stock in the main batch.",
    "rationale": "All current layers omit stock-addition descriptors. Retain the explicit receiving dose and source recipe separately.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Traceelements Solution\",\n                        \"solution_id\": 2099,\n                        \"amount\": 5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q24",
    "component_or_context": "Tris solution receiving dose",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "12.114",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "12.114",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "12.114",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "100 mL of Tris buffer",
    "rationale": "The current 12.114 g/L is consistent with the provider derived value (0.1 mol × 121.14 g/mol), but omits the explicit 100 mL, 1 M, pH 8.0 solution specification. Recover that source representation; no preparation of a substitute buffer is inferred.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Tris buffer\",\n                        \"compound_id\": 1101,\n                        \"attribute\": \"1 M pH 8.0\",\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"g_l\": 12.114,\n                        \"mmol_l\": 100,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q25",
    "component_or_context": "Tris stock molarity",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "12.114",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "12.114",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "12.114",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "1 M Tris buffer",
    "rationale": "The current 12.114 g/L is consistent with the provider derived value (0.1 mol × 121.14 g/mol), but omits the explicit 100 mL, 1 M, pH 8.0 solution specification. Recover that source representation; no preparation of a substitute buffer is inferred.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Tris buffer\",\n                        \"compound_id\": 1101,\n                        \"attribute\": \"1 M pH 8.0\",\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"g_l\": 12.114,\n                        \"mmol_l\": 100,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q26",
    "component_or_context": "Tris stock pH",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "12.114",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "12.114",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "12.114",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Tris buffer pH 8.0",
    "rationale": "The current 12.114 g/L is consistent with the provider derived value (0.1 mol × 121.14 g/mol), but omits the explicit 100 mL, 1 M, pH 8.0 solution specification. Recover that source representation; no preparation of a substitute buffer is inferred.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Tris buffer\",\n                        \"compound_id\": 1101,\n                        \"attribute\": \"1 M pH 8.0\",\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"g_l\": 12.114,\n                        \"mmol_l\": 100,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q27",
    "component_or_context": "Main water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "845 mL water in its named stage.",
    "rationale": "This water quantity is absent from every current layer. Main liquid inputs sum to 845+50+5+100=1000 mL nominally; stock water plus solutes does not independently establish measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[0].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 845,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q28",
    "component_or_context": "Mineral stock water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "solutions[0].composition[7].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "solutions[0].composition[7].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "solutions[0].composition[7].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "1000 mL water in its named stage.",
    "rationale": "This water quantity is absent from every current layer. Main liquid inputs sum to 845+50+5+100=1000 mL nominally; stock water plus solutes does not independently establish measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q29",
    "component_or_context": "Trace stock water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "solutions[1].composition[6].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "solutions[1].composition[6].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "solutions[1].composition[6].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "1000 mL water in its named stage.",
    "rationale": "This water quantity is absent from every current layer. Main liquid inputs sum to 845+50+5+100=1000 mL nominally; stock water plus solutes does not independently establish measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[2].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q30",
    "component_or_context": "Main pH range",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.8,
          "max": 8.2
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.8,
          "max": 8.2
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.8,
          "max": 8.2
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Preserve main pH 7.8–8.2, distinct from the Tris stock pH 8.0.",
    "rationale": "Existing ph_range matches the source/provider interpretation; attach evidence. DSMZ owner also preserves the preparation instruction.",
    "source_snippets": [
      {
        "source_key": "dsmz1242",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1242.pdf",
        "source_locator": "Page 1, main preparation",
        "exact_source_quote": "Adjust pH 8 + 0.2",
        "snapshot_sha256": "ff57b846652d92e2c97a7e6f08a406aee9b5a3877e4382aba3c0ea0c7e136e8e",
        "parsed_text_sha256": "aa160f4038e9f3fb17c3a89357aec8e37882354b36dc5f8792e46a345e706c7d"
      },
      {
        "source_key": "mediadive1242api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1242",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Adjust pH 7.8-8.2",
        "snapshot_sha256": "86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3"
      }
    ]
  },
  {
    "quantity_id": "q31",
    "component_or_context": "Autoclave temperature 121°C",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Autoclave at 121°C for 15 minutes.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Autoclave temperature 121°C for the main recipe.",
    "rationale": "Absent from target and KOMODO owner; already preserved as prose in DSMZ owner. Preserve source scope and attach evidence, without importing the 1033 basal procedure.",
    "source_snippets": [
      {
        "source_key": "dsmz1242",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1242.pdf",
        "source_locator": "Page 1, main preparation",
        "exact_source_quote": "Autoclave at 121°C for 15 minutes.",
        "snapshot_sha256": "ff57b846652d92e2c97a7e6f08a406aee9b5a3877e4382aba3c0ea0c7e136e8e",
        "parsed_text_sha256": "aa160f4038e9f3fb17c3a89357aec8e37882354b36dc5f8792e46a345e706c7d"
      }
    ]
  },
  {
    "quantity_id": "q32",
    "component_or_context": "Autoclave duration 15 minutes",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Autoclave at 121°C for 15 minutes.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Autoclave duration 15 minutes for the main recipe.",
    "rationale": "Absent from target and KOMODO owner; already preserved as prose in DSMZ owner. Preserve source scope and attach evidence, without importing the 1033 basal procedure.",
    "source_snippets": [
      {
        "source_key": "dsmz1242",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1242.pdf",
        "source_locator": "Page 1, main preparation",
        "exact_source_quote": "Autoclave at 121°C for 15 minutes.",
        "snapshot_sha256": "ff57b846652d92e2c97a7e6f08a406aee9b5a3877e4382aba3c0ea0c7e136e8e",
        "parsed_text_sha256": "aa160f4038e9f3fb17c3a89357aec8e37882354b36dc5f8792e46a345e706c7d"
      }
    ]
  }
]

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:003999.

18 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 18/21 primary and 16/21 secondary instances; all asserted current CHEBI-based secondary keys have exact pinned MIM rows. The separate legacy MediaIngredientMech:000170 and :000171 historical correspondences remain unresolved; current catalog absence is a completed lookup, not an unavailable fetch. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 21: primary 85.71%; secondary 76.19%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Historical nitrate secondary identifiers

grounding: concern. Targets: CultureMech:003999.

The exact legacy IDs occur on potassium and sodium nitrate in all three layers. Full pinned catalog/tree lookup completed with no matching historical objects; the current chemical mappings do not recover a historical legacy crosswalk. Do not infer a replacement from label similarity.

### Source accession, record identity and maintained ownership

identity: supported. Targets: CultureMech:003999.

CM003999 is generated from the exact KOMODO 1242 owner and DSMZ CM000701 owner. Their linked paths and stable IDs resolve; their matching flattened signatures establish local duplicate correspondence, not correctness of the formulation.

### Claim-level source support and historical evidence placement

evidence: concern. Targets: CultureMech:003999.

Collection/provider source access and ingredient-level evidence are distinct. Existing import URLs and history do not attach exact amount evidence; the inventory records literal source snippets and stage-specific follow-up. No source access failure is treated as a scientific contradiction.

### Source-scoped preparation and missing conditions

completeness: concern. Targets: CultureMech:003999.

DSMZ owner retains the main pH range and 121°C/15 minute cycle; target and KOMODO owner omit the cycle. Restore complete stock scope and the Tris specification. Only the explicitly referenced trace subsection of DSMZ 1033 is applicable.

### Composition, physical state and organism claims

scope: supported. Targets: CultureMech:003999.

The medium contains yeast extract, proteose peptone, casamino acids and agar; COMPLEX/UNDEFINED and SOLID_AGAR are consistent with the listed formulation. KOMODO Aerobic: No remains provider metadata, not an independently evidenced phenotype or an instruction to add anaerobic conditions.

### Supplied chemical forms and specificity

grounding: concern. Targets: CultureMech:003999.

Explicit hydrate forms match their asserted chemical parents at the named resolution. Generic Glucose does not independently establish a specific supplier or stereochemical product; CHEBI:17234 is retained as the existing general glucose mapping without inventing a source grade. The Tris compound identity does not encode its solution pH or strength.

### Growth assertions, taxonomic scope and graph applicability

scope: not_applicable. Targets: CultureMech:003999.

The record provides no claim-level experimental growth evidence or target-organism assertions. Medium titles, source species names, provider categories and application notes are contextual, not strain-level growth or current taxonomy evidence. No unrelated organism, culture condition or graph membership is imported.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:003999.

35 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Maintained-input changes and current transformation context

provenance: concern. Targets: CultureMech:003999.

Both maintained owners require source-stage recovery before regeneration. The recorded historical duplicate-summing event explains a provenance claim, not scientific validity. Current duplicate cleanup and source resolver code were read and cannot establish that the present implementation created the historic 1.1 value.

## Findings

### f1: Stock concentrations are presented as direct medium concentrations

blocker / open / confirmed; issue key: flattened-stock-stages.

All three layers lose mineral/trace dosing and water stages. Magnesium sulfate is stored at 1.1 g/L after combining 0.10 g direct with the mineral-stock 1 g/L. The source requires 50 mL mineral stock and 5 mL trace stock; on the declared nominal stock litre, magnesium contributes 0.05 g from stock, conditionally totaling 0.15 g per main batch. Tris is stored only as 12.114 g/L, losing 100 mL of 1 M buffer at pH 8.0. The record cannot be interpreted faithfully as a single direct formulation.

### f2: The generated and KOMODO layers omit the supported main preparation cycle

major / open / confirmed; issue key: lost-preparation-cycle.

The DSMZ owner retains the pH instruction and 121°C for 15 minutes. Target and KOMODO owner retain ph_range but omit preparation_steps; the source correspondence claim does not justify dropping supported preparation.

### f3: Historical nitrate MIM links remain unresolved

minor / open / confirmed; issue key: legacy-nitrate-mim.

The legacy identifiers MediaIngredientMech:000170 and :000171 on nitrate rows lack a verified historical crosswalk. Complete pinned current catalog/tree lookups do not contain those IDs; current CHEBI-linked rows do not authenticate legacy objects. This is a correspondence gap, not proof of wrong nitrate chemistry.

### f4: Historical timestamps need an appended clarification

minor / open / confirmed; issue key: history-timestamp-shape.

The complete history audit records malformed or timezone-naive historical timestamp instances. These events must remain auditable; a later clarification must not silently rewrite prior import or repair claims.

## Recommended Actions And Acceptance Checks

### a1

Restore main, mineral-stock and trace-stock scopes in both maintained owners; preserve every source unit, water amount and receiving dose, plus the full Tris solution specification. Keep any dilution arithmetic explicitly conditional on declared stock and receiving-volume bases. Regenerate the target after authorized owner correction.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the source-supported main preparation and its evidence through owner reconciliation and regeneration. Do not import the unrelated basal preparation of medium 1033.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve exact historical legacy records/crosswalks before replacing or affirming these secondary links; record unresolved scope explicitly meanwhile and preserve current chemical IDs absent contrary evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Append a dated, timezone-aware clarification identifying the affected historical events and source scope; preserve original events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch020/199/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch020/199/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml:1:id: CultureMech:003999<br>./data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml:1:id: CultureMech:003999<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch020/source-preflight-bound/199/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 27 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1242.pdf; Page 1: main formulation, preparation and Mineralsolution 1 | supports | DSMZ 1242 explicitly separates the basal recipe, 50 mL mineral stock, 5 mL referenced trace stock, 100 mL Tris solution and 845 mL water. |
| trace-primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1033.pdf; Page 1: Traceelements Solution subsection only | supports | The 1242 cross-reference imports only the six-solute trace stock and its water quantity. The 1033 basal formulation, iron addition, NTA adjustment and culture context are outside this recipe. |
| provider | https://mediadive.dsmz.de/rest/medium/1242; data.medium; solutions 2464, 2465 and 2099 | supports | The provider retains three stages, each declared 1000 mL, and the Tris attribute 1 M pH 8.0. Its derived 12.114 g/L value does not replace the solution specification. |
| mineral-endpoint | https://mediadive.dsmz.de/rest/solution/2465; Exact solution endpoint; recipe and declared volume | supports | The separately captured stock endpoint agrees with the scoped stock recipe in the medium response. |
| trace-endpoint | https://mediadive.dsmz.de/rest/solution/2099; Exact solution endpoint; recipe and declared volume | supports | The separately captured stock endpoint agrees with the scoped stock recipe in the medium response. |
| komodo-list | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact table row for KOMODO 1242 and its DSMZ accession | supports | The accessible catalog supports the accession cross-reference only, not detailed formulation or growth. |
| komodo1242detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1242; Preserved exact public retrieval result | context_only | The exact KOMODO 1242 detail request returned HTTP 403. The live DSMZ primary and MediaDive recipe are usable, but the historical contributing KOMODO formulation cannot be independently confirmed from its inaccessible detail page. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch020/199/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17234 resolves to glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32583 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32583; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32583 resolves to calcium sulfate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32816 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32816; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32816 resolves to pyruvic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63005 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63005; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63005 resolves to sodium nitrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63043 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63043 resolves to potassium nitrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi9754 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9754; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:9754 resolves to tris. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32583": [{"label": "CaSO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32583", "preferred_term": "CaSO4 x 2 H2O", "ontology_id": "CHEBI:32583", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32816": [{"label": "Pyruvic acid", "match_type": "preferred_term", "identifier": "CHEBI:32816", "preferred_term": "Pyruvic acid", "ontology_id": "CHEBI:32816", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34683": [{"label": "Na2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:9754": [{"label": "Tris base", "match_type": "preferred_term", "identifier": "CHEBI:9754", "preferred_term": "Tris base", "ontology_id": "CHEBI:9754", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| mimPinnedCatalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Complete pinned catalog/tree, exact legacy-ID lookup | supports | Both asserted legacy IDs are absent from the captured complete current snapshot. This completed lookup does not establish their historical meanings or invalidate the chemical CHEBI identifiers. |
| mimPinnedTree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Complete pinned catalog/tree, exact legacy-ID lookup | supports | Both asserted legacy IDs are absent from the captured complete current snapshot. This completed lookup does not establish their historical meanings or invalidate the chemical CHEBI identifiers. |
| history-metadata | data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml; data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:16.605523"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml", "events": 11, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:16.605523"}]}, {"input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml", "events": 11, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Both maintained owners require source-stage recovery before regeneration. The recorded historical duplicate-summing event explains a provenance claim, not scientific validity. Current duplicate cleanup and source resolver code were read and cannot establish that the present implementation created the historic 1.1 value. |
| writer-1 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Both maintained owners require source-stage recovery before regeneration. The recorded historical duplicate-summing event explains a provenance claim, not scientific validity. Current duplicate cleanup and source resolver code were read and cannot establish that the present implementation created the historic 1.1 value. |
| writer-2 | src/culturemech/enrich/dsmz_resolver.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Both maintained owners require source-stage recovery before regeneration. The recorded historical duplicate-summing event explains a provenance claim, not scientific validity. Current duplicate cleanup and source resolver code were read and cannot establish that the present implementation created the historic 1.1 value. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Both maintained owners require source-stage recovery before regeneration. The recorded historical duplicate-summing event explains a provenance claim, not scientific validity. Current duplicate cleanup and source resolver code were read and cannot establish that the present implementation created the historic 1.1 value. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact KOMODO 1242 detail request returned HTTP 403. The live DSMZ primary and MediaDive recipe are usable, but the historical contributing KOMODO formulation cannot be independently confirmed from its inaccessible detail page.
- Fresh native inspection source.inputs and the bound per-record source catalog are authoritative. Original preflight contexts remain provisional historical captures; the current schema/project.justfile hashes differ from that old base. No historical importer execution is inferred from current code alone.
- Partial completion rests on unavailable required historical MIM correspondence. Exact KOMODO detail is an optional unavailable source: DSMZ 1242 and its explicitly referenced DSMZ 1033 trace subsection, MediaDive and the exact catalog row support review of the current formulation. Current snapshot absence is a completed lookup, not a failed access check.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T122011Z-culturemech-003999-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: algoriphagus_alkaliphilus_medium (CultureMech:003999)'
started_at: '2026-10-21T12:11:57Z'
finished_at: '2026-10-21T12:20:11Z'
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
summary: The two maintained owners and generated target flatten mineral and trace
  stocks into direct concentrations, combine magnesium sulfate across incompatible
  stages, and lose the Tris solution specification. The DSMZ source supports a complete
  staged correction, but exact KOMODO detail and historical legacy MIM correspondence
  remain unresolved; the review is partial.
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
  - path: data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml
    sha256: bdcae9ef30f913c011e2013db182fb66d1d8b1f325edfc19382bdcee45309c9d
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml
    sha256: edfb0c2459e7fd5533f30b151de66c4f56bf2dac195b6b694fda3e5c3521652c
    role: context
  - path: data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml
    sha256: f0fb4f91d50d83825cc2def73f3ff8d1e5a1ad4bbb8fc82783c6992b8d28ada2
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
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
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
  selection: Task review 199; batch 020 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding nineteen task batches
    contain 190 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 193 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003999
targets:
- target_id: CultureMech:003999
  path: data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml
  label: algoriphagus_alkaliphilus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch020/199/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch020/199/strict.tsv"
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003999
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
  - CultureMech:003999
- check_id: komodo1242detail-source-access
  name: 'Exact source content access: komodo1242detail'
  required: false
  status: unavailable
  summary: The exact KOMODO 1242 detail request returned HTTP 403. The live DSMZ primary
    and MediaDive recipe are usable, but the historical contributing KOMODO formulation
    cannot be independently confirmed from its inaccessible detail page.
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - komodo1242detail-attempt
- check_id: historical-mim-correspondence
  name: Exact historical MIM 000170/000171 correspondence
  required: true
  status: unavailable
  summary: Complete current pinned catalog/tree searches finished successfully, but
    the required historical legacy objects or an exact crosswalk are unavailable.
    Current CHEBI-based mappings cannot authenticate those historical identifiers.
    This is not a current-source access failure.
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - mimPinnedCatalog
  - mimPinnedTree
  - mim
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T12:20:10Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T12:20:10Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T12:20:10Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:13:20.304418Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch020/199/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T12:13:22.225378Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch020/199/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:13:25.142204Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:13:26.891283Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T12:20:10Z'
  support: supports
  summary: './data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml:1:id: CultureMech:003999

    ./data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml:1:id:
    CultureMech:003999

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch020/source-preflight-bound/199/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T12:20:10Z'
  support: supports
  summary: 27 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 1808425955fad0fab1329563ffbc92264ebaf1d2cd5cf0b7dea59d3154e6d292
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1242.pdf
  locator: 'Page 1: main formulation, preparation and Mineralsolution 1'
  accessed_at: '2026-10-21T11:58:00.739669Z'
  support: supports
  summary: DSMZ 1242 explicitly separates the basal recipe, 50 mL mineral stock, 5
    mL referenced trace stock, 100 mL Tris solution and 845 mL water.
  snapshot_sha256: ff57b846652d92e2c97a7e6f08a406aee9b5a3877e4382aba3c0ea0c7e136e8e
- evidence_id: trace-primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1033.pdf
  locator: 'Page 1: Traceelements Solution subsection only'
  accessed_at: '2026-10-21T11:58:26.671305Z'
  support: supports
  summary: The 1242 cross-reference imports only the six-solute trace stock and its
    water quantity. The 1033 basal formulation, iron addition, NTA adjustment and
    culture context are outside this recipe.
  snapshot_sha256: 4411256ce7ac5dbc5182da120fec026f70a1e858612e14134f00b353f5a15644
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1242
  locator: data.medium; solutions 2464, 2465 and 2099
  accessed_at: '2026-10-21T11:57:59.678278Z'
  support: supports
  summary: The provider retains three stages, each declared 1000 mL, and the Tris
    attribute 1 M pH 8.0. Its derived 12.114 g/L value does not replace the solution
    specification.
  snapshot_sha256: 86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3
- evidence_id: mineral-endpoint
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/2465
  locator: Exact solution endpoint; recipe and declared volume
  accessed_at: '2026-10-21T11:58:26.027286Z'
  support: supports
  summary: The separately captured stock endpoint agrees with the scoped stock recipe
    in the medium response.
  snapshot_sha256: 15b91c6e80f5b8cdc767f492809d3b7d32caa0a17795d790d819a62075777433
- evidence_id: trace-endpoint
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/2099
  locator: Exact solution endpoint; recipe and declared volume
  accessed_at: '2026-10-21T11:58:26.026992Z'
  support: supports
  summary: The separately captured stock endpoint agrees with the scoped stock recipe
    in the medium response.
  snapshot_sha256: ed0f1c54c1f6bb0f9a1bcc57752ad8890db19d33bccb2021c8915cdc1e71aaa7
- evidence_id: komodo-list
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact table row for KOMODO 1242 and its DSMZ accession
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The accessible catalog supports the accession cross-reference only, not
    detailed formulation or growth.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodo1242detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1242
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T11:57:59.143576Z'
  support: context_only
  summary: The exact KOMODO 1242 detail request returned HTTP 403. The live DSMZ primary
    and MediaDive recipe are usable, but the historical contributing KOMODO formulation
    cannot be independently confirmed from its inaccessible detail page.
  snapshot_sha256: bbeb5debf51f1b54fb91839f3f6a8350898f64f498d1cdd451b85c23a44aed90
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch020/199/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T12:20:10Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: b1ca3e43aebe9025fb37ba5be975e39e64e4605752b5a52425be4498df112220
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
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
- evidence_id: chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:28.489501Z'
  support: supports
  summary: CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
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
- evidence_id: chebi32583
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32583
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:31:16.887678Z'
  support: supports
  summary: CHEBI:32583 resolves to calcium sulfate dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: e0851fb219d91e71915c9d74b56d917e393753c4cdb94ade75821d447f4aec3c
- evidence_id: chebi32816
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32816
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:58:02.312651Z'
  support: supports
  summary: CHEBI:32816 resolves to pyruvic acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: c7dd6f7736ec2a7cc2a10d73857262299df502ae91892cb5debe2f9c69c1fe1e
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
- evidence_id: chebi34683
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:46.851695Z'
  support: supports
  summary: CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: chebi44557
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:46:15.250117Z'
  support: supports
  summary: CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi63005
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63005
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T04:02:36.443517Z'
  support: supports
  summary: CHEBI:63005 resolves to sodium nitrate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 1ec6a815a0e22ba0d12f84ad998bef39b9e6b80cf90c25cd1ab51903bbb54da3
- evidence_id: chebi63043
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:40.679699Z'
  support: supports
  summary: CHEBI:63043 resolves to potassium nitrate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: c324450e6330a169c708c32a7908b6df0276f4dc76da413e473b563928f61c13
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
- evidence_id: chebi86364
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:35.036768Z'
  support: supports
  summary: CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069
- evidence_id: chebi9754
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9754
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:13.713319Z'
  support: supports
  summary: CHEBI:9754 resolves to tris. Identifier existence and label metadata do
    not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b9f921dfa34f343d4ef51ee217fc47702a8f03e2b9a8353effa10de89e9c6659
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T12:20:10Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label":
    "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term":
    "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label":
    "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term":
    "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32583": [{"label": "CaSO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:32583", "preferred_term": "CaSO4 x 2 H2O", "ontology_id":
    "CHEBI:32583", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32816":
    [{"label": "Pyruvic acid", "match_type": "preferred_term", "identifier": "CHEBI:32816",
    "preferred_term": "Pyruvic acid", "ontology_id": "CHEBI:32816", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type":
    "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34683":
    [{"label": "Na2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:34683",
    "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic
    acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type":
    "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride
    hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364":
    [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364",
    "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:9754": [{"label": "Tris base", "match_type":
    "preferred_term", "identifier": "CHEBI:9754", "preferred_term": "Tris base", "ontology_id":
    "CHEBI:9754", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mimPinnedCatalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Complete pinned catalog/tree, exact legacy-ID lookup
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: supports
  summary: Both asserted legacy IDs are absent from the captured complete current
    snapshot. This completed lookup does not establish their historical meanings or
    invalidate the chemical CHEBI identifiers.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: mimPinnedTree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Complete pinned catalog/tree, exact legacy-ID lookup
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: supports
  summary: Both asserted legacy IDs are absent from the captured complete current
    snapshot. This completed lookup does not establish their historical meanings or
    invalidate the chemical CHEBI identifiers.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml;
    data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T12:20:10Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:16.605523"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml",
    "events": 11, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:16.605523"}]}, {"input": "data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml",
    "events": 11, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:20:10Z'
  support: context_only
  summary: Both maintained owners require source-stage recovery before regeneration.
    The recorded historical duplicate-summing event explains a provenance claim, not
    scientific validity. Current duplicate cleanup and source resolver code were read
    and cannot establish that the present implementation created the historic 1.1
    value.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:20:10Z'
  support: context_only
  summary: Both maintained owners require source-stage recovery before regeneration.
    The recorded historical duplicate-summing event explains a provenance claim, not
    scientific validity. Current duplicate cleanup and source resolver code were read
    and cannot establish that the present implementation created the historic 1.1
    value.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:20:10Z'
  support: context_only
  summary: Both maintained owners require source-stage recovery before regeneration.
    The recorded historical duplicate-summing event explains a provenance claim, not
    scientific validity. Current duplicate cleanup and source resolver code were read
    and cannot establish that the present implementation created the historic 1.1
    value.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:20:10Z'
  support: context_only
  summary: Both maintained owners require source-stage recovery before regeneration.
    The recorded historical duplicate-summing event explains a provenance claim, not
    scientific validity. Current duplicate cleanup and source resolver code were read
    and cannot establish that the present implementation created the historic 1.1
    value.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 32 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Main: Yeast extract\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Main batch: 1 g; preserve source stage.\",\n    \"rationale\": \"No attached\
    \ amount evidence exists. The value matches the declared nominal litre; attach\
    \ exact evidence without claiming measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"Main: Proteose peptone no. 3\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Main batch: 1 g; preserve source stage.\",\n    \"rationale\": \"No attached\
    \ amount evidence exists. The value matches the declared nominal litre; attach\
    \ exact evidence without claiming measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Proteose peptone no. 3\\\",\\n                        \\\"compound_id\\\
    \": 316,\\n                        \\\"amount\\\": 1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n    \
    \                    \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"Main: Casamino acids\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Main batch: 1 g; preserve source stage.\",\n    \"rationale\": \"No attached\
    \ amount evidence exists. The value matches the declared nominal litre; attach\
    \ exact evidence without claiming measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Casamino acids\\\",\\n                        \\\"compound_id\\\
    \": 101,\\n                        \\\"amount\\\": 1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n    \
    \                    \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"Main: Glucose\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Main batch: 1 g; preserve source stage.\",\n    \"rationale\": \"No attached\
    \ amount evidence exists. The value matches the declared nominal litre; attach\
    \ exact evidence without claiming measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Glucose\\\",\\n                        \\\"compound_id\\\":\
    \ 5,\\n                        \\\"amount\\\": 1,\\n                        \\\
    \"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n          \
    \              \\\"mmol_l\\\": 5.55062,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"Main: Pyruvic acid\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Main batch: 0.05 g; preserve source stage.\",\n    \"rationale\": \"No attached\
    \ amount evidence exists. The value matches the declared nominal litre; attach\
    \ exact evidence without claiming measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Pyruvic acid\\\",\\n                        \\\"compound_id\\\
    \": 540,\\n                        \\\"amount\\\": 0.05,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\\
    n                        \\\"mmol_l\\\": 0.567795,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"Main: MgSO4 x 7 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Main batch: 0.1 g; preserve source stage.\",\n    \"rationale\": \"No attached\
    \ amount evidence exists. Restore direct magnesium sulfate 0.10 g separately from\
    \ the mineral-stock magnesium; 1.1 g/L is not supported.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.405719,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"Main: K2HPO4\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Main batch: 0.6 g; preserve source stage.\",\n    \"rationale\": \"No attached\
    \ amount evidence exists. The value matches the declared nominal litre; attach\
    \ exact evidence without claiming measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\": 10,\\\
    n                        \\\"amount\\\": 0.6,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.6,\\n                \
    \        \\\"mmol_l\\\": 3.44479,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Main: Agar\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Main batch: 15 g; preserve source stage.\",\n    \"rationale\": \"No attached\
    \ amount evidence exists. The value matches the declared nominal litre; attach\
    \ exact evidence without claiming measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\": 3,\\\
    n                        \\\"amount\\\": 15,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                 \
    \       \\\"mmol_l\\\": 44.5991,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"Mineralsolution 1: Nitrilotriacetic acid\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Stock recipe: 1000 mg with 1000 mL listed water; provider declares stock volume\
    \ 1000 mL. Dose 50 mL per main batch.\",\n    \"rationale\": \"The current direct\
    \ concentration belongs to the mineral-stock stage. On the provider nominal litre\
    \ stock basis, multiply stock g/L by 0.050 L for its listed main-batch mass. Magnesium\
    \ contributes 0.050 g in addition to the direct 0.10 g, conditionally totaling\
    \ 0.15 g; never add 0.10 and 1.0 as same-stage concentrations.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Nitrilotriacetic acid\\\",\\n                        \\\"compound_id\\\
    \": 189,\\n                        \\\"amount\\\": 1000,\\n                  \
    \      \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 1,\\n\
    \                        \\\"mmol_l\\\": 5.23177,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Mineralsolution 1: CaSO4 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Stock recipe: 600 mg with 1000 mL listed water; provider declares stock volume\
    \ 1000 mL. Dose 50 mL per main batch.\",\n    \"rationale\": \"The current direct\
    \ concentration belongs to the mineral-stock stage. On the provider nominal litre\
    \ stock basis, multiply stock g/L by 0.050 L for its listed main-batch mass. Magnesium\
    \ contributes 0.050 g in addition to the direct 0.10 g, conditionally totaling\
    \ 0.15 g; never add 0.10 and 1.0 as same-stage concentrations.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"CaSO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 190,\\n                        \\\"amount\\\": 600,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.6,\\\
    n                        \\\"mmol_l\\\": 3.48489,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"Mineralsolution 1: MgSO4 x 7 H2O\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Stock recipe: 1000 mg with 1000 mL listed water; provider declares stock volume\
    \ 1000 mL. Dose 50 mL per main batch.\",\n    \"rationale\": \"The current direct\
    \ concentration belongs to the mineral-stock stage. On the provider nominal litre\
    \ stock basis, multiply stock g/L by 0.050 L for its listed main-batch mass. Magnesium\
    \ contributes 0.050 g in addition to the direct 0.10 g, conditionally totaling\
    \ 0.15 g; never add 0.10 and 1.0 as same-stage concentrations.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 1,\\n  \
    \                      \\\"mmol_l\\\": 4.05719,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"Mineralsolution 1: NaCl\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Stock recipe: 800 mg with 1000 mL listed water; provider declares stock volume\
    \ 1000 mL. Dose 50 mL per main batch.\",\n    \"rationale\": \"The current direct\
    \ concentration belongs to the mineral-stock stage. On the provider nominal litre\
    \ stock basis, multiply stock g/L by 0.050 L for its listed main-batch mass. Magnesium\
    \ contributes 0.050 g in addition to the direct 0.10 g, conditionally totaling\
    \ 0.15 g; never add 0.10 and 1.0 as same-stage concentrations.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 800,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.8,\\n               \
    \         \\\"mmol_l\\\": 13.6893,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"Mineralsolution 1: KNO3\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Stock recipe: 1030 mg with 1000 mL listed water; provider declares stock volume\
    \ 1000 mL. Dose 50 mL per main batch.\",\n    \"rationale\": \"The current direct\
    \ concentration belongs to the mineral-stock stage. On the provider nominal litre\
    \ stock basis, multiply stock g/L by 0.050 L for its listed main-batch mass. Magnesium\
    \ contributes 0.050 g in addition to the direct 0.10 g, conditionally totaling\
    \ 0.15 g; never add 0.10 and 1.0 as same-stage concentrations.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"KNO3\\\",\\n                        \\\"compound_id\\\": 191,\\\
    n                        \\\"amount\\\": 1030,\\n                        \\\"\
    unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 1.03,\\n        \
    \                \\\"mmol_l\\\": 10.1876,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"Mineralsolution 1: NaNO3\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.89\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.89\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.89\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Stock recipe: 6890 mg with 1000 mL listed water; provider declares stock volume\
    \ 1000 mL. Dose 50 mL per main batch.\",\n    \"rationale\": \"The current direct\
    \ concentration belongs to the mineral-stock stage. On the provider nominal litre\
    \ stock basis, multiply stock g/L by 0.050 L for its listed main-batch mass. Magnesium\
    \ contributes 0.050 g in addition to the direct 0.10 g, conditionally totaling\
    \ 0.15 g; never add 0.10 and 1.0 as same-stage concentrations.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"NaNO3\\\",\\n                        \\\"compound_id\\\": 187,\\\
    n                        \\\"amount\\\": 6890,\\n                        \\\"\
    unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 6.89,\\n        \
    \                \\\"mmol_l\\\": 81.0636,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"Mineralsolution 1: Na2HPO4\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.11\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.11\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.11\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Stock recipe: 1110 mg with 1000 mL listed water; provider declares stock volume\
    \ 1000 mL. Dose 50 mL per main batch.\",\n    \"rationale\": \"The current direct\
    \ concentration belongs to the mineral-stock stage. On the provider nominal litre\
    \ stock basis, multiply stock g/L by 0.050 L for its listed main-batch mass. Magnesium\
    \ contributes 0.050 g in addition to the direct 0.10 g, conditionally totaling\
    \ 0.15 g; never add 0.10 and 1.0 as same-stage concentrations.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Na2HPO4\\\",\\n                        \\\"compound_id\\\":\
    \ 233,\\n                        \\\"amount\\\": 1110,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 1.11,\\\
    n                        \\\"mmol_l\\\": 7.81916,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"Traceelements Solution: MnSO4 x H2O\",\n    \"decision\": \"correct\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.22\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.22\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.22\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Stock recipe: 0.22 g; 1000 mL water; add 5 mL stock to the main batch.\",\n\
    \    \"rationale\": \"The 1033 trace subsection is the dependency, not the 1033\
    \ basal medium. Provider milligram rows equal the primary gram rows. On its declared\
    \ litre stock basis, multiply stock g/L by 0.005 L; do not retain undiluted stock\
    \ concentrations as direct medium amounts.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 0.22,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.22,\\\
    n                        \\\"mmol_l\\\": 1.30165,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\"\
    : \"Traceelements Solution: ZnSO4 x 7 H2O\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Stock recipe: 0.05 g; 1000 mL water; add 5 mL stock to the main batch.\",\n\
    \    \"rationale\": \"The 1033 trace subsection is the dependency, not the 1033\
    \ basal medium. Provider milligram rows equal the primary gram rows. On its declared\
    \ litre stock basis, multiply stock g/L by 0.005 L; do not retain undiluted stock\
    \ concentrations as direct medium amounts.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 0.05,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\\
    n                        \\\"mmol_l\\\": 0.173876,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"Traceelements Solution: H3BO3\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Stock recipe: 0.05 g; 1000 mL water; add 5 mL stock to the main batch.\",\n\
    \    \"rationale\": \"The 1033 trace subsection is the dependency, not the 1033\
    \ basal medium. Provider milligram rows equal the primary gram rows. On its declared\
    \ litre stock basis, multiply stock g/L by 0.005 L; do not retain undiluted stock\
    \ concentrations as direct medium amounts.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\": 37,\\\
    n                        \\\"amount\\\": 0.05,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\n         \
    \               \\\"mmol_l\\\": 0.808538,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\"\
    : \"Traceelements Solution: CuSO4 x 5 H2O\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0025\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0025\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0025\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Stock recipe: 2.5 mg; 1000 mL water; add 5 mL stock to the main batch.\",\n\
    \    \"rationale\": \"The 1033 trace subsection is the dependency, not the 1033\
    \ basal medium. Provider milligram rows equal the primary gram rows. On its declared\
    \ litre stock basis, multiply stock g/L by 0.005 L; do not retain undiluted stock\
    \ concentrations as direct medium amounts.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"CuSO4 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 121,\\n                        \\\"amount\\\": 2.5,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0025,\\\
    n                        \\\"mmol_l\\\": 0.0100126,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"Traceelements Solution: Na2MoO4 x 2 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0025\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0025\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0025\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Stock recipe: 2.5 mg; 1000 mL water; add 5 mL stock to the main batch.\",\n\
    \    \"rationale\": \"The 1033 trace subsection is the dependency, not the 1033\
    \ basal medium. Provider milligram rows equal the primary gram rows. On its declared\
    \ litre stock basis, multiply stock g/L by 0.005 L; do not retain undiluted stock\
    \ concentrations as direct medium amounts.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 2.5,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0025,\\\
    n                        \\\"mmol_l\\\": 0.0103327,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"Traceelements Solution: CoCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0046\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0046\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0046\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Stock recipe: 4.6 mg; 1000 mL water; add 5 mL stock to the main batch.\",\n\
    \    \"rationale\": \"The 1033 trace subsection is the dependency, not the 1033\
    \ basal medium. Provider milligram rows equal the primary gram rows. On its declared\
    \ litre stock basis, multiply stock g/L by 0.005 L; do not retain undiluted stock\
    \ concentrations as direct medium amounts.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 4.6,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0046,\\\
    n                        \\\"mmol_l\\\": 0.0354285,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\"\
    : \"Mineralsolution 1 dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"solutions[0].concentration\",\n        \"stored\":\
    \ null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"50 mL of the named stock in the main batch.\",\n    \"rationale\": \"All current\
    \ layers omit stock-addition descriptors. Retain the explicit receiving dose and\
    \ source recipe separately.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"mediadive1242api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1242\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 8,\\\
    n                        \\\"solution\\\": \\\"Mineralsolution 1\\\",\\n     \
    \                   \\\"solution_id\\\": 2465,\\n                        \\\"\
    amount\\\": 50,\\n                        \\\"unit\\\": \\\"ml\\\",\\n       \
    \                 \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\"\
    : \"Traceelements Solution dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"solutions[1].concentration\",\n        \"stored\":\
    \ null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"5 mL of the named stock in the main batch.\",\n    \"rationale\": \"All current\
    \ layers omit stock-addition descriptors. Retain the explicit receiving dose and\
    \ source recipe separately.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"mediadive1242api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1242\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[8]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 9,\\\
    n                        \\\"solution\\\": \\\"Traceelements Solution\\\",\\n\
    \                        \\\"solution_id\\\": 2099,\\n                       \
    \ \\\"amount\\\": 5,\\n                        \\\"unit\\\": \\\"ml\\\",\\n  \
    \                      \\\"optional\\\": 0\\n                    }\",\n      \
    \  \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\"\
    : \"Tris solution receiving dose\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.114\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.114\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.114\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"100 mL of Tris buffer\",\n    \"rationale\": \"The current 12.114 g/L is consistent\
    \ with the provider derived value (0.1 mol × 121.14 g/mol), but omits the explicit\
    \ 100 mL, 1 M, pH 8.0 solution specification. Recover that source representation;\
    \ no preparation of a substitute buffer is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Tris buffer\\\",\\n                        \\\"compound_id\\\
    \": 1101,\\n                        \\\"attribute\\\": \\\"1 M pH 8.0\\\",\\n\
    \                        \\\"amount\\\": 100,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 12.114,\\n            \
    \            \\\"mmol_l\\\": 100,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\"\
    : \"Tris stock molarity\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.114\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.114\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.114\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"1 M Tris buffer\",\n    \"rationale\": \"The current 12.114 g/L is consistent\
    \ with the provider derived value (0.1 mol × 121.14 g/mol), but omits the explicit\
    \ 100 mL, 1 M, pH 8.0 solution specification. Recover that source representation;\
    \ no preparation of a substitute buffer is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Tris buffer\\\",\\n                        \\\"compound_id\\\
    \": 1101,\\n                        \\\"attribute\\\": \\\"1 M pH 8.0\\\",\\n\
    \                        \\\"amount\\\": 100,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 12.114,\\n            \
    \            \\\"mmol_l\\\": 100,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\"\
    : \"Tris stock pH\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.114\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.114\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.114\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Tris buffer pH 8.0\",\n    \"rationale\": \"The current 12.114 g/L is consistent\
    \ with the provider derived value (0.1 mol × 121.14 g/mol), but omits the explicit\
    \ 100 mL, 1 M, pH 8.0 solution specification. Recover that source representation;\
    \ no preparation of a substitute buffer is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Tris buffer\\\",\\n                        \\\"compound_id\\\
    \": 1101,\\n                        \\\"attribute\\\": \\\"1 M pH 8.0\\\",\\n\
    \                        \\\"amount\\\": 100,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 12.114,\\n            \
    \            \\\"mmol_l\\\": 100,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\"\
    : \"Main water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"845 mL water in its named stage.\",\n    \"rationale\": \"This water quantity\
    \ is absent from every current layer. Main liquid inputs sum to 845+50+5+100=1000\
    \ mL nominally; stock water plus solutes does not independently establish measured\
    \ final volume.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1242api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1242\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[11]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 12,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 845,\\n                        \\\"unit\\\": \\\"ml\\\",\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\"\
    : \"Mineral stock water\",\n    \"decision\": \"add\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[7].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[7].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[7].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": \"1000 mL water in its named stage.\",\n\
    \    \"rationale\": \"This water quantity is absent from every current layer.\
    \ Main liquid inputs sum to 845+50+5+100=1000 mL nominally; stock water plus solutes\
    \ does not independently establish measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\"\
    : \"Trace stock water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[6].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[6].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[6].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": \"1000 mL water in its named stage.\",\n\
    \    \"rationale\": \"This water quantity is absent from every current layer.\
    \ Main liquid inputs sum to 845+50+5+100=1000 mL nominally; stock water plus solutes\
    \ does not independently establish measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\"\
    : \"Main pH range\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.8,\n          \"max\": 8.2\n        },\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.8,\n          \"max\": 8.2\n        },\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.8,\n          \"max\": 8.2\n        },\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"Preserve main pH\
    \ 7.8–8.2, distinct from the Tris stock pH 8.0.\",\n    \"rationale\": \"Existing\
    \ ph_range matches the source/provider interpretation; attach evidence. DSMZ owner\
    \ also preserves the preparation instruction.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1242\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1242.pdf\"\
    ,\n        \"source_locator\": \"Page 1, main preparation\",\n        \"exact_source_quote\"\
    : \"Adjust pH 8 + 0.2\",\n        \"snapshot_sha256\": \"ff57b846652d92e2c97a7e6f08a406aee9b5a3877e4382aba3c0ea0c7e136e8e\"\
    ,\n        \"parsed_text_sha256\": \"aa160f4038e9f3fb17c3a89357aec8e37882354b36dc5f8792e46a345e706c7d\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1242api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1242\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"Adjust\
    \ pH 7.8-8.2\",\n        \"snapshot_sha256\": \"86757bf91552965a23085b29a2d67025d9060e44187074da0d6614b26fcd37f3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\"\
    : \"Autoclave temperature 121°C\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Autoclave at 121°C for 15 minutes.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"Autoclave temperature\
    \ 121°C for the main recipe.\",\n    \"rationale\": \"Absent from target and KOMODO\
    \ owner; already preserved as prose in DSMZ owner. Preserve source scope and attach\
    \ evidence, without importing the 1033 basal procedure.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1242\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1242.pdf\",\n       \
    \ \"source_locator\": \"Page 1, main preparation\",\n        \"exact_source_quote\"\
    : \"Autoclave at 121°C for 15 minutes.\",\n        \"snapshot_sha256\": \"ff57b846652d92e2c97a7e6f08a406aee9b5a3877e4382aba3c0ea0c7e136e8e\"\
    ,\n        \"parsed_text_sha256\": \"aa160f4038e9f3fb17c3a89357aec8e37882354b36dc5f8792e46a345e706c7d\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q32\",\n    \"component_or_context\"\
    : \"Autoclave duration 15 minutes\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALGORIPHAGUS_ALKALIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Autoclave at 121°C for 15 minutes.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"Autoclave duration\
    \ 15 minutes for the main recipe.\",\n    \"rationale\": \"Absent from target\
    \ and KOMODO owner; already preserved as prose in DSMZ owner. Preserve source\
    \ scope and attach evidence, without importing the 1033 basal procedure.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1242\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1242.pdf\"\
    ,\n        \"source_locator\": \"Page 1, main preparation\",\n        \"exact_source_quote\"\
    : \"Autoclave at 121°C for 15 minutes.\",\n        \"snapshot_sha256\": \"ff57b846652d92e2c97a7e6f08a406aee9b5a3877e4382aba3c0ea0c7e136e8e\"\
    ,\n        \"parsed_text_sha256\": \"aa160f4038e9f3fb17c3a89357aec8e37882354b36dc5f8792e46a345e706c7d\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '18 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 18/21 primary and 16/21 secondary
    instances; all asserted current CHEBI-based secondary keys have exact pinned MIM
    rows. The separate legacy MediaIngredientMech:000170 and :000171 historical correspondences
    remain unresolved; current catalog absence is a completed lookup, not an unavailable
    fetch. Source forms are assessed separately.'
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi131527
  - chebi17234
  - chebi2509
  - chebi26710
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi32583
  - chebi32816
  - chebi33118
  - chebi34683
  - chebi44557
  - chebi53503
  - chebi63005
  - chebi63043
  - chebi75213
  - chebi86364
  - chebi9754
  details: 'Instance coverage on a 0–100 percent scale, denominator 21: primary 85.71%;
    secondary 76.19%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: legacy-correspondence
  area: grounding
  topic: Historical nitrate secondary identifiers
  outcome: concern
  summary: The exact legacy IDs occur on potassium and sodium nitrate in all three
    layers. Full pinned catalog/tree lookup completed with no matching historical
    objects; the current chemical mappings do not recover a historical legacy crosswalk.
    Do not infer a replacement from label similarity.
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - record
  - mimPinnedCatalog
  - mimPinnedTree
  - mim
- assessment_id: identity
  area: identity
  topic: Source accession, record identity and maintained ownership
  outcome: supported
  summary: CM003999 is generated from the exact KOMODO 1242 owner and DSMZ CM000701
    owner. Their linked paths and stable IDs resolve; their matching flattened signatures
    establish local duplicate correspondence, not correctness of the formulation.
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - record
  - id-search
  - owner-0
  - owner-1
  - primary
  - trace-primary
  - provider
  - komodo-list
- assessment_id: source-evidence
  area: evidence
  topic: Claim-level source support and historical evidence placement
  outcome: concern
  summary: Collection/provider source access and ingredient-level evidence are distinct.
    Existing import URLs and history do not attach exact amount evidence; the inventory
    records literal source snippets and stage-specific follow-up. No source access
    failure is treated as a scientific contradiction.
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - trace-primary
  - provider
  - komodo-list
- assessment_id: preparation
  area: completeness
  topic: Source-scoped preparation and missing conditions
  outcome: concern
  summary: DSMZ owner retains the main pH range and 121°C/15 minute cycle; target
    and KOMODO owner omit the cycle. Restore complete stock scope and the Tris specification.
    Only the explicitly referenced trace subsection of DSMZ 1033 is applicable.
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - trace-primary
  - provider
  - komodo-list
- assessment_id: classification
  area: scope
  topic: Composition, physical state and organism claims
  outcome: supported
  summary: 'The medium contains yeast extract, proteose peptone, casamino acids and
    agar; COMPLEX/UNDEFINED and SOLID_AGAR are consistent with the listed formulation.
    KOMODO Aerobic: No remains provider metadata, not an independently evidenced phenotype
    or an instruction to add anaerobic conditions.'
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - record
  - primary
  - trace-primary
  - provider
  - komodo-list
- assessment_id: forms
  area: grounding
  topic: Supplied chemical forms and specificity
  outcome: concern
  summary: Explicit hydrate forms match their asserted chemical parents at the named
    resolution. Generic Glucose does not independently establish a specific supplier
    or stereochemical product; CHEBI:17234 is retained as the existing general glucose
    mapping without inventing a source grade. The Tris compound identity does not
    encode its solution pH or strength.
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - record
  - primary
  - trace-primary
  - provider
  - komodo-list
- assessment_id: growth
  area: scope
  topic: Growth assertions, taxonomic scope and graph applicability
  outcome: not_applicable
  summary: The record provides no claim-level experimental growth evidence or target-organism
    assertions. Medium titles, source species names, provider categories and application
    notes are contextual, not strain-level growth or current taxonomy evidence. No
    unrelated organism, culture condition or graph membership is imported.
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - record
  - primary
  - trace-primary
  - provider
  - komodo-list
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 35 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: writer
  area: provenance
  topic: Maintained-input changes and current transformation context
  outcome: concern
  summary: Both maintained owners require source-stage recovery before regeneration.
    The recorded historical duplicate-summing event explains a provenance claim, not
    scientific validity. Current duplicate cleanup and source resolver code were read
    and cannot establish that the present implementation created the historic 1.1
    value.
  target_ids:
  - CultureMech:003999
  evidence_ids:
  - record
  - writer-0
  - writer-1
  - writer-2
  - writer-3
findings:
- finding_id: f1
  issue_key: flattened-stock-stages
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock concentrations are presented as direct medium concentrations
  description: All three layers lose mineral/trace dosing and water stages. Magnesium
    sulfate is stored at 1.1 g/L after combining 0.10 g direct with the mineral-stock
    1 g/L. The source requires 50 mL mineral stock and 5 mL trace stock; on the declared
    nominal stock litre, magnesium contributes 0.05 g from stock, conditionally totaling
    0.15 g per main batch. Tris is stored only as 12.114 g/L, losing 100 mL of 1 M
    buffer at pH 8.0. The record cannot be interpreted faithfully as a single direct
    formulation.
  target_ids:
  - CultureMech:003999
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - primary
  - trace-primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml
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
  issue_key: lost-preparation-cycle
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The generated and KOMODO layers omit the supported main preparation cycle
  description: The DSMZ owner retains the pH instruction and 121°C for 15 minutes.
    Target and KOMODO owner retain ph_range but omit preparation_steps; the source
    correspondence claim does not justify dropping supported preparation.
  target_ids:
  - CultureMech:003999
  field_paths:
  - preparation_steps
  - ph_range
  evidence_ids:
  - record
  - owner-1
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml
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
  issue_key: legacy-nitrate-mim
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Historical nitrate MIM links remain unresolved
  description: The legacy identifiers MediaIngredientMech:000170 and :000171 on nitrate
    rows lack a verified historical crosswalk. Complete pinned current catalog/tree
    lookups do not contain those IDs; current CHEBI-linked rows do not authenticate
    legacy objects. This is a correspondence gap, not proof of wrong nitrate chemistry.
  target_ids:
  - CultureMech:003999
  field_paths:
  - ingredients[12]
  - ingredients[13]
  evidence_ids:
  - record
  - mimPinnedCatalog
  - mimPinnedTree
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: history-timestamp-shape
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical timestamps need an appended clarification
  description: The complete history audit records malformed or timezone-naive historical
    timestamp instances. These events must remain auditable; a later clarification
    must not silently rewrite prior import or repair claims.
  target_ids:
  - CultureMech:003999
  field_paths:
  - curation_history
  evidence_ids:
  - record
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml
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
  description: Restore main, mineral-stock and trace-stock scopes in both maintained
    owners; preserve every source unit, water amount and receiving dose, plus the
    full Tris solution specification. Keep any dilution arithmetic explicitly conditional
    on declared stock and receiving-volume bases. Regenerate the target after authorized
    owner correction.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003999
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml
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
  description: Preserve the source-supported main preparation and its evidence through
    owner reconciliation and regeneration. Do not import the unrelated basal preparation
    of medium 1033.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003999
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml
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
  description: Resolve exact historical legacy records/crosswalks before replacing
    or affirming these secondary links; record unresolved scope explicitly meanwhile
    and preserve current chemical IDs absent contrary evidence.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003999
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml
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
  description: Append a dated, timezone-aware clarification identifying the affected
    historical events and source scope; preserve original events.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003999
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml
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
- The exact KOMODO 1242 detail request returned HTTP 403. The live DSMZ primary and
  MediaDive recipe are usable, but the historical contributing KOMODO formulation
  cannot be independently confirmed from its inaccessible detail page.
- Fresh native inspection source.inputs and the bound per-record source catalog are
  authoritative. Original preflight contexts remain provisional historical captures;
  the current schema/project.justfile hashes differ from that old base. No historical
  importer execution is inferred from current code alone.
- 'Partial completion rests on unavailable required historical MIM correspondence.
  Exact KOMODO detail is an optional unavailable source: DSMZ 1242 and its explicitly
  referenced DSMZ 1033 trace subsection, MediaDive and the exact catalog row support
  review of the current formulation. Current snapshot absence is a completed lookup,
  not a failed access check.'
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-020
- generated-medium
```
